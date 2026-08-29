"""Tests for daily-gather workflow 與下游 routine 的時間關係。

2026-08-27／08-28 連兩天日報開天窗。抓料 10:23 UTC、雲端 routine 13:00 UTC，緩衝
2.6 小時，而 GitHub 那兩天把排程事件晚了 10–11 小時才派下來（三支 workflow 一起中招，
還掉了一場——是 GitHub 側的問題，執行時間全都只有 2 分鐘）。

第一版修法是把 routine 移到 22:00 UTC，用 11.6 小時的緩衝蓋過實測變異。它有效，但
**那 11.6 小時全部是空等**：抓料 2 分鐘、pipeline 30–60 分鐘，常態日根本不需要等，
卻天天付最壞情況的代價（送達由台北 21:00 變隔日 06:00）。

現在改成**多班重試**：routine 一天排 6 班，第一班在抓料之後不久，之後每 2 小時一班。
資料到了就做，沒到就靜默結束、留給下一班。這不需要新機制——「資料還沒到就不做」是
Step 1b 的新鮮度防線，「已經做過就別再做」是 Step 0b 的冪等閘，兩道都早就在了。

所以本檔釘的不再是「一個夠久的緩衝」，而是「**這組班次涵蓋得住變異、而且中間沒有
空窗**」。
"""
import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent      # CLAUDE_NEWS/
WORKFLOW = REPO_ROOT.parent / ".github" / "workflows" / "daily-gather.yml"
TRIGGER = REPO_ROOT / "docs" / "cloud-runbooks" / "triggers" / "daily-news-pipeline-cloud.json"

# GitHub 排程延遲的實測最大值（2026-08-28，+11.2h）。最後一班必須涵蓋它。
# 這個數字要調小，必須先有一段時間的實測支撐——調小它等於把賭注押得更近。
OBSERVED_MAX_DELAY_H = 11.2

# 常態派工延遲（2026-08 連續 11 天觀測：+29 到 +42 分鐘）。第一班要排在它之後，
# 否則常態日的第一班必然空跑，等於白費一班。
NORMAL_DISPATCH_DELAY_H = 0.75

# 相鄰班次的最大間隔。間隔大於這個值，「重試」就變成一段沒人看的空窗——資料在
# 空窗初期到達時，日報要多等一整個間隔才產出。
MAX_GAP_H = 2.0

# 一輪 pipeline 的實測執行時間上限（30–60 分鐘，取 2 小時當保守值）。
# 最後一班 + 這個值不得跨過 UTC 午夜——跨了的話後半段重算 `date -u +%F` 會拿到
# D+1，commit 訊息與檔名就會對不上。
MAX_RUNTIME_H = 2.0


CRON_RE = r'^\s*- cron: "([^"]+)"'


def _hours(cron):
    """cron 的小時清單（支援 `0 12,14,16 * * *`）。步進與範圍語法仍不支援。"""
    minute, hour = cron.split()[0], cron.split()[1]
    if not minute.isdigit() or not all(h.isdigit() for h in hour.split(",")):
        raise AssertionError(
            f"cron「{cron}」用了本檔不支援的語法（步進／範圍）。要改用它，"
            "先擴充 _hours() 再改 cron，否則時間推算會靜默失真")
    return sorted(int(h) + int(minute) / 60 for h in hour.split(","))


def _hour(cron):
    """單一時刻的 cron。多時刻請用 _hours()。"""
    hs = _hours(cron)
    assert len(hs) == 1, f"cron「{cron}」有多個時刻，呼叫端該用 _hours()"
    return hs[0]


def _routine_attempts():
    return _hours(json.loads(TRIGGER.read_text(encoding="utf-8"))["cron_expression"])


# 各 routine 的實測執行時間。碰撞檢查比的是佔用區間，不是起跑點距離。
# 沒列到的一律給 0.5h（watchdog、健康檢查這類短工作）。
_RUNTIME_H = {"daily-news-pipeline-cloud": MAX_RUNTIME_H,
              "weekly-wiki-lint-cloud": MAX_RUNTIME_H}


