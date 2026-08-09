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

Two watch modes:

``hash`` (default)
    Content-hash diff over one page's visible text. Answers "did this page
    change", which is what a billing or quota page needs.

``index``
    For a machine-readable documentation index (``llms.txt``), where every line
    is ``- [Title](URL): description``. Hashing that whole file is useless — 280
    lines churn constantly and the hash only ever says "something moved". This
    mode stores the *set of page URLs* and emits only when pages are **added or
    removed**, so a description reword stays silent while a brand-new feature
    page announces itself. This is the one source that catches a feature the
    project can't name yet: on 2026-08-08 five outlets reported cross-session
    messaging and the pipeline logged "no official corroboration" for a day,
    while the docs index had gained /en/cross-session-messaging.
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

# A line of an llms.txt index: "- [Title](https://…): description".
# The description is deliberately not captured — rewording it must stay silent.
_INDEX_LINE_RE = re.compile(r"^\s*-\s*\[([^\]]+)\]\((https?://[^)\s]+)\)", re.M)

# How many added/removed pages to name in the summary before truncating. A docs
# reorganisation can move dozens at once; the item exists to prompt a look, not
# to reproduce the diff.
MAX_LISTED_PAGES = 12

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
            mode = page.get("mode") or "hash"
            try:
                text = _fetch_text(url, raw=(mode == "index"))
            except Exception as e:
                # A watched page failing must never take the pipeline down; the
                # stored hash is left untouched so the next run retries cleanly.
                logger.warning("Official watch '%s' failed: %s", name, e)
                continue

            prev = state.get(url)
            if mode == "index":
                item = _index_item(name, url, text, prev, state)
            else:
                item = _hash_item(name, url, text, prev, state)
            dirty = True
            if item is not None:
                items.append(item)

        if dirty:
            _save_state(state)

        return items


def _hash_item(name: str, url: str, text: str, prev, state: dict) -> FeedItem | None:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    state[url] = {"hash": digest, "length": len(text)}

    if prev is None:
        logger.info("Official watch '%s' baseline recorded", name)
        return None
    if prev.get("hash") == digest:
        return None
    if abs(len(text) - int(prev.get("length", 0))) < MIN_DELTA_CHARS:
        logger.info("Official watch '%s' changed below threshold", name)
        return None

    return FeedItem(
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


def _index_item(name: str, url: str, text: str, prev, state: dict) -> FeedItem | None:
    """Emit only when the documentation index gains or loses pages."""
    pages = {u: t for t, u in _INDEX_LINE_RE.findall(text)}

    if not pages:
        # Parsed nothing: the format changed, or we fetched an error page. The
        # stored page set must survive untouched — overwriting it with {} would
        # make the next successful run report every page as newly added.
        logger.warning("Official watch '%s' parsed no index entries", name)
        return None

    state[url] = {"pages": pages}

    if prev is None or not prev.get("pages"):
        logger.info("Official watch '%s' index baseline recorded (%d pages)", name, len(pages))
        return None

    before = set(prev["pages"])
    added = sorted(set(pages) - before)
    removed = sorted(before - set(pages))
    if not added and not removed:
        return None

    parts = []
    if added:
        parts.append(f"新增 {len(added)} 頁：" + "、".join(
            f"{pages[u]}（{u}）" for u in added[:MAX_LISTED_PAGES]
        ) + ("…" if len(added) > MAX_LISTED_PAGES else ""))
    if removed:
        parts.append(f"移除 {len(removed)} 頁：" + "、".join(
            f"{prev['pages'].get(u, u)}" for u in removed[:MAX_LISTED_PAGES]
        ) + ("…" if len(removed) > MAX_LISTED_PAGES else ""))

    headline = "、".join(
        filter(None, [
            f"新增 {len(added)} 頁" if added else "",
            f"移除 {len(removed)} 頁" if removed else "",
        ])
    )
    return FeedItem(
        title=f"官方文件索引異動：{name}（{headline}）",
        url=url,
        source="Official Docs",
        published=datetime.now(tz=timezone.utc),
        score=0,
        summary=(
            "；".join(parts)
            + "。此為官方文件索引的頁面增減偵測，非新聞報導——新增頁通常代表新功能上線，"
            "請開啟該頁確認實際內容。"
        ),
        category="official",
        score_unit="",
    )


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


def _fetch_text(url: str, raw: bool = False) -> str:
    resp = requests.get(
        url,
        headers={"User-Agent": "ClaudeNewsBot/1.0"},
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    # Markdown and llms.txt carry no markup to strip, and _visible_text would
    # eat the line structure the index parser needs.
    return resp.text if raw else _visible_text(resp.text)


def _visible_text(html: str) -> str:
    """Strip markup so cosmetic asset-hash churn doesn't read as a content change."""
    body = _SCRIPT_RE.sub(" ", html)
    body = _TAG_RE.sub(" ", body)
    return _WS_RE.sub(" ", body).strip()
