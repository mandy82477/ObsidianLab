"""Tests for news_aggregator.sources.official_docs_watch.OfficialDocsWatch.

The point of this source is to notice that a static official page changed, so
the tests pin down the two ways it can betray that job: staying silent when a
watched page really changed, and crying wolf on churn that carries no meaning
(first sight of a URL, cosmetic markup, sub-threshold noise).
"""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch

from news_aggregator.sources import official_docs_watch as mod
from news_aggregator.sources.official_docs_watch import OfficialDocsWatch, _visible_text

URL = "https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan"


def _config(pages):
    return json.dumps({"pages": pages})


def _page(**kw):
    base = {"name": "Fable 5 on your plan", "url": URL, "status": "active"}
    base.update(kw)
    return base


class _Ctx:
    """Point CONFIG_PATH/STATE_PATH at a temp dir so tests never touch the repo."""

    def __init__(self, pages):
        self._tmp = TemporaryDirectory()
        d = Path(self._tmp.name)
        self.config = d / "official_watch.json"
        self.state = d / "official_watch_state.json"
        self.config.write_text(_config(pages), encoding="utf-8")
        self._patches = [
            patch.object(mod, "CONFIG_PATH", self.config),
            patch.object(mod, "STATE_PATH", self.state),
        ]

    def __enter__(self):
        for p in self._patches:
            p.start()
        return self

    def __exit__(self, *exc):
        for p in self._patches:
            p.stop()
        self._tmp.cleanup()
        return False


def _resp(html):
    r = MagicMock()
    r.text = html
    r.raise_for_status = MagicMock()
    return r


class TestBaseline(unittest.TestCase):
    def test_first_sight_records_silently(self):
        """新增一個監看頁不得立刻噴一則『變更』——否則每次加頁都是假警報。"""
        with _Ctx([_page()]) as ctx:
            with patch.object(mod.requests, "get", return_value=_resp("<p>hello world</p>")):
                items = OfficialDocsWatch().fetch()
            self.assertEqual(items, [])
            state = json.loads(ctx.state.read_text(encoding="utf-8"))
            self.assertIn(URL, state)

    def test_unchanged_page_emits_nothing(self):
        with _Ctx([_page()]) as ctx:
            html = "<p>" + "x" * 500 + "</p>"
            with patch.object(mod.requests, "get", return_value=_resp(html)):
                OfficialDocsWatch().fetch()
                items = OfficialDocsWatch().fetch()
            self.assertEqual(items, [])


class TestChangeDetection(unittest.TestCase):
    def test_real_change_emits_one_item(self):
        """這是本 source 存在的唯一理由：官方靜態頁改了，要有人講。"""
        with _Ctx([_page()]):
            with patch.object(mod.requests, "get", return_value=_resp("<p>" + "a" * 500 + "</p>")):
                OfficialDocsWatch().fetch()
            new_html = "<p>" + "a" * 500 + "b" * 200 + "</p>"
            with patch.object(mod.requests, "get", return_value=_resp(new_html)):
                items = OfficialDocsWatch().fetch()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].url, URL)
        self.assertEqual(items[0].category, "official")
        self.assertIn("Fable 5 on your plan", items[0].title)

    def test_subthreshold_churn_is_ignored(self):
        """輪替的 token / 計數器不算內容變更，否則讀者會學會忽略這個來源。"""
        with _Ctx([_page()]):
            with patch.object(mod.requests, "get", return_value=_resp("<p>" + "a" * 500 + "</p>")):
                OfficialDocsWatch().fetch()
            with patch.object(mod.requests, "get", return_value=_resp("<p>" + "a" * 500 + "b" * 5 + "</p>")):
                items = OfficialDocsWatch().fetch()
        self.assertEqual(items, [])

    def test_markup_only_change_is_ignored(self):
        """CSS class / asset hash 變動不是內容變動。"""
        with _Ctx([_page()]):
            body = "The earlier promotion ended on July 19, 2026. " * 20
            with patch.object(mod.requests, "get", return_value=_resp(f"<div class='a1'>{body}</div>")):
                OfficialDocsWatch().fetch()
            with patch.object(mod.requests, "get", return_value=_resp(f"<section id='x9'><p>{body}</p></section>")):
                items = OfficialDocsWatch().fetch()
        self.assertEqual(items, [])


