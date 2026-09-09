"""讀者標籤（`data/reader-tags.json`）的看守。

標籤只給網站 HTML 分類用，與 wiki 標頭的「領域」（記者認領欄）無關。名單住在自己的
檔裡而不是從 index 路由表推導——2026-09-03 曾為了把 claude-code 擋出 tab 而把抽取
範圍縮到表格列，09-06 有人在表裡加一列，它就從表格列這條路靜默回來了。本檔看守的是
「靜默」：id 打錯、標籤值沒有對應的前端 chip、以及已裁決不列的頁面悄悄回流。
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CFG = ROOT / "data" / "reader-tags.json"
INDEX_HTML = ROOT / "web_reader" / "index.html"
APP_JS = ROOT / "web_reader" / "assets" / "app.js"


def _cfg():
    return json.loads(CFG.read_text(encoding="utf-8"))


def _wiki_slugs():
    slugs = set()
    for sub in ("entities", "topics"):
        for f in (ROOT / "wiki" / sub).glob("*.md"):
            slugs.add(f.stem)
    return slugs


class TestSchema(unittest.TestCase):
    def test_every_tag_has_label_definition_and_pages(self):
        for tag, spec in _cfg()["tags"].items():
            for field in ("label", "定義", "維護", "pages"):
                self.assertIn(field, spec, f"{tag} 缺 {field} 欄")
            self.assertTrue(spec["定義"].strip(), f"{tag} 的定義句是空的——沒有定義句的標籤，六個人會有六把尺")

    def test_no_duplicate_pages_within_a_tag(self):
        for tag, spec in _cfg()["tags"].items():
            pages = spec["pages"]
            self.assertEqual(len(pages), len(set(pages)), f"{tag} 的 pages 有重複 id")


class TestNoDeadIds(unittest.TestCase):
    """id 打錯 → 那頁靜默從 tab 消失，畫面上看不出差別（舊機制的 feature-radar 就是這樣）。"""

    def test_every_listed_page_exists(self):
        known = _wiki_slugs()
        for tag, spec in _cfg()["tags"].items():
            dead = [s for s in spec["pages"] if s not in known]
            self.assertEqual(dead, [], f"{tag} 名單裡有不存在的頁面 id：{dead}")


class TestFrontEndChipExists(unittest.TestCase):
    """chip 是寫死的：新增標籤值卻沒動前端，那個標籤就永遠沒有入口，讀者按不到。"""

    def test_each_tag_has_chip_and_map_chip(self):
        html = INDEX_HTML.read_text(encoding="utf-8")
        js = APP_JS.read_text(encoding="utf-8")
        map_chips = re.search(r"const MAP_CHIPS = \[(.*?)\]", js, re.S)
        self.assertIsNotNone(map_chips, "app.js 找不到 MAP_CHIPS")
        for tag in _cfg()["tags"]:
            self.assertIn(f'data-domain="{tag}"', html, f"index.html 的 chip 列少了 {tag}")
            self.assertIn(tag, map_chips.group(1), f"app.js 的 MAP_CHIPS 少了 {tag}")


class TestDecidedExclusions(unittest.TestCase):
    """已裁決不列的頁面不得回流——這正是本檔存在的理由。"""

    EXCLUDED = {
        "market-signals": "投資訊號判讀，不是程式（使用者原話：「market signal 不是程式」）",
        "competitor-landscape": "競品雷達＝市場在幹嘛；「別家誰強」的主出口 model-task-leaderboard 已在名單",
        "anthropic-business": "估值／IPO／營收，跟寫 code 的距離同 market-signals",
        "fable-5": "模型實體頁是那個模型的百科；選型的家是 model-comparison",
        "opus-5": "同上——模型頁一律不列，才不會出現「fable-5 在、預設模型 sonnet-5 不在」的不一致",
    }

    def test_decided_exclusions_stay_out(self):
        """2026-09-09 使用者逐頁裁決不列的五頁，不得悄悄回到名單。"""
        pages = _cfg()["tags"]["💻 開發實務"]["pages"]
        for slug, why in self.EXCLUDED.items():
            self.assertNotIn(slug, pages, f"{slug} 不算開發實務：{why}")


if __name__ == "__main__":
    unittest.main()
