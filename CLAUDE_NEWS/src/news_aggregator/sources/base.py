import time
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
    category: str  # "official" | "community"


class BaseSource(ABC):
    @abstractmethod
    def fetch(self) -> list[FeedItem]:
        """Return items from the last LOOKBACK_HOURS. Never raise — return [] on failure."""


def parse_feed_time(entry) -> datetime | None:
    """Parse published/updated time from a feedparser entry."""
    try:
        t = entry.get("published_parsed") or entry.get("updated_parsed")
        if t:
            return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
    except Exception:
        pass
    return None
