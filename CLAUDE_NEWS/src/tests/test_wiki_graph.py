"""wiki_graph.py 煙霧測試 — 節點查詢層的最低保證。

守的是「衍生層必須有消費迴路」的定律（2026-08-27 節點政策辯論共識）：
wiki 模板或 wikilink 語法改版若讓解析器失效，這裡當天紅，不會靜默腐爛。
"""
import re
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


class GraphJsonContract(unittest.TestCase):
    """網站地圖的資料契約（web_reader/data/graph.json，build_web.py 產出）。"""

    def _graph(self):
        import json
        from pathlib import Path
        p = Path(__file__).resolve().parents[2] / "web_reader" / "data" / "graph.json"
        if not p.exists():
            self.skipTest("graph.json 尚未建置")
        return json.loads(p.read_text(encoding="utf-8"))

    def test_節點標籤非空_否則領域chip全淡(self):
        """2026-09-04 實例：產圖區塊排在 readerDomains 計算之前，tags 全空 → 任何領域 chip 點下去整張圖變淡。"""
        g = self._graph()
        pages = [n for n in g["nodes"] if n["pageType"] in ("entity", "topic")]
        self.assertGreater(len(pages), 40)
        untagged = [n["id"] for n in pages if not n.get("tags")]
        self.assertEqual(untagged, [], f"無標籤節點：{untagged[:5]}")
        self.assertTrue(any("💻 開發實務" in n["tags"] for n in pages), "開發實務多標籤未投影進地圖")

    def test_邊端點皆為節點(self):
        g = self._graph()
        ids = {n["id"] for n in g["nodes"]}
        bad = [e for e in g["edges"] if e["s"] not in ids or e["d"] not in ids]
        self.assertEqual(bad, [])


class SimilarityAndGaps(unittest.TestCase):
    """similar／gaps 的門檻契約：單一共享樞紐不算相似，封存頁不推不列。"""

    def _toy(self):
        import wiki_graph as g
        pages = {"hub", "a", "b", "c", "d", "x", "y", "arch/old-archive"}
        L = lambda s, d, z="正文": g.Link(s, d, 1, "", z)
        links = [
            # a 與 b 共享 c、d（不直接相連）→ 相似；x、y 只共享 hub → 不算
            L("a", "c"), L("a", "d"), L("b", "c"), L("b", "d"), L("c", "hub"), L("d", "hub"),
            L("x", "hub"), L("y", "hub"), L("hub", "a"), L("hub", "b"),
            L("arch/old-archive", "c"), L("arch/old-archive", "d"),
        ]
        return g, pages, links

    def test_共享兩個鄰居才算相似_封存頁不推(self):
        g, pages, links = self._toy()
        recs = [r[0] for r in g.similar_pages("a", pages, links, top=5, min_score=0.0)]
        self.assertIn("b", recs)
        self.assertNotIn("arch/old-archive", recs)
        self.assertEqual([r[0] for r in g.similar_pages("x", pages, links, top=5, min_score=0.0)], [])

    def test_gaps_排除已相連與封存(self):
        g, pages, links = self._toy()
        rows, _ = g.gap_pairs(pages, links, top=10, min_score=0.0)
        pairs = {frozenset((a, b)) for a, b, *_ in rows}
        self.assertIn(frozenset(("a", "b")), pairs)
        self.assertFalse(any("archive" in p for pr in pairs for p in pr))
        self.assertNotIn(frozenset(("a", "c")), pairs)   # 已相連


