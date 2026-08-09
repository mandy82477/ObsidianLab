"""Tests for scripts/gen_wiki_frontmatter.py 的入鏈統計。

背景：懸置標記語法（`.claude/rules/wiki-ingest-format.md`「懸置標記語法」節）允許
metadata 區塊（`（標 YYYY-MM-DD｜查 探針…）`）裡放 `[[wikilink]]` 當偵測探針。探針
是給人／未來查證用的定位提示，不是內容引用，不該被算進 `inbound_links`——否則
全庫回填懸置標記後，signal 欄（孤島／高引用但停滯 四象限判定）會整批失真。

`strip_pending_probes()` 負責在入鏈統計前把 metadata 括號段換掉，只留下
`❓**待查證**` 本身；標記後方第四段（`｜**題目**：內文`）不在 PENDING_RE 的
match 範圍內，所以完全不受影響——那裡的 wikilink 是正文引用，照常計入。
"""
import unittest

from tests._helpers import load_script_module

mod = load_script_module("gen_wiki_frontmatter")


class TestStripPendingProbes(unittest.TestCase):
    def test_probe_wikilink_removed(self):
        text = (
            "- ❓ **待查證**（標 2026-08-07｜查 [[topics/ai-agent-safety]]、CI workflow secrets）"
            "｜**GitHub Issue 觸及 CI secrets**：內文不含連結"
        )
        stripped = mod.strip_pending_probes(text)
        self.assertEqual(mod.WIKILINK_RE.findall(stripped), [])
        self.assertIn("❓**待查證**", stripped)

    def test_body_wikilink_after_marker_still_counted(self):
        text = (
            "❓ **待查證**（標 2026-08-07｜查 usage credits、方案分界）"
            "｜**旗艦分界**：詳見 [[topics/model-comparison]] 的對照表"
        )
        stripped = mod.strip_pending_probes(text)
        self.assertEqual(mod.WIKILINK_RE.findall(stripped), ["topics/model-comparison"])

    def test_plain_prose_wikilink_unaffected(self):
        text = "一般正文提到 [[entities/sonnet-5]] 與 [[entities/opus-4-8|Opus 4.8]]。"
        stripped = mod.strip_pending_probes(text)
        self.assertEqual(
            mod.WIKILINK_RE.findall(stripped),
            ["entities/sonnet-5", "entities/opus-4-8"],
        )

    def test_multiple_probes_including_wikilink_and_plain_text(self):
        text = (
            "❓ **待查證**（標 2026-08-07｜查 [[topics/ai-agent-safety]]、CI secrets、"
            "[[entities/claude-code]]）｜**題目**：本次事件無正文連結"
        )
        stripped = mod.strip_pending_probes(text)
        self.assertEqual(mod.WIKILINK_RE.findall(stripped), [])

    def test_no_pending_marker_text_unchanged(self):
        text = "純粹的一般段落，沒有任何懸置標記，也沒有 wikilink。"
        self.assertEqual(mod.strip_pending_probes(text), text)

    def test_short_form_marker_not_matched_by_pending_re(self):
        # ⟨Q-nn⟩ 短標記不含 metadata 括號段，PENDING_RE 本就不吃它，
        # strip_pending_probes 對它必須是 no-op。
        text = "| 某議題 | ❓ 待查證 ⟨Q-07⟩ | 2026-08-07 |"
        self.assertEqual(mod.strip_pending_probes(text), text)


if __name__ == "__main__":
    unittest.main()
