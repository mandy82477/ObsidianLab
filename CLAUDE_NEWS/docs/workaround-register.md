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
| 每日自動化分裂架構（GH Actions 抓料 + 雲端 routine 做 LLM，見 `docs/daily-automation.md`）**根因已於 2026-07-13 確定**：② 雲端 routine `daily-news-pipeline-cloud` 從未被實際建立——用 `RemoteTrigger list` 查詢，文件記載的 trigger ID `trig_01JNrBGyrsZk1HjBQeJ7UKLG` 根本不存在（使用者本人到 claude.ai routines 頁確認「看起來沒有排」）。① GH Actions 抓料本身正常（07-12 已用完整 CI log 核對：58→34 則、`e18b02d` 於 11:18 UTC 正常 push），07-11/07-12 未自動生日報單純是②從頭到尾沒有排程在跑，不是延遲或中止。已於 2026-07-13 15:15 UTC 用 `RemoteTrigger create` 重新建立（trig_01AWf2wwmVeL3ykPCSyxyvzw，cron `0 13 * * *`，含新鮮度防線 prompt），兩天皆已本機 `/news-pipeline` 補跑補推 | 已建立正確排程，待觀察 2026-07-14 13:00 UTC 首次真正執行是否成功產出 news/wiki/web 三段 commit；若當天仍無產出，需再查 routine 執行紀錄本身（權限/環境/prompt 問題） | 使用者（2026-07-14 起看 master 是否出現 `news: daily digest 2026-07-14` 等 3-4 筆 commit） | 2026-07-15 | 🟡 繞路中（根因已修復並重建排程，待驗證首跑是否穩定） |
| Blogroll RSS 名單已於 2026-07-11 確認上線（simonwillison / jessevincent / arminronacher / antirez，皆 probation）；煙霧測試 0 命中已診斷為 (a) 26h 窗內無 Claude/Anthropic 相關新文，非技術問題（4 個 feed HTTP 200、bozo=False、時間解析正常，Simon Willison 窗內僅 1 篇且與主題無關已正確被關鍵字擋下）。剩餘待辦：`/source-review` 汰換節奏未定＋probation 首月觀察 | `/source-review` skill 節奏（週更或按需）待定案後補進 CLAUDE.md skills 表；30 天 probation 期滿後檢視命中率決定去留 | 使用者 | 2026-08-11 | 🟡 繞路中 |

## 已收斂

（空）
