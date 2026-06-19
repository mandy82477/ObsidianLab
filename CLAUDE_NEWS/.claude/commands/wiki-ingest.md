---
description: 讀取今日日報並更新 wiki 知識庫。每天聚合器執行後使用。
argument-hint: [YYYY-MM-DD]
---

# Wiki Ingest

讀取今日日報，以多記者架構更新 wiki 知識庫。

> ⚠️ 本檔的 ingest 步驟在 `.claude/commands/news-pipeline-steps.md` Step 2 有精簡複本，修改任一方時必須同步另一方。

## 步驟

### 1. 確認今日日報與 wiki 現況

讀取 `news/$ARGUMENTS.md`（若無提供日期，使用今天的日期）。
若檔案不存在，停止並告知使用者。

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/rules/wiki-ingest.md` — 分類標準與派工流程（主編指南）
- `wiki/index.md` — 取得所有現有頁面清單
- `wiki/log.md` — 確認最近是否已處理過同一份日報（避免重複 ingest）

### 2. 分類（主編）

讀完日報所有條目後，依 `.claude/rules/wiki-ingest.md` 的分類表為每則新聞標記類別。
跨類別條目可標多個類別。

分類完成後，為每個有條目的類別整理原文節錄（格式如下）：

```
## [類別] 條目（共 N 則）

### [條目標題]
- **來源：** [媒體/平台]
- **日期：** YYYY-MM-DD
- **摘要：** [原文關鍵內容，保留數字、版本號、具名企業等細節]
- **原文重點：** [直接引用日報中的關鍵段落，不壓縮細節]

### [下一則...]
```

無條目的類別標記「無」，不派工。

### 3. 派工（Agent tool）

**對每個有條目的類別，呼叫 Agent tool**。有多個類別時，在同一訊息中同時發出所有 Agent 呼叫（並行執行）。

| 類別 | subagent_type |
|------|--------------|
| 模型 | `wiki-reporter-models` |
| 功能 | `wiki-reporter-features` |
| 商業 | `wiki-reporter-commercial` |
| 安全政策 | `wiki-reporter-safety-policy` |
| 社群 | `wiki-reporter-community` |
| 人物 | `wiki-reporter-people` |

每個 Agent 呼叫的 prompt 傳入：

```
今日日報日期：[YYYY-MM-DD]
你負責的分類條目原文節錄：

[貼入 Step 2 整理好的該類別條目區塊]
```

記者的角色、規則引用、回報格式已定義在各 agent 的 system prompt（`.claude/agents/wiki-reporter-[category].md`）中。

### 4. 彙整共用檔案（主編）

收到所有記者回報後，統一更新共用檔案：

**`wiki/feature-radar.md`**
- 彙整模型 + 功能記者回報的所有 feature-radar 新增條目
- 依 `.claude/rules/wiki-ingest-features.md` 的條目格式寫入「最新功能」區塊
- 同步更新全覽表的熱度與試用價值

**`wiki/index.md`**
- 彙整所有記者回報的 `index.md 狀態變更` 欄位，逐一更新
- 彙整所有記者回報的 `新增頁面` 欄位，在對應分類下補上新連結

**`wiki/log.md`**（append only，不可修改既有條目）
```
## YYYY-MM-DD Ingest

- 來源日報：[[news/YYYY-MM-DD]]
- 更新頁面：（彙整所有記者的「更新頁面」列表）
- 新增頁面：（彙整所有記者的「新增頁面」，若無則寫「無」）
- 摘要：（一句話說明今日主要新聞方向）
- 呈現品質：（彙整所有記者的品質審查結果；全數通過則寫「全部通過」）
```

**`wiki/overview.md`**（視情況）
- 若有重大事件（新模型發布、重大政策變化），更新「當前局勢」段落

### 5. 完成前強制核對清單

**在宣告完成之前，逐項確認所有項目已完成。**

- [ ] 每個有條目的類別均已派工，記者回報已收齊
- [ ] feature-radar.md 已彙整更新（無新功能則標「本日無新功能」）
- [ ] wiki/index.md 狀態已全部同步（含所有記者回報的狀態變更）
- [ ] wiki/log.md 已 append 本次 ingest 紀錄（含品質審查彙整，未修改既有條目）
- [ ] 未在 `CLAUDE_NEWS/wiki/` 以外路徑建立或修改任何 wiki 檔案

完成後輸出摘要：

| 項目 | 內容 |
|------|------|
| 日報來源 | news/YYYY-MM-DD |
| 參與記者 | [有條目的類別列表] |
| 更新頁面 | [彙整列表] |
| 新增頁面 | [列出或「無」] |
| feature-radar 變動 | [功能名稱與熱度變化，或「無」] |
| 今日主要方向 | [一句話摘要] |

## 注意事項

- 繁體中文為主，英文術語保留英文
- 所有 wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下
- `news/` 目錄為唯讀，不可修改日報內容
- 若日報今日無新內容（來源全部失敗），在 log.md 記錄一筆「無新內容」即可
