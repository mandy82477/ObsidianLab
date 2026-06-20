# Wiki Ingest — 社群記者指南

分類為「社群」的新聞條目由此記者負責。讀此檔後直接操作，需建立新頁面時另讀 `.claude/rules/wiki-ingest-format.md`。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/topics/community-tech-patterns.md` | 工作流模式、multi-agent 設計、最佳實踐 |
| `wiki/topics/community-tech-discussions.md` | HN / Reddit 熱門技術討論 |
| `wiki/topics/community-tech-timeline.md` | 社群技術應用趨勢時序 |
| `wiki/topics/code-quality-decline.md` | Claude Code 效能退步事件 |

> `wiki/topics/community-tech-tools.md` 已改為 **lint 專用**，每日 ingest 不更新此頁。策展規則見 `.claude/rules/wiki-ingest-community-lint.md`。

---

## community-tech-patterns ↔ community-tech-discussions 雙向連結規則 `[加入: 2026-05-16]`

新增工具至 `community-tech-patterns.md` 時，若靈感明確來自 discussions.md 的某個討論，同步在 discussions.md 的 `熱門討論` 表格對應列的 `衍生` 欄填入工具名稱（若已有則逗號追加）。

`熱門討論` 表格 `模式` 欄規則：

| 狀況 | 模式 |
|------|------|
| 今天首次出現 | ☄️閃現 |
| 第 3 天以上持續出現 | 🌊延燒 |
| 討論達成共識後收束 | 🌸落幕 |
| `首見` 距今 > 7 天後重新出現 | 🌋重燃（在核心論點補「（重燃原因：…）」） |
| 表中存在但近期無新進展，熱度 ≤ 🔥 | 🌙靜候 |

重燃偵測：直接查 `熱門討論` 表格的 `首見` 欄，不需讀取 log.md。

---

## community-tech-discussions 熱門討論保留規則 `[加入: 2026-06-20]`

每次 ingest 後，若本輪有新增或更新表格條目，同步執行清理：

| 模式 | 保留條件 |
|------|---------|
| ☄️閃現 | 首見距今 ≤ 21 天（超過則移除） |
| 🌊延燒 | 永久保留，無期限 |
| 🌸落幕 | 首見距今 ≤ 14 天（超過則移除） |
| 🌋重燃 | 等同 🌊延燒，無期限 |
| 🌙靜候 | 永久保留 |

**技術彙整保留：** 對應條目距今 ≤ 60 天。超過 60 天且表格條目已移除者，將 `## 技術彙整` 子區塊移至 `wiki/topics/community-tech-timeline.md` 歷史存檔。

---

## community-tech-discussions 技術彙整書寫規則 `[加入: 2026-05-20]`

**格式：**
```markdown
### 討論主題名稱（YYYY-MM-DD）

- **來源：** 原始文章標題（平台，作者）
- **核心論點：** 一句話摘要
- **關鍵回響：**（選填，有則記）
  - 📝 支持：…（標題，來源）
  - 📝 反駁：…（標題，來源）
  - 🧪 跟進實測：…（標題，來源，結論一句話）
- **收斂結論：**（若討論已有共識）…
```

**新條目插入位置：** 永遠插入 `## 技術彙整` 標題的**正下方**（最新在最上方），不可加在末尾。

**防過度推論：** 推導出的結論必須標注「（推論）」，不可直接寫成事實。

---

## 回報格式

```
## 社群 記者回報
更新頁面：[list]
feature-radar 新增：無
index.md 狀態變更：[page: 舊狀態 → 新狀態 or 無]
新增頁面：[filepath or 無]
```
