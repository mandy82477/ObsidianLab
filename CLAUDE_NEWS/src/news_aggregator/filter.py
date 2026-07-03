"""Rule-based relevance filter (no LLM).

History: this module originally scored items 1-5 via the Anthropic API, but
this project runs without ANTHROPIC_API_KEY, so that path never executed and
every item passed through untouched. The LLM code was removed on 2026-07-03
in favour of an honest, keyless rule layer; editorial curation happens
downstream in the Claude-session digest step (Step 1b) and wiki ingest.

Current rules:
- Google News items must mention a relevant keyword in the title. GNews
  queries match loosely (e.g. "Anthropic AI" returns generic AI market
  round-ups), and it is the only source without its own quality gate.
- All other sources pass through: their fetchers already filter by
  keyword/tag/threshold at the source.
"""
import logging

from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

_TITLE_KEYWORDS = ("claude", "anthropic", "mcp")


def filter_relevant(items: list[FeedItem], min_score: int = 3) -> list[FeedItem]:
    """Drop loosely-matched Google News items whose title lacks any relevant keyword.

    `min_score` is kept in the signature for call-site compatibility; it is unused.
    """
    if not items:
        return items

    kept = []
    dropped = 0
    for item in items:
        if item.source.startswith("Google News"):
            title = item.title.lower()
            if not any(kw in title for kw in _TITLE_KEYWORDS):
                dropped += 1
                logger.debug("Rule filter dropped (no keyword in title): %s", item.title)
                continue
        kept.append(item)

    if dropped:
        logger.info("Rule filter: kept %d / %d items (dropped %d Google News off-topic)",
                    len(kept), len(items), dropped)
    return kept
