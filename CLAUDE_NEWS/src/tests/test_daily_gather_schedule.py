"""Tests for .github/workflows/daily-gather.yml 與它的下游耦合。

2026-08-27／08-28 連兩天日報開天窗。當時的修法是加一個 00:00 UTC 保險窗——那是在
對抗症狀。根因在下游：目標日期取自**時鐘**，又要求它等於資料的日期，等於強迫
抓料與生成兩個各自排程的工作落在同一個 UTC 日；任一邊延遲，那天的日報永久消失。

根因修在 `docs/cloud-runbooks/daily.md`：目標日期改由 `gathered_archive/`（按資料
日期分檔、已進 git、保留 14 天）決定——哪天沒出過報就補哪天。保險窗因此移除。

所以這裡不再釘「排程要多早」（那是在維護一個不該存在的耦合），改釘根因的所在地。
"""
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent      # CLAUDE_NEWS/
WORKFLOW = REPO_ROOT.parent / ".github" / "workflows" / "daily-gather.yml"
RUNBOOK = REPO_ROOT / "docs" / "cloud-runbooks" / "daily.md"


def _crons():
    # 刻意不用 PyYAML：它沒登記在 src/requirements_news.txt，乾淨環境會 ImportError。
    return re.findall(r'- cron: "([^"]+)"', WORKFLOW.read_text(encoding="utf-8"))


class TestScheduleIsNotLoadBearing(unittest.TestCase):
    def test_the_target_date_comes_from_the_durable_archive(self):
        """根因的所在地。目標日期若改回時鐘、或改讀單槽的 gathered_items.json，
        排程延遲就會再度變成永久資料遺失——而 workflow 這邊看不出任何異狀。

        單槽檔不行的理由是時序：抓料排在 routine 之前，延遲那批會被隔天準時的
        抓料覆寫掉。耐久的那一份是 gathered_archive/。
        """
        runbook = RUNBOOK.read_text(encoding="utf-8")
        self.assertIn("src/gathered_archive/", runbook)
        self.assertIn("還沒出過報的原料日期", runbook)

    def test_the_freshness_guard_still_checks_the_date(self):
        """replay 路徑（cp gathered_archive/<date>.json）唯一擋得住「複製錯一天」
        的地方。曾被誤刪一次，理由建立在已被推翻的單槽設計上。"""
        steps = (REPO_ROOT / ".claude" / "commands" / "news-pipeline-steps.md"
                 ).read_text(encoding="utf-8")
        self.assertIn("確認 `date` 等於 TARGET_DATE 且 `items` 非空", steps)

    def test_a_schedule_still_exists(self):
        """根因修好不代表可以不抓料。"""
        self.assertTrue(_crons())


class TestDataActuallyLands(unittest.TestCase):
    def test_push_retries_with_rebase(self):
        """裸 push 會在兩分鐘視窗內被任何併發推送打掉，當天抓料整包不落地。"""
        body = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("git pull --rebase", body)
        # 重試耗盡必須讓 job 失敗——GitHub 寄信是本系統唯一的主動告警管道
        self.assertIn("::error::", body)
        self.assertIn("exit 1", body)

if __name__ == "__main__":
    unittest.main()
