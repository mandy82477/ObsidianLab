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
import daily_health_check as hc  # noqa: E402
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

    def test_the_hole_window_is_exactly_seven_days(self):
        """回看窗兩端都要釘：不含今天（今天由三項主檢查負責），只到 7 天前。

        `range(1, 8)` 的兩個數字改任一個都不會有別的測試發現——2026-08-29 突變測試
        實測。窗口變短會漏報舊缺口，變長會把已經超出 archive 保留期（14 天）的日期
        報成「可 replay」，兩種都讓這份報告失準。
        """
        with TemporaryDirectory() as tmp:
            # 今天有日報；前 1～8 天全部沒有
            root = build_repo(Path(tmp), past_digests=[])
            r = check(TODAY, repo=root)
            dates = [h["date"] for h in r["holes"]]
            self.assertEqual(len(dates), 7, f"回看窗應為 7 天，實得 {dates}")
            self.assertEqual(dates[0], "2026-07-30", "應從昨天開始，不含今天")
            self.assertEqual(dates[-1], "2026-07-24", "應止於 7 天前")

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



class TestRenderMdBranches(unittest.TestCase):
    """render_md 的每個分支都要真的被走過。

    2026-08-29 突變測試：這支腳本 27 個突變有 20 個沒被任何測試抓到，而它是 watchdog
    寄信與手機推播**共用的判準**——漏網的代價是「壞掉了但沒人喊」。
    """

    def _r(self, **kw):
        base = {"date": "2026-07-31", "gather_n": 73, "digest_ok": True, "web_ok": True,
                "healthy": True, "problems": [], "holes": [], "parked": []}
        base.update(kw)
        return base

    def test_gather_count_decides_the_first_line(self):
        self.assertIn("✅ ① 抓料：73 則", render_md(self._r()))
        md = render_md(self._r(gather_n=0, healthy=False, problems=[("抓料", "x")]))
        self.assertIn("❌ ① 抓料缺件", md)
        self.assertNotIn("✅ ① 抓料", md)

    def test_one_gathered_item_still_counts_as_present(self):
        """邊界：> 0 而不是 > 1。抓到一則也是抓到了，不該報缺件。"""
        self.assertIn("✅ ① 抓料：1 則", render_md(self._r(gather_n=1)))

    def test_no_holes_says_so_explicitly(self):
        self.assertIn("✅ 近 7 天無缺口", render_md(self._r()))

    def test_parked_branch_makes_it_offer_a_remedy_even_when_healthy(self):
        """健康但有未併分支 → 仍要給補救指引。

        那一行的條件是 `not healthy or parked`；改成 and 的話，成果卡在分支而檔案
        剛好齊全的那天，訊息會完全不提該怎麼救。
        """
        md = render_md(self._r(parked=["cloud-daily-2026-07-31-unmerged"]))
        self.assertIn("**補救**", md)

    def test_healthy_and_unparked_needs_no_remedy_line(self):
        self.assertNotIn("**補救**", render_md(self._r()))


class TestRenderPushBranches(unittest.TestCase):
    def _r(self, **kw):
        base = {"date": "2026-07-31", "gather_n": 0, "digest_ok": False, "web_ok": False,
                "healthy": False, "problems": [("抓料", "細節"), ("日報", "細節")],
                "holes": [], "parked": []}
        base.update(kw)
        return base

    def test_push_lists_problem_names_not_their_details(self):
        """訊息要短：只放問題名，不放括號裡的長說明。"""
        msg = render_push(self._r())
        self.assertIn("抓料、日報", msg)
        self.assertNotIn("細節", msg)

    def test_single_parked_branch_has_no_extra_count(self):
        msg = render_push(self._r(healthy=True, parked=["b1"]))
        self.assertIn("b1", msg)
        self.assertNotIn("另有", msg)

    def test_two_parked_branches_report_one_extra(self):
        """邊界：> 1 而不是 > 2。剛好兩條時也要說「另有 1 條」。"""
        msg = render_push(self._r(healthy=True, parked=["b1", "b2"]))
        self.assertIn("另有 1 條", msg)

    def test_multiple_parked_branches_report_the_remainder(self):
        """兩條時要說「另有 1 條」——減一，不是總數。"""
        msg = render_push(self._r(healthy=True, parked=["b1", "b2", "b3"]))
        self.assertIn("另有 2 條", msg)

    def test_parked_message_is_truncated_too(self):
        """未併分支那條路徑也吃 200 字元上限——分支名可以很長。"""
        msg = render_push(self._r(healthy=True, parked=["x" * 400]))
        self.assertLessEqual(len(msg), 200)

    def test_problem_message_is_truncated(self):
        msg = render_push(self._r(problems=[("抓料" * 200, "d")]))
        self.assertLessEqual(len(msg), 200)

    def test_holes_are_appended_as_a_count(self):
        msg = render_push(self._r(holes=[{"date": "2026-07-30", "replayable": True}]))
        self.assertIn("1 個舊缺口", msg)


