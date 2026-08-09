"""Tests for scripts/scan_pending_verifications.py — 每日懸置掃描器。

規格見 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節。所有測試用
`TemporaryDirectory` 建假的 wiki_dir + 假日報 + 假 jsonl，`scan_digest()` 是
唯一的可測核心（`main()` 只負責 CLI 與找檔案），不需要真的 repo 內容。
"""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("scan_pending_verifications")


class _ScanCase(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.wiki_dir = self.root / "wiki"
        (self.wiki_dir / "topics").mkdir(parents=True)
        (self.wiki_dir / "entities").mkdir(parents=True)
        self.news_dir = self.root / "news"
        self.news_dir.mkdir()
        self.jsonl_path = self.root / "data" / "pending-signals.jsonl"

    def tearDown(self):
        self._tmp.cleanup()

    def write_wiki(self, rel_path: str, text: str) -> Path:
        p = self.wiki_dir / rel_path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def write_digest(self, date: str, text: str) -> Path:
        p = self.news_dir / f"{date}.md"
        p.write_text(text, encoding="utf-8")
        return p

    def scan(self, digest_path: Path, dry_run: bool = False) -> dict:
        return mod.scan_digest(digest_path, wiki_dir=self.wiki_dir,
                                jsonl_path=self.jsonl_path, dry_run=dry_run)


DIGEST_HEADER = "# Claude Code & Anthropic 每日新聞摘要\n\n---\n\n### ⭐ 重點話題\n"


class TestMultiProbeAnd(_ScanCase):
    def test_two_probes_in_same_entry_hits(self):
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 usage credits、方案分界）"
            "｜**旗艦分界**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[方案分界說明](https://example.com/a)**\n"
            "新方案的 usage credits 用量規則有變。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertEqual(len(result["new_records"]), 1)
        rec = result["new_records"][0]
        self.assertEqual(set(rec["probes_hit"]), {"usage credits", "方案分界"})

    def test_single_wide_probe_alone_does_not_hit(self):
        """單一過寬（短）探針，且非 wikilink，不構成命中——只有一個探針時
        必須滿足「wikilink 或正規化後長度 ≥6」才放行；`npm` 太短。"""
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 npm）｜**某工具**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[npm 套件更新](https://example.com/b)**\n"
            "npm 這次更新了幾個依賴。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertEqual(result["new_records"], [])

    def test_single_long_probe_passes_length_floor(self):
        """單探針但長度 ≥6，放行例外成立。"""
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 cross-session messaging）"
            "｜**跨 session 訊息**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[新功能上線](https://example.com/c)**\n"
            "支援 cross-session messaging 的討論。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertEqual(len(result["new_records"]), 1)


class TestWikilinkExpansion(_ScanCase):
    def test_wikilink_probe_matches_h1_alias(self):
        self.write_wiki("topics/ai-agent-safety.md", "# AI Agent 安全事件\n\n內容。\n")
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 [[topics/ai-agent-safety]]、CI secrets）"
            "｜**安全事件**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[AI Agent 安全事件更新](https://example.com/d)**\n"
            "本次涉及 CI secrets 外洩。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertEqual(len(result["new_records"]), 1)
        rec = result["new_records"][0]
        self.assertIn("[[topics/ai-agent-safety]]", rec["probes_hit"])
        self.assertEqual(rec["where"], "title")

    def test_wikilink_probe_matches_slug_segment_when_no_h1(self):
        """目標頁不存在或無 H1 時，退回 slug 末段當別名。"""
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 [[topics/ai-agent-safety]]、secrets leak）"
            "｜**安全事件**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[更新](https://example.com/e)**\n"
            "ai-agent-safety 議題延燒，涉及 secrets leak。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertEqual(len(result["new_records"]), 1)


class TestTiering(_ScanCase):
    def test_s_tier_two_probes_one_in_title(self):
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 usage credits、方案分界）"
            "｜**旗艦分界**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[usage credits 方案分界公布](https://example.com/f)**\n"
            "官方說明。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertEqual(result["new_records"][0]["tier"], "S")

    def test_a_tier_two_probes_both_in_body(self):
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 usage credits、方案分界）"
            "｜**旗艦分界**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[今日更新](https://example.com/g)**\n"
            "說明本次 usage credits 與方案分界的變動細節。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertEqual(result["new_records"][0]["tier"], "A")

    def test_b_tier_single_long_probe_in_body(self):
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 cross-session messaging）"
            "｜**跨 session 訊息**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[某更新](https://example.com/h)**\n"
            "提到了 cross-session messaging 這件事。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        rec = result["new_records"][0]
        self.assertEqual(rec["tier"], "B")
        # B 級不進派工附件
        groups, _ = mod.build_dispatch(result["new_records"])
        self.assertEqual(groups, {})


class TestDispatchGrouping(_ScanCase):
    def test_no_hit_list_excludes_reporters_that_did_hit(self):
        """回歸測試：REPORTER_ORDER 曾誤用 reporter slug 而非中文標籤，
        導致「無命中記者」永遠列出全部六類——即使商業記者當次確實有命中。"""
        self.write_wiki(
            "topics/example.md",
            "**領域：** 💼 商業\n\n"
            "❓ **待查證**（標 2026-08-01｜查 usage credits、方案分界）"
            "｜**旗艦分界**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[usage credits 方案分界公布](https://example.com/l)**\n"
            "官方說明。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        groups, no_hit = mod.build_dispatch(result["new_records"])
        self.assertIn("wiki-reporter-commercial", groups)
        self.assertNotIn("商業", no_hit, "商業當次有命中，不該出現在無命中清單")
        self.assertIn("模型", no_hit)


class TestDedup(_ScanCase):
    def test_rerun_does_not_duplicate(self):
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 usage credits、方案分界）"
            "｜**旗艦分界**：內文。\n",
        )
        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[usage credits 方案分界公布](https://example.com/i)**\n"
            "官方說明。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        first = self.scan(digest, dry_run=False)
        self.assertEqual(len(first["new_records"]), 1)
        lines_after_first = self.jsonl_path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines_after_first), 1)

        second = self.scan(digest, dry_run=False)
        self.assertEqual(second["new_records"], [], "同一 marker × entry 重跑不應再產生新紀錄")
        lines_after_second = self.jsonl_path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines_after_second), 1, "jsonl 不應被重複寫入")


