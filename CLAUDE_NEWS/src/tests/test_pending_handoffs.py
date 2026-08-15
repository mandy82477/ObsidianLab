"""Tests for scripts/pending_handoffs.py — 記者間轉知帳本。

守的是四件事：開立冪等、結案是 append 不是改寫、只列 open、派工附件無則印「無」。
"""
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

ph = load_script_module("pending_handoffs")


class TestLedger(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.path = Path(self._tmp.name) / "pending-handoffs.jsonl"

    def tearDown(self):
        self._tmp.cleanup()

    def test_open_is_idempotent_and_close_appends(self):
        a = ph.open_handoff("社群", "功能", "topics/official-community-gap", "評估矩陣新增列：X",
                            opened="2026-08-15", path=self.path)
        b = ph.open_handoff("社群", "功能", "topics/official-community-gap", "評估矩陣新增列：X",
                            opened="2026-08-15", path=self.path)
        self.assertEqual(a, b)
        self.assertEqual(len(self.path.read_text(encoding="utf-8").splitlines()), 1)
        self.assertEqual(len(ph.open_items(self.path)), 1)

        ph.close_handoff(a, "功能", "已補列", closed="2026-08-16", path=self.path)
        lines = self.path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2, "結案必須 append 新行，不可改寫開立行")
        self.assertEqual(ph.open_items(self.path), [])
        self.assertEqual(ph.load(self.path)[a]["status"], "done")
        with self.assertRaises(SystemExit):
            ph.close_handoff(a, "功能", "再結一次", path=self.path)

    def test_same_category_rejected(self):
        with self.assertRaises(SystemExit):
            ph.open_handoff("功能", "功能", "x", "n", path=self.path)

    def test_render_groups_by_target_and_flags_stale(self):
        self.assertEqual(ph.render([]), "無")
        ph.open_handoff("安全政策", "功能", "entities/claude-code", "issue #1 併入已知問題",
                        opened="2026-07-20", path=self.path)
        ph.open_handoff("模型", "商業", "entities/pricing", "新模型定價待記", opened="2026-08-14",
                        path=self.path)
        text = ph.render(ph.open_items(self.path), today=date(2026, 8, 15))
        self.assertIn("→ 功能 記者", text)
        self.assertIn("→ 商業 記者", text)
        self.assertIn("⚠️ 逾 14 天", text)
        self.assertEqual(text.count("⚠️ 逾 14 天"), 1)
        only = ph.render(ph.open_items(self.path, to="人物"))
        self.assertEqual(only, "無")


if __name__ == "__main__":
    unittest.main()
