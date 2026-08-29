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
_DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
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
            desc = cells[0][:60] + ("…" if len(cells[0]) > 60 else "")
            overdue.append(f"複查日 {due.isoformat()}（逾 {(today - due).days} 天）：{desc}")
    return overdue


class PendingScanUnavailable(RuntimeError):
    """懸置掃描不可用。刻意不吞——見 pending_marker_backlog。"""


def pending_marker_backlog(today: date) -> tuple[int, int, int]:
    """(逾期筆數, 舊語法盲區筆數, 最久逾期天數)。處理端是 `/wiki-lint` 5c，本處只報數。

    走上游的公開契約 `backlog_summary()`，不自己再寫一套解析——同一事實兩套解析
    必然漂移。契約寫在擁有資料的那一側，上游重構時看得到有外部消費者。
    """
    try:
        import check_pending_markers as cpm
        return cpm.backlog_summary(today=today)
    except Exception as e:
        # 不可靜默回 0——那會讓掃描壞掉看起來像「很乾淨」，正是本腳本要治的病。
        raise PendingScanUnavailable(str(e)) from e


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
        rows.append(f"放置 {(today - d).days} 天（{d.isoformat()}）：{desc}")
    return rows


def feature_radar_watching(today: date) -> tuple[int, int]:
    """(觀望中條目數, 其中逾 90 天者)。只解析「功能全覽表」的列，不做全文 count。

    2026-08-29 review 實測：`text.count("⏳")` 得 23，真實只有 13——
    9 條同時出現在詳細條目標頭與全覽表（跨層重複）、1 個是圖例列。
    一支專門防低報的腳本在這一類**高報 77%**，而且吃進了總計。

    只有「逾 90 天」那個數字進總計：依 `.claude/rules/wiki-ingest-features.md`
    「⏳ 觀望是有期限的判斷，不是停車場」，兩天前發布的 ⏳ 不是積壓。

    **這個數字是上界**：純年齡判準分不出「零後續」與「有後續但仍觀望」——
    5a 於 2026-08-28 對 Dreaming 的裁決是「有後續、僅降 1 格」，但它仍逾 90 天。
    要更準需排除條目名帶「無後續報導」以外者，但那是對散文措辭的脆弱耦合，
    刻意不做；讀者把它理解為「至多這麼多」即可。

    用欄位位置（試用價值欄）而非全文比對，措辭漂移（觀望／觀察中）不影響。
    """
    if not FEATURE_RADAR.exists():
        return (0, 0)
    lines = FEATURE_RADAR.read_text(encoding="utf-8").splitlines()
    start = None
    for n, line in enumerate(lines):
        if line.startswith("## ") and "功能全覽表" in line:
            start = n + 1
            break
    if start is None:
        return (0, 0)
    watching = overdue = 0
    for line in lines[start:]:
        if line.startswith("## "):
            break
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0] == "功能" or set(cells[0]) <= {"-", ":"}:
            continue
        if "⏳" not in cells[3]:
            continue
        watching += 1
        d = _DATE_RE.search(cells[1])
        if d and (today - date(int(d.group(1)), int(d.group(2)), int(d.group(3)))).days > 90:
            overdue += 1
    return (watching, overdue)

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

    try:
        pend_overdue, pend_legacy, pend_oldest = pending_marker_backlog(today)
        pend_broken = None
    except PendingScanUnavailable as e:
        pend_overdue = pend_legacy = pend_oldest = 0
        pend_broken = str(e)
    if pend_broken is not None:
        print("\n[3] 懸置標記：❌ 掃描失敗，數量未知")
    else:
        print(f"\n[3] 懸置標記：逾期 {pend_overdue} 筆（最久逾 {pend_oldest} 天）＋ 舊語法盲區 {pend_legacy} 筆")
    if pend_broken is not None:
        print(f"    ❌ 掃描失敗，此類積壓未知（不可當成 0）：{pend_broken[:80]}")
    elif pend_overdue or pend_legacy:
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

    radar_all, radar_overdue = feature_radar_watching(today)
    print(f"\n[5] feature-radar 觀望中（⏳）：{radar_all} 條，其中逾 90 天 {radar_overdue} 條（上界，含已由 5a 處置者）")
    if radar_overdue:
        print("    → 逾 90 天者依 `/wiki-lint` 5a 三選一處置，不得留原狀；未逾期者不算積壓")

    open_count = len(changes) + len(overdue)
    # 三個數字回答三個不同的問題：
    #   需收尾   = 這次該做完的（前兩類）
    #   已跳票   = 逾自身期限的承諾，五類共用「件」為單位、同質可追蹤
    #   存量遷移 = 舊語法盲區，是格式債、沒對讀者承諾過什麼，另計不入總
    # 2026-08-29 review：原本只印一個 229，其中 195 由盲區＋逾期懸置主導，
    # 其餘四類全部歸零總數也只掉到 34——那不是彙整，是「盲區筆數＋雜訊」。
    overdue_promises = len(overdue) + len(notes) + radar_overdue
    if pend_broken is None:
        overdue_promises += pend_overdue
        prefix, legacy_txt = "", f"{pend_legacy} 筆"
    else:
        prefix, legacy_txt = "≥ ", "未知"
    print(f"\n=== 需收尾（前兩類）：{open_count} 個"
          f"｜已跳票（逾自身期限）：{prefix}{overdue_promises} 筆"
          f"｜存量遷移（舊語法盲區）：{legacy_txt} ===")
    if pend_broken is not None:
        print("    ⚠️ 檔尾數字不含懸置類（掃描失敗）——不可當成 0")
    print("    「需收尾」是這次該做完的；「已跳票」是已逾自身期限的承諾（同質、可追蹤）；"
          "存量遷移是格式債，另計不入總。三者不互斥——逾期 workaround 同時計入前兩者，"
          "不可相加。2026-08-29 之前本腳本只算前兩類，當時報 8 個。")
    return 1 if (open_count or pend_broken is not None) else 0


if __name__ == "__main__":
    sys.exit(main())
