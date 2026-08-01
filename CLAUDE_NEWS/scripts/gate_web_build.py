#!/usr/bin/env python3
"""gate_web_build.py — 決定「這次測試失敗該不該擋掉 web build」。

## 為什麼需要這層

原本的 gate 是「`run_tests.py` 整包過才建 web」。2026-07-31 雲端日更因 3 個
`ModuleNotFoundError: No module named 'feedparser_sgmllib'` 判定測試失敗，
依規則跳過 web build——但那 3 個案例是**抓料端的環境依賴**，跟 `build_web.py`
的輸入（`news/*.md`、`wiki/*.md`，皆已正常產出並 commit）毫無關係。結果是一個
無關的依賴缺口讓網站整天停在前一天，日報和 wiki 明明都好好的。

耦合太緊的 gate 會用「正確性」的名義製造「可用性」的損失。所以改成：

  - 失敗案例**全部**落在 `docs/known-test-gaps.json` 已登記的缺口內 → 放行，
    但把放行理由印出來、寫進 log，讓它無法悄悄變常態
  - 出現**任何一個沒登記的失敗** → 照舊擋下（這才是 gate 真正該擋的東西）
  - 測試失敗但解析不出任何案例名（例如 `check_rules.py` / `check_arch_docs.py`
    這類規則一致性檢查失敗）→ **擋下**。規則檔不一致會直接影響產出內容，
    不屬於「與 web build 無關」的類別，保守處理

## 允許清單的紀律

`docs/known-test-gaps.json` 每一筆都必須指回 `docs/workaround-register.md` 的
對應列，並填 `review_date`。逾複查日的項目**仍然放行**（擋住網站不是懲罰逾期的
正確手段），但會印出 `⚠️ 逾複查日` 並計入回傳訊息，由 `open_loops.py` 那條路
去追。缺口修好後從 json 移除即可，不需要動這支腳本。

用法：
    python scripts/gate_web_build.py          # exit 0 = 可以建 web
    python scripts/gate_web_build.py --json    # 附機器可讀結果

exit code：
    0 = 放行（全綠，或失敗全屬已登記缺口）
    1 = 擋下（有未登記的失敗）
"""
from __future__ import annotations

import argparse
import io
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _use_utf8_stdout() -> None:
    """只在 `__main__` 路徑呼叫——模組層級換 `sys.stdout` 會在本檔被測試 import 時
    連帶關掉呼叫端的輸出流（理由與實例見 `daily_health_check.py` 同名函式）。"""
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
RUN_TESTS = REPO_ROOT / "scripts" / "run_tests.py"
GAPS_FILE = REPO_ROOT / "docs" / "known-test-gaps.json"

# run_tests.py 的失敗清單格式：「  FAIL: test_x (pkg.Class)」／「  ERROR: ...」
FAILURE_LINE = re.compile(r"^\s*(?:FAIL|ERROR):\s*(.+?)\s*$", re.MULTILINE)


def load_gaps(path: Path = GAPS_FILE) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"⚠️ {path.name} 解析失敗（{e}）——視同無允許清單，一律擋下")
        return []
    return [g for g in data.get("gaps", []) if isinstance(g, dict)]


def parse_failures(output: str) -> list[str]:
    """從 run_tests.py 輸出取出失敗案例名稱。"""
    return [m.strip() for m in FAILURE_LINE.findall(output)]


def match_gap(test_id: str, output: str, gaps: list[dict]) -> dict | None:
    """一個失敗案例要被放行，必須同時命中某筆缺口的 test 樣式與 error 樣式。

    兩個條件都要的理由：只比對案例名稱的話，同一個測試日後因**真的壞了**而失敗
    也會被誤放行；錯誤訊息才是「這是不是同一個已知缺口」的判準。
    """
    for gap in gaps:
        test_pat, err_pat = gap.get("test"), gap.get("error")
        if not test_pat or not err_pat:
            continue
        try:
            if re.search(test_pat, test_id) and re.search(err_pat, output):
                return gap
        except re.error as e:
            print(f"⚠️ 缺口 {gap.get('id', '?')} 的樣式無效（{e}），略過此筆")
    return None


def evaluate(output: str, exit_code: int, gaps: list[dict], today: date | None = None) -> dict:
    """純函式：吃 run_tests 的輸出與 exit code，吐放行決定。方便單元測試。"""
    today = today or date.today()
    if exit_code == 0:
        return {"allow": True, "reason": "tests_green", "failures": [], "matched": [], "unmatched": [], "overdue": []}

    failures = parse_failures(output)
    if not failures:
        # 例如 check_rules.py / check_arch_docs.py 失敗：不屬於「與 web 無關」的類別
        return {"allow": False, "reason": "no_parsable_failures", "failures": [], "matched": [], "unmatched": [], "overdue": []}

    matched, unmatched, overdue = [], [], []
    for test_id in failures:
        gap = match_gap(test_id, output, gaps)
        if gap is None:
            unmatched.append(test_id)
            continue
        matched.append({"test": test_id, "gap": gap.get("id", "?"), "register_row": gap.get("register_row", "")})
        rd = gap.get("review_date")
        if rd and rd < today.isoformat() and gap.get("id") not in overdue:
            overdue.append(gap.get("id"))

    allow = not unmatched
    return {
        "allow": allow,
        "reason": "all_failures_known" if allow else "unknown_failure",
        "failures": failures,
        "matched": matched,
        "unmatched": unmatched,
        "overdue": overdue,
    }


def render(result: dict) -> str:
    """產生一行摘要，供 pipeline 直接抄進 task_scheduler.log。"""
    if result["reason"] == "tests_green":
        return "測試全綠 - web build 放行"
    if result["reason"] == "no_parsable_failures":
        return "測試失敗且非單元測試案例（規則一致性檢查等）- web build 擋下"
    if result["allow"]:
        ids = ", ".join(sorted({m["gap"] for m in result["matched"]}))
        extra = f"；⚠️ 逾複查日：{', '.join(result['overdue'])}" if result["overdue"] else ""
        return f"測試失敗 {len(result['failures'])} 案，全屬已登記缺口（{ids}）- web build 放行{extra}"
    return f"測試失敗含未登記案例（{', '.join(result['unmatched'])}）- web build 擋下"


def main() -> int:
    _use_utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="額外輸出機器可讀的 JSON 結果")
    args = ap.parse_args()

    print("=== web build gate：先跑測試套件 ===")
    proc = subprocess.run(
        [sys.executable, str(RUN_TESTS)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    output = (proc.stdout or "") + (proc.stderr or "")

    result = evaluate(output, proc.returncode, load_gaps())

    if proc.returncode != 0:
        # 失敗時把原始輸出印出來，不要讓 gate 變成遮蔽測試結果的黑盒
        print(output.rstrip())

    print("\n=== 判定 ===")
    for m in result["matched"]:
        print(f"  ✅ 已登記缺口放行：{m['test']} → {m['gap']}（{m['register_row']}）")
    for u in result["unmatched"]:
        print(f"  ⛔ 未登記失敗：{u}")
    for o in result["overdue"]:
        print(f"  ⚠️ 缺口 {o} 已逾複查日——仍放行，但請回 docs/workaround-register.md 收尾")

    summary = render(result)
    print(f"\n{summary}")
    if args.json:
        print("JSON: " + json.dumps({**result, "summary": summary}, ensure_ascii=False))
    return 0 if result["allow"] else 1


if __name__ == "__main__":
    sys.exit(main())
