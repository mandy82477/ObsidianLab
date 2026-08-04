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
| **GitHub Search 成長偵測器的歷史存量盲區**（2026-08-04 改版附帶）：B 穿越窗升冪只接得住「今後剛越過 500 星」的 repo；改版前已越線、卡在 500..3000 帶中段的存量（如觸發此次改版的 claude-workflow-v2 本身，1.4k 星）永不進窗。該 repo 已人工收錄，其餘存量未盤點 | 下次 `/wiki-lint` 時社群記者做**一次性**分頁掃描（`claude-code stars:500..3000 pushed:>30d` 等三個 scope，per_page=100 全撈），對照 tools 頁去重後按互動門檻表（星）人工策展；做完此列即收斂，日後靠 B 窗常態接手 | Claude（下次 `/wiki-lint` session） | 2026-08-08 | 🟡 待一次性掃描 |
| **pipeline-change-check compare 待跑**（2026-08-04 GitHub Search 改版）：baseline 已記（`src/logs/pipeline_baseline.json`，對照 2026-08-01 digest）；改版後首次 pipeline (雲端 08-04 13:00 UTC 或本機) 跑完須執行 `/pipeline-change-check compare` 對照，特別留意 GitHub 來源 count 是否脫離連續 4 日 0 的狀態、以及首日湧入量 | 跑 compare 確認無 ⚠️ 漂移即移入已收斂 | Claude（下次 pipeline 後的 session） | 2026-08-06 | 🟡 待對照 |
| **記者間「轉知」標記無接手驗收機制**：2026-08-01 第二次月度聚焦校準發現，session/cache 跨帳號洩漏疑慮（#74066，06-29~07-05 週）在日誌中兩度被標「轉知安全政策記者」「下次併入 ai-agent-safety」，但 30 天內 `wiki/topics/ai-agent-safety.md` 查無任何記錄——**轉知＝發出即忘，無人驗收**。現行繞路：靠月度聚焦校準事後抽查才會發現（30 天延遲，且只覆蓋當週聚焦條目） | 讓「⚠️ 需主編轉知」成為可追蹤項而非一次性字串：主編彙整時把每筆轉知寫入 `wiki/log.md` 當次 ingest 紀錄的獨立欄位，並由 `/wiki-lint` 每週掃描「近 14 天曾轉知但目標頁面無對應更新」的殘留項；規則落點 `.claude/rules/wiki-ingest.md` 第三步 + `.claude/commands/wiki-lint.md` | Claude（下次 `/wiki-lint` session 設計並實作掃描步驟） | 2026-08-08 | 🟡 繞路中 |
| Reddit RSS 走 `sort=top&t=week` 加「· 週熱門」標記，wiki 視標記為達低門檻（RSS 天生無分數 → score 恆 0） | 設 Reddit OAuth 憑證（環境變數 `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET`）→ `reddit.py` OAuth 路徑取真實 `ups`；之後退役「週熱門」特例 | 使用者（reddit.com/prefs/apps 建 script app） | 2026-07-24 | 🟡 繞路中 |
| GitHub API 走匿名（60 req/hr、搜尋 10 req/min），GitHub Search 常撞限流回 0 | 設 GitHub PAT（環境變數 `GITHUB_TOKEN`，classic token 免勾 scope）→ 60/hr 升 5000/hr，`github_releases.py` 已備 Authorization 路徑 | 使用者（github.com Settings→Developer settings→Tokens classic） | 2026-08-10 | 🟡 繞路中（選配，非資料殘缺） |
| Blogroll RSS 名單已於 2026-07-11 確認上線（simonwillison / jessevincent / arminronacher / antirez，皆 probation）；煙霧測試 0 命中已診斷為 (a) 26h 窗內無 Claude/Anthropic 相關新文，非技術問題（4 個 feed HTTP 200、bozo=False、時間解析正常，Simon Willison 窗內僅 1 篇且與主題無關已正確被關鍵字擋下）。剩餘待辦：probation 首月觀察（汰換節奏已定：來源記分卡 2026-07-16 上線，每週隨 `/wiki-lint` 6e 執行，見 `docs/source-scoring-optimization.md`） | 30 天 probation 期滿（2026-08-11）後以記分卡數據檢視命中率決定去留 | 使用者 | 2026-08-11 | 🟡 繞路中 |
| news-pipeline-steps.md 新增 Step 3c 摘要忠實度自檢（2026-07-17），`/pipeline-change-check baseline` 已記錄（對照 07-16 digest）；依規定改後首次 pipeline 跑完須執行 `compare` 對照，尚未執行 | 下次 `/news-pipeline` 跑完後執行 `/pipeline-change-check compare`，確認指標無 ⚠️ 漂移即可移入已收斂 | Claude（下次 pipeline session） | 2026-07-19 | 🟡 待對照 |
| `data/external/domain_pc1.csv`（Lin et al. 2023 domain 信譽表）底層評級為 2022–2023 快照，新站查無資料落「未知」桶 | 每季複查：記分卡「未知」桶占比持續 > 30% 時重新下載上游（hauselin/domain-quality-ratings）或評估補充 idiap / Iffy Index 資料集 | Claude（隨 `/wiki-lint` 順檢） | 2026-10-16 | 🟡 繞路中（低風險，查無＝中性不懲罰） |
| 雲端 routine 的自訂 `subagent_type` 註冊表（`.claude/agents/wiki-reporter-*.md` 六份）未載入進 Agent tool，呼叫時回傳「Agent type not found」：已至少於 07-18、07-19、07-22、07-24 四次雲端 routine 執行中復現，每次皆改用 `general-purpose` agent 內嵌對應記者角色規則＋開始前必讀清單（讀 `wiki-reporter-shared.md` + 對應 `wiki-ingest-[category].md`）繞過，功能等同專職記者但需在派工 prompt 手動塞入完整規則路徑與邊界提醒，較原生 subagent_type 派工囉唆且容易遺漏細節 | 需要環境層級的持久解：確認雲端 routine 執行環境是否讀取專案層 `.claude/agents/` 目錄（可能是路徑掃描範圍或載入時機問題），或改為 repo 內建機制自動偵測並注入這六份 agent 定義 | 使用者（確認雲端 routine agent 註冊表載入機制） | 2026-07-29 | 🟡 繞路中 |

