"""GitHub Search two-pass query tests (new-repo window + rising window).

The rising pass exists because created:>{26h} only sees brand-new repos
(almost always 0-5 stars), so repos that take off weeks after creation were
never gathered again and the emitted-cache reignite check had no fresh star
count to compare against. These tests pin the pass structure, cross-pass
dedup, rising labeling, and pushed_at dating without touching the network.
"""
import unittest
from unittest.mock import MagicMock, patch

import news_aggregator.sources.github_releases as gr


def _repo(full_name, created_at, pushed_at, stars, desc="d"):
    return {
        "full_name": full_name,
        "html_url": f"https://github.com/{full_name}",
        "created_at": created_at,
        "pushed_at": pushed_at,
        "stargazers_count": stars,
        "description": desc,
    }


def _fake_get(search_results_by_kind):
    """search_results_by_kind: {"new": [...], "rising": [...]} applied to the
    first keyword query of each pass; other queries return empty."""
    calls = []

    def fake(url, headers=None, timeout=None, params=None):
        r = MagicMock()
        r.headers = {"X-RateLimit-Remaining": "100"}
        r.raise_for_status = lambda: None
        if "releases" in url:
            r.json = lambda: []
            return r
        q = params["q"]
        calls.append(q)
        kind = "rising" if f"stars:>={gr.RISING_MIN_STARS}" in q else "new"
        payload = search_results_by_kind.get(kind, []) if "claude-code" in q else []
        r.json = lambda: {"items": payload}
        return r

    return fake, calls


class TestTwoPassQueries(unittest.TestCase):
    def test_both_windows_are_queried_for_every_keyword(self):
        fake, calls = _fake_get({})
        with patch.object(gr.requests, "get", side_effect=fake):
            gr.GitHubReleases().fetch()
        new_calls = [q for q in calls if f"stars:>={gr.RISING_MIN_STARS}" not in q]
        rising_calls = [q for q in calls if f"stars:>={gr.RISING_MIN_STARS}" in q]
        self.assertEqual(len(new_calls), len(gr.REPO_SEARCH_QUERIES))
        self.assertEqual(len(rising_calls), len(gr.REPO_SEARCH_QUERIES))
        for q in rising_calls:
            self.assertIn("created:>", q)

    def test_rising_item_labeled_and_dated_by_pushed_at(self):
        fake, _ = _fake_get({"rising": [
            _repo("hot/only-rising", "2026-07-05T00:00:00Z", "2026-07-29T01:00:00Z", 320),
        ]})
        with patch.object(gr.requests, "get", side_effect=fake):
            items = gr.GitHubReleases().fetch()
        self.assertEqual(len(items), 1)
        it = items[0]
        self.assertTrue(it.summary.startswith("📈 上升中"))
        self.assertEqual(it.score, 320)
        self.assertEqual(it.score_unit, "星")
        self.assertEqual(it.published.date().isoformat(), "2026-07-29")

    def test_new_repo_item_keeps_plain_summary_and_created_date(self):
        fake, _ = _fake_get({"new": [
            _repo("fresh/tool", "2026-07-28T20:00:00Z", "2026-07-28T21:00:00Z", 3, desc="new tool"),
        ]})
        with patch.object(gr.requests, "get", side_effect=fake):
            items = gr.GitHubReleases().fetch()
        self.assertEqual(len(items), 1)
        it = items[0]
        self.assertEqual(it.summary, "new tool")
        self.assertEqual(it.score_unit, "星")
        self.assertEqual(it.published.date().isoformat(), "2026-07-28")

    def test_repo_in_both_passes_emitted_once_from_new_pass(self):
        dup_new = _repo("dup/repo", "2026-07-28T20:00:00Z", "2026-07-28T21:00:00Z", 3)
        dup_rising = _repo("dup/repo", "2026-07-28T20:00:00Z", "2026-07-28T22:00:00Z", 60)
        fake, _ = _fake_get({"new": [dup_new], "rising": [dup_rising]})
        with patch.object(gr.requests, "get", side_effect=fake):
            items = gr.GitHubReleases().fetch()
        self.assertEqual(len(items), 1)
        self.assertFalse(items[0].summary.startswith("📈"), "new-repo pass runs first and wins dedup")


if __name__ == "__main__":
    unittest.main()
