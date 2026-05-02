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
NEWS_DIR      = ROOT / "news"
OUT_JS        = ROOT / "web_reader" / "data" / "data.js"
OUT_WIKI_DIR  = ROOT / "web_reader" / "data" / "wiki"
OUT_DIGEST_DIR= ROOT / "web_reader" / "data" / "digest"

# ── Status → CSS pill class ──────────────────────────────────────────────────

STATUS_MAP = {
    "active": "active",
    "ongoing": "active",
    "monitoring": "warn",
    "deprecated": "danger",
    "rumoured": "info",
    "resolved": "gray",
    "秘密開發中": "warn",
    "公開測試版": "active",
    "active": "active",
}


def pill_class(status: str) -> str:
    s = status.strip().lower()
    for k, v in STATUS_MAP.items():
        if k.lower() in s:
            return v
    return "gray"


# ── Wiki page parser ─────────────────────────────────────────────────────────

META_RE = {
    "entityType": re.compile(r"\*\*類型[：:]\*\*\s*(.+)"),
    "type":       re.compile(r"\*\*類型[：:]\*\*\s*(.+)"),
    "status":     re.compile(r"\*\*狀態[：:]\*\*\s*(.+)"),
    "firstSeen":  re.compile(r"\*\*首次出現[：:]\*\*\s*(.+)"),
    "startDate":  re.compile(r"\*\*開始日期[：:]\*\*\s*(.+)"),
    "lastUpdated":re.compile(r"\*\*最後更新[：:]\*\*\s*(.+)"),
}

SUMMARY_HEADERS = ["## 現況", "## 摘要"]


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
        "pill": "gray",
        "firstSeen": "",
        "startDate": "",
        "lastUpdated": "",
        "summary": "",
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
    meta["pill"] = pill_class(meta["status"])

    return meta


# ── Digest parser ─────────────────────────────────────────────────────────────

SECTION_EMOJI = {"⭐": "topStories", "🔧": "techUpdates", "💬": "discussions",
                 "💰": "billing", "📌": "focus"}

SENTIMENT_RE = re.compile(r"`情緒：(.+?)`")
# star stories start with "⭐ **[Title](url)**" — strip any leading emoji/chars before **
STORY_RE = re.compile(r"\*\*\[(.+?)\]\((.+?)\)\*\*")
SOURCE_RE = re.compile(r"^`(.+?)`\s*·\s*(.+?)(?:\s*UTC)?(?:\s*·\s*`情緒：(.+?)`)?$")
FOCUS_RE = re.compile(r"^-\s+\*\*(.+?)\*\*\s+(.*)")
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
            if re.match(rf"^#+\s+{re.escape(emoji)}", line):
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

            # focus items
            if current_section == "focus":
                m = FOCUS_RE.match(line)
                if m:
                    tag, text = m.group(1).strip(), m.group(2).strip()
                    result["focus"].append({"tag": tag, "text": text})
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

    # ── Write per-wiki JSON files (full content including markdown) ──────────
    OUT_WIKI_DIR.mkdir(parents=True, exist_ok=True)
    existing_wiki_ids = {f.stem for f in OUT_WIKI_DIR.glob("*.json")}
    current_wiki_ids  = {item["id"] for item in entities + topics}
    for stale in existing_wiki_ids - current_wiki_ids:
        (OUT_WIKI_DIR / f"{stale}.json").unlink()
        print(f"  [clean] removed stale wiki/{stale}.json")
    for item in entities + topics:
        with (OUT_WIKI_DIR / f"{item['id']}.json").open("w", encoding="utf-8") as fp:
            json.dump(item, fp, ensure_ascii=False, indent=2)

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
    }

    OUT_JS.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JS.open("w", encoding="utf-8") as fp:
        fp.write("// AUTO-GENERATED — do not edit. Run: python scripts/build_web.py\n")
        fp.write("window.WIKI_DATA = ")
        json.dump(wiki_data, fp, ensure_ascii=False, indent=2)
        fp.write(";\n")
        fp.write("// Digest content is loaded on-demand from data/digest/{date}.json\n")
        fp.write("// Wiki content is loaded on-demand from data/wiki/{id}.json\n")

    # Update cache-busting version in index.html
    ver = str(int(time.time()))
    index = ROOT / "web_reader" / "index.html"
    if index.exists():
        html = index.read_text(encoding="utf-8")
        import re as _re
        html = _re.sub(r'data/data\.js(\?v=\d+)?', f'data/data.js?v={ver}', html)
        index.write_text(html, encoding="utf-8")

    print(f"OK: {len(entities)} entities, {len(topics)} topics, {len(digest_all)} digests")
    print(f"    -> {OUT_JS} ({OUT_JS.stat().st_size//1024} KB)")
    print(f"    -> {OUT_WIKI_DIR}/ ({len(entities)+len(topics)} files)")
    print(f"    -> {OUT_DIGEST_DIR}/ ({len(digest_all)} files)")


if __name__ == "__main__":
    build()
