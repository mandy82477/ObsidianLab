#!/usr/bin/env python3
"""質疑題庫——把使用者歷史上「真的嗎？」的問法制度化（現八種），供 `/wiki-lint` 7b 抽問。

為什麼存在（2026-09-02）：
    `wiki/log.md` 有 35 筆 Query 條目（2026-05-28 起），紀錄「使用者哪句話揭露了
    哪個缺陷」。回顧發現：歷史上所有重大品質問題（25 則新聞靜默消失、日報漏收
    48%、Dreaming 假死案、懸置 20 天無人讀、排程從未建立…）**全部**來自使用者的
    不定期質疑，沒有一次是排程檢查抓到的——排程檢查考的是「考卷內」，真問題在
    「考卷外」。而使用者的質疑歸納起來反覆只有少數幾種模式，每種都可操作化成探針
    （首版七種；2026-09-02 經使用者確認加入第八種「資產重用審計」——加題條件與
    流程見 .claude/rules/wiki-lint-inquiry.md「題庫維護」）。
    本題庫把「已經問過的問題」變成常設檢查：使用者問過一次的，不需要再問第二次；
    但新型質疑仍然只有人問得出來——所以 `open_loops.py` 的
    「人類質疑時效燈」不因本題庫在跑而熄滅。

抽選紀律（為什麼 seed 綁 ISO 週）：
    行為層抽驗的教訓：規則只寫「隨機抽」時，LLM 的「隨機」是自由心證，會偏向
    好答的題。本腳本用 ISO 週字串當預設 seed——同一週內重跑結果相同，主編不能
    重擲骰子換題；下一週自動換題。`--seed` 僅供測試與補跑指定。

用法：
    python scripts/inquiry_bank.py draw          # 本週抽 2 題（seed=ISO 週）
    python scripts/inquiry_bank.py draw --n 1
    python scripts/inquiry_bank.py all           # 列出全部題目
純標準庫、零網路、無 LLM 呼叫。
"""
import argparse
import io
import random
import sys
from datetime import date

