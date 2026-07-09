# CLAUDE.md 及規則檔修改規則

修改 `CLAUDE.md`、`.claude/commands/*.md`、`.claude/rules/*.md` 前必須讀取此檔案。

---

## 修改前：確認影響範圍

**先執行反向查詢，找出所有引用方：**
```
grep -r "被修改的檔名" .claude/commands/ .claude/rules/
```

逐一確認每個引用方在修改後仍能正確找到所需規則。若不確定影響範圍，寧可先查、再動手。

---

## 修改時：路徑引用原則

command / skill 中永遠使用明確路徑，**禁止裸露的 `CLAUDE.md`**：

| 寫法 | 判斷 |
|------|------|
| `` `wiki/CLAUDE.md` `` | ✅ 明確 |
| `` `.claude/rules/wiki-ingest.md` `` | ✅ 明確 |
| `` `CLAUDE.md` ``（無路徑前綴） | ❌ 禁止 |
| `見 CLAUDE.md`（無路徑前綴） | ❌ 禁止 |

理由：裸露路徑在重構時無法靠 grep 追蹤，容易造成 skill 靜默失效。

---

## 修改時：CLAUDE.md 設計原則

**適合放進 CLAUDE.md 的內容：**
- 有明確觸發條件的操作規則（「執行 X 時必須做 Y」）
- 可用 grep 驗證的格式規範
- 邊界判斷（單一 yes/no 問題）
- 跨 skill 共用的限制（路徑、語言、唯讀）

**不適合放進 CLAUDE.md 的內容：**
- 快速上手、安裝說明（→ `README.md`）
- 只有一個 skill 需要的格式模板（→ `.claude/rules/` 對應檔）
- 面向人類的操作範例（→ `README.md`）
- 超過 3 行的格式範本（→ `.claude/rules/` 對應檔）

> 規則檔以「內容是否精簡、有無重複」為準，不設行數上限；長度非簡化理由（同 wiki 頁面「一頁一故事」哲學）。

---

## 修改後：強制驗證

**修改完成後執行 `/review-commands`，直到零錯誤才可收工。**

**判斷標準：**
> 所有引用這個檔案的 command / skill，在修改後還能正確找到所需的規則或格式嗎？若否，先修引用再收工。
