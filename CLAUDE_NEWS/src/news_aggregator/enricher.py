"""Enrich FeedItems with actual article/discussion content.

Priority per item type:
  HN link post  → fetch external article via trafilatura
  HN thread     → Firebase API text + top-2 comment texts
  Reddit post   → Reddit JSON API selftext
  Other         → trafilatura on the article URL (only if summary is thin)
"""
import html
import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import replace
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter

from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

MAX_SUMMARY_CHARS = 800
_THIN_THRESHOLD = 120   # existing summary shorter than this → try to enrich
_WORKERS = 6
_ARTICLE_TIMEOUT = 8    # per-URL cap for article fetching (trafilatura.fetch_url ignores ours)
_HN_FIREBASE = "https://hacker-news.firebaseio.com/v0/item/{}.json"
_HN_ITEM_RE = re.compile(r"news\.ycombinator\.com/item\?id=(\d+)")

# Domains where article extraction is useless or handled separately
_SKIP_ARTICLE_DOMAINS = frozenset([
    "github.com",
    "news.google.com",
    "reddit.com",
    "twitter.com",
    "x.com",
    "linkedin.com",
])

# Hard-paywalled domains — trafilatura only gets a login wall / teaser, so
# skip fetching entirely (saves time, avoids junk summaries). Original
# summary from the feed is kept as-is.
_PAYWALL_DOMAINS = frozenset([
    "wsj.com",
    "theinformation.com",
    "bloomberg.com",
    "ft.com",
    "nytimes.com",
])

# Shared session with larger connection pool (avoids "pool is full" warnings)
_session = requests.Session()
_adapter = HTTPAdapter(pool_connections=10, pool_maxsize=20)
_session.mount("http://", _adapter)
_session.mount("https://", _adapter)


# ── public API ────────────────────────────────────────────────────────────────

def enrich(items: list[FeedItem]) -> list[FeedItem]:
    """Return items with richer summary fields. Never raises."""
    with ThreadPoolExecutor(max_workers=_WORKERS) as pool:
        futures = {pool.submit(_safe_enrich, item): item for item in items}
        result = {}
        for fut in as_completed(futures, timeout=60):
            original = futures[fut]
            try:
                result[id(original)] = fut.result()
            except Exception:
                result[id(original)] = original
    # preserve original order
    return [result[id(item)] for item in items]


# ── per-item enrichment ───────────────────────────────────────────────────────

def _safe_enrich(item: FeedItem) -> FeedItem:
    try:
        return _enrich_one(item)
    except Exception as e:
        logger.debug("enrich failed for %s: %s", item.url, e)
        return item


def _enrich_one(item: FeedItem) -> FeedItem:
    # ── HN items ──────────────────────────────────────────────────────────────
    hn_id = _extract_hn_id(item.url) or _extract_hn_id(item.summary)
    if hn_id:
        return _enrich_hn(item, hn_id)

    # ── Reddit items ──────────────────────────────────────────────────────────
    if "reddit.com/r/" in item.url and "/comments/" in item.url:
        text = _fetch_reddit(item.url)
        if text:
            return _with_summary(item, text)

    # ── Generic articles (only if existing summary is thin) ───────────────────
    if len(item.summary) < _THIN_THRESHOLD and item.url.startswith("http"):
        text = _fetch_article(item.url)
        if text:
            return _with_summary(item, text)

    return item


# ── HN ────────────────────────────────────────────────────────────────────────

def _enrich_hn(item: FeedItem, hn_id: str) -> FeedItem:
    data = _hn_api(hn_id)
    if not data:
        return item

    parts: list[str] = []

    # Ask HN / Show HN / Tell HN — item has a `text` body
    if data.get("text"):
        parts.append(_strip_html(data["text"]))

    # If it's a link post, fetch the external article
    ext_url = data.get("url") or ""
    if ext_url and "ycombinator.com" not in ext_url:
        article = _fetch_article(ext_url)
        if article:
            parts.append(article)

    # Top-2 comments for discussion context — fetch in parallel
    kid_ids = [str(k) for k in (data.get("kids") or [])[:2]]
    if kid_ids:
        with ThreadPoolExecutor(max_workers=len(kid_ids)) as pool:
            for comment in pool.map(_hn_api, kid_ids):
                if comment and comment.get("text"):
                    parts.append("💬 " + _strip_html(comment["text"]))

    combined = "\n\n".join(parts)
    return _with_summary(item, combined) if combined else item


def _hn_api(item_id: str) -> dict | None:
    try:
        resp = _session.get(
            _HN_FIREBASE.format(item_id),
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        logger.debug("HN Firebase API failed for %s: %s", item_id, e)
        return None


def _extract_hn_id(text: str) -> str | None:
    m = _HN_ITEM_RE.search(text or "")
    return m.group(1) if m else None


# ── Reddit ────────────────────────────────────────────────────────────────────

def _fetch_reddit(url: str) -> str:
    """Fetch post selftext via Reddit JSON API."""
    try:
        # Strip trailing slash, append .json
        json_url = url.rstrip("/") + ".json"
        resp = _session.get(
            json_url,
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
        )
        resp.raise_for_status()
        data = resp.json()
        # data[0] = post listing, data[0]["data"]["children"][0]["data"]["selftext"]
        selftext = (
            data[0]["data"]["children"][0]["data"].get("selftext", "").strip()
        )
        return selftext
    except Exception as e:
        logger.debug("Reddit JSON fetch failed for %s: %s", url, e)
        return ""


# ── Generic article ───────────────────────────────────────────────────────────

try:
    import trafilatura as _trafilatura
except ImportError:
    _trafilatura = None  # type: ignore[assignment]


def _fetch_article(url: str) -> str:
    """Extract main article text using requests + trafilatura.

    Uses requests (with _ARTICLE_TIMEOUT) instead of trafilatura.fetch_url()
    so that we control the timeout — trafilatura.fetch_url() has its own 30s
    default that ignores REQUEST_TIMEOUT and causes slow pipeline runs.
    """
    if _trafilatura is None:
        logger.debug("trafilatura not installed, skipping article fetch")
        return ""
    try:
        # Skip domains where extraction is useless or handled separately
        domain = urlparse(url).netloc.lstrip("www.")
        if domain in _SKIP_ARTICLE_DOMAINS:
            return ""
        # Skip hard paywalls (apex domain or any subdomain)
        if any(domain == d or domain.endswith("." + d) for d in _PAYWALL_DOMAINS):
            logger.debug("paywall domain, skipping article fetch: %s", url)
            return ""
        resp = _session.get(
            url,
            timeout=_ARTICLE_TIMEOUT,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ClaudeNewsBot/1.0)"},
            allow_redirects=True,
        )
        if resp.status_code != 200:
            return ""
        text = _trafilatura.extract(
            resp.text,
            include_comments=False,
            include_tables=False,
            no_fallback=False,
        )
        return (text or "").strip()
    except Exception as e:
        logger.debug("article fetch failed for %s: %s", url, e)
        return ""


# ── helpers ───────────────────────────────────────────────────────────────────

def _with_summary(item: FeedItem, text: str) -> FeedItem:
    return replace(item, summary=text.strip()[:MAX_SUMMARY_CHARS])


def _strip_html(raw: str) -> str:
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()
