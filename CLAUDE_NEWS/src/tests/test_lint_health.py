# -*- coding: utf-8 -*-
"""lint_health.py 的契約：密度量測、突變測試、命中帳、漏抓帳。

守的是「lint 進化迴路的四個訊號源各自能產出正確訊號」——
特別是突變測試必須抓得到恆真 pattern（2026-09-04 實例：`——` 散文出現 60 次）。
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import lint_health as lh  # noqa: E402


class Density(unittest.TestCase):
    def test_量測與門檻(self):
        d = Path(tempfile.mkdtemp())
        f = d / "r.md"
        f.write_text("# x `[加入: 2026-01-01]`\n" + "踩過\n" * 3 + "normal\n" * 10, encoding="utf-8")
        rows = lh.density_rows([f])
        self.assertEqual(rows[0]["lines"], 14)
        self.assertEqual(rows[0]["marks"], 1)
        self.assertEqual(rows[0]["lesson_lines"], 3)
        self.assertTrue(lh.density_candidates(rows, 300, 20, 5.0))   # 教訓 21% 超門檻
        self.assertFalse(lh.density_candidates(rows, 300, 20, 50.0))


class Mutate(unittest.TestCase):
    def test_恆真_pattern_被抓到(self):
        d = Path(tempfile.mkdtemp())
        (d / "a.md").write_text("規則——說明——另一句——\n- **值**——說明\n", encoding="utf-8")
        old_root = lh.REPO_ROOT
        lh.REPO_ROOT = d
        try:
            reg = {"sync_pairs": [
                {"name": "裝飾 pattern", "assertion": "all_contain", "files": ["a.md"], "patterns": ["——"]},
                {"name": "精確 pattern", "assertion": "all_contain", "files": ["a.md"], "patterns": ["\\*\\*值\\*\\*——說明"]},
            ]}
            weak = lh.mutate_pairs(reg)
        finally:
            lh.REPO_ROOT = old_root
        # 抹掉所有 `——` 後 all_contain 必紅；本測試確認精確 pattern 與裝飾 pattern 都會在突變後轉紅
        # （裝飾 pattern 的問題在「同檔散文也能滿足」——那由真實 registry 上的 mutate 命令暴露：
        #   若 re.sub 抹掉命中後仍能匹配，代表 pattern 形狀與內容脫鉤）
        self.assertEqual(weak, [])

    def test_抹不乾淨的_pattern_會被回報(self):
        # 一個抹掉命中後仍能被其他文字滿足的 pattern：`.` 任意字元
        d = Path(tempfile.mkdtemp())
        (d / "a.md").write_text("abc\n", encoding="utf-8")
        old_root = lh.REPO_ROOT
        lh.REPO_ROOT = d
        try:
            reg = {"sync_pairs": [{"name": "任意", "assertion": "all_contain", "files": ["a.md"], "patterns": ["."]}]}
            weak = lh.mutate_pairs(reg)
        finally:
            lh.REPO_ROOT = old_root
        self.assertEqual(len(weak), 1)


class Broad(unittest.TestCase):
    def test_過寬_pattern_被回報(self):
        d = Path(tempfile.mkdtemp())
        (d / "a.md").write_text("——\n" * 12 + "- **值**——說明\n", encoding="utf-8")
        old_root = lh.REPO_ROOT
        lh.REPO_ROOT = d
        try:
            reg = {"sync_pairs": [{"name": "破折號", "assertion": "all_contain", "files": ["a.md"], "patterns": ["——"]}]}
            weak = lh.mutate_pairs(reg)
        finally:
            lh.REPO_ROOT = old_root
        self.assertEqual(len(weak), 1)
        self.assertIn("過寬", weak[0]["reason"])


class Hits(unittest.TestCase):
    def test_零命中連續輪數(self):
        rows = [
            {"date": "2026-08-01", "steps": {"5c": 3, "6a": 0}},
            {"date": "2026-08-08", "steps": {"5c": 0, "6a": 0}},
            {"date": "2026-08-15", "steps": {"5c": 0, "6a": 1}},
        ]
        s = lh.zero_streaks(rows)
        self.assertEqual(s["5c"], 2)
        self.assertEqual(s["6a"], 0)

    def test_step_args_解析(self):
        self.assertEqual(lh.parse_step_args(["5c=9", "6a=1"]), {"5c": 9, "6a": 1})


class Misses(unittest.TestCase):
    def test_why_受限(self):
        self.assertIn("考卷外", lh.WHY_VALUES)
        self.assertEqual(len(lh.WHY_VALUES), 4)


if __name__ == "__main__":
    unittest.main()
