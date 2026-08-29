#!/usr/bin/env python3
"""懸置標記語法檢查器 — 388 筆舊字樣回填為新語法時的每批驗收工具。

語法規格見 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節，解析邏輯全部
複用 `scripts/pending_markers.py`（`PENDING_RE`／`SHORT_RE`／`QDEF_RE`／
`iter_pending()`／`probe_too_weak()`／`wikilink_target()` 等），本檔不重新發明
parser，只做「這筆標記合不合規格」的判定。

用法：
    python scripts/check_pending_markers.py            # 全庫語法檢查
    python scripts/check_pending_markers.py --queue     # 逾期佇列（供 5c 用）

已掛進 `scripts/run_tests.py`（回填完成、全庫 0 FAIL 後掛載），亦可獨立執行供單批
回填後的手動驗收。

檢查項對照 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節：

  1. 語法完整性（FAIL）   標記日為合法 ISO 日期且 ≤ 今日；複查日（若有）晚於標記日；
                          探針至少 1 個非空
  2. 符號/類別詞一致（FAIL） ❓↔待查證、🔎↔查無官方，兩者是各自獨立的 regex 群組，
                          規格要求一一對應，`SYM_TO_KIND` 之外的組合視為語法錯誤
  3. 排版正規式（FAIL）   `**待查證（標` / `**查無官方（標`——括號誤寫在粗體內，
                          PENDING_RE 吃不到，得用獨立 regex 才抓得到
  4. 探針品質（FAIL）     每個探針過 `probe_too_weak()`（過寬詞／長度地板）
  5. wikilink 探針目標存在（FAIL） `wikilink_target()` 解出的頁面必須在 wiki/ 下實際存在
  6. ⟨Q-nn⟩ 雙向對帳（FAIL） 表格短標記 (SHORT_RE) 與細節區定義 (Marker.qid) 一一對應，
                          同頁 qid 不重複
  6b. 探針偵測力（FAIL／WARN）`[加入: 2026-08-10]` 用 `detective_aliases()`（與
                          scanner 共用同一份判定）算出每筆標記「有非空偵測別名的
                          探針數」——0 個 FAIL（整組探針無偵測力，樞紐頁 wikilink
                          與過寬詞不計）；探針數 >1 但偵測力只剩 1 個時併入下方
                          檢查 7 的 WARN
  7. 探針數不足（WARN）   單探針、非 wikilink、長度 < 6（含 6b 併入的多探針
                          僅剩 1 個有偵測力的情形）
  8. 語意反轉殘留（WARN） 標記同行出現「解除／結案／轉為」+ ✅
  9. 逾期（WARN，明確不得 FAIL） 複查日（或標記日+14 天）≤ 今日——專案拒絕機械棘輪，
                          見 `scripts/gate_web_build.py` 的註解哲學：逾期是排程訊號，
                          不是語法錯誤，FAIL 會逼記者為了轉綠而亂改標記
  10. 存量殘餘（只印數字，不判定） `iter_legacy()` 掃到的舊字樣筆數，供回填進度追蹤

原計畫的檢查「命中未消費」依賴每日掃描器產生的 jsonl 對照當日日報，該掃描器尚未
上線，本檔跳過，留待掃描器上線後另補。
"""
from __future__ import annotations

import io
import re
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pending_markers import (  # noqa: E402
    Doc, WIKI_DIR, detective_aliases, iter_legacy, iter_pending,
    probe_is_wikilink, probe_too_weak, wikilink_target, wiki_pages,
    SHORT_RE, SYM_TO_KIND,
)

REVIEW_DEFAULT_DAYS = 14
QUEUE_LIMIT = 5  # Lane B（本輪額度 5）需 web 查證；四處同步見 .claude/review-registry.json
SIGNAL_LIMIT = 10  # Lane A（本輪額度 10）已有日報訊號；四處同步見 .claude/review-registry.json
RATE_WINDOW_DAYS = 7  # 產消對帳的回看窗口
SHORT_PROBE_LEN = 6

BAD_BRACKET_RE = re.compile(r"\*\*(?:待查證|查無官方)（標")
REVERSAL_CUES = ("解除", "結案", "轉為")


def _stdout():
    """Windows 主控台預設 cp950，直接 print 狀態符號會 UnicodeEncodeError（同 check_weekly_ledger.py）。"""
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def _parse_date(s: str) -> date | None:
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def _slug(path: Path, wiki_dir: Path) -> str:
    try:
        return path.relative_to(wiki_dir).as_posix()[:-3]
    except ValueError:
        return path.stem


