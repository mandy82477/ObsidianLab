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
| 1 | topics/model-comparison | 樞紐(28) | 2026-09-05 | 進行中 | — | — | `model-comparison-2026-09-05*.md` |
| 1 | topics/model-task-leaderboard | 葉子(5)→升輕量卡 | 2026-09-05 | 進行中 | — | — | 併入同一波產物 |

> 第 1 波同時吃掉 `wiki/reader-notes.md` 的 ⏳「『誰比較強』三頁互踢」——考題集必含「Codex 和 Claude 誰強」，落點必須唯一。
