"""日報未收錄條目清單測試。

分層原則：日報是呈現層，只留讀者要讀的重點，篩選是預期行為；wiki 是沉澱層，
要考慮全部。本清單是兩層之間的橋——把日報篩掉的條目交給 ingest 的分類與派工，
讓記者「看過再決定收不收」，而不是根本沒看到。

2026-07-25 踩過的實況：抓料 73 則、日報收 38 則，其餘 35 則（含 61 留言與 47
留言的 GitHub Issue）因為 ingest 的輸入只有日報而完全沒被評估。
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))

from list_digest_omissions import find_omissions, render  # noqa: E402


def gathered(urls, scores=None):
    return {
        "items": [
            {
                "url": u,
                "title": f"t{i}",
                "score": (scores[i] if scores else i),
                "score_unit": "分",
                "source": "Hacker News",
                "summary": f"摘要 {i}",
            }
            for i, u in enumerate(urls)
        ]
    }


def digest_with(urls):
    return "\n".join(f"**[標題]({u})**\n說明\n`來源` · 07/25 00:00 UTC" for u in urls)


class TestFindOmissions(unittest.TestCase):
    def test_no_omissions_when_digest_covers_everything(self):
        urls = [f"https://e.com/{i}" for i in range(10)]
        self.assertEqual(find_omissions(gathered(urls), digest_with(urls)), [])

    def test_finds_the_difference(self):
        urls = [f"https://e.com/{i}" for i in range(73)]
        omissions = find_omissions(gathered(urls), digest_with(urls[:38]))
        self.assertEqual(len(omissions), 35)

    def test_sorted_by_interaction_desc(self):
        """高互動的排前面——記者先看到最可能該收的那幾則。"""
        urls = [f"https://e.com/{i}" for i in range(4)]
        g = gathered(urls, scores=[1, 61, 5, 47])
        omissions = find_omissions(g, digest_with([]))
        self.assertEqual([o["score"] for o in omissions], [61, 47, 5, 1])

    def test_items_without_url_are_ignored(self):
        g = {"items": [{"title": "no url"}, {"url": "https://e.com/1", "title": "x"}]}
        self.assertEqual(len(find_omissions(g, "")), 1)


class TestRender(unittest.TestCase):
    def test_render_states_the_layering_rule(self):
        urls = [f"https://e.com/{i}" for i in range(3)]
        g = gathered(urls)
        out = "\n".join(render(g, find_omissions(g, "")))
        self.assertIn("不收可以，沒看過不行", out)
        self.assertIn("t0", out)

    def test_render_when_nothing_omitted(self):
        urls = [f"https://e.com/{i}" for i in range(3)]
        out = "\n".join(render(gathered(urls), []))
        self.assertIn("全部進了日報", out)


if __name__ == "__main__":
    unittest.main()
