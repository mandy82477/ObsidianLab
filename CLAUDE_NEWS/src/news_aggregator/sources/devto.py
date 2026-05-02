"""dev.to RSS source — developer community articles tagged with Claude / Anthropic."""
import logging
from datetime import datetime, timedelta, timezone

import feedparser
import requests

import news_aggregator.config as _cfg
from news_aggregator.config import MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

# dev.to tag-based RSS feeds
TAGS = [
    "claudecode",
    "anthropic",
    "claudeai",
]


class DevTo(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=_cfg.LOOKBACK_HOURS)
            items: list[FeedItem] = []

            for tag in TAGS:
                url = f"https://dev.to/feed/tag/{tag}"
                try:
                    raw = requests.get(
                        url,
                        headers={"User-Agent": "ClaudeNewsBot/1.0"},
                        timeout=REQUEST_TIMEOUT,
                    )
                    raw.raise_for_status()
                    feed = feedparser.parse(raw.content)

                    for entry in feed.entries[:MAX_ITEMS_PER_SOURCE]:
                        pub = _parse_time(entry)
                        if pub and pub < cutoff:
                            continue
                        items.append(FeedItem(
                            title=entry.get("title", "(no title)"),
                            url=entry.get("link", ""),
                            source=f"dev.to / #{tag}",
                            published=pub or datetime.now(tz=timezone.utc),
                            score=0,
                            summary=entry.get("summary", "")[:200],
                            category="community",
                        ))
                except Exception as e:
                    logger.warning("DevTo tag '%s' failed: %s", tag, e)

            return items[:MAX_ITEMS_PER_SOURCE]
        except Exception as e:
            logger.warning("DevTo.fetch failed: %s", e)
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