class TestResilience(unittest.TestCase):
    def test_missing_config_returns_empty(self):
        with _Ctx([]) as ctx:
            ctx.config.unlink()
            self.assertEqual(OfficialDocsWatch().fetch(), [])

    def test_invalid_config_never_raises(self):
        with _Ctx([]) as ctx:
            ctx.config.write_text("{not json", encoding="utf-8")
            self.assertEqual(OfficialDocsWatch().fetch(), [])

    def test_retired_page_is_skipped(self):
        with _Ctx([_page(status="retired")]) as ctx:
            with patch.object(mod.requests, "get", side_effect=AssertionError("must not fetch")):
                self.assertEqual(OfficialDocsWatch().fetch(), [])
            self.assertFalse(ctx.state.exists())

    def test_one_page_failure_does_not_block_others(self):
        other = "https://claude.com/pricing"
        pages = [_page(), _page(name="Pricing", url=other)]
        with _Ctx(pages):
            def _get(url, **kw):
                if url == URL:
                    raise ConnectionError("network down")
                return _resp("<p>" + "z" * 500 + "</p>")

            with patch.object(mod.requests, "get", side_effect=_get):
                OfficialDocsWatch().fetch()

            def _get2(url, **kw):
                if url == URL:
                    raise ConnectionError("still down")
                return _resp("<p>" + "z" * 500 + "y" * 200 + "</p>")

            with patch.object(mod.requests, "get", side_effect=_get2):
                items = OfficialDocsWatch().fetch()

        self.assertEqual([i.url for i in items], [other])

    def test_failed_page_keeps_prior_hash(self):
        """抓失敗不得覆寫既有 hash，否則下次會把『恢復連線』誤判成內容變更。"""
        with _Ctx([_page()]) as ctx:
            with patch.object(mod.requests, "get", return_value=_resp("<p>" + "q" * 500 + "</p>")):
                OfficialDocsWatch().fetch()
            before = json.loads(ctx.state.read_text(encoding="utf-8"))[URL]
            with patch.object(mod.requests, "get", side_effect=ConnectionError("down")):
                self.assertEqual(OfficialDocsWatch().fetch(), [])
            after = json.loads(ctx.state.read_text(encoding="utf-8"))[URL]
        self.assertEqual(before, after)

    def test_corrupt_state_resets_instead_of_raising(self):
        with _Ctx([_page()]) as ctx:
            ctx.state.write_text("{broken", encoding="utf-8")
            with patch.object(mod.requests, "get", return_value=_resp("<p>hello</p>")):
                self.assertEqual(OfficialDocsWatch().fetch(), [])


INDEX_URL = "https://code.claude.com/docs/llms.txt"


def _index_page(**kw):
    base = {
        "name": "Claude Code 文件索引",
        "url": INDEX_URL,
        "status": "active",
        "mode": "index",
    }
    base.update(kw)
    return base


def _index(entries):
    """Render an llms.txt body from (title, path, description) triples."""
    head = "# Claude Code Docs\n\n"
    return head + "\n".join(
        f"- [{t}](https://code.claude.com/docs/en/{p}.md): {d}" for t, p, d in entries
    )


BASE_INDEX = [
    ("Manage sessions", "sessions", "Name, resume, branch."),
    ("Settings", "settings", "Configure Claude Code."),
]


