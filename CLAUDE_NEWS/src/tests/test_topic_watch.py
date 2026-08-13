"""Tests for news_aggregator.sources.topic_watch.TopicWatch.

這個來源的職責是「為指定 wiki 頁開一條窄通道」，所以測試釘的是兩件事：
通道有沒有正確標記（`topic` 是它豁免 filter 標題閘的唯一鑰匙），以及
**閘門有沒有關緊**——量的上限是防止定向抓取稀釋日報的第一道，設定壞掉或
某條 query 爆量時不能讓它整包灌進來。
"""
import json
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from news_aggregator.sources import topic_watch as mod
from news_aggregator.sources.base import FeedItem
from news_aggregator.sources.topic_watch import TopicWatch

NOW = datetime.now(tz=timezone.utc)


def _raw(title, url, minutes_ago=10):
    """模擬 _fetch_google_query 的回傳（尚未帶 topic 的原始條目）。"""
    return FeedItem(
        title=title, url=url, source="Google News / X",
        published=NOW - timedelta(minutes=minutes_ago),
        score=0, summary="orig", category="media",
    )


class _Cfg:
    """把 CONFIG_PATH 指到暫存檔，測試不碰 repo 內的真實設定。"""

    def __init__(self, payload):
        self._tmp = TemporaryDirectory()
        self.path = Path(self._tmp.name) / "topic_watch.json"
        self.path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        self._p = patch.object(mod, "CONFIG_PATH", self.path)

    def __enter__(self):
        self._p.start()
        return self

    def __exit__(self, *exc):
        self._p.stop()
        self._tmp.cleanup()
        return False


def _cfg(topics, global_max=8):
    return {"_global_max": global_max, "topics": topics}


def _topic(slug="ai-talent-flow", queries=("q1",), max_items=3, status="active"):
    return {"slug": slug, "queries": list(queries),
            "max_items": max_items, "status": status}


class TestTagging(unittest.TestCase):
    def test_items_carry_topic_slug_and_source_label(self):
        """`topic` 是豁免鑰匙，沒標等於這條通道白開。"""
        with _Cfg(_cfg([_topic()])):
            with patch.object(mod, "_fetch_google_query",
                              return_value=[_raw("Jeff Dean leaves Google", "https://a/1")]):
                with patch.object(mod, "_resolve_items", side_effect=lambda x: x):
                    items = TopicWatch().fetch()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].topic, "ai-talent-flow")
        self.assertEqual(items[0].source, "Topic Watch / ai-talent-flow")

    def test_summary_carries_context_note(self):
        """摘要自帶語境，讓日報 agent 與記者不必倚賴額外規則記憶。"""
        with _Cfg(_cfg([_topic()])):
            with patch.object(mod, "_fetch_google_query",
                              return_value=[_raw("t", "https://a/1")]):
                with patch.object(mod, "_resolve_items", side_effect=lambda x: x):
                    (item,) = TopicWatch().fetch()
        self.assertIn("專頁定向抓取", item.summary)
        self.assertIn("ai-talent-flow", item.summary)


class TestCaps(unittest.TestCase):
    """上限是防稀釋的第一道，必須在抓料層就關緊。"""

    def test_per_topic_cap(self):
        many = [_raw(f"t{i}", f"https://a/{i}", minutes_ago=i) for i in range(20)]
        with _Cfg(_cfg([_topic(max_items=3)])):
            with patch.object(mod, "_fetch_google_query", return_value=many):
                with patch.object(mod, "_resolve_items", side_effect=lambda x: x):
                    items = TopicWatch().fetch()
        self.assertEqual(len(items), 3)

    def test_global_cap_across_topics(self):
        many = [_raw(f"t{i}", f"https://a/{i}", minutes_ago=i) for i in range(20)]
        topics = [_topic(slug=f"s{n}", max_items=5) for n in range(4)]
        with _Cfg(_cfg(topics, global_max=6)):
            with patch.object(mod, "_fetch_google_query",
                              side_effect=lambda q, c: [
                                  _raw(f"{q}-{i}", f"https://{q}/{i}", i) for i in range(20)
                              ]):
                with patch.object(mod, "_resolve_items", side_effect=lambda x: x):
                    items = TopicWatch().fetch()
        self.assertEqual(len(items), 6)

    def test_duplicate_urls_within_topic_collapse(self):
        dupes = [_raw("same", "https://a/1"), _raw("same", "https://a/1")]
        with _Cfg(_cfg([_topic()])):
            with patch.object(mod, "_fetch_google_query", return_value=dupes):
                with patch.object(mod, "_resolve_items", side_effect=lambda x: x):
                    items = TopicWatch().fetch()
        self.assertEqual(len(items), 1)


