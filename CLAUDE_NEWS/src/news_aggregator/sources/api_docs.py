"""Claude API / Platform release notes — server-rendered changelog page.

docs.claude.com/en/release-notes/api has no RSS feed, but the HTML is
server-rendered (Next.js SSR): each day's changes live under an
``id="month-day-year"`` <h3> anchor followed by a <ul> of bullet items.
That structure is stable enough to scrape directly.

Note: docs.claude.com/en/release-notes/claude-code redirects to the
claude-code GitHub CHANGELOG.md, which is already covered by
GitHubReleases (via the Releases API) — scraping the GitHub markdown
render here would be redundant and more fragile, so only the API/platform
release notes page is scraped.
"""
import logging
import re
from datetime import datetime, timedelta, timezone

import requests

import news_aggregator.config as _cfg
from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

RELEASE_NOTES_URL = "https://docs.claude.com/en/release-notes/api"
_TAG_RE = re.compile(r"<[^>]+>")
_SECTION_RE = re.compile(
    r'id="([a-z0-9-]+-20\d\d)"[^>]*>.*?<div>([A-Za-z]+ \d{1,2}, 20\d\d)</div>.*?</h3>'
    r"\s*<ul[^>]*>(.*?)</ul>",
    re.S,
)


def _strip_html(fragment: str) -> str:
    text = _TAG_RE.sub(" ", fragment)
    text = text.replace("&#x27;", "'").replace("&quot;", '"').replace("&amp;", "&")
    return re.sub(r"\s+", " ", text).strip()


class ApiDocs(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=_cfg.LOOKBACK_HOURS)
            resp = requests.get(
                RELEASE_NOTES_URL,
                headers={"User-Agent": "ClaudeNewsBot/1.0"},
                timeout=REQUEST_TIMEOUT,
            )
            resp.raise_for_status()
            html = resp.text

            items = []
            for anchor, date_str, body in _SECTION_RE.findall(html):
                try:
                    day = datetime.strptime(date_str, "%B %d, %Y").replace(tzinfo=timezone.utc)
                except ValueError:
                    continue
                # 條目只有日期沒有時刻，`day` 因此是當日 00:00 UTC——但 Anthropic 常在
                # 美國時間稍晚才發布，晚於本 pipeline 當天的抓取時刻。若拿 00:00 比
                # cutoff，該條目在自己發布當天還沒上線（抓不到），隔天再抓時 cutoff
                # 已經越過它的 00:00（被永久排除），於是每天都 gathered: 0——2026-07-11
                # 起連續 26 天零產出即由此而來，且不會報錯，完全靜默。
                # 改比「當日結束」，給每個只有日期的條目一整天的寬限，確保它至少能被
                # 下一輪抓取看見。
                if day + timedelta(hours=23, minutes=59, seconds=59) < cutoff:
                    continue
                summary = _strip_html(body)[:200]
                items.append(FeedItem(
                    title=f"[API Docs] {date_str} 異動",
                    url=f"{RELEASE_NOTES_URL}#{anchor}",
                    # The per-entry anchor already makes each release note distinct, but
                    # `_normalize_url` strips fragments — so every note collapsed onto the
                    # same cache key and only the first one (2026-08-07) ever got through.
                    # `dedup_key` is used verbatim, which keeps the anchor.
                    dedup_key=f"{RELEASE_NOTES_URL}#{anchor}",
                    source="Claude API Release Notes",
                    published=day,
                    score=0,
                    summary=summary,
                    category="official",
                ))
            return items
        except Exception as e:
            logger.warning("ApiDocs.fetch failed: %s", e)
            return []