class TestIndexMode(unittest.TestCase):
    """llms.txt 是 280 行的頁面索引：整檔雜湊只會天天說『變了』。這個模式的價值
    在於只回答『多了哪一頁』——新功能上線必然新增一頁。"""

    def test_index_baseline_records_silently(self):
        with _Ctx([_index_page()]) as ctx:
            with patch.object(mod.requests, "get", return_value=_resp(_index(BASE_INDEX))):
                self.assertEqual(OfficialDocsWatch().fetch(), [])
            state = json.loads(ctx.state.read_text(encoding="utf-8"))
            self.assertEqual(len(state[INDEX_URL]["pages"]), 2)

    def test_added_page_is_reported_with_its_title(self):
        """本 source 存在的唯一理由：官方悄悄多了一頁，要在當天講出來。"""
        with _Ctx([_index_page()]):
            with patch.object(mod.requests, "get", return_value=_resp(_index(BASE_INDEX))):
                OfficialDocsWatch().fetch()
            grown = BASE_INDEX + [
                ("Message your other Claude Code sessions", "cross-session-messaging", "Let Claude message sessions."),
            ]
            with patch.object(mod.requests, "get", return_value=_resp(_index(grown))):
                items = OfficialDocsWatch().fetch()
        self.assertEqual(len(items), 1)
        self.assertIn("新增 1 頁", items[0].title)
        self.assertIn("Message your other Claude Code sessions", items[0].summary)
        self.assertIn("cross-session-messaging", items[0].summary)
        self.assertEqual(items[0].category, "official")

    def test_description_reword_stays_silent(self):
        """描述改寫每天都在發生。它若觸發，讀者三天內就學會忽略這個來源。"""
        with _Ctx([_index_page()]):
            with patch.object(mod.requests, "get", return_value=_resp(_index(BASE_INDEX))):
                OfficialDocsWatch().fetch()
            reworded = [
                ("Manage sessions", "sessions", "Completely rewritten description, much longer than before."),
                ("Settings", "settings", "Another totally different blurb here."),
            ]
            with patch.object(mod.requests, "get", return_value=_resp(_index(reworded))):
                items = OfficialDocsWatch().fetch()
        self.assertEqual(items, [])

    def test_removed_page_is_reported(self):
        with _Ctx([_index_page()]):
            with patch.object(mod.requests, "get", return_value=_resp(_index(BASE_INDEX))):
                OfficialDocsWatch().fetch()
            with patch.object(mod.requests, "get", return_value=_resp(_index(BASE_INDEX[:1]))):
                items = OfficialDocsWatch().fetch()
        self.assertEqual(len(items), 1)
        self.assertIn("移除 1 頁", items[0].title)
        self.assertIn("Settings", items[0].summary)

    def test_unparseable_index_keeps_prior_pages(self):
        """抓到錯誤頁時若把 state 寫成空集合，下次正常抓取會謊報『新增 280 頁』。"""
        with _Ctx([_index_page()]) as ctx:
            with patch.object(mod.requests, "get", return_value=_resp(_index(BASE_INDEX))):
                OfficialDocsWatch().fetch()
            before = json.loads(ctx.state.read_text(encoding="utf-8"))[INDEX_URL]

            with patch.object(mod.requests, "get", return_value=_resp("<html>502 Bad Gateway</html>")):
                self.assertEqual(OfficialDocsWatch().fetch(), [])
            after = json.loads(ctx.state.read_text(encoding="utf-8"))[INDEX_URL]
            self.assertEqual(before, after)

            with patch.object(mod.requests, "get", return_value=_resp(_index(BASE_INDEX))):
                self.assertEqual(OfficialDocsWatch().fetch(), [])

    def test_index_mode_does_not_strip_markup(self):
        """index 模式吃純文字：若沿用 HTML 剝除，行結構會被壓成一行而解析失敗。"""
        with _Ctx([_index_page()]):
            captured = {}

            def _get(url, **kw):
                captured["url"] = url
                return _resp(_index(BASE_INDEX))

            with patch.object(mod.requests, "get", side_effect=_get):
                OfficialDocsWatch().fetch()
            self.assertEqual(captured["url"], INDEX_URL)

    def test_hash_mode_is_unaffected_by_index_support(self):
        """既有 hash 模式頁面不得因新增 index 模式而改變行為。"""
        with _Ctx([_page(), _index_page()]):
            def _get(url, **kw):
                if url == INDEX_URL:
                    return _resp(_index(BASE_INDEX))
                return _resp("<p>" + "a" * 500 + "</p>")

            with patch.object(mod.requests, "get", side_effect=_get):
                OfficialDocsWatch().fetch()

            def _get2(url, **kw):
                if url == INDEX_URL:
                    return _resp(_index(BASE_INDEX))
                return _resp("<p>" + "a" * 500 + "b" * 200 + "</p>")

            with patch.object(mod.requests, "get", side_effect=_get2):
                items = OfficialDocsWatch().fetch()
        self.assertEqual([i.url for i in items], [URL])


class TestVisibleText(unittest.TestCase):
    def test_scripts_and_styles_are_stripped(self):
        html = "<style>.a{color:red}</style><script>var t=1</script><p>Real text</p>"
        self.assertEqual(_visible_text(html), "Real text")


if __name__ == "__main__":
    unittest.main()