def _occupied():
    """{trigger 名: [(起, 迄), …]}，單位為 UTC 小時。多班次的 routine 有多個區間。"""
    out = {}
    for path in sorted(TRIGGER.parent.glob("*.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        if d.get("cron_expression"):
            run = _RUNTIME_H.get(path.stem, 0.5)
            out[path.stem] = [(s, s + run) for s in _hours(d["cron_expression"])]
    return out


def _crons():
    # 刻意不用 PyYAML：它沒登記在 src/requirements_news.txt，乾淨環境會 ImportError。
    # 必須錨定行首（只容許空白），否則註解裡提到的 cron 字串也會被當成真的——
    # 本檔就有一句「加回 `- cron: "17 0 * * *"` 即可」，2026-08-29 實測它讓緩衝
    # 算成 12.7h 而非 2.6h，整條不變式因此失效。
    return re.findall(CRON_RE, WORKFLOW.read_text(encoding="utf-8"), flags=re.M)


class TestRetryWindowCoversTheVariance(unittest.TestCase):
    """多班重試的三條性質：起點不浪費、終點蓋得住、中間沒空窗。"""

    def setUp(self):
        # 取 max 而非 min：決定時間關係的是**最晚**那班抓料。取 min 的話，加一班晚間
        # 抓料就能繞過這些不變式。
        self.gather = max(_hour(c) for c in _crons())
        self.attempts = _routine_attempts()

    def test_the_first_attempt_is_after_the_normal_dispatch_delay(self):
        """第一班早於常態派工延遲的話，常態日它必然空跑，等於少一班。"""
        self.assertGreaterEqual(
            self.attempts[0] - self.gather, NORMAL_DISPATCH_DELAY_H,
            f"抓料 {self.gather:.2f}h、第一班 {self.attempts[0]:.2f}h，"
            f"間隔 {self.attempts[0] - self.gather:.2f}h 小於常態派工延遲 "
            f"{NORMAL_DISPATCH_DELAY_H}h——這一班常態日必然空跑")

    def test_the_last_attempt_covers_the_worst_observed_delay(self):
        """最後一班就是這個設計的緩衝。它蓋不過實測變異，那天就沒有日報。"""
        self.assertGreaterEqual(
            self.attempts[-1] - self.gather, OBSERVED_MAX_DELAY_H,
            f"抓料 {self.gather:.2f}h、最後一班 {self.attempts[-1]:.2f}h，"
            f"涵蓋 {self.attempts[-1] - self.gather:.2f}h 未蓋過實測變異 "
            f"{OBSERVED_MAX_DELAY_H}h")

    def test_no_gap_between_attempts(self):
        """班次之間的空窗＝資料到了卻沒人看。間隔決定的是最壞的等待時間。"""
        for a, b in zip(self.attempts, self.attempts[1:]):
            self.assertLessEqual(
                b - a, MAX_GAP_H,
                f"{a:.2f}h 與 {b:.2f}h 之間隔了 {b - a:.2f}h，超過上限 {MAX_GAP_H}h")

    def test_the_last_attempt_finishes_inside_the_same_utc_day(self):
        """TARGET_DATE 取自 `date -u +%F`（一句指令，不是一次求值），跑到後半段
        若重算就會拿到 D+1，commit 訊息與檔名對不上。

        這條曾經寫成 `assertLess(routine, 24)`——而時數最大只會是 23.98，所以它恆真、
        永遠不會紅，卻被 commit 訊息記了功勞。看的必須是**收尾**不是起跑。
        """
        last = self.attempts[-1]
        self.assertLessEqual(
            last + MAX_RUNTIME_H, 24,
            f"最後一班 {last:.2f}h + 執行 {MAX_RUNTIME_H}h 會跨過 UTC 午夜")

    def test_the_watchdog_checks_the_previous_utc_day(self):
        """最後一班在 UTC 午夜收尾，所以看門狗**不可能**在當天判斷當天。

        這條原本寫成「看門狗時刻 ≥ 最後一班收尾」——而看門狗查前一日，換算後恆為
        真，永遠不會紅（2026-08-29 破壞測試當場抓到，是同一天第五條假綠的斷言）。
        真正要釘的是它查哪一天：改成查當日就會天天在班次還沒跑完時喊缺件。
        """
        self.assertGreaterEqual(self.attempts[-1] + MAX_RUNTIME_H, 24,
                                "最後一班若不再頂到 UTC 午夜，本條的前提就要重想")
        body = (REPO_ROOT.parent / ".github" / "workflows" / "daily-watchdog.yml"
                ).read_text(encoding="utf-8")
        self.assertIn("date -u -d yesterday", body,
                      "看門狗必須查前一個 UTC 日——最後一班 22:00 起跑、跨到午夜才收尾")

    def test_the_weekly_line_also_outlasts_the_variance(self):
        """同一個根因也存在於週更那條線：linkcheck 產報告 → weekly lint 讀它。

        linkcheck 延遲超過緩衝時，lint 會讀到上週的 link_health.json，而它的新鮮度
        門檻是 10 天——7 天的舊報告照樣通過，於是拿上週資料標死鏈而不自知。
        （週更只有一班，沒有重試可言，所以這條仍是「一個夠久的緩衝」。）
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


class TestRetryDoesNotSpamTheRepo(unittest.TestCase):
    """一天六班，若每班都寫開跑標記與心跳，就是每天最多 12 筆垃圾 commit。

    多班重試唯一的代價是放棄「每一班的可追查性」：只有真正生日報的那一班留證據，
    空跑的班次完全靜默。守住「今天到底有沒有日報」的是看門狗，不是逐班的心跳。
    """

    def test_the_shared_rules_say_empty_attempts_stay_silent(self):
        shared = (REPO_ROOT / "docs" / "cloud-runbooks" / "_shared.md"
                  ).read_text(encoding="utf-8")
        self.assertIn("空跑的班次完全靜默", shared)
        # 開跑標記必須排在兩道閘之後，否則靜默就無從談起
        self.assertIn("通過冪等閘與新鮮度防線之後", shared)


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

        門檻曾寫死 1 小時，於是 watchdog-push 排在 23:00 會通過——而每日 routine
        22:00 起跑、最長跑 2 小時，那正是該 trigger 檔的 _cron_note 明文記載「會在
        pipeline 還沒跑完時相撞」的配置。護欄放行了文件已裁定為錯的設定。
        """
        occupied = _occupied()
        for a, ia in occupied.items():
            for b, ib in occupied.items():
                if a < b:
                    for sa, ea in ia:
                        for sb, eb in ib:
                            # 各自往前後繞一圈，處理跨 UTC 午夜的區間
                            overlap = any(sa < eb + k and sb + k < ea for k in (-24, 0, 24))
                            self.assertFalse(
                                overlap,
                                f"{a}（{sa:.2f}–{ea:.2f}h）與 {b}（{sb:.2f}–{eb:.2f}h）"
                                "佔用區間重疊，兩者都會 push 同一個 repo")


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
