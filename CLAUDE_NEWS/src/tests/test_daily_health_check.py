"""每日產出健康檢查的判準測試。

這支腳本是 watchdog（GitHub Actions 寄信）與推播 routine（手機通知）**共用的
單一判準**，所以它判錯的代價是雙份的：誤報會讓人開始忽略通知，漏報會讓
2026-07-31 那種「日報有、網站沒有」的半成品狀態再次無聲過關。

重點測「半成品狀態」與「近 7 天缺口」——前者是漏報過一次的實際缺陷。
"""
import json
import sys
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from daily_health_check import check, render_push, render_md, parked_branches  # noqa: E402

TODAY = date(2026, 7, 31)


def build_repo(root: Path, *, gather_date="2026-07-31", gather_n=73,
               digest=True, web=True, past_digests=(), past_archives=()):
    (root / "src").mkdir(parents=True, exist_ok=True)
    (root / "news").mkdir(parents=True, exist_ok=True)
    (root / "web_reader" / "data" / "digest").mkdir(parents=True, exist_ok=True)
    (root / "src" / "gathered_archive").mkdir(parents=True, exist_ok=True)

    (root / "src" / "gathered_items.json").write_text(
        json.dumps({"date": gather_date, "items": [{"t": i} for i in range(gather_n)]}),
        encoding="utf-8")
    if gather_date:
        (root / "src" / "gathered_archive" / f"{gather_date}.json").write_text(
            json.dumps({"date": gather_date, "items": [{"t": i} for i in range(gather_n)]}),
            encoding="utf-8")
    if digest:
        (root / "news" / f"{TODAY}.md").write_text("# 日報", encoding="utf-8")
    if web:
        (root / "web_reader" / "data" / "digest" / f"{TODAY}.json").write_text("{}", encoding="utf-8")
    for d in past_digests:
        (root / "news" / f"{d}.md").write_text("# 日報", encoding="utf-8")
    for d in past_archives:
        (root / "src" / "gathered_archive" / f"{d}.json").write_text("{}", encoding="utf-8")
    return root


ALL_PAST = [f"2026-07-{d:02d}" for d in range(24, 31)]


class TestCheck(unittest.TestCase):
    def _check(self, **kw):
        with TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp), past_digests=kw.pop("past_digests", ALL_PAST), **kw)
            return check(TODAY, repo=root)

    def test_all_green(self):
        r = self._check()
        self.assertTrue(r["healthy"])
        self.assertEqual(r["problems"], [])
        self.assertEqual(r["holes"], [])

    def test_digest_present_but_web_missing_is_a_problem(self):
        """2026-07-31 的實際狀態：日報與 wiki 都好，只有 web build 被跳過。

        這是本檔存在的主因——只檢查日報的話，這種半成品會被判成健康。
        """
        r = self._check(web=False)
        self.assertFalse(r["healthy"])
        self.assertEqual([p[0] for p in r["problems"]], ["網站"])

    def test_missing_digest_does_not_also_report_web(self):
        """日報就沒有時，不該同時噴「網站沒重建」——那是同一件事的兩種說法，
        會讓推播訊息看起來像壞了兩段。"""
        r = self._check(digest=False, web=False)
        self.assertEqual([p[0] for p in r["problems"]], ["日報"])

    def test_stale_gather_date_is_a_problem(self):
        r = self._check(gather_date="2026-07-30")
        self.assertIn("抓料", [p[0] for p in r["problems"]])

    def test_the_single_slot_file_moving_on_is_not_a_problem(self):
        """單槽的 gathered_items.json 已前進到隔天，但當日 archive 在——這是健康的。

        看門狗查的是前一個 UTC 日，而它自己若被 GitHub 排程延遲 ≥ 9.4 小時就會跑在
        下一班抓料之後。舊判準讀單槽檔，此時會把健康的一天判成抓料缺件、寄信＋推播
        假警報——而看門狗延遲正是本系統踩過的事故本身。
        """
        with TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp))
            (root / "src" / "gathered_items.json").write_text(
                json.dumps({"date": "2026-08-01", "items": [{"t": 1}]}), encoding="utf-8")
            r = check(TODAY, repo=root)
            self.assertEqual(r["problems"], [])

    def test_empty_gather_is_a_problem(self):
        """date 對但一則都沒抓到，等同沒跑——不可因為日期對就放行。"""
        r = self._check(gather_n=0)
        self.assertIn("抓料", [p[0] for p in r["problems"]])

    def test_holes_flag_replayability(self):
        past = [d for d in ALL_PAST if d != "2026-07-27"]
        with TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp), past_digests=past, past_archives=["2026-07-27"])
            r = check(TODAY, repo=root)
        self.assertEqual(len(r["holes"]), 1)
        self.assertTrue(r["holes"][0]["replayable"])

    def test_holes_alone_do_not_fail_today(self):
        """近 7 天有洞但今天齊全 → 今天算健康。

        補歷史洞是另一件事；讓它一直把今天的告警染紅，等於訓練人忽略告警。
        """
        r = self._check(past_digests=[d for d in ALL_PAST if d != "2026-07-27"])
        self.assertTrue(r["healthy"])
        self.assertEqual(len(r["holes"]), 1)

    def test_missing_gathered_file_does_not_crash(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "news").mkdir(parents=True)
            r = check(TODAY, repo=root)
        self.assertFalse(r["healthy"])


