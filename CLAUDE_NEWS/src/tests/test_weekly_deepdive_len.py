"""`deepdive_visible_len()` 的回歸測試。

它是深挖字數閘門的量測端。舊版連 URL、wikilink 路徑、反引號、粗體星號一起數，
markup 佔比在 5%（W31）到 20%（W34）之間浮動——同樣長度的兩段文字可能差 300 字
才觸發提醒，那不是字數上限而是雜訊（2026-08-30 校準）。

量測函式壞掉不會噴錯，只會把閘門開向錯的一邊：多數了就冤枉合格的稿、少數了就放行
過長的稿。兩種都靜默。故本檔的每一條都釘住「哪些字不該算」。
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

NL = chr(10)

_SPEC = importlib.util.spec_from_file_location(
    "check_weekly_ledger",
    Path(__file__).resolve().parents[2] / "scripts" / "check_weekly_ledger.py",
)
mod = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(mod)
visible = mod.deepdive_visible_len


class DeepdiveVisibleLenTest(unittest.TestCase):
    def test_plain_text_counts_every_non_space_char(self):
        self.assertEqual(visible("同一份工作換個模型差多少"), 12)

    def test_whitespace_and_newlines_do_not_count(self):
        self.assertEqual(visible("  同一份\n工作\t換個模型差多少  "), 12)

    def test_markdown_link_keeps_label_drops_url(self):
        """[文字](url)：讀者讀到的是文字，URL 不佔閱讀成本。"""
        self.assertEqual(
            visible("見[官方定價頁](https://platform.claude.com/docs/en/about-claude/pricing)"),
            len("見官方定價頁"),
        )

    def test_wikilink_is_dropped_entirely(self):
        """[[頁面#錨點]] 在網站上渲染成按鈕，頁名與錨點都不是正文。"""
        self.assertEqual(visible("細節見[[topics/model-comparison#同一份工作，換設定差多少]]"), len("細節見"))

    def test_wikilink_with_alias_is_also_dropped(self):
        self.assertEqual(visible("見[[entities/pricing|定價頁]]"), len("見"))

    def test_inline_code_keeps_content_drops_backticks(self):
        """`count_tokens` 是讀者要讀的字，反引號不是。"""
        self.assertEqual(visible("先跑 `count_tokens`"), len("先跑count_tokens"))

    def test_bold_and_italic_markers_do_not_count(self):
        self.assertEqual(visible("**牌價沒動**，*實付漲了*"), len("牌價沒動，實付漲了"))

    def test_markup_heavy_and_plain_text_of_equal_reading_length_measure_equal(self):
        """本次校準的核心：同樣長度的兩段文字，不該因為誰連結多而差一大截。"""
        plain = "牌價沒動實付卻漲了原因是換代"
        marked = "**牌價沒動**實付卻漲了，原因是[換代](https://example.com/a/very/long/url/indeed)"
        self.assertEqual(visible(plain), 14)
        self.assertEqual(visible(marked), len("牌價沒動實付卻漲了，原因是換代"))

    def test_thresholds_are_the_calibrated_pair(self):
        """門檻與規格檔 `.claude/commands/weekly-report.md` 同步（2026-08-30 校準）。"""
        self.assertEqual((mod.DEEPDIVE_MIN_CHARS, mod.DEEPDIVE_MAX_CHARS), (900, 1300))



class WeeklyNumbersGuardTest(unittest.TestCase):
    """`check_weekly_numbers()` 的回歸測試。

    2026-08-30 W35 踩過：「本週數字」整節寫成三欄表格，markdown 讀起來完全正常，
    但 build_web 的 WEEKLY_STAT_RE 只認 `- **值**——說明`，於是解析出 0 筆、
    網站上該節渲染成空殼。W30–W34 各 5 筆，只有 W35 是 0——**沒有任何檢查會擋**，
    最後是使用者自己發現「怎麼沒有本週數字」。
    """

    def _write(self, tmp, body: str):
        (tmp / "2026-W99.md").write_text(
            "# 2026-W99\n\n## 四、本週數字\n\n" + body + "\n", encoding="utf-8")

    def test_bullet_form_passes(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self._write(tmp, NL.join([
                "- **+25%**——配額調高幅度",
                "- **450 億美元**——合約總額",
                "- **120 ／ 8,265**——未註冊套件份數",
            ]))
            rep: list = []
            self.assertTrue(mod.check_weekly_numbers(rep, tmp), rep)

    def test_table_form_is_blocked(self):
        """殺手：表格在 markdown 裡好看，在網站上是空的。"""
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self._write(tmp, NL.join([
                "| 數字 | 是什麼 |", "|---|---|",
                "| **+25%** | 配額 |", "| **450 億美元** | 合約 |", "| **120** | 套件 |",
            ]))
            rep: list = []
            self.assertFalse(mod.check_weekly_numbers(rep, tmp))
            self.assertIn("寫成表格", " ".join(rep), "訊息要說得出病因，否則讀者只知道數字不對")

    def test_too_few_bullets_is_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self._write(tmp, "- **+25%**——只有一筆")
            rep: list = []
            self.assertFalse(mod.check_weekly_numbers(rep, tmp))

    def test_half_width_dash_is_blocked(self):
        """破折號必須是全形——半形 `--` build_web 認不得，同樣靜默落空。"""
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self._write(tmp, NL.join([
                "- **+25%**--配額", "- **450 億**--合約", "- **120**--套件",
            ]))
            rep: list = []
            self.assertFalse(mod.check_weekly_numbers(rep, tmp))

if __name__ == "__main__":
    unittest.main()
