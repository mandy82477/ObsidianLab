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

## 搜尋策略

1. 先讀 `wiki/index.md`
2. 再讀 `wiki/log.md` 確認最近更新
3. 最後讀具體頁面

---

## 連結慣例

- 頁面間：`[[entities/claude-code]]`
- 引用日報：`[[news/2026-04-25]]`
- 外部：`[標題](url)`

---

## ✅ 每次修改頁面必須同步更新「最後更新」欄位

格式：**只填日期，不加說明文字。**
- ✅ `**最後更新：** 2026-06-18`
- ❌ `**最後更新：** 2026-06-18（任何說明文字）`
