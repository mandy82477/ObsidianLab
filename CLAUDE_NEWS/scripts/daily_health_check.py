#!/usr/bin/env python3
"""daily_health_check.py — 每日產出是否齊全的單一判準來源。

分裂架構有兩段（① GitHub Actions 抓料、② 雲端 routine 產日報/wiki/網站），
任一段失敗時系統本身不會喊。本腳本定義「今天到底算不算成功」，由兩個地方共用：

  - `.github/workflows/daily-watchdog.yml`（15:00 UTC）：失敗即 job 失敗 → GitHub 寄信
  - 雲端 routine `daily-watchdog-push`（23:00 UTC = 隔天 07:00 台北）：失敗才推播到手機

**判準只能有一份。** 這兩處原本各寫一套的話，遲早會出現「信說壞了、推播說好」的
狀況，那時你會兩邊都不信。所以邏輯放這裡，兩邊都只負責呼叫與呈現。

檢查四項：
  ① 抓料：`src/gathered_items.json` 的 date 是今天且 items 非空
  ② 日報：`news/YYYY-MM-DD.md` 存在
  ③ 網站：`web_reader/data/digest/YYYY-MM-DD.json` 存在
     —— 單獨檢查是因為「日報有、網站沒有」是真實會發生的半成品狀態
     （2026-07-31 就是這樣：日報與 wiki 都好，只有 web build 被跳過）
  ④ 近 7 天缺口：Step 0 只看昨天，連漏數天時要能一次看到全貌

用法：
    python scripts/daily_health_check.py                  # 人看的摘要
    python scripts/daily_health_check.py --format md      # GitHub job summary 用
    python scripts/daily_health_check.py --format push    # 一行推播訊息（<200 字元）
    python scripts/daily_health_check.py --date 2026-07-31

exit code：0 = 齊全，1 = 有缺件（近 7 天缺口只提示，不影響 exit code——
補歷史洞是另一件事，不該讓今天的告警一直紅著）。
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _use_utf8_stdout() -> None:
    """Windows 主控台預設 cp950，印不出 ✅／⚠️ 會 UnicodeEncodeError。

    **只在 `__main__` 路徑呼叫，不可放模組層級**——模組層級換掉 `sys.stdout` 會在
    本檔被 import 時連帶關掉呼叫端的輸出流（`run_tests.py` 用 unittest discover
    匯入本檔的測試後噴 `ValueError: I/O operation on closed file`，2026-08-01 實際
    踩到；同樣的坑 `cloud_bootstrap.py` 也記過一次）。
    """
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def check(target: date, repo: Path = REPO_ROOT) -> dict:
    d = target.isoformat()
    gathered = repo / "src" / "gathered_items.json"

    gather_date, gather_n = None, 0
    if gathered.exists():
        try:
            # encoding 明寫 utf-8：資料含中文，非 UTF-8 預設環境會讀失敗而誤報缺件
            data = json.loads(gathered.read_text(encoding="utf-8"))
            gather_date, gather_n = data.get("date"), len(data.get("items") or [])
        except (json.JSONDecodeError, OSError):
            pass

    digest_ok = (repo / "news" / f"{d}.md").exists()
    web_ok = (repo / "web_reader" / "data" / "digest" / f"{d}.json").exists()

    problems = []
    if gather_date != d or gather_n == 0:
        problems.append(("抓料", f"gathered_items.json date={gather_date} items={gather_n}（daily-gather 失敗或被 GitHub 丟棄）"))
    if not digest_ok:
        problems.append(("日報", f"news/{d}.md 不存在（雲端 routine 未執行、中止、或 push 失敗）"))
    elif not web_ok:
        # 只有在日報存在時才算「網站沒跟上」；日報本身就沒有的話，上面那條已經涵蓋
        problems.append(("網站", f"web_reader/data/digest/{d}.json 不存在——日報有但網站沒重建（多半是 web build gate 擋下）"))

    holes = []
    for i in range(1, 8):
        past = (target - timedelta(days=i)).isoformat()
        if not (repo / "news" / f"{past}.md").exists():
            replayable = (repo / "src" / "gathered_archive" / f"{past}.json").exists()
            holes.append({"date": past, "replayable": replayable})

    return {
        "date": d,
        "healthy": not problems,
        "gather_date": gather_date,
        "gather_n": gather_n,
        "digest_ok": digest_ok,
        "web_ok": web_ok,
        "problems": problems,
        "holes": holes,
    }


def render_md(r: dict) -> str:
    lines = [f"## 每日產出檢查 {r['date']} (UTC)"]
    if r["gather_date"] == r["date"] and r["gather_n"] > 0:
        lines.append(f"- ✅ ① 抓料：{r['gather_n']} 則")
    else:
        lines.append(f"- ❌ ① 抓料缺件：gathered_items.json date={r['gather_date']} items={r['gather_n']}（daily-gather 失敗或被 GitHub 丟棄）")
    lines.append(f"- ✅ ② 日報已上站：news/{r['date']}.md" if r["digest_ok"]
                 else f"- ❌ ② 日報缺件：news/{r['date']}.md 不存在（雲端 routine 未執行、中止、或 push 失敗）")
    if r["web_ok"]:
        lines.append("- ✅ ② web reader 已重建")
    elif r["digest_ok"]:
        lines.append(f"- ❌ ② 日報有但網站沒重建：web_reader/data/digest/{r['date']}.json 不存在（多半是 web build gate 擋下）")

    lines += ["", "### 近 7 天缺口"]
    if not r["holes"]:
        lines.append("- ✅ 近 7 天無缺口")
    for h in r["holes"]:
        if h["replayable"]:
            lines.append(f"- ⚠️ {h['date']} 缺日報（**有原料副本，可完整 replay 補回**：`/news-pipeline {h['date']}`）")
        else:
            lines.append(f"- ⚠️ {h['date']} 缺日報（無原料副本，只能重抓，內容會偏稀疏）")

    if not r["healthy"]:
        lines += ["", f"**補救**：本機執行 `/news-pipeline {r['date']}`（見 CLAUDE_NEWS/docs/daily-automation.md）"]
    return "\n".join(lines)


def render_push(r: dict) -> str:
    """一行推播訊息。開頭直接講哪一段壞了，讓通知列不用點開就能判斷要不要現在處理。"""
    if r["healthy"]:
        return f"每日新聞 {r['date']} 產出齊全"
    what = "、".join(p[0] for p in r["problems"])
    msg = f"每日新聞 {r['date']} 缺件：{what}。本機跑 /news-pipeline {r['date']} 補"
    if r["holes"]:
        msg += f"（另有近 7 天 {len(r['holes'])} 個舊缺口）"
    return msg[:200]


def main() -> int:
    _use_utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="檢查日期 YYYY-MM-DD，預設今日（UTC）")
    ap.add_argument("--format", choices=["text", "md", "push"], default="text")
    args = ap.parse_args()

    target = (datetime.strptime(args.date, "%Y-%m-%d").date() if args.date
              else datetime.now(timezone.utc).date())
    r = check(target)

    print(render_push(r) if args.format == "push" else render_md(r))
    return 0 if r["healthy"] else 1


if __name__ == "__main__":
    sys.exit(main())
