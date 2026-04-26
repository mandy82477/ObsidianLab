"""Enrich FeedItems with actual article/discussion content.

Priority per item type:
  HN link post  → fetch external article via trafilatura
  HN thread     → Firebase API text + top-2 comment texts
  Reddit post   → Reddit JSON API selftext
  Other         → trafilatura on the article URL (only if summary is thin)
"""
import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

import requests

from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

MAX_SUMMARY_CHARS = 800
_THIN_THRESHOLD = 120   # existing summary shorter than this → try to enrich
_WORKERS = 6
_HN_FIREBASE = "https://hacker-news.firebaseio.com/v0/item/{}.json"
_HN_ITEM_RE = re.compile(r"news\.ycombinator\.com/item\?id=(\d+)")


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

    # Top-2 comments for discussion context
    for kid_id in (data.get("kids") or [])[:2]:
        comment = _hn_api(str(kid_id))
        if comment and comment.get("text"):
            parts.append("💬 " + _strip_html(comment["text"]))

    combined = "\n\n".join(parts)
    return _with_summary(item, combined) if combined else item


def _hn_api(item_id: str) -> dict | None:
    try:
        resp = requests.get(
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
        resp = requests.get(
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

def _fetch_article(url: str) -> str:
    """Extract main article text using trafilatura."""
    try:
        import trafilatura
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            return ""
        text = trafilatura.extract(
            downloaded,
            include_comments=False,
            include_tables=False,
            no_fallback=False,
        )
        return (text or "").strip()
    except ImportError:
        logger.debug("trafilatura not installed, skipping article fetch")
        return ""
    except Exception as e:
        logger.debug("trafilatura failed for %s: %s", url, e)
        return ""


# ── helpers ───────────────────────────────────────────────────────────────────

def _with_summary(item: FeedItem, text: str) -> FeedItem:
    clean = text.strip()[:MAX_SUMMARY_CHARS]
    from dataclasses import replace
    return replace(item, summary=clean)


def _strip_html(html: str) -> str:
    """Very lightweight HTML tag stripper."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&#x27;", "'", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
