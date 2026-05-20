# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 專案概述

這個 repo 有兩個獨立部分：

1. **`news_aggregator/`** — Python 爬蟲，每日自動抓取 Claude / Anthropic 相關新聞，寫出 `news/YYYY-MM-DD.md`
2. **`wiki/`** — LLM 維護的知識庫，從日報萃取並整理成結構化頁面

完整流程圖見 `src/DesignDocument/Design Diagram.md`。

---

## 快速上手（首次設定）

### 步驟 1：安裝 Python 依賴

```bash
pip install -r src/requirements_news.txt
```

### 步驟 2：建立 `.env` 設定 API 金鑰

在 repo 根目錄建立 `.env` 檔案：

```
ANTHROPIC_API_KEY=sk-ant-...   # 必要：用於 LLM 過濾與摘要
GITHUB_TOKEN=ghp_...           # 建議：用於 GitHub Releases + Repo Search，提高 rate limit
REDDIT_CLIENT_ID=...           # 可選：啟用 Reddit 來源
REDDIT_CLIENT_SECRET=...
```

`ANTHROPIC_API_KEY` 若未設定，會自動退回使用本機 `claude` CLI（需登入 Claude.ai Pro）。

### 步驟 3：手動執行一次確認正常

```bash
cd src
python -m news_aggregator.main
```

執行完成後應看到 `news/YYYY-MM-DD.md` 被寫出，並自動 git commit & push（含 `seen_urls.json`）。

### 步驟 4：設定 Windows 工作排程器（自動化）

用 Windows 工作排程器每天定時執行 `src/run_news.bat`，建議時間為每日 08:00。
`run_news.bat` 會依序執行四個步驟（詳見下方）。

執行日誌：
- `src/logs/task_scheduler.log` — 完整 pipeline 日誌
- `src/logs/news_aggregator.log` — 聚合器詳細日誌

---

## 每日自動化流程

`run_news.bat` 每天自動執行完整流程（含 `claude -p` wiki ingest）。`/news-pipeline` 為互動式等效指令，wiki ingest 由 Claude 直接在 session 內執行（不走 `claude -p`，不產生 6/15 後的額外計費）。

```
每天 08:00（Windows 排程器，run_news.bat）
  ├─ Step 1  Python 聚合器 → news/YYYY-MM-DD.md + seen_urls.json → git push
  ├─ Step 2  claude -p "/wiki-ingest" → 更新 wiki/entities/、wiki/topics/、wiki/log.md、wiki/index.md
  ├─ Step 3  git add wiki/ → commit "wiki: auto-ingest YYYY-MM-DD" → git push
  └─ Step 4  python scripts/build_web.py → 更新 web_reader/data/data.js → commit "web: rebuild YYYY-MM-DD" → git push

手動（互動式 Claude Code，/news-pipeline）
  └─ 同上 5 步，但 Step 2 由 Claude 直接執行（不走 claude -p）

每週（手動）
  └─ 告訴 Claude：「執行 wiki lint 並更新 overview.md」
```

### 手動觸發 Wiki Ingest

若需要補跑（例如排程失敗、或日報重新抓取後想更新 wiki）：

```
/wiki-ingest
```

或指定日期：

```
請根據 news/2026-04-27.md 執行每日 ingest，更新 wiki。
```

### 每週 Wiki Lint 指令範例

```
請執行 wiki lint：找出矛盾頁面、孤立頁面、過期 ongoing 議題，並更新 wiki/overview.md。
```

---

## 聚合器 Pipeline 架構

程式碼位於 `src/news_aggregator/`，執行日誌在 `src/logs/`。

```
sources/*.py  →  dedup.py  →  enricher.py  →  filter.py  →  analyzer.py  →  digest.py  →  git_push.py
```