def _wikilink_path(target: str, wiki_dir: Path) -> Path:
    return wiki_dir / f"{target}.md"


def _page_report(path: Path, text: str, wiki_dir: Path, today: date) -> tuple[list[str], list[str], int]:
    """回傳 (fail_lines, warn_lines, legacy_count) for a single page。"""
    fails: list[str] = []
    warns: list[str] = []
    slug = _slug(path, wiki_dir)
    doc = Doc(text, path)
    markers = iter_pending(text, path)

    # ── 3. 排版正規式（括號誤寫在粗體內，PENDING_RE 天生吃不到，獨立掃）───────
    for m in BAD_BRACKET_RE.finditer(text):
        if doc.in_code(m.start()) or doc.in_frontmatter(m.start()):
            continue
        fails.append(f"  ❌ {slug}:{doc.line_of(m.start())}：括號誤寫在粗體內（應為「…**（標」不是「**…（標」）")

    for mk in markers:
        loc = f"{slug}:{mk.line}"

        # ── 1. 語法完整性 ──
        marked_date = _parse_date(mk.marked)
        if marked_date is None:
            fails.append(f"  ❌ {loc}：標記日「{mk.marked}」不是合法 ISO 日期")
        elif marked_date > today:
            fails.append(f"  ❌ {loc}：標記日 {mk.marked} 晚於今日（未來日期）")

        if mk.review:
            review_date = _parse_date(mk.review)
            if review_date is None:
                fails.append(f"  ❌ {loc}：複查日「{mk.review}」不是合法 ISO 日期")
            elif marked_date is not None and review_date <= marked_date:
                fails.append(f"  ❌ {loc}：複查日 {mk.review} 未晚於標記日 {mk.marked}")

        probes = mk.probes
        if not probes:
            fails.append(f"  ❌ {loc}：探針為空")

        # ── 2. 符號/類別詞一致 ──
        if SYM_TO_KIND.get(mk.sym) != mk.kind:
            fails.append(f"  ❌ {loc}：符號「{mk.sym}」與類別詞「{mk.kind}」不一致（應為 {SYM_TO_KIND.get(mk.sym)}）")

        # ── 4. 探針品質 + 5. wikilink 探針目標存在 ──
        for probe in probes:
            reason = probe_too_weak(probe)
            if reason:
                fails.append(f"  ❌ {loc}：探針不合格——{reason}")
            target = wikilink_target(probe)
            if target and not _wikilink_path(target, wiki_dir).exists():
                fails.append(f"  ❌ {loc}：wikilink 探針指向不存在的頁面「{target}」")

        # ── 6b. 探針偵測力：與 scanner 共用 detective_aliases() 的判定 ──
        detective = [p for p in probes if detective_aliases(p, wiki_dir)]
        if probes and not detective:
            fails.append(f"  ❌ {loc}：整組探針無偵測力（樞紐頁 wikilink 與過寬詞不計）")

        # ── 7. 探針數不足（WARN）──
        if (len(probes) == 1 and not probe_is_wikilink(probes[0])
                and len(probes[0].strip()) < SHORT_PROBE_LEN):
            warns.append(f"  ⚠️ {loc}：單一探針「{probes[0]}」過短，偵測力不足（建議補第二個或改長）")
        elif len(probes) > 1 and len(detective) == 1 and not probe_is_wikilink(detective[0]):
            warns.append(
                f"  ⚠️ {loc}：探針組實際偵測力僅剩「{detective[0]}」，其餘探針無偵測力（建議補足或改長）"
            )

        # ── 8. 語意反轉殘留（WARN）──
        line = doc.line_text(mk.start)
        if "✅" in line and any(cue in line for cue in REVERSAL_CUES):
            warns.append(f"  ⚠️ {loc}：同行出現「解除／結案／轉為」與 ✅，疑似語意反轉殘留，請確認標記是否早該移除")

        # ── 9. 逾期（WARN，明確不得 FAIL）──
        if marked_date is not None:
            review_date = _parse_date(mk.review) if mk.review else marked_date + timedelta(days=REVIEW_DEFAULT_DAYS)
            if review_date is not None and review_date <= today:
                overdue = (today - review_date).days
                warns.append(f"  ⚠️ {loc}：已逾期 {overdue} 天（複查日 {review_date.isoformat()}）")

    # ── 6. ⟨Q-nn⟩ 雙向對帳 ──
    short_qids = [sm.group("qid") for sm in SHORT_RE.finditer(text)]
    def_qids = [mk.qid for mk in markers if mk.qid]
    short_set, def_set = set(short_qids), set(def_qids)
    for qid in sorted(short_set - def_set):
        fails.append(f"  ❌ {slug}：⟨{qid}⟩ 表格短標記無對應的懸置細節定義")
    for qid in sorted(def_set - short_set):
        fails.append(f"  ❌ {slug}：⟨{qid}⟩ 有懸置細節定義但無表格短標記引用")
    for qid, n in Counter(short_qids).items():
        if n > 1:
            fails.append(f"  ❌ {slug}：⟨{qid}⟩ 表格短標記重複出現 {n} 次")
    for qid, n in Counter(def_qids).items():
        if n > 1:
            fails.append(f"  ❌ {slug}：⟨{qid}⟩ 懸置細節重複定義 {n} 次")

    legacy_count = len(iter_legacy(text, path))
    return fails, warns, legacy_count


