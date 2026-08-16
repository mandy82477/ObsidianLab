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
    # Overrides the normalized URL as the emitted-cache key. Empty for normal news
    # items, whose URL identifies the story once and for all.
    #
    # Change-detection sources (official docs / skills / release-notes watchers) are
    # different: they re-report *the same stable URL* every time its content changes,
    # and their items carry score=0. Keyed by URL alone, the first change gets emitted
    # and confirmed, and every later change to that page is dropped forever — the
    # score-reignition escape hatch (>=2x and +10) can never fire from 0. That silently
    # killed 8 of 9 watched pages between 2026-08-07 and 2026-08-12, including
    # claude.com/pricing and the support-centre plan/quota articles that
    # `.claude/rules/wiki-ingest-commercial.md` names as the authoritative source.
    #
    # Those sources set this to "<url>#<content-hash>", so each distinct change is a
    # distinct cache entry. Old bare-URL entries can never collide with it, so the
    # burned pages heal on their next change — no cache surgery needed.
    dedup_key: str = ""


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