| 模組 | 職責 |
|------|------|
| `sources/base.py` | `FeedItem` dataclass + `BaseSource` ABC |
| `sources/anthropic_blog.py` | Anthropic 官方 Blog RSS |
| `sources/github_releases.py` | 官方 Releases（3 個 repo）+ GitHub Search API 搜尋過去 26h 內新建的社群工具 repo |
| `sources/hackernews.py` | Story 搜尋（score ≥ 3）+ Show HN 搜尋（score ≥ 1，捕捉剛發布的工具） |
| `sources/reddit.py` | r/ClaudeAI、r/artificial、r/MachineLearning、r/LocalLLaMA |
| `sources/google_news.py` | Google News RSS，查詢 `"Claude Code"` / `"Anthropic AI"` / `"Anthropic Claude"` / `"Claude API"` / `"MCP server Anthropic"` |
| `sources/devto.py` | dev.to RSS，tag：`#claudecode`、`#anthropic`、`#claudeai` |
| `dedup.py` | URL 正規化去重 + 模糊標題去重（threshold 0.85）；官方來源優先；維護 `seen_urls.json` |
| `enricher.py` | 用 trafilatura 抓原文補充 `summary` 欄位（最多 600 字） |
| `filter.py` | 呼叫 Claude Haiku 批次評分 1–5，丟棄 < 3 分；無 API key 則退回 claude CLI，再退回保留全部 |
| `analyzer.py` | 呼叫 Claude 產生繁體中文 Markdown 摘要；輸出 5 個區塊（見下方）；三條路徑：API key → claude CLI → fallback |
| `digest.py` | 組合 header + body + 來源狀態表，寫出 `news/YYYY-MM-DD.md` |
| `git_push.py` | `git add news/YYYY-MM-DD.md seen_urls.json` → commit → push |
| `config.py` | 路徑、API token、`LOOKBACK_HOURS=26`、`MAX_ITEMS_PER_SOURCE=20` |

### analyzer.py 輸出區塊

| 區塊 | 內容 |
|------|------|
| 📌 今日聚焦 | 3–5 點條列總結（置頂），標籤：重大事件 / 持續追蹤 / 新工具 / 社群趨勢 / 風險警示 |
| ⭐ 重點話題 | 跨多來源同時出現或引發大量討論的項目（2–5 則） |
| 🔧 技術更新 | 模型發布、功能更新、API/SDK 變更、官方公告 |
| 💬 技術熱度討論 | 社群討論、工具分享、開發者心得，附情緒標籤 |
| 💰 付費方案動態 | 定價、配額、Token 費用 |

### 新增來源

繼承 `BaseSource`，實作 `fetch() -> list[FeedItem]`，在 `main.py` 的 `sources` 列表加入即可。

---

## Wiki Schema

### 目錄結構

```
wiki/
├── index.md        ← 查詢入口，所有頁面目錄
├── log.md          ← Append-only 時序紀錄（不可修改既有條目）
├── overview.md     ← 當前局勢綜覽（每週更新）
├── feature-radar.md ← 新功能熱度追蹤、試用推薦與使用指南（每次 ingest 更新）
├── entities/       ← 模型、功能、人物、產品的持久頁面
└── topics/         ← 跨日追蹤的進行中議題
```

`news/` 為唯讀原始資料，不可修改。

### 每日 Ingest 流程（LLM 執行）

1. 讀 `news/YYYY-MM-DD.md`
2. 讀 `wiki/index.md` + `wiki/log.md`，確認未重複 ingest
3. 比對日報內容，找受影響的既有頁面
4. 更新相關 entities/ 和 topics/ 頁面
5. 判斷事件性質，決定建頁類型：
   - **具體事物**（模型/工具/人物/產品）有足夠描述 → 當天建 entities/ 頁
   - **現象/爭議/趨勢** 且 log.md 顯示昨天也出現 → 建 topics/ 頁
   - **現象/爭議/趨勢** 今天首次出現 → 暫記於相關 entities/ 歷史，明天再評估
6. **更新 `wiki/feature-radar.md`**（見下方規則）
7. Append 至 `wiki/log.md`
8. 更新 `wiki/index.md`

### feature-radar.md 更新規則 `[加入: 2026-05-13]`

每次 ingest 後必須更新 `wiki/feature-radar.md`：

