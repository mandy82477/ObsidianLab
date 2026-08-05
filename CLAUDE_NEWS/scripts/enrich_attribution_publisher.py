"""為 source_attribution.jsonl 補上 publisher（出版者／子版／站名）欄位。

**為什麼需要這個檔**

`source` 欄記的是來源 slug，但其中 `google-news` 根本不是一個來源，是聚合器：
2026-07-11～08-04 的 662 則 Google News 條目來自 **253 個不同出版者**，143 家只出現
過一次，前 20 大加起來也只佔 36%。同一個 slug 底下同時有 Reuters／WSJ／FT／
Bloomberg／NYT，和 tech-insider.org／Startup Fortune／Yogonet——`source_registry.json`
給 Google News 的那組品質標籤同時套在 Reuters 和 Yogonet 上，等於沒有標籤。

出版者其實**從來沒有遺失**：`sources/google_news.py` 存的是 `Google News / Reuters`，
日報 `news/*.md` 的來源標記也原樣保留。是歸因那一步（`.claude/rules/wiki-reporter-shared.md`
規定 slug「取『/』前半段」）把斜線後半段丟掉的。本檔把它撿回來——不改上游、不改
記者契約，純粹從日報回推。

同樣的斜線結構也存在於其他來源，一併還原：
    Google News / Financial Times   → publisher: Financial Times
    Reddit / r/ClaudeAI · 週熱門     → publisher: r/ClaudeAI
    Blog / Simon Willison           → publisher: Simon Willison
    GitHub Issues / claude-code     → publisher: claude-code
    Hacker News                     → 無斜線，不補 publisher（來源即出版者）

**冪等**：已有 publisher 的行不動，可重複執行。日報找不到對應 URL 的行也不動
（歸因機制 2026-07-11 上線，更早的日報條目未必留存對應連結）。

用法：
    python scripts/enrich_attribution_publisher.py --dry-run   # 只報告，不寫檔
    python scripts/enrich_attribution_publisher.py             # 實際寫入
"""

from __future__ import annotations

import collections
import io
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "news"
ATTRIBUTION = REPO_ROOT / "data" / "source_attribution.jsonl"

# 日報條目標題行：**[標題](url)**
TITLE_RE = re.compile(r"^\*\*\[.*?\]\((\S+?)\)\*\*\s*$")
# 來源標記行：`Google News / Financial Times` · 08/04 07:03 UTC
SOURCE_RE = re.compile(r"^`([^`]+)`")


def _stdout():
    """Windows 主控台預設 cp950，直接 print 中文/符號會 UnicodeEncodeError。"""
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def split_publisher(source_marker: str) -> str | None:
    """`Google News / Financial Times` → 'Financial Times'；無斜線回 None。

    Reddit 的 `· 週熱門` 是抓法標記不是出版者身分，切掉。
    """
    if "/" not in source_marker:
        return None
    tail = source_marker.split("/", 1)[1].strip()
    tail = tail.split("·", 1)[0].strip()
    return tail or None


def build_url_map() -> dict[str, str]:
    """掃全部日報，建 url → 完整來源標記字串 的對照。"""
    url_to_source: dict[str, str] = {}
    for path in sorted(NEWS_DIR.glob("*.md")):
        pending_url: str | None = None
        for line in path.read_text(encoding="utf-8").splitlines():
            m = TITLE_RE.match(line.strip())
            if m:
                pending_url = m.group(1)
                continue
            if pending_url:
                s = SOURCE_RE.match(line.strip())
                if s:
                    # 後見優先：同一 URL 跨日重複出現時保留較新日報的標記
                    url_to_source[pending_url] = s.group(1).strip()
                    pending_url = None
    return url_to_source


def main(argv: list[str]) -> int:
    stream = _stdout()
    dry_run = "--dry-run" in argv

    if not ATTRIBUTION.exists():
        stream.write(f"ERROR: 找不到 {ATTRIBUTION}\n")
        return 1

    url_to_source = build_url_map()
    stream.write(f"日報 URL 對照表：{len(url_to_source)} 筆\n")

    rows: list[dict] = []
    already = added = unmatched = no_publisher = 0
    pub_counter: collections.Counter[str] = collections.Counter()

    with ATTRIBUTION.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                stream.write(f"WARN: 第 {line_no} 行非合法 JSON，原樣保留\n")
                rows.append({"__raw__": line})
                continue

            if "publisher" in row:
                already += 1
                rows.append(row)
                continue

            marker = url_to_source.get(row.get("item_url", ""))
            if marker is None:
                unmatched += 1
            else:
                pub = split_publisher(marker)
                if pub is None:
                    no_publisher += 1
                else:
                    row["publisher"] = pub
                    pub_counter[pub] += 1
                    added += 1
            rows.append(row)

    stream.write(
        f"\n新增 publisher：{added} 筆／已有：{already} 筆／"
        f"來源無斜線（不需要）：{no_publisher} 筆／日報查無此 URL：{unmatched} 筆\n"
    )
    if pub_counter:
        stream.write(f"涵蓋出版者：{len(pub_counter)} 家，前 10：\n")
        for name, n in pub_counter.most_common(10):
            stream.write(f"  {n:>4}  {name}\n")

    if dry_run:
        stream.write("\n(--dry-run，未寫入)\n")
        stream.flush()
        return 0

    if added:
        with ATTRIBUTION.open("w", encoding="utf-8", newline="\n") as fh:
            for row in rows:
                if "__raw__" in row:
                    fh.write(row["__raw__"] + "\n")
                else:
                    fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        stream.write(f"\n已寫入 {ATTRIBUTION.relative_to(REPO_ROOT)}\n")
    else:
        stream.write("\n無需寫入（沒有新增任何 publisher）\n")
    stream.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
