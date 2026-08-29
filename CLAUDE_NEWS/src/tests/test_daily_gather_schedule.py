"""Tests for daily-gather workflow 與下游 routine 的時間關係。

2026-08-27／08-28 連兩天日報開天窗。根因是**消費者的緩衝小於生產者的實測變異**：
抓料 10:23 UTC、雲端 routine 13:00 UTC，緩衝 2.6 小時，而 GitHub 排程延遲了 10–11
小時。當時我先加保險窗 cron（增加生產者）、又試過讓 routine 掃 archive 補所有缺日
（增加語意），兩者都是在繞開根因。正解是把消費者移到變異之外——一個數字。

漏掉那天的**內容**本來就有保護：`main.py` 的 `check_gap_lookback()` 會在昨日日報
缺件時把回看窗拉到 50 小時。所以缺的只是檔案，不值得用「補跑舊日期」換 wiki 逆序。
"""
import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent      # CLAUDE_NEWS/
WORKFLOW = REPO_ROOT.parent / ".github" / "workflows" / "daily-gather.yml"
TRIGGER = REPO_ROOT / "docs" / "cloud-runbooks" / "triggers" / "daily-news-pipeline-cloud.json"

# GitHub 排程延遲的實測最大值（2026-08-28，+11.2h）。緩衝必須蓋過它。
# 這個數字要調小，必須先有一段時間的實測支撐——調小它等於把賭注押得更近。
OBSERVED_MAX_DELAY_H = 11.2


def _hour(cron):
    return int(cron.split()[1]) + int(cron.split()[0]) / 60


def _crons():
    # 刻意不用 PyYAML：它沒登記在 src/requirements_news.txt，乾淨環境會 ImportError。
    # 必須錨定行首（只容許空白），否則註解裡提到的 cron 字串也會被當成真的——
    # 本檔就有一句「加回 `- cron: "17 0 * * *"` 即可」，2026-08-29 實測它讓緩衝
    # 算成 12.7h 而非 2.6h，整條不變式因此失效。
    return re.findall(r'^\s*- cron: "([^"]+)"', WORKFLOW.read_text(encoding="utf-8"),
                      flags=re.M)


class TestConsumerOutlastsProducerVariance(unittest.TestCase):
    def test_the_routine_waits_longer_than_the_worst_observed_delay(self):
        """核心不變式。緩衝小於實測變異時，排程一延遲就整天開天窗。"""
        gather = min(_hour(c) for c in _crons())
        routine = _hour(json.loads(TRIGGER.read_text(encoding="utf-8"))["cron_expression"])
        self.assertGreater(routine - gather, OBSERVED_MAX_DELAY_H,
                           f"抓料 {gather:.2f}h、routine {routine:.2f}h，"
                           f"緩衝 {routine - gather:.2f}h 未蓋過實測變異 {OBSERVED_MAX_DELAY_H}h")

    def test_the_routine_still_lands_inside_the_same_utc_day(self):
        """跨過 UTC 午夜的話，抓料會寫成隔天的檔名，日期語意就散了。"""
        routine = _hour(json.loads(TRIGGER.read_text(encoding="utf-8"))["cron_expression"])
        self.assertLess(routine, 24)


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
