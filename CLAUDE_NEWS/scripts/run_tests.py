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
"""
import io
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"


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

    if result.wasSuccessful():
        stream.write(f"\nOK: {result.testsRun} 個測試案例全數通過\n")
        stream.flush()
        return 0

    stream.write(f"\nFAILED: {len(result.failures)} 個失敗、{len(result.errors)} 個錯誤（共 {result.testsRun} 個案例）\n")
    for test, _ in result.failures:
        stream.write(f"  FAIL: {test}\n")
    for test, _ in result.errors:
        stream.write(f"  ERROR: {test}\n")
    stream.flush()
    return 1


if __name__ == "__main__":
    sys.exit(main())
