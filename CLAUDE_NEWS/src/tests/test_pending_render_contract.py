"""懸置標記的渲染契約 — app.js 的 regex ↔ 規格的四段形狀。

規格端：`.claude/rules/wiki-ingest-format.md`「懸置標記語法」節
    `狀態符號` + `**類別詞**` + `（metadata）` + `｜**題目**：內文`
    狀態符號 ❓/🔎、類別詞 待查證/查無官方、metadata 欄位 標／查／複／訊、
    表格短標記 `⟨Q-nn⟩` 與細節區 `- ⟨Q-nn⟩ …` 一一對應。

消費端：`web_reader/assets/app.js` 的 `collapsePendingMeta()`／`annotateQids()`
    ——渲染層把 metadata 括號摺成 hover，正文只留狀態符號＋類別詞＋題目。

為什麼要這個測試：渲染層是**第三個**吃這份語法的地方（另兩個是
scripts/pending_markers.py 與 scripts/scan_pending_verifications.py）。
規格改了而渲染層沒跟，症狀是「網站上的標記靜默不再摺疊」——沒有任何既有檢查
會轉紅（2026-09-04 對抗輪的主要發現型態就是「規格改了、機器沒跟」）。
另於 `.claude/review-registry.json` 登記規格端／消費端各一組 sync_pair。
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP_JS = ROOT / "web_reader" / "assets" / "app.js"
SPEC = ROOT / ".claude" / "rules" / "wiki-ingest-format.md"


def _spec_section() -> str:
    text = SPEC.read_text(encoding="utf-8")
    m = re.search(r"^## 懸置標記語法.*?(?=^## |\Z)", text, re.M | re.S)
    assert m, "規格檔找不到「懸置標記語法」節——節名改了就必須同步本測試與渲染層"
    return m.group(0)


class TestPendingRenderContract(unittest.TestCase):
    def setUp(self):
        self.js = APP_JS.read_text(encoding="utf-8")
        self.spec = _spec_section()

    def test_kinds_match_spec(self):
        """類別詞（待查證／查無官方）兩端必須一致。"""
        m = re.search(r"const PENDING_KINDS = '([^']+)'", self.js)
        self.assertIsNotNone(m, "app.js 缺 PENDING_KINDS 常數")
        kinds = m.group(1).split("|")
        self.assertEqual(sorted(kinds), ["待查證", "查無官方"])
        for k in kinds:
            self.assertIn(k, self.spec, f"規格檔未出現類別詞「{k}」")

    def test_meta_fields_match_spec(self):
        """metadata 四欄（標／查／複／訊）兩端必須一致。"""
        m = re.search(r"const PENDING_META_FIELDS = \[([^\]]+)\]", self.js)
        self.assertIsNotNone(m, "app.js 缺 PENDING_META_FIELDS 常數")
        fields = re.findall(r"'([^']+)'", m.group(1))
        self.assertEqual(fields, ["標", "查", "複", "訊"])
        for f in fields:
            self.assertRegex(self.spec, rf"`{f} ", f"規格檔未出現 metadata 欄位「{f}」")

    def test_meta_regex_anchors_on_bold_kind_and_full_width_paren(self):
        """括號寫在粗體外是規格明文要求，渲染層的 regex 必須照這個形狀錨定。"""
        m = re.search(r"const PENDING_META_RE =\s*(/.+/g);", self.js)
        self.assertIsNotNone(m, "app.js 缺 PENDING_META_RE")
        pattern = m.group(1)
        self.assertIn("<strong>", pattern)
        self.assertIn("（", pattern)   # 全形左括號——半形版本吃不到規格的形狀
        self.assertIn("）", pattern)
        for kind in re.search(r"const PENDING_KINDS = '([^']+)'", self.js).group(1).split("|"):
            self.assertIn(kind, pattern, f"PENDING_META_RE 未涵蓋類別詞「{kind}」")
        self.assertIn("括號寫在粗體外", self.spec)

    def test_qid_regex_matches_spec_shape(self):
        """`⟨Q-nn⟩` 短標記形狀兩端一致；nn 為數字序號。"""
        m = re.search(r"const QID_RE = (/.+/g);", self.js)
        self.assertIsNotNone(m, "app.js 缺 QID_RE")
        self.assertIn("⟨Q-", m.group(1))
        self.assertIn("⟨Q-nn⟩", self.spec)

    def test_qid_regex_actually_matches_a_spec_example(self):
        """用規格檔裡的真實範例反向驗——regex 改壞（如漏掉全形括號）本測試轉紅。"""
        example = "❓ 待查證 ⟨Q-07⟩"
        js_qid = re.compile(r"(<li>\s*)?⟨Q-(\d+)⟩")
        self.assertTrue(js_qid.search(example))
        self.assertIn("⟨Q-07⟩", self.spec)

    def test_renderer_functions_are_wired_into_render_path(self):
        """有 regex 但沒接進渲染路徑＝假看守（本庫病史的標準形狀）。"""
        body = re.search(r"function renderMarkdownBody\([\s\S]*?\n  \}", self.js)
        self.assertIsNotNone(body)
        self.assertIn("collapsePendingMeta", body.group(0))
        self.assertIn("annotateQids", body.group(0))

    def test_markdown_source_is_not_modified(self):
        """摺疊只在渲染層。渲染層若改寫 wiki markdown，Obsidian 與檢查器會兩套真相。"""
        self.assertNotIn("pending-meta", (ROOT / "scripts" / "build_web.py").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
