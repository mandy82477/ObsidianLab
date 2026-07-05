"""Tests for scripts/check_links.py URL-extraction regex (URL_RE) and
collect_links(). Does not perform any real network requests — check_one()
is never called.

Regression: URL_RE previously over-matched into trailing CJK/full-width
punctuation when a URL was immediately followed by Chinese commentary with
no whitespace separator (e.g. "...id=123（HN score 8）"), swallowing the
Chinese text into the "URL". The fix excludes full-width punctuation and the
CJK Unified Ideographs range from the URL character class.
"""
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

check_links = load_script_module("check_links")


class TestUrlRegexBoundary(unittest.TestCase):
    def test_url_stops_before_fullwidth_paren_and_cjk(self):
        text = "詳見 https://example.com/issues?id=123（HN score 8）的討論"
        m = check_links.URL_RE.search(text)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(0), "https://example.com/issues?id=123")

    def test_url_stops_at_whitespace(self):
        text = "來源 https://example.com/a/b 後面還有文字"
        m = check_links.URL_RE.search(text)
        self.assertEqual(m.group(0), "https://example.com/a/b")

    def test_url_stops_at_markdown_link_close_paren(self):
        text = "[標題](https://example.com/page)之後的文字"
        m = check_links.URL_RE.search(text)
        self.assertEqual(m.group(0), "https://example.com/page")

    def test_url_with_query_string_kept_intact(self):
        text = "https://example.com/search?q=claude&lang=zh-TW 結尾"
        m = check_links.URL_RE.search(text)
        self.assertEqual(m.group(0), "https://example.com/search?q=claude&lang=zh-TW")


class TestCollectLinks(unittest.TestCase):
    def test_collect_links_excludes_news_dir_and_maps_pages(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            wiki_topics = root / "wiki" / "topics"
            wiki_topics.mkdir(parents=True)
            news_dir = root / "news"
            news_dir.mkdir(parents=True)

            page = wiki_topics / "sample.md"
            page.write_text(
                "參考 https://example.com/ref1 與 https://example.com/ref1 重複出現",
                encoding="utf-8",
            )
            news_page = news_dir / "2026-01-01.md"
            news_page.write_text("https://example.com/should-not-be-collected", encoding="utf-8")

            originals = {"WIKI_DIR": check_links.WIKI_DIR}
            check_links.WIKI_DIR = root / "wiki"
            try:
                links = check_links.collect_links()
            finally:
                check_links.WIKI_DIR = originals["WIKI_DIR"]

            self.assertIn("https://example.com/ref1", links)
            # same URL referenced twice in one file -> two entries in the list
            self.assertEqual(len(links["https://example.com/ref1"]), 2)
            self.assertNotIn("https://example.com/should-not-be-collected", links)


if __name__ == "__main__":
    unittest.main()
