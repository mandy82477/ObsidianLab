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


def _inherit_topic(winner: FeedItem, loser: FeedItem) -> None:
    """Merging must not discard a `topic` tag.

    Topic-watch items are fetched precisely because their titles do *not* mention
    Claude/Anthropic, and `topic` is their only exemption from filter.py's Google
    News title gate. But dedup runs *before* filter, and Google News outranks
    Topic Watch in SOURCE_PRIORITY — so when both sources find the same article,
    the surviving copy would carry the "Google News" label, lose the tag, and be
    dropped by the gate. The targeted fetch would then be silently wasted: the
    logs show only "filter dropped", never that a topic hit was thrown away.
    """
    if not winner.topic and loser.topic:
        winner.topic = loser.topic


def _inherit_merge_fields(winner: FeedItem, loser: FeedItem) -> None:
    """Fields whose loss on merge silently wastes the losing fetch.

    `topic` (see above) and `dedup_key`: a change-detection item can be merged away
    by a news article pointing at the same doc URL, and without the key the surviving
    copy falls back to bare-URL caching — i.e. straight back into the permanent
    suppression this key exists to prevent.
    """
    _inherit_topic(winner, loser)
    if not winner.dedup_key and loser.dedup_key:
        winner.dedup_key = loser.dedup_key
    _merge_contributors(winner, loser)


def _merge_contributors(winner: FeedItem, loser: FeedItem) -> None:
    """Remember every source that covered this item, not just the winner's.

    Order-independent and idempotent, so a chain of merges (A<-B, then AB<-C)
    ends up with the same set whichever copy wins each round.
    """
    names = set(winner.contributors) | set(loser.contributors) | {loser.source}
    names.discard(winner.source)
    winner.contributors = tuple(sorted(names))


def deduplicate(items: list[FeedItem]) -> list[FeedItem]:
    seen_urls: dict[str, FeedItem] = {}
    result: list[FeedItem] = []

    for item in items:
        norm = _normalize_url(item.url)
        if norm in seen_urls:
            existing = seen_urls[norm]
            merged_count = existing.source_count + 1
            # Keep the one with higher score; tiebreak by source priority
            if item.score > existing.score or (
                item.score == existing.score and _source_rank(item) < _source_rank(existing)
            ):
                _inherit_merge_fields(item, existing)
                item.source_count = merged_count
                seen_urls[norm] = item
                result = [item if i is existing else i for i in result]
            else:
                _inherit_merge_fields(existing, item)
                existing.source_count = merged_count
        else:
            seen_urls[norm] = item
            result.append(item)

    # Fuzzy title dedup across different URLs
    final: list[FeedItem] = []
    for item in result:
        duplicate = False
        for idx, kept in enumerate(final):
            ratio = difflib.SequenceMatcher(None, item.title.lower(), kept.title.lower()).ratio()
            if ratio > 0.85:
                merged_count = item.source_count + kept.source_count
                # Replace kept if current has better score/priority
                if item.score > kept.score or (
                    item.score == kept.score and _source_rank(item) < _source_rank(kept)
                ):
                    _inherit_merge_fields(item, kept)
                    item.source_count = merged_count
                    final[idx] = item
                else:
                    _inherit_merge_fields(kept, item)
                    kept.source_count = merged_count
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
