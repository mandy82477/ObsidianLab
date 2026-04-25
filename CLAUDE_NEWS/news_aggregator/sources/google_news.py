import logging
from datetime import datetime, timezone

import feedparser
import requests

from news_aggregator.config import LOOKBACK_HOURS, MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

QUERIES = ["Claude Code", "Anthropic AI"]


class GoogleNews(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            from datetime import timedelta
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=LOOKBACK_HOURS)
            items: list[FeedItem] = []

            for query in QUERIES:
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
                        continue

                    for entry in feed.entries[:MAX_ITEMS_PER_SOURCE]:
                        pub = _parse_time(entry)
                        if pub and pub < cutoff:
                            continue
                        source_name = "Google News"
                        if hasattr(entry, "source") and hasattr(entry.source, "title"):
                            source_name = f"Google News / {entry.source.title}"
                        items.append(FeedItem(
                            title=entry.get("title", "(no title)"),
                            url=entry.get("link", ""),
                            source=source_name,
                            published=pub or datetime.now(tz=timezone.utc),
                            score=0,
                            summary=entry.get("summary", "")[:200],
                            category="community",
                        ))
                except Exception as e:
                    logger.warning("GoogleNews query '%s' failed: %s", query, e)

            return items
        except Exception as e:
            logger.warning("GoogleNews.fetch failed: %s", e)
            return []


def _parse_time(entry) -> datetime | None:
    try:
        import time as _time
        t = entry.get("published_parsed") or entry.get("updated_parsed")
        if t:
            return datetime.fromtimestamp(_time.mktime(t), tz=timezone.utc)
    except Exception:
        pass
    return None
