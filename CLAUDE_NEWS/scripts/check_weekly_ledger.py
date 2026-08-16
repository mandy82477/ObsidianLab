"""週報預告帳本一致性檢查。

週報第 (3) 段是一本帳：每期立下可證偽預告，下一期回收。這本帳沒有外部事實來源
（刻意的——markdown 才是事實，web 只是視圖），因此它的完整性必須靠機械比對維持，
否則所有失敗都是靜默的：

  1. 漏收    上期立的預告，下期沒回收 → 該條靜默蒸發（2026-W31 實際發生：三條未結案的
             條目回收一次寫「未定」後就再也沒被提起）
  2. 改判準  回收時把當初的判準改寫成對自己有利的版本 → 帳面永遠好看，讀者無從查證
  3. 殭屍    同一條每期都「未定」，長住帳本卻不產生資訊
  4. 跳期    某週沒跑週報，下期不知道該回收哪一期
  5. 湊數    硬湊條數，混進沒把握怎麼驗的題目

檢查對象是 weekly/ 內**最新兩期**（更早的已凍結，不重複檢查）。
規格見 `.claude/commands/weekly-report.md` 第 (3) 段；欄名與標題為兩者共用錨點。
"""

from __future__ import annotations

import difflib
import io
import re
import sys
from pathlib import Path


def _stdout():
    """Windows 主控台預設 cp950，直接 print 狀態符號會 UnicodeEncodeError（同 check_rules.py）。"""
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout

REPO_ROOT = Path(__file__).resolve().parent.parent
WEEKLY_DIR = REPO_ROOT / "weekly"

RECAP_HEADER_RE = re.compile(r"^\|\s*上週預告\s*\|\s*判準\s*\|\s*本週結果\s*\|\s*$", re.MULTILINE)
FORECAST_HEADER_RE = re.compile(r"^\|\s*類型\s*\|\s*預告\s*\|\s*判準\s*\|\s*$", re.MULTILINE)
RECAP_HEADING_RE = re.compile(r"^###\s*先回收上週（(\d{4}-W\d{2})）", re.MULTILINE)
SEPARATOR_RE = re.compile(r"^\|[-: |]+\|$")

# 結案 vs 未結案：結果欄首字元決定。
# ⏰（到期日未到）算未結案——它必須一路帶到期限那週才結，否則會在中途靜默消失；
# 但它天生就會跨多期，故豁免下方的殭屍規則（到期日本身即內建結案時點）。
CLOSED_MARKS = ("✅", "❌")
OPEN_MARKS = ("⏳", "🟡", "⏰")
ZOMBIE_EXEMPT_MARKS = ("⏰",)

MIN_FORECASTS = 3
MAX_FORECASTS = 6

# 深挖小標必須恰好是 `###`——`scripts/build_web.py` 以 h3 切子區塊，再把「深挖：」
# 那節抽成專屬元件（kicker「深挖專欄 · DEEP DIVE」＋標題＋內文）。寫成 `####` 時
# 子區塊根本不存在，deepDive 變 None，整段內文被靜默併進「討論綜述」，網站上專欄
# 消失且無任何錯誤——2026-08-16 W33 踩過。規格檔的範例原本就寫成 `####`（那是規格
# 文件自己的巢狀深度，輸出檔少一層），W30–W32 三期各自從輸出結構推導出 `###`、
# 沒人回頭改規格，於是錯誤範例活了三週而無人察覺。
DEEPDIVE_HEADING_RE = re.compile(r"^(#{2,6})\s*深挖[：:]\s*(.*)$", re.MULTILINE)
DEEPDIVE_LEVEL = "###"
DEEPDIVE_MIN_CHARS = 800
DEEPDIVE_MAX_CHARS = 1200


def _strip_bold(text: str) -> str:
    return re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text).strip()


def _parse_table(body: str, header_re: re.Pattern) -> list[list[str]]:
    m = header_re.search(body)
    if not m:
        return []
    rows: list[list[str]] = []
    started = False
    for line in body[m.end():].splitlines():
        ls = line.strip()
        if not ls.startswith("|"):
            if started:
                break
            continue
        if SEPARATOR_RE.match(ls):
            started = True
            continue
        if not started:
            continue
        cells = [_strip_bold(c.strip()) for c in ls.strip("|").split("|")]
        if len(cells) >= 3:
            rows.append(cells)
    return rows


