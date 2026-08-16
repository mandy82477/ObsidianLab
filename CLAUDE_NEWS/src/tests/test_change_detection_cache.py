"""Change-detection sources must not be silenced after their first report.

2026-08-16: `official_docs_watch`, `official_skills_repos` and `api_docs` all
re-report the *same stable URL* whenever its content changes, with score=0.
The emitted-cache keyed on the normalized URL alone, and the only escape from a
confirmed entry is score re-ignition (>=2x and +10) — unreachable from 0. So the
first change to a page was emitted and confirmed, and every later change was
dropped forever, silently.

Measured damage before the fix: 8 of 9 watched pages burned between 2026-08-07
and 2026-08-12, including `claude.com/pricing` and the support-centre plan and
quota articles that `.claude/rules/wiki-ingest-commercial.md` names as the
authoritative source for billing facts. `api_docs` was burned too — it already
put a per-note `#anchor` in the URL, but `_normalize_url` strips fragments, so
every release note collapsed onto one key.

The fix is `FeedItem.dedup_key` ("<url>#<content-hash>"), used verbatim as the
cache key. These tests pin the behaviour that was missing.
"""
import unittest
from datetime import date, datetime, timezone

from news_aggregator.dedup import deduplicate
from news_aggregator.emitted_cache import cache_key, confirm_digest, filter_new_or_reignited
from news_aggregator.sources import official_docs_watch as docs_mod
from news_aggregator.sources.base import FeedItem

TODAY = date(2026, 8, 16)
WATCHED = "https://claude.com/pricing"


def _change(content_hash, url=WATCHED, source="Official Docs", score=0):
    """An item as a change-detection source emits it: stable URL, score 0."""
    return FeedItem(
        title="官方文件更新：Pricing", url=url, source=source,
        published=datetime(2026, 8, 16, tzinfo=timezone.utc),
        score=score, summary="", category="official", score_unit="",
        dedup_key=f"{url}#{content_hash}",
    )


class TestSecondChangeSurvives(unittest.TestCase):
    def test_second_change_to_same_url_is_emitted(self):
        """The exact bug: page changes, gets digested, then changes again."""
        _, cache = filter_new_or_reignited([_change("aaa")], {}, today=TODAY)
        cache = confirm_digest(cache, [{"url": WATCHED, "dedup_key": f"{WATCHED}#aaa"}], today=TODAY)

        kept, _ = filter_new_or_reignited([_change("bbb")], cache, today=TODAY)
        self.assertEqual(len(kept), 1, "a later change to the same page must reach the digest")

    def test_unchanged_content_is_still_suppressed(self):
        """The fix must not defeat the cache: identical content stays dropped.

        This is what keeps a re-detected non-change (e.g. the CI state file not
        being committed, so the same diff is found daily) out of the digest.
        """
        _, cache = filter_new_or_reignited([_change("aaa")], {}, today=TODAY)
        cache = confirm_digest(cache, [{"url": WATCHED, "dedup_key": f"{WATCHED}#aaa"}], today=TODAY)

        kept, _ = filter_new_or_reignited([_change("aaa")], cache, today=TODAY)
        self.assertEqual(kept, [], "the same change must not be re-offered")

    def test_confirm_under_bare_url_does_not_confirm_the_real_entry(self):
        """Why confirm_digest takes the record, not just the URL.

        Confirming the bare URL while the item is cached under its dedup_key would
        leave the real entry unconfirmed forever — re-offered every single run.
        """
        _, cache = filter_new_or_reignited([_change("aaa")], {}, today=TODAY)
        cache = confirm_digest(cache, [{"url": WATCHED, "dedup_key": f"{WATCHED}#aaa"}], today=TODAY)
        self.assertTrue(cache[f"{WATCHED}#aaa"]["digest_confirmed"])
        self.assertNotIn(WATCHED, cache, "bare URL must not become a second phantom entry")

    def test_plain_items_still_key_on_url(self):
        """Normal news items are unaffected — no dedup_key, same behaviour as before."""
        plain = FeedItem(
            title="t", url="https://example.com/a", source="Hacker News",
            published=datetime(2026, 8, 16, tzinfo=timezone.utc),
            score=10, summary="", category="community", score_unit="分",
        )
        _, cache = filter_new_or_reignited([plain], {}, today=TODAY)
        self.assertIn("https://example.com/a", cache)

    def test_cache_key_keeps_the_fragment_normalization_would_strip(self):
        self.assertEqual(cache_key(WATCHED, f"{WATCHED}#aaa"), f"{WATCHED}#aaa")
        self.assertEqual(cache_key(WATCHED + "/"), WATCHED)