class TestParkedBranchesParsing(unittest.TestCase):
    def test_nonzero_exit_yields_nothing(self):
        """git 失敗要回空清單，不是把 stderr 當成分支名。"""
        class R:
            # stdout 用真實格式（含 tab），否則就算 returncode 判斷被改壞，
            # 正則也匹配不到而照樣回 []——那會讓這條測試假綠。
            # 用 git 真正會回的失敗碼（128），不是 1——寫 1 的話「!= 0」被改成
            # 「!= 1」時這條測試照樣綠，等於沒守住那個判斷。
            returncode = 128
            stdout = "abc123" + chr(9) + "refs/heads/cloud-daily-2026-07-31-unmerged" + chr(10)
        orig = hc.subprocess.run
        hc.subprocess.run = lambda *a, **k: R()
        try:
            self.assertEqual(parked_branches(), [])
        finally:
            hc.subprocess.run = orig

    def test_branch_names_are_deduped_and_sorted(self):
        class R:
            returncode = 0
            stdout = ("x\trefs/heads/cloud-daily-2026-07-31-unmerged\n"
                      "y\trefs/heads/cloud-daily-2026-07-30-unmerged\n"
                      "z\trefs/heads/cloud-daily-2026-07-31-unmerged\n"
                      "w\trefs/heads/master\n")
        orig = hc.subprocess.run
        hc.subprocess.run = lambda *a, **k: R()
        try:
            got = parked_branches()
        finally:
            hc.subprocess.run = orig
        self.assertEqual(len(got), 2, f"應去重且只收未併分支，實得 {got}")
        self.assertEqual(got, sorted(got))

    def test_git_is_called_with_captured_text_output(self):
        """capture_output／text 任一為 False，stdout 就不是可比對的字串。"""
        seen = {}

        class R:
            returncode, stdout = 0, ""
        orig = hc.subprocess.run

        def fake(*a, **k):
            seen.update(k)
            return R()
        hc.subprocess.run = fake
        try:
            parked_branches()
        finally:
            hc.subprocess.run = orig
        self.assertTrue(seen.get("capture_output"))
        self.assertTrue(seen.get("text"))


class TestMainExitCode(unittest.TestCase):
    """退出碼就是告警本身——GitHub 對失敗的排程 workflow 寄信，那是唯一的主動管道。"""

    def _main(self, argv, result, parked):
        orig_check, orig_parked, orig_argv = hc.check, hc.parked_branches, sys.argv
        hc.check = lambda *a, **k: dict(result)
        hc.parked_branches = lambda *a, **k: list(parked)
        sys.argv = ["daily_health_check.py", *argv]
        try:
            import io as _io
            import contextlib
            buf = _io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = hc.main()
            return code, buf.getvalue()
        finally:
            hc.check, hc.parked_branches, sys.argv = orig_check, orig_parked, orig_argv

    BASE = {"date": "2026-07-31", "gather_n": 73, "digest_ok": True, "web_ok": True,
            "healthy": True, "problems": [], "holes": []}

    def test_all_green_exits_zero(self):
        code, _ = self._main(["--date", "2026-07-31"], self.BASE, [])
        self.assertEqual(code, 0)

    def test_unhealthy_exits_one(self):
        r = dict(self.BASE, healthy=False, problems=[("日報", "x")])
        code, _ = self._main(["--date", "2026-07-31"], r, [])
        self.assertEqual(code, 1)

    def test_healthy_but_parked_still_exits_one(self):
        """檔案齊全但成果卡在分支＝有東西沒整合，仍要喊。這是本檔補過的靜默洞。"""
        code, _ = self._main(["--date", "2026-07-31"], self.BASE, ["b1"])
        self.assertEqual(code, 1)

    def test_push_format_prints_one_line(self):
        _, out = self._main(["--date", "2026-07-31", "--format", "push"], self.BASE, [])
        self.assertEqual(len(out.strip().splitlines()), 1)

    def test_md_format_prints_the_report(self):
        _, out = self._main(["--date", "2026-07-31", "--format", "md"], self.BASE, [])
        self.assertIn("## 每日產出檢查", out)


if __name__ == "__main__":
    unittest.main()
