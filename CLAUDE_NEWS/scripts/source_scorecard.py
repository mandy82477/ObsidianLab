#!/usr/bin/env python3
"""
source_scorecard.py — 來源記分卡：從 funnel + attribution 兩份 ledger 算出每來源的效益指標。

只用標準庫、零 LLM、確定性輸出。設計依據與公式出處：docs/source-scoring-optimization.md。

用法：
    python scripts/source_scorecard.py            # 輸出 markdown 記分卡到 stdout
    python scripts/source_scorecard.py --json     # 輸出機器可讀 JSON（供未來自動化）

指標（監控用，不回饋 pipeline；enforcement 屬 Phase 2，需 60 天以上樣本＋/pipeline-change-check）：
    收錄率   = emitted / gathered（Bayesian 假票平滑，先驗＝全站平均，k=20）
    wiki 率  = wiki 歸因筆數 / emitted（同法，k=10）
    Presence = 該來源 wiki 歸因占全站比例（Techmeme 式）
    Wilson   = 收錄率的 95% 信賴區間下界（小樣本自動壓低，供排序參考）
    HHI      = Presence 平方和（來源集中度，越高越依賴少數來源）
    domain 先驗 = attribution 條目 URL 對 Lin et al. (2023) domain 分數（pc1 0–1）的分佈

樣本閘門：觀測天數 < MIN_DAYS 或 gathered < MIN_GATHERED 的來源標「樣本不足」，數字僅供趨勢觀察。
"""
import argparse
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
REGISTRY_FILE = DATA_DIR / "source_registry.json"
FUNNEL_FILE = DATA_DIR / "source_funnel.jsonl"
ATTRIBUTION_FILE = DATA_DIR / "source_attribution.jsonl"
DOMAIN_PC1_FILE = DATA_DIR / "external" / "domain_pc1.csv"

PSEUDO_K_EMIT = 20   # 收錄率平滑假票數
PSEUDO_K_WIKI = 10   # wiki 率平滑假票數
MIN_DAYS = 14        # 樣本閘門：最少觀測天數
MIN_GATHERED = 30    # 樣本閘門：最少抓取條數
PC1_HIGH = 0.7       # domain 分數分桶
PC1_LOW = 0.4


def smoothed_rate(successes: int, trials: int, prior_rate: float, k: int) -> float:
    """Bayesian 假票平滑：(successes + k*prior) / (trials + k)。trials=0 時回先驗。"""
    denom = trials + k
    if denom <= 0:
        return prior_rate
    return (successes + k * prior_rate) / denom


def wilson_lower(successes: int, trials: int, z: float = 1.96) -> float:
    """二項比例的 Wilson score 95% 信賴區間下界（Evan Miller 版公式）。"""
    if trials <= 0:
        return 0.0
    p = successes / trials
    n = trials
    denom = 1 + z * z / n
    centre = p + z * z / (2 * n)
    margin = z * math.sqrt((p * (1 - p) + z * z / (4 * n)) / n)
    return max(0.0, (centre - margin) / denom)


def hhi(shares: list[float]) -> float:
    """Herfindahl–Hirschman 集中度指數：占比平方和（0–1，越高越集中）。"""
    return sum(s * s for s in shares)


def load_registry(path: Path = REGISTRY_FILE) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)["sources"]


def load_funnel(path: Path = FUNNEL_FILE) -> dict:
    """讀 funnel jsonl，每個日期只取 gathered 總數最大的一筆（gather/render/backfill 會重複記同日）。

    回傳 {"days": N, "dates": (min, max), "per_source": {name: {gathered, filtered, emitted}}}
    """
    best_by_date: dict[str, dict] = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                d = row.get("date", "")
                cur = best_by_date.get(d)
                if cur is None or row.get("totals", {}).get("gathered", 0) > cur.get("totals", {}).get("gathered", 0):
                    best_by_date[d] = row

    per_source: dict[str, dict] = defaultdict(lambda: {"gathered": 0, "filtered": 0, "emitted": 0, "days_seen": 0})
    for row in best_by_date.values():
        for name, st in row.get("sources", {}).items():
            agg = per_source[name]
            agg["gathered"] += int(st.get("gathered", 0))
            agg["filtered"] += int(st.get("filtered", 0))
            agg["emitted"] += int(st.get("emitted", 0))
            agg["days_seen"] += 1

    dates = sorted(best_by_date.keys())
    return {
        "days": len(dates),
        "dates": (dates[0], dates[-1]) if dates else ("—", "—"),
        "per_source": dict(per_source),
    }


def load_attribution(path: Path = ATTRIBUTION_FILE) -> list[dict]:
    rows = []
    if path.exists():
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    return rows


