#!/usr/bin/env python3
"""開放迴路掃描——每週跑一次，把「悄悄沒收尾」的東西攤出來。

檢查五類開放迴路（每類的處理節奏各自不同，本腳本只彙整「可見性」，不合併處理）：
  1. 未 commit 的「實質改動」（code / 規則 / wiki / 腳本），排除每日變動的 data 檔
  2. `docs/workaround-register.md`「進行中」表格裡逾複查日的 workaround
  3. 懸置標記逾期佇列 ＋ 舊語法盲區（處理端：`/wiki-lint` 5c）
  4. `wiki/reader-notes.md` 的 ⏳ 待處理（處理端：`/wiki-weekly-review`）
  5. `wiki/feature-radar.md` 的 ⏳ 觀望（逾期判定端：`/wiki-lint` 5a 的 90 天規則）

為何 3–5 要納入（2026-08-29 新增）：本腳本原本只算前兩類，報「合計開放迴路 7 個」，
而同日實測後三類合計約 222 筆——**唯一的彙整端低報 30 倍**。這與 `--queue` 改版前
「只印存量、不印流量」是同一種病：看得到的地方沒有積壓，積壓都在看不到的地方。
納入的是**數字與最舊年齡**，不是處理權——每類仍由各自的流程消化。

不呼叫任何 LLM，純本地 git + 檔案解析（符合本專案無 API key 前提）。
用法：python scripts/open_loops.py
"""
import io
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

def _use_utf8_stdout() -> None:
    """Windows 主控台預設 cp950，印不出 ⚠️ 會 UnicodeEncodeError——而這個腳本正是
    「有逾期 workaround 時才印 ⚠️」，等於愈該示警愈會當掉（2026-08-01 實際踩到：
    掃描在列出 4 筆逾期項目的當下 traceback 中止）。

    **只在 `__main__` 路徑呼叫，不可放模組層級**（理由見 `daily_health_check.py`
    同名函式；`scripts/test_no_module_level_stdout_swap` 會擋回來）。
    """
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parent.parent          # CLAUDE_NEWS/
REGISTER = REPO / "docs" / "workaround-register.md"
READER_NOTES = REPO / "wiki" / "reader-notes.md"
FEATURE_RADAR = REPO / "wiki" / "feature-radar.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))

# 與 SessionStart hook 一致的排除清單：每日正常變動的 data / 本機 junk / 父層
_EXCLUDE = re.compile(
    r"gathered_items\.json|emitted_items\.json|seen_urls\.json|"
    r"\.stackdump|settings\.local\.json|\.obsidian/|\.gitignore|\.canvas|smart-connections"
)


def uncommitted_real_changes() -> list[str]:
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
    except Exception as e:
        return [f"(git status 失敗：{e})"]
    return [ln for ln in out.splitlines() if ln.strip() and not _EXCLUDE.search(ln)]


def overdue_workarounds(today: date) -> list[str]:
    """回傳『進行中』表格中複查日 <= today 的列摘要。"""
    if not REGISTER.exists():
        return []
    text = REGISTER.read_text(encoding="utf-8")
    # 只看「## 進行中」到下一個 「## 」之間
    m = re.search(r"##\s*進行中\s*(.*?)(?:\n##\s|\Z)", text, re.S)
    if not m:
        return []
    overdue = []
    for line in m.group(1).splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("繞路內容", "---") or set(cells[0]) <= {"-", ":"}:
            continue
        d = re.search(r"(\d{4})-(\d{2})-(\d{2})", cells[3])
        if not d:
            continue
        due = date(int(d.group(1)), int(d.group(2)), int(d.group(3)))
        if due <= today:
            desc = cells[0][:60]
            overdue.append(f"複查日 {due.isoformat()}（逾 {(today - due).days} 天）：{desc}")
    return overdue


