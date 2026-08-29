"""Tests for official_docs_watch 的段落級 diff。

舊行為只能說「變了」，摘要因此寫「具體改了什麼需開啟連結比對」——警報響了，
沒人知道響什麼，於是沒人去比對。2026-08-10 Sonnet 5 的 $2/$10 永久化、9/1 漲價
取消就死在這個縫裡。

測試釘四件事：

1. **移除型變動要說得出來**——「9/1 漲價取消」在頁面上就是少了一句話，這是最
   容易靜默的方向。
2. **價格必須和它的主詞留在同一段**——切到 td 或 div 會讓 `$2 / MTok` 變成低於
   門檻的碎片被丟掉，價格改動因此變成零 diff，壞在最該偵測的那一頁上。
3. **hash 與 length 的算法不得改動**——改了會讓部署當天所有頁同時報「變了」，
   一次假警報足以把整個來源訓練成可忽略。
4. **跨頁共用區的變動不得歸因到個別頁**，且**儲存的必須是未過濾全量**——後者
   是前者能安全實作的前提。
"""
import hashlib
import json
import logging
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from news_aggregator.sources import official_docs_watch as mod


def _page(*paragraphs):
    return "<html><body>" + "".join(f"<p>{p}</p>" for p in paragraphs) + "</body></html>"


BEFORE = _page(
    "Claude Sonnet 5 costs $2/$10 per million tokens.",
    "Introductory pricing runs through August 31, 2026.",
)
AFTER = _page(
    "Claude Sonnet 5 costs $2/$10 per million tokens.",
    "The scheduled increase to $3/$15 will not occur.",
)


class TestRemovalIsReported(unittest.TestCase):
    def test_the_2026_08_10_change_is_described_not_merely_flagged(self):
        before_segs = sorted(mod._visible_segments(BEFORE))
        after_segs = sorted(mod._visible_segments(AFTER))
        prev = {"hash": "old", "length": len(mod._visible_text(BEFORE)), "segments": before_segs}

        summary = mod._change_summary("方案與定價", prev, mod._visible_text(AFTER),
                                      after_segs, set())

        self.assertIn("新增", summary)
        self.assertIn("will not occur", summary)
        self.assertIn("移除", summary)
        self.assertIn("through August 31", summary)
        # 舊行為的措辭必須消失，否則等於沒修
        self.assertNotIn("需開啟連結比對", summary)

    def test_no_real_difference_yields_no_item(self):
        segs = sorted(mod._visible_segments(BEFORE))
        prev = {"hash": "old", "length": 1, "segments": segs}
        summary = mod._change_summary("x", prev, mod._visible_text(BEFORE), segs, set())
        self.assertIsNone(summary)


class TestHashUnchanged(unittest.TestCase):
    def test_hash_and_length_still_come_from_visible_text(self):
        """算法一改，部署當天每一頁都會報『變了』——假警報比沒警報更貴。"""
        text = mod._visible_text(BEFORE)
        state: dict = {}
        mod._hash_item("x", "https://e.test/p", text, None, state,
                       segments=sorted(mod._visible_segments(BEFORE)), boilerplate=set())
        entry = state["https://e.test/p"]
        self.assertEqual(entry["hash"], hashlib.sha256(text.encode("utf-8")).hexdigest())
        self.assertEqual(entry["length"], len(text))

class TestGracefulDegradation(unittest.TestCase):
    def test_legacy_state_without_segments_falls_back_and_says_so(self):
        """靜默地假裝有 diff 才是問題；退化並說明是可接受的。"""
        prev = {"hash": "old", "length": 10}  # 本功能部署前記下的基線
        summary = mod._change_summary("x", prev, mod._visible_text(AFTER),
                                      sorted(mod._visible_segments(AFTER)), set())
        self.assertIn("下次變動起會列出差異", summary)

    def test_a_shared_index_change_is_not_attributed_to_each_page(self):
        """6 個 support 頁共享一份會變的 Help Center 文章索引（實測 354 段）。
        官方發一篇新文章時若不剔除，6 頁會各報一次「新增 1 段：<新標題>」——
        配額頁與計費頁會宣稱自己新增了一段不相干的內容，錯誤歸因會進 wiki。"""
        shared_old = {"Article A", "Article B"}
        shared_new = shared_old | {"Article C is newly published today"}
        own = "Page one own content sentence."
        boiler = mod._boilerplate({"p1": shared_new | {own},
                                   "p2": shared_new | {"Page two own content."},
                                   "p3": shared_new | {"Page three own content."}})
        prev = {"hash": "o", "length": 10, "segments": sorted(shared_old | {own})}
        summary = mod._change_summary("P1", prev, "x" * 50,
                                      sorted(shared_new | {own}), boiler)
        # 這一頁自己沒改：回 None，_hash_item 因此整則不發
        self.assertIsNone(summary)

    def test_stored_segments_are_unfiltered_so_yesterday_stays_comparable(self):
        """儲存未過濾的全量是整個設計的關鍵：存進去的東西一旦帶著「當時的樣板
        基準」，基準一變昨天今天就不可比——那是前三輪三個缺陷的共同根源。"""
        state: dict = {}
        segs = sorted(mod._visible_segments(BEFORE))
        mod._hash_item("x", "https://e.test/p", mod._visible_text(BEFORE), None,
                       state, segments=segs, boilerplate=set(segs))
        self.assertEqual(state["https://e.test/p"]["segments"], segs)

    def test_oversized_page_stores_no_segments(self):
        huge = _page(*[f"paragraph number {n} with enough characters" for n in range(mod.MAX_SEGMENTS + 50)])
        state: dict = {}
        mod._hash_item("x", "https://e.test/huge", mod._visible_text(huge), None,
                       state, segments=sorted(mod._visible_segments(huge)), boilerplate=set())
        self.assertNotIn("segments", state["https://e.test/huge"])


