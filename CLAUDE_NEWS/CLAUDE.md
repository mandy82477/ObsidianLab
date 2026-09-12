# CLAUDE.md

每日聚焦 Claude Code 與 Anthropic 核心動態，從官方更新到社群實測。所有條目經 LLM 評分過濾、繁中摘要、再沉澱進 wiki。

**收不收錄一律問這句：** 這份資料能幫助**需要深度與穩定資訊的工程師**更了解 Claude / Anthropic 生態系嗎？若否，不收錄。
目標讀者、蒐集範圍與不收錄清單：`.claude/rules/collection-scope.md`（動到 `src/news_aggregator/` 時自動載入）。

## 專案架構

- **`src/news_aggregator/`** — Python 爬蟲，每日抓 Claude / Anthropic 新聞 → `news/YYYY-MM-DD.md`。執行日誌 `src/logs/`，模組說明 `src/DesignDocument/`
- **`wiki/`** — 從日報萃取的知識庫；`web_reader/` 是它與日報的網站版（`scripts/build_web.py` 建置）
- 規則分三處：`.claude/rules/`（主 session，`paths:` 觸發）、`.claude/reporter-rules/`（記者與主編明文 Read）、`.claude/commands/`（指令）

## 這是一個 LLM wiki：三個動作

- **Ingest（每日，`/news-pipeline`）**：爬蟲產日報（`news/` 唯讀原料）→ 主編分類、派六位記者各寫自己領域的頁 → 主編彙整 `wiki/index.md`、`feature-radar.md`、`log.md`。頁面是「被策展的現在」，log 是不可改的過去，index 只放路由；每個事實只有一個家，別處用 wikilink 指過去。
- **Query（任何 session）**：專有名詞／issue 號／版本號 → 直接 Grep `wiki/`；概念、選型 → `wiki/index.md` 挑頁，頁頂 callout 是最新狀態；「最近怎樣」→ `wiki/log.md` 先 Grep 日期；誰負責哪頁 → `.claude/reporter-rules/` 的負責頁面表；引用關係 → `python scripts/wiki_graph.py`。完整六路見 `wiki/CLAUDE.md`「搜尋策略」。
- **Lint（每週，`/weekly`、`/wiki-lint`）**：矛盾、孤兒、過期、蒸餾封存；歷史質疑抽題代打。
- **使用者提問通道**：使用者在對話中點名的事實，由主編以 web 工具查證一手來源後直接寫進 wiki（標查證日＋來源），並在 `wiki/log.md` append 一筆 Query 條目；不經日報，歸因 slug `user-query`。

## 環境限制

**此專案沒有 `ANTHROPIC_API_KEY`，開發時不得假設其存在。**

- **`claude -p` 任何情境一律禁止**：commands / skills 本身、它們呼叫的 script、子程序、間接觸發，全部不行
- 不得新增任何「有 API key 才能運作」的功能或 fallback；唯一合法的 LLM 路徑是 Claude session 直接執行
- 判斷式：這個改動在完全沒有 `ANTHROPIC_API_KEY` 的環境下也能正確運作嗎？若否，重新設計

## 完工定義（Definition of Done）

**改動未閉迴路不算完成。** 實質改動（pipeline / 規則 / wiki / 腳本）三者到齊：

1. **測試綠**：`python scripts/run_tests.py` 通過
2. **已 commit**：非 data 檔的改動已進 git（`gathered_items.json` / `emitted_items.json` / `seen_urls.json` 這類 data 檔例外）
3. **依賴缺口已登記**：若改動依賴尚缺的憑證／服務／真解，在 `docs/workaround-register.md` 登記 owner ＋ 複查日，不可只留在對話裡

三者缺一，任務標「進行中」，不標「完成」。

### commit 範圍

**任何 session、任何情境，一律不得 `git add -A` / `git add .`**，一律指名路徑（如 `git add wiki/ .claude/`）。`.claude/hooks/block_git_add_all.py` 會擋下，`scripts/check_workflow_paths.py` 看守 workflow。

> **判斷式：** 這個 commit 的訊息，說得出裡面每一個檔案為什麼在嗎？說不出 → 你 add 太多了。（立法依據見沿革檔 `docs/rules-changelog/CLAUDE.md` 2026-08-29 A）

## Skills

- 🟢 每天：`/news-pipeline`（抓新聞 → 日報 → wiki ingest → 建置 web → push；已含 `/wiki-ingest`）
- 🟡 每週：`/weekly`（週報 ＋ wiki 週度回顧 ＋ 開放迴路掃描 ＋ 單一 push；已含 `/weekly-report`、`/wiki-weekly-review`），另跑 `/wiki-lint` 做每週品質檢查
- 改完 `.claude/` 或本檔：`/review-commands`，直到零錯誤

> 其餘指令（`/wiki-backfill`、`/wiki-readability`、`/pipeline-change-check` …）見 `.claude/commands/` 各檔的 description。
> **新增 skill 的判斷標準：** 這個任務是否需要跨多個步驟、值得重複執行，且有明確的輸入與完成條件？若否，用對話即可。

## Wiki 規則入口

- **`wiki/CLAUDE.md`**（碰 `wiki/` 檔案自動載入）：目錄結構、資訊架構哲學、連結語法契約、搜尋策略
- **`.claude/reporter-rules/`**（記者與 ingest／lint 主編明文 Read，無自動載入）：分類與派工、六類記者的負責頁面、頁面格式模板。導覽見該資料夾的 README
- **`.claude/rules/`**（主 session，`paths:` 觸發）：`claude-md-edit.md`、`web-reader-design.md`、`collection-scope.md`

**🚫 關鍵限制：** Wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/`，**不可**誤存至父層 `ObsidianLab/` 目錄。

## 修改 rules 或 commands

改任何 `.claude/` 下的檔案或本檔後，執行 `/review-commands` 直到零錯誤；規則與流程見 `.claude/rules/claude-md-edit.md`（修改前必須讀取）。
