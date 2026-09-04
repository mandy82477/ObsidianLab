# -*- coding: utf-8 -*-
"""lint 自身的健康與進化迴路（2026-09-04 使用者裁決「讓 lint 可以持續進化」）。

lint 原本是靜態考卷：進化只靠使用者不定期質疑 → 主編改題。本腳本提供四個
子命令，讓 lint 自己產生「我漏了什麼／我是不是壞了／我是不是太肥了」的訊號，
並各自有消費端（見 .claude/commands/wiki-lint.md 6h／6i 與步驟 8）：

  density   規則密度量測（6h 的量測端）：每檔行數、[加入:]/[改版:] 標記數、
            教訓敘事行數與佔比；超過門檻者列為蒸餾候選。規則債跟內容債一樣
            會壓垮閱讀者，而規則的閱讀者是每個 agent。
  mutate    檢查器的檢查（6i）：對 review-registry 每組 all_contain／min_count
            配對做突變測試——在記憶體裡把 pattern 的命中抹掉、重跑斷言，
            仍綠的就是「恆真的假看守」（2026-09-04 實例：`——` 全形破折號在
            散文出現 60 次，pattern 恆真）。不寫檔、不動工作樹。
  hits      lint 各步驟命中帳（record／report）：每輪 lint 收尾記各步命中數，
            report 印連續零命中的步驟——「連續滿分與抓不到問題是同一枚硬幣」
            原本只是一句話，這裡讓它變成數字。
  misses    lint 漏抓帳（add／list／stats）：使用者質疑揭露而 lint 沒抓到的缺陷，
            結構化記錄「哪一步本該抓到／為什麼沒抓到」。三個月後看分佈，
            投資哪一步才有依據——「歷史上所有重大問題全來自使用者質疑」
            在此之前只是印象，不是統計。

用法：
    python scripts/lint_health.py density [--threshold-lines 300 --threshold-marks 20 --threshold-lesson-pct 5]
    python scripts/lint_health.py mutate
    python scripts/lint_health.py hits record --date YYYY-MM-DD --step 5c=9 --step 6a=1 ...
    python scripts/lint_health.py hits report [--weeks 8]
    python scripts/lint_health.py misses add --date YYYY-MM-DD --issue "..." --should-catch "5c" \
        --why "考卷外|考卷內抽樣不足|檢查失效|無對應檢查" --fix "..."
    python scripts/lint_health.py misses list | stats

exit code：density／mutate／hits report 發現候選或失效時回 2（提醒，不擋 build）；
資料寫入失敗回 1。掃描失敗不得當成 0（同 open_loops.py 原則）。
"""
from __future__ import annotations

import argparse
import glob
import io
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
HITS_PATH = DATA_DIR / "lint_step_hits.jsonl"
MISSES_PATH = DATA_DIR / "lint_misses.jsonl"
REGISTRY_PATH = REPO_ROOT / ".claude" / "review-registry.json"

RULE_GLOBS = [".claude/rules/*.md", ".claude/commands/*.md", "CLAUDE.md", "wiki/CLAUDE.md"]
MARK_RE = re.compile(r"\[(?:加入|改版|裁決|使用者指示)")
LESSON_RE = re.compile(r"踩過|教訓|反例|實測|實例|曾犯|曾發生|發生過|首次發現|立法依據")

WHY_VALUES = ("考卷外", "考卷內抽樣不足", "檢查失效", "無對應檢查")
BROAD_HITS = 10  # 同檔命中達此數的 pattern 視為過寬（被散文滿足的假看守）


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


# ── density ──────────────────────────────────────────────────────────────────

def rule_files() -> list[Path]:
    out: list[Path] = []
    for g in RULE_GLOBS:
        out += [REPO_ROOT / p for p in glob.glob(g, root_dir=REPO_ROOT)]
    return sorted(set(out))


def density_rows(files: list[Path] | None = None) -> list[dict]:
    rows = []
    for f in files or rule_files():
        text = f.read_text(encoding="utf-8")
        lines = text.splitlines()
        n = len(lines)
        marks = len(MARK_RE.findall(text))
        lesson = sum(1 for l in lines if LESSON_RE.search(l))
        try:
            name = f.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            name = f.as_posix()
        rows.append({
            "file": name,
            "lines": n, "marks": marks, "lesson_lines": lesson,
            "lesson_pct": round(100.0 * lesson / n, 1) if n else 0.0,
        })
    rows.sort(key=lambda r: -r["lines"])
    return rows


def density_candidates(rows: list[dict], t_lines: int, t_marks: int, t_pct: float) -> list[dict]:
    return [r for r in rows if r["lines"] > t_lines or r["marks"] > t_marks or r["lesson_pct"] > t_pct]