class TestSegmentation(unittest.TestCase):
    def test_table_rows_are_not_shattered_into_cells(self):
        """切到「格」會讓 `$2 / MTok` 變成 9 字元碎片而低於門檻被丟掉——於是
        「Sonnet 5 從 $2 改成 $3」在偵測器眼中是零變動，正好壞在這個功能唯一
        存在理由的那一頁上（2026-08-28 首版即如此）。"""
        table = ("<table><tr><td>Claude Sonnet 5</td><td>$2 / MTok</td><td>$10 / MTok</td></tr>"
                 "<tr><td>Claude Opus 5</td><td>$5 / MTok</td><td>$25 / MTok</td></tr></table>")
        segs = mod._visible_segments(table)
        self.assertIn("Claude Sonnet 5 $2 / MTok $10 / MTok", segs)
        # 價格必須和模型名在同一段，否則 diff 說不出改的是誰
        self.assertTrue(all("$" in s for s in segs))

        # 行銷頁（claude.com/pricing）不用 table，把每個價格各包一個 div——切 div
        # 同樣會讓價格變成無主詞碎片而被門檻丟掉。2026-08-29 實測：含 div 邊界時
        # 該頁 19 個價格段只有 1 個帶模型名。
        marketing = "<div><div>Claude Sonnet 5</div><div>$2 / MTok</div></div>"
        self.assertEqual(mod._visible_segments(marketing), {"Claude Sonnet 5 $2 / MTok"})

    def test_a_price_change_produces_an_interpretable_diff(self):
        old_t = "<table><tr><td>Claude Sonnet 5</td><td>$2 / MTok</td></tr></table>"
        new_t = "<table><tr><td>Claude Sonnet 5</td><td>$3 / MTok</td></tr></table>"
        prev = {"hash": "o", "length": 1, "segments": sorted(mod._visible_segments(old_t))}
        summary = mod._change_summary("定價", prev, mod._visible_text(new_t),
                                      sorted(mod._visible_segments(new_t)), set())
        self.assertIn("Claude Sonnet 5 $3 / MTok", summary)
        self.assertIn("Claude Sonnet 5 $2 / MTok", summary)

    def test_markdown_newlines_are_preserved(self):
        md = "# Title\n\nSonnet 5 costs $2 per million tokens.\n\nOpus 5 costs $5.\n"
        segs = mod._visible_segments(md)
        self.assertIn("Sonnet 5 costs $2 per million tokens.", segs)


class TestSharedChromeAtFetchLevel(unittest.TestCase):
    """fetch 層的多頁情境。

    單元測 _boilerplate、再單元測 _change_summary，兩者都綠——但 2026-08-29 的
    第 5 輪 review 發現「濾完沒有差異卻照樣發條目」正是從這兩層之間走出來的：
    6 個 support 頁會各發一則「未偵測到差異」，下游 enricher 再把空條目改寫成
    看起來像新聞的摘要。所以這兩條必須測到 fetch。全程 mock，不連網。
    """

    IDX = [f"Help Center article number {n} title text" for n in range(30)]
    URLS = [f"https://support.test/p{i}" for i in range(6)]

    def _page(self, own, idx):
        return "<html><body>" + "".join(f"<p>{x}</p>" for x in idx + [own]) + "</body></html>"

    def _run(self, cfg_path, state_path, own_of, idx):
        with patch.object(mod, "CONFIG_PATH", cfg_path), \
             patch.object(mod, "STATE_PATH", state_path), \
             patch.object(mod, "_fetch_body",
                          lambda u: self._page(own_of(u), idx)):
            return mod.OfficialDocsWatch().fetch()

    def test_a_shared_index_change_emits_nothing_at_all(self):
        """官方發一篇新文章，6 個共享索引的頁都會「變了」——但沒有一頁自己改。
        修法前這裡是 6 則空條目。"""
        logging.disable(logging.CRITICAL)
        self.addCleanup(logging.disable, logging.NOTSET)
        with TemporaryDirectory() as d:
            cfg = Path(d) / "c.json"
            cfg.write_text(json.dumps({"pages": [
                {"name": f"p{i}", "url": u, "status": "active"}
                for i, u in enumerate(self.URLS)]}), encoding="utf-8")
            state = Path(d) / "s.json"
            base = lambda u: f"Own content of page {u[-2:]} here."  # noqa: E731
            self._run(cfg, state, base, self.IDX)          # 基線
            grown = self.IDX + ["Help Center article number 30 title text"]
            self.assertEqual(self._run(cfg, state, base, grown), [])

    def test_a_real_change_on_one_page_still_reports_which_segment(self):
        """對照組：抑制不得誤傷真變動，且要說得出改了哪一段。"""
        logging.disable(logging.CRITICAL)
        self.addCleanup(logging.disable, logging.NOTSET)
        with TemporaryDirectory() as d:
            cfg = Path(d) / "c.json"
            cfg.write_text(json.dumps({"pages": [
                {"name": f"p{i}", "url": u, "status": "active"}
                for i, u in enumerate(self.URLS)]}), encoding="utf-8")
            state = Path(d) / "s.json"
            base = lambda u: f"Own content of page {u[-2:]} here."  # noqa: E731
            self._run(cfg, state, base, self.IDX)
            new = "Sonnet 5 pricing rises to three dollars per million input tokens on September."
            items = self._run(cfg, state,
                              lambda u: new if u.endswith("p2") else base(u), self.IDX)
        self.assertEqual(len(items), 1)
        self.assertIn("p2", items[0].title)
        self.assertIn("Sonnet 5 pricing rises", items[0].summary)

if __name__ == "__main__":
    unittest.main()
