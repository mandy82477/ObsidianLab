# -*- coding: utf-8 -*-
"""check_hierarchy.py 的改壞驗紅測試（臨時 wiki 夾具，不碰本庫）。

每一題對應 reviewer 2026-09-03 列的一種「靜默壞法」：壞了看起來像正常的東西，這裡要它變紅。
"""
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("ch", ROOT / "scripts" / "check_hierarchy.py")
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)


def page(domain="🌐 社群", parent=None, last_news="2026-09-01", callout="2026-09-01", body=""):
    lines = ["# 頁", "", "**狀態：** ongoing", f"**領域：** {domain}"]
    if parent:
        lines.append(f"**上層：** [[{parent}]]")
    lines += ["**最後更新：** 2026-09-01", f"**最後新聞更新：** {last_news}", ""]
    if callout:
        lines += [f"> **最新動態**（{callout}）", "> 一句。", ""]
    lines += ["## 摘要", body or "內容。", ""]
    return "\n".join(lines)


class HierarchyFixture(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        (self.d / "topics").mkdir()
        (self.d / "entities").mkdir()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def w(self, slug, text):
        p = self.d / f"{slug}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def index(self, rows):
        self.w("index", "| 頁面 | 領域 | 狀態 | 摘要 |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")

    def test_valid_tree_passes(self):
        self.w("topics/hub", page(callout="2026-09-02"))
        self.w("topics/kid", page(parent="topics/hub", last_news="2026-09-02"))
        self.index(["| [[topics/hub]] | 🌐 社群 | ongoing | 摘要 ↳ 子故事：[[topics/kid]] |"])
        fails, n = ch.check(self.d)
        self.assertEqual(fails, [])
        self.assertEqual(n, 1)

    def test_no_hierarchy_is_fine(self):
        self.w("topics/a", page())
        self.index(["| [[topics/a]] | 🌐 社群 | ongoing | 摘要 |"])
        fails, n = ch.check(self.d)
        self.assertEqual((fails, n), ([], 0))

    def test_nested_dir_is_red(self):
        self.w("topics/hub", page())
        self.w("topics/hub/kid", page(parent="topics/hub"))  # 子目錄——半數機制看不見
        fails, _ = ch.check(self.d)
        self.assertTrue(any("非扁平" in f for f in fails), fails)

    def test_cycle_and_missing_parent_are_red(self):
        self.w("topics/a", page(parent="topics/b"))
        self.w("topics/b", page(parent="topics/a"))
        self.w("topics/c", page(parent="topics/nope"))
        fails, _ = ch.check(self.d)
        self.assertTrue(any("成環" in f for f in fails), fails)
        self.assertTrue(any("上層不存在" in f for f in fails), fails)

    def test_domain_inheritance_is_red(self):
        self.w("topics/hub", page(domain="🌐 社群", callout="2026-09-02"))
        self.w("topics/kid", page(domain="🛠️ 工具/功能", parent="topics/hub"))
        self.index(["| [[topics/hub]] | 🌐 社群 | ongoing | 摘要 ↳ 子故事：[[topics/kid]] |"])
        fails, _ = ch.check(self.d)
        self.assertTrue(any("領域未繼承" in f for f in fails), fails)

    def test_hub_behind_child_is_red(self):
        """母頁 callout 停在 09-01，子頁 09-03 吃了新聞 → 母頁靜默過期，必須紅。"""
        self.w("topics/hub", page(callout="2026-09-01"))
        self.w("topics/kid", page(parent="topics/hub", last_news="2026-09-03"))
        self.index(["| [[topics/hub]] | 🌐 社群 | ongoing | 摘要 ↳ 子故事：[[topics/kid]] |"])
        fails, _ = ch.check(self.d)
        self.assertTrue(any("hub 落後" in f for f in fails), fails)

    def test_index_projection_missing_is_red(self):
        self.w("topics/hub", page(callout="2026-09-02"))
        self.w("topics/kid", page(parent="topics/hub"))
        self.index(["| [[topics/hub]] | 🌐 社群 | ongoing | 摘要 |"])  # 沒有 ↳ 投影
        fails, _ = ch.check(self.d)
        self.assertTrue(any("index 投影缺子頁" in f for f in fails), fails)

    def test_archive_must_have_parent(self):
        self.w("topics/x-archive", page())
        fails, _ = ch.check(self.d)
        self.assertTrue(any("archive 未掛父" in f for f in fails), fails)

    def test_redirect_shell_skips_freshness(self):
        self.w("topics/hub", page(callout="2026-09-01"))
        self.w("topics/old", page(parent="topics/hub", last_news="2026-09-05", body="已併回 [[topics/hub]]"))
        self.index(["| [[topics/hub]] | 🌐 社群 | ongoing | 摘要 ↳ 子故事：[[topics/old]] |"])
        fails, _ = ch.check(self.d)
        self.assertFalse(any("hub 落後" in f for f in fails), fails)


if __name__ == "__main__":
    unittest.main()
