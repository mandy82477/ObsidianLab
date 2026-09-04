#!/usr/bin/env python3
"""
build_web.py — converts wiki/*.md + news/*.md → web_reader/data/data.js

Usage:
    python scripts/build_web.py

Output:
    web_reader/data/data.js   (window.WIKI_DATA + window.DIGEST_ALL)
"""

import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_DIR      = ROOT / "wiki"
WIKI_ENTITIES = ROOT / "wiki" / "entities"
WIKI_TOPICS   = ROOT / "wiki" / "topics"
WIKI_RADAR    = ROOT / "wiki" / "feature-radar.md"
NEWS_DIR      = ROOT / "news"
WEEKLY_DIR    = ROOT / "weekly"
OUT_JS           = ROOT / "web_reader" / "data" / "data.js"
OUT_WIKI_DIR     = ROOT / "web_reader" / "data" / "wiki"
OUT_DIGEST_DIR   = ROOT / "web_reader" / "data" / "digest"
OUT_WEEKLY_DIR   = ROOT / "web_reader" / "data" / "weekly"
OUT_SEARCH_INDEX = ROOT / "web_reader" / "data" / "search-index.json"

# ── Markdown 讀取（統一剝除 YAML frontmatter）──────────────────────────────

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)


def read_md(f: Path) -> str:
    """讀 markdown 並剝掉檔頭 YAML frontmatter。

    wiki 頁面的 frontmatter 由 scripts/gen_wiki_frontmatter.py 生成，是給 Obsidian
    Bases 查詢用的機器投影，**不是給讀者看的內容**。若不在此剝除，下游 md_to_text()
    的 `^---+$` 規則只會抹掉兩條分隔線、把 `type: model` 這類欄位留在正文裡，直接
    外洩到網站頁面與搜尋索引。

    對沒有 frontmatter 的檔案（news/、weekly/、以及尚未生成的頁面）為 no-op。
    """
    return FRONTMATTER_RE.sub("", f.read_text(encoding="utf-8-sig"), count=1)


# ── Markdown → plain text (for search index) ────────────────────────────────

def strip_markdown_to_text(md: str) -> str:
    """Strip markdown syntax to plain searchable text."""
    text = md
    # Remove fenced code blocks (keep content — useful for command search)
    text = re.sub(r'```\w*\n?', '', text)
    # Remove inline code backticks (keep text)
    text = re.sub(r'`([^`\n]+)`', r'\1', text)
    # Remove heading markers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove bold/italic markers (keep text)
    text = re.sub(r'\*{1,3}([^*\n]+)\*{1,3}', r'\1', text)
    # Remove wiki links [[page]] or [[page|label]] → keep label or page name
    text = re.sub(r'\[\[(?:[^\]|]+\|)?([^\]]+)\]\]', r'\1', text)
    # Remove markdown links [text](url) → keep text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove table separator rows
    text = re.sub(r'^\|[-:| ]+\|$', '', text, flags=re.MULTILINE)
    # Replace table pipes with space
    text = re.sub(r'\|', ' ', text)
    # Remove horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)
    # Collapse whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    return text.strip()


# ── Status → CSS pill class ──────────────────────────────────────────────────

STATUS_MAP = {
    "active":      "active",
    "ongoing":     "active",
    "beta":        "info",
    "monitoring":  "warn",
    "deprecated":  "danger",
    "acquired":    "gray",
    "resolved":    "gray",
}


def pill_class(status: str) -> str:
    # 只取「（」之前的主值再匹配，忽略括號內的補充說明
    s = re.split(r"[（(]", status.strip())[0].strip().lower()
    return STATUS_MAP.get(s, "gray")


# ── Wiki page parser ─────────────────────────────────────────────────────────

META_RE = {
    "entityType": re.compile(r"\*\*類型[：:]\*\*\s*(.+)"),
    "type":       re.compile(r"\*\*類型[：:]\*\*\s*(.+)"),
    "status":     re.compile(r"\*\*狀態[：:]\*\*\s*(.+)"),
    "domain":     re.compile(r"\*\*領域[：:]\*\*\s*(.+)"),
    "firstSeen":  re.compile(r"\*\*首次出現[：:]\*\*\s*(.+)"),
    "startDate":  re.compile(r"\*\*開始日期[：:]\*\*\s*(.+)"),
    "lastUpdated":    re.compile(r"\*\*最後更新[：:]\*\*\s*(.+)"),
    "lastNewsUpdate": re.compile(r"\*\*最後新聞更新[：:]\*\*\s*(.+)"),
    "updateFreq":     re.compile(r"\*\*更新頻率[：:]\*\*\s*(.+)"),
    "parent":         re.compile(r"\*\*上層[：:]\*\*\s*\[\[([^\]|#]+)\]\]"),  # 子故事階層（2026-09-03）
}

SUMMARY_HEADERS = ["## 現況", "## 摘要"]

# 六個標準領域值（見 .claude/rules/wiki-ingest-format.md「命名與分類規則」）
VALID_DOMAINS = {"🤖 模型", "🛠️ 工具/功能", "👤 人物", "💼 商業", "🏛️ 政策/安全", "🌐 社群"}


def readable_inline(text: str) -> str:
    """把 wikilink / markdown link 轉為可讀文字，供列表 snippet 使用。

    直接刪除 [[...]] 會留下「本頁從 的具體模式中」這種懸空斷句（2026-07-28
    讀者 review 高影響項），故一律以顯示文字取代：
    [[a|b]] → b；[[topics/x]] → x（取末段）；[text](url) → text。
    """
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', lambda m: m.group(1).split('/')[-1], text)
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    return text


def latest_headline(raw: str) -> str:
    """Extract the most recent update headline from wiki markdown."""
    def clean_line(ls: str) -> str:
        text = re.sub(r'^-\s*', '', ls)           # strip leading "- "
        text = re.sub(r'^\*{0,2}\d{4}-\d{2}-\d{2}\*{0,2}\s*.?\s*', '', text)  # strip date (bold or plain) + any colon
        text = re.sub(r'^\*\*\[[^\]]*\]\*\*\s*', '', text)       # strip **[tag]**
        text = re.sub(r'\*{1,3}([^*\n]+)\*{1,3}', r'\1', text)  # strip bold/italic
        text = readable_inline(text)
        return text.strip()[:160]

    # Pattern 1: ## 歷史記錄 — "- YYYY-MM-DD：text"
    hist_m = re.search(r'##\s*歷史記錄\s*\n([\s\S]*?)(?:\n##|\n---|\Z)', raw)
    if hist_m:
        for line in hist_m.group(1).splitlines():
            ls = line.strip()
            if ls.startswith('- '):
                result = clean_line(ls)
                if result:
                    return result
    # Pattern 2: ## 時序 — "### YYYY-MM-DD\n- **[tag] description**"
    time_m = re.search(r'##\s*時序\s*\n([\s\S]*?)(?:\n##|\Z)', raw)
    if time_m:
        for line in time_m.group(1).splitlines():
            ls = line.strip()
            if ls.startswith('- '):
                result = clean_line(ls)
                if result:
                    return result
    # Pattern 3: ## 歷史記錄 table — "| YYYY-MM-DD | description |"
    hist_table_m = re.search(r'##\s*歷史記錄\s*\n([\s\S]*?)(?:\n##|\Z)', raw)
    if hist_table_m:
        for line in hist_table_m.group(1).splitlines():
            ls = line.strip()
            if not ls.startswith('|') or '|---' in ls or '日期' in ls:
                continue
            cols = [c.strip() for c in ls.strip('|').split('|')]
            if len(cols) >= 2 and re.match(r'\d{4}-\d{2}-\d{2}', cols[0]):
                text = re.sub(r'\*{1,3}([^*\n]+)\*{1,3}', r'\1', cols[1]).strip()
                text = readable_inline(text).strip()
                if text:
                    return text[:160]
    # Pattern 4: ## 現況 — first non-empty content line (strip bold markers)
    summary_m = re.search(r'##\s*(?:現況|摘要)\s*\n([\s\S]*?)(?:\n##|\Z)', raw)
    if summary_m:
        for line in summary_m.group(1).splitlines():
            ls = line.strip()
            if not ls or ls.startswith('#') or ls.startswith('---') or ls.startswith('|'):
                continue
            text = re.sub(r'\*{1,3}([^*\n]+)\*{1,3}', r'\1', ls).strip()
            text = readable_inline(text).strip()
            if text:
                return text[:160]
    return ''


