#!/usr/bin/env python3
"""list_digest_omissions.py — 列出「抓到了但沒進日報」的條目，供 wiki ingest 補評估。

分層原則（2026-07-26 釐清）：

  - **日報是給讀者看的**，只留讀者需要讀的重點，**可以也應該篩選**
  - **wiki 是沉澱層，要考慮全部**——收不收由記者依各自類別規則判斷，
    但「沒被看到」和「看過後判斷不收」是兩回事

因此日報的篩選不該連帶讓 wiki 失明。本腳本把兩者的差集列出來，作為 wiki ingest
分類階段的補充輸入。

背景：2026-07-25 抓料 73 則、日報收 38 則，其餘 35 則（含 61 留言與 47 留言的
GitHub Issue）因為 wiki ingest 的輸入只有日報，從此沒有任何記者看過。當時誤判為
「日報漏收」而加了覆蓋率閘，後經釐清：日報篩選是對的，錯的是 wiki 的輸入來源。

**本腳本永遠不擋流程**（只有讀取失敗才回非 0），它的產出是要餵給記者的資料。

用法：
    python scripts/list_digest_omissions.py --date 2026-07-25
    python scripts/list_digest_omissions.py --date 2026-07-25 --json
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _use_utf8_stdout() -> None:
    """Windows 主控台預設 cp950，印不出中文/符號會 UnicodeEncodeError。

    只在直接執行時呼叫，**不可**放在模組層級：本檔會被測試 import，模組層級換掉
    sys.stdout 會連帶關掉 unittest runner 的輸出流（實際踩過：
    `ValueError: I/O operation on closed file`）。
    """
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def find_omissions(gathered: dict, digest_text: str) -> list[dict]:
    """回傳 gathered 中未出現於日報的條目，依互動分數由高到低。純函式，供測試呼叫。"""
    items = gathered.get("items") or []
    missing = [it for it in items if it.get("url") and it["url"] not in digest_text]
    return sorted(missing, key=lambda x: -(x.get("score") or 0))


def render(gathered: dict, omissions: list[dict]) -> list[str]:
    total = len(gathered.get("items") or [])
    covered = total - len(omissions)
    lines = [f"# 日報未收錄條目（{len(omissions)} 則；日報收錄 {covered}/{total}）", ""]
    if not omissions:
        lines.append("（無——本日抓到的條目全部進了日報）")
        return lines
    lines += [
        "以下條目抓到了但未進日報。日報只留讀者要讀的重點，這是預期行為；",
        "但 wiki 沉澱要考慮全部，因此這批也要納入分類與派工，",
        "由各類別記者依自己的收錄門檻判斷收不收——**不收可以，沒看過不行**。",
        "",
    ]
    for it in omissions:
        score = f"{it.get('score', 0)}{it.get('score_unit', '')}"
        lines.append(f"- **{it.get('title', '')}**")
        lines.append(f"  - 來源：{it.get('source', '?')}｜互動：{score}｜{it.get('url', '')}")
        summary = (it.get("summary") or "").strip().replace("\n", " ")
        if summary:
            lines.append(f"  - 摘要：{summary[:400]}")
    return lines


def main() -> int:
    _use_utf8_stdout()
    p = argparse.ArgumentParser()
    p.add_argument("--date", help="YYYY-MM-DD，推導出 news/<date>.md 與原料檔")
    p.add_argument("--digest")
    p.add_argument("--gathered")
    p.add_argument("--json", action="store_true", help="輸出 JSON 陣列而非 Markdown")
    args = p.parse_args()

    digest_path = Path(args.digest) if args.digest else REPO_ROOT / "news" / f"{args.date}.md"
    if args.gathered:
        gathered_path = Path(args.gathered)
    else:
        # 優先用當日原料副本：補跑時 gathered_items.json 可能已被其他日期覆寫
        archived = REPO_ROOT / "src" / "gathered_archive" / f"{args.date}.json"
        gathered_path = archived if archived.exists() else REPO_ROOT / "src" / "gathered_items.json"

    try:
        gathered = json.loads(gathered_path.read_text(encoding="utf-8"))
        text = digest_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"讀取失敗：{e}")
        return 3

    omissions = find_omissions(gathered, text)
    if args.json:
        print(json.dumps(omissions, ensure_ascii=False, indent=2))
    else:
        print("\n".join(render(gathered, omissions)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
