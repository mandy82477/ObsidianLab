#!/usr/bin/env python3
"""
run_tests.py — 執行 src/tests/ 下所有確定性單元測試（unittest discover）。

只用標準庫，不依賴 pytest 或任何第三方套件。

用法：
    python scripts/run_tests.py

行為：
    全部通過 → exit 0
    任何失敗／錯誤 → 印出失敗案例清單，exit 1

供 news-pipeline-steps.md Step 4（建置 Web Reader）前置檢查呼叫：
測試失敗時視同 Step 4 失敗，跳過 web build 與 web commit。

跑完 unittest 全數通過後，另外執行 scripts/check_rules.py（.claude/commands、
.claude/rules 的規則一致性機械檢查）、scripts/check_arch_docs.py（架構文件
來源清單/日期/charset/CSS token 漂移檢查）、scripts/check_weekly_ledger.py
（週報預告帳本：漏收/判準遭改寫/殭屍條目/跳期）、scripts/check_wiki_freshness.py
（頁面「最後新聞更新」宣稱 × 歸因記錄交叉比對：漏更/無從對照/欄位缺失）、
scripts/check_feature_radar.py（feature-radar 當月詳細條目 ↔ 全覽表列對帳）與
scripts/check_pending_markers.py（懸置標記語法：日期/符號對應/排版/探針品質/
wikilink 目標存在/⟨Q-nn⟩ 雙向對帳）與 scripts/check_workflow_paths.py（GH Actions
workflow 指名的產出路徑逐一驗存在，防 2026-09-04 那種「刪了檔沒刪登記 → git add
exit 128 → 當天抓料整包不落地」）；任一失敗都會讓本腳本整體 exit 1。
"""
import io
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
CHECK_RULES = REPO_ROOT / "scripts" / "check_rules.py"
CHECK_ARCH_DOCS = REPO_ROOT / "scripts" / "check_arch_docs.py"
CHECK_WEEKLY_LEDGER = REPO_ROOT / "scripts" / "check_weekly_ledger.py"
CHECK_WIKI_FRESHNESS = REPO_ROOT / "scripts" / "check_wiki_freshness.py"
CHECK_FEATURE_RADAR = REPO_ROOT / "scripts" / "check_feature_radar.py"
CHECK_PENDING_MARKERS = REPO_ROOT / "scripts" / "check_pending_markers.py"
CHECK_TOOLS_PAGE = REPO_ROOT / "scripts" / "check_tools_page.py"
CHECK_HIERARCHY = REPO_ROOT / "scripts" / "check_hierarchy.py"
CHECK_WORKFLOW_PATHS = REPO_ROOT / "scripts" / "check_workflow_paths.py"


