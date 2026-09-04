#!/usr/bin/env python3
"""wiki_graph.py — wiki 節點查詢層（隨需解析，零落地檔案）。

wiki 的圖從第一天起就存在：頁面＝節點、wikilink＝邊。本腳本把它升格為可查詢，
不建常駐圖檔（沒有檔案就沒有過期問題）。設計依據：2026-08-27 graphifyy 試點
（docs/graphify-pilot-plan.md）與雙 agent 節點政策辯論的收斂結論。

節點衛生規則（與既有衍生層字面共用，不另立設定檔）：
  - wikilink 解析：import build_web.WIKILINK_RE / ANCHORED_WIKILINK_RE
  - 懸置探針剝除：import gen_wiki_frontmatter.strip_pending_probes（探針 wikilink
    是偵測器不是內容引用）
  - 樞紐排除：index / log 指向所有頁面、無鑑別力（同 gen_wiki_frontmatter 入鏈統計）
  - 模板標題（參考來源／相關實體／時序…）與純日期標題不是一級節點：sections 查詢
    回傳時上捲到最近的語意標題
  - 「參考來源」等樣板區的邊標記 zone=樣板；指向 news/ 的連結排除（日報是原料不是節點）

子命令：
  explain <頁slug>      雙向引用，出邊按產地分組，含「頁 § 最近標題 § 行號」
  path <頁A> <頁B>      頁層 BFS 最短路徑（樣板區邊不參與）
  sections <關鍵詞>     跨頁找「議題散在哪幾節」，回傳限定名＋行號
  cluster              頁層 references 投影分群（label propagation），與 frontmatter
                       領域欄比對，列出「分群歸屬 vs 人工領域」不一致的頁（診斷用）
  sources <頁slug>     查原文：列出該頁在 data/source_attribution.jsonl 的歸因
                       （日期｜來源｜條目標題｜原始 URL，新到舊）——帳本 07-11 起收，
                       更早的事實走日報：頁內時序找日期 → news/該日.md 條目附原文連結
  similar <頁slug>     「你可能也想看」：與該頁**不直接相連**但共享鄰居的頁，加權 Jaccard
                       （鄰居權重 1/度數，壓樞紐）；build_web 用同一函式產讀者推薦
  gaps [--top N]       缺口偵測（lint 用）：全庫兩兩算同一分數，取分數高卻互不相連的頁對；
                       data/graph_gap_ignore.json 登記「已審、無需連結」的對，不再列出

用法：python scripts/wiki_graph.py explain entities/pricing
"""
from __future__ import annotations

import io
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_web import ANCHORED_WIKILINK_RE, WIKI_DIR, WIKILINK_RE  # noqa: E402
from gen_wiki_frontmatter import strip_body, strip_pending_probes  # noqa: E402

# 樞紐與維運層：目錄/流水帳/規則/儀表，指向或被指向一切，無鑑別力（辯論共識 2）
EXCLUDE_PAGES = {"index", "log", "CLAUDE", "metrics", "reader-notes"}
# 樣板區標題：此 h2 之下的 wikilink 屬 see-also / 出處性質，非敘事主動提及
TEMPLATE_ZONE_H2 = {"參考來源", "相關實體", "相關議題", "使用指南"}
# 模板標題與純日期標題：sections 回傳時上捲、不作為錨定名（辯論共識：圖上的過寬詞）
TEMPLATE_HEADINGS = {
    "參考來源", "相關實體", "相關議題", "歷史記錄", "時序", "摘要", "現況",
    "目前結論", "技術彙整", "核心功能", "使用指南", "懸置細節", "選型細節",
}
DATE_HEADING_RE = re.compile(r"^\d{4}-\d{2}(-\d{2})?\b")


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def _slug(f: Path) -> str:
    return f.relative_to(WIKI_DIR).as_posix()[:-3]


