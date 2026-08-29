"""Tests for official_docs_watch 的段落級 diff。

舊行為只能說「變了」，摘要因此寫「具體改了什麼需開啟連結比對」——警報響了，
沒人知道響什麼，於是沒人去比對。2026-08-10 Sonnet 5 的 $2/$10 永久化、9/1 漲價
取消就死在這個縫裡。

測試釘六件事：

1. **移除型變動要說得出來**——「9/1 漲價取消」在頁面上就是少了一句話，這是最
   容易靜默的方向。
2. **表格切到「列」不切到「格」**——切到格會讓 `$2 / MTok` 變成低於門檻的碎片
   被丟掉，價格改動因此變成零 diff，壞在最該偵測的那一頁上。
3. **hash 與 length 的算法不得改動**——改了會讓部署當天所有頁同時報「變了」，
   一次假警報足以把整個來源訓練成可忽略。
4. **舊 state 沒有 segments 時要退化，不得假裝有 diff。**
5. **跨頁樣板要濾掉**——它佔六成儲存量，且會報出「新增 1 段：Try Claude」這種
   把真訊號淹掉的噪音。
6. **監看清單一改就重記基線**——樣板集合會整批位移，不擋會報出假的「移除」。
"""
import hashlib
import unittest

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

        summary = mod._change_summary("方案與定價", prev, mod._visible_text(AFTER), after_segs)

        self.assertIn("新增", summary)
        self.assertIn("will not occur", summary)
        self.assertIn("移除", summary)
        self.assertIn("through August 31", summary)
        # 舊行為的措辭必須消失，否則等於沒修
        self.assertNotIn("需開啟連結比對", summary)

    def test_unchanged_segments_are_not_reported_as_a_diff(self):
        segs = sorted(mod._visible_segments(BEFORE))
        prev = {"hash": "old", "length": 1, "segments": segs}
        summary = mod._change_summary("x", prev, mod._visible_text(BEFORE), segs)
        self.assertIn("僅順序或版面調整", summary)


class TestHashUnchanged(unittest.TestCase):
    def test_hash_and_length_still_come_from_visible_text(self):
        """算法一改，部署當天每一頁都會報『變了』——假警報比沒警報更貴。"""
        text = mod._visible_text(BEFORE)
        state: dict = {}
        mod._hash_item("x", "https://e.test/p", text, None, state,
                       segments=sorted(mod._visible_segments(BEFORE)))
        entry = state["https://e.test/p"]
        self.assertEqual(entry["hash"], hashlib.sha256(text.encode("utf-8")).hexdigest())
        self.assertEqual(entry["length"], len(text))

class TestGracefulDegradation(unittest.TestCase):
    def test_legacy_state_without_segments_falls_back_and_says_so(self):
        """靜默地假裝有 diff 才是問題；退化並說明是可接受的。"""
        prev = {"hash": "old", "length": 10}  # 本功能部署前記下的基線
        summary = mod._change_summary("x", prev, mod._visible_text(AFTER),
                                      sorted(mod._visible_segments(AFTER)))
        self.assertIn("下次變動起會列出差異", summary)

    def test_oversized_page_stores_no_segments(self):
        huge = _page(*[f"paragraph number {n} with enough characters" for n in range(mod.MAX_SEGMENTS + 50)])
        state: dict = {}
        mod._hash_item("x", "https://e.test/huge", mod._visible_text(huge), None,
                       state, segments=sorted(mod._visible_segments(huge)))
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
                                      sorted(mod._visible_segments(new_t)))
        self.assertIn("Claude Sonnet 5 $3 / MTok", summary)
        self.assertIn("Claude Sonnet 5 $2 / MTok", summary)

    def test_markdown_newlines_are_preserved(self):
        md = "# Title\n\nSonnet 5 costs $2 per million tokens.\n\nOpus 5 costs $5.\n"
        segs = mod._visible_segments(md)
        self.assertIn("Sonnet 5 costs $2 per million tokens.", segs)

class TestBoilerplate(unittest.TestCase):
    def test_segments_on_many_pages_are_dropped(self):
        """導覽／頁尾佔六成儲存量，且變動時報出「新增 1 段：Try Claude」這種噪音。"""
        segs_by_url = {
            "a": {"Contact sales Contact sales", "Page A unique content sentence."},
            "b": {"Contact sales Contact sales", "Page B unique content sentence."},
        }
        boiler = mod._boilerplate(segs_by_url)
        self.assertIn("Contact sales Contact sales", boiler)
        self.assertNotIn("Page A unique content sentence.", boiler)

    def test_fingerprint_comes_from_config_not_from_what_was_fetched(self):
        """取自抓取結果的話，任一頁 timeout 就會讓當輪所有頁的 diff 失效兩輪。"""
        pages = [{'url': 'https://a.test'}, {'url': 'https://b.test'},
                 {'url': 'https://idx.test', 'mode': 'index'}]
        fp = mod._watch_fingerprint(pages)
        self.assertEqual(fp, ['https://a.test', 'https://b.test'])   # index 模式不參與
        # 少抓到一頁不得改變指紋——它是設定的性質，不是今天網路好不好
        self.assertEqual(fp, mod._watch_fingerprint(list(reversed(pages))))
        self.assertNotEqual(fp, mod._watch_fingerprint(pages + [{'url': 'https://c.test'}]))

    def test_resegmented_run_degrades_instead_of_reporting_a_false_removal(self):
        prev = {"hash": "o", "length": 1, "segments": ["Some earlier sentence here."]}
        summary = mod._change_summary("x", prev, "new text",
                                      ["A different sentence entirely."], resegmented=True)
        self.assertIn("下次變動起會列出差異", summary)
        self.assertNotIn("移除", summary)


if __name__ == "__main__":
    unittest.main()
