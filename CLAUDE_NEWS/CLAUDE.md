# Claude Code News Wiki — Schema

本文件定義 wiki 的結構、慣例與操作流程，是 LLM 維護此知識庫的核心指引。

---

## 目錄結構

```
ObsidianLab/
├── news/YYYY-MM-DD.md      ← 每日日報（不可修改，唯讀來源）
├── wiki/
│   ├── index.md            ← 所有 wiki 頁的目錄（查詢入口）
│   ├── log.md              ← Append-only 時序紀錄
│   ├── overview.md         ← 當前局勢綜覽（每週更新）
│   ├── entities/           ← 實體頁：模型、功能、人物、產品
│   └── topics/             ← 進行中議題：跨日追蹤的事件或趨勢
└── CLAUDE.md               ← 本文件（Schema）
```

---

## 層級職責

| 層級 | 路徑 | 誰寫 | 規則 |
|------|------|------|------|
| Raw Sources | `news/` | 程式自動 | 不可修改 |
| Wiki | `wiki/` | LLM 維護 | 可增刪改 |
| Schema | `CLAUDE.md` | 人 + LLM | 共同演進 |

---

## 頁面格式

### entities/ 頁面

```markdown
# 實體名稱

**類型：** model / feature / person / product / policy
**狀態：** active / deprecated / rumoured
**首次出現：** YYYY-MM-DD
**最後更新：** YYYY-MM-DD

## 現況
（一段簡短的當前狀態說明）

## 歷史記錄
（時序條列，新的在上）

## 相關議題
（連結到 topics/ 頁面）

## 參考來源
（連結到相關日報）
```

### topics/ 頁面

```markdown
# 議題名稱

**狀態：** ongoing / resolved / monitoring
**開始日期：** YYYY-MM-DD
**最後更新：** YYYY-MM-DD

## 摘要
（一段話說明這個議題是什麼）

## 時序
（事件列表，最新在上）

## 目前結論
（目前已知的結論或待確認事項）

## 相關實體
（連結到 entities/ 頁面）
```

---

## 操作流程

### 每日 Ingest（程式自動執行）

1. 讀取當日 `news/YYYY-MM-DD.md`
2. 比對 `wiki/index.md`，找出被今日新聞觸及的既有頁面
3. 更新相關 entities/ 和 topics/ 頁面
4. 若新議題持續 2 天以上，建立新的 topics/ 頁
5. 在 `wiki/log.md` 追加本次執行紀錄
6. 更新 `wiki/index.md`

### Lint（每週手動或 Claude 執行）

- 找出矛盾頁面（兩頁描述同一事件但說法不同）
- 找出孤立頁面（無其他頁面連結到它）
- 標記可能已過期的 "ongoing" 議題
- 建議新實體頁（被多次提及但尚無專頁）

---

## 連結慣例

- 頁面之間使用 Obsidian wikilink：`[[entities/claude-code]]`
- 引用日報：`[[news/2026-04-25]]`
- 外部連結使用標準 Markdown：`[標題](url)`

---

## 搜尋策略

查詢時，LLM 應：
1. 先讀 `wiki/index.md` 找相關頁面
2. 再讀 `wiki/log.md` 確認最近有無相關更新
3. 最後讀具體頁面取得詳細資訊

---

## 注意事項

- 每頁的「最後更新」欄位必須在每次修改時同步更新
- 議題頁面解決後，移至 entities/ 作為歷史記錄，勿刪除
- `log.md` 只能 append，不可修改既有條目
- 繁體中文為主要語言；英文術語保留英文
