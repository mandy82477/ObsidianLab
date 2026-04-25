from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


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
