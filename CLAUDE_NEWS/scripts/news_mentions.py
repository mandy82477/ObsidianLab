#!/usr/bin/env python3
"""
news_mentions.py — 回答「這個東西最近有沒有在日報被提到」。

為什麼要有這支腳本
------------------
這個問題在規則裡至少被問過四次（wiki-lint 5a 熱度降溫、features 規則的
⏳ 逾期與熱度降溫、community-lint 的工具汰除），每一處都由執行者臨場手刻
一個 grep——於是每一處都能用不同的方式失敗。

2026-08-28 實際踩到，同一次查證裡兩種錯各犯一次：

  漏抓：查 feature-radar 的「Dreaming 記憶整合」只用英文全名精確比對，
        判定「113 天無後續」。實際上 2026-07-17 日報寫著「Python SDK
        0.117.0 新增對『dreaming』API 功能的支援」——功能還活著，卻差點
        被降到 🔥 並在讀者面前標上「細節未公布」。日報是繁體中文寫的，
        只用英文全名比對必然漏抓。

  假命中：查「Proactive Workflows」時忽略大小寫，`proactive` 命中 5 天，
        其中三次全是「Proactive financial news」這個財經媒體名，與該功能
        毫無關係。只數命中次數不看原文，會把死的判活。

懸置標記系統（`pending_markers.py` / `scan_pending_verifications.py`）早就
把這兩種錯防住了——它要求 ≥2 個探針同時命中、禁用過寬詞、中文探針有長度
地板。本腳本不發明新方法，只是把那套已經被 run_tests 覆蓋的紀律借出來，
讓另外四個消費端也用得到。

三條設計原則
------------
1. **強制 ≥2 個詞**：單一詞的偵測力不足（同懸置探針規則）。這條擋假命中。
2. **過寬詞直接拒絕執行**（非警告）：沿用 `probe_too_weak()` 的判準與停用詞
   清單。拒絕而不是警告，是因為警告會被略過。
3. **輸出必附命中原文行**：只給次數會讓人直接下結論。附原文是為了逼出
   「看一眼這是不是真的在講同一件事」那一步——那是唯一擋得住「Proactive
   financial news」的東西。

用法
----
    python scripts/news_mentions.py --since 4w "Dreaming" "記憶整合"
    python scripts/news_mentions.py --since 90d --any "Capability Curve" "能力曲線"
    python scripts/news_mentions.py --since 4w --json "SendFeedback" "回報工具"

    --since  4w / 30d / YYYY-MM-DD（預設 4w）
    --any    任一詞命中即算（預設：需 ≥2 個不同詞在同一天命中）
    --json   機器可讀輸出
    --allow-weak  放行過寬詞（僅限確知無替代詞時，會在輸出標警告）

退出碼：0=有命中，1=無命中，2=用法或探針品質錯誤。
"""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "news"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pending_markers import normalize_probe, probe_too_weak  # noqa: E402

DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.md$")


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def _is_ascii(s: str) -> bool:
    return all(ord(c) < 128 for c in s)


def term_hit(term: str, text_norm: str) -> bool:
    """與 scan_pending_verifications._term_hit 同一判準：英數詞加詞邊界，
    中文詞直接含有即可（中文沒有詞邊界概念）。"""
    norm = normalize_probe(term)
    if not norm:
        return False
    if _is_ascii(norm):
        return re.search(r"(?<![a-z0-9])" + re.escape(norm) + r"(?![a-z0-9])", text_norm) is not None
    return norm in text_norm


def parse_since(spec: str, today: date) -> date | None:
    m = re.fullmatch(r"(\d+)([wd])", spec)
    if m:
        n = int(m.group(1))
        return today - timedelta(weeks=n) if m.group(2) == "w" else today - timedelta(days=n)
    try:
        return date.fromisoformat(spec)
    except ValueError:
        return None  # 呼叫端轉成 rc=2 並印到 stdout（用法錯誤與「查無命中」必須可分辨）


def iter_news(since: date, today: date):
    if not NEWS_DIR.is_dir():
        return
    for p in sorted(NEWS_DIR.glob("*.md")):
        m = DATE_RE.match(p.name)
        if not m:
            continue
        d = date.fromisoformat(m.group(1))
        if since <= d <= today:
            yield d, p


