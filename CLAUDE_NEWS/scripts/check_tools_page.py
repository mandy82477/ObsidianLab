#!/usr/bin/env python3
"""community-tech-tools 決策表契約檢查。

2026-09-02 改版把該頁核心從「工具清單」換成「症狀 → 首選」決策表，
新增了兩種對讀者的承諾，各配一條機械檢查（reviewer 審查結論：承諾
不配偵測器就是本庫病史的複製——規則有了、執行點沒有）：

  1. 數字必帶日期：決策表與「推薦細節」「不綁症狀的精選」區裡含
     量化宣稱（%、倍、星數、token 數）的行，同行必須有日期
     （YYYY-MM-DD 或 MM-DD）。證據值是收錄當時的快照，沒有日期
     的快照半年後仍讀作現況——這正是 pricing 頁「資料截至」紀律
     的複製，只是這裡交給機器驗（改壞驗紅：刪掉任一日期本檢查應轉紅）。
  2. 首選唯一：決策表「先裝這個」欄每格至多一個工具（一個粗體名
     或一條連結；「—」豁免）。9 個工具擠一格＝沒有推薦，是改版
     要治的根病，不可默默長回去。

純標準庫、零網路。用法：python scripts/check_tools_page.py
exit 0=通過；1=違規（列出行號）。
"""
import io
import re
import sys
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "wiki" / "topics" / "community-tech-tools.md"

NUM_CLAIM = re.compile(r"\d+(?:[\d,.]*)\s*(?:%|倍|星|萬星|k stars|stars|token)", re.I)
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}|（\d{2}-\d{2}[，)）]|\d{2}-\d{2}\b")


def _section(text: str, header: str) -> str:
    m = re.search(rf"^## {re.escape(header)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def check(text: str):
    fails = []

    # ── 1. 數字必帶日期（決策表＋細節＋精選；目錄沿用舊制不查，待後續波次遷移）──
    scope = _section(text, "我卡在這裡") + _section(text, "不綁症狀的精選")
    offset_lines = []
    for name in ("我卡在這裡", "不綁症狀的精選"):
        m = re.search(rf"^## {re.escape(name)}", text, re.M)
        if m:
            offset_lines.append((name, text[: m.start()].count("\n") + 1))
    for i, line in enumerate(scope.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if NUM_CLAIM.search(s) and not DATE_RE.search(s):
            fails.append(f"數字無日期：…{s[:70]}")

    # ── 2. 首選唯一 ──
    table = _section(text, "我卡在這裡")
    for line in table.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 4 or cells[0] in ("我的症狀",) or set(cells[0]) <= {"-", ":", " "}:
            continue
        pick = cells[1]
        if pick.startswith("—"):
            continue
        tools = len(re.findall(r"\*\*[^*]+\*\*", pick))
        if tools != 1:
            fails.append(f"首選非唯一（{tools} 個粗體工具名）：{cells[0][:24]} → {pick[:50]}")

    if not table.strip():
        fails.append("找不到 `## 我卡在這裡` 決策表——頁面結構被改動，本檢查與規則檔需同步")
    return fails


def check_spokes(text: str, wiki_dir: Path):
    """全站 🧰 行的症狀句對帳——hub-spoke 唯一 graph 做不到的機械檢查。

    問題頁的「🧰 現在就能下的解」行引用決策表症狀句；首選換名、症狀列改寫時
    這些散在各頁的引用會靜默失真（同懸置探針回掃的理由）。graph 管「邊存不存在」
    （wiki_graph.py explain），本函式管「引的句子還在不在」。
    缺口態（含「候選症狀：」）不對帳——那是誠實留白，聚合由策展 grep 處理。
    """
    symptoms = set()
    for line in _section(text, "我卡在這裡").splitlines():
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) >= 4 and cells[0] not in ("我的症狀",) and not set(cells[0]) <= {"-", ":", " "}:
                symptoms.add(cells[0])
    fails = []
    for f in list(wiki_dir.glob("topics/*.md")) + list(wiki_dir.glob("entities/*.md")):
        if f.name == "community-tech-tools.md":
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "🧰" not in line or "community-tech-tools" not in line:
                continue
            quoted = re.findall(r"「([^」]+)」", line.split("候選症狀")[0])
            for q in quoted:
                if q in ("我卡在這裡",):
                    continue
                if q not in symptoms:
                    fails.append(f"spoke 引用失效 {f.name}:{n}：「{q}」不在決策表症狀欄")
    return fails


def main() -> int:
    text = PAGE.read_text(encoding="utf-8")
    fails = check(text) + check_spokes(text, PAGE.parent.parent)
    print("# check_tools_page.py（決策表契約＋spoke 對帳）")
    if fails:
        for f in fails:
            print(f"  ❌ {f}")
        print(f"狀態：❌ {len(fails)} 項違規")
        return 1
    print("狀態：✅ 數字皆帶日期、首選皆唯一、全站 🧰 spoke 症狀句對帳通過")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.exit(main())
