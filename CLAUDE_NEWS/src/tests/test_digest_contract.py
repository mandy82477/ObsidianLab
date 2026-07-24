"""Contract tests: does scripts/build_web.py's parse_digest() actually parse
what real news/*.md digest files contain?

Written 2026-07-24 after diffing web_reader/data/digest/2026-07-18.json
against news/2026-07-18.md by hand and finding three live parsing bugs.
Fixture `fixtures/realistic_digest.md` reproduces the exact header and
source/time-line shapes found in real committed digests (see news/2026-07-14
through news/2026-07-18.md — none of them use "&nbsp;" as a separator, and
none of them wrap "情緒：<emoji>" in backticks the way the older 2026-04-26/27
digests did).

Bug 1 — sourceCount swallows the rest of the header line:
    src_count_re stopped at the next "&" (assuming a "&nbsp;|&nbsp;"
    separator per digest.py's render()), but every real digest header uses a
    plain " | " separator, so the non-greedy group ran to end of line and
    "sourceCount" became "10/10 | **文章數：** 67 | **更新時間：** ...".

Bug 2 — story "time" swallows a trailing "UTC 情緒：<emoji>" suffix:
    SOURCE_RE only recognized a sentiment suffix wrapped in backticks with a
    preceding "·" (`` · `情緒：😊 正面` ``) — the format used by digests up to
    2026-04-27. Every digest from 2026-07 on instead appends a bare
    "情緒：<emoji>" (no backticks, no extra "·") straight after "UTC", which
    the old regex didn't recognize, so the whole tail leaked into "time".

Bug 3 — "sentiment" is always "": direct consequence of bug 2 — the capture
    group for the backtick-wrapped style never matched the bare style, so it
    was always None/empty.
"""
import json
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module, FIXTURES_DIR

build_web = load_script_module("build_web")


class TestSourceCountDelimiter(unittest.TestCase):
    """Bug 1: real digest headers separate fields with a plain '|', not
    '&nbsp;|&nbsp;'."""

    def setUp(self):
        self.fixture = FIXTURES_DIR / "realistic_digest.md"

    def test_source_count_is_just_the_ratio(self):
        d = build_web.parse_digest(self.fixture)
        self.assertEqual(d["sourceCount"], "10/10")

    def test_article_count_still_parses(self):
        # header_re/gen_re were never broken by this bug — locked in here so
        # a future delimiter change that breaks them is also caught.
        d = build_web.parse_digest(self.fixture)
        self.assertEqual(d["articleCount"], 3)
        self.assertEqual(d["generatedAt"], "2026-07-18 13:05 UTC")


class TestSentimentSuffixParsing(unittest.TestCase):
    """Bugs 2 & 3: current-format discussion entries put a bare
    '情緒：<emoji>' (no backticks, no extra '·') at the end of the
    source/time line."""

    def setUp(self):
        self.fixture = FIXTURES_DIR / "realistic_digest.md"

    def test_time_excludes_sentiment_suffix(self):
        d = build_web.parse_digest(self.fixture)
        story = next(s for s in d["discussions"] if s["title"] == "討論標題一")
        self.assertEqual(story["time"], "07/17 14:26")

    def test_sentiment_extracted_for_first_entry(self):
        d = build_web.parse_digest(self.fixture)
        story = next(s for s in d["discussions"] if s["title"] == "討論標題一")
        self.assertEqual(story["sentiment"], "🤔")

    def test_sentiment_extracted_for_second_entry(self):
        d = build_web.parse_digest(self.fixture)
        story = next(s for s in d["discussions"] if s["title"] == "討論標題二")
        self.assertEqual(story["time"], "07/18 02:02")
        self.assertEqual(story["sentiment"], "😤")

    def test_non_discussion_entry_unaffected(self):
        # 🔧 技術更新 entries never carry a sentiment suffix — time should
        # simply drop the trailing " UTC" as it always did.
        d = build_web.parse_digest(self.fixture)
        story = d["techUpdates"][0]
        self.assertEqual(story["time"], "07/18 01:20")
        self.assertEqual(story["sentiment"], "")


class TestOldBacktickSentimentStillSupported(unittest.TestCase):
    """Backward compatibility: digests up to 2026-04-27 wrapped the sentiment
    in backticks with an extra '·' (`` · `情緒：😊 正面` ``). news/*.md is
    read-only, so the parser must still handle this style, not just the
    current bare one."""

    def test_old_style_line_parsed_via_direct_regex(self):
        line = "`Hacker News` · 04/25 14:56 UTC · `情緒：😊 正面`"
        m = build_web.SOURCE_RE.match(line)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "Hacker News")
        self.assertEqual(m.group(2), "04/25 14:56")
        sentiment = m.group(3) or m.group(4)
        self.assertEqual(sentiment, "😊 正面")