def scan(terms: list[str], since: date, today: date, need_two: bool) -> list[dict]:
    """回傳每個命中日的 {date, terms, lines}。lines 為命中原文行（去頭尾空白）。"""
    hits: list[dict] = []
    for d, path in iter_news(since, today):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        norm_full = normalize_probe(text)
        matched = [t for t in terms if term_hit(t, norm_full)]
        if not matched:
            continue
        if need_two and len(matched) < 2:
            continue
        lines = []
        for raw in text.split("\n"):
            ln = normalize_probe(raw)
            if any(term_hit(t, ln) for t in matched):
                s = raw.strip()
                if s:
                    lines.append(s[:200])
        hits.append({"date": d.isoformat(), "terms": matched, "lines": lines[:4]})
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="查日報有沒有提到某個東西（共用搜尋紀律）")
    ap.add_argument("terms", nargs="*", help="別名，至少 2 個；日報為繁中，務必含中文譯名")
    ap.add_argument("--since", default="4w", help="時間窗：4w / 30d / YYYY-MM-DD（預設 4w）")
    ap.add_argument("--any", action="store_true", help="任一詞命中即算（預設需 ≥2 詞同日命中）")
    ap.add_argument("--json", action="store_true", help="機器可讀輸出")
    ap.add_argument("--allow-weak", action="store_true", help="放行過寬詞（會標警告）")
    ap.add_argument("--today", default=None, help="覆寫今日（測試用）")
    args = ap.parse_args()
    out = _stdout()

    if len(args.terms) < 2:
        print("❌ 至少要給 2 個別名。單一詞偵測力不足——這是懸置探針系統的既有結論"
              "（2026-08-28：單用 `proactive` 命中的三次全是「Proactive financial news」媒體名）。\n"
              "   日報是繁體中文寫的，別名務必含中文譯名，否則必然漏抓。", file=out)
        out.flush()
        return 2

    weak = [(t, why) for t in args.terms if (why := probe_too_weak(t))]
    if weak and not args.allow_weak:
        print("❌ 探針品質不合格（沿用懸置標記的判準，拒絕執行而非警告——警告會被略過）：", file=out)
        for t, why in weak:
            print(f"   - {why}", file=out)
        print("   換更具體的詞；確知無替代時才加 --allow-weak。", file=out)
        out.flush()
        return 2

    today = date.fromisoformat(args.today) if args.today else date.today()
    since = parse_since(args.since, today)
    if since is None:
        print(f"❌ --since 格式錯誤：{args.since}（用 4w / 30d / YYYY-MM-DD）", file=out)
        out.flush()
        return 2
    hits = scan(args.terms, since, today, need_two=not args.any)

    if args.json:
        print(json.dumps({
            "terms": args.terms, "since": since.isoformat(), "today": today.isoformat(),
            "mode": "any" if args.any else "need_two",
            "days_hit": len(hits), "last_hit": hits[-1]["date"] if hits else None,
            "hits": hits,
        }, ensure_ascii=False, indent=2), file=out)
        out.flush()
        return 0 if hits else 1

    print(f"# 日報提及查詢：{' / '.join(args.terms)}", file=out)
    print(f"窗口 {since} ~ {today}｜模式 {'任一詞命中' if args.any else '需 ≥2 詞同日命中'}"
          f"{'｜⚠️ 已放行過寬詞' if weak else ''}\n", file=out)
    if not hits:
        print("命中 0 天。", file=out)
        print("\n⚠️ 判「無後續」前先自問：別名夠不夠？有沒有中文譯名？"
              "（2026-08-28 教訓：只用英文全名查，把還活著的功能判死了）", file=out)
        out.flush()
        return 1

    for h in hits:
        print(f"── {h['date']}（命中：{'、'.join(h['terms'])}）", file=out)
        for ln in h["lines"]:
            print(f"     {ln}", file=out)
    print(f"\n命中 {len(hits)} 天，最後一次 {hits[-1]['date']}。", file=out)
    print("⚠️ 上面的原文行必須逐條看過再下結論——同名媒體／同名產品會製造假命中，"
          "只數次數會把死的判活。", file=out)
    out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
