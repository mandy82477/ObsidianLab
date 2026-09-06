"""HN D 窗（高分榜補撈）：關鍵字閘的漏球補救。

存在理由：HN 來源以四個關鍵字 query 打 Algolia，標題／內文不含
claude/anthropic 的東西**從來不會被抓過**，分數再高也一樣。
2026-05-01 的 Understand-Anything（169 分、49 留言、repo 描述明寫
Works with Claude Code）就是這樣掉的，靠使用者質疑才發現。

這些測試釘的是「判準不可放寬」——D 窗一旦把非 GitHub 連結或
描述無關的東西放進來，它就從補救變成噪音源。
"""
import unittest

import news_aggregator.sources.hackernews as mod


class TestRepoUrlParsing(unittest.TestCase):
    def test_accepts_plain_repo_url(self):
        self.assertEqual(mod._gh_repo("https://github.com/Lum1104/Understand-Anything"),
                         "Lum1104/Understand-Anything")

    def test_strips_git_suffix_and_query(self):
        self.assertEqual(mod._gh_repo("https://github.com/a/b.git"), "a/b")
        self.assertEqual(mod._gh_repo("https://github.com/a/b?tab=readme"), "a/b")

    def test_rejects_non_repo_github_paths(self):
        """github.com/topics/... 這類不是 repo，抓下去只會浪費 API 額度。"""
        for url in ("https://github.com/topics/ai", "https://github.com/orgs/anthropics",
                    "https://github.com/pricing", "https://github.com/anthropics"):
            self.assertIsNone(mod._gh_repo(url), url)

    def test_rejects_non_github(self):
        for url in ("", "https://example.com/a/b", "https://gitlab.com/a/b"):
            self.assertIsNone(mod._gh_repo(url), url)


class TestInScopeMatching(unittest.TestCase):
    """判準是 repo 描述／topics 出現 claude 或 anthropic——確定性規則，無需 LLM。"""

    def test_matches_understand_anything_shaped_description(self):
        self.assertTrue(mod._INSCOPE_RE.search(
            "Turn any code into a knowledge graph. Works with Claude Code, Codex, Cursor."))

    def test_matches_topic_only(self):
        self.assertTrue(mod._INSCOPE_RE.search("ai-agents claude digital-twin"))

    def test_does_not_match_generic_agent_tooling(self):
        """agent／skills 生態但與 Claude 無關者不得入場——本庫 scope 綁 Claude。"""
        for blob in ("A library of agent skills for CAD, CAE and CAM",
                     "A SOTA quantization toolkit for low-bit LLM inference",
                     "Safe(ish) C programming library"):
            self.assertIsNone(mod._INSCOPE_RE.search(blob), blob)


class TestQuotaGuards(unittest.TestCase):
    def test_score_floor_is_highscore_tier(self):
        """降門檻會讓母體與 API 呼叫量一起爆——14 天實測 ≥100 分平均每日只需 2.1 次呼叫。"""
        self.assertGreaterEqual(mod.D_MIN_SCORE, 100)

    def test_lookup_cap_exists_and_is_bounded(self):
        self.assertTrue(0 < mod.D_MAX_LOOKUPS <= 100)


if __name__ == "__main__":
    unittest.main()
