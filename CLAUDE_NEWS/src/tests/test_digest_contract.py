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
import unittest

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


if __name__ == "__main__":
    unittest.main()
