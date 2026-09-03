import logging
import os

from news_aggregator.config import HAIKU_MODEL
from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

_SYSTEM = "你是一位專注於 AI 技術的中文科技記者，擅長用繁體中文撰寫清晰、客觀的技術新聞摘要。"

_USER_TEMPLATE = """\
以下是今天從各來源收集到的 {count} 條與 Claude / Anthropic 相關的資訊。
每條資料都附有標題、來源連結、以及從原始文章或討論串擷取的實際內容摘要，請善加利用這些內容。

請仔細閱讀，用繁體中文撰寫一份易讀的 Markdown 新聞摘要。

---

## 輸出結構

按以下六個區塊順序輸出（若某區塊無內容則完全省略）：

### 🔔 今日快訊
一行純文字，列出今日 2–3 個最關鍵的技術訊號，讓讀者掃一眼就能判斷是否需要深入閱讀。
格式：`訊號一 ｜ 訊號二 ｜ 訊號三（如有）`
訊號範例：「Claude Code v2.1.x 升版」「無破壞性更新」「新 API 棄用」「Fable 5 管制持續」
若今日無特別訊號，寫「今日新聞平穩」。
**僅輸出一行純文字，不加任何 Markdown 格式符號。**

### 📌 今日聚焦
放在最前面，作為全文導讀。條列 3–5 點，說明今日最值得關注的主題與趨勢。
每點格式：`**[標籤]** 說明`，標籤選用以下其一：`重大事件`、`持續追蹤`、`新工具`、`社群趨勢`、`風險警示`。
每點 1–2 句，說明「為何值得關注」或「接下來要注意什麼」。
若該聚焦點直接對應下方某則**特定文章**，在句末加上 `（ref: URL）`，URL 為該文章的原始連結。
若為跨多篇的主題性描述，則不加 ref。
若今日無明顯亮點，可寫「今日新聞平穩，無重大突破」。

### ⭐ 重點話題
跨多來源同時出現、引起大量社群討論、或代表重大變化的項目（通常 2–5 則）。
- **每則必須寫得出「為何今天是重點」**——一句具體理由（跨幾個來源、討論熱度數字、變化是什麼）。寫不出理由的條目不進本區。
- **`GitHub Search` 來源的存量／發現條目：星數是 repo 一生累積的規模，不是今日討論熱度**，不得僅憑星數進本區或置頂；「本庫首次收錄」不是理由。要進本區，必須有今天的訊號（剛好接上本週某討論、有實測回饋、有新事件）；沒有就放 💬 社群討論區尾端。
- 排序依據＝今日訊號強度（跨來源數、當日互動數），不是累積規模。

### 🔧 官方公告
**僅收錄標記為 `[官方]` 的條目**（Anthropic Blog、GitHub Releases、官方公告）。
模型發布、功能更新、API／SDK 變更等官方訊息。

### 💬 社群討論
**僅收錄標記為 `[社群]` 的條目**（HackerNews、Reddit、dev.to、Google News 轉載、社群工具等）。
開發者心得、教學、評測、工具分享、討論串等。
每條需在來源行末加上情緒標籤，格式：`情緒：😊 正面` / `情緒：😤 負面` / `情緒：😐 中性` / `情緒：🤔 褒貶不一`
情緒判斷依據討論串的整體氛圍，而非單一留言。

### 💰 付費方案動態
定價調整、訂閱方案、Token 費用、配額限制等。

---

## 每條資訊的排版格式（嚴格遵守）

一般區塊（⭐ 重點話題、🔧 技術更新、💰 付費方案動態）：
**[原文標題（保持英文）](url)**
一到兩句繁體中文（**合計 ≤ 80 字**），寫這則的核心事實。請根據提供的文章摘要內容撰寫，而非只依賴標題猜測。
「為何值得關注」只在**摘要本身給得出理由**時寫進句子，寫不出就只寫事實——不得補「值得關注」「值得留意」「後續發展有待觀察」這類無資訊的收尾。
`來源名稱` · MM/DD HH:MM UTC

💬 技術熱度討論區塊（多一個情緒標籤）：
**[原文標題（保持英文）](url)**
一到兩句繁體中文（合計 ≤ 80 字），寫這則的核心事實；「為何值得關注」只在給得出理由時寫。
`來源名稱` · MM/DD HH:MM UTC · `情緒：😊 正面`

（每兩條之間空一行）

---

## 注意事項

- 標題本身以方括號開頭時（如 GitHub issue 的「[BUG] xxx」），markdown 連結須完整保留標題的方括號，寫成 **[[BUG] xxx](url)**——不可把標題的 [ 併入連結語法吞掉（曾造成網站顯示「BUG] xxx」缺左括號）
- 重點話題區塊：在標題前加 ⭐，並多寫一句說明「為何是重點」
- 摘要內容如果顯示文章是標題黨或內容空洞，可以在描述中點出（例如「討論熱度高但內容尚待驗證」）
- **一句一資訊點**：每句只承載一個事實。副詞性評價（「相當」「頗為」「某種程度上」）與空收尾（「值得關注」「有待觀察」「引發廣泛討論」）一律刪除
- **括號補述每條至多一個**，且只用於數字單位、版本號或原文術語；不得用括號堆疊評論
- **缺項用固定短式**：資訊只到標題層級時寫「（僅標題）」，不得展開成「具體 X、Y、Z 未見報導細節，僅標題層級資訊」
- **不重述前情**：同一事件先前已在本區塊出現時，只寫今日增量，不重寫背景
- 語氣客觀、專業、不誇大
- 直接輸出 Markdown，不要加前言、後記或區塊以外的說明文字
- 同一區塊的條目之間保持一個空行，方便閱讀

---

原始資料：

{items_text}
"""


