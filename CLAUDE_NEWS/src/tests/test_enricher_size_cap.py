"""Tests for the article-size cap in news_aggregator.enricher.

為什麼這條上限值得單獨測：底下的 `trafilatura.extract()` 走 lxml（C 擴充），
把病態大小的 HTML 丟給它會吃光記憶體或在 C 層 abort——而 **C 層的 abort
Python 的 try/except 攔不住**，整個 process 帶著 SIGABRT（exit 134）死掉，
`main.py` 逐來源的 try/except 完全無效。

2026-08-15 GitHub Actions 的抓料就是這樣整個失敗（exit 134），當日無原料、
雲端 routine 新鮮度防線正確中止、當天沒有日報。上限是唯一能在 Python 層
擋下這種死法的地方，所以它壞掉不能靠測試以外的方式察覺。
"""
import unittest

from news_aggregator.enricher import _MAX_ARTICLE_BYTES, _read_capped


class _Resp:
    """最小的 requests.Response 替身，只提供 _read_capped 用到的介面。"""

    url = "https://example.com/article"

    def __init__(self, chunks, encoding="utf-8"):
        self._chunks = chunks
        self.encoding = encoding

    def iter_content(self, chunk_size=0):
        return iter(self._chunks)


class TestReadCapped(unittest.TestCase):
    def test_normal_page_passes_through(self):
        html = b"<html><body><p>hello</p></body></html>"
        self.assertEqual(_read_capped(_Resp([html])), html.decode())

    def test_chunks_are_reassembled_in_order(self):
        self.assertEqual(_read_capped(_Resp([b"<htm", b"l>ab", b"c</html>"])),
                         "<html>abc</html>")

    def test_oversized_page_is_abandoned(self):
        """超過上限即放棄——回空字串，呼叫端保留原摘要，不把它交給 lxml。"""
        over = [b"x" * (1024 * 1024)] * ((_MAX_ARTICLE_BYTES // (1024 * 1024)) + 3)
        self.assertEqual(_read_capped(_Resp(over)), "")

    def test_page_just_under_cap_still_read(self):
        under = [b"y" * (_MAX_ARTICLE_BYTES - 10)]
        self.assertEqual(len(_read_capped(_Resp(under))), _MAX_ARTICLE_BYTES - 10)

    def test_empty_chunks_ignored(self):
        self.assertEqual(_read_capped(_Resp([b"", b"<p>x</p>", b""])), "<p>x</p>")

    def test_undeclared_encoding_falls_back_without_raising(self):
        """header 沒宣告編碼時不得拋錯——壞位元組以替代字元帶過即可。"""
        self.assertEqual(_read_capped(_Resp([b"<p>caf\xe9</p>"], encoding=None)),
                         "<p>caf�</p>")

    def test_cap_is_sane(self):
        """6 個 worker 並行，上限 × 6 必須遠低於 runner 記憶體。"""
        self.assertLessEqual(_MAX_ARTICLE_BYTES * 6, 64 * 1024 * 1024)
        self.assertGreaterEqual(_MAX_ARTICLE_BYTES, 1024 * 1024)


if __name__ == "__main__":
    unittest.main()
