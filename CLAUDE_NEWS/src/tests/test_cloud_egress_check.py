"""`scripts/cloud_egress_check.py` 的摘要行格式與退出碼。

這支腳本的存在理由是「讓 lint 各步不必寫死『雲端一律跳過』」，所以它的輸出是
**機械契約**——`.claude/commands/wiki-lint.md` 各步 grep `EGRESS: <組> OK` 那一行
來決定要不要執行。契約壞掉時的失效模式是靜默的：grep 不到就一律走「跳過」分支，
那幾步會恢復成永遠不跑，而沒有任何人會收到錯誤。因此本檔驗兩件事：

1. 三種狀態（全通／部分通／全不通）各自印對摘要行、回對退出碼
2. 空組（market）一律回 OK——那是「本步不需要 egress」的表達，不是「沒查」
"""
import importlib.util
import io
import unittest
import urllib.error
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent.parent / "scripts" / "cloud_egress_check.py"

_spec = importlib.util.spec_from_file_location("cloud_egress_check", SCRIPT)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


class _FakeResp:
    def __init__(self, status):
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _urlopen_all_ok(req, timeout=None):
    return _FakeResp(200)


def _urlopen_all_blocked(req, timeout=None):
    raise urllib.error.URLError(ConnectionRefusedError("EGRESS_BLOCKED"))


def _urlopen_first_ok(req, timeout=None):
    """只有清單第一個網域通——用來造出 PARTIAL。"""
    if req.full_url == f"https://{mod.GROUPS['official'][0]}/":
        return _FakeResp(200)
    raise urllib.error.URLError(ConnectionRefusedError("EGRESS_BLOCKED"))


class TestProbeStatus(unittest.TestCase):
    def setUp(self):
        self._real = mod.urllib.request.urlopen
        self.addCleanup(lambda: setattr(mod.urllib.request, "urlopen", self._real))

    def _run_group(self, fake, group="official"):
        mod.urllib.request.urlopen = fake
        buf = io.StringIO()
        status = mod.check_group(group, timeout=1, out=buf)
        return status, buf.getvalue()

    def test_all_reachable_prints_ok(self):
        status, out = self._run_group(_urlopen_all_ok)
        self.assertEqual(status, "OK")
        n = len(mod.GROUPS["official"])
        self.assertIn(f"EGRESS: official OK ({n}/{n} 個網域)", out)

    def test_none_reachable_prints_blocked(self):
        status, out = self._run_group(_urlopen_all_blocked)
        self.assertEqual(status, "BLOCKED")
        n = len(mod.GROUPS["official"])
        self.assertIn(f"EGRESS: official BLOCKED (0/{n} 個網域)", out)

    def test_some_reachable_prints_partial(self):
        """PARTIAL 必須跟 OK 長得不一樣——半套查證比不查更危險。"""
        status, out = self._run_group(_urlopen_first_ok)
        self.assertEqual(status, "PARTIAL")
        n = len(mod.GROUPS["official"])
        self.assertIn(f"EGRESS: official PARTIAL (1/{n} 個網域)", out)
        self.assertNotIn("EGRESS: official OK", out)

    def test_empty_group_is_ok(self):
        """market 組刻意為空（5h 走 WebSearch，不經沙盒 egress）。"""
        status, out = self._run_group(_urlopen_all_blocked, group="market")
        self.assertEqual(status, "OK")
        self.assertIn("EGRESS: market OK (0/0 個網域)", out)

    def test_http_error_counts_as_reachable(self):
        """量的是 egress 不是頁面存在：403/404 代表封包出得去，算通。"""
        def _403(req, timeout=None):
            raise urllib.error.HTTPError(req.full_url, 403, "Forbidden", {}, None)

        status, out = self._run_group(_403)
        self.assertEqual(status, "OK")
        self.assertIn("HTTP 403", out)


class TestExitCodes(unittest.TestCase):
    def test_exit_code_mapping(self):
        self.assertEqual(mod.exit_code_for(["OK", "OK"]), 0)
        self.assertEqual(mod.exit_code_for(["OK", "BLOCKED"]), 1)
        self.assertEqual(mod.exit_code_for(["PARTIAL"]), 1)
        self.assertEqual(mod.exit_code_for(["BLOCKED", "BLOCKED"]), 2)

    def test_main_returns_two_when_all_blocked(self):
        real = mod.urllib.request.urlopen
        mod.urllib.request.urlopen = _urlopen_all_blocked
        self.addCleanup(lambda: setattr(mod.urllib.request, "urlopen", real))
        buf = io.StringIO()
        import contextlib

        with contextlib.redirect_stdout(buf):
            rc = mod.main(["--group", "official,github", "--timeout", "1"])
        self.assertEqual(rc, 2)
        self.assertIn("EGRESS: official BLOCKED", buf.getvalue())
        self.assertIn("EGRESS: github BLOCKED", buf.getvalue())

    def test_unknown_group_rejected(self):
        self.assertEqual(mod.main(["--group", "nosuchgroup"]), 2)


class TestGroupRegistry(unittest.TestCase):
    def test_groups_cover_every_lint_step_that_needs_egress(self):
        """五個受影響的 lint 步驟（5b/5c/5e/5h/5m）都要有組可問。"""
        for g in ("official", "github", "leaderboard", "market"):
            self.assertIn(g, mod.GROUPS)

    def test_leaderboard_group_is_not_empty(self):
        """5b 真的需要 egress——這組空掉等於 5b 永遠判「可做」然後抓不到榜。"""
        self.assertTrue(mod.GROUPS["leaderboard"])


if __name__ == "__main__":
    unittest.main()
