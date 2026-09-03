"""Wiki 頁面新鮮度宣稱 × 歸因記錄的交叉檢查。

每個 entities/ topics/ 頁面標頭都宣稱「最後新聞更新」＝這頁上次因新聞而長出內容的
日期。這個宣稱是讀者與 lint 判斷頁面死活的唯一依據，但它是**手填的**——填錯或漏填
都不會有任何症狀，頁面照常渲染、鏈結照常有效，只是新鮮度永遠說謊。

`data/source_attribution.jsonl` 是同一件事的另一份獨立記錄（哪則新聞、哪天、寫進哪頁），
兩者本該對得上。對不上就是缺陷，本檔把三種對不上的形狀變成會紅的測試：

  1. 漏更      歸因說某日有新聞落地該頁，頁面「最後新聞更新」卻早於那天
               → 新聞進來了、欄位沒跟著動（2026-08-05 首次發現：recursive-self-improvement
                 把欄位填成事件發生日 07-13，而非日報日 07-14，規則要的是後者）
  2. 無從對照  頁面宣稱近期有新聞更新，歸因卻從無任何一筆
               → 要嘛記者漏報歸因，要嘛這頁根本不吃新聞（衍生頁，須明文宣告）
  3. 欄位缺失  標頭根本沒有「最後新聞更新」

第 2 類的白名單即**觸發邊清冊的機器可讀版本**：一個頁面若不吃新聞條目，它就必須吃
別的東西（別的頁面、lint 策展），而那條邊必須在規則檔裡有明文出處——沒有出處的
衍生頁會孤兒化（2026-07-26 建立的 community-large-codebase-workflow 因此空轉 10 天）。
新增衍生頁時同步在 DERIVED_PAGES 登記，登記時必須填得出 rule 欄位。

欄位語意（`.claude/rules/wiki-reporter-shared.md`）：「最後新聞更新」填**日報日期**，
不是新聞事件發生日。兩者常差一天，是第 1 類缺陷的主要來源。

用法：
    python scripts/check_wiki_freshness.py            # 以今日為基準
    python scripts/check_wiki_freshness.py 2026-08-05 # 指定基準日（測試用）

全部通過 exit 0；任一類命中 exit 1。
"""

from __future__ import annotations

import io
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
ATTRIBUTION = REPO_ROOT / "data" / "source_attribution.jsonl"

# 歸因機制上線日。此日之前的頁面更新沒有歸因記錄可對照，一律豁免。
ATTRIBUTION_START = "2026-07-11"

# 第 2 類的新鮮度窗：只有宣稱「近期」有新聞更新才需要歸因佐證。
# 更早的日期屬休眠，無從對照是正常的（該頁本來就沒有新東西）。
RECENT_DAYS = 14

# 衍生頁：不吃新聞條目，吃別的頁面或 lint 策展，故天生零歸因。
# rule 欄位＝該頁觸發邊的明文出處，登記時必須填得出來，否則不得列入。
DERIVED_PAGES = {
    "topics/coding-workflow-guide":
        ".claude/rules/wiki-ingest-features.md（週更，吃官方技能清冊與社群工具策展，非新聞條目）",
    "topics/community-tech-tools":
        ".claude/rules/wiki-ingest-community-lint.md（週策展，讀近 7–14 天日報）",
    "topics/community-pattern-trends":
        ".claude/rules/wiki-ingest-community-lint.md（週更，讀 patterns 頁）",
    "topics/community-large-codebase-workflow":
        ".claude/rules/wiki-ingest-community-lint.md 週更整線重寫（吃 patterns 頁"
        "帶 `**主線：**` tag 的節點；每日 ingest 只標 tag、不寫此頁）",
    "topics/official-community-gap":
        ".claude/rules/wiki-ingest-features.md 產品化矩陣同步",
    "topics/anthropic-commitments":
        ".claude/rules/wiki-ingest.md 第三步（主編彙整）",
    "topics/model-task-leaderboard":
        ".claude/rules/wiki-ingest-models.md 例外條（吃外部榜單網站，"
        "由 /wiki-lint 步驟 5b 抓取；每日 ingest 不更新）",
    "topics/engineering-skill-playbook":
        ".claude/rules/wiki-ingest-features.md「工程流程 Skill 指南維護」"
        "（週更，讀官方 skills repo 清冊，非新聞條目；每日 ingest 不更新）",
    "topics/skill-interest-watch":
        ".claude/rules/wiki-ingest-community-lint.md「skill-interest-watch：機器快照頁」"
        "（每日由 scripts/skill_interest_snapshot.py 覆寫，吃 GitHub Search 非新聞條目；"
        "2026-09-02 建頁時漏登記，擋掉當日雲端 web build——教訓見同日 log）",
}