def cmd_density(args, out) -> int:
    rows = density_rows()
    cands = density_candidates(rows, args.threshold_lines, args.threshold_marks, args.threshold_lesson_pct)
    out.write(f"# 規則密度（{len(rows)} 檔｜門檻：行 >{args.threshold_lines}、標記 >{args.threshold_marks}、教訓行 >{args.threshold_lesson_pct}%）\n")
    out.write(f"{'行數':>5} {'標記':>4} {'教訓':>4} {'教訓%':>5}  檔案\n")
    for r in rows[:15]:
        flag = "⚠️" if r in cands else "  "
        out.write(f"{r['lines']:>5} {r['marks']:>4} {r['lesson_lines']:>4} {r['lesson_pct']:>5}  {flag} {r['file']}\n")
    out.write(f"總計 {sum(r['lines'] for r in rows)} 行、{sum(r['marks'] for r in rows)} 標記、{sum(r['lesson_lines'] for r in rows)} 教訓行\n")
    if cands:
        out.write(f"\n⚠️ 蒸餾候選 {len(cands)} 檔（每次 lint 至多提案 2 檔，經使用者確認才動）：\n")
        for r in cands:
            out.write(f"  - {r['file']}：{r['lines']} 行／{r['marks']} 標記／教訓 {r['lesson_pct']}%\n")
        return 2
    out.write("\n✅ 無檔超過密度門檻\n")
    return 0


# ── mutate ───────────────────────────────────────────────────────────────────

def _mutate_text(text: str, pattern: str) -> str | None:
    """抹掉 pattern 的每一個命中（換成等長的 X），回傳突變後文字；無命中回 None。"""
    if not re.search(pattern, text):
        return None
    return re.sub(pattern, lambda m: "X" * max(1, len(m.group(0))), text)


def mutate_pairs(registry: dict | None = None) -> list[dict]:
    """對每組 all_contain／min_count 配對做突變：逐檔逐 pattern 抹掉命中後，
    該斷言若仍通過 → 這組是恆真的假看守。回傳失效清單。"""
    reg = registry or json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    weak: list[dict] = []
    for pair in reg.get("sync_pairs", []):
        assertion = pair.get("assertion")
        if assertion not in ("all_contain", "min_count"):
            continue
        if pair.get("_mutate_exempt"):
            continue  # 明示豁免：詞本身即契約、天然高頻（豁免理由必須寫在 _mutate_exempt 值裡）
        min_n = pair.get("min", 1)
        for f in pair["files"]:
            target = REPO_ROOT / f
            if not target.exists():
                continue
            original = target.read_text(encoding="utf-8")
            for pattern in pair["patterns"]:
                hits = len(re.findall(pattern, original))
                if hits >= BROAD_HITS:
                    weak.append({"pair": pair["name"], "file": f, "pattern": pattern,
                                 "reason": f"過寬：同檔命中 {hits} 次（≥{BROAD_HITS}），散文即可滿足——改壞契約字串它仍綠（2026-09-04 `——` 實例）"})
                    continue
                mutated = _mutate_text(original, pattern)
                if mutated is None:
                    continue  # 本來就不命中——check_rules 自己會紅，不是突變議題
                still_ok = (re.search(pattern, mutated) is not None) if assertion == "all_contain" \
                    else (len(re.findall(pattern, mutated)) >= min_n)
                if still_ok:
                    weak.append({"pair": pair["name"], "file": f, "pattern": pattern,
                                 "reason": "抹掉所有命中後斷言仍通過（pattern 可能被其他文字滿足，或 re.sub 未消除命中）"})
    return weak


def cmd_mutate(args, out) -> int:
    weak = mutate_pairs()
    reg = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    n = sum(1 for p in reg.get("sync_pairs", []) if p.get("assertion") in ("all_contain", "min_count"))
    out.write(f"# 檢查器突變測試：{n} 組 all_contain／min_count 配對\n")
    if weak:
        out.write(f"⚠️ {len(weak)} 處假看守（抹掉命中後仍綠）：\n")
        for w in weak:
            out.write(f"  - {w['pair'][:60]}\n      {w['file']} ← `{w['pattern']}`\n")
        return 2
    out.write("✅ 全部配對在突變後轉紅——看守有效\n")
    return 0


# ── hits ─────────────────────────────────────────────────────────────────────

def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def _append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def parse_step_args(items: list[str]) -> dict[str, int]:
    steps: dict[str, int] = {}
    for it in items:
        if "=" not in it:
            raise SystemExit(f"--step 格式須為 步驟=命中數，得到 {it!r}")
        k, v = it.split("=", 1)
        steps[k.strip()] = int(v)
    return steps


def cmd_hits_record(args, out) -> int:
    row = {"date": args.date, "rules_rev": args.rules_rev or "", "steps": parse_step_args(args.step)}
    _append_jsonl(HITS_PATH, row)
    out.write(f"已記錄 {args.date}：{len(row['steps'])} 步\n")
    return 0


def zero_streaks(rows: list[dict]) -> dict[str, int]:
    """每步驟自最近一筆往回連續零命中的輪數（該步從未出現者不計）。"""
    by_step: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for r in sorted(rows, key=lambda x: x["date"]):
        for k, v in r.get("steps", {}).items():
            by_step[k].append((r["date"], v))
    streaks = {}
    for k, seq in by_step.items():
        n = 0
        for _, v in reversed(seq):
            if v == 0:
                n += 1
            else:
                break
        streaks[k] = n
    return streaks


