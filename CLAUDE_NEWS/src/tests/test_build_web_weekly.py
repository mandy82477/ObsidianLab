"""Regression tests for scripts/build_web.py weekly (weekly/*.md) parsing.

Covers:
- parse_weekly() extracts id (from filename stem) / name (H1) / preview
  (first non-empty, non-heading, non-callout line) from a realistic
  four-section weekly report fixture.
- build() gracefully produces an empty weeklyIndex when weekly/ does not
  exist yet (empty-state contract the front-end "尚無週報" message relies on).
- structured extraction (journal layout, §A of the web-reader upgrade):
  lede, four keyword-classified §H2 sections, §H3 sub-sections inside
  discussion (versionNote/roundup/deepDive), the nextweek forecast table,
  the numbers stat bullets, and footer — all with graceful degradation
  (missing section → None/[], never an exception) since headline order
  and numbering ("一、二、三、四") may change week to week.
"""
import tempfile
import textwrap
import unittest
from pathlib import Path

from tests._helpers import load_script_module, FIXTURES_DIR

build_web = load_script_module("build_web")


def _write_weekly(tmpdir: str, name: str, content: str) -> Path:
    p = Path(tmpdir) / name
    p.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")
    return p


class TestParseWeekly(unittest.TestCase):
    def setUp(self):
        self.fixture = FIXTURES_DIR / "2026-W30.md"

    def test_id_from_filename_stem(self):
        w = build_web.parse_weekly(self.fixture)
        self.assertEqual(w["id"], "2026-W30")

    def test_page_type(self):
        w = build_web.parse_weekly(self.fixture)
        self.assertEqual(w["pageType"], "weekly")

    def test_name_from_h1(self):
        w = build_web.parse_weekly(self.fixture)
        self.assertEqual(w["name"], "2026 年第 30 週：Sonnet 5 定價之爭與升版抉擇")

    def test_preview_skips_callout_and_headings(self):
        w = build_web.parse_weekly(self.fixture)
        # First real content line is inside the "> ..." callout, which must be
        # skipped; the real preview comes from the next non-heading paragraph.
        self.assertTrue(w["preview"])
        self.assertFalse(w["preview"].startswith(">"))
        self.assertFalse(w["preview"].startswith("#"))

    def test_markdown_full_content_preserved(self):
        w = build_web.parse_weekly(self.fixture)
        self.assertIn("深挖：折扣定價機制拆解", w["markdown"])


class TestParseWeeklyStructured(unittest.TestCase):
    """Structured extraction against the real four-section fixture."""

    def setUp(self):
        self.w = build_web.parse_weekly(FIXTURES_DIR / "2026-W30.md")

    def test_lede_extracted_and_label_stripped(self):
        self.assertEqual(
            self.w["lede"],
            "Sonnet 5 折扣即將到期，社群兩極反應同時牽動升版抉擇。",
        )

    def test_headline_section_classified_by_keyword(self):
        headline = self.w["sections"]["headline"]
        self.assertIsNotNone(headline)
        self.assertIn("頭條", headline["title"])
        self.assertIn("折扣倒數牽動的兩難", headline["title"])
        self.assertIn("兩極反應", headline["body"])

    def test_discussion_subsections(self):
        disc = self.w["sections"]["discussion"]
        self.assertIsNotNone(disc)
        self.assertIn("建議可升", disc["versionNote"])
        self.assertIn("tool_runner", disc["roundup"])
        self.assertIsNotNone(disc["deepDive"])
        self.assertEqual(disc["deepDive"]["title"], "折扣定價機制拆解")
        self.assertIn("階梯制", disc["deepDive"]["body"])

    def test_nextweek_forecast_table(self):
        nw = self.w["sections"]["nextweek"]
        self.assertIsNotNone(nw)
        self.assertEqual(len(nw["forecasts"]), 2)
        first = nw["forecasts"][0]
        self.assertEqual(set(first.keys()), {"type", "forecast", "criterion"})
        self.assertEqual(first["type"], "到期日")  # bold markers stripped
        self.assertIn("8/1", first["forecast"])
        self.assertIn("Opus 使用量", first["criterion"])

    def test_numbers_stats(self):
        nums = self.w["sections"]["numbers"]
        self.assertIsNotNone(nums)
        self.assertEqual(len(nums["stats"]), 4)
        self.assertEqual(nums["stats"][0], {"value": "42", "desc": "本週共收錄的條目總數。"})

    def test_footer_extracted_and_excluded_from_numbers_body(self):
        self.assertIsNotNone(self.w["footer"])
        self.assertIn("news/2026-07-20.md", self.w["footer"])
        # footer must not leak into the numbers section's raw body
        self.assertNotIn("素材涵蓋窗", self.w["sections"]["numbers"]["body"])

    def test_no_unclassified_extra_sections_in_full_fixture(self):
        self.assertEqual(self.w["extraSections"], [])


