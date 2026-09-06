"""table_census.py — 成長型態與機制判定的正確性測試。

2026-09-06 修正兩個假象：
1. `_growth()` 對無日期欄的表一律回報 `static`（讀起來像「已判定不會變」），
   實際上是「判不出來」——改回報 `unknown`。
2. `_mechanism()` 對通用節名（摘要／時序…）只要規則檔任何地方出現同名小標＋
   淘汰類關鍵詞就判「有」，命中的可能是別頁的規則。改為命中行必須同時出現
   該頁 slug／頁名，或落在該頁專屬規則節內。

全部用合成 fixture（臨時目錄自建頁與規則檔），不依賴任何真實 wiki 頁的節名或
行號——真實頁面會隨改版變動（2026-09-06 教訓：原版測試硬編了
`wiki/topics/anthropic-business.md` 的節名，該頁改版後全部變紅）。
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import table_census as tc  # noqa: E402


class GrowthUnknown(unittest.TestCase):
    def test_無日期欄回報unknown_不是static(self):
        rows = ["| 風險 | 當前狀況 | 嚴重度 |", "| A | B | C |"]
        self.assertEqual(tc._growth(rows, has_date_col=False), "unknown")

    def test_有日期欄且可判定仍照舊分類(self):
        rows = [
            "| x | 2026-09-01 |",
            "| y | 2026-08-01 |",
            "| z | 2026-07-01 |",
        ]
        self.assertEqual(tc._growth(rows, has_date_col=True), "prepend")

    def test_有日期欄由舊到新判為append(self):
        rows = [
            "| x | 2026-07-01 |",
            "| y | 2026-08-01 |",
            "| z | 2026-09-01 |",
        ]
        self.assertEqual(tc._growth(rows, has_date_col=True), "append")

    def test_有日期欄但證據不足仍回unknown(self):
        rows = ["| x | 無日期 |", "| y | 無日期 |"]
        self.assertEqual(tc._growth(rows, has_date_col=True), "unknown")

    def test_census整合_無日期欄的表回unknown_非static(self):
        """端到端：用合成頁驗證 census() 組裝出的 growth 欄不再出現 static 字面值。"""
        with tempfile.TemporaryDirectory() as tmp:
            page = Path(tmp) / "widget-page.md"
            page.write_text(
                "---\n"
                "page: \"topics/widget-page\"\n"
                "---\n"
                "# 小工具頁\n\n"
                "## 風險總覽\n\n"
                "| 風險 | 狀況 |\n"
                "|---|---|\n"
                "| A | B |\n"
                "| C | D |\n",
                encoding="utf-8",
            )
            orig_rule_files = tc.RULE_FILES
            tc.RULE_FILES = []  # 無規則檔命中，機制欄不受影響本測試只看 growth
            try:
                rows = tc.census([("topics/widget-page", page)])
            finally:
                tc.RULE_FILES = orig_rule_files
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["growth"], "unknown")
            self.assertNotEqual(rows[0]["growth"], "static")


class MechanismDirect(unittest.TestCase):
    """`_mechanism()` 的頁面範圍過濾——直接餵合成 rules 清單，不碰真實規則檔。"""

    def _rules(self, docs):
        """docs: [(filename, text), ...] → [(Path, text), ...]（Path 不需真實存在，只取 .name）。"""
        return [(Path(name), text) for name, text in docs]

    def test_命中行落在無關節內時判為無(self):
        rules = self._rules([
            ("wiki-ingest-format.md",
             "## 通用規則\n"
             "`## 摘要` 內帶日期的段落超過 2 段時移除，其餘頁面比照辦理。\n"),
        ])
        got = tc._mechanism("摘要", rules, "topics/widget-page", "小工具頁")
        self.assertEqual(got, "無")

    def test_命中行所屬標題含頁slug時判為有(self):
        rules = self._rules([
            ("wiki-ingest-widget.md",
             "## widget-page 更新規則\n"
             "`## 摘要` 表格過期後移除，改寫為結論。\n"),
        ])
        got = tc._mechanism("摘要", rules, "topics/widget-page", "小工具頁")
        self.assertEqual(got, "有（wiki-ingest-widget.md）")

    def test_命中行本身含頁標題時也判為有(self):
        rules = self._rules([
            ("wiki-ingest-other.md",
             "## 其他規則\n"
             "小工具頁的『時序』區塊，逾期節點需汰除。\n"),
        ])
        got = tc._mechanism("時序", rules, "topics/widget-page", "小工具頁")
        self.assertNotEqual(got, "無")
        self.assertIn("wiki-ingest-other.md", got)

    def test_多檔命中時各自列出_且無關檔不列入(self):
        rules = self._rules([
            ("wiki-ingest-widget-a.md", "## widget-page 更新規則\n`## 摘要` 表格過期後覆寫。\n"),
            ("wiki-ingest-widget-b.md", "## widget-page 補充規則\n`## 摘要` 內容逾期後封存。\n"),
            ("wiki-ingest-unrelated.md", "## 通用\n`## 摘要` 內容逾期後覆寫，各頁比照辦理。\n"),
        ])
        got = tc._mechanism("摘要", rules, "topics/widget-page", "小工具頁")
        self.assertTrue(got.startswith("有（"), got)
        self.assertIn("wiki-ingest-widget-a.md", got)
        self.assertIn("wiki-ingest-widget-b.md", got)
        self.assertNotIn("wiki-ingest-unrelated.md", got)


class MechanismCensusIntegration(unittest.TestCase):
    """端到端：census() 用合成頁 + 合成規則檔，驗證 slug/title 過濾確實接上 _mechanism。"""

    def _census_with_rules(self, page_text, rule_docs):
        with tempfile.TemporaryDirectory() as tmp:
            page = Path(tmp) / "widget-page.md"
            page.write_text(page_text, encoding="utf-8")
            rule_files = []
            for i, (name, text) in enumerate(rule_docs):
                rf = Path(tmp) / f"rule{i}-{name}"
                rf.write_text(text, encoding="utf-8")
                rule_files.append(rf)
            orig_rule_files = tc.RULE_FILES
            tc.RULE_FILES = rule_files
            try:
                return tc.census([("topics/widget-page", page)])
            finally:
                tc.RULE_FILES = orig_rule_files

    PAGE_TEXT = (
        "---\n"
        "page: \"topics/widget-page\"\n"
        "---\n"
        "# 小工具頁\n\n"
        "## 摘要\n\n"
        "| 風險 | 狀況 |\n"
        "|---|---|\n"
        "| A | B |\n"
    )

    def test_只有通用規則檔時機制為無(self):
        rows = self._census_with_rules(
            self.PAGE_TEXT,
            [("wiki-ingest-format.md", "## 通用規則\n`## 摘要` 逾期段落應移除。\n")],
        )
        summary = [r for r in rows if r["section"] == "摘要"]
        self.assertTrue(summary)
        self.assertEqual(summary[0]["mechanism"], "無")
        self.assertEqual(summary[0]["growth"], "unknown")  # 無日期欄

    def test_有頁專屬規則檔時機制為有(self):
        rule_name = "wiki-ingest-widget.md"
        rows = self._census_with_rules(
            self.PAGE_TEXT,
            [
                ("wiki-ingest-format.md", "## 通用規則\n`## 摘要` 逾期段落應移除。\n"),
                (rule_name, "## widget-page 更新規則\n`## 摘要` 表格過期後移除。\n"),
            ],
        )
        summary = [r for r in rows if r["section"] == "摘要"]
        self.assertTrue(summary)
        self.assertIn(f"rule1-{rule_name}", summary[0]["mechanism"])


if __name__ == "__main__":
    unittest.main()