| 情況 | 動作 |
|------|------|
| 日報出現新的官方功能（🔧 技術更新 或官方公告） | 在「最新功能」區塊新增條目 + 更新全覽表 |
| 已追蹤功能在新日報再次出現（討論、工具跟進、問題） | 熱度 +1 格（上限 🔥🔥🔥🔥🔥） |
| 出現多個正面使用案例 | 試用價值升級（⏳→⚡→✅） |
| 出現重大 bug 或集中負評 | 試用價值降級（✅→⚡→⏳→❌） |
| 功能從 Preview 升格正式發布 | 考慮升為 ✅，更新狀態欄 |

**新功能條目格式：**
```markdown
### 功能名稱
**發布：** YYYY-MM-DD（版本號） | **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** Research Preview

**是什麼：** 一句話描述功能用途。

**為何熱：** 社群反應、討論來源、工具跟進情況。

**快速上手：**
\```
最小可用指令或配置範例
\```

**注意事項：** 已知限制或使用前提。
```

**功能類型判斷：**
- 有具體指令/API 可用 → 必須提供「快速上手」範例
- 僅公告無具體用法 → 標「⏳ 觀望」，待正式文件後補
- 負面評價主導 → 直接標「❌ 暫不推薦」，說明原因

### entities/ 頁面格式 `[加入: 2026-04-25]`

功能類型（`類型: feature`）的 entity 頁面，若熱度 ≥ 🔥🔥🔥，必須包含 `## 熱度與試用價值` 及 `## 使用指南` 區塊。

```markdown
# 實體名稱

**類型：** model / feature / person / product / policy
**狀態：** active / deprecated / rumoured
**首次出現：** YYYY-MM-DD
**最後更新：** YYYY-MM-DD

## 現況

## 熱度與試用價值        ← feature 類型必填（熱度 ≥ 🔥🔥🔥）

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥 |
| 試用價值 | ✅ / ⚡ / ⏳ / ❌ |
| 最適合 | 適用場景描述 |
| 不適合 | 不適用場景描述 |

> 詳細最新熱度見 [[feature-radar]]

## 使用指南             ← feature 類型必填（熱度 ≥ 🔥🔥🔥 且有具體用法）

（最小可用指令 / SDK 範例 / 配置片段 / 注意事項）

## 核心功能
## 相關議題
## 參考來源
## 歷史記錄
```

### topics/ 頁面格式 `[加入: 2026-04-25]`

```markdown
# 議題名稱

**狀態：** ongoing / resolved / monitoring
**開始日期：** YYYY-MM-DD
**最後更新：** YYYY-MM-DD

## 摘要
## 技術彙整
## 目前結論
## 相關實體
## 時序
```

**技術彙整** 區塊：跨多天日報萃取的技術細節，條列式呈現。包含：
- 涉及的技術機制、API 行為、參數變化
- 已確認的限制或已知問題
- 社群發現的 workaround 或最佳實踐
- 每次 ingest 後累積更新，不重複已有條目

議題解決後移至 entities/ 作為歷史記錄，不刪除。

### 搜尋策略 `[加入: 2026-04-25]`

1. 先讀 `wiki/index.md`
2. 再讀 `wiki/log.md` 確認最近更新
3. 最後讀具體頁面

### 連結慣例 `[加入: 2026-04-25]`

- 頁面間：`[[entities/claude-code]]`
- 引用日報：`[[news/2026-04-25]]`
- 外部：`[標題](url)`

### 注意事項 `[加入: 2026-04-25]`

- 每次修改頁面必須同步更新「最後更新」欄位
- `log.md` 只能 append
- 繁體中文為主；英文術語保留英文

---

## Wiki Ingest Workflow

- Wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下，**不可**誤存至父層 `ObsidianLab/` 目錄
- 每次 ingest 結束必須同時更新 `log.md`（append）與 `index.md`（同步新增頁面與頁面總數）
- 更新頁面前先用 Grep 確認是否已有 `## 參考來源` 區塊，避免重複插入
- `community-tech-patterns.md` 等大型頁面（> 300 行）使用 Grep + offset 讀取目標段落，不做全文讀取
- 每次 ingest 結尾必須輸出強制核對清單並全部勾選（見 `/wiki-ingest` Step 9）