def _pages() -> dict[str, Path]:
    out = {}
    for f in WIKI_DIR.rglob("*.md"):
        s = _slug(f)
        if s in EXCLUDE_PAGES or s.startswith("_views/"):
            continue
        out[s] = f
    return out


def _clean(target: str) -> str:
    return target.strip().strip("\\")


class Link:
    __slots__ = ("src", "dst", "line", "heading", "zone")

    def __init__(self, src, dst, line, heading, zone):
        self.src, self.dst, self.line, self.heading, self.zone = src, dst, line, heading, zone


def _semantic_heading(headings: list[tuple[int, str]], line: int) -> str:
    """回傳 line 所屬的最近「語意」標題（模板/日期標題上捲到前一個語意標題）。"""
    best = ""
    for h_line, title in headings:
        if h_line > line:
            break
        bare = title.strip().strip("`")
        if bare in TEMPLATE_HEADINGS or DATE_HEADING_RE.match(bare):
            continue
        best = bare
    return best


def _parse_page(slug: str, f: Path):
    """回傳 (headings[(line, title, level)], links[Link])。"""
    text = strip_pending_probes(strip_body(f.read_text(encoding="utf-8-sig")))
    lines = text.split("\n")
    headings: list[tuple[int, str]] = []      # (line_no, title)
    h2_zones: list[tuple[int, str]] = []      # (line_no, h2_title)
    for i, ln in enumerate(lines, 1):
        m = re.match(r"^(#{2,4})\s+(.+?)\s*$", ln)
        if m:
            title = m.group(2).strip().strip("`").split(" `[")[0]
            headings.append((i, title))
            if len(m.group(1)) == 2:
                h2_zones.append((i, title))
    links: list[Link] = []
    for i, ln in enumerate(lines, 1):
        anchored_spans = [m.span() for m in ANCHORED_WIKILINK_RE.finditer(ln)]
        for m in WIKILINK_RE.finditer(ln):
            dst = _clean(m.group(1))
            if dst.startswith("news/") or dst in EXCLUDE_PAGES:
                continue
            zone = "正文"
            for h_line, h_title in h2_zones:
                if h_line > i:
                    break
                zone = "樣板" if h_title in TEMPLATE_ZONE_H2 else "正文"
            if any(a <= m.start() < b for a, b in anchored_spans):
                zone = "錨點"
            if ln.lstrip().startswith("**上層"):
                zone = "階層"  # 子故事的 part-of 邊（2026-09-03），與引用邊分型：cluster／孤島不計
            links.append(Link(slug, dst, i, _semantic_heading(headings, i), zone))
    return headings, links


def build():
    pages = _pages()
    all_links: list[Link] = []
    headings_by_page: dict[str, list[tuple[int, str]]] = {}
    for slug, f in pages.items():
        hs, ls = _parse_page(slug, f)
        headings_by_page[slug] = hs
        all_links.extend(l for l in ls if l.dst in pages)
    return pages, headings_by_page, all_links


def _domain(f: Path) -> str:
    for ln in f.read_text(encoding="utf-8-sig").split("\n")[:40]:
        if ln.startswith("**領域：**"):
            return ln.replace("**領域：**", "").strip()
        m = re.match(r'^domain:\s*"?(.+?)"?\s*$', ln)
        if m:
            return m.group(1)
    return "—"


def cmd_explain(target: str, out) -> int:
    pages, _, links = build()
    if target not in pages:
        cands = [s for s in pages if target in s]
        print(f"找不到頁 {target}" + (f"；相近：{cands[:5]}" if cands else ""), file=out)
        return 1
    outbound = [l for l in links if l.src == target]
    inbound = [l for l in links if l.dst == target]
    print(f"# {target}（出 {len(outbound)} ／ 入 {len(inbound)}）\n", file=out)
    for name, group in (("出邊（本頁引用誰）", outbound), ("入邊（誰引用本頁）", inbound)):
        print(f"## {name}", file=out)
        by_zone: dict[str, list[Link]] = defaultdict(list)
        for l in group:
            by_zone[l.zone].append(l)
        for zone in ("正文", "錨點", "階層", "樣板"):
            for l in sorted(by_zone.get(zone, []), key=lambda x: (x.src, x.line)):
                other = l.dst if name.startswith("出") else l.src
                sec = f" § {l.heading}" if l.heading else ""
                print(f"  [{zone}] {other}（{sec.strip() or '—'} :L{l.line}）", file=out)
        print(file=out)
    return 0