## 已收斂

- ✅ **雲端 sandbox 缺 `feedparser`／`sgmllib3k` 依賴鏈**（登記於 2026-07-14，收斂於 2026-08-01，期間復現至少 9 次、順延 4 次）：**根因已由上游移除，不是我們繞過去的。** 2026-08-01 查證 PyPI，`feedparser` 6.0.14 的 `requires_dist` 已從壞掉的 `sgmllib3k`（用 `setup.py install`、Python 3.11 撞 distutils `install_layout` AttributeError）換成 `feedparser-sgmllib>=2,<3`——後者是純 python wheel、無依賴、`requires_python >=3.10`，`pip install` 一次到位。即登記表原列的真解方向 (c)「上游移除 sgmllib3k 依賴」已由 feedparser 自己完成。

  **為什麼拖到現在才發現：** `cloud_bootstrap.py` 當初為了躲開壞掉的 sgmllib3k 而用 `pip install --no-deps`，這個旗標同時也讓 pip **永遠看不到上游換掉依賴**——workaround 親手擋掉了自己的退場路徑。四次復現（07-28 套件內路徑、07-31 獨立套件路徑、08-01 週度 lint、08-01 日更）每次都在補新症狀，沒有人回頭問「上游是不是已經修好了」。教訓：**長期繞路必須定期回頭查上游狀態，而不是只在它又炸的時候補洞**；凡是為了繞開壞依賴而加的 `--no-deps`／`--ignore-installed` 類旗標，都應視為「會遮蔽上游修復」的高風險項，登記時一併註明複查方式。

  **修法：** `cloud_bootstrap.py` 移除 `--no-deps`、鎖 `feedparser>=6.0.14` 讓 pip 正常解析依賴；`verify_feedparser_import()` 直接驗 `import feedparser.sgml` 成功才回報就緒（前三次都是 bootstrap 說就緒、實際仍炸）；手動 vendoring 修法降級為離線退路（退路二），另補退路一處理「環境預裝舊版 feedparser 而不觸發安裝」。`src/requirements_news.txt` 同步鎖 `feedparser>=6.0.14`。

  **驗證（乾淨 venv 三情境）：** ① 全新空環境 → 正常裝完、import 驗證通過，完全不需要 vendoring；② 預裝 `--no-deps feedparser==6.0.13`（07-31 現場重現）→ 精準重現 `ModuleNotFoundError: No module named 'feedparser.sgmllib'`，退路一升版後自動修復；③ 同環境重跑 → 全部跳過，冪等。另 `run_tests.py` 144 案例全過。