def _fallback_summary_lines(raw: str) -> list[str]:
    """`## 現況`／`## 摘要` 都不在時的後備摘要來源。

    先取頂部 delta-first callout（`>` 引用區塊，格式規則要求 ongoing/monitoring 頁必備），
    取不到再退到第一段正文。兩者皆跳過標頭欄位、分隔線、標題、表格與程式碼區塊。
    """
    lines = raw.splitlines()
    callout: list[str] = []
    prose: list[str] = []
    in_code = False

    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s:
            # callout 收完就停：只要第一個引用區塊，不把後面的也吃進來
            if callout:
                break
            continue
        if s.startswith("#") or s.startswith("---") or s.startswith("|"):
            continue
        if re.match(r"\*\*[^*]+：\*\*", s):        # 標頭欄位（**狀態：** …）
            continue
        if s.startswith(">"):
            body = s.lstrip("> ").strip()
            # callout 首行是標籤（**最新動態**（2026-08-08）），內容在第二行起——標籤進了卡片
            # 只會佔掉 160 字裡的前 20 字卻不說明任何事
            if re.fullmatch(r"\*\*[^*]+\*\*(?:（[^）]*）|\([^)]*\))?", body):
                continue
            if body and not body.startswith("-"):
                callout.append(re.sub(r"\*{1,3}([^*\n]+)\*{1,3}", r"\1", body))
            continue
        if callout:
            break
        prose.append(s)
        if len(" ".join(prose)) >= 160:
            break

    return callout or prose



def safe_console(text: str) -> str:
    """把主控台編不出來的字元換掉。Windows 預設 cp950，訊息裡只要有 emoji 就會
    在 print 當下再拋一次例外，把原本的錯誤訊息整個蓋掉——2026-08-08 的頁面消失事故
    就是這樣變得無從診斷的。"""
    enc = (sys.stdout.encoding or "utf-8")
    return text.encode(enc, errors="replace").decode(enc, errors="replace")

def strip_llm_sections(md: str) -> str:
    """Remove any H2 section whose title contains '給 LLM' (and everything after it)."""
    return re.sub(r'\n## [^\n]*給 LLM[^\n]*\n[\s\S]*', '', md)


