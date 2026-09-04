"""build_web 端的投資訊號解析契約（wiki/topics/market-signals.md → 日報頁 💰 條目）。

判讀標題 `### 💰 事件名（YYYY-MM-DD）` 是規格（`.claude/rules/wiki-ingest-market.md`
「判讀格式（機械契約字串）」表）與程式（`MARKET_SIGNAL_RE`）的共同契約。形狀漂了
不會有任何錯誤訊息——網站上的 💰 條目只是消失，正是 2026-08-14 日報區塊 emoji
的死法。本檔把三件事釘住：

  1. 取的是最新一則（頁面最新在上）且標題／日期解析正確
  2. 日期對得上的那天才注入 marketSignal，其餘日期不動
  3. 頁面不存在或無任何判讀時回 None（無訊號的日子頁面本來就不動）

另加一條真實頁面的煙霧測試：正式頁若有判讀，必須解析得出來。
"""
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module, REPO_ROOT

build_web = load_script_module("build_web")

PAGE = """# 投資訊號判讀

**狀態：** ongoing

## 近期判讀

### 💰 最新事件名（2026-09-04）

**方向**：某公司 ↑。

### 💰 較舊事件名（2026-08-26）

**方向**：某公司 ～。
"""


class TestParseMarketSignal(unittest.TestCase):
    def _write(self, text: str) -> Path:
        d = Path(tempfile.mkdtemp())
        f = d / "market-signals.md"
        f.write_text(text, encoding="utf-8")
        return f

    def test_takes_latest_entry(self):
        sig = build_web.parse_market_signal(self._write(PAGE))
        self.assertEqual(sig, {"title": "最新事件名", "date": "2026-09-04"})

    def test_missing_page_returns_none(self):
        self.assertIsNone(build_web.parse_market_signal(Path("no-such-file.md")))

    def test_no_signal_entries_returns_none(self):
        f = self._write("# 投資訊號判讀\n\n## 近期判讀\n\n本週無訊號。\n")
        self.assertIsNone(build_web.parse_market_signal(f))

    def test_heading_shape_must_match(self):
        """缺 💰、缺全形括號日期、或標成 h2 都不算判讀（契約收得夠緊）。"""
        for bad in ("### 事件名（2026-09-04）",
                    "### 💰 事件名 (2026-09-04)",
                    "## 💰 事件名（2026-09-04）"):
            with self.subTest(bad=bad):
                self.assertIsNone(build_web.parse_market_signal(self._write(bad + "\n")))


class TestAttachMarketSignal(unittest.TestCase):
    def setUp(self):
        self.digests = {"2026-09-04": {"date": "2026-09-04"},
                        "2026-09-03": {"date": "2026-09-03"}}

    def test_injects_only_on_matching_date(self):
        sig = {"title": "事件", "date": "2026-09-04"}
        build_web.attach_market_signal(self.digests, sig)
        self.assertEqual(self.digests["2026-09-04"]["marketSignal"], sig)
        self.assertNotIn("marketSignal", self.digests["2026-09-03"])

    def test_no_signal_injects_nothing(self):
        build_web.attach_market_signal(self.digests, None)
        for d in self.digests.values():
            self.assertNotIn("marketSignal", d)

    def test_date_without_digest_is_noop(self):
        build_web.attach_market_signal(self.digests, {"title": "事件", "date": "2026-01-01"})
        for d in self.digests.values():
            self.assertNotIn("marketSignal", d)


class TestRealPage(unittest.TestCase):
    def test_live_page_parses_if_it_has_entries(self):
        page = REPO_ROOT / "wiki" / "topics" / "market-signals.md"
        if not page.exists():
            self.skipTest("market-signals.md 尚未建立")
        text = page.read_text(encoding="utf-8")
        if "### 💰" not in text:
            self.skipTest("正式頁目前無判讀條目")
        sig = build_web.parse_market_signal(page)
        self.assertIsNotNone(sig, "正式頁有 ### 💰 標題卻解析不出——標題形狀已漂")
        self.assertRegex(sig["date"], r"^\d{4}-\d{2}-\d{2}$")


if __name__ == "__main__":
    unittest.main()
