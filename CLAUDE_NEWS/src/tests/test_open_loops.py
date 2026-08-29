"""Tests for scripts/open_loops.py 的五類彙整（2026-08-29 新增，同日 review 後補強）。

背景：本腳本原本只算「未 commit 改動」與「逾期 workaround」，報「合計開放迴路 8 個」，
而同日實測懸置標記 51+144、reader-notes 4、feature-radar 13——**唯一的彙整端低報 30 倍**。
這與 `--queue` 改版前「只印存量不印流量」是同一種病：看得到的地方沒有積壓。

第二輪 review 又抓到兩件事，本檔的測試多數是為它們而寫：
  1. 掃描失敗時，條列層有警語但**標題與總計仍當成 0**——防低報的腳本在總計那行低報
  2. `text.count("⏳")` 得 23，真實只有 13（9 條跨層重複、1 個圖例）——**高報 77%**
"""
import contextlib
import io
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("open_loops")
TODAY = date(2026, 8, 29)
NL = chr(10)


class _PatchedPaths(unittest.TestCase):
    """把模組層的路徑常數換成 tmp 檔，測完還原。"""

    ATTRS: tuple[str, ...] = ()

    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self._orig = {a: getattr(mod, a) for a in self.ATTRS}

    def tearDown(self):
        for a, v in self._orig.items():
            setattr(mod, a, v)
        self._tmp.cleanup()


class ReaderNotesPendingTest(_PatchedPaths):
    ATTRS = ("READER_NOTES",)

    def _write(self, text):
        mod.READER_NOTES = self.dir / "reader-notes.md"
        mod.READER_NOTES.write_text(text, encoding="utf-8")

    def test_counts_only_pending_and_reports_age(self):
        self._write(NL.join([
            "- [⏳] 2026-07-12｜\U0001f50d｜舊事",
            "- [✅] 2026-08-01｜\U0001f50d｜已納入",
            "- [\U0001f4cc] 2026-08-01｜\U0001f4d3｜雜記",
        ]))
        rows = mod.reader_notes_pending(TODAY)
        self.assertEqual(len(rows), 1, "只算 ⏳")
        self.assertIn("放置 48 天", rows[0])

    def test_missing_file_degrades_to_empty(self):
        mod.READER_NOTES = self.dir / "nope.md"
        self.assertEqual(mod.reader_notes_pending(TODAY), [])


class FeatureRadarWatchingTest(_PatchedPaths):
    """只解析全覽表列；跨層重複與圖例都不得計入。"""

    ATTRS = ("FEATURE_RADAR",)

    def _write(self, text):
        mod.FEATURE_RADAR = self.dir / "feature-radar.md"
        mod.FEATURE_RADAR.write_text(text, encoding="utf-8")

    def test_ignores_legend_row_and_detail_headers(self):
        self._write(NL.join([
            "## 圖例",
            "| 項目 | 值 |",
            "|---|---|",
            "| 試用價值 | ✅ 推薦 / ⏳ 觀望 |",   # 圖例，不得算
            "",
            "### SendFeedback",
            "**試用價值：** ⏳ 觀望",                      # 詳細條目標頭，不得算
            "",
            "## \U0001f4cb 功能全覽表",
            "| 功能 | 發布日期 | 熱度 | 試用價值 | 狀態 |",
            "|---|---|---|---|---|",
            "| **A** | 2026-08-27 | \U0001f525 | ⏳ 觀望 | 正式 |",     # 2 天，未逾期
            "| **B** | 2026-05-01 | \U0001f525 | ⏳ 觀察中 | 正式 |",  # 120 天，逾期；措辭漂移
            "| **C** | 2026-08-01 | \U0001f525 | ⚡ 有條件 | 正式 |",  # 非 ⏳
        ]))
        self.assertEqual(mod.feature_radar_watching(TODAY), (2, 1))

    def test_stops_at_next_h2_section(self):
        """Z8 殺手：不在下個 `## ` 停，後面章節的 ⏳ 表列會被誤算。"""
        self._write(NL.join([
            "## \U0001f4cb 功能全覽表",
            "| 功能 | 發布日期 | 熱度 | 試用價值 | 狀態 |",
            "|---|---|---|---|---|",
            "| **A** | 2026-08-27 | \U0001f525 | ⏳ 觀望 | 正式 |",
            "",
            "## 已封存",
            "| 功能 | 發布日期 | 熱度 | 試用價值 | 狀態 |",
            "| **Z** | 2026-01-01 | \U0001f525 | ⏳ 觀望 | 正式 |",
        ]))
        self.assertEqual(mod.feature_radar_watching(TODAY), (1, 0), "封存區不得計入")

    def test_skips_header_and_separator_rows(self):
        """Z4 殺手：表頭與分隔列不是條目。"""
        self._write(NL.join([
            "## \U0001f4cb 功能全覽表",
            "| 功能 | 發布日期 | 熱度 | ⏳ 試用價值 | 狀態 |",   # 表頭混入 ⏳
            "|---|---|---|⏳|---|",                                  # 分隔列混入 ⏳
            "| **A** | 2026-08-27 | \U0001f525 | ⏳ 觀望 | 正式 |",
        ]))
        self.assertEqual(mod.feature_radar_watching(TODAY), (1, 0))

    def test_ninety_day_threshold_is_strict(self):
        """Z6 殺手：> 90 而非 >= 90。剛好 90 天當天還在期限內。"""
        self._write(NL.join([
            "## \U0001f4cb 功能全覽表",
            "| 功能 | 發布日期 | 熱度 | 試用價值 | 狀態 |",
            "|---|---|---|---|---|",
            "| **剛好90** | 2026-05-31 | \U0001f525 | ⏳ 觀望 | 正式 |",   # 90 天整
            "| **91天** | 2026-05-30 | \U0001f525 | ⏳ 觀望 | 正式 |",     # 91 天
        ]))
        self.assertEqual(mod.feature_radar_watching(TODAY), (2, 1), "90 天整不算逾期")

    def test_missing_file_is_zero(self):
        mod.FEATURE_RADAR = self.dir / "nope.md"
        self.assertEqual(mod.feature_radar_watching(TODAY), (0, 0))