class CoLanded(unittest.TestCase):
    """co-landed：同一則新聞落地兩頁卻不互連。

    全部用臨時帳本，**不得讀 data/source_attribution.jsonl**——真實帳本每天成長，
    拿它當斷言基準的測試會在某天無關的 ingest 後變紅或變假綠。
    """

    def _fixture(self, tmp, rows, ignore=None):
        import json
        import wiki_graph as g
        pages = {"a", "b", "c", "linked1", "linked2", "old/x-archive"}
        L = lambda s, d, z="正文": g.Link(s, d, 1, "", z)
        links = [
            L("linked1", "linked2"),          # 正文邊 → 已相連
            L("a", "c", "樣板"),               # 樣板邊也算已相連（相關實體欄有連結就不算缺）
        ]
        ledger = Path(tmp) / "att.jsonl"
        ledger.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
            encoding="utf-8",
        )
        ig = Path(tmp) / "ig.json"
        ig.write_text(json.dumps({"pairs": ignore or []}, ensure_ascii=False), encoding="utf-8")
        return g, pages, links, ledger, ig

    @staticmethod
    def _row(url, page, date="2026-09-01", title="T"):
        return {"item_url": url, "page": page, "date": date, "item_title": title}

    def test_計數_已相連不列_封存不列(self):
        import tempfile
        rows = [
            # u1、u2 都落在 a 與 b（不相連）→ 應列出，計數 2
            self._row("u1", "a"), self._row("u1", "b"),
            self._row("u2", "a", "2026-09-03", "最新標題"), self._row("u2", "b", "2026-09-03", "最新標題"),
            # linked1/linked2 已相連 → 不列
            self._row("u3", "linked1"), self._row("u3", "linked2"),
            # a/c 有樣板邊 → 算已相連，不列
            self._row("u4", "a"), self._row("u4", "c"),
            # 封存頁 → 不列
            self._row("u5", "b"), self._row("u5", "old/x-archive"),
            # 不在圖上的頁（已刪／改名）→ 不列
            self._row("u6", "b"), self._row("u6", "topics/gone"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            g, pages, links, ledger, ig = self._fixture(tmp, rows)
            out, n_ign = g.co_landed_pairs(pages, links, attribution_path=ledger,
                                           min_shared=1, ignore_path=ig)
            got = {(a, b): (n, title) for a, b, n, title, _ in out}
            self.assertEqual(set(got), {("a", "b")})
            self.assertEqual(got[("a", "b")][0], 2)
            self.assertEqual(got[("a", "b")][1], "最新標題")  # 例＝最新一則
            self.assertEqual(n_ign, 0)

    def test_min_門檻(self):
        import tempfile
        rows = [self._row("u1", "a"), self._row("u1", "b")]
        with tempfile.TemporaryDirectory() as tmp:
            g, pages, links, ledger, ig = self._fixture(tmp, rows)
            kw = dict(attribution_path=ledger, ignore_path=ig)
            self.assertEqual(len(g.co_landed_pairs(pages, links, min_shared=1, **kw)[0]), 1)
            self.assertEqual(len(g.co_landed_pairs(pages, links, min_shared=2, **kw)[0]), 0)

    def test_ignore_檔生效_且與gaps共用格式(self):
        import tempfile
        rows = [self._row("u1", "a"), self._row("u1", "b")]
        with tempfile.TemporaryDirectory() as tmp:
            g, pages, links, ledger, ig = self._fixture(tmp, rows, ignore=[{"pages": ["a", "b"]}])
            out, n_ign = g.co_landed_pairs(pages, links, attribution_path=ledger,
                                           min_shared=1, ignore_path=ig)
            self.assertEqual(out, [])
            self.assertEqual(n_ign, 1)

    def test_預設門檻為1_改動需連同docstring實測數字一起改(self):
        import wiki_graph as g
        self.assertEqual(g.CO_LANDED_MIN_DEFAULT, 1)


class ExplainSection(unittest.TestCase):
    """explain --section：回掃的必查名單靠 anchor 分組，anchor 解析壞掉即失去分組能力。"""

    def test_錨點邊帶目標端anchor(self):
        import wiki_graph as g
        _, _, links = g.build()
        anchored = [l for l in links if l.anchor]
        self.assertTrue(anchored, "全庫零錨點邊＝ANCHORED_WIKILINK_RE 解析失效")
        for l in anchored:
            self.assertEqual(l.zone, "錨點")
            self.assertNotIn("#", l.dst, "dst 不該含錨點，錨點要落在 anchor 欄")

    def test_整頁邊不帶anchor(self):
        import wiki_graph as g
        _, _, links = g.build()
        self.assertTrue(any(l.anchor is None for l in links))


class ExplainLineNumbers(unittest.TestCase):
    """explain 的行號必須是檔案原始行號（含 frontmatter），不是去 frontmatter 後的行號。

    2026-09-06 教訓：wiki_graph 對每頁做 strip_body（剝 frontmatter）後才切行號，
    但顯示給人看的行號從未把 frontmatter 的行數加回去——導致每頁行號都比
    `grep -n` 看到的真實行號少了該頁 frontmatter 的行數（各頁不同，anthropic-business
    少 24 行）。回掃、開檔核對全部會對錯行。
    """

    PAGE = "topics/anthropic-business"
    FILE = Path(__file__).resolve().parents[2] / "wiki" / "topics" / "anthropic-business.md"

    def test_行號對得上grep_n看到的原始行號(self):
        import wiki_graph as g
        _, _, links = g.build()
        raw_lines = self.FILE.read_text(encoding="utf-8-sig").splitlines()
        # 533 為固定測試錨點：本頁時序節內一則指向 entities/pricing 的出邊（2026-09-06 核對）
        target_raw_line = 533
        self.assertIn("[[entities/pricing]]", raw_lines[target_raw_line - 1])
        hit = [l for l in links if l.src == self.PAGE and l.dst == "entities/pricing"
               and l.line == target_raw_line]
        self.assertTrue(hit, "找不到行號等於原始檔案行號的出邊——行號可能仍是去 frontmatter 後的相對行號")

    def test_無邊的行號落在去frontmatter前的相對行號之外(self):
        """反向防呆：不能巧合對上——舊行號（去 frontmatter 後）在這個位置應該是 509，不是 533。"""
        import wiki_graph as g
        _, _, links = g.build()
        stale = [l for l in links if l.src == self.PAGE and l.dst == "entities/pricing" and l.line == 509]
        self.assertEqual(stale, [], "行號仍停留在去 frontmatter 後的相對值，offset 沒有加回去")


class ExplainHeadingZone(unittest.TestCase):
    """explain 的節名歸屬：時序節內的邊不該被上捲到時序之前的最後一個實質標題。

    2026-09-06 教訓：`_semantic_heading` 對「時序」「摘要」等模板標題與純日期標題
    一律跳過、往前找最近的「語意」標題——這個上捲邏輯是為 `sections` 查詢設計的
    （避免命中詞落在過寬的通用標題上）。但套用到 `explain` 的節名顯示上就變成錯的：
    anthropic-business `## 時序` 底下所有邊全部標成再往前的「戰略合作（商業擴張信號）」，
    使用者拿著行號去查以為那則邊在戰略合作表附近，實際上在時序區。
    """

    PAGE = "topics/anthropic-business"

    def test_時序節內的邊標為時序或其月份小標(self):
        import wiki_graph as g
        _, _, links = g.build()
        hit = [l for l in g.build()[2] if l.src == self.PAGE and l.dst == "entities/pricing" and l.line == 533]
        self.assertTrue(hit)
        heading = hit[0].heading
        self.assertTrue(
            heading == "時序" or re.match(r"^\d{4}-\d{2}", heading),
            f"時序節內的邊節名應為「時序」或其 h3 月份，實得：{heading!r}",
        )
