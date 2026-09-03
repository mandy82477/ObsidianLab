"""wiki_graph.py 煙霧測試 — 節點查詢層的最低保證。

守的是「衍生層必須有消費迴路」的定律（2026-08-27 節點政策辯論共識）：
wiki 模板或 wikilink 語法改版若讓解析器失效，這裡當天紅，不會靜默腐爛。
"""
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import wiki_graph  # noqa: E402


class WikiGraphSmoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages, cls.headings, cls.links = wiki_graph.build()

    def test_圖非空且量級合理(self):
        """55+ 頁的 wiki 至少要有 50 頁節點與 200 條內部邊——低於此代表解析器壞了。"""
        self.assertGreaterEqual(len(self.pages), 50)
        self.assertGreaterEqual(len(self.links), 200)

    def test_樞紐與維運層已排除(self):
        """index/log/news 不得成為節點或邊的端點（辯論共識：無鑑別力樞紐）。"""
        for banned in ("index", "log", "CLAUDE"):
            self.assertNotIn(banned, self.pages)
        for l in self.links:
            self.assertFalse(l.dst.startswith("news/"), f"news/ 懸空邊殘留：{l.src}→{l.dst}")

    def test_explain_pricing_有入邊且帶行號(self):
        """pricing 是全庫高入鏈頁；入邊歸零＝wikilink 解析失效。"""
        inbound = [l for l in self.links if l.dst == "entities/pricing"]
        self.assertGreater(len(inbound), 20)

    def test_產地標記三值(self):
        zones = {l.zone for l in self.links}
        # 「階層」為子故事 part-of 邊（2026-09-03），與引用邊分型；cluster／孤島不計它
        self.assertTrue(zones <= {"正文", "樣板", "錨點", "階層"})
        self.assertIn("正文", zones)
        self.assertIn("樣板", zones)


if __name__ == "__main__":
    unittest.main()