def check(report: list[str], wiki_dir: Path | None = None, today: date | None = None) -> bool:
    wiki_dir = wiki_dir or WIKI_DIR
    today = today or date.today()

    ok = True
    total_legacy = 0
    total_markers = 0

    for path in wiki_pages(wiki_dir):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        fails, warns, legacy_count = _page_report(path, text, wiki_dir, today)
        total_legacy += legacy_count
        total_markers += len(iter_pending(text, path))
        if fails:
            ok = False
            report.extend(fails)
        report.extend(warns)

    report.append(
        f"  ℹ️ 存量殘餘：舊字樣（未回填為新語法）共 {total_legacy} 筆，"
        f"新語法標記共 {total_markers} 筆（本項只計數，不影響判定）"
    )
    return ok


def _overdue_entries(wiki_dir: Path, today: date) -> list[tuple[bool, int, str]]:
    """回傳 (有訊欄, 逾期天數, 顯示行) 供排序。"""
    entries: list[tuple[bool, int, str]] = []
    for path in wiki_pages(wiki_dir):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        slug = _slug(path, wiki_dir)
        for mk in iter_pending(text, path):
            marked_date = _parse_date(mk.marked)
            if marked_date is None:
                continue
            review_date = _parse_date(mk.review) if mk.review else marked_date + timedelta(days=REVIEW_DEFAULT_DAYS)
            if review_date is None or review_date > today:
                continue
            overdue = (today - review_date).days
            has_signal = mk.signal is not None
            probes_summary = "、".join(mk.probes[:3])
            line = f"{slug}:{mk.line}｜逾期 {overdue} 天｜標 {mk.marked}｜{probes_summary}"
            entries.append((has_signal, overdue, line))

    # 主鍵（訊欄優先）在 2026-08-29 分流後對 --queue 已無作用（兩條 Lane 各自成組），
    # 保留是因為完整報告仍共用 _overdue_entries；次鍵「逾期天數降序」才是兩邊都要的。
    entries.sort(key=lambda e: (0 if e[0] else 1, -e[1]))
    return entries


def _legacy_by_page(wiki_dir: Path) -> list[tuple[str, int]]:
    """舊字樣標記的頁面分佈，筆數降序。供 --queue 揭露佇列看不到的盲區。

    必須走 wiki_pages() 與 utf-8-sig，與主報告的「存量殘餘」及 _overdue_entries
    同一口徑——自己 rglob 會多算 index/_views 等頁，兩個數字打架
    （2026-08-04 已為同類問題修過一次：iter_legacy 排除清單漏排 SHORT_RE）。
    """
    rows: list[tuple[str, int]] = []
    for path in wiki_pages(wiki_dir):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        n = len(iter_legacy(text, path))
        if n:
            rows.append((_slug(path, wiki_dir), n))
    rows.sort(key=lambda r: (-r[1], r[0]))
    return rows


def _recent_marked(wiki_dir: Path, today: date, days: int) -> int:
    """近 N 天新增的新語法標記筆數。供產消對帳——沒有它，積壓只會安靜長大。"""
    cutoff = today - timedelta(days=days)
    n = 0
    for path in wiki_pages(wiki_dir):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except Exception:
            continue
        for mk in iter_pending(text, path):
            d = _parse_date(mk.marked)
            if d is not None and d > cutoff:
                n += 1
    return n


HISTORY_PATH = WIKI_DIR.parent / "data" / "pending_queue_history.csv"