### community-tech-patterns ↔ community-tech-discussions 雙向連結規則 `[加入: 2026-05-16]`

**新增工具條目至 `community-tech-patterns.md` 時：**
- 每個工具條目必須包含 `**靈感來源：**` 欄位（無明確來源則填「—」）
- 若靈感來源是 `community-tech-discussions.md` 的某個討論（例如「HTML vs Markdown 辯論催生 agent-html-skills」），需同步至 discussions.md 的 `熱門討論` 表格：找到對應討論列，將工具名稱填入 `衍生` 欄（若已有則以逗號追加）

**更新 `community-tech-discussions.md` 的 `熱門討論` 表格時，`模式` 欄規則：**

| 狀況 | 模式 |
|------|------|
| 今天首次出現，無後續跡象 | ☄️閃現 |
| 已在表格中，且這是第 3 天以上持續出現 | 🌊延燒 |
| 討論在表格中已有明確共識描述（核心論點含「共識」「收束」「確立」） | 🌸落幕 |
| 表格中已存在，距上次出現（參考 `首見` 或技術彙整日期）> 7 天後重新出現 | 🌋重燃，並在核心論點補充「（重燃原因：…）」 |
| 表格中已存在但近期無新進展，熱度 ≤ 🔥 | 🌙靜候 |

**重燃偵測方式（避免掃描 log.md）：**
直接查 `熱門討論` 表格中該列的 `首見` 欄位——若 `首見` 距今超過 7 天且今日日報再次出現同主題，即判定為 🌋重燃。不需讀取 log.md。

### community-tech-discussions 技術彙整書寫規則 `[加入: 2026-05-20]`

每個進入 `## 技術彙整` 的討論條目，必須同時記錄**來源**與**引發的回響**，格式如下：

```markdown
### 討論主題名稱（YYYY-MM-DD）

- **來源：** 原始文章標題或貼文（來源平台，作者若可知）
- **核心論點：** 一句話摘要
- **關鍵回響：**（選填，有則記，無則省略此欄）
  - 📝 支持：…（文章 / 貼文標題，來源）
  - 📝 反駁：…（文章 / 貼文標題，來源）
  - 🧪 跟進實測：…（標題，來源，結論一句話）
- **收斂結論：**（若討論已有共識）…
```

**何時補充回響：**
- 日報出現明確針對某討論的反駁、實測、延伸文章時，回頭找對應的技術彙整條目補入 `關鍵回響`
- 不需要補齊所有回應——只記對「共識形成」或「立場轉變」有影響的文章

**結論寫入前必須自我審查（防止過度推論）：**
寫入「共識」、「結論」、「適用場景」等欄位前，逐一確認：
1. 這個結論是原文明確說的，還是我從其他論點**推導出來**的？
2. 如果是推導，是否有足夠的直接證據支撐，還是只是合理猜測？
3. 推導出的結論必須標注「（推論）」或「（非原文說法）」，不可直接寫成事實

**常見過度推論模式（應避免）：**
- 從反駁推導對立面：「A 說 HTML 不好協作」→ 直接寫成「共識：HTML 適合機器消費」
- 把「可能更優」寫成「應使用」
- 把「部分社群認為」寫成「社群共識」

**新條目插入位置：** 永遠插入 `## 技術彙整` 標題的**正下方**（最新在最上方），不可加在末尾。

**來源回溯方式（當 wiki 只有摘要無 URL 時）：**
1. 先查 `wiki/topics/community-tech-discussions.md` 的 `首見` 欄位取得日期
2. 讀取對應 `news/YYYY-MM-DD.md`，grep 關鍵字找原始條目
3. 原始條目通常含完整標題與來源平台，可作為引用依據

### community-tech-tools 工具新增規則 `[加入: 2026-05-20]`

新增工具至 `topics/community-tech-tools.md` 時，必須遵守以下格式：

