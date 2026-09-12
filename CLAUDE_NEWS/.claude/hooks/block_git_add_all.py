"""
PreToolUse hook: 擋下 `git add -A` / `git add --all` / `git add .`。

為什麼要用 hook 而不是只寫在規則裡：這條規則必須**每次都發生**，而規則文字只在
agent 剛好記得時生效。2026-08-29 一個訊息為「fix: 目標日期取自耐久的 gathered_archive」
的 commit 掃走了同時間另一份工作的四個 wiki 檔——當事 session 不是不知道規則，
是沒想到自己正在違反它。

行為：
- 讀 stdin JSON；tool_name 為 Bash／PowerShell 且 tool_input.command 命中全加樣式
  → stderr 印一句指回規則、exit 2（PreToolUse 的 exit 2 = 拒絕該次工具呼叫）
- 其餘一律 exit 0 放行
- 任何解析錯誤 → exit 0（hook 壞掉不可把使用者卡死）

命中樣式（`git add` 之後、任何旗標之間，出現裸 `.` / `-A` / `--all`）：
    git add -A          git add --all        git add .
    git add -A -- .     git add -v --all     git -C <path> add .
不命中：`git add wiki/`、`git add ./scripts/x.py`、`git add -p`、`git add --dry-run wiki/`、
    以及只在字串裡提到的字面（`git commit -m 'ban git add -A'`、`echo git add -A`、`grep 'git add .'`）
已知邊界（刻意不擋）：`git stage -A`；tool_name 非 Bash／PowerShell 的 shell 工具一律放行
"""
import io
import json
import re
import sys

sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

TOOLS = {"Bash", "PowerShell"}

# `git ... add` 之後的引數列；只看到下一個 `;` `&&` `||` `|` 為止。
# `git` 必須位於指令起點（行首／`;`／`&&`／`||`／`|`／`then`／`do`／`$(`／反引號之後），
# 句中字面（commit 訊息、echo、grep 的引數）不命中。
ADD_RE = re.compile(
    r"(?:^|[;&|\n(`]|\bthen\b|\bdo\b)\s*"
    r"\bgit\b(?P<pre>(?:\s+-[-\w]+(?:=\S+)?|\s+-C\s+\S+)*)\s+add\b(?P<args>[^;&|\n)`]*)"
)
ALL_TOKEN_RE = re.compile(r"(?:^|\s)(?:-A|--all|\.)(?:\s|$)")

REASON = (
    "🚫 擋下 `git add -A` / `git add --all` / `git add .`。\n"
    "本專案一律指名路徑（如 `git add wiki/ .claude/`）——commit 訊息說不出某個檔案"
    "為什麼在裡面，它就不該在這個 commit 裡。\n"
    "規則與立法依據：根目錄 CLAUDE.md「commit 範圍」＋ docs/rules-changelog/CLAUDE.md 2026-08-29。"
)


def is_add_all(command: str) -> bool:
    for m in ADD_RE.finditer(command):
        if ALL_TOKEN_RE.search(m.group("args")):
            return True
    return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if payload.get("tool_name") not in TOOLS:
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if not isinstance(command, str) or not is_add_all(command):
        return 0
    sys.stderr.write(REASON + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