BANK = [
    {
        "id": "Q1",
        "name": "溯源",
        "question": "近 7 天寫進 wiki 的具體數字，答得出「你哪來的」嗎？",
        "origin": "2026-08-08 pricing 官方查證（懸置 20 天）；CLAUDE_BIZ 96GB 事件同型",
        "probe": [
            "列近 7 天 wiki 新增的帶單位數字：git diff $(git rev-list -1 --before=\"7 days ago\" HEAD) -- wiki/entities wiki/topics | grep '^+' | grep -oE '[0-9][0-9,.]*(%|倍|萬|億|美元|/Mtok|天)' | sort -u（不可用 reflog 語法——雲端 lint 是 fresh clone，reflog 為空）",
            "用本週 seed 擲骰抽 1 個數字（同週重跑須同題）",
            "回查：該數字在 news/*.md 或該頁「參考來源」有沒有對應條目／官方連結",
            "答不出來源 → 依 .claude/rules/wiki-ingest-format.md 懸置標記語法標記，或退回對應記者",
        ],
    },
    {
        "id": "Q2",
        "name": "缺席偵測",
        "question": "有沒有東西該進來卻沒進來？（抓到的 vs 刊出的）",
        "origin": "2026-07-13 emitted-cache 25 則靜默消失；2026-07-26 日報漏收 48%；2026-08-28 Dreaming 假死案",
        "probe": [
            "讀 data/source_funnel.jsonl 最新一列的 sources 欄（每來源有 gathered/filtered/emitted 三數）",
            "抽 1 個「gathered>0 且 emitted=0」的來源（無則抽 gathered−emitted 落差最大者）",
            "開當日 src/gathered_archive/ 對應檔，逐條判斷被擋條目「擋得對嗎」（對照收錄門檻，不可只看數字就結案）",
            "發現該收未收 → 走補跑流程並記 log；判斷模稜 → 記待辦回報使用者",
        ],
    },
    {
        "id": "Q3",
        "name": "沉默質疑",
        "question": "沒動靜的東西，是 no-op 還是死了？",
        "origin": "2026-07-13 排程從未建立；2026-08-12 push 卡分支；2026-08-08 本週推薦凍結 14 天",
        "probe": [
            "驗三個心跳：news/ 最新檔距今 ≤1 天；weekly/ 最新 ≤8 天；git log --since=\"36 hours\" --oneline 有自動線 commit",
            "任一沉默：找「no-op 證據」（心跳紀錄／watchdog run 綠）或「死因」，二選一，不可只看產出缺席就宣稱正常或逕行補跑",
            "feature-radar「本週推薦」最後輪替日 >14 天 → 依防霸榜規則覆核",
        ],
    },
    {
        "id": "Q4",
        "name": "讀者查找",
        "question": "隨機一則長尾事實，讀者 3 跳內找得到嗎？",
        "origin": "2026-08-10「有跨 session 傳送功能嗎？wiki 有寫嗎」→ 懸置無消化端",
        "probe": [
            "從近 7 天日報條目擲骰抽 1 個功能／事件名（刻意不挑熱點——步驟 7 讀者模擬已覆蓋熱點題，本題考長尾）",
            "模擬讀者：從 wiki/index.md 出發 3 跳找它",
            "找不到 → 先問「這個事實在分類表有沒有落點」（對照 2026-08-16 兩層都漏案），是縫隙就回報使用者，不是就補 wikilink／callout",
        ],
    },
    {
        "id": "Q5",
        "name": "可讀性",
        "question": "冷讀者打開近期改過的頁，前 160 字讀得懂嗎？表格爆版了嗎？",
        "origin": "2026-07-28 網站 review 15 項修正；2026-08-05 model-comparison 表格爆版",
        "probe": [
            "列近 7 天有改動的頁：git diff --name-only $(git rev-list -1 --before=\"7 days ago\" HEAD) -- wiki/entities wiki/topics，擲骰抽 1 頁（不可用 reflog 語法，雲端 reflog 為空）",
            "跑儲存格量測（>120 字元即違規，指令見 .claude/rules/wiki-ingest-format.md「表格放結論，細節下沉」）",
            "讀該頁前 160 字：能否不看背景就懂（delta-first ＋ 可獨立閱讀）",
            "違規依 .claude/rules/wiki-ingest-format.md 修復；修不動記待辦",
        ],
    },
    {
        "id": "Q6",
        "name": "結構健檢",
        "question": "文件說存在的自動化元件，真的存在、而且活著嗎？",
        "origin": "2026-07-13 trigger 從未建立；2026-08-16 週報規格範本錯了三週沒人回頭校對",
        "probe": [
            "從 docs/daily-automation.md 與 docs/cloud-runbooks/ 宣稱的元件（workflow／trigger／腳本名）擲骰抽 1 個",
            "驗兩層：存在（workflow 檔在 git repo 根層的 .github/workflows/——注意在父層 ObsidianLab/，不在 CLAUDE_NEWS/ 內；腳本在 scripts/）＋活著（近 7 天有對應 run／commit／產出／心跳）",
            "雲端 trigger 本機驗不了 → 記「需雲端 RemoteTrigger list 核對」待辦，不可宣稱已驗——文件寫了 ID 不代表它存在",
        ],
    },
    {
        "id": "Q8",
        "name": "資產重用審計",
        "question": "本輪新建的機制／腳本，動手前盤點過既有資產嗎？",
        "origin": "2026-09-02 兩例同日：graphify（答題時單入口滿足）、wiki_graph（設計時零盤點，使用者一句「graph 不能幫上忙嗎」砍半設計）",
        "probe": [
            "列本輪新增資產：git log --since=\"7 days ago\" --diff-filter=A --name-only -- scripts | sort -u，另 grep 規則檔近 7 天新增的 `[加入:` 機制節",
            "逐一回答「動手前有沒有先盤點既有能力」——證據＝盤點結果寫在哪（commit 訊息／log／規則檔）；答不出即 ⚠️",
            "對每個新機制問：wiki_graph／news_mentions／check_* 家族是否已蓋住其一部分？有重疊 → 記待辦提減法重構（本庫教訓：有效的修改全部是減法）",
        ],
    },
    {
        "id": "Q7",
        "name": "宣稱對帳",
        "question": "頁面上描述「現在」的句子，今天還成立嗎？",
        "origin": "2026-08-28 Sonnet 促銷殘留 5 處（距不存在的到期日 3 天）；2026-08-08 上修沒回掃 12 天",
        "probe": [
            "grep -rnE '(截至|預計|即將|促銷|到期|生效)' wiki/entities wiki/topics 取帶日期者，擲骰抽 1 筆",
            "該日期已過 → 查日報／官方後續，依 .claude/rules/wiki-reporter-shared.md「事實更正必回掃」處理：改掉＋回掃（先 `wiki_graph.py explain <頁> --section`，再拿關鍵字 grep 補漏）",
            "未過期 → 驗敘述與最新日報一致即結案",
        ],
    },
]


