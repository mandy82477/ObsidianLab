"""web build gate 的放行判斷測試。

背景：2026-07-31 雲端日更因 3 個 `ModuleNotFoundError: No module named
'feedparser_sgmllib'` 判定測試失敗，依「整包測試過才建 web」的舊 gate 跳過
web build，網站整天停在前一天——但那 3 個案例是抓料端依賴，跟 build_web.py
的輸入毫無關係。gate_web_build.py 就是為了拆掉這個過緊的耦合。

這支測試的重點不是「放行邏輯會不會動」，而是**它會不會放行過頭**：
允許清單一旦變成橡皮圖章，這層 gate 就等於沒有。
"""
import json
import unittest
from datetime import date
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from gate_web_build import evaluate, load_gaps, parse_failures  # noqa: E402

GAPS_FILE = Path(__file__).resolve().parent.parent.parent / "docs" / "known-test-gaps.json"

GAPS = [
    {
        "id": "feedparser-sgmllib",
        "test": r"^test_(blogroll|source_funnel)\b",
        "error": "No module named 'feedparser",
        "register_row": "雲端 sandbox 缺 feedparser 依賴鏈",
        "review_date": "2026-08-08",
    }
]

# 重現 2026-07-31 現場的 run_tests.py 輸出
OUTPUT_KNOWN = """
FAILED: 0 個失敗、2 個錯誤（共 121 個案例）
  ERROR: test_blogroll (news_aggregator.tests.test_blogroll.TestBlogroll)
  ERROR: test_source_funnel (news_aggregator.tests.test_source_funnel.TestFunnel)
ModuleNotFoundError: No module named 'feedparser_sgmllib'
"""

OUTPUT_MIXED = OUTPUT_KNOWN + "\n  FAIL: test_digest_contract (tests.test_digest_contract.TestContract)\n"

OUTPUT_RULES_ONLY = """
OK: 144 個測試案例全數通過
狀態：❌ check_rules.py 發現 2 組同步配對不一致
"""


class TestParseFailures(unittest.TestCase):
    def test_picks_up_both_fail_and_error(self):
        self.assertEqual(len(parse_failures(OUTPUT_MIXED)), 3)

    def test_green_output_has_no_failures(self):
        self.assertEqual(parse_failures("OK: 144 個測試案例全數通過"), [])


class TestEvaluate(unittest.TestCase):
    def test_green_always_allows(self):
        r = evaluate("OK: 144 個測試案例全數通過", 0, [])
        self.assertTrue(r["allow"])
        self.assertEqual(r["reason"], "tests_green")

    def test_known_gap_allows_build(self):
        """07-31 現場：全部失敗都屬已登記缺口 → 網站該照常更新。"""
        r = evaluate(OUTPUT_KNOWN, 1, GAPS, today=date(2026, 8, 1))
        self.assertTrue(r["allow"])
        self.assertEqual(len(r["matched"]), 2)
        self.assertEqual(r["unmatched"], [])

    def test_one_unknown_failure_blocks_everything(self):
        """混入一個沒登記的失敗 → 整批擋下。gate 的存在意義在這一條。"""
        r = evaluate(OUTPUT_MIXED, 1, GAPS, today=date(2026, 8, 1))
        self.assertFalse(r["allow"])
        self.assertEqual(len(r["unmatched"]), 1)
        self.assertIn("test_digest_contract", r["unmatched"][0])

    def test_matching_name_but_different_error_is_not_allowed(self):
        """同一個測試日後因真的壞了而失敗，不可被舊缺口的名字擋箭牌放行。"""
        output = """
FAILED: 1 個失敗（共 121 個案例）
  FAIL: test_blogroll (news_aggregator.tests.test_blogroll.TestBlogroll)
AssertionError: blogroll 來源清單解析錯誤
"""
        r = evaluate(output, 1, GAPS, today=date(2026, 8, 1))
        self.assertFalse(r["allow"])

    def test_rule_check_failure_blocks(self):
        """check_rules.py 失敗解析不出案例名 → 保守擋下，不可當作『與 web 無關』。"""
        r = evaluate(OUTPUT_RULES_ONLY, 1, GAPS)
        self.assertFalse(r["allow"])
        self.assertEqual(r["reason"], "no_parsable_failures")

    def test_empty_allowlist_blocks_everything(self):
        """允許清單空的時候，行為必須等同舊 gate——預設是嚴格，不是寬鬆。"""
        r = evaluate(OUTPUT_KNOWN, 1, [])
        self.assertFalse(r["allow"])

    def test_overdue_gap_still_allows_but_warns(self):
        """逾複查日仍放行：擋住網站不會讓逾期的 workaround 早一天收尾。"""
        r = evaluate(OUTPUT_KNOWN, 1, GAPS, today=date(2026, 9, 1))
        self.assertTrue(r["allow"])
        self.assertIn("feedparser-sgmllib", r["overdue"])


class TestShippedAllowlist(unittest.TestCase):
    REQUIRED = ("id", "test", "error", "register_row", "review_date", "why_safe")

    def test_shipped_file_parses_and_entries_are_complete(self):
        """實際 ship 的 docs/known-test-gaps.json 必須可解析，且每筆欄位齊全。

        允許清單漏欄位不會報錯、只會靜默不匹配（等於該缺口沒被登記到），
        所以這裡明著檢查，避免有人以為登記了、實際上沒生效。

        **同時驗 `_example`**：`gaps` 平常是空的（現在就是），只跑迴圈的話這條測試
        一次斷言都不會執行——2026-08-29 全庫掃描抓到它是唯一真正恆真的一條。而
        `_example` 是這份檔案自己宣告的欄位樣板，拿它當常在的樣本，欄位清單日後改了
        卻忘了同步樣板，這裡就會紅。
        """
        example = json.loads(GAPS_FILE.read_text(encoding="utf-8"))["_example"]
        for field in self.REQUIRED:
            self.assertIn(field, example, f"_example 樣板缺欄位 {field}")

        for gap in load_gaps():
            for field in self.REQUIRED:
                self.assertIn(field, gap, f"缺口 {gap.get('id', '?')} 缺欄位 {field}")


if __name__ == "__main__":
    unittest.main()
