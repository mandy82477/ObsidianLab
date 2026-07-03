import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path

import requests

from news_aggregator.config import REQUEST_TIMEOUT, MAX_ITEMS_PER_SOURCE, SEEN_CACHE_FILE
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

BASE_URL = "https://www.anthropic.com"

# (listing page URL, link path prefix, source label)
PAGES = [
    (f"{BASE_URL}/news", "/news", "Anthropic Blog"),
    (f"{BASE_URL}/engineering", "/engineering", "Anthropic Engineering"),
]


class AnthropicBlog(BaseSource):
    def fetch(self) -> list[FeedItem]:
        cache = _load_cache()
        now = datetime.now(tz=timezone.utc)
        items = []

        for page_url, prefix, source_label in PAGES:
            try:
                items.extend(_fetch_page(page_url, prefix, source_label, cache, now))
            except Exception as e:
                logger.warning("AnthropicBlog.fetch failed for %s: %s", page_url, e)

        _save_cache(cache)
        return items


def _fetch_page(page_url: str, prefix: str, source_label: str,
                cache: dict, now: datetime) -> list[FeedItem]:
    resp = requests.get(
        page_url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()

    # Extract /news/slug (or /engineering/slug) links and their adjacent titles
    links = re.findall(rf'href="({re.escape(prefix)}/[a-z0-9_-]+)"', resp.text)
    unique_links = list(dict.fromkeys(links))

    items = []
    for path in unique_links[:MAX_ITEMS_PER_SOURCE]:
        url = BASE_URL + path
        if url in cache:
            continue  # Already reported in a previous run
        # Extract title from context
        idx = resp.text.find(f'"{path}"')
        title = f"({source_label})"
        if idx >= 0:
            m = re.search(r'<h\d[^>]*>([^<]{5,120})</h\d>', resp.text[idx:idx + 600])
            if m:
                title = m.group(1).strip()

        items.append(FeedItem(
            title=title,
            url=url,
            source=source_label,
            published=now,
            score=0,
            summary="",
            category="official",
        ))

    # Update cache with all seen URLs (not just new ones)
    for path in unique_links:
        cache[BASE_URL + path] = now.isoformat()

    return items


def _load_cache() -> dict:
    try:
        if SEEN_CACHE_FILE.exists():
            return json.loads(SEEN_CACHE_FILE.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {}


def _save_cache(cache: dict) -> None:
    try:
        SEEN_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        SEEN_CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception as e:
        logger.warning("Could not save seen_urls cache: %s", e)
