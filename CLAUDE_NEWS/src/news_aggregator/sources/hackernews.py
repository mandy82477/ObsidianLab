import logging
import time
from datetime import datetime, timezone

import requests

from news_aggregator.config import LOOKBACK_HOURS, MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT, SEARCH_TERMS
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"


class HackerNews(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = int(time.time()) - (LOOKBACK_HOURS * 3600)
            items: list[FeedItem] = []

            # Regular story search (score >= 3)
            for term in ["Claude Code", "Anthropic"]:
                try:
                    resp = requests.get(
                        HN_SEARCH_URL,
                        params={
                            "query": term,
                            "tags": "story",
                            "numericFilters": f"created_at_i>{cutoff}",
                            "hitsPerPage": MAX_ITEMS_PER_SOURCE,
                        },
                        timeout=REQUEST_TIMEOUT,
                        headers={"User-Agent": "ClaudeNewsBot/1.0"},
                    )
                    resp.raise_for_status()
                    hits = resp.json().get("hits", [])
                    for h in hits:
                        score = h.get("points") or 0
                        if score < 3:
                            continue
                        obj_id = h.get("objectID", "")
                        url = h.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
                        items.append(FeedItem(
                            title=h.get("title", "(no title)"),
                            url=url,
                            source="Hacker News",
                            published=datetime.fromtimestamp(
                                h.get("created_at_i", time.time()), tz=timezone.utc
                            ),
                            score=score,
                            summary=f"HN discussion: https://news.ycombinator.com/item?id={obj_id}",
                            category="community",
                        ))
                except Exception as e:
                    logger.warning("HackerNews query '%s' failed: %s", term, e)

            # Show HN search — lower threshold (>= 1) to catch newly posted tools
            for term in ["claude", "anthropic"]:
                try:
                    resp = requests.get(
                        HN_SEARCH_URL,
                        params={
                            "query": term,
                            "tags": "show_hn",
                            "numericFilters": f"created_at_i>{cutoff}",
                            "hitsPerPage": 10,
                        },
                        timeout=REQUEST_TIMEOUT,
                        headers={"User-Agent": "ClaudeNewsBot/1.0"},
                    )
                    resp.raise_for_status()
                    hits = resp.json().get("hits", [])
                    for h in hits:
                        score = h.get("points") or 0
                        if score < 1:
                            continue
                        obj_id = h.get("objectID", "")
                        url = h.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
                        items.append(FeedItem(
                            title=h.get("title", "(no title)"),
                            url=url,
                            source="Hacker News",
                            published=datetime.fromtimestamp(
                                h.get("created_at_i", time.time()), tz=timezone.utc
                            ),
                            score=score,
                            summary=f"HN discussion: https://news.ycombinator.com/item?id={obj_id}",
                            category="community",
                        ))
                except Exception as e:
                    logger.warning("HackerNews Show HN query '%s' failed: %s", term, e)

            return items[:MAX_ITEMS_PER_SOURCE * 2]
        except Exception as e:
            logger.warning("HackerNews.fetch failed: %s", e)
            return []
