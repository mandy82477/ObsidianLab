---
description: 完整每日 pipeline：抓新聞 → wiki ingest → 推送 wiki → 建置 web reader → 推送。
argument-hint: [YYYY-MM-DD]
---

# News Pipeline

執行完整每日自動化流程，分三段執行。

**為何拆三段：** Step 2（wiki ingest 記者派工）需要用 Agent tool 呼叫記者 agent。若把這步包進背景 agent 內執行，「背景 agent 自己再派 agent」這個巢狀情境下，記者的完成通知會被系統送到最上層 session，而不是送回中間那層背景 agent——即使呼叫時完全沒有設定 `run_in_background: true` 也一樣，這是巢狀背景執行的系統性限制，不是措辭問題（已實際發生過一次，該次記錄見 Phase B 說明）。因此：

- **Step 2 必須由呼叫 `/news-pipeline` 的本 session 親自執行**，不可再包進任何背景 agent
- **`/news-pipeline` 本身也不可被包進背景 agent 呼叫**（例如不可用 Agent tool 以 `run_in_background: true` 派一個 agent去執行 `/news-pipeline`）——否則本 session 也變成巢狀背景層，Phase B 一樣會壞掉
- 其餘不涉及 Agent 派工的步驟（Step 0、1a、1b、3、4、5、6）可安全包進背景 agent，節省本 session context

### TARGET_DATE 一律取 UTC 日期 `[加入: 2026-08-29]`

**`date -u +%F`，不是本機時區的今天。** 雲端 routine 用的就是 UTC（見 `docs/cloud-runbooks/daily.md`），本機若用台北日期，兩邊在**台北 00:00–08:00** 這個窗內會差一天——而深夜補跑正好落在那個窗裡。

> 2026-08-29 踩過：台北 00:44 跑的一次補跑，把 UTC 08-28 的資料標成 08-29 那天的日報檔名。那份日報裡 08/29 的條目**一則都沒有**（08/26 三則、08/27 十七則、08/28 廿一則），而它佔住了 08-29 的檔名，使當天真正的新聞被 `Step 0b：冪等閘` 擋在門外——**錯標一天不只是標籤錯，它會吃掉一整天的日報。**

若提供日期參數（`$ARGUMENTS`），以補跑模式執行；否則以今天為目標。

---

## Phase A：背景 agent 執行 Step 0 + 1a + 1b

使用 **Agent tool**：

| 參數 | 值 |
|------|---|
| description | `News pipeline Phase A {TARGET_DATE}` |
| run_in_background | `true` |
| model | `sonnet` |

**prompt**（`{TARGET_DATE}` 替換為**今日的 UTC 日期**（`date -u +%F`）或 `$ARGUMENTS`，格式 YYYY-MM-DD）：

```
你是 Claude News Pipeline Agent（Phase A）。

設定：
- REPO_ROOT   = C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
- PYTHON      = C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe
- TARGET_DATE = {TARGET_DATE}

讀取 `C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS\.claude\commands\news-pipeline-steps.md`，只執行「Phase A 步驟」（Step 0、Step 0b、Step 1a、Step 1b、Step 1c），不執行 Step 2 以後任何步驟，也不呼叫 Agent tool 派工任何 sub-agent。完成後回報 Step 0/1a/1b 各自結果；**若本次走了 archive replay 路徑（`cp src/gathered_archive/<date>.json`）而非現抓，回報中必須明講**（Step 5 的「replay 路徑收尾」是條件式規則，而執行它的 Phase C 看不到 Phase A 的過程）。若 Step 1a 失敗，立即停止並明確標註「Aggregator FAILED」。使用繁體中文輸出。
```

Phase A agent 完成後自動通知本 session。

---

## Phase B：Step 2 Wiki Ingest（本 session 親自執行，不可委派）

收到 Phase A 完成通知後：

- **若 Phase A 回報 Step 1a FAILED** → 不進入 Phase B、不進入 Phase C。本 session 直接用 Bash 對 `REPO_ROOT\src\logs\task_scheduler.log` append 一行 `Aggregator FAILED - stopping`（依 `.claude/commands/news-pipeline-steps.md` Step 6 格式），輸出完成摘要（Step 2 以後全部標記 ⏭️），結束
- **若 Phase A 成功** → **本 session 直接**（不透過任何背景 agent）依 `.claude/commands/wiki-ingest.md` 的完整步驟，針對 TARGET_DATE 執行 wiki ingest：分類 → foreground 派工六類記者 → 彙整 `feature-radar.md` / `index.md` / `log.md`。記下本階段結果（OK / FAILED）供 Phase C 寫入 Step 6 log

---

## Phase C：背景 agent 執行 Step 3–6

Phase B 結束後（無論成功或失敗，皆須進入本階段以完成 Step 6 log 寫入），使用 **Agent tool** spawn 第二個背景 agent：

| 參數 | 值 |
|------|---|
| description | `News pipeline Phase C {TARGET_DATE}` |
| run_in_background | `true` |
| model | `sonnet` |

**prompt**（`{PHASE_A_RESULT}` / `{PHASE_B_RESULT}` 替換為本 session 已知的 Phase A、Phase B 結果摘要）：

```
你是 Claude News Pipeline Agent（Phase C）。

設定：
- REPO_ROOT   = C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
- PYTHON      = C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe
- TARGET_DATE = {TARGET_DATE}

已知結果（供 Step 6 log 寫入使用，不必重新查證）：
- Phase A（Step 0/1a/1b）：{PHASE_A_RESULT}
- Phase B（Step 2 wiki ingest）：{PHASE_B_RESULT}

讀取 `C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS\.claude\commands\news-pipeline-steps.md`，只執行「Phase C 步驟」（Step 3、Step 4、Step 5、Step 6），不呼叫 Agent tool 派工任何 sub-agent。Step 6 log 需整合上述已知結果與本階段（Step 3/4/5）實際結果。使用繁體中文輸出。
```

Phase C agent 完成後自動通知本 session；本 session 彙整 Phase A + B + C 結果，輸出完整完成摘要（格式見 `.claude/commands/news-pipeline-steps.md`「完成摘要」）。完成摘要**必含「📋 待使用者裁示」區塊**（同檔案該小節），把 `wiki/log.md` 當日待確認事項接出來給使用者看，無未決項也要寫「無」。

---

完整步驟規範：`.claude/commands/news-pipeline-steps.md`
