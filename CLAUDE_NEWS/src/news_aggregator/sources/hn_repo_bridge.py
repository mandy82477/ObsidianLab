# -*- coding: utf-8 -*-
"""D 窗：HN 高分帶 GitHub repo 補撈（2026-09-03 Phase 1 上線）。

為什麼存在：本庫 HN 來源以關鍵字查 Algolia，一個 in-scope 工具若標題不含
claude/anthropic，169 分也照漏——2026-05-01 的「Understand Anything」（169 分、
repo 描述明寫 Works with Claude Code）就是這樣漏掉的，直到 09-02 使用者問起才補。
這不是門檻問題，是取樣母體問題：我們從沒看過 HN 高分榜長什麼樣。

設計（兩道閘串聯，主題邊界零放寬）：
1. 母體：26h 內 ≥100 分的故事（實測約 15–40 則/日），空 query＋numericFilters
   （2026-09-03 探針實測可用；歷史回測命中 Understand-Anything 該篇）
2. 第一道（形狀閘）：url 連到 github.com 的 repo 才進第二道；官方網域
   （claude.com／anthropic.com）直接收；其餘全丟
3. 第二道（主題閘）：GET /repos/{o}/{r}，對 description＋topics＋homepage 做
   確定性關鍵字測試（allow-list，見 _SCOPE_TERMS）——標題會不提 claude，
   但 repo 的 description 與 topics 是作者自填的分類，誠實得多
4. 每日上限 3、共用已報導閘（日報＋清倉帳本）
5. 誤放/誤擋：誤放優先——這一層底下沒有別的感測器（關鍵字閘正是黑洞成因），
   入場券已是 ≥100 分的人類集體訊號，編輯層扛得住

壞掉時的樣子（D6-c）：Algolia 空 query 若被拒會回 0 hits，與「今天沒有高分故事」
無法分辨——防線是存在性斷言：HN 每天必有 ≥100 分故事，母體為 0 即視為來源異常
（拋例外讓 sourceStatus 記 ok=false），不是回空 list。
"""
import logging
import re
import time
from datetime import datetime, timezone

import requests

from news_aggregator.config import GITHUB_TOKEN, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem
from news_aggregator.sources.github_releases import _emitted_repo_urls, _record_queue

logger = logging.getLogger(__name__)

MIN_POINTS = 100        # 入場券：HN 人類集體訊號門檻
WINDOW_HOURS = 26       # 與全管線 LOOKBACK 對齊的取樣窗
DAILY_CAP = 3           # 每日上限（塞車優先序第 1——HN 頭條明天就冷了）

# 主題閘 allow-list：對 description+topics+homepage 小寫串接測試，命中任一即 in-scope。
# 不單獨列 `agent`（會把通用 AI agent 生態灌進來）；`agent skill(s)` 是複合詞，安全。
_SCOPE_TERMS = [
    "claude", "anthropic", "claude-code", "claude code",
    "mcp", "model context protocol",
    "skill.md", "agent skill", "agent-skills", ".claude",
]

_OFFICIAL_HOSTS = ("claude.com", "anthropic.com", "docs.claude.com")

_GH_REPO_RE = re.compile(r"^https://github\.com/([\w.\-]+)/([\w.\-]+)/?$")


class HNRepoBridge(BaseSource):
    def fetch(self) -> list[FeedItem]:
        now = datetime.now(tz=timezone.utc)
        cutoff = int(time.time()) - WINDOW_HOURS * 3600
        resp = requests.get(
            "https://hn.algolia.com/api/v1/search_by_date",
            params={
                "tags": "story",
                "hitsPerPage": 50,
                "numericFilters": f"created_at_i>{cutoff},points>={MIN_POINTS}",
            },
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
        )
        resp.raise_for_status()
        hits = resp.json().get("hits", [])
        if not hits:
            # 存在性斷言：HN 每天必有 ≥100 分故事，母體為 0 就是介面壞了，
            # 不是「今天沒新聞」。拋出去讓 sourceStatus 記 ok=false。
            raise RuntimeError(
                f"HN high-score population is empty (>= {MIN_POINTS} pts in {WINDOW_HOURS}h) "
                "— Algolia empty-query interface likely broken")

        emitted = _emitted_repo_urls()
        gh_headers = {"Accept": "application/vnd.github.v3+json",
                      "User-Agent": "ClaudeNewsBot/1.0"}
        if GITHUB_TOKEN:
            gh_headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

        candidates = []  # (points, FeedItem)
        checked = 0
        for h in sorted(hits, key=lambda x: x.get("points") or 0, reverse=True):
            url = (h.get("url") or "").strip()
            points = h.get("points") or 0
            title = h.get("title") or ""
            hn_url = f"https://news.ycombinator.com/item?id={h.get('objectID','')}"

            if any(host in url for host in _OFFICIAL_HOSTS):
                candidates.append((points, FeedItem(
                    title=title, url=url, source="HN Repo Bridge",
                    published=now, score=points, score_unit="分",
                    summary=f"[HN 高分補撈] 官方網域內容上 HN {points} 分（{hn_url}）",
                    category="community",
                )))
                continue

            m = _GH_REPO_RE.match(url)
            if not m:
                continue
            if emitted is not None and url.rstrip("/").lower() in emitted:
                continue
            # 第二道：主題閘（每則 1 次 core REST call，非 search 配額）
            checked += 1
            try:
                r = requests.get(f"https://api.github.com/repos/{m.group(1)}/{m.group(2)}",
                                 headers=gh_headers, timeout=REQUEST_TIMEOUT)
                if r.status_code != 200:
                    continue
                repo = r.json()
            except Exception as e:
                logger.warning("HNRepoBridge repo lookup failed for %s: %s", url, e)
                continue
            haystack = " ".join([
                (repo.get("description") or ""),
                " ".join(repo.get("topics") or []),
                (repo.get("homepage") or ""),
            ]).lower()
            if not any(t in haystack for t in _SCOPE_TERMS):
                continue
            desc = (repo.get("description") or "")[:250]
            candidates.append((points, FeedItem(
                title=f"{repo.get('full_name', title)}",
                url=repo.get("html_url", url),
                source="HN Repo Bridge",
                published=now,
                score=points, score_unit="分",
                summary=(f"[HN 高分補撈｜HN {points} 分，標題「{title[:80]}」不含關鍵字"
                         f"故未入常規 HN 來源] {desc}（{hn_url}）"),
                category="community",
            )))

        candidates.sort(key=lambda t: t[0], reverse=True)
        picked = [it for _, it in candidates[:DAILY_CAP]]
        _record_queue("hn_bridge", queued=len(candidates), emitted_n=len(picked), now=now)
        logger.info("HNRepoBridge: population=%d, gh-linked checked=%d, in-scope=%d, emitting=%d",
                    len(hits), checked, len(candidates), len(picked))
        return picked
