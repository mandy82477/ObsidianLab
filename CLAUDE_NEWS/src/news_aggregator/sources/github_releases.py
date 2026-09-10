import logging
import re
import time
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
CROSSING_STAR_RANGE = "500..5000"  # B 窗：穿越帶（2026-09-03 上限 3000→5000，與 C 窗
#   下限 3000 刻意重疊——接壤設計在 repo 跨帶的那幾天恰好誰都排序不到它時會漏，
#   重疊帶是接縫保險，成本只是既有去重）
CROSSING_ACTIVE_DAYS = 30  # B 窗：多久內有 push 才算活躍
AB_WINDOW_CAP = 3          # A/B 窗每日各自硬上限（2026-09-03）：上限的意義是壞掉時
#   的爆炸半徑——改版前 A/B 滿載可灌 40 則進日報
SOURCE_TOTAL_CAP = 16      # 本來源總回傳硬上限（官方 releases ＋ 各窗合計）


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


# ── E 窗吐出端：星速觸發（2026-09-10 Phase 2 上線）─────────────────────────
#
# 記錄端（_record_star_history，2026-09-03）累積各窗每日看到的星數快照；本吐出端
# 拿快照自算星速，補 A/B/C/D 都接不到的那一種 repo：**已被某個窗「看見」過、
# 但每天都排序不進該窗的吐出名單，而它正在暴衝**。星數帶窗（A/B/C）按星數排序，
# 排序永遠輸給巨頭的中型 repo 在暴紅那幾天結構性隱形——星速是唯一能把「正在
# 發生」與「一直都大」分開的訊號。
#
# 閾值校準（2026-09-10，取 09-02～09-08 六個資料日、388 個 ≥2 觀測 repo）：
#   全體星速 p50=5、p90=114、p95=197 ★/日；未報導子集 top 名單顯示兩型值得吐——
#   絕對暴衝型（orca +703★/日）與年輕爆紅型（anti-slop 1.7k 星 +166★/日=24%/日）。
#   絕對線取 300（>p95，全體六日僅 7 個過線）；相對型取 100★/日 且 ≥5%/日
#   （巨頭日常成長 <1%/日，5% 只有真的在爆的年輕 repo 過得了）。
#   ⚠️ 校準基期僅 6 日，複查登記於 docs/workaround-register.md（2026-09-24）。
VELOCITY_LOOKBACK_DAYS = 8   # 回看窗：與最舊比較點的最大距離
VELOCITY_MIN_SPAN_DAYS = 2   # 兩筆觀測至少隔 2 天才算得出速度（單日雜訊不觸發）
VELOCITY_ABS = 300           # ★/日：絕對暴衝線，單獨成立
VELOCITY_FAST = 100          # ★/日：搭配相對成長率的較低線
VELOCITY_REL_PCT = 5.0       # %/日：相對成長率（以區間起點星數為基底）
VELOCITY_PER_DAY = 2         # 每日至多吐幾則（同 C 窗哲學：上限＝爆炸半徑）


# 無 token 時 GitHub search API 限 10 次/分鐘，而本來源一次 fetch 恰好發出
# 10 次 search 呼叫（A/B 窗 3 scope × 2 ＋ C 窗 4 scope）——第 10 次（C 窗
# agent skills 那條 scope）會貼著限流線。雲端班次有 GITHUB_TOKEN（30/min）
# 不受影響；本機無 token 補跑時以間隔節流換完整掃描（多花 ~1 分鐘）。
_SEARCH_MIN_INTERVAL = 6.2
_last_search_ts = 0.0


