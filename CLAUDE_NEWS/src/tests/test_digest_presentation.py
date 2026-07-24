"""Tests for news_aggregator.digest.reformat_presentation() — the two
2026-07-24 呈現優化 transformations applied to an assembled digest markdown
string (header + LLM/fallback body + footer):

a. ref 連結編號化：📌 今日聚焦 行內的 `（ref: URL）` 換成 `[N]` 編號引用，
   URL 移到檔尾一份彙整的「今日聚焦參考連結」清單（依首次出現順序編號、
   同 URL 去重共用同一個編號）。
b. 選材門檻下沉：今日聚焦區塊內的「**選材門檻 ...**」meta 說明（連同其
   子項目）整段移到檔尾，內容一字不刪。

Both are pure text post-processing on the fully-assembled content string —
see docstring on reformat_presentation() for why it operates there instead
of on the raw LLM `body` fragment.
"""
import unittest

from news_aggregator.digest import reformat_presentation

SAMPLE = """# Claude Code & Anthropic 每日新聞摘要

**日期：** 2026-03-01 | **來源：** 2/10 | **文章數：** 2 | **更新時間：** 2026-03-01 00:00 UTC

---

### 📌 今日聚焦

- **[重大事件]** 測試事件一，來自兩則新聞。（ref: https://example.com/a）（ref: https://example.com/b）
- **[持續追蹤]** 測試事件二。（ref: https://example.com/c）

**選材門檻 `[加入: 2026-07-16，依首次聚焦校準修正]`：**
- **[新工具]**：測試門檻說明一。
- **[風險警示]**：測試門檻說明二。

---

### 🔧 技術更新

**[技術更新標題](https://example.com/a)**
說明文字一。
`GitHub` · 03/01 00:00 UTC

### 📡 來源狀態

| 來源 | 狀態 | 條數 |
|------|------|------|
| GitHub | ✅ | 1 |
"""


class TestRefRenumbering(unittest.TestCase):
    def setUp(self):
        self.out = reformat_presentation(SAMPLE)

    def test_focus_bullets_use_numbered_citations(self):
        self.assertIn(
            "- **[重大事件]** 測試事件一，來自兩則新聞。[1][2]", self.out
        )
        self.assertIn("- **[持續追蹤]** 測試事件二。[3]", self.out)

    def test_no_inline_ref_urls_remain_in_focus_section(self):
        focus_section = self.out.split("### 🔧 技術更新")[0]
        self.assertNotIn("（ref:", focus_section)
        self.assertNotIn("example.com", focus_section)

    def test_zero_information_loss_all_urls_present_at_tail(self):
        # 紅線：三個 URL 一個都不能少，只是移出閱讀行。
        self.assertIn("https://example.com/a", self.out)
        self.assertIn("https://example.com/b", self.out)
        self.assertIn("https://example.com/c", self.out)
        tail = self.out.split("今日聚焦參考連結")[1]
        self.assertIn("1. https://example.com/a", tail)
        self.assertIn("2. https://example.com/b", tail)
        self.assertIn("3. https://example.com/c", tail)

    def test_duplicate_url_reuses_same_number(self):
        content = SAMPLE.replace(
            "（ref: https://example.com/c）", "（ref: https://example.com/a）"
        )
        out = reformat_presentation(content)
        self.assertIn("- **[持續追蹤]** 測試事件二。[1]", out)
        # 只有兩個相異 URL，參考清單應只有兩筆
        ref_tail = out.split("今日聚焦參考連結：**\n")[1]
        self.assertEqual(ref_tail.strip().count("\n") + 1, 2)

    def test_story_headline_links_untouched(self):
        # ⭐/🔧/📰/💬/💰 各區塊的 **[title](url)** 標題連結不在改寫範圍內。
        self.assertIn("**[技術更新標題](https://example.com/a)**", self.out)


class TestSelectionThresholdRelocation(unittest.TestCase):
    def setUp(self):
        self.out = reformat_presentation(SAMPLE)

    def test_threshold_block_removed_from_focus_section(self):
        focus_section = self.out.split("### 🔧 技術更新")[0]
        self.assertNotIn("選材門檻", focus_section)

    def test_threshold_block_present_verbatim_at_tail(self):
        self.assertIn(
            "**選材門檻 `[加入: 2026-07-16，依首次聚焦校準修正]`：**\n"
            "- **[新工具]**：測試門檻說明一。\n"
            "- **[風險警示]**：測試門檻說明二。",
            self.out,
        )

    def test_threshold_appears_after_source_status_table(self):
        src_idx = self.out.index("### 📡 來源狀態")
        threshold_idx = self.out.index("選材門檻")
        self.assertGreater(threshold_idx, src_idx)


class TestNoFocusHeadingIsNoOp(unittest.TestCase):
    """digest.py's analyze() falls back to _fallback_body() when
    ANTHROPIC_API_KEY is unset (always true in this project) — that body has
    no 📌 今日聚焦 section at all. reformat_presentation() must not touch or
    crash on content with no such heading."""

    def test_content_without_focus_heading_returned_unchanged(self):
        content = (
            "# Claude Code & Anthropic 每日新聞摘要\n\n"
            "**日期：** 2026-03-01 | **來源：** 0/10 | **文章數：** 1 | "
            "**更新時間：** 2026-03-01 00:00 UTC\n\n---\n\n"
            "- **[某標題](https://example.com/x)**\n"
            "  *GitHub · 03/01 00:00 UTC*\n"
        )
        self.assertEqual(reformat_presentation(content), content)


if __name__ == "__main__":
    unittest.main()
