#!/usr/bin/env python3
"""
cloud_egress_check.py — 探測本執行環境連不連得到某一組外部網域。

## 為什麼需要它

雲端環境的網路存取分四級（官方文件 `cloud-environments.md#network-access`）：
None／Trusted（預設，約 70 個網域白名單）／Custom（使用者自填網域）／Full。
本專案的雲端環境目前是 **Trusted**，所以 Reddit／HN／Google News／官方文件站
一律回 403 或 `EGRESS_BLOCKED`——`/wiki-lint` 的 5b／5c／5e／5h／5m 因此曾被寫死
「雲端一律跳過」。

**寫死跳過的條文永遠不會自己好起來**：使用者哪天把環境改成 Custom 並加入網域，
規則檔還是寫著跳過，那幾步在雲端就永遠餓死。所以改成**探測式**——各步先問這支
腳本「我需要的網域通不通」，通就照做，不通才跳過留待辦。環境改前改後都正確。

## 機械契約（lint 步驟會 grep 這一行，改動要同步 .claude/commands/wiki-lint.md）

每組印**恰好一行**摘要，形狀固定：

    EGRESS: <group> OK|PARTIAL|BLOCKED (<通>/<總> 個網域)

- `OK`      — 該組全部網域可達
- `PARTIAL` — 部分可達（lint 一律當作不可用：半套查證比不查更危險）
- `BLOCKED` — 全部不可達

摘要行之前逐一印每個網域的 `OK` ／ `BLOCKED（原因）` 明細（供人判讀，非契約）。

## 退出碼

    0  全部探測到的網域都通
    1  部分通（PARTIAL）
    2  全部不通（BLOCKED）

多組同時探測時取**最壞**的那一組決定退出碼（全 OK → 0；有任一 BLOCKED 且有任一
OK → 1；全 BLOCKED → 2）。

## 用法

    python scripts/cloud_egress_check.py                        # 全部組
    python scripts/cloud_egress_check.py --group official,github
    python scripts/cloud_egress_check.py --group leaderboard --timeout 5

純標準庫（urllib），無第三方依賴——它要能在最貧瘠的雲端映像裡跑起來。
"""
import argparse
import socket
import ssl
import sys
import urllib.error
import urllib.request

# ---------------------------------------------------------------------------
# 網域分組：依 lint 步驟分，讓各步只問自己需要的
# ---------------------------------------------------------------------------
GROUPS: dict[str, list[str]] = {
    # 5c Lane B（官方一手來源查證）、5e（官方計價頁）、5m 的官方文件面
    "official": [
        "platform.claude.com",
        "support.claude.com",
        "docs.claude.com",
        "www.anthropic.com",
    ],
    # 5m issue 狀態（gh CLI 走 api.github.com）、feature-radar 升版階梯的 changelog 抓取
    "github": [
        "api.github.com",
        "raw.githubusercontent.com",
    ],
    # 5b 跨家任務榜單週更。清單取自 wiki/topics/model-task-leaderboard.md
    # 「涵蓋榜單」表各列的連結網域（2026-09-12 盤點，18 列 / 12 個相異網域）。
    # 該表增減榜單時同步本清單。
    "leaderboard": [
        "www.swebench.com",
        "aider.chat",
        "lmarena.ai",
        "arena.ai",
        "artificialanalysis.ai",
        "www.tbench.ai",
        "llm-stats.com",
        "huggingface.co",
        "eqbench.com",
        "metr.org",
        "github.com",
        "openrouter.ai",
    ],
    # 5h 投資訊號回顧環。**刻意為空**：該步的股價方向用 **WebSearch**
    # （`.claude/reporter-rules/wiki-ingest-market-lint.md` 執行步驟第 3 步逐字寫
    # 「WebSearch 查該標的…」），而 WebSearch 由 Anthropic 端執行、不經沙盒 egress，
    # 因此不受本腳本量測的限制；催化劑那一半本來就純庫內。空組一律回 OK。
    # 若日後該步改用 WebFetch 直抓行情站，把那些網域填進這裡。
    "market": [],
}

DEFAULT_TIMEOUT = 8
_UA = "cloud-egress-check/1.0 (+CLAUDE_NEWS lint probe)"


def probe(domain: str, timeout: int = DEFAULT_TIMEOUT) -> tuple[bool, str]:
    """回傳 (可達?, 原因)。

    先 HEAD，遇 405/501（不收 HEAD 的站）退回 GET。判定採「**連得上就算通**」：
    任何 HTTP 狀態碼（含 403/404）都代表封包出得去、回得來——本腳本量的是 egress，
    不是那一頁存不存在。只有連線層失敗（DNS、TCP、TLS、逾時、proxy 擋下）才算不通。
    """
    url = f"https://{domain}/"
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": _UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return True, f"HTTP {resp.status}"
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (405, 501):
                continue  # 不收 HEAD，改試 GET
            return True, f"HTTP {e.code}"
        except urllib.error.URLError as e:
            return False, f"{type(e.reason).__name__ if not isinstance(e.reason, str) else 'URLError'}: {e.reason}"
        except (socket.timeout, TimeoutError):
            return False, f"timeout >{timeout}s"
        except ssl.SSLError as e:
            return False, f"SSLError: {e}"
        except OSError as e:
            return False, f"{type(e).__name__}: {e}"
    return False, "unreachable"


def check_group(name: str, timeout: int = DEFAULT_TIMEOUT, out=None) -> str:
    """探測一組，印明細＋契約摘要行，回傳 'OK' / 'PARTIAL' / 'BLOCKED'。

    `out` 預設在**呼叫時**才取 sys.stdout（不寫成參數預設值）——寫成預設值會在
    import 時綁死，contextlib.redirect_stdout 就攔不到，測試看到的是空字串。
    """
    out = sys.stdout if out is None else out
    domains = GROUPS[name]
    if not domains:
        print(f"[{name}] 本組無需探測的網域（見腳本內註解）", file=out)
        print(f"EGRESS: {name} OK (0/0 個網域)", file=out)
        return "OK"

    ok = 0
    for d in domains:
        reachable, reason = probe(d, timeout)
        if reachable:
            ok += 1
            print(f"[{name}] {d}: OK（{reason}）", file=out)
        else:
            print(f"[{name}] {d}: BLOCKED（{reason}）", file=out)

    if ok == len(domains):
        status = "OK"
    elif ok == 0:
        status = "BLOCKED"
    else:
        status = "PARTIAL"
    print(f"EGRESS: {name} {status} ({ok}/{len(domains)} 個網域)", file=out)
    return status


def exit_code_for(statuses: list[str]) -> int:
    if not statuses or all(s == "OK" for s in statuses):
        return 0
    if all(s == "BLOCKED" for s in statuses):
        return 2
    return 1


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="探測本環境連不連得到 lint 各步需要的外部網域（見檔頭機械契約）",
    )
    p.add_argument(
        "--group",
        help="逗號分隔的組名（" + "／".join(GROUPS) + "）；省略＝全部",
    )
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help=f"單一網域逾時秒數（預設 {DEFAULT_TIMEOUT}）")
    args = p.parse_args(argv)

    if args.group:
        names = [g.strip() for g in args.group.split(",") if g.strip()]
        unknown = [g for g in names if g not in GROUPS]
        if unknown:
            print(f"未知組名：{', '.join(unknown)}（可用：{', '.join(GROUPS)}）", file=sys.stderr)
            return 2
    else:
        names = list(GROUPS)

    statuses = [check_group(n, args.timeout) for n in names]
    return exit_code_for(statuses)


if __name__ == "__main__":
    sys.exit(main())
