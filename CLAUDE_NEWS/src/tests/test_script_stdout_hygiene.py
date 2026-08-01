"""擋住「模組層級抽換 sys.stdout」這個會反覆再犯的坑。

症狀：`scripts/*.py` 為了在 Windows cp950 主控台印得出 ✅／⚠️ 而把 `sys.stdout`
換成 UTF-8 wrapper。寫在模組層級的話，該檔被 import（測試 import、或另一支腳本
import）時就會執行，把**呼叫端**的輸出流一起換掉；原 wrapper 被回收時關閉底層
buffer，於是 `run_tests.py` 整包炸在 `ValueError: I/O operation on closed file`。

已踩過兩次：`cloud_bootstrap.py` 的 docstring 記過一次，2026-08-01 新增
`gate_web_build.py` / `daily_health_check.py` 時又踩一次——註解擋不住第三次，
所以改用測試擋。正確寫法是包成 `_use_utf8_stdout()` 只在 `main()` 裡呼叫。

用 AST 而非字串比對：只認「模組頂層對 sys.stdout 的指派」，包在函式內的不算。
"""
import ast
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"


def assigns_stdout_at_module_level(tree: ast.Module) -> bool:
    for node in tree.body:  # 只看頂層，不遞迴進函式
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        elif isinstance(node, ast.If):
            # `if hasattr(sys.stdout, "buffer"): sys.stdout = ...` 也算模組層級
            for inner in [*node.body, *node.orelse]:
                if isinstance(inner, ast.Assign):
                    targets.extend(inner.targets)
        for t in targets:
            if isinstance(t, ast.Attribute) and t.attr == "stdout" and isinstance(t.value, ast.Name) and t.value.id == "sys":
                return True
    return False


class TestScriptStdoutHygiene(unittest.TestCase):
    def test_no_module_level_stdout_swap(self):
        offenders = []
        for py in sorted(SCRIPTS_DIR.glob("*.py")):
            tree = ast.parse(py.read_text(encoding="utf-8"), filename=str(py))
            if assigns_stdout_at_module_level(tree):
                offenders.append(py.name)
        self.assertEqual(
            offenders, [],
            f"這些腳本在模組層級抽換 sys.stdout：{offenders}。"
            "請包成 _use_utf8_stdout() 並只在 main() 內呼叫——模組層級會在被 import 時"
            "關掉呼叫端的輸出流（run_tests.py 會整包炸）。",
        )

    def test_detector_catches_the_bad_pattern(self):
        """反向驗證：偵測器本身要抓得到壞寫法，否則這條測試是空的。"""
        bad = ast.parse("import sys\nif hasattr(sys.stdout, 'buffer'):\n    sys.stdout = 1\n")
        good = ast.parse("import sys\ndef f():\n    sys.stdout = 1\n")
        self.assertTrue(assigns_stdout_at_module_level(bad))
        self.assertFalse(assigns_stdout_at_module_level(good))


if __name__ == "__main__":
    unittest.main()
