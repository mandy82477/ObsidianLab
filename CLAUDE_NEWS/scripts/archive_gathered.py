#!/usr/bin/env python3
"""archive_gathered.py — 把 src/gathered_items.json 存一份按日期分檔的副本。

為什麼需要：`gathered_items.json` 沒有按日分檔，每次抓料都直接覆寫它。若某天的
日報沒產出（雲端 routine 失敗、中止、push 失敗），那天「已經抓到手」的原料會在
隔天抓料時被蓋掉；之後想補跑只能回頭重抓，但來源多是近期視窗的 RSS/API，幾天前
的內容早已滾出視窗——那天的新聞就永久漏失。

有了副本，補跑可以直接 replay 當天的真實原料，產出與原本該有的日報一致
（見 `.claude/commands/news-pipeline-steps.md` 的「補跑（backfill）注意事項」）。

檔名取 `gathered_items.json` 內的 `date` 欄位，不取系統當下日期——這樣 backfill
產生的原料也會歸檔到它真正對應的那一天。

保留天數與 emitted-cache 的 TTL 一致（14 天）。

用法：
    python scripts/archive_gathered.py            # 歸檔 + 清理過期
    python scripts/archive_gathered.py --prune-only
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GATHERED = REPO_ROOT / "src" / "gathered_items.json"
ARCHIVE_DIR = REPO_ROOT / "src" / "gathered_archive"
RETENTION_DAYS = 14


def prune(archive_dir: Path = ARCHIVE_DIR, today: date | None = None) -> list[str]:
    """刪除超過保留天數的副本，回傳被刪檔名。以檔名日期判斷，不看 mtime
    （git checkout 會把 mtime 全部重設為 checkout 當下，mtime 在 CI 不可信）。"""
    today = today or date.today()
    cutoff = today - timedelta(days=RETENTION_DAYS)
    removed = []
    if not archive_dir.exists():
        return removed
    for f in sorted(archive_dir.glob("*.json")):
        try:
            stamp = date.fromisoformat(f.stem)
        except ValueError:
            continue  # 檔名不是日期就別亂刪
        if stamp < cutoff:
            f.unlink()
            removed.append(f.name)
    return removed


def archive(gathered: Path = GATHERED, archive_dir: Path = ARCHIVE_DIR) -> Path | None:
    if not gathered.exists():
        print(f"跳過歸檔：{gathered} 不存在")
        return None
    try:
        stamp = json.loads(gathered.read_text(encoding="utf-8"))["date"]
        date.fromisoformat(stamp)  # 驗證格式
    except Exception as e:
        print(f"跳過歸檔：無法從 {gathered.name} 讀出合法的 date 欄位（{e}）")
        return None
    archive_dir.mkdir(parents=True, exist_ok=True)
    target = archive_dir / f"{stamp}.json"
    shutil.copyfile(gathered, target)
    return target


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--prune-only", action="store_true")
    args = p.parse_args()

    if not args.prune_only:
        target = archive()
        if target:
            print(f"已歸檔：{target.relative_to(REPO_ROOT)}")
    removed = prune()
    if removed:
        print(f"已清理過期副本（保留 {RETENTION_DAYS} 天）：{', '.join(removed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
