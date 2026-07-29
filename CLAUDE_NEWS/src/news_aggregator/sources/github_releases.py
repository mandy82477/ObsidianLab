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

# Rising window — the created:>{26h} pass only sees brand-new repos, which are
# almost always at 0-5 stars, so "popular" repos that take off weeks after
# creation never enter the pipeline and the emitted-cache reignite check
# (score 2x and delta >= 10) never gets a fresh star count to compare against.
# This second pass re-queries repos created within RISING_WINDOW_DAYS that
# already crossed RISING_MIN_STARS: takeoffs get gathered again with current
# stars, letting reignite decide whether they resurface.
RISING_WINDOW_DAYS = 30
RISING_MIN_STARS = 50


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
                    if remaining <= 2:
                        logger.warning("GitHub rate limit critical (%d remaining), skipping further official repos", remaining)
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
            # Two passes per keyword query: brand-new repos (created within the
            # lookback window) and rising repos (see RISING_WINDOW_DAYS above).
            cutoff_date = cutoff.strftime("%Y-%m-%d")
            rising_date = (datetime.now(tz=timezone.utc) - timedelta(days=RISING_WINDOW_DAYS)).strftime("%Y-%m-%d")
            searches = [(f"{q} created:>{cutoff_date}", False) for q in REPO_SEARCH_QUERIES] + [
                (f"{q} created:>{rising_date} stars:>={RISING_MIN_STARS}", True) for q in REPO_SEARCH_QUERIES
            ]
            seen_search_urls: set[str] = set()
            for query, is_rising in searches:
                try:
                    resp = requests.get(
                        "https://api.github.com/search/repositories",
                        headers=headers,
                        timeout=REQUEST_TIMEOUT,
                        params={
                            "q": query,
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
                        url = repo["html_url"]
                        if url in seen_search_urls:
                            continue
                        seen_search_urls.add(url)
                        # rising repos surface because of current traction, so
                        # date them by last push, not creation (up to 30d ago)
                        pub_str = (repo.get("pushed_at") if is_rising else repo.get("created_at")) or repo.get("created_at", "")
                        try:
                            pub = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
                        except Exception:
                            pub = datetime.now(tz=timezone.utc)
                        desc = (repo.get("description") or "")[:300]
                        if is_rising:
                            desc = f"📈 上升中（{RISING_WINDOW_DAYS} 天內建立、已達 ★{RISING_MIN_STARS}+）｜{desc}"
                        items.append(FeedItem(
                            title=repo["full_name"],
                            url=url,
                            source="GitHub Search",
                            published=pub,
                            score=repo.get("stargazers_count", 0),
                            score_unit="星",
                            summary=desc,
                            category="community",
                        ))
                except Exception as e:
                    logger.warning("GitHub repo search '%s' failed: %s", query, e)

            return items[:MAX_ITEMS_PER_SOURCE * 2]
        except Exception as e:
            logger.warning("GitHubReleases.fetch failed: %s", e)
            return []
