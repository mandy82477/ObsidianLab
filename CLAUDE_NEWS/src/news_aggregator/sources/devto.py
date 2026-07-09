"""dev.to official API source — developer community articles tagged with Claude / Anthropic.

Unlike the firehose sources (HN/Reddit/GitHub), dev.to is an evergreen tutorial
platform: reactions accrue slowly over days, so a fresh-post + reaction-threshold
gate systematically kills the good tutorials before they earn any engagement (a
26h window catches only hours-old 0-reaction posts). We therefore fetch by the
API's `top` param — the highest-reaction articles over the past TOP_DAYS — decoupled
from the daily lookback window. Quality over recency by design. The cross-run
emitted cache (main.py) prevents the same top article from re-surfacing every day.
"""
import logging
from datetime import datetime, timedelta, timezone

import requests

from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

API_URL = "https://dev.to/api/articles"

TAGS = [
    "claudecode",
    "anthropic",
    "claudeai",
]

# Window for the API `top` sort (days). dev.to Claude tags are niche/low-volume,
# so a month surfaces genuinely-upvoted tutorials that a week would miss.
TOP_DAYS = 30
# Modest engagement floor to drop 0-0 noise, well below the old 5/2 gate — the
# `top` sort already orders by reactions, so this only trims the long tail.
MIN_REACTIONS = 3
MIN_COMMENTS = 2
PER_TAG_CAP = 8
TOTAL_CAP = 15


class DevTo(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            items: list[FeedItem] = []

            for tag in TAGS:
                try:
                    resp = requests.get(
                        API_URL,
                        params={"tag": tag, "top": TOP_DAYS, "per_page": 30},
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
