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
- 不可新增任何「有 API key 才能運作」的功能或 fallback
- 若提出需要 API key 的方案，必須同時提供不需要 key 的替代做法

---

## 快速上手（首次設定）

1. `pip install -r src/requirements_news.txt`
2. 在 repo 根目錄建立 `.env`，填入 `GITHUB_TOKEN`（建議）、Reddit 金鑰（可選）
3. 執行 `cd src && python -m news_aggregator.main`，確認 `news/YYYY-MM-DD.md` 被寫出並 git push
4. 設定 Windows 工作排程器，每日 08:00 執行 `src/run_news.bat`（日誌：`src/logs/task_scheduler.log`）

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

程式碼位於 `src/news_aggregator/`，執行日誌在 `src/logs/`。完整模組說明見 `src/DesignDocument/`。

Pipeline：`sources/*.py → dedup.py → enricher.py → filter.py → analyzer.py → digest.py → git_push.py`

**日報 `news/YYYY-MM-DD.md` 的五個區塊**（wiki ingest 時參考）：

| 區塊 | 內容 |
|------|------|
| 📌 今日聚焦 | 3–5 點條列總結（置頂），標籤：重大事件 / 持續追蹤 / 新工具 / 社群趨勢 / 風險警示 |
| ⭐ 重點話題 | 跨多來源同時出現或引發大量討論的項目（2–5 則） |
| 🔧 技術更新 | 模型發布、功能更新、API/SDK 變更、官方公告 |
| 💬 技術熱度討論 | 社群討論、工具分享、開發者心得，附情緒標籤 |
| 💰 付費方案動態 | 定價、配額、Token 費用 |

新增來源：繼承 `BaseSource`，實作 `fetch() -> list[FeedItem]`，在 `main.py` 的 `sources` 列表加入即可。

---

## Wiki 知識庫

詳細的 Wiki 格式規則、Ingest 流程、呈現品質標準、社群技術工具規則，全部移至 **`wiki/CLAUDE.md`**。

在 `wiki/` 目錄工作時自動載入；從 repo 根目錄執行 wiki 操作（ingest / lint）時，**Step 1 必須先讀取 `wiki/CLAUDE.md`**。

### 關鍵限制（快速查閱）

- Wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下，**不可**誤存至父層 `ObsidianLab/` 目錄
- `news/` 為唯讀原始資料，不可修改
- `log.md` 只能 append，不可修改既有條目
- 繁體中文為主；英文術語保留英文