def analyze(items: list[FeedItem]) -> tuple[str, str]:
    """Call Claude API to produce a Chinese natural-language digest body.

    Returns (body, method) where method is one of:
      "Anthropic API (claude-haiku-4-5)"
      "fallback (純文字列表)"
    """
    if not items:
        return "## 今日無新增資訊\n\n> 所有來源在過去 26 小時內未發現相關新內容。\n", "—"

    prompt = _USER_TEMPLATE.format(
        count=len(items),
        items_text=_format_items(items),
    )

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            message = client.messages.create(
                model=HAIKU_MODEL,
                max_tokens=4096,
                system=[{"type": "text", "text": _SYSTEM, "cache_control": {"type": "ephemeral"}}],
                messages=[{"role": "user", "content": prompt}],
            )
            return message.content[0].text, "Anthropic API (claude-haiku-4-5-20251001)"
        except Exception as e:
            logger.warning("Claude API (key) failed (%s) — using plain fallback", e)

    logger.warning("No ANTHROPIC_API_KEY — using plain fallback digest")
    return _fallback_body(items), "fallback (純文字列表)"


def _format_items(items: list[FeedItem]) -> str:
    lines = []
    for i, item in enumerate(items, 1):
        pub_str = item.published.strftime("%m/%d %H:%M UTC")
        category_label = "官方" if item.category == "official" else "社群"
        unit = item.score_unit or "分"
        score_part = f" | 討論熱度：{item.score} {unit}" if item.score > 0 else ""
        source_part = f" | ✦ 跨 {item.source_count} 個獨立來源" if item.source_count > 1 else ""
        # Show up to 600 chars of enriched summary, preserving line breaks for readability
        if item.summary:
            summary_text = item.summary[:600].strip()
            summary_part = f"\n   內容摘要：\n   {summary_text.replace(chr(10), chr(10) + '   ')}"
        else:
            summary_part = ""
        lines.append(
            f"{i}. [{category_label}] {item.title}\n"
            f"   URL：{item.url}\n"
            f"   來源：{item.source} | 時間：{pub_str}{score_part}{source_part}"
            f"{summary_part}"
        )
    return "\n\n".join(lines)


def _fallback_body(items: list[FeedItem]) -> str:
    lines = []
    for item in items:
        pub_str = item.published.strftime("%m/%d %H:%M UTC")
        score_str = f" — {item.score} {item.score_unit or '分'}" if item.score > 0 else ""
        source_note = f" ✦ 跨 {item.source_count} 來源" if item.source_count > 1 else ""
        lines.append(f"- **[{item.title}]({item.url})**{score_str}{source_note}")
        lines.append(f"  *{item.source} · {pub_str}*")
        if item.summary:
            excerpt = item.summary[:150].replace("\n", " ").strip()
            if excerpt:
                lines.append(f"  > {excerpt}")
        lines.append("")
    return "\n".join(lines)
