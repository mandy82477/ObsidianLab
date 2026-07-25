# 雲端 routine：每日新聞 pipeline（daily-news-pipeline-cloud）

`[建立: 2026-07-25]`

**先讀 `docs/cloud-runbooks/_shared.md`**（環境覆寫、收尾閉迴路、無人值守原則），再照本檔執行。

你執行的是「GitHub Actions 抓料 + 雲端 routine 做 LLM」分裂架構的**第二段**（架構全貌見 `docs/daily-automation.md`）。第一段（抓新聞）已由 GitHub Actions 完成並把資料 commit 進 repo，**你不重複抓料**——雲端 egress 被封鎖，抓也抓不到。

TARGET_DATE = `date -u +%F`。

---

## 前置閘與失敗處理：不在本檔

`Step 0b：冪等閘`（日報已存在則中止）、`Step 1b` 開頭的新鮮度防線（資料非目標日期則中止）、以及 `Step 5` 的 push 失敗重試，全部定義在 `.claude/commands/news-pipeline-steps.md`，**本機與雲端行為完全相同**，照該檔執行即可。

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
| `Step 0：昨日缺跑檢查` | 照做（TARGET_DATE 為今日，不是 backfill 模式） |
| `Step 0b：冪等閘` | 照做（TARGET_DATE 為今日，非 backfill，所以「日報已存在」一律中止） |
| `Step 1a：新聞抓取` | **跳過**——GitHub Actions 已完成，`gathered_items.json` 已存在（新鮮度由 Step 1b 開頭的防線把關） |
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
- 派工帶 `model: "sonnet"`
- **若 `wiki-reporter-*` 這六個自訂 subagent_type 在雲端環境無法解析**（歷史上發生過：2026-07-18 雲端 ingest 因 subagent 註冊表未載入而 fallback），改用 `general-purpose` agent 並在 prompt 內嵌對應的 `.claude/rules/wiki-ingest-[類別].md` 與 `.claude/rules/wiki-reporter-shared.md` 規則，功能等同。**但這屬於降級執行，必須在最終摘要與 `wiki/log.md` 本次紀錄中明確標注**，不可靜默 fallback

**失敗處理：** Step 2 整體失敗或部分記者失敗時，記錄錯誤但仍繼續後續步驟（web build 不依賴 wiki 完整性）。

---

## 完成後輸出摘要

- 新鮮度檢查結果（fresh / aborted，aborted 時附實際 date 與 items 數）
- 上表各步驟結果（OK / FAILED / SKIPPED）
- TARGET_DATE
- 記者是否降級為 general-purpose（是 / 否）
- wiki ingest 記者回報中的異常
- 若 runbook 步驟表與來源檔不同步，附上 `⚠️` 那一行
