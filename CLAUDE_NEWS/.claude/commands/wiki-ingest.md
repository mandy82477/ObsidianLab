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

**再取懸置標記命中偵測結果 `[加入: 2026-08-10]`：** 若當日 `/news-pipeline` 已跑過 Step 3f，直接取用其 stdout 印出的派工附件（依記者分組的「待查證命中」清單）；若無此輸出（如單獨補跑 `/wiki-ingest`），自行執行：

```
python scripts/scan_pending_verifications.py $ARGUMENTS
```

輸出依記者類別分組，供下一步派工時原樣附在對應記者的訊息裡；某類別無命中則該記者派工訊息此區塊寫「無」。規格見 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節。

**再取轉知待接手清單 `[加入: 2026-08-15]`：** 執行 `python scripts/pending_handoffs.py list`，輸出依目標記者分組，派工時附在對應記者訊息的「轉知待接手」區塊；無則寫「無」。這是先前 ingest 的記者「⚠️ 需主編轉知」經主編登帳後的未結案項（帳本 `data/pending-handoffs.jsonl`，規格見 `.claude/rules/wiki-ingest.md`「第三步」轉知帳本段）。

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/rules/wiki-ingest.md` — 分類標準與派工流程（主編指南）
- `wiki/index.md` — 取得所有現有頁面清單
- `wiki/log.md` — 確認最近是否已處理過同一份日報（避免重複 ingest）

### 2. 分類（主編）

讀完**日報條目 + 上一步列出的未收錄條目**後，依 `.claude/rules/wiki-ingest.md` 的分類表為每則新聞標記類別。
跨類別條目可標多個類別。

未進日報的條目在原文節錄中標一行 `- **日報未收錄**（僅原始抓取資料，摘要較簡略）`，讓記者知道細節密度不同、判斷時以自己的類別門檻為準。

**專頁定向抓取的條目（`topic` 欄非空）`[加入: 2026-08-13]`**：`gathered_items.json` 中 `topic` 非空者，是為某個 wiki 專頁定向抓來的（來源標籤 `Topic Watch / <slug>`），**直接路由給該 slug 所屬領域的記者**，不必再走類別判斷。原文節錄中標一行 `- **專頁定向**（目標頁：topics/<slug>；收錄判準為該專頁觸發條件，**不套用 Claude/Anthropic 關聯門檻**）`。

> 這批的標題天生不含 Claude/Anthropic——那正是它們被定向抓來的原因（2026-08-05 Jeff Dean 等人離開 Google 創辦 Discovery Loop，因標題是 Google 視角而被 12 個來源全數漏掉 8 天）。記者**不得因為「跟 Claude 沒關係」而略過**，但仍須依該專頁自己的觸發條件判斷收不收——不收可以，沒看過不行。

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

**對每個有條目的類別，呼叫 Agent tool**。有多個類別時，在同一訊息中同時發出所有 Agent 呼叫（並行執行）。每個呼叫一律 **`subagent_type: "general-purpose"` + `model: "sonnet"`**（本機與雲端唯一正典派工路徑，理由見 `.claude/rules/wiki-ingest.md`「派工方式」；sonnet 因分類與頁面更新為有界任務，不需旗艦模型；未指定會繼承主 session 模型，六記者並行足以打穿訂閱配額）。

> ⚠️ **記者 agent 必須以 foreground（同步）方式啟動，不可設 `run_in_background: true`。** 背景記者的完成通知無法回到派工 agent，會造成永久等待。

| 類別 | 角色檔（`.claude/agents/`） |
|------|--------------|
| 模型 | `wiki-reporter-models` |
| 功能 | `wiki-reporter-features` |
| 商業 | `wiki-reporter-commercial` |
| 安全政策 | `wiki-reporter-safety-policy` |
| 社群 | `wiki-reporter-community` |
| 人物 | `wiki-reporter-people` |

每個 Agent 呼叫的 prompt 傳入（第一段角色前導不可省略——它是記者拿到規則的唯一途徑）：

```
你是 CLAUDE_NEWS wiki 的「[類別]」記者。開工前先 Read `.claude/agents/wiki-reporter-[category].md`——那是你的角色定義（含「開始前必讀」規則清單與回報契約），逐條照做後再處理下面的任務。你不可再呼叫 Agent tool 委派任何工作。

今日日報日期：[YYYY-MM-DD]
你負責的分類條目原文節錄：

[貼入 Step 2 整理好的該類別條目區塊]

你負責頁面今日命中的待查證項目（機械偵測，可能誤判；無則寫「無」）：

[貼入掃描器輸出中該類別的區塊，無命中該類別則寫「無」]

轉知待接手（其他記者先前交辦給你的事；無則寫「無」）：

