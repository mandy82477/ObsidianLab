#!/usr/bin/env python3
"""
check_arch_docs.py — 架構文件漂移機械檢查（取代 /arch-doc-sync 人肉核對）。

只用標準庫（re / pathlib），比照 scripts/check_rules.py 的風格：讀設定 →
跑確定性檢查 → 印人類可讀報告 → exit code。

四類檢查：
    1. sources        — src/news_aggregator/main.py 的 sources 清單
                         與 Design Diagram.md / architecture-current.html 是否一致
                         （含「已退役來源」黑名單，抓「圖上還畫著但 main.py 已移除」的漂移）
    2. dates           — Design Diagram.md「最後更新」／architecture-current.html
                         「現況截至」／architecture-evolution.html 副標結束日 三處相等
    3. charset         — 兩份 HTML 皆含 <meta charset="utf-8">
    4. css_tokens      — 兩份 HTML 用到的 var(--xxx) 皆在 architecture.css 的
                         :root 有定義

用法：
    python scripts/check_arch_docs.py

行為：
    全部通過 → exit 0，列印報告
    任一檢查失敗 → exit 1，列印報告與失敗明細

供 scripts/run_tests.py 呼叫，也供 .claude/commands/arch-doc-sync.md 步驟 5/6 呼叫。
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MAIN_PY = REPO_ROOT / "src" / "news_aggregator" / "main.py"
DESIGN_DIAGRAM = REPO_ROOT / "src" / "DesignDocument" / "Design Diagram.md"
CURRENT_HTML = REPO_ROOT / "docs" / "architecture-current.html"
EVOLUTION_HTML = REPO_ROOT / "docs" / "architecture-evolution.html"
ARCH_CSS = REPO_ROOT / "docs" / "architecture.css"

# main.py 顯示名 → 文件內比對用關鍵字（預設等於顯示名本身；
# main.py 的 "GitHub" 對應 GitHubReleases class，文件內寫「GitHub Releases」，
# 若直接用 "GitHub" 當關鍵字會誤命中「GitHub Issues」，故特例覆寫）。
NAME_KEYWORD_OVERRIDES = {
    "GitHub": "GitHub Releases",
}

# 已退役來源黑名單：若這些字串仍出現在文件裡，代表文件沒跟著 main.py 移除
# （2026-07-11 踩過的坑：lobste.rs 已從 main.py 移除，圖上卻仍畫著）。
RETIRED_SOURCES = ["lobste.rs", "lobste"]


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


class Report:
    def __init__(self):
        self.sections: list[dict] = []
        self.ok = True

    def add(self, name: str, passed: bool, details: list[str]):
        self.sections.append({"name": name, "passed": passed, "details": details})
        if not passed:
            self.ok = False

    def render(self) -> str:
        lines = ["# check_arch_docs.py 報告", ""]
        for sec in self.sections:
            icon = "✅" if sec["passed"] else "❌"
            lines.append(f"{icon} {sec['name']}")
            for d in sec["details"]:
                lines.append(f"    {d}")
            lines.append("")
        lines.append("=" * 40)
        if self.ok:
            lines.append("狀態：✅ 全部檢查通過")
        else:
            lines.append("狀態：❌ 有檢查失敗，exit 1")
        return "\n".join(lines)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


# ---------------------------------------------------------------------------
# 檢查 1：來源清單一致（sources）
# ---------------------------------------------------------------------------

def parse_registered_sources() -> list[str]:
    """從 main.py 的 `sources = [ ("Name", Class()), ... ]` 抽出顯示名清單。"""
    if not MAIN_PY.exists():
        return []
    text = read_text(MAIN_PY)
    m = re.search(r"sources\s*=\s*\[(.*?)\]\s*\n", text, re.DOTALL)
    if not m:
        return []
    block = m.group(1)
    return re.findall(r'\(\s*"([^"]+)"\s*,', block)


def check_sources(report: Report):
    names = parse_registered_sources()
    if not names:
        report.add(
            "檢查 1：來源清單一致（sources）",
            False,
            [f"無法從 {rel(MAIN_PY)} 解析出 sources 清單（正規表達式未命中，檢查 main.py 是否改了寫法）"],
        )
        return

    targets = {
        "Design Diagram.md": DESIGN_DIAGRAM,
        "architecture-current.html": CURRENT_HTML,
    }
    texts = {label: (read_text(p) if p.exists() else None) for label, p in targets.items()}

    details = [f"main.py 註冊來源（{len(names)} 個）：{', '.join(names)}"]
    missing: list[str] = []
    for label, text in texts.items():
        if text is None:
            missing.append(f"{label}：檔案不存在")
            continue
        for name in names:
            keyword = NAME_KEYWORD_OVERRIDES.get(name, name)
            # mermaid 節點常把長名稱用「字面上的 \n」折行（如 "Claude API\nRelease Notes"，
            # 檔案裡是反斜線+n 兩個字元，不是真正換行），故關鍵字內的空白改成寬鬆比對：
            # 允許真實空白/換行，或字面 \n。
            keyword_re = re.compile(r"(?:\s+|\\n)".join(re.escape(part) for part in keyword.split(" ")))
            if not keyword_re.search(text):
                missing.append(f"{label}：缺少來源 `{name}`（比對關鍵字 `{keyword}`）")

    retired_hits: list[str] = []
    for label, text in texts.items():
        if text is None:
            continue
        for retired in RETIRED_SOURCES:
            if retired in text:
                retired_hits.append(f"{label}：仍含已退役來源 `{retired}`（main.py 已無此來源，文件未跟著移除）")

    if missing:
        details.append(f"缺漏 {len(missing)} 處：")
        details.extend(f"  - {m}" for m in missing)
    else:
        details.append("兩份文件皆涵蓋全部註冊來源")

    if retired_hits:
        details.append(f"已退役來源殘留 {len(retired_hits)} 處：")
        details.extend(f"  - {h}" for h in retired_hits)
    else:
        details.append(f"無已退役來源殘留（黑名單：{', '.join(RETIRED_SOURCES)}）")

    passed = not missing and not retired_hits
    report.add("檢查 1：來源清單一致（sources）", passed, details)


# ---------------------------------------------------------------------------
# 檢查 2：日期三處同步（dates）
# ---------------------------------------------------------------------------

def check_dates(report: Report):
    date_re = r"(\d{4}-\d{2}-\d{2})"
    sources = {
        "Design Diagram.md（最後更新）": (DESIGN_DIAGRAM, r"\*\*最後更新：\*\*\s*" + date_re),
        "architecture-current.html（現況截至）": (CURRENT_HTML, r"現況截至\s*" + date_re),
        "architecture-evolution.html（副標結束日）": (EVOLUTION_HTML, r"&rarr;\s*" + date_re),
    }

    values: dict[str, str] = {}
    details = []
    missing = []
    for label, (path, pattern) in sources.items():
        if not path.exists():
            missing.append(f"{label}：檔案不存在（{rel(path)}）")
            continue
        text = read_text(path)
        m = re.search(pattern, text)
        if not m:
            missing.append(f"{label}：找不到符合 `{pattern}` 的日期")
            continue
        values[label] = m.group(1)

    for label, val in values.items():
        details.append(f"{label} = {val}")

    unique_values = set(values.values())
    passed = not missing and len(unique_values) <= 1 and len(values) == len(sources)
    if missing:
        details.append(f"缺漏 {len(missing)} 處：")
        details.extend(f"  - {m}" for m in missing)
    elif len(unique_values) > 1:
        details.append(f"三處日期不一致：{values}")
    else:
        details.append("三處日期一致")

    report.add("檢查 2：日期三處同步（dates）", passed, details)


# ---------------------------------------------------------------------------
# 檢查 3：charset meta（charset）
# ---------------------------------------------------------------------------

def check_charset(report: Report):
    targets = [CURRENT_HTML, EVOLUTION_HTML]
    charset_re = re.compile(r'<meta\s+charset\s*=\s*["\']utf-8["\']', re.IGNORECASE)

    missing = []
    for path in targets:
        if not path.exists():
            missing.append(f"{rel(path)}：檔案不存在")
            continue
        text = read_text(path)
        if not charset_re.search(text):
            missing.append(f"{rel(path)}：缺少 <meta charset=\"utf-8\">")

    passed = not missing
    details = [f"檢查 {len(targets)} 份 HTML"]
    if missing:
        details.extend(f"  - {m}" for m in missing)
    else:
        details.append("皆含 <meta charset=\"utf-8\">")
    report.add("檢查 3：charset meta（charset）", passed, details)


# ---------------------------------------------------------------------------
# 檢查 4：CSS token 存在性（css_tokens）
# ---------------------------------------------------------------------------

def extract_root_tokens(css_text: str) -> set[str]:
    m = re.search(r":root\s*\{(.*?)\}", css_text, re.DOTALL)
    if not m:
        return set()
    block = m.group(1)
    return set(re.findall(r"(--[a-zA-Z0-9-]+)\s*:", block))


def extract_used_tokens(html_text: str) -> set[str]:
    return set(re.findall(r"var\((--[a-zA-Z0-9-]+)\)", html_text))


def check_css_tokens(report: Report):
    if not ARCH_CSS.exists():
        report.add(
            "檢查 4：CSS token 存在性（css_tokens）",
            False,
            [f"{rel(ARCH_CSS)} 不存在"],
        )
        return

    defined = extract_root_tokens(read_text(ARCH_CSS))
    targets = [CURRENT_HTML, EVOLUTION_HTML]

    missing = []
    total_used = 0
    for path in targets:
        if not path.exists():
            missing.append(f"{rel(path)}：檔案不存在")
            continue
        used = extract_used_tokens(read_text(path))
        total_used += len(used)
        undefined = sorted(t for t in used if t not in defined)
        for t in undefined:
            missing.append(f"{rel(path)}：使用 `var({t})` 但 {rel(ARCH_CSS)} 的 :root 未定義")

    passed = not missing
    details = [f"architecture.css :root 定義 {len(defined)} 個 token；兩份 HTML 共用到 {total_used} 個引用"]
    if missing:
        details.append(f"未定義 token {len(missing)} 處：")
        details.extend(f"  - {m}" for m in missing)
    else:
        details.append("使用到的 token 皆有定義")
    report.add("檢查 4：CSS token 存在性（css_tokens）", passed, details)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    stream = _stdout()
    report = Report()

    check_sources(report)
    check_dates(report)
    check_charset(report)
    check_css_tokens(report)

    stream.write(report.render() + "\n")
    stream.flush()

    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
