# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 專案概述

這個 repo 有兩個獨立部分：

1. **`news_aggregator/`** — Python 爬蟲，每日自動抓取 Claude / Anthropic 相關新聞，寫出 `news/YYYY-MM-DD.md`
2. **`wiki/`** — LLM 維護的知識庫，從日報萃取並整理成結構化頁面

---

## 快速上手（首次設定）

### 步驟 1：安裝 Python 依賴

```bash
pip install -r requirements_news.txt
```

### 步驟 2：建立 `.env` 設定 API 金鑰

在 repo 根目錄建立 `.env` 檔案：

```
ANTHROPIC_API_KEY=sk-ant-...   # 必要：用於 LLM 過濾與摘要
GITHUB_TOKEN=ghp_...           # 建議：提高 GitHub API rate limit
REDDIT_CLIENT_ID=...           # 可選：啟用 Reddit 來源
REDDIT_CLIENT_SECRET=...
```

`ANTHROPIC_API_KEY` 若未設定，會自動退回使用本機 `claude` CLI（需登入 Claude.ai Pro）。

### 步驟 3：手動執行一次確認正常

```bash
python -m news_aggregator.main
```

執行完成後應看到 `news/YYYY-MM-DD.md` 被寫出，並自動 git commit & push。

### 步驟 4：設定 Windows 工作排程器（自動化）

用 Windows 工作排程器每天定時執行 `run_news.bat`，建議時間為每日 08:00。
執行日誌會寫到 `logs/task_scheduler.log`，聚合器本身的日誌在 `logs/news_aggregator.log`。

---

## 每日操作流程

```
每天
  ├─ [自動] run_news.bat 執行 → 產生 news/YYYY-MM-DD.md + git push
  └─ [手動] 告訴 Claude：「請根據今天的日報執行 ingest，更新 wiki」
              → Claude 更新 wiki/entities/、wiki/topics/、wiki/log.md、wiki/index.md

每週
  └─ [手動] 告訴 Claude：「執行 wiki lint 並更新 overview.md」
```

### 每日 Wiki Ingest 指令範例

```
請根據 news/2026-04-26.md 執行每日 ingest，更新 wiki。
```

### 每週 Wiki Lint 指令範例

```
請執行 wiki lint：找出矛盾頁面、孤立頁面、過期 ongoing 議題，並更新 wiki/overview.md。
```

---

## 執行聚合器

```bash
# 手動執行（需在 repo 根目錄）
python -m news_aggregator.main

# Windows 排程器使用的 bat 檔
run_news.bat
```

安裝依賴：
```bash
pip install -r requirements_news.txt
```

環境變數（放在 repo 根目錄的 `.env`）：
```
ANTHROPIC_API_KEY=...      # 用於 LLM 過濾 + 摘要（可選，無則退回 claude CLI）
GITHUB_TOKEN=...           # 用於 GitHub Releases 來源（可選）
REDDIT_CLIENT_ID=...       # 用於 Reddit 來源（可選）
REDDIT_CLIENT_SECRET=...
```

---

## 聚合器 Pipeline 架構

```
sources/*.py  →  dedup.py  →  enricher.py  →  filter.py  →  analyzer.py  →  digest.py
```

| 模組 | 職責 |
|------|------|
| `sources/base.py` | `FeedItem` dataclass + `BaseSource` ABC |
| `sources/*.py` | 各來源 fetch，回傳 `list[FeedItem]`，失敗回傳 `[]` 不 raise |
| `dedup.py` | URL 正規化去重 + 模糊標題去重（threshold 0.85）；官方來源優先 |
| `enricher.py` | 用 trafilatura 抓原文補充 `summary` 欄位 |
| `filter.py` | 呼叫 Claude Haiku 批次評分 1–5，丟棄 < 3 分（無 API key 則略過） |
| `analyzer.py` | 呼叫 Claude 產生繁體中文 Markdown 摘要；三條路徑：API key → claude CLI → fallback |
| `classifier.py` | regex 分類（pricing / tech_update / tech_discuss）+ 亮點偵測 |
| `digest.py` | 組合 header + body + 來源狀態表，寫出 `news/YYYY-MM-DD.md` |
| `config.py` | 路徑、API token、`LOOKBACK_HOURS=26`、`MAX_ITEMS_PER_SOURCE=20` |
| `dedup.py` `seen_urls.json` | 跨執行的 URL 去重快取 |

新增來源：繼承 `BaseSource`，實作 `fetch() -> list[FeedItem]`，在 `main.py` 的 `sources` 列表加入即可。

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
2. 比對 `wiki/index.md` 找受影響的既有頁面
3. 更新相關 entities/ 和 topics/ 頁面
4. 若新議題持續 ≥ 2 天，建立新的 topics/ 頁
5. Append 至 `wiki/log.md`
6. 更新 `wiki/index.md`

### entities/ 頁面格式

```markdown
# 實體名稱

**類型：** model / feature / person / product / policy
**狀態：** active / deprecated / rumoured
**首次出現：** YYYY-MM-DD
**最後更新：** YYYY-MM-DD

## 現況
## 歷史記錄
## 相關議題
## 參考來源
```

### topics/ 頁面格式

```markdown
# 議題名稱

**狀態：** ongoing / resolved / monitoring
**開始日期：** YYYY-MM-DD
**最後更新：** YYYY-MM-DD

## 摘要
## 時序
## 技術彙整
## 目前結論
## 相關實體
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