def _norm(text: str) -> str:
    """比對用正規化：去空白與全半形括號差異，避免換行/排版差異造成假失敗。"""
    t = re.sub(r"\s+", "", text)
    for a, b in (("（", "("), ("）", ")"), ("／", "/"), ("，", ",")):
        t = t.replace(a, b)
    return t


def _issues() -> list[Path]:
    return sorted(WEEKLY_DIR.glob("[0-9][0-9][0-9][0-9]-W[0-9][0-9].md"))


def check(report: list[str]) -> bool:
    if not WEEKLY_DIR.exists():
        return True  # 尚未啟用週報體裁

    files = _issues()
    if len(files) < 2:
        report.append(f"  ℹ️ 週報僅 {len(files)} 期，無上一期可比對，跳過帳本檢查")
        return True

    prev_f, curr_f = files[-2], files[-1]
    prev_raw = prev_f.read_text(encoding="utf-8-sig")
    curr_raw = curr_f.read_text(encoding="utf-8-sig")
    prev_id, curr_id = prev_f.stem, curr_f.stem

    ok = True

    # ── 1. 跳期：回收小標必須指名實際的上一期 ────────────────────────────────
    m = RECAP_HEADING_RE.search(curr_raw)
    if not m:
        report.append(f"  ❌ {curr_id}：找不到回收小標（需為 `### 先回收上週（{prev_id}）的帳`）")
        ok = False
    elif m.group(1) != prev_id:
        report.append(
            f"  ❌ {curr_id}：回收小標指向 {m.group(1)}，但 weekly/ 內實際的上一期是 {prev_id}"
            f"（跳期未處理，帳會斷）"
        )
        ok = False

    prev_forecasts = _parse_table(prev_raw, FORECAST_HEADER_RE)
    prev_recap = _parse_table(prev_raw, RECAP_HEADER_RE)
    curr_recap = _parse_table(curr_raw, RECAP_HEADER_RE)
    curr_forecasts = _parse_table(curr_raw, FORECAST_HEADER_RE)

    if not curr_recap:
        report.append(f"  ❌ {curr_id}：回收表解析不到任何列（欄名須為 `| 上週預告 | 判準 | 本週結果 |`）")
        return False

    def _pair(forecast: str) -> list[str] | None:
        """把「應收」條目配到回收表的某一列。

        逐字比對太脆——同一條在回收表裡順手縮寫措辭就會誤報漏收；但完全放寬又會讓
        真正的漏收混過去。折衷：先試完全相同，再用相似度／包含關係配對，配到了才
        進一步檢查判準是否被改。配不到才算漏收。
        """
        key = _norm(forecast)
        for row in curr_recap:
            if _norm(row[0]) == key:
                return row
        best, best_ratio = None, 0.0
        for row in curr_recap:
            cand = _norm(row[0])
            if key in cand or cand in key:
                return row
            ratio = difflib.SequenceMatcher(None, key, cand).ratio()
            if ratio > best_ratio:
                best, best_ratio = row, ratio
        return best if best_ratio >= 0.6 else None

    # ── 2. 漏收：上期「新立的」＋「仍未結案的」都必須被回收 ────────────────────
    owed: list[tuple[str, str, str]] = []          # (預告, 判準, 來源)
    for row in prev_forecasts:
        owed.append((row[1], row[2], "上期新立"))
    for row in prev_recap:
        result = row[2]
        if result.startswith(OPEN_MARKS):
            owed.append((row[0], row[1], "上期未結案"))

    for forecast, criterion, origin in owed:
        row = _pair(forecast)
        if row is None:
            report.append(f"  ❌ {curr_id}：漏收（{origin}）「{forecast[:40]}」")
            ok = False
            continue
        # ── 3. 改判準：回收時的判準必須與立案當期逐字相同 ──────────────────
        if _norm(row[1]) != _norm(criterion):
            report.append(
                f"  ❌ {curr_id}：判準遭改寫「{forecast[:30]}」\n"
                f"       立案（{prev_id}）：{criterion[:70]}\n"
                f"       回收（{curr_id}）：{row[1][:70]}"
            )
            ok = False

    # ── 4. 結果欄必須帶狀態符號，未結案者必須寫明續盯去向 ──────────────────────
    for row in curr_recap:
        result = row[2]
        if not result.startswith(CLOSED_MARKS + OPEN_MARKS):
            report.append(
                f"  ❌ {curr_id}：結果欄缺狀態符號（需 ✅／❌／⏰ 結案，或 ⏳／🟡 續盯）"
                f"——「{row[0][:30]}」"
            )
            ok = False
        elif result.startswith(OPEN_MARKS) and "續盯" not in result:
            report.append(
                f"  ❌ {curr_id}：未結案卻未寫續盯去向（需「→ 續盯至 Wnn」）——「{row[0][:30]}」"
            )
            ok = False

    # ── 5. 殭屍：同一條連續兩期未結案 → 應強制結案 ────────────────────────────
    prev_open = {
        _norm(r[0]) for r in prev_recap
        if r[2].startswith(OPEN_MARKS) and not r[2].startswith(ZOMBIE_EXEMPT_MARKS)
    }
    for row in curr_recap:
        if (_norm(row[0]) in prev_open and row[2].startswith(OPEN_MARKS)
                and not row[2].startswith(ZOMBIE_EXEMPT_MARKS)):
            report.append(
                f"  ❌ {curr_id}：殭屍條目——「{row[0][:36]}」連續兩期未結案，"
                f"依規格應強制結案（無結論／降級為未證實）"
            )
            ok = False

    # ── 6. 條數與可查證性 ────────────────────────────────────────────────────
    n = len(curr_forecasts)
    if not (MIN_FORECASTS <= n <= MAX_FORECASTS):
        report.append(f"  ❌ {curr_id}：新開 {n} 條，規格為 {MIN_FORECASTS}–{MAX_FORECASTS} 條（寧缺勿湊）")
        ok = False
    missing_probe = [r[1] for r in curr_forecasts if "查證：" not in r[2]]
    if missing_probe:
        for forecast in missing_probe:
            report.append(
                f"  ❌ {curr_id}：判準缺查證線索（結尾需「｜查證：關鍵字1、關鍵字2」）——「{forecast[:36]}」"
            )
        ok = False

    if ok:
        report.append(
            f"  ✅ {curr_id} ← {prev_id}：回收 {len(curr_recap)} 筆、應收 {len(owed)} 筆全數到位；"
            f"判準無改寫；新開 {n} 條均帶查證線索"
        )
    return ok


