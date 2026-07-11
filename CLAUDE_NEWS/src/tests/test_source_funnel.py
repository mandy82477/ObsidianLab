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
    def __init__(self, source):
        self.source = source


class TestCountByPrefix(unittest.TestCase):
    def test_plain_source(self):
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
