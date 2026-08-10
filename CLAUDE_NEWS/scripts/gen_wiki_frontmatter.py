"""為 wiki 頁面生成 YAML frontmatter，供 Obsidian Bases 查詢。

**為什麼是「生成」而不是「手寫」**

`wiki/CLAUDE.md` 的資訊架構哲學要求「每個事實只有一個家」。頁面標頭那幾行粗體
（`**類型：** model`）是作者手寫的**唯一的家**；本檔產出的 frontmatter 是它的
**機器投影**，跟 `web_reader/data/*.json` 一樣是建置產物，不是第二份手抄副本。
所以：改內容改粗體標頭，重跑本檔即可；**不要手改 frontmatter**（會被覆寫）。

**為什麼需要它**

Bases 只讀 note properties，讀不到散文與粗體文字，所以沒有 frontmatter 就無法用
Obsidian 做任何結構化盤點。而且有些欄位根本不在頁面裡——入鏈數要掃全庫 wikilink、
供料數要查 `data/source_attribution.jsonl`——這些算完寫進 frontmatter 之後，
Bases 才能直接排序篩選，不需要外部腳本。

**signal 欄位**（四象限，判準在此處定義一次，Bases 視圖只管篩選）

| 值 | 條件 | 讀法 |
|---|---|---|
| `⚠️ 高引用但停滯` | 入鏈 ≥ 15 且 超過 21 天無新聞 | **最該看的一格**：很多頁指向它，讀者被導過去卻看到舊東西。頁面沒壞、鏈結沒斷，是靜默失效 |
| `孤島` | 入鏈 ≤ 3 且 21 天內有新聞 | 一直在更新但幾乎沒人指向，讀者到不了 |
| `休眠` | 入鏈 < 15 且 超過 21 天無新聞 | 正常，該主題近期沒事發生 |
| `健康` | 其餘 | — |

用法：
    python scripts/gen_wiki_frontmatter.py --dry-run   # 只報告
    python scripts/gen_wiki_frontmatter.py             # 實際寫入
"""

from __future__ import annotations

import collections
import io
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pending_markers import PENDING_RE, iter_pending  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
ATTRIBUTION = REPO_ROOT / "data" / "source_attribution.jsonl"

INBOUND_HIGH = 15
STALE_DAYS = 21
ISLAND_INBOUND = 3
PENDING_REVIEW_DEFAULT_DAYS = 14  # 與 scripts/check_pending_markers.py 的 REVIEW_DEFAULT_DAYS 對齊

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")

