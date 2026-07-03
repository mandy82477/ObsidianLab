"""Cross-run dedup cache — prevents the same story from being emitted twice.

Tracks every item that has already made it into a digest (`gathered_items.json`
output), keyed by normalized URL. Reduces two symptoms:
  - GitHub Issues re-appearing every run while comments keep trickling in
  - Backfill / lookback overlap re-emitting the same story across days

An item is re-emitted only on a genuine "re-ignition": current score is
>= 2x the score recorded at first emit AND the absolute increase is >= 10.
That signals the story picked up meaningfully more traction, worth a
second mention. Otherwise it's filtered out.

Cache entries expire after CACHE_TTL_DAYS so the file doesn't grow forever.
"""
import json
import logging
from datetime import date, timedelta

from news_aggregator.config import SRC_DIR
from news_aggregator.dedup import _normalize_url
from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

CACHE_FILE = SRC_DIR / "news_aggregator" / "emitted_items.json"
CACHE_TTL_DAYS = 14
REIGNITE_MULTIPLIER = 2
REIGNITE_MIN_DELTA = 10


def load_cache() -> dict:
    try:
        if CACHE_FILE.exists():
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        logger.warning("Could not load emitted_items cache: %s", e)
    return {}


def save_cache(cache: dict) -> None:
    try:
        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception as e:
        logger.warning("Could not save emitted_items cache: %s", e)


def prune_expired(cache: dict, today: date | None = None) -> dict:
    """Drop entries older than CACHE_TTL_DAYS (by first_emitted date)."""
    today = today or date.today()
    cutoff = today - timedelta(days=CACHE_TTL_DAYS)
    pruned = {}
    for url, entry in cache.items():
        try:
            first_emitted = date.fromisoformat(entry["first_emitted"])
        except Exception:
            continue  # drop malformed entries
        if first_emitted >= cutoff:
            pruned[url] = entry
    return pruned


def filter_new_or_reignited(
    items: list[FeedItem], cache: dict, today: date | None = None
) -> tuple[list[FeedItem], dict]:
    """Return (items to keep, updated cache — not yet saved).

    - Item not in cache -> kept, added to cache.
    - Item in cache, current score < reignite threshold -> dropped.
    - Item in cache, current score >= 2x recorded score and delta >= 10
      -> kept (reignited), cache entry's score_at_emit updated.
    """
    today = today or date.today()
    today_str = today.isoformat()
    updated_cache = dict(cache)
    kept: list[FeedItem] = []

    for item in items:
        norm = _normalize_url(item.url)
        existing = updated_cache.get(norm)

        if existing is None:
            kept.append(item)
            updated_cache[norm] = {"first_emitted": today_str, "score_at_emit": item.score}
            continue

        prev_score = existing.get("score_at_emit", 0)
        delta = item.score - prev_score
        reignited = item.score >= prev_score * REIGNITE_MULTIPLIER and delta >= REIGNITE_MIN_DELTA

        if reignited:
            kept.append(item)
            updated_cache[norm] = {
                "first_emitted": existing.get("first_emitted", today_str),
                "score_at_emit": item.score,
            }
        # else: already emitted, no reignition -> drop silently

    return kept, updated_cache
