"""dev.to official API source — developer community articles tagged with Claude / Anthropic.

Uses the public JSON API (no auth) rather than the tag RSS feed, since the API
exposes engagement numbers (positive_reactions_count, comments_count) needed
for a quality gate. RSS-only fields like slash_comments were unreliable.
"""
import logging
from datetime import datetime, timedelta, timezone

import requests

import news_aggregator.config as _cfg
from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

API_URL = "https://dev.to/api/articles"

TAGS = [
    "claudecode",
    "anthropic",
    "claudeai",
]

MIN_REACTIONS = 5
MIN_COMMENTS = 2
PER_TAG_CAP = 8
TOTAL_CAP = 15


class DevTo(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=_cfg.LOOKBACK_HOURS)
            items: list[FeedItem] = []

            for tag in TAGS:
                try:
                    resp = requests.get(
                        API_URL,
                        params={"tag": tag, "per_page": 30},
                        headers={"User-Agent": "ClaudeNewsBot/1.0"},
                        timeout=REQUEST_TIMEOUT,
                    )
                    resp.raise_for_status()
                    articles = resp.json()

                    tag_items: list[FeedItem] = []
                    for a in articles:
                        published_at = a.get("published_at")
                        if not published_at:
                            continue
                        try:
                            pub = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
                        except Exception:
                            continue
                        if pub < cutoff:
                            continue

                        reactions = a.get("positive_reactions_count", 0) or 0
                        comments = a.get("comments_count", 0) or 0
                        if reactions < MIN_REACTIONS and comments < MIN_COMMENTS:
                            continue

                        tag_items.append(FeedItem(
                            title=a.get("title", "(no title)"),
                            url=a.get("url", ""),
                            source=f"dev.to / #{tag}",
                            published=pub,
                            score=reactions,
                            score_unit="讚",
                            summary=(a.get("description") or "")[:200],
                            category="community",
                        ))

                    items.extend(tag_items[:PER_TAG_CAP])
                except Exception as e:
                    logger.warning("DevTo tag '%s' failed: %s", tag, e)

            return items[:TOTAL_CAP]
        except Exception as e:
            logger.warning("DevTo.fetch failed: %s", e)
            return []
