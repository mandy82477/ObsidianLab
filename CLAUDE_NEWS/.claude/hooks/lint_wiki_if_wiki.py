"""
PostToolUse hook: 只有被 Edit/Write 的檔案位於 wiki/ 下才執行 markdownlint-cli2。

取代 settings.local.json 原本無條件的 `markdownlint-cli2 "wiki/**/*.md" || true`
（改 Python / web 檔也 lint 整個 wiki，浪費且吵）。

行為：
- 讀 stdin JSON，取 tool_input.file_path
- 路徑不在 wiki/ 下 → 直接靜默 exit 0
- 在 wiki/ 下 → subprocess 跑 markdownlint-cli2（|| true 語意：無論 lint
  結果如何都 exit 0，只把輸出印出來供參考）
"""
import io
import json
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent  # .claude/hooks -> repo root

try:
    data = json.load(sys.stdin)
except (json.JSONDecodeError, OSError):
    sys.exit(0)

path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")

if "/wiki/" not in path and not path.startswith("wiki/"):
    sys.exit(0)

if not path.endswith(".md"):
    sys.exit(0)

try:
    proc = subprocess.run(
        ["markdownlint-cli2", "wiki/**/*.md"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=(sys.platform == "win32"),  # Windows 下 markdownlint-cli2 是 .cmd shim
        timeout=120,
    )
    if proc.stdout:
        print(proc.stdout)
    if proc.stderr:
        print(proc.stderr)
except (OSError, subprocess.TimeoutExpired):
    pass  # || true 語意：lint 工具缺失或逾時都不阻塞

sys.exit(0)