[貼入 `python scripts/pending_handoffs.py list --to [類別]` 的輸出]
```

**防偏誤說明（隨每次派工附上，不可省略）：** 此清單僅供比對——若今日條目足以作為某筆懸置的後續，在該標記加 `｜訊 YYYY-MM-DD` 並更新內文；證據不足則不動並在回報說明。**不可為了消化懸置而過度解讀新聞；不可刪標記、改狀態符號或宣告結案**（結案屬 `/wiki-lint` 5c）。

記者的角色、規則引用、回報格式只定義在角色檔 `.claude/agents/wiki-reporter-[category].md`（單一來源），由上方角色前導導入；派工 prompt 不重抄規則內文。

**🚫 prompt 內不得臨場加寫「今日順手做 X」「記得同步 Y 頁」這類操作指示**——上方五個區塊（角色前導／日期／條目節錄／待查證命中／轉知待接手）加防偏誤說明即為完整 prompt，不再增加。針對單一條目的事實性提示寫在該條目的 `- **註：**` 行內。理由與 2026-08-15 教訓見 `.claude/rules/wiki-ingest.md`「派工 prompt 不得臨場加寫操作指示」。

### 4. 彙整共用檔案（主編）

收到所有記者回報後，統一更新共用檔案：

**`wiki/feature-radar.md`**
- 彙整模型 + 功能記者回報的所有 feature-radar 新增條目
- 依 `.claude/rules/wiki-ingest-features.md` 的條目格式寫入「最新功能」區塊
- 同步更新全覽表的熱度與試用價值
- 依 `.claude/rules/wiki-ingest-features.md`「⭐ 現在值得跟的三件 自動更新規則」覆寫 `## ⭐ 現在值得跟的三件` section
- 依 `.claude/rules/wiki-ingest-features.md`「⚠️ 從你現在的版本升上去，會遇到什麼 自動更新規則」更新 `## ⚠️ 從你現在的版本升上去，會遇到什麼` section

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

**`data/pending-handoffs.jsonl`**（轉知帳本，append only，透過腳本操作）
- 記者回報「轉知處置」欄的「已處理」→ 逐筆 `python scripts/pending_handoffs.py close H-xxxxxx --by [類別] --result "[一句話]"`；「不適用」→ 判斷：理由成立則 `void`，理由是「不屬我」則保留 open 並改派（重新 `open` 給正確類別後 `void` 原筆）
- 記者回報「同步自查」欄出現 `⚠️ 需主編轉知[目標類別]記者：…` 且目標是**另一位記者**（非主編自己的彙整工作）→ `python scripts/pending_handoffs.py open --from [來源類別] --to [目標類別] --page [頁面] --note "[要做什麼]"`；今日就能在同一輪派工內解決的（目標記者尚未派出）可直接附進其派工訊息並同時登帳
- 主編自己要做的（feature-radar、index、commitments）不登帳，照第 4 步做

**`wiki/overview.md`**（視情況）
- 若有重大事件（新模型發布、重大政策變化），更新「當前局勢」段落

### 4b. devpractice 沉澱派工（主編）`[加入: 2026-09-02]`

彙整完成後（wiki 檔案已定稿），派 devpractice 記者做每日沉澱——他不吃日報條目，吃**本輪 ingest 寫進 wiki 的 diff**，所以必須排在彙整之後。以 `subagent_type: "general-purpose"` + `model: "sonnet"` 派出，prompt 首段：

```
你是 CLAUDE_NEWS wiki 的「開發實務（devpractice）」記者。開工前先 Read `.claude/agents/wiki-reporter-devpractice.md`——那是你的角色定義，逐條照做後執行 **daily 沉澱**。今日日期：[YYYY-MM-DD]。你不可再呼叫 Agent tool 委派任何工作。
```

收報後把「候選 N 筆／本日無候選」記入 log.md 本次 ingest 紀錄一行 `devpractice 沉澱：…`；`data/devpractice-candidates.jsonl` 與 `data/devpractice_state.json` 併入收尾 commit（雲端與本機共用同一條 diff 基準線，不 commit 會斷）。

### 4c. market 判讀派工（主編）`[加入: 2026-09-05]`

與 4b 同批派出（兩者互不相干，可並行）。投資分析記者不吃分類路由，吃**當日日報本身**換市場框架重讀，但判讀要 wikilink 指向已定稿的事實頁，故同樣排在彙整之後。以 `subagent_type: "general-purpose"` + `model: "sonnet"` 派出，prompt 首段：

```
你是 CLAUDE_NEWS wiki 的「投資分析（market）」記者。開工前先 Read `.claude/agents/wiki-reporter-market.md`——那是你的角色定義，逐條照做後執行 **daily 判讀**。今日日期：[YYYY-MM-DD]。你不可再呼叫 Agent tool 委派任何工作。
```

其後附今日日報條目節錄（與六記者同一份 Step 2 產物，不另篩）。收報後把「判讀 N 則／本日無訊號」記入 log.md 本次 ingest 紀錄一行 `market 判讀：…`；記者回報的來源歸因照第 4 步 append 至 `data/source_attribution.jsonl`（slug 用該則日報條目的來源，不是 `user-query`）。

### 5. 完成前強制核對清單

**在宣告完成之前，逐項確認所有項目已完成。**

- [ ] 每個有條目的類別均已派工，記者回報已收齊
- [ ] 六記者回報的「待查證命中處置」欄皆有值（已標訊／證據不足不動／無命中，三選一，不可空白或省略）
- [ ] 六記者回報的「轉知處置」欄皆有值，且已處理者已 `close`、新轉知已 `open` 登帳（`python scripts/pending_handoffs.py list` 的結果與記者回報一致）
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
