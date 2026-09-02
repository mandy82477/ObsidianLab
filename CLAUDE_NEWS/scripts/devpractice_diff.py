# -*- coding: utf-8 -*-
"""devpractice 記者的沉澱訊號源：上次看過之後，wiki 新增了什麼。

設計依據（2026-09-02 使用者裁決）：
- devpractice 不靠其他記者標 tag（跨記者耦合＝已知失效模式：主線 tag 規則明寫
  「漏填等於該節點不存在」）。他自己在各記者沉澱完之後 git diff 撿料，
  「什麼算 coding 相關」的判斷權單一歸他。
- 基準線不是「今天的 commit」——補跑、雲端／本機交錯、漏一天都會漏看。
  改記狀態檔（上次看到的 commit sha），每次 diff <上次sha>..HEAD，看完更新 sha。
  漏跑三天，下次自動補齊三天的量。
- 狀態檔與候選帳本都在 data/ 且必須隨 pipeline push——雲端與本機共用同一條基準線，
  不 commit 的話兩邊各自為政，基準線就斷了。

用法：
    python scripts/devpractice_diff.py show   # 印出上次以來 wiki/ 的新增行（依檔案分組）
    python scripts/devpractice_diff.py mark   # 把基準線推進到目前 HEAD

失敗模式處理：
- 狀態檔缺失／sha 已不在歷史中（rebase、force push）→ 退回「48 小時前的 commit」
  當基準線（用 rev-list --before，不用 reflog——雲端 fresh clone 的 reflog 是空的）。
- diff 為空 → 印「無新增」，exit 0（無料是正常結果，不是錯誤）。
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATE = ROOT / "data" / "devpractice_state.json"
# log.md 是編輯部日誌、index.md 是路由層——都不是新聞內容，撿了只會混入雜訊
EXCLUDE = ("wiki/log.md", "wiki/index.md")
MAX_LINES_PER_FILE = 120  # 單檔新增行上限，防單頁大改版灌爆輸出


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )


def _fallback_sha():
    r = _git("rev-list", "-1", "--before=48 hours ago", "HEAD")
    return r.stdout.strip() or None


def _base_sha():
    """讀狀態檔的基準 sha；缺失或已不在歷史中則退回 48 小時前。"""
    sha = None
    if STATE.exists():
        try:
            sha = json.loads(STATE.read_text(encoding="utf-8")).get("last_sha")
        except (json.JSONDecodeError, OSError):
            sha = None
    if sha and _git("cat-file", "-e", f"{sha}^{{commit}}").returncode == 0:
        return sha, "state"
    fb = _fallback_sha()
    return fb, "fallback-48h"


def show():
    sha, origin = _base_sha()
    if not sha:
        print("⚠️ 找不到基準 commit（repo 太新？），無法 diff")
        return 1
    head = _git("rev-parse", "HEAD").stdout.strip()
    print(f"基準線：{sha[:10]}（{origin}）→ HEAD {head[:10]}")
    if sha == head:
        print("無新增（基準線已是 HEAD）")
        return 0
    r = _git("diff", f"{sha}..HEAD", "--unified=0", "--", "wiki/")
    if r.returncode != 0:
        print(f"⚠️ git diff 失敗：{r.stderr.strip()}")
        return 1
    current, buf, total = None, [], 0

    def flush():
        nonlocal buf
        if current and buf:
            shown = buf[:MAX_LINES_PER_FILE]
            print(f"\n## {current}（新增 {len(buf)} 行"
                  + (f"，只列前 {MAX_LINES_PER_FILE}" if len(buf) > MAX_LINES_PER_FILE else "")
                  + "）")
            for line in shown:
                print(line)
        buf = []

    for line in r.stdout.splitlines():
        if line.startswith("+++ b/"):
            flush()
            path = line[6:]
            # repo root 在 CLAUDE_NEWS 上一層，diff 標頭路徑帶 CLAUDE_NEWS/ 前綴——用 endswith 比對
            current = None if any(path.endswith(e) for e in EXCLUDE) else path
        elif line.startswith("+") and not line.startswith("+++") and current:
            text = line[1:].rstrip()
            if text.strip():
                buf.append(text)
                total += 1
    flush()
    if total == 0:
        print("無新增（wiki/ 內容無變化）")
    else:
        print(f"\n合計新增 {total} 行（不含 log.md／index.md）")
    return 0


def mark():
    head = _git("rev-parse", "HEAD").stdout.strip()
    if not head:
        print("⚠️ 取不到 HEAD")
        return 1
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps({
        "last_sha": head,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"基準線已推進：{head[:10]}")
    return 0


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    cmd = sys.argv[1] if len(sys.argv) > 1 else "show"
    if cmd == "show":
        return show()
    if cmd == "mark":
        return mark()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
