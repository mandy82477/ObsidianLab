# -*- coding: utf-8 -*-
"""resolve_append_only.py：白名單契約＋union 合併行為（用臨時 git repo 實測，不碰本庫）。"""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "resolve_append_only.py"
spec = importlib.util.spec_from_file_location("rao", SCRIPT)
rao = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rao)


class TestWhitelist(unittest.TestCase):
    def test_only_append_only_files(self):
        """白名單裡不得出現會被改寫既有行的檔（index/頁面/設定）。"""
        for p in rao.APPEND_ONLY:
            self.assertTrue(p.endswith((".md", ".jsonl", ".log")), p)
            self.assertNotIn("index.md", p)
            self.assertNotIn("topics/", p)
            self.assertNotIn("entities/", p)
        self.assertIn("CLAUDE_NEWS/wiki/log.md", rao.APPEND_ONLY)
        self.assertNotIn("CLAUDE_NEWS/src/news_aggregator/emitted_items.json", rao.APPEND_ONLY)


class TestUnionMerge(unittest.TestCase):
    def _git(self, cwd, *args):
        return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                              encoding="utf-8", check=True)

    def test_union_keeps_both_appends_in_order(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            g = lambda *a: self._git(d, *a)
            g("init", "-q", "-b", "master")
            g("config", "user.email", "t@t"); g("config", "user.name", "t")
            f = d / "log.md"
            f.write_text("## base\n", encoding="utf-8"); g("add", "."); g("commit", "-qm", "base")
            g("checkout", "-qb", "cloud")
            f.write_text("## base\n## cloud-append\n", encoding="utf-8"); g("commit", "-qam", "cloud")
            g("checkout", "-q", "master")
            f.write_text("## base\n## local-append\n", encoding="utf-8"); g("commit", "-qam", "local")
            g("checkout", "-q", "cloud")
            r = subprocess.run(["git", "rebase", "master"], cwd=d, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0, "預期 rebase 衝突")
            # 在臨時 repo 內模擬本腳本的 union 合併
            orig_repo, orig_wl = rao.REPO, rao.APPEND_ONLY
            try:
                rao.REPO = d
                rao.APPEND_ONLY = {"log.md"}
                self.assertEqual(rao.conflicted_paths(), ["log.md"])
                rao.resolve_union("log.md")
            finally:
                rao.REPO, rao.APPEND_ONLY = orig_repo, orig_wl
            merged = f.read_text(encoding="utf-8")
            self.assertIn("## local-append", merged)
            self.assertIn("## cloud-append", merged)
            self.assertNotIn("<<<<<<<", merged)
            self.assertLess(merged.index("## base"), merged.index("## local-append"))
            subprocess.run(["git", "-c", "core.editor=true", "rebase", "--continue"],
                           cwd=d, capture_output=True, text=True, check=True)

    def test_refuses_outside_whitelist(self):
        """白名單外的衝突 → exit 1 且不動檔（那是需要人判斷的）。"""
        orig = rao.conflicted_paths
        try:
            rao.conflicted_paths = lambda: ["CLAUDE_NEWS/wiki/index.md", "CLAUDE_NEWS/wiki/log.md"]
            self.assertEqual(rao.main(["--check"]), 1)
        finally:
            rao.conflicted_paths = orig


if __name__ == "__main__":
    unittest.main()
