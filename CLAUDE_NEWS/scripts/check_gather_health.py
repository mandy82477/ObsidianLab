#!/usr/bin/env python3
"""check_gather_health.py — 生日報前的原料健康檢查。

原本的新鮮度防線只問兩件事：資料是不是目標日期、筆數是不是 > 0。這擋得住
「沒抓到」，擋不住「抓到但殘缺」——10 個來源掛 9 個、只剩 Google News 回 3 則，
照樣會生出一份看起來正常的日報，然後被六記者沉澱進 wiki 變成長期污染。

本檢查回答：這批原料撐不撐得起一份日報？

門檻（2026-07-25 設定，依 07-10~07-24 實績校準：來源恆為 10 個、每日條數
34~71 則、來源失敗數常態為 0）：

  - 失敗來源數 >= FAIL_SOURCES → 中止，不生日報
  - 條數 < FAIL_ITEMS → 中止，不生日報
  - 失敗來源數 >= WARN_SOURCES → 照生，但要求日報與 log 標警示

「條數少」與「來源掛掉」分開判斷的理由：新聞本來就有淡日（實績最低 34 則），
條數低不必然代表管線壞了；但來源大量失敗一定是管線或網路出問題，那天的日報
必然是偏食的，寧可沒有也不要一份有系統性偏差的。

用法：
    python scripts/check_gather_health.py [--file src/gathered_items.json]

退出碼：
    0 = 健康（或僅警示，警示內容印在輸出）
    2 = 不健康，呼叫端必須中止並照該步驟的中止程序處理
    3 = 檔案讀不到／格式不對（視同不健康）
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILE = REPO_ROOT / "src" / "gathered_items.json"

FAIL_SOURCES = 4   # 10 個來源掛掉 4 個（四成）→ 那天的日報必然偏食
WARN_SOURCES = 2
FAIL_ITEMS = 10    # 實績最低 34 則；低到 10 以下已非淡日而是管線異常

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def evaluate(data: dict) -> tuple[int, list[str]]:
    """回傳 (exit_code, 訊息列)。純函式，供測試直接呼叫。"""
    msgs: list[str] = []
    status = data.get("source_status") or {}
    items = data.get("items") or []

    if isinstance(status, dict):
        failed = [name for name, s in status.items() if not (s or {}).get("ok", False)]
        total = len(status)
    else:  # 陣列格式（防呆）
        failed = [s.get("name", "?") for s in status if not s.get("ok", False)]
        total = len(status)

    msgs.append(f"來源：{total - len(failed)}/{total} 正常，條數：{len(items)}")

    code = 0
    if len(failed) >= FAIL_SOURCES:
        msgs.append(f"❌ 失敗來源 {len(failed)} 個（門檻 {FAIL_SOURCES}）：{', '.join(failed)}")
        msgs.append("   → 這批原料有系統性偏差，中止優於生出一份偏食的日報")
        code = 2
    elif len(failed) >= WARN_SOURCES:
        msgs.append(f"⚠️ 失敗來源 {len(failed)} 個：{', '.join(failed)}——照生，但日報與 log 須標警示")

    if len(items) < FAIL_ITEMS:
        msgs.append(f"❌ 條數 {len(items)} 低於門檻 {FAIL_ITEMS}，判定為管線異常而非淡日")
        code = 2

    if code == 0 and len(failed) < WARN_SOURCES:
        msgs.append("✅ 原料健康")
    return code, msgs


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--file", default=str(DEFAULT_FILE))
    args = p.parse_args()

    path = Path(args.file)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"❌ 無法讀取 {path}：{e}")
        return 3

    code, msgs = evaluate(data)
    for m in msgs:
        print(m)
    return code


if __name__ == "__main__":
    sys.exit(main())
