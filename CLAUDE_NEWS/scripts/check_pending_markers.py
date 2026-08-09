#!/usr/bin/env python3
"""懸置標記語法檢查器 — 388 筆舊字樣回填為新語法時的每批驗收工具。

語法規格見 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節，解析邏輯全部
複用 `scripts/pending_markers.py`（`PENDING_RE`／`SHORT_RE`／`QDEF_RE`／
`iter_pending()`／`probe_too_weak()`／`wikilink_target()` 等），本檔不重新發明
parser，只做「這筆標記合不合規格」的判定。

用法：
    python scripts/check_pending_markers.py            # 全庫語法檢查
    python scripts/check_pending_markers.py --queue     # 逾期佇列（供 5c 用）

**尚未掛進 `scripts/run_tests.py`**——回填全庫 388 筆之前掛上去，測試會立刻紅
（目前新語法命中數為 0），所以先讓它獨立可跑，供每批回填後的手動驗收；掛載留待
回填完成後另一階段處理。

檢查項對照 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節：

  1. 語法完整性（FAIL）   標記日為合法 ISO 日期且 ≤ 今日；複查日（若有）晚於標記日；
                          探針至少 1 個非空
  2. 符號/類別詞一致（FAIL） ❓↔待查證、🔎↔查無官方，兩者是各自獨立的 regex 群組，
                          規格要求一一對應，`SYM_TO_KIND` 之外的組合視為語法錯誤
  3. 排版正規式（FAIL）   `**待查證（標` / `**查無官方（標`——括號誤寫在粗體內，
                          PENDING_RE 吃不到，得用獨立 regex 才抓得到
  4. 探針品質（FAIL）     每個探針過 `probe_too_weak()`（過寬詞／長度地板）
  5. wikilink 探針目標存在（FAIL） `wikilink_target()` 解出的頁面必須在 wiki/ 下實際存在
  6. ⟨Q-nn⟩ 雙向對帳（FAIL） 表格短標記 (SHORT_RE) 與細節區定義 (Marker.qid) 一一對應，
                          同頁 qid 不重複
  7. 探針數不足（WARN）   單探針、非 wikilink、長度 < 6
  8. 語意反轉殘留（WARN） 標記同行出現「解除／結案／轉為」+ ✅
  9. 逾期（WARN，明確不得 FAIL） 複查日（或標記日+14 天）≤ 今日——專案拒絕機械棘輪，
                          見 `scripts/gate_web_build.py` 的註解哲學：逾期是排程訊號，
                          不是語法錯誤，FAIL 會逼記者為了轉綠而亂改標記
  10. 存量殘餘（只印數字，不判定） `iter_legacy()` 掃到的舊字樣筆數，供回填進度追蹤

原計畫的檢查「命中未消費」依賴每日掃描器產生的 jsonl 對照當日日報，該掃描器尚未
上線，本檔跳過，留待掃描器上線後另補。
"""
from __future__ import annotations

import io
import re
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pending_markers import (  # noqa: E402
    Doc, WIKI_DIR, iter_legacy, iter_pending, probe_is_wikilink,
    probe_too_weak, wikilink_target, wiki_pages, SHORT_RE, SYM_TO_KIND,
)

REVIEW_DEFAULT_DAYS = 14
QUEUE_LIMIT = 10
SHORT_PROBE_LEN = 6

BAD_BRACKET_RE = re.compile(r"\*\*(?:待查證|查無官方)（標")
REVERSAL_CUES = ("解除", "結案", "轉為")


def _stdout():
    """Windows 主控台預設 cp950，直接 print 狀態符號會 UnicodeEncodeError（同 check_weekly_ledger.py）。"""
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def _parse_date(s: str) -> date | None:
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def _slug(path: Path, wiki_dir: Path) -> str:
    try:
        return path.relative_to(wiki_dir).as_posix()[:-3]
    except ValueError:
        return path.stem


def _wikilink_path(target: str, wiki_dir: Path) -> Path:
    return wiki_dir / f"{target}.md"


