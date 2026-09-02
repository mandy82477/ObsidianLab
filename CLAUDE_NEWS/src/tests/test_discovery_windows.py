# -*- coding: utf-8 -*-
"""發現窗 Phase 1（2026-09-03）迴歸測試：D 窗主題閘、產消對帳、星史記錄端。

鎖住的真實案例：
- Understand-Anything（HN 169 分、標題無 claude、repo 描述含 Works with Claude Code）
  必須過 D 窗主題閘——這是 D 窗存在的唯一理由，此斷言失守整個窗白做。
- 對帳 CSV「窗沒跑」與「今天沒候選」必須分得開（逐窗缺列偵測的資料前提）。
"""
import importlib.util
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from news_aggregator.sources import github_releases as gr
from news_aggregator.sources.hn_repo_bridge import _GH_REPO_RE, _SCOPE_TERMS


class TestDWindowScopeGate(unittest.TestCase):
    def _in_scope(self, description="", topics=(), homepage=""):
        hay = " ".join([description, " ".join(topics), homepage]).lower()
        return any(t in hay for t in _SCOPE_TERMS)

    def test_understand_anything_passes(self):
        """歷史回測錨點：標題無 claude、描述有 Works with Claude Code → 必須過閘。"""
        self.assertTrue(self._in_scope(
            "Graphs that teach > graphs that impress. Turn any code into an "
            "interactive knowledge graph. Works with Claude Code, Codex, Cursor."))

    def test_topics_only_passes(self):
        """描述無關鍵字但 topics 標了 claude-code → 過閘（topics 是新資訊面）。"""
        self.assertTrue(self._in_scope("A fast code indexer.", topics=("claude-code", "cli")))

    def test_unrelated_repo_blocked(self):
        """跟 Claude 無關的高分 repo → 擋下（主題邊界零放寬）。"""
        self.assertFalse(self._in_scope(
            "A blazingly fast game engine written in Rust.", topics=("gamedev", "rust")))

    def test_bare_agent_not_enough(self):
        """單獨 agent 字樣不得過閘（會灌入通用 AI agent 生態）。"""
        self.assertFalse(self._in_scope("An autonomous agent framework for browsing."))

    def test_repo_url_regex(self):
        self.assertTrue(_GH_REPO_RE.match("https://github.com/tt-a1i/archify"))
        self.assertTrue(_GH_REPO_RE.match("https://github.com/a/b/"))
        self.assertFalse(_GH_REPO_RE.match("https://github.com/a/b/issues/3"))
        self.assertFalse(_GH_REPO_RE.match("https://gist.github.com/a/b"))


class TestQueueAccounting(unittest.TestCase):
    def setUp(self):
        self.orig = gr.NEWS_DIR
        self.tmp = ROOT / "data" / "_test_dq"
        (self.tmp / "data").mkdir(parents=True, exist_ok=True)
        gr.NEWS_DIR = self.tmp / "news"  # NEWS_DIR.parent/data = tmp/data

    def tearDown(self):
        gr.NEWS_DIR = self.orig
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_per_window_upsert(self):
        now = datetime(2026, 9, 3, tzinfo=timezone.utc)
        gr._record_queue("rising", 10, 3, now)
        gr._record_queue("hn_bridge", 5, 3, now)
        gr._record_queue("rising", 12, 3, now)  # 同日同窗 upsert
        lines = (self.tmp / "data" / "discovery_queue_history.csv").read_text(
            encoding="utf-8").strip().splitlines()
        self.assertEqual(lines[0], "date,window,queued,emitted,note")
        rising = [l for l in lines if ",rising," in l]
        self.assertEqual(rising, ["2026-09-03,rising,12,3,ok"])
        # 不同窗互不覆蓋——「窗沒跑」（缺列）與「沒候選」（queued=0）由此分得開
        self.assertEqual(len([l for l in lines if ",hn_bridge," in l]), 1)

    def test_star_history_upsert_and_retention(self):
        now = datetime(2026, 9, 3, tzinfo=timezone.utc)
        hist = self.tmp / "data" / "repo_star_history.csv"
        hist.write_text(
            "date,repo_url,stars\n"
            "2026-01-01,https://github.com/old/gone,10\n"      # 逾 60 天 → 汰除
            "2026-09-03,https://github.com/a/b,100\n",          # 同日 upsert
            encoding="utf-8")
        gr._record_star_history({"https://github.com/a/b": 120,
                                 "https://github.com/c/d": 50}, now)
        text = hist.read_text(encoding="utf-8")
        self.assertNotIn("old/gone", text)
        self.assertIn("2026-09-03,https://github.com/a/b,120", text)
        self.assertNotIn(",100", text)
        self.assertIn("https://github.com/c/d,50", text)


if __name__ == "__main__":
    unittest.main()
