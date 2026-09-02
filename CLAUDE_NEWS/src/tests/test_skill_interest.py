# -*- coding: utf-8 -*-
"""興趣類別 skill 榜（2026-09-03）：設定檔契約＋render 離線測試（不連網）。"""
import importlib.util
import json
import re
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "data" / "skill_interest_watch.json"
spec = importlib.util.spec_from_file_location("sis", ROOT / "scripts" / "skill_interest_snapshot.py")
sis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sis)




class TestConfigContract(unittest.TestCase):
    def setUp(self):
        self.cfg = json.loads(CONFIG.read_text(encoding="utf-8"))

    def test_slugs_unique_and_groups_valid(self):
        slugs = [c["slug"] for c in self.cfg["categories"]]
        self.assertEqual(len(slugs), len(set(slugs)))
        self.assertTrue(all(c["group"] in ("A", "B") for c in self.cfg["categories"]))

    def test_needs_calibration_has_no_queries_and_why(self):
        """誠實標未校準的類別：queries 必空、why 必說明——不得偷塞寬 query。"""
        for c in self.cfg["categories"]:
            if c.get("status") == "needs_calibration":
                self.assertEqual(c["queries"], [], c["slug"])
                self.assertTrue(c.get("why"), c["slug"])
            else:
                self.assertTrue(c["queries"], f"{c['slug']} active 卻無 query")

    def test_active_queries_are_scoped(self):
        """每條 query 必含 in: 或 topic: 限定，避免 README 全文命中。"""
        for c in self.cfg["categories"]:
            for q in c["queries"]:
                self.assertTrue("in:" in q or "topic:" in q, q)

    def test_group_a_has_section_label_not_anchor(self):
        """A 組連頁＋「第 N 段」文字，不得寫錨點（段標題帶會變的標記，錨定必腐化）。"""
        for c in self.cfg["categories"]:
            self.assertNotIn("guide_anchor", c, c["slug"])
            if c["group"] == "A":
                self.assertRegex(c.get("guide_section") or "", r"^第 \S+ 段$", c["slug"])


class TestRender(unittest.TestCase):
    def test_render_cold_start_and_disabled(self):
        cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
        data = {c["slug"]: {"repos": {}, "per_query": []} for c in cfg["categories"]}
        data["planning"]["repos"] = {"https://github.com/github/spec-kit": {
            "full_name": "github/spec-kit", "html_url": "https://github.com/github/spec-kit",
            "stargazers_count": 133049, "description": "Spec-Driven | Development"}}
        data["planning"]["per_query"] = [("q", 1)]
        orig = sis.STAR_HISTORY
        try:
            sis.STAR_HISTORY = ROOT / "data" / "_no_such_history.csv"
            md = sis.render(cfg, data, datetime(2026, 9, 3, tzinfo=timezone.utc))
        finally:
            sis.STAR_HISTORY = orig
        self.assertIn("冷啟動", md)                       # 星史不足 → 明寫，不留白
        self.assertIn("尚未校準出有辨識力", md)             # 未校準類別 → ⚠️ 不裝正常
        self.assertIn("| [github/spec-kit]", md)
        self.assertIn("Spec-Driven ／ Development", md)   # 儲存格 | 轉義
        self.assertIn("**最後更新：** 2026-09-03", md)


if __name__ == "__main__":
    unittest.main()
