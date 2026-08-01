#!/usr/bin/env python3
"""開放迴路掃描——每週跑一次，把「悄悄沒收尾」的東西攤出來。

檢查兩類開放迴路：
  1. 未 commit 的「實質改動」（code / 規則 / wiki / 腳本），排除每日變動的 data 檔
  2. `docs/workaround-register.md`「進行中」表格裡逾複查日的 workaround

不呼叫任何 LLM，純本地 git + 檔案解析（符合本專案無 API key 前提）。
用法：python scripts/open_loops.py
"""
import io
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

# Windows 主控台預設 cp950，印不出 ⚠️ 會 UnicodeEncodeError——而這個腳本正是「有逾期
# workaround 時才印 ⚠️」，等於愈該示警愈會當掉（2026-08-01 實際踩到：掃描在列出 4 筆
# 逾期項目的當下 traceback 中止）。與 cloud_bootstrap.py 用同一招把 stdout 轉 UTF-8。
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parent.parent          # CLAUDE_NEWS/
REGISTER = REPO / "docs" / "workaround-register.md"

# 與 SessionStart hook 一致的排除清單：每日正常變動的 data / 本機 junk / 父層
_EXCLUDE = re.compile(
    r"gathered_items\.json|emitted_items\.json|seen_urls\.json|"
    r"\.stackdump|settings\.local\.json|\.obsidian/|\.gitignore|\.canvas|smart-connections"
)


def uncommitted_real_changes() -> list[str]:
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
    except Exception as e:
        return [f"(git status 失敗：{e})"]
    return [ln for ln in out.splitlines() if ln.strip() and not _EXCLUDE.search(ln)]


def overdue_workarounds(today: date) -> list[str]:
    """回傳『進行中』表格中複查日 <= today 的列摘要。"""
    if not REGISTER.exists():
        return []
    text = REGISTER.read_text(encoding="utf-8")
    # 只看「## 進行中」到下一個 「## 」之間
    m = re.search(r"##\s*進行中\s*(.*?)(?:\n##\s|\Z)", text, re.S)
    if not m:
        return []
    overdue = []
    for line in m.group(1).splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("繞路內容", "---") or set(cells[0]) <= {"-", ":"}:
            continue
        d = re.search(r"(\d{4})-(\d{2})-(\d{2})", cells[3])
        if not d:
            continue
        due = date(int(d.group(1)), int(d.group(2)), int(d.group(3)))
        if due <= today:
            desc = cells[0][:60]
            overdue.append(f"複查日 {due.isoformat()}（逾 {(today - due).days} 天）：{desc}")
    return overdue


def main() -> int:
    today = date.today()
    changes = uncommitted_real_changes()
    overdue = overdue_workarounds(today)

    print(f"=== 開放迴路掃描（{today.isoformat()}）===\n")

    print(f"[1] 未 commit 的實質改動：{len(changes)} 個")
    for ln in changes:
        print(f"    {ln}")
    if not changes:
        print("    ✅ 無——實質改動都已收尾")

    print(f"\n[2] 逾複查日的 workaround：{len(overdue)} 個")
    for ln in overdue:
        print(f"    ⚠️ {ln}")
    if not overdue:
        print("    ✅ 無逾期繞路")

    open_count = len(changes) + len(overdue)
    print(f"\n=== 合計開放迴路：{open_count} 個 ===")
    return 1 if open_count else 0


if __name__ == "__main__":
    sys.exit(main())
