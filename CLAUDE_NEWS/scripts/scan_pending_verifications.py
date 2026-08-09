#!/usr/bin/env python3
"""每日懸置掃描器 — 拿懸置標記的探針比對當日日報，命中就產出可直接貼進記者
派工的附件。

語法與 parser 全部複用 `scripts/pending_markers.py`（`iter_pending()` /
`normalize_probe()` / `probe_is_wikilink()` / `detective_aliases()` /
`wiki_pages()` / `page_slug()` / `reporter_of()` / `DOMAIN_TO_REPORTER`），
本檔不重新發明比對邏輯以外的任何東西。

三條界線，仿 `scripts/scan_open_forecasts.py`：
1. **只偵測，不判定** —— 命中只代表「這裡可能有動靜」，是否算數由記者判斷。
2. **只讀不寫日報** —— 不修改 news/，只 append `data/pending-signals.jsonl`。
3. **永遠 exit 0** —— 找不到日報／零 marker 都印訊息後 return 0，失敗只記錄
   不阻斷 pipeline。

比對演算法（規格見 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節）：

  1. 條目切分：`ENTRY_RE` 把日報切成 entry，比對範圍是 entry.title 與
     entry.body 兩個獨立欄位，不是全檔 substring。
  2. 探針正規化：NFKC + casefold；純 ASCII 探針加 word boundary；wikilink
     探針展開為別名集合（slug 末段 + 目標頁 H1 標題），再經
     `detective_aliases()` 剔除落在 `PROBE_STOPLIST` 的別名——樞紐頁（如
     `claude-code`）展開出的別名多半是頁面本身的通用詞，過濾後不參與比對
     `[加入: 2026-08-10]`。
  3. 多探針 AND：≥2 個不同探針同時出現在該 entry 才算命中；單探針放行例外
     ＝該探針是 wikilink 且展開後仍有非空偵測別名，或正規化後長度 ≥6。
  4. 分級：S＝≥2 探針命中且至少一個在 title，或 1 個 wikilink 探針在
     title；A＝≥2 探針同 entry（title 或 body）；B＝僅 1 探針且僅在
     body（含「單探針放行但不在 title」的殘餘情況）→ 記入 jsonl 但不進
     派工附件。

用法：
    python scripts/scan_pending_verifications.py [YYYY-MM-DD]
    python scripts/scan_pending_verifications.py --dry-run
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pending_markers import (  # noqa: E402
    WIKI_DIR, DOMAIN_TO_REPORTER, Marker, PROBE_DETECTIVE_LEN_FLOOR,
    detective_aliases, iter_pending, normalize_probe, probe_is_wikilink,
    wiki_pages, page_domain, reporter_of,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "news"
DATA_DIR = REPO_ROOT / "data"
SIGNALS_PATH = DATA_DIR / "pending-signals.jsonl"

# 日報條目：標題行為 **[標題](url)**，其後為說明句（同 scan_open_forecasts.py）
ENTRY_RE = re.compile(r"^\*\*\[(.+?)\]\((https?://[^)]+)\)\*\*", re.MULTILINE)
SECTION_HEADER_RE = re.compile(r"^#{2,3}[ \t]", re.MULTILINE)

TOPIC_LEN = 24
SINGLE_PROBE_LEN_FLOOR = PROBE_DETECTIVE_LEN_FLOOR  # 與 pending_markers.detective_aliases() 同一地板
SUPPRESS_AFTER = 3

REPORTER_LABEL = {
    "wiki-reporter-models": "模型",
    "wiki-reporter-features": "功能",
    "wiki-reporter-commercial": "商業",
    "wiki-reporter-safety-policy": "安全政策",
    "wiki-reporter-community": "社群",
    "wiki-reporter-people": "人物",
}
# 顯示順序依 DOMAIN_TO_REPORTER 的 domain 插入順序（模型/功能/商業/安全政策/社群/人物），
# 但要轉成中文標籤——`DOMAIN_TO_REPORTER.values()` 是 reporter slug 不是標籤，
# 直接拿 slug 去跟 REPORTER_LABEL 的標籤比對永遠比不中，「無命中記者」會恆列全部六個。
REPORTER_ORDER = [REPORTER_LABEL[r] for r in dict.fromkeys(DOMAIN_TO_REPORTER.values())]


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def _slug(path: Path, wiki_dir: Path) -> str:
    """同 `scripts/check_pending_markers.py` 的 `_slug()`：`pending_markers.page_slug()`
    寫死用模組層級的 `WIKI_DIR`，測試用臨時 wiki_dir 時會 fallback 成 `path.stem`
    （丟失 `topics/` 前綴），故在此重新以傳入的 wiki_dir 為準。"""
    try:
        return path.relative_to(wiki_dir).as_posix()[:-3]
    except ValueError:
        return path.stem


def _is_ascii(s: str) -> bool:
    return all(ord(c) < 128 for c in s)


def _term_hit(term: str, text_norm: str) -> bool:
    norm = normalize_probe(term)
    if not norm:
        return False
    if _is_ascii(norm):
        pattern = r"(?<![a-z0-9])" + re.escape(norm) + r"(?![a-z0-9])"
        return re.search(pattern, text_norm) is not None
    return norm in text_norm


def probe_search_terms(probe: str, wiki_dir: Path) -> list[str]:
    """實際拿去比對日報文字的詞——wikilink 探針走 `detective_aliases()`，只留
    非 STOPLIST 別名；被剔除的別名（如樞紐頁展開出的「Claude Code」）不參與
    比對，這是 2026-08-10 修復的核心：舊版直接用展開後的全部別名比對，等於
    讓樞紐頁 wikilink 對任何含頁名的條目都放行。"""
    if probe_is_wikilink(probe):
        return detective_aliases(probe, wiki_dir)
    return [probe]


def probe_hit(probe: str, title_norm: str, body_norm: str, wiki_dir: Path) -> tuple[bool, bool]:
    """回傳 (在 title 命中, 在 body 命中)。"""
    terms = probe_search_terms(probe, wiki_dir)
    title_hit = any(_term_hit(t, title_norm) for t in terms)
    body_hit = any(_term_hit(t, body_norm) for t in terms)
    return title_hit, body_hit


def iter_digest_entries(text: str) -> list[dict]:
    """把日報切成 entry：title / url / body（body 止於下一個 entry 或下一個
    ## / ### 小節標題，避免最後一則 entry 的 body 吃到後面整個 📡 來源狀態表）。"""
    matches = list(ENTRY_RE.finditer(text))
    boundaries = sorted(
        {m.start() for m in matches}
        | {m.start() for m in SECTION_HEADER_RE.finditer(text)}
        | {len(text)}
    )
    entries = []
    for m in matches:
        header_end = m.end()
        body_end = next((b for b in boundaries if b > header_end), len(text))
        title = m.group(1)
        body = text[header_end:body_end]
        entries.append({
            "title": title,
            "url": m.group(2),
            "body": body,
            "title_norm": normalize_probe(title),
            "body_norm": normalize_probe(body),
        })
    return entries


