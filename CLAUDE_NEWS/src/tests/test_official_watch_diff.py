"""Tests for official_docs_watch 的段落級 diff。

**行為測試一律走 `_hash_item` 或 `fetch()`，不直接呼叫摘要函式。** 這是 2026-08-29
六輪 review 換來的紀律：前幾輪的缺陷每一個都在單元層綠燈、卻漏在層與層之間——
「濾完沒差異卻照樣發條目」漏在 `_boilerplate` 與摘要之間；「價格改動端到端 0 則」
漏在摘要與長度閘之間（當時的測試直接呼叫摘要函式，繞過了那道閘）。測到決策層
才守得住。

釘住的事：

1. **價格數字改動必須報得出來**——它是長度守恆的（$2 → $3 差 0 字元），而本
   清單存在的目的就是追蹤這類數字事實。
2. **輪替雜訊仍要擋**——長度閘沒被廢掉，只是不再排在段落 diff 前面。
3. **跨頁共用區的變動不得歸因到個別頁**——6 個 support 頁共享一份會變的文章
   索引，官方發一篇新文章不該讓 6 頁各發一則。
4. **價格必須和它的主詞留在同一段**——切到 td 或 div 會讓 `$2 / MTok` 變成低於
   門檻的碎片被丟掉。
5. **hash／length 的算法不得改動**——改了會讓部署當天所有頁同時報假警報。
6. **不得丟棄昨天的基線**，也不得謊稱「尚無可比對的前一版段落」。
"""
import hashlib
import json
import logging
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from news_aggregator.sources import official_docs_watch as mod

URL = "https://p.test/x"


def _page(*paragraphs):
    return "<html><body>" + "".join(f"<p>{p}</p>" for p in paragraphs) + "</body></html>"


BEFORE = _page(
    "Claude Sonnet 5 costs two dollars per million input tokens.",
    "Introductory pricing runs through August 31, 2026.",
)
AFTER = _page(
    "Claude Sonnet 5 costs two dollars per million input tokens.",
    "The scheduled increase to three dollars will not occur.",
)


def _price_table(price):
    return ("<html><body><table>"
            f"<tr><td>Claude Sonnet 5</td><td>{price} / MTok</td><td>$10 / MTok</td></tr>"
            "<tr><td>Claude Opus 5</td><td>$5 / MTok</td><td>$25 / MTok</td></tr>"
            "</table></body></html>")


class _Watch:
    """把 config／state 導到暫存目錄並打樁 `_fetch_body`。全程不連網。

    連網實跑這個模組會**消費掉真實事件**：state 是「已消費」的帳本不是快取，
    新 hash 一旦寫進去，那則官方變動就再也不會進日報（2026-08-29 第 4 輪
    reviewer 發現我用連網驗證吃掉了一則 desktop.md 的真實變動）。
    """

    def __init__(self, urls):
        self._tmp = TemporaryDirectory()
        d = Path(self._tmp.name)
        self.cfg = d / "c.json"
        self.cfg.write_text(json.dumps({"pages": [
            {"name": f"p{i}", "url": u, "status": "active"} for i, u in enumerate(urls)
        ]}), encoding="utf-8")
        self.state = d / "s.json"

    def run(self, body_of):
        with patch.object(mod, "CONFIG_PATH", self.cfg), \
             patch.object(mod, "STATE_PATH", self.state), \
             patch.object(mod, "_fetch_body", body_of):
            return mod.OfficialDocsWatch().fetch()

    def __enter__(self):
        logging.disable(logging.CRITICAL)
        return self

    def __exit__(self, *exc):
        logging.disable(logging.NOTSET)
        self._tmp.cleanup()


class TestNumericChangesSurvive(unittest.TestCase):
    def test_a_length_neutral_price_change_is_reported_with_the_model_name(self):
        """$2 → $3 差 0 字元。長度閘若排在段落 diff 前面，這則永遠報不出來，
        而且新值會被吸收進基線——本模組唯一存在理由的那類變動就此消失。"""
        with _Watch([URL]) as w:
            w.run(lambda u: _price_table("$2"))
            items = w.run(lambda u: _price_table("$3"))
        self.assertEqual(len(items), 1)
        self.assertIn("Claude Sonnet 5 $3 / MTok", items[0].summary)
        self.assertIn("Claude Sonnet 5 $2 / MTok", items[0].summary)

    def test_a_removal_is_reported_not_just_an_addition(self):
        """「9/1 漲價取消」在頁面上就是少了一句話，是最容易靜默的方向。"""
        with _Watch([URL]) as w:
            w.run(lambda u: BEFORE)
            items = w.run(lambda u: AFTER)
        self.assertEqual(len(items), 1)
        self.assertIn("移除", items[0].summary)
        self.assertIn("August 31", items[0].summary)


