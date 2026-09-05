#!/usr/bin/env python3
"""表格儲存格 / 細節區條列字元上限機械閘 — 「表格放結論，細節下沉」的執行點。

立法依據：`.claude/rules/wiki-ingest-format.md`「表格放結論，細節下沉（全站
通用）」與 `.claude/rules/wiki-reporter-shared.md`「書寫風格」——查證過程、
演進脈絡、多來源歧異塞進表格儲存格會讓表格失去可掃描性並在網站爆版；下沉
到表格正下方的細節區後，細節區條列本身仍受 200 字元上限拘束，不是換成無
上限的傾倒區。2026-08-27 起這兩條規則只有規則檔明文，沒有偵測器（本庫病史
的標準形狀：承諾有了、執行點沒有）。本檔是那兩條規則的執行點，模型記者
2026-09-05 model-comparison 健檢定稿 §7.2 指定新增。

用法：
    python scripts/check_cell_limits.py                # 全庫檢查
    python scripts/check_cell_limits.py --page X        # 只看某頁（slug 片段）
    python scripts/check_cell_limits.py --rebuild        # 重建存量基線（需人工確認）

量測規則：
    - 表格列（以 `|` 開頭的行）：逐格量測，**> 120 字元**算超限
    - 非表格的條列（`- ` / `* ` 開頭，含巢狀縮排）：整行（去除項目符號後）
      **> 200 字元**算超限
    - 量測前先剝掉 markdown 連結的 URL（`[文字](url)` -> `[文字]`），只量渲染
      可見文字
    - 排除純引用來源格（標題＋URL＋日期，去 URL 後仍是短句）——本檔以「剝除
      URL 後仍超限」為準，天然涵蓋此豁免：純引用格的可見文字通常很短
    - 排除 `*-archive.md`（蒐集契約明定 archive 原文一字不刪，不受本閘拘束）
    - frontmatter / code fence / `%% … %%` 註解 / HTML 註解不算（沿用
      check_reader_language.py 的 body_lines() 剝除邏輯）

存量基線（照 `data/reader-language-baseline.json` 的先例）：首跑必然命中大量
存量，全部 FAIL 只會讓人把檢查關掉。故 `data/cell-limit-baseline.json` 記下
「頁 → 命中指紋」，本檔只對**基線外的新增**報 FAIL，基線內的印為 WARN 摘要。
清乾淨一頁就把該頁從基線移除——棘輪只能往下轉。

exit 0 = 無新增超限；1 = 有新增超限（或基線檔損毀）。
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
BASELINE = ROOT / "data" / "cell-limit-baseline.json"

TABLE_LIMIT = 120
LIST_LIMIT = 200

TARGET_GLOBS = ("entities/*.md", "topics/*.md")
TARGET_FILES = ("feature-radar.md", "overview.md", "index.md")

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
INLINE_PCT_RE = re.compile(r"%%.*?%%", re.S)
INLINE_HTML_RE = re.compile(r"<!--.*?-->", re.S)
MD_LINK_RE = re.compile(r"\]\([^)]*\)")
LIST_ITEM_RE = re.compile(r"^(\s*)([-*])\s+(.*)$")


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
    # archive 頁排除：蒐集契約明定原文一字不刪，不受本閘拘束
    return [f for f in files if not f.stem.endswith("-archive")]


def page_id(f: Path) -> str:
    try:
        return f.relative_to(WIKI).as_posix()[:-3]
    except ValueError:
        return f.stem


def body_lines(text: str) -> list[tuple[int, str]]:
    """回傳 (行號, 可檢查的正文) — frontmatter / code fence / %% 註解 / HTML 註解已剝除。

    邏輯與 check_reader_language.py 的同名函式一致（單一演算法，兩處各自維護
    是可接受的重複——兩支腳本各自獨立、互不 import，複製比抽共用模組簡單）。
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


def _strip_link_urls(text: str) -> str:
    """剝掉 markdown 連結的 URL，只留可見文字——規則檔明文的量測前置步驟。"""
    return MD_LINK_RE.sub("]", text)


def _table_cells(line: str) -> list[str]:
    """表格列的儲存格（去頭尾空格），不含開頭/結尾的空字串。"""
    stripped = line.strip()
    if not stripped.startswith("|"):
        return []
    parts = stripped.split("|")
    # split 會在開頭/結尾產生空字串（因為列以 | 開頭與結尾）
    return [p.strip() for p in parts[1:-1]] if len(parts) > 2 else []