def _search_throttle() -> None:
    global _last_search_ts
    if GITHUB_TOKEN:
        return
    wait = _SEARCH_MIN_INTERVAL - (time.monotonic() - _last_search_ts)
    if wait > 0:
        time.sleep(wait)
    _last_search_ts = time.monotonic()


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
            emitted = _emitted_repo_urls()  # 2026-09-03：升為所有窗的共用已報導閘
            star_seen: dict[str, int] = {}  # E 窗記錄端：本次各窗看到的 repo 星數
            rising_cutoff = (now - timedelta(days=RISING_WINDOW_DAYS)).strftime("%Y-%m-%d")
            active_cutoff = (now - timedelta(days=CROSSING_ACTIVE_DAYS)).strftime("%Y-%m-%d")
            search_windows = []
            for scope in _REPO_SEARCH_SCOPES:
                search_windows.append(  # A 新星窗
                    ("rising", f"{scope} created:>{rising_cutoff} stars:>={RISING_MIN_STARS}", "desc"))
                search_windows.append(  # B 穿越窗（升冪取剛越過門檻者）
                    ("crossing", f"{scope} stars:{CROSSING_STAR_RANGE} pushed:>{active_cutoff}", "asc"))

            window_pool: dict[str, list] = {"rising": [], "crossing": []}
            for window, query, order in search_windows:
                try:
                    _search_throttle()
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
                        star_seen[repo["html_url"].rstrip("/")] = repo.get("stargazers_count", 0)
                        url_key = repo["html_url"].rstrip("/").lower()
                        # 共用已報導閘：日報＋清倉帳本出現過的不再吐（改版前 A/B 只有
                        # 14 天 TTL 的 emitted-cache，清倉後的 repo 會被重吐）
                        if emitted is not None and url_key in emitted:
                            continue
                        window_pool[window].append(repo)
                except Exception as e:
                    logger.warning("GitHub repo search '%s' failed: %s", query, e)

            for window, pool in window_pool.items():
                # 各窗硬上限：rising 依星數降冪取前 N、crossing 依星數升冪取前 N
                pool.sort(key=lambda r: r.get("stargazers_count", 0),
                          reverse=(window == "rising"))
                picked = []
                seen_urls_local = set()
                for repo in pool:
                    if repo["html_url"] in seen_urls_local:
                        continue
                    seen_urls_local.add(repo["html_url"])
                    picked.append(repo)
                    if len(picked) >= AB_WINDOW_CAP:
                        break
                _record_queue(window, queued=len(pool), emitted_n=len(picked), now=now)
                for repo in picked:
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

            items = items + _inventory_sweep(headers, now, emitted, star_seen)
            items = items + _velocity_sweep(headers, now, emitted, star_seen)
            _record_star_history(star_seen, now)
            # 總量硬上限：壞掉時的爆炸半徑（改版前為 MAX_ITEMS_PER_SOURCE*2=40）
            return items[:SOURCE_TOTAL_CAP]
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


def _record_queue(window: str, queued: int, emitted_n: int, now: datetime, note: str = "ok") -> None:
    """發現窗產消對帳（D7 量規）：每窗每日一列，同日 upsert。

    schema：date,window,queued,emitted,note（note 值域 ok|cold_start|disabled|error）。
    「今天沒有候選」（queued=0 的列）與「今天這個窗沒跑」（整列缺席）必須分得開——
    lint 6e 以「某窗連 3 天缺列」判窗靜默死亡。
    """
    try:
        hist = NEWS_DIR.parent / "data" / "discovery_queue_history.csv"
        today = now.strftime("%Y-%m-%d")
        prefix = f"{today},{window},"
        if hist.exists():
            rows = [l for l in hist.read_text(encoding="utf-8").splitlines()
                    if l and not l.startswith(prefix)]
        else:
            rows = ["date,window,queued,emitted,note"]
        rows.append(f"{today},{window},{queued},{emitted_n},{note}")
        hist.write_text("\n".join(rows) + "\n", encoding="utf-8")
    except Exception as e:
        logger.warning("Discovery queue history write failed (%s): %s", window, e)


STAR_HISTORY_RETENTION_DAYS = 60  # E 窗歷史檔保留天數（每日 ~數百列，防無限增長）