def cmd_path(a: str, b: str, out) -> int:
    pages, _, links = build()
    adj: dict[str, set[str]] = defaultdict(set)
    for l in links:
        if l.zone != "樣板":
            adj[l.src].add(l.dst)
            adj[l.dst].add(l.src)
    if a not in pages or b not in pages:
        print(f"頁不存在：{[x for x in (a, b) if x not in pages]}", file=out)
        return 1
    prev = {a: None}
    q = deque([a])
    while q:
        cur = q.popleft()
        if cur == b:
            break
        for nxt in sorted(adj[cur]):
            if nxt not in prev:
                prev[nxt] = cur
                q.append(nxt)
    if b not in prev:
        print(f"{a} 與 {b} 在正文邊上不連通（樣板區邊不計）", file=out)
        return 1
    path = []
    cur = b
    while cur:
        path.append(cur)
        cur = prev[cur]
    print(" → ".join(reversed(path)), file=out)
    return 0


def cmd_sections(keyword: str, out) -> int:
    pages, headings_by_page, _ = build()
    hits = []
    for slug, f in pages.items():
        text = strip_body(f.read_text(encoding="utf-8-sig"))
        for i, ln in enumerate(text.split("\n"), 1):
            if keyword.lower() in ln.lower():
                sec = _semantic_heading(headings_by_page[slug], i)
                hits.append((slug, sec, i))
    seen = set()
    hot, cold = [], []
    for slug, sec, line in hits:
        key = (slug, sec)
        if key in seen:
            continue
        seen.add(key)
        row = f"{slug} § {sec or '(頁首)'} :L{line}"
        (cold if "-archive" in slug else hot).append(row)
    for row in hot:
        print(row, file=out)
    if cold:
        print("\n──（封存細節層，要看原始條目再下鑽）──", file=out)
        for row in cold:
            print(row, file=out)
    print(f"\n{len(seen)} 節命中（關鍵詞「{keyword}」，同節只列首見行；重點頁在前、封存頁在後）", file=out)
    return 0


def cmd_cluster(out) -> int:
    pages, _, links = build()
    w: dict[frozenset, int] = defaultdict(int)
    for l in links:
        if l.zone not in ("樣板", "階層") and l.src != l.dst:  # 家族邊不參與分群，否則親屬互連淹掉主題結構
            w[frozenset((l.src, l.dst))] += 1
    adj: dict[str, dict[str, int]] = defaultdict(dict)
    for pair, n in w.items():
        x, y = sorted(pair)
        adj[x][y] = n
        adj[y][x] = n
    label = {s: s for s in pages}
    for _ in range(20):
        changed = 0
        for node in sorted(pages):
            if not adj[node]:
                continue
            score: dict[str, int] = defaultdict(int)
            for nb, n in adj[node].items():
                score[label[nb]] += n
            best = max(sorted(score), key=lambda k: score[k])
            if best != label[node]:
                label[node] = best
                changed += 1
        if not changed:
            break
    groups: dict[str, list[str]] = defaultdict(list)
    for node, lab in label.items():
        groups[lab].append(node)
    doms = {s: _domain(f) for s, f in pages.items()}
    print("# 頁層分群（label propagation，樣板邊不計）vs 人工領域欄\n", file=out)
    mism = []
    for lab, members in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        if len(members) == 1:
            continue
        dom_count: dict[str, int] = defaultdict(int)
        for m in members:
            dom_count[doms[m]] += 1
        major = max(dom_count, key=lambda k: dom_count[k])
        print(f"群（{len(members)} 頁，主領域 {major}）: {', '.join(sorted(members))}", file=out)
        for m in members:
            if doms[m] != major:
                mism.append((m, doms[m], major))
    singles = [m for lab, ms in groups.items() if len(ms) == 1 for m in ms]
    print(f"\n孤立頁（無正文入出邊或自成一群，{len(singles)}）: {', '.join(sorted(singles))}", file=out)
    print("\n## 領域 vs 分群不一致（wikilink 稀疏或領域可疑的訊號）", file=out)
    for m, d, major in mism:
        print(f"  {m}：領域 {d}，但落在主領域 {major} 的群", file=out)
    if not mism:
        print("  （無）", file=out)
    return 0


