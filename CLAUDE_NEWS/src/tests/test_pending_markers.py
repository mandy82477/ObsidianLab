"""Tests for scripts/pending_markers.py — the shared parser for 懸置標記.

Every fixture below is **real text from the wiki**, and most of them are shapes
that a first-pass classifier actually got wrong on 2026-08-09:

  · 「非已修復或拒絕」        誤判為已解除（否定詞翻轉語意）
  · 小節標題裡的「（…，待查證）」 誤判為元層級（標頭 ≠ 元層級）
  · 「12 條內容…待查證原文補全」 誤判為狀態計數摘要（「N 條」不緊接標記）
  · 「移除逾 80% 系統提示詞，列為待查證傳聞」 誤判為已解除（動詞受詞不是標記）
  · 「✅ 廣泛採用 / ⚡ 小圈子 / ⏳ 觀望中 / ⚠️ 效果存疑」 誤判為已解除（是圖例）

那次盤點的四類誤判合計 11 筆。這些斷言存在的理由就是不讓它們回來。
"""
import unittest

from tests._helpers import load_script_module

mod = load_script_module("pending_markers")


def cls_of(text: str, word_index: int = 0) -> str:
    hits = mod.iter_legacy(text)
    return hits[word_index].cls if hits else "(none)"


def reason_of(text: str, word_index: int = 0) -> str:
    hits = mod.iter_legacy(text)
    return hits[word_index].reason if hits else "(none)"


class TestNewSyntaxParsing(unittest.TestCase):
    def test_standard_form(self):
        text = (
            "- ❓ **待查證**（標 2026-08-07｜查 [[topics/ai-agent-safety]]、CI workflow secrets）"
            "｜**GitHub Issue 觸及 CI secrets**：The Hacker News 報導…"
        )
        (m,) = mod.iter_pending(text)
        self.assertEqual(m.sym, "❓")
        self.assertEqual(m.kind, "待查證")
        self.assertEqual(m.marked, "2026-08-07")
        self.assertEqual(m.probes, ["[[topics/ai-agent-safety]]", "CI workflow secrets"])
        self.assertIsNone(m.review)
        self.assertIsNone(m.signal)

    def test_all_optional_fields(self):
        text = "🔎 **查無官方**（標 2026-07-18｜查 usage credits、方案分界｜複 2026-08-21｜訊 2026-08-10）｜**旗艦分界**：…"
        (m,) = mod.iter_pending(text)
        self.assertEqual((m.review, m.signal), ("2026-08-21", "2026-08-10"))

    def test_table_short_marker_and_detail_anchor_pair_up(self):
        text = (
            "| 某議題 | ❓ 待查證 ⟨Q-07⟩ | 2026-08-07 |\n\n"
            "**懸置細節**\n"
            "- ⟨Q-07⟩ ❓ **待查證**（標 2026-08-07｜查 [[topics/ai-agent-safety]]、CI secrets）：僅標題可用\n"
        )
        short = mod.SHORT_RE.search(text)
        self.assertEqual(short.group("qid"), "Q-07")
        (m,) = mod.iter_pending(text)
        self.assertEqual(m.qid, "Q-07", "細節區的標記要認得自己屬於哪個 ⟨Q-nn⟩")

    def test_marker_inside_code_block_is_ignored(self):
        text = "```\n❓ **待查證**（標 2026-08-07｜查 example probe）\n```\n"
        self.assertEqual(mod.iter_pending(text), [])


class TestShortMarkerExcludedFromLegacy(unittest.TestCase):
    """表格短標記 ❓ 待查證 ⟨Q-nn⟩ 是新語法，不該被 iter_legacy() 算成舊字樣。

    2026-08-09 起 iter_legacy() 排除清單只含 iter_pending()（完整標準式）的 span，
    漏排 SHORT_RE 的 span，導致已回填的表格短標記被 audit 誤計為「P 未回填」，
    與 checker（只認新語法，判定合規）打架。"""

    def test_table_short_marker_not_counted_as_legacy(self):
        text = "| 某議題 | ❓ 待查證 ⟨Q-07⟩ | 2026-08-07 |\n"
        self.assertEqual(mod.iter_legacy(text), [])

    def test_short_marker_inside_code_block_stays_meta(self):
        """code block 內的字樣本就走 M（code span）分類，與本次修復的排除邏輯無關；
        這裡只確認 SHORT_RE 排除不會在 in_code 情境下拋錯或誤判成別的類別。"""
        text = "```\n❓ 待查證 ⟨Q-01⟩\n```\n"
        (hit,) = mod.iter_legacy(text)
        self.assertEqual(hit.cls, "M")


class TestSemanticInversion(unittest.TestCase):
    """字面相同、意思相反。誤判成待辦會讓已收斂的成功案例算成未結負債。"""

    def test_resolved_narratives_are_class_r(self):
        for text in (
            "- 2026-06-22：…非 Boris Cherny；本頁解除待核實",
            "具名 Business Insider 來源確認發言人為 Fiona Fung，兩頁待核實已解除。",
            "#### 2026-08-08：官方 Help Center 查證，四方矛盾報導收斂（✅ 待查證結案）",
            "已知問題 #24798 狀態自待查證轉為 ✅ 已修復 v2.1.224",
            "解除 08-08 媒體報導階段「未經官方確認」標記，已同步矩陣",
        ):
            with self.subTest(text[:24]):
                self.assertEqual(cls_of(text), "R")

    def test_negated_cue_stays_pending(self):
        """「非已修復」含「已修復」，但那是真懸置。"""
        text = "- ❓ **待查證（尚待官方受理，非已修復或拒絕）**｜**某問題**：…"
        self.assertEqual(cls_of(text), "P")

    def test_cue_with_different_object_stays_pending(self):
        """「移除」的受詞是系統提示詞，不是標記——中間隔著逗號。"""
        text = "轉述一則低互動（16 分）推文稱 Anthropic 為 Opus 5 移除逾 80% 系統提示詞，列為待查證傳聞"
        self.assertEqual(cls_of(text), "P")


