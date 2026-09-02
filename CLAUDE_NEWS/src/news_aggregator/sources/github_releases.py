import logging
import re
from datetime import datetime, timedelta, timezone

import requests

import news_aggregator.config as _cfg
from news_aggregator.config import GITHUB_TOKEN, MAX_ITEMS_PER_SOURCE, NEWS_DIR, REQUEST_TIMEOUT
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


# ── C 窗：存量盤點（2026-08-28 加入）───────────────────────────────────────
#
# A 窗與 B 窗都是發現期偵測器（只看得到剛出生或還很小的），所以任何一條 scope
# 底下既存的大 repo 永久隱形——addyosmani/agent-skills 90,233 星、每日 push，
# 本庫 12 個來源 × 121 篇日報零命中。這個洞每新增一條 scope 就復發一次，故 C 窗
# 掛在所有 scope 上。
#
# 「已報導過」取自 news/*.md 全文，不另立 state 檔——日報是唯一的永久記錄
# （emitted_items.json 只有 14 天 TTL）。白送兩個性質：日報沒建成則明天自動重試；
# repo 日後才越過門檻也會被撿起。詳細沿革見 wiki/log.md 2026-08-28。
_INVENTORY_SCOPES = _REPO_SEARCH_SCOPES + [
    # skills 生態不綁 claude：SKILL.md 是 Anthropic originated 的格式，這個生態
    # 整體屬 Claude 生態，但多數 repo 的 name/description 不會出現 claude 這個字
    # （superpowers 的描述是「agentic skills framework」）。綁 claude 就漏掉生態
    # 裡最大的那些。**這條 scope 只進 C 窗、不進 A/B 窗**：2026-08-28 實測
    # 100–3000 星帶被單一用途的內容型 skill 洗版（PPT 排版、公眾號排版、戀愛
    # 分析、logo 產生），工程級框架全部落在 20k 星以上——在這條 scope 上，
    # 星數本身就是品質過濾器。
    '"agent skills" in:name,description',
]
INVENTORY_MIN_STARS = 3000  # C 窗下限＝B 窗上限，兩窗接壤不重疊
INVENTORY_PER_DAY = 2       # 每日至多吐幾則（防止首日灌入一批人盡皆知的條目）


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

            # C 窗接在截斷之後：它每日至多 INVENTORY_PER_DAY 則，若排在截斷內
            # 會被 A/B 窗的量洗掉（A/B 兩窗滿載即 48 則 > 上限 40），等於裝了
            # 偵測器卻讀不到讀數。
            return items[:MAX_ITEMS_PER_SOURCE * 2] + _inventory_sweep(headers, now)
        except Exception as e:
            logger.warning("GitHubReleases.fetch failed: %s", e)
            return []


def _emitted_repo_urls() -> "set[str] | None":
    """日報全文出現過的 GitHub repo URL（小寫、去尾斜線）。

    日報是唯一的永久記錄。這裡刻意不建索引檔——多一個 state 檔就多一個會與
    事實不同步的東西，而 121 篇日報全讀不到一秒。
    """
    urls: set[str] = set()
    # 清倉帳本（2026-09-02）：一次性清倉的 repo 不經日報、記在此檔，與日報同等視為
    # 「已報導」。放 data/ 而非 news/ 的理由：news/*.md 會被 build_web 當日報解析
    # 上網站、被多支掃描腳本讀取，塞一份非日報格式的清單會污染所有消費端。
    # 檔案不存在屬正常（尚未清倉過），不觸發任何保護性跳過。
    try:
        clearance = NEWS_DIR.parent / "data" / "inventory_clearance.md"
        if clearance.exists():
            for m in re.finditer(r"https://github\.com/[\w.\-]+/[\w.\-]+",
                                 clearance.read_text(encoding="utf-8")):
                urls.add(m.group(0).rstrip("/").lower())
    except Exception as e:
        logger.warning("Inventory clearance ledger read failed: %s", e)
    try:
        digests = sorted(NEWS_DIR.glob("*.md"))
        # 空集合等價於「全部沒報導過」，會讓 C 窗把整個存量灌進日報。而
        # `Path.glob()` 對不存在的目錄不拋錯、只回空——光靠 try/except 擋不住這條
        # 路徑（本測試套件即以此為案例）。本庫恆有上百篇日報，零篇代表環境壞了，
        # 不代表檔案庫是空的：此時必須不吐。
        if not digests:
            logger.warning("Inventory sweep: no digests under %s, skipping", NEWS_DIR)
            return None
        for path in digests:
            for m in re.finditer(r"https://github\.com/[\w.\-]+/[\w.\-]+", path.read_text(encoding="utf-8")):
                urls.add(m.group(0).rstrip("/").lower())
    except Exception as e:
        logger.warning("Inventory sweep: cannot read news dir, skipping (%s)", e)
        return None
    return urls


