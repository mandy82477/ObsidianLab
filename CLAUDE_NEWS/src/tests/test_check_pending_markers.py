"""Tests for scripts/check_pending_markers.py — 懸置標記語法檢查器。

回填全庫 388 筆舊字樣為新語法前的驗收工具（規格見
`.claude/rules/wiki-ingest-format.md`「懸置標記語法」節）。每個測試用一個假
wiki 目錄（`TemporaryDirectory`），呼叫 `check(report, wiki_dir=..., today=...)`
——`check_pending_markers.check()` 明確接受這兩個參數以支援測試，不需 monkeypatch
模組全域。
"""
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("check_pending_markers")

TODAY = date(2026, 8, 9)


class _WikiCase(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.wiki_dir = Path(self._tmp.name)
        (self.wiki_dir / "topics").mkdir()
        (self.wiki_dir / "entities").mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel_path: str, text: str) -> Path:
        p = self.wiki_dir / rel_path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def run_check(self, today: date = TODAY):
        report: list[str] = []
        ok = mod.check(report, wiki_dir=self.wiki_dir, today=today)
        return ok, report


class TestValidMarkers(_WikiCase):
    def test_standard_form_passes(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 issue-1234、version-string）"
            "｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))

    def test_table_variant_with_matched_qid_passes(self):
        self.write(
            "topics/example.md",
            "| 議題 | 狀態 |\n"
            "| --- | --- |\n"
            "| 某議題 | ❓ 待查證 ⟨Q-07⟩ |\n\n"
            "**懸置細節**\n"
            "- ⟨Q-07⟩ ❓ **待查證**（標 2026-08-01｜查 CI-workflow、secrets-leak）：僅標題可用\n",
        )
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))

    def test_wikilink_probe_pointing_to_existing_page_passes(self):
        self.write("topics/ai-agent-safety.md", "# ai-agent-safety\n")
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 [[topics/ai-agent-safety]]）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))