def _record_star_history(star_seen: "dict[str, int]", now: datetime) -> None:
    """E 窗記錄端（Phase 1，2026-09-03）：把本次各窗查詢看到的每個 repo 星數記一列。

    資料已在記憶體裡，零額外 API 成本。只記錄、不吐條目——吐出端（星速觸發）
    待 ≥2 週真實資料校準閾值後另行上線（Phase 2）。schema：date,repo_url,stars，
    同日同 repo upsert。壞掉時的樣子：本函式失敗只 warning 不中斷抓取；
    「歷史檔沒在長」由 lint 6e 的產消對帳看守（雲端保存靠 daily-gather 指名 commit）。
    """
    if not star_seen:
        return
    try:
        hist = NEWS_DIR.parent / "data" / "repo_star_history.csv"
        today = now.strftime("%Y-%m-%d")
        keep_after = (now - timedelta(days=STAR_HISTORY_RETENTION_DAYS)).strftime("%Y-%m-%d")
        rows = []
        if hist.exists():
            for l in hist.read_text(encoding="utf-8").splitlines()[1:]:
                if not l:
                    continue
                parts = l.split(",")
                d, url = parts[0], parts[1] if len(parts) > 1 else ""
                if d < keep_after:
                    continue  # 逾保留期
                if d == today and url in star_seen:
                    continue  # 同日同 repo upsert
                rows.append(l)
        for url, stars in sorted(star_seen.items()):
            rows.append(f"{today},{url},{stars}")
        hist.write_text("date,repo_url,stars\n" + "\n".join(rows) + "\n", encoding="utf-8")
        logger.info("Star history: recorded %d repos (file now %d rows)", len(star_seen), len(rows))
    except Exception as e:
        logger.warning("Star history write failed: %s", e)


def _inventory_sweep(headers: dict, now: datetime,
                     emitted: "set[str] | None" = None,
                     star_seen: "dict[str, int] | None" = None) -> list[FeedItem]:
    """C 窗：把每條 scope 底下「已成名但本庫從未報導過」的 repo 逐日補進來。

    設計說明見檔頭 `_INVENTORY_SCOPES` 常數區。
    """
    if emitted is None:
        emitted = _emitted_repo_urls()
    if emitted is None:
        _record_queue("inventory", 0, 0, now, note="error")
        return []

    candidates: dict[str, dict] = {}
    for scope in _INVENTORY_SCOPES:
        try:
            _search_throttle()
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
                if not url:
                    continue
                if star_seen is not None:  # E 窗記錄端：C 窗看到的也記
                    star_seen[url] = repo.get("stargazers_count", 0)
                if url.lower() not in emitted:
                    candidates[url] = repo
        except Exception as e:
            logger.warning("Inventory sweep '%s' failed: %s", scope, e)

    picked = sorted(candidates.values(), key=lambda r: r.get("stargazers_count", 0), reverse=True)
    picked = picked[:INVENTORY_PER_DAY]
    logger.info("Inventory sweep: %d unreported repos in range, emitting %d",
                len(candidates), len(picked))

    # 產消對帳（2026-09-02 建，09-03 泛化為逐窗五欄制）。教訓：C 窗上線 5 天悄悄積
    # 到 154 個未報導候選（每日吐 2 ≈ 77 天排空），佇列長度只在上面那行 logger.info
    # ——訊號無消費端，與 pending 佇列 19 天 0→51 同病。
    _record_queue("inventory", queued=len(candidates), emitted_n=len(picked), now=now)

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


