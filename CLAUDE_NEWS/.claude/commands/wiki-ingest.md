---
description: 讀取今日日報並更新 wiki 知識庫。每天聚合器執行後使用。
argument-hint: [YYYY-MM-DD]
---

# Wiki Ingest

讀取今日日報，以多記者架構更新 wiki 知識庫。

> `/news-pipeline` 的 Step 2 直接呼叫本檔案執行（見 `.claude/commands/news-pipeline.md` Phase B），不再維護獨立副本——修改本檔案的分類、派工或彙整邏輯時，`/news-pipeline` 會自動套用最新版本，不需同步修改其他檔案。

## 步驟

### 1. 確認今日日報與 wiki 現況

讀取 `news/$ARGUMENTS.md`（若無提供日期，使用今天的日期）。
若檔案不存在，停止並告知使用者。

**再取當日「未進日報」的條目（強制）`[加入: 2026-07-26]`：**

```
python scripts/list_digest_omissions.py --date $ARGUMENTS
```

**日報是給讀者看的，只留讀者要讀的重點，篩掉一部分是預期行為；但 wiki 是沉澱層，要考慮全部。** 收不收由各類別記者依自己的門檻判斷——**不收可以，沒看過不行**。上述指令列出的條目與日報條目一起進入下一步分類。

（2026-07-25 踩過：抓料 73 則、日報收 38 則，其餘 35 則因為 ingest 的輸入只有日報，包含 61 留言與 47 留言的 GitHub Issue 在內，沒有任何記者看過。）

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/rules/wiki-ingest.md` — 分類標準與派工流程（主編指南）
- `wiki/index.md` — 取得所有現有頁面清單
- `wiki/log.md` — 確認最近是否已處理過同一份日報（避免重複 ingest）

### 2. 分類（主編）

讀完**日報條目 + 上一步列出的未收錄條目**後，依 `.claude/rules/wiki-ingest.md` 的分類表為每則新聞標記類別。
跨類別條目可標多個類別。

未進日報的條目在原文節錄中標一行 `- **日報未收錄**（僅原始抓取資料，摘要較簡略）`，讓記者知道細節密度不同、判斷時以自己的類別門檻為準。

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

**對每個有條目的類別，呼叫 Agent tool**。有多個類別時，在同一訊息中同時發出所有 Agent 呼叫（並行執行）。每個呼叫必須帶 `model: "sonnet"`（分類與頁面更新為有界任務，不需旗艦模型；未指定會繼承主 session 模型，六記者並行足以打穿訂閱配額）。

> ⚠️ **記者 agent 必須以 foreground（同步）方式啟動，不可設 `run_in_background: true`。** 背景記者的完成通知無法回到派工 agent，會造成永久等待。

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
- 依 `.claude/rules/wiki-ingest-features.md`「本週推薦自動更新規則」覆寫 `## ⭐ 本週推薦` section
- 依 `.claude/rules/wiki-ingest-features.md`「升版風險自動更新規則」更新 `## ⚠️ 升版風險` section

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
- 品質備註：（若彙整時發現記者品質問題——回報含糊、漏同步自查、格式退化等——每項一行 `[類別] [問題型態一句話]`；無問題則不寫此行）
```

**`data/source_attribution.jsonl`**（append only，不可修改既有行）
- 把所有記者回報的「來源歸因」欄逐筆轉成一行 JSON append，schema 與 slug 對照見 `.claude/rules/wiki-ingest.md`「第三步」與 `data/README.md`
- 記者回報「無」則該記者不寫；全部記者皆「無」則不動此檔

**`wiki/overview.md`**（視情況）
- 若有重大事件（新模型發布、重大政策變化），更新「當前局勢」段落

### 5. 完成前強制核對清單

**在宣告完成之前，逐項確認所有項目已完成。**

- [ ] 每個有條目的類別均已派工，記者回報已收齊
- [ ] feature-radar.md 已彙整更新（無新功能則標「本日無新功能」）
- [ ] wiki/index.md 狀態已全部同步（含所有記者回報的狀態變更）
- [ ] wiki/log.md 已 append 本次 ingest 紀錄（含品質審查彙整，未修改既有條目）
- [ ] data/source_attribution.jsonl 已 append 所有記者回報的來源歸因（每筆一行 JSON；全部回報「無」則跳過）
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
- **收件匣提醒**：ingest 完成後檢查 `wiki/reader-notes.md`，若有狀態 ⏳ 且距今 > 14 天的項目，在完成摘要末尾列出提醒（避免使用者「記一下」的想法積壓無人處理）；無則不提
