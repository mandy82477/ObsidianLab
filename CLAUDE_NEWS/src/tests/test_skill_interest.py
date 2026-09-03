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

    def test_no_site_ops_group(self):
        """原 C 組（本站抓料工具規模榜）2026-09-03 使用者裁決下架：營運參考不是讀者內容，不進 wiki。
        設定只能留在 _rejected，不得回到 categories；總覽頁不得再印它。"""
        self.assertFalse(any(c.get("group") == "C" for c in self.cfg["categories"]))
        md = sis.render(self.cfg, {c["slug"]: {"repos": {}, "per_query": []} for c in self.cfg["categories"]},
                        datetime(2026, 9, 3, tzinfo=timezone.utc))
        self.assertNotIn("資料源韌性", md)
        self.assertFalse(hasattr(sis, "render_site"))
        self.assertFalse((sis.ROOT / "wiki" / "topics" / "site-source-tooling.md").exists())

    def test_retired_has_no_queries_and_bridge(self):
        """retired 類別：queries 必空、why 必說明、且必有指路（tools_symptom 或 tools_note）——
        不得偷塞寬 query 重上線，也不得撤下後讓需求無處可去。"""
        for c in self.cfg["categories"]:
            if c.get("status") == "retired":
                self.assertEqual(c["queries"], [], c["slug"])
                self.assertTrue(c.get("why"), c["slug"])
                self.assertTrue(c.get("tools_symptom") or c.get("tools_note"), f"{c['slug']} 撤下卻無指路")
            else:
                self.assertTrue(c["queries"], f"{c['slug']} active 卻無 query")

    def test_bridge_symptoms_exist_in_decision_table(self):
        """單向橋對帳：tools_symptom 必須是決策表症狀句原文（check_spokes 同源）。"""
        import importlib.util as iu
        spec2 = iu.spec_from_file_location("ctp", ROOT / "scripts" / "check_tools_page.py")
        ctp = iu.module_from_spec(spec2); spec2.loader.exec_module(ctp)
        text = ctp.PAGE.read_text(encoding="utf-8")
        fails = [f for f in ctp.check_spokes(text, ctp.PAGE.parent.parent) if "榜橋" in f]
        self.assertEqual(fails, [])
        # 改壞驗紅：塞一個不存在的症狀句，check_spokes 必須抓到
        bad = json.loads(CONFIG.read_text(encoding="utf-8"))
        bad["categories"][0]["tools_symptom"] = "這句不在決策表"
        tmp = ROOT / "data" / "_tmp_siw.json"
        tmp.write_text(json.dumps(bad, ensure_ascii=False), encoding="utf-8")
        try:
            wiki_dir = ROOT / "wiki"
            import shutil
            backup = CONFIG.read_text(encoding="utf-8")
            CONFIG.write_text(tmp.read_text(encoding="utf-8"), encoding="utf-8")
            try:
                fails = [f for f in ctp.check_spokes(text, wiki_dir) if "榜橋" in f]
                self.assertTrue(fails, "塞錯症狀句 check_spokes 未轉紅")
            finally:
                CONFIG.write_text(backup, encoding="utf-8")
        finally:
            tmp.unlink(missing_ok=True)

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
        self.assertIn("## 我卡在這裡（決策表）", md)        # 決策表機械抄自 tools 頁
        self.assertIn("| 我的症狀 | 先裝這個 |", md)        # 抄本有表頭（tools 頁契約）
        self.assertIn("**本庫判斷**", md)                  # 每類判斷區塊
        self.assertIn("規模榜：無", md)                    # retired 類只印判斷、不掛空榜
        self.assertNotIn("本庫判斷 →", md)                 # 舊式指路橋已由抄錄取代
        self.assertIn("| [github/spec-kit]", md)
        self.assertIn("Spec-Driven ／ Development", md)   # 儲存格 | 轉義
        self.assertIn("**最後更新：** 2026-09-03", md)


if __name__ == "__main__":
    unittest.main()