class TestParseWeeklyGracefulDegradation(unittest.TestCase):
    """淡週容忍：缺段、亂序、格式跑掉都不可拋例外，只留 None/[]。"""

    def test_missing_nextweek_section_yields_none(self):
        with tempfile.TemporaryDirectory() as d:
            f = _write_weekly(d, "2026-W31.md", """
                # 淡週測試

                > **本週一句話**：本週沒有下週看什麼段落。

                ## 一、頭條敘事：無事發生

                本週相對平靜。

                ## 四、本週數字

                - **10**——條目數。
                """)
            w = build_web.parse_weekly(f)
            self.assertIsNone(w["sections"]["nextweek"])
            self.assertIsNotNone(w["sections"]["headline"])
            self.assertEqual(w["sections"]["numbers"]["stats"], [{"value": "10", "desc": "條目數。"}])

    def test_section_order_does_not_matter(self):
        """分類靠關鍵字，不靠「一、二、三、四」——刻意把段落順序打亂＋去掉編號。"""
        with tempfile.TemporaryDirectory() as d:
            f = _write_weekly(d, "2026-W32.md", """
                # 亂序測試

                ## 本週數字

                - **99**——條目數。

                ## 下週看什麼

                | 類型 | 預告 | 判準 |
                |------|------|------|
                | 修復追蹤 | 某功能 | 若修復 → 收斂 |

                ## 頭條敘事：順序不影響分類

                內文。
                """)
            w = build_web.parse_weekly(f)
            self.assertIsNotNone(w["sections"]["headline"])
            self.assertIn("順序不影響分類", w["sections"]["headline"]["title"])
            self.assertEqual(w["sections"]["numbers"]["stats"][0]["value"], "99")
            self.assertEqual(len(w["sections"]["nextweek"]["forecasts"]), 1)
            self.assertIsNone(w["sections"]["discussion"])

    def test_unrecognized_h2_goes_to_extra_sections(self):
        with tempfile.TemporaryDirectory() as d:
            f = _write_weekly(d, "2026-W33.md", """
                # 額外段落測試

                ## 一個沒人分類過的標題

                這段沒有關鍵字可對應。
                """)
            w = build_web.parse_weekly(f)
            self.assertEqual(len(w["extraSections"]), 1)
            self.assertEqual(w["extraSections"][0]["title"], "一個沒人分類過的標題")
            for key in ("headline", "discussion", "nextweek", "numbers"):
                self.assertIsNone(w["sections"][key])

    def test_malformed_table_does_not_raise(self):
        """表格缺分隔線列——解析器不應拋例外，寧可回傳空 forecasts。"""
        with tempfile.TemporaryDirectory() as d:
            f = _write_weekly(d, "2026-W34.md", """
                # 壞表格測試

                ## 下週看什麼

                | 類型 | 預告 | 判準 |
                | 修復追蹤 | 某功能 | 若修復 → 收斂 |
                """)
            try:
                w = build_web.parse_weekly(f)
            except Exception as e:  # pragma: no cover
                self.fail(f"parse_weekly raised on malformed table: {e}")
            self.assertIsInstance(w["sections"]["nextweek"]["forecasts"], list)

    def test_no_lede_yields_none(self):
        with tempfile.TemporaryDirectory() as d:
            f = _write_weekly(d, "2026-W35.md", """
                # 無一句話測試

                ## 一、頭條敘事：無 lede

                內文。
                """)
            w = build_web.parse_weekly(f)
            self.assertIsNone(w["lede"])


class TestWeeklyEmptyState(unittest.TestCase):
    """Locks in collect_weekly()'s empty-state contract — the front-end's
    "尚無週報" message depends on weeklyIndex being an empty list (not a
    missing key, not an exception) when no weekly/ directory exists yet."""

    def test_nonexistent_dir_yields_empty_containers(self):
        weekly_all, weekly_index = build_web.collect_weekly(Path("Z:/does/not/exist/weekly"))
        self.assertEqual(weekly_all, {})
        self.assertEqual(weekly_index, [])

    def test_existing_dir_parses_weekly_fixture(self):
        weekly_all, weekly_index = build_web.collect_weekly(FIXTURES_DIR)
        self.assertIn("2026-W30", weekly_all)
        ids = [w["id"] for w in weekly_index]
        self.assertIn("2026-W30", ids)


if __name__ == "__main__":
    unittest.main()
