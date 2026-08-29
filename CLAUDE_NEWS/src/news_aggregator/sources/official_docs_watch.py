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

State (per URL: previous hash/length/segments, or the page list for index mode) lives next to seen_urls.json. A URL with no
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

# 相對時間戳是易變 chrome：support.claude.com 的 Intercom 小工具會吐
# 「Updated over 2 weeks ago …」，每週自己滾一次而頁面內容一個字沒改。它與
# 價格一樣是「長度守恆的數字變動」，所以任何以數字為鍵的規則都分不開兩者——
# 分不開就不要分，直接從源頭剝掉（同 _SCRIPT_RE 剝 script 的道理）。剝在
# _visible_text 裡，hash 因此也不會為它而變，問題不是被過濾而是不存在。
# 2026-08-29 實測：全庫 4 個段落含此樣式，無其他數字型輪替 chrome。
# `updated` 前綴**必填**：少了它會吃掉正文裡任何「N 天前」的句子——
# 「If you purchased your subscription less than 14 days ago, you may request a
# refund.」的退款期限就這樣消失，而那正是本模組要守的計費事實，且因為
# _visible_text 也剝，hash 不變 → 該事實從此不可能被偵測到（2026-08-29 第 8 輪）。
_VOLATILE_RE = re.compile(
    r"\bupdated\s+(?:about|over|almost|less\s+than)?\s*"
    r"(?:\d+|a|an)\s+(?:second|minute|hour|day|week|month|year)s?\s+ago\b"
    r"|\bupdated\s+(?:just\s+now|today|yesterday|this\s+(?:week|month|year))\b",
    re.I)
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

# 差異裡出現這些字元的變動時，一律繞過長度閘。理由：本清單存在的目的是追蹤
# 定價、配額、截止日這些**數字事實**，而它們的變動常是長度守恆的（$2 → $3 差
# 0 字元）。2026-08-29 實測：長度閘讓這類變動端到端 0 則，且新值被吸收進基線、
# 日後永遠報不出來。反過來把長度閘整個拿掉也不行——state 的 git 歷史顯示 22 個
# commit 中有 28 次字數差 <40 的變動被它擋掉（多為排版與措辭微調）。
_NUMERIC_RE = re.compile(r"[0-9$%]")

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
# 出現在幾個監看頁以上就算樣板。6 個 support 頁共享一份會變動的 Help Center
# 文章索引，官方發一篇新文章時這些頁會同時「變了」——若不剔除，配額頁與計費頁
# 會各自宣稱新增了一段不相干的文章標題（錯誤歸因，非單純噪音）。
#
# 門檻取 3 而非 2 的理由：`claude.com/pricing` 與 `platform.claude.com/.../pricing`
# 是彼此鏡像的兩個定價頁，真正的價格字串可能同時出現在這兩頁。門檻 2 會把
# **創建本模組的那類變動**當成樣板而雙頁靜音——那是唯一不可接受的偽陰性。
# 代價：僅出現在 2 頁的產品導覽列（Claude Cowork、Claude Design…共 9 段）不被
# 過濾，官方上架新產品時該 2 頁會各報一則。已登記為已知取捨。
BOILERPLATE_MIN_PAGES = 3
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

        # 先全部抓回來：樣板判定需要看過本輪所有頁面。注意**存進 state 的是
        # 未過濾的全量段落**，過濾只發生在比較時——存進去的東西一旦帶著
        # 「當時的樣板基準」，基準一變昨天今天就不可比，那正是前三輪三個
        # 缺陷的共同根源（2026-08-29 review 第 4 輪）。
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

        for name, url, mode, raw_body in fetched:
            # index 模式吃原文（_visible_text 會吃掉索引解析器需要的行結構）
            text = raw_body if mode == "index" else _visible_text(raw_body)
            prev = state.get(url)
            if mode == "index":
                item = _index_item(name, url, text, prev, state)
            else:
                item = _hash_item(name, url, text, prev, state,
                                  segments=sorted(segs_by_url[url]),
                                  boilerplate=boilerplate)
            if item is not None:
                items.append(item)

        if fetched:
            _save_state(state)

        return items


