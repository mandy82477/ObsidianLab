import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import requests

import news_aggregator.config as _cfg
from news_aggregator.config import MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"

# (term, tags, hitsPerPage, min_score)
_QUERIES = [
    ("Claude Code", "story",   MAX_ITEMS_PER_SOURCE, 10),
    ("Anthropic",   "story",   MAX_ITEMS_PER_SOURCE, 10),
    ("claude",      "show_hn", 10,                   1),
    ("anthropic",   "show_hn", 10,                   1),
]


def _fetch_hn_query(term: str, tags: str, hits: int, min_score: int, cutoff: int) -> list[FeedItem]:
    try:
        resp = requests.get(
            HN_SEARCH_URL,
            params={
                "query": term,
                "tags": tags,
                "numericFilters": f"created_at_i>{cutoff}",
                "hitsPerPage": hits,
            },
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
        )
        resp.raise_for_status()
        result = []
        for h in resp.json().get("hits", []):
            score = h.get("points") or 0
            if score < min_score:
                continue
            obj_id = h.get("objectID", "")
            url = h.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
            result.append(FeedItem(
                title=h.get("title", "(no title)"),
                url=url,
                source="Hacker News",
                published=datetime.fromtimestamp(
                    h.get("created_at_i", time.time()), tz=timezone.utc
                ),
                score=score,
                score_unit="分",
                summary=f"HN discussion: https://news.ycombinator.com/item?id={obj_id}",
                category="community",
            ))
        return result
    except Exception as e:
        logger.warning("HackerNews query '%s' (%s) failed: %s", term, tags, e)
        return []


class HackerNews(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = int(time.time()) - (_cfg.LOOKBACK_HOURS * 3600)
            items: list[FeedItem] = []
            with ThreadPoolExecutor(max_workers=len(_QUERIES)) as pool:
                futures = [
                    pool.submit(_fetch_hn_query, term, tags, hits, min_score, cutoff)
                    for term, tags, hits, min_score in _QUERIES
                ]
                for fut in as_completed(futures):
                    items.extend(fut.result())
            return items[:MAX_ITEMS_PER_SOURCE * 2]
        except Exception as e:
            logger.warning("HackerNews.fetch failed: %s", e)
            return []
