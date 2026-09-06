# Wiki Ingest — 商業 Lint 指南（主編層）

`/wiki-lint` 步驟 5e 由**主編**載入，維護 `wiki/entities/pricing.md` 的 `## 通路與乘數` 區塊。每日 ingest 不需讀此檔。

---

## 為什麼這條規則不在 `.claude/rules/wiki-ingest-commercial.md` `[加入: 2026-08-29]`

pricing 的前三個彙整區塊（我的方案現在有什麼／模型 API 定價現況／當前生效的計費規則）吃的是**日報條目**，由商業記者於每日 ingest 維護。

「通路與乘數」不同——它的進料是 **`platform.claude.com` 與各雲端平台的官方計價文件**，不在日報來源清單內。而 `.claude/rules/wiki-ingest-commercial.md` 的「官方文件查證優先於媒體轉述」已明訂：**記者無 web 工具**，遇此類事實只能回報主編查證。把這個區塊寫成記者的每日責任，會製造一個永遠空著、且記者每天回報「無法處理」的區塊。

> 判斷式：這個區塊的答案在**日報**裡，還是在**官方文件**裡？在日報 → 記者 daily；在官方文件 → 主編 lint。

---

## 維護規則（主編，每次 `/wiki-lint`）

### 要維持的兩張表

1. **通路對照**——同一個模型經不同通路，費率制定者、計費單位與可用功能都不同。欄位固定：`通路｜誰營運｜誰定價｜計費單位｜取不到的計費手段`。涵蓋：Claude API（第一方）、Claude Platform on AWS、Amazon Bedrock、Google Cloud／Vertex AI、Microsoft Foundry
2. **乘數對照**——一條一乘數：`乘數｜倍率｜套用範圍｜觸發條件`。涵蓋快取寫入／命中、Batch、資料落地（`inference_geo`）、地區端點、fast mode、長脈絡（**分世代**）

### 複查動作

| 檢查 | 動作 |
|---|---|
| 表上方「資料截至 YYYY-MM-DD」距今 > 30 天 | WebFetch 官方定價頁與平台可用性頁複查，一致則只更新查證日 |
| 新模型世代發布 | 確認長脈絡是否仍不加價、tokenizer 是否再換代；後者回報模型記者（`.claude/rules/wiki-ingest-models.md` I 條）|
| 日報出現通路政策變動或乘數異動 | 以日報為**線索**，仍須 WebFetch 官方原文確認後才寫入，並標來源連結與查證日 |
| 通路表任一列的計費手段或上限有異動 | 同批回掃 [[topics/anthropic-business]]「哪個合作會改到你用的 Claude」的引用快照與「資料截至」日 |

### 紀律

- **儲存格 ≤ 120 字元**（同 pricing 既有紀律）：通路的功能缺項清單、乘數的適用細節一律下沉表下條列
- **partner 通路（Bedrock、Google Cloud）的絕對數字不寫入**——費率由該平台自訂且各自調整，抄下來即過期且無人複查，比不寫更糟。只寫「由該平台自訂」＋官方定價頁連結
- **功能落差不在本區塊展開**：某通路取不到哪些功能，只列**影響計費的那幾項**（如 Bedrock 無 Message Batches API ⇒ 拿不到 Batch 折扣）；完整功能落差屬 [[entities/claude-code]]，加 wikilink 不複製（同 `wiki/CLAUDE.md`「每個事實只有一個家」）
- **模型間的選型換算不在本頁**：「同一份工作換個模型差多少」屬 [[topics/model-comparison]] 的 `## 同一份工作，換設定差多少`，加 wikilink 指過去
- 通路的功能可用性若影響**升版或遷移決策**（如某通路取不到 compaction／context editing），走 `data/pending-handoffs.jsonl` 轉知功能記者評估是否同步 feature-radar 升版風險

### 本區塊為非新聞性維護

只更新 pricing 的「最後更新」，**不動「最後新聞更新」**。
