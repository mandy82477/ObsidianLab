"""Regression tests for scripts/build_web.py weekly (weekly/*.md) parsing.

Covers:
- parse_weekly() extracts id (from filename stem) / name (H1) / preview
  (first non-empty, non-heading, non-callout line) from a realistic
  four-section weekly report fixture.
- build() gracefully produces an empty weeklyIndex when weekly/ does not
  exist yet (empty-state contract the front-end "尚無週報" message relies on).
"""
import unittest
from pathlib import Path

from tests._helpers import load_script_module, FIXTURES_DIR

build_web = load_script_module("build_web")


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
