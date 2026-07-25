"""原料健康檢查門檻測試。

這道閘擋的是「抓到但殘缺」——原本的新鮮度防線只看日期與筆數 > 0，10 個來源掛
9 個仍會生出一份看起來正常、實則系統性偏食的日報，並被記者沉澱進 wiki。
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))

from check_gather_health import FAIL_ITEMS, FAIL_SOURCES, WARN_SOURCES, evaluate  # noqa: E402


def make(ok_count: int, failed_count: int, items: int) -> dict:
    status = {f"ok{i}": {"ok": True, "count": 3} for i in range(ok_count)}
    status.update({f"bad{i}": {"ok": False, "count": 0} for i in range(failed_count)})
    return {"source_status": status, "items": [{"url": f"u{i}"} for i in range(items)]}


class TestEvaluate(unittest.TestCase):
    def test_healthy_day_passes(self):
        code, msgs = evaluate(make(10, 0, 63))
        self.assertEqual(code, 0)
        self.assertTrue(any("原料健康" in m for m in msgs))

    def test_quiet_day_with_all_sources_ok_still_passes(self):
        """淡日不是異常：來源全正常、條數偏低但仍在門檻之上要放行，
        否則會為了『補滿』而放寬收錄門檻。"""
        code, _ = evaluate(make(10, 0, FAIL_ITEMS + 1))
        self.assertEqual(code, 0)

    def test_few_failed_sources_warns_but_passes(self):
        code, msgs = evaluate(make(10 - WARN_SOURCES, WARN_SOURCES, 40))
        self.assertEqual(code, 0)
        self.assertTrue(any("須標警示" in m for m in msgs))

    def test_many_failed_sources_aborts(self):
        code, msgs = evaluate(make(10 - FAIL_SOURCES, FAIL_SOURCES, 40))
        self.assertEqual(code, 2)
        self.assertTrue(any("系統性偏差" in m for m in msgs))

    def test_too_few_items_aborts_even_with_healthy_sources(self):
        code, msgs = evaluate(make(10, 0, FAIL_ITEMS - 1))
        self.assertEqual(code, 2)
        self.assertTrue(any("管線異常" in m for m in msgs))

    def test_empty_gather_aborts(self):
        code, _ = evaluate({"source_status": {}, "items": []})
        self.assertEqual(code, 2)

    def test_missing_keys_do_not_raise(self):
        code, _ = evaluate({})
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