class PendingBacklogContractTest(unittest.TestCase):
    """P1-4：回傳 tuple 的欄位順序必須釘住。

    review 的 Y10/Y11 突變（legacy 與 oldest 對調、oldest 取 min）全部存活，
    因為所有測試都 mock 掉這個函式、從未驗過真實回傳值。對調後輸出會變成
    「舊語法盲區 5 筆、最久逾 144 天」，總數從 229 掉到 90。
    """

    def test_returns_overdue_legacy_oldest_in_that_order(self):
        import check_pending_markers as cpm
        with TemporaryDirectory() as tmp:
            wiki = Path(tmp)
            (wiki / "topics").mkdir()
            marker = ("❓ **待查證**（標 %s｜"
                      "查 Electron、桌面應用）｜**題**：內文")
            # 三筆逾期（最久 60 天）＋ 一筆舊語法 → 三個數字互異：(3, 1, 60)
            (wiki / "topics" / "a.md").write_text(
                NL.join([marker % "2026-06-16", marker % "2026-08-01", marker % "2026-08-05",
                         "待查證：舊字樣"]),
                encoding="utf-8")
            overdue, legacy, oldest = cpm.backlog_summary(wiki_dir=wiki, today=TODAY)
        self.assertEqual(overdue, 3, "第一個是逾期筆數")
        self.assertEqual(legacy, 1, "第二個是舊語法盲區")
        self.assertEqual(oldest, 60, "第三個是最久逾期天數（max 非 min）")


