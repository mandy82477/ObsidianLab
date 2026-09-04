# .claude/rules/wiki-ingest-format.md 沿革（教訓存檔）

本檔是 `.claude/rules/wiki-ingest-format.md` 的歷史敘事，不是待執行規則；條文處的「沿革檔 YYYY-MM-DD[ 字母]」皆指本檔對應段。考古鏈：`[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

本檔是**歷史敘事，不是待執行規則**——條文已在上方，建頁或格式審查時不必讀本檔。存放於此的原因：條文本身已能獨立執行，敘事只在有人想問「為什麼有這條」時才需要。考古鏈為 `[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

**2026-07-26**（建頁必須登記觸發邊）：`community-large-codebase-workflow` 建頁時未登記觸發邊，僅靠「領域＝🌐 社群」概括條款覆蓋（所有權≠會被更新），孤兒化 10 天——patterns 持續進節點、主線零縫合；補上 daily 小縫後又因記者每天只看一個節點、只能往段尾加句，兩週把綜合頁長回 log，2026-08-15 改為 daily 標 tag＋weekly 整線重寫。

**2026-08-08 A**（懸置標記語法的由來）：跨 session 訊息互通條目標了「未經官方確認」並寫著「後續 ingest 若查得官方一手來源應更新」——那句話沒有任何流程會去讀，條目掛到使用者親自問起才被發現，而官方文件從第一天就存在。

**2026-08-08 B**（不得寫「至今無後續」）：pricing 旗艦計費分界懸置 20 天，每天誠實回報「至今無後續」20 次。

**2026-08-10**（樞紐頁 wikilink 不具偵測力）：`[[entities/claude-code]]` 單獨一個探針曾讓任何標題含「Claude Code」的條目都誤判命中。

**2026-08-13**（蒐集邊界欄位）：`topics/ai-talent-flow` 自述「追蹤 AI 前沿實驗室**之間**的人才流動」，但 pipeline 結構上只收得到標題提及 Claude/Anthropic 的那一半。2026-08-05 Jeff Dean 等四人離開 Google 創辦 Discovery Loop——該主題史上最大事件——12 個來源零命中、漏 8 天，而讀者從頁面看不出有這個缺口。

**2026-08-28**（別名欄位）：terminology drift（同物多名造成搜尋與連結失準）是 LLM wiki 的已知失效模式，canonical name＋別名是標準解。

**2026-09-03**（先蒸餾再談拆分）：量測 patterns 1,786 行中 1,087 行是早該蒸餾的舊月份。

**2026-09-04**（蒸餾契約全站泛化）：原契約寫在社群 lint 檔裡，於是 `ai-agent-safety`（1,257 行）、`anthropic-government-policy`（705 行）、`competitor-landscape`（663 行）、`anthropic-business`、`claude-code`、`pricing`、各人物頁的歷史記錄**結構上沒有封存路徑**——不是誰疏忽，是契約住在一個只有社群記者會讀的檔案裡。

**更新頻率欄位（選填）`[加入: 2026-07-16，改版: 2026-07-28]`**：非每日維護的頁面（週更／lint 專用）在標頭「領域」之後加一行 `**更新頻率：** 🗓️ 週更（讀者導向的節奏說明）`，並在 `wiki/index.md` 對應摘要前綴「🗓️ 週更」——向讀者說明日期停留是設計而非漏更新。補充說明用讀者語言（如「每週策展一次；更新日期停留數天屬正常節奏」），**不得出現 `/wiki-lint`、ingest 等內部指令名**（此欄位會原樣顯示在網站詳頁標頭）。每日維護頁**不加**此欄。目前適用：`wiki/overview.md`、`wiki/topics/community-pattern-trends.md`、`wiki/topics/community-tech-tools.md`、`wiki/topics/model-task-leaderboard.md`、`wiki/topics/community-large-codebase-workflow.md`；日後新增週更頁時比照。
