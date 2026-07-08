---
description: 系統架構變動時，快速同步更新架構文件（Design Diagram.md + 現有架構頁 + 演進頁），內建今日血淚換來的防坑檢查。
---

# Architecture Doc Sync（/arch-doc-sync）

當 CLAUDE_NEWS 系統結構改變（新 pipeline 步驟、新來源、新記者規則、新治理機制、模型分工變化等）時，用此流程把三份架構文件同步到最新——**快、準、不重蹈過期與踩坑覆轍**。

## 為什麼需要這個 skill

架構文件會過期，而過期的架構圖比沒有更糟（會誤導）。今天（2026-07-05/06）重建這套文件時踩過的坑，全部固化成本流程的強制檢查，下次不必重新流血。

## 三份文件與其分工（改哪個看這裡）

| 檔案 | 角色 | 什麼時候改 |
|------|------|-----------|
| `src/DesignDocument/Design Diagram.md` | **現況的單一事實來源**（mermaid） | 任何現況架構變動，**先改這裡** |
| `docs/architecture-current.html` | 現況操作視圖（5 張 HTML box 圖 + filter）| 跟著 Design Diagram.md 改 |
| `docs/architecture-evolution.html` | 演進敘事（時間軸事件 + diagram A–F）| 只有「里程碑級」變動才加一筆事件 |
| `docs/architecture.css` | 兩頁共用樣式（token + class）| **只有改設計（顏色/字體/間距）才動；改內容不碰** |

> `docs/architecture-evolution-react.bak.html` 是舊 React 版備份，唯讀，不要拿它當範本。

---

## 步驟

### 1. 判斷變更範圍
- 讀 `src/DesignDocument/Design Diagram.md` 標頭「最後更新」日期
- `git log --oneline --since="<那個日期>"` 看這段期間的 commit，挑出**結構性**變動（pipeline 步驟增減、`sources/*.py` 增減、`.claude/rules/` 或 `.claude/commands/` 的流程改動、新治理機制）
- 分類每筆變動：
  - **現況變動**（改了系統「現在怎麼運作」）→ 要更新 Design Diagram.md + current 頁
  - **里程碑**（一次有意義的架構演進，值得記入歷史）→ 額外在 evolution 頁加一筆事件
  - 純 bug fix / 微調 → 通常不進架構文件

### 2. 先更新事實來源 `Design Diagram.md`
- 對照**實際系統**核實，不憑記憶：pipeline 讀 `.claude/commands/news-pipeline-steps.md` 與 `news-pipeline.md`；來源清單讀 `src/news_aggregator/main.py` 的 `sources = [...]`；lint 讀 `.claude/commands/wiki-lint.md`；派工讀 `.claude/rules/wiki-ingest.md`
- 改對應的 mermaid 圖與文字；更新標頭「最後更新」為今日
- 這是下游 HTML 的依據，**先它、後 HTML**

### 3. 更新 `docs/architecture-current.html`
- 5 張圖各是一個 `#dgm-<key>` panel（overview / agg / ingest / lint / artifacts），用 `architecture.css` 的 class 畫：`.dgm-box`、`.dgm-step`、`.dgm-arrow`、`.phase--a/b/c`（a/c=success 綠、b=ochre）、`.dgm-row`
- 只改有變動的那張 panel，比照既有 box 的 class 寫法
- 若新增一張圖：filter bar 加一個 `.dgm-tab`（`data-dgm="<key>"`）+ 一個 `#dgm-<key>` panel
- **更新日期標記**「現況截至 YYYY-MM-DD」為今日
- 設計 token（顏色/字體）若要調，**只改 `architecture.css`**，不在 HTML 內寫死

### 4. 更新 `docs/architecture-evolution.html`（僅里程碑）
- 時間軸事件卡片結構：`.event-card`（含 `.event-date`、`.event-title`、`.event-tag--script/llm/agent`、可選 `.event-tag--diagram`、`.event-body` 內 `.event-md` + 可選 `.event-diagram`）
- 新事件插入**對應月份分組**、依日期排序（不是塞末尾）
- `track` 三選一：`script`（腳本/pipeline）/ `llm`（LLM 呼叫點）/ `agent`（Agent 設計）
- 只有真正的新架構模式才配新 diagram（SVG）；沿用既有 A–F 的畫法

### 5. 驗證（強制，用 preview，不可略過）
launch.json 已有 `docs-preview`（port 3132）。preview_start 後對**每個改過的 HTML** 逐項查（用 preview_eval / preview_inspect）：

| 檢查 | 怎麼查 | 為什麼（哪次踩過）|
|------|--------|------------------|
| **charset UTF-8** | `document.characterSet==='UTF-8'` 且 h1 中文非亂碼 | 漏 `<meta charset="utf-8">` 會整頁亂碼，且**不產生 console error** |
| 共用 CSS 有套上 | 抽一個 `.dgm-box` 查 `borderTopColor` 是 `rgb(176,137,104)` | class 名不符會 fallback 成無樣式，肉眼未必立刻看出 |
| 版面置中 | 容器 `maxWidth` 是 `896px`、`margin:auto` | utility class 缺失會讓版面全寬爆掉 |
| filter / 互連 | 實際點擊，確認 panel 切換、cross-link href 正確 | — |
| console | `preview_console_logs` level error 為空 | — |

- **截圖工具此環境會逾時，不要用 screenshot**，一律 eval/inspect
- **不可只信「看起來好了」或 agent 的「已驗證」**——親自 eval 查渲染後的實際值

### 6. Commit
- `git add docs/ src/DesignDocument/`，commit 訊息 `docs: 架構文件同步 <一句話變動>`，結尾加 Co-Authored-By 行；push

---

## 🚫 不變式（today's lessons，違反必出事）

1. **charset meta 必備**：每個 HTML 檔 `<html>` 後必須有 `<meta charset="utf-8">`。
2. **設計 token 單一來源**：顏色/字體/圓角只在 `architecture.css` 的 `:root` 改，兩頁自動同步；HTML 內不寫死色碼。
3. **獨立驗證**：改完一定親自用 preview 查渲染後的實際值，不靠肉眼、不靠「已完成」回報。
4. **派工要重驗最終狀態**：若把機械式 HTML 編輯派給 sonnet agent，**主 session 必須在最後重新驗證 disk 上的最終檔**——併發/委派可能讓中間狀態與最終狀態不一致（曾發生兩 agent 並行覆蓋同一檔）。
5. **先事實來源、後 HTML**：永遠先改 `Design Diagram.md`，HTML 跟著它，避免兩者漂移。
6. **原 React 備份唯讀**：`architecture-evolution-react.bak.html` 不當範本、不修改。

---

## 快速心法

> 系統變了 → 先問「這是**現況變動**還是**里程碑**？」→ 改 Design Diagram.md → current 頁跟上（里程碑才動 evolution 頁）→ preview 五項強制檢查 → commit。設計要動只碰 architecture.css。