def _read_last_history(path: Path, today: date) -> tuple[str, int] | None:
    """上一筆快照 (date, total)。查無或格式壞掉一律回 None——診斷用資料不該讓主流程掛掉。"""
    try:
        rows = [r for r in path.read_text(encoding="utf-8").splitlines() if r and not r.startswith("date,")]
    except Exception:
        return None
    # 跳過今日列：5c 步驟 1 本來就會先跑完整報告再跑佇列，操作者改完幾筆再看一次是常態。
    # 不跳過的話基準會變成「今天」，趨勢永遠印（0）——功能自我抵銷。
    rows = [r for r in rows if not r.startswith(today.isoformat() + ",")]
    if not rows:
        return None
    try:
        cells = rows[-1].split(",")
        return cells[0], int(cells[1])
    except Exception:
        return None


def _append_history(path: Path, today: date, total: int, a: int, b: int, added: int) -> None:
    """每輪 append 一列。沒有這個，下週跑同一支腳本仍答不出「比上週好還是壞」——
    而本次改版的起因正是『19 天從 0 長到 51 無人察覺』。"""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        header = "date,total,lane_a,lane_b,added_7d"
        try:
            existing = [r for r in path.read_text(encoding="utf-8").splitlines() if r]
        except Exception:
            existing = []
        existing = [r for r in existing if r != header and not r.startswith(today.isoformat() + ",")]
        rows = [header] + existing + [f"{today.isoformat()},{total},{a},{b},{added}"]
        path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    except Exception:
        pass  # 寫不進去不該擋住報表


