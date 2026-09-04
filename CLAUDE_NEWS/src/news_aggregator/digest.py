import re
from datetime import date, datetime, timezone
from pathlib import Path

from news_aggregator.analyzer import analyze
from news_aggregator.config import NEWS_DIR
from news_aggregator.sources.base import FeedItem

# ── Presentation post-processing (呈現優化，2026-07-24) ──────────────────────
#
# 兩項優化都只作用在「📌 今日聚焦」小節，其餘小節（⭐ 重點話題 / 🔧 技術更新 /
# 📰 媒體報導 / 💬 技術熱度討論 / 💰 付費方案動態 / 📡 來源狀態）逐字不動：
# ⚠️ 此路徑非 pipeline 正典（正典為 news-pipeline-steps.md Step 1b，由 Claude session 生成）；
# 本模組僅在 fallback 情境使用，呈現格式停留在 2026-07-24 版（[N] 腳注＋檔尾附錄），
# 2026-09-04 的行內連結改版刻意未跟進——若要啟用此路徑先同步 Step 1b 現行格式。
#
#   a. ref 連結編號化：聚焦條目行內的 `（ref: URL）` 改成 `[N]` 編號引用，
#      URL 移到檔尾一份彙整的參考清單（依首次出現順序編號、同 URL 去重共用
#      同一個編號）。
#   b. 選材門檻下沉：今日聚焦區塊內的「**選材門檻 ...**」meta 說明（連同其
#      子項目）整段移到檔尾，內容一字不刪。
#
# 兩者都是純文字後處理，作用在 header+body+footer 組好之後的完整 markdown
# 字串上，不依賴 body 是 API 產生還是 fallback 產生——沒有「📌 今日聚焦」
# 標題（例如 fallback body）時直接原樣回傳，不是 no-op 就是壞資料。

FOCUS_HEADING_RE = re.compile(r"###\s*📌\s*今日聚焦\s*\n")
FOCUS_REF_RE = re.compile(r"（ref:\s*(https?://[^\s（）)]+)[）)]")
SELECTION_THRESHOLD_RE = re.compile(r"\*\*選材門檻[^\n]*\n(?:- .*\n)+")


def _renumber_focus_refs(section: str) -> tuple[str, list[str]]:
    """Replace inline `（ref: URL）` markers with numbered `[N]` citations
    (deduped by URL, numbered by first appearance). Returns the rewritten
    section text and the ordered URL list (index 0 → citation [1])."""
    url_order: list[str] = []
    url_num: dict[str, int] = {}

    def _sub(m: re.Match) -> str:
        url = m.group(1)
        if url not in url_num:
            url_order.append(url)
            url_num[url] = len(url_order)
        return f"[{url_num[url]}]"

    rewritten = FOCUS_REF_RE.sub(_sub, section)
    return rewritten, url_order


def _extract_selection_threshold(section: str) -> tuple[str, str]:
    """Pull the `**選材門檻 ...**` block (bold intro line + its immediate
    `- ` sub-bullets) out of the 今日聚焦 section. Returns
    (section_without_threshold, threshold_block); threshold_block is '' if
    no such block is present (older digests predate the 選材門檻 calibration
    note, e.g. before 2026-07-16 — this keeps them a no-op)."""
    m = SELECTION_THRESHOLD_RE.search(section)
    if not m:
        return section, ""
    block = m.group(0).rstrip("\n")
    prefix = section[:m.start()]
    # collapse the blank line that used to separate the focus bullets from
    # the threshold block, so removal doesn't leave a dangling empty line
    if prefix.endswith("\n\n"):
        prefix = prefix[:-1]
    rest = section[m.end():]
    return prefix + rest, block


def reformat_presentation(content: str) -> str:
    """Post-process an assembled digest markdown string: renumber 📌 今日聚焦
    inline refs into `[N]` citations (URLs collected into a reference list
    appended at the end of the document) and move the 選材門檻 meta block to
    the end of the document. No-op if there's no 📌 今日聚焦 heading."""
    heading_m = FOCUS_HEADING_RE.search(content)
    if not heading_m:
        return content

    section_start = heading_m.end()
    next_heading_m = re.search(r"\n###\s+", content[section_start:])
    section_end = section_start + next_heading_m.start() if next_heading_m else len(content)

    section = content[section_start:section_end]
    section, threshold_block = _extract_selection_threshold(section)
    section, ref_urls = _renumber_focus_refs(section)

    new_content = content[:section_start] + section + content[section_end:]

    appendix_parts = []
    if threshold_block:
        appendix_parts.append(threshold_block)
    if ref_urls:
        ref_lines = "\n".join(f"{i}. {u}" for i, u in enumerate(ref_urls, 1))
        appendix_parts.append(f"**今日聚焦參考連結：**\n{ref_lines}")

    if appendix_parts:
        new_content = new_content.rstrip("\n") + "\n\n---\n\n" + "\n\n".join(appendix_parts) + "\n"

    return new_content


def render(
    items: list[FeedItem],
    run_date: date,
    source_status: dict[str, dict],
) -> tuple[Path, bool]:
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

    body, analyze_method = analyze(items)

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
        f"*自動產生 by Claude Code News Aggregator · {now_str} · 摘要方式：{analyze_method}*",
    ]

    content = "\n".join(header) + body + "\n\n" + "\n".join(footer)
    content = reformat_presentation(content)
    out_path.write_text(content, encoding="utf-8")
    is_fallback = analyze_method.startswith("fallback")
    return out_path, is_fallback
