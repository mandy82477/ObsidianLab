#!/usr/bin/env python3
"""check_digest_coverage.py — 日報收錄完整性檢查。

日報的定位是「留原始資料給人看」，過濾與精煉是 wiki 記者的職責（見根目錄
`CLAUDE.md`）。因此 `gathered_items.json` 裡的條目原則上都該出現在日報的對應
區塊裡，只有極少數重複或明顯無關的可以略過。

2026-07-25 出現回歸：抓料 73 則、日報只收 38 則（漏 48%），漏掉的包含 61 留言與
47 留言的 GitHub Issue。前一天同樣流程只漏 2/63（3%）。推測是當日改版把「選材
門檻」區塊搬到檔尾後，該門檻被理解成整份日報的收錄門檻，而非只用於挑選
「📌 今日聚焦」那 3–5 條導讀。

措辭修得再清楚都可能再被讀歪，所以改用機械檢查把關：比對 gathered 的 URL 有多少
真的出現在日報裡，低於門檻就要求重寫。

用法：
    python scripts/check_digest_coverage.py --date 2026-07-25
    python scripts/check_digest_coverage.py --digest news/x.md --gathered src/gathered_items.json

退出碼：
    0 = 通過（或僅警示）
    2 = 覆蓋率不足，呼叫端必須補齊遺漏條目後重檢
    3 = 檔案讀不到／格式不對
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FAIL_RATIO = 0.90   # 低於九成視為漏收，必須補
WARN_RATIO = 0.97   # 九成七以下提醒，但不擋

def _use_utf8_stdout() -> None:
    """Windows 主控台預設 cp950，印不出 ✅／⚠️ 會 UnicodeEncodeError。

    只在直接執行時呼叫，**不可**放在模組層級：本檔會被測試 import，模組層級換掉
    sys.stdout 會連帶關掉 unittest runner 的輸出流（實際踩過：
    `ValueError: I/O operation on closed file`）。
    """
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def evaluate(gathered: dict, digest_text: str) -> tuple[int, list[str], list[dict]]:
    """回傳 (exit_code, 訊息列, 遺漏條目列)。純函式，供測試直接呼叫。"""
    items = gathered.get("items") or []
    if not items:
        return 3, ["❌ gathered_items 沒有任何條目，無法檢查覆蓋率"], []

    missing = [it for it in items if it.get("url") and it["url"] not in digest_text]
    covered = len(items) - len(missing)
    ratio = covered / len(items)
    msgs = [f"收錄 {covered}/{len(items)}（{ratio:.0%}）"]

    if ratio < FAIL_RATIO:
        msgs.append(f"❌ 覆蓋率低於 {FAIL_RATIO:.0%}——日報的定位是留原始資料，"
                    f"過濾是 wiki 的職責，不可在此階段大量篩掉")
        msgs.append("   → 把下列條目補進對應區塊後重檢（選材門檻只用於挑選"
                    "「📌 今日聚焦」的 3–5 條導讀，不是整份日報的收錄門檻）")
        code = 2
    elif ratio < WARN_RATIO:
        msgs.append(f"⚠️ 覆蓋率 {ratio:.0%} 略低，確認遺漏的是重複或明顯無關的條目")
        code = 0
    else:
        msgs.append("✅ 收錄完整")
        code = 0

    if missing and code != 0:
        for it in sorted(missing, key=lambda x: -(x.get("score") or 0))[:20]:
            score = f"{it.get('score', 0)}{it.get('score_unit', '')}"
            msgs.append(f"   - [{score}] {it.get('source', '?')[:24]} | {it.get('title', '')[:70]}")
        if len(missing) > 20:
            msgs.append(f"   …另有 {len(missing) - 20} 則")
    return code, msgs, missing


def main() -> int:
    _use_utf8_stdout()
    p = argparse.ArgumentParser()
    p.add_argument("--date", help="YYYY-MM-DD，推導出 news/<date>.md")
    p.add_argument("--digest")
    p.add_argument("--gathered", default=str(REPO_ROOT / "src" / "gathered_items.json"))
    args = p.parse_args()

    digest_path = Path(args.digest) if args.digest else REPO_ROOT / "news" / f"{args.date}.md"
    try:
        gathered = json.loads(Path(args.gathered).read_text(encoding="utf-8"))
        text = digest_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"❌ 讀取失敗：{e}")
        return 3

    code, msgs, _ = evaluate(gathered, text)
    for m in msgs:
        print(m)
    return code


if __name__ == "__main__":
    sys.exit(main())