def cmd_sources(target: str, out) -> int:
    import json
    ledger = WIKI_DIR.parent / "data" / "source_attribution.jsonl"
    if not ledger.exists():
        print(f"帳本不存在：{ledger}", file=out)
        return 1
    rows = []
    for ln in ledger.read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        try:
            r = json.loads(ln)
        except ValueError:
            continue
        if r.get("page") == target:
            rows.append(r)
    if not rows:
        print(f"{target} 在帳本無歸因（帳本 2026-07-11 起收；更早的事實走日報：頁內時序找日期 → news/該日.md）", file=out)
        return 0
    rows.sort(key=lambda r: r.get("date", ""), reverse=True)
    print(f"# {target} 的來源歸因（{len(rows)} 筆，新到舊）\n", file=out)
    for r in rows:
        print(f"{r.get('date','—')}｜{r.get('source','—')}｜{r.get('item_title','—')}", file=out)
        print(f"    {r.get('item_url','—')}", file=out)
    return 0



# ── 相似度／缺口：加權 Jaccard（鄰居權重 1/度數，樞紐不霸榜）──────────────────
def _neighbor_sets(links, pages):
    """正文引用邊的無向鄰居表（樣板／階層邊不算：相關實體欄與家族邊不是語意證據）。"""
    adj: dict[str, set] = defaultdict(set)
    linked: set = set()
    for l in links:
        if l.src == l.dst or l.src not in pages or l.dst not in pages:
            continue
        linked.add(frozenset((l.src, l.dst)))          # 任何 zone 的邊都算「已相連」
        if l.zone in ("樣板", "階層"):
            continue
        adj[l.src].add(l.dst)
        adj[l.dst].add(l.src)
    return adj, linked


def weighted_jaccard(a: str, b: str, adj) -> float:
    na, nb = adj.get(a, set()), adj.get(b, set())
    if not na or not nb:
        return 0.0
    w = lambda n: 1.0 / max(1, len(adj.get(n, ())))
    inter = sum(w(n) for n in na & nb)
    union = sum(w(n) for n in na | nb)
    return inter / union if union else 0.0


MIN_SHARED = 2      # 只共享一個鄰居（通常是樞紐）不算相似——兩個人物頁都連 anthropic-business 曾拿到 1.0
MIN_DEGREE = 3      # 太孤的頁沒有足夠證據談相似
_ARCHIVE_RE = re.compile(r"(^|/)[^/]*archive")


def similar_pages(target: str, pages, links, top: int = 3, min_score: float = 0.08, doms=None):
    """回傳 [(slug, score, shared_neighbors)]：不直接相連、共享鄰居多者優先；封存頁不推。"""
    adj, linked = _neighbor_sets(links, pages)
    out = []
    for other in pages:
        if other == target or frozenset((target, other)) in linked or _ARCHIVE_RE.search(other):
            continue
        shared = adj[target] & adj[other]
        if len(shared) < MIN_SHARED or len(adj[other]) < MIN_DEGREE:
            continue
        s = weighted_jaccard(target, other, adj)
        if doms and doms.get(target) and doms.get(target) == doms.get(other):
            s *= 1.3   # 同領域微加權：讀者順著同一條線往下讀的機率較高
        if s >= min_score:
            out.append((other, s, sorted(shared)))
    out.sort(key=lambda x: -x[1])
    return out[:top]


