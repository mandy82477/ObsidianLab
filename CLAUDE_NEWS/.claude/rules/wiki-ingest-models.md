# Wiki Ingest — 模型記者指南

分類為「模型」的新聞條目由此記者負責。讀此檔後直接操作，需建立新頁面時另讀 `.claude/rules/wiki-ingest-format.md`。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/entities/fable-5.md` | Fable 5 動態、出口管制、解封進展 |
| `wiki/entities/opus-4-8.md` | Opus 4.8 能力更新、評測新資料 |
| `wiki/entities/opus-4-7.md` | Opus 4.7 後續、思考深度議題 |
| `wiki/entities/mythos.md` | Mythos 漏洞更新、安全模型動態 |
| `wiki/entities/sonnet-5.md` | Sonnet 5 動態、評測、預設模型變化 |
| `wiki/topics/model-comparison.md` | 任一模型發布/下線/狀態/定價/預設變更（見下方同步規則）|

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 🤖 模型 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

> `wiki/entities/pricing.md` 由**商業記者主責**（見 `.claude/rules/wiki-ingest-commercial.md`）。模型記者遇模型定價時，將定價細節留給商業記者，僅在模型頁記能力並加 wikilink 至 pricing。

新模型發布時，依 `.claude/rules/wiki-ingest-format.md` 建立新 entities/ 頁。

---

## 更新規則

**模型頁基本欄位：** 每次更新必須同步「最後更新」日期。若狀態改變（如 `beta` → `active`），標記回報讓主編同步 `wiki/index.md`。

**評測數據：** 優先記錄官方或三方確認來源，補注測試日期。若有相互矛盾的評測結果，保留兩者並標注來源。

**版本號：** 模型版本號視為元資訊（`entities/` 標頭），不另建頁面。若版本迭代有重大能力差異，加入 `## 歷史記錄` 條目。

**定價歸屬：** 模型本身（能力、評測）進模型頁；定價細節進 `wiki/entities/pricing.md`（**商業記者主責**，模型記者不直接維護該頁）。同一事件有兩面向時，模型記者記能力面、商業記者記定價面，互相加 wikilink。

**選型對照同步 `[加入: 2026-07-02]`：** `wiki/topics/model-comparison.md` 是「我該用哪個模型」的單一入口。任一模型發布/下線/狀態/定價/Claude Code 預設變更時，除更新該模型頁外，**必須同步更新對照頁的快速選型表與情境推薦**；深度細節仍留在各模型頁，對照頁只放一行式結論。此項納入回報的「同步自查」欄。

---

## feature-radar 判斷

新模型發布 = 使用者可 `--model` 選用 → **須回報主編新增 feature-radar 條目**。

純模型評測論文或研究報告（無可用介面）→ **不進 feature-radar**，記於模型頁即可。

---

## 回報格式

```
## 模型 記者回報
更新頁面：[list]
feature-radar 新增：[條目標題 or 無]
index.md 狀態變更：[page: 舊狀態 → 新狀態 or 無]
新增頁面：[filepath or 無]
同步自查：[✅ 已同步 / ⚠️ 需主編轉知（說明）/ 不適用]
```
