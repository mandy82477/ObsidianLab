"""Topic Watch — 為特定 wiki 專頁定向抓取，繞過 Claude/Anthropic 關聯門檻。

**這個來源存在的理由，是 pipeline 的一個結構性盲區。**

其餘 11 個來源全部在來源端就與 Claude/Anthropic 綁定（Google News 的 QUERIES、
HN 的搜尋詞、Reddit 的 subreddit、dev.to 的 tag、lobste.rs 的標題 regex，或本身
就是官方站台），`filter.py` 再對 Google News 加一道標題關鍵字閘。這是 CLAUDE.md
收錄原則的正確執行——不收與 Claude/Anthropic 無直接關聯的通用 AI 新聞。

但 wiki 有幾頁的主題**天生延伸到那條線之外**。2026-08-05 Jeff Dean、Sanjay
Ghemawat、Oriol Vinyals、Quoc Le 離開 Google 共同創辦 Discovery Loop，是
`topics/ai-talent-flow` 主題史上最大的事件，報導標題卻全是 Google 視角
（"Google AI leadership departures erase $190 billion"），Anthropic 只在內文
被順帶提及甚至完全未提。結果：12 個來源零命中，該頁休眠 31 天，直到使用者
親自問起才被發現。

本來源的解法不是放寬全域門檻（那會把通用 AI 新聞灌進日報），而是**為指定的
wiki 頁開一條窄通道**：每頁配少量經實測校準的 query，抓回來的條目標上 `topic`
＝該頁 slug，該標記是它豁免標題閘的唯一鑰匙（見 `filter.py`），且會在去重合併時
傳染給存活者（見 `dedup._inherit_topic`——不傳染的話定向命中會被靜默丟棄）。

三道防稀釋護欄：每 topic `max_items`、全域 `_global_max`、以及日報把這些條目
收在獨立的「專頁雷達」區塊而非正文六區（見 news-pipeline-steps.md Step 1b）。

設定與 query 校準紀錄見 `topic_watch.json`；**新增 query 前必須實測命中率**，
未驗證的 query 等於沒有偵測力，只會製造雜訊。
"""
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from news_aggregator.sources.base import BaseSource, FeedItem
from news_aggregator.sources.google_news import _fetch_google_query, _resolve_items

logger = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).parent / "topic_watch.json"

DEFAULT_MAX_ITEMS = 3
DEFAULT_GLOBAL_MAX = 8


def _load_config() -> dict:
    if not CONFIG_PATH.exists():
        logger.warning("Topic watch config not found: %s", CONFIG_PATH)
        return {}
    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        # 設定壞掉不得拖垮整個 pipeline——其餘 11 個來源照常。
        logger.warning("Topic watch config is invalid JSON (%s): %s", CONFIG_PATH, e)
        return {}


def _newest_first(items: list[FeedItem]) -> list[FeedItem]:
    return sorted(
        items,
        key=lambda i: i.published or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )


class TopicWatch(BaseSource):
    def fetch(self) -> list[FeedItem]:
        cfg = _load_config()
        topics = [t for t in (cfg.get("topics") or []) if t.get("status") != "retired"]
        if not topics:
            return []

        global_max = int(cfg.get("_global_max") or DEFAULT_GLOBAL_MAX)
        from news_aggregator.config import LOOKBACK_HOURS
        from datetime import timedelta
        cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=LOOKBACK_HOURS)

        collected: list[FeedItem] = []
        for topic in topics:
            slug = topic.get("slug")
            queries = topic.get("queries") or []
            if not slug or not queries:
                logger.warning("Topic watch entry missing slug/queries: %s", topic)
                continue

            got: list[FeedItem] = []
            # 每個 query 獨立失敗——一條掛掉不影響同 topic 的其餘 query。
            with ThreadPoolExecutor(max_workers=len(queries)) as pool:
                for res in pool.map(lambda q: self._safe_query(q, cutoff, slug), queries):
                    got.extend(res)

            seen: set[str] = set()
            unique = [i for i in _newest_first(got) if not (i.url in seen or seen.add(i.url))]
            cap = int(topic.get("max_items") or DEFAULT_MAX_ITEMS)
            kept = unique[:cap]
            if kept:
                logger.info("Topic watch '%s': %d item(s) (from %d)", slug, len(kept), len(unique))
            collected.extend(kept)

        collected = _newest_first(collected)[:global_max]
        return _resolve_items(collected) if collected else []

    @staticmethod
    def _safe_query(query: str, cutoff: datetime, slug: str) -> list[FeedItem]:
        try:
            items = _fetch_google_query(query, cutoff)
        except Exception as e:
            logger.warning("Topic watch query failed (%s / %s): %s", slug, query[:40], e)
            return []
        out = []
        for it in items:
            # summary 前綴讓日報 agent 與記者都自帶語境，不必倚賴額外規則記憶
            note = (
                f"【專頁定向抓取：{slug}】本條的收錄判準是「對該 wiki 專頁有無價值」，"
                f"不套用 Claude/Anthropic 關聯門檻。"
            )
            out.append(FeedItem(
                title=it.title,
                url=it.url,
                source=f"Topic Watch / {slug}",
                published=it.published,
                score=it.score,
                summary=f"{note} {it.summary or ''}".strip(),
                category="media",
                score_unit="",
                topic=slug,
            ))
        return out
