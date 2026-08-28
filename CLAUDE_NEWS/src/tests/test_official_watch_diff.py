"""Tests for official_docs_watch 的段落級 diff。

舊行為只能說「變了」，摘要因此寫「具體改了什麼需開啟連結比對」——警報響了，
沒人知道響什麼，於是沒人去比對。2026-08-10 Sonnet 5 的 $2/$10 永久化、9/1 漲價
取消就死在這個縫裡。

測試釘四件事：

1. **移除型變動要說得出來**——「9/1 漲價取消」在頁面上就是少了一句話，這是最
   容易靜默的方向。
2. **hash 與 length 的算法不得改動**——改了會讓部署當天所有頁同時報「變了」，
   一次假警報足以把整個來源訓練成可忽略。
3. **舊 state 沒有 segments 時要退化，不得假裝有 diff。**
4. **超大頁不存 segments**，否則 state 檔無上限成長。
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
        before_segs = mod._visible_segments(BEFORE)
        after_segs = mod._visible_segments(AFTER)
        prev = {"hash": "old", "length": len(mod._visible_text(BEFORE)), "segments": before_segs}

        summary = mod._change_summary("方案與定價", prev, mod._visible_text(AFTER), after_segs)

        self.assertIn("新增", summary)
        self.assertIn("will not occur", summary)
        self.assertIn("移除", summary)
        self.assertIn("through August 31", summary)
        # 舊行為的措辭必須消失，否則等於沒修
        self.assertNotIn("需開啟連結比對", summary)

    def test_unchanged_segments_are_not_reported_as_a_diff(self):
        segs = mod._visible_segments(BEFORE)
        prev = {"hash": "old", "length": 1, "segments": segs}
        summary = mod._change_summary("x", prev, mod._visible_text(BEFORE), segs)
        self.assertIn("僅順序或版面調整", summary)


class TestHashUnchanged(unittest.TestCase):
    def test_hash_and_length_still_come_from_visible_text(self):
        """算法一改，部署當天每一頁都會報『變了』——假警報比沒警報更貴。"""
        text = mod._visible_text(BEFORE)
        state: dict = {}
        mod._hash_item("x", "https://e.test/p", text, None, state, raw_body=BEFORE)
        entry = state["https://e.test/p"]
        self.assertEqual(entry["hash"], hashlib.sha256(text.encode("utf-8")).hexdigest())
        self.assertEqual(entry["length"], len(text))

    def test_first_sighting_records_baseline_without_emitting(self):
        state: dict = {}
        item = mod._hash_item("x", "https://e.test/p", mod._visible_text(BEFORE),
                              None, state, raw_body=BEFORE)
        self.assertIsNone(item)
        self.assertIn("segments", state["https://e.test/p"])


class TestGracefulDegradation(unittest.TestCase):
    def test_legacy_state_without_segments_falls_back_and_says_so(self):
        """靜默地假裝有 diff 才是問題；退化並說明是可接受的。"""
        prev = {"hash": "old", "length": 10}  # 本功能部署前記下的基線
        summary = mod._change_summary("x", prev, mod._visible_text(AFTER),
                                      mod._visible_segments(AFTER))
        self.assertIn("下次變動起會列出差異", summary)

    def test_oversized_page_stores_no_segments(self):
        huge = _page(*[f"paragraph number {n} with enough characters" for n in range(mod.MAX_SEGMENTS + 50)])
        state: dict = {}
        mod._hash_item("x", "https://e.test/huge", mod._visible_text(huge), None,
                       state, raw_body=huge)
        self.assertNotIn("segments", state["https://e.test/huge"])


class TestSegmentation(unittest.TestCase):
    def test_block_boundaries_survive_so_there_is_something_to_diff(self):
        """_visible_text 把全頁空白壓成一行；沒有這條，diff 沒有可比對的單位。"""
        self.assertEqual(len(mod._visible_segments(BEFORE)), 2)

    def test_markdown_newlines_are_preserved(self):
        md = "# Title\n\nSonnet 5 costs $2 per million tokens.\n\nOpus 5 costs $5.\n"
        segs = mod._visible_segments(md)
        self.assertIn("Sonnet 5 costs $2 per million tokens.", segs)

    def test_navigation_crumbs_are_dropped(self):
        segs = mod._visible_segments(_page("Home", "OK", "A real sentence of content here."))
        self.assertEqual(segs, ["A real sentence of content here."])


if __name__ == "__main__":
    unittest.main()
