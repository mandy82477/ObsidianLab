#!/usr/bin/env python3
"""盤點 wiki 既有的懸置標記，把雜訊與真待辦分開。

用法：
    python scripts/audit_pending_markers.py            # 全庫盤點
    python scripts/audit_pending_markers.py --page entities/claude-code
    python scripts/audit_pending_markers.py --json-only

為什麼需要這支：全庫約 400 行帶「待查證／待核實／…」字樣，但那**不是 400 筆待辦**。
裡面混著已解除的成功案例（「本頁解除待核實」）、符號圖例、計數摘要標頭、目錄
anchor。回填前必須先知道真實分母，否則會照著一份灌水的清單派工。

**這支腳本是篩子不是判官。** R（已解除敘述）與 U（偵測不了）兩類一律附原文脈絡並
標「需人工過目」——它的任務是把 400 筆砍成可讀的一百多筆，不是替人做判斷。

回填完成後本腳本不退役：`--json-only` 供進度對帳，而 `iter_legacy()` 永遠是
「有沒有人又手寫舊字樣」的偵測器。
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pending_markers import (  # noqa: E402
    REPO_ROOT, WIKI_DIR, iter_legacy, iter_pending, page_domain,
    page_slug, reporter_of, wiki_pages,
)

OUT_PATH = REPO_ROOT / "data" / "pending-audit.json"

CLS_LABEL = {
    "P": "P 真懸置",
    "M": "M 元層級",
    "R": "R 已解除敘述",
    "U": "U 偵測不了",
}
SHAPE_LABEL = {"list": "條列", "table": "表格列", "callout": "callout",
               "heading": "標頭", "prose": "散文"}


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def _norm_seg(seg: str) -> str:
    return re.sub(r"\s+", "", seg)


def _record_id(slug: str, word: str, seg: str) -> str:
    """刻意不含行號——回填本身會讓行號漂移，含行號的 id 一改就無法對帳進度。"""
    raw = f"{slug}|{word}|{_norm_seg(seg)}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:8]


def collect(pages: list[Path]) -> tuple[list[dict], Counter, int]:
    records: list[dict] = []
    tally: Counter = Counter()
    already_new = 0

    for path in pages:
        try:
            text = path.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        slug = page_slug(path)
        already_new += len(iter_pending(text, path))
        domain = page_domain(path)
        reporter = reporter_of(path)

        for hit in iter_legacy(text, path):
            tally[hit.cls] += 1
            if hit.cls == "P":
                tally[f"P:{hit.shape}"] += 1
            records.append({
                "id": _record_id(slug, hit.word, hit.segment),
                "page": slug,
                "file": path.relative_to(REPO_ROOT).as_posix(),
                "line": hit.line,
                "word": hit.word,
                "cls": hit.cls,
                "cls_reason": hit.reason,
                "shape": hit.shape,
                "in_table_cell": hit.in_table_cell,
                "cell_len": hit.cell_len,
                "segment": hit.segment,
                "event_dates": hit.event_dates,
                "wikilinks": hit.wikilinks,
                "domain": domain,
                "reporter": reporter,
                "backfilled": False,
            })
    return records, tally, already_new


def render(records: list[dict], tally: Counter, already_new: int, pages: int, out) -> None:
    total = len(records)
    print("# audit_pending_markers.py 報告\n", file=out)
    print(f"  掃描 {pages} 頁，舊字樣 {total} 筆，已是新語法 {already_new} 筆\n", file=out)

    for cls in ("M", "R", "U", "P"):
        n = tally.get(cls, 0)
        pct = f"{n / total * 100:4.1f}%" if total else "  0.0%"
        note = ""
        if cls in ("R", "U"):
            note = "  ← 需人工過目"
        if cls == "P":
            shapes = "｜".join(
                f"{SHAPE_LABEL.get(s, s)} {tally.get(f'P:{s}', 0)}"
                for s in ("list", "table", "callout", "heading", "prose")
                if tally.get(f"P:{s}", 0)
            )
            note = f"  （{shapes}）" if shapes else ""
        print(f"  {CLS_LABEL[cls]:<14} {n:>4}  {pct}{note}", file=out)

    by_reporter: Counter = Counter()
    by_page: Counter = Counter()
    for r in records:
        if r["cls"] == "P":
            by_reporter[r["reporter"] or "（未分派）"] += 1
            by_page[r["page"]] += 1

    if by_page:
        print("\n  ── P 真懸置分布（前 10 頁）──", file=out)
        for page, n in by_page.most_common(10):
            print(f"    {n:>4}  {page}", file=out)
        print("\n  ── P 真懸置分派 ──", file=out)
        for rep, n in by_reporter.most_common():
            print(f"    {n:>4}  {rep}", file=out)

    for cls in ("R", "U"):
        rows = [r for r in records if r["cls"] == cls]
        if not rows:
            continue
        print(f"\n  ── {CLS_LABEL[cls]}（需人工過目，{len(rows)} 筆）──", file=out)
        for r in rows[:25]:
            print(f"    {r['file']}:{r['line']}  [{r['cls_reason']}]", file=out)
            print(f"      …{r['segment'][:100]}…", file=out)
        if len(rows) > 25:
            print(f"    （另 {len(rows) - 25} 筆見 {OUT_PATH.name}）", file=out)


def main() -> int:
    out = _stdout()
    args = sys.argv[1:]
    json_only = "--json-only" in args
    page_filter = None
    if "--page" in args:
        try:
            page_filter = args[args.index("--page") + 1]
        except IndexError:
            print("用法：--page entities/claude-code", file=out)
            out.flush()
            return 2

    pages = wiki_pages()
    if page_filter:
        pages = [p for p in pages if page_slug(p) == page_filter]
        if not pages:
            print(f"找不到頁面：{page_filter}", file=out)
            out.flush()
            return 2

    records, tally, already_new = collect(pages)

    if not json_only:
        render(records, tally, already_new, len(pages), out)

    payload = {
        "tool": "scripts/audit_pending_markers.py",
        "pages_scanned": len(pages),
        "totals": {
            "legacy_total": len(records),
            "already_new_syntax": already_new,
            **{c: tally.get(c, 0) for c in ("P", "M", "R", "U")},
        },
        "records": records,
    }
    OUT_PATH.parent.mkdir(exist_ok=True)
    OUT_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    if not json_only:
        print(f"\n狀態：✅ 盤點完成，結構化結果寫入 {OUT_PATH.relative_to(REPO_ROOT).as_posix()}", file=out)
    out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
