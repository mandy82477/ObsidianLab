"""Tests for news_aggregator.sources.official_skills_repos.OfficialSkillsRepos.

This source answers one question — "did an official skill appear or disappear?"
— so the tests pin the two failure modes that would make it useless: missing a
real membership change, and emitting on things that are not membership changes
(first sight, file-level churn, a failed listing that looks like deletions).
"""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch

from news_aggregator.sources import official_skills_repos as mod
from news_aggregator.sources.official_skills_repos import OfficialSkillsRepos

REPO = "anthropics/skills"


def _watch(**kw):
    base = {"repo": REPO, "path": "skills", "label": "官方技能庫", "status": "active"}
    base.update(kw)
    return base


class _Ctx:
    def __init__(self, watches):
        self._tmp = TemporaryDirectory()
        d = Path(self._tmp.name)
        self.config = d / "official_skills_repos.json"
        self.state = d / "official_skills_repos_state.json"
        self.config.write_text(json.dumps({"watches": watches}), encoding="utf-8")
        self._patches = [
            patch.object(mod, "CONFIG_PATH", self.config),
            patch.object(mod, "STATE_PATH", self.state),
        ]

    def __enter__(self):
        for p in self._patches:
            p.start()
        return self

    def __exit__(self, *exc):
        for p in self._patches:
            p.stop()
        self._tmp.cleanup()
        return False


def _resp(entries, remaining="4999"):
    r = MagicMock()
    r.json.return_value = entries
    r.headers = {"X-RateLimit-Remaining": remaining}
    r.raise_for_status = MagicMock()
    return r


def _dirs(*names):
    return [{"name": n, "type": "dir"} for n in names]


class TestBaseline(unittest.TestCase):
    def test_first_sight_records_silently(self):
        """第一次看到某路徑不得把既有技能全部當成新增。"""
        with _Ctx([_watch()]) as ctx:
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf", "docx"))):
                items = OfficialSkillsRepos().fetch()
            self.assertEqual(items, [])
            state = json.loads(ctx.state.read_text(encoding="utf-8"))
            self.assertEqual(state[f"{REPO}/skills"], ["docx", "pdf"])

    def test_unchanged_membership_emits_nothing(self):
        with _Ctx([_watch()]):
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf", "docx"))):
                OfficialSkillsRepos().fetch()
                items = OfficialSkillsRepos().fetch()
            self.assertEqual(items, [])


class TestMembershipChange(unittest.TestCase):
    def test_new_skill_emits_item(self):
        with _Ctx([_watch()]):
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf", "docx"))):
                OfficialSkillsRepos().fetch()
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf", "docx", "mcp-builder"))):
                items = OfficialSkillsRepos().fetch()
        self.assertEqual(len(items), 1)
        self.assertIn("mcp-builder", items[0].title)
        self.assertEqual(items[0].category, "official")

    def test_removed_skill_emits_item(self):
        with _Ctx([_watch()]):
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf", "docx"))):
                OfficialSkillsRepos().fetch()
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf"))):
                items = OfficialSkillsRepos().fetch()
        self.assertEqual(len(items), 1)
        self.assertIn("docx", items[0].title)

    def test_files_and_dotdirs_are_ignored(self):
        """只有目錄算技能；README 變動與 .claude-plugin 不是新技能。"""
        with _Ctx([_watch()]):
            payload = _dirs("pdf") + [
                {"name": "README.md", "type": "file"},
                {"name": ".claude-plugin", "type": "dir"},
            ]
            with patch.object(mod.requests, "get", return_value=_resp(payload)):
                OfficialSkillsRepos().fetch()
            payload2 = _dirs("pdf") + [{"name": "README.md", "type": "file"}]
            with patch.object(mod.requests, "get", return_value=_resp(payload2)):
                items = OfficialSkillsRepos().fetch()
        self.assertEqual(items, [])


class TestResilience(unittest.TestCase):
    def test_missing_config_returns_empty(self):
        with _Ctx([]) as ctx:
            ctx.config.unlink()
            self.assertEqual(OfficialSkillsRepos().fetch(), [])

    def test_invalid_config_never_raises(self):
        with _Ctx([]) as ctx:
            ctx.config.write_text("{not json", encoding="utf-8")
            self.assertEqual(OfficialSkillsRepos().fetch(), [])

    def test_retired_watch_is_skipped(self):
        with _Ctx([_watch(status="retired")]):
            with patch.object(mod.requests, "get", side_effect=AssertionError("must not fetch")):
                self.assertEqual(OfficialSkillsRepos().fetch(), [])

    def test_failed_listing_keeps_prior_set(self):
        """抓失敗不得覆寫既有集合，否則下次恢復會噴出一整批假『新增』。"""
        with _Ctx([_watch()]) as ctx:
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf", "docx"))):
                OfficialSkillsRepos().fetch()
            with patch.object(mod.requests, "get", side_effect=ConnectionError("down")):
                self.assertEqual(OfficialSkillsRepos().fetch(), [])
            state = json.loads(ctx.state.read_text(encoding="utf-8"))
        self.assertEqual(state[f"{REPO}/skills"], ["docx", "pdf"])

    def test_non_list_payload_does_not_wipe_state(self):
        """404/rate-limit 會回 dict；當成空清單就等於宣告全部技能被刪。"""
        with _Ctx([_watch()]) as ctx:
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf", "docx"))):
                OfficialSkillsRepos().fetch()
            bad = _resp(_dirs())
            bad.json.return_value = {"message": "Not Found"}
            with patch.object(mod.requests, "get", return_value=bad):
                self.assertEqual(OfficialSkillsRepos().fetch(), [])
            state = json.loads(ctx.state.read_text(encoding="utf-8"))
        self.assertEqual(state[f"{REPO}/skills"], ["docx", "pdf"])

    def test_rate_limit_floor_stops_further_watches(self):
        second = _watch(repo="anthropics/knowledge-work-plugins", path="", label="職能外掛")
        with _Ctx([_watch(), second]):
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf"), remaining="3")) as g:
                OfficialSkillsRepos().fetch()
        self.assertEqual(g.call_count, 1)

    def test_corrupt_state_resets_instead_of_raising(self):
        with _Ctx([_watch()]) as ctx:
            ctx.state.write_text("{broken", encoding="utf-8")
            with patch.object(mod.requests, "get", return_value=_resp(_dirs("pdf"))):
                self.assertEqual(OfficialSkillsRepos().fetch(), [])


if __name__ == "__main__":
    unittest.main()