class TestRenderPush(unittest.TestCase):
    def test_push_message_within_length_limit(self):
        """PushNotification 限 200 字元，超過會被行動裝置截斷。"""
        with TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp), gather_date="2026-01-01", digest=False, web=False, past_digests=[])
            r = check(TODAY, repo=root)
        self.assertLessEqual(len(render_push(r)), 200)

    def test_push_message_leads_with_what_broke(self):
        with TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp), web=False, past_digests=ALL_PAST)
            r = check(TODAY, repo=root)
        msg = render_push(r)
        self.assertIn("網站", msg)
        self.assertIn("2026-07-31", msg)


class TestParkedBranches(unittest.TestCase):
    """未併分支偵測（2026-08-11 教訓：成果做完但 push 失敗停在分支，
    watchdog 卻建議重抓）。救法與缺件相反，訊息必須優先講清楚。"""

    def test_parked_branch_leads_push_message(self):
        """有未併分支時，推播要先講 git 救回，而不是叫人重抓。"""
        with TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp), past_digests=ALL_PAST)  # 今天檔案齊全
            r = check(TODAY, repo=root)
        r["parked"] = ["cloud-daily-2026-08-11-unmerged"]
        msg = render_push(r)
        self.assertIn("cloud-daily-2026-08-11-unmerged", msg)
        self.assertIn("git", msg)
        self.assertLessEqual(len(msg), 200)
        # 關鍵：明確勸阻重跑（提到 /news-pipeline 是為了說「勿」，不是建議）
        self.assertIn("勿", msg)

    def test_parked_branch_shown_in_md(self):
        with TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp), past_digests=ALL_PAST)
            r = check(TODAY, repo=root)
        r["parked"] = ["cloud-daily-2026-08-11-unmerged"]
        md = render_md(r)
        self.assertIn("未併成果分支", md)
        self.assertIn("cloud-daily-2026-08-11-unmerged", md)

    def test_render_without_parked_key_is_backward_compatible(self):
        """check() 不含 parked 鍵；render 不得因此 KeyError。"""
        with TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp), past_digests=ALL_PAST)
            r = check(TODAY, repo=root)
        self.assertNotIn("parked", r)
        render_push(r)   # 不得拋錯
        render_md(r)

    def test_parked_branches_failsafe_on_git_error(self):
        """git 查詢失敗一律回 []，絕不讓看門狗自己崩掉。"""
        self.assertEqual(parked_branches(Path("/nonexistent-repo-xyz")), [])


if __name__ == "__main__":
    unittest.main()
