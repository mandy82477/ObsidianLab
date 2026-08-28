"""Tests for github_releases 的 C 窗（存量盤點）。

這扇窗的職責是「把已成名但本庫從未報導過的 repo 逐日補進來」，所以測試釘的是
三件會讓它從資產變成負債的事：

1. **不重吐**——判準取自 `news/*.md`。這個判準壞掉的後果不是漏一則，是每天把
   整個存量重灌一次，日報直接報廢。
2. **上限關得緊**——2026-08-04 的設計註解明白寫著怕「首日灌入一批人盡皆知的
   條目」，上限是唯一防線。
3. **讀不到日報時安靜失敗**——空的 emitted 集合等價於「全部沒出現過」，那是
   最危險的狀態；此時必須不吐，而不是吐滿。
"""
import unittest
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from news_aggregator.sources import github_releases as mod

NOW = datetime.now(tz=timezone.utc)
HEADERS = {"User-Agent": "test"}


def _repo(name, stars, created="2026-01-01", desc="d"):
    return {
        "full_name": name,
        "html_url": f"https://github.com/{name}",
        "stargazers_count": stars,
        "created_at": f"{created}T00:00:00Z",
        "description": desc,
    }


class _FakeResp:
    """夠用就好的 requests.Response 替身。"""

    def __init__(self, repos):
        self._repos = repos
        self.headers = {"X-RateLimit-Remaining": "999"}

    def raise_for_status(self):
        pass

    def json(self):
        return {"items": self._repos}


class _NewsDir:
    """把 NEWS_DIR 指到暫存目錄，測試不依賴 repo 內的真實日報。"""

    def __init__(self, texts):
        self._tmp = TemporaryDirectory()
        root = Path(self._tmp.name)
        for i, text in enumerate(texts):
            (root / f"2026-08-{i + 1:02d}.md").write_text(text, encoding="utf-8")
        self._p = patch.object(mod, "NEWS_DIR", root)

    def __enter__(self):
        self._p.start()
        return self

    def __exit__(self, *exc):
        self._p.stop()
        self._tmp.cleanup()


class TestAlreadyReported(unittest.TestCase):
    def test_repo_present_in_a_digest_is_never_re_emitted(self):
        """日報出現過就不再吐——這是本窗唯一的去重機制。"""
        digest = "見 [superpowers](https://github.com/obra/superpowers) 這個框架。"
        repos = [_repo("obra/superpowers", 278000), _repo("new/thing", 5000)]
        with _NewsDir([digest]), patch.object(mod.requests, "get", return_value=_FakeResp(repos)):
            items = mod._inventory_sweep(HEADERS, NOW)
        self.assertEqual([i.title for i in items], ["new/thing"])

    def test_match_ignores_trailing_slash_and_case(self):
        """日報裡的連結寫法不該影響去重判定。"""
        digest = "https://github.com/Obra/Superpowers/"
        with _NewsDir([digest]), patch.object(
            mod.requests, "get", return_value=_FakeResp([_repo("obra/superpowers", 278000)])
        ):
            self.assertEqual(mod._inventory_sweep(HEADERS, NOW), [])


class TestDailyCap(unittest.TestCase):
    def test_cap_holds_even_when_the_whole_backlog_is_unreported(self):
        """冷啟動當天存量最大，上限就是為了這一天存在的。"""
        repos = [_repo(f"o/r{n}", 100000 - n) for n in range(50)]
        with _NewsDir(["（空日報）"]), patch.object(
            mod.requests, "get", return_value=_FakeResp(repos)
        ):
            items = mod._inventory_sweep(HEADERS, NOW)
        self.assertEqual(len(items), mod.INVENTORY_PER_DAY)

    def test_picks_the_highest_starred_first(self):
        """逐日往下走，先補最大的——讀者最可能已經聽過、卻在本庫查無的那些。"""
        repos = [_repo("o/small", 4000), _repo("o/huge", 90000), _repo("o/mid", 20000)]
        with _NewsDir(["（空日報）"]), patch.object(
            mod.requests, "get", return_value=_FakeResp(repos)
        ), patch.object(mod, "INVENTORY_PER_DAY", 2):
            items = mod._inventory_sweep(HEADERS, NOW)
        self.assertEqual([i.title for i in items], ["o/huge", "o/mid"])


class TestFailSilent(unittest.TestCase):
    def test_unreadable_news_dir_emits_nothing(self):
        """讀不到日報 ≠ 全部沒報導過。此時吐滿等於把整個存量重灌一次。"""
        with patch.object(mod, "NEWS_DIR", Path("/definitely/not/here")), patch.object(
            mod.requests, "get", return_value=_FakeResp([_repo("o/r", 90000)])
        ):
            self.assertEqual(mod._inventory_sweep(HEADERS, NOW), [])

    def test_search_failure_does_not_raise(self):
        """一條 scope 掛掉不得拖垮整個來源。"""
        with _NewsDir(["（空日報）"]), patch.object(
            mod.requests, "get", side_effect=RuntimeError("network down")
        ):
            self.assertEqual(mod._inventory_sweep(HEADERS, NOW), [])


class TestHonestLabelling(unittest.TestCase):
    def test_summary_carries_provenance_and_birth_date(self):
        """一個 2 月出生的 9 萬星 repo 不是今日新聞；摘要必須讓撰寫者看得出來。"""
        with _NewsDir(["（空日報）"]), patch.object(
            mod.requests,
            "get",
            return_value=_FakeResp([_repo("o/r", 90000, created="2026-02-15", desc="skills")]),
        ):
            item = mod._inventory_sweep(HEADERS, NOW)[0]
        self.assertIn("存量盤點", item.summary)
        self.assertIn("2026-02-15", item.summary)
        self.assertEqual(item.score_unit, "星")


class TestWindowGeometry(unittest.TestCase):
    def test_c_window_floor_meets_b_window_ceiling(self):
        """兩窗接壤不留縫也不重疊——縫隙就是下一個 agent-skills 藏身處。"""
        b_ceiling = int(mod.CROSSING_STAR_RANGE.split("..")[1])
        self.assertEqual(mod.INVENTORY_MIN_STARS, b_ceiling)

    def test_skills_scope_is_inventory_only(self):
        """skills scope 不得進 A/B 窗：100–3000 星帶實測被內容型 skill 洗版。"""
        skills_scope = '"agent skills" in:name,description'
        self.assertIn(skills_scope, mod._INVENTORY_SCOPES)
        self.assertNotIn(skills_scope, mod._REPO_SEARCH_SCOPES)

    def test_every_ab_scope_is_also_swept(self):
        """C 窗掛在所有 scope 上，不是只為 skills 打的補丁——冷啟動洞才算關掉。"""
        for scope in mod._REPO_SEARCH_SCOPES:
            self.assertIn(scope, mod._INVENTORY_SCOPES)


if __name__ == "__main__":
    unittest.main()
