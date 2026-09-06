import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import requests

import news_aggregator.config as _cfg
from news_aggregator.config import GITHUB_TOKEN, MAX_ITEMS_PER_SOURCE, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"

# (term, tags, hitsPerPage, min_score)
_QUERIES = [
    ("Claude Code", "story",   MAX_ITEMS_PER_SOURCE, 10),
    ("Anthropic",   "story",   MAX_ITEMS_PER_SOURCE, 10),
    ("claude",      "show_hn", 10,                   1),
    ("anthropic",   "show_hn", 10,                   1),
]


def _fetch_hn_query(term: str, tags: str, hits: int, min_score: int, cutoff: int) -> list[FeedItem]:
    try:
        resp = requests.get(
            HN_SEARCH_URL,
            params={
                "query": term,
                "tags": tags,
                "numericFilters": f"created_at_i>{cutoff}",
                "hitsPerPage": hits,
            },
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
        )
        resp.raise_for_status()
        result = []
        for h in resp.json().get("hits", []):
            score = h.get("points") or 0
            if score < min_score:
                continue
            obj_id = h.get("objectID", "")
            url = h.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
            num_comments = h.get("num_comments") or 0
            summary = f"HN discussion: https://news.ycombinator.com/item?id={obj_id}"
            if num_comments > 0:
                summary += f"（HN 討論 {num_comments} 則）"
            result.append(FeedItem(
                title=h.get("title", "(no title)"),
                url=url,
                source="Hacker News",
                published=datetime.fromtimestamp(
                    h.get("created_at_i", time.time()), tz=timezone.utc
                ),
                score=score,
                score_unit="分",
                summary=summary,
                category="community",
            ))
        return result
    except Exception as e:
        logger.warning("HackerNews query '%s' (%s) failed: %s", term, tags, e)
        return []



# ── D 窗：高分榜補撈（繞過關鍵字閘）────────────────────────────────────────
#
# 上面四個 query 是**關鍵字閘**：HN 上標題／內文不含這四個字的東西，從來不會
# 進到管線裡——不是被過濾掉，是根本沒被抓過。分數再高也一樣。
#
# 2026-09-02 實證此閘漏球：Understand-Anything 於 2026-05-01 上 HN 169 分／
# 49 留言，落在本庫收錄窗內、遠超高門檻（≥50 分），repo 描述明寫
# 「Works with Claude Code」——是 in-scope 內容，卻因標題叫「Understand
# Anything」不含 claude 字樣而整篇沒被抓過。是使用者一句質疑才發現的，
# 沒有任何排程檢查抓得到它（見 `wiki/log.md` 2026-09-02 Query 條目）。
#
# 補法：空 query 撈當窗高分榜，對**帶 GitHub repo 連結**者抓 repo description
# 判 claude/anthropic 字樣。全程確定性規則、無需 LLM（本專案無 API key）。
# 判準刻意窄：只認 GitHub repo 連結，因為那是唯一能免費、確定性地問到
# 「這東西跟 Claude 有沒有關係」的地方；部落格文章沒有等價的描述欄可查。
D_MIN_SCORE = 100          # HN 高分榜量級；26h 母體實測約 36 則
D_MAX_LOOKUPS = 40         # GitHub API 呼叫上限，防止母體暴增時打爆額度
_GH_REPO_RE = re.compile(r"^https?://(?:www\.)?github\.com/([^/\s]+)/([^/\s?#]+)")
_INSCOPE_RE = re.compile(r"claude|anthropic", re.IGNORECASE)


def _gh_repo(url: str) -> str | None:
    m = _GH_REPO_RE.match(url or "")
    if not m:
        return None
    owner, repo = m.group(1), m.group(2)
    if owner.lower() in {"orgs", "topics", "features", "about", "pricing", "marketplace"}:
        return None
    return f"{owner}/{repo.removesuffix('.git')}"


def _repo_is_inscope(repo: str, headers: dict) -> tuple[bool, str]:
    """回傳 (是否 in-scope, 用來判定的描述)。查不到一律判 False，不猜。"""
    try:
        resp = requests.get(
            f"https://api.github.com/repos/{repo}",
            headers=headers, timeout=REQUEST_TIMEOUT,
        )
        if resp.status_code != 200:
            return False, ""
        data = resp.json()
        blob = " ".join(str(x) for x in (
            data.get("description") or "",
            " ".join(data.get("topics") or []),
        ))
        return bool(_INSCOPE_RE.search(blob)), (data.get("description") or "")[:200]
    except Exception as e:
        logger.warning("D window: repo lookup %s failed: %s", repo, e)
        return False, ""


def _fetch_hn_highscore(cutoff: int) -> list[FeedItem]:
    """空 query 撈高分榜，只留 repo 描述證明 in-scope 的那幾則。"""
    headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": "ClaudeNewsBot/1.0"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    try:
        resp = requests.get(
            HN_SEARCH_URL,
            params={
                "query": "",
                "tags": "story",
                "numericFilters": f"created_at_i>{cutoff},points>={D_MIN_SCORE}",
                "hitsPerPage": 100,
            },
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
        )
        resp.raise_for_status()
        hits = resp.json().get("hits", [])
    except Exception as e:
        logger.warning("HackerNews high-score window failed: %s", e)
        return []

    out: list[FeedItem] = []
    lookups = 0
    for h in hits:
        url = h.get("url") or ""
        repo = _gh_repo(url)
        if not repo:
            continue
        title_blob = f"{h.get('title', '')} {h.get('story_text') or ''}"
        if _INSCOPE_RE.search(title_blob):
            continue          # 關鍵字閘本來就撈得到，別重複進料（dedup 前先省一次 API）
        if lookups >= D_MAX_LOOKUPS:
            logger.warning("D window: lookup cap %d reached, stopping", D_MAX_LOOKUPS)
            break
        lookups += 1
        inscope, desc = _repo_is_inscope(repo, headers)
        if not inscope:
            continue
        obj_id = h.get("objectID", "")
        num_comments = h.get("num_comments") or 0
        summary = f"HN discussion: https://news.ycombinator.com/item?id={obj_id}"
        if num_comments > 0:
            summary += f"（HN 討論 {num_comments} 則）"
        summary += f"｜高分榜補撈：repo 描述 {desc}"
        out.append(FeedItem(
            title=h.get("title", "(no title)"),
            url=url,
            source="Hacker News",
            published=datetime.fromtimestamp(
                h.get("created_at_i", time.time()), tz=timezone.utc
            ),
            score=h.get("points") or 0,
            score_unit="分",
            summary=summary,
            category="community",
        ))
    logger.info("D window: %d hits, %d repo lookups, %d in-scope", len(hits), lookups, len(out))
    return out


class HackerNews(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = int(time.time()) - (_cfg.LOOKBACK_HOURS * 3600)
            items: list[FeedItem] = []
            with ThreadPoolExecutor(max_workers=len(_QUERIES)) as pool:
                futures = [
                    pool.submit(_fetch_hn_query, term, tags, hits, min_score, cutoff)
                    for term, tags, hits, min_score in _QUERIES
                ]
                for fut in as_completed(futures):
                    items.extend(fut.result())
            items.extend(_fetch_hn_highscore(cutoff))
            return items[:MAX_ITEMS_PER_SOURCE * 2]
        except Exception as e:
            logger.warning("HackerNews.fetch failed: %s", e)
            return []
