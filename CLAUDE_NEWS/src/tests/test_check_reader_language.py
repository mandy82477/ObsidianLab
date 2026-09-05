"""Tests for scripts/check_reader_language.py — 讀者語言閘。

規則端：`.claude/rules/wiki-reporter-shared.md`「派工過程不上頁」與
`.claude/rules/wiki-ingest-format.md`「無維運術語洩漏」列。

每個測試用假檔（`TemporaryDirectory`）餵 `scan(files=..., allow=...)`——
`scan()` 明確接受這兩個參數以支援測試，不需 monkeypatch 模組全域。
"""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("check_reader_language")


class _Case(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, name: str, text: str) -> Path:
        p = self.dir / name
        p.write_text(text, encoding="utf-8")
        return p

    def scan(self, name: str, text: str, allow=None):
        return mod.scan([self.write(name, text)], allow=allow or [])


class TestHits(_Case):
    def test_plain_internal_term_is_caught(self):
        hits = self.scan("x.md", "# X\n\n本節每次 ingest 更新，由主編彙整。\n")
        terms = {h["term"] for h in hits}
        self.assertIn("ingest", terms)
        self.assertIn("主編", terms)

    def test_hit_carries_reason_and_alternative(self):
        """每筆命中都要能告訴修的人「為什麼不行」與「改成什麼」——否則檢查器只是罵人。"""
        hits = self.scan("x.md", "本節受 12 列上限汰出。\n")
        self.assertEqual(len(hits), 1)
        self.assertTrue(hits[0]["why"])
        self.assertTrue(hits[0]["alt"])

    def test_clean_page_has_no_hits(self):
        hits = self.scan("x.md", "# 乾淨頁\n\n本頁每日更新，最新排名見另一頁。\n")
        self.assertEqual(hits, [])


class TestScopeAndSkips(_Case):
    def test_table_scoped_term_only_fires_in_table(self):
        prose = self.scan("a.md", "他買了一台二手筆電。\n")
        self.assertEqual([h for h in prose if h["term"] == "二手"], [])
        table = self.scan("b.md", "| 來源 | 二手 |\n")
        self.assertEqual(len(table), 1)
        self.assertEqual(table[0]["term"], "二手")

    def test_percent_comment_is_skipped(self):
        """`%% … %%` 是維運備忘的家（網站建置會剝除），不算外洩。"""
        inline = self.scan("a.md", "本頁每週更新。%% 由主編於 lint 時派工覆寫 %%\n")
        self.assertEqual(inline, [])
        block = self.scan("b.md", "正文一句。\n%%\n這段是給下一輪記者看的：暫不覆寫，理由是…\n%%\n正文二句。\n")
        self.assertEqual(block, [])

    def test_html_comment_and_code_fence_are_skipped(self):
        html = self.scan("a.md", "<!-- 主編備忘：這裡的派工順序不要動 -->\n正文。\n")
        self.assertEqual(html, [])
        fence = self.scan("b.md", "```\npython scripts/foo.py --ingest\n```\n")
        self.assertEqual(fence, [])

    def test_frontmatter_is_skipped_and_line_numbers_stay_true(self):
        text = "---\nkind: topic\nnote: ingest\n---\n# 標題\n\n本頁由主編彙整。\n"
        hits = self.scan("a.md", text)
        self.assertEqual([h["term"] for h in hits], ["主編"])
        # frontmatter 佔 4 行 → 命中在原檔第 7 行，行號不可因剝除而位移
        self.assertEqual(hits[0]["line"], 7)


class TestAllowlist(_Case):
    def test_allowlist_entry_suppresses_hit(self):
        allow = [{"page": "a", "term": "門檻", "line_contains": "低門檻", "reason": "測試"}]
        text = "這是低門檻的做法。\n"
        self.assertEqual(len(self.scan("a.md", text)), 1)
        self.assertEqual(self.scan("a.md", text, allow=allow), [])

    def test_allowlist_line_contains_must_match(self):
        allow = [{"page": "a", "term": "門檻", "line_contains": "別的句子", "reason": "測試"}]
        self.assertEqual(len(self.scan("a.md", "這是低門檻的做法。\n", allow=allow)), 1)


class TestBaseline(_Case):
    def test_baseline_hit_is_legacy_new_hit_is_fail(self):
        """存量基線只擋新增：基線內的算 WARN，基線外的算 FAIL（同 pending-legacy-baseline 先例）。"""
        old_line = "舊句：本節受 12 列上限汰出。"
        hits_old = self.scan("a.md", old_line + "\n")
        baseline = {"a": [hits_old[0]["fp"]]}
        new, legacy = mod.split_hits(hits_old, baseline)
        self.assertEqual((len(new), len(legacy)), (0, 1))

        # 同頁新加一句同樣違規的話 → 指紋不同 → FAIL
        hits_both = self.scan("a.md", old_line + "\n新句：已移交 [[entities/x]]。\n")
        new, legacy = mod.split_hits(hits_both, baseline)
        self.assertEqual(len(legacy), 1)
        self.assertEqual([h["term"] for h in new], ["移交"])

    def test_fingerprint_ignores_whitespace_but_not_content(self):
        a = mod.fingerprint("汰出", "  受上限汰出  ")
        b = mod.fingerprint("汰出", "受上限汰出")
        self.assertEqual(a, b)
        self.assertNotEqual(a, mod.fingerprint("汰出", "受別的上限汰出"))


class TestRepoState(unittest.TestCase):
    def test_repo_baseline_file_is_wellformed(self):
        data = json.loads(mod.BASELINE.read_text(encoding="utf-8"))
        self.assertIn("pages", data)
        self.assertTrue(all(isinstance(v, list) for v in data["pages"].values()))

    def test_allowlist_never_wildcards_everything(self):
        """page 與 term 同時 `*` 等於關掉檢查——留白名單機制可以，開後門不行。"""
        for a in mod.load_allowlist():
            self.assertFalse(a.get("page") == "*" and a.get("term") == "*", a)
            self.assertTrue(a.get("reason"), f"白名單必須附理由：{a}")

    def test_terms_all_carry_why_and_alt(self):
        for t in mod.TERMS:
            self.assertTrue(t.get("why"), t["key"])
            self.assertTrue(t.get("alt"), t["key"])


if __name__ == "__main__":
    unittest.main()