def gap_pairs(pages, links, top: int = 10, min_score: float = 0.15):
    import json
    ignore_file = WIKI_DIR.parent / "data" / "graph_gap_ignore.json"
    ignored = set()
    if ignore_file.exists():
        for pr in json.loads(ignore_file.read_text(encoding="utf-8")).get("pairs", []):
            ignored.add(frozenset(pr["pages"]))
    adj, linked = _neighbor_sets(links, pages)
    out = []
    slugs = sorted(pages)
    for i, a in enumerate(slugs):
        for b in slugs[i + 1:]:
            key = frozenset((a, b))
            if key in linked or key in ignored or _ARCHIVE_RE.search(a) or _ARCHIVE_RE.search(b):
                continue
            if len(adj[a] & adj[b]) < MIN_SHARED or min(len(adj[a]), len(adj[b])) < MIN_DEGREE:
                continue
            s = weighted_jaccard(a, b, adj)
            if s >= min_score:
                out.append((a, b, s, sorted(adj[a] & adj[b])))
    out.sort(key=lambda x: -x[2])
    return out[:top], len(ignored)


def cmd_similar(target: str, out) -> int:
    pages, _, links = build()
    if target not in pages:
        print(f"找不到頁面：{target}", file=out)
        return 1
    rows = similar_pages(target, pages, links, top=5, doms={s: _domain(f) for s, f in pages.items()})
    print(f"# 你可能也想看（與 {target} 不直接相連、共享鄰居多）\n", file=out)
    if not rows:
        print("（無達標候選）", file=out)
    for slug, s, shared in rows:
        print(f"  {slug}  {s:.2f}  共享：{', '.join(shared[:4])}{' …' if len(shared) > 4 else ''}", file=out)
    return 0


def cmd_gaps(rest: list[str], out) -> int:
    top = 10
    if "--top" in rest:
        top = int(rest[rest.index("--top") + 1])
    pages, _, links = build()
    rows, n_ign = gap_pairs(pages, links, top=top)
    doms = {s: _domain(f) for s, f in pages.items()}
    print(f"# 缺口偵測：分數高卻互不相連的頁對（前 {top}；已忽略 {n_ign} 對）\n", file=out)
    print("| 頁 A | 頁 B | 分數 | 共享鄰居 |\n|---|---|---|---|", file=out)
    for a, b, s, shared in rows:
        print(f"| {a}（{doms[a]}） | {b}（{doms[b]}） | {s:.2f} | {', '.join(shared[:4])}{' …' if len(shared) > 4 else ''} |", file=out)
    if not rows:
        print("| （無候選） | | | |", file=out)
    print("\n每對三選一：補 wikilink／併頁或蒸餾候選／登記 data/graph_gap_ignore.json（已審、無需連結）。", file=out)
    return 0


def main() -> int:
    out = _stdout()
    args = sys.argv[1:]
    if not args:
        print(__doc__, file=out)
        return 0
    cmd, rest = args[0], args[1:]
    try:
        if cmd == "explain" and len(rest) == 1:
            return cmd_explain(rest[0], out)
        if cmd == "path" and len(rest) == 2:
            return cmd_path(rest[0], rest[1], out)
        if cmd == "sections" and len(rest) == 1:
            return cmd_sections(rest[0], out)
        if cmd == "cluster":
            return cmd_cluster(out)
        if cmd == "sources" and len(rest) == 1:
            return cmd_sources(rest[0], out)
        if cmd == "similar" and len(rest) == 1:
            return cmd_similar(rest[0], out)
        if cmd == "gaps":
            return cmd_gaps(rest, out)
        print(__doc__, file=out)
        return 1
    finally:
        out.flush()


if __name__ == "__main__":
    sys.exit(main())