def pending_marker_backlog(today: date) -> tuple[int, int, int]:
    """(逾期筆數, 舊語法盲區筆數, 最久逾期天數)。處理端是 `/wiki-lint` 5c，本處只報數。

    直接沿用 check_pending_markers 的解析，不自己再寫一套——同一個事實兩套解析
    必然漂移（`_legacy_by_page` 的 docstring 記過同型教訓）。
    """
    try:
        import check_pending_markers as cpm
    except Exception:
        return (0, 0, 0)
    try:
        entries = cpm._overdue_entries(cpm.WIKI_DIR, today)
        legacy = sum(n for _, n in cpm._legacy_by_page(cpm.WIKI_DIR))
        oldest = max((e[1] for e in entries), default=0)
        return (len(entries), legacy, oldest)
    except Exception:
        return (0, 0, 0)


def reader_notes_pending(today: date) -> list[str]:
    """`- [⏳] YYYY-MM-DD｜…` 的待處理項，附放置天數。

    reader-notes 的 ⏳ 沒有期限規則（feature-radar 的 ⏳ 有 90 天，見
    `.claude/rules/wiki-ingest-features.md`「⏳ 觀望是有期限的判斷，不是停車場」）。
    在補上規則之前，至少讓它的年齡每週被看見一次。
    """
    if not READER_NOTES.exists():
        return []
    rows = []
    for line in READER_NOTES.read_text(encoding="utf-8").splitlines():
        m = re.match(r"-\s*\[⏳\]\s*(\d{4})-(\d{2})-(\d{2})", line)
        if not m:
            continue
        d = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        desc = line.split("｜")[-1][:50] if "｜" in line else line[:50]
        rows.append((today - d).days)
        rows[-1] = f"放置 {(today - d).days} 天（{d.isoformat()}）：{desc}"
    return rows


def feature_radar_watching() -> int:
    """feature-radar 標 ⏳ 的條目數。逾期判定（>90 天）屬 `/wiki-lint` 5a，此處不重複實作。"""
    if not FEATURE_RADAR.exists():
        return 0
    return FEATURE_RADAR.read_text(encoding="utf-8").count("⏳")


def main() -> int:
    _use_utf8_stdout()
    today = date.today()
    changes = uncommitted_real_changes()
    overdue = overdue_workarounds(today)

    print(f"=== 開放迴路掃描（{today.isoformat()}）===\n")

    print(f"[1] 未 commit 的實質改動：{len(changes)} 個")
    for ln in changes:
        print(f"    {ln}")
    if not changes:
        print("    ✅ 無——實質改動都已收尾")

    print(f"\n[2] 逾複查日的 workaround：{len(overdue)} 個")
    for ln in overdue:
        print(f"    ⚠️ {ln}")
    if not overdue:
        print("    ✅ 無逾期繞路")

    pend_overdue, pend_legacy, pend_oldest = pending_marker_backlog(today)
    print(f"\n[3] 懸置標記：逾期 {pend_overdue} 筆（最久逾 {pend_oldest} 天）＋ 舊語法盲區 {pend_legacy} 筆")
    if pend_overdue or pend_legacy:
        print("    → 處理端：`/wiki-lint` 5c（Lane A/B 兩條分流）；盲區須先由記者輪回填才進得了佇列")
        print("    → 明細與產消速率：python scripts/check_pending_markers.py --queue")
    else:
        print("    ✅ 無逾期懸置")

    notes = reader_notes_pending(today)
    print(f"\n[4] reader-notes 待處理（⏳）：{len(notes)} 個")
    for ln in notes:
        print(f"    ⚠️ {ln}")
    if not notes:
        print("    ✅ 無待處理")

    radar = feature_radar_watching()
    print(f"\n[5] feature-radar 觀望中（⏳）：{radar} 條")
    if radar:
        print("    → 逾期判定（發布逾 90 天者三選一處置）屬 `/wiki-lint` 5a，本處只報總量")

    open_count = len(changes) + len(overdue)
    total_backlog = open_count + pend_overdue + pend_legacy + len(notes) + radar
    print(f"\n=== 需收尾（前兩類）：{open_count} 個｜全庫積壓合計：{total_backlog} 筆 ===")
    print("    兩個數字刻意分開：前者是「這次該做完的」，後者是「還欠著的」。"
          "只看前者會像 2026-08-29 之前那樣——報 8 個，實際欠 200+ 筆。")
    return 1 if open_count else 0


if __name__ == "__main__":
    sys.exit(main())
