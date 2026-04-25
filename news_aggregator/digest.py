from datetime import date, datetime, timezone
from pathlib import Path

from news_aggregator.config import NEWS_DIR
from news_aggregator.sources.base import FeedItem


def render(
    items: list[FeedItem],
    run_date: date,
    source_status: dict[str, dict],
) -> Path:
    NEWS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = NEWS_DIR / f"{run_date.isoformat()}.md"

    official = [i for i in items if i.category == "official"]
    community = [i for i in items if i.category == "community"]

    now_str = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total_sources = len(source_status)
    ok_sources = sum(1 for s in source_status.values() if s["ok"])

    lines = [
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

    if official:
        lines += ["## 官方動態", ""]
        lines += _render_group(official)

    if community:
        lines += ["## 社群熱議", ""]
        lines += _render_group(community)

    if not items:
        lines += ["## 今日無新增資訊", "", "> 所有來源在過去 26 小時內未發現相關新內容。", ""]

    # Source status table
    lines += [
        "---",
        "",
        "## 來源狀態",
        "",
        "| 來源 | 狀態 | 文章數 |",
        "|------|:----:|:------:|",
    ]
    for src_name, info in source_status.items():
        status_icon = "✅" if info["ok"] else "❌"
        lines.append(f"| {src_name} | {status_icon} | {info['count']} |")

    lines += [
        "",
        "> 備注：Twitter/X 資料不包含在本摘要中（官方 API 需付費）。",
        "",
        "---",
        "",
        f"*自動產生 by Claude Code News Aggregator · {now_str}*",
    ]

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def _render_group(items: list[FeedItem]) -> list[str]:
    lines = []
    current_source = None
    for item in items:
        if item.source != current_source:
            current_source = item.source
            lines += [f"### {item.source}", ""]
        score_str = f" — **{item.score} 分**" if item.score > 0 else ""
        pub_str = item.published.strftime("%Y-%m-%d %H:%M UTC")
        lines.append(f"- **[{item.title}]({item.url})**{score_str}")
        lines.append(f"  *{item.source} · {pub_str}*")
        if item.summary:
            excerpt = item.summary[:150].replace("\n", " ").strip()
            if excerpt:
                lines.append(f"  > {excerpt}")
        lines.append("")
    return lines
