"""Tests for scripts/scan_expiring_deadlines.py。

這個偵測器存在的理由是 2026-08-10 那次：官方取消了 9/1 漲價，本庫的「⏰
2026-08-31 到期」倒數掛到剩 5 天才被人工發現。所以測試釘的是「那次會不會被
抓到」，以及兩個會讓它靜默失效的細節：

1. **兩種書寫形式都要掃到**——倒數表列與散文 ⏰ 標記。只認得其中一種，另一種
   就是新的盲區。
2. **同一截止日的多處引用要全部列出**——只報一處，另外兩處會留著舊日期，正是
   2026-08-10 事後上修 13 處的由來。
3. **log.md 不掃**——它記的是歷史，不是對讀者的承諾。
"""
import sys
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import scan_expiring_deadlines as mod  # noqa: E402

NL = chr(10)


class _Wiki:
    def __init__(self, files: dict):
        self._tmp = TemporaryDirectory()
        self.root = Path(self._tmp.name) / "wiki"
        self.root.mkdir()
        for name, text in files.items():
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8")
        self._prev = mod.REPO_ROOT
        mod.REPO_ROOT = self.root.parent

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        mod.REPO_ROOT = self._prev
        self._tmp.cleanup()


class TestBothWritingForms(unittest.TestCase):
    def test_countdown_table_row_is_found(self):
        radar = (
            "## ⏰ 倒數中\n\n"
            "| 截止日 | 事件 | 到期後 | 你該做的決定 |\n"
            "|--------|------|--------|------------|\n"
            "| **2026-08-31** | 週用量 +50% 促銷結束 | 上限可能回落 | 留意是否延長 |\n"
        )
        with _Wiki({"feature-radar.md": radar}) as w:
            found = mod.collect(w.root)
        self.assertEqual([x["date"] for x in found], [date(2026, 8, 31)])
        self.assertIn("週用量", found[0]["what"])

    def test_prose_marker_is_found(self):
        page = "- **⏰ 2026-08-31 到期｜週用量促銷**：官方於 2026-08-18 確認延長。\n"
        with _Wiki({"entities/pricing.md": page}) as w:
            found = mod.collect(w.root)
        self.assertEqual([x["date"] for x in found], [date(2026, 8, 31)])

    def test_prose_excerpt_starts_at_the_marker_not_the_line_start(self):
        """同一行先講別的事時，行首文字會讓報告指向錯的議題（首版即踩到）。"""
        page = "> **已失效並移除的規則**：Fable 5 免費期。另見 ⏰ 2026-08-31 到期條目。\n"
        with _Wiki({"entities/pricing.md": page}) as w:
            found = mod.collect(w.root)
        self.assertTrue(found[0]["what"].startswith("⏰"))
        self.assertNotIn("已失效並移除", found[0]["what"])


class TestEveryReferenceIsListed(unittest.TestCase):
    def test_same_deadline_in_three_places_yields_three_rows(self):
        """只報一處，另外兩處會留著舊日期——2026-08-10 事後上修 13 處的由來。"""
        with _Wiki({
            "feature-radar.md": "| **2026-08-31** | 促銷結束 | x | y |\n",
            "entities/pricing.md": "- ⏰ 2026-08-31 到期｜促銷\n\n> 見 ⏰ 2026-08-31 到期條目\n",
        }) as w:
            found = mod.collect(w.root)
        self.assertEqual(len(found), 3)
        self.assertEqual({x["date"] for x in found}, {date(2026, 8, 31)})


class TestScope(unittest.TestCase):
    def test_log_is_not_scanned(self):
        """log.md 記的是歷史，不是對讀者的承諾。"""
        with _Wiki({"log.md": "- ⏰ 2026-08-31 到期（歷史紀錄）\n"}) as w:
            self.assertEqual(mod.collect(w.root), [])

    def test_scans_the_whole_wiki_not_a_hardcoded_file_list(self):
        """截止日會擴散到別的頁；寫死檔名的偵測器只看得到今天想得到的那兩頁。"""
        with _Wiki({"entities/some-future-model.md": "- ⏰ 2026-09-30 免費期結束\n"}) as w:
            found = mod.collect(w.root)
        self.assertEqual([x["date"] for x in found], [date(2026, 9, 30)])


class TestVerifiedSuppression(unittest.TestCase):
    """查證過就別再天天叫——永遠在響的警報會被整段跳過。"""

    VERIFIED = "- ⏰ 2026-08-31 到期（2026-08-28 查官方原文複查，日期仍有效）｜促銷" + NL
    CROSSREF = "> 另見 ⏰ 2026-08-31 到期條目" + NL
    RADAR_ROW = "| **2026-08-31** | 促銷結束 | x | y |" + NL

    def test_line_marked_verified_is_suppressed(self):
        with _Wiki({"entities/pricing.md": self.VERIFIED}) as w:
            self.assertEqual(mod.collect(w.root, today=date(2026, 8, 29)), [])

    def test_suppression_is_per_deadline_not_per_line(self):
        """同一日期常散在 3 處；只抑制帶註記那行，交叉引用行仍會天天叫。"""
        with _Wiki({"entities/pricing.md": self.VERIFIED + self.CROSSREF,
                    "feature-radar.md": self.RADAR_ROW}) as w:
            self.assertEqual(mod.collect(w.root, today=date(2026, 8, 29)), [])

    def test_suppression_expires_so_it_fires_again_later(self):
        """靜默期過了要重新提醒，否則等於永久關掉。"""
        page = "- ⏰ 2026-09-30 到期（2026-08-28 查官方原文複查，仍有效）" + NL
        with _Wiki({"entities/pricing.md": page}) as w:
            quiet = mod.collect(w.root, today=date(2026, 8, 29))
            later = mod.collect(w.root, today=date(2026, 9, 20))
        self.assertEqual(quiet, [])
        self.assertEqual(len(later), 1)


if __name__ == "__main__":
    unittest.main()
