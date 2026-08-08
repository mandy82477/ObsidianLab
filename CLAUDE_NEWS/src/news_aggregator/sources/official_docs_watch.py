"""Official docs watchlist — content-hash diff over a few authoritative pages.

Anthropic publishes *plan / quota / billing* facts in the Help Center
(support.claude.com) and on claude.com/pricing, not in the blog or the API
release notes. Those pages are static documents, not feeds: when the July 20
2026 flagship-billing split landed, the daily pipeline only ever saw four
mutually-contradictory media headlines about it, and the authoritative answer
sat unread on the Help Center for 20 days.

Feeds cannot catch that — the Help Center's own "Release notes" article covers
model launches and features, not billing changes. So this source watches a small
hand-curated list of URLs and emits an item only when a page's meaningful text
actually changes. Low volume by design: a quiet week emits nothing.

State (the previous hash per URL) lives next to seen_urls.json. A URL with no
recorded hash is *recorded silently* rather than emitted — otherwise every new
watch entry would fire a bogus "changed" item on its first run.
"""
import hashlib
import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path

import requests

from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).parent / "official_watch.json"
STATE_PATH = Path(__file__).parent / "official_watch_state.json"

_SCRIPT_RE = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")

# Sub-threshold churn (a rotating CSRF token, a "last viewed" widget) would
# otherwise emit an item every single day and train the reader to ignore this
# source. Require a change of at least this many characters.
MIN_DELTA_CHARS = 40


class OfficialDocsWatch(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            pages = _load_pages()
        except Exception as e:
            logger.warning("Official watch config load failed: %s", e)
            return []

        if not pages:
            return []

        state = _load_state()
        items: list[FeedItem] = []
        dirty = False

        for page in pages:
            url = page.get("url")
            name = page.get("name") or url
            if not url:
                logger.warning("Official watch entry missing url: %s", name)
                continue
            try:
                text = _fetch_text(url)
            except Exception as e:
                # A watched page failing must never take the pipeline down; the
                # stored hash is left untouched so the next run retries cleanly.
                logger.warning("Official watch '%s' failed: %s", name, e)
                continue

            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            prev = state.get(url)
            state[url] = {"hash": digest, "length": len(text)}
            dirty = True

            if prev is None:
                logger.info("Official watch '%s' baseline recorded", name)
                continue
            if prev.get("hash") == digest:
                continue
            if abs(len(text) - int(prev.get("length", 0))) < MIN_DELTA_CHARS:
                logger.info("Official watch '%s' changed below threshold", name)
                continue

            items.append(
                FeedItem(
                    title=f"官方文件更新：{name}",
                    url=url,
                    source="Official Docs",
                    published=datetime.now(tz=timezone.utc),
                    score=0,
                    summary=(
                        f"{name} 內容有變動（前次 {prev.get('length', 0)} 字 → 本次 {len(text)} 字）。"
                        "此為官方一手文件的變更偵測，非新聞報導；具體改了什麼需開啟連結比對。"
                    ),
                    category="official",
                    score_unit="",
                )
            )

        if dirty:
            _save_state(state)

        return items


def _load_pages() -> list[dict]:
    if not CONFIG_PATH.exists():
        logger.warning("Official watch config not found: %s", CONFIG_PATH)
        return []
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        logger.warning("Official watch config is invalid JSON (%s): %s", CONFIG_PATH, e)
        return []
    return [p for p in (data.get("pages") or []) if p.get("status") != "retired"]


def _load_state() -> dict:
    if not STATE_PATH.exists():
        return {}
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        # A corrupt state file must not wedge the source: start over. The cost
        # is one silent baseline run, not a crash.
        logger.warning("Official watch state unreadable, resetting: %s", e)
        return {}


def _save_state(state: dict) -> None:
    try:
        STATE_PATH.write_text(
            json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    except Exception as e:
        logger.warning("Official watch state write failed (non-fatal): %s", e)


def _fetch_text(url: str) -> str:
    resp = requests.get(
        url,
        headers={"User-Agent": "ClaudeNewsBot/1.0"},
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    return _visible_text(resp.text)


def _visible_text(html: str) -> str:
    """Strip markup so cosmetic asset-hash churn doesn't read as a content change."""
    body = _SCRIPT_RE.sub(" ", html)
    body = _TAG_RE.sub(" ", body)
    return _WS_RE.sub(" ", body).strip()
