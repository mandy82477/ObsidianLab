"""Anthropic status page source — first-hand service incident signals.

Statuspage incident history RSS (status.anthropic.com redirects to
status.claude.com). One item per incident updated within the lookback
window, so 529/500 outages reach the digest without waiting for community
posts to surface them.
"""
import logging
import re
from datetime import datetime, timedelta, timezone

import feedparser
import requests

import news_aggregator.config as _cfg
from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem, parse_feed_time

logger = logging.getLogger(__name__)

STATUS_RSS = "https://status.claude.com/history.rss"
MAX_ITEMS = 10
_TAG_RE = re.compile(r"<[^>]+>")


class AnthropicStatus(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=_cfg.LOOKBACK_HOURS)
            resp = requests.get(STATUS_RSS, headers={"User-Agent": "ClaudeNewsBot/1.0"},
                                timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            feed = feedparser.parse(resp.content)
            if feed.bozo and not feed.entries:
                raise ValueError(f"bozo feed: {feed.bozo_exception}")

            items = []
            for entry in feed.entries[:30]:
                pub = parse_feed_time(entry)
                if pub and pub < cutoff:
                    continue
                # description is HTML with the full incident update log; strip tags
                summary = _TAG_RE.sub(" ", entry.get("summary", ""))
                summary = re.sub(r"\s+", " ", summary).strip()[:200]
                items.append(FeedItem(
                    title=f"[Status] {entry.get('title', '(no title)')}",
                    url=entry.get("link", ""),
                    source="Anthropic Status",
                    published=pub or datetime.now(tz=timezone.utc),
                    score=0,
                    summary=summary,
                    category="official",
                ))
                if len(items) >= MAX_ITEMS:
                    break
            return items
        except Exception as e:
            logger.warning("AnthropicStatus.fetch failed: %s", e)
            return []
