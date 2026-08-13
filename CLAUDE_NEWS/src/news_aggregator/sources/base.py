import calendar
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class FeedItem:
    title: str
    url: str
    source: str
    published: datetime
    score: int
    summary: str
    category: str  # "official" | "community" | "media"
    source_count: int = 1  # how many independent sources covered this item
    score_unit: str = ""   # what `score` counts: "分" (HN points) | "留言" (comments) | "" (n/a)
    # Non-empty when the item was fetched *for a specific wiki page* rather than by the
    # usual Claude/Anthropic relevance. Holds that page's slug (e.g. "ai-talent-flow").
    # It is the sole exemption key for filter.py's Google News title gate — see
    # sources/topic_watch.py for why the gate would otherwise drop these by design.
    topic: str = ""


class BaseSource(ABC):
    @abstractmethod
    def fetch(self) -> list[FeedItem]:
        """Return items from the last LOOKBACK_HOURS. Never raise — return [] on failure."""


def parse_feed_time(entry) -> datetime | None:
    """Parse published/updated time from a feedparser entry."""
    try:
        t = entry.get("published_parsed") or entry.get("updated_parsed")
        if t:
            return datetime.fromtimestamp(calendar.timegm(t), tz=timezone.utc)
    except Exception:
        pass
    return None
