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
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_ENTITIES = ROOT / "wiki" / "entities"
WIKI_TOPICS   = ROOT / "wiki" / "topics"
WIKI_RADAR    = ROOT / "wiki" / "feature-radar.md"
NEWS_DIR      = ROOT / "news"
OUT_JS           = ROOT / "web_reader" / "data" / "data.js"
OUT_WIKI_DIR     = ROOT / "web_reader" / "data" / "wiki"
OUT_DIGEST_DIR   = ROOT / "web_reader" / "data" / "digest"
OUT_SEARCH_INDEX = ROOT / "web_reader" / "data" / "search-index.json"

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
}

SUMMARY_HEADERS = ["## 現況", "## 摘要"]


def latest_headline(raw: str) -> str:
    """Extract the most recent update headline from wiki markdown."""
    def clean_line(ls: str) -> str:
        text = re.sub(r'^-\s*', '', ls)           # strip leading "- "
        text = re.sub(r'^\*{0,2}\d{4}-\d{2}-\d{2}\*{0,2}\s*.?\s*', '', text)  # strip date (bold or plain) + any colon
        text = re.sub(r'^\*\*\[[^\]]*\]\*\*\s*', '', text)       # strip **[tag]**
        text = re.sub(r'\*{1,3}([^*\n]+)\*{1,3}', r'\1', text)  # strip bold/italic
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
    return ''


def strip_llm_sections(md: str) -> str:
    """Remove any H2 section whose title contains '給 LLM' (and everything after it)."""
    return re.sub(r'\n## [^\n]*給 LLM[^\n]*\n[\s\S]*', '', md)


def parse_enterprise_tracker(f: Path) -> dict | None:
    """Parse enterprise-tool-tracker.md table → structured matrix JSON."""
    if not f.exists():
        return None
    raw = f.read_text(encoding="utf-8")

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
    raw = f.read_text(encoding="utf-8")
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


def parse_wiki(f: Path, page_type: str) -> dict:
    raw = f.read_text(encoding="utf-8")
    lines = raw.splitlines()

    name = lines[0].lstrip("# ").strip() if lines else f.stem
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
        "summary": "",
        "latestHeadline": "",
        "markdown": raw,
    }

    in_summary = False
    summary_lines: list[str] = []

    for line in lines[1:]:
        for field, rx in META_RE.items():
            m = rx.match(line)
            if m:
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

    # first 160 chars of summary
    raw_summary = " ".join(summary_lines)
    meta["summary"] = raw_summary[:160] + ("…" if len(raw_summary) > 160 else "")
    meta["latestHeadline"] = latest_headline(raw)
    meta["pill"] = pill_class(meta["status"])

    return meta


# ── Digest parser ─────────────────────────────────────────────────────────────

SECTION_EMOJI = {"🔔": "bulletin", "⭐": "topStories", "🔧": "techUpdates", "💬": "discussions",
                 "💰": "billing", "📌": "focus"}

SENTIMENT_RE = re.compile(r"`情緒：(.+?)`")
# star stories start with "⭐ **[Title](url)**" — strip any leading emoji/chars before **
STORY_RE = re.compile(r"\*\*\[(.+?)\]\((.+?)\)\*\*")
SOURCE_RE = re.compile(r"^`(.+?)`\s*·\s*(.+?)(?:\s*UTC)?(?:\s*·\s*`情緒：(.+?)`)?$")
FOCUS_RE    = re.compile(r"^(?:-\s+)?\*\*(.+?)\*\*\s+(.*)")
FOCUS_REF_RE = re.compile(r"（ref:\s*(https?://[^\s（）)]+)[）)]")
SOURCE_TABLE_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*(✅|❌)\s*\|\s*(\d+)\s*\|")


