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

    Tries: API key → claude CLI → keep all (fallback).
    """
    if not items:
        return items

    raw: str | None = None

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        try:
            raw = _call_api(items, api_key)
        except Exception as e:
            logger.warning("Relevance filter API failed (%s) — trying claude CLI", e)

    if raw is None:
        raw = _call_claude_cli(items)

    if raw is None:
        logger.warning("Relevance filter unavailable — keeping all %d items", len(items))
        return items

    try:
        scores = _parse_scores(raw, len(items))
        kept = [item for item, score in zip(items, scores) if score >= min_score]
        dropped = len(items) - len(kept)
        logger.info(
            "Relevance filter: kept %d / %d items (dropped %d with score < %d)",
            len(kept), len(items), dropped, min_score,
        )
        return kept if kept else items  # never return empty list
    except Exception as e:
        logger.warning("Relevance filter parse failed (%s) — keeping all %d items", e, len(items))
        return items


# ── internals ─────────────────────────────────────────────────────────────────

def _call_api(items: list[FeedItem], api_key: str) -> str:
    import anthropic

    prompt = _PROMPT.format(count=len(items), items_text=_format_for_filter(items))
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


def _call_claude_cli(items: list[FeedItem]) -> str | None:
    import shutil
    import subprocess
    import sys

    if not shutil.which("claude"):
        logger.warning("claude CLI not found in PATH — skipping relevance filter")
        return None

    prompt = _PROMPT.format(count=len(items), items_text=_format_for_filter(items))
    full_prompt = f"{_SYSTEM}\n\n{prompt}"
    use_shell = sys.platform == "win32"
    try:
        result = subprocess.run(
            ["claude", "-p"],
            input=full_prompt.encode("utf-8"),
            capture_output=True,
            timeout=120,
            shell=use_shell,
        )
        stdout = result.stdout.decode("utf-8", errors="replace")
        stderr = result.stderr.decode("utf-8", errors="replace")
        if result.returncode == 0 and stdout.strip():
            logger.info("claude CLI filter succeeded")
            return stdout.strip()
        logger.warning("claude CLI filter exited %d: %s", result.returncode, stderr[:200])
    except subprocess.TimeoutExpired:
        logger.warning("claude CLI filter timed out")
    except Exception as e:
        logger.warning("claude CLI filter failed: %s", e)
    return None


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
