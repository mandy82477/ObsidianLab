#!/usr/bin/env python3
r"""
check_workflow_paths.py — GitHub Actions workflow 裡指名的產出路徑，逐一驗存在。

為什麼要有這支（2026-09-04 事故）：
    09-03 的 commit「下架 site-source-tooling」刪了 wiki 頁面、也加了測試擋它回流，
    但漏刪 .github/workflows/daily-gather.yml 的 `git add` 登記。隔天排程跑到
    commit 步驟時 `git add` 撞到不存在的 pathspec，直接 exit 128 —— 抓料三個步驟
    全綠、資料卻整包沒落地，於是 news/2026-09-04.md 從未產生，而失敗訊息看起來
    像 git 的問題，不像「有人刪了一個檔」。

    當時的測試只驗「那頁不該存在」（單向），沒有任何東西驗「workflow 清單裡的每
    一筆都該存在」（反向）。本檢查器補的就是反向那半邊：**刪檔的人會在 commit 前
    就被擋下，而不是隔天由缺一天的日報來通知。**

檢查兩類寫法：
    1. `NAME_PATHS=( ... )` bash 陣列（daily-gather.yml 的 GATHER_PATHS 現行寫法）
    2. `git add a b \` 續行式的指名路徑（防有人改回舊寫法時失去看守）

另外擋下 `git add -A` / `git add .`——CLAUDE.md「commit 範圍」明訂任何情境不得使用。

用法：
    python scripts/check_workflow_paths.py

    全部存在 → exit 0；任一缺件或用了 -A/. → 列出並 exit 1。

只用標準庫（不 import yaml），與 run_tests.py 的其餘檢查器一致。
"""
import io
import re
import sys
from pathlib import Path

# 本腳本住 CLAUDE_NEWS/scripts/，workflow 住上一層的 .github/workflows/
PROJECT_ROOT = Path(__file__).resolve().parent.parent      # …/CLAUDE_NEWS
REPO_ROOT = PROJECT_ROOT.parent                            # …/ObsidianLab（workflow 的 working-directory）
WORKFLOW_DIR = REPO_ROOT / ".github" / "workflows"

ARRAY_OPEN_RE = re.compile(r"^\s*([A-Z_]+_PATHS)=\(\s*$")
ARRAY_CLOSE_RE = re.compile(r"^\s*\)\s*$")
GIT_ADD_RE = re.compile(r"^\s*git add\s+(.*)$")
BLANKET_ADD_RE = re.compile(r"^\s*git add\s+(-A\b|--all\b|\.\s*$)")
# 路徑長相：不含 shell 變數、萬用字元與引號的相對路徑
PLAIN_PATH_RE = re.compile(r"^[A-Za-z0-9._/-]+$")


def _record(findings, wf_name, lineno, path):
    findings.append((wf_name, lineno, path))


def collect(workflow: Path):
    """回傳 (paths, blankets)：paths 為 [(lineno, path)]，blankets 為 [(lineno, 原行)]。"""
    paths, blankets = [], []
    lines = workflow.read_text(encoding="utf-8").split("\n")
    in_array = False

    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()

        if in_array:
            if ARRAY_CLOSE_RE.match(line):
                in_array = False
            elif stripped and not stripped.startswith("#"):
                if PLAIN_PATH_RE.match(stripped):
                    paths.append((lineno, stripped))
            continue

        if ARRAY_OPEN_RE.match(line):
            in_array = True
            continue

        if BLANKET_ADD_RE.match(line):
            blankets.append((lineno, stripped))
            continue

        m = GIT_ADD_RE.match(line)
        if m:
            # 續行式：把 `git add a \` 之後的續行一併吃掉
            chunk = m.group(1)
            cursor = lineno
            while chunk.rstrip().endswith("\\") and cursor < len(lines):
                chunk = chunk.rstrip()[:-1]
                cursor += 1
                chunk += " " + lines[cursor - 1].strip()
            for token in chunk.split():
                if PLAIN_PATH_RE.match(token) and "/" in token:
                    paths.append((lineno, token))

    return paths, blankets


def main() -> int:
    # 與其餘檢查器同慣例：本檔輸出含中文，被 run_tests.py 以 subprocess 收集時
    # 若沿用 Windows 預設 locale（cp950）會讓母行程的 UTF-8 解碼失敗，
    # 連帶讓 proc.stdout 變成 None、整個測試套件崩潰（2026-09-05 踩過，擋掉當天建站）。
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    if not WORKFLOW_DIR.is_dir():
        print(f"WARN: {WORKFLOW_DIR} 不存在，跳過 workflow 路徑檢查")
        return 0

    missing, blanket_hits, checked = [], [], 0

    for workflow in sorted(WORKFLOW_DIR.glob("*.yml")):
        paths, blankets = collect(workflow)
        for lineno, line in blankets:
            blanket_hits.append((workflow.name, lineno, line))
        for lineno, rel in paths:
            checked += 1
            if not (REPO_ROOT / rel).exists():
                _record(missing, workflow.name, lineno, rel)

    if not missing and not blanket_hits:
        print(f"OK: workflow 指名路徑 {checked} 筆全數存在，無 git add -A/.")
        return 0

    if missing:
        print(f"FAIL: workflow 指名了 {len(missing)} 個不存在的路徑"
              f"（git add 會 exit 128，讓當天抓料整包不落地）：")
        for wf, lineno, rel in missing:
            print(f"  {wf}:{lineno}  {rel}")
        print("  → 刪檔時一併刪掉 workflow 的登記；或該檔本就該存在 → 查為何消失")
    if blanket_hits:
        print(f"FAIL: workflow 使用了 git add -A / git add .（CLAUDE.md「commit 範圍」明訂禁止）：")
        for wf, lineno, line in blanket_hits:
            print(f"  {wf}:{lineno}  {line}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
