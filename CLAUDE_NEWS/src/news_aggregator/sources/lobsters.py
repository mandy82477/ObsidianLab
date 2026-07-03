"""lobste.rs RSS source — the `ai` tag is broad, so filter by title keyword."""
import logging
import re
from datetime import datetime, timedelta, timezone

import feedparser
import requests

import news_aggregator.config as _cfg
from news_aggregator.config import MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem, parse_feed_time

logger = logging.getLogger(__name__)

LOBSTERS_AI_RSS = "https://lobste.rs/t/ai.rss"
_KEYWORD_RE = re.compile(r"claude|anthropic|mcp", re.IGNORECASE)


class Lobsters(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=_cfg.LOOKBACK_HOURS)
            resp = requests.get(
                LOBSTERS_AI_RSS,
                headers={"User-Agent": "ClaudeNewsBot/1.0"},
                timeout=REQUEST_TIMEOUT,
            )
            resp.raise_for_status()
            feed = feedparser.parse(resp.content)
            if feed.bozo and not feed.entries:
                raise ValueError(f"bozo feed: {feed.bozo_exception}")

            items = []
            for entry in feed.entries[:MAX_ITEMS_PER_SOURCE]:
                title = entry.get("title", "(no title)")
                if not _KEYWORD_RE.search(title):
                    continue
                pub = parse_feed_time(entry)
                if pub and pub < cutoff:
                    continue
                items.append(FeedItem(
                    title=title,
                    url=entry.get("link", ""),
                    source="lobste.rs",
                    published=pub or datetime.now(tz=timezone.utc),
                    score=0,
                    summary=entry.get("summary", "")[:200],
                    category="community",
                ))

            return items[:MAX_ITEMS_PER_SOURCE]
        except Exception as e:
            logger.warning("Lobsters.fetch failed: %s", e)
            return []
