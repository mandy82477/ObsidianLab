"""Tests for the `topic` tag surviving deduplication.

這是整個專頁定向抓取最容易靜默失效的地方，值得單獨釘住。

pipeline 順序是 dedup → enrich → filter，而 `SOURCE_PRIORITY` 裡 Google News 排 4、
Topic Watch 沒登記所以拿 99（`_source_rank` 的預設）。同一篇文章被兩邊抓到時，合併後
存活的是「Google News」那份——若 `topic` 沒跟著傳過去，它就會在 filter 的標題閘被丟掉，
而定向抓取明明命中了。失敗時日誌只會顯示一則 "filter dropped"，看不出定向命中被扔了，
所以這個坑不寫測試就等著再踩一次。
"""
import unittest
from datetime import datetime, timezone

from news_aggregator.dedup import deduplicate
from news_aggregator.sources.base import FeedItem

URL = "https://techcrunch.com/2026/08/05/jeff-dean-discovery-loop/"
TITLE = "Jeff Dean and other top AI researchers are leaving Google to launch their own startup"


def _item(source, topic="", score=0, title=TITLE, url=URL):
    return FeedItem(
        title=title,
        url=url,
        source=source,
        published=datetime(2026, 8, 5, tzinfo=timezone.utc),
        score=score,
        summary="",
        category="media",
        topic=topic,
    )


class TestTopicSurvivesUrlMerge(unittest.TestCase):
    def test_google_news_wins_but_inherits_topic(self):
        """Google News 優先序較高會存活，但必須繼承 topic。"""
        items = [
            _item("Topic Watch / ai-talent-flow", topic="ai-talent-flow"),
            _item("Google News / TechCrunch"),
        ]
        (survivor,) = deduplicate(items)
        self.assertTrue(survivor.source.startswith("Google News"))
        self.assertEqual(survivor.topic, "ai-talent-flow")
        self.assertEqual(survivor.source_count, 2)

    def test_order_independent(self):
        """兩種到達順序都要傳染成功（合併分支不同）。"""
        items = [
            _item("Google News / TechCrunch"),
            _item("Topic Watch / ai-talent-flow", topic="ai-talent-flow"),
        ]
        (survivor,) = deduplicate(items)
        self.assertEqual(survivor.topic, "ai-talent-flow")

    def test_existing_topic_not_overwritten(self):
        """已有 topic 者不被另一個 topic 覆蓋（先到者為準，避免隨機性）。"""
        items = [
            _item("Topic Watch / ai-talent-flow", topic="ai-talent-flow"),
            _item("Topic Watch / competitor-landscape", topic="competitor-landscape"),
        ]
        (survivor,) = deduplicate(items)
        self.assertEqual(survivor.topic, "ai-talent-flow")


class TestTopicSurvivesFuzzyTitleMerge(unittest.TestCase):
    def test_topic_inherited_across_different_urls(self):
        """標題近似但 URL 不同（同一事件、不同媒體轉載）也要傳染。"""
        items = [
            _item("Topic Watch / ai-talent-flow", topic="ai-talent-flow",
                  url="https://example.com/a"),
            _item("Google News / Memeburn", score=5,
                  title=TITLE + " (report)", url="https://example.com/b"),
        ]
        merged = deduplicate(items)
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0].topic, "ai-talent-flow")


class TestNoRegression(unittest.TestCase):
    def test_untagged_items_unaffected(self):
        """未帶 topic 的一般條目行為不變（預設空字串＝現況零差異）。"""
        items = [_item("Google News / A"), _item("Hacker News", score=99)]
        (survivor,) = deduplicate(items)
        self.assertEqual(survivor.topic, "")
        self.assertEqual(survivor.source, "Hacker News")


if __name__ == "__main__":
    unittest.main()
