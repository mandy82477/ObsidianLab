import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone

import feedparser
import requests

import news_aggregator.config as _cfg
from news_aggregator.config import MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem, parse_feed_time

logger = logging.getLogger(__name__)

QUERIES = [
    "Claude Code",
    "Anthropic AI",
    "Anthropic Claude",
    "Claude API",
    "MCP server Anthropic",
]


def _fetch_google_query(query: str, cutoff: datetime) -> list[FeedItem]:
    url = (
        f"https://news.google.com/rss/search"
        f"?q={query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
    )
    try:
        raw = requests.get(url, headers={"User-Agent": "ClaudeNewsBot/1.0"}, timeout=REQUEST_TIMEOUT)
        raw.raise_for_status()
        feed = feedparser.parse(raw.content)
        if feed.bozo and not feed.entries:
            logger.warning("GoogleNews feed malformed for '%s': %s", query, feed.bozo_exception)
            return []
        result = []
        for entry in feed.entries[:MAX_ITEMS_PER_SOURCE]:
            pub = parse_feed_time(entry)
            if pub and pub < cutoff:
                continue
            source_name = "Google News"
            if hasattr(entry, "source") and hasattr(entry.source, "title"):
                source_name = f"Google News / {entry.source.title}"
            result.append(FeedItem(
                title=entry.get("title", "(no title)"),
                url=entry.get("link", ""),
                source=source_name,
                published=pub or datetime.now(tz=timezone.utc),
                score=0,
                summary=entry.get("summary", "")[:200],
                category="community",
            ))
        return result
    except Exception as e:
        logger.warning("GoogleNews query '%s' failed: %s", query, e)
        return []


class GoogleNews(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=_cfg.LOOKBACK_HOURS)
            items: list[FeedItem] = []
            with ThreadPoolExecutor(max_workers=len(QUERIES)) as pool:
                futures = [pool.submit(_fetch_google_query, q, cutoff) for q in QUERIES]
                for fut in as_completed(futures):
                    items.extend(fut.result())
            return items
        except Exception as e:
            logger.warning("GoogleNews.fetch failed: %s", e)
            return []
