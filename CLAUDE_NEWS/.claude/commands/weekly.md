---
description: 每週總指揮：依序跑週報產出（對外交付）與 wiki 週度延伸回顧（對內策展），最後統一收尾單一 push。
argument-hint: [YYYY-Wnn]
---

# Weekly — 每週總指揮

**每週只要下這一個指令。** 它依序帶起兩個子指令，最後統一收尾：

| 順序 | 子指令 | 性質 | 產出 |
|---|---|---|---|
| 0 | 本檔步驟 0 | 本機專屬補跑 | 5b 榜單週更、5c 清算（5 筆）、lint 待裁示呈報 |
| 1 | `.claude/commands/weekly-report.md` | 對外交付 | `weekly/YYYY-Wnn.md`（凍結存檔） |
| 2 | `.claude/commands/wiki-weekly-review.md` | 對內策展 | `wiki/` 頁面加碼 + `wiki/log.md` |
| 3 | 本檔步驟 3 | 收尾 | commit + test + build + **單一 push** |

---

## 使用方式

- `/weekly`：跑本週（今日所在 ISO 週）
- `/weekly 2026-W30`：指定週次，`$ARGUMENTS` 原樣傳給 `/weekly-report`；`/wiki-weekly-review` 不吃週次參數，一律以今日為準

只想跑其中一段時，直接下該子指令（`/weekly-report` 或 `/wiki-weekly-review`），它們各自的收尾步驟會自己負責。

---

## 🔒 順序與邊界（不可調換、不可合併）

**執行順序固定為「週報先、策展後」**，且兩者是兩段獨立工作，不可揉成一段。三個理由：

| 理由 | 說明 |
|---|---|
| **確認閘相反** | `/wiki-weekly-review` 明訂未經使用者確認不得修改任何頁面（延伸判斷屬主觀取捨）；`/weekly-report` 是自主產出。合併後只會二選一：週報被卡在確認閘後面，或策展變成自動執行——後者等於廢掉那條規則 |
| **凍結語義衝突** | `/weekly-report` 步驟 5 明訂寫入後即凍結、不因後續 ingest 回頭修改；`/wiki-weekly-review` 則主動改 wiki。若策展先跑，週報會引用到同一次執行中剛被改出來的頁面狀態 |
| **帳本獨立性** | 週報第 (3) 段的帳本有機械檢查（`scripts/check_weekly_ledger.py`）與反確認偏誤護欄。策展若先知道本週開了哪些預告，會傾向加碼「能讓預告成真」的主題——與 `.claude/commands/news-pipeline-steps.md` Step 3e 對選材的警告同源 |

> 判斷式：**這一步會不會讓後面那步「已經知道答案」？** 會 → 順序錯了。

---

## 步驟

### 0. 本機專屬步驟補跑（先做，不可略過）`[加入: 2026-08-20]`

`/wiki-lint` 有三個步驟需要「網路 ＋ LLM 同時具備」，雲端 routine（egress 封鎖）做不到、GitHub Actions（無 LLM）也做不到——**只有本機 session 有**。它們原本寫「留待本機執行」，但沒有任何機制保證本機真的會跑，結果是系統性餓死：

| 佐證（`wiki/log.md`） | 現象 |
|---|---|
| 08-01 留待辦 → 08-08「非本月首次，跳過」→ 08-15 再跳過 | 死鏈檢查自 2026-07 起一次都沒真正跑過（已於 2026-08-20 移交 GitHub Actions，不再需要本步） |
| `topics/model-task-leaderboard` 最後更新 = 建頁當天 | 號稱「週快照」的頁停更 15 天 |
| 5c 上次執行是使用者親自要求 | 待查證存量的唯一消化端，實際消化速率趨近於零 |

`/weekly` 是**本機每週固定會下的指令**，因此把這些步驟掛在這裡。誠實揭露其失效模式：**你哪週沒跑 `/weekly`，這兩步那週就沒跑**——但這遠優於現況（每週都跑不到）。

依序執行，全部讀 `.claude/commands/wiki-lint.md` 的對應節，不在此重述做法：