class BankIntegrityError(RuntimeError):
    """題庫自檢失敗。刻意不吞——一支代打質疑的腳本自己壞掉還印題目，就是它要治的病。"""


def check_integrity(bank=None) -> None:
    bank = BANK if bank is None else bank
    if len(bank) < 7:
        raise BankIntegrityError(f"題庫只剩 {len(bank)} 題（<7）——刪題須經使用者確認並同步七模式文件")
    ids = [q["id"] for q in bank]
    if len(set(ids)) != len(ids):
        raise BankIntegrityError(f"題目 id 重複：{ids}")
    for q in bank:
        for field in ("id", "name", "question", "origin", "probe"):
            if not q.get(field):
                raise BankIntegrityError(f"{q.get('id', '?')} 缺欄位 {field}")
        if len(q["probe"]) < 2:
            raise BankIntegrityError(f"{q['id']} 探針少於 2 步——單步探針驗不出東西（同懸置探針 ≥2 的理由）")


def default_seed(today=None) -> str:
    today = today or date.today()
    iso = today.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


def draw(n=2, seed=None, today=None):
    check_integrity()
    seed = seed or default_seed(today)
    rng = random.Random(seed)
    n = max(1, min(n, len(BANK)))
    return seed, rng.sample(BANK, n)


def _print_question(q: dict) -> None:
    print(f"\n[{q['id']}] {q['name']}——{q['question']}")
    print(f"    教訓出處：{q['origin']}")
    for i, step in enumerate(q["probe"], 1):
        print(f"    {i}. {step}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="質疑題庫（/wiki-lint 7b 抽問）")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_draw = sub.add_parser("draw", help="抽題（預設 2 題，seed=本 ISO 週）")
    p_draw.add_argument("--n", type=int, default=2)
    p_draw.add_argument("--seed", default=None, help="僅供測試與補跑；日常不可傳（防重擲換題）")
    sub.add_parser("all", help="列出全部題目")
    args = parser.parse_args(argv)

    try:
        check_integrity()
    except BankIntegrityError as e:
        print(f"❌ 題庫自檢失敗：{e}")
        return 2

    if args.cmd == "all":
        print(f"質疑題庫共 {len(BANK)} 題（單一來源；機制說明見 .claude/rules/wiki-lint-inquiry.md）")
        for q in BANK:
            _print_question(q)
        return 0

    seed, picked = draw(n=args.n, seed=args.seed)
    print(f"本輪抽題 seed={seed}（同週重跑同題，不可重擲換題）：{ '、'.join(q['id'] for q in picked) }")
    for q in picked:
        _print_question(q)
    print("\n每題三態結果：✅ 通過（附證據行）／⚠️ 已修復（說明改了什麼）／❌ 待辦（記 log 並回報使用者）")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.exit(main())