def _page_report(path: Path, text: str, wiki_dir: Path, today: date) -> tuple[list[str], list[str], int]:
    """回傳 (fail_lines, warn_lines, legacy_count) for a single page。"""
    fails: list[str] = []
    warns: list[str] = []
    slug = _slug(path, wiki_dir)
    doc = Doc(text, path)
    markers = iter_pending(text, path)

    # ── 3. 排版正規式（括號誤寫在粗體內，PENDING_RE 天生吃不到，獨立掃）───────
    for m in BAD_BRACKET_RE.finditer(text):
        if doc.in_code(m.start()) or doc.in_frontmatter(m.start()):
            continue
        fails.append(f"  ❌ {slug}:{doc.line_of(m.start())}：括號誤寫在粗體內（應為「…**（標」不是「**…（標」）")

    for mk in markers:
        loc = f"{slug}:{mk.line}"

        # ── 1. 語法完整性 ──
        marked_date = _parse_date(mk.marked)
        if marked_date is None:
            fails.append(f"  ❌ {loc}：標記日「{mk.marked}」不是合法 ISO 日期")
        elif marked_date > today:
            fails.append(f"  ❌ {loc}：標記日 {mk.marked} 晚於今日（未來日期）")

        if mk.review:
            review_date = _parse_date(mk.review)
            if review_date is None:
                fails.append(f"  ❌ {loc}：複查日「{mk.review}」不是合法 ISO 日期")
            elif marked_date is not None and review_date <= marked_date:
                fails.append(f"  ❌ {loc}：複查日 {mk.review} 未晚於標記日 {mk.marked}")

        probes = mk.probes
        if not probes:
            fails.append(f"  ❌ {loc}：探針為空")

        # ── 2. 符號/類別詞一致 ──
        if SYM_TO_KIND.get(mk.sym) != mk.kind:
            fails.append(f"  ❌ {loc}：符號「{mk.sym}」與類別詞「{mk.kind}」不一致（應為 {SYM_TO_KIND.get(mk.sym)}）")

        # ── 4. 探針品質 + 5. wikilink 探針目標存在 ──
        for probe in probes:
            reason = probe_too_weak(probe)
            if reason:
                fails.append(f"  ❌ {loc}：探針不合格——{reason}")
            target = wikilink_target(probe)
            if target and not _wikilink_path(target, wiki_dir).exists():
                fails.append(f"  ❌ {loc}：wikilink 探針指向不存在的頁面「{target}」")

        # ── 7. 探針數不足（WARN）──
        if (len(probes) == 1 and not probe_is_wikilink(probes[0])
                and len(probes[0].strip()) < SHORT_PROBE_LEN):
            warns.append(f"  ⚠️ {loc}：單一探針「{probes[0]}」過短，偵測力不足（建議補第二個或改長）")

        # ── 8. 語意反轉殘留（WARN）──
        line = doc.line_text(mk.start)
        if "✅" in line and any(cue in line for cue in REVERSAL_CUES):
            warns.append(f"  ⚠️ {loc}：同行出現「解除／結案／轉為」與 ✅，疑似語意反轉殘留，請確認標記是否早該移除")

        # ── 9. 逾期（WARN，明確不得 FAIL）──
        if marked_date is not None:
            review_date = _parse_date(mk.review) if mk.review else marked_date + timedelta(days=REVIEW_DEFAULT_DAYS)
            if review_date is not None and review_date <= today:
                overdue = (today - review_date).days
                warns.append(f"  ⚠️ {loc}：已逾期 {overdue} 天（複查日 {review_date.isoformat()}）")

    # ── 6. ⟨Q-nn⟩ 雙向對帳 ──
    short_qids = [sm.group("qid") for sm in SHORT_RE.finditer(text)]
    def_qids = [mk.qid for mk in markers if mk.qid]
    short_set, def_set = set(short_qids), set(def_qids)
    for qid in sorted(short_set - def_set):
        fails.append(f"  ❌ {slug}：⟨{qid}⟩ 表格短標記無對應的懸置細節定義")
    for qid in sorted(def_set - short_set):
        fails.append(f"  ❌ {slug}：⟨{qid}⟩ 有懸置細節定義但無表格短標記引用")
    for qid, n in Counter(short_qids).items():
        if n > 1:
            fails.append(f"  ❌ {slug}：⟨{qid}⟩ 表格短標記重複出現 {n} 次")
    for qid, n in Counter(def_qids).items():
        if n > 1:
            fails.append(f"  ❌ {slug}：⟨{qid}⟩ 懸置細節重複定義 {n} 次")

    legacy_count = len(iter_legacy(text, path))
    return fails, warns, legacy_count


def check(report: list[str], wiki_dir: Path | None = None, today: date | None = None) -> bool:
    wiki_dir = wiki_dir or WIKI_DIR
    today = today or date.today()

    ok = True
    total_legacy = 0
    total_markers = 0

    for path in wiki_pages(wiki_dir):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        fails, warns, legacy_count = _page_report(path, text, wiki_dir, today)
        total_legacy += legacy_count
        total_markers += len(iter_pending(text, path))
        if fails:
            ok = False
            report.extend(fails)
        report.extend(warns)

    report.append(
        f"  ℹ️ 存量殘餘：舊字樣（未回填為新語法）共 {total_legacy} 筆，"
        f"新語法標記共 {total_markers} 筆（本項只計數，不影響判定）"
    )
    return ok


def _overdue_entries(wiki_dir: Path, today: date) -> list[tuple[bool, int, str]]:
    """回傳 (有訊欄, 逾期天數, 顯示行) 供排序。"""
    entries: list[tuple[bool, int, str]] = []
    for path in wiki_pages(wiki_dir):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        slug = _slug(path, wiki_dir)
        for mk in iter_pending(text, path):
            marked_date = _parse_date(mk.marked)
            if marked_date is None:
                continue
            review_date = _parse_date(mk.review) if mk.review else marked_date + timedelta(days=REVIEW_DEFAULT_DAYS)
            if review_date is None or review_date > today:
                continue
            overdue = (today - review_date).days
            has_signal = mk.signal is not None
            probes_summary = "、".join(mk.probes[:3])
            line = f"{slug}:{mk.line}｜標 {mk.marked}｜複 {review_date.isoformat()}｜{probes_summary}"
            entries.append((has_signal, overdue, line))

    entries.sort(key=lambda e: (0 if e[0] else 1, -e[1]))
    return entries


def print_queue(out, wiki_dir: Path | None = None, today: date | None = None) -> None:
    wiki_dir = wiki_dir or WIKI_DIR
    today = today or date.today()
    entries = _overdue_entries(wiki_dir, today)
    print("# check_pending_markers.py --queue 逾期佇列\n", file=out)
    for _, _, line in entries[:QUEUE_LIMIT]:
        print(f"  {line}", file=out)
    if not entries:
        print("  （無逾期標記）", file=out)
    print(file=out)
    print(f"總逾期數：{len(entries)}", file=out)


def main() -> int:
    args = sys.argv[1:]
    out = _stdout()

    if "--queue" in args:
        print_queue(out)
        out.flush()
        return 0

    report: list[str] = []
    ok = check(report)
    print("# check_pending_markers.py 報告\n", file=out)
    print("\n".join(report) if report else "  （無懸置標記）", file=out)
    print(file=out)
    print("狀態：" + ("✅ 懸置標記語法檢查通過" if ok else "❌ 懸置標記語法有誤"), file=out)
    out.flush()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
