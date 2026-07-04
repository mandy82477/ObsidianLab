---
description: 驗證所有 commands / rules / CLAUDE.md 修改後，相關指令仍可正確執行。持續循環直到零錯誤。
---

# Review Commands

每次修改 `.claude/commands/`、`.claude/rules/` 或 `CLAUDE.md` 後執行。
**終止條件：完整跑完一輪所有檢查，零 ❌，才可結束。每發現一個 ❌ 立即修正，然後從頭重新開始整輪。**

---

## 同步配對註冊表

以下配對描述「同一行為在兩處定義」，任一方修改時必須同步檢查另一方是否仍一致。**新增或修改任何配對其中一方時，必須同步檢查另一方；新配對出現時必須登記進此表。**

| 配對 | 必須一致的內容 | 驗證 grep |
|------|--------------|----------|
| `.claude/commands/news-pipeline.md` spawn 模板 ↔ `.claude/commands/news-pipeline-steps.md` | 記者派工 foreground 例外（不可設 `run_in_background: true`）；REPO_ROOT / PYTHON 設定值一致 | `grep -n "run_in_background: true\|REPO_ROOT\s*=\|PYTHON\s*=" .claude/commands/news-pipeline.md .claude/commands/news-pipeline-steps.md` |
| `.claude/commands/news-pipeline-steps.md` Step 2 ↔ `.claude/commands/wiki-ingest.md` | 兩檔皆明文「精簡複本，修改任一方必須同步另一方」 | `grep -n "精簡複本" .claude/commands/news-pipeline-steps.md .claude/commands/wiki-ingest.md` |
| `.claude/commands/wiki-ingest.md` / `.claude/commands/wiki-lint.md` 派工段 ↔ `.claude/rules/wiki-ingest.md` 類別對應表 | 六類 subagent_type 名稱一致；派工呼叫皆帶 `model: "sonnet"` | `grep -n "wiki-reporter-\|model: \"sonnet\"" .claude/commands/wiki-ingest.md .claude/commands/wiki-lint.md .claude/rules/wiki-ingest.md` |
| `.claude/rules/wiki-ingest-community.md` ↔ `.claude/rules/wiki-ingest-community-lint.md` | lint-only 規則分離邊界（`community-tech-tools.md` 明文標註「已脫離每日 ingest」/「lint 專用」）| `grep -n "已脫離每日 ingest\|lint 專用\|每日 ingest 不" .claude/rules/wiki-ingest-community.md .claude/rules/wiki-ingest-community-lint.md` |
| `.claude/rules/wiki-reporter-shared.md` 回報格式 ↔ 各 `.claude/rules/wiki-ingest-[category].md` 回報格式段 | 六份回報格式段皆含「更新頁面 / feature-radar 新增 / index.md 狀態變更 / 新增頁面 / 同步自查」五欄 | `grep -n "更新頁面：\|feature-radar 新增：\|index.md 狀態變更：\|新增頁面：\|同步自查：" .claude/rules/wiki-reporter-shared.md .claude/rules/wiki-ingest-*.md` |

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
| `wiki-ingest.md` | `wiki/CLAUDE.md` + `.claude/rules/wiki-ingest.md` | Step 1 的讀取清單 |
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

### 檢查 4：一致性斷言（依同步配對註冊表）

對「同步配對註冊表」每一組配對，執行其驗證 grep，確認雙方輸出語意一致（非僅字面相同，需人工判讀 grep 結果）：

| 配對 | 斷言 |
|------|------|
| news-pipeline.md ↔ news-pipeline-steps.md | 兩檔都含 `run_in_background: true` 前綴否定語（「不可設」）與 foreground 字樣；REPO_ROOT、PYTHON 兩檔數值逐字相同 |
| news-pipeline-steps.md Step 2 ↔ wiki-ingest.md | 兩檔都含「精簡複本」與「同步另一方」語意 |
| wiki-ingest.md / wiki-lint.md ↔ wiki-ingest.md 類別對應表 | 三處六類 subagent_type 名稱集合相同；派工段都含 `model: "sonnet"` |
| wiki-ingest-community.md ↔ wiki-ingest-community-lint.md | community.md 明文排除 tools 頁每日更新；community-lint.md 明文承接 tools 頁策展 |
| wiki-reporter-shared.md ↔ 各 wiki-ingest-[category].md | 六份回報格式段五欄字串（更新頁面/feature-radar 新增/index.md 狀態變更/新增頁面/同步自查）皆出現 |

任一斷言失敗 → 標記 ❌，修正後**從檢查 1 重新開始整輪**。

---

## 循環規則

```
do {
  執行檢查 1 → 2 → 3 → 4
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
| 4 一致性斷言（同步配對）| ✅ 5/5 通過 / ❌ N 個已修正 |

迭代次數：X 輪
本輪修正：（列出修正項目，若無則寫「無」）
狀態：✅ 全部通過，零錯誤
```