def load_domain_scores(path: Path = DOMAIN_PC1_FILE) -> dict[str, float]:
    scores: dict[str, float] = {}
    if path.exists():
        with open(path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                try:
                    scores[row["domain"].strip().lower()] = float(row["pc1"])
                except (KeyError, ValueError):
                    continue
    return scores


def lookup_pc1(url: str, scores: dict[str, float]) -> float | None:
    """host 全名查表，查不到就逐層剝 subdomain（news.reuters.com → reuters.com）。"""
    try:
        host = (urlparse(url).netloc or "").lower().split(":")[0]
    except ValueError:
        return None
    if host.startswith("www."):
        host = host[4:]
    labels = host.split(".")
    while len(labels) >= 2:
        candidate = ".".join(labels)
        if candidate in scores:
            return scores[candidate]
        labels = labels[1:]
    return None


def pc1_bucket(score: float | None) -> str:
    if score is None:
        return "unknown"
    if score >= PC1_HIGH:
        return "high"
    if score >= PC1_LOW:
        return "mid"
    return "low"


def compute(registry: list[dict], funnel: dict, attribution: list[dict],
            domain_scores: dict[str, float]) -> dict:
    per_source = funnel["per_source"]
    total_gathered = sum(s["gathered"] for s in per_source.values())
    total_emitted = sum(s["emitted"] for s in per_source.values())
    prior_emit = (total_emitted / total_gathered) if total_gathered else 0.0

    hits_by_slug: dict[str, int] = defaultdict(int)
    buckets_by_slug: dict[str, dict] = defaultdict(lambda: defaultdict(int))
    for row in attribution:
        slug = row.get("source", "_unknown")
        hits_by_slug[slug] += 1
        buckets_by_slug[slug][pc1_bucket(lookup_pc1(row.get("item_url", ""), domain_scores))] += 1
    total_hits = sum(hits_by_slug.values())
    prior_wiki = (total_hits / total_emitted) if total_emitted else 0.0

    known_slugs = set()
    rows = []
    for src in registry:
        name, slug = src["name"], src["slug"]
        known_slugs.add(slug)
        f = per_source.get(name, {"gathered": 0, "filtered": 0, "emitted": 0, "days_seen": 0})
        hits = hits_by_slug.get(slug, 0)
        low_sample = f["days_seen"] < MIN_DAYS or f["gathered"] < MIN_GATHERED
        rows.append({
            "name": name,
            "slug": slug,
            "active": src.get("active", True),
            "score_reliability": src.get("score_reliability", "none"),
            "curation_mode": src.get("curation_mode", "content"),
            "rate_comparable": src.get("rate_comparable", True),
            "days_seen": f["days_seen"],
            "gathered": f["gathered"],
            "filtered": f["filtered"],
            "emitted": f["emitted"],
            "wiki_hits": hits,
            "emit_rate": smoothed_rate(f["emitted"], f["gathered"], prior_emit, PSEUDO_K_EMIT),
            "emit_wilson": wilson_lower(f["emitted"], f["gathered"]),
            "wiki_rate": smoothed_rate(hits, f["emitted"], prior_wiki, PSEUDO_K_WIKI),
            "presence": (hits / total_hits) if total_hits else 0.0,
            "low_sample": low_sample,
            "pc1_buckets": dict(buckets_by_slug.get(slug, {})),
        })

    unknown_hits = {s: n for s, n in hits_by_slug.items() if s not in known_slugs}
    presence_hhi = hhi([r["presence"] for r in rows if r["presence"] > 0])
    return {
        "window": {"days": funnel["days"], "from": funnel["dates"][0], "to": funnel["dates"][1]},
        "totals": {"gathered": total_gathered, "emitted": total_emitted, "wiki_hits": total_hits,
                   "prior_emit": prior_emit, "prior_wiki": prior_wiki},
        "hhi": presence_hhi,
        "sources": rows,
        "unknown_slugs": unknown_hits,
        "domain_data_loaded": len(domain_scores),
    }


def render_markdown(result: dict) -> str:
    w, t = result["window"], result["totals"]
    lines = [
        "# 來源記分卡",
        "",
        f"觀測窗：{w['from']} ～ {w['to']}（{w['days']} 天）｜全站：抓取 {t['gathered']}、"
        f"收錄 {t['emitted']}（基準收錄率 {t['prior_emit']:.0%}）、wiki 歸因 {t['wiki_hits']} 筆"
        f"（基準 wiki 率 {t['prior_wiki']:.0%}）",
        f"來源集中度 HHI：{result['hhi']:.3f}（>0.25 高度集中）｜domain 信譽表：{result['domain_data_loaded']:,} 筆",
        "",
        "> 指標為**平滑後**數值（小樣本被拉向全站基準）；標 ⚠️ 者樣本不足"
        f"（< {MIN_DAYS} 天或 < {MIN_GATHERED} 條），數字僅供趨勢觀察，不可作汰換依據。",
        "",
        "## 社群 / 媒體來源（依 Presence 排序）",
        "",
        "| 來源 | 樣本 | 抓取 | 收錄 | wiki | 收錄率* | Wilson下界 | wiki率* | Presence | 分數可信度 |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    has_incomparable = False
    active = [r for r in result["sources"] if r["active"]]
    for r in sorted((r for r in active if r["curation_mode"] != "whitelist"),
                    key=lambda x: -x["presence"]):
        flag = "⚠️" if r["low_sample"] else "✅"
        if r["gathered"] == 0:
            emit_cell, wilson_cell = "—", "—"
        else:
            dagger = "" if r["rate_comparable"] else "†"
            emit_cell = f"{r['emit_rate']:.0%}{dagger}"
            wilson_cell = f"{r['emit_wilson']:.0%}{dagger}"
            has_incomparable = has_incomparable or not r["rate_comparable"]
        wiki_cell = f"{r['wiki_rate']:.0%}" if r["emitted"] > 0 else "—"
        lines.append(
            f"| {r['name']} | {flag} {r['days_seen']}天 | {r['gathered']} | {r['emitted']} | {r['wiki_hits']} "
            f"| {emit_cell} | {wilson_cell} | {wiki_cell} "
            f"| {r['presence']:.0%} | {r['score_reliability']} |"
        )
    if has_incomparable:
        lines.append("")
        lines.append("† 抓法為跨日重覆視窗（如 dev.to top=30），gathered 含跨日重複、"
                     "收錄率結構性偏低，**不可與 26h 窗來源比較**，只看自身趨勢。")

    lines += [
        "",
        "## 官方 / 白名單來源（保險性來源，不排名）",
        "",
        "> 這組的價值是「事件發生時第一時間在場」（官方源）或「策展名單的長期沉澱」（Blogroll），"
        "比率與 Presence 排名不適用；要盯的是**漏接與斷線**（wiki-lint 6e 連續缺席告警）與"
        "**probation 期滿的絕對命中數**（Blogroll，見 docs/workaround-register.md）。官方源抓取 0 = 該期間無官方更新，屬正常。",
        "",
        "| 來源 | 樣本 | 抓取 | 收錄 | wiki 筆數 |",
        "|---|---|---|---|---|",
    ]
    for r in sorted((r for r in active if r["curation_mode"] == "whitelist"),
                    key=lambda x: x["name"]):
        flag = "⚠️" if r["low_sample"] else "✅"
        lines.append(f"| {r['name']} | {flag} {r['days_seen']}天 | {r['gathered']} | {r['emitted']} | {r['wiki_hits']} |")

    gnews = next((r for r in result["sources"] if r["slug"] == "google-news"), None)
    if gnews and gnews["pc1_buckets"]:
        b = gnews["pc1_buckets"]
        lines += [
            "",
            "## Google News domain 信譽分佈（wiki 歸因條目，Lin et al. 2023 pc1）",
            "",
            f"- 高信譽（≥ {PC1_HIGH}）：{b.get('high', 0)} 筆",
            f"- 中間（{PC1_LOW}–{PC1_HIGH}）：{b.get('mid', 0)} 筆",
            f"- 低信譽（< {PC1_LOW}）：{b.get('low', 0)} 筆 ← 若持續出現，優先人工覆核",
            f"- 未知（不在表內，多為新興垂直媒體）：{b.get('unknown', 0)} 筆",
        ]

    if result["unknown_slugs"]:
        lines += ["", "## ⚠️ 未註冊 slug（attribution 出現但 registry 查無，需修 registry 或記者回報）", ""]
        for s, n in sorted(result["unknown_slugs"].items()):
            lines.append(f"- `{s}`：{n} 筆")

    lines += [
        "",
        "---",
        "*收錄率與 wiki 率為 Bayesian 假票平滑值（k=20/10，先驗＝全站基準）。"
        "Wilson 下界為未平滑收錄率的 95% 信賴區間下界。公式與設計依據：`docs/source-scoring-optimization.md`。*",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="來源記分卡")
    parser.add_argument("--json", action="store_true", help="輸出 JSON 而非 markdown")
    args = parser.parse_args()

    result = compute(load_registry(), load_funnel(), load_attribution(), load_domain_scores())
    if args.json:
        out = json.dumps(result, ensure_ascii=False, indent=2)
    else:
        out = render_markdown(result)

    # Windows console 常為 cp950，強制 UTF-8 避免中文/emoji 壞掉（同 run_tests.py 做法）
    if hasattr(sys.stdout, "buffer"):
        sys.stdout.buffer.write(out.encode("utf-8"))
        sys.stdout.buffer.write(b"\n")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
