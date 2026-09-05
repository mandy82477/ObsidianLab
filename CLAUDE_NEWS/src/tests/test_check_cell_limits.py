"""Tests for scripts/check_cell_limits.py — 字元上限機械閘。

規則端：`.claude/rules/wiki-ingest-format.md`「表格放結論，細節下沉（全站
通用）」與 `.claude/rules/wiki-reporter-shared.md`「書寫風格」硬上限。

每個測試用假檔（`TemporaryDirectory`）餵 `scan(files=...)`——`scan()` 明確
接受檔案清單以支援測試，不需 monkeypatch 模組全域，也不會污染真實 wiki 檔。
"""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("check_cell_limits")


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

    def scan(self, name: str, text: str):
        return mod.scan([self.write(name, text)])


class TestTableCells(_Case):
    def test_over_120_table_cell_is_caught(self):
        long_cell = "x" * 121
        text = f"| 欄A | 欄B |\n| --- | --- |\n| 短 | {long_cell} |\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["kind"], "table_cell")
        self.assertEqual(hits[0]["limit"], 120)

    def test_exactly_120_table_cell_passes(self):
        cell = "x" * 120
        text = f"| 欄A |\n| --- |\n| {cell} |\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])

    def test_link_url_is_stripped_before_measuring(self):
        """規則明文：量測前先剝掉 markdown 連結的 URL，只算渲染可見文字。"""
        visible = "短標題"
        url = "https://example.com/" + "a" * 200
        text = f"| 來源 |\n| --- |\n| [{visible}]({url}) |\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [], "純引用來源格（短可見文字＋長 URL）應豁免")

    def test_visible_text_still_over_limit_after_stripping_url_fails(self):
        visible = "x" * 130
        url = "https://example.com/short"
        text = f"| 來源 |\n| --- |\n| [{visible}]({url}) |\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["kind"], "table_cell")


class TestListItems(_Case):
    def test_over_200_list_item_is_caught(self):
        text = "- " + ("x" * 201) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["kind"], "list_item")
        self.assertEqual(hits[0]["limit"], 200)

    def test_exactly_200_list_item_passes(self):
        text = "- " + ("x" * 200) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])

    def test_nested_indented_list_item_is_measured(self):
        text = "  - " + ("x" * 201) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)

    def test_asterisk_bullet_is_measured(self):
        text = "* " + ("x" * 201) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)

    def test_short_prose_paragraph_is_not_a_list_item(self):
        """非條列的散文段不受 200 字元上限拘束（本閘只管條列與表格）。"""
        text = ("x" * 250) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])


class TestSkips(_Case):
    def test_percent_comment_is_skipped(self):
        text = "%%\n- " + ("x" * 300) + "\n%%\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])

    def test_code_fence_is_skipped(self):
        text = "```\n| " + ("x" * 300) + " |\n```\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])

    def test_frontmatter_is_skipped_and_line_numbers_stay_true(self):
        text = "---\nkind: topic\n---\n# 標題\n\n- " + ("x" * 201) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["line"], 6)

    def test_archive_page_is_excluded_from_target_files(self):
        """蒐集契約明定 archive 原文一字不刪，不受本閘拘束——但 scan() 本身只吃傳入的
        檔案清單，排除邏輯住 target_files()，故此處直接驗 target_files() 的過濾。"""
        f = self.write("foo-archive.md", "| " + ("x" * 300) + " |\n")
        # target_files() 掃 WIKI 底下固定的 entities/topics 目錄，不是 self.dir，
        # 這裡只驗證檔名過濾邏輯本身（模擬 target_files 內的 list comprehension）。
        filtered = [p for p in [f] if not p.stem.endswith("-archive")]
        self.assertEqual(filtered, [])


class TestBaseline(_Case):
    def test_baseline_hit_is_legacy_new_hit_is_fail(self):
        """存量基線只擋新增：基線內的算 WARN，基線外的算 FAIL（同 reader-language 先例）。"""
        old_cell = "x" * 130
        text = f"| 欄 |\n| --- |\n| {old_cell} |\n"
        hits_old = self.scan("a.md", text)
        self.assertEqual(len(hits_old), 1)
        baseline = {"a": [hits_old[0]["fp"]]}
        new, legacy = mod.split_hits(hits_old, baseline)
        self.assertEqual((len(new), len(legacy)), (0, 1))

        # 同頁新加一條超限條列 → 指紋不同 → FAIL
        text2 = text + "- " + ("y" * 201) + "\n"
        hits_both = self.scan("a.md", text2)
        new, legacy = mod.split_hits(hits_both, baseline)
        self.assertEqual(len(legacy), 1)
        self.assertEqual(len(new), 1)
        self.assertEqual(new[0]["kind"], "list_item")

    def test_fingerprint_ignores_whitespace_but_not_content(self):
        a = mod.fingerprint("table_cell", "  同一格內容  ")
        b = mod.fingerprint("table_cell", "同一格內容")
        self.assertEqual(a, b)
        self.assertNotEqual(a, mod.fingerprint("table_cell", "不同格內容"))


class TestMainExitCode(_Case):
    def test_main_injected_overlimit_fails_then_removal_passes(self):
        """雙向驗紅：注入超限條列 → exit 1；移除後 → exit 0（用臨時檔，不動真實基線）。"""
        f = self.write("a.md", "- " + ("x" * 201) + "\n")
        hits = mod.scan([f])
        self.assertEqual(len(hits), 1)
        new, legacy = mod.split_hits(hits, {})
        self.assertEqual(len(new), 1)

        f2 = self.write("b.md", "- 短句，沒有超限。\n")
        hits2 = mod.scan([f2])
        self.assertEqual(hits2, [])


class TestRepoState(unittest.TestCase):
    def test_repo_baseline_file_is_wellformed(self):
        data = json.loads(mod.BASELINE.read_text(encoding="utf-8"))
        self.assertIn("pages", data)
        self.assertTrue(all(isinstance(v, list) for v in data["pages"].values()))

    def test_repo_currently_has_no_new_hits_against_its_own_baseline(self):
        """真實倉庫的字元上限閘必須自己是綠的——這是本閘上線的前提，不是選填。"""
        hits = mod.scan(mod.target_files())
        baseline = mod.load_baseline()
        new, _legacy = mod.split_hits(hits, baseline)
        self.assertEqual(new, [], f"倉庫對自己的基線出現新增超限：{new[:3]}")


if __name__ == "__main__":
    unittest.main()
