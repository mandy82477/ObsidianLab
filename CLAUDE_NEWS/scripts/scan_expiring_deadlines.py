"""到期前強制官方複查的偵測器。

`feature-radar.md` 的「⏰ 倒數中」與 `entities/pricing.md` 的「⏰ … 到期」是本庫
對讀者做的**時間承諾**：到了那天，事情會變。但截止日寫下去之後，沒有任何機制
會在它到期前回頭問一次「這個日期還算數嗎」。

2026-08-10 官方把 Claude Sonnet 5 的 $2/$10 永久化、取消 9/1 漲至 $3/$15 的計畫。
本庫 12 個來源 16 天零覆蓋，`entities/pricing` 的「⏰ 2026-08-31 到期」倒數就這樣
掛到剩 5 天才被人工發現——期間 `feature-radar`、`model-comparison`、
`entities/sonnet-5` 同步誤導，讀者會據以做錯誤的成本決策。

偵測器本身不查證（本檔無網路存取，也不該有）。它只回答一個問題：**哪些截止日
即將到期或已過期，需要主編拿 WebFetch 去官方原文確認一次。** 查證是主編層的事，
和 `scan_pending_verifications.py` 的分工一致。

用法：
    python scripts/scan_expiring_deadlines.py [--days 7] [--today YYYY-MM-DD]

exit code 恆為 0——這是報告工具，不是閘門。有無命中由呼叫端判讀。
"""
import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki"

# 預設在到期前幾天開始要求複查。7 天的理由：官方變動到本庫察覺的實測延遲是
# 26–30 小時，週更 lint 的間隔是 7 天——比 7 天短會讓週更路徑接不到。
DEFAULT_WINDOW_DAYS = 7

# 已查證過的截止日，多久內不再重複要求複查。沒有這道，掃描器會無視自己的答案：
# 頁面上明明寫著「2026-08-28 查官方原文複查，日期仍有效」，它照樣天天要求再查
# 一次，直到到期為止——一個永遠在響的警報會把讀者訓練成整段跳過（2026-08-29
# review 發現）。
VERIFIED_QUIET_DAYS = 14

_DATE_RE = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")

# feature-radar「⏰ 倒數中」表格列：| **YYYY-MM-DD** | 事件 | 到期後 | 你該做的決定 |
_RADAR_ROW_RE = re.compile(r"^\|\s*\*\*(20\d{2}-\d{2}-\d{2})\*\*\s*\|(.+)$")

# 散文型：- **⏰ YYYY-MM-DD 到期（…）｜標題**：內文
_PROSE_RE = re.compile(r"⏰\s*(20\d{2}-\d{2}-\d{2})")


def _parse_date(s: str) -> date | None:
    m = _DATE_RE.search(s)
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def _recently_verified(line: str, deadline: date, today: date) -> bool:
    """這一行是否已標明近期查證過？

    判準刻意寬鬆——只要行內有「複查／查證」字樣，且帶一個非截止日本身、落在近
    VERIFIED_QUIET_DAYS 天內的日期。本工具是提醒而非閘門，寧可漏提醒也不要天天
    重複要求做過的事。
    """
    if "複查" not in line and "查證" not in line:
        return False
    for y, m, d in _DATE_RE.findall(line):
        try:
            seen = date(int(y), int(m), int(d))
        except ValueError:
            continue
        if seen != deadline and 0 <= (today - seen).days <= VERIFIED_QUIET_DAYS:
            return True
    return False


def _first_cell(row: str) -> str:
    """表格列的第二欄（事件描述），用來讓報告看得懂是哪一筆。"""
    cells = [c.strip() for c in row.split("|") if c.strip()]
    return cells[0] if cells else ""


def collect(wiki_dir: Path, today: date | None = None) -> list[dict]:
    """掃出全庫所有帶截止日的承諾。

    刻意掃整個 wiki/ 而不是寫死兩個檔名：截止日會擴散到別的頁（模型免費期、
    政策生效日），寫死檔名的偵測器只看得到今天想得到的那兩頁。
    """
    today = today or date.today()
    found: list[dict] = []
    for path in sorted(wiki_dir.rglob("*.md")):
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel.endswith("wiki/log.md"):
            continue  # 日誌記的是歷史，不是對讀者的承諾
        try:
            lines = path.read_text(encoding="utf-8").split("\n")
        except Exception:
            continue
        for n, line in enumerate(lines, 1):
            m = _RADAR_ROW_RE.match(line)
            if m:
                d = _parse_date(m.group(1))
                if d:
                    found.append({"date": d, "file": rel, "line": n,
                                  "what": _first_cell(m.group(2))[:110],
                                  "verified": _recently_verified(line, d, today)})
                continue
            m = _PROSE_RE.search(line)
            if m:
                d = _parse_date(m.group(1))
                if d:
                    # 從 ⏰ 的位置起擷取，不是行首——同一行可能先講別的事，行首
                    # 文字會讓報告指向錯的議題（2026-08-28 首版即踩到）
                    found.append({"date": d, "file": rel, "line": n,
                                  "what": line[m.start():].strip()[:110],
                                  "verified": _recently_verified(line, d, today)})
    # 抑制以「截止日」為單位，不是以行為單位：同一個日期常散在 3 處以上，查證的
    # 是那個日期而不是某一行，只抑制帶註記的那行等於留著交叉引用行天天叫。
    verified_dates = {x["date"] for x in found if x["verified"]}
    return [x for x in found if x["date"] not in verified_dates]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=DEFAULT_WINDOW_DAYS)
    ap.add_argument("--today", default="")
    args = ap.parse_args()

    today = _parse_date(args.today) or date.today()
    horizon = today + timedelta(days=args.days)

    items = collect(WIKI_DIR, today)
    overdue = sorted([x for x in items if x["date"] < today], key=lambda x: x["date"])
    due = sorted([x for x in items if today <= x["date"] <= horizon], key=lambda x: x["date"])
    later = [x for x in items if x["date"] > horizon]

    print(f"# scan_expiring_deadlines.py（{today.isoformat()}，視窗 {args.days} 天）\n")
    print(f"  掃出 {len(items)} 筆截止日 → 已過期 {len(overdue)}／{args.days} 天內到期 "
          f"{len(due)}／尚遠 {len(later)}\n")

    if not overdue and not due:
        print("無需複查的截止日。")
        return 0

    print("**需主編拿 WebFetch 查官方原文確認一次**（記者無 web 工具，不可自行推斷）：\n")
    for label, rows in (("🔴 已過期", overdue), ("🟠 即將到期", due)):
        if not rows:
            continue
        by_date: dict = {}
        for x in rows:
            by_date.setdefault(x["date"], []).append(x)
        print(f"### {label}（{len(by_date)} 個截止日、{len(rows)} 處引用）")
        for d in sorted(by_date):
            delta = (d - today).days
            when = f"逾期 {-delta} 天" if delta < 0 else (f"剩 {delta} 天" if delta else "今日到期")
            group = by_date[d]
            print(f"- `{d}`（{when}）——{len(group)} 處：")
            for x in group:
                print(f"    - {x['file']}:{x['line']}｜{x['what']}")
        print()

    print("> 查證後三選一：日期仍有效 → 不動；已延長 → 更新截止日並記事件；"
          "已作廢／永久化 → 移除倒數並回掃全庫引用方（同 `/wiki-lint` 5c 的回掃紀律）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
