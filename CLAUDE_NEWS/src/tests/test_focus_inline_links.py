# -*- coding: utf-8 -*-
"""聚焦行內連結格式（2026-09-04 起）的解析契約。

冷讀者 review 改版：聚焦 [N] 腳注改為句末行內連結 `（[來源名](url)）`。
prompt reviewer 抓到規格單方面改格式、build_web 解析器沒跟上會三連壞：
focus text 印出字面 markdown、focus badge 全站消失、典藏頁 preview 混入語法。
本測試鎖住三件事：URL 進 ref_urls、顯示文字剝乾淨、badge 能對回區塊條目。
舊 [N] 與 （ref:） 格式的相容不在此檔（沿用既有實檔驗證）。
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_web  # noqa: E402

SAMPLE = """# Claude Code & Anthropic 每日新聞摘要

**日期：** 2026-09-04 | **來源：** 9/10 | **文章數：** 30 | **更新時間：** 2026-09-04 12:00 UTC

---

### 📌 今日聚焦

- **[重大事件]** Claude 發布 Sonnet 6，context 翻倍。（[官方](https://example.com/ann)）
- **[社群趨勢]** 三款工具同批亮相。（[HN](https://example.com/a)、[HN](https://example.com/b)）
- **[持續追蹤]** 無連結的推論句。

### ⭐ 重點話題

**[Some story](https://example.com/ann)**
說明文字。
`Hacker News` · 09/04 10:00 UTC
"""


class FocusInlineLinks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        p = Path(tempfile.mkdtemp()) / "2026-09-04.md"
        p.write_text(SAMPLE, encoding="utf-8")
        cls.r = build_web.parse_digest(p)

    def test_url_抽進_ref_urls(self):
        urls = [f["ref_urls"] for f in self.r["focus"]]
        self.assertEqual(urls[0], ["https://example.com/ann"])
        self.assertEqual(urls[1], ["https://example.com/a", "https://example.com/b"])
        self.assertEqual(urls[2], [])

    def test_顯示文字不殘留_markdown(self):
        for f in self.r["focus"]:
            self.assertNotIn("](http", f["text"], f["text"])
            self.assertNotIn("（[", f["text"], f["text"])

    def test_badge_對回區塊條目(self):
        self.assertEqual(self.r["topStories"][0]["focusTags"], ["[重大事件]"])

    def test_preview_乾淨(self):
        self.assertNotIn("http", self.r["preview"])


if __name__ == "__main__":
    unittest.main()
