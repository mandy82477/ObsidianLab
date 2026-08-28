#!/usr/bin/env python3
"""observe_large_reads.py — 大頁全讀觀察 hook（只記錄，不攔截）。

PreToolUse(Read)：目標為 wiki/ 或 news/ 下的 .md、未帶 limit、且檔案 > 400 行時，
append 一行到 src/logs/large_read_observations.log。**永遠 exit 0**——觀察模式，
任何內部錯誤一律放行（fail-open），不得影響流程。

背景（2026-08-28）：「>300 行先 Grep 再 offset/limit」是建議層規則，遵守是機率性的；
Read 工具預設可一次吞 2000 行，全庫最長頁 1628 行——機械層允許整頁全讀（單次
6–12 萬 token，靜默）。本 hook 先量測違規實際發生率，一至兩週後依記錄決定是否
升級為硬攔截（exit 2 擋下＋處方箋訊息）。升級判準：記錄多且皆屬「順手全讀」→
升級；出現正當全讀被記到煩 → 調閾值或維持觀察。
"""
import json
import sys
from datetime import datetime
from pathlib import Path

THRESHOLD_LINES = 400
PROJECT = Path(__file__).resolve().parents[2]
LOG = PROJECT / "src" / "logs" / "large_read_observations.log"


def main() -> int:
    try:
        data = json.load(sys.stdin)
        if data.get("tool_name") != "Read":
            return 0
        ti = data.get("tool_input") or {}
        fp = ti.get("file_path") or ""
        if ti.get("limit"):
            return 0
        p = Path(fp)
        try:
            rel = p.resolve().relative_to(PROJECT).as_posix()
        except Exception:
            return 0
        if not (rel.startswith(("wiki/", "news/")) and rel.endswith(".md")):
            return 0
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            lines = sum(1 for _ in f)
        if lines <= THRESHOLD_LINES:
            return 0
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        offset = ti.get("offset") or 0
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{stamp}\t{rel}\t{lines} 行\toffset={offset} limit=無\n")
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
