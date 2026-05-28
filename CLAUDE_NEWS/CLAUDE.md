# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 專案概述

這個 repo 有兩個獨立部分：

1. **`news_aggregator/`** — Python 爬蟲，每日自動抓取 Claude / Anthropic 相關新聞，寫出 `news/YYYY-MM-DD.md`
2. **`wiki/`** — LLM 維護的知識庫，從日報萃取並整理成結構化頁面

完整流程圖見 `src/DesignDocument/Design Diagram.md`。

---

## 環境限制（開發前必讀）

**此專案沒有 `ANTHROPIC_API_KEY`，開發時不得假設其存在。**

- 所有需要 LLM 的功能，必須走以下其中一條路：
  1. `claude -p`（**僅限 `run_news.bat` 排程器**，不可出現在任何 skill 或 command 中）
  2. Claude session 直接執行（skills / commands 的唯一合法路徑）
- **Skills（`.claude/skills/`）和 Commands（`.claude/commands/`）中嚴禁出現 `claude -p`**，包括任何形式的子程序呼叫、shell 執行、或間接觸發
- **Skills / Commands 呼叫到的 Python script 或其他腳本，也不得在其呼叫鏈中觸發 `claude -p`**（例如：command 呼叫 `main.py --gather-only`，則 `--gather-only` 路徑上的所有模組都不得呼叫 `claude -p`）
- 不可新增任何「有 API key 才能運作」的功能或 fallback
- 若提出需要 API key 的方案，必須同時提供不需要 key 的替代做法

---

## 每日自動化流程

`/news-pipeline` 為互動式執行指令，wiki ingest 由 Claude 直接在 session 內執行（**不走 `claude -p`**，不產生 6/15 後的額外計費）。

```
自動（Windows 排程器，run_news.bat，每天 08:00）
  ├─ Step 1  Python 聚合器 → news/YYYY-MM-DD.md → git push
  ├─ Step 2  claude -p "/wiki-ingest" → 更新 wiki/
  ├─ Step 3  git push wiki/
  └─ Step 4  build_web.py → git push web_reader/

手動（/news-pipeline）
  └─ 同上，但 Step 2 由 Claude 直接在 session 執行
```

---

## 聚合器 Pipeline 架構

程式碼位於 `src/news_aggregator/`，執行日誌在 `src/logs/`。完整模組說明見 `src/DesignDocument/`。

Pipeline：`sources/*.py → dedup.py → enricher.py → filter.py → analyzer.py → digest.py → git_push.py`

新增來源：繼承 `BaseSource`，實作 `fetch() -> list[FeedItem]`，在 `main.py` 的 `sources` 列表加入即可。

日報五個區塊格式、wiki 頁面模板、呈現品質標準：見 **`.claude/rules/wiki-ingest.md`**（ingest / lint 時載入）。

---

## Wiki 知識庫

詳細的 Wiki 格式規則、Ingest 流程、呈現品質標準、社群技術工具規則，全部移至 **`wiki/CLAUDE.md`**。

在 `wiki/` 目錄工作時自動載入；從 repo 根目錄執行 wiki 操作（ingest / lint）時，**Step 1 必須先讀取 `wiki/CLAUDE.md`**。

### 關鍵限制（快速查閱）

- Wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下，**不可**誤存至父層 `ObsidianLab/` 目錄
- `news/` 為唯讀原始資料，不可修改
- `log.md` 只能 append，不可修改既有條目
- 繁體中文為主；英文術語保留英文