class TestNoiseIsStillSuppressed(unittest.TestCase):
    @staticmethod
    def _churn(extra):
        return _page("a" * 500 + extra)

    def test_a_small_non_numeric_edit_is_still_ignored(self):
        """長度閘沒被廢掉，只是不再排在段落 diff 前面。實測 state 的 git 歷史：
        22 個 commit 中有 28 次字數差 <40 的變動被它擋掉。"""
        with _Watch([URL]) as w:
            w.run(lambda u: self._churn(""))
            self.assertEqual(w.run(lambda u: self._churn("bbbbb")), [])

    def test_a_large_non_numeric_edit_still_gets_through(self):
        with _Watch([URL]) as w:
            w.run(lambda u: self._churn(""))
            self.assertEqual(len(w.run(lambda u: self._churn("b" * 60))), 1)

    def test_a_rolling_relative_timestamp_is_not_a_change(self):
        """support.claude.com 的 Intercom 小工具每週自己滾一次「Updated over N
        weeks ago」。它是長度守恆的**數字**變動——與價格同型，任何以數字為鍵的
        規則都分不開兩者。所以從源頭剝掉：hash 不為它而變，問題不存在。

        沒有這條測試，第 6 輪的數字繞道會讓 3–4 個真實監看頁每週各發一則，而且
        時間戳與文章首段同段，摘要讀起來像整段說明被改寫（第 7 輪 reviewer 用
        真 state 的段落實測過）。"""
        def page(stamp):
            return _page(
                f"Updated over {stamp} ago Copy for LLM This article explains credits.",
                "Claude Sonnet 5 costs two dollars per million input tokens.")
        with _Watch([URL]) as w:
            w.run(lambda u: page("2 weeks"))
            self.assertEqual(w.run(lambda u: page("3 weeks")), [])
            self.assertEqual(w.run(lambda u: page("4 weeks")), [])

    def test_a_price_change_still_surfaces_through_a_rolling_timestamp(self):
        """對照組：剝掉時間戳不得連帶把同頁的真變動一起吃掉。"""
        def page(stamp, price):
            return _page(
                f"Updated over {stamp} ago Copy for LLM This article explains credits.",
                f"Claude Sonnet 5 costs {price} / MTok input.")
        with _Watch([URL]) as w:
            w.run(lambda u: page("2 weeks", "$2"))
            items = w.run(lambda u: page("3 weeks", "$3"))
        self.assertEqual(len(items), 1)
        self.assertIn("$3 / MTok", items[0].summary)

    def test_an_unchanged_page_emits_nothing(self):
        with _Watch([URL]) as w:
            w.run(lambda u: BEFORE)
            self.assertEqual(w.run(lambda u: BEFORE), [])


class TestSharedChrome(unittest.TestCase):
    """6 個 support 頁共享一份會變動的 Help Center 文章索引（實測 350 段）。"""

    IDX = [f"Help Center article number {n} title text" for n in range(30)]
    URLS = [f"https://support.test/p{i}" for i in range(6)]

    @staticmethod
    def _own(u):
        return f"Own content of page {u[-2:]} here and then some."

    def _body(self, own_of, idx):
        return lambda u: _page(*(idx + [own_of(u)]))

    def test_a_shared_index_change_emits_nothing_at_all(self):
        """官方發一篇新文章，6 頁都「變了」但沒有一頁自己改。修法前這裡是 6 則
        空條目，而下游 enricher 會把空條目改寫成看起來像新聞的摘要。"""
        with _Watch(self.URLS) as w:
            w.run(self._body(self._own, self.IDX))
            grown = self.IDX + ["Help Center article number 30 title text"]
            self.assertEqual(w.run(self._body(self._own, grown)), [])

    def test_a_real_change_on_one_page_still_names_the_segment(self):
        new = "Sonnet 5 pricing rises to three dollars per million input tokens in September."
        with _Watch(self.URLS) as w:
            w.run(self._body(self._own, self.IDX))
            items = w.run(self._body(
                lambda u: new if u.endswith("p2") else self._own(u), self.IDX))
        self.assertEqual(len(items), 1)
        self.assertIn("p2", items[0].title)
        self.assertIn("Sonnet 5 pricing rises", items[0].summary)


