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

# ── 段落級 diff（2026-08-28 加入）──────────────────────────────────────────
#
# hash 模式只給一個 bit：變了／沒變。摘要因此只能寫「具體改了什麼需開啟連結
# 比對」，於是沒有人去比對——2026-08-10 Sonnet 5 定價永久化就死在這個縫裡，
# 而移除型變動（頁面少一句「到期」）尤其隱形。
#
# 修法沿用 _index_item 已證明有效的集合差。hash 與 length 的算法**刻意不動**：
# 改了會讓部署當天每頁同時報假警報，一次就足以把這個來源訓練成可忽略。segments
# 是純新增欄位，舊 state 沒有它則退化並說明。詳細沿革見 wiki/log.md 2026-08-28。
#
# **價格必須和它的主詞留在同一段**，否則 diff 說不出是誰漲價；更糟的是集合差可能
# 算出空的（頁上別的模型已有同一個價格字串時）。因此兩個邊界不能切：
#   td/th —— 切了價格表碎成 `$2 / MTok`，只有 9 字元、低於門檻被整個丟掉
#   div   —— 行銷頁把每個價格各包一個 div，切了同樣碎成無主詞片段
# 2026-08-29 實測 claude.com/pricing：含 div 時 19 個價格段僅 1 個帶模型名，去掉後
# 14 個；且每頁最長段落長度不變，沒有把整頁併成一坨的副作用。
_BLOCK_END_RE = re.compile(
    r"</(?:p|li|h[1-6]|tr|section|article|blockquote|pre)\s*>|<br\s*/?>", re.I)
MIN_SEGMENT_CHARS = 12   # 更短的多半是導覽殘骸與圖示 alt，進來只會製造假 diff
MAX_SEGMENTS = 1200      # 超過此數的頁面不存 segments（state 檔無上限成長的閘）
BOILERPLATE_MIN_PAGES = 2   # 出現在幾個頁面以上就算樣板
_META_KEY = "_meta"         # state 內存放樣板指紋（不是 URL，不會與監看頁衝突）
MAX_LISTED_SEGMENTS = 5  # 摘要裡列幾條就夠了——目的是讓人知道往哪看，不是重現 diff
SEGMENT_PREVIEW_CHARS = 120


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

        # 先全部抓回來再處理：樣板判定需要看過本輪所有頁面（見 _boilerplate）
        fetched = []
        for page in pages:
            url = page.get("url")
            name = page.get("name") or url
            if not url:
                logger.warning("Official watch entry missing url: %s", name)
                continue
            mode = page.get("mode") or "hash"
            try:
                raw_body = _fetch_body(url)
            except Exception as e:
                # A watched page failing must never take the pipeline down; the
                # stored hash is left untouched so the next run retries cleanly.
                logger.warning("Official watch '%s' failed: %s", name, e)
                continue
            fetched.append((name, url, mode, raw_body))

        segs_by_url = {u: _visible_segments(b) for _, u, m, b in fetched if m != "index"}
        boilerplate = _boilerplate(segs_by_url)
        # 樣板集合隨監看清單而變：清單一改，同一段可能從「內容」變成「樣板」
        # 而消失，下次 diff 就會把它報成「移除」。指紋不同時本輪只重記基線、
        # 不報 diff——與舊 state 無 segments 的處理一致。指紋取自設定清單而非
        # 抓取結果，否則單一頁 timeout 會誤判成清單變動（2026-08-29 review）。
        fingerprint = _watch_fingerprint(pages)
        resegmented = state.get(_META_KEY, {}).get("fingerprint") != fingerprint
        if resegmented and state.get(_META_KEY) is not None:
            logger.info("Official watch: watchlist changed, re-baselining segments this run")
        state[_META_KEY] = {"fingerprint": fingerprint}

        for name, url, mode, raw_body in fetched:
            # index 模式吃原文（_visible_text 會吃掉索引解析器需要的行結構）
            text = raw_body if mode == "index" else _visible_text(raw_body)
            prev = state.get(url)
            if mode == "index":
                item = _index_item(name, url, text, prev, state)
            else:
                item = _hash_item(name, url, text, prev, state,
                                  segments=sorted(segs_by_url.get(url, set()) - boilerplate),
                                  resegmented=resegmented)
            dirty = True
            if item is not None:
                items.append(item)

        if dirty:
            _save_state(state)

        return items


def _hash_item(name: str, url: str, text: str, prev, state: dict,
               segments: list[str] | None = None,
               resegmented: bool = False) -> FeedItem | None:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    segments = segments or []
    entry: dict = {"hash": digest, "length": len(text)}
    if segments and len(segments) <= MAX_SEGMENTS:
        entry["segments"] = segments
    state[url] = entry

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
        # Each change to this stable URL must be its own emitted-cache entry, or only
        # the first one ever reaches a digest (score=0 can never re-ignite).
        dedup_key=f"{url}#{digest[:16]}",
        source="Official Docs",
        published=datetime.now(tz=timezone.utc),
        score=0,
        summary=_change_summary(name, prev, text, segments, resegmented),
        category="official",
        score_unit="",
    )


