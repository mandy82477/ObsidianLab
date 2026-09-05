# 全站頁面 review 總帳

流程與角色見 `.claude/skills/page-audit-review/SKILL.md`；共用派工前綴見 `docs/page-audits/dispatch-prefix.md`。

**起點（使用者裁決 2026-09-05）：** 從讀者三個根問題各走一條路徑，不從單一樞紐頁擴散。
**裁決節奏（使用者裁決 2026-09-05）：** 授權主 session 下非阻擋級裁決（文筆、欄位、表格判準、蒸餾）；**拆頁／砍整節／改頁面使命句**必須停下來問使用者。

## 三條路徑

| 路徑 | 讀者的根問題 | 涉及頁面（依入邊） |
|---|---|---|
| P1 | 我該用哪個模型／誰比較強 | `topics/model-comparison`(28)、`topics/model-task-leaderboard`(5)、`topics/competitor-landscape`(52，已定稿) |
| P2 | 我該不該升版 | `wiki/feature-radar`、`entities/claude-code`、`topics/code-quality-decline`（待盤點） |
| P3 | 外面有什麼會衝擊我／要花多少錢 | `entities/pricing`(135)、`topics/enterprise-cost-management`、`topics/competitor-landscape`（待盤點） |

## 分層判準（入邊數，`python scripts/wiki_graph.py explain <slug>`）

樞紐 ≥15：完整六問卡＋設計／評審（Opus）｜中層 5–14：輕量卡（Q1/Q2/Q4/Q5）｜葉子 <5：機械掃描＋一句冷讀者判斷（Sonnet）

## 總帳

| 波 | 頁面 | 層 | 健檢日 | 裁決 | 複驗 | 回訪日 | 產物 |
|---|---|---|---|---|---|---|---|
| 0（試點） | topics/competitor-landscape | 樞紐(52) | 2026-09-05 | 已定稿（雷達表／一行制時序／06 月封存；587→423 行） | ✅ 原考題複驗過 | 2026-09-12 | `competitor-landscape-2026-09-05{,-proposals,-review,-final}.md` |
| 1 | topics/model-comparison | 樞紐(28) | 2026-09-05 | 定稿：使命句定稿、三節移出正文、Benchmark 表凍結降位第 8 節（到期 2027-03-04）、摘要補真答案＋出口 | ✅ 複驗過（Q1 死路→3 跳拿到帶數字答案；Q2–Q4 由 2 跳→1 跳） | 2026-09-12 | `model-comparison-2026-09-05{,-proposals,-review,-final}.md`、`wave1-cold-reader-2026-09-05.md` |
| 1 | topics/model-task-leaderboard | 葉子(5)→升輕量卡 | 2026-09-05 | 定稿：摘要宣告「跨家到此為止」、承認本頁量模型不量工具＋懸置登記、index 補路由 | ✅ 複驗過（Q1 死路→3 跳拿到帶數字答案；Q2–Q4 由 2 跳→1 跳） | 2026-09-12 | 併入同一波產物 |
| 2 | entities/managed-agents | 樞紐(31) | 2026-09-05 | 進行中（使用者點名；新契約首用：健檢卡＋冷讀者 2 棒起，Q2 判定後決定是否加設計者） | — | — | `managed-agents-2026-09-05*.md`、`wave2-cold-reader-2026-09-05.md` |

> 第 1 波同時吃掉 `wiki/reader-notes.md` 的 ⏳「『誰比較強』三頁互踢」——考題集必含「Codex 和 Claude 誰強」，落點必須唯一。

## 本波順帶落地的機械看守（第 1 波）

| 閘 | 治什麼 | 存量處置 | 驗證 |
|---|---|---|---|
| `scripts/check_cell_limits.py`（掛 `run_tests.py`） | 儲存格 >120／細節區條列 >200 —— 規則檔明文兩個月、零偵測器 | `data/cell-limit-baseline.json` 1191 筆／38 頁，只擋新增 | 注入 121／201 字元 → FAIL；邊界值 → 通過 |
| `build_web.py` 錨點掃描補 `weekly/` 並改致命 | 節名凍結的第二把鎖（registry `anchors` 只擋節名被改，擋不到別頁把錨點打錯） | 存量失效 0 筆，今天成本 0 | 注入壞錨點 → exit 1 指名該筆；還原 → exit 0 且 byte-identical |

## 2026-09-12 回訪要查什麼（第 1 波）

1. 每日更新有沒有把兩頁磨回舊形狀（MC 三節有沒有長回來、LB 摘要的邊界句還在不在）
2. 凍結節名有沒有被改（`registry` anchors 兩筆＋錨點致命閘應該擋得住，但要確認擋的是對的東西）
3. `check_cell_limits` 有沒有誤擋（記者改寫既有超限文字會脫離指紋基線）——看 lint 回報有沒有人抱怨
4. 複驗留下的未修項：LB `## 本週註記` 的編輯部進度報告口吻（修它要同步改 `/wiki-lint` 5b，否則下週長回來）、`⟨Q-nn⟩` 短標記無圖例
5. 三筆轉知帳本（H-7dbf7a／H-27721d／H-402a37）有沒有被接手
