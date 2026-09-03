# -*- coding: utf-8 -*-
"""興趣類別 skill 榜：對使用者指定的類別搜 GitHub，產出覆寫式快照頁。

為什麼有這支（2026-09-03 使用者裁決）：熱度管線回答「大家在看什麼」（推播型），
使用者的需求是「我這幾類現在誰最熱、本週誰竄上來」（拉取型）——治理型類別
（agent 誠實、派工、規則不腐爛、git 衛生）在生態裡是少數派，永遠上不了熱度榜，
只能定向搜。設定檔 data/skill_interest_watch.json；A 組按 coding-workflow-guide
九段流程分類（連頁＋「第 N 段」提示，不連錨），與 devpractice 記者互相餵料。

用法：
    python scripts/skill_interest_snapshot.py            # 抓取＋寫頁＋記星史＋對帳
    python scripts/skill_interest_snapshot.py --probe    # 只印各 query 命中，供校準，不寫頁
    python scripts/skill_interest_snapshot.py --dry-run  # 抓取但不寫任何檔

環境（D6）：跑在 daily-gather GitHub Actions（有 GITHUB_TOKEN，search 30/min）與本機
（匿名 10/min，自動放慢）。輸出：wiki 頁（覆寫）、repo_star_history.csv（E 窗共用，
「本週竄升」即從此檔算，是 E 窗記錄端的第一個消費者）、discovery_queue_history.csv
（window=interest:<slug>，lint 6e 逐窗看守——某類連 3 天缺列即窗死）。
壞掉時：單一 query 失敗只 warning；整類零命中寫 note=error 不寫成「本類無熱門」；
星史不足 rise_window_days 天時「本週竄升」欄明寫冷啟動，不留白裝正常。
"""
import argparse
import csv
import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from news_aggregator.sources.github_releases import (  # noqa: E402
    _record_queue, _record_star_history, _emitted_repo_urls)

CONFIG = ROOT / "data" / "skill_interest_watch.json"
PAGE = ROOT / "wiki" / "topics" / "skill-interest-watch.md"
STAR_HISTORY = ROOT / "data" / "repo_star_history.csv"
GUIDE = "topics/coding-workflow-guide"

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("skill_interest")