class MainOutputTest(unittest.TestCase):
    _STUBS = ("uncommitted_real_changes", "overdue_workarounds", "pending_marker_backlog",
              "reader_notes_pending", "feature_radar_watching", "_use_utf8_stdout")

    def _run(self, **stubs):
        orig = {a: getattr(mod, a) for a in self._STUBS}
        buf = io.StringIO()
        try:
            mod._use_utf8_stdout = lambda: None
            for k, v in stubs.items():
                setattr(mod, k, v)
            with contextlib.redirect_stdout(buf):
                rc = mod.main()
        finally:
            for a, v in orig.items():
                setattr(mod, a, v)
        return buf.getvalue(), rc

    def test_three_numbers_are_computed_from_all_categories(self):
        out, rc = self._run(
            uncommitted_real_changes=lambda: ["a", "b"],          # 需收尾 2
            overdue_workarounds=lambda today: ["c"],              # 需收尾 +1 → 3；已跳票 +1
            pending_marker_backlog=lambda today: (51, 144, 5),    # 已跳票 +51；存量 144
            reader_notes_pending=lambda today: ["d", "e"],        # 已跳票 +2
            feature_radar_watching=lambda today: (13, 3),         # 已跳票 +3
        )
        self.assertIn("需收尾（前兩類）：3 個", out)
        self.assertIn("已跳票（逾自身期限）：57 筆", out)  # 1+51+2+3
        self.assertIn("存量遷移（舊語法盲區）：144 筆", out)
        self.assertEqual(rc, 1)

    def test_broken_scan_never_reads_as_zero_anywhere(self):
        """P0-1：條列層有警語不夠——標題、總計、exit code 三處都不得把失敗當成 0。"""
        def boom(today):
            raise mod.PendingScanUnavailable("boom")

        out, rc = self._run(
            uncommitted_real_changes=lambda: [],
            overdue_workarounds=lambda today: [],
            pending_marker_backlog=boom,
            reader_notes_pending=lambda today: [],
            feature_radar_watching=lambda today: (13, 3),
        )
        self.assertIn("掃描失敗，數量未知", out, "標題不得印 0")
        self.assertNotIn("逾期 0 筆", out)
        self.assertIn("≥ ", out, "總計須標為下界")
        self.assertIn("存量遷移（舊語法盲區）：未知", out)
        self.assertIn("檔尾數字不含懸置類", out, "檔尾須有專屬警語，不可靠 [3] 那行的同字串頂替")
        self.assertNotEqual(rc, 0, "掃描壞掉不得回報成功")

    def test_clean_state_returns_zero(self):
        out, rc = self._run(
            uncommitted_real_changes=lambda: [],
            overdue_workarounds=lambda today: [],
            pending_marker_backlog=lambda today: (0, 0, 0),
            reader_notes_pending=lambda today: [],
            feature_radar_watching=lambda today: (0, 0),
        )
        self.assertEqual(rc, 0)


class PendingScanFailureTest(unittest.TestCase):
    def test_backlog_scan_raises_rather_than_returning_zeros(self):
        import sys
        saved = sys.modules.pop("check_pending_markers", None)
        sys.modules["check_pending_markers"] = None      # import 會拋
        try:
            with self.assertRaises(mod.PendingScanUnavailable):
                mod.pending_marker_backlog(TODAY)
        finally:
            if saved is not None:
                sys.modules["check_pending_markers"] = saved
            else:
                sys.modules.pop("check_pending_markers", None)


class OverdueWorkaroundsBoundaryTest(_PatchedPaths):
    """Y8 殺手：複查日「當天」就該提醒，`<=` 改 `<` 會讓當天到期的靜默漏掉。"""

    ATTRS = ("REGISTER",)

    def _write(self, due: str):
        mod.REGISTER = self.dir / "workaround-register.md"
        mod.REGISTER.write_text(NL.join([
            "## 進行中",
            "| 繞路內容 | 真解 | owner | 複查日 | 狀態 |",
            "|---|---|---|---|---|",
            f"| 某繞路 | 某真解 | Claude | {due} | \U0001f7e1 |",
        ]), encoding="utf-8")

    def test_due_today_is_reported(self):
        self._write("2026-08-29")
        self.assertEqual(len(mod.overdue_workarounds(TODAY)), 1, "當天到期就該提醒")

    def test_due_tomorrow_is_not_reported(self):
        self._write("2026-08-30")
        self.assertEqual(mod.overdue_workarounds(TODAY), [])

    def test_long_description_is_truncated_with_ellipsis(self):
        """硬切在半個詞上讀者會以為資料壞了；慣例是補刪節號。"""
        mod.REGISTER = self.dir / "workaround-register.md"
        long_desc = "甲" * 80
        mod.REGISTER.write_text(NL.join([
            "## 進行中",
            "| 繞路內容 | 真解 | owner | 複查日 | 狀態 |",
            "|---|---|---|---|---|",
            f"| {long_desc} | 真解 | Claude | 2026-08-01 | x |",
        ]), encoding="utf-8")
        row = mod.overdue_workarounds(TODAY)[0]
        self.assertTrue(row.endswith("…"), "超長描述須補刪節號")


if __name__ == "__main__":
    unittest.main()