def _extract_topic(text: str, marker_end: int) -> str:
    """粗略萃取標記本身的「題目」（標準式在 metadata 後接 `｜**題目**：`；
    表格細節區則直接接 `：內文`），供 stdout 附件可讀性使用，非強規格欄位。"""
    tail = text[marker_end: marker_end + 300].split("\n", 1)[0]
    tail = tail.lstrip("｜").strip()
    m = re.match(r"\*\*(.+?)\*\*[:：]?\s*(.*)", tail)
    topic = m.group(1) if m else tail.lstrip(":：").strip()
    return topic[:TOPIC_LEN]


def classify(mk: Marker, entry: dict, wiki_dir: Path) -> dict | None:
    """判斷一筆 marker 對一則 entry 是否命中，命中則回傳分級結果，否則 None。"""
    hits = []
    for probe in mk.probes:
        th, bh = probe_hit(probe, entry["title_norm"], entry["body_norm"], wiki_dir)
        if th or bh:
            hits.append((probe, th, bh))

    if not hits:
        return None

    if len(hits) >= 2:
        any_title = any(th for _, th, _ in hits)
        tier = "S" if any_title else "A"
    else:
        probe, th, _bh = hits[0]
        # wikilink 探針的單探針放行特權，收緊為「展開後仍有非 STOPLIST 別名」
        # 才成立——樞紐頁 wikilink 展開全落在 STOPLIST 時 `probe_search_terms()`
        # 已回傳空集合，不會出現在 hits 裡；這裡再擋一次是防禦性重複檢查。
        qualifies = (
            (probe_is_wikilink(probe) and probe_search_terms(probe, wiki_dir))
            or len(normalize_probe(probe)) >= SINGLE_PROBE_LEN_FLOOR
        )
        if not qualifies:
            return None
        any_title = th
        tier = "S" if (probe_is_wikilink(probe) and th) else "B"

    return {
        "tier": tier,
        "probes_hit": [p for p, _, _ in hits],
        "where": "title" if any_title else "body",
    }


