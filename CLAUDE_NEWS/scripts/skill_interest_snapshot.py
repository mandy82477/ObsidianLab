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


def render(cfg: dict, data: dict, now: datetime) -> str:
    today = now.strftime("%Y-%m-%d")
    before, span = stars_days_ago(cfg["rise_window_days"])
    cold = span < cfg["rise_window_days"]
    emitted = _emitted_repo_urls() or set()
    judged = judged_repo_urls()
    active = [c for c in cfg["categories"] if c.get("status") != "retired" and c.get("queries")]
    retired = [c for c in cfg["categories"] if c.get("status") == "retired"]
    lines = [
        "# 興趣類別 skill 榜",
        "",
        "**狀態：** ongoing",
        "**開始日期：** 2026-09-03",
        "**領域：** 🌐 社群",
        "**更新頻率：** 🗓️ 每日快照（機器產出；「本週竄升」以七日星數差計）",
        f"**最後更新：** {today}",
        f"**最後新聞更新：** {today}",
        "",
        f"> **本頁是什麼**（{today} 快照）",
        f"> 針對讀者指定的類別（{len(active)} 類可用 GitHub 辨識），每天到 GitHub 問「這一類現在誰最熱、本週誰竄上來」。"
        "本頁是**感測層**（機器、規模、零判斷）；**判斷層**在 [[topics/community-tech-tools]]——"
        "該裝哪個、證據多強、為什麼。每類末的「本庫判斷 →」是唯一的橋（單向：榜連 tools，tools 不抄榜）。"
        "**星數是規模不是品質**。",
        "",
        "---",
        "",
        "## 怎麼讀",
        "",
        "| 欄 | 意思 |",
        "|---|---|",
        "| 目前前 5 | 該類別 query 命中的 repo 依星數排序，星數為快照當日值 |",
        "| 本週竄升 | 七日內星數增量 ≥ "
        f"{cfg['rise_min_delta']:,} 者，依增量排序；資料來自各發現窗每日記錄的星史檔 |",
        "| 📰 | 本庫日報或清倉帳本已報導過 |",
        "| 🧭 | 本庫已有判斷——該 repo 出現在 [[topics/community-tech-tools]]（決策表／速查／目錄） |",
        "",
    ]
    if cold:
        lines += [f"> ⚠️ 星史檔目前只涵蓋 {span} 天（需 {cfg['rise_window_days']} 天），"
                  "「本週竄升」欄尚在冷啟動，本週先只看「目前前 5」。", ""]
    groups = {"A": "## A. 開發實務（按流程階段，對應 [[topics/coding-workflow-guide]]）",
              "B": "## B. 治理（管 agent 的需求）"}
    def bridge_line(cat: dict) -> str:
        if cat.get("tools_symptom"):
            return f"本庫判斷 → 見 [[{TOOLS_LINK}]]「我卡在這裡」的「{cat['tools_symptom']}」列"
        if cat.get("tools_note"):
            return f"本庫判斷 → {cat['tools_note']}"
        return f"本庫判斷 → 見 [[{TOOLS_LINK}]]（🧭 者已有證據等級與一句為什麼）"

    current_group = None
    for cat in active:
        if cat["group"] != current_group:
            current_group = cat["group"]
            lines += [groups[current_group], ""]
        d = data.get(cat["slug"], {"repos": {}, "per_query": []})
        repos = d["repos"]
        # 連頁不連錨：guide 段標題帶 [社群面待補]/[已補] 這類會變的標記，錨定必腐化
        anchor = f"（對應 [[{GUIDE}]] {cat['guide_section']}）" if cat.get("guide_section") else ""
        lines += [f"### {cat['name']}{anchor}", ""]
        hits = [n for _, n in d["per_query"]]
        if not repos:
            lines += ["> ⚠️ 本類別本次零命中"
                      + ("（query 失敗）" if any(n < 0 for n in hits) else "（query 需校準）")
                      + "——不代表本類沒有工具。", ""]
            continue
        top = sorted(repos.values(), key=lambda r: r["stargazers_count"], reverse=True)[:cfg["top_n"]]
        lines += ["| 目前前 5 | ★ | 一句話 |", "|---|---|---|"]
        for r in top:
            url = r["html_url"].rstrip("/")
            mark = (" 🧭" if url.lower() in judged else "") + (" 📰" if url.lower() in emitted else "")
            desc = (r.get("description") or "").replace("|", "／")[:90]
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
        lines += ["", bridge_line(cat), ""]
    if retired:
        lines += [
            "## 無法用 GitHub 辨識的需求（指路）",
            "",
            "以下需求兩輪 query 校準皆被巨頭洗版或 0 命中——不是還沒調好，是**感測器裝錯層**："
            "治理型需求是讀者講痛點的語言（「它說做完了但沒做」），在 HN／dev.to 全文，不在 repo 描述。"
            "本頁不掛空榜；答案在判斷層：",
            "",
            "| 需求 | 本庫判斷 |",
            "|---|---|",
        ]
        for cat in retired:
            lines.append(f"| {cat['name']} | {bridge_line(cat).replace('本庫判斷 → ', '')} |")
        lines.append("")
    lines += [
        "---",
        "",
        "## 參考來源",
        "",
        "- 設定檔與 query 校準紀錄：`data/skill_interest_watch.json`；產出腳本 `scripts/skill_interest_snapshot.py`",
        "- 星史：`data/repo_star_history.csv`（各發現窗每日記錄，保留 60 天）",
        "",
    ]
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
        elif not cat.get("queries"):
            note = "disabled"
        elif failed and not d["repos"]:
            note = "error"
        else:
            note = "ok"
        _record_queue(f"interest:{cat['slug']}", queued=len(d["repos"]),
                      emitted_n=min(len(d["repos"]), cfg["top_n"]), now=now, note=note)
    PAGE.write_text(render(cfg, data, now), encoding="utf-8")
    logger.info("skill-interest-watch: %d categories, %d repos, page written",
                len(cfg["categories"]), len(star_seen))
    return 0


if __name__ == "__main__":
    sys.exit(main())