def _velocity_candidates(history_rows: "list[tuple[str, str, int]]",
                         star_seen: "dict[str, int]",
                         emitted: "set[str]",
                         today: str) -> "list[tuple[float, float, int, int, int, str]]":
    """E 窗判定核心（純函式，供測試鎖行為）。

    輸入：星史列（date, url, stars）、今日觀測、已報導閘、今日日期字串。
    輸出：達標候選 [(星速/日, 成長%/日, 星差, 天數, 現星數, url)]，星速降冪。
    比較基準取回看窗內**最舊**且距今 ≥ VELOCITY_MIN_SPAN_DAYS 的觀測——取最舊
    而非任兩點，讓速度量的是「這一週」而不是被單日抖動放大。
    """
    from datetime import date as _date
    today_d = _date.fromisoformat(today)
    obs: dict[str, dict[str, int]] = {}
    for d, url, stars in history_rows:
        try:
            age = (today_d - _date.fromisoformat(d)).days
        except ValueError:
            continue
        if 0 <= age <= VELOCITY_LOOKBACK_DAYS:
            obs.setdefault(url, {})[d] = stars
    for url, stars in star_seen.items():
        obs.setdefault(url, {})[today] = stars

    out = []
    for url, series in obs.items():
        if url.rstrip("/").lower() in emitted:
            continue
        if today not in series or len(series) < 2:
            continue
        oldest = min(series)
        span = (today_d - _date.fromisoformat(oldest)).days
        if span < VELOCITY_MIN_SPAN_DAYS:
            continue
        delta = series[today] - series[oldest]
        base = series[oldest] or 1
        v = delta / span
        rel = 100.0 * delta / base / span
        if v >= VELOCITY_ABS or (v >= VELOCITY_FAST and rel >= VELOCITY_REL_PCT):
            out.append((v, rel, delta, span, series[today], url))
    out.sort(reverse=True)
    return out


def _fetch_repo_meta(url: str, headers: dict) -> dict:
    """取單一 repo 的 metadata（core REST，非 search 配額）；失敗回空 dict。"""
    m = re.match(r"^https://github\.com/([\w.\-]+)/([\w.\-]+)$", url.rstrip("/"))
    if not m:
        return {}
    try:
        r = requests.get(f"https://api.github.com/repos/{m.group(1)}/{m.group(2)}",
                         headers=headers, timeout=REQUEST_TIMEOUT)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        logger.warning("Velocity sweep repo lookup failed for %s: %s", url, e)
    return {}


def _velocity_sweep(headers: dict, now: datetime,
                    emitted: "set[str] | None",
                    star_seen: "dict[str, int]") -> list[FeedItem]:
    """E 窗吐出端：星史快照自算星速，吐出正在暴衝但各窗排序不到的 repo。

    設計說明與閾值校準見檔頭 VELOCITY_* 常數區。
    """
    if emitted is None:
        _record_queue("velocity", 0, 0, now, note="error")
        return []
    today = now.strftime("%Y-%m-%d")
    history_rows: list[tuple[str, str, int]] = []
    try:
        hist = NEWS_DIR.parent / "data" / "repo_star_history.csv"
        if hist.exists():
            for l in hist.read_text(encoding="utf-8").splitlines()[1:]:
                parts = l.split(",")
                if len(parts) >= 3:
                    try:
                        history_rows.append((parts[0], parts[1], int(parts[2])))
                    except ValueError:
                        continue
    except Exception as e:
        logger.warning("Velocity sweep: star history unreadable, skipping (%s)", e)
        _record_queue("velocity", 0, 0, now, note="error")
        return []
    if not history_rows:
        # 冷啟動（星史尚未累積）與「今天沒人達標」要分得開
        _record_queue("velocity", 0, 0, now, note="cold_start")
        return []

    candidates = _velocity_candidates(history_rows, star_seen, emitted, today)
    picked = candidates[:VELOCITY_PER_DAY]
    _record_queue("velocity", queued=len(candidates), emitted_n=len(picked), now=now)
    logger.info("Velocity sweep: %d over threshold, emitting %d", len(candidates), len(picked))

    items = []
    for v, rel, delta, span, stars, url in picked:
        meta = _fetch_repo_meta(url, headers)
        desc = (meta.get("description") or "")[:300]
        name = meta.get("full_name") or "/".join(url.rstrip("/").split("/")[-2:])
        items.append(FeedItem(
            title=name,
            url=url,
            source="GitHub Search",
            published=now,
            score=stars,
            score_unit="星",
            # 前綴是給日報撰寫者的誠實訊號：這則的新聞點是「成長速度」本身，
            # 不是 repo 剛出生也不是首次成名——寫作時應交代它正在暴衝。
            summary=f"[星速偵測｜近 {span} 天 +{delta:,} 星（約 {v:,.0f} 星/日）] {desc}",
            category="community",
        ))
    return items
