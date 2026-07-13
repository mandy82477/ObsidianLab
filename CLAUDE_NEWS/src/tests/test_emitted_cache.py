import unittest
from datetime import date, datetime, timezone

from news_aggregator.emitted_cache import confirm_digest, filter_new_or_reignited
from news_aggregator.sources.base import FeedItem

TODAY = date(2026, 7, 14)


def _item(url="https://example.com/a", score=10, score_unit="分"):
    return FeedItem(
        title="t", url=url, source="Hacker News",
        published=datetime(2026, 7, 14, tzinfo=timezone.utc),
        score=score, summary="", category="community", score_unit=score_unit,
    )


class TestUnconfirmedTreatedAsNew(unittest.TestCase):
    """Regression test for the 2026-07-13 GH Actions blackhole: a gather-only
    run that never reaches a confirmed digest must not permanently suppress
    its items."""

    def test_first_seen_is_kept_and_left_unconfirmed(self):
        kept, cache = filter_new_or_reignited([_item()], {}, today=TODAY)
        self.assertEqual(len(kept), 1)
        self.assertFalse(cache["https://example.com/a"]["digest_confirmed"])

    def test_unconfirmed_entry_is_kept_again_next_run(self):
        # Simulates: gather-only ran once (item cached but never confirmed
        # because the digest build that should have followed never happened).
        _, cache = filter_new_or_reignited([_item(score=10)], {}, today=TODAY)
        # A later run re-fetches the same unchanged item.
        kept, cache2 = filter_new_or_reignited([_item(score=10)], cache, today=TODAY)
        self.assertEqual(len(kept), 1, "unconfirmed item must not be silently dropped")
        self.assertFalse(cache2["https://example.com/a"]["digest_confirmed"])

    def test_confirmed_entry_without_reignition_is_dropped(self):
        _, cache = filter_new_or_reignited([_item(score=10)], {}, today=TODAY)
        cache = confirm_digest(cache, ["https://example.com/a"], today=TODAY)
        kept, _ = filter_new_or_reignited([_item(score=10)], cache, today=TODAY)
        self.assertEqual(kept, [])

    def test_confirmed_entry_with_reignition_is_kept(self):
        _, cache = filter_new_or_reignited([_item(score=10)], {}, today=TODAY)
        cache = confirm_digest(cache, ["https://example.com/a"], today=TODAY)
        kept, cache2 = filter_new_or_reignited([_item(score=30)], cache, today=TODAY)
        self.assertEqual(len(kept), 1)
        # Reignited entries reset to unconfirmed pending the next confirm-digest call.
        self.assertFalse(cache2["https://example.com/a"]["digest_confirmed"])

    def test_zero_score_source_never_reignites_but_stays_recoverable_while_unconfirmed(self):
        # Blogroll items are always score=0, so they can never satisfy the
        # reignite threshold — the only thing that can save them from being
        # a permanent blackhole once confirmed is never re-emitting them
        # again unconfirmed, which is exactly what should NOT happen here
        # (they're never confirmed in this test, so they keep coming back).
        item = _item(url="https://blog.example/post", score=0, score_unit="")
        _, cache = filter_new_or_reignited([item], {}, today=TODAY)
        kept, _ = filter_new_or_reignited([item], cache, today=TODAY)
        self.assertEqual(len(kept), 1)


class TestConfirmDigest(unittest.TestCase):
    def test_confirms_known_entry_preserving_first_emitted(self):
        cache = {"https://example.com/a": {
            "first_emitted": "2026-07-01", "score_at_emit": 5, "digest_confirmed": False,
        }}
        updated = confirm_digest(cache, ["https://example.com/a"], today=TODAY)
        entry = updated["https://example.com/a"]
        self.assertTrue(entry["digest_confirmed"])
        self.assertEqual(entry["first_emitted"], "2026-07-01")

    def test_confirms_unknown_url_by_adding_it_fresh(self):
        updated = confirm_digest({}, ["https://example.com/new"], today=TODAY)
        entry = updated["https://example.com/new"]
        self.assertTrue(entry["digest_confirmed"])
        self.assertEqual(entry["first_emitted"], TODAY.isoformat())


if __name__ == "__main__":
    unittest.main()
