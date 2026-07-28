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
| 2026-07-25 週六 01:03 UTC 的 weekly-wiki-lint-cloud 觸發後**無聲失敗**（無 commit、無 log 紀錄、無 abort 證據，三個週更頁停在 07-18）——舊 prompt 的最後一次執行，死因不可考；本機補跑 `/wiki-lint` 恢復本週週更 | 薄殼＋runbook 架構（2026-07-25 上線）＋心跳紀錄（2026-07-27 補，`wiki-lint.md`「10. 收尾閉迴路」步驟 4）＋STARTED 開跑標記（2026-07-27 補，`_shared.md`「無人值守原則」）：08-01 首跑判定改為**四態**——`STARTED + OK 心跳`＝收斂；`STARTED + FAILED`＝失敗可追查；`STARTED 無後續`＝中途死（07-25 的死法，首次可診斷）；`完全無 STARTED`＝trigger 未觸發或環境起不來。另 08-01 為 8 月首次 lint，月度「外部死鏈」已在 runbook 明令雲端跳過（egress 封鎖會產生假死鏈），驗證時確認**沒有**大量「原文已失效」標註出現即為防護生效 | Claude（08-01 後首個 session） | 2026-08-01 | 🟡 待下週六驗證 |
| Reddit RSS 走 `sort=top&t=week` 加「· 週熱門」標記，wiki 視標記為達低門檻（RSS 天生無分數 → score 恆 0） | 設 Reddit OAuth 憑證（環境變數 `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET`）→ `reddit.py` OAuth 路徑取真實 `ups`；之後退役「週熱門」特例 | 使用者（reddit.com/prefs/apps 建 script app） | 2026-07-24 | 🟡 繞路中 |
| GitHub API 走匿名（60 req/hr、搜尋 10 req/min），GitHub Search 常撞限流回 0 | 設 GitHub PAT（環境變數 `GITHUB_TOKEN`，classic token 免勾 scope）→ 60/hr 升 5000/hr，`github_releases.py` 已備 Authorization 路徑 | 使用者（github.com Settings→Developer settings→Tokens classic） | 2026-08-10 | 🟡 繞路中（選配，非資料殘缺） |
| Blogroll RSS 名單已於 2026-07-11 確認上線（simonwillison / jessevincent / arminronacher / antirez，皆 probation）；煙霧測試 0 命中已診斷為 (a) 26h 窗內無 Claude/Anthropic 相關新文，非技術問題（4 個 feed HTTP 200、bozo=False、時間解析正常，Simon Willison 窗內僅 1 篇且與主題無關已正確被關鍵字擋下）。剩餘待辦：probation 首月觀察（汰換節奏已定：來源記分卡 2026-07-16 上線，每週隨 `/wiki-lint` 6e 執行，見 `docs/source-scoring-optimization.md`） | 30 天 probation 期滿（2026-08-11）後以記分卡數據檢視命中率決定去留 | 使用者 | 2026-08-11 | 🟡 繞路中 |
| news-pipeline-steps.md 新增 Step 3c 摘要忠實度自檢（2026-07-17），`/pipeline-change-check baseline` 已記錄（對照 07-16 digest）；依規定改後首次 pipeline 跑完須執行 `compare` 對照，尚未執行 | 下次 `/news-pipeline` 跑完後執行 `/pipeline-change-check compare`，確認指標無 ⚠️ 漂移即可移入已收斂 | Claude（下次 pipeline session） | 2026-07-19 | 🟡 待對照 |
| `data/external/domain_pc1.csv`（Lin et al. 2023 domain 信譽表）底層評級為 2022–2023 快照，新站查無資料落「未知」桶 | 每季複查：記分卡「未知」桶占比持續 > 30% 時重新下載上游（hauselin/domain-quality-ratings）或評估補充 idiap / Iffy Index 資料集 | Claude（隨 `/wiki-lint` 順檢） | 2026-10-16 | 🟡 繞路中（低風險，查無＝中性不懲罰） |
| 雲端 routine（cloud sandbox）環境預設無 `feedparser`/`sgmllib3k`（且 2026-07-22 本次另發現同一台環境連 `python-dotenv` 也未預裝，`main.py` 匯入鏈第一步就先撞這個）：`pip install -r src/requirements_news.txt` 因 `sgmllib3k` 用 `setup.py install` 觸發 Python 3.11 `distutils`／`setuptools` 相容性錯誤（`install_layout` AttributeError）導致 wheel build 失敗，使 `src/news_aggregator/main.py` 整條匯入鏈（`--confirm-digest`、`scripts/run_tests.py` 的 `test_blogroll`／`test_source_funnel`）失敗。2026-07-14 起每次雲端 routine 皆需重新用 `pip install python-dotenv` 補 dotenv、`pip download --no-deps sgmllib3k` 取原始碼、手動把 `sgmllib.py` 複製進 site-packages 繞過壞掉的 setup.py 安裝步驟；2026-07-22 本次再次確認：修法當次 session 內測試套件與 Step 1c 皆修復通過，但此修法是 session-local（容器回收後不持久），確認每次開新容器皆重新踩坑（已連續至少 5 次雲端 routine 執行復現：07-14、07-21、07-22、07-23、07-24；07-24 本次修法與前次相同，額外手動 `pip install python-dotenv` + 下載 sgmllib3k 原始碼複製 `sgmllib.py`，當次 session 內 `run_tests.py` 全數轉為通過）（已順延 1 次）。**2026-07-28 新增復現樣態：** `scripts/cloud_bootstrap.py` 本身已固化修法（把 `sgmllib.py` 放進頂層 site-packages），三個依賴皆回報「就緒」，但本次環境的 `feedparser` 版本為 6.0.13，其 `feedparser/sgml.py` 改成 `import feedparser.sgmllib as sgmllib`（要求套件**內部**有 `feedparser/sgmllib.py`），與頂層 `sgmllib` 模組是兩個不同路徑——舊修法對新版 feedparser 已失效，`--confirm-digest` 仍以 `ModuleNotFoundError: No module named 'feedparser.sgmllib'` 失敗。研判是 feedparser 上游版本漂移導致同一根因換了新症狀，非 `cloud_bootstrap.py` 邏輯本身退化。本次依 Step 1c 規則記警告後跳過（不影響已完成的 news commit），未嘗試修補 `cloud_bootstrap.py`——真解方向未變、且已明確指定由使用者決定，故不在雲端 routine 內自行變更腳本邏輯（已順延 2 次） | 需要環境層級的持久解，例如：(a) 雲端 sandbox 基礎映像預裝 `feedparser`（連同 `sgmllib3k`）與 `python-dotenv`、或 (b) repo 內建 SessionStart hook / setup script 自動執行本次的手動修法、或 (c) 上游改用不依賴 `sgmllib3k` 的 HTML 清理器取代 feedparser 內建的 legacy 解析路徑，徹底移除此依賴；若選 (a)/(b)，需同時處理 `cloud_bootstrap.py` 對新版 feedparser（6.0.13+）要求 `feedparser/sgmllib.py`（套件內部）而非頂層 `sgmllib` 模組的落差 | 使用者（決定要修環境映像或加 setup hook） | 2026-08-04 | 🔴 繞路中且已逾期 |
| 雲端 routine 的自訂 `subagent_type` 註冊表（`.claude/agents/wiki-reporter-*.md` 六份）未載入進 Agent tool，呼叫時回傳「Agent type not found」：已至少於 07-18、07-19、07-22、07-24 四次雲端 routine 執行中復現，每次皆改用 `general-purpose` agent 內嵌對應記者角色規則＋開始前必讀清單（讀 `wiki-reporter-shared.md` + 對應 `wiki-ingest-[category].md`）繞過，功能等同專職記者但需在派工 prompt 手動塞入完整規則路徑與邊界提醒，較原生 subagent_type 派工囉唆且容易遺漏細節 | 需要環境層級的持久解：確認雲端 routine 執行環境是否讀取專案層 `.claude/agents/` 目錄（可能是路徑掃描範圍或載入時機問題），或改為 repo 內建機制自動偵測並注入這六份 agent 定義 | 使用者（確認雲端 routine agent 註冊表載入機制） | 2026-07-29 | 🟡 繞路中 |

