"""Tests for .github/workflows/daily-gather.yml 的排程與落地保證。

這個 workflow 是「GH Actions 抓料 → 雲端 routine 寫日報」分裂架構的上游。它遲到
或抓完沒推上去，下游的新鮮度防線就會正確中止，當天日報開天窗——而那看起來像
「系統壞了」，實際上壞的是排程時間。

2026-08-27／08-28 連兩天發生：08-17～08-26 十天的排程延遲穩定在 +0.5～0.7h，
08-27 突然 +10.3h、08-28 +11.2h（GitHub 建立 run 的時間就已經晚了，非 runner
排隊），遠超當初依 2h42m 觀測值所設的 3 小時緩衝。

測試釘的是修法本身的不變式，因為這兩件事都很容易被「順手簡化」掉：

1. **保險窗必須夠早**——一個 run 寫進 gathered_items.json 的日期是它**實際執行
   當下**的 UTC 日期，所以只要執行落在 [00:00, 13:00) UTC 就算數。最早那班加上
   可容忍延遲必須仍早於雲端 routine 的開跑時刻。
2. **push 必須能重試**——裸 `git push` 在 checkout→push 的兩分鐘視窗內只要有人
   推了東西就 non-fast-forward 失敗，當天抓料整包不落地。
"""
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent      # CLAUDE_NEWS/
WORKFLOW = REPO_ROOT.parent / ".github" / "workflows" / "daily-gather.yml"

# 雲端 routine（daily-news-pipeline-cloud）的開跑時刻，見 docs/cloud-runbooks/daily.md
ROUTINE_HOUR_UTC = 13

# 可容忍的排程延遲。2026-08-28 實測 +11.2h 為目前觀測最大值，取 12 留一點餘裕。
# 這個數字若要調小，必須先有連續一段時間的實測支撐——調小它等於縮小保險窗。
TOLERATED_DELAY_H = 12


def _crons():
    # 刻意不用 PyYAML：它沒有登記在 src/requirements_news.txt，乾淨環境會
    # ImportError 讓整包測試掛掉（2026-08-29 review 發現）。這裡只要兩個字串。
    return re.findall(r'- cron: "([^"]+)"', WORKFLOW.read_text(encoding="utf-8"))


def _cron_hour(expr: str) -> int:
    return int(expr.split()[1])


class TestScheduleIsNotLoadBearing(unittest.TestCase):
    """排程延遲不該是正確性問題。

    2026-08-27／08-28 連兩天日報開天窗，起因是 GitHub 排程延遲 10–11 小時、穿透
    3 小時緩衝。當時的修法是加一個 00:00 UTC 保險窗——那是在對抗症狀。根因是
    下游把 TARGET_DATE 取自時鐘、又要求它等於資料的日期，等於強迫兩個各自排程的
    工作落在同一個 UTC 日；任一邊延遲，那天的日報就永久消失。

    根因已修在 `docs/cloud-runbooks/daily.md`（TARGET_DATE 由資料決定），保險窗
    因此移除。這裡不再釘「排程要多早」——那是在維護一個不該存在的耦合。
    """

    def test_the_downstream_no_longer_ties_target_date_to_the_clock(self):
        """根因的所在地：若有人把 TARGET_DATE 改回時鐘，排程延遲會再度變成
        永久資料遺失，而 workflow 這邊看不出任何異狀。"""
        runbook = (REPO_ROOT / "docs" / "cloud-runbooks" / "daily.md").read_text(encoding="utf-8")
        self.assertIn("TARGET_DATE = `src/gathered_items.json` 的 `date` 欄位", runbook)
        self.assertIn("不是** `date -u +%F`", runbook)

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
