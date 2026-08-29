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


class TestScheduleSurvivesDelay(unittest.TestCase):
    def test_earliest_run_still_lands_before_the_cloud_routine(self):
        """最早那班 ＋ 可容忍延遲，必須仍早於雲端 routine 開跑。

        這是整個修法的核心不變式。2026-08-29 之前只有 10:00 一班，10+12=22 > 13，
        所以 11 小時級的延遲一來就開天窗。
        """
        earliest = min(_cron_hour(c) for c in _crons())
        self.assertLessEqual(
            earliest + TOLERATED_DELAY_H, ROUTINE_HOUR_UTC,
            f"最早的 cron 在 {earliest}:00 UTC，加上可容忍延遲 {TOLERATED_DELAY_H}h "
            f"會落在 {earliest + TOLERATED_DELAY_H}:00，晚於 routine 的 {ROUTINE_HOUR_UTC}:00")

    def test_keeps_a_late_run_for_freshness_when_github_is_healthy(self):
        """保險窗不該取代原本那班：健康時 10:00 的資料比 00:00 新鮮 10 小時。"""
        self.assertTrue(any(_cron_hour(c) >= 6 for c in _crons()),
                        "全部 cron 都擠在清晨會讓健康日的日報平白老掉半天")


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
