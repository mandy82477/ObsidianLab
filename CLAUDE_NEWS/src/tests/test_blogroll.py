"""Tests for news_aggregator.sources.blogroll.Blogroll.

Covers:
- Missing/invalid blogroll.json config never raises, returns [].
- Empty blog list returns [].
- status == "retired" blogs are skipped.
- Keyword pre-filter admits on-topic posts and rejects off-topic ones.
- A single blog's RSS failure (network error, bozo feed) never raises and
  does not prevent other blogs in the list from being fetched.
"""
import json
import time
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

from news_aggregator.sources.blogroll import Blogroll, _matches_keywords


class _FakeEntry(dict):
    """feedparser entries behave like dicts with a .get() method."""


def _entry(title, summary="", hours_ago=1):
    pub = datetime.now(tz=timezone.utc) - timedelta(hours=hours_ago)
    return _FakeEntry(
        title=title,
        summary=summary,
        link=f"https://example.com/{title}",
        published_parsed=time.gmtime(pub.timestamp()),
    )


class _FakeFeed:
    def __init__(self, entries, bozo=False, bozo_exception=None):
        self.entries = entries
        self.bozo = bozo
        self.bozo_exception = bozo_exception


class TestKeywordFilter(unittest.TestCase):
    def test_admits_claude_mention(self):
        self.assertTrue(_matches_keywords("My thoughts on Claude Code", ""))

    def test_admits_anthropic_in_summary(self):
        self.assertTrue(_matches_keywords("Untitled", "A post about Anthropic's latest release"))

    def test_admits_case_insensitive(self):
        self.assertTrue(_matches_keywords("ANTHROPIC ships something", ""))

    def test_rejects_unrelated_post(self):
        self.assertFalse(_matches_keywords("My vacation in Kyoto", "Photos and food"))


class TestBlogrollConfig(unittest.TestCase):
    def test_missing_config_returns_empty(self):
        with patch("news_aggregator.sources.blogroll.CONFIG_PATH") as mock_path:
            mock_path.exists.return_value = False
            self.assertEqual(Blogroll().fetch(), [])

    def test_invalid_json_returns_empty(self):
        with patch("news_aggregator.sources.blogroll.CONFIG_PATH") as mock_path:
            mock_path.exists.return_value = True
            mock_path.read_text.return_value = "{not valid json"
            self.assertEqual(Blogroll().fetch(), [])

    def test_empty_blog_list_returns_empty(self):
        with patch("news_aggregator.sources.blogroll.CONFIG_PATH") as mock_path:
            mock_path.exists.return_value = True
            mock_path.read_text.return_value = json.dumps({"blogs": []})
            self.assertEqual(Blogroll().fetch(), [])

    def test_config_load_exception_never_raises(self):
        with patch("news_aggregator.sources.blogroll.CONFIG_PATH") as mock_path:
            mock_path.exists.side_effect = Exception("disk error")
            try:
                result = Blogroll().fetch()
            except Exception as e:  # pragma: no cover
                self.fail(f"fetch() raised: {e}")
            self.assertEqual(result, [])


class TestBlogrollFetch(unittest.TestCase):
    def _blogs(self, **overrides):
        blog = {
            "slug": "example",
            "name": "Example Blog",
            "rss_url": "https://example.com/rss.xml",
            "added": "2026-07-11",
            "tags": [],
            "status": "probation",
            "notes": "",
        }
        blog.update(overrides)
        return [blog]

    def _patch_config(self, blogs):
        return patch(
            "news_aggregator.sources.blogroll._load_blogs",
            return_value=blogs,
        )

    def test_retired_blog_is_skipped(self):
        with self._patch_config(self._blogs(status="retired")):
            with patch("news_aggregator.sources.blogroll.requests.get") as mock_get:
                result = Blogroll().fetch()
                mock_get.assert_not_called()
                self.assertEqual(result, [])

    def test_keyword_filter_admits_and_rejects(self):
        entries = [
            _entry("Why Claude Code changed my workflow"),
            _entry("What I ate for lunch"),
        ]
        with self._patch_config(self._blogs()):
            with patch("news_aggregator.sources.blogroll.requests.get") as mock_get:
                mock_get.return_value = MagicMock(content=b"<rss></rss>")
                mock_get.return_value.raise_for_status = MagicMock()
                with patch(
                    "news_aggregator.sources.blogroll.feedparser.parse",
                    return_value=_FakeFeed(entries),
                ):
                    result = Blogroll().fetch()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Why Claude Code changed my workflow")
        self.assertEqual(result[0].source, "Blog / Example Blog")
        self.assertEqual(result[0].category, "community")
        self.assertEqual(result[0].score, 0)

    def test_bozo_feed_with_no_entries_does_not_raise(self):
        with self._patch_config(self._blogs()):
            with patch("news_aggregator.sources.blogroll.requests.get") as mock_get:
                mock_get.return_value = MagicMock(content=b"not xml")
                mock_get.return_value.raise_for_status = MagicMock()
                with patch(
                    "news_aggregator.sources.blogroll.feedparser.parse",
                    return_value=_FakeFeed([], bozo=True, bozo_exception=ValueError("bad xml")),
                ):
                    try:
                        result = Blogroll().fetch()
                    except Exception as e:  # pragma: no cover
                        self.fail(f"fetch() raised: {e}")
        self.assertEqual(result, [])

    def test_one_blog_failure_does_not_block_others(self):
        blogs = self._blogs(slug="a", name="Blog A") + [{
            "slug": "b",
            "name": "Blog B",
            "rss_url": "https://example.org/rss.xml",
            "added": "2026-07-11",
            "tags": [],
            "status": "active",
            "notes": "",
        }]

        def fake_get(url, **kwargs):
            if "example.com" in url:
                raise ConnectionError("network down")
            resp = MagicMock(content=b"<rss></rss>")
            resp.raise_for_status = MagicMock()
            return resp

        with self._patch_config(blogs):
            with patch("news_aggregator.sources.blogroll.requests.get", side_effect=fake_get):
                with patch(
                    "news_aggregator.sources.blogroll.feedparser.parse",
                    return_value=_FakeFeed([_entry("Claude Code deep dive")]),
                ):
                    try:
                        result = Blogroll().fetch()
                    except Exception as e:  # pragma: no cover
                        self.fail(f"fetch() raised: {e}")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].source, "Blog / Blog B")

    def test_missing_rss_url_skipped_gracefully(self):
        with self._patch_config(self._blogs(rss_url="")):
            with patch("news_aggregator.sources.blogroll.requests.get") as mock_get:
                result = Blogroll().fetch()
                mock_get.assert_not_called()
                self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
