# -*- coding: utf-8 -*-
"""devpractice_diff.py 的迴歸測試。

真實踩過的坑（2026-09-02 首跑）：
- repo root 在 CLAUDE_NEWS 上一層，diff 標頭是 `CLAUDE_NEWS/wiki/log.md`，
  EXCLUDE 用相等比對永遠不命中 → 編輯部日誌混進候選訊號。
- 基準線退回不可用 reflog（HEAD@{...}）——雲端 fresh clone 的 reflog 是空的。
"""
import importlib.util
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "devpractice_diff.py"

spec = importlib.util.spec_from_file_location("devpractice_diff", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class TestExclude(unittest.TestCase):
    def test_exclude_matches_prefixed_paths(self):
        """log.md / index.md 即使帶 repo 前綴也要被排除。"""
        for e in mod.EXCLUDE:
            self.assertTrue(f"CLAUDE_NEWS/{e}".endswith(e))
        src = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("endswith", src, "排除比對必須用 endswith（diff 路徑帶 repo 前綴）")

    def test_no_reflog_syntax(self):
        """雲端 fresh clone 的 reflog 是空的，禁用 HEAD@{...} 語法。"""
        src = SCRIPT.read_text(encoding="utf-8")
        self.assertNotIn("HEAD@{", src)


class TestStateRoundtrip(unittest.TestCase):
    def test_base_sha_fallback_on_bad_state(self):
        """狀態檔壞掉（非 JSON／sha 不存在）→ 退回 fallback，不炸。"""
        orig = mod.STATE
        try:
            mod.STATE = ROOT / "data" / "_devpractice_state_test.json"
            mod.STATE.write_text("not json", encoding="utf-8")
            sha, origin = mod._base_sha()
            self.assertEqual(origin, "fallback-48h")
            mod.STATE.write_text(json.dumps({"last_sha": "0" * 40}), encoding="utf-8")
            sha, origin = mod._base_sha()
            self.assertEqual(origin, "fallback-48h")
        finally:
            if mod.STATE.exists():
                mod.STATE.unlink()
            mod.STATE = orig

    def test_cli_show_runs(self):
        """show 在真 repo 上跑得動且 exit 0（有無新增皆為正常結果）。"""
        r = subprocess.run(
            [sys.executable, str(SCRIPT), "show"], cwd=ROOT,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("基準線：", r.stdout)
        # 編輯部日誌不得出現在輸出的檔案分組標題裡
        self.assertNotRegex(r.stdout, re.compile(r"^## .*wiki/log\.md", re.M))


if __name__ == "__main__":
    unittest.main()
