#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""子故事階層（part-of 樹）的機械檢查——2026-09-03 設計 reviewer 列出的「會靜默壞」項目全部在此變成會紅的檢查。

階層的單一來源是頁面標頭一行 `**上層：** [[topics/xxx]]`（frontmatter 的 parent 由它生成）。
本檔驗的是「階層存在但沒人看得出壞掉」的形狀：

  1. 扁平放置    子頁一律扁平放在 entities/ 或 topics/——四支腳本用非遞迴 glob、兩支用 rglob，
                 子目錄裡的頁會被一半機制看見、一半看不見，且沒有任何一處報錯
  2. 上層有效    上層必須是存在的頁、不可指向自己、不可成環（樹，不是 DAG）
  3. 領域繼承    子頁領域＝母頁領域——懸置命中靠頁面領域派記者，子頁領域寫錯就永遠派錯且看起來「無命中」
  4. archive 掛父 slug 含 -archive 的頁必須有上層（封存頁掛在它封存的頁底下，不參與三題），
                 且狀態必須是 `resolved（封存頁）`——證據層頁若掛著 ongoing／monitoring，會被過期議題
                 掃描與訊號排序當成活躍頁追殺，也讓讀者以為那是還在更新的敘事
  5. hub 不落後  母頁 callout 日期 ≥ 子樹最新「最後新聞更新」——母頁自身的「最後新聞更新」不因子頁動
                 （動了會與 freshness 第 2 類互斥、擋 web build），改驗 callout（本來就每日覆寫）
  6. index 投影  子頁不入 index 目錄表，但母頁該列的摘要格必須帶 `↳ 子故事：[[a]]、[[b]]` 投影
                 （由 gen_wiki_frontmatter.py 生成；本檔只驗）——查詢入口與記者認領靠它，不靠記者自己遍歷
  7. 併回殼      帶上層且正文含「已併回」的頁是 redirect 殼，允許只有標頭，跳過 5/6

