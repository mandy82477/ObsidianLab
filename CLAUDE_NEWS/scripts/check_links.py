#!/usr/bin/env python3
"""
check_links.py — 月檢 wiki/**/*.md 中的外部連結（http/https），找出疑似死鏈。

排除 news/ 目錄——歷史日報的外部連結自然腐爛屬正常現象，不列入死鏈檢查。

用法：
    python scripts/check_links.py            # 掃描全部
    python scripts/check_links.py --limit 20  # 只驗證前 20 條（快速驗證邏輯用）

僅使用標準庫（urllib），不依賴第三方套件。
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_DIR = ROOT / "wiki"

# 停在空白、markdown/引號收尾字元、以及全形標點與 CJK 字元（URL 後面緊接中文說明時常見，如「...id=123（HN」）
# 排除全形標點：中文行文裡它們緊貼 URL 後方，被吃進去會產生「無回應」的假結果。
# 2026-08-30 實例：`…cybersecurity；Digital` 讓 urllib 直接拋 ascii 編碼錯誤。
# `一-鿿` 只涵蓋漢字，全形標點不在該區段，需逐個列出。
URL_RE = re.compile(r'https?://[^\s\)\]>"\'`（）「」『』、，。；：？！…—《》〈〉【】一-鿿]+')

TIMEOUT = 10
_SEP = chr(10)
USER_AGENT = "Mozilla/5.0 (compatible; ClaudeNewsLinkChecker/1.0; +https://github.com/)"

# 「擋機器人」而非「內容不存在」的狀態碼：不算死鏈，只標記人工確認。
#
# 401 是 2026-08-20 首次全量掃描後補進來的：15 筆 401 全部來自 Reuters(10)／
# Barron's(3)／WSJ(2)，是付費牆／登入牆，內容其實還在。原本把它歸為死鏈，
# 會讓記者在頁面標「（原文已失效）」——正是雲端 egress 守衛當初要防的頁面污染。
ANTI_BOT_CODES = {401, 403, 429}

# 只有這些狀態碼代表「內容真的不在了」，也只有它們會驅動頁面標註。
# 5xx 不列入：伺服器暫時掛掉不等於文章消失。
DEAD_CODES = {404, 410}

# 逾時／連線失敗重試一次用的較長逾時。單次逾時是很弱的證據——2026-08-20
# 全量掃描有 38 筆逾時，含 www.anthropic.com 自己逾時 3 次，顯然不是死鏈。
RETRY_TIMEOUT = 25


def collect_links() -> dict[str, list[Path]]:
    """回傳 {url: [引用此連結的頁面, ...]}，排除 news/ 目錄。"""
    links: dict[str, list[Path]] = {}
    for f in sorted(WIKI_DIR.rglob("*.md")):
        try:
            raw = f.read_text(encoding="utf-8")
        except Exception:
            continue
        for m in URL_RE.finditer(raw):
            url = m.group(0).rstrip('.,;:!?')
            links.setdefault(url, []).append(f)
    return links


def check_one(url: str) -> tuple[str, int | None, str]:
    """回傳 (url, status_code or None, note)。"""
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return url, resp.status, ""
    except urllib.error.HTTPError as e:
        if e.code in ANTI_BOT_CODES:
            return url, e.code, "可能反爬，人工確認"
        if 400 <= e.code < 600:
            # HEAD 失敗時 fallback 用 GET 再試一次（有些伺服器不支援 HEAD）
            try:
                req_get = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req_get, timeout=TIMEOUT) as resp:
                    return url, resp.status, ""
            except urllib.error.HTTPError as e2:
                if e2.code in ANTI_BOT_CODES:
                    return url, e2.code, "可能反爬，人工確認"
                return url, e2.code, ""
            except Exception as e2:
                return url, None, f"GET fallback 失敗：{e2}"
        return url, e.code, ""
    except urllib.error.URLError as e:
        return _retry_slow(url, f"連線失敗：{e.reason}")
    except TimeoutError:
        return _retry_slow(url, "逾時")
    except Exception as e:
        return url, None, f"錯誤：{e}"


def _retry_slow(url: str, first_note: str) -> tuple[str, int | None, str]:
    """逾時／連線失敗時用較長逾時 + GET 再試一次。

    很多新聞站對 HEAD 或對陌生 UA 反應慢，10 秒一刀切會製造大量假死鏈。
    重試仍失敗才回 None，並由呼叫端歸入「無法判定」而非「死鏈」。
    """
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=RETRY_TIMEOUT) as resp:
            return url, resp.status, "重試後正常"
    except urllib.error.HTTPError as e:
        note = "可能反爬，人工確認" if e.code in ANTI_BOT_CODES else "重試後仍失敗"
        return url, e.code, note
    except Exception:
        return url, None, first_note


def _load_prev(report_path):
    """讀既有報告供分層掃描比對。讀不到就回 None，呼叫端退回全量。"""
    if not report_path:
        return None
    p = Path(report_path)
    if not p.is_absolute():
        p = ROOT / p
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def _write_report(path_str, links, urls, dead, anti_bot, unverified, ok_count,
                  as_of, ok_urls=None, incremental=False):
    """輸出 JSON 報告。消費端是 `/wiki-lint` 指標三——它讀這個檔而不自己連網，
    因此雲端 lint（egress 封鎖）也能完成該步驟。"""
    checked_at = as_of or date.today().isoformat()
    payload = {
        "checked_at": checked_at,
        "total_unique_links": len(links),
        "mode": "incremental" if incremental else "full",
        "checked": len(urls),
        "ok_urls": sorted(ok_urls or []),
        "ok": ok_count,
        "dead": [
            {
                "url": url,
                "status": status,
                "note": note,
                "pages": sorted(str(p.relative_to(ROOT)).replace("\\", "/") for p in links[url]),
            }
            for url, status, note in dead
        ],
        "unverified": [
            {
                "url": url,
                "status": status,
                "note": note,
                "pages": sorted(str(p.relative_to(ROOT)).replace(chr(92), "/") for p in links[url]),
            }
            for url, status, note in unverified
        ],
        "anti_bot": [
            {
                "url": url,
                "status": status,
                "pages": sorted(str(p.relative_to(ROOT)).replace("\\", "/") for p in links[url]),
            }
            for url, status, note in anti_bot
        ],
    }
    out = Path(path_str)
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="掃描 wiki/**/*.md 外部連結，找出疑似死鏈")
    parser.add_argument("--limit", type=int, default=None, help="只驗證前 N 條連結（用於快速驗證邏輯）")
    parser.add_argument(
        "--report",
        type=str,
        default=None,
        metavar="PATH",
        help="額外輸出機器可讀的 JSON 報告（供 GH Actions commit 回 repo、由 /wiki-lint 讀取）",
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        help="分層掃描：只驗『新連結 + 上次非 OK 者』，其餘沿用上次結果（需 --report 指向既有報告）",
    )
    parser.add_argument(
        "--as-of",
        type=str,
        default=None,
        metavar="YYYY-MM-DD",
        help="報告的檢查日期，預設為今日（測試用，避免報告內容隨時鐘變動）",
    )
    args = parser.parse_args()

    links = collect_links()
    urls = list(links.keys())

    # ── 分層掃描 ────────────────────────────────────────────────────────
    # 全量 795 條裡約 680 條上週正常、這週幾乎必然還正常；真正需要每週看的是
    # 新連結與上次非 OK 者。分層後每週約 120 條（省 ~85% 請求），全量仍每月跑
    # 一次補回「上週好、這週壞」的漏網。
    # 代價寫清楚：非 OK 之外的連結，其失效最多晚一個月被發現——對 wiki 引用的
    # 新聞連結，這個延遲可接受；對死鏈標註的正確性沒有影響（標註只認 dead 桶）。
    carried: dict[str, dict] = {}
    if args.incremental:
        prev = _load_prev(args.report)
        if prev is None:
            print("⚠️ --incremental 需要既有報告，找不到則退回全量掃描")
        else:
            suspect = {e["url"] for k in ("dead", "anti_bot", "unverified") for e in prev.get(k, [])}
            prev_ok = {e for e in prev.get("ok_urls", [])}
            todo = [u for u in urls if u in suspect or u not in prev_ok]
            carried = {"count": len(urls) - len(todo), "since": prev.get("checked_at")}
            print(f"分層掃描：本次驗 {len(todo)} 條（新連結 + 上次非 OK），"
                  f"沿用上次結果 {carried['count']} 條（上次檢查日 {carried['since']}）")
            urls = todo

    if args.limit:
        urls = urls[: args.limit]

    print(f"共發現 {len(links)} 個唯一外部連結（wiki/，排除 news/），本次檢查 {len(urls)} 條")
    print("-" * 60)

    dead: list[tuple[str, int | None, str]] = []
    anti_bot: list[tuple[str, int | None, str]] = []
    unverified: list[tuple[str, int | None, str]] = []
    ok_count = 0

    for i, url in enumerate(urls, 1):
        _, status, note = check_one(url)
        if status in ANTI_BOT_CODES:
            anti_bot.append((url, status, note or "可能反爬，人工確認"))
            print(f"[{i}/{len(urls)}] ?? {status} {url}  (擋機器人)")
        elif status in DEAD_CODES:
            dead.append((url, status, note))
            print(f"[{i}/{len(urls)}] XX {status} {url}  {note}")
        elif status is None or status >= 400:
            # 逾時、連線失敗、5xx：證據不足以判死。歸「無法判定」，不驅動頁面標註。
            unverified.append((url, status, note))
            print(f"[{i}/{len(urls)}] -- {status or '無回應'} {url}  {note}")
        else:
            ok_count += 1
            print(f"[{i}/{len(urls)}] OK {status} {url}")

    ok_urls = [u for u in urls if u not in {x[0] for x in dead + anti_bot + unverified}]

    # 分層模式：把「本次沒掃的連結」用上次的結果補回來。
    # 這一步不可省——少了它，報告只涵蓋本次掃描的子集，於是 (a) 下週會把沒掃的
    # 全當成新連結（分層失效），(b) lint 讀到縮水的死鏈清單，把仍失效的連結
    # 當成已修好。分層是省請求，不是省結論。
    if carried:
        prev = _load_prev(args.report) or {}
        scanned = set(urls)
        for bucket, lst in (("dead", dead), ("anti_bot", anti_bot), ("unverified", unverified)):
            for e in prev.get(bucket, []):
                if e["url"] not in scanned and e["url"] in links:
                    lst.append((e["url"], e.get("status"), e.get("note", "沿用上次結果")))
        for u in prev.get("ok_urls", []):
            if u not in scanned and u in links:
                ok_urls.append(u)
                ok_count += 1

    # 完整性自檢：分層之後，四個桶的總和必須仍等於全部唯一連結數。
    # 這是分層唯一會出錯的地方（沿用邏輯漏掉某些 url），而錯了不會有任何症狀
    # ——lint 只會看到一份「比較短的」死鏈清單，把仍失效的連結當成已修好。
    # 手動驗過一次不夠，讓它每次自己驗。
    _total = len(ok_urls) + len(dead) + len(anti_bot) + len(unverified)
    if carried and _total != len(links):
        print(f"❌ 分層合併後清單不完整：{_total} / {len(links)} 條——"
              f"缺 {len(links) - _total} 條。報告不可信，請改跑全量（不加 --incremental）。")
        return 2

    print("-" * 60)
    print(
        f"正常：{ok_count}　確認死鏈（404/410）：{len(dead)}　"
        f"擋機器人（401/403/429）：{len(anti_bot)}　無法判定（逾時/5xx）：{len(unverified)}"
    )

    if dead:
        print(_SEP + "=== 確認死鏈清單（404/410，僅這些驅動頁面標註）===")
        for url, status, note in dead:
            pages = ", ".join(str(p.relative_to(ROOT)) for p in links[url])
            print(f"- {url}  [狀態: {status}]  引用頁面: {pages}")

    if anti_bot:
        print(_SEP + "=== 擋機器人（401/403/429，不算死鏈、不標註）===")
        for url, status, note in anti_bot:
            pages = ", ".join(str(p.relative_to(ROOT)) for p in links[url])
            print(f"- {url}  [狀態: {status}]  引用頁面: {pages}")

    if unverified:
        print(_SEP + "=== 無法判定（逾時/連線失敗/5xx，已重試一次仍失敗）===")
        print("  單次逾時是很弱的證據，不足以判死；連續多週落在此桶才值得人工看。")
        for url, status, note in unverified:
            pages = ", ".join(str(p.relative_to(ROOT)) for p in links[url])
            print(f"- {url}  [狀態: {status or '無回應'}]  {note}  引用頁面: {pages}")

    if args.report:
        _write_report(args.report, links, urls, dead, anti_bot, unverified, ok_count,
                      args.as_of, ok_urls, bool(carried))
        print(f"\n報告已寫入：{args.report}")

    # exit code 只代表「有沒有死鏈」，供本機使用者判讀。
    # GH Actions 那條線刻意不看它（見 .github/workflows/weekly-linkcheck.yml）：
    # 有死鏈是預期中的常態發現，不是 workflow 失敗——若讓它紅燈，紅燈會變成
    # 背景雜訊，真正的抓取失敗就沒人看得出來。
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