def print_queue(out, wiki_dir: Path | None = None, today: date | None = None,
                history_path: Path | None = None) -> None:
    """兩條分流 + 產消對帳。

    為什麼分流（2026-08-29）：原本單一額度 5 筆、排序「訊欄優先」，
    結果**有訊的筆數佔滿全部額度**——而有訊代表記者已在日報找到後續，
    結案**多數可免 web**（仍須逐筆確認日報證據是否真指該事實）。便宜的工作吃光了昂貴查證的配額，
    真正需要 WebFetch 的那批永遠排不進來。一個額度混用兩種成本結構的工作，
    必然被便宜那種佔滿。

    為什麼要有產消對帳：改版前輸出只有「總逾期數」這個存量數字，
    看不出流量。2026-08-29 實測近 7 天新增 24 筆、
    本輪實際可消費 13 筆（A 8＋B 5）——而這件事在輸出裡完全看不到，
    於是 19 天內從 0 長到 51 筆沒有任何人察覺。

    注意本行是**概估**：額度為上限、7 天內建立又已結案者不計入分子。
    """
    wiki_dir = wiki_dir or WIKI_DIR
    today = today or date.today()
    entries = _overdue_entries(wiki_dir, today)
    lane_a = [e for e in entries if e[0]]       # 有訊欄
    lane_b = [e for e in entries if not e[0]]   # 無訊欄
    print("# check_pending_markers.py --queue 逾期佇列\n", file=out)

    print(f"## Lane A（本輪額度 {SIGNAL_LIMIT}）：日報已有後續訊號，多數可免 web——{len(lane_a)} 筆", file=out)
    print("   記者已標 `訊`＝日報有後續。多數可只憑日報收斂，但探針是機械比對、可能假命中——", file=out)
    print("   逐筆確認該日條目是否真指此事實；確認不了就退回 Lane B，不可硬結。處置見 5c 步驟 3 第四列。", file=out)
    for _, _, line in lane_a[:SIGNAL_LIMIT]:
        print(f"  {line}", file=out)
    if not lane_a:
        print("  （無）", file=out)
    elif len(lane_a) > SIGNAL_LIMIT:
        print(f"  … 另 {len(lane_a) - SIGNAL_LIMIT} 筆未顯示", file=out)

    print(file=out)
    print(f"## Lane B（本輪額度 {QUEUE_LIMIT}）：需 WebFetch 官方查證——{len(lane_b)} 筆", file=out)
    print("   需官方一手來源，雲端 egress 封鎖時整個 5c 跳過（含本區）。", file=out)
    for _, _, line in lane_b[:QUEUE_LIMIT]:
        print(f"  {line}", file=out)
    if not lane_b:
        print("  （無）", file=out)
    elif len(lane_b) > QUEUE_LIMIT:
        print(f"  … 另 {len(lane_b) - QUEUE_LIMIT} 筆未顯示", file=out)

    print(file=out)
    print(f"總逾期數：{len(entries)}（Lane A {len(lane_a)}／Lane B {len(lane_b)}）", file=out)

    # 產消對帳：存量數字看不出流量，沒有這段就無法判斷額度夠不夠。
    added = _recent_marked(wiki_dir, today, RATE_WINDOW_DAYS)
    # 兩個不同的數字，別混用：
    #   throughput = 每週產能（能力值），是「會不會結構性落後」的分母
    #   clearable  = 這輪實際消得掉幾筆（受現有積壓限制），只作展示
    # 2026-08-29 review 建議把 min() 當分母，實測會在「積壓 0 但近期有新標記」時
    # 誤報產出過快——積壓空不代表產能是 0，只代表沒東西可消。
    throughput = SIGNAL_LIMIT + QUEUE_LIMIT
    clearable = min(len(lane_a), SIGNAL_LIMIT) + min(len(lane_b), QUEUE_LIMIT)
    net = added - throughput
    verdict = f"淨增 {net} 筆/週" if net > 0 else (f"淨減 {-net} 筆/週" if net < 0 else "打平")
    print(
        f"📊 產消對帳（概估）：近 {RATE_WINDOW_DAYS} 天新增 {added} 筆｜每週產能 {throughput} 筆"
        f"（A {SIGNAL_LIMIT}＋B {QUEUE_LIMIT}）｜本輪實際可消 {clearable} 筆｜{verdict}",
        file=out,
    )
    if net > 0:
        print(
            "   ⚠️ 產出快過消費，積壓會持續成長。要嘛提高額度，要嘛降低標記產出"
            "（記者端提高標記門檻），不可只看「總逾期數」而不看這一行。",
            file=out,
        )

    # 趨勢：上一輪快照對照。存量數字沒有方向，只有序列才答得出「比上週好還是壞」。
    if history_path is not None:
        prev = _read_last_history(history_path, today)
        if prev is not None:
            prev_date, prev_total = prev
            delta = len(entries) - prev_total
            sign = "+" if delta > 0 else ""
            print(f"📈 趨勢：{prev_date} {prev_total} 筆 → 今日 {len(entries)} 筆（{sign}{delta}）", file=out)
        else:
            # 不印假數字是對的，但整行消失會讓讀者分不出「沒有基準」與「這功能壞了」。
            print("📈 趨勢：尚無上一輪快照（下次執行起可比較）", file=out)
        _append_history(history_path, today, len(entries), len(lane_a), len(lane_b), added)

    # 排空預估：「43 筆」沒有時間感，「8.6 週」有。
    if lane_b and QUEUE_LIMIT:
        print(f"⏳ 依現行額度，Lane B 需約 {len(lane_b) / QUEUE_LIMIT:.1f} 週排空（期間仍在進料）", file=out)

    # 舊語法盲區：佇列只讀新語法標記（舊字樣沒有探針欄，機器找不到它）。
    # 只印數字會讓 5c 誤以為「總逾期數 0」＝沒事，故在此列出頁面分佈，
    # 讓消化端每輪至少看得到盲區規模與位置。
    legacy = _legacy_by_page(wiki_dir)
    if legacy:
        total = sum(n for _, n in legacy)
        print(file=out)
        print(f"⚠️ 舊語法盲區：{total} 筆未回填，不在上方佇列內（前 10 頁）", file=out)
        for name, n in legacy[:10]:
            print(f"  {n:>3} 筆  {name}", file=out)
        print("  → 這些筆沒有探針欄，5c 永遠撈不到；依 `/wiki-lint` 3g 於記者輪回填為新語法後才會進佇列", file=out)

    print(file=out)
    print(
        f"→ 本輪請處理 Lane A {min(len(lane_a), SIGNAL_LIMIT)} 筆 ＋ Lane B "
        f"{min(len(lane_b), QUEUE_LIMIT)} 筆；寫回四選一見 `/wiki-lint` 5c 步驟 3",
        file=out,
    )


def main() -> int:
    args = sys.argv[1:]
    out = _stdout()

    if "--queue" in args:
        print_queue(out, history_path=HISTORY_PATH)
        out.flush()
        return 0

    report: list[str] = []
    ok = check(report)
    print("# check_pending_markers.py 報告\n", file=out)
    print("\n".join(report) if report else "  （無懸置標記）", file=out)
    print(file=out)
    print("狀態：" + ("✅ 懸置標記語法檢查通過" if ok else "❌ 懸置標記語法有誤"), file=out)
    out.flush()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
