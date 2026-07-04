---
description: 改版前後品質對照：管線/日報格式/收錄門檻改動時，改前記錄基線、改後對照差異並做舊資料回歸，防止改版靜默劣化產出。
argument-hint: baseline | compare
---

# Pipeline Change Check

修改 `src/news_aggregator/`、`scripts/build_web.py`、`.claude/commands/news-pipeline-steps.md` 的日報格式區、或收錄門檻規則（`.claude/rules/wiki-reporter-shared.md` 互動門檻對照表）**之前與之後**執行，防止改版靜默劣化產出。依 `$ARGUMENTS` 分兩種模式。

---

## 指標組（兩模式共用）

用 inline Python 從最新一份 `web_reader/data/digest/*.json` 計算：

- `articleCount`（文章數）
- `sourceStatus` 各來源 ok/count（來源分布；目前欄位可能為空陣列，仍須回報長度）
- 各區塊條目數：`focus` / `topStories` / `techUpdates` / `mediaReports` / `discussions` / `billing`
- `discussions` 條目中含 `sentiment` 非空值的比率（格式健康 proxy）
- 各區塊條目中 `body` 非空的比率（解析健康 proxy）

---

## 模式一：`baseline`（改動前）

1. 用 Bash 找出 `web_reader/data/digest/` 目錄下日期最新的 JSON 檔
2. inline Python 讀取該檔，計算上述指標組
3. 記錄當下 `git rev-parse HEAD`
4. 寫入 `src/logs/pipeline_baseline.json`，含：快照建立時間、對應 digest 日期、指標組、git HEAD hash

`src/logs/` 已被 repo 根目錄（`ObsidianLab/.gitignore`）的 `logs/` 規則涵蓋，`pipeline_baseline.json` 屬工作狀態不需 commit，也不需另外調整 `.gitignore`。

## 模式二：`compare`（改動後、首次跑完 pipeline 之後）

1. 讀取 `src/logs/pipeline_baseline.json`；不存在則提示先跑 `baseline` 並中止
2. 對最新一份 digest 重算同組指標
3. 並排輸出差異表（baseline vs 現在），每項數值變動 ±30% 以上視為顯著差異，必須附一句解釋：
   - 能歸因於本次改動意圖 → 標 ✅（例如「dev.to 條目減少＝門檻生效」）
   - 無法歸因 → 標 ⚠️，於最終回報中列出交給使用者判斷
4. **舊資料回歸（必做）：**
   - 執行 `python scripts/build_web.py`，確認成功不報錯
   - inline Python 迴圈 load 全部 `web_reader/data/digest/*.json`，確認每份都能正確解析、無一 JSONDecodeError 或例外
5. 全部通過後提醒使用者：「連續 3 天留意文章數與來源分布；週期性異常由 `/wiki-lint` 的 6f 來源健康檢查接手。」

---

## 注意事項

- 本 skill 不執行 `python -m news_aggregator.main`（不重新抓新聞），只讀既有 digest JSON
- `baseline` 檔案是工作狀態快照，不是內容產物，不進 git
- 兩模式皆不修改 `wiki/`、`news/` 任何檔案
