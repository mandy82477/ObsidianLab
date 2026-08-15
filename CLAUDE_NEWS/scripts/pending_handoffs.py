"""記者間「轉知」帳本 —— 讓跨記者交辦有接手驗收，而不是主編口頭轉達後消失。

背景：記者回報的「同步自查」常出現「⚠️ 需主編轉知功能記者評估產品化矩陣」這類跨記者
交辦。過去主編讀到後靠下一次派工時記得口頭帶上，沒有任何機制保證目標記者真的接手
（`docs/workaround-register.md` 登記為「轉知標記無接手驗收機制」）。本腳本照
`scan_pending_verifications.py` 的同構做法：**主編寫帳本 → 派工時附清單 → 記者回報處置
→ 主編結案**，四步都留痕。

帳本：`data/pending-handoffs.jsonl`（append only，最後一筆勝出）
  開立：{"id","opened","from","to","page","note","status":"open"}
  結案：{"id","closed","status":"done","by":"<類別>","result":"<一句話>"}
  作廢：{"id","closed","status":"void","result":"<為何不需處理>"}

用法：
  python scripts/pending_handoffs.py open  --from 社群 --to 功能 --page topics/official-community-gap --note "評估產品化矩陣新增列：<模式名>"
  python scripts/pending_handoffs.py list                       # 依目標類別分組印出未結案清單（派工附件）
  python scripts/pending_handoffs.py list --to 功能             # 只印該類別（無則印「無」）
  python scripts/pending_handoffs.py close H-a1b2c3 --by 功能 --result "已補矩陣列"
  python scripts/pending_handoffs.py void  H-a1b2c3 --result "議題已失效"

設計原則：
1. 只 append 不改寫既有行——結案是新一行，歷史可稽。
2. id 由 (opened, from, to, note) 決定性雜湊而來，同一交辦重複開立不會產生兩筆。
3. 逾 14 天未結案的在 list 中標 ⚠️，讓主編看得到積壓。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEDGER = REPO_ROOT / "data" / "pending-handoffs.jsonl"
CATEGORIES = ("模型", "功能", "商業", "安全政策", "社群", "人物")
STALE_DAYS = 14


def _make_id(opened: str, src: str, dst: str, note: str) -> str:
    h = hashlib.sha1(f"{opened}|{src}|{dst}|{note}".encode("utf-8")).hexdigest()[:6]
    return f"H-{h}"


def load(path: Path = LEDGER) -> dict[str, dict]:
    """回傳 id → 合併後狀態（開立欄位 + 最後一筆結案欄位）。"""
    state: dict[str, dict] = {}
    if not path.exists():
        return state
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError:
            continue
        hid = row.get("id")
        if not hid:
            continue
        cur = state.setdefault(hid, {})
        cur.update(row)
    return state


def _append(row: dict, path: Path = LEDGER) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def open_handoff(src: str, dst: str, page: str, note: str, opened: str | None = None,
                 path: Path = LEDGER) -> str:
    if src not in CATEGORIES or dst not in CATEGORIES:
        raise SystemExit(f"from/to 必須是六類別之一：{', '.join(CATEGORIES)}")
    if src == dst:
        raise SystemExit("from 與 to 相同——同記者的待辦不是轉知，寫進頁面或 log 即可")
    opened = opened or date.today().isoformat()
    hid = _make_id(opened, src, dst, note)
    if hid in load(path):
        return hid  # 冪等：同日同交辦重複開立不重複記
    _append({"id": hid, "opened": opened, "from": src, "to": dst, "page": page,
             "note": note, "status": "open"}, path)
    return hid


def close_handoff(hid: str, by: str, result: str, status: str = "done",
                  closed: str | None = None, path: Path = LEDGER) -> None:
    state = load(path)
    if hid not in state:
        raise SystemExit(f"找不到 {hid}")
    if state[hid].get("status") != "open":
        raise SystemExit(f"{hid} 已是 {state[hid].get('status')}，不可重複結案")
    _append({"id": hid, "closed": closed or date.today().isoformat(), "status": status,
             "by": by, "result": result}, path)


def open_items(path: Path = LEDGER, to: str | None = None) -> list[dict]:
    rows = [r for r in load(path).values() if r.get("status") == "open"]
    if to:
        rows = [r for r in rows if r.get("to") == to]
    return sorted(rows, key=lambda r: (r.get("to", ""), r.get("opened", "")))


def render(rows: list[dict], today: date | None = None) -> str:
    """派工附件：依目標類別分組；無則印「無」。"""
    today = today or date.today()
    if not rows:
        return "無"
    out: list[str] = []
    by_to: dict[str, list[dict]] = {}
    for r in rows:
        by_to.setdefault(r.get("to", "?"), []).append(r)
    for dst in CATEGORIES:
        group = by_to.get(dst)
        if not group:
            continue
        out.append(f"### 轉知待接手 → {dst} 記者（{len(group)} 筆）")
        for r in group:
            try:
                age = (today - datetime.strptime(r["opened"], "%Y-%m-%d").date()).days
            except Exception:
                age = 0
            flag = " ⚠️ 逾 14 天" if age > STALE_DAYS else ""
            out.append(
                f"- {r['id']}（{r.get('opened','?')} 由 {r.get('from','?')} 記者轉知{flag}）"
                f"｜頁面 `{r.get('page','—')}`｜{r.get('note','')}"
            )
        out.append("")
    return "\n".join(out).rstrip()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_open = sub.add_parser("open"); p_open.add_argument("--from", dest="src", required=True)
    p_open.add_argument("--to", required=True); p_open.add_argument("--page", default="—")
    p_open.add_argument("--note", required=True); p_open.add_argument("--date")
    p_list = sub.add_parser("list"); p_list.add_argument("--to")
    p_close = sub.add_parser("close"); p_close.add_argument("id"); p_close.add_argument("--by", required=True)
    p_close.add_argument("--result", required=True)
    p_void = sub.add_parser("void"); p_void.add_argument("id"); p_void.add_argument("--result", required=True)
    a = ap.parse_args(argv)

    if a.cmd == "open":
        print(open_handoff(a.src, a.to, a.page, a.note, a.date))
    elif a.cmd == "list":
        print(render(open_items(to=a.to)))
    elif a.cmd == "close":
        close_handoff(a.id, a.by, a.result); print(f"closed {a.id}")
    elif a.cmd == "void":
        close_handoff(a.id, "主編", a.result, status="void"); print(f"void {a.id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