def _inventory_sweep(headers: dict, now: datetime) -> list[FeedItem]:
    """C 窗：把每條 scope 底下「已成名但本庫從未報導過」的 repo 逐日補進來。

    設計說明見檔頭 `_INVENTORY_SCOPES` 常數區。
    """
    emitted = _emitted_repo_urls()
    if emitted is None:
        return []

    candidates: dict[str, dict] = {}
    for scope in _INVENTORY_SCOPES:
        try:
            resp = requests.get(
                "https://api.github.com/search/repositories",
                headers=headers,
                timeout=REQUEST_TIMEOUT,
                params={
                    "q": f"{scope} stars:>{INVENTORY_MIN_STARS}",
                    "sort": "stars",
                    "order": "desc",
                    "per_page": 100,
                },
            )
            if int(resp.headers.get("X-RateLimit-Remaining", 999)) <= 2:
                logger.warning("Inventory sweep: rate limit low, stopping")
                break
            resp.raise_for_status()
            for repo in resp.json().get("items", []):
                url = (repo.get("html_url") or "").rstrip("/")
                if url and url.lower() not in emitted:
                    candidates[url] = repo
        except Exception as e:
            logger.warning("Inventory sweep '%s' failed: %s", scope, e)

    picked = sorted(candidates.values(), key=lambda r: r.get("stargazers_count", 0), reverse=True)
    picked = picked[:INVENTORY_PER_DAY]
    logger.info("Inventory sweep: %d unreported repos in range, emitting %d",
                len(candidates), len(picked))

    # 產消對帳（2026-09-02）：佇列量寫進歷史檔供 lint 6e 讀取告警。教訓：C 窗上線
    # 5 天悄悄積到 154 個未報導候選（每日吐 2 ≈ 77 天排空），佇列長度只在上面那行
    # logger.info——訊號無消費端，與 pending 佇列 19 天 0→51 同病。同日 upsert。
    try:
        hist = NEWS_DIR.parent / "data" / "inventory_queue_history.csv"
        today = now.strftime("%Y-%m-%d")
        if hist.exists():
            rows = [l for l in hist.read_text(encoding="utf-8").splitlines()
                    if l and not l.startswith(today + ",")]
        else:
            rows = ["date,unreported,emitted"]
        rows.append(f"{today},{len(candidates)},{len(picked)}")
        hist.write_text("\n".join(rows) + "\n", encoding="utf-8")
    except Exception as e:
        logger.warning("Inventory queue history write failed: %s", e)

    items = []
    for repo in picked:
        created = (repo.get("created_at") or "")[:10]
        desc = (repo.get("description") or "")[:300]
        items.append(FeedItem(
            title=repo["full_name"],
            url=repo["html_url"],
            source="GitHub Search",
            published=now,
            score=repo.get("stargazers_count", 0),
            score_unit="星",
            # 前綴是給日報撰寫者的誠實訊號：這則不是「今天發生的事」，是本庫今天
            # 才第一次看見的存量。沒有它，一個 2 月出生的 9 萬星 repo 會被寫成
            # 今日新聞。
            summary=f"[存量盤點｜{created} 出生、本庫今日首次收錄] {desc}",
            category="community",
        ))
    return items
