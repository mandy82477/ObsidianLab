"""gathered 原料副本歸檔與保留測試。

副本存在的理由：`gathered_items.json` 不按日分檔、每次抓料直接覆寫，某天日報沒
產出時，那天已經抓到手的原料會在隔天被蓋掉，補跑只能回頭重抓，但來源視窗早已
滾過去 → 該日永久漏失。歸檔讓補跑可以 replay 當天真實原料。
"""
import json
import sys
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))

from archive_gathered import archive, prune  # noqa: E402


class TestArchive(unittest.TestCase):
    def test_archives_under_the_date_inside_the_file(self):
        """檔名取檔案內的 date 欄位，不取系統當下日期——backfill 產生的原料才會
        歸檔到它真正對應的那一天。"""
        with TemporaryDirectory() as d:
            src = Path(d) / "gathered_items.json"
            src.write_text(json.dumps({"date": "2026-07-20", "items": [1, 2]}), encoding="utf-8")
            out = Path(d) / "archive"
            target = archive(src, out)
            self.assertEqual(target.name, "2026-07-20.json")
            self.assertEqual(json.loads(target.read_text(encoding="utf-8"))["items"], [1, 2])

    def test_missing_source_is_not_an_error(self):
        with TemporaryDirectory() as d:
            self.assertIsNone(archive(Path(d) / "nope.json", Path(d) / "archive"))

    def test_malformed_source_is_not_an_error(self):
        """抓料失敗留下半截檔案時，歸檔只能跳過，不能讓整條 pipeline 掛掉。"""
        with TemporaryDirectory() as d:
            src = Path(d) / "gathered_items.json"
            src.write_text("{ this is not json", encoding="utf-8")
            self.assertIsNone(archive(src, Path(d) / "archive"))

    def test_source_without_date_field_is_skipped(self):
        with TemporaryDirectory() as d:
            src = Path(d) / "gathered_items.json"
            src.write_text(json.dumps({"items": []}), encoding="utf-8")
            self.assertIsNone(archive(src, Path(d) / "archive"))


class TestPrune(unittest.TestCase):
    def test_removes_only_expired_and_ignores_non_date_names(self):
        with TemporaryDirectory() as d:
            p = Path(d)
            for name in ("2026-07-01.json", "2026-07-11.json", "2026-07-24.json", "readme.json"):
                (p / name).write_text("{}", encoding="utf-8")
            removed = prune(p, today=date(2026, 7, 25))
            self.assertEqual(removed, ["2026-07-01.json"])  # 07-11 剛好在 14 天內
            self.assertTrue((p / "readme.json").exists(), "檔名不是日期就不該被刪")

    def test_missing_dir_is_not_an_error(self):
        with TemporaryDirectory() as d:
            self.assertEqual(prune(Path(d) / "nope", today=date(2026, 7, 25)), [])


if __name__ == "__main__":
    unittest.main()
