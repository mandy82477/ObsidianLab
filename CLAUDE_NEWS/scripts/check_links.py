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
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_DIR = ROOT / "wiki"

# 停在空白、markdown/引號收尾字元、以及全形標點與 CJK 字元（URL 後面緊接中文說明時常見，如「...id=123（HN」）
URL_RE = re.compile(r'https?://[^\s\)\]>"\'`（）「」『』、，。《》〈〉一-鿿]+')

TIMEOUT = 10
USER_AGENT = "Mozilla/5.0 (compatible; ClaudeNewsLinkChecker/1.0; +https://github.com/)"

# 反爬蟲常見狀態碼：不算死鏈，只標記「可能反爬，人工確認」
ANTI_BOT_CODES = {403, 429}


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
        return url, None, f"連線失敗：{e.reason}"
    except TimeoutError:
        return url, None, "逾時"
    except Exception as e:
        return url, None, f"錯誤：{e}"


def main():
    parser = argparse.ArgumentParser(description="掃描 wiki/**/*.md 外部連結，找出疑似死鏈")
    parser.add_argument("--limit", type=int, default=None, help="只驗證前 N 條連結（用於快速驗證邏輯）")
    args = parser.parse_args()

    links = collect_links()
    urls = list(links.keys())
    if args.limit:
        urls = urls[: args.limit]

    print(f"共發現 {len(links)} 個唯一外部連結（wiki/，排除 news/），本次檢查 {len(urls)} 條")
    print("-" * 60)

    dead: list[tuple[str, int | None, str]] = []
    anti_bot: list[tuple[str, int | None, str]] = []
    ok_count = 0

    for i, url in enumerate(urls, 1):
        _, status, note = check_one(url)
        if note == "可能反爬，人工確認":
            anti_bot.append((url, status, note))
            print(f"[{i}/{len(urls)}] ?? {status} {url}  ({note})")
        elif status is None or status >= 400:
            dead.append((url, status, note))
            print(f"[{i}/{len(urls)}] XX {status or '???'} {url}  {note}")
        else:
            ok_count += 1
            print(f"[{i}/{len(urls)}] OK {status} {url}")

    print("-" * 60)
    print(f"正常：{ok_count}　疑似死鏈：{len(dead)}　可能反爬（人工確認）：{len(anti_bot)}")

    if dead:
        print("\n=== 疑似死鏈清單 ===")
        for url, status, note in dead:
            pages = ", ".join(str(p.relative_to(ROOT)) for p in links[url])
            print(f"- {url}  [狀態: {status or '逾時/連線失敗'}]  引用頁面: {pages}")

    if anti_bot:
        print("\n=== 可能反爬（人工確認，不算死鏈）===")
        for url, status, note in anti_bot:
            pages = ", ".join(str(p.relative_to(ROOT)) for p in links[url])
            print(f"- {url}  [狀態: {status}]  引用頁面: {pages}")

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