def check_deepdive(report: list[str]) -> bool:
    """深挖專欄的小標層級與篇幅。

    層級錯誤會讓網站上的專欄元件整個消失（見 DEEPDIVE_HEADING_RE 註解），故硬擋；
    篇幅只 WARN——那是編輯判斷，且本專案不用「數字只准往某方向走」的機械棘輪。
    """
    ok = True
    for path in _issues():
        text = path.read_text(encoding="utf-8-sig")
        matches = DEEPDIVE_HEADING_RE.findall(text)
        if not matches:
            # 規格允許「查無不補位」時整段省略，故不硬擋，只提醒。
            report.append(f"  ⚠️ {path.stem}：找不到深挖小標（若為本週略過，忽略此提醒）")
            continue
        if len(matches) > 1:
            report.append(f"  ❌ {path.stem}：出現 {len(matches)} 個深挖小標，專欄應只有一個")
            ok = False
        level, title = matches[0]
        if level != DEEPDIVE_LEVEL:
            report.append(
                f"  ❌ {path.stem}：深挖小標為 `{level}`，必須是 `{DEEPDIVE_LEVEL}`"
                f"——build_web.py 以 h3 切子區塊，其他層級會讓專欄元件整個不渲染、"
                f"內文被靜默併進「討論綜述」"
            )
            ok = False

        start = text.index(matches[0][1]) if matches[0][1] else 0
        body = re.split(r"^#{2,3}\s", text[start:], maxsplit=1, flags=re.MULTILINE)[0]
        n = len(re.sub(r"\s", "", body))
        if not (DEEPDIVE_MIN_CHARS <= n <= DEEPDIVE_MAX_CHARS):
            report.append(
                f"  ⚠️ {path.stem}：深挖 {n} 字，規格為 "
                f"{DEEPDIVE_MIN_CHARS}–{DEEPDIVE_MAX_CHARS}（提醒，不擋）"
            )
    return ok


def main() -> int:
    report: list[str] = []
    ok = check(report)
    ok = check_deepdive(report) and ok
    out = _stdout()
    print("# check_weekly_ledger.py 報告\n", file=out)
    print("\n".join(report) if report else "  （無週報）", file=out)
    print(file=out)
    print("狀態：" + ("✅ 週報帳本一致" if ok else "❌ 週報帳本有缺口"), file=out)
    out.flush()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