- ✅ **每日新聞摘要「待驗證」項目正式收斂**（收斂於 2026-07-28）：2026-07-25 改版後首次雲端實跑（`news/2026-07-28.md`）驗證規格確實落地——📌 今日聚焦 5 條全數使用 `[N]` 編號（非行內 `（ref: ...)`）；`grep -cE '^\*\*\[.+\]\(https?://' news/2026-07-28.md` = 27（3a 自檢 ≥5）；來源狀態表 10 列（3b 自檢 ≥8，UTF-8 locale 下驗證）；「選材門檻」與「今日聚焦參考連結」皆位於 📡 來源狀態表格之後的檔尾附錄，順序與格式與規格逐字相符。判定 LLM 手動生成路徑穩定產出符合規格的輸出，不需回頭修 Step 1b 措辭。

- ✅ **雲端排程薄殼架構首跑驗證**（收斂於 2026-07-26）：07-25 13:02 UTC 首次真實執行四項驗收全過——(a) 日報產出且符合新 Step 1b 格式（6 個 [N] 編號引用＋檔尾參考清單）；(b) 有 `data: confirm emitted-cache 2026-07-25` commit；(c) `emitted_items.json` 當日確認率 66/66=100%（對比前一日 1/54）；(d) watchdog 首跑（run #1）於 07-26 以 origin 內容重算四項判準全綠、無 GitHub 失敗通知信。薄殼 trigger → runbook 執行路徑確認可用。

- ✅ **雲端 routine 無法 commit `task_scheduler.log`**（2026-07-25 雲端回報、同日收斂）：根目錄 `.gitignore` 的 `logs/`（無前導斜線）連帶忽略 `CLAUDE_NEWS/src/logs/`，而 runbook 明文要求該檔必須 commit + push。已改用「放行目錄 → 排除目錄內容 → 單獨放行 task_scheduler.log」三行寫法（git 規定父目錄被排除時無法單獨 re-include 子檔案），並以 `git check-ignore` 驗證三種情境：目標檔可加入、同目錄其他 log 仍忽略、其他專案的 logs/ 仍忽略。雲端不再需要 `git add -f`。

- ✅ **「每日新聞摘要呈現優化」第一波接回真實生成路徑**（收斂於 2026-07-25，原登記 2026-07-24，複查日 2026-08-07 提前完成）：`.claude/commands/news-pipeline-steps.md` Step 1b 的日報格式規格已改為與 `digest.py::reformat_presentation()` 輸出一致——📌 今日聚焦區塊改用 `[N]` 編號引用（不再是行內 `（ref: URL）`），選材門檻說明與「今日聚焦參考連結」清單移到 📡 來源狀態表格之後的檔尾附錄，並附上完整範例供 LLM 手動生成時照抄格式。`python scripts/run_tests.py`（含 `check_rules.py` 全部同步配對）與 `/review-commands` 皆零錯誤。因規格是給 LLM 手動生成用（非確定性腳本），另登記一列「待驗證」追蹤下次實跑輸出是否確實照規格產出。
- ✅ **每日自動化分裂架構首跑驗證**（2026-07-15 提前收斂於 2026-07-14）：雲端 routine `daily-news-pipeline-cloud`（trig_01AWf2wwmVeL3ykPCSyxyvzw）於 2026-07-14 13:00 UTC 首次真正排程執行，成功產出完整 4 筆 commit（`news: daily digest 2026-07-14` → `wiki: auto-ingest 2026-07-14`（分兩次 commit，因執行中 Stop hook 觸發中繼 commit）→ `web: rebuild 2026-07-14`）並統一 push（`1b90dfb..8b6793e`）。分裂架構（① GH Actions 抓料 + ② 雲端 routine 產 news/wiki/web）確認穩定跑通，根因修復生效。
