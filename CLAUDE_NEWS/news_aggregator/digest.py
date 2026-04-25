from datetime import date, datetime, timezone
from pathlib import Path

from news_aggregator.analyzer import analyze
from news_aggregator.config import NEWS_DIR
from news_aggregator.sources.base import FeedItem


def render(
    items: list[FeedItem],
    run_date: date,
    source_status: dict[str, dict],
) -> Path:
    NEWS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = NEWS_DIR / f"{run_date.isoformat()}.md"

    now_str = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total_sources = len(source_status)
    ok_sources = sum(1 for s in source_status.values() if s["ok"])

    header = [
        "# Claude Code & Anthropic 每日新聞摘要",
        "",
        f"**日期：** {run_date.isoformat()} &nbsp;|&nbsp; "
        f"**來源：** {ok_sources}/{total_sources} &nbsp;|&nbsp; "
        f"**文章數：** {len(items)} &nbsp;|&nbsp; "
        f"**更新時間：** {now_str}",
        "",
        "---",
        "",
    ]

    body = analyze(items)

    footer = [
        "",
        "---",
        "",
        "## 來源狀態",
        "",
        "| 來源 | 狀態 | 文章數 |",
        "|------|:----:|:------:|",
    ]
    for src_name, info in source_status.items():
        status_icon = "✅" if info["ok"] else "❌"
        footer.append(f"| {src_name} | {status_icon} | {info['count']} |")

    footer += [
        "",
        "> 備注：Twitter/X 資料不包含在本摘要中（官方 API 需付費）。",
        "",
        "---",
        "",
        f"*自動產生 by Claude Code News Aggregator · {now_str}*",
    ]

    content = "\n".join(header) + body + "\n\n" + "\n".join(footer)
    out_path.write_text(content, encoding="utf-8")
    return out_path