class TestFailChecks(_WikiCase):
    def test_probe_hits_stoplist(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 Claude）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        joined = "\n".join(report)
        self.assertIn("過寬詞", joined)

    def test_symbol_kind_mismatch(self):
        self.write(
            "topics/example.md",
            "❓ **查無官方**（標 2026-08-01｜查 issue-1234）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("不一致", "\n".join(report))

    def test_bracket_misplaced_inside_bold(self):
        self.write(
            "topics/example.md",
            "❓ **待查證（標 2026-08-01｜查 issue-1234）**｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("括號誤寫在粗體內", "\n".join(report))

    def test_qid_cell_without_definition(self):
        self.write(
            "topics/example.md",
            "| 議題 | 狀態 |\n"
            "| --- | --- |\n"
            "| 某議題 | ❓ 待查證 ⟨Q-09⟩ |\n",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("無對應的懸置細節定義", "\n".join(report))

    def test_qid_definition_without_cell(self):
        self.write(
            "topics/example.md",
            "**懸置細節**\n"
            "- ⟨Q-09⟩ ❓ **待查證**（標 2026-08-01｜查 issue-1234、version-string）：說明\n",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("有懸置細節定義但無表格短標記引用", "\n".join(report))

    def test_wikilink_probe_target_missing(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 [[entities/nonexistent-page]]）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("指向不存在的頁面", "\n".join(report))

    def test_future_marked_date_fails(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-09-01｜查 issue-1234、version-string）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("未來日期", "\n".join(report))

    def test_review_not_after_marked_fails(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 issue-1234、version-string｜複 2026-08-01）"
            "｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("未晚於標記日", "\n".join(report))


class TestWarnChecks(_WikiCase):
    def test_overdue_marker_is_warn_not_fail(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-07-01｜查 issue-1234、version-string）｜**題目**：內文。",
        )
        ok, report = self.run_check(today=TODAY)
        self.assertTrue(ok, "\n".join(report))
        self.assertIn("已逾期", "\n".join(report))

    def test_single_short_probe_warns(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 x1）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        # 探針太短同時觸發 check4 FAIL（長度地板），確認 check7 的 WARN 訊息也出現
        self.assertIn("過短", "\n".join(report))


class TestQueueMode(_WikiCase):
    def test_queue_lists_overdue_sorted_and_capped(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-06-01｜查 issue-1234、version-string）｜**題目A**：內文。\n\n"
            "❓ **待查證**（標 2026-07-20｜查 issue-5678、other-string｜訊 2026-08-01）"
            "｜**題目B**：內文。\n",
        )
        entries = mod._overdue_entries(self.wiki_dir, TODAY)
        self.assertEqual(len(entries), 2)
        # 有訊欄者（題目B）應排在前面，即便逾期天數較短
        self.assertTrue(entries[0][0])


if __name__ == "__main__":
    unittest.main()


NL = chr(10)
_SIG = '❓ **待查證**（標 %s｜查 Electron、桌面應用｜訊 2026-08-20）｜**題**：內文'
_NOSIG = '❓ **待查證**（標 %s｜查 Electron、桌面應用）｜**題**：內文'


class QueueLaneSplitTest(_WikiCase):
    """--queue 兩條分流 + 產消對帳（2026-08-29 加入，同日 review 後補強）。

    初版測試把 15 筆標記全寫進同一頁，於是「Lane B 區段含該頁 slug」在
    **原始 bug 原封復活**（Lane B 改印合併排序前 5 筆）時照樣通過——
    review 的突變 M9 實證此漏。現在有訊／無訊分兩頁，斷言 Lane B 區段
    **不含**有訊頁，飢餓語意才真的被釘住。額度切片（M6/M7）、額度不可
    對調（M3）、產能非名目（P1-5）亦一併補上。
    """

    def _queue(self, today=date(2026, 8, 29), history_path=None):
        import io
        buf = io.StringIO()
        mod.print_queue(buf, wiki_dir=self.wiki_dir, today=today, history_path=history_path)
        return buf.getvalue()

    def _lane_sections(self, out):
        a = out.split("## Lane A")[1].split("## Lane B")[0]
        b = out.split("## Lane B")[1].split("總逾期數")[0]
        return a, b

    def _fill(self, n_sig, n_nosig, marked="2026-08-01"):
        if n_sig:
            self.write("topics/alpha.md", NL.join([_SIG % marked] * n_sig))
        if n_nosig:
            self.write("topics/bravo.md", NL.join([_NOSIG % marked] * n_nosig))

    def test_lane_b_is_not_starved_by_lane_a(self):
        """M9 殺手：Lane B 區段不得混入有訊頁。"""
        self._fill(n_sig=8, n_nosig=7)
        lane_a, lane_b = self._lane_sections(self._queue())
        self.assertIn("bravo", lane_b, "Lane B 必須排得進來")
        self.assertNotIn("alpha", lane_b, "Lane B 不得混入有訊筆（原始 bug 的形狀）")
        self.assertIn("alpha", lane_a)
        self.assertNotIn("bravo", lane_a)

    def test_lane_a_quota_caps_listing(self):
        """M6 殺手：額度切片必須生效。"""
        self._fill(n_sig=15, n_nosig=0)
        lane_a, _ = self._lane_sections(self._queue())
        self.assertEqual(lane_a.count("alpha"), mod.SIGNAL_LIMIT)

    def test_lane_b_quota_caps_listing(self):
        """M7 殺手。"""
        self._fill(n_sig=0, n_nosig=15)
        _, lane_b = self._lane_sections(self._queue())
        self.assertEqual(lane_b.count("bravo"), mod.QUEUE_LIMIT)

    def test_lane_quotas_are_not_interchangeable(self):
        """M3 殺手：兩個額度對調就失去分流意義（A 是便宜工作，額度必須較大）。"""
        self._fill(n_sig=15, n_nosig=15)
        lane_a, lane_b = self._lane_sections(self._queue())
        self.assertGreater(
            lane_a.count("alpha"), lane_b.count("bravo"),
            "Lane A（不需 web）額度必須大於 Lane B（需 web）"
        )

    def test_capacity_uses_actual_backlog_not_nominal_quota(self):
        """本輪實際可消 = min(積壓, 額度) 逐 Lane 相加；產能仍是名目值（見 print_queue 註解）。"""
        self._fill(n_sig=3, n_nosig=20)
        out = self._queue()
        self.assertIn("本輪實際可消 8 筆", out)

    # ---- 趨勢／歷史子系統（2026-08-29 第二輪 review：N8–N12、N15 全存活，此處補洞）----

    def _hist(self):
        return Path(self._tmp.name) / "hist.csv"

    def test_trend_line_reports_signed_delta_against_previous_snapshot(self):
        """N8 殺手：delta 反號會讓惡化印成改善——報表說謊比報錯更危險。"""
        self._fill(n_sig=0, n_nosig=7)
        h = self._hist()
        h.write_text("date,total,lane_a,lane_b,added_7d" + NL + "2026-08-22,3,0,3,3" + NL, encoding="utf-8")
        out = self._queue(history_path=h)
        self.assertIn("趨勢", out)
        self.assertIn("2026-08-22 3 筆", out)
        self.assertIn("今日 7 筆", out)
        self.assertIn("+4", out)

    def test_trend_reads_last_row_not_first(self):
        """N11 殺手。"""
        self._fill(n_sig=0, n_nosig=7)
        h = self._hist()
        h.write_text("date,total,lane_a,lane_b,added_7d" + NL
                     + "2026-08-01,99,0,99,0" + NL + "2026-08-22,3,0,3,3" + NL, encoding="utf-8")
        out = self._queue(history_path=h)
        trend = [l for l in out.splitlines() if "趨勢" in l][0]
        self.assertIn("2026-08-22 3 筆", trend)
        self.assertNotIn("2026-08-01", trend)

    def test_same_day_rerun_does_not_become_its_own_baseline(self):
        """P0-6 迴歸：同日重跑若拿今天當基準，趨勢永遠印（0），功能自我抵銷。"""
        self._fill(n_sig=0, n_nosig=7)
        h = self._hist()
        self._queue(history_path=h)          # 第一次寫入今日
        out = self._queue(history_path=h)    # 同日重跑
        self.assertNotIn("趨勢", out, "同日重跑不得以今日為基準")
        rows = [r for r in h.read_text(encoding="utf-8").splitlines() if r.startswith("2026-08-29")]
        self.assertEqual(len(rows), 1, "同日應 upsert 而非 append")

    def test_history_is_appended_with_expected_columns(self):
        """N10／N12 殺手：不寫檔＝序列永遠只有一列；欄序寫錯＝日後讀出來的是別的數字。"""
        self._fill(n_sig=8, n_nosig=7)
        h = self._hist()
        self._queue(history_path=h)
        lines = [r for r in h.read_text(encoding="utf-8").splitlines() if r]
        self.assertEqual(lines[0], "date,total,lane_a,lane_b,added_7d")
        self.assertEqual(lines[-1], "2026-08-29,15,8,7,0")

    def test_corrupt_history_degrades_to_no_trend_not_wrong_trend(self):
        """N15 殺手：讀壞掉的檔要回 None（不印），不可回一個假基準。"""
        self._fill(n_sig=0, n_nosig=7)
        h = self._hist()
        h.write_text("date,total" + NL + "garbage-row" + NL, encoding="utf-8")
        out = self._queue(history_path=h)
        self.assertNotIn("趨勢", out)

    def test_no_history_path_means_no_file_written(self):
        """print_queue 不傳 history_path 時必須是純函式（測試環境不得留檔）。"""
        self._fill(n_sig=0, n_nosig=7)
        self._queue()
        self.assertFalse(self._hist().exists())

    # ---- 截斷提示與排空預估（N1–N5 全存活，此處補洞）----

    def test_truncation_notice_counts_hidden_rows(self):
        """N1／N2／N3 殺手。"""
        self._fill(n_sig=14, n_nosig=12)
        out = self._queue()
        self.assertIn("另 4 筆未顯示", out)   # Lane A: 14 - 10
        self.assertIn("另 7 筆未顯示", out)   # Lane B: 12 - 5

    def test_no_truncation_notice_when_within_quota(self):
        self._fill(n_sig=3, n_nosig=3)
        self.assertNotIn("未顯示", self._queue())

    def test_drain_estimate_divides_lane_b_by_its_own_quota(self):
        """N4 殺手：除以 SIGNAL_LIMIT 會把 8.6 週算成 4.3 週，低估一半。"""
        self._fill(n_sig=0, n_nosig=20)
        out = self._queue()
        self.assertIn("Lane B 需約 4.0 週排空", out)   # 20 / QUEUE_LIMIT(5)

    def test_rate_window_boundary_is_exclusive_and_width_matters(self):
        """M4／M8 殺手：窗口寬度與邊界都要釘死。

        today=08-29、窗口 7 天 → cutoff=08-22，條件為 d > cutoff（不含當日）。
        佈局：08-28 兩筆（內）、08-22 一筆（邊界，不含）、08-09 一筆（窗外）。
        期望 added=2；`>` 改 `>=` 會變 3，窗口改 30 會變 4。
        """
        self.write("topics/win.md", NL.join(
            [_NOSIG % "2026-08-28"] * 2 + [_NOSIG % "2026-08-22"] + [_NOSIG % "2026-08-09"]
        ))
        out = self._queue()
        self.assertIn("近 7 天新增 2 筆", out)

    def test_rate_meter_warns_when_production_exceeds_capacity(self):
        self._fill(n_sig=0, n_nosig=30, marked="2026-08-27")
        out = self._queue()
        self.assertIn("產消對帳", out)
        self.assertIn("淨增", out)
        self.assertIn("產出快過消費", out)

    def test_rate_meter_silent_when_within_capacity(self):
        self._fill(n_sig=0, n_nosig=3, marked="2026-08-27")
        out = self._queue()
        self.assertIn("產消對帳", out)
        self.assertNotIn("產出快過消費", out)
