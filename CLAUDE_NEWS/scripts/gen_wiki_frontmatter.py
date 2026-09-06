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

`signal` 有消費端才不會白算：`⚠️ 高引用但停滯` 由 `/wiki-lint` 步驟 5g 逐頁處置
（`--list-signal` 即其入口）。**列出方式刻意留在本檔而非 wiki_graph**——判準（入鏈 ≥ 15、
> 21 天無新聞、子樹聚合）在這裡定義，列表若另寫一支就會有第二份門檻，改一邊忘一邊。

用法：
    python scripts/gen_wiki_frontmatter.py --dry-run   # 只報告
    python scripts/gen_wiki_frontmatter.py             # 實際寫入
    python scripts/gen_wiki_frontmatter.py --list-signal "⚠️ 高引用但停滯"   # 只列該訊號的頁（不寫入）
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


PARENT_RE = re.compile(r"^\*\*上層[：:]\*\*\s*\[\[([^\]|#]+)", re.MULTILINE)
LAST_NEWS_RE_ANY = re.compile(r"^\*\*最後新聞更新[：:]\*\*\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE)
INDEX_ROW_RE = re.compile(r"^(\|\s*\[\[([^\]|#]+)\]\]\s*\|.*?)(\s*↳ 子故事：[^|]*)?(\|\s*)$")


def project_children_into_index(children_of: dict, index_path: Path, dry_run: bool, redirect_slugs: set | None = None) -> int:
    """把「↳ 子故事：[[a]]、[[b]]」投影寫進母頁的 index 列摘要格（機器投影，家在各子頁的上層欄）。

    子頁不入 index（2026-09-03 裁決：子頁只從母頁下鑽），但 index 仍是查詢入口與 13 處
    記者認領的依據——讓記者自己遍歷「上層」欄是把可靠性押在 sonnet 的主動性上。
    投影由本腳本每次重生，idempotent；check_hierarchy.py 驗它存在。回傳改動列數。

    `redirect_slugs`（`[加入: 2026-09-06]`）：投影排除本身是 redirect 殼的子頁——併回的殼
    對讀者沒有內容價值，母頁「↳ 子故事：」不該列出一個只寫著「已併回」的空殼。
    """
    if not index_path.exists():
        return 0
    redirect_slugs = redirect_slugs or set()
    lines = index_path.read_text(encoding="utf-8-sig").splitlines(keepends=True)
    changed = 0
    for i, line in enumerate(lines):
        m = INDEX_ROW_RE.match(line.rstrip("\r\n"))
        if not m:
            continue
        slug = m.group(2).strip()
        kids = sorted(k for k in children_of.get(slug, []) if k not in redirect_slugs)
        if not kids and not m.group(3):
            continue  # 無子頁也無舊投影的列一律不碰——不做無關的空白正規化（避免 diff 噪音）
        seg = ("　↳ 子故事：" + "、".join(f"[[{k}]]" for k in kids)) if kids else ""
        new_line = m.group(1).rstrip() + seg + " " + m.group(4).strip()
        eol = "\n" if line.endswith("\n") else ""
        if new_line != line.rstrip("\r\n"):
            lines[i] = new_line + eol
            changed += 1
    if changed and not dry_run:
        index_path.write_text("".join(lines), encoding="utf-8")
    return changed


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
    list_signal = None
    if "--list-signal" in argv:
        i = argv.index("--list-signal")
        list_signal = argv[i + 1] if i + 1 < len(argv) else "⚠️ 高引用但停滯"
    # 列出模式一律不寫入：它是 lint 的查詢入口，不該有副作用
    dry_run = "--dry-run" in argv or list_signal is not None
    today = date.today()

    pages = [
        (f"{sub}/{p.stem}", p, sub)
        for sub in ("entities", "topics")
        for p in sorted((WIKI_DIR / sub).glob("*.md"))
    ]
    slugs = {slug for slug, _, _ in pages}

    # ── 階層（2026-09-03）：單一來源是標頭 `**上層：** [[slug]]`。parent→child 的目錄邊與
    #    child→parent 的上層邊是「家族邊」，不算入鏈（否則每個子頁天生 1 入鏈、母頁被子頁灌爆，
    #    孤島與高引用兩個訊號都失真）。
    parent_of: dict[str, str] = {}
    redirect_slugs: set[str] = set()
    for slug, p, _ in pages:
        head60 = "\n".join(p.read_text(encoding="utf-8-sig").splitlines()[:60])
        m = PARENT_RE.search(head60)
        if m and m.group(1).strip() in slugs and m.group(1).strip() != slug:
            parent_of[slug] = m.group(1).strip()
            if "已併回" in head60:
                redirect_slugs.add(slug)
    children_of: dict[str, list[str]] = collections.defaultdict(list)
    for c, par in parent_of.items():
        children_of[par].append(c)

    def _kin(a: str, b: str) -> bool:
        return parent_of.get(a) == b or parent_of.get(b) == a

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
            if target in slugs and target != me and not _kin(me, target):
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
    signal_rows: list[tuple[str, str, int, int | None]] = []

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

        # 階層欄位：parent／children／page_role（root／hub／child／archive／redirect）。
        # 刻意不重用既有 `kind`（entity|topic）——wiki/_views/wiki-health.base 以它為欄。
        par = parent_of.get(slug)
        kids = sorted(children_of.get(slug, []))
        meta["parent"] = par
        meta["children"] = kids
        head60 = "\n".join(body.splitlines()[:60])
        if "-archive" in slug.split("/")[-1]:
            role = "archive"
        elif par and "已併回" in head60:
            role = "redirect"
        elif kids and par:
            role = "hub+child"
        elif kids:
            role = "hub"
        elif par:
            role = "child"
        else:
            role = "root"
        meta["page_role"] = role
        # 子樹新鮮度：hub 自身「最後新聞更新」不因子頁動（會與 freshness 第 2 類互斥），
        # 訊號判準改看子樹——否則熱議題的根頁會被判「高引用但停滯」或在列表沉底。
        subtree_days = days
        stack = list(kids)
        while stack:
            k = stack.pop()
            klnu = LAST_NEWS_RE_ANY.search("\n".join((WIKI_DIR / f"{k}.md").read_text(encoding="utf-8-sig").splitlines()[:60]))
            if klnu:
                kd = (today - date.fromisoformat(klnu.group(1))).days
                subtree_days = kd if subtree_days is None else min(subtree_days, kd)
            stack.extend(children_of.get(k, []))
        meta["days_since_news_subtree"] = subtree_days
        if kids:
            days = subtree_days

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
        signal_rows.append((signal, slug, ib, days))

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

    if list_signal is not None:
        rows = sorted((r for r in signal_rows if r[0] == list_signal), key=lambda r: (-r[2], r[1]))
        stream.write(f"# signal = {list_signal}（{len(rows)} 頁；入鏈多者在前）\n\n")
        stream.write("| 頁 | 入鏈 | 距上次新聞 |\n|---|---|---|\n")
        for _, slug, ib, days in rows:
            stream.write(f"| {slug} | {ib} | {'—' if days is None else str(days) + ' 天'} |\n")
        if not rows:
            stream.write("| （無） | | |\n")
        stream.flush()
        return 0

    stream.write(f"頁面 {len(pages)}：寫入 {written}／未變 {unchanged}\n")
    # index 投影：母頁列摘要格的「↳ 子故事：」由此重生（子頁不入 index，查詢與認領靠投影）
    n_proj = project_children_into_index(children_of, WIKI_DIR / "index.md", dry_run, redirect_slugs)
    if n_proj:
        stream.write(f"index 子故事投影：改動 {n_proj} 列\n")
    stream.write("signal 分布：" + "、".join(f"{k} {v}" for k, v in signals.most_common()) + "\n")
    if dry_run:
        stream.write("(--dry-run，未寫入)\n")
    stream.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