def compute_marker_id(page: str, mk: Marker) -> str:
    probes_joined = "、".join(normalize_probe(p) for p in mk.probes)
    raw = f"{page}|{mk.marked}|{probes_joined}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]


def compute_dedup_key(marker_id: str, entry_url: str) -> str:
    raw = f"{marker_id}|{entry_url}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def load_existing(jsonl_path: Path) -> tuple[set[str], Counter]:
    dedup_keys: set[str] = set()
    counts: Counter = Counter()
    if not jsonl_path.exists():
        return dedup_keys, counts
    for line in jsonl_path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "dedup_key" in rec:
            dedup_keys.add(rec["dedup_key"])
        if "marker_id" in rec:
            counts[rec["marker_id"]] += 1
    return dedup_keys, counts


def scan_digest(digest_path: Path, wiki_dir: Path | None = None,
                 jsonl_path: Path | None = None, dry_run: bool = False) -> dict:
    """核心掃描（可測試）：讀 wiki 全部懸置標記，對指定日報逐一比對，回傳
    統計與新命中的紀錄，並（非 dry_run 時）append 至 jsonl。"""
    wiki_dir = wiki_dir or WIKI_DIR
    jsonl_path = jsonl_path or SIGNALS_PATH

    digest_text = digest_path.read_text(encoding="utf-8-sig")
    scan_date = digest_path.stem
    entries = iter_digest_entries(digest_text)

    pages = wiki_pages(wiki_dir)
    page_text: dict[Path, str] = {}
    all_markers: list[tuple[Path, Marker]] = []
    for path in pages:
        try:
            text = path.read_text(encoding="utf-8-sig")
        except OSError:
            continue
        page_text[path] = text
        for mk in iter_pending(text, path):
            all_markers.append((path, mk))

    dedup_keys, counts = load_existing(jsonl_path)
    new_records: list[dict] = []
    tiers: Counter = Counter()

    for path, mk in all_markers:
        page = _slug(path, wiki_dir)
        domain = page_domain(path)
        reporter = reporter_of(path)
        for entry in entries:
            result = classify(mk, entry, wiki_dir)
            if result is None:
                continue
            marker_id = compute_marker_id(page, mk)
            dedup_key = compute_dedup_key(marker_id, entry["url"])
            if dedup_key in dedup_keys:
                continue  # 已記錄過的命中，不重寫

            prior = counts.get(marker_id, 0)
            suppressed = prior >= SUPPRESS_AFTER and mk.signal is None

            record = {
                "scan_date": scan_date,
                "tier": result["tier"],
                "marker_id": marker_id,
                "dedup_key": dedup_key,
                "page": page,
                "line": mk.line,
                "kind": mk.kind,
                "marked": mk.marked,
                "review": mk.review,
                "signal": mk.signal,
                "topic": _extract_topic(page_text[path], mk.end),
                "probes_all": mk.probes,
                "probes_hit": result["probes_hit"],
                "where": result["where"],
                "domain": domain,
                "reporter": reporter,
                "entry_title": entry["title"],
                "entry_url": entry["url"],
                "suppressed": suppressed,
            }
            new_records.append(record)
            tiers[result["tier"]] += 1
            dedup_keys.add(dedup_key)
            counts[marker_id] = prior + 1

    if new_records and not dry_run:
        jsonl_path.parent.mkdir(parents=True, exist_ok=True)
        with jsonl_path.open("a", encoding="utf-8") as fh:
            for rec in new_records:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    return {
        "scan_date": scan_date,
        "total_markers": len(all_markers),
        "total_entries": len(entries),
        "tiers": tiers,
        "new_records": new_records,
    }


