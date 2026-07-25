"""日報收錄完整性檢查測試。

日報的定位是留原始資料給人看，過濾是 wiki 記者的職責。2026-07-25 出現回歸：
抓料 73 則、日報只收 38 則（48% 被篩掉，含 61 留言與 47 留言的 GitHub Issue），
推測是「選材門檻」區塊搬到檔尾後被理解成整份日報的收錄門檻，而非只用於挑選
「📌 今日聚焦」的 3–5 條導讀。措辭可能再被讀歪，因此改用機械檢查把關。
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))

from check_digest_coverage import evaluate  # noqa: E402


def gathered(urls):
    return {"items": [{"url": u, "title": f"t{i}", "score": i} for i, u in enumerate(urls)]}


def digest_with(urls):
    return "\n".join(f"**[標題]({u})**\n說明\n`來源` · 07/25 00:00 UTC" for u in urls)


class TestCoverage(unittest.TestCase):
    def test_full_coverage_passes(self):
        urls = [f"https://e.com/{i}" for i in range(20)]
        code, msgs, missing = evaluate(gathered(urls), digest_with(urls))
        self.assertEqual(code, 0)
        self.assertEqual(missing, [])
        self.assertTrue(any("收錄完整" in m for m in msgs))

    def test_small_gap_warns_but_passes(self):
        """漏一兩則可能是重複或明顯無關，不該擋下整條 pipeline。"""
        urls = [f"https://e.com/{i}" for i in range(40)]
        code, msgs, missing = evaluate(gathered(urls), digest_with(urls[:39]))
        self.assertEqual(code, 0)
        self.assertEqual(len(missing), 1)

    def test_large_gap_fails(self):
        """2026-07-25 的實際形狀：73 收 38。"""
        urls = [f"https://e.com/{i}" for i in range(73)]
        code, msgs, missing = evaluate(gathered(urls), digest_with(urls[:38]))
        self.assertEqual(code, 2)
        self.assertEqual(len(missing), 35)
        self.assertTrue(any("覆蓋率低於" in m for m in msgs))

    def test_failure_lists_missing_items_for_repair(self):
        urls = [f"https://e.com/{i}" for i in range(20)]
        code, msgs, _ = evaluate(gathered(urls), digest_with(urls[:5]))
        self.assertEqual(code, 2)
        self.assertTrue(any("t19" in m for m in msgs), "應列出遺漏條目供補齊")

    def test_empty_gathered_is_an_error_not_a_pass(self):
        code, _, _ = evaluate({"items": []}, "")
        self.assertEqual(code, 3)


if __name__ == "__main__":
    unittest.main()
