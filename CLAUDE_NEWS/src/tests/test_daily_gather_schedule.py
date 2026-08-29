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


# 一輪 pipeline 的實測執行時間上限（30–60 分鐘，取 2 小時當保守值）。
# routine 起跑點 + 這個值不得跨過 UTC 午夜——跨了的話後半段重算 `date -u +%F`
# 會拿到 D+1，commit 訊息與檔名就會對不上。
MAX_RUNTIME_H = 2.0


CRON_RE = r'^\s*- cron: "([^"]+)"'


def _hour(cron):
    minute, hour = cron.split()[0], cron.split()[1]
    if not (minute.isdigit() and hour.isdigit()):
        raise AssertionError(
            f"cron「{cron}」用了清單或步進語法，本檔的時間推算只支援單一時刻。"
            "要改用多時刻排程，先擴充 _hour() 再改 cron，否則緩衝計算會靜默失真")
    return int(hour) + int(minute) / 60


# 各 routine 的實測執行時間。碰撞檢查比的是佔用區間，不是起跑點距離。
# 沒列到的一律給 0.5h（watchdog、健康檢查這類短工作）。
_RUNTIME_H = {"daily-news-pipeline-cloud": MAX_RUNTIME_H,
              "weekly-wiki-lint-cloud": MAX_RUNTIME_H}


def _occupied():
    """{trigger 名: (起, 迄)}，單位為 UTC 小時。"""
    out = {}
    for path in sorted(TRIGGER.parent.glob("*.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        if d.get("cron_expression"):
            start = _hour(d["cron_expression"])
            out[path.stem] = (start, start + _RUNTIME_H.get(path.stem, 0.5))
    return out


def _crons():
    # 刻意不用 PyYAML：它沒登記在 src/requirements_news.txt，乾淨環境會 ImportError。
    # 必須錨定行首（只容許空白），否則註解裡提到的 cron 字串也會被當成真的——
    # 本檔就有一句「加回 `- cron: "17 0 * * *"` 即可」，2026-08-29 實測它讓緩衝
    # 算成 12.7h 而非 2.6h，整條不變式因此失效。
    return re.findall(CRON_RE, WORKFLOW.read_text(encoding="utf-8"), flags=re.M)


class TestConsumerOutlastsProducerVariance(unittest.TestCase):
    def test_the_routine_waits_longer_than_the_worst_observed_delay(self):
        """核心不變式。緩衝小於實測變異時，排程一延遲就整天開天窗。"""
        # 取 max 而非 min：決定緩衝夠不夠的是**最晚**那班抓料。取 min 的話，加一班晚間抓料
        # 就能繞過這條不變式——而「不要再靠增加抓料班次對抗延遲」正是它的存在理由。
        gather = max(_hour(c) for c in _crons())
        routine = _hour(json.loads(TRIGGER.read_text(encoding="utf-8"))["cron_expression"])
        self.assertGreater(routine - gather, OBSERVED_MAX_DELAY_H,
                           f"抓料 {gather:.2f}h、routine {routine:.2f}h，"
                           f"緩衝 {routine - gather:.2f}h 未蓋過實測變異 {OBSERVED_MAX_DELAY_H}h")

    def test_the_routine_finishes_inside_the_same_utc_day(self):
        """看的是**收尾**不是起跑。

        原本這條寫 `assertLess(routine, 24)`——而 _hour() 對任何合法 cron 最大回傳
        23.98，所以它恆真、永遠不會紅。2026-08-29 reviewer 實測：把 routine 改成
        02:00 時紅的是緩衝條與碰撞條，這條完全沒動，卻被 commit 訊息記了功勞。
        這是同一天內第三次出現「護欄自己壞掉而看起來是綠的」。

        真正要守的是：TARGET_DATE 取自 `date -u +%F`（一句指令，不是一次求值），
        pipeline 跑到後半段若重算就會拿到 D+1。
        """
        routine = _hour(json.loads(TRIGGER.read_text(encoding="utf-8"))["cron_expression"])
        self.assertLessEqual(routine + MAX_RUNTIME_H, 24,
                             f"routine {routine:.2f}h + 執行 {MAX_RUNTIME_H}h 會跨過 UTC 午夜")


    def test_the_weekly_line_also_outlasts_the_variance(self):
        """同一個根因也存在於週更那條線：linkcheck 產報告 → weekly lint 讀它。

        linkcheck 延遲超過緩衝時，lint 會讀到上週的 link_health.json，而它的新鮮度
        門檻是 10 天——7 天的舊報告照樣通過，於是拿上週資料標死鏈而不自知。
        """
        linkcheck = REPO_ROOT.parent / ".github" / "workflows" / "weekly-linkcheck.yml"
        produced = _hour(re.findall(CRON_RE, linkcheck.read_text(encoding="utf-8"),
                                    flags=re.M)[0])
        lint = _hour(json.loads(
            (TRIGGER.parent / "weekly-wiki-lint-cloud.json").read_text(encoding="utf-8")
        )["cron_expression"]) + 24        # 週五產出 → 週六消費
        self.assertGreater(lint - produced, OBSERVED_MAX_DELAY_H,
                           f"linkcheck {produced:.2f}h → weekly lint {lint - 24:.2f}h(+1d)，"
                           f"緩衝 {lint - produced:.2f}h 未蓋過實測變異 {OBSERVED_MAX_DELAY_H}h")

class TestReplayCannotSilentlyCopyTheWrongDay(unittest.TestCase):
    """手動補跑仍然 `cp gathered_archive/<date>.json`，檔名差一個字就 replay 錯一天。

    這條測試在 2026-08-29 隨 v2 撤回被一起刪掉，但它與 v1/v2 無關——補跑路徑沒消失，
    護欄卻消失了。那是那一輪唯一淨減少的保護，由 reviewer 抓出後搬回。
    """

    def test_the_freshness_guard_still_checks_the_date(self):
        steps = (REPO_ROOT / ".claude" / "commands" / "news-pipeline-steps.md"
                 ).read_text(encoding="utf-8")
        self.assertIn("確認 `date` 等於 TARGET_DATE 且 `items` 非空", steps)


class TestCloudRoutinesDoNotCollide(unittest.TestCase):
    """兩個會 push 的雲端 routine 排在同一小時 → 非快轉推送被打掉，而且是靜默的。

    2026-08-29 移動排程時親自踩到：watchdog-push 移到 01:30，沒注意 weekly-wiki-lint
    就排在 01:00 週六。
    """

    def test_pushing_routines_do_not_overlap(self):
        """比的是**佔用區間**，不是起跑點的距離。

        原本門檻寫死 1 小時，於是 watchdog-push 排在 23:00 會通過——而每日 routine
        22:00 起跑、最長跑 2 小時，那正是該 trigger 檔的 _cron_note 明文記載「會在
        pipeline 還沒跑完時相撞」的配置。護欄放行了文件已裁定為錯的設定。
        """
        for a, (sa, ea) in _occupied().items():
            for b, (sb, eb) in _occupied().items():
                if a < b:
                    # 各自往前後繞一圈，處理跨 UTC 午夜的區間
                    overlap = any(sa < eb + k and sb + k < ea for k in (-24, 0, 24))
                    self.assertFalse(
                        overlap,
                        f"{a}（{sa:.2f}–{ea:.2f}h）與 {b}（{sb:.2f}–{eb:.2f}h）佔用區間重疊，"
                        "兩者都會 push 同一個 repo")


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
