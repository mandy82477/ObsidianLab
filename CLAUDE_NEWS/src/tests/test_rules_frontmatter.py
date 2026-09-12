"""`.claude/rules/*.md` 的 `paths:` frontmatter 看守。

沒有 `paths:` 的規則檔會在每個 session 無條件載入（2026-09-12 實測 19 檔 244 KB）。
本檔驗三件事，對應三種靜默失效：
  1. 每檔都有 frontmatter 且有 `paths:`——漏寫就退回無條件全載
  2. 至少一個 glob 項目——空清單等於沒有範圍
  3. 每個 glob 在庫內至少匹配一個既有檔案——打錯路徑會讓規則永遠不載入，且沒人會發現
"""
import glob as globmod
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RULES_DIR = REPO_ROOT / ".claude" / "rules"

ITEM_RE = re.compile(r'^\s*-\s*"([^"]+)"\s*$')
BRACE_RE = re.compile(r"\{([^{}]*)\}")


def expand_braces(pattern: str) -> list[str]:
    """展開 {a,b} —— pathlib/glob 不支援 brace expansion。"""
    m = BRACE_RE.search(pattern)
    if not m:
        return [pattern]
    out = []
    for alt in m.group(1).split(","):
        out.extend(expand_braces(pattern[: m.start()] + alt + pattern[m.end():]))
    return out


def parse_paths(text: str) -> list[str] | None:
    """回傳 paths 清單；沒有 frontmatter 或沒有 paths key 時回 None。"""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block = text[4:end]
    lines = block.split("\n")
    try:
        start = next(i for i, ln in enumerate(lines) if ln.strip() == "paths:")
    except StopIteration:
        return None
    items = []
    for ln in lines[start + 1:]:
        m = ITEM_RE.match(ln)
        if not m:
            break
        items.append(m.group(1))
    return items


class TestRulesFrontmatter(unittest.TestCase):
    def setUp(self):
        self.files = sorted(RULES_DIR.glob("*.md"))
        self.assertTrue(self.files, "找不到任何 .claude/rules/*.md")

    def test_every_rule_has_paths(self):
        for path in self.files:
            with self.subTest(rule=path.name):
                text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
                self.assertTrue(
                    text.startswith("---\n"),
                    f"{path.name} 缺 frontmatter（無 paths 的規則檔會無條件全載）",
                )
                items = parse_paths(text)
                self.assertIsNotNone(items, f"{path.name} frontmatter 內找不到 paths:")
                self.assertGreaterEqual(
                    len(items), 1, f"{path.name} 的 paths 清單為空，等於沒有範圍"
                )

    def test_frontmatter_followed_by_heading(self):
        for path in self.files:
            with self.subTest(rule=path.name):
                text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
                body = text[text.find("\n---", 4) + len("\n---"):].lstrip("\n")
                self.assertTrue(
                    body.startswith("# "),
                    f"{path.name} frontmatter 之後應緊接 `# 標題`",
                )

    def test_every_glob_matches_something(self):
        for path in self.files:
            items = parse_paths(path.read_bytes().decode("utf-8").replace("\r\n", "\n")) or []
            for pattern in items:
                with self.subTest(rule=path.name, glob=pattern):
                    hit = any(
                        globmod.glob(str(REPO_ROOT / p), recursive=True)
                        for p in expand_braces(pattern)
                    )
                    self.assertTrue(
                        hit,
                        f"{path.name} 的 glob `{pattern}` 在庫內零匹配"
                        "（打錯路徑 → 規則永遠不載入且不會報錯）",
                    )


if __name__ == "__main__":
    unittest.main()
