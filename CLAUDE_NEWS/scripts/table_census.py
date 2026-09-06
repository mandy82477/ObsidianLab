#!/usr/bin/env python3
"""table_census.py — 全站 wiki 表格普查（頁面健檢卡第 6 問「熱表格有沒有淘汰機制」的機械輸入）。

每張表列出：頁｜所在節｜欄數｜列數｜有無日期欄｜成長型態｜規則檔有無明文機制。
- 成長型態：`prepend`（列內含日期且由新到舊）／`append`（由舊到新）／`mixed`（順序混雜）／
  `unknown`（判不出來：無日期欄，或有日期欄但列內找不到足夠日期樣本）。
  `unknown` 不是「已判定不會變」，是「這支腳本量不出來」——無日期欄的表可能仍在成長
  （如純累加列表），只是看不出方向；不可把 `unknown` 讀成「安全，不用管」。
- 機制：在 `.claude/rules/*.md`、`.claude/commands/*.md` 搜該表所在節名，**命中行必須同時
  含該頁 slug／頁名，或落在該頁專屬規則節內**，才算「有」；否則視為命中別頁同名節（規則檔
  常見「摘要」「時序」這類通用節名，任何頁都會字面命中，但講的是別頁的規則）。
  這是啟發式，「有」代表有人寫過規則，不代表規則被執行；「無」是真正的訊號——
  只長不縮的表遲早爆版（2026-09-05 立法依據：健檢卡框架第 6 問；頁面範圍過濾：2026-09-06）。

用法：
  python scripts/table_census.py                 # 全站，依列數降序
  python scripts/table_census.py topics/competitor-landscape   # 單頁
  python scripts/table_census.py --no-mechanism  # 只列無機制的成長表
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RULE_FILES = list((ROOT / ".claude" / "rules").glob("*.md")) + list((ROOT / ".claude" / "commands").glob("*.md"))
MECH_RE = re.compile(r"淘汰|移除|保留|封存|覆寫|蒸餾|汰除|到期|清理")
DATE_RE = re.compile(r"\b20\d\d-\d\d(?:-\d\d)?\b|\b\d{1,2}/\d{1,2}\b")
EXCLUDE = {"index", "log", "CLAUDE", "metrics", "reader-notes"}


def _stdout():
    return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True)


def _rule_text():
    return [(f, f.read_text(encoding="utf-8-sig")) for f in RULE_FILES]


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def _mechanism(section: str, rules, page_slug: str, page_title: str = "") -> str:
    """判定該表所在節名，在規則檔裡是否有「這頁專屬」的淘汰／覆寫類機制。

    通用節名（摘要、時序……）在任何頁都會字面命中規則檔裡講別頁的同名節，因此
    命中行本身，或命中行所屬的最近標題，必須含該頁的 slug 基名或頁面標題其中之一，
    才算數——否則只是巧合撞名。
    """
    key = section.strip().strip("`").split(" `[")[0]
    key = re.sub(r"（.*?）", "", key).strip()
    if len(key) < 2:
        return "無"
    basename = page_slug.rsplit("/", 1)[-1]
    idents = [i for i in (basename, page_title) if i]
    hits = []
    for f, text in rules:
        heading = ""
        for ln in text.splitlines():
            hm = HEADING_RE.match(ln)
            if hm:
                heading = hm.group(2)
            if key in ln and MECH_RE.search(ln):
                scope = f"{ln} {heading}"
                if any(ident and ident in scope for ident in idents):
                    hits.append(f.name)
                    break
    return "有（" + "、".join(sorted(set(hits))[:2]) + "）" if hits else "無"


def _growth(rows: list[str], has_date_col: bool) -> str:
    """判斷表格的成長方向；判不出來（無日期欄，或日期樣本不足）一律回 `unknown`。"""
    if not has_date_col:
        return "unknown"
    dates = []
    for r in rows:
        m = DATE_RE.search(r)
        if m:
            dates.append(m.group(0))
    if len(dates) < 2 or len(dates) < len(rows) * 0.5:
        return "unknown"
    norm = [d if "-" in d else "0000-" + d.replace("/", "-").zfill(5) for d in dates]
    if norm == sorted(norm, reverse=True):
        return "prepend"
    if norm == sorted(norm):
        return "append"
    return "mixed"


def census(pages):
    rules = _rule_text()
    out = []
    for slug, f in pages:
        section = "—"
        lines = f.read_text(encoding="utf-8-sig").splitlines()
        title = ""
        for ln0 in lines[:5]:
            tm = re.match(r"^#\s+(.+?)\s*$", ln0)
            if tm:
                title = tm.group(1)
                break
        i = 0
        while i < len(lines):
            ln = lines[i]
            m = re.match(r"^(#{2,4})\s+(.+?)\s*$", ln)
            if m:
                section = m.group(2)
            if ln.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
                header = [c.strip() for c in ln.strip().strip("|").split("|")]
                j = i + 2
                rows = []
                while j < len(lines) and lines[j].lstrip().startswith("|"):
                    rows.append(lines[j])
                    j += 1
                date_col = any(re.search(r"日期|日|首見|確認|更新", h) for h in header)
                out.append({
                    "page": slug, "section": section, "cols": len(header), "rows": len(rows),
                    "date_col": date_col,
                    "growth": _growth(rows, date_col),
                    "mechanism": _mechanism(section, rules, slug, title),
                    "header": header,
                })
                i = j
                continue
            i += 1
    return out


def main() -> int:
    out = _stdout()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only_gap = "--no-mechanism" in sys.argv
    pages = []
    for f in sorted(WIKI.rglob("*.md")):
        slug = f.relative_to(WIKI).as_posix()[:-3]
        if slug in EXCLUDE or slug.startswith("_views/"):
            continue
        if args and slug not in args:
            continue
        pages.append((slug, f))
    rows = census(pages)
    if only_gap:
        rows = [r for r in rows if r["growth"] in ("prepend", "append", "mixed") and r["mechanism"] == "無"]
    rows.sort(key=lambda r: -r["rows"])
    print(f"# 表格普查：{len(rows)} 張（頁 {len(pages)}）\n", file=out)
    print("| 頁 | 節 | 欄 | 列 | 成長 | 機制 |\n|---|---|---|---|---|---|", file=out)
    for r in rows:
        print(f"| {r['page']} | {r['section'][:34]} | {r['cols']} | {r['rows']} | {r['growth']} | {r['mechanism']} |", file=out)
    grow = [r for r in rows if r["growth"] not in ("unknown",)]
    nomech = [r for r in grow if r["mechanism"] == "無"]
    unk = [r for r in rows if r["growth"] == "unknown"]
    print(f"\n成長型表 {len(grow)}，其中無明文機制 {len(nomech)}。"
          f"另有 {len(unk)} 張 unknown（無日期欄或日期樣本不足，判不出成長方向，非「已判定不會變」）。",
          file=out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
