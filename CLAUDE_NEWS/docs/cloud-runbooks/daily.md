# 雲端 routine：每日新聞 pipeline（daily-news-pipeline-cloud）

`[建立: 2026-07-25]`

**先讀 `docs/cloud-runbooks/_shared.md`**（環境覆寫、收尾閉迴路、無人值守原則），再照本檔執行。

你執行的是「GitHub Actions 抓料 + 雲端 routine 做 LLM」分裂架構的**第二段**（架構全貌見 `docs/daily-automation.md`）。第一段（抓新聞）已由 GitHub Actions 完成並把資料 commit 進 repo，**你不重複抓料**——雲端 egress 被封鎖，抓也抓不到。

**目標日期不是「今天」，是「還沒出過報的原料日期」。**

開工前先算出待生成清單：`src/gathered_archive/` 裡每一個檔名日期 `<date>`，若
`news/<date>.md` **不存在**，就是一個待生成目標。由舊到新排序，逐一執行；清單為空
則本輪無事可做（照 `_shared.md` 寫心跳，不算失敗）。

每個目標走 `.claude/commands/news-pipeline-steps.md`「補跑注意事項」第 2 條的 replay
路徑：`cp src/gathered_archive/<date>.json src/gathered_items.json`，**跳過 Step 1a**，
從 Step 1b 開始，TARGET_DATE 即該 `<date>`。

> **為什麼不是 `date -u +%F`，也不是 `gathered_items.json` 的 date。**
> 抓料與本 routine 是兩個各自排程的工作。用時鐘當目標，等於要求兩者落在同一個
> UTC 日——任一邊延遲就中止（2026-08-27／08-28 連兩天如此）。改讀
> `gathered_items.json` 也不行：它是**單槽**的，而抓料（10:23 UTC）排在本 routine
> （13:00 UTC）之前，延遲那批會被隔天準時的抓料覆寫掉。
> `gathered_archive/` 按資料日期分檔、已進 git、保留 14 天——它是耐久的那一份，
> 讀它就不需要任何補償機制：哪天沒出過報就補哪天，正常日恰好只有今天一個目標。
---

## 前置閘與失敗處理：不在本檔

`Step 0b：冪等閘`（日報已存在則中止）、`Step 1b` 開頭的新鮮度防線（資料非目標日期／為空則中止）、以及 `Step 5` 的 push 失敗重試，全部定義在 `.claude/commands/news-pipeline-steps.md`，**本機與雲端行為完全相同**，照該檔執行即可。

本檔不重複這些邏輯——兩處各寫一份就會失步，而失步的那一份會在無人值守時生效。

**雲端專屬的只有中止時的落地方式：** 中止時把該步驟要求的訊息 append 到 `src/logs/task_scheduler.log`，並 commit + push 出去：

```
git add src/logs/task_scheduler.log
git commit -m "chore: cloud routine abort log TARGET_DATE"
git push        # 失敗時照 Step 5 的 push 重試程序處理
```

否則在沒有互動使用者的環境下，中止理由會跟著容器一起消失。中止**不是**錯誤，是設計上的正確行為，摘要照常輸出，但要寫清楚是哪一道閘擋下的。

---

## 第二步：執行 pipeline 步驟

規範來源是 `.claude/commands/news-pipeline-steps.md`（步驟細節不在本檔重複，避免兩份副本失步）。依下表對照執行，**用標題找步驟，不要用編號推測範圍**：

| 該檔中的步驟標題 | 雲端如何處理 |
|------|------|
| `Step 0：昨日缺跑檢查` | TARGET_DATE 為今日時照做；補上前一天的日報時 TARGET_DATE 非今日，該步驟本就跳過 |
| `Step 0b：冪等閘` | 照做。非 backfill 模式，所以「日報已存在」一律中止——這正是「這批資料已經變成日報了」的判斷 |
| `Step 1a：新聞抓取` | **跳過**——改為 `cp src/gathered_archive/<目標日>.json src/gathered_items.json`（replay 該日真實原料），新鮮度由 Step 1b 開頭的防線把關 |
| `Step 1b：生成日報` | 照做，完成後 commit（**不 push**） |
| `Step 1c：確認 emitted-cache` | **照做，不可跳過，且必須 commit `src/news_aggregator/emitted_items.json`**（該 Step 已明文要求）——你是全新 checkout、結束後容器銷毀，不 commit 等於沒改過。2026-07-14～07-24 雲端每日確認率幾乎為 0 就是漏了這個 commit。失敗只記警告，繼續後續步驟 |
| `Step 2：Wiki Ingest` | 照做，但規範在別的檔案，見下方「Wiki Ingest」段落 |
| `Step 3：Commit Wiki 變更` | 照做（不 push） |
| `Step 4：建置 Web Reader` | 照做（先跑測試套件，失敗則跳過 build 仍繼續） |
| `Step 5：Commit Web 並統一推送` | 照做，**單一 push** |
| `Step 6：寫入 task_scheduler.log` | 照做，無論前面成敗都必須寫 |

> 上表若與 `.claude/commands/news-pipeline-steps.md` 的實際步驟標題對不上（有標題被改名、或出現表中沒有的新步驟），**不要自行猜測略過**：照該檔實際內容執行，並在最終摘要標一行 `⚠️ runbook 步驟表與 news-pipeline-steps.md 不同步`，供使用者回頭修 runbook。

**Phase 劃分不適用於雲端：** `news-pipeline-steps.md` 與 `.claude/commands/news-pipeline.md` 把步驟分成 Phase A / B / C，那是為了本機 session 省 context 而拆的背景 agent 邊界。你是雲端頂層 session，**全部步驟自己一條龍做完，不 spawn 背景 agent 執行 pipeline 步驟**（記者派工除外，見下）。

---

## Wiki Ingest（上表的 Step 2）

完整步驟見 `.claude/commands/wiki-ingest.md`，照該檔執行：分類今日日報條目 → 平行派工六類記者 → 彙整 `wiki/feature-radar.md` / `wiki/index.md` / `wiki/log.md` / `data/source_attribution.jsonl`。

**派工注意：**
- 你是頂層 session，用 Task tool 派工會同步等待完成，不會有本機那個「巢狀背景通知迷路」的問題，可放心派
- 派工一律 `subagent_type: "general-purpose"` + `model: "sonnet"`，prompt 首段為角色前導（導向 `.claude/agents/wiki-reporter-[category].md`），格式照 `.claude/commands/wiki-ingest.md` 步驟 3。**這就是正典路徑，不是降級**——2026-08-15 起本機與雲端同一條路，不再需要在 log 標注「降級執行」（歷史：07-18～08-14 雲端無法載入自訂 `wiki-reporter-*` subagent_type，六次退回內嵌路徑；已裁決轉正，見 `.claude/rules/wiki-ingest.md`「派工方式」）

**失敗處理：** Step 2 整體失敗或部分記者失敗時，記錄錯誤但仍繼續後續步驟（web build 不依賴 wiki 完整性）。

---

## 完成後輸出摘要

- 待生成清單（哪幾個日期）與每個目標的新鮮度檢查結果（fresh / aborted，aborted 時附實際 date 與 items 數）
- 上表各步驟結果（OK / FAILED / SKIPPED）
- TARGET_DATE
- wiki ingest 記者回報中的異常
- 若 runbook 步驟表與來源檔不同步，附上 `⚠️` 那一行