1. **5b 跨家任務榜單週更**——照 `.claude/commands/wiki-lint.md`「5b. 跨家任務榜單週更」執行（派 `general-purpose` ＋ `model: "haiku"` 抓榜）
2. **5c 逾期待查證清算**——照該檔「5c. 逾期待查證清算」執行，**本輪額度 5 筆**（`check_pending_markers.py --queue` 已內建此上限）。務必照 5c 第 5 步做結案回掃，並把輸出末尾的「⚠️ 舊語法盲區」抄進回報
3. **lint 待裁示事項呈報**——`Grep "待使用者確認\|待裁示" wiki/log.md` 取最近 3 次 lint 紀錄的未決事項，**直接列在本指令的輸出裡呈給使用者**，每項標「⏳ 已擱置 N 週」。理由：那些事項只寫進 `wiki/log.md`，而**使用者不讀該檔**——不呈報等於沒提過（實例：某建頁候選連續第 6 週被提出而未被看見）

> 這三項的產出一律**併入步驟 3 的單一 push**，不自行 commit（同步驟 1、2 的收尾紀律）。

### 1. 週報產出（對外交付）

讀 `.claude/commands/weekly-report.md` 並依其步驟 1–5 執行，`$ARGUMENTS` 原樣傳入。

**跳過該檔的步驟 6（收尾閉迴路）**——commit / build / push 一律留到本檔步驟 3，避免兩次 push 觸發兩個 GitHub Pages 部署互相搶佔。

### 2. wiki 週度延伸回顧（對內策展）

讀 `.claude/commands/wiki-weekly-review.md` 並依其步驟 1–5 執行（含六記者並行判斷、月度聚焦校準判斷、`wiki/reader-notes.md` 收件匣消費、彙整清單交使用者確認、依確認執行、log 記錄）。

- **使用者確認閘保留**：步驟 3 的建議清單仍須經使用者確認才可執行修改，本指令不代為決定
- **跳過該檔的步驟 6（收尾閉迴路）**——同上，留到步驟 3
- 使用者若回「都不要」，仍須照該檔規定 append log.md 那一筆

### 3. 統一收尾閉迴路

兩段都跑完後才執行。`REPO_ROOT` = `C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS`，`PYTHON` = `C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe`：

1. `git -C REPO_ROOT add weekly/ wiki/ data/source_attribution.jsonl` → `git -C REPO_ROOT commit -m "weekly: YYYY-Wnn 週報＋週度延伸回顧"`（無變更則跳過）
2. `PYTHON REPO_ROOT\scripts\run_tests.py`（失敗 → 跳過 build 與 web commit，仍執行第 4 步推送已完成的 commit，並在回報標「Tests FAILED - build skipped」）
3. `PYTHON REPO_ROOT\scripts\build_web.py` → `git -C REPO_ROOT add web_reader/` → `git -C REPO_ROOT commit -m "web: rebuild YYYY-Wnn（週報＋週度回顧上站）"`
4. `git -C REPO_ROOT push`（**單一 push**）

- **push 失敗**：照 `.claude/commands/news-pipeline-steps.md` 的 `Step 5` push 失敗重試程序處理（`pull --rebase` 上限 2 次），不要另寫一套
- **與排程的關係**：本指令無雲端排程。`weekly/` 不與任何排程重疊；`wiki/` 會與 `weekly-wiki-lint-cloud`（每週六 01:00 UTC）及 `daily-news-pipeline-cloud`（每日 13:00 UTC）競爭，靠上述 push 重試化解

---

## 完成回報

```
## Weekly YYYY-Wnn

- 週報：weekly/YYYY-Wnn.md（深挖題目：…）
- 延伸回顧：執行 N 項 / 使用者跳過 M 項
- 聚焦校準：（月度才有，或「非本月首次，跳過」）
- 收尾：測試 ✅／❌｜build ✅／跳過｜push ✅
```

---

## 注意事項

- 繁體中文為主
- 兩個子指令各自的規則以其檔案為準，本檔只負責**順序、邊界與收尾**，不重複它們的內容規範（避免兩處失步）
- 兩子指令的收尾步驟被本檔接管——修改任一子指令的收尾段落時，必須同步確認本檔步驟 3 仍涵蓋其產出路徑
