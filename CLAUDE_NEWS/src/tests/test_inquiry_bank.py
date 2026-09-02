"""inquiry_bank.py（質疑題庫）的回歸測試。

題庫是 `/wiki-lint` 7b 的抽問來源，它的三個承諾各對應一組斷言：
  1. 七種模式一題不少、欄位齊全（自檢會擋，這裡驗自檢本身沒被弄鈍）
  2. 抽選是程式擲骰且同週決定性——「隨機是自由心證」正是這支腳本要治的病
  3. 探針引用的檔案路徑真實存在——探針指向不存在的檔，等於題目作廢還顯示綠燈
"""
import re
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import inquiry_bank  # noqa: E402


class TestBankIntegrity(unittest.TestCase):
    def test_至少七題且欄位齊全(self):
        inquiry_bank.check_integrity()  # 不拋即過
        self.assertGreaterEqual(len(inquiry_bank.BANK), 7)

    def test_模式名各就各位(self):
        names = {q["name"] for q in inquiry_bank.BANK}
        for expected in ("溯源", "缺席偵測", "沉默質疑", "讀者查找", "可讀性",
                         "結構健檢", "宣稱對帳", "資產重用審計"):
            self.assertIn(expected, names)

    def test_題數不足會被自檢擋下(self):
        with self.assertRaises(inquiry_bank.BankIntegrityError):
            inquiry_bank.check_integrity(inquiry_bank.BANK[:3])

    def test_單步探針會被自檢擋下(self):
        bad = [dict(q) for q in inquiry_bank.BANK]
        bad[0] = dict(bad[0], probe=["只有一步"])
        with self.assertRaises(inquiry_bank.BankIntegrityError):
            inquiry_bank.check_integrity(bad)


class TestDrawDiscipline(unittest.TestCase):
    def test_同_seed_抽題決定性(self):
        s1, p1 = inquiry_bank.draw(n=2, seed="2026-W36")
        s2, p2 = inquiry_bank.draw(n=2, seed="2026-W36")
        self.assertEqual([q["id"] for q in p1], [q["id"] for q in p2])

    def test_預設_seed_綁_ISO_週(self):
        self.assertEqual(inquiry_bank.default_seed(date(2026, 9, 2)), "2026-W36")
        # 同一週的另一天 → 同 seed（主編不能靠隔天重跑換題）
        self.assertEqual(inquiry_bank.default_seed(date(2026, 9, 6)), "2026-W36")
        # 下一週 → 換 seed
        self.assertEqual(inquiry_bank.default_seed(date(2026, 9, 7)), "2026-W37")

    def test_抽出題目不重複(self):
        _, picked = inquiry_bank.draw(n=7, seed="x")
        ids = [q["id"] for q in picked]
        self.assertEqual(len(ids), len(set(ids)))


class TestProbesPointAtRealFiles(unittest.TestCase):
    """探針文字裡引用的 repo 路徑必須存在——防題庫在重構後靜默腐爛。"""

    def test_引用路徑存在(self):
        pattern = re.compile(
            r"(?:scripts|data|docs|src|wiki|news|weekly|\.claude)[/\\][\w./\\-]+"
        )
        for q in inquiry_bank.BANK:
            for step in q["probe"] + [q["question"], q["origin"]]:
                for ref in pattern.findall(step):
                    ref = ref.rstrip(".,；、）)")
                    # 帶萬用字元或範例佔位者跳過
                    if "*" in ref or "YYYY" in ref:
                        continue
                    self.assertTrue(
                        (REPO_ROOT / ref).exists(),
                        f"{q['id']} 探針引用不存在的路徑：{ref}",
                    )


class TestProbesRunInCloud(unittest.TestCase):
    """探針必須在雲端 lint 的執行環境（fresh clone）跑得動。

    2026-09-02 首次審計抓到：兩題探針用 `HEAD@{7 days ago}`——那是 reflog 語法，
    本機有效、fresh clone 的 reflog 是空的，等於這兩題在正式執行環境必壞。
    正確寫法是 commit-history 基底的 `git rev-list -1 --before=...`。
    """

    def test_探針不得依賴_reflog(self):
        for q in inquiry_bank.BANK:
            for step in q["probe"]:
                self.assertNotIn(
                    "HEAD@{", step,
                    f"{q['id']} 探針用了 reflog 語法，雲端 fresh clone 會壞",
                )


class TestCli(unittest.TestCase):
    def _run(self, *args):
        p = subprocess.run(
            [sys.executable, str(SCRIPTS / "inquiry_bank.py"), *args],
            capture_output=True, cwd=str(REPO_ROOT),
        )
        return p.returncode, p.stdout.decode("utf-8", "replace")

    def test_draw_印出_seed_與紀律警語(self):
        rc, out = self._run("draw", "--seed", "2026-W36")
        self.assertEqual(rc, 0)
        self.assertIn("seed=2026-W36", out)
        self.assertIn("不可重擲換題", out)

    def test_all_列出全部題目(self):
        rc, out = self._run("all")
        self.assertEqual(rc, 0)
        for qid in ("Q1", "Q7"):
            self.assertIn(qid, out)


if __name__ == "__main__":
    unittest.main()