def build_dispatch(new_records: list[dict]) -> tuple[dict[str, list[dict]], list[str]]:
    """依 reporter 分組（僅 S/A、非 suppressed），回傳 (分組, 無命中記者標籤列表)。"""
    groups: dict[str, list[dict]] = {}
    for rec in new_records:
        if rec["tier"] not in ("S", "A") or rec["suppressed"]:
            continue
        reporter = rec.get("reporter")
        if not reporter:
            continue
        groups.setdefault(reporter, []).append(rec)

    hit_labels = {REPORTER_LABEL.get(r, r) for r in groups}
    no_hit = [label for label in REPORTER_ORDER if label not in hit_labels]
    return groups, no_hit


def format_report(result: dict, out) -> None:
    scan_date = result["scan_date"]
    tiers = result["tiers"]
    print(f"# scan_pending_verifications.py（{scan_date}）\n", file=out)
    print(
        f"  懸置標記 {result['total_markers']} 筆／日報 {result['total_entries']} 則條目 "
        f"→ 命中 S:{tiers.get('S', 0)} A:{tiers.get('A', 0)} B:{tiers.get('B', 0)}"
        "（B 級弱訊號不派工）",
        file=out,
    )

    groups, no_hit = build_dispatch(result["new_records"])
    for reporter, label in [(r, REPORTER_LABEL[r]) for r in REPORTER_LABEL if r in groups]:
        recs = groups[reporter]
        print(f"\n## [{label}] 待查證命中（{len(recs)} 筆｜機械偵測，可能誤判）", file=out)
        for rec in recs:
            where_label = "命中標題" if rec["where"] == "title" else "命中內文"
            print(
                f"- ⟨{rec['tier']}⟩ {rec['page']}:{rec['line']}「{rec['topic']}」（標 {rec['marked']}）",
                file=out,
            )
            print(
                f"  探針 {'＋'.join(rec['probes_hit'])} {where_label}："
                f"**[{rec['entry_title']}]({rec['entry_url']})**",
                file=out,
            )

    print(f"\n無命中記者：{'、'.join(no_hit) if no_hit else '無'}", file=out)


def main() -> int:
    args = sys.argv[1:]
    out = _stdout()
    dry_run = "--dry-run" in args
    positional = [a for a in args if not a.startswith("--")]
    target = positional[0] if positional else None

    if target:
        digest_path = NEWS_DIR / f"{target}.md"
    else:
        candidates = sorted(NEWS_DIR.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md"))
        digest_path = candidates[-1] if candidates else None

    if not digest_path or not digest_path.exists():
        print(f"  略過：找不到日報 {digest_path}", file=out)
        out.flush()
        return 0

    result = scan_digest(digest_path, dry_run=dry_run)

    if result["total_markers"] == 0:
        print(f"# scan_pending_verifications.py（{result['scan_date']}）\n", file=out)
        print("  略過：wiki/ 無任何懸置標記", file=out)
        out.flush()
        return 0

    format_report(result, out)
    out.flush()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001 — 掃描器必須永不阻斷 pipeline
        _out = _stdout()
        print(f"  ⚠️ scan_pending_verifications.py 執行異常（已忽略，不阻斷 pipeline）：{exc}", file=_out)
        _out.flush()
        sys.exit(0)