class TestSegmentation(unittest.TestCase):
    def test_prices_stay_with_their_subject(self):
        """切到 td 會讓 `$2 / MTok` 變成 9 字元碎片、低於門檻被整個丟掉；行銷頁
        把每個價格各包一個 div，切 div 同樣碎掉。"""
        segs = mod._visible_segments(_price_table("$2"))
        self.assertIn("Claude Sonnet 5 $2 / MTok $10 / MTok", segs)
        self.assertTrue(all("$" in s for s in segs))
        marketing = "<div><div>Claude Sonnet 5</div><div>$2 / MTok</div></div>"
        self.assertEqual(mod._visible_segments(marketing), {"Claude Sonnet 5 $2 / MTok"})

    def test_markdown_newlines_are_preserved(self):
        md = "# Title\n\nSonnet 5 costs two dollars per million tokens.\n\nOpus 5 costs five.\n"
        self.assertIn("Sonnet 5 costs two dollars per million tokens.",
                      mod._visible_segments(md))


class TestStateDiscipline(unittest.TestCase):
    def test_hash_and_length_still_come_from_visible_text(self):
        """算法一改，部署當天每一頁都會報「變了」——假警報比沒警報更貴。"""
        text = mod._visible_text(BEFORE)
        state: dict = {}
        mod._hash_item("x", URL, text, None, state,
                       segments=sorted(mod._visible_segments(BEFORE)), boilerplate=set())
        self.assertEqual(state[URL]["hash"], hashlib.sha256(text.encode("utf-8")).hexdigest())
        self.assertEqual(state[URL]["length"], len(text))

    def test_stored_segments_are_unfiltered(self):
        """儲存未過濾全量是整個設計的關鍵：存進去的東西一旦帶著「當時的樣板
        基準」，基準一變昨天今天就不可比——那是前三輪三個缺陷的共同根源。"""
        state: dict = {}
        segs = sorted(mod._visible_segments(BEFORE))
        mod._hash_item("x", URL, mod._visible_text(BEFORE), None, state,
                       segments=segs, boilerplate=set(segs))
        self.assertEqual(state[URL]["segments"], segs)

    def test_yesterdays_baseline_survives_a_page_we_cannot_segment(self):
        """今日切不出段落（骨架頁、版型改版）不代表昨天的基線該丟。丟了之後
        訊息會說「本頁尚無可比對的前一版段落」——而那句話必定是假的。"""
        prev = {"hash": "old", "length": 900, "segments": ["Yesterday's real sentence."]}
        state: dict = {}
        item = mod._hash_item("x", URL, "ok", prev, state, segments=[], boilerplate=set())
        self.assertEqual(state[URL]["segments"], ["Yesterday's real sentence."])
        self.assertIn("未能從頁面解析出可比對的段落", item.summary)

    def test_yesterdays_baseline_survives_an_oversized_page(self):
        prev = {"hash": "old", "length": 10, "segments": ["Yesterday's real sentence."]}
        state: dict = {}
        huge = [f"segment number {n} with enough characters" for n in range(mod.MAX_SEGMENTS + 5)]
        mod._hash_item("x", URL, "x" * 900, prev, state, segments=huge, boilerplate=set())
        self.assertEqual(state[URL]["segments"], ["Yesterday's real sentence."])

    def test_the_message_matches_what_state_actually_holds(self):
        """訊息說「尚無可比對的前一版段落」時，state 裡就真的不能有。第 7 輪
        發現這句話在「段落集合相同」那條路徑上是假的——而當時的測試釘的是訊息
        文字，不是訊息與 state 相不相符，所以釘不住。"""
        # (a) 真的沒有前版段落（本功能部署前的舊 state）
        prev = {"hash": "old", "length": 10}
        state: dict = {}
        item = mod._hash_item("x", URL, "x" * 900, prev, state,
                              segments=["A real sentence here."], boilerplate=set())
        self.assertIn("尚無可比對的前一版段落", item.summary)
        self.assertNotIn("segments", {k: v for k, v in prev.items()})

        # (b) 段落集合與前版相同、hash 卻變了（變動落在段落層看不見處）
        segs = ["Claude Sonnet 5 costs two dollars per million input tokens."]
        prev = {"hash": "old", "length": 10, "segments": segs}
        state = {}
        item = mod._hash_item("x", URL, "x" * 900, prev, state,
                              segments=segs, boilerplate=set())
        self.assertNotIn("尚無可比對的前一版段落", item.summary)
        self.assertEqual(state[URL]["segments"], segs)


if __name__ == "__main__":
    unittest.main()
