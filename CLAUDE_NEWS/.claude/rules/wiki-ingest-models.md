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
| `wiki/entities/pricing.md` | 模型定價、計費變更（按 token / 訂閱） |

新模型發布時，依 `.claude/rules/wiki-ingest-format.md` 建立新 entities/ 頁。

---

## 更新規則

**模型頁基本欄位：** 每次更新必須同步「最後更新」日期。若狀態改變（如 `beta` → `active`），標記回報讓主編同步 `wiki/index.md`。

**評測數據：** 優先記錄官方或三方確認來源，補注測試日期。若有相互矛盾的評測結果，保留兩者並標注來源。

**版本號：** 模型版本號視為元資訊（`entities/` 標頭），不另建頁面。若版本迭代有重大能力差異，加入 `## 歷史記錄` 條目。

**定價歸屬：** 模型本身（能力、評測）進模型頁；定價細節進 `wiki/entities/pricing.md`。同一事件有兩面向時分別記錄，互相加 wikilink。

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
```