# ── Internal wikilink dead-link check ───────────────────────────────────────

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+?)(?:\\?#[^\]|]*)?(?:\\?\|[^\]]*)?\]\]')


def _clean_wikilink_target(raw_target: str) -> str:
    """Strip a trailing markdown-table escape backslash, e.g. 'entities/foo\\' → 'entities/foo'."""
    return raw_target.rstrip('\\').strip()


ANCHORED_WIKILINK_RE = re.compile(r'\[\[([^\]|#]+?)\\?#([^\]|]+?)(?:\\?\|[^\]]*)?\]\]')

HEADING_RE = re.compile(r'^#{2,4}\s+(.+?)\s*$', flags=re.MULTILINE)


def _page_file(target: str) -> Path | None:
    """Resolve a wikilink target (with or without directory prefix) to its .md file."""
    target = target.strip()
    candidates = [
        WIKI_DIR / f"{target}.md",
        WIKI_ENTITIES / f"{target}.md",
        WIKI_TOPICS / f"{target}.md",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def _headings_of(target: str) -> set[str] | None:
    """所有 h2–h4 標題文字（去掉粗體標記），查無頁面回傳 None。"""
    f = _page_file(target)
    if f is None:
        return None
    try:
        raw = read_md(f)
    except Exception:
        return None
    return {re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', h).strip() for h in HEADING_RE.findall(raw)}


def check_wikilink_anchors(all_md_files: list[Path]) -> int:
    """[[頁面#錨點]] 的錨點必須真的是目標頁的 h2–h4 標題，否則讀者點過去只會落在頁首。
    純頁面斷鏈由 check_wikilinks 負責，本函式只管錨點；同樣不中斷建置。
    回傳 WARN 數——WARN 原本只印在滾動輸出裡沒有消費端（2026-09-02 reviewer：
    「讓 WARN 有消費端」），呼叫端會在建置尾行印合計供心跳抄錄。"""
    warns = 0
    for f in all_md_files:
        try:
            raw = read_md(f)
        except Exception:
            continue
        for m in ANCHORED_WIKILINK_RE.finditer(raw):
            target = _clean_wikilink_target(m.group(1))
            anchor = m.group(2).replace('\\', '').strip()
            if not anchor.startswith('^'):  # 區塊 id 不在本檢查範圍
                headings = _headings_of(target)
                if headings is None:
                    continue  # 頁面本身斷鏈 → 交給 check_wikilinks 報
                if anchor not in headings:
                    warns += 1
                    print(f"WARN: {f.relative_to(ROOT)} 的 [[{target}#{anchor}]] 錨點不存在於該頁標題")
    return warns


def check_wikilinks(all_md_files: list[Path]) -> int:
    """Scan wiki/*.md for [[target]] / [[target|alias]] wikilinks and print a
    WARN for any target that doesn't resolve to a real page. Never raises —
    purely advisory, does not interrupt the build."""
    # 合法 target 集合：entities/topics 檔名（含/不含前綴）、特殊根頁面、news/ 日期頁
    entity_slugs = {f.stem for f in WIKI_ENTITIES.glob("*.md")}
    topic_slugs  = {f.stem for f in WIKI_TOPICS.glob("*.md")}
    root_slugs   = {f.stem for f in WIKI_DIR.glob("*.md")}  # feature-radar, feature-radar-archive-*, index, overview
    news_dates   = {f.stem for f in NEWS_DIR.glob("*.md")}

    valid_targets = set(root_slugs)
    valid_targets |= entity_slugs | {f"entities/{s}" for s in entity_slugs}
    valid_targets |= topic_slugs | {f"topics/{s}" for s in topic_slugs}
    valid_targets |= {f"news/{d}" for d in news_dates}

    warns = 0
    for f in all_md_files:
        try:
            raw = read_md(f)
        except Exception:
            continue
        headings = set(re.findall(r'^##\s+(.+?)\s*$', raw, flags=re.MULTILINE))
        for m in WIKILINK_RE.finditer(raw):
            target = _clean_wikilink_target(m.group(1))
            if target in valid_targets:
                continue
            if target in headings:
                continue  # in-page section self-reference (e.g. [[已知問題]])
            warns += 1
            print(f"WARN: {f.relative_to(ROOT)} 含斷鏈 wikilink [[{target}]]")
    return warns


def parse_enterprise_tracker(f: Path) -> dict | None:
    """Parse enterprise-tool-tracker.md table → structured matrix JSON."""
    if not f.exists():
        return None
    raw = read_md(f)

    STATUS_MAP = {"✅": "active", "⚠️": "warning", "🔄": "switching", "❌": "exited", "❓": "unknown"}

    rows: list[dict] = []
    in_table = False

    for line in raw.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            in_table = False
            continue
        if "企業" in line and "AI 編碼工具" in line:
            in_table = True
            continue
        if not in_table:
            continue
        if re.match(r"^\|[-: |]+\|$", line):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 7:
            continue
        enterprise, size, tool, status_raw, event_date, note, confirmed_date = (cells + [""] * 7)[:7]
        status_key = next((v for k, v in STATUS_MAP.items() if k in status_raw), "unknown")
        rows.append({
            "enterprise": enterprise,
            "size": size,
            "tool": tool,
            "status": status_raw,
            "statusKey": status_key,
            "eventDate": "" if event_date in ("—", "-", "") else event_date,
            "note": note,
            "confirmedDate": confirmed_date,
        })

    # Unique enterprises + tools (insertion order)
    enterprises: dict[str, str] = {}   # name → size
    tools: list[str] = []
    for r in rows:
        enterprises.setdefault(r["enterprise"], r["size"])
        if r["tool"] not in tools:
            tools.append(r["tool"])

    # Matrix: enterprise → tool → cell
    matrix: dict[str, dict] = {}
    for r in rows:
        matrix.setdefault(r["enterprise"], {})
        matrix[r["enterprise"]][r["tool"]] = {
            "status": r["status"],
            "statusKey": r["statusKey"],
            "eventDate": r["eventDate"],
            "note": r["note"],
            "confirmedDate": r["confirmedDate"],
        }

    return {
        "enterprises": [{"name": k, "size": v} for k, v in enterprises.items()],
        "tools": tools,
        "matrix": matrix,
        "rows": rows,
    }


def parse_radar(f: Path) -> dict:
    raw = read_md(f)
    lines = raw.splitlines()
    name = lines[0].lstrip("# ").strip() if lines else f.stem

    last_updated = ""
    lu_re = re.compile(r"\*\*最後更新[：:]\*\*\s*(.+)")
    for line in lines:
        m = lu_re.match(line)
        if m:
            # strip parenthetical annotations like "（含 5/13 ingest 更新）"
            last_updated = re.sub(r'[（(][^）)]*[）)]', '', m.group(1)).strip()
            break

    return {
        "id": "feature-radar",
        "pageType": "radar",
        "name": name,
        "entityType": "meta",
        "status": "",
        "pill": "warn",
        "lastUpdated": last_updated,
        "markdown": strip_llm_sections(raw),
        "summary": "追蹤 Claude / Claude Code 每個新發布功能的社群熱度、試用價值與快速上手方式。",
    }


def attach_sedimented_badges(digest_all: dict, entities: list, topics: list) -> None:
    """為每篇日報標記「已沉澱」——沿用 wiki 頁既有的 lastNewsUpdate 欄位（不新增
    資料管線）：若某 wiki 頁 lastNewsUpdate 等於日報日期，且該頁「name」出現在
    某條目的標題/內文中，該條目附上 sedimented 徽章；同時彙整當日全部已沉澱頁
    為 sedimentedToday，供前端「今日 wiki 動態」小節使用。"""
    all_pages = entities + topics
    by_id = {p["id"]: p for p in all_pages if p.get("id")}
    for date_str, d in digest_all.items():
        # 專頁雷達條目：把「→ slug」解析成可點的 wiki 頁（slug 可能帶 topics/ 前綴）
        for item in d.get("topicRadar", []):
            slug = item.get("topic", "").split("/")[-1]
            p = by_id.get(slug)
            item["topicPage"] = ({"id": p["id"], "name": p["name"], "pageType": p["pageType"]}
                                 if p else None)
        today_pages = [p for p in all_pages
                       if p.get("lastNewsUpdate") == date_str and p.get("name")]
        if not today_pages:
            d["sedimentedToday"] = []
            continue
        d["sedimentedToday"] = [
            {"id": p["id"], "name": p["name"], "pageType": p["pageType"]}
            for p in today_pages
        ]
        for sec in ("topStories", "techUpdates", "mediaReports", "discussions", "billing"):
            for s in d.get(sec, []):
                text = f"{s.get('title', '')} {s.get('body', '')}"
                hits = [p for p in today_pages if p["name"] in text]
                if hits:
                    s["sedimented"] = [
                        {"id": p["id"], "pageType": p["pageType"]} for p in hits[:2]
                    ]


# ── Weekly 結構化解析（journal 版面用，§A）──────────────────────────────────
# 週報是自由行文的四段式 markdown；解析器用內容關鍵字對應四大段（頭條/技術討論/
# 下週/數字），不依賴「一、二、三、四、」編號（編號可能改版），任一段缺失時
# 對應欄位為 None/[]，不報錯（淡週容忍）。解析失敗的段落仍保留在整段 `markdown`
# 供前端 fallback 走舊的 marked 渲染路徑。

WEEKLY_LEDE_RE = re.compile(r'^>\s*\*\*本週一句話\*\*[：:]\s*(.+)$', re.MULTILINE)
WEEKLY_H2_RE = re.compile(r'^##\s+(.+?)\s*$', re.MULTILINE)
WEEKLY_H3_RE = re.compile(r'^###\s+(.+?)\s*$', re.MULTILINE)
WEEKLY_FOOTER_RE = re.compile(r'\n-{3,}\s*\n+(\*\*素材涵蓋窗.*)\Z', re.DOTALL)
WEEKLY_FORECAST_HEADER_RE = re.compile(r'^\|\s*類型\s*\|\s*預告\s*\|\s*判準\s*\|\s*$', re.MULTILINE)
# 回收表（回頭看上一期預告的結果）——欄名與 forecasts 表刻意不同，兩張表才能在同段共存。
# 欄名若改動，`.claude/commands/weekly-report.md` 第 (3) 段的欄位定義必須同步（見 review-registry sync_pair）。
WEEKLY_RECAP_HEADER_RE = re.compile(r'^\|\s*上週預告\s*\|\s*判準\s*\|\s*本週結果\s*\|\s*$', re.MULTILINE)
# 回收小標與回收表之間那行盤點摘要（幾條活著／幾條死了／幾筆判錯）。2026-08-30 新增：
# 新順序（新開在上、回收在下）下，節導言與新開導言併入 intro，回收導言需獨立欄位才進得了網站。
WEEKLY_RECAP_HEADING_RE = re.compile(r"^###\s*上週的線怎麼了（\d{4}-W\d{2}）\s*$", re.MULTILINE)
WEEKLY_STAT_RE = re.compile(r'^-\s*\*\*(.+?)\*\*\s*——\s*(.+)$', re.MULTILINE)


def _weekly_strip_bold(text: str) -> str:
    return re.sub(r'\*{1,3}([^*\n]+)\*{1,3}', r'\1', text)


def _weekly_clean_trailing_hr(text: str) -> str:
    """移除區塊尾端殘留的 '---' 分隔線（H2/H3 切段後，前一段結尾常留下它）。"""
    return re.sub(r'\n?-{3,}\s*\Z', '', text).strip()


def _split_by_heading(body: str, heading_re: re.Pattern) -> list[tuple[str, str]]:
    """依標題 regex 切段，回傳 [(標題文字, 段落內文), …]，內文含到下一個同層標題前。"""
    matches = list(heading_re.finditer(body))
    parts: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        parts.append((title, body[start:end]))
    return parts


def _classify_weekly_h2(title: str) -> str | None:
    if "頭條" in title:
        return "headline"
    if "技術討論" in title or "深挖" in title:
        return "discussion"
    if "下週" in title:
        return "nextweek"
    if "數字" in title:
        return "numbers"
    return None


def _parse_weekly_forecasts(body: str) -> list[dict]:
    """解析『下週看什麼』段落內的三欄表格（類型/預告/判準），依表頭順序輸出。"""
    header_m = WEEKLY_FORECAST_HEADER_RE.search(body)
    if not header_m:
        return []
    rest = body[header_m.end():].splitlines()
    forecasts: list[dict] = []
    started = False
    for line in rest:
        ls = line.strip()
        if not ls.startswith("|"):
            if started:
                break
            continue
        if re.match(r"^\|[-: |]+\|$", ls):
            started = True
            continue
        if not started:
            # 表頭與分隔線之間不該有其他內容，但保守略過非分隔線的雜訊行
            continue
        cells = [c.strip() for c in ls.strip("|").split("|")]
        if len(cells) < 3:
            continue
        cells = [_weekly_strip_bold(c) for c in cells]
        forecasts.append({"type": cells[0], "forecast": cells[1], "criterion": cells[2]})
    return forecasts


def _parse_weekly_recap(body: str) -> list[dict]:
    """解析『下週看什麼』段落內的**回收表**（上週預告/判準/本週結果），依表頭順序輸出。

    與 _parse_weekly_forecasts 的差別是方向：回收表講「上一期預告的結果」（回頭看），
    forecasts 表講「這一期新立的預告」（往前看）。兩張表同段並列時，若只解析後者，
    回收表會被整張吃掉不進 JSON——2026-W31 首次出現回收表時即如此（網站看不到對帳，
    且回收小標被 _parse_weekly_nextweek_intro 誤當引言印在新預告卡片上方）。
    """
    header_m = WEEKLY_RECAP_HEADER_RE.search(body)
    if not header_m:
        return []
    rest = body[header_m.end():].splitlines()
    recap: list[dict] = []
    started = False
    for line in rest:
        ls = line.strip()
        if not ls.startswith("|"):
            if started:
                break
            continue
        if re.match(r"^\|[-: |]+\|$", ls):
            started = True
            continue
        if not started:
            continue
        cells = [c.strip() for c in ls.strip("|").split("|")]
        if len(cells) < 3:
            continue
        cells = [_weekly_strip_bold(c) for c in cells]
        result = cells[2]
        mark_m = re.match(r"^([^\w\s一-鿿]+)\s*", result)
        recap.append({
            "forecast": cells[0],
            "criterion": cells[1],
            "result": result,
            "mark": mark_m.group(1).strip() if mark_m else "",
        })
    return recap


def _parse_weekly_stats(body: str) -> list[dict]:
    """解析『本週數字』段落內的 bullet（格式：- **數值**——說明）。"""
    return [
        {"value": m.group(1).strip(), "desc": m.group(2).strip()}
        for m in WEEKLY_STAT_RE.finditer(body)
    ]


def _parse_weekly_recap_intro(body: str) -> str:
    """回收小標與回收表之間的盤點摘要一行。舊期用舊小標，抓不到即回空字串（不報錯）。"""
    m = WEEKLY_RECAP_HEADING_RE.search(body)
    if not m:
        return ""
    out: list[str] = []
    for line in body[m.end():].splitlines():
        ls = line.strip()
        if ls.startswith("|"):
            break
        if ls and not ls.startswith("#"):
            out.append(_weekly_strip_bold(ls))
    return " ".join(out).strip()


def _parse_weekly_nextweek_intro(body: str) -> str:
    """『下週看什麼』表格前的引言段（如「每條都立了判準，下週開欄先回收對錯。」）。

    取到第一個 `|` 開頭行之前的非空文字；無引言（表格緊接標題）時回傳空字串。
    **跳過 `#` 開頭的子標題行**——段內子標題（如「### 先回收上週的六條」）是結構，不是引言；
    2026-W31 曾因此把回收小標印在新預告卡片上方，讀者無從分辨哪張表是回頭看、哪張是往前看。
    """
    intro_lines: list[str] = []
    for line in body.splitlines():
        ls = line.strip()
        if ls.startswith("|"):
            break
        if ls.startswith("#"):
            continue
        if ls:
            intro_lines.append(_weekly_strip_bold(ls))
    return " ".join(intro_lines).strip()


def parse_weekly(f: Path) -> dict:
    """週報頁解析（weekly/YYYY-Wnn.md）。

    保留原有欄位（id/pageType/name/preview/markdown）向下相容；額外萃取結構化
    欄位供期刊版面渲染：lede、sections.{headline,discussion,nextweek,numbers}、
    extraSections、footer。任一段解析失敗只印警告、留 None/[]，不中斷整體 build。
    """
    raw = read_md(f)
    lines = raw.splitlines()
    week_id = f.stem  # e.g. "2026-W30"
    name = lines[0].lstrip("# ").strip() if lines else week_id

    # ── 既有欄位：preview（原邏輯不動，向下相容）──────────────────────────────
    preview = ""
    for line in lines[1:]:
        ls = line.strip()
        if not ls or ls.startswith("#") or ls.startswith(">") or ls.startswith("---"):
            continue
        preview = re.sub(r'\*{1,3}([^*\n]+)\*{1,3}', r'\1', ls)
        preview = readable_inline(preview).strip()[:160]
        if preview:
            break

    result: dict = {
        "id": week_id,
        "pageType": "weekly",
        "name": name,
        "preview": preview,
        "markdown": raw,
        "lede": None,
        "sections": {"headline": None, "discussion": None, "nextweek": None, "numbers": None},
        "extraSections": [],
        "footer": None,
    }

    # ── lede：H1 後第一個 "> **本週一句話**：…" ───────────────────────────────
    try:
        m = WEEKLY_LEDE_RE.search(raw)
        if m:
            result["lede"] = _weekly_strip_bold(m.group(1)).strip()
    except Exception as e:
        print(f"  [warn] weekly {f.name}: lede 解析失敗：{e}")

    # ── footer：檔尾『素材涵蓋窗』——先切掉，避免混進「本週數字」段落 body ──────
    content_for_sections = raw
    try:
        fm = WEEKLY_FOOTER_RE.search(raw)
        if fm:
            footer_text = fm.group(1).strip()
            footer_text = _weekly_strip_bold(footer_text)
            footer_text = re.sub(r'`([^`]+)`', r'\1', footer_text)
            result["footer"] = footer_text.strip()
            content_for_sections = raw[:fm.start()]
    except Exception as e:
        print(f"  [warn] weekly {f.name}: footer 解析失敗：{e}")

    # ── 四大段（依內容關鍵字分類，非編號）──────────────────────────────────────
    try:
        for title, body in _split_by_heading(content_for_sections, WEEKLY_H2_RE):
            body = _weekly_clean_trailing_hr(body)
            kind = _classify_weekly_h2(title)

            if kind == "headline":
                result["sections"]["headline"] = {"title": title, "body": body}

            elif kind == "discussion":
                disc = {"title": title, "body": body,
                        "versionNote": None, "roundup": None, "deepDive": None}
                try:
                    for sub_title, sub_body in _split_by_heading(body, WEEKLY_H3_RE):
                        sub_body = _weekly_clean_trailing_hr(sub_body)
                        if "本週版本" in sub_title:
                            disc["versionNote"] = sub_body
                        elif "討論綜述" in sub_title:
                            disc["roundup"] = sub_body
                        elif sub_title.startswith("深挖"):
                            dd_title = re.sub(r'^深挖[：:]\s*', '', sub_title).strip()
                            disc["deepDive"] = {"title": dd_title, "body": sub_body}
                except Exception as e:
                    print(f"  [warn] weekly {f.name}: discussion 子段解析失敗：{e}")
                result["sections"]["discussion"] = disc

            elif kind == "nextweek":
                nw = {"title": title, "body": body, "forecasts": [], "recap": [], "intro": "", "recapIntro": ""}
                try:
                    nw["forecasts"] = _parse_weekly_forecasts(body)
                except Exception as e:
                    print(f"  [warn] weekly {f.name}: forecasts 表格解析失敗：{e}")
                try:
                    nw["recap"] = _parse_weekly_recap(body)
                except Exception as e:
                    print(f"  [warn] weekly {f.name}: recap 表格解析失敗：{e}")
                try:
                    nw["intro"] = _parse_weekly_nextweek_intro(body)
                    nw["recapIntro"] = _parse_weekly_recap_intro(body)
                except Exception as e:
                    print(f"  [warn] weekly {f.name}: nextweek intro 解析失敗：{e}")
                result["sections"]["nextweek"] = nw

            elif kind == "numbers":
                nums = {"title": title, "body": body, "stats": []}
                try:
                    nums["stats"] = _parse_weekly_stats(body)
                except Exception as e:
                    print(f"  [warn] weekly {f.name}: stats 解析失敗：{e}")
                result["sections"]["numbers"] = nums

            else:
                result["extraSections"].append({"title": title, "body": body})
    except Exception as e:
        print(f"  [warn] weekly {f.name}: 段落切分失敗：{e}")

    return result


def collect_weekly(weekly_dir: Path) -> tuple[dict, list]:
    """Parse all weekly/*.md under weekly_dir into (weekly_all, weekly_index).

    Returns empty containers when weekly_dir doesn't exist — this is the
    contract the front-end's "尚無週報" empty state depends on (no weekly/
    directory yet is a normal, expected state, not an error)."""
    weekly_all: dict = {}
    weekly_index: list = []
    if not weekly_dir.exists():
        return weekly_all, weekly_index
    for f in sorted(weekly_dir.glob("*.md"), reverse=True):
        try:
            w = parse_weekly(f)
            weekly_all[w["id"]] = w
            weekly_index.append({"id": w["id"], "name": w["name"], "preview": w["preview"]})
        except Exception as e:
            print(f"  [warn] weekly {f.name}: {e}")
    return weekly_all, weekly_index


def parse_wiki(f: Path, page_type: str) -> dict:
    raw = read_md(f)
    lines = raw.splitlines()

    _first = next((l for l in lines if l.strip()), "")
    name = _first.lstrip("# ").strip() or f.stem  # 取首個非空行：frontmatter 後多一空行曾讓 name 變空、全站 wikilink 退化為 slug（2026-09-02）
    entity_id = f.stem

    meta: dict = {
        "id": entity_id,
        "pageType": page_type,
        "name": name,
        "entityType": "",
        "status": "",
        "domain": "",
        "pill": "gray",
        "firstSeen": "",
        "startDate": "",
        "lastUpdated": "",
        "lastNewsUpdate": "",
        "updateFreq": "",
        "parent": "",
        "summary": "",
        "latestHeadline": "",
        "markdown": raw,
    }

    in_summary = False
    summary_lines: list[str] = []

    for raw_line in lines[1:]:
        # 根因修復：CRLF 檔案逐行 split 後行尾仍殘留 \r，一併清掉，避免污染解析值
        line = raw_line.rstrip("\r")
        for field, rx in META_RE.items():
            m = rx.match(line)
            if m:
                # .strip() 涵蓋 \r 與任何欄位值首尾空白，不只限於本次發現的 domain 欄位
                val = m.group(1).strip()
                if field in ("entityType", "type"):
                    meta["entityType"] = val
                else:
                    meta[field] = val

        if line.strip() in SUMMARY_HEADERS:
            in_summary = True
            continue
        if in_summary:
            if line.startswith("## "):
                in_summary = False
            elif line.strip():
                summary_lines.append(line.strip())

    # 後備：SUMMARY_HEADERS 只認「## 現況 / ## 摘要」兩個標題名，任何用其他首節標題的頁面
    # 都會靜默產出空摘要，在 wiki 列表頁變成一張空卡（2026-08-08 發現，當時全庫已有 2 頁中招）。
    # 改為往下退：頂部 delta-first callout → 第一段正文。頁面該叫什麼標題是編輯決定，
    # 不該為了餵這支腳本而被限定。
    if not summary_lines:
        summary_lines = _fallback_summary_lines(raw)

    # first 160 chars of summary（wikilink 先轉可讀文字，避免截斷後懸空斷句）
    raw_summary = readable_inline(" ".join(summary_lines))
    meta["summary"] = raw_summary[:160] + ("…" if len(raw_summary) > 160 else "")
    meta["latestHeadline"] = latest_headline(raw)
    meta["pill"] = pill_class(meta["status"])

    # ── 防呆：缺少領域欄位、或領域值不在六個標準值內 ──────────────────────────
    if not meta["domain"]:
        print(f"  WARN: {page_type}/{f.name} 缺少「領域」欄位")
    elif meta["domain"] not in VALID_DOMAINS:
        print(f"  WARN: {page_type}/{f.name} 領域值不在標準六選一內：{meta['domain']!r}")

    return meta


# ── Digest parser ─────────────────────────────────────────────────────────────

SECTION_EMOJI = {"🔔": "bulletin", "⭐": "topStories", "🔧": "techUpdates", "📰": "mediaReports",
                 "💬": "discussions", "💰": "billing", "📌": "focus",
                 # 🧭 專頁雷達（2026-08-13 起，Topic Watch 定向抓取）——獨立區塊，不混入正文六區。
                 # 📡 來源狀態必須也列入：否則它的表格行會被當成前一區最後一則故事的 body
                 # （2026-08-14 症狀：專頁雷達條目跑進「付費方案動態」，來源表黏在最後一條底下）。
                 "🧭": "topicRadar", "📡": "sourceStatusSection"}

# 專頁雷達每行：`- **[標題](url)** — 一句話說明（→ 專頁 slug）`
TOPIC_RADAR_RE = re.compile(
    r"^-\s+\*\*\[(.+?)\]\((.+?)\)\*\*\s*(?:[—–-]+\s*(.*?))?\s*(?:[（(]→\s*([\w./-]+)\s*[）)])?\s*$"
)

SENTIMENT_RE = re.compile(r"`情緒：(.+?)`")
# star stories start with "⭐ **[Title](url)**" — strip any leading emoji/chars before **
STORY_RE = re.compile(r"\*\*\[(.+?)\]\((.+?)\)\*\*")
# source/timestamp line — two sentiment styles observed in real news/*.md:
#   舊格式（如 2026-04-26/27）：`Source` · MM/DD HH:MM UTC · `情緒：😊 正面`（反引號包住、前有額外 ·）
#   現行格式（2026-07 起）：    `Source` · MM/DD HH:MM UTC 情緒：😤          （裸文字，無反引號、無額外 ·）
# group(3) = 舊格式的情緒值，group(4) = 現行格式的情緒值；兩者最多命中一個。
SOURCE_RE = re.compile(
    r"^`(.+?)`\s*·\s*(.+?)(?:\s*UTC)?"
    r"(?:\s*·\s*`情緒[：:]\s*(.+?)`"
    r"|\s*情緒[：:]\s*(.+?))?"
    r"\s*$"
)
FOCUS_RE    = re.compile(r"^(?:-\s+)?\*\*(.+?)\*\*\s+(.*)")
# 舊格式：今日聚焦行內直接嵌完整 URL，如 "（ref: https://...）"。
FOCUS_REF_RE = re.compile(r"（ref:\s*(https?://[^\s（）)]+)[）)]")
# 中期格式（2026-07-24～2026-09-03，見 digest.py::reformat_presentation）：行內只留編號
# 引用 "[N]"，完整 URL 移到檔尾「今日聚焦參考連結」清單，須另外解析還原。
FOCUS_NUM_RE = re.compile(r"\[(\d+)\]")
# 現行格式（2026-09-04 起，冷讀者 review 改版）：句末行內 markdown 連結
# `（[來源名](url)）`，多則頓號並列。抽 URL 進 ref_urls（餵 focus badge 與典藏頁
# 標籤），顯示文字把整個括號連結群移除——app.js 的 focus text 是純轉義不渲染
# markdown，不移除會印出字面 `（[HN](https://…)）`。
FOCUS_INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)")
FOCUS_INLINE_GROUP_RE = re.compile(
    r"[（(]\s*(?:\[[^\]]+\]\(https?://[^\s)]+\)\s*[、,]?\s*)+[）)]"
)
FOCUS_REF_LIST_RE = re.compile(
    r"今日聚焦參考連結[：:]\**\s*\n((?:\d+\.\s+\S+\s*\n?)+)"
)
FOCUS_REF_LIST_ITEM_RE = re.compile(r"^\d+\.\s+(\S+)\s*$", re.MULTILINE)
SOURCE_TABLE_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*(✅|❌)\s*\|\s*(\d+)\s*\|")


def parse_digest(f: Path) -> dict:
    raw = read_md(f)
    lines = raw.splitlines()
    date_str = f.stem  # YYYY-MM-DD

    result: dict = {
        "date": date_str,
        "generatedAt": "",
        "articleCount": 0,
        "sourceCount": "",
        "bulletin": "",
        "topStories": [],
        "techUpdates": [],
        "mediaReports": [],
        "discussions": [],
        "billing": [],
        "focus": [],
        "topicRadar": [],
        "sourceStatus": [],
        "preview": "",
    }

    # header line: **日期：** … | **來源：** … | **文章數：** … | **更新時間：** …
    # 分隔符實際上有兩種：真實 news/*.md 一律用純 "|"；digest.py 原始碼另有一支
    # "&nbsp;|&nbsp;" 版本（目前尚未有任何實檔採用，但保留相容不吃虧）——兩者都要停。
    header_re = re.compile(r"\*\*文章數[：:]\*\*\s*(\d+)")
    gen_re = re.compile(r"\*\*更新時間[：:]\*\*\s*(.+)")
    src_count_re = re.compile(r"\*\*來源[：:]\*\*\s*(.+?)(?:\s*[|&]|$)")

    current_section: str | None = None
    current_story: dict | None = None
    current_body: list[str] = []
    focus_ref_nums: list[list[int]] = []  # 新格式 [N] 編號，索引對齊 result["focus"]

    def flush_story():
        nonlocal current_story, current_body
        if current_story and current_section and current_section != "focus":
            current_story["body"] = " ".join(current_body).strip()
            result[current_section].append(current_story)
        current_story = None
        current_body = []

    for line in lines:
        # header metadata
        m = header_re.search(line)
        if m:
            result["articleCount"] = int(m.group(1))
        m = gen_re.search(line)
        if m:
            result["generatedAt"] = m.group(1).strip()
        m = src_count_re.search(line)
        if m:
            result["sourceCount"] = m.group(1).strip()

        # section header
        for emoji, key in SECTION_EMOJI.items():
            if re.match(rf"^(?:#+\s+)?{re.escape(emoji)}\s+(?!\*\*\[)", line):
                flush_story()
                current_section = key
                break
        else:
            if current_section is None:
                continue

            # source status table — check before focus handling so it works in any section
            m = SOURCE_TABLE_RE.match(line)
            if m:
                src_name, status_icon, count = m.group(1), m.group(2), m.group(3)
                if src_name.strip() not in ("來源", "---", "------"):
                    result["sourceStatus"].append({
                        "name": src_name.strip(),
                        "ok": status_icon == "✅",
                        "count": int(count),
                    })
                continue

            # bulletin — single line of plain text
            if current_section == "bulletin":
                stripped = line.strip()
                if stripped and not stripped.startswith("#") and not stripped.startswith("---"):
                    if not result["bulletin"]:
                        result["bulletin"] = stripped
                continue

            # 專頁雷達：每行一條 bullet，無來源行；讀者需看到「這是為哪個專頁抓的」
            if current_section == "topicRadar":
                m = TOPIC_RADAR_RE.match(line.strip())
                if m:
                    result["topicRadar"].append({
                        "title": m.group(1), "url": m.group(2),
                        "body": (m.group(3) or "").strip(),
                        "topic": (m.group(4) or "").strip(),
                    })
                continue
            if current_section == "sourceStatusSection":
                continue  # 表格行已在上方 SOURCE_TABLE_RE 處理

            # focus items
            if current_section == "focus":
                m = FOCUS_RE.match(line)
                if m:
                    tag, text_raw = m.group(1).strip(), m.group(2).strip()
                    ref_urls = FOCUS_REF_RE.findall(text_raw)  # 舊格式：行內完整 URL
                    ref_nums = [int(n) for n in FOCUS_NUM_RE.findall(text_raw)]  # 中期格式：[N] 編號
                    # 現行格式（2026-09-04 起）：行內 markdown 連結——先抽 URL 再整群移除
                    ref_urls += [u for _, u in FOCUS_INLINE_LINK_RE.findall(text_raw)]
                    text = FOCUS_INLINE_GROUP_RE.sub("", text_raw)
                    text = FOCUS_INLINE_LINK_RE.sub(r"\1", text)  # 群外落單連結：留來源名
                    text = FOCUS_REF_RE.sub("", text)
                    text = FOCUS_NUM_RE.sub("", text).strip()
                    result["focus"].append({"tag": tag, "text": text, "ref_urls": ref_urls})
                    focus_ref_nums.append(ref_nums)
                continue

            # story title line: **[Title](url)** (may be preceded by ⭐ or other chars)
            m = STORY_RE.search(line)
            if m:
                flush_story()
                title = m.group(1)
                # 修復缺左括號的標題（如「BUG] xxx」）：日報產生時 LLM 偶爾把
                # 標題自身的開頭方括號併入連結語法吞掉（**[BUG] t](url)**）。
                # 判準：第一個 ] 之前沒有任何 [ → 補回開頭的 [。
                if ']' in title and '[' not in title.split(']', 1)[0]:
                    title = '[' + title
                current_story = {"title": title, "url": m.group(2),
                                  "source": "", "time": "", "sentiment": "", "body": ""}
                current_body = []
                continue

            # source / timestamp line
            if current_story:
                m = SOURCE_RE.match(line.strip())
                if m:
                    current_story["source"] = m.group(1).strip()
                    current_story["time"] = m.group(2).strip()
                    sentiment = m.group(3) or m.group(4)
                    if sentiment:
                        current_story["sentiment"] = sentiment.strip()
                    flush_story()
                    continue
                # body text
                if line.strip() and not line.startswith("#") and not line.startswith("---"):
                    current_body.append(line.strip())

    flush_story()

    # ── 新格式：解析檔尾「今日聚焦參考連結」清單，把 [N] 編號還原成實際 URL ──
    # 舊格式檔案沒有這份清單（FOCUS_REF_LIST_RE 找不到就整段跳過），focus_ref_nums
    # 對應的 ref_nums 全空，等同無操作。
    ref_list_m = FOCUS_REF_LIST_RE.search(raw)
    if ref_list_m:
        ref_list = FOCUS_REF_LIST_ITEM_RE.findall(ref_list_m.group(1))
        for focus_item, nums in zip(result["focus"], focus_ref_nums):
            for n in nums:
                if 1 <= n <= len(ref_list):
                    focus_item["ref_urls"].append(ref_list[n - 1])

    # preview：優先取「今日聚焦」第一條（編輯已判定當日最重要的事），
    # 沒有聚焦才退回第一則重點話題標題——避免典藏頁用離題條目當當日門面
    # （2026-07-28 讀者 review：07-22 曾以「space economy SIM in Rust」代表當日）。
    if result["focus"]:
        result["preview"] = result["focus"][0]["text"][:160]
    elif result["topStories"]:
        result["preview"] = result["topStories"][0]["title"]
    elif result["techUpdates"]:
        result["preview"] = result["techUpdates"][0]["title"]

    # ── Post-process: assign focusTags to each story ─────────────────────────
    # Google News RSS URLs have unstable base64 tails; normalize to first 100 chars.
    def _norm(url: str) -> str:
        u = url.rstrip("/")
        return u[:100] if "news.google.com" in u else u

    url_tag: dict[str, str] = {}
    for f in result["focus"]:
        for u in (f.get("ref_urls") or []):
            url_tag[u] = f["tag"]
            url_tag[_norm(u)] = f["tag"]

    for sec in ("topStories", "techUpdates", "mediaReports", "discussions", "billing"):
        for s in result[sec]:
            su = s.get("url", "")
            tag = url_tag.get(su) or url_tag.get(_norm(su)) or ""
            s["focusTags"] = [tag] if tag else []

    return result


# ── Build ─────────────────────────────────────────────────────────────────────

def build():
    # ── Internal wikilink dead-link check (free, runs every build) ───────────
    all_wiki_md = sorted(WIKI_DIR.glob("*.md")) + sorted(WIKI_ENTITIES.glob("*.md")) + sorted(WIKI_TOPICS.glob("*.md"))
    _broken = check_wikilinks(all_wiki_md)
    _anchor = check_wikilink_anchors(all_wiki_md)
    print(f"wikilink 健檢合計：斷鏈 WARN {_broken}／錨點 WARN {_anchor}（此行供 lint 心跳抄錄——WARN 要有消費端）")

    # 解析失敗 = 該頁在網站上直接消失。原本只印一行 [warn] 就繼續，build 照樣 exit 0，
    # 於是「少了一頁」沒有任何人會發現（2026-08-08：標頭領域欄一個全形斜線就讓整頁蒸發，
    # 而輸出只差在 53 vs 54 個檔）。改為蒐集後統一致命，讓 gate_web_build 攔得到。
    wiki_parse_failures: list[str] = []

    entities = []
    for f in sorted(WIKI_ENTITIES.glob("*.md")):
        try:
            entities.append(parse_wiki(f, "entity"))
        except Exception as e:
            wiki_parse_failures.append(f"entity {f.name}: {e}")

    topics = []
    for f in sorted(WIKI_TOPICS.glob("*.md")):
        try:
            topics.append(parse_wiki(f, "topic"))
        except Exception as e:
            wiki_parse_failures.append(f"topic {f.name}: {e}")

    if wiki_parse_failures:
        print("ERROR: 下列 wiki 頁面解析失敗，會從網站上整頁消失：")
        for msg in wiki_parse_failures:
            print(f"  - {safe_console(msg)}")
        sys.exit(1)

    digest_all: dict = {}
    digest_index: list = []
    for f in sorted(NEWS_DIR.glob("*.md"), reverse=True):
        try:
            d = parse_digest(f)
            digest_all[d["date"]] = d
            digest_index.append({
                "date": d["date"],
                "articleCount": d["articleCount"],
                "preview": d["preview"],
                "topCount": len(d["topStories"]),
            })
        except Exception as e:
            print(f"  [warn] digest {f.name}: {e}")

    # ── 已沉澱徽章／今日 wiki 動態（用既有 lastNewsUpdate 欄位比對，不新增管線）──
    attach_sedimented_badges(digest_all, entities, topics)

    # ── Parse weekly reports (weekly/YYYY-Wnn.md) ─────────────────────────────
    weekly_all, weekly_index = collect_weekly(WEEKLY_DIR)

    # ── Parse feature radar (root-level wiki doc) ─────────────────────────────
    radar = None
    if WIKI_RADAR.exists():
        try:
            radar = parse_radar(WIKI_RADAR)
        except Exception as e:
            print(f"  [warn] feature-radar: {e}")

    # ── Enrich enterprise-tool-tracker with matrix data ──────────────────────
    tracker_md = ROOT / "wiki" / "topics" / "enterprise-tool-tracker.md"
    tracker_data = parse_enterprise_tracker(tracker_md)
    if tracker_data:
        for t in topics:
            if t["id"] == "enterprise-tool-tracker":
                t["enterpriseTracker"] = tracker_data
                break

    # ── Write per-wiki JSON files (full content including markdown) ──────────
    OUT_WIKI_DIR.mkdir(parents=True, exist_ok=True)
    existing_wiki_ids = {f.stem for f in OUT_WIKI_DIR.glob("*.json")}
    current_wiki_ids  = {item["id"] for item in entities + topics}
    if radar:
        current_wiki_ids.add(radar["id"])  # prevent stale-cleanup of feature-radar.json
    for stale in existing_wiki_ids - current_wiki_ids:
        (OUT_WIKI_DIR / f"{stale}.json").unlink()
        print(f"  [clean] removed stale wiki/{stale}.json")
    for item in entities + topics:
        with (OUT_WIKI_DIR / f"{item['id']}.json").open("w", encoding="utf-8") as fp:
            json.dump(item, fp, ensure_ascii=False, indent=2)
    if radar:
        with (OUT_WIKI_DIR / "feature-radar.json").open("w", encoding="utf-8") as fp:
            json.dump(radar, fp, ensure_ascii=False, indent=2)

    # ── Write per-digest JSON files ───────────────────────────────────────────
    OUT_DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    existing_digest_dates = {f.stem for f in OUT_DIGEST_DIR.glob("*.json")}
    current_digest_dates  = set(digest_all.keys())
    for stale in existing_digest_dates - current_digest_dates:
        (OUT_DIGEST_DIR / f"{stale}.json").unlink()
        print(f"  [clean] removed stale digest/{stale}.json")
    for date_str, d in digest_all.items():
        with (OUT_DIGEST_DIR / f"{date_str}.json").open("w", encoding="utf-8") as fp:
            json.dump(d, fp, ensure_ascii=False, indent=2)

    # ── Write per-weekly JSON files ────────────────────────────────────────────
    OUT_WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    existing_weekly_ids = {f.stem for f in OUT_WEEKLY_DIR.glob("*.json")}
    current_weekly_ids  = set(weekly_all.keys())
    for stale in existing_weekly_ids - current_weekly_ids:
        (OUT_WEEKLY_DIR / f"{stale}.json").unlink()
        print(f"  [clean] removed stale weekly/{stale}.json")
    for week_id, w in weekly_all.items():
        with (OUT_WEEKLY_DIR / f"{week_id}.json").open("w", encoding="utf-8") as fp:
            json.dump(w, fp, ensure_ascii=False, indent=2)

    # ── Write slim data.js (no markdown, no DIGEST_ALL) ───────────────────────
    def slim(item):
        return {k: v for k, v in item.items() if k != "markdown"}

    def coding_pages():
        """從 wiki/index.md「## 💻 開發實務入口」表萃取頁面 id。

        「💻 開發實務」chip 是跨領域集合（coding 頁散在 🛠️ 與 🌐 兩領域），
        成員名單的單一來源就是 index.md 的入口路由表——入口表改，網站分頁跟著改。
        """
        try:
            text = (WIKI_DIR / "index.md").read_text(encoding="utf-8")
        except OSError:
            return []
        m = re.search(r"^## 💻[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        if not m:
            return []
        ids = []
        # 只取路由表格列的連結：導言散文裡的「產品動態住別頁」出口連結（feature-radar、
        # claude-code）不是 tab 成員——2026-09-03 使用者裁決 tab 只留開發實務強相關
        table_text = "\n".join(l for l in m.group(1).splitlines() if l.lstrip().startswith("|"))
        for target in re.findall(r"\[\[([^\]|#]+)", table_text):
            base = target.strip().split("/")[-1]
            if base and base not in ids:
                ids.append(base)
        return ids

    # 讀者分類（2026-09-03 使用者裁決）：wiki 標頭的「領域」是記者認領欄（誰維護），網站不需要
    # 知道記者是誰——讀者看到的分類是 readerDomains（多標籤）：領域值照放，index「💻 開發實務入口」
    # 表列出的頁再加一枚 💻 開發實務（不獨佔——模型選型頁在 🤖 與 💻 下都找得到；同日第二次裁決）。
    _coding_ids = coding_pages()
    _coding_set = set(_coding_ids)
    for _it in entities + topics:
        _tags = [_it["domain"]] if _it["domain"] else []
        if _it["id"] in _coding_set:
            _tags.append("💻 開發實務")
        _it["readerDomains"] = _tags

    wiki_data = {
        "entities":    [slim(e) for e in entities],
        "topics":      [slim(t) for t in topics],
        "codingPages": _coding_ids,
        "digestIndex": digest_index,
        "weeklyIndex": weekly_index,
        "radar": radar if radar else None,  # include markdown — rendered inline, no fetch needed
    }

    # ── 來源透明度資料（scripts/source_scorecard.py，隨每日 build 更新）────────────
    transparency = None
    try:
        import importlib.util
        _sc_spec = importlib.util.spec_from_file_location(
            "source_scorecard", ROOT / "scripts" / "source_scorecard.py")
        _sc = importlib.util.module_from_spec(_sc_spec)
        _sc_spec.loader.exec_module(_sc)
        transparency = _sc.compute(
            _sc.load_registry(), _sc.load_funnel(),
            _sc.load_attribution(), _sc.load_domain_scores())
    except Exception as e:  # 記分卡失敗不阻擋 build，透明度區塊在前端優雅缺席
        print(f"WARN: transparency data skipped ({e})")

    OUT_JS.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JS.open("w", encoding="utf-8") as fp:
        fp.write("// AUTO-GENERATED — do not edit. Run: python scripts/build_web.py\n")
        fp.write("window.WIKI_DATA = ")
        json.dump(wiki_data, fp, ensure_ascii=False, indent=2)
        fp.write(";\n")
        fp.write("window.TRANSPARENCY = ")
        json.dump(transparency, fp, ensure_ascii=False, separators=(",", ":"))
        fp.write(";\n")
        fp.write("// Digest content is loaded on-demand from data/digest/{date}.json\n")
        fp.write("// Wiki content is loaded on-demand from data/wiki/{id}.json\n")

    # Update cache-busting version in index.html (data.js + app.js + design.css)
    ver = str(int(time.time()))
    index = ROOT / "web_reader" / "index.html"
    if index.exists():
        html = index.read_text(encoding="utf-8")
        import re as _re
        html = _re.sub(r'data/data\.js(\?v=\d+)?', f'data/data.js?v={ver}', html)
        html = _re.sub(r'assets/app\.js(\?v=\d+)?', f'assets/app.js?v={ver}', html)
        html = _re.sub(r'assets/design\.css(\?v=\d+)?', f'assets/design.css?v={ver}', html)
        index.write_text(html, encoding="utf-8")

    # Bump the service-worker cache version so each deploy ships a fresh cache
    # name → clients auto-drop stale content (PWA offline cache).
    sw = ROOT / "web_reader" / "sw.js"
    if sw.exists():
        import re as _re2
        sw_txt = sw.read_text(encoding="utf-8")
        sw_txt = _re2.sub(r"const SW_VERSION = '[^']*';",
                          f"const SW_VERSION = '{ver}';", sw_txt, count=1)
        sw.write_text(sw_txt, encoding="utf-8")

    # ── Write search index (full plain text, stripped of markdown syntax) ────────
    search_index = []
    for item in entities + topics:
        search_index.append({
            "id":      item["id"],
            "type":    item["pageType"],
            "name":    item["name"],
            "summary": item["summary"],
            "text":    strip_markdown_to_text(item.get("markdown", "")),
        })
    if radar:
        search_index.append({
            "id":      radar["id"],
            "type":    "radar",
            "name":    radar["name"],
            "summary": radar["summary"],
            "text":    strip_markdown_to_text(radar.get("markdown", "")),
        })
    # Digests: index 今日聚焦 text + all story titles + story bodies —
    # body 補入前索引只到標題層，關鍵字若只出現在條目內文（未出現在標題）就搜不到。
    for date_str, d in digest_all.items():
        focus_txt = "；".join(f["text"] for f in d.get("focus", []))
        titles = "；".join(
            s["title"]
            for sec in ("topStories", "techUpdates", "mediaReports", "discussions", "billing")
            for s in d.get(sec, [])
        )
        bodies = "；".join(
            s["body"]
            for sec in ("topStories", "techUpdates", "mediaReports", "discussions", "billing")
            for s in d.get(sec, [])
            if s.get("body")
        )
        search_index.append({
            "id":      date_str,
            "type":    "digest",
            "name":    f"日報 {date_str}",
            "summary": (d.get("preview") or "")[:90],
            "text":    f"{focus_txt}；{titles}；{bodies}",
        })
    for week_id, w in weekly_all.items():
        search_index.append({
            "id":      week_id,
            "type":    "weekly",
            "name":    w["name"],
            "summary": w.get("preview", ""),
            "text":    strip_markdown_to_text(w.get("markdown", "")),
        })
    with OUT_SEARCH_INDEX.open("w", encoding="utf-8") as fp:
        json.dump(search_index, fp, ensure_ascii=False, separators=(",", ":"))

    print(f"OK: {len(entities)} entities, {len(topics)} topics, {len(digest_all)} digests, "
          f"{len(weekly_all)} weekly reports" + (" + radar" if radar else ""))
    print(f"    -> {OUT_JS} ({OUT_JS.stat().st_size//1024} KB)")
    print(f"    -> {OUT_SEARCH_INDEX} ({OUT_SEARCH_INDEX.stat().st_size//1024} KB)")
    print(f"    -> {OUT_WIKI_DIR}/ ({len(entities)+len(topics)} files)")
    print(f"    -> {OUT_DIGEST_DIR}/ ({len(digest_all)} files)")
    print(f"    -> {OUT_WEEKLY_DIR}/ ({len(weekly_all)} files)")


if __name__ == "__main__":
    build()
