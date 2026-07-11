---
description: 驗證所有 commands / rules / CLAUDE.md 修改後，相關指令仍可正確執行。持續循環直到零錯誤。
---

# Review Commands

每次修改 `.claude/commands/`、`.claude/rules/` 或根目錄 `CLAUDE.md` 後執行。
**終止條件：`python scripts/check_rules.py` 零 ❌ 才可結束。**

---

## 執行成本原則

規則一致性的機械檢查（裸露引用、路徑存在性、錨點、同步配對）已全部收斂進 `scripts/check_rules.py`（純 Python stdlib，跨平台，掛在 `scripts/run_tests.py` 內一併執行）。本指令**只做失敗判讀與修復**，不再手動 grep 或逐檔通讀——任何模型都可執行，不需旗艦模型。

---

## 步驟

### 1. 執行機械檢查

```
python scripts/check_rules.py
```

- exit 0 → 讀報告確認全部 ✅（含 warn-only 的 coupling hints），直接跳到「輸出完成報告」
- exit 1 → 進入步驟 2

### 2. 逐項判讀失敗

對每個 ❌，判斷屬於哪一種：

| 失敗類型 | 判讀 | 動作 |
|---------|------|------|
| 檔案內容真的錯了（裸露引用、路徑打錯、步驟被刪、格式漂移）| 真問題 | 修正該檔案 |
| 檢查本身過時（措辭改了但語意仍對、路徑合理搬遷）| registry 過時 | 修正 `.claude/review-registry.json` 對應項目 |

**修正檔案前**先讀 `.claude/rules/claude-md-edit.md`（路徑引用原則、反向查詢）。
**修正 registry 前**確認不是在「放水」掩蓋真問題——若不確定，先當真問題處理。

修正後回到步驟 1，重跑直到零錯誤。

### 3. Coupling hints（warn-only，不阻塞）

若報告列出「檢查 5：coupling hints」的高頻互引檔案對，判斷是否為真實耦合：
- 是 → 在 `.claude/review-registry.json` 的 `sync_pairs` 新增一組配對（登記其「必須一致的內容」）
- 否（只是一般提及，非需同步的耦合）→ 略過，不需登記

### 4. 維護規則

**新增同步配對或錨點時，登記進 `.claude/review-registry.json`**（`sync_pairs` / `anchors` / `bare_references.line_allowlist` / `path_existence.allowlist_patterns`），不要另外維護紙本註冊表——registry 本身就是唯一事實來源，`scripts/check_rules.py` 直接讀取執行。

---

## 輸出完成報告

```
## /review-commands 完成報告

python scripts/check_rules.py：✅ 零錯誤 / ❌ → 已修正

| 檢查項目 | 結果 |
|---------|------|
| 1 裸露引用 | ✅ / ❌ N 處已修正 |
| 2 路徑存在性 | ✅ / ❌ N 個已修正 |
| 3 錨點 | ✅ / ❌ N 個已修正 |
| 4 同步配對 | ✅ N/N 通過 |
| 5 coupling hints | ✅ 無新耦合 / 已登記 N 組 |

本輪修正：（列出修正的檔案與原因，若無則寫「無」）
狀態：✅ 全部通過，零錯誤
```
