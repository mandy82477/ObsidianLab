"""
PostToolUse hook: 偵測 .claude/commands/、.claude/rules/、CLAUDE.md 是否被修改。

dirty-period 提醒機制（每個「dirty 期間」只提醒一次，不逐次轟炸）：
- `.claude/.last-rules-check`：scripts/check_rules.py 全綠時寫入的時間戳（上次綠檢）
- `.claude/.rules-reminder-sent`：本 dirty 期間已提醒過的記號（本 hook touch）

判斷：`.rules-reminder-sent` 不存在、或其 mtime 早於 `.last-rules-check` 的 mtime
（表示綠檢之後這是第一次改規則檔）→ 印提醒 + touch `.rules-reminder-sent`；
否則沉默。任何 IO 失敗 fallback 成印提醒（寧可吵不可漏）。
"""
import io
import json
import re
import sys
from pathlib import Path

# 強制 UTF-8 輸出，避免 Windows CP950 編碼問題
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HOOK_DIR = Path(__file__).resolve().parent          # .claude/hooks
CLAUDE_DIR = HOOK_DIR.parent                        # .claude
LAST_CHECK = CLAUDE_DIR / ".last-rules-check"       # 上次綠檢（check_rules.py 寫入）
REMINDER_SENT = CLAUDE_DIR / ".rules-reminder-sent" # 本 dirty 期間已提醒

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")

WATCH_PATTERNS = [
    r"\.claude/commands/",
    r"\.claude/rules/",
    r"/CLAUDE\.md$",
    r"^CLAUDE\.md$",
]


def should_remind() -> bool:
    """本 dirty 期間尚未提醒過才回 True；IO 失敗一律回 True（寧可吵不可漏）。"""
    try:
        if not REMINDER_SENT.exists():
            return True
        if not LAST_CHECK.exists():
            # 從未綠檢過，但已提醒過 → 沉默（仍在同一個 dirty 期間）
            return False
        return REMINDER_SENT.stat().st_mtime < LAST_CHECK.stat().st_mtime
    except OSError:
        return True


if any(re.search(p, path) for p in WATCH_PATTERNS):
    if should_remind():
        filename = path.split("/")[-1]
        print(f"[RULE MODIFIED] {filename}")
        print("-> 修改前請先讀取 .claude/rules/claude-md-edit.md")
        print("-> 改完跑 python scripts/check_rules.py 快速自檢；commit 前 run_tests.py 會強制驗證")
        print("（本輪 dirty 期間只提醒這一次，綠檢後重置）")
        sys.stdout.flush()
        try:
            REMINDER_SENT.touch()  # 已存在時 Path.touch() 會更新 mtime
        except OSError:
            pass
