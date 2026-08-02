# Wiki 知識庫規則

一般 wiki 查詢時自動載入。**執行 ingest / lint 操作時，必須同時讀取 `.claude/rules/wiki-ingest.md`**（分類標準與派工流程）。頁面格式模板見 `.claude/rules/wiki-ingest-format.md`。

---

## 目錄結構

```
wiki/
├── index.md         ← 查詢入口，所有頁面目錄
├── log.md           ← Append-only 時序紀錄
├── overview.md      ← 當前局勢綜覽（每週更新）
├── feature-radar.md ← 官方功能熱度追蹤（每次 ingest 更新）
├── reader-notes.md  ← 使用者「記一下」的待辦收件匣（weekly-review 每週消費）
├── entities/        ← 模型、功能、人物、產品的持久頁面
└── topics/          ← 跨日追蹤的進行中議題
```

---

## 🚫 絕對限制

- `news/` 為唯讀原始資料，**不可修改**
- `log.md` **只能 append**，不可修改既有條目
- Wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下，**不可**誤存至父層 `ObsidianLab/` 目錄
- 繁體中文為主；英文術語保留英文

---

## 搜尋策略（查詢分流）

依問題型態選路徑，不要一律先讀 index：

1. **專有名詞／issue 編號／錯誤碼**（如 `ECONNRESET`、`#826`、版本號）→ 直接 Grep `wiki/`（必要時擴及 `news/`）——目錄摘要不含這類字串，先讀 index 是白讀
2. **概念／選型／主題**（「哪頁在講 X」）→ 讀 `wiki/index.md` 目錄表挑頁 → 讀該頁（頁面頂部 callout 即最新動態）
3. **結構性盤點**（哪些頁某狀態／某領域／多久沒更新）→ Grep 頁面標頭欄位（如 `最後新聞更新`、`狀態`），不需逐頁閱讀
4. **「最近發生什麼」**→ `wiki/log.md`（append-only，先 Grep 日期定位再讀該段，不可整讀）或 `news/` 日報

---

## 連結慣例

- 頁面間：`[[entities/claude-code]]`
- 引用日報：`[[news/2026-04-25]]`
- 外部：`[標題](url)`
- 來源歸因不寫入 wiki 正文：記者在回報訊息的「來源歸因」欄回報，由主編 append 至 `data/source_attribution.jsonl`，規則見 `.claude/rules/wiki-reporter-shared.md`

---

## ✅ 每次修改頁面必須同步更新「最後更新」欄位

格式：**只填日期，不加說明文字。**
- ✅ `**最後更新：** 2026-06-18`
- ❌ `**最後更新：** 2026-06-18（任何說明文字）`
