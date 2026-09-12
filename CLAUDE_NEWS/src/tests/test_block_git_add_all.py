"""`.claude/hooks/block_git_add_all.py` 的命中/不命中判定。

規則寫在文件裡只在 agent 剛好記得時生效；hook 是「必須每次都發生」的那一半。
本檔驗兩件事：該擋的擋得到（否則規則等於沒上鎖），不該擋的不擋（誤擋會讓人
關掉 hook，等於也沒上鎖）。
"""
import importlib.util
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent.parent / ".claude" / "hooks" / "block_git_add_all.py"

_spec = importlib.util.spec_from_file_location("block_git_add_all", HOOK)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


class TestBlockGitAddAll(unittest.TestCase):
    def test_blocks_all_forms(self):
        """三種全加寫法都要命中——漏掉任一種，規則就有一條沒上鎖的側門。"""
        for cmd in (
            "git add -A",
            'git -C "C:/repo" add --all',
            "cd repo && git add . && git commit -m x",
        ):
            with self.subTest(cmd=cmd):
                self.assertTrue(mod.is_add_all(cmd))

    def test_allows_named_paths(self):
        """指名路徑是本專案唯一合法的 add 形式，不得被誤擋。"""
        for cmd in (
            "git add wiki/ .claude/reporter-rules/",
            "git add ./scripts/check_rules.py",
            "git add -p wiki/index.md",
        ):
            with self.subTest(cmd=cmd):
                self.assertFalse(mod.is_add_all(cmd))

    def test_main_exit_codes(self):
        """PreToolUse 契約：擋下回 2、放行回 0；非 Bash 工具一律放行。"""
        import io
        import json
        import sys

        def run(payload):
            old = sys.stdin
            sys.stdin = io.StringIO(json.dumps(payload))
            try:
                return mod.main()
            finally:
                sys.stdin = old

        self.assertEqual(run({"tool_name": "Bash", "tool_input": {"command": "git add -A"}}), 2)
        self.assertEqual(run({"tool_name": "Bash", "tool_input": {"command": "git add wiki/"}}), 0)
        self.assertEqual(run({"tool_name": "Read", "tool_input": {"command": "git add -A"}}), 0)


if __name__ == "__main__":
    unittest.main()
