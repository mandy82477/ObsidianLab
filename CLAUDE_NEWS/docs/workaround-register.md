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
| Blogroll RSS 名單已於 2026-07-11 確認上線（simonwillison / jessevincent / arminronacher / antirez，皆 probation）；煙霧測試 0 命中已診斷為 (a) 26h 窗內無 Claude/Anthropic 相關新文，非技術問題（4 個 feed HTTP 200、bozo=False、時間解析正常，Simon Willison 窗內僅 1 篇且與主題無關已正確被關鍵字擋下）。剩餘待辦：probation 首月觀察（汰換節奏已定：來源記分卡 2026-07-16 上線，每週隨 `/wiki-lint` 6e 執行，見 `docs/source-scoring-optimization.md`） | 30 天 probation 期滿（2026-08-11）後以記分卡數據檢視命中率決定去留 | 使用者 | 2026-08-11 | 🟡 繞路中 |
| news-pipeline-steps.md 新增 Step 3c 摘要忠實度自檢（2026-07-17），`/pipeline-change-check baseline` 已記錄（對照 07-16 digest）；依規定改後首次 pipeline 跑完須執行 `compare` 對照，尚未執行 | 下次 `/news-pipeline` 跑完後執行 `/pipeline-change-check compare`，確認指標無 ⚠️ 漂移即可移入已收斂 | Claude（下次 pipeline session） | 2026-07-19 | 🟡 待對照 |
| 「每日新聞摘要呈現優化」第一波（2026-07-24）在 `digest.py::reformat_presentation()` 完整實作了 ref 連結編號化＋選材門檻下沉，`build_web.py` 也已相容新舊兩種格式（皆有 fixture round-trip 測試佐證）；但發現 `digest.py` 的 `render()`/`analyze()` 路徑在目前 production pipeline 中實際上是死碼——真正的每日日報由 `news-pipeline-steps.md` Step 1b 的手動 prompt 規格產生（commit message 逐字相符可證），該規格本身沒有同步這兩項優化。在規格更新前，真實每日日報會繼續維持舊格式，兩項優化不會自動生效 | 更新 `news-pipeline-steps.md` Step 1b 的日報格式規格（📌 今日聚焦排版段落）比照 `digest.py::reformat_presentation()` 的輸出（`[N]` 編號引用＋檔尾參考清單、選材門檻移到檔尾），改完跑 `/review-commands` 確認同步 | 使用者／主 session（是否／何時做此規格更新，屬於超出 wave 1「Python 層」範圍的決策） | 2026-08-07 | 🟡 繞路中 |
| `data/external/domain_pc1.csv`（Lin et al. 2023 domain 信譽表）底層評級為 2022–2023 快照，新站查無資料落「未知」桶 | 每季複查：記分卡「未知」桶占比持續 > 30% 時重新下載上游（hauselin/domain-quality-ratings）或評估補充 idiap / Iffy Index 資料集 | Claude（隨 `/wiki-lint` 順檢） | 2026-10-16 | 🟡 繞路中（低風險，查無＝中性不懲罰） |
| 雲端 routine（cloud sandbox）環境預設無 `feedparser`/`sgmllib3k`：`pip install -r src/requirements_news.txt` 因 `sgmllib3k` 用 `setup.py install` 觸發 Python 3.11 `distutils`／`setuptools` 相容性錯誤（`install_layout` AttributeError）導致 wheel build 失敗，使 `src/news_aggregator/main.py` 整條匯入鏈（`--confirm-digest`、`scripts/run_tests.py` 的 `test_blogroll`／`test_source_funnel`）失敗。2026-07-14 本次雲端 routine 已用 `pip download --no-deps sgmllib3k` 取原始碼、手動把 `sgmllib.py` 複製進 site-packages 繞過壞掉的 setup.py 安裝步驟，當次 session 內測試套件與 Step 1c 皆已修復通過；但此修法是 session-local（容器回收後不持久），下次雲端 routine 開新容器大機率會重新踩坑 | 需要環境層級的持久解，例如：(a) 雲端 sandbox 基礎映像預裝 `feedparser`（連同 `sgmllib3k`）、或 (b) repo 內建 SessionStart hook / setup script 自動執行本次的手動修法、或 (c) 上游改用不依賴 `sgmllib3k` 的 HTML 清理器取代 feedparser 內建的 legacy 解析路徑，徹底移除此依賴 | 使用者（決定要修環境映像或加 setup hook） | 2026-07-21 | 🟡 繞路中 |

## 已收斂

- ✅ **每日自動化分裂架構首跑驗證**（2026-07-15 提前收斂於 2026-07-14）：雲端 routine `daily-news-pipeline-cloud`（trig_01AWf2wwmVeL3ykPCSyxyvzw）於 2026-07-14 13:00 UTC 首次真正排程執行，成功產出完整 4 筆 commit（`news: daily digest 2026-07-14` → `wiki: auto-ingest 2026-07-14`（分兩次 commit，因執行中 Stop hook 觸發中繼 commit）→ `web: rebuild 2026-07-14`）並統一 push（`1b90dfb..8b6793e`）。分裂架構（① GH Actions 抓料 + ② 雲端 routine 產 news/wiki/web）確認穩定跑通，根因修復生效。
