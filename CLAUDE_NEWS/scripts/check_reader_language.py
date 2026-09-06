#!/usr/bin/env python3
"""讀者語言閘 — 擋掉內部維運用語外洩到讀者看得見的 wiki 正文。

立法依據：2026-09-05 競品頁健檢，冷讀者兩輪都抓到同一件事——讀者看不懂
「12 列上限汰出」「不回訪」「已移交」「每日抄錄」「模式庫」「二手」。
`.claude/rules/wiki-ingest-format.md` 的「無維運術語洩漏」列與
`.claude/rules/wiki-reporter-shared.md` 的「派工過程不上頁」早已明文禁止，
但兩條都只是規則、沒有偵測器——本庫病史的標準形狀（承諾有了、執行點沒有）。
本檔是那兩條規則的執行點。

用法：
    python scripts/check_reader_language.py              # 全庫檢查
    python scripts/check_reader_language.py --list       # 印出禁詞清單與替代詞
    python scripts/check_reader_language.py --page X     # 只看某頁（slug 或路徑片段）
    python scripts/check_reader_language.py --write-baseline   # 重建存量基線（需人工確認）

掃描範圍：wiki/entities/*.md、wiki/topics/*.md、wiki/feature-radar.md、
wiki/overview.md、wiki/index.md 的**正文**——frontmatter、code fence、
Obsidian `%% … %%` 註解、HTML 註解一律跳過（前兩者不上站，後兩者是
「維運備忘的家」，見 `.claude/rules/wiki-reporter-shared.md`）。

存量基線（照 `data/pending-legacy-baseline.json` 的先例）：首跑必然命中大量
存量，全部 FAIL 只會讓人把檢查關掉。故 `data/reader-language-baseline.json`
記下「頁 → 命中指紋」，本檔只對**基線外的新增**報 FAIL，基線內的印為 WARN
摘要。清乾淨一頁就把該頁從基線移除——棘輪只能往下轉。

exit 0 = 無新增命中；1 = 有新增命中（或基線檔損毀）。
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
BASELINE = ROOT / "data" / "reader-language-baseline.json"
ALLOWLIST = ROOT / "data" / "reader-language-allow.json"

# ── 禁詞清單（單一來源）────────────────────────────────────────────────────
# 每筆四欄：
#   key     短代號，指紋與白名單用它指認
#   pattern 命中用的 regex
#   why     為什麼這是內部語言（給修的人判斷用）
#   alt     讀者語言替代詞（給修的人直接抄）
# scope: "any"（預設）或 "table"（只在表格列上算命中）
TERMS: list[dict] = [
    {"key": "ingest", "pattern": r"ingest",
     "why": "產製流程的內部步驟名，讀者不知道 wiki 是怎麼被寫出來的",
     "alt": "「每日更新」"},
    {"key": "lint", "pattern": r"\blint\b",
     "why": "同上，是維運動作名不是頁面性質",
     "alt": "「每週整理」／「每週策展」"},
    {"key": "派工", "pattern": r"派工",
     "why": "編輯部內部分工，讀者不需要知道誰寫的",
     "alt": "刪掉；真要說節奏就寫「每週更新」"},
    {"key": "記者", "pattern": r"記者",
     "why": "本庫的 agent 角色名，對讀者是不存在的職稱",
     "alt": "刪掉，或改成被動語態（「本頁每日更新」）"},
    {"key": "主編", "pattern": r"主編",
     "why": "同上，內部角色名",
     "alt": "刪掉，或寫成 `%% … %%` 維運備忘"},
    {"key": "抄錄", "pattern": r"抄錄",
     "why": "描述的是機器怎麼搬資料，不是讀者拿到什麼",
     "alt": "「本節內容同步自 [[…]]」，或直接不提"},
    {"key": "裁示", "pattern": r"裁示|裁決待|待使用者",
     "why": "本庫的決策流程，讀者不在那個流程裡",
     "alt": "刪掉；未定的事寫成懸置標記或「尚未確定」"},
    {"key": "移交", "pattern": r"已移交|移交\s*\[\[",
     "why": "編輯部的頁面歸屬調整，讀者只需要知道去哪讀",
     "alt": "「完整脈絡見 [[…]]」"},
    {"key": "汰出", "pattern": r"汰出|汰除",
     "why": "策展動作，讀者不需要知道表格怎麼被裁掉的",
     "alt": "「以下未列入上表」，理由寫成 `%% … %%` 備忘"},
    {"key": "不回訪", "pattern": r"不回訪|不再回訪",
     "why": "維護承諾（我們不會再查），不是內容",
     "alt": "「本節為 YYYY-MM-DD 的一次性查證結果，最新請見 [[…]]」"},
    {"key": "source_count", "pattern": r"source_count",
     "why": "收錄門檻的欄位名，是程式碼不是中文",
     "alt": "「多家報導」／「單一來源」"},
    {"key": "專頁定向", "pattern": r"專頁定向|定向抓取",
     "why": "抓取管道的內部名稱",
     "alt": "刪掉；覆蓋範圍寫在「蒐集邊界」欄即可"},
    {"key": "門檻", "pattern": r"達[^。\n|]{0,12}門檻|低門檻|中門檻|高門檻|准入門檻",
     "why": "收錄判準，屬編輯部日誌不屬頁面內容",
     "alt": "刪掉；要說證據強度就寫「多家報導」「單一實測」"},
    {"key": "覆寫", "pattern": r"覆寫",
     "why": "檔案寫入動作，讀者看到的只有結果",
     "alt": "「每週重寫」／刪掉"},
    {"key": "prepend", "pattern": r"prepend",
     "why": "程式術語",
     "alt": "「最新在上」／刪掉"},
    {"key": "回掃", "pattern": r"回掃",
     "why": "更正流程的內部動作",
     "alt": "刪掉"},
    {"key": "轉知", "pattern": r"轉知",
     "why": "跨角色交辦，讀者不在收件人裡",
     "alt": "刪掉，或寫成 `%% … %%` 維運備忘"},
    {"key": "同步自查", "pattern": r"同步自查",
     "why": "記者回報欄名",
     "alt": "刪掉"},
    {"key": "模式庫", "pattern": r"模式庫",
     "why": "內部對 patterns 頁的稱呼，讀者只看得到頁名",
     "alt": "直接寫頁名 [[topics/community-tech-patterns]]"},
    {"key": "二手", "pattern": r"二手", "scope": "table",
     "why": "表格欄名寫「二手」是本庫的證據分級術語，讀者讀成「中古」",
     "alt": "欄名改「媒體轉述」／「非一手來源」"},
    {"key": "週更策展", "pattern": r"週更策展|策展層|lint 專用",
     "why": "描述的是這頁怎麼被維護，不是這頁在講什麼",
     "alt": "「每週更新」"},
    {"key": "每日抄錄", "pattern": r"每日抄錄|機械抄錄",
     "why": "同上，且「機械」二字在講實作",
     "alt": "「內容同步自 [[…]]，每日更新」"},
    {"key": "未收錄", "pattern": r"未收錄",
     "why": "收錄／篩選是編輯部日誌用語，讀者不在收錄決策的流程裡",
     "alt": "刪掉；要說明就寫「證據不足，暫不列入」"},
    {"key": "收錄標準", "pattern": r"收錄標準|收錄門檻",
     "why": "同上，是策展判準不是頁面內容",
     "alt": "刪掉，或改寫成讀者能自行對號的分界句"},
    {"key": "候選症狀", "pattern": r"候選症狀",
     "why": "決策表開新列前的內部暫記用語，讀者看不懂在候選什麼",
     "alt": "移進 `%% … %%` 維運備忘，或直接刪掉"},
    {"key": "低度信號", "pattern": r"低度信號",
     "why": "本庫內部的證據分級詞，不是讀者語言",
     "alt": "「證據不足」／「單一低互動來源」"},
    {"key": "退場", "pattern": r"(?<!企業)退場(?!交易|機制)",
     "why": "表格列存續與否的內部維運判準，讀者不需要知道一列什麼時候被拿掉",
     "alt": "「不再列入表格」／「已解決，見歷史記錄」；描述真實事件用「下市」「退出」等具體詞",
     "why_exception": "「退場交易」「退場機制」「企業退場」是財經／產業常用語（IPO、併購、退出市場），與本庫表格維護的「退場」語意不同，正則排除"},
    {"key": "留表優先序", "pattern": r"留表優先序",
     "why": "表格滿載時決定誰留誰讓位的內部排序規則，讀者看不到表格背後的排序邏輯",
     "alt": "刪掉；要交代取捨就直接寫具體理由一句"},
    {"key": "表滿載", "pattern": r"表滿載",
     "why": "表格容量已滿的維運狀態描述，不是頁面內容",
     "alt": "「未列入上表」，理由寫成 `%% … %%` 備忘"},
    {"key": "讓位者", "pattern": r"讓位者",
     "why": "表格滿載時被擠出去的那一列的內部稱呼",
     "alt": "刪掉，或直接寫「移出表格」"},
    {"key": "證據層", "pattern": r"證據層",
     "why": "本庫的頁面分層術語（結論層 vs 證據層），讀者只看得到內容本身",
     "alt": "刪掉，或直接描述這是什麼樣的證據"},
    {"key": "結論層", "pattern": r"結論層",
     "why": "同上，是內部的頁面結構分層詞",
     "alt": "刪掉，或直接寫結論本身"},
    {"key": "墊底下沉", "pattern": r"墊底下沉",
     "why": "表格淘汰機制的內部稱呼",
     "alt": "刪掉，或寫「移出表格」"},
    {"key": "蒸餾", "pattern": r"蒸餾候選|時段蒸餾|月度蒸餾|下一輪蒸餾|待蒸餾|蒸餾工程",
     "why": "本庫「厚頁減重」editorial 流程的內部稱呼，讀者不需要知道頁面怎麼被收斂",
     "alt": "刪掉，或寫「本節為精簡摘要，完整記錄見 [[…封存頁]]」",
     "why_exception": "只narrow 到與「候選/時段/月度/下一輪/待/工程」搭配的內部流程用法——裸字「蒸餾」在本庫也是真實新聞詞（Alibaba Qwen 對 Claude 的模型蒸餾攻擊指控、Opus 4.8「蒸餾雙標」爭議），裸字全面禁止會誤傷這條持續在報導的新聞線"},
    {"key": "封存", "pattern": r"封存", "skip_if_archive": True,
     "why": "頁面被移到 archive 子頁保存的內部維運動作，讀者只需要知道去哪讀最新內容",
     "alt": "「完整記錄見 [[…]]」；archive 頁本身的說明文字不受此限（見白名單）"},
    {"key": "保留最近", "pattern": r"保留最近",
     "why": "內容保留窗口是編輯部的資料保存政策，不是頁面在講的事",
     "alt": "刪掉，或直接寫「最新 N 天」而不解釋為什麼只留這些"},
]

_COMPILED = [(t, re.compile(t["pattern"])) for t in TERMS]

TARGET_GLOBS = ("entities/*.md", "topics/*.md")
TARGET_FILES = ("feature-radar.md", "overview.md", "index.md")

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
INLINE_PCT_RE = re.compile(r"%%.*?%%", re.S)
INLINE_HTML_RE = re.compile(r"<!--.*?-->", re.S)


def _stdout():
    """Windows 主控台預設 cp950，直接 print 中文與符號會 UnicodeEncodeError。"""
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def target_files() -> list[Path]:
    files: list[Path] = []
    for g in TARGET_GLOBS:
        files.extend(sorted(WIKI.glob(g)))
    for name in TARGET_FILES:
        f = WIKI / name
        if f.exists():
            files.append(f)
    return files


def page_id(f: Path) -> str:
    try:
        return f.relative_to(WIKI).as_posix()[:-3]
    except ValueError:
        return f.stem


def body_lines(text: str) -> list[tuple[int, str]]:
    """回傳 (行號, 可檢查的正文) — frontmatter / code fence / %% 註解 / HTML 註解已剝除。

    多行註解用狀態機處理；單行內的 `%%…%%` 與 `<!--…-->` 先就地剝除。
    行號以原檔為準（frontmatter 佔的行數要補回去，否則報出來的行號對不上檔案）。
    """
    fm = FRONTMATTER_RE.match(text)
    offset = text[: fm.end()].count("\n") if fm else 0
    body = text[fm.end():] if fm else text

    out: list[tuple[int, str]] = []
    in_fence = False
    in_pct = False
    in_html = False
    for i, raw in enumerate(body.splitlines(), 1):
        lineno = i + offset
        line = raw
        if in_pct:
            if "%%" in line:
                in_pct = False
                line = line.split("%%", 1)[1]
            else:
                continue
        if in_html:
            if "-->" in line:
                in_html = False
                line = line.split("-->", 1)[1]
            else:
                continue
        if re.match(r"\s*```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = INLINE_PCT_RE.sub("", line)
        line = INLINE_HTML_RE.sub("", line)
        if "%%" in line:
            in_pct = True
            line = line.split("%%", 1)[0]
        if "<!--" in line:
            in_html = True
            line = line.split("<!--", 1)[0]
        if line.strip():
            out.append((lineno, line))
    return out


def fingerprint(term_key: str, line: str) -> str:
    """指紋 = 詞 + 該行正規化內容的雜湊。用內容而非行號，頁面增刪行不會讓基線整批失效。"""
    norm = re.sub(r"\s+", "", line.strip())
    return f"{term_key}:{hashlib.sha1(norm.encode('utf-8')).hexdigest()[:12]}"


def load_allowlist() -> list[dict]:
    if not ALLOWLIST.exists():
        return []
    data = json.loads(ALLOWLIST.read_text(encoding="utf-8"))
    return data.get("allow", [])


def is_allowed(allow: list[dict], page: str, term: str, line: str) -> bool:
    for a in allow:
        if a.get("page") not in (page, "*"):
            continue
        if a.get("term") not in (term, "*"):
            continue
        needle = a.get("line_contains")
        if needle and needle not in line:
            continue
        return True
    return False


def scan(files: list[Path] | None = None, allow: list[dict] | None = None) -> list[dict]:
    """回傳所有命中：{page, line, term, why, alt, snippet, fp}。"""
    allow = load_allowlist() if allow is None else allow
    hits: list[dict] = []
    for f in files if files is not None else target_files():
        pid = page_id(f)
        try:
            text = f.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        for lineno, line in body_lines(text):
            is_table = line.lstrip().startswith("|")
            for term, rx in _COMPILED:
                if term.get("scope") == "table" and not is_table:
                    continue
                if term.get("skip_if_archive") and pid.endswith("-archive"):
                    continue
                if not rx.search(line):
                    continue
                if is_allowed(allow, pid, term["key"], line):
                    continue
                hits.append({
                    "page": pid, "line": lineno, "term": term["key"],
                    "why": term["why"], "alt": term["alt"],
                    "snippet": line.strip()[:90], "fp": fingerprint(term["key"], line),
                })
    return hits


def load_baseline() -> dict[str, list[str]]:
    if not BASELINE.exists():
        return {}
    data = json.loads(BASELINE.read_text(encoding="utf-8"))
    return {k: v for k, v in data.get("pages", {}).items()}


def write_baseline(hits: list[dict]) -> None:
    pages: dict[str, list[str]] = {}
    for h in hits:
        pages.setdefault(h["page"], [])
        if h["fp"] not in pages[h["page"]]:
            pages[h["page"]].append(h["fp"])
    for v in pages.values():
        v.sort()
    payload = {
        "_note": (
            "讀者語言閘的存量基線（頁 → 命中指紋）。check_reader_language.py 只對基線外的"
            "新增命中 FAIL，基線內的印為 WARN 摘要。清乾淨一頁就把該頁整筆移除——棘輪只能"
            "往下轉，不可為了轉綠而加回去。指紋 = 禁詞 + 該行正規化內容雜湊，改寫該行即失效。"
        ),
        "_baseline_set": "2026-09-05",
        "_pages": len(pages),
        "_hits": sum(len(v) for v in pages.values()),
        "pages": dict(sorted(pages.items())),
    }
    BASELINE.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def split_hits(hits: list[dict], baseline: dict[str, list[str]]) -> tuple[list[dict], list[dict]]:
    """(基線外新增, 基線內存量)。"""
    new, legacy = [], []
    for h in hits:
        (legacy if h["fp"] in baseline.get(h["page"], []) else new).append(h)
    return new, legacy


def main() -> int:
    ap = argparse.ArgumentParser(description="讀者語言閘")
    ap.add_argument("--list", action="store_true", help="印禁詞清單與讀者語言替代詞")
    ap.add_argument("--page", help="只掃某頁（slug 片段）")
    ap.add_argument("--write-baseline", action="store_true", help="以當前命中重建存量基線")
    args = ap.parse_args()
    out = _stdout()

    if args.list:
        out.write(f"讀者語言閘禁詞清單（{len(TERMS)} 個）\n\n")
        for t in TERMS:
            scope = "（僅表格列）" if t.get("scope") == "table" else ""
            out.write(f"- {t['key']}{scope}\n    為什麼：{t['why']}\n    改成：{t['alt']}\n")
        out.flush()
        return 0

    files = target_files()
    if args.page:
        files = [f for f in files if args.page in page_id(f)]

    hits = scan(files)

    if args.write_baseline:
        if args.page:
            out.write("拒絕：--write-baseline 必須掃全庫，不可只憑單頁重建基線\n")
            out.flush()
            return 1
        write_baseline(hits)
        out.write(f"已重建基線：{BASELINE.relative_to(ROOT).as_posix()}（{len(hits)} 筆）\n")
        out.flush()
        return 0

    baseline = load_baseline()
    new, legacy = split_hits(hits, baseline)

    if new:
        out.write(f"FAIL: 讀者語言閘 — {len(new)} 筆新增的內部用語外洩\n\n")
        for h in new:
            out.write(f"  {h['page']}.md:{h['line']}  [{h['term']}]\n")
            out.write(f"    {h['snippet']}\n")
            out.write(f"    為什麼不行：{h['why']}\n")
            out.write(f"    改成：{h['alt']}\n\n")
        out.write("修法三選一：改寫成讀者語言／移進 `%% … %%` 維運備忘（網站不渲染）／"
                  "確有正當理由則登記 data/reader-language-allow.json（附理由）\n")

    # 存量 WARN 摘要（供 /wiki-lint 抄進回報）
    by_page: dict[str, int] = {}
    for h in legacy:
        by_page[h["page"]] = by_page.get(h["page"], 0) + 1
    top = sorted(by_page.items(), key=lambda kv: -kv[1])[:5]
    out.write(f"\nWARN: 存量基線內 {len(legacy)} 筆／{len(by_page)} 頁"
              f"（前 5 頁：{'、'.join(f'{p}({n})' for p, n in top) or '無'}）\n")
    if not new:
        out.write("OK: 讀者語言閘 — 無新增命中\n")
    out.flush()
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
