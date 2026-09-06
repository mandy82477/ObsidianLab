"""Tests for check_weekly_ledger.check_headline() — 頭條敘事機械規則（W35 起生效）。

守四件事：生效閘（舊期不回溯）、跨期模板連兩期才擋、日期句首/粗體硬擋、
角色詞與日期遞增只 WARN 不擋。
"""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

ledger = load_script_module("check_weekly_ledger")


def _issue(body: str) -> str:
    return f"# 本週深挖\n\n## 一、頭條敘事：測試\n\n{body}\n\n## 二、技術討論與深挖\n\n內容\n"


CLEAN = "使用者這週撞到配額問題（08-17），官方補了說明頁（08-18）。"


class TestHeadline(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def _write(self, stem: str, body: str):
        (self.dir / f"{stem}.md").write_text(_issue(body), encoding="utf-8")

    def _run(self):
        report: list[str] = []
        ok = ledger.check_headline(report, weekly_dir=self.dir)
        return ok, "\n".join(report)

    def test_pre_w35_issues_are_frozen(self):
        self._write("2026-W34", "08-17 一句。08-18 又一句。08-16 回頭。**很長的一整句判斷被加粗超過十五個字**。")
        ok, out = self._run()
        self.assertTrue(ok)
        self.assertEqual(out, "")

    def test_template_blocked_only_on_consecutive_hit(self):
        self._write("2026-W34", "把三條線並排看，這週的故事不是A而是B。")
        self._write("2026-W35", "把三條線並排，這週的張力不是C而是D。")
        ok, out = self._run()
        self.assertFalse(ok)
        self.assertIn("同構", out)
        # 單期首次使用（上期無命中）合法
        self._write("2026-W34", CLEAN)
        ok, out = self._run()
        self.assertTrue(ok, out)

    def test_date_lead_and_bold_are_hard_fails(self):
        self._write("2026-W35", "08-17 發生了一件事。08-18 又發生了一件事。")
        ok, out = self._run()
        self.assertFalse(ok)
        self.assertIn("以日期開頭", out)

        self._write("2026-W35", "事故發生（08-16）。**650 億**與**四天四起**之外還有**第三處**。")
        ok, out = self._run()
        self.assertFalse(ok)
        self.assertIn("粗體 3 處", out)

    def test_role_words_and_date_order_only_warn(self):
        self._write(
            "2026-W35",
            "本週兩個數字：90 億的合約與 115 億，之後才有 08-15 的報導，回頭看 08-11 的起點。",
        )
        ok, out = self._run()
        self.assertTrue(ok, out)  # 只 WARN，不擋
        self.assertIn("缺角色詞", out)
        self.assertIn("非由早到晚", out)
        # 角色詞齊備時不告警
        self._write("2026-W35", "合約總額 90 億（08-11），單季 115 億（08-15）。")
        ok, out = self._run()
        self.assertTrue(ok)
        self.assertNotIn("缺角色詞", out)

    def test_missing_headline_section_warns(self):
        (self.dir / "2026-W35.md").write_text("# 只有標題\n\n## 二、其他\n\n內容\n", encoding="utf-8")
        ok, out = self._run()
        self.assertTrue(ok)
        self.assertIn("找不到「## 一、」頭條節", out)



class TestHeadlineDeck(unittest.TestCase):
    """頭條標題（`## 一、頭條敘事：<一句話>`），W36 起硬擋。

    這條檢查存在的唯一理由是「上一次它是靠沒人注意而死的」：W30–W34 五期都寫了
    這句、渲染層 weeklyHeadlineDeck() 一直支援，但規格從未寫下它——W35 一漏無人
    察覺，還誤把另立「本週一句話」callout 當成修法（2026-09-06 兩者合併）。
    """

    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def _run(self, stem: str, heading: str):
        (self.dir / f"{stem}.md").write_text(
            f"# 本週深挖\n\n{heading}\n\n一段正常的頭條正文。\n\n## 二、技術討論與深挖\n\n內容\n",
            encoding="utf-8",
        )
        report: list[str] = []
        ok = ledger.check_headline(report, weekly_dir=self.dir)
        return ok, "\n".join(report)

    def test_missing_deck_is_blocked(self):
        ok, out = self._run("2026-W36", "## 一、頭條敘事")
        self.assertFalse(ok)
        self.assertIn("缺頭條標題", out)

    def test_deck_present_passes(self):
        ok, out = self._run(
            "2026-W36", "## 一、頭條敘事：讓 Claude Code 讀一個網頁，就可能有人在你電腦上跑程式"
        )
        self.assertTrue(ok)
        self.assertNotIn("缺頭條標題", out)

    def test_overlong_deck_is_blocked(self):
        ok, out = self._run("2026-W36", "## 一、頭條敘事：" + "字" * (ledger.HEADLINE_DECK_MAX + 1))
        self.assertFalse(ok)
        self.assertIn("上限", out)

    def test_pre_w36_issues_are_not_retrofitted(self):
        """W35 以前已凍結——回溯只會產出永遠不修的 ❌，把真訊號淹掉。"""
        ok, out = self._run("2026-W35", "## 一、頭條敘事")
        self.assertNotIn("缺頭條標題", out)

if __name__ == "__main__":
    unittest.main()
