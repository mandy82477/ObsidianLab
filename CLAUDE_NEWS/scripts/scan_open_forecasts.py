"""把當日日報掃一遍，找出可能與「未結案週報預告」相關的條目。

週報第 (3) 段是一本可證偽預告的帳，回收發生在一週後。若回收時才憑記憶重讀七天日報，
漏收幾乎是必然的（2026-W31 實際漏了三條）。這支腳本把偵測前移到每天：日報寫完後，
用未結案預告判準裡的「｜查證：關鍵字」對當日內容做字串比對，命中就記一行到
`weekly/open-signals.jsonl`，下期 /weekly-report 直接讀這個檔。

三條刻意的設計界線：

1. **只偵測，不判定** —— 命中只代表「這裡可能有動靜」，是否算命中判準由週報的人／LLM 決定。
2. **只讀不寫日報** —— 不修改 news/，不影響當日產出；失敗只記錄不阻斷 pipeline。
3. **必須在選材之後執行** —— 若選材階段知道週報正在賭什麼，會產生確認偏誤（選材傾向撿
   能證實預告的條目），命中率虛高，並破壞每月聚焦校準的獨立性（校準量測的正是選材品質，
   兩者不得互相知情）。呼叫點固定在 `.claude/commands/news-pipeline-steps.md` Step 3e。

用法：
    python scripts/scan_open_forecasts.py 2026-08-02
    （省略日期則用 news/ 內最新一份日報）
"""

from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WEEKLY_DIR = REPO_ROOT / "weekly"
NEWS_DIR = REPO_ROOT / "news"
SIGNALS_PATH = WEEKLY_DIR / "open-signals.jsonl"

RECAP_HEADER_RE = re.compile(r"^\|\s*上週預告\s*\|\s*判準\s*\|\s*本週結果\s*\|\s*$", re.MULTILINE)
FORECAST_HEADER_RE = re.compile(r"^\|\s*類型\s*\|\s*預告\s*\|\s*判準\s*\|\s*$", re.MULTILINE)
SEPARATOR_RE = re.compile(r"^\|[-: |]+\|$")
PROBE_RE = re.compile(r"｜\s*查證[：:]\s*(.+?)\s*$")
OPEN_MARKS = ("⏳", "🟡", "⏰")

# 日報條目：標題行為 **[標題](url)**，其後為說明句
ENTRY_RE = re.compile(r"^\*\*\[(.+?)\]\((https?://[^)]+)\)\*\*", re.MULTILINE)


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def _strip_bold(text: str) -> str:
    return re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text).strip()


def _parse_table(body: str, header_re: re.Pattern) -> list[list[str]]:
    m = header_re.search(body)
    if not m:
        return []
    rows, started = [], False
    for line in body[m.end():].splitlines():
        ls = line.strip()
        if not ls.startswith("|"):
            if started:
                break
            continue
        if SEPARATOR_RE.match(ls):
            started = True
            continue
        if not started:
            continue
        cells = [_strip_bold(c.strip()) for c in ls.strip("|").split("|")]
        if len(cells) >= 3:
            rows.append(cells)
    return rows


def open_forecasts() -> tuple[str, list[dict]]:
    """最新一期週報中仍未結案的預告：本期新立的（全部）＋回收表中標記未結案的。"""
    files = sorted(WEEKLY_DIR.glob("[0-9][0-9][0-9][0-9]-W[0-9][0-9].md"))
    if not files:
        return "", []
    latest = files[-1]
    raw = latest.read_text(encoding="utf-8-sig")
    items: list[dict] = []

    for row in _parse_table(raw, FORECAST_HEADER_RE):
        items.append({"forecast": row[1], "criterion": row[2], "origin": "新立"})
    for row in _parse_table(raw, RECAP_HEADER_RE):
        if row[2].startswith(OPEN_MARKS):
            items.append({"forecast": row[0], "criterion": row[1], "origin": "續盯"})

    for it in items:
        m = PROBE_RE.search(it["criterion"])
        it["probes"] = [p.strip() for p in re.split(r"[、,，]", m.group(1)) if p.strip()] if m else []
    return latest.stem, items


def scan(digest_path: Path, week_id: str, items: list[dict]) -> list[dict]:
    raw = digest_path.read_text(encoding="utf-8-sig")
    lowered = raw.lower()
    entries = [(m.group(1), m.group(2)) for m in ENTRY_RE.finditer(raw)]
    hits: list[dict] = []

    for it in items:
        for probe in it["probes"]:
            if probe.lower() not in lowered:
                continue
            # 找出實際包含該關鍵字的條目標題（找不到就只記關鍵字命中）
            matched = [
                {"title": t, "url": u} for t, u in entries if probe.lower() in t.lower()
            ][:3]
            hits.append({
                "date": digest_path.stem,
                "week": week_id,
                "forecast": it["forecast"],
                "origin": it["origin"],
                "probe": probe,
                "entries": matched,
            })
    return hits


def main() -> int:
    out = _stdout()
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if target:
        digest = NEWS_DIR / f"{target}.md"
    else:
        candidates = sorted(NEWS_DIR.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md"))
        digest = candidates[-1] if candidates else None

    if not digest or not digest.exists():
        print(f"  略過：找不到日報 {digest}", file=out)
        out.flush()
        return 0

    week_id, items = open_forecasts()
    if not items:
        print("  略過：weekly/ 無未結案預告", file=out)
        out.flush()
        return 0

    no_probe = [it["forecast"] for it in items if not it["probes"]]
    hits = scan(digest, week_id, items)

    if hits:
        WEEKLY_DIR.mkdir(exist_ok=True)
        with SIGNALS_PATH.open("a", encoding="utf-8") as fh:
            for h in hits:
                fh.write(json.dumps(h, ensure_ascii=False) + "\n")

    print(f"# scan_open_forecasts.py（{digest.stem} ← {week_id}）\n", file=out)
    print(f"  未結案預告 {len(items)} 條，命中 {len(hits)} 筆" +
          (f"，已 append 至 {SIGNALS_PATH.relative_to(REPO_ROOT)}" if hits else ""), file=out)
    for h in hits:
        title = h["entries"][0]["title"][:52] if h["entries"] else "（關鍵字出現於內文，非標題）"
        print(f"    · 「{h['forecast'][:28]}」← 查證「{h['probe']}」：{title}", file=out)
    if no_probe:
        for f in no_probe:
            print(f"  ⚠️ 無查證線索，無法偵測：「{f[:40]}」", file=out)
    out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