def parse_digest(f: Path) -> dict:
    raw = f.read_text(encoding="utf-8")
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
        "discussions": [],
        "billing": [],
        "focus": [],
        "sourceStatus": [],
        "preview": "",
    }

    # header line: **日期：** … | **來源：** … | **文章數：** … | **更新時間：** …
    header_re = re.compile(r"\*\*文章數[：:]\*\*\s*(\d+)")
    gen_re = re.compile(r"\*\*更新時間[：:]\*\*\s*(.+)")
    src_count_re = re.compile(r"\*\*來源[：:]\*\*\s*(.+?)(?:\s*&|$)")

    current_section: str | None = None
    current_story: dict | None = None
    current_body: list[str] = []

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

            # focus items
            if current_section == "focus":
                m = FOCUS_RE.match(line)
                if m:
                    tag, text_raw = m.group(1).strip(), m.group(2).strip()
                    ref_urls = FOCUS_REF_RE.findall(text_raw)   # list of all URLs
                    text = FOCUS_REF_RE.sub("", text_raw).strip()
                    result["focus"].append({"tag": tag, "text": text, "ref_urls": ref_urls})
                continue

            # story title line: **[Title](url)** (may be preceded by ⭐ or other chars)
            m = STORY_RE.search(line)
            if m:
                flush_story()
                current_story = {"title": m.group(1), "url": m.group(2),
                                  "source": "", "time": "", "sentiment": "", "body": ""}
                current_body = []
                continue

            # source / timestamp line
            if current_story:
                m = SOURCE_RE.match(line.strip())
                if m:
                    current_story["source"] = m.group(1).strip()
                    current_story["time"] = m.group(2).strip()
                    if m.group(3):
                        current_story["sentiment"] = m.group(3).strip()
                    flush_story()
                    continue
                # body text
                if line.strip() and not line.startswith("#") and not line.startswith("---"):
                    current_body.append(line.strip())

    flush_story()

    # preview = first top story title
    if result["topStories"]:
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

    for sec in ("topStories", "techUpdates", "discussions", "billing"):
        for s in result[sec]:
            su = s.get("url", "")
            tag = url_tag.get(su) or url_tag.get(_norm(su)) or ""
            s["focusTags"] = [tag] if tag else []

    return result


# ── Build ─────────────────────────────────────────────────────────────────────

def build():
    entities = []
    for f in sorted(WIKI_ENTITIES.glob("*.md")):
        try:
            entities.append(parse_wiki(f, "entity"))
        except Exception as e:
            print(f"  [warn] entity {f.name}: {e}")

    topics = []
    for f in sorted(WIKI_TOPICS.glob("*.md")):
        try:
            topics.append(parse_wiki(f, "topic"))
        except Exception as e:
            print(f"  [warn] topic {f.name}: {e}")

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

    # ── Write slim data.js (no markdown, no DIGEST_ALL) ───────────────────────
    def slim(item):
        return {k: v for k, v in item.items() if k != "markdown"}

    wiki_data = {
        "entities":    [slim(e) for e in entities],
        "topics":      [slim(t) for t in topics],
        "digestIndex": digest_index,
        "radar": radar if radar else None,  # include markdown — rendered inline, no fetch needed
    }

    OUT_JS.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JS.open("w", encoding="utf-8") as fp:
        fp.write("// AUTO-GENERATED — do not edit. Run: python scripts/build_web.py\n")
        fp.write("window.WIKI_DATA = ")
        json.dump(wiki_data, fp, ensure_ascii=False, indent=2)
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
    # Digests: index 今日聚焦 text + all story titles (compact, ~1-2 KB/day)
    for date_str, d in digest_all.items():
        focus_txt = "；".join(f["text"] for f in d.get("focus", []))
        titles = "；".join(
            s["title"]
            for sec in ("topStories", "techUpdates", "discussions", "billing")
            for s in d.get(sec, [])
        )
        search_index.append({
            "id":      date_str,
            "type":    "digest",
            "name":    f"日報 {date_str}",
            "summary": (d.get("preview") or "")[:90],
            "text":    f"{focus_txt}；{titles}",
        })
    with OUT_SEARCH_INDEX.open("w", encoding="utf-8") as fp:
        json.dump(search_index, fp, ensure_ascii=False, separators=(",", ":"))

    print(f"OK: {len(entities)} entities, {len(topics)} topics, {len(digest_all)} digests" +
          (" + radar" if radar else ""))
    print(f"    -> {OUT_JS} ({OUT_JS.stat().st_size//1024} KB)")
    print(f"    -> {OUT_SEARCH_INDEX} ({OUT_SEARCH_INDEX.stat().st_size//1024} KB)")
    print(f"    -> {OUT_WIKI_DIR}/ ({len(entities)+len(topics)} files)")
    print(f"    -> {OUT_DIGEST_DIR}/ ({len(digest_all)} files)")


if __name__ == "__main__":
    build()
