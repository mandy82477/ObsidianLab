import logging
import os

from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

_SYSTEM = "你是一位專注於 AI 技術的中文科技記者，擅長用繁體中文撰寫清晰、客觀的技術新聞摘要。"

_USER_TEMPLATE = """\
以下是今天從各來源收集到的 {count} 條與 Claude / Anthropic 相關的資訊。
每條資料都附有標題、來源連結、以及從原始文章或討論串擷取的實際內容摘要，請善加利用這些內容。

請仔細閱讀，用繁體中文撰寫一份易讀的 Markdown 新聞摘要。

---

## 輸出結構

按以下五個區塊順序輸出（若某區塊無內容則完全省略）：

### ⭐ 重點話題
跨多來源同時出現、引起大量社群討論、或代表重大變化的項目（通常 2–5 則）。

### 🔧 技術更新
模型發布、功能更新、API／SDK 變更、官方公告等。

### 💬 技術熱度討論
社群討論、開發者心得、教學、評測、工具分享等。
每條需在來源行末加上情緒標籤，格式：`情緒：😊 正面` / `情緒：😤 負面` / `情緒：😐 中性` / `情緒：🤔 褒貶不一`
情緒判斷依據討論串的整體氛圍，而非單一留言。

### 💰 付費方案動態
定價調整、訂閱方案、Token 費用、配額限制等。

### 📌 今日聚焦
放在最後，作為全文總結。條列 3–5 點，說明今日最值得關注的主題與趨勢。
每點格式：`**[標籤]** 說明`，標籤選用以下其一：`重大事件`、`持續追蹤`、`新工具`、`社群趨勢`、`風險警示`。
每點 1–2 句，說明「為何值得關注」或「接下來要注意什麼」。
若今日無明顯亮點，可寫「今日新聞平穩，無重大突破」。

---

## 每條資訊的排版格式（嚴格遵守）

一般區塊（⭐ 重點話題、🔧 技術更新、💰 付費方案動態）：
**[原文標題（保持英文）](url)**
一到兩句繁體中文，說明這則資訊的核心重點與為何值得關注。請根據提供的文章摘要內容撰寫，而非只依賴標題猜測。
`來源名稱` · MM/DD HH:MM UTC

💬 技術熱度討論區塊（多一個情緒標籤）：
**[原文標題（保持英文）](url)**
一到兩句繁體中文，說明這則資訊的核心重點與為何值得關注。
`來源名稱` · MM/DD HH:MM UTC · `情緒：😊 正面`

（每兩條之間空一行）

---

## 注意事項

- 重點話題區塊：在標題前加 ⭐，並多寫一句說明「為何是重點」
- 摘要內容如果顯示文章是標題黨或內容空洞，可以在描述中點出（例如「討論熱度高但內容尚待驗證」）
- 語氣客觀、專業、不誇大
- 直接輸出 Markdown，不要加前言、後記或區塊以外的說明文字
- 同一區塊的條目之間保持一個空行，方便閱讀

---

原始資料：

{items_text}
"""


def analyze(items: list[FeedItem]) -> tuple[str, str]:
    """Call Claude to produce a Chinese natural-language digest body.

    Returns (body, method) where method is one of:
      "Anthropic API (claude-haiku-4-5)"
      "claude CLI (Claude.ai Pro)"
      "fallback (純文字列表)"

    Priority:
    1. ANTHROPIC_API_KEY in env → direct SDK call
    2. `claude` CLI available → subprocess call (Claude.ai Pro subscription)
    3. Plain fallback list
    """
    if not items:
        return "## 今日無新增資訊\n\n> 所有來源在過去 26 小時內未發現相關新內容。\n", "—"

    prompt = _USER_TEMPLATE.format(
        count=len(items),
        items_text=_format_items(items),
    )

    # ── Path 1: direct API key ────────────────────────────────────────────
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            message = client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=4096,
                system=_SYSTEM,
                messages=[{"role": "user", "content": prompt}],
            )
            return message.content[0].text, "Anthropic API (claude-haiku-4-5)"
        except Exception as e:
            logger.warning("Claude API (key) failed (%s) — trying claude CLI", e)

    # ── Path 2: claude CLI (Claude.ai Pro subscription) ───────────────────
    result = _call_claude_cli(prompt)
    if result:
        return result, "claude CLI (Claude.ai Pro)"

    # ── Path 3: plain fallback ────────────────────────────────────────────
    logger.warning("All Claude paths failed — using plain fallback digest")
    return _fallback_body(items), "fallback (純文字列表)"


def _call_claude_cli(prompt: str) -> str | None:
    import shutil
    import subprocess
    import sys

    if not shutil.which("claude"):
        logger.warning("claude CLI not found in PATH")
        return None

    full_prompt = f"{_SYSTEM}\n\n{prompt}"
    # Pass prompt via stdin to avoid Windows command-line length limits
    use_shell = sys.platform == "win32"
    try:
        result = subprocess.run(
            ["claude", "-p"],
            input=full_prompt.encode("utf-8"),
            capture_output=True,
            timeout=600,
            shell=use_shell,
        )
        stdout = result.stdout.decode("utf-8", errors="replace")
        stderr = result.stderr.decode("utf-8", errors="replace")
        if result.returncode == 0 and stdout.strip():
            logger.info("claude CLI analysis succeeded")
            return stdout.strip()
        logger.warning("claude CLI exited %d: %s", result.returncode, stderr[:200])
    except subprocess.TimeoutExpired:
        logger.warning("claude CLI timed out after 600s")
    except Exception as e:
        logger.warning("claude CLI failed: %s", e)
    return None


def _format_items(items: list[FeedItem]) -> str:
    lines = []
    for i, item in enumerate(items, 1):
        pub_str = item.published.strftime("%m/%d %H:%M UTC")
        category_label = "官方" if item.category == "official" else "社群"
        score_part = f" | 討論熱度：{item.score}" if item.score > 0 else ""
        # Show up to 600 chars of enriched summary, preserving line breaks for readability
        if item.summary:
            summary_text = item.summary[:600].strip()
            summary_part = f"\n   內容摘要：\n   {summary_text.replace(chr(10), chr(10) + '   ')}"
        else:
            summary_part = ""
        lines.append(
            f"{i}. [{category_label}] {item.title}\n"
            f"   URL：{item.url}\n"
            f"   來源：{item.source} | 時間：{pub_str}{score_part}"
            f"{summary_part}"
        )
    return "\n\n".join(lines)


def _fallback_body(items: list[FeedItem]) -> str:
    lines = []
    for item in items:
        pub_str = item.published.strftime("%m/%d %H:%M UTC")
        score_str = f" — {item.score} 分" if item.score > 0 else ""
        lines.append(f"- **[{item.title}]({item.url})**{score_str}")
        lines.append(f"  *{item.source} · {pub_str}*")
        if item.summary:
            excerpt = item.summary[:150].replace("\n", " ").strip()
            if excerpt:
                lines.append(f"  > {excerpt}")
        lines.append("")
    return "\n".join(lines)
