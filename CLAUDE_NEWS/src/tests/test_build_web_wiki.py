"""Regression tests for scripts/build_web.py wiki-page parsing.

Covers:
- parse_wiki() extracts all header meta fields from a well-formed page.
- CRLF regression: a header field line ending in "\r" (Windows line ending)
  must produce a clean value with no trailing "\r" — this is the actual bug
  that caused the 領域 (domain) field to go missing/dirty on some pages and
  falsely trip the "缺少領域欄位" WARN.
- Missing 領域 field triggers a WARN printed to stdout.
- check_wikilinks(): a dangling [[target]] wikilink is reported; legitimate
  links ([[entities/xxx]], [[xxx|alias]], and a wikilink inside a markdown
  table cell escaped as "\\|") must NOT be falsely reported.
"""
import io
import contextlib
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module, FIXTURES_DIR

build_web = load_script_module("build_web")


class TestParseWikiHeaderFields(unittest.TestCase):
    def test_all_meta_fields_present(self):
        f = FIXTURES_DIR / "sample_entity.md"
        meta = build_web.parse_wiki(f, "entity")
        self.assertEqual(meta["name"], "測試實體")
        self.assertEqual(meta["entityType"], "feature")
        self.assertEqual(meta["status"], "active")
        self.assertEqual(meta["domain"], "🛠️ 工具/功能")
        self.assertEqual(meta["firstSeen"], "2026-01-01")
        self.assertEqual(meta["lastUpdated"], "2026-01-02")
        self.assertEqual(meta["lastNewsUpdate"], "2026-01-02")
        self.assertTrue(meta["summary"].startswith("這是測試實體的現況說明"))


