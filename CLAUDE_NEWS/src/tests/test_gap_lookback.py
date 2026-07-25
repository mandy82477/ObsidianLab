"""失敗補撈（gap recovery）行為與可達性測試。

背景：雲端 routine 漏跑一天時，隔天的 --gather-only 應該把 LOOKBACK_HOURS 從
預設值拉長到 50h，去撈回昨天那個洞裡的新聞。2026-07-25 發現這段程式碼被寫在
`if args.confirm_digest:` 分支內、且在該分支的 `return` 之後——是不可達的死碼，
自寫下以來從未執行過，等於「雲端漏一天 → 那天的新聞永久漏掉」完全沒有保護。

因此本檔測兩件事：
  1. check_gap_lookback 的判斷語意（缺檔 / 空日報 / 正常）
  2. 補撈區塊在 main() 中的**結構位置**——用 AST 斷言它不是巢狀在別的 if 裡、
     也不在任何 return 之後。純行為測試抓不到「死碼」這種缺陷，因為死碼不會
     產生錯誤結果，它只是不會執行。
"""
import ast
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from news_aggregator.main import check_gap_lookback

MAIN_PY = Path(__file__).resolve().parent.parent / "news_aggregator" / "main.py"


class TestCheckGapLookback(unittest.TestCase):
    def test_missing_yesterday_returns_reason(self):
        with TemporaryDirectory() as d:
            reason = check_gap_lookback(date(2026, 7, 25), news_dir=Path(d))
            self.assertIsNotNone(reason)
            self.assertIn("2026-07-24", reason)

    def test_empty_yesterday_returns_reason(self):
        with TemporaryDirectory() as d:
            p = Path(d) / "2026-07-24.md"
            p.write_text("# 日報\n\n今日無新增資訊\n", encoding="utf-8")
            reason = check_gap_lookback(date(2026, 7, 25), news_dir=Path(d))
            self.assertIsNotNone(reason)
            self.assertIn("為空", reason)

    def test_healthy_yesterday_returns_none(self):
        with TemporaryDirectory() as d:
            p = Path(d) / "2026-07-24.md"
            p.write_text("# 日報\n\n**[某則新聞](https://example.com)**\n", encoding="utf-8")
            self.assertIsNone(check_gap_lookback(date(2026, 7, 25), news_dir=Path(d)))


class TestGapRecoveryReachable(unittest.TestCase):
    """回歸防護：補撈區塊必須留在 main() 的頂層、且在任何 return 之前。"""

    def _main_body(self):
        tree = ast.parse(MAIN_PY.read_text(encoding="utf-8"))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name == "main":
                return node.body
        self.fail("main.py 中找不到 main() 函式")

    def _find_gap_stmt(self, body):
        """在給定的敘述串裡找呼叫 check_gap_lookback 的那個 if 區塊，回傳 index。"""
        for i, stmt in enumerate(body):
            if any(
                isinstance(n, ast.Name) and n.id == "check_gap_lookback"
                for n in ast.walk(stmt)
            ):
                return i, stmt
        return None, None

    def test_gap_recovery_is_at_main_top_level(self):
        body = self._main_body()
        idx, stmt = self._find_gap_stmt(body)
        self.assertIsNotNone(
            idx,
            "check_gap_lookback 不在 main() 的頂層敘述中——很可能又被巢狀進某個 "
            "if 分支（2026-07-25 的死碼缺陷就是這個形狀）",
        )
        self.assertIsInstance(stmt, ast.If, "補撈區塊應為 `if args.gather_only:`")

    def test_no_return_before_gap_recovery_at_same_level(self):
        body = self._main_body()
        idx, _ = self._find_gap_stmt(body)
        self.assertIsNotNone(idx)
        for stmt in body[:idx]:
            self.assertNotIsInstance(
                stmt,
                ast.Return,
                "main() 頂層在補撈區塊之前出現了 return，補撈將不可達",
            )


if __name__ == "__main__":
    unittest.main()
