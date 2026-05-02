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

`run_news.bat` 每天自動執行，**wiki ingest 與網站建置已整合在內，無需手動觸發**。

```
每天 08:00（Windows 排程器）
  ├─ Step 1  Python 聚合器 → news/YYYY-MM-DD.md + seen_urls.json → git push
  ├─ Step 2  claude -p "/wiki-ingest" → 更新 wiki/entities/、wiki/topics/、wiki/log.md、wiki/index.md
  ├─ Step 3  git add wiki/ → commit "wiki: auto-ingest YYYY-MM-DD" → git push
  └─ Step 4  python scripts/build_web.py → 更新 web_reader/data/data.js → commit "web: rebuild YYYY-MM-DD" → git push

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
├── entities/       ← 模型、功能、人物、產品的持久頁面
└── topics/         ← 跨日追蹤的進行中議題
```

`news/` 為唯讀原始資料，不可修改。

### 每日 Ingest 流程（LLM 執行）

1. 讀 `news/YYYY-MM-DD.md`
2. 讀 `wiki/index.md` + `wiki/log.md`，確認未重複 ingest
3. 比對日報內容，找受影響的既有頁面
4. 更新相關 entities/ 和 topics/ 頁面
5. 若新議題持續 ≥ 2 天，建立新的 topics/ 頁
6. 若新實體有具體資訊可記錄，建立新的 entities/ 頁
7. Append 至 `wiki/log.md`
8. 更新 `wiki/index.md`

### entities/ 頁面格式

```markdown
# 實體名稱

**類型：** model / feature / person / product / policy
**狀態：** active / deprecated / rumoured
**首次出現：** YYYY-MM-DD
**最後更新：** YYYY-MM-DD

## 現況
## 相關議題
## 參考來源
## 歷史記錄
```

### topics/ 頁面格式

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

### 搜尋策略

1. 先讀 `wiki/index.md`
2. 再讀 `wiki/log.md` 確認最近更新
3. 最後讀具體頁面

### 連結慣例

- 頁面間：`[[entities/claude-code]]`
- 引用日報：`[[news/2026-04-25]]`
- 外部：`[標題](url)`

### 注意事項

- 每次修改頁面必須同步更新「最後更新」欄位
- `log.md` 只能 append
- 繁體中文為主；英文術語保留英文