**表格欄位：** `| 工具 | 類型 | 採用 | 首次出現 | 簡介 |`
- **工具欄**：若在日報中找到 URL（GitHub / HN / Reddit 等），格式為 `[**ToolName**](url)`；若無 URL，格式為 `**ToolName**`
- **首次出現**：填入日報日期（YYYY-MM-DD）；若無法確認則填 `—`
- **採用初始值**：新工具預設 `⏳ 觀望中`；Show HN / Reddit 正面反應明顯者填 `⚡`
- **URL 取得方式**：直接從當天日報原文中擷取（日報中的 Markdown 連結包含原始 URL）

**每次 ingest 後同步更新 `## 痛點洞察` 表格：**
- 新工具歸屬某痛點時，更新 `代表工具` 欄（加入新工具名稱）與 `近期工具` 欄（填當日日期）
- `狀態` 欄判斷規則：若 `近期工具` 距今 ≤ 14 天 → 🔥 持續升溫；> 14 天 → 🌙 冷卻觀望；Anthropic 發布對應官方功能 → ✅ 官方解決；工具潮退且有穩定最佳實踐 → ⚡ 社群收斂

---

## Wiki 頁面呈現品質標準

每次新增或更新 wiki 頁面後，必須對照以下標準審查。分為**必須修復**與**警示觸發重構**兩級。

### 必須修復（本次 ingest 完成前不得跳過） `[加入: 2026-05-15]`

| 項目 | 判斷方式 | 修復動作 |
|------|---------|---------|
| **摘要可獨立閱讀** | `## 現況`（entity）或 `## 摘要`（topic）的前 160 字，能讓不熟悉背景的讀者理解頁面主題 | 改寫摘要段落，移除只有 LLM 才懂的背景假設 |
| **關鍵資訊前置** | 最重要的事實、數字、結論出現在頁面前 1/3 | 將核心表格或結論區塊移至頁面前段 |
| **熱度表格緊接摘要** | 若頁面含熱度統計表格（如 `熱門討論`、`熱門應用`），表格必須緊接在 `## 摘要` / `## 現況` 之後，不可置於頁面末尾 | 將熱度表格整個區塊移至摘要段落正下方 |
| **無 LLM 專屬指令** | 頁面正文不含「請執行」「下一步」「若日報出現…」等面向 LLM 的操作語句 | 將這類內容移至 CLAUDE.md 或刪除 |

### 警示觸發重構（超過閾值時，本次 ingest 嘗試修復；若工作量過大，記錄至 log.md 待辦） `[加入: 2026-05-15]`

| 警示條件 | 閾值 | 重構方向 |
|---------|------|---------|
| **頁面過長** | 超過 200 行 | 事件流按主題分組，移除重複細節，考慮拆分子頁面 |
| **事件流堆積** | 連續 8 個以上 `### YYYY-MM-DD` 條目且無主題分組 | 合併為主題段落，僅保留日期作為參考標記 |
| **缺少結構化** | 方案比較、功能對照、多選項等內容以純段落表達 | 改為 Markdown 表格 |
| **表格不可排序** | 同一欄的值格式不一致（如日期、熱度、狀態混用不同符號）| 統一欄位值格式（日期用 `YYYY-MM-DD`、熱度用 🔥 數量、狀態用一致符號），使 web reader 排序功能正確運作 |
| **摘要缺失** | `## 現況` 或 `## 摘要` 區塊不存在或為空 | 從頁面內容萃取並補寫 |

### 審查輸出格式 `[加入: 2026-05-15]`

每次 ingest 結尾的強制核對清單（Step 9）中，必須包含以下欄位：

```
| 呈現品質審查 | （列出每個修改頁面的審查結果：✅ 通過 / ⚠️ 已修復 / 📋 已記錄待辦）|
```

---

## 大型檔案平行編輯

當 wiki 頁面過長無法一次讀完時，使用以下策略：

1. 先用 Grep 搜尋目標區塊的關鍵標題，取得行號範圍
2. 用 `Read` 搭配 `offset` / `limit` 只讀取需要的段落，避免讀取整份大型檔案
3. 若同一次 ingest 需要更新多個不相關頁面，在單一訊息中發出多個 Edit 呼叫（平行執行，縮短總時間）

典型大型頁面：`wiki/topics/community-tech-patterns.md`、`wiki/entities/claude-code.md`
