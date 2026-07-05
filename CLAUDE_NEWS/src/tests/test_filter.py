"""Tests for news_aggregator.filter.filter_relevant.

Covers:
- PR-wire domains (prnewswire.com etc.) are dropped regardless of source.
- Normal domains pass through untouched.
- Google News items are dropped unless their title contains one of the
  relevant keywords (claude / anthropic / mcp), case-insensitively.
"""
import unittest
from datetime import datetime, timezone

from news_aggregator.filter import filter_relevant
from news_aggregator.sources.base import FeedItem


def _item(title, url, source="Hacker News"):
    return FeedItem(
        title=title,
        url=url,
        source=source,
        published=datetime(2026, 1, 1, tzinfo=timezone.utc),
        score=10,
        summary="",
        category="community",
    )


class TestPRWireFilter(unittest.TestCase):
    def test_pr_wire_domain_dropped(self):
        items = [_item("Some Anthropic Announcement", "https://www.prnewswire.com/news/x")]
        self.assertEqual(filter_relevant(items), [])

    def test_pr_wire_subdomain_dropped(self):
        items = [_item("Anthropic partners with Foo", "https://ir.businesswire.com/press/1")]
        self.assertEqual(filter_relevant(items), [])

    def test_normal_domain_kept(self):
        items = [_item("Anthropic ships new feature", "https://techcrunch.com/2026/01/01/anthropic")]
        result = filter_relevant(items)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].url, "https://techcrunch.com/2026/01/01/anthropic")

    def test_lookalike_domain_not_dropped(self):
        # "notprnewswire.com" must not match via naive substring check —
        # only exact host or subdomain of the registered PR-wire domain.
        items = [_item("Claude update", "https://notprnewswire.com/x")]
        result = filter_relevant(items)
        self.assertEqual(len(result), 1)


class TestGoogleNewsKeywordFilter(unittest.TestCase):
    def test_gnews_without_keyword_dropped(self):
        items = [_item("Generic AI market roundup", "https://example.com/a", source="Google News / Foo")]
        self.assertEqual(filter_relevant(items), [])

    def test_gnews_with_keyword_kept(self):
        items = [_item("Anthropic releases Claude update", "https://example.com/b", source="Google News / Foo")]
        result = filter_relevant(items)
        self.assertEqual(len(result), 1)

    def test_gnews_keyword_case_insensitive(self):
        items = [_item("CLAUDE CODE ships v2", "https://example.com/c", source="Google News / Foo")]
        result = filter_relevant(items)
        self.assertEqual(len(result), 1)

    def test_non_gnews_source_passes_without_keyword_check(self):
        items = [_item("Unrelated title with no keywords", "https://example.com/d", source="Hacker News")]
        result = filter_relevant(items)
        self.assertEqual(len(result), 1)

    def test_empty_list_returns_empty(self):
        self.assertEqual(filter_relevant([]), [])


if __name__ == "__main__":
    unittest.main()