def _visible_segments(body: str) -> set[str]:
    """把頁面切成可比對的段落。

    `_visible_text` 為了讓 asset hash 抖動不算內容變動，把全頁空白壓成單一
    空格——壓完只剩一行，沒有可比對的單位。這裡改為先把區塊結束標籤換成換行
    （markdown 本來就有換行，原樣保留），再逐行收斂空白。
    """
    stripped = _SCRIPT_RE.sub(" ", body)
    stripped = _BLOCK_END_RE.sub('\n', stripped)
    stripped = _TAG_RE.sub(" ", stripped)
    out = set()
    for line in stripped.split('\n'):
        seg = _WS_RE.sub(" ", line).strip()
        if len(seg) >= MIN_SEGMENT_CHARS:
            # 回傳集合而非清單：diff 本來就只用集合語意，存重複段落是白存
            # （定價頁光是重複的表頭列就有 142 段）
            out.add(seg)
    return out


def _boilerplate(segs_by_url: dict) -> set:
    """本輪出現在 ≥ BOILERPLATE_MIN_PAGES 個頁面的段落，視為導覽／頁尾樣板。

    這些段落佔掉六成的儲存量，而且它們變動時報出來的 diff 是「新增 1 段：
    Try Claude Try Claude」——既沒有資訊，又會把真訊號淹掉。判準用「跨頁重複」
    而不是關鍵字黑名單：樣板的定義就是「每頁都有」，這是它唯一穩定的特徵。
    """
    seen: dict = {}
    for segs in segs_by_url.values():
        for seg in segs:
            seen[seg] = seen.get(seg, 0) + 1
    return {seg for seg, n in seen.items() if n >= BOILERPLATE_MIN_PAGES}


def _watch_fingerprint(pages: list) -> list:
    """參與樣板判定的頁面清單（排序後的 URL）。

    取自**設定**而非本輪抓成功的頁：樣板集合會不會位移，取決於清單裡有哪些頁，
    不取決於今天網路好不好。取自抓取結果的話，任一頁 timeout 就會讓當輪所有頁
    的 diff 失效，隔天該頁恢復再失效一輪。

    不雜湊：11 個 URL 存原樣才看得出是哪一頁進出，雜湊只是把失效原因藏起來。
    """
    return sorted(p.get("url") for p in pages
                  if p.get("url") and (p.get("mode") or "hash") != "index")


def _change_summary(name: str, prev: dict, text: str, segments: list[str],
                    resegmented: bool = False) -> str:
    """說出「改了什麼」，而不只是「變了」。

    舊 state 沒有 segments（本函式部署前記的基線），或頁面大到不存 segments 時，
    退回舊的字數敘述——退化是可接受的，靜默地假裝有 diff 才不行。
    """
    head = f"{name} 內容有變動（前次 {prev.get('length', 0)} 字 → 本次 {len(text)} 字）。"
    before = prev.get("segments")
    if resegmented or not before or not segments:
        return head + "此為官方一手文件的變更偵測，非新聞報導；具體改了什麼需開啟連結比對（本頁尚無可比對的前一版段落，下次變動起會列出差異）。"

    before_set, now_set = set(before), set(segments)
    added = [x for x in segments if x not in before_set]
    removed = [x for x in before if x not in now_set]
    if not added and not removed:
        # 只有順序變動：不是內容變更，但 hash 已經不同，還是誠實說明
        return head + "段落內容相同、僅順序或版面調整。"

    def _fmt(label: str, rows: list[str]) -> str:
        shown = "；".join(r[:SEGMENT_PREVIEW_CHARS] for r in rows[:MAX_LISTED_SEGMENTS])
        more = f"（另有 {len(rows) - MAX_LISTED_SEGMENTS} 段未列）" if len(rows) > MAX_LISTED_SEGMENTS else ""
        return f"{label} {len(rows)} 段：{shown}{more}"

    parts = []
    if added:
        parts.append(_fmt("新增", added))
    if removed:
        # 移除型變動最容易被忽略——「9/1 漲價取消」在頁面上就是少了一句話
        parts.append(_fmt("移除", removed))
    return head + "；".join(parts) + "。（官方一手文件的變更偵測，非新聞報導）"


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
        # Keyed by which pages appeared/disappeared, so a later index change on the
        # same URL is a distinct entry rather than a silently-dropped duplicate.
        dedup_key=f"{url}#" + hashlib.sha256(
            ("+".join(added) + "|" + "-".join(removed)).encode("utf-8")
        ).hexdigest()[:16],
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


def _fetch_body(url: str) -> str:
    """抓回未經處理的原文。壓平交給呼叫端決定——段落級 diff 需要原文的區塊邊界。"""
    resp = requests.get(
        url,
        headers={"User-Agent": "ClaudeNewsBot/1.0"},
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.text




def _visible_text(html: str) -> str:
    """Strip markup so cosmetic asset-hash churn doesn't read as a content change."""
    body = _SCRIPT_RE.sub(" ", html)
    body = _TAG_RE.sub(" ", body)
    return _WS_RE.sub(" ", body).strip()
