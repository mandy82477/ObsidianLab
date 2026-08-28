"""index.md ↔ 頁面標頭一致性檢查。

index 是手工彙整的路由層，頁面標頭是事實的家（`wiki/CLAUDE.md`「每個事實只有一個家」）。
主編彙整漏同步時，index 的領域/狀態欄會安靜地漂移——這正是 LLM wiki 文獻的
structure drift：索引與實際頁面集失步。本檢查抓三種漂移：

  1. entities/topics 有頁、index 無列（頁面在路由上不存在）
  2. index 有列、頁面不存在（死鏈——build 的 wikilink 檢查也會抓，這裡雙保險）
  3. index 的領域/狀態主值 ≠ 頁面標頭（單邊改動未同步）

狀態只比對主值（括號補充說明不計），領域比對全字串（六選一 emoji 標籤）。
"""
import re
import unittest
from pathlib import Path

WIKI = Path(__file__).resolve().parents[2] / "wiki"

ROW_RE = re.compile(r"^\|\s*\[\[([^\]|]+)(?:\|[^\]]*)?\]\]\s*\|(.+)$")


def _main_value(s: str) -> str:
    return re.split(r"[（(]", s.strip())[0].strip()


def _index_rows() -> dict[str, tuple[str, str]]:
    """回傳 {slug: (領域, 狀態主值)}。entities 表 5 欄（頁面|類型|領域|狀態|摘要）、
    topics 表 4 欄（頁面|領域|狀態|摘要）——以欄數判定領域/狀態落在哪格。"""
    rows: dict[str, tuple[str, str]] = {}
    for line in (WIKI / "index.md").read_text(encoding="utf-8-sig").splitlines():
        m = ROW_RE.match(line)
        if not m or not m.group(1).startswith(("entities/", "topics/")):
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        cells = [c for c in cells if c != ""] or [""]
        if len(cells) >= 4:          # 類型|領域|狀態|摘要
            domain, status = cells[1], cells[2]
        elif len(cells) == 3:        # 領域|狀態|摘要
            domain, status = cells[0], cells[1]
        else:
            continue
        rows[m.group(1)] = (domain, _main_value(status))
    return rows


def _page_header(f: Path) -> tuple[str, str]:
    domain = status = ""
    for ln in f.read_text(encoding="utf-8-sig").splitlines()[:40]:
        if ln.startswith("**領域：**"):
            domain = ln.replace("**領域：**", "").strip()
        elif ln.startswith("**狀態：**"):
            status = _main_value(ln.replace("**狀態：**", ""))
    return domain, status


class IndexSync(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = _index_rows()
        cls.pages = {
            f"{sub}/{p.stem}": p
            for sub in ("entities", "topics")
            for p in sorted((WIKI / sub).glob("*.md"))
        }

    def test_每頁都有_index_列(self):
        missing = sorted(set(self.pages) - set(self.rows))
        self.assertEqual(missing, [], f"這些頁在 index.md 無列（路由上不存在）：{missing}")

    def test_index_列都有對應頁(self):
        dead = sorted(set(self.rows) - set(self.pages))
        self.assertEqual(dead, [], f"index.md 這些列指向不存在的頁：{dead}")

    def test_領域與狀態主值一致(self):
        diffs = []
        for slug in sorted(set(self.rows) & set(self.pages)):
            idx_domain, idx_status = self.rows[slug]
            pg_domain, pg_status = _page_header(self.pages[slug])
            if pg_domain and idx_domain != pg_domain:
                diffs.append(f"{slug}: 領域 index『{idx_domain}』≠ 頁面『{pg_domain}』")
            if pg_status and idx_status != pg_status:
                diffs.append(f"{slug}: 狀態 index『{idx_status}』≠ 頁面『{pg_status}』")
        self.assertEqual(diffs, [], "index 與頁面標頭失步：\n" + "\n".join(diffs))


if __name__ == "__main__":
    unittest.main()
