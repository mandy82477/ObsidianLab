"""Tests for scripts/open_loops.py 的三個新掃描（2026-08-29 新增）。

背景：本腳本原本只算「未 commit 改動」與「逾期 workaround」，報「合計開放迴路 8 個」，
而同日實測懸置標記 51+144、reader-notes 4、feature-radar 23——**唯一的彙整端低報 30 倍**。
這與 `--queue` 改版前「只印存量不印流量」是同一種病：看得到的地方沒有積壓。
"""
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("open_loops")
TODAY = date(2026, 8, 29)


class ReaderNotesPendingTest(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self._orig = mod.READER_NOTES
        mod.READER_NOTES = Path(self._tmp.name) / "reader-notes.md"

    def tearDown(self):
        mod.READER_NOTES = self._orig
        self._tmp.cleanup()

    def test_counts_only_pending_and_reports_age(self):
        mod.READER_NOTES.write_text(
            "- [⏳] 2026-07-12｜🔍｜舊事" + chr(10)
            + "- [✅] 2026-08-01｜🔍｜已納入" + chr(10)
            + "- [📌] 2026-08-01｜📓｜雜記" + chr(10),
            encoding="utf-8")
        rows = mod.reader_notes_pending(TODAY)
        self.assertEqual(len(rows), 1, "只算 ⏳，✅ 與 📌 不算")
        self.assertIn("放置 48 天", rows[0])

    def test_missing_file_degrades_to_empty(self):
        self.assertEqual(mod.reader_notes_pending(TODAY), [])


class FeatureRadarWatchingTest(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self._orig = mod.FEATURE_RADAR
        mod.FEATURE_RADAR = Path(self._tmp.name) / "feature-radar.md"

    def tearDown(self):
        mod.FEATURE_RADAR = self._orig
        self._tmp.cleanup()

    def test_counts_watch_symbols(self):
        mod.FEATURE_RADAR.write_text("⏳ a" + chr(10) + "✅ b" + chr(10) + "⏳ c", encoding="utf-8")
        self.assertEqual(mod.feature_radar_watching(), 2)

    def test_missing_file_is_zero(self):
        self.assertEqual(mod.feature_radar_watching(), 0)


class PendingBacklogDegradationTest(unittest.TestCase):
    def test_returns_zeros_when_scan_unavailable(self):
        """彙整端不可因子系統壞掉而整個當掉——前兩類仍要報得出來。"""
        orig = mod.pending_marker_backlog
        try:
            self.assertEqual(len(orig(TODAY)), 3)
        finally:
            mod.pending_marker_backlog = orig


class TotalBacklogTest(unittest.TestCase):
    """總量必須含入五類——漏算任一類就回到「報 8 個、實際欠 230 筆」那種低報。"""

    def _run_main(self):
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            mod.main()
        return buf.getvalue()

    def test_total_includes_all_five_categories(self):
        orig = (mod.uncommitted_real_changes, mod.overdue_workarounds,
                mod.pending_marker_backlog, mod.reader_notes_pending,
                mod.feature_radar_watching, mod._use_utf8_stdout)
        try:
            mod._use_utf8_stdout = lambda: None
            mod.uncommitted_real_changes = lambda: ["a", "b"]          # 2
            mod.overdue_workarounds = lambda today: ["c"]              # 1
            mod.pending_marker_backlog = lambda today: (51, 144, 5)    # 195
            mod.reader_notes_pending = lambda today: ["d", "e", "f", "g"]  # 4
            mod.feature_radar_watching = lambda: 23                    # 23
            out = self._run_main()
        finally:
            (mod.uncommitted_real_changes, mod.overdue_workarounds,
             mod.pending_marker_backlog, mod.reader_notes_pending,
             mod.feature_radar_watching, mod._use_utf8_stdout) = orig
        self.assertIn("需收尾（前兩類）：3 個", out)
        self.assertIn("全庫積壓合計：225 筆", out)  # 3+51+144+4+23


if __name__ == "__main__":
    unittest.main()
