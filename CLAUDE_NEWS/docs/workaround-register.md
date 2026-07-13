# Workaround 登記表

每上一個 workaround（繞路而非真解）就在此登記一列，避免繞路悄悄變永久（見根目錄 `CLAUDE.md`「完工定義」第 3 條）。
`scripts/open_loops.py` 每週讀此表，**逾「複查日」仍在「進行中」的列**會被列出提醒。

## 使用規則

- **上 workaround 時當場新增一列**到「進行中」（繞路內容 / 真解 / owner / 複查日 / 狀態）
- **複查日** = 預期能上真解的日期；到期未解就順延並在狀態欄記一次「（已順延 N 次）」
- **拿到真解後**：把該列移到「已收斂」區並標 ✅ 與收斂日；git history 留存原繞路
- 狀態符號：🟡 繞路中 ／ 🔴 繞路中且已逾期 ／ ✅ 已上真解

## 進行中

| 繞路內容 | 真解 | owner | 複查日 | 狀態 |
|---|---|---|---|---|
| Reddit RSS 走 `sort=top&t=week` 加「· 週熱門」標記，wiki 視標記為達低門檻（RSS 天生無分數 → score 恆 0） | 設 Reddit OAuth 憑證（環境變數 `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET`）→ `reddit.py` OAuth 路徑取真實 `ups`；之後退役「週熱門」特例 | 使用者（reddit.com/prefs/apps 建 script app） | 2026-07-24 | 🟡 繞路中 |
| GitHub API 走匿名（60 req/hr、搜尋 10 req/min），GitHub Search 常撞限流回 0 | 設 GitHub PAT（環境變數 `GITHUB_TOKEN`，classic token 免勾 scope）→ 60/hr 升 5000/hr，`github_releases.py` 已備 Authorization 路徑 | 使用者（github.com Settings→Developer settings→Tokens classic） | 2026-08-10 | 🟡 繞路中（選配，非資料殘缺） |
| 每日自動化分裂架構（GH Actions 抓料 + 雲端 routine 做 LLM，見 `docs/daily-automation.md`）**07-11、07-12 連兩天失敗，根因不同**：07-11 是 GitHub Actions scheduled workflow 延遲 1.5–2.7 小時實跑，30 分鐘緩衝不足，雲端 routine 新鮮度防線正確中止；已將 cron 提早至 10:00 UTC、緩衝拉大為 3 小時。07-12 該次修復後 gather 排程準時於 11:16 UTC 執行且 job 顯示全步驟成功，但**未產出任何 commit**（無 `data: daily gather` commit），雲端 routine 端當日也無任何產出痕跡（無 digest/ingest commit）；受限於匿名 API 無法讀取完整 Python log，尚未確認是抓料腳本邏輯 bug（誤判無資料差異）或雲端 routine 未觸發。兩天皆已本機 `/news-pipeline` 補跑並補推 | 需使用者登入 GitHub 查看該次 run 的 "Gather news" 步驟完整輸出（確認是否真的 0 新增條目）＋查看 claude.ai routines 頁確認雲端 routine 07-12 13:00 UTC 是否觸發；兩者皆此工具無法觸及 | 使用者（看 Actions 頁完整 log + routines 頁 + 網站，2026-07-13 起連續觀察） | 2026-07-14 | 🔴 繞路中且已逾期風險（連兩天失敗，緩衝加大未解決 07-12 這類根因） |
| Blogroll RSS 名單已於 2026-07-11 確認上線（simonwillison / jessevincent / arminronacher / antirez，皆 probation）；煙霧測試 0 命中已診斷為 (a) 26h 窗內無 Claude/Anthropic 相關新文，非技術問題（4 個 feed HTTP 200、bozo=False、時間解析正常，Simon Willison 窗內僅 1 篇且與主題無關已正確被關鍵字擋下）。剩餘待辦：`/source-review` 汰換節奏未定＋probation 首月觀察 | `/source-review` skill 節奏（週更或按需）待定案後補進 CLAUDE.md skills 表；30 天 probation 期滿後檢視命中率決定去留 | 使用者 | 2026-08-11 | 🟡 繞路中 |

## 已收斂

（空）
