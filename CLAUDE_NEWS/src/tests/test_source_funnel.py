"""Tests for the source funnel stats in news_aggregator.main.

Covers:
- _count_by_prefix groups by the leading part of the source label,
  handling both " / " and " · " separators.
- write_funnel_record appends (never overwrites) one JSON line per call.
- Counts that cannot be mapped back to a registered source go to "_unmapped".
- write_funnel_record never raises on failure (best-effort).
"""
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from news_aggregator.main import _count_by_prefix, write_funnel_record


class _Item:
    def __init__(self, source, contributors=()):
        self.source = source
        self.contributors = tuple(contributors)


class TestContributorsAreCredited(unittest.TestCase):
    """A merged-away source must not read as having produced nothing.

    2026-08-15: the Anthropic Blog fetched the day's biggest story (the
    text-watermark post), dedup kept the Hacker News copy, and the funnel recorded
    Anthropic Blog as gathered 1 → filtered 0 → emitted 0. `source_scorecard.py`
    turns those numbers into 收錄率 = emitted / gathered, which `/wiki-lint` 6e
    uses to decide whether a source is worth keeping — so the source that supplied
    the headline scored 0%.
    """

    def test_merged_source_is_counted(self):
        counts = _count_by_prefix([_Item("Hacker News", contributors=("Anthropic Blog",))])
        self.assertEqual(counts["Anthropic Blog"], 1)
        self.assertEqual(counts["Hacker News"], 1)

    def test_contributor_labels_are_prefix_normalized(self):
        counts = _count_by_prefix([
            _Item("Google News / Reuters", contributors=("Reddit / r/ClaudeAI · 週熱門",)),
        ])
        self.assertEqual(counts, {"Google News": 1, "Reddit": 1})

    def test_a_source_is_counted_once_per_item_even_if_listed_twice(self):
        counts = _count_by_prefix([
            _Item("Hacker News / Show HN", contributors=("Hacker News / Ask HN",)),
        ])
        self.assertEqual(counts, {"Hacker News": 1}, "same source twice on one item is still one item")


class TestCountByPrefix(unittest.TestCase):
    def test_plain_source(self):
        """也涵蓋「沒有 contributors 的條目維持原行為」——contributors 那組原本另有一條
        逐字相同的測試（2026-08-29 測試盤查刪除），兩條驗的是同一個呼叫與同一個期望值。
        """
        counts = _count_by_prefix([_Item("Hacker News"), _Item("Hacker News")])
        self.assertEqual(counts, {"Hacker News": 2})

    def test_slash_variant(self):
        counts = _count_by_prefix([_Item("Hacker News / Show HN"), _Item("Reddit / r/ClaudeCode")])
        self.assertEqual(counts, {"Hacker News": 1, "Reddit": 1})

    def test_middle_dot_variant(self):
        counts = _count_by_prefix([_Item("Reddit / r/ClaudeAI · 週熱門"), _Item("Reddit · 週熱門")])
        self.assertEqual(counts, {"Reddit": 2})

    def test_empty_and_missing_source(self):
        counts = _count_by_prefix([_Item(""), object()])
        self.assertEqual(counts, {"": 2})


class TestWriteFunnelRecord(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.path = Path(self._tmp.name) / "data" / "source_funnel.jsonl"
        self.status = {
            "Hacker News": {"ok": True, "count": 5},
            "Reddit": {"ok": False, "count": 0},
        }

    def _write(self, filtered=(), emitted=()):
        write_funnel_record(
            self.path, date(2026, 7, 11), "gather", 26,
            self.status, list(filtered), list(emitted),
        )

    def _lines(self):
        return [json.loads(l) for l in self.path.read_text(encoding="utf-8").splitlines()]

    def test_creates_parent_dir_and_writes_record(self):
        self._write(filtered=[_Item("Hacker News / Show HN")], emitted=[_Item("Hacker News")])
        lines = self._lines()
        self.assertEqual(len(lines), 1)
        rec = lines[0]
        self.assertEqual(rec["date"], "2026-07-11")
        self.assertEqual(rec["mode"], "gather")
        self.assertEqual(rec["lookback_hours"], 26)
        self.assertIn("run_ts", rec)
        hn = rec["sources"]["Hacker News"]
        self.assertEqual(hn, {"ok": True, "gathered": 5, "filtered": 1, "emitted": 1})
        self.assertEqual(rec["sources"]["Reddit"]["ok"], False)
        self.assertEqual(rec["totals"], {"gathered": 5, "filtered": 1, "emitted": 1})

    def test_append_does_not_overwrite(self):
        self._write()
        self._write()
        self._write()
        lines = self._lines()
        self.assertEqual(len(lines), 3)
        # every line remains valid standalone JSON
        for rec in lines:
            self.assertEqual(rec["date"], "2026-07-11")

    def test_unmapped_bucket(self):
        self._write(
            filtered=[_Item("Mystery Source / feed"), _Item("Reddit / r/X · 週熱門")],
            emitted=[_Item("Mystery Source")],
        )
        rec = self._lines()[0]
        self.assertEqual(rec["sources"]["_unmapped"]["filtered"], 1)
        self.assertEqual(rec["sources"]["_unmapped"]["emitted"], 1)
        self.assertEqual(rec["sources"]["Reddit"]["filtered"], 1)
        self.assertEqual(rec["totals"]["filtered"], 2)
        self.assertEqual(rec["totals"]["emitted"], 1)

    def test_failure_does_not_raise(self):
        # A directory at the target path makes open("a") fail on every OS.
        bad = Path(self._tmp.name) / "as_dir"
        bad.mkdir()
        try:
            write_funnel_record(bad, "2026-07-11", "render", 26, self.status, [], [])
        except Exception as e:  # pragma: no cover
            self.fail(f"write_funnel_record raised: {e}")


if __name__ == "__main__":
    unittest.main()
