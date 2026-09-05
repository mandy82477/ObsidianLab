"""feature-radar 索引層對帳：當月詳細條目 ↔ 全覽表列。

**為什麼需要機械檢查**

`wiki/feature-radar.md` 的 `## 📋 功能全覽表` 與 `## 🆕 最新功能（YYYY-MM）` 是同一件事的
兩個入口：表是掃描用的索引，詳細條目是內文。只寫詳細條目不補表列，該功能在索引上等於
不存在——2026-08-09 讀者回報：08 月 6 條詳細條目只有 4 條進表，漏的正是跨 session 訊息
互通與 Auto 模式預設化，當月最重要的兩條，且雙雙已進「本週推薦」與「⏰ 倒數中」，唯獨
索引查無。

規則已寫進 `.claude/rules/wiki-ingest-features.md`，但當初失敗的正是「靠記者記得補」這一層，
所以再補一道機械檢查。

**只對帳當月**：舊月份的詳細條目會被封存或裁撤（見 `feature-radar-archive-*.md`），
表列則長期保留，因此舊月份表列多於詳細條目屬正常，不是缺漏。

用法：
    python scripts/check_feature_radar.py              # 以今天所屬月份對帳
    python scripts/check_feature_radar.py 2026-08-09   # 指定日期（測試用）
"""

from __future__ import annotations

import io
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RADAR = REPO_ROOT / "wiki" / "feature-radar.md"

TABLE_HEADER_RE = re.compile(r"^##\s+📋\s+功能全覽表")
MONTH_SECTION_RE = re.compile(r"^##\s+🆕\s+最新功能（(\d{4}-\d{2})）")
# 表列的發布日期欄：允許「2026-08-14 生效（08-07 公告）」這類未生效寫法
ROW_DATE_RE = re.compile(r"\|\s*(\d{4}-\d{2})-\d{2}[^|]*\|")

# 熱度／試用價值單一家守門（2026-09-06）：只住 ## 📋 功能全覽表，詳細條目標頭與
# 推薦節不得再複製一份——範圍寫死兩條，不可全檔搜「熱度 🔥」（會誤中 ## 評分說明 圖例）。
DETAIL_HEADER_RE = re.compile(r"^\*\*發布：\*\*")
RECOMMEND_SECTION_RE = re.compile(r"^##\s+⭐")


def check_hotness_single_home(raw: str) -> list[str]:
    """回傳違規訊息列表：detail-entry 標頭或「本週推薦」節內出現熱度副本。"""
    violations: list[str] = []
    lines = raw.split("\n")

    in_recommend = False
    for i, line in enumerate(lines, start=1):
        if line.startswith("## "):
            in_recommend = bool(RECOMMEND_SECTION_RE.match(line))
            continue

        if DETAIL_HEADER_RE.match(line) and "**熱度：**" in line:
            violations.append(f"  行 {i}：詳細條目標頭仍含 **熱度：**（應只住全覽表）：{line.strip()}")

        if in_recommend and "熱度 🔥" in line:
            violations.append(f"  行 {i}：「## ⭐」節內出現「熱度 🔥」副本（應只住全覽表）：{line.strip()}")

    return violations


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def parse(raw: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    """回傳 (全覽表各月列數, 各月詳細條目標題)。"""
    lines = raw.split("\n")

    table_rows: dict[str, int] = {}
    details: dict[str, list[str]] = {}

    in_table = False
    cur_month: str | None = None

    for line in lines:
        if TABLE_HEADER_RE.match(line):
            in_table, cur_month = True, None
            continue

        m = MONTH_SECTION_RE.match(line)
        if m:
            in_table, cur_month = False, m.group(1)
            details.setdefault(cur_month, [])
            continue

        # 其他 h2 結束當前區塊
        if line.startswith("## "):
            in_table, cur_month = False, None
            continue

        if in_table and line.startswith("|") and "**" in line:
            dm = ROW_DATE_RE.search(line)
            if dm:
                table_rows[dm.group(1)] = table_rows.get(dm.group(1), 0) + 1

        if cur_month and line.startswith("### "):
            details[cur_month].append(line[4:].strip())

    return table_rows, details


def main(argv: list[str]) -> int:
    stream = _stdout()

    if not RADAR.exists():
        stream.write(f"WARN: {RADAR} 不存在，跳過 feature-radar 對帳\n")
        stream.flush()
        return 0

    today = date.fromisoformat(argv[1]) if len(argv) > 1 else date.today()
    month = today.strftime("%Y-%m")

    raw = RADAR.read_text(encoding="utf-8-sig")
    table_rows, details = parse(raw)

    hotness_violations = check_hotness_single_home(raw)
    if hotness_violations:
        stream.write("\n[熱度單一家] feature-radar 出現熱度／試用價值副本：\n")
        for v in hotness_violations:
            stream.write(v + "\n")
        stream.write(
            "  修法：熱度與試用價值只寫在 ## 📋 功能全覽表；詳細條目標頭只留「發布」與「狀態」，\n"
            "        推薦節不寫熱度括號（.claude/rules/wiki-ingest-features.md §7(a)）\n"
        )
        stream.flush()
        return 1

    n_detail = len(details.get(month, []))
    n_rows = table_rows.get(month, 0)

    # 當月還沒有任何新功能是正常的（月初、或整月無官方發布）
    if n_detail == 0 and n_rows == 0:
        stream.write(f"OK: feature-radar 對帳通過（{month} 當月尚無新功能條目）\n")
        stream.flush()
        return 0

    if n_detail == n_rows:
        stream.write(
            f"OK: feature-radar 對帳通過（{month}：詳細條目 {n_detail} 條 = 全覽表 {n_rows} 列）\n"
        )
        stream.flush()
        return 0

    stream.write(
        f"\n[索引缺漏] feature-radar {month}：詳細條目 {n_detail} 條，"
        f"全覽表僅 {n_rows} 列\n"
    )
    for title in details.get(month, []):
        stream.write(f"  - 詳細條目：{title}\n")
    stream.write(
        "  修法：詳細條目與全覽表列必須一一對應。缺列 → 依 "
        ".claude/rules/wiki-ingest-features.md\n"
        "        「新條目必須同時補全覽表一列」補上（五欄，依發布日期插入，熱度／試用價值\n"
        "        須與詳細條目標頭逐字一致）；表列多於詳細條目 → 確認是否誤把舊月份條目\n"
        "        寫進當月區塊\n"
    )
    stream.flush()
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