## 已收斂

- ✅ **每日新聞摘要「待驗證」項目正式收斂**（收斂於 2026-07-28）：2026-07-25 改版後首次雲端實跑（`news/2026-07-28.md`）驗證規格確實落地——📌 今日聚焦 5 條全數使用 `[N]` 編號（非行內 `（ref: ...)`）；`grep -cE '^\*\*\[.+\]\(https?://' news/2026-07-28.md` = 27（3a 自檢 ≥5）；來源狀態表 10 列（3b 自檢 ≥8，UTF-8 locale 下驗證）；「選材門檻」與「今日聚焦參考連結」皆位於 📡 來源狀態表格之後的檔尾附錄，順序與格式與規格逐字相符。判定 LLM 手動生成路徑穩定產出符合規格的輸出，不需回頭修 Step 1b 措辭。

- ✅ **雲端排程薄殼架構首跑驗證**（收斂於 2026-07-26）：07-25 13:02 UTC 首次真實執行四項驗收全過——(a) 日報產出且符合新 Step 1b 格式（6 個 [N] 編號引用＋檔尾參考清單）；(b) 有 `data: confirm emitted-cache 2026-07-25` commit；(c) `emitted_items.json` 當日確認率 66/66=100%（對比前一日 1/54）；(d) watchdog 首跑（run #1）於 07-26 以 origin 內容重算四項判準全綠、無 GitHub 失敗通知信。薄殼 trigger → runbook 執行路徑確認可用。

