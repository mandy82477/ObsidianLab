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

# GitHub repo search — 成長偵測器，不是新生兒偵測器（2026-08-04 改版）。
#
# 舊版查詢綁 created:>{26h}，只看得到「昨天剛出生」的 repo——出生時 0 星過不了任何
# 互動門檻，等它半年後長到 1.4k 星卻永遠不會再進入查詢範圍（實例：CloudAI-X/
# claude-workflow-v2，7 個月 1.4k 星、走 X + skills.sh 生態成長，全程隱形）。
# 慢燒型工具在舊設計下沒有任何感測器。
#
# 新設計每個主題範圍開兩扇窗（emitted 後由 seen_urls 去重，每個 repo 一生只進一次）：
#   A 新星窗：近 90 天出生且已 ≥100 星 —— 年輕但有真實吸引力，按星數取前幾名
#   B 穿越窗：500..3000 星、近 30 天仍活躍，**按星數升冪** —— 取「剛越過 500 星」
#     的上升者。升冪是關鍵：降冪永遠回傳同一批巨頭（去重後整窗空轉）；上限 3000
#     排除早已成名的老牌 repo（不需要被「發現」，且避免首日灌入一批人盡皆知的條目）
_REPO_SEARCH_SCOPES = [
    "claude-code in:name,description",
    "claude anthropic in:name",
    "mcp-server claude in:name,description",
]

RISING_WINDOW_DAYS = 90    # A 窗：出生多久內算「新星」
RISING_MIN_STARS = 100     # A 窗：最低星數（對照互動門檻表「低」檔）
CROSSING_STAR_RANGE = "500..3000"  # B 窗：穿越帶
CROSSING_ACTIVE_DAYS = 30  # B 窗：多久內有 push 才算活躍


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

            # ── Community repo search（成長偵測，設計說明見檔頭常數區）──────────
            now = datetime.now(tz=timezone.utc)
            rising_cutoff = (now - timedelta(days=RISING_WINDOW_DAYS)).strftime("%Y-%m-%d")
            active_cutoff = (now - timedelta(days=CROSSING_ACTIVE_DAYS)).strftime("%Y-%m-%d")
            search_windows = []
            for scope in _REPO_SEARCH_SCOPES:
                search_windows.append(  # A 新星窗
                    (f"{scope} created:>{rising_cutoff} stars:>={RISING_MIN_STARS}", "desc"))
                search_windows.append(  # B 穿越窗（升冪取剛越過門檻者）
                    (f"{scope} stars:{CROSSING_STAR_RANGE} pushed:>{active_cutoff}", "asc"))

            for query, order in search_windows:
                try:
                    resp = requests.get(
                        "https://api.github.com/search/repositories",
                        headers=headers,
                        timeout=REQUEST_TIMEOUT,
                        params={
                            "q": query,
                            "sort": "stars",
                            "order": order,
                            "per_page": 8,
                        },
                    )
                    remaining = int(resp.headers.get("X-RateLimit-Remaining", 999))
                    if remaining <= 2:
                        logger.warning("GitHub rate limit low (%d remaining), stopping repo search", remaining)
                        break
                    resp.raise_for_status()
                    for repo in resp.json().get("items", []):
                        # published 用「被偵測到的時間」而非 created_at：成長偵測下
                        # repo 出生可能在數月前，掛舊日期會被日報排序沉底、在補跑
                        # 模式被 until_dt 上界誤傷；「何時越過門檻被看見」才是這則
                        # 條目的新聞時間（新生兒偵測時代兩者恰好等價，所以沒暴露）
                        desc = (repo.get("description") or "")[:300]
                        items.append(FeedItem(
                            title=repo["full_name"],
                            url=repo["html_url"],
                            source="GitHub Search",
                            published=now,
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
