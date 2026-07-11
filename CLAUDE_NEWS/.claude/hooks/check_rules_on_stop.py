"""
Stop hook: 收工前檢查是否有「未驗證的規則改動」。

三層防線的第二層（第一層：check_rule_modified.py 的 dirty-period 預告；
第三層：run_tests.py 的 DoD 兜底），三者共用 `.claude/.last-rules-check`
記號檔（scripts/check_rules.py 全綠時寫入）。

行為：
- 掃描 .claude/commands/*.md、.claude/rules/*.md、根目錄 CLAUDE.md 的 mtime
- 任一檔案 mtime > .last-rules-check 的 mtime（或記號檔不存在）→ 輸出
  {"decision": "block", "reason": "..."} 要求先跑 check_rules.py
- 防無限迴圈：stdin JSON 的 stop_hook_active 為 true（已在 block 後的續跑中）
  → 無條件放行
- 任何錯誤 → 放行（Stop hook 壞掉不可把使用者卡死）
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HOOK_DIR = Path(__file__).resolve().parent   # .claude/hooks
CLAUDE_DIR = HOOK_DIR.parent                 # .claude
REPO_ROOT = CLAUDE_DIR.parent                # repo root（CLAUDE_NEWS）
LAST_CHECK = CLAUDE_DIR / ".last-rules-check"

BLOCK_REASON = (
    "偵測到規則檔改動尚未通過 check_rules.py 驗證，"
    "請執行 python scripts/check_rules.py（零錯誤後會自動重置此檢查）"
)


def rule_files():
    yield from (CLAUDE_DIR / "commands").glob("*.md")
    yield from (CLAUDE_DIR / "rules").glob("*.md")
    root_claude = REPO_ROOT / "CLAUDE.md"
    if root_claude.exists():
        yield root_claude


def has_unverified_changes() -> bool:
    if not LAST_CHECK.exists():
        # 從未綠檢過：只要有任何規則檔存在就視為未驗證
        return any(True for _ in rule_files())
    last_check_mtime = LAST_CHECK.stat().st_mtime
    return any(f.stat().st_mtime > last_check_mtime for f in rule_files())


def main() -> int:
    try:
        try:
            data = json.load(sys.stdin)
        except (json.JSONDecodeError, OSError):
            data = {}

        if data.get("stop_hook_active"):
            return 0  # 已在 block 後的續跑中，不可再 block（防無限迴圈）

        if has_unverified_changes():
            print(json.dumps({"decision": "block", "reason": BLOCK_REASON}, ensure_ascii=False))
        return 0
    except Exception:
        return 0  # 出錯放行


if __name__ == "__main__":
    sys.exit(main())
