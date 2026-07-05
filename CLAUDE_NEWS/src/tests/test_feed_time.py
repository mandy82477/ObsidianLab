"""Regression test for news_aggregator.sources.base.parse_feed_time.

History: this function once computed local time via time.mktime()-style
handling of the feedparser struct_time, which is UTC, causing every parsed
timestamp to be off by the local UTC offset (an 8-hour skew was observed for
UTC+8). The fix uses calendar.timegm() (which treats the struct_time as UTC)
before converting to an aware UTC datetime. This test locks in that a known
struct_time input produces the exact expected UTC datetime with zero offset,
using a fixed, unambiguous timestamp so the test itself is not host-timezone
dependent.
"""
import time
import unittest
from datetime import datetime, timezone

from news_aggregator.sources.base import parse_feed_time


class _FakeEntry(dict):
    """feedparser entries behave like dicts with a .get() method; a plain
    dict already satisfies that, this subclass exists only for clarity."""


class TestParseFeedTime(unittest.TestCase):
    def test_published_parsed_is_utc_with_no_offset(self):
        # 2026-01-01 12:00:00 UTC, built directly from a UTC struct via
        # calendar.timegm's inverse (time.gmtime) so the expectation is
        # independent of the host machine's local timezone.
        expected = datetime(2026, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        struct = time.gmtime(expected.timestamp())
        entry = _FakeEntry(published_parsed=struct)

        result = parse_feed_time(entry)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)
        self.assertEqual(result.utcoffset().total_seconds(), 0)
        self.assertEqual(result.hour, 12)

    def test_falls_back_to_updated_parsed(self):
        expected = datetime(2026, 6, 15, 3, 30, 0, tzinfo=timezone.utc)
        struct = time.gmtime(expected.timestamp())
        entry = _FakeEntry(updated_parsed=struct)

        result = parse_feed_time(entry)

        self.assertEqual(result, expected)

    def test_missing_time_returns_none(self):
        entry = _FakeEntry()
        self.assertIsNone(parse_feed_time(entry))

    def test_malformed_struct_returns_none_not_raises(self):
        entry = _FakeEntry(published_parsed="not-a-struct")
        # Must never raise — base.py contract says fetch() should never
        # raise, and parse_feed_time backs that guarantee.
        self.assertIsNone(parse_feed_time(entry))


if __name__ == "__main__":
    unittest.main()
