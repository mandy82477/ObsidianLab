# Wiki Ingest 主編指南

執行 `/wiki-ingest`、`/wiki-lint`、`/news-pipeline` 時讀取此檔案。
**主編職責：分類 → 派工 → 彙整共用檔案。** 頁面格式模板見 `.claude/rules/wiki-ingest-format.md`。

---

## 第一步：分類

讀完日報所有條目後，為每則標記類別（可標多個）：

| 類別 | 分類標準 |
|------|---------|
| **模型** | 模型發布、模型能力評測、模型棄用、模型版本迭代 |
| **功能** | Claude Code 版本 / 指令 / 旗標、SDK 變更、Breaking change、官方 beta 功能 |
| **商業** | 融資、收購、合作、企業採用 / 退出、計費政策、成本案例 |
| **安全政策** | 安全事件 / 漏洞、政府政策、出口管制、軍事合約 |
| **社群** | 社群工具（Show HN / score ≥ 30）、技術討論、工作流模式 |
| **人物** | Anthropic 人員動態、重要外部人物言論 / 加入 / 離開 |

跨類別條目標記多個類別——各記者只負責自己那一面。

---

## 第二步：派工

依分類結果，對每個有條目的類別呼叫 Agent tool，傳入今日日期與該類別的**原文節錄**（保留數字、版本號、具名企業等細節，不壓縮）。有多個類別時同一訊息並行發出。

記者的角色、規則引用、回報格式已定義在 `.claude/agents/wiki-reporter-[category].md` 的 system prompt 中，派工時無需重複指示。

| 類別 | subagent_type |
|------|--------------|
| 模型 | `wiki-reporter-models` |
| 功能 | `wiki-reporter-features` |
| 商業 | `wiki-reporter-commercial` |
| 安全政策 | `wiki-reporter-safety-policy` |
| 社群 | `wiki-reporter-community` |
| 人物 | `wiki-reporter-people` |

---

## 第三步：彙整共用檔案

收到所有記者回報後，統一更新：

**`wiki/feature-radar.md`**：彙整模型 + 功能記者回報的新增條目，依 `.claude/rules/wiki-ingest-features.md` 格式寫入（含本週推薦、升版風險、⏰ 倒數中三個 section）。

**`wiki/topics/anthropic-commitments.md`**：任一記者回報中出現「官方承諾修復 / 承諾政策 / 明確拒絕 / 兌現先前承諾」事件時，更新追蹤表對應列的狀態與最後檢查日；新承諾則新增列；兌現或死案移入「已結案」。無相關事件則不動此頁。

**`wiki/index.md`**：彙整所有記者回報的狀態變更與新增頁面列。

**`wiki/log.md`**（append only）：寫入完整 ingest 紀錄，含所有記者回報摘要與品質審查結果。

**`wiki/overview.md`**：若有重大事件（新模型發布、重大政策變化），更新「當前局勢」段落。

---

## 記者回報格式（標準化）

每個記者完成後必須輸出：

```
## [類別] 記者回報
更新頁面：[list]
feature-radar 新增：[條目標題 or 無]
index.md 狀態變更：[page: 舊狀態 → 新狀態 or 無]
新增頁面：[filepath or 無]
同步自查：[✅ 已同步 / ⚠️ 需主編轉知（說明）/ 不適用]
```

主編依此格式彙整，確保不遺漏任何狀態變更。