def cmd_hits_report(args, out) -> int:
    rows = _read_jsonl(HITS_PATH)
    if not rows:
        out.write("（尚無命中帳；每輪 lint 收尾以 `hits record` 記錄）\n")
        return 0
    streaks = zero_streaks(rows)
    out.write(f"# lint 步驟命中帳（{len(rows)} 輪，最新 {max(r['date'] for r in rows)}）\n")
    suspicious = {k: v for k, v in streaks.items() if v >= args.weeks}
    for k, v in sorted(streaks.items()):
        flag = "⚠️" if v >= args.weeks else "  "
        out.write(f"  {flag} {k}: 連續零命中 {v} 輪\n")
    if suspicious:
        out.write(f"\n⚠️ {len(suspicious)} 步連續 ≥{args.weeks} 輪零命中——疑似失效或可降頻，排入 6i 突變或 6h 汰除評估\n")
        return 2
    out.write("\n✅ 無步驟連續零命中達門檻\n")
    return 0


# ── misses ───────────────────────────────────────────────────────────────────

def cmd_misses_add(args, out) -> int:
    if args.why not in WHY_VALUES:
        raise SystemExit(f"--why 須為 {WHY_VALUES} 之一")
    row = {"date": args.date, "issue": args.issue, "should_catch": args.should_catch,
           "why": args.why, "fix": args.fix or "", "source": args.source or "user-query"}
    _append_jsonl(MISSES_PATH, row)
    out.write(f"已登記漏抓：{args.issue[:40]}…（本該由 {args.should_catch} 抓到，原因 {args.why}）\n")
    return 0


def cmd_misses_list(args, out) -> int:
    rows = _read_jsonl(MISSES_PATH)
    out.write(f"# lint 漏抓帳（{len(rows)} 筆）\n")
    for r in rows[-args.limit:]:
        out.write(f"- {r['date']}｜本該 {r['should_catch']}｜{r['why']}｜{r['issue'][:70]}\n")
    return 0


def cmd_misses_stats(args, out) -> int:
    rows = _read_jsonl(MISSES_PATH)
    if not rows:
        out.write("（尚無漏抓帳）\n")
        return 0
    by_why = Counter(r["why"] for r in rows)
    by_step = Counter(r["should_catch"] for r in rows)
    out.write(f"# lint 漏抓分佈（{len(rows)} 筆，{min(r['date'] for r in rows)}～{max(r['date'] for r in rows)}）\n")
    out.write("按原因：" + "、".join(f"{k} {v}" for k, v in by_why.most_common()) + "\n")
    out.write("按本該抓到的步驟：" + "、".join(f"{k} {v}" for k, v in by_step.most_common()) + "\n")
    top = by_step.most_common(1)[0]
    out.write(f"→ 最值得投資的步驟：{top[0]}（{top[1]} 次漏抓）\n")
    return 0


# ── main ─────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("density")
    d.add_argument("--threshold-lines", type=int, default=300)
    d.add_argument("--threshold-marks", type=int, default=20)
    d.add_argument("--threshold-lesson-pct", type=float, default=5.0)

    sub.add_parser("mutate")

    h = sub.add_parser("hits")
    hs = h.add_subparsers(dest="hcmd", required=True)
    hr = hs.add_parser("record")
    hr.add_argument("--date", required=True)
    hr.add_argument("--rules-rev", default="")
    hr.add_argument("--step", action="append", default=[], help="步驟=命中數，可重複")
    hp = hs.add_parser("report")
    hp.add_argument("--weeks", type=int, default=8)

    m = sub.add_parser("misses")
    ms = m.add_subparsers(dest="mcmd", required=True)
    ma = ms.add_parser("add")
    ma.add_argument("--date", required=True)
    ma.add_argument("--issue", required=True)
    ma.add_argument("--should-catch", required=True, help="本該抓到的 lint 步驟（如 5c／3e／無）")
    ma.add_argument("--why", required=True, help="|".join(WHY_VALUES))
    ma.add_argument("--fix", default="")
    ma.add_argument("--source", default="user-query")
    ml = ms.add_parser("list")
    ml.add_argument("--limit", type=int, default=30)
    ms.add_parser("stats")

    args = ap.parse_args(argv)
    out = _stdout()
    try:
        if args.cmd == "density":
            rc = cmd_density(args, out)
        elif args.cmd == "mutate":
            rc = cmd_mutate(args, out)
        elif args.cmd == "hits":
            rc = cmd_hits_record(args, out) if args.hcmd == "record" else cmd_hits_report(args, out)
        else:
            rc = {"add": cmd_misses_add, "list": cmd_misses_list, "stats": cmd_misses_stats}[args.mcmd](args, out)
    finally:
        out.flush()
    return rc


if __name__ == "__main__":
    sys.exit(main())