def fingerprint(kind: str, content: str) -> str:
    """指紋 = 類型 + 正規化內容雜湊。用內容而非行號，頁面增刪行不會讓基線整批失效。"""
    norm = re.sub(r"\s+", "", content.strip())
    return f"{kind}:{hashlib.sha1(norm.encode('utf-8')).hexdigest()[:12]}"


def scan(files: list[Path] | None = None) -> list[dict]:
    """回傳所有超限命中：{page, line, kind, limit, length, snippet, fp}。"""
    hits: list[dict] = []
    for f in files if files is not None else target_files():
        pid = page_id(f)
        try:
            text = f.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        for lineno, raw_line in body_lines(text):
            stripped = raw_line.strip()
            if stripped.startswith("|"):
                for cell in _table_cells(raw_line):
                    visible = _strip_link_urls(cell)
                    if len(visible) > TABLE_LIMIT:
                        hits.append({
                            "page": pid, "line": lineno, "kind": "table_cell",
                            "limit": TABLE_LIMIT, "length": len(visible),
                            "snippet": visible[:100],
                            "fp": fingerprint("table_cell", cell),
                        })
                continue
            m = LIST_ITEM_RE.match(raw_line)
            if m:
                content = m.group(3)
                visible = _strip_link_urls(content)
                if len(visible) > LIST_LIMIT:
                    hits.append({
                        "page": pid, "line": lineno, "kind": "list_item",
                        "limit": LIST_LIMIT, "length": len(visible),
                        "snippet": visible[:100],
                        "fp": fingerprint("list_item", content),
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
            "字元上限機械閘的存量基線（頁 → 命中指紋）。check_cell_limits.py 只對基線外的"
            "新增超限報 FAIL，基線內的印為 WARN 摘要。清乾淨一頁就把該頁整筆移除——棘輪只能"
            "往下轉，不可為了轉綠而加回去。指紋 = 類型 + 該格/該條正規化內容雜湊，改寫即失效。"
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
    ap = argparse.ArgumentParser(description="字元上限機械閘")
    ap.add_argument("--page", help="只掃某頁（slug 片段）")
    ap.add_argument("--rebuild", action="store_true", help="以當前命中重建存量基線")
    args = ap.parse_args()
    out = _stdout()

    files = target_files()
    if args.page:
        files = [f for f in files if args.page in page_id(f)]

    hits = scan(files)

    if args.rebuild:
        if args.page:
            out.write("拒絕：--rebuild 必須掃全庫，不可只憑單頁重建基線\n")
            out.flush()
            return 1
        write_baseline(hits)
        out.write(f"已重建基線：{BASELINE.relative_to(ROOT).as_posix()}（{len(hits)} 筆）\n")
        out.flush()
        return 0

    baseline = load_baseline()
    new, legacy = split_hits(hits, baseline)

    if new:
        out.write(f"FAIL: 字元上限機械閘 — {len(new)} 筆新增的超限儲存格／條列\n\n")
        for h in new:
            what = "表格儲存格（>120）" if h["kind"] == "table_cell" else "細節區條列（>200）"
            out.write(f"  {h['page']}.md:{h['line']}  [{what}，實測 {h['length']} 字元]\n")
            out.write(f"    {h['snippet']}...\n\n")
        out.write("修法：查證過程／原文比對／多來源歧異一律下沉到表格正下方的細節區；細節區"
                  "條列本身仍受 200 字元上限拘束，超過就拆成兩條或改用 wikilink 指回事實的家\n")
        out.write("誤擋自查：指紋是內容雜湊，改寫既有超限文字（哪怕沒變長、甚至變短）也會脫離"
                  "基線而被判新增。若你改寫的是既有超限段落且已切到上限內，那不是誤擋，照修法"
                  "處理；若確認該段本來就在基線、你也沒有加長它，跑 --rebuild 重收基線並在 "
                  "commit 訊息說明原因\n")

    # 存量 WARN 摘要（供 /wiki-lint 抄進回報）
    by_page: dict[str, int] = {}
    for h in legacy:
        by_page[h["page"]] = by_page.get(h["page"], 0) + 1
    top = sorted(by_page.items(), key=lambda kv: -kv[1])[:5]
    out.write(f"\nWARN: 存量基線內 {len(legacy)} 筆／{len(by_page)} 頁"
              f"（前 5 頁：{'、'.join(f'{p}({n})' for p, n in top) or '無'}）\n")
    if not new:
        out.write("OK: 字元上限機械閘 — 無新增超限\n")
    out.flush()
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
