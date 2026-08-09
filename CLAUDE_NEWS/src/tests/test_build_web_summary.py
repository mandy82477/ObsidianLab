"""Wiki 卡片摘要不得為空。

`build_web.py` 的 `SUMMARY_HEADERS` 只認 `## 現況` 與 `## 摘要` 兩個標題名。2026-08-08
發現任何用其他首節標題的頁面都會靜默產出空摘要，在 wiki 列表頁變成一張沒有任何說明
的卡片——讀者連「要不要點進去」都判斷不了，而建置照樣 exit 0，沒有任何訊號。

當時全庫已有 2 頁中招（`coding-workflow-guide`、`ai-agent-safety-archive`）。
修法是加後備（callout → 第一段正文），這裡把「不得為空」釘成測試，避免後備日後被改壞
或又出現新的繞過路徑。
"""
import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
WIKI_JSON_DIR = REPO_ROOT / "web_reader" / "data" / "wiki"


class TestWikiCardSummary(unittest.TestCase):
    def test_no_wiki_page_has_empty_summary(self):
        """列表頁的每張卡片都要有摘要，否則讀者無從判斷該不該點進去。"""
        if not WIKI_JSON_DIR.is_dir():
            self.skipTest("web_reader 尚未建置，跳過")

        pages = sorted(WIKI_JSON_DIR.glob("*.json"))
        self.assertTrue(pages, "web_reader/data/wiki/ 沒有任何頁面，建置可能失敗")

        empty = []
        for f in pages:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except Exception as e:  # 壞掉的 JSON 是另一種故障，一併報出來
                empty.append(f"{f.stem}（JSON 無法解析: {e}）")
                continue
            if not (data.get("summary") or "").strip():
                empty.append(f.stem)

        self.assertEqual(
            [], empty,
            "以下頁面在網站上會是空白卡片，請確認 build_web.py 的摘要後備是否失效：\n  - "
            + "\n  - ".join(empty),
        )


if __name__ == "__main__":
    unittest.main()