class TestSuppression(_ScanCase):
    def test_suppressed_after_three_prior_hits_without_signal(self):
        marker_text = (
            "❓ **待查證**（標 2026-08-01｜查 usage credits、方案分界）"
            "｜**旗艦分界**：內文。\n"
        )
        self.write_wiki("topics/example.md", marker_text)

        # 預先塞 3 筆同 marker_id 的舊紀錄（無 訊 欄）到 jsonl，模擬過去已累積命中。
        # marker.marked = 2026-08-01；探針 join 順序需與 mk.probes 一致
        marker_id = mod.compute_marker_id(
            "topics/example",
            type("M", (), {"marked": "2026-08-01", "probes": ["usage credits", "方案分界"]})(),
        )
        self.jsonl_path.parent.mkdir(parents=True, exist_ok=True)
        with self.jsonl_path.open("w", encoding="utf-8") as fh:
            for i in range(3):
                fh.write(json.dumps({
                    "marker_id": marker_id,
                    "dedup_key": f"prior-{i}",
                }, ensure_ascii=False) + "\n")

        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[usage credits 方案分界公布](https://example.com/j)**\n"
            "官方說明。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertEqual(len(result["new_records"]), 1)
        self.assertTrue(result["new_records"][0]["suppressed"])
        groups, _ = mod.build_dispatch(result["new_records"])
        self.assertEqual(groups, {}, "suppressed 命中不得進派工附件")

    def test_not_suppressed_when_signal_present(self):
        """已有 訊 欄代表記者已看過，不應被壓制（規格：無一筆對應 marker 已有 訊 欄才壓制）。"""
        self.write_wiki(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 usage credits、方案分界｜訊 2026-08-05）"
            "｜**旗艦分界**：內文。\n",
        )
        marker_id = mod.compute_marker_id(
            "topics/example",
            type("M", (), {"marked": "2026-08-01", "probes": ["usage credits", "方案分界"]})(),
        )
        self.jsonl_path.parent.mkdir(parents=True, exist_ok=True)
        with self.jsonl_path.open("w", encoding="utf-8") as fh:
            for i in range(3):
                fh.write(json.dumps({
                    "marker_id": marker_id,
                    "dedup_key": f"prior-{i}",
                }, ensure_ascii=False) + "\n")

        digest = self.write_digest(
            "2026-08-10",
            DIGEST_HEADER +
            "**[usage credits 方案分界公布](https://example.com/k)**\n"
            "官方說明。\n"
            "`來源` · 08/10 00:00 UTC\n",
        )
        result = self.scan(digest, dry_run=True)
        self.assertFalse(result["new_records"][0]["suppressed"])


class TestMissingDigest(unittest.TestCase):
    def test_missing_digest_exits_zero(self):
        """找不到日報時 main() 必須 return 0，且不得動 wiki/ 或寫 jsonl。

        `_stdout()` 換成 `io.StringIO()`——真正的 `_stdout()` 包一層
        `io.TextIOWrapper(sys.stdout.buffer, ...)`，該 wrapper 被回收時會連帶
        關掉底層 `sys.stdout.buffer`，在同一行程內直接呼叫 `main()`（而非
        subprocess）會讓 `run_tests.py` 後續全部輸出炸掉
        （`ValueError: I/O operation on closed file`，同
        `test_script_stdout_hygiene.py` 防的那個坑，只是這裡是呼叫端而非
        模組層級抽換，該測試偵測不到，改用替身閃避）。
        """
        import io as _io

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            news_dir = root / "news"
            news_dir.mkdir()

            orig_news_dir = mod.NEWS_DIR
            orig_stdout_fn = mod._stdout
            mod.NEWS_DIR = news_dir
            mod._stdout = lambda: _io.StringIO()
            try:
                import sys as _sys
                old_argv = _sys.argv
                _sys.argv = ["scan_pending_verifications.py", "2099-01-01"]
                try:
                    rc = mod.main()
                finally:
                    _sys.argv = old_argv
            finally:
                mod.NEWS_DIR = orig_news_dir
                mod._stdout = orig_stdout_fn
            self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