TOKEN = os.getenv("GITHUB_TOKEN", "")
HEADERS = {"Accept": "application/vnd.github.v3+json", "User-Agent": "ClaudeNewsBot/1.0"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"
PACE_SECONDS = 2.5 if TOKEN else 6.5  # search 配額：有 token 30/min、匿名 10/min


def load_config() -> dict:
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def search(query: str, min_stars: int, per_page: int = 30) -> list[dict]:
    resp = requests.get(
        "https://api.github.com/search/repositories",
        headers=HEADERS, timeout=30,
        params={"q": f"{query} stars:>={min_stars}", "sort": "stars",
                "order": "desc", "per_page": per_page},
    )
    if resp.status_code == 403 and "rate limit" in resp.text.lower():
        raise RuntimeError("GitHub search rate limit hit")
    resp.raise_for_status()
    return resp.json().get("items", [])


def stars_days_ago(days: int) -> tuple[dict, int]:
    """讀星史檔：回傳 {repo_url: stars} 於 N 天前（取 ≤ 該日最近一筆）與檔案涵蓋天數。"""
    if not STAR_HISTORY.exists():
        return {}, 0
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    latest_before: dict[str, tuple[str, int]] = {}
    dates = set()
    with STAR_HISTORY.open(encoding="utf-8") as fp:
        for row in csv.DictReader(fp):
            d, url = row["date"], row["repo_url"]
            dates.add(d)
            try:
                s = int(row["stars"])
            except ValueError:
                continue
            if d <= cutoff and (url not in latest_before or d > latest_before[url][0]):
                latest_before[url] = (d, s)
    span = (max(dates) > min(dates)) and (
        (datetime.strptime(max(dates), "%Y-%m-%d") - datetime.strptime(min(dates), "%Y-%m-%d")).days) or 0
    return {u: s for u, (_, s) in latest_before.items()}, span


def collect(cfg: dict, probe: bool = False) -> dict:
    """逐類別查詢；回傳 {slug: {"repos": {url: repo}, "per_query": [(q, n)]}}。"""
    out = {}
    for cat in cfg["categories"]:
        repos: dict[str, dict] = {}
        per_query = []
        if cat.get("status") == "hidden":
            out[cat["slug"]] = {"repos": repos, "per_query": per_query}
            continue  # 隱藏類不查（省配額）、不印
        for q in cat["queries"]:
            try:
                items = search(q, cfg["min_stars"])
            except Exception as e:
                logger.warning("[%s] query failed: %s — %s", cat["slug"], q[:50], e)
                per_query.append((q, -1))
                time.sleep(PACE_SECONDS)
                continue
            per_query.append((q, len(items)))
            if probe:
                names = ", ".join(f"{r['full_name']}({r['stargazers_count']:,})" for r in items[:5])
                print(f"[{cat['slug']}] {len(items):>2} 命中 ← {q}\n      前 5：{names or '—'}")
            for r in items:
                repos[r["html_url"].rstrip("/")] = r
            time.sleep(PACE_SECONDS)
        out[cat["slug"]] = {"repos": repos, "per_query": per_query}
    return out


TOOLS_PAGE = ROOT / "wiki" / "topics" / "community-tech-tools.md"
TOOLS_LINK = "topics/community-tech-tools"


def judged_repo_urls() -> set[str]:
    """tools 頁（判斷層）出現過的 GitHub repo URL——機器唯讀人工頁，只用來標 🧭。"""
    try:
        text = TOOLS_PAGE.read_text(encoding="utf-8")
    except OSError:
        return set()
    import re
    return {m.group(0).rstrip("/").lower()
            for m in re.finditer(r"https://github\.com/[\w.\-]+/[\w.\-]+", text)}


def decision_table_from_tools() -> tuple[list[str], str]:
    """從 tools 頁（判斷的家）機械抄「我卡在這裡」決策表：回傳 (表格行列表, 圖例行)。

    2026-09-03 使用者裁決：開發實務 tab 只留本頁一頁，判斷仍只在 tools 頁**寫**（單一寫者），
    本頁每日重產時**抄**過來給讀者讀——「每個事實一個家」管的是誰寫，不是讀者在哪讀。
    抄本最多落後一天；抄不到（tools 頁改版）時明說，不留白裝正常。
    """
    try:
        text = TOOLS_PAGE.read_text(encoding="utf-8")
    except OSError:
        return [], ""
    import re as _re
    m = _re.search(r"^## 我卡在這裡\s*$(.*?)(?=^## |\Z)", text, _re.M | _re.S)
    if not m:
        return [], ""
    rows = [l.rstrip() for l in m.group(1).splitlines() if l.strip().startswith("|")]
    legend = next((l.strip() for l in m.group(1).splitlines() if l.strip().startswith("**圖例**")), "")
    return rows, legend


def render(cfg: dict, data: dict, now: datetime) -> str:
    today = now.strftime("%Y-%m-%d")
    before, span = stars_days_ago(cfg["rise_window_days"])
    cold = span < cfg["rise_window_days"]
    emitted = _emitted_repo_urls() or set()
    judged = judged_repo_urls()
    table_rows, legend = decision_table_from_tools()
    row_by_symptom = {}
    for l in table_rows:
        cells = [c.strip() for c in l.strip("|").split("|")]
        if len(cells) >= 4 and cells[0] not in ("我的症狀",) and not set(cells[0]) <= {"-", ":", " "}:
            row_by_symptom[cells[0]] = l
    n_active = sum(1 for c in cfg["categories"] if c.get("status") != "retired" and c.get("queries"))
    lines = [
        "# 興趣類別 skill 總覽",
        "",
        "**狀態：** ongoing",
        "**開始日期：** 2026-09-02",
        "**領域：** 🌐 社群",
        "**更新頻率：** 🗓️ 每日快照（機器產出；決策表抄自社群工具目錄、最多落後一天；「本週竄升」以七日星數差計）",
        f"**最後更新：** {today}",
        f"**最後新聞更新：** {today}",
        "",
        f"> **本頁是什麼**（{today} 快照）",
        "> 讀者關心的開發實務類別，一頁看完兩件事：**該裝哪個**（「我卡在這裡」決策表——有人判斷過、帶證據等級與判定日）"
        f"與**這一類現在誰大、本週誰在漲**（GitHub 每日規模榜，{n_active} 類可用 GitHub 辨識）。"
        "**星數是規模不是品質**：榜不做推薦，推薦只看決策表；榜上標 🧭 的工具代表決策表或工具目錄已有判斷。"
        "判斷的完整證據、推薦細節、Skills 速查與 125 列工具目錄在 [[topics/community-tech-tools]]。",
        "",
        "---",
        "",
        "## 我卡在這裡（決策表）",
        "",
        f"本表每日機械抄自 [[topics/community-tech-tools]]（判斷與證據的家；改判斷請改那頁），抄錄日 {today}。",
        "",
    ]
    if table_rows:
        lines += table_rows + ([""] + [legend, ""] if legend else [""])
    else:
        lines += ["> ⚠️ 本次抄不到決策表（社群工具目錄的「我卡在這裡」節可能改版）——請直接看 [[topics/community-tech-tools]]。", ""]
    lines += [
        "---",
        "",
        "## 各類別：本庫判斷＋規模榜",
        "",
        "| 欄 | 意思 |",
        "|---|---|",
        "| 本庫判斷 | 該類別對應的決策表列（同上表，就近重印方便對照） |",
        "| 目前前 5 | 該類別 GitHub 搜尋命中的 repo 依星數排序，星數為快照當日值 |",
        "| 本週竄升 | 七日內星數增量 ≥ "
        f"{cfg['rise_min_delta']:,} 者，依增量排序；資料來自本庫每日記錄的星數 |",
        "| 📰 | 本庫日報已報導過 |",
        "| 🧭 | 決策表或工具目錄已有判斷 |",
        "",
        "> 榜依 GitHub 描述機械比對，偶有跨類誤收（同一 repo 出現在兩類、或非本類工具混入）；星數與分類皆非推薦。",
        "",
    ]
    if cold:
        lines += [f"> ⚠️ 星數記錄目前只涵蓋 {span} 天（需 {cfg['rise_window_days']} 天），"
                  "「本週竄升」欄尚在冷啟動，本週先只看「目前前 5」。", ""]
    groups = {"A": "## A. 開發實務（按流程階段，對應 [[topics/coding-workflow-guide]]）",
              "B": "## B. 治理（管 agent 的需求）"}

    def judgment_block(cat: dict, has_judged: bool) -> list[str]:
        sym = cat.get("tools_symptom")
        syms = ([sym] if isinstance(sym, str) else sym) if sym else []
        rows = [row_by_symptom[s] for s in syms if s in row_by_symptom]
        if rows:
            out = ["**本庫判斷**（同頁首決策表對應列）", "", "| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |", "|---|---|---|---|"] + rows
            if cat.get("caveat"):
                out += ["", f"> {cat['caveat']}"]
            return out
        if cat.get("tools_note"):
            return [f"**本庫判斷**：{cat['tools_note']}"]
        if has_judged:
            return [f"**本庫判斷**：標 🧭 者的判斷見 [[{TOOLS_LINK}]] Skills 速查或工具目錄"]
        return ["**本庫判斷**：本庫尚無判斷（榜上無 🧭 條目）——星數不是推薦，裝前自行查證"]

    current_group = None
    for cat in cfg["categories"]:
        if cat.get("status") == "hidden" or cat.get("group") == "C":
            continue  # hidden：設定保留不印；C 組＝本站維運需求，另出 site-source-tooling 頁
        if cat["group"] != current_group:
            current_group = cat["group"]
            lines += [groups[current_group], ""]
        anchor = f"（對應 [[{GUIDE}]] {cat['guide_section']}）" if cat.get("guide_section") else ""
        lines += [f"### {cat['name']}{anchor}", ""]
        if cat.get("status") == "retired" or not cat.get("queries"):
            lines += judgment_block(cat, False)
            lines += ["", "規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。", ""]
            continue
        d = data.get(cat["slug"], {"repos": {}, "per_query": []})
        repos = d["repos"]
        hits = [n for _, n in d["per_query"]]
        top = sorted(repos.values(), key=lambda r: r["stargazers_count"], reverse=True)[:cfg["top_n"]]
        any_judged = any(r["html_url"].rstrip("/").lower() in judged for r in top)
        lines += judgment_block(cat, any_judged) + [""]
        if not repos:
            lines += ["> ⚠️ 規模榜本次零命中"
                      + ("（查詢失敗）" if any(n < 0 for n in hits) else "（搜尋條件需校準）")
                      + "——不代表本類沒有工具。", ""]
            continue
        lines += ["| 目前前 5 | ★ | 一句話 |", "|---|---|---|"]
        for r in top:
            url = r["html_url"].rstrip("/")
            mark = (" 🧭" if url.lower() in judged else "") + (" 📰" if url.lower() in emitted else "")
            full = (r.get("description") or "").replace("|", "／")
            desc = full if len(full) <= 90 else full[:89].rstrip() + "…"
            lines.append(f"| [{r['full_name']}]({url}){mark} | {r['stargazers_count']:,} | {desc} |")
        risers = []
        if not cold:
            for url, r in repos.items():
                prev = before.get(url)
                if prev is not None and r["stargazers_count"] - prev >= cfg["rise_min_delta"]:
                    risers.append((r["stargazers_count"] - prev, r))
            risers.sort(key=lambda t: t[0], reverse=True)
        if risers:
            lines += ["", "| 本週竄升 | 七日增量 | ★ 現值 |", "|---|---|---|"]
            for delta, r in risers[:cfg["top_n"]]:
                lines.append(f"| [{r['full_name']}]({r['html_url']}) | +{delta:,} | {r['stargazers_count']:,} |")
        elif not cold:
            lines += ["", f"本週無 ≥{cfg['rise_min_delta']:,} 星的竄升者。"]
        lines.append("")
    lines += [
        "---",
        "",
        "## 參考來源",
        "",
        "- 決策表與判斷：[[topics/community-tech-tools]]（每週人工策展；本頁每日抄錄）",
        "- 規模榜：GitHub Search API（依星數排序，每日快照）；「本週竄升」以本庫每日記錄的星數差計算，保留 60 天",
        "- 類別與搜尋條件由維護者校準（每條 query 上線前實測命中；找不到有辨識力 query 的類別只印判斷，不掛空榜）",
        "",
    ]
    return "\n".join(lines)

PAGE_SITE = ROOT / "wiki" / "topics" / "site-source-tooling.md"


def render_site(cfg: dict, data: dict, now: datetime) -> str:
    """C 組（本站維運需求）獨立頁：只有規模榜，不做判斷——2026-09-03 使用者裁決
    「找個合適的頁面放」，理由：它服務的是本站怎麼抓料，不是讀者的開發實務。"""
    today = now.strftime("%Y-%m-%d")
    cats = [c for c in cfg["categories"] if c.get("group") == "C" and c.get("status") == "active"]
    emitted = _emitted_repo_urls() or set()
    lines = [
        "# 本站抓料工具規模榜",
        "",
        "**狀態：** ongoing",
        "**開始日期：** 2026-09-03",
        "**領域：** 🛠️ 工具/功能",
        "**更新頻率：** 🗓️ 每日快照（機器產出；只有星數，不做推薦）",
        f"**最後更新：** {today}",
        f"**最後新聞更新：** {today}",
        "",
        f"> **本頁是什麼**（{today} 快照）",
        "> 本站自己的資料來源會壞（RSS 分數恆 0、事件流退化、來源改版），這頁每天到 GitHub 看「新聞聚合／爬蟲韌性這一類現在誰大」，"
        "當本站評估抓料工具時的參考。**不是讀者的開發實務**——開發實務入口在 [[index]]；**星數是規模不是品質**。",
        "",
        "---",
        "",
    ]
    for cat in cats:
        d = data.get(cat["slug"], {"repos": {}, "per_query": []})
        top = sorted(d["repos"].values(), key=lambda r: r["stargazers_count"], reverse=True)[:cfg["top_n"]]
        lines += [f"## {cat['name']}", ""]
        if not top:
            lines += ["> ⚠️ 本次零命中（查詢失敗或搜尋條件需校準）。", ""]
            continue
        lines += ["| 目前前 5 | ★ | 一句話 |", "|---|---|---|"]
        for r in top:
            url = r["html_url"].rstrip("/")
            mark = " 📰" if url.lower() in emitted else ""
            full = (r.get("description") or "").replace("|", "／")
            desc = full if len(full) <= 90 else full[:89].rstrip() + "…"
            lines.append(f"| [{r['full_name']}]({url}){mark} | {r['stargazers_count']:,} | {desc} |")
        lines.append("")
    lines += ["---", "", "## 參考來源", "", "- GitHub Search API 每日快照；📰＝本庫日報已報導過。本站來源健康與記分卡見網站「關於」頁。", ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true", help="只印命中，供 query 校準")
    ap.add_argument("--dry-run", action="store_true", help="不寫任何檔")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    cfg = load_config()
    now = datetime.now(timezone.utc)
    data = collect(cfg, probe=args.probe)
    if args.probe:
        return 0
    star_seen = {u: r["stargazers_count"] for d in data.values() for u, r in d["repos"].items()}
    if args.dry_run:
        print(render(cfg, data, now))
        return 0
    _record_star_history(star_seen, now)
    for cat in cfg["categories"]:
        d = data[cat["slug"]]
        failed = any(n < 0 for _, n in d["per_query"])
        if cat.get("status") == "retired":
            note = "retired"  # 刻意撤下，lint 6e 不得判為窗死
        elif cat.get("status") == "hidden" or not cat.get("queries"):
            note = "disabled"
        elif failed and not d["repos"]:
            note = "error"
        else:
            note = "ok"
        _record_queue(f"interest:{cat['slug']}", queued=len(d["repos"]),
                      emitted_n=min(len(d["repos"]), cfg["top_n"]), now=now, note=note)
    PAGE.write_text(render(cfg, data, now), encoding="utf-8")
    if any(c.get("group") == "C" and c.get("status") == "active" for c in cfg["categories"]):
        PAGE_SITE.write_text(render_site(cfg, data, now), encoding="utf-8")
    logger.info("skill-interest-watch: %d categories, %d repos, page written",
                len(cfg["categories"]), len(star_seen))
    return 0


if __name__ == "__main__":
    sys.exit(main())
