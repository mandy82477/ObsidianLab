# CLAUDE.md

---

## 專案目標

每日聚焦 Claude Code 與 Anthropic 核心動態，從官方更新到社群實測，一站掌握技術情報。所有條目經 LLM 評分過濾、繁中摘要、再沉澱進 wiki，**給需要穩定訊號而非即時噪音的工程師**。

### 蒐集範圍

| 類型 | 內容 |
|------|------|
| **官方核心** | GitHub Changelog、SDK / API 迭代、定價結構變化、Anthropic 公告 |
| **社群實測** | 開發者真實回饋、Bug 回報、替代方案（HN / Reddit） |
| **生態動態** | 融資、大型企業合作（AWS / Google）、政策趨勢、周邊工具 |

### 不收錄

- X / Discord 即時訊號（社交平台秒級爆料；26–30 小時延遲是設計取捨，非缺陷）
- NDA 保護下的企業非公開資訊
- 與 Claude / Anthropic 無直接關聯的通用 AI 新聞
- 無技術內容的純行銷稿

**新增 source 或 command 時的判斷標準：**
> 這份資料能幫助**需要深度與穩定資訊的工程師**更了解 Claude / Anthropic 生態系嗎？若否，不收錄。

### Web Reader 目的

- **自用**：在瀏覽器閱讀日報與 wiki，不需開啟 Obsidian 或看 raw Markdown
- **分享**：部署後可將連結分享給他人，無需安裝任何工具即可瀏覽

---

## 專案架構

兩個獨立部分：

1. **`src/news_aggregator/`** — Python 爬蟲，每日抓取 Claude / Anthropic 新聞 → `news/YYYY-MM-DD.md`
   Pipeline：`sources/*.py → dedup.py → enricher.py → filter.py → analyzer.py → digest.py → git_push.py`
   新增來源：繼承 `BaseSource`，實作 `fetch() -> list[FeedItem]`，在 `main.py` 的 `sources` 列表加入即可。

2. **`wiki/`** — LLM 維護的知識庫，從日報萃取並整理為結構化頁面
   規則：`wiki/CLAUDE.md`（進入 wiki/ 自動載入）+ `.claude/rules/wiki-ingest.md`（ingest / lint 時載入）

執行日誌：`src/logs/` | 完整模組說明：`src/DesignDocument/`

---

## 環境限制（開發前必讀）

**此專案沒有 `ANTHROPIC_API_KEY`，開發時不得假設其存在。**

- 所有需要 LLM 的功能，必須走以下其中一條路：
  1. `claude -p`（**僅限 `run_news.bat` 排程器**，不可出現在任何 skill 或 command 中）
  2. Claude session 直接執行（skills / commands 的唯一合法路徑）
- **Skills / Commands 中嚴禁出現 `claude -p`**，包括任何形式的子程序呼叫、shell 執行、或間接觸發
- **Skills / Commands 呼叫到的 Python script，也不得在其呼叫鏈中觸發 `claude -p`**
- 不可新增任何「有 API key 才能運作」的功能或 fallback

**新增功能或修改 pipeline 時的判斷標準：**
> 這個改動，在完全沒有 `ANTHROPIC_API_KEY` 的環境下也能正確運作嗎？若否，重新設計。

---

## Skills

| 指令 | 用途 | 詳細規格 |
|------|------|---------|
| `/news-pipeline` | 完整 pipeline：抓新聞 → 生成日報 → wiki ingest → 建置 web → 全部 push | `.claude/commands/news-pipeline.md` |
| `/wiki-ingest` | 讀取日報，更新 wiki entities / topics / feature-radar | `.claude/commands/wiki-ingest.md` |
| `/wiki-lint` | 每週品質檢查：矛盾頁面、孤立頁面、過期議題、CLAUDE.md 健檢 | `.claude/commands/wiki-lint.md` |

**新增 skill 時的判斷標準：**
> 這個任務是否需要跨多個步驟、值得重複執行，且有明確的輸入與完成條件？若否，用對話即可，不需要新 skill。

---

## Wiki 規則入口

- **`wiki/CLAUDE.md`**（進入 wiki/ 自動載入）：目錄結構、基本限制、搜尋策略
- **`.claude/rules/wiki-ingest.md`**（ingest / lint 時載入）：頁面格式模板、欄位規則、品質標準

### 🚫 Wiki 關鍵限制

- Wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/`，**不可**誤存至父層 `ObsidianLab/` 目錄
- `news/` 為唯讀原始資料，不可修改
- `log.md` 只能 append，不可修改既有條目
- 繁體中文為主；英文術語保留英文

**新增 wiki 頁面時的判斷標準：**
> 這個主題已有足夠的具體資訊（名稱 + 狀態 + 至少一個事件）嗎？若今日首見，先附記在相關頁面的歷史記錄，明天再評估是否建頁。
