"""news_mentions.py 的回歸測試。

測資刻意用 2026-08-28 真實踩到的兩種錯，而不是人造字串——那天同一次查證
裡「漏抓」與「假命中」各犯一次，這支腳本存在的唯一理由就是讓它們不再發生。
若哪天有人「優化」了比對邏輯而讓其中任一條失守，這裡會紅。
"""
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPT = REPO_ROOT / "scripts" / "news_mentions.py"
NEWS_DIR = REPO_ROOT / "news"


def run(*args):
    p = subprocess.run(
        [sys.executable, str(SCRIPT), "--today", "2026-08-29", *args],
        capture_output=True, cwd=str(REPO_ROOT),
    )
    return p.returncode, p.stdout.decode("utf-8", "replace")


class TestProbeQualityGate(unittest.TestCase):
    def test_單一別名被拒(self):
        """單詞偵測力不足——這是懸置探針系統早就有的結論，不是新規定。"""
        rc, out = run("--since", "4w", "proactive")
        self.assertEqual(rc, 2)
        self.assertIn("至少要給 2 個別名", out)

    def test_過寬詞拒絕執行而非警告(self):
        """警告會被略過，所以這裡是拒絕。"""
        rc, out = run("--since", "4w", "Claude", "Anthropic")
        self.assertEqual(rc, 2)
        self.assertIn("過寬詞", out)

    def test_過寬詞可在明確放行下使用(self):
        rc, _ = run("--since", "4w", "--any", "--allow-weak", "Claude", "Anthropic")
        self.assertIn(rc, (0, 1))


@unittest.skipUnless(NEWS_DIR.is_dir(), "需要 news/ 目錄")
class TestRealRegressions(unittest.TestCase):
    def test_漏抓_Dreaming_有後續必須查得到(self):
        """2026-08-28：只用英文全名查，判定「113 天無後續」並差點把還活著的
        功能降到 🔥、在讀者面前標「細節未公布」。實際上 2026-07-17 日報寫著
        SDK 新增 dreaming API 支援。"""
        rc, out = run("--since", "90d", "--any", "Dreaming", "記憶整合")
        self.assertEqual(rc, 0, "Dreaming 在窗口內有後續，不得回報零命中")
        self.assertIn("2026-07-17", out)
        self.assertIn("0.117.0", out, "必須附上命中原文行，不能只給次數")

    def test_假命中_必須附原文行讓人辨識(self):
        """2026-08-28：`proactive` 命中的三次全是「Proactive financial news」
        媒體名。只數次數會把死的判活；附原文才擋得住。"""
        rc, out = run("--since", "60d", "--any", "--allow-weak", "proactive", "主動式工作流")
        self.assertEqual(rc, 0)
        self.assertIn("Proactive financial news", out,
                      "命中原文行必須輸出，否則無從辨識假命中")

    def test_零命中時提醒別名是否足夠(self):
        """判『無後續』是有後果的動作，零命中時必須提醒先檢討別名。"""
        rc, out = run("--since", "4w", "zzz-not-a-real-feature", "這不是真的功能名稱")
        self.assertEqual(rc, 1)
        self.assertIn("別名", out)


class TestSinceParsing(unittest.TestCase):
    def test_週與日與絕對日期皆可(self):
        for spec in ("4w", "30d", "2026-05-01"):
            rc, _ = run("--since", spec, "--any", "Dreaming", "記憶整合")
            self.assertIn(rc, (0, 1), f"--since {spec} 應可解析")

    def test_格式錯誤明確報錯(self):
        rc, out = run("--since", "四週", "--any", "Dreaming", "記憶整合")
        self.assertEqual(rc, 2)
        self.assertIn("--since 格式錯誤", out)


if __name__ == "__main__":
    unittest.main()
