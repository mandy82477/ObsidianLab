import logging
from datetime import datetime, timedelta, timezone

import requests

from news_aggregator.config import GITHUB_TOKEN, LOOKBACK_HOURS, MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

REPOS = [
    "anthropics/claude-code",
    "anthropics/anthropic-sdk-python",
    "anthropics/anthropic-sdk-typescript",
]


class GitHubReleases(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=LOOKBACK_HOURS)
            headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": "ClaudeNewsBot/1.0"}
            if GITHUB_TOKEN:
                headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

            items = []
            for repo in REPOS:
                try:
                    resp = requests.get(
                        f"https://api.github.com/repos/{repo}/releases",
                        headers=headers,
                        timeout=REQUEST_TIMEOUT,
                        params={"per_page": 5},
                    )
                    remaining = int(resp.headers.get("X-RateLimit-Remaining", 999))
                    if remaining <= 5:
                        logger.warning("GitHub rate limit low (%d remaining), skipping further calls", remaining)
                        break
                    resp.raise_for_status()
                    for rel in resp.json():
                        pub_str = rel.get("published_at") or rel.get("created_at", "")
                        try:
                            pub = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
                        except Exception:
                            pub = datetime.now(tz=timezone.utc)
                        if pub < cutoff:
                            continue
                        body = (rel.get("body") or "")[:200].replace("\r\n", " ").replace("\n", " ")
                        items.append(FeedItem(
                            title=f"[{repo}] {rel.get('name') or rel.get('tag_name', '')}",
                            url=rel.get("html_url", ""),
                            source=f"GitHub / {repo}",
                            published=pub,
                            score=0,
                            summary=body,
                            category="official",
                        ))
                except Exception as e:
                    logger.warning("GitHubReleases repo '%s' failed: %s", repo, e)

            return items[:MAX_ITEMS_PER_SOURCE]
        except Exception as e:
            logger.warning("GitHubReleases.fetch failed: %s", e)
            return []
