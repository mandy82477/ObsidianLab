"""
PostToolUse hook: 偵測 .claude/commands/、.claude/rules/、CLAUDE.md 是否被修改。
若是，輸出提示要求執行 /review-commands。
"""
import io
import json
import re
import sys

# 強制 UTF-8 輸出，避免 Windows CP950 編碼問題
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")

WATCH_PATTERNS = [
    r"\.claude/commands/",
    r"\.claude/rules/",
    r"/CLAUDE\.md$",
    r"^CLAUDE\.md$",
]

if any(re.search(p, path) for p in WATCH_PATTERNS):
    filename = path.split("/")[-1]
    print(f"[RULE MODIFIED] {filename}")
    print("-> 下次修改前請先讀取 .claude/rules/claude-md-edit.md")
    print("-> 修改完成後執行 /review-commands，直到零錯誤為止。")
    sys.stdout.flush()
