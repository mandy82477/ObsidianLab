# -*- coding: utf-8 -*-
"""append-only 檔案的 rebase 衝突自解：以 union 保留兩側新增（2026-09-03）。

為什麼有這支：2026-09-02 雲端 17:00 UTC 班完整跑完日報＋wiki＋web，push 時撞上本機
同時間的 commit——衝突檔只有 wiki/log.md，而它是 append-only：兩側都只是在檔尾各自加段落。
依當時規則（唯一可自解的是 emitted_items.json）該班放棄整輪，22:00 班重做一遍。
append-append 衝突可以機械聯集，不需要人判斷；讓一個沒有語意衝突的衝突逼整班重跑，
是把「謹慎」用錯地方。

只解白名單內的 append-only 檔（APPEND_ONLY）；白名單外的衝突一律不碰、exit 1，
交回人類——那才是需要判斷的。解法用 `git merge-file --union`（三方合併、保留兩側
hunk、順序保 base→ours→theirs），不是 set 聯集：log.md 的段落順序有意義。

用法（rebase 停在衝突時）：
    python scripts/resolve_append_only.py          # 解白名單內的衝突檔並 git add，印出結果
    python scripts/resolve_append_only.py --check  # 只列出衝突檔與是否在白名單，不改動
exit 0＝全部衝突檔都在白名單且已解；1＝有白名單外的衝突（未動任何檔）或無衝突可解。
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent  # git root 在 CLAUDE_NEWS 上一層

# 相對 git root。只放「兩側都只會 append」的檔——任何會被改寫既有行的檔都不准進來。
APPEND_ONLY = {
    "CLAUDE_NEWS/wiki/log.md",
    "CLAUDE_NEWS/data/source_attribution.jsonl",
    "CLAUDE_NEWS/data/devpractice-candidates.jsonl",
    "CLAUDE_NEWS/data/pending-signals.jsonl",
    "CLAUDE_NEWS/weekly/open-signals.jsonl",
    "CLAUDE_NEWS/src/logs/task_scheduler.log",
}


def _git(*args, check=True, **kw):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", check=check, **kw)


def conflicted_paths() -> list[str]:
    out = _git("diff", "--name-only", "--diff-filter=U", check=False).stdout
    return [l.strip() for l in out.splitlines() if l.strip()]


def resolve_union(path: str) -> None:
    """三方 union 合併：base(:1) / ours(:2) / theirs(:3)。任一 stage 缺席（一側新增檔）
    則退化為把兩側串接（新檔的 append-append 無 base）。"""
    stages = {}
    for n in (1, 2, 3):
        r = _git("show", f":{n}:{path}", check=False)
        stages[n] = r.stdout if r.returncode == 0 else None
    if stages[1] is None:
        merged = (stages[2] or "") + (stages[3] or "")
    else:
        tmp = [REPO / f".merge_{n}.tmp" for n in (2, 1, 3)]
        for f, n in zip(tmp, (2, 1, 3)):
            f.write_text(stages[n] or "", encoding="utf-8")
        try:
            r = _git("merge-file", "-p", "--union", *[str(f) for f in tmp], check=False)
            merged = r.stdout
        finally:
            for f in tmp:
                f.unlink(missing_ok=True)
    (REPO / path).write_text(merged, encoding="utf-8")
    _git("add", path)


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    check_only = "--check" in argv
    paths = conflicted_paths()
    if not paths:
        print("無衝突檔")
        return 1
    outside = [p for p in paths if p not in APPEND_ONLY]
    inside = [p for p in paths if p in APPEND_ONLY]
    for p in paths:
        print(f"  {'✅ append-only，可自解' if p in APPEND_ONLY else '❌ 白名單外，須人工'}：{p}")
    if outside:
        print(f"有 {len(outside)} 個白名單外衝突，未動任何檔——交回人工（依 Step 5 規則 abort）")
        return 1
    if check_only:
        return 0
    for p in inside:
        resolve_union(p)
        print(f"已 union 合併並 git add：{p}")
    print("下一步：git rebase --continue（或 git -c core.editor=true rebase --continue）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