def _hash_item(name: str, url: str, text: str, prev, state: dict,
               segments: list[str], boilerplate: set) -> FeedItem | None:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    usable = bool(segments) and len(segments) <= MAX_SEGMENTS

    entry: dict = {"hash": digest, "length": len(text)}
    if usable:
        entry["segments"] = segments
    elif prev and prev.get("segments"):
        # 今日切不出段落（骨架頁、版型改版）或段落數超標，都不代表昨天的基線
        # 該丟。丟了之後訊息會說「本頁尚無可比對的前一版段落」——而那句話在
        # 剛丟完的當下必定是假的（2026-08-29 review 第 6 輪）。
        entry["segments"] = prev["segments"]
    state[url] = entry

    if prev is None:
        logger.info("Official watch '%s' baseline recorded", name)
        return None
    if prev.get("hash") == digest:
        return None

    before = prev.get("segments")
    big_enough = abs(len(text) - int(prev.get("length", 0))) >= MIN_DELTA_CHARS
    if usable and before:
        # 樣板從兩邊同時剔除：對稱套用才不會憑空生出增減（理由見 BOILERPLATE_MIN_PAGES）
        added = sorted((set(segments) - boilerplate) - (set(before) - boilerplate))
        removed = sorted((set(before) - boilerplate) - (set(segments) - boilerplate))
        if added or removed:
            if _touches_numbers(added, removed) or big_enough:
                return _item(name, url, digest,
                             _diff_summary(_head(name, prev, text), added, removed))
            logger.info("Official watch '%s' sub-threshold non-numeric edit", name)
            return None
        if set(segments) != set(before):
            # 原始有差、濾後全空：變動全部落在跨頁共用區，這一頁自己沒改。不發
            # 條目——發一則「未偵測到差異」等於把錯誤歸因從段落層級搬到條目層級。
            logger.info("Official watch '%s' changed only in shared chrome", name)
            return None
        # 原始也全空：段落層看不見這次變動（低於 MIN_SEGMENT_CHARS 的碎片，或只有
        # 重複次數變化）。落到下面的長度閘判斷，過閘則發退化條目。

    # 拿不到可比的段落 diff 時，才退回 2026-08-08 的長度閘這個粗糙代理。它擋的是
    # 輪替 token、「最近瀏覽」小工具那類雜訊；但它對**長度守恆**的編輯無能為力
    # （$2 → $3 差 0 字元），所以絕不能排在段落 diff 前面。
    if not big_enough:
        logger.info("Official watch '%s' changed below threshold", name)
        return None

    if not usable and segments:
        why = f"本頁段落數（{len(segments)}）超過上限 {MAX_SEGMENTS}，不做段落比對"
    elif not segments:
        why = "本次未能從頁面解析出可比對的段落"
    elif before:
        # 段落集合與前一版相同，變動落在段落層看不見的地方（低於
        # MIN_SEGMENT_CHARS 的碎片、或只有重複次數變化）。前一版段落是存在的，
        # 不可說「尚無」（2026-08-29 review 第 7 輪：這句話在此路徑上是假的）。
        why = "段落層級未見差異，變動落在可比對的段落之外"
    else:
        why = "本頁尚無可比對的前一版段落，下次變動起會列出差異"
    return _item(name, url, digest, _head(name, prev, text)
                 + f"此為官方一手文件的變更偵測，非新聞報導；{why}，具體改了什麼需開啟連結比對。")


def _touches_numbers(added: list[str], removed: list[str]) -> bool:
    """差異兩側的數字／金額字元有沒有不同（見 _NUMERIC_RE 的理由）。"""
    a = "".join(_NUMERIC_RE.findall("".join(added)))
    r = "".join(_NUMERIC_RE.findall("".join(removed)))
    return a != r


def _item(name: str, url: str, digest: str, summary: str) -> FeedItem:
    return FeedItem(
        title=f"官方文件更新：{name}",
        url=url,
        # Each change to this stable URL must be its own emitted-cache entry, or only
        # the first one ever reaches a digest (score=0 can never re-ignite).
        dedup_key=f"{url}#{digest[:16]}",
        source="Official Docs",
        published=datetime.now(tz=timezone.utc),
        score=0,
        summary=summary,
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
        # volatile 必須在**標籤剝除與空白收斂之後**才剝，且與 _visible_text 同
        # 順序。剝在標籤還在時，`Updated <time>over <b>2</b> weeks ago</time>`
        # 這種 inline markup 剝不掉，於是 hash 與 segments 對同一頁得出不同
        # 結論（2026-08-29 第 8 輪）。
        seg = _WS_RE.sub(" ", _VOLATILE_RE.sub(" ", _WS_RE.sub(" ", line))).strip()
        if len(seg) >= MIN_SEGMENT_CHARS:
            # 回傳集合而非清單：diff 本來就只用集合語意，存重複段落是白存
            # （定價頁光是重複的表頭列就有 142 段）
            out.add(seg)
    return out


def _boilerplate(segs_by_url: dict) -> set:
    """本輪出現在 ≥ BOILERPLATE_MIN_PAGES 個監看頁的段落（判準見該常數）。

    只用於比較時剔除，**不影響儲存內容**——儲存未過濾的全量，才能讓昨天與
    今天永遠可比，不受樣板集合變動影響。"""
    seen: dict = {}
    for segs in segs_by_url.values():
        for seg in segs:
            seen[seg] = seen.get(seg, 0) + 1
    return {seg for seg, n in seen.items() if n >= BOILERPLATE_MIN_PAGES}


def _head(name: str, prev: dict, text: str) -> str:
    return f"{name} 內容有變動（前次 {int(prev.get('length', 0))} 字 → 本次 {len(text)} 字）。"


def _diff_summary(head: str, added: list[str], removed: list[str]) -> str:
    """把段落差異講成人話。移除型變動最容易被忽略——「9/1 漲價取消」在頁面上
    就是少了一句話，所以兩個方向都要列。"""
    def _fmt(label: str, rows: list[str]) -> str:
        shown = "；".join(r[:SEGMENT_PREVIEW_CHARS] for r in rows[:MAX_LISTED_SEGMENTS])
        more = f"（另有 {len(rows) - MAX_LISTED_SEGMENTS} 段未列）" if len(rows) > MAX_LISTED_SEGMENTS else ""
        return f"{label} {len(rows)} 段：{shown}{more}"

    parts = []
    if added:
        parts.append(_fmt("新增", added))
    if removed:
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
    """剝成純可見文字：標籤、script/style，以及相對時間戳這類易變 chrome。

    volatile 與 _visible_segments 走同一順序（標籤 → 空白收斂 → volatile），
    否則兩者會對同一頁得出不同結論。本函式的輸出餵給 hash，改動它等於改動
    變更偵測的算法——由 test_visible_text_algorithm_is_pinned 的 golden digest
    守著（2026-08-29 第 8 輪發現原本那條守護測試結構上不可能失敗）。
    """
    body = _SCRIPT_RE.sub(" ", html)
    body = _TAG_RE.sub(" ", body)
    body = _WS_RE.sub(" ", body)
    return _WS_RE.sub(" ", _VOLATILE_RE.sub(" ", body)).strip()
