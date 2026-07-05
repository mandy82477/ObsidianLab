"""Regression tests for scripts/build_web.py digest (news/*.md) parsing.

Covers:
- parse_digest() correctly splits the six digest sections and counts items.
- mediaReports section is parsed.
- sourceStatus table is parsed.
- Regression (2026-07-02 format-breakage incident): bullet-style entries
  ("- **標題**：內文") must NOT be recognized as valid story entries — this
  locks in the parser's contract that only "**[標題](url)**" headline lines
  count, so a future format regression is caught immediately by this test
  rather than silently producing an empty section on the live site.
"""
import unittest
from pathlib import Path

from tests._helpers import load_script_module, FIXTURES_DIR

build_web = load_script_module("build_web")


class TestParseDigest(unittest.TestCase):
    def setUp(self):
        self.fixture = FIXTURES_DIR / "sample_digest.md"

    def test_header_metadata(self):
        d = build_web.parse_digest(self.fixture)
        self.assertEqual(d["date"], "sample_digest")
        self.assertEqual(d["articleCount"], 5)
        self.assertEqual(d["generatedAt"], "2026-01-01 23:59 UTC")

    def test_section_counts(self):
        d = build_web.parse_digest(self.fixture)
        self.assertEqual(len(d["topStories"]), 1)
        self.assertEqual(len(d["techUpdates"]), 1)
        self.assertEqual(len(d["mediaReports"]), 1)
        self.assertEqual(len(d["discussions"]), 2)
        self.assertEqual(len(d["billing"]), 1)

    def test_media_reports_parsed(self):
        d = build_web.parse_digest(self.fixture)
        self.assertEqual(len(d["mediaReports"]), 1)
        story = d["mediaReports"][0]
        self.assertEqual(story["title"], "媒體報導標題")
        self.assertEqual(story["url"], "https://example.com/story-3")
        self.assertEqual(story["source"], "Google News / Example")

    def test_source_status_table_parsed(self):
        d = build_web.parse_digest(self.fixture)
        self.assertEqual(len(d["sourceStatus"]), 3)
        names = {s["name"] for s in d["sourceStatus"]}
        self.assertEqual(names, {"Anthropic Blog", "Hacker News", "GitHub"})
        github_row = next(s for s in d["sourceStatus"] if s["name"] == "GitHub")
        self.assertFalse(github_row["ok"])
        self.assertEqual(github_row["count"], 0)
        hn_row = next(s for s in d["sourceStatus"] if s["name"] == "Hacker News")
        self.assertTrue(hn_row["ok"])
        self.assertEqual(hn_row["count"], 2)

    def test_focus_ref_urls_extracted(self):
        d = build_web.parse_digest(self.fixture)
        self.assertEqual(len(d["focus"]), 2)
        # FOCUS_RE captures the bracketed tag including its brackets verbatim.
        self.assertEqual(d["focus"][0]["tag"], "[重大事件]")
        self.assertEqual(d["focus"][0]["ref_urls"], ["https://example.com/focus-1"])
        self.assertEqual(
            d["focus"][1]["ref_urls"],
            ["https://example.com/story-2", "https://example.com/story-3"],
        )

    def test_discussion_body_contains_sentiment_marker(self):
        # NOTE: SENTIMENT_RE (`` `情緒：(.+?)` `` with backticks) is defined in
        # build_web.py but never invoked inside parse_digest — sentiment text
        # (plain "情緒：😊", no backticks) ends up folded into the story body,
        # and the "sentiment" field is always "". This test locks in the
        # *current* observed behavior so a future accidental change is caught;
        # it is not asserting this is the desired behavior.
        d = build_web.parse_digest(self.fixture)
        bodies = {s["title"]: s for s in d["discussions"]}
        self.assertEqual(bodies["討論標題一"]["sentiment"], "")
        self.assertIn("情緒：😊", bodies["討論標題一"]["body"])
        self.assertEqual(bodies["討論標題二"]["sentiment"], "")
        self.assertIn("情緒：😤", bodies["討論標題二"]["body"])


class TestBulletStyleRegression(unittest.TestCase):
    """2026-07-02 incident: a digest written with bullet-style entries instead
    of the required '**[title](url)**' headline format silently produced an
    empty section on the web reader. This test locks in that the parser does
    NOT recognize bullet-style entries as stories, so any future change that
    accidentally "fixes" this (making bullets parse) is caught — the true
    fix belongs in digest generation (news-pipeline-steps.md), not the parser.
    """

    def test_bullet_entries_not_parsed_as_stories(self):
        fixture = FIXTURES_DIR / "bullet_style_digest.md"
        d = build_web.parse_digest(fixture)
        # The bullet-style line under ⭐ 重點話題 must NOT produce a story.
        self.assertEqual(d["topStories"], [])


if __name__ == "__main__":
    unittest.main()