- ✅ **雲端 routine 無法 commit `task_scheduler.log`**（2026-07-25 雲端回報、同日收斂）：根目錄 `.gitignore` 的 `logs/`（無前導斜線）連帶忽略 `CLAUDE_NEWS/src/logs/`，而 runbook 明文要求該檔必須 commit + push。已改用「放行目錄 → 排除目錄內容 → 單獨放行 task_scheduler.log」三行寫法（git 規定父目錄被排除時無法單獨 re-include 子檔案），並以 `git check-ignore` 驗證三種情境：目標檔可加入、同目錄其他 log 仍忽略、其他專案的 logs/ 仍忽略。雲端不再需要 `git add -f`。

- ✅ **「每日新聞摘要呈現優化」第一波接回真實生成路徑**（收斂於 2026-07-25，原登記 2026-07-24，複查日 2026-08-07 提前完成）：`.claude/commands/news-pipeline-steps.md` Step 1b 的日報格式規格已改為與 `digest.py::reformat_presentation()` 輸出一致——📌 今日聚焦區塊改用 `[N]` 編號引用（不再是行內 `（ref: URL）`），選材門檻說明與「今日聚焦參考連結」清單移到 📡 來源狀態表格之後的檔尾附錄，並附上完整範例供 LLM 手動生成時照抄格式。`python scripts/run_tests.py`（含 `check_rules.py` 全部同步配對）與 `/review-commands` 皆零錯誤。因規格是給 LLM 手動生成用（非確定性腳本），另登記一列「待驗證」追蹤下次實跑輸出是否確實照規格產出。
- ✅ **每日自動化分裂架構首跑驗證**（2026-07-15 提前收斂於 2026-07-14）：雲端 routine `daily-news-pipeline-cloud`（trig_01AWf2wwmVeL3ykPCSyxyvzw）於 2026-07-14 13:00 UTC 首次真正排程執行，成功產出完整 4 筆 commit（`news: daily digest 2026-07-14` → `wiki: auto-ingest 2026-07-14`（分兩次 commit，因執行中 Stop hook 觸發中繼 commit）→ `web: rebuild 2026-07-14`）並統一 push（`1b90dfb..8b6793e`）。分裂架構（① GH Actions 抓料 + ② 雲端 routine 產 news/wiki/web）確認穩定跑通，根因修復生效。