LAST_NEWS_RE = re.compile(r"^\*\*最後新聞更新：\*\*\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)


def _stdout():
    """Windows 主控台預設 cp950，直接 print 狀態符號會 UnicodeEncodeError（同 check_rules.py）。"""
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def load_last_attribution() -> dict[str, str]:
    """每頁最後一筆歸因的日報日期。歸因檔不存在時回傳空 dict（視同全部豁免）。"""
    last: dict[str, str] = {}
    if not ATTRIBUTION.exists():
        return last
    with ATTRIBUTION.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                # 壞行不讓整個檢查停擺，但要說出來——它代表 append 流程出過問題
                print(f"WARN: {ATTRIBUTION.name}:{line_no} 非合法 JSON，已略過")
                continue
            page, d = row.get("page"), row.get("date")
            if page and d:
                last[page] = max(last.get(page, ""), d)
    return last


UPDATE_FREQ_RE = re.compile(r"^\*\*更新頻率：\*\*", re.MULTILINE)


def scan_pages() -> list[tuple[str, str | None]]:
    """回傳 (頁面相對路徑不含 .md, 最後新聞更新日期 or None)。"""
    out = []
    for sub in ("entities", "topics"):
        for path in sorted((WIKI_DIR / sub).glob("*.md")):
            slug = f"{sub}/{path.stem}"
            m = LAST_NEWS_RE.search(path.read_text(encoding="utf-8"))
            out.append((slug, m.group(1) if m else None))
    return out


def unregistered_derived_pages() -> list[str]:
    """標頭有「更新頻率」欄（週更／機器快照＝不吃日報條目）卻未登記 DERIVED_PAGES 的頁。

    2026-09-02 教訓：skill-interest-watch 建頁當天沒登記，當晚雲端 web build gate
    被本檢查擋下、網站停一天。「更新頻率」欄本身就是「本頁不走每日 ingest」的宣告，
    宣告了卻沒登記觸發邊，等於建頁者自己都說不出這頁靠什麼更新——當場擋，不等
    第一次跑 gate 才發現。
    """
    out = []
    for sub in ("entities", "topics"):
        for path in sorted((WIKI_DIR / sub).glob("*.md")):
            slug = f"{sub}/{path.stem}"
            if UPDATE_FREQ_RE.search(path.read_text(encoding="utf-8")) and slug not in DERIVED_PAGES:
                out.append(slug)
    return out


def main(argv: list[str]) -> int:
    stream = _stdout()
    today = date.fromisoformat(argv[1]) if len(argv) > 1 else date.today()
    recent_cutoff = (today - timedelta(days=RECENT_DAYS)).isoformat()

    last_att = load_last_attribution()
    stale_updates: list[str] = []
    unverifiable: list[str] = []
    missing_field: list[str] = []

    # 階層（2026-09-03）：母頁（有子頁者）的歸因會落在子頁——第 2 類對母頁改看子樹歸因，
    # 否則母頁 bump 日期就紅、擋 web build（母不落後子 × 唯讀 × 本檢查三者互斥，reviewer B1）。
    parent_re = re.compile(r"^\*\*上層[：:]\*\*\s*\[\[([^\]|#]+)", re.MULTILINE)
    children: dict[str, list[str]] = {}
    for sub in ("entities", "topics"):
        for path in (WIKI_DIR / sub).glob("*.md"):
            m = parent_re.search("\n".join(path.read_text(encoding="utf-8").splitlines()[:60]))
            if m:
                children.setdefault(m.group(1).strip(), []).append(f"{sub}/{path.stem}")

    def subtree_att(slug: str) -> str:
        best = last_att.get(slug, "")
        stack = list(children.get(slug, []))
        while stack:
            k = stack.pop()
            best = max(best, last_att.get(k, ""))
            stack.extend(children.get(k, []))
        return best

    for slug, last_news in scan_pages():
        if last_news is None:
            missing_field.append(slug)
            continue

        att = last_att.get(slug)
        if slug in children:
            att = subtree_att(slug) or None
        if att:
            # 1. 漏更：歸因記錄比頁面宣稱新
            if last_news < att:
                stale_updates.append(
                    f"{slug}：頁面宣稱 {last_news}，但 {att} 日報有條目落地此頁"
                )
        elif last_news >= max(recent_cutoff, ATTRIBUTION_START) and slug not in DERIVED_PAGES:
            # 2. 無從對照：宣稱近期有新聞更新，卻從無任何歸因
            unverifiable.append(
                f"{slug}：頁面宣稱 {last_news} 有新聞更新，但歸因記錄從無此頁"
            )

    ok = True
    if missing_field:
        ok = False
        stream.write(f"\n[缺欄位] {len(missing_field)} 頁沒有「最後新聞更新」：\n")
        for s in missing_field:
            stream.write(f"  - {s}\n")

    if stale_updates:
        ok = False
        stream.write(f"\n[漏更] {len(stale_updates)} 頁的新鮮度落後歸因記錄：\n")
        for s in stale_updates:
            stream.write(f"  - {s}\n")
        stream.write("  修法：把該頁「最後新聞更新」補為該筆歸因的日報日期"
                     "（填日報日，不是事件發生日）\n")

    unregistered = unregistered_derived_pages()
    if unregistered:
        ok = False
        stream.write(f"\n[未登記衍生頁] {len(unregistered)} 頁標頭宣告「更新頻率」卻未登記 DERIVED_PAGES：\n")
        for s in unregistered:
            stream.write(f"  - {s}\n")
        stream.write("  修法：在本檔 DERIVED_PAGES 登記並填得出觸發邊的規則檔出處"
                     "（建頁當天就做，不等 gate 擋）\n")

    if unverifiable:
        ok = False
        stream.write(f"\n[無從對照] {len(unverifiable)} 頁宣稱近期有新聞更新卻零歸因：\n")
        for s in unverifiable:
            stream.write(f"  - {s}\n")
        stream.write("  修法：屬記者漏報歸因 → 補 data/source_attribution.jsonl；\n"
                     "        屬不吃新聞的衍生頁 → 在本檔 DERIVED_PAGES 登記，"
                     "並填得出觸發邊的規則檔出處\n")

    if ok:
        n = len(scan_pages())
        stream.write(
            f"OK: wiki 新鮮度檢查通過（{n} 頁；衍生頁 {len(DERIVED_PAGES)} 頁已宣告觸發邊）\n"
        )
    stream.flush()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
