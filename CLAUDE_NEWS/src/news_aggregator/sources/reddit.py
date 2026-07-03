import logging
import time
from datetime import datetime, timedelta, timezone

import feedparser
import requests

import news_aggregator.config as _cfg
from news_aggregator.config import MAX_ITEMS_PER_SOURCE, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem, parse_feed_time

logger = logging.getLogger(__name__)

SUBREDDIT_QUERIES = [
    ("ClaudeCode", None),
    ("ClaudeAI", "Claude Code"),
    ("ClaudeAI", "Anthropic"),
    ("artificial", "Claude Code"),
    ("MachineLearning", "Anthropic"),
    ("LocalLLaMA", "Claude Code"),
    ("LocalLLaMA", "Anthropic"),
]

_TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
_OAUTH_BASE = "https://oauth.reddit.com"


class Reddit(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            lookback = _cfg.LOOKBACK_HOURS
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=lookback)

            if REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET:
                return _fetch_oauth(cutoff)
            return _fetch_rss_all(cutoff, lookback)
        except Exception as e:
            logger.warning("Reddit.fetch failed: %s", e)
            return []


# ── RSS path (no credentials) ───────────────────────────────────────────────

def _fetch_rss_all(cutoff: datetime, lookback: int) -> list[FeedItem]:
    # Reddit's ?t= param is server-side: use 'week' for backfill runs > 26h
    reddit_time = "week" if lookback > 30 else "day"
    items = []

    for subreddit, query in SUBREDDIT_QUERIES:
        if query is None:
            # Entire subreddit is on-topic: skip search, pull the new feed directly.
            url = f"https://www.reddit.com/r/{subreddit}/new.rss"
        else:
            url = (
                f"https://www.reddit.com/r/{subreddit}/search.rss"
                f"?q={query.replace(' ', '+')}&sort=new&t={reddit_time}&restrict_sr=1"
            )
        fetched = _fetch_rss(url)
        for entry in fetched[:MAX_ITEMS_PER_SOURCE // 2]:
            pub = parse_feed_time(entry)
            if pub and pub < cutoff:
                continue
            items.append(FeedItem(
                title=entry.get("title", "(no title)"),
                url=entry.get("link", ""),
                source=f"Reddit / r/{subreddit}",
                published=pub or datetime.now(tz=timezone.utc),
                score=int(entry.get("slash_comments", 0)),
                score_unit="留言",
                summary=entry.get("summary", "")[:200],
                category="community",
            ))

    return items[:MAX_ITEMS_PER_SOURCE]


def _fetch_rss(url: str) -> list:
    headers = {"User-Agent": "ClaudeNewsBot/1.0"}
    for attempt in range(2):
        try:
            # Fetch raw content with requests first to avoid feedparser's UA getting blocked
            resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            feed = feedparser.parse(resp.content)
            if feed.bozo and not feed.entries:
                raise ValueError(f"bozo feed: {feed.bozo_exception}")
            return feed.entries
        except Exception as e:
            if attempt == 0:
                logger.debug("Reddit RSS attempt 1 failed (%s), retrying in 5s", e)
                time.sleep(5)
            else:
                logger.warning("Reddit RSS failed after 2 attempts for %s: %s", url, e)
    return []


# ── OAuth path (REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET set) ───────────────

def _get_oauth_token() -> str | None:
    try:
        resp = requests.post(
            _TOKEN_URL,
            data={"grant_type": "client_credentials"},
            auth=(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET),
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json().get("access_token")
    except Exception as e:
        logger.warning("Reddit OAuth token request failed: %s", e)
        return None


def _oauth_url_for(subreddit: str, query: str | None) -> str:
    if query is None:
        return f"{_OAUTH_BASE}/r/{subreddit}/new.json"
    return (
        f"{_OAUTH_BASE}/r/{subreddit}/search.json"
        f"?q={query.replace(' ', '+')}&sort=new&restrict_sr=1"
    )


def _fetch_oauth_json(url: str, token: str) -> list[dict]:
    headers = {
        "User-Agent": "ClaudeNewsBot/1.0",
        "Authorization": f"Bearer {token}",
    }
    try:
        resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        children = resp.json().get("data", {}).get("children", [])
        return [c.get("data", {}) for c in children]
    except Exception as e:
        logger.warning("Reddit OAuth fetch failed for %s: %s", url, e)
        return []


def _fetch_oauth(cutoff: datetime) -> list[FeedItem]:
    token = _get_oauth_token()
    if not token:
        logger.warning("Reddit OAuth token unavailable, falling back to RSS")
        return _fetch_rss_all(cutoff, _cfg.LOOKBACK_HOURS)

    items = []
    for subreddit, query in SUBREDDIT_QUERIES:
        url = _oauth_url_for(subreddit, query)
        posts = _fetch_oauth_json(url, token)
        for post in posts[:MAX_ITEMS_PER_SOURCE // 2]:
            created_utc = post.get("created_utc")
            pub = (
                datetime.fromtimestamp(created_utc, tz=timezone.utc)
                if created_utc else datetime.now(tz=timezone.utc)
            )
            if pub < cutoff:
                continue
            permalink = post.get("permalink", "")
            items.append(FeedItem(
                title=post.get("title", "(no title)"),
                url=f"https://www.reddit.com{permalink}" if permalink else post.get("url", ""),
                source=f"Reddit / r/{subreddit}",
                published=pub,
                score=int(post.get("ups", 0)),
                score_unit="分",
                summary=(post.get("selftext", "") or "")[:200],
                category="community",
            ))

    return items[:MAX_ITEMS_PER_SOURCE]