class TestFocusRefFormatCompat(unittest.TestCase):
    """2026-07-24 呈現優化 a）：digest.py::reformat_presentation() 把 📌 今日聚焦
    行內的 `（ref: URL）` 換成 `[N]` 編號引用，URL 移到檔尾「今日聚焦參考連結」
    清單。news/*.md 是唯讀資料，兩種格式都可能存在，parse_digest() 必須兩者
    都認得，且產出的 tag / text / ref_urls / focusTags 完全等價。

    fixtures/focus_refs_new_format.md 不是手刻的——是拿
    fixtures/focus_refs_old_format.md 實際跑一次
    news_aggregator.digest.reformat_presentation() 產生的，保證兩份 fixture
    描述的是同一份日報的新舊兩種呈現，不是兩份湊出來、可能悄悄跑偏的樣本。
    """

    def test_new_format_focus_matches_old_format(self):
        old = build_web.parse_digest(FIXTURES_DIR / "focus_refs_old_format.md")
        new = build_web.parse_digest(FIXTURES_DIR / "focus_refs_new_format.md")

        self.assertEqual(len(new["focus"]), len(old["focus"]))
        for fo, fn in zip(old["focus"], new["focus"]):
            self.assertEqual(fn["tag"], fo["tag"])
            self.assertEqual(fn["text"], fo["text"])
            self.assertEqual(sorted(fn["ref_urls"]), sorted(fo["ref_urls"]))

    def test_new_format_focus_text_has_no_bracket_markers(self):
        new = build_web.parse_digest(FIXTURES_DIR / "focus_refs_new_format.md")
        for f in new["focus"]:
            self.assertNotIn("[1]", f["text"])
            self.assertNotRegex(f["text"], r"\[\d+\]")

    def test_new_format_story_focus_tags_match_old_format(self):
        old = build_web.parse_digest(FIXTURES_DIR / "focus_refs_old_format.md")
        new = build_web.parse_digest(FIXTURES_DIR / "focus_refs_new_format.md")
        for sec in ("topStories", "techUpdates", "mediaReports", "discussions", "billing"):
            old_tags = [s["focusTags"] for s in old[sec]]
            new_tags = [s["focusTags"] for s in new[sec]]
            self.assertEqual(new_tags, old_tags, f"section={sec}")

    def test_new_format_selection_threshold_not_misparsed_as_focus_item(self):
        # 選材門檻 block now lives at the tail of the file, outside any
        # SECTION_EMOJI heading — it must not leak into result["focus"] (it
        # never did even in the old in-section placement, since its
        # sub-bullets use "**[tag]**：" with no space, which FOCUS_RE
        # requires; this locks in the same guarantee post-relocation).
        new = build_web.parse_digest(FIXTURES_DIR / "focus_refs_new_format.md")
        self.assertEqual(len(new["focus"]), 2)
        tags = [f["tag"] for f in new["focus"]]
        self.assertNotIn("[新工具]", tags)
        self.assertNotIn("[風險警示]", tags)  # real focus item uses [持續追蹤], not this
        all_text = "".join(f["text"] for f in new["focus"])
        self.assertNotIn("門檻說明", all_text)


class TestSearchIndexIncludesBody(unittest.TestCase):
    """search-index.json used to only index 今日聚焦 text + story titles —
    a keyword that only appears in a story's body (never in its title) was
    unfindable via the web reader's search box. build()'s digest indexing
    loop must now also fold in each story's body text."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmpdir.cleanup)
        self.root = Path(self.tmpdir.name)
        (self.root / "wiki" / "entities").mkdir(parents=True)
        (self.root / "wiki" / "topics").mkdir(parents=True)
        (self.root / "news").mkdir(parents=True)
        (self.root / "web_reader" / "data").mkdir(parents=True)

        digest_md = (
            "# Claude Code & Anthropic 每日新聞摘要\n\n"
            "**日期：** 2026-02-02 | **來源：** 1/10 | **文章數：** 1 | "
            "**更新時間：** 2026-02-02 00:00 UTC\n\n---\n\n"
            "### 🔧 技術更新\n\n"
            "**[標題完全不含關鍵字](https://example.com/body-only)**\n"
            "這段內文獨家提到了indexbodyonlyword這個關鍵字，標題裡完全沒有。\n"
            "`GitHub` · 02/02 00:00 UTC\n\n"
            "### 📡 來源狀態\n\n"
            "| 來源 | 狀態 | 條數 |\n|------|------|------|\n| GitHub | ✅ | 1 |\n"
        )
        (self.root / "news" / "2026-02-02.md").write_text(digest_md, encoding="utf-8")

    def _patch_paths(self):
        patched = {
            "ROOT": self.root,
            "WIKI_DIR": self.root / "wiki",
            "WIKI_ENTITIES": self.root / "wiki" / "entities",
            "WIKI_TOPICS": self.root / "wiki" / "topics",
            "WIKI_RADAR": self.root / "wiki" / "feature-radar.md",
            "NEWS_DIR": self.root / "news",
            "OUT_JS": self.root / "web_reader" / "data" / "data.js",
            "OUT_WIKI_DIR": self.root / "web_reader" / "data" / "wiki",
            "OUT_DIGEST_DIR": self.root / "web_reader" / "data" / "digest",
            "OUT_SEARCH_INDEX": self.root / "web_reader" / "data" / "search-index.json",
        }
        originals = {k: getattr(build_web, k) for k in patched}
        for k, v in patched.items():
            setattr(build_web, k, v)
        self.addCleanup(lambda: [setattr(build_web, k, v) for k, v in originals.items()])

    def test_body_only_keyword_present_in_index_text(self):
        self._patch_paths()
        build_web.build()
        index = json.loads(build_web.OUT_SEARCH_INDEX.read_text(encoding="utf-8"))
        entry = next(item for item in index if item["id"] == "2026-02-02")
        self.assertIn("indexbodyonlyword", entry["text"])


if __name__ == "__main__":
    unittest.main()