class TestResilience(unittest.TestCase):
    """本來源掛掉不得拖垮其餘 11 個來源——BaseSource 契約是「絕不 raise」。"""

    def test_missing_config_returns_empty(self):
        with _Cfg(_cfg([_topic()])) as c:
            c.path.unlink()
            self.assertEqual(TopicWatch().fetch(), [])

    def test_invalid_config_never_raises(self):
        with _Cfg(_cfg([_topic()])) as c:
            c.path.write_text("{not json", encoding="utf-8")
            self.assertEqual(TopicWatch().fetch(), [])

    def test_retired_topic_skipped(self):
        with _Cfg(_cfg([_topic(status="retired")])):
            with patch.object(mod, "_fetch_google_query",
                              side_effect=AssertionError("must not fetch")):
                self.assertEqual(TopicWatch().fetch(), [])

    def test_one_query_failure_does_not_lose_the_others(self):
        def _q(query, cutoff):
            if query == "bad":
                raise ConnectionError("network down")
            return [_raw("good", "https://a/ok")]

        with _Cfg(_cfg([_topic(queries=("bad", "good"))])):
            with patch.object(mod, "_fetch_google_query", side_effect=_q):
                with patch.object(mod, "_resolve_items", side_effect=lambda x: x):
                    items = TopicWatch().fetch()
        self.assertEqual([i.title for i in items], ["good"])

    def test_topic_missing_queries_is_skipped_not_fatal(self):
        cfg = _cfg([{"slug": "broken", "status": "active"}, _topic()])
        with _Cfg(cfg):
            with patch.object(mod, "_fetch_google_query",
                              return_value=[_raw("t", "https://a/1")]):
                with patch.object(mod, "_resolve_items", side_effect=lambda x: x):
                    items = TopicWatch().fetch()
        self.assertEqual(len(items), 1)


class TestShippedConfig(unittest.TestCase):
    """實際 ship 的設定檔必須可解析、每筆欄位齊全——壞了會讓來源整個靜默歸零。"""

    def test_real_config_is_valid(self):
        cfg = json.loads(mod.CONFIG_PATH.read_text(encoding="utf-8"))
        topics = cfg.get("topics") or []
        self.assertTrue(topics, "設定檔沒有任何 topic")
        for t in topics:
            self.assertTrue(t.get("slug"), t)
            self.assertTrue(t.get("queries"), t)
            self.assertIsInstance(t.get("max_items"), int)
            self.assertTrue(t.get("why"), f"{t.get('slug')} 缺 why（為何值得定向抓取）")
            for q in t["queries"]:
                low = q.lower()
                self.assertNotIn("anthropic", low,
                                 f"{t['slug']}: query 不可含 Anthropic（那是既有來源的地盤）")
                self.assertNotIn("claude", low,
                                 f"{t['slug']}: query 不可含 Claude（同上）")

    def test_global_max_present(self):
        cfg = json.loads(mod.CONFIG_PATH.read_text(encoding="utf-8"))
        self.assertIsInstance(cfg.get("_global_max"), int)


if __name__ == "__main__":
    unittest.main()
