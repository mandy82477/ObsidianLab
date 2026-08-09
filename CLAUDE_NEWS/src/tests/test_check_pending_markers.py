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
