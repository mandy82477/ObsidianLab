---
description: 驗證所有 commands / rules / CLAUDE.md 修改後，相關指令仍可正確執行。持續循環直到零錯誤。
---

# Review Commands

每次修改 `.claude/commands/`、`.claude/rules/` 或 `CLAUDE.md` 後執行。
**終止條件：完整跑完一輪所有檢查，零 ❌，才可結束。每發現一個 ❌ 立即修正，然後從頭重新開始整輪。**

---

## 每輪執行的三項檢查

### 檢查 1：路徑引用完整性

逐一讀取 `.claude/commands/*.md` 及 `.claude/rules/*.md` 所有檔案。

**1a. 裸露 CLAUDE.md 引用**
在所有檔案中 grep `CLAUDE\.md`，找出**不含明確路徑前綴**的引用：
- ✅ 允許：`` `wiki/CLAUDE.md` ``（有明確路徑）
- ❌ 禁止：`` `CLAUDE.md` ``、`CLAUDE.md`（裸露，無前綴）
- 發現 ❌ → 立即修正為明確路徑，然後**從頭重新執行整輪**

**1b. 明確路徑檔案存在性**
提取所有 backtick 包住的路徑（如 `` `.claude/rules/wiki-ingest.md` ``），確認對應檔案存在：
- 逐一用 Bash 的 `test -f` 或 `ls` 確認
- 發現不存在的路徑 → 標記 ❌，修正後重新執行整輪

**1c. 錨點引用有效性**
以下錨點必須存在於對應 wiki 檔案中（grep 結果應有內容）：

| 錨點 | 應存在於 |
|------|---------|
| `\| 首次出現 \|` | `wiki/topics/community-tech-tools.md` |
| `## 痛點洞察` | `wiki/topics/community-tech-tools.md` |
| `近期工具` | `wiki/topics/community-tech-tools.md` |
| `## 技術彙整` | `wiki/topics/community-tech-discussions.md` |
| `熱門討論` | `wiki/topics/community-tech-discussions.md` |
| `衍生` | `wiki/topics/community-tech-discussions.md` |
| `全覽表` | `wiki/feature-radar.md` |

---

### 檢查 2：載入鏈完整性

對三個主要 skill 讀取其文字內容，逐一確認：

| Skill | 必須明確載入 | 驗證位置 |
|-------|------------|---------|
| `wiki-ingest.md` | `wiki/CLAUDE.md` + `.claude/rules/wiki-ingest.md` | Step 2 的讀取清單 |
| `wiki-lint.md` | `wiki/CLAUDE.md` + `.claude/rules/wiki-ingest.md` | Step 1 的讀取清單 |
| `news-pipeline-steps.md` | `wiki/CLAUDE.md` + `.claude/rules/wiki-ingest.md` | Step 2 的讀取清單 |

「明確載入」的意思：**在步驟文字中直接列出這兩個檔案路徑**，不可只靠「見 CLAUDE.md」或「自動載入」等隱含指示。

---

### 檢查 3：關鍵步驟存在性

讀取各 command 內容，確認以下步驟存在且語意正確：

**wiki-ingest.md**
- [ ] Step 4 更新 `wiki/feature-radar.md` 存在，且引用 `.claude/rules/wiki-ingest-features.md`
- [ ] Step 4 的 `wiki/log.md` 格式含 `呈現品質` 欄位
- [ ] Step 5 核對清單存在

**wiki-lint.md**
- [ ] Step 1 同時讀取 `wiki/CLAUDE.md` 和 `.claude/rules/wiki-ingest.md`
- [ ] Step 3e 引用 `.claude/rules/wiki-ingest-format.md`「Wiki 頁面呈現品質標準」
- [ ] Step 6b 錨點驗證表存在
- [ ] Step 6d 指向 `.claude/rules/wiki-ingest-format.md` 及 `wiki-ingest-*.md` 中的 `[加入:]` 標記
- [ ] Step 6e 分別檢查 `wiki/CLAUDE.md`（閾值 80 行）和 `.claude/rules/wiki-ingest.md`（閾值 80 行）

**news-pipeline-steps.md**
- [ ] Step 2 明確讀取 `wiki/CLAUDE.md` + `.claude/rules/wiki-ingest.md`
- [ ] Step 2 有 4 個子項目（分類、讀取、派工、彙整）
- [ ] Step 6 log 寫入步驟存在

---

## 循環規則

```
do {
  執行檢查 1 → 2 → 3
  if 發現任何 ❌:
    立即修正
    重新從檢查 1 開始
} while (本輪有 ❌)

輸出最終報告
```

**不可在仍有 ❌ 的情況下跳過任何檢查或提前結束。**

---

## 最終報告格式

```
## /review-commands 完成報告

| 檢查項目 | 結果 |
|---------|------|
| 1a 裸露 CLAUDE.md 引用 | ✅ 無 / ❌ N 處已修正 |
| 1b 明確路徑檔案存在 | ✅ 全部存在 / ❌ N 個已修正 |
| 1c 錨點引用有效 | ✅ 全部有效 / ❌ N 個已修正 |
| 2 載入鏈完整 | ✅ 3/3 完整 / ❌ N 個已修正 |
| 3 關鍵步驟存在 | ✅ 全部存在 / ❌ N 個已修正 |

迭代次數：X 輪
本輪修正：（列出修正項目，若無則寫「無」）
狀態：✅ 全部通過，零錯誤
```