def main() -> int:
    # Windows 預設 console/file 編碼常是 cp950，日報與 wiki fixture 含大量中文
    # 與 emoji，非 UTF-8 環境下讀檔／print 會壞掉，故此處手動包一層 UTF-8 stream，
    # 不依賴 PYTHONUTF8 環境變數（設定它對已啟動的直譯器 stdout 編碼無效）。
    if hasattr(sys.stdout, "buffer"):
        stream = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    else:
        stream = sys.stdout

    if str(SRC_DIR) not in sys.path:
        sys.path.insert(0, str(SRC_DIR))

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(SRC_DIR / "tests"), pattern="test_*.py", top_level_dir=str(SRC_DIR))

    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)

    unit_ok = result.wasSuccessful()
    if unit_ok:
        stream.write(f"\nOK: {result.testsRun} 個測試案例全數通過\n")
    else:
        stream.write(f"\nFAILED: {len(result.failures)} 個失敗、{len(result.errors)} 個錯誤（共 {result.testsRun} 個案例）\n")
        for test, _ in result.failures:
            stream.write(f"  FAIL: {test}\n")
        for test, _ in result.errors:
            stream.write(f"  ERROR: {test}\n")
    stream.flush()

    # 規則一致性機械檢查（commands / rules 的裸露引用、路徑存在性、錨點、同步配對）
    rules_ok = True
    if CHECK_RULES.exists():
        proc = subprocess.run([sys.executable, str(CHECK_RULES)], capture_output=True, text=True, encoding="utf-8", errors="replace")
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        rules_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_RULES} 不存在，跳過規則一致性檢查\n")
    stream.flush()

    # 架構文件漂移機械檢查（來源清單 / 日期三處同步 / charset / CSS token）
    arch_docs_ok = True
    if CHECK_ARCH_DOCS.exists():
        proc = subprocess.run(
            [sys.executable, str(CHECK_ARCH_DOCS)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        arch_docs_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_ARCH_DOCS} 不存在，跳過架構文件漂移檢查\n")
    stream.flush()

    # 週報預告帳本一致性（漏收 / 判準遭改寫 / 殭屍條目 / 跳期 / 條數與查證線索）
    weekly_ledger_ok = True
    if CHECK_WEEKLY_LEDGER.exists():
        proc = subprocess.run(
            [sys.executable, str(CHECK_WEEKLY_LEDGER)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        weekly_ledger_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_WEEKLY_LEDGER} 不存在，跳過週報帳本檢查\n")
    stream.flush()

    # wiki 新鮮度宣稱 × 歸因記錄交叉比對（漏更 / 無從對照 / 缺欄位）
    freshness_ok = True
    if CHECK_WIKI_FRESHNESS.exists():
        proc = subprocess.run(
            [sys.executable, str(CHECK_WIKI_FRESHNESS)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        freshness_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_WIKI_FRESHNESS} 不存在，跳過 wiki 新鮮度檢查\n")
    stream.flush()

    # feature-radar 索引層對帳（當月詳細條目 ↔ 全覽表列）
    radar_ok = True
    if CHECK_FEATURE_RADAR.exists():
        proc = subprocess.run(
            [sys.executable, str(CHECK_FEATURE_RADAR)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        radar_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_FEATURE_RADAR} 不存在，跳過 feature-radar 對帳\n")
    stream.flush()

    # 懸置標記語法檢查（日期/符號對應/排版/探針品質/wikilink 目標存在/⟨Q-nn⟩ 雙向對帳）
    pending_ok = True
    if CHECK_PENDING_MARKERS.exists():
        proc = subprocess.run(
            [sys.executable, str(CHECK_PENDING_MARKERS)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        pending_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_PENDING_MARKERS} 不存在，跳過懸置標記語法檢查\n")
    stream.flush()

    # tools 決策表契約（數字帶日期／首選唯一——2026-09-02 改版的兩個讀者承諾）
    tools_ok = True
    if CHECK_TOOLS_PAGE.exists():
        proc = subprocess.run(
            [sys.executable, str(CHECK_TOOLS_PAGE)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        tools_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_TOOLS_PAGE} 不存在，跳過 tools 決策表契約檢查\n")
    stream.flush()

    # 子故事階層契約（2026-09-03：扁平／上層有效／領域繼承／archive 掛父／hub 不落後／index 投影）
    hierarchy_ok = True
    if CHECK_HIERARCHY.exists():
        proc = subprocess.run(
            [sys.executable, str(CHECK_HIERARCHY)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        hierarchy_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_HIERARCHY} 不存在，跳過階層契約檢查\n")
    stream.flush()

    # workflow 指名路徑存在性（2026-09-04：刪頁漏刪 git add 登記 → 抓料整包不落地）
    workflow_paths_ok = True
    if CHECK_WORKFLOW_PATHS.exists():
        proc = subprocess.run(
            [sys.executable, str(CHECK_WORKFLOW_PATHS)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write("\n" + (proc.stdout or "") + "\n")
        if proc.stderr:
            stream.write(proc.stderr + "\n")
        workflow_paths_ok = proc.returncode == 0
    else:
        stream.write(f"\nWARN: {CHECK_WORKFLOW_PATHS} 不存在，跳過 workflow 路徑檢查\n")
    stream.flush()

    return 0 if (unit_ok and rules_ok and arch_docs_ok and weekly_ledger_ok
                 and freshness_ok and radar_ok and pending_ok and tools_ok and hierarchy_ok
                 and workflow_paths_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
