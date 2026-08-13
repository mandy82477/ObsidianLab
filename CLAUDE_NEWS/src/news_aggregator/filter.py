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
from urllib.parse import urlparse

from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

_TITLE_KEYWORDS = ("claude", "anthropic", "mcp")

# Press-release wire services — pure marketing copy, never editorial content.
# Matched against the item URL's registered domain (including subdomains),
# per CLAUDE.md's "不收錄...無技術內容的純行銷稿" rule, enforced mechanically.
_PR_WIRE_DOMAINS = (
    "prnewswire.com",
    "businesswire.com",
    "globenewswire.com",
    "accesswire.com",
    "newsfilecorp.com",
)


def _is_pr_wire(url: str) -> bool:
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        return False
    if not host:
        return False
    host = host.split(":")[0]  # strip port
    return any(host == d or host.endswith("." + d) for d in _PR_WIRE_DOMAINS)


def filter_relevant(items: list[FeedItem], min_score: int = 3) -> list[FeedItem]:
    """Drop loosely-matched Google News items whose title lacks any relevant keyword,
    and drop items from press-release wire domains regardless of source.

    `min_score` is kept in the signature for call-site compatibility; it is unused.
    """
    if not items:
        return items

    kept = []
    dropped = 0
    dropped_pr = 0
    for item in items:
        if _is_pr_wire(item.url):
            dropped_pr += 1
            logger.debug("Rule filter dropped (PR wire domain): %s", item.title)
            continue
        # Topic-watch items are fetched *for a named wiki page*, and their whole point
        # is that the title does not mention Claude/Anthropic (2026-08-05 Jeff Dean →
        # Discovery Loop went unseen for 8 days because of that). The tag survives dedup
        # via dedup._inherit_topic, so an item co-discovered by Google News keeps it.
        if item.source.startswith("Google News") and not item.topic:
            title = item.title.lower()
            if not any(kw in title for kw in _TITLE_KEYWORDS):
                dropped += 1
                logger.debug("Rule filter dropped (no keyword in title): %s", item.title)
                continue
        kept.append(item)

    if dropped or dropped_pr:
        logger.info(
            "Rule filter: kept %d / %d items (dropped %d Google News off-topic, %d PR wire)",
            len(kept), len(items), dropped, dropped_pr,
        )
    return kept