class TestMetaLevel(unittest.TestCase):
    def test_status_count_heading(self):
        text = "### 🛡️ 安全與隱私（5 條未修復、6 條待查證）"
        self.assertEqual(cls_of(text), "M")
        self.assertIn("計數", reason_of(text))

    def test_symbol_legend(self):
        text = "> 每條開頭的狀態標記回答「現在還會發生嗎」：🔴 未修復 / ✅ 已修復 / ⛔ 官方拒修 / ❓ 待查證。"
        self.assertEqual(cls_of(text), "M")

    def test_adoption_legend_is_meta_not_resolved(self):
        """這行含 ✅ 與「已放棄」，但它是圖例不是已解除敘述。"""
        text = "> ✅ 廣泛採用 / ⚡ 小圈子使用 / ⏳ 觀望中 / ⚠️ 效果存疑 / ❌ 已放棄"
        self.assertEqual(cls_of(text), "M")

    def test_toc_anchor(self):
        text = "| 沙盒逃脫案例 | [第 3 段](#3-decrypt沙盒逃脫案例待查證) |"
        self.assertEqual(cls_of(text), "M")
        self.assertIn("anchor", reason_of(text))

    def test_daibu_is_out_of_scope(self):
        """「待補」＝資料不全（去補就好），與「事實未確認」是兩種處置，刻意不掃。
        它也是誤命中大戶——coding-workflow-guide 的目錄 anchor 就吃掉 17 筆。"""
        self.assertEqual(mod.iter_legacy("- 官方技術細節尚待補充"), [])
        self.assertEqual(mod.iter_legacy("| [第 7 段](#7-社群面待補) |"), [])

    def test_frontmatter_is_derived_not_source(self):
        text = '---\npage: "entities/x"\nstatus: "active（待核實）"\n---\n# X\n'
        self.assertEqual(cls_of(text), "M")

    def test_heading_is_not_automatically_meta(self):
        """小節標題裡的懸置是真懸置——這條誤判曾一次吃掉 ai-agent-safety 5 筆。"""
        text = "### Decrypt：「Claude 也出現沙盒逃脫案例」（2026-07-28 新增，待查證）"
        self.assertEqual(cls_of(text), "P")

    def test_count_not_adjacent_to_marker_is_not_a_summary(self):
        """「12 條」講的是內容數量，不是狀態計數。"""
        text = "系統性整理出 12 種常見架構決策錯誤（具體 12 條內容原文未詳列，待查證原文補全）"
        self.assertEqual(cls_of(text), "P")


class TestCoOccurrence(unittest.TestCase):
    def test_inference_tag_does_not_swallow_the_pending_one(self):
        """（推論）是永久認識論標籤，會與懸置同句共現——排除必須在 match 層。"""
        text = "市值蒸發約 2,700 億美元、Gemini 3.5 延期（皆推論，未經官方確認）。"
        hits = mod.iter_legacy(text)
        self.assertEqual([h.word for h in hits], ["未經官方確認"])
        self.assertEqual(hits[0].cls, "P")

    def test_giant_cell_yields_multiple_independent_matches(self):
        """一格 1200+ 字含多筆，行與儲存格都不是合法單位。"""
        text = (
            "| 2026-08-09 | **今日彙整**：" + "背景敘述。" * 40
            + "另收錄 1 則待查證問題：prompt 過長。" + "更多說明。" * 40
            + "另有一項待核實傳聞。" + "尾巴。" * 20 + " |"
        )
        hits = mod.iter_legacy(text)
        self.assertGreaterEqual(len(hits), 2)
        self.assertTrue(all(h.in_table_cell for h in hits))


class TestProbeQuality(unittest.TestCase):
    def test_stoplist_rejected(self):
        for probe in ("Claude", "anthropic", "AI", "Cowork"):
            with self.subTest(probe):
                self.assertIsNotNone(mod.probe_too_weak(probe))

    def test_too_short_rejected(self):
        self.assertIsNotNone(mod.probe_too_weak("npm"))     # ASCII < 4
        self.assertIsNotNone(mod.probe_too_weak("管制"))     # CJK < 3

    def test_reasonable_probes_pass(self):
        for probe in ("cross-session messaging", "usage credits", "出口管制", "#74649"):
            with self.subTest(probe):
                self.assertIsNone(mod.probe_too_weak(probe))

    def test_wikilink_probe_always_passes(self):
        """wikilink 由建置驗證目標存在，且探針詞跟著實體頁走。"""
        self.assertIsNone(mod.probe_too_weak("[[entities/pricing]]"))
        self.assertEqual(mod.wikilink_target("[[entities/pricing]]"), "entities/pricing")


class TestScanScope(unittest.TestCase):
    def test_non_content_files_excluded(self):
        from pathlib import Path
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmp:
            base = Path(tmp)
            (base / "entities").mkdir()
            (base / "_views").mkdir()
            for rel in ("log.md", "CLAUDE.md", "feature-radar-archive-2026-05.md",
                        "_views/pending.md", "entities/real.md", "overview.md"):
                (base / rel).write_text("待查證", encoding="utf-8")
            names = {p.name for p in mod.wiki_pages(base)}
        self.assertEqual(names, {"real.md", "overview.md"})


if __name__ == "__main__":
    unittest.main()