純標準庫、零網路。用法：python scripts/check_hierarchy.py [wiki_dir]
exit 0＝通過；1＝違規（列出項目）。無任何階層時印「無階層頁面」並 exit 0。
"""
import io
import re
import sys
from pathlib import Path

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"

PARENT_RE = re.compile(r"^\*\*上層[：:]\*\*\s*\[\[([^\]|#]+)", re.M)
DOMAIN_RE = re.compile(r"^\*\*領域[：:]\*\*\s*(.+?)\s*$", re.M)
STATUS_RE = re.compile(r"^\*\*狀態[：:]\*\*\s*(.+?)\s*$", re.M)
LAST_NEWS_RE = re.compile(r"^\*\*最後新聞更新[：:]\*\*\s*(\d{4}-\d{2}-\d{2})", re.M)
CALLOUT_DATE_RE = re.compile(r"^> \*\*[^\n]*?（(\d{4}-\d{2}-\d{2})）", re.M)
INDEX_ROW_RE = re.compile(r"^\|\s*\[\[([^\]|#]+)\]\]\s*\|(.*)\|\s*$")
CHILDREN_SEG_RE = re.compile(r"↳ 子故事：(.*)$")


def page_info(path: Path, wiki_dir: Path) -> dict:
    text = path.read_text(encoding="utf-8-sig")
    head = "\n".join(text.splitlines()[:60])
    m = PARENT_RE.search(head)
    d = DOMAIN_RE.search(head)
    st = STATUS_RE.search(head)
    ln = LAST_NEWS_RE.search(head)
    cd = CALLOUT_DATE_RE.search(head)
    return {
        "slug": path.relative_to(wiki_dir).as_posix()[:-3],
        "parent": m.group(1).strip() if m else None,
        "domain": d.group(1).strip() if d else "",
        "status": st.group(1).strip() if st else "",
        "last_news": ln.group(1) if ln else "",
        "callout_date": cd.group(1) if cd else "",
        "redirect": bool(m) and "已併回" in head,
    }


def load(wiki_dir: Path) -> tuple[dict, list[str]]:
    """回傳 ({slug: info}, fails_from_flatness)。"""
    fails = []
    flat = set()
    for sub in ("entities", "topics"):
        for p in (wiki_dir / sub).glob("*.md"):
            flat.add(p)
    deep = set()
    for sub in ("entities", "topics"):
        for p in (wiki_dir / sub).rglob("*.md"):
            deep.add(p)
    for p in sorted(deep - flat):
        fails.append(f"非扁平：{p.relative_to(wiki_dir).as_posix()} 在子目錄，半數機制看不見它")
    pages = {}
    for p in sorted(flat):
        info = page_info(p, wiki_dir)
        pages[info["slug"]] = info
    return pages, fails


def index_children_projection(wiki_dir: Path) -> dict[str, set[str]]:
    """讀 index.md 每列摘要格的「↳ 子故事：」投影 → {hub: {child slugs}}。"""
    out: dict[str, set[str]] = {}
    idx = wiki_dir / "index.md"
    if not idx.exists():
        return out
    for line in idx.read_text(encoding="utf-8-sig").splitlines():
        m = INDEX_ROW_RE.match(line)
        if not m:
            continue
        seg = CHILDREN_SEG_RE.search(m.group(2))
        if seg:
            out[m.group(1).strip()] = set(re.findall(r"\[\[([^\]|#]+)\]\]", seg.group(1)))
    return out


def check(wiki_dir: Path = WIKI_DIR) -> tuple[list[str], int]:
    pages, fails = load(wiki_dir)
    children: dict[str, list[str]] = {}
    for slug, info in pages.items():
        par = info["parent"]
        if not par:
            continue
        if par == slug:
            fails.append(f"上層指向自己：{slug}")
            continue
        if par not in pages:
            fails.append(f"上層不存在：{slug} → [[{par}]]")
            continue
        children.setdefault(par, []).append(slug)
    # 成環
    for slug in pages:
        seen, cur = set(), slug
        while cur and pages.get(cur, {}).get("parent"):
            if cur in seen:
                fails.append(f"上層成環：{slug} 的祖先鏈回到 {cur}")
                break
            seen.add(cur)
            cur = pages[cur]["parent"]
    # 領域繼承、archive 掛父
    for slug, info in pages.items():
        par = info["parent"]
        if par and par in pages and info["domain"] and pages[par]["domain"] and info["domain"] != pages[par]["domain"]:
            fails.append(f"領域未繼承：{slug}『{info['domain']}』≠ 上層 {par}『{pages[par]['domain']}』")
        if "-archive" in slug.split("/")[-1]:
            if not par:
                fails.append(f"archive 未掛父：{slug} 缺「上層」欄（封存頁必須掛在它封存的頁底下）")
            if "封存頁" not in info["status"]:
                fails.append(
                    f"archive 狀態非封存頁：{slug}『{info['status'] or '缺'}』"
                    "（封存頁狀態須為 resolved（封存頁），否則會被過期掃描與訊號排序當活躍頁）"
                )
    # hub 不落後、index 投影
    proj = index_children_projection(wiki_dir)
    for hub, kids in children.items():
        real_kids = [k for k in kids if not pages[k]["redirect"]]
        newest = max((pages[k]["last_news"] for k in real_kids if pages[k]["last_news"]), default="")
        cd = pages[hub]["callout_date"]
        if newest and (not cd or cd < newest):
            fails.append(f"hub 落後：{hub} callout 日期 {cd or '缺'} < 子樹最新新聞 {newest}（母頁 callout 須跟上子頁）")
        listed = proj.get(hub, set())
        # redirect 殼不進投影（`[加入: 2026-09-06]`，見 gen_wiki_frontmatter.py 同步）——
        # 併回的空殼對讀者無內容價值，不該出現在母頁「↳ 子故事：」
        missing = sorted(set(real_kids) - listed)
        if missing:
            fails.append(f"index 投影缺子頁：{hub} 列的「↳ 子故事：」未含 {missing}（跑 python scripts/gen_wiki_frontmatter.py 生成）")
    return fails, len(children)


def main() -> int:
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    wiki = Path(sys.argv[1]) if len(sys.argv) > 1 else WIKI_DIR
    fails, n_hubs = check(wiki)
    print("# check_hierarchy.py（子故事階層：扁平／上層有效／領域繼承／archive 掛父／hub 不落後／index 投影）")
    if fails:
        for f in fails:
            print(f"  ❌ {f}")
        print(f"狀態：❌ {len(fails)} 項違規")
        return 1
    print(f"狀態：✅ 通過（{n_hubs} 個母頁）" if n_hubs else "狀態：✅ 無階層頁面（尚未升格任何子故事）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