class TestCRLFRegression(unittest.TestCase):
    """Regression for the incident where CRLF-terminated header lines left a
    trailing '\\r' in parsed meta values (e.g. domain became '🛠️ 工具/功能\\r'),
    which then failed the VALID_DOMAINS membership check and produced a false
    "領域值不在標準六選一內" WARN."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmpdir.cleanup)

    def _write_crlf(self, content: str) -> Path:
        p = Path(self.tmpdir.name) / "crlf_entity.md"
        # Write raw bytes with CRLF line endings, no newline translation.
        with open(p, "wb") as fp:
            fp.write(content.replace("\n", "\r\n").encode("utf-8"))
        return p

    def test_domain_value_has_no_trailing_cr(self):
        content = (
            "# CRLF 測試實體\n"
            "\n"
            "**類型：** feature\n"
            "**狀態：** active\n"
            "**領域：** 🛠️ 工具/功能\n"
            "**首次出現：** 2026-01-01\n"
            "**最後更新：** 2026-01-01\n"
            "**最後新聞更新：** 2026-01-01\n"
            "\n"
            "## 現況\n"
            "\n"
            "測試內容。\n"
        )
        f = self._write_crlf(content)
        meta = build_web.parse_wiki(f, "entity")
        self.assertEqual(meta["domain"], "🛠️ 工具/功能")
        self.assertNotIn("\r", meta["domain"])
        self.assertIn(meta["domain"], build_web.VALID_DOMAINS)

    def test_no_domain_warn_when_crlf_value_is_valid(self):
        content = (
            "# CRLF 測試實體\n"
            "\n"
            "**類型：** feature\n"
            "**狀態：** active\n"
            "**領域：** 🛠️ 工具/功能\n"
            "**首次出現：** 2026-01-01\n"
            "**最後更新：** 2026-01-01\n"
            "**最後新聞更新：** 2026-01-01\n"
            "\n"
            "## 現況\n"
            "\n"
            "測試內容。\n"
        )
        f = self._write_crlf(content)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            build_web.parse_wiki(f, "entity")
        self.assertNotIn("WARN", buf.getvalue())


class TestMissingDomainWarn(unittest.TestCase):
    def test_missing_domain_triggers_warn(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "no_domain.md"
            f.write_text(
                "# 無領域測試實體\n"
                "\n"
                "**類型：** feature\n"
                "**狀態：** active\n"
                "**首次出現：** 2026-01-01\n"
                "**最後更新：** 2026-01-01\n"
                "**最後新聞更新：** 2026-01-01\n"
                "\n"
                "## 現況\n"
                "\n"
                "測試內容。\n",
                encoding="utf-8",
            )
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                build_web.parse_wiki(f, "entity")
            self.assertIn("WARN", buf.getvalue())
            self.assertIn("缺少「領域」欄位", buf.getvalue())


class TestCheckWikilinks(unittest.TestCase):
    """check_wikilinks() prints WARN for dangling links, but must not
    false-positive on legitimate ones (bare page name, entities/ prefixed,
    aliased, or embedded in a markdown table cell with an escaped pipe)."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmpdir.cleanup)
        self.root = Path(self.tmpdir.name)
        (self.root / "wiki" / "entities").mkdir(parents=True)
        (self.root / "wiki" / "topics").mkdir(parents=True)
        (self.root / "news").mkdir(parents=True)
        # a real target page that links can point to
        (self.root / "wiki" / "entities" / "real-entity.md").write_text(
            "# Real Entity\n", encoding="utf-8"
        )

    def _patch_dirs(self):
        """Monkeypatch build_web module-level Path constants to point at our
        temp wiki tree for the duration of a check_wikilinks() call."""
        patched = {
            "ROOT": self.root,
            "WIKI_DIR": self.root / "wiki",
            "WIKI_ENTITIES": self.root / "wiki" / "entities",
            "WIKI_TOPICS": self.root / "wiki" / "topics",
            "NEWS_DIR": self.root / "news",
        }
        originals = {k: getattr(build_web, k) for k in patched}
        for k, v in patched.items():
            setattr(build_web, k, v)
        return originals

    def _restore_dirs(self, originals):
        for k, v in originals.items():
            setattr(build_web, k, v)

    def test_dangling_link_reported(self):
        originals = self._patch_dirs()
        self.addCleanup(self._restore_dirs, originals)
        page = self.root / "wiki" / "topics" / "sample-topic.md"
        page.write_text(
            "# Sample Topic\n\n連結至 [[entities/does-not-exist]]。\n",
            encoding="utf-8",
        )
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            build_web.check_wikilinks([page])
        self.assertIn("斷鏈 wikilink", buf.getvalue())
        self.assertIn("does-not-exist", buf.getvalue())

    def test_legitimate_links_not_reported(self):
        originals = self._patch_dirs()
        self.addCleanup(self._restore_dirs, originals)
        page = self.root / "wiki" / "topics" / "sample-topic2.md"
        page.write_text(
            "# Sample Topic 2\n\n"
            "連結至 [[entities/real-entity]]。\n"
            "也可用別名 [[entities/real-entity|真實實體]]。\n"
            "或裸露頁名 [[real-entity]]。\n"
            "| 欄位 | wikilink |\n"
            "|------|----------|\n"
            "| 範例 | [[entities/real-entity\\|表格連結]] |\n",
            encoding="utf-8",
        )
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            build_web.check_wikilinks([page])
        self.assertNotIn("斷鏈 wikilink", buf.getvalue())


if __name__ == "__main__":
    unittest.main()


class TestBomTolerance(unittest.TestCase):
    """帶 UTF-8 BOM 的 wiki 檔不可讓頁名解析走樣。

    2026-07-26 實際踩到：4 份 wiki 檔帶 BOM（含 feature-radar.md 與 index.md），
    BOM 擋在 `#` 前面使 `lstrip('# ')` 失效，頁名被解析成 `\ufeff# Anthropic 商業健康度`，
    並直接顯示在日報新增的「今日 wiki 動態」清單裡。已把解析端改為 utf-8-sig，
    BOM 從此無害；本測試防止改回 utf-8 而重現。
    """

    def test_page_name_parsed_correctly_with_bom(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "bom-page.md"
            f.write_bytes("\ufeff# 商業健康度\n\n**類型：** topic\n**狀態：** ongoing\n".encode("utf-8"))
            page = build_web.parse_wiki(f, "topic")
            self.assertEqual(page["name"], "商業健康度")
            self.assertFalse(page["name"].startswith("\ufeff"))
            self.assertFalse(page["name"].startswith("#"))
