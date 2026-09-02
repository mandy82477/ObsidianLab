"""scripts/source_scorecard.py 的確定性單元測試（不讀真實 data/，全部用暫存 fixture）。"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPT = REPO_ROOT / "scripts" / "source_scorecard.py"

spec = importlib.util.spec_from_file_location("source_scorecard", SCRIPT)
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)


class TestFormulas(unittest.TestCase):
    def test_smoothed_rate_pulls_small_sample_to_prior(self):
        # lobste.rs 式小樣本：2 抓 1 中（原始 50%）被拉向全站基準 20%
        r = sc.smoothed_rate(1, 2, prior_rate=0.2, k=20)
        self.assertAlmostEqual(r, (1 + 20 * 0.2) / 22)
        self.assertLess(r, 0.3)  # 遠低於原始 50%

    def test_smoothed_rate_large_sample_dominates_prior(self):
        r = sc.smoothed_rate(500, 1000, prior_rate=0.2, k=20)
        self.assertGreater(r, 0.49)

    def test_smoothed_rate_zero_trials_returns_prior(self):
        self.assertEqual(sc.smoothed_rate(0, 0, prior_rate=0.15, k=20), 0.15)

    def test_wilson_lower_small_sample_below_point_estimate(self):
        # 2 中 1（點估計 50%）的 Wilson 下界必須大幅低於 50%
        self.assertLess(sc.wilson_lower(1, 2), 0.15)

    def test_wilson_lower_monotone_in_sample_size(self):
        # 同比例下，樣本越大下界越接近點估計
        self.assertLess(sc.wilson_lower(5, 10), sc.wilson_lower(50, 100))

    def test_wilson_lower_zero_trials(self):
        self.assertEqual(sc.wilson_lower(0, 0), 0.0)

    def test_hhi(self):
        self.assertAlmostEqual(sc.hhi([0.5, 0.5]), 0.5)
        self.assertAlmostEqual(sc.hhi([1.0]), 1.0)
        self.assertAlmostEqual(sc.hhi([0.25] * 4), 0.25)


class TestDomainLookup(unittest.TestCase):
    SCORES = {"reuters.com": 1.0, "theverge.com": 0.8}

    def test_exact_match(self):
        self.assertEqual(sc.lookup_pc1("https://reuters.com/a", self.SCORES), 1.0)

    def test_strips_www_and_subdomain(self):
        self.assertEqual(sc.lookup_pc1("https://www.reuters.com/x", self.SCORES), 1.0)
        self.assertEqual(sc.lookup_pc1("https://news.reuters.com/x", self.SCORES), 1.0)

    def test_unknown_domain_returns_none(self):
        self.assertIsNone(sc.lookup_pc1("https://example-blog.dev/post", self.SCORES))

    def test_bucket_boundaries(self):
        self.assertEqual(sc.pc1_bucket(None), "unknown")
        self.assertEqual(sc.pc1_bucket(0.7), "high")
        self.assertEqual(sc.pc1_bucket(0.4), "mid")
        self.assertEqual(sc.pc1_bucket(0.39), "low")


class TestLoaders(unittest.TestCase):
    def test_funnel_dedupes_same_date_by_max_gathered(self):
        rows = [
            {"date": "2026-07-13", "mode": "backfill", "totals": {"gathered": 5},
             "sources": {"Hacker News": {"gathered": 5, "filtered": 4, "emitted": 2}}},
            {"date": "2026-07-13", "mode": "gather", "totals": {"gathered": 80},
             "sources": {"Hacker News": {"gathered": 14, "filtered": 13, "emitted": 6}}},
            {"date": "2026-07-12", "mode": "gather", "totals": {"gathered": 70},
             "sources": {"Hacker News": {"gathered": 10, "filtered": 9, "emitted": 5}}},
        ]
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "funnel.jsonl"
            p.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
            funnel = sc.load_funnel(p)
        self.assertEqual(funnel["days"], 2)
        hn = funnel["per_source"]["Hacker News"]
        self.assertEqual(hn["gathered"], 24)  # 14（同日取大者）+ 10，backfill 的 5 不重複計
        self.assertEqual(hn["emitted"], 11)

    def test_missing_files_yield_empty(self):
        missing = Path(tempfile.gettempdir()) / "nonexistent_scorecard_fixture.jsonl"
        self.assertEqual(sc.load_funnel(missing)["days"], 0)
        self.assertEqual(sc.load_attribution(missing), [])
        self.assertEqual(sc.load_domain_scores(missing), {})


class TestRegistryIntegrity(unittest.TestCase):
    """registry 是名稱↔slug 的單一真相源：與 main.py 註冊清單、shared.md slug 對照表保持一致。"""

    @classmethod
    def setUpClass(cls):
        cls.registry = sc.load_registry()
        cls.by_name = {s["name"]: s for s in cls.registry}

    def test_no_duplicate_names_or_slugs(self):
        names = [s["name"] for s in self.registry]
        slugs = [s["slug"] for s in self.registry]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(len(slugs), len(set(slugs)))

    def test_required_fields_and_enums(self):
        for s in self.registry:
            self.assertIn(s["score_reliability"], {"trusted", "untrusted", "none"}, s["name"])
            self.assertIn(s["curation_mode"], {"score", "content", "whitelist"}, s["name"])
            self.assertIsInstance(s["active"], bool, s["name"])

    def test_covers_main_py_registered_sources(self):
        main_py = (REPO_ROOT / "src" / "news_aggregator" / "main.py").read_text(encoding="utf-8")
        # pipeline=false 的通道（如 user-query 使用者提問）無 fetch 程式，不在 main.py
        active_names = {s["name"] for s in self.registry if s["active"] and s.get("pipeline", True)}
        for name in active_names:
            self.assertIn(f'("{name}"', main_py, f"registry 標 active 的來源 {name} 不在 main.py sources 清單")

    def test_render_fairness_rules(self):
        """公道性三規則：零樣本顯示 —、dev.to 收錄率帶 †、whitelist 組不參與排名表。"""
        funnel = {"days": 20, "dates": ("2026-07-01", "2026-07-20"), "per_source": {
            "Hacker News": {"gathered": 100, "filtered": 80, "emitted": 50, "days_seen": 20},
            "dev.to": {"gathered": 90, "filtered": 80, "emitted": 40, "days_seen": 20},
            "Claude API Release Notes": {"gathered": 0, "filtered": 0, "emitted": 0, "days_seen": 20},
            "Anthropic Blog": {"gathered": 2, "filtered": 2, "emitted": 1, "days_seen": 20},
        }}
        result = sc.compute(self.registry, funnel, [], {})
        md = sc.render_markdown(result)

        ranked_section = md.split("## 官方 / 白名單來源")[0]
        whitelist_section = md.split("## 官方 / 白名單來源")[1]
        # whitelist 來源只出現在保險組，不進排名表
        self.assertNotIn("Anthropic Blog", ranked_section)
        self.assertIn("| Anthropic Blog |", whitelist_section)
        self.assertIn("| Claude API Release Notes |", whitelist_section)
        # dev.to（rate_comparable=false）收錄率帶 † 且有腳註
        devto_line = next(l for l in ranked_section.splitlines() if l.startswith("| dev.to"))
        self.assertIn("%†", devto_line)
        self.assertIn("† 抓法為跨日重覆視窗", ranked_section)
        # HN（rate_comparable 預設 true）不帶 †
        hn_line = next(l for l in ranked_section.splitlines() if l.startswith("| Hacker News"))
        self.assertNotIn("†", hn_line)

    def test_render_zero_gathered_shows_dash_not_prior(self):
        """零樣本來源不得顯示平滑先驗值（會被誤讀為實測）。以 content 來源驗證 — 邏輯。"""
        funnel = {"days": 20, "dates": ("2026-07-01", "2026-07-20"), "per_source": {
            "Hacker News": {"gathered": 100, "filtered": 80, "emitted": 50, "days_seen": 20},
            "Google News": {"gathered": 0, "filtered": 0, "emitted": 0, "days_seen": 20},
        }}
        result = sc.compute(self.registry, funnel, [], {})
        md = sc.render_markdown(result)
        gn_line = next(l for l in md.splitlines() if l.startswith("| Google News"))
        self.assertIn("| — | — | — |", gn_line)

    def test_compute_end_to_end_with_fixtures(self):
        funnel = {"days": 3, "dates": ("2026-07-11", "2026-07-13"),
                  "per_source": {"Hacker News": {"gathered": 40, "filtered": 30, "emitted": 15, "days_seen": 3}}}
        attribution = [
            {"source": "hacker-news", "item_url": "https://reuters.com/a"},
            {"source": "hacker-news", "item_url": "https://unknown.dev/b"},
            {"source": "mystery-slug", "item_url": "https://x.test/c"},
        ]
        result = sc.compute(self.registry, funnel, attribution, {"reuters.com": 1.0})
        hn = next(r for r in result["sources"] if r["slug"] == "hacker-news")
        self.assertEqual(hn["wiki_hits"], 2)
        self.assertFalse(hn["low_sample"] and hn["days_seen"] >= 14)  # 3 天必為樣本不足
        self.assertTrue(hn["low_sample"])
        self.assertIn("mystery-slug", result["unknown_slugs"])
        md = sc.render_markdown(result)
        self.assertIn("Hacker News", md)
        self.assertIn("mystery-slug", md)


if __name__ == "__main__":
    unittest.main()
