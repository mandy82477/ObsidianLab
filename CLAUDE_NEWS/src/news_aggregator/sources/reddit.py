import logging
import time
from datetime import datetime, timedelta, timezone

import feedparser
import requests

import news_aggregator.config as _cfg
from news_aggregator.config import MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

SUBREDDIT_QUERIES = [
    ("ClaudeAI", "Claude Code"),
    ("ClaudeAI", "Anthropic"),
    ("artificial", "Claude Code"),
    ("MachineLearning", "Anthropic"),
    ("LocalLLaMA", "Claude"),
    ("LocalLLaMA", "Anthropic"),
]


class Reddit(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            lookback = _cfg.LOOKBACK_HOURS
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=lookback)
            # Reddit's ?t= param is server-side: use 'week' for backfill runs > 26h
            reddit_time = "week" if lookback > 30 else "day"
            items = []

            for subreddit, query in SUBREDDIT_QUERIES:
                url = (
                    f"https://www.reddit.com/r/{subreddit}/search.rss"
                    f"?q={query.replace(' ', '+')}&sort=new&t={reddit_time}&restrict_sr=1"
                )
                fetched = _fetch_rss(url)
                for entry in fetched[:MAX_ITEMS_PER_SOURCE // 2]:
                    pub = _parse_time(entry)
                    if pub and pub < cutoff:
                        continue
                    items.append(FeedItem(
                        title=entry.get("title", "(no title)"),
                        url=entry.get("link", ""),
                        source=f"Reddit / r/{subreddit}",
                        published=pub or datetime.now(tz=timezone.utc),
                        score=0,
                        summary=entry.get("summary", "")[:200],
                        category="community",
                    ))

            return items[:MAX_ITEMS_PER_SOURCE]
        except Exception as e:
            logger.warning("Reddit.fetch failed: %s", e)
            return []


def _fetch_rss(url: str) -> list:
    headers = {"User-Agent": "ClaudeNewsBot/1.0"}
    for attempt in range(2):
        try:
            # Fetch raw content with requests first to avoid feedparser's UA getting blocked
            resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            feed = feedparser.parse(resp.content)
            if feed.bozo and not feed.entries:
                raise ValueError(f"bozo feed: {feed.bozo_exception}")
            return feed.entries
        except Exception as e:
            if attempt == 0:
                logger.debug("Reddit RSS attempt 1 failed (%s), retrying in 5s", e)
                time.sleep(5)
            else:
                logger.warning("Reddit RSS failed after 2 attempts for %s: %s", url, e)
    return []


def _parse_time(entry) -> datetime | None:
    try:
        t = entry.get("published_parsed") or entry.get("updated_parsed")
        if t:
            return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
    except Exception:
        pass
    return None