FIELD_RE = {
    "type": re.compile(r"^\*\*類型[：:]\*\*\s*(.+?)\s*$", re.MULTILINE),
    "status": re.compile(r"^\*\*狀態[：:]\*\*\s*(.+?)\s*$", re.MULTILINE),
    "domain": re.compile(r"^\*\*領域[：:]\*\*\s*(.+?)\s*$", re.MULTILINE),
    "last_updated": re.compile(r"^\*\*最後更新[：:]\*\*\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE),
    "last_news_update": re.compile(r"^\*\*最後新聞更新[：:]\*\*\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE),
    "update_freq": re.compile(r"^\*\*更新頻率[：:]\*\*\s*(.+?)\s*$", re.MULTILINE),
}


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def yaml_scalar(v) -> str:
    """最小 YAML 標量輸出。字串一律雙引號包起來，避免 emoji／冒號／中文括號踩到語法。"""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if v is None:
        return "null"
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'


def strip_body(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def strip_pending_probes(text: str) -> str:
    """移除懸置標記 metadata 區塊（`（標 …｜查 …）`），只留下 `❓**待查證**` 本身。

    metadata 括號段裡的 wikilink 是偵測用探針，不是內容引用（見
    `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節），入鏈統計不該算它。
    標記後方的第四段（`｜**題目**：內文`）不在 PENDING_RE 的 match 範圍內，故
    這裡整段替換掉 match 不會動到它，內文若有 wikilink 仍照常留給 findall 計入。
    """
    return PENDING_RE.sub(
        lambda m: f"{m.group('sym')}**{m.group('kind')}**", text
    )


def main(argv: list[str]) -> int:
    stream = _stdout()
    dry_run = "--dry-run" in argv
    today = date.today()

    pages = [
        (f"{sub}/{p.stem}", p, sub)
        for sub in ("entities", "topics")
        for p in sorted((WIKI_DIR / sub).glob("*.md"))
    ]
    slugs = {slug for slug, _, _ in pages}

    # ── 入鏈：掃全 wiki 的 wikilink。index/log 是目錄與流水帳，指向所有頁面，
    #    計入會讓每頁齊頭加一、失去鑑別度，故排除。
    inbound: collections.Counter[str] = collections.Counter({s: 0 for s in slugs})
    for f in WIKI_DIR.rglob("*.md"):
        me = f.relative_to(WIKI_DIR).as_posix()[:-3]
        if me in ("index", "log"):
            continue
        page_text = strip_pending_probes(strip_body(f.read_text(encoding="utf-8-sig")))
        for target in WIKILINK_RE.findall(page_text):
            target = target.strip()
            if target in slugs and target != me:
                inbound[target] += 1

    # ── 供料：歸因 ledger
    att_count: collections.Counter[str] = collections.Counter()
    att_last: dict[str, str] = {}
    att_srcs: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    if ATTRIBUTION.exists():
        for line in ATTRIBUTION.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            pg = row.get("page")
            if not pg:
                continue
            att_count[pg] += 1
            att_last[pg] = max(att_last.get(pg, ""), row.get("date", ""))
            if row.get("source"):
                att_srcs[pg][row["source"]] += 1

    written = unchanged = 0
    signals: collections.Counter[str] = collections.Counter()

    for slug, path, sub in pages:
        with path.open(encoding="utf-8-sig", newline="") as fh:
            raw = fh.read()
        body = strip_body(raw)

        meta: dict[str, object] = {
            "page": slug,
            "kind": "entity" if sub == "entities" else "topic",
        }
        for key, rx in FIELD_RE.items():
            m = rx.search(body)
            if m:
                meta[key] = m.group(1)

        status = str(meta.get("status", ""))
        meta["status_main"] = re.split(r"[（(]", status)[0].strip() or None

        lnu = meta.get("last_news_update")
        days = (today - date.fromisoformat(str(lnu))).days if lnu else None
        meta["days_since_news"] = days

        ib = inbound[slug]
        meta["inbound_links"] = ib
        meta["attribution_count"] = att_count.get(slug, 0)
        meta["attribution_last"] = att_last.get(slug) or None
        top = att_srcs.get(slug)
        meta["top_source"] = top.most_common(1)[0][0] if top else None

        # ── 懸置標記彙總：逐頁解析 ❓/🔎，供 Bases 排序篩選 ──
        markers = iter_pending(body, path)
        meta["pending_count"] = len(markers)
        overdue = 0
        next_review: date | None = None
        signalled = 0
        for mk in markers:
            marked_date = date.fromisoformat(mk.marked)
            review_date = (
                date.fromisoformat(mk.review) if mk.review
                else marked_date + timedelta(days=PENDING_REVIEW_DEFAULT_DAYS)
            )
            if review_date <= today:
                overdue += 1
            elif next_review is None or review_date < next_review:
                next_review = review_date
            if mk.signal:
                signalled += 1
        meta["pending_overdue"] = overdue
        meta["pending_next_review"] = next_review.isoformat() if next_review else None
        meta["pending_signalled"] = signalled

        stale = days is not None and days > STALE_DAYS
        if ib >= INBOUND_HIGH and stale:
            signal = "⚠️ 高引用但停滯"
        elif ib <= ISLAND_INBOUND and not stale:
            signal = "孤島"
        elif stale:
            signal = "休眠"
        else:
            signal = "健康"
        meta["signal"] = signal
        signals[signal] += 1

        meta["generated_by"] = "scripts/gen_wiki_frontmatter.py"

        nl = "\r\n" if "\r\n" in raw[:400] else "\n"
        fm = "---" + nl
        for k, v in meta.items():
            fm += f"{k}: {yaml_scalar(v)}{nl}"
        fm += "---" + nl

        new_raw = fm + body
        if new_raw == raw:
            unchanged += 1
            continue
        written += 1
        if not dry_run:
            with path.open("w", encoding="utf-8", newline="") as fh:
                fh.write(new_raw)

    stream.write(f"頁面 {len(pages)}：寫入 {written}／未變 {unchanged}\n")
    stream.write("signal 分布：" + "、".join(f"{k} {v}" for k, v in signals.most_common()) + "\n")
    if dry_run:
        stream.write("(--dry-run，未寫入)\n")
    stream.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
