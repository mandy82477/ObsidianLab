import difflib
from urllib.parse import urlparse, urlencode, parse_qs, urlunparse

from news_aggregator.sources.base import FeedItem

SOURCE_PRIORITY = {
    "Anthropic Blog": 0,
    "GitHub": 1,
    "Hacker News": 2,
    "Reddit": 3,
    "Google News": 4,
}

def _source_rank(item: FeedItem) -> int:
    for key, rank in SOURCE_PRIORITY.items():
        if key in item.source:
            return rank
    return 99


def _normalize_url(url: str) -> str:
    try:
        parsed = urlparse(url)
        # Strip UTM and tracking params
        keep_params = {
            k: v for k, v in parse_qs(parsed.query).items()
            if not k.startswith("utm_") and k not in ("ref", "src", "via")
        }
        clean_query = urlencode(keep_params, doseq=True)
        clean_path = parsed.path.rstrip("/")
        return urlunparse((parsed.scheme, parsed.netloc, clean_path, "", clean_query, ""))
    except Exception:
        return url.rstrip("/")


def deduplicate(items: list[FeedItem]) -> list[FeedItem]:
    seen_urls: dict[str, FeedItem] = {}
    result: list[FeedItem] = []

    for item in items:
        norm = _normalize_url(item.url)
        if norm in seen_urls:
            existing = seen_urls[norm]
            # Keep the one with higher score; tiebreak by source priority
            if item.score > existing.score or (
                item.score == existing.score and _source_rank(item) < _source_rank(existing)
            ):
                seen_urls[norm] = item
                result = [item if i is existing else i for i in result]
        else:
            seen_urls[norm] = item
            result.append(item)

    # Fuzzy title dedup across different URLs
    final: list[FeedItem] = []
    for item in result:
        duplicate = False
        for kept in final:
            ratio = difflib.SequenceMatcher(None, item.title.lower(), kept.title.lower()).ratio()
            if ratio > 0.85:
                # Replace kept if current has better score/priority
                if item.score > kept.score or (
                    item.score == kept.score and _source_rank(item) < _source_rank(kept)
                ):
                    idx = final.index(kept)
                    final[idx] = item
                duplicate = True
                break
        if not duplicate:
            final.append(item)

    # Sort: official first, then community; within each group sort by score desc then date desc
    final.sort(key=lambda x: (
        0 if x.category == "official" else 1,
        -x.score,
        -x.published.timestamp(),
    ))
    return final