class TestBurnedEntriesHealThemselves(unittest.TestCase):
    def test_legacy_bare_url_entry_does_not_block_the_next_change(self):
        """No cache surgery needed for the 8 pages already burned.

        Their pre-fix entries are keyed by bare URL; post-fix items are keyed by
        "<url>#<hash>", which can never collide — so the next real change goes
        through on its own.
        """
        legacy = {WATCHED: {"first_emitted": "2026-08-11", "score_at_emit": 0,
                            "digest_confirmed": True}}
        kept, _ = filter_new_or_reignited([_change("ccc")], legacy, today=TODAY)
        self.assertEqual(len(kept), 1)


class TestMergeDoesNotDropTheKey(unittest.TestCase):
    def test_dedup_key_survives_url_merge(self):
        """Same lesson as `topic`: a merge must not silently waste the fetch.

        A news article linking straight at the watched doc URL outranks the
        watcher; without inheritance the survivor falls back to bare-URL caching
        — straight back into permanent suppression.
        """
        watcher = _change("aaa")
        news = FeedItem(
            title="Anthropic updates its pricing page", url=WATCHED, source="Hacker News",
            published=datetime(2026, 8, 16, tzinfo=timezone.utc),
            score=200, summary="", category="community", score_unit="分",
        )
        merged = deduplicate([watcher, news])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0].source, "Hacker News", "higher score should win as before")
        self.assertEqual(merged[0].dedup_key, f"{WATCHED}#aaa")


class TestSourcesActuallySetTheKey(unittest.TestCase):
    """The cache fix is inert unless the sources populate the field."""

    def test_hash_item_sets_a_content_derived_key(self):
        state = {}
        prev = {"hash": "0" * 64, "length": 100}
        item = docs_mod._hash_item("Pricing", WATCHED, "x" * 4000, prev, state)
        self.assertIsNotNone(item)
        self.assertTrue(item.dedup_key.startswith(f"{WATCHED}#"))
        self.assertNotEqual(item.dedup_key, WATCHED)

    def test_two_different_contents_get_two_different_keys(self):
        prev = {"hash": "0" * 64, "length": 100}
        a = docs_mod._hash_item("Pricing", WATCHED, "x" * 4000, prev, {})
        b = docs_mod._hash_item("Pricing", WATCHED, "y" * 4000, prev, {})
        self.assertNotEqual(a.dedup_key, b.dedup_key)

    def test_index_item_key_tracks_which_pages_moved(self):
        def _index(*slugs):
            return "\n".join(f"- [{s.upper()}](https://code.claude.com/docs/en/{s})" for s in slugs)

        prev = {"pages": {f"https://code.claude.com/docs/en/{s}": s.upper() for s in ("a", "b")}}
        first = docs_mod._index_item("Docs index", WATCHED, _index("a", "b", "c"), prev, {})
        self.assertIsNotNone(first)
        self.assertTrue(first.dedup_key.startswith(f"{WATCHED}#"))

        second = docs_mod._index_item("Docs index", WATCHED, _index("a", "b", "c", "d"), prev, {})
        self.assertNotEqual(first.dedup_key, second.dedup_key,
                           "a different set of added pages must be a different entry")


if __name__ == "__main__":
    unittest.main()
