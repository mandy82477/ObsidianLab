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
from tempfile import TemporaryDirectory
import contextlib
import io as _io

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from gate_web_build import (evaluate, load_gaps, parse_failures,  # noqa: E402
                            match_gap, render)

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



class TestLoadGapsIsDefensive(unittest.TestCase):
    """允許清單壞掉時必須**擋下**，不是放行。

    這支腳本決定「測試失敗時網站要不要停更」，判錯的方向決定一切：誤放行會讓壞掉的
    產出上站，而那正是它存在要防的事。
    """

    def test_missing_file_yields_no_allowlist(self):
        with TemporaryDirectory() as tmp:
            self.assertEqual(load_gaps(Path(tmp) / "nope.json"), [])

    def test_broken_json_yields_no_allowlist(self):
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "gaps.json"
            p.write_text("{ not json", encoding="utf-8")
            # 吞掉警告輸出：它含 emoji，而 Windows 主控台預設 cp950。生產路徑由
            # main() 的 _use_utf8_stdout() 保護，測試不該依賴主控台編碼。
            with contextlib.redirect_stdout(_io.StringIO()):
                self.assertEqual(load_gaps(p), [])

    def test_non_dict_entries_are_dropped(self):
        """清單裡混進字串時只丟那一筆，不是整份作廢。"""
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "gaps.json"
            p.write_text(json.dumps({"gaps": ["壞的", {"id": "ok"}]}), encoding="utf-8")
            self.assertEqual(load_gaps(p), [{"id": "ok"}])


class TestMatchGapNeedsBothPatterns(unittest.TestCase):
    """只比對案例名稱的話，同一個測試日後真的壞了也會被誤放行。"""

    GAP = {"id": "g1", "test": r"^test_alpha\b", "error": "ImportError"}

    def test_both_patterns_match(self):
        self.assertIsNotNone(match_gap("test_alpha", "ImportError: boom", [self.GAP]))

    def test_name_matches_but_error_does_not(self):
        self.assertIsNone(match_gap("test_alpha", "AssertionError: 1 != 2", [self.GAP]))

    def test_error_matches_but_name_does_not(self):
        self.assertIsNone(match_gap("test_beta", "ImportError: boom", [self.GAP]))

    def test_entry_missing_a_pattern_is_skipped_not_treated_as_wildcard(self):
        """漏欄位的登記等於沒登記——不可因為少一半條件就變成無條件放行。"""
        self.assertIsNone(match_gap("test_alpha", "ImportError", [{"id": "g", "test": "test_alpha"}]))
        self.assertIsNone(match_gap("test_alpha", "ImportError", [{"id": "g", "error": "ImportError"}]))

    def test_invalid_regex_does_not_crash_and_does_not_match(self):
        bad = {"id": "bad", "test": "[unclosed", "error": "x"}
        with contextlib.redirect_stdout(_io.StringIO()):
            self.assertIsNone(match_gap("test_alpha", "x", [bad]))


class TestRenderCoversEveryBranch(unittest.TestCase):
    """render 的那行摘要會被原樣抄進 task_scheduler.log，是事後查案的唯一線索。"""

    def test_green(self):
        self.assertIn("放行", render(evaluate("", 0, [])))

    def test_blocked_by_unknown_failure(self):
        r = evaluate("FAIL: test_x (mod.Case.test_x)", 1, [])
        self.assertIn("擋下", render(r))
        self.assertIn("test_x", render(r))

    def test_allowed_lists_gap_ids(self):
        gaps = [{"id": "g1", "test": "test_x", "error": "Boom",
                 "review_date": "2099-01-01"}]
        r = evaluate("FAIL: test_x (mod.Case.test_x)\nBoom", 1, gaps)
        out = render(r)
        self.assertIn("g1", out)
        self.assertIn("放行", out)
        self.assertNotIn("逾複查日", out)

    def test_review_date_equal_to_today_is_not_overdue_yet(self):
        """邊界：複查日「當天」還不算逾期，隔天才算。

        判成當天就逾期的話，每個缺口在複查日當天都會多一行假警報——而固定假警報
        會讓人開始略過整份報告。
        """
        gaps = [{"id": "g1", "test": "test_x", "error": "Boom",
                 "review_date": "2026-09-01"}]
        r = evaluate("FAIL: test_x (mod.Case.test_x)" + chr(10) + "Boom", 1, gaps,
                     today=date(2026, 9, 1))
        self.assertEqual(r["overdue"], [])

    def test_overdue_is_appended_to_the_summary(self):
        gaps = [{"id": "g1", "test": "test_x", "error": "Boom",
                 "review_date": "2000-01-01"}]
        r = evaluate("FAIL: test_x (mod.Case.test_x)\nBoom", 1, gaps)
        self.assertIn("逾複查日", render(r))

    def test_failure_count_is_reported(self):
        gaps = [{"id": "g1", "test": "test_", "error": "Boom",
                 "review_date": "2099-01-01"}]
        out = render(evaluate("FAIL: test_x (a.b.test_x)\nFAIL: test_y (a.b.test_y)\nBoom", 1, gaps))
        self.assertIn("2 案", out)



class TestGateExitCode(unittest.TestCase):
    """退出碼決定 web build 跑不跑——判反了就是「壞掉的產出照樣上站」。"""

    def _main(self, allow):
        import gate_web_build as gate

        class R:
            returncode, stdout, stderr = (0 if allow else 1), "", ""

        orig = gate.subprocess.run, gate.load_gaps, gate.evaluate, sys.argv
        gate.subprocess.run = lambda *a, **k: R()
        gate.load_gaps = lambda *a, **k: []
        gate.evaluate = lambda *a, **k: {
            "allow": allow, "reason": "tests_green" if allow else "unknown_failure",
            "failures": [], "matched": [], "unmatched": [] if allow else ["test_x"],
            "overdue": []}
        sys.argv = ["gate_web_build.py"]
        try:
            with contextlib.redirect_stdout(_io.StringIO()):
                return gate.main()
        finally:
            (gate.subprocess.run, gate.load_gaps, gate.evaluate, sys.argv) = orig

    def test_allowed_exits_zero(self):
        self.assertEqual(self._main(True), 0)

    def test_blocked_exits_nonzero(self):
        self.assertEqual(self._main(False), 1)


if __name__ == "__main__":
    unittest.main()
