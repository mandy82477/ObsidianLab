import logging
from datetime import datetime, timedelta, timezone

import requests

import news_aggregator.config as _cfg
from news_aggregator.config import GITHUB_TOKEN, MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

REPOS = [
    "anthropics/claude-code",
    "anthropics/anthropic-sdk-python",
    "anthropics/anthropic-sdk-typescript",
]

# GitHub repo search queries — find new community tools before media coverage
REPO_SEARCH_QUERIES = [
    "claude-code in:name,description",
    "claude anthropic in:name",
    "mcp-server claude in:name,description",
]


class GitHubReleases(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=_cfg.LOOKBACK_HOURS)
            headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": "ClaudeNewsBot/1.0"}
            if GITHUB_TOKEN:
                headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

            items = []

            # ── Official releases ─────────────────────────────────────────────
            for repo in REPOS:
                try:
                    resp = requests.get(
                        f"https://api.github.com/repos/{repo}/releases",
                        headers=headers,
                        timeout=REQUEST_TIMEOUT,
                        params={"per_page": 5},
                    )
                    remaining = int(resp.headers.get("X-RateLimit-Remaining", 999))
                    if remaining <= 10:
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

            # ── Community repo search ─────────────────────────────────────────
            cutoff_date = cutoff.strftime("%Y-%m-%d")
            for query in REPO_SEARCH_QUERIES:
                try:
                    resp = requests.get(
                        "https://api.github.com/search/repositories",
                        headers=headers,
                        timeout=REQUEST_TIMEOUT,
                        params={
                            "q": f"{query} created:>{cutoff_date}",
                            "sort": "stars",
                            "order": "desc",
                            "per_page": 8,
                        },
                    )
                    remaining = int(resp.headers.get("X-RateLimit-Remaining", 999))
                    if remaining <= 10:
                        logger.warning("GitHub rate limit low (%d remaining), stopping repo search", remaining)
                        break
                    resp.raise_for_status()
                    for repo in resp.json().get("items", []):
                        try:
                            pub = datetime.fromisoformat(repo["created_at"].replace("Z", "+00:00"))
                        except Exception:
                            pub = datetime.now(tz=timezone.utc)
                        desc = (repo.get("description") or "")[:300]
                        items.append(FeedItem(
                            title=repo["full_name"],
                            url=repo["html_url"],
                            source="GitHub Search",
                            published=pub,
                            score=repo.get("stargazers_count", 0),
                            summary=desc,
                            category="community",
                        ))
                except Exception as e:
                    logger.warning("GitHub repo search '%s' failed: %s", query, e)

            return items[:MAX_ITEMS_PER_SOURCE * 2]
        except Exception as e:
            logger.warning("GitHubReleases.fetch failed: %s", e)
            return []
