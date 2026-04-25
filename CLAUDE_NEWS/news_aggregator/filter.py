"""LLM-based relevance filter.

Sends all items to Claude Haiku in a single batched call and asks for a
relevance score 1–5 per item.  Items scoring below `min_score` are dropped.

Falls back to keeping all items if the API key is missing or the call fails.
"""
import json
import logging
import os
import re

from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

_SYSTEM = (
    "你是新聞分類專家，專門評估科技新聞與「Claude Code / Anthropic AI 技術動態」的相關程度。"
    "輸出純 JSON，不要加任何前言或說明。"
)

_PROMPT = """\
以下是 {count} 篇新聞，請評估每篇與「Claude Code 或 Anthropic 技術動態」的相關程度。

評分標準：
5 = 核心：直接討論 Claude Code 功能、bug、使用體驗、版本更新
4 = 重要：Anthropic 官方公告（模型發布、定價、政策、API 變更）
3 = 相關：AI 工具/代理框架趨勢，且與 Claude/Anthropic 有明確連結
2 = 邊緣：只是附帶提及 Anthropic/Claude，主題是其他產品或公司
1 = 無關：主題與 Claude Code 或 Anthropic 無實質關連

請輸出 JSON 陣列，每個元素只含 idx（從 0 開始）和 score：
[{{"idx": 0, "score": 4}}, {{"idx": 1, "score": 2}}, ...]

文章列表：
{items_text}
"""


def filter_relevant(items: list[FeedItem], min_score: int = 3) -> list[FeedItem]:
    """Return only items with LLM relevance score >= min_score.

    Falls back to all items if filter cannot run.
    """
    if not items:
        return items

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        logger.info("ANTHROPIC_API_KEY not set — skipping relevance filter")
        return items

    try:
        scores = _score_items(items, api_key)
        kept = [item for item, score in zip(items, scores) if score >= min_score]
        dropped = len(items) - len(kept)
        logger.info(
            "Relevance filter: kept %d / %d items (dropped %d with score < %d)",
            len(kept), len(items), dropped, min_score,
        )
        return kept if kept else items  # never return empty list
    except Exception as e:
        logger.warning("Relevance filter failed (%s) — keeping all %d items", e, len(items))
        return items


# ── internals ─────────────────────────────────────────────────────────────────

def _score_items(items: list[FeedItem], api_key: str) -> list[int]:
    import anthropic

    items_text = _format_for_filter(items)
    prompt = _PROMPT.format(count=len(items), items_text=items_text)

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = message.content[0].text.strip()

    return _parse_scores(raw, len(items))


def _format_for_filter(items: list[FeedItem]) -> str:
    lines = []
    for i, item in enumerate(items):
        summary_snippet = item.summary[:200].replace("\n", " ") if item.summary else ""
        lines.append(
            f"{i}. {item.title}\n"
            f"   來源: {item.source} | 摘要: {summary_snippet}"
        )
    return "\n\n".join(lines)


def _parse_scores(raw: str, expected: int) -> list[int]:
    """Parse JSON array from LLM response; fall back to score=5 (keep all)."""
    try:
        # Strip markdown code fences if present
        cleaned = re.sub(r"```[a-z]*\n?", "", raw).strip().rstrip("`")
        data = json.loads(cleaned)
        score_map: dict[int, int] = {entry["idx"]: entry["score"] for entry in data}
        return [score_map.get(i, 5) for i in range(expected)]
    except Exception as e:
        logger.warning("Could not parse filter scores (%s) — keeping all", e)
        return [5] * expected
