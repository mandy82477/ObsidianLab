"""table_census.py — 成長型態與機制判定的正確性測試。

2026-09-06 修正兩個假象：
1. `_growth()` 對無日期欄的表一律回報 `static`（讀起來像「已判定不會變」），
   實際上是「判不出來」——改回報 `unknown`。
2. `_mechanism()` 對通用節名（摘要／時序…）只要規則檔任何地方出現同名小標＋
   淘汰類關鍵詞就判「有」，命中的可能是別頁的規則。改為命中行必須同時出現
   該頁 slug／頁名，或落在該頁專屬規則節內。
"""
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import table_census as tc  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


class GrowthUnknown(unittest.TestCase):
    def test_無日期欄回報unknown_不是static(self):
        rows = ["| 風險 | 當前狀況 | 嚴重度 |", "| A | B | C |"]
        self.assertEqual(tc._growth(rows, has_date_col=False), "unknown")

    def test_有日期欄且可判定仍照舊分類(self):
        rows = [
            "| x | 2026-09-01 |",
            "| y | 2026-08-01 |",
            "| z | 2026-07-01 |",
        ]
        self.assertEqual(tc._growth(rows, has_date_col=True), "prepend")

    def test_有日期欄但證據不足仍回unknown(self):
        rows = ["| x | 無日期 |", "| y | 無日期 |"]
        self.assertEqual(tc._growth(rows, has_date_col=True), "unknown")

    def test_全站掃描不再輸出static(self):
        """static 字串整個從輸出詞彙表移除，不留半個殘值。"""
        pages = []
        for f in sorted((ROOT / "wiki").rglob("*.md")):
            slug = f.relative_to(ROOT / "wiki").as_posix()[:-3]
            if slug in tc.EXCLUDE or slug.startswith("_views/"):
                continue
            pages.append((slug, f))
        rows = tc.census(pages)
        self.assertNotIn("static", {r["growth"] for r in rows})


class MechanismPageScoped(unittest.TestCase):
    def test_anthropic_business_商業風險表為unknown(self):
        pages = [("topics/anthropic-business",
                   ROOT / "wiki" / "topics" / "anthropic-business.md")]
        rows = tc.census(pages)
        risk = [r for r in rows if r["section"].startswith("商業風險")]
        self.assertTrue(risk, "找不到「商業風險」表——頁面結構可能已變")
        self.assertEqual(risk[0]["growth"], "unknown")

    def test_anthropic_business_摘要表機制為無(self):
        """摘要表命中的是別頁通用規則（news-pipeline-steps、wiki-ingest-format 泛用條文），
        不含 anthropic-business 字樣，修正後不應算「有」。"""
        pages = [("topics/anthropic-business",
                   ROOT / "wiki" / "topics" / "anthropic-business.md")]
        rows = tc.census(pages)
        summary = [r for r in rows if r["section"] == "摘要"]
        self.assertTrue(summary)
        self.assertEqual(summary[0]["mechanism"], "無")

    def test_pricing_模型api定價現況表機制為有(self):
        pages = [("entities/pricing", ROOT / "wiki" / "entities" / "pricing.md")]
        rows = tc.census(pages)
        hit = [r for r in rows if r["section"].startswith("模型 API 定價現況")]
        self.assertTrue(hit, "找不到「模型 API 定價現況」表——頁面結構可能已變")
        self.assertEqual(hit[0]["mechanism"], "有（wiki-ingest-commercial.md）")

    def test_ai_agent_safety_現在會打到你的表機制為有(self):
        pages = [("topics/ai-agent-safety", ROOT / "wiki" / "topics" / "ai-agent-safety.md")]
        rows = tc.census(pages)
        hit = [r for r in rows if r["section"].startswith("現在會打到你的")]
        self.assertTrue(hit, "找不到「現在會打到你的」表——頁面結構可能已變")
        self.assertNotEqual(hit[0]["mechanism"], "無")


if __name__ == "__main__":
    unittest.main()
