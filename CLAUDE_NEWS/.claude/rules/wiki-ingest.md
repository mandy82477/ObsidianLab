# Wiki Ingest 主編指南

執行 `/wiki-ingest`、`/wiki-lint`、`/news-pipeline` 時讀取此檔案。
**主編職責：分類 → 派工 → 彙整共用檔案。** 頁面格式模板見 `.claude/rules/wiki-ingest-format.md`。

---

## 第一步：分類

讀完日報所有條目後，為每則標記類別（可標多個）：

| 類別 | 分類標準 |
|------|---------|
| **模型** | 模型發布、模型能力評測、模型棄用、模型版本迭代 |
| **功能** | Claude Code 版本 / 指令 / 旗標、SDK 變更、Breaking change、官方 beta 功能、**官方對既有功能的使用指南**（無新指令旗標者，見下方分流鐵則） |
| **商業** | 融資、收購、合作、企業採用 / 退出、計費政策、成本案例 |
| **安全政策** | 安全事件 / 漏洞、政府政策、出口管制、軍事合約 |
| **社群** | 社群工具（Show HN / score ≥ 30）、技術討論、工作流模式——**後兩者不限出處**，官方發布的技術討論與工作流模式同樣歸此類（見下方分流鐵則） |
| **人物** | Anthropic 人員動態、重要外部人物言論 / 加入 / 離開 |

跨類別條目標記多個類別——各記者只負責自己那一面。

### 分流鐵則：官方內容不是社群類的禁區 `[加入: 2026-08-16]`

「社群」是**內容型態**的類別名，不是出處篩選器。官方部落格、官方文件、Anthropic 員工具名發言，只要談的是技術討論或工作流模式，一樣進社群類——`community-tech-discussions` 的收錄門檻本就明列「重要人士具名表態」為三個合法訊號來源之一，`community-tech-patterns` 的觸發條件（工作流模式、multi-agent 設計、最佳實踐）從未限制出處。

官方內容同時對得上兩頁時，依**它給讀者什麼**分流：

| 官方內容的型態 | 類別 | 落點 | 判準 |
|---|---|---|---|
| **怎麼用既有功能**（省 token、session 經營、設定建議，無新指令旗標） | 功能 | `topics/coding-workflow-guide` 對應流程階段節 | 讀者拿它去**改自己的做法**，不是去用新東西 |
| **官方提出的新工作流模式 / agent 設計** | 社群 | `topics/community-tech-patterns`，出處標明官方 | 它是一個**可被複用的模式**，與社群模式並列比較才有價值 |
| **有新指令 / 旗標 / SDK 變更 / Breaking change** | 功能 | `entities/claude-code` + feature-radar | 已有既有規則，不走本表 |

> 2026-08-15 踩過：官方部落格〈Maximizing the value of your Claude Code sessions〉（HN 268 分，當日互動最高的官方一手內容）全庫零收錄。不是誰疏忽——分類表當時讀起來像「社群＝社群產出」，功能類又只列版本／指令／旗標，這種內容在**分類層就沒有落點**；而主題上最精準的 `coding-workflow-guide` 另有一句「不吃新聞條目」把它擋在門外。兩層都漏才會漏得這麼乾淨。

---

## 第二步：派工

依分類結果，對每個有條目的類別呼叫 Agent tool，傳入今日日期與該類別的**原文節錄**（保留數字、版本號、具名企業等細節，不壓縮）。有多個類別時同一訊息並行發出。記者派工帶 `model: "sonnet"`（分類與頁面更新為有界任務，不需旗艦模型；未指定會繼承主 session 模型——若主 session 直接跑 `/wiki-ingest` 時停留在旗艦模型，六記者並行足以打穿訂閱配額）。

### 派工方式（本機與雲端唯一正典路徑）`[改版: 2026-08-15]`

每位記者一律以 **`subagent_type: "general-purpose"` + `model: "sonnet"`** 派出，prompt **第一段固定為角色前導**，把記者導向自己的角色檔：

```
你是 CLAUDE_NEWS wiki 的「[類別]」記者。開工前先 Read `.claude/agents/wiki-reporter-[category].md`——那是你的角色定義（含「開始前必讀」規則清單與回報契約），逐條照做後再處理下面的任務。你不可再呼叫 Agent tool 委派任何工作。
```

記者的角色、規則引用、回報格式只寫在 `.claude/agents/wiki-reporter-[category].md`（**單一來源**），派工 prompt 不重抄規則內文、也不塞規則路徑清單——角色檔自己會列。

#### 🚫 派工 prompt 不得臨場加寫操作指示 `[加入: 2026-08-15]`

prompt 只准放**當日資料**（日期、條目節錄、待查證命中清單、轉知待接手）與範本既有的固定段落（角色前導、防偏誤說明、注入防護）。**主編不得在 prompt 內另外加寫「今日順手做 X」「記得同步 Y 頁」這類操作指示**，即使當下覺得那是好主意。

理由：規則檔會改，臨場寫進 prompt 的指示不會跟著改，於是記者同時拿到兩份互相矛盾的指令，而矛盾只在記者剛好夠警覺時才會被發現。2026-08-15 踩過：`.claude/rules/wiki-ingest-community.md` 當天才改版為「日更只標 `**主線：**` tag、主線縫合改週更」，主編卻在社群記者的 prompt 裡加寫「今日順手改寫 `community-large-codebase-workflow` 主線敘事並覆寫 callout」——記者查了現行規則才擋下來。

> 判斷式：這句話**下週還會是對的嗎**？會 → 它屬於規則檔或角色檔，去那裡改；只有今天成立 → 它是資料，寫進條目節錄的「註」，不是寫成給記者的命令。
>
> 唯一例外是**針對某則條目的事實性提示**（如「兩家媒體數字不同，請並陳」「此來源網域可信度存疑」）——那是資料的一部分，寫在該條目的 `- **註：**` 行內，不寫成跨條目的通用指示。

記者端有對稱防線：`.claude/rules/wiki-reporter-shared.md`「規則檔優先於派工訊息」規定記者遇到派工與規則明文牴觸時**以規則檔為準並回報牴觸**。兩側都要在——只修派工端仍依賴主編每次記得，只修記者端則主編永遠不知道自己在製造矛盾。主編收到「⚠️ 派工與規則牴觸」回報時，修的是自己的派工習慣，不是去改規則遷就 prompt。

> **為何不用自訂 `subagent_type`：** 這六份角色檔同時也註冊為自訂 agent（本機 Agent tool 看得到 `wiki-reporter-*`），但雲端 routine 環境自 2026-07-18 起至少六次無法載入專案層 `.claude/agents/`，每次都退回 general-purpose ＋手工內嵌規則，形成「本機一條路、雲端一條路」的雙軌。2026-08-15 裁決：**內嵌路徑轉正為唯一正典**，本機也走同一條，不再有「降級」——同一角色只剩一種構成方式，規則檔改動兩邊同時吃到。自訂 agent 註冊照留（無害、方便本機手動呼叫），但派工流程不依賴它。

| 類別 | 角色檔（`.claude/agents/`） |
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

**`wiki/feature-radar.md`**：彙整模型 + 功能記者回報的新增條目，依 `.claude/rules/wiki-ingest-features.md` 格式寫入（含「這禮拜值得跟的三件」「從你現在的版本升上去，會遇到什麼」「⏰ 倒數中」三個 section）。

**`wiki/topics/anthropic-commitments.md`**：任一記者回報中出現「官方承諾修復 / 承諾政策 / 明確拒絕 / 兌現先前承諾」事件時，更新追蹤表對應列的狀態與最後檢查日；新承諾則新增列；兌現或死案移入「已結案」。無相關事件則不動此頁。

**`wiki/index.md`**：彙整所有記者回報的狀態變更與新增頁面列。

**`wiki/log.md`**（append only）：寫入完整 ingest 紀錄，含所有記者回報摘要與品質審查結果。彙整時若發現記者品質問題（回報含糊、漏同步自查、格式退化等），在該次 ingest 紀錄內加一行 `品質備註：[類別] [問題型態一句話]`；無問題則不寫此行。

**`data/source_attribution.jsonl`**（append only）：把所有記者回報的「來源歸因」欄逐筆轉成一行 JSON append，schema：

```json
{"date": "<日報日期>", "source": "<slug>", "category": "<六類別>", "page": "<wiki相對路徑不含.md>", "item_url": "...", "item_title": "..."}
```

slug 對照表見 `.claude/rules/wiki-reporter-shared.md`「來源歸因回報」；記者回報「無」則不寫。schema 詳細說明見 `data/README.md`。

**`data/pending-handoffs.jsonl`（轉知帳本）`[加入: 2026-08-15]`**：記者間的跨記者交辦不靠口頭轉達，走帳本閉迴路（與懸置標記掃描同構：主編登帳 → 派工附清單 → 記者回報處置 → 主編結案）。一律用 `scripts/pending_handoffs.py` 操作，不手改檔案：

| 主編看到 | 動作 |
|---|---|
| 記者「同步自查」寫 `⚠️ 需主編轉知[目標類別]記者：…`，目標是另一位記者 | `open --from 來源類別 --to 目標類別 --page 頁面 --note "要做什麼"` |
| 記者「轉知處置」寫「已處理 H-xxx」 | `close H-xxx --by 類別 --result "一句話"` |
| 記者「轉知處置」寫「不適用 H-xxx（理由）」 | 理由成立 → `void`；理由是「不屬我」→ `open` 給正確類別後 `void` 原筆 |
| 目標是主編自己的彙整工作（feature-radar／index／commitments） | 不登帳，直接做 |

派工前 `list` 一次，輸出依目標記者分組原樣附進派工訊息；`list` 中標 ⚠️ 逾 14 天的積壓要在 `wiki/log.md` 本次紀錄寫一行 `轉知積壓：H-xxx（N 天）`。

**`wiki/overview.md`**：若有重大事件（新模型發布、重大政策變化），更新「當前局勢」段落。

---

## 第四步：衍生記者派工（不在分類路由內）`[加入: 2026-09-05]`

彙整完成、wiki 檔案定稿後，派兩位**不吃分類路由**的衍生記者。他們沒有任何日報條目會被分類過來，本節即其明文觸發邊（依 `.claude/rules/wiki-ingest-format.md`「建頁時必須確認觸發邊」）；派工方式與六記者相同（`subagent_type: "general-purpose"` + `model: "sonnet"` + 角色前導），逐字 prompt 見 `.claude/commands/wiki-ingest.md` 的 4b／4c。

| 記者 | 吃什麼 | 角色檔 | daily 規則 | 為何排在彙整之後 |
|---|---|---|---|---|
| 開發實務（devpractice） | 本輪 ingest 寫進 wiki 的 diff | `.claude/agents/wiki-reporter-devpractice.md` | `.claude/rules/wiki-ingest-devpractice.md` | diff 必須先存在 |
| 投資分析（market） | 當日日報本身（換市場框架重讀） | `.claude/agents/wiki-reporter-market.md` | `.claude/rules/wiki-ingest-market.md` | 判讀要 wikilink 指向已定稿的事實頁 |

投資分析記者只寫 `wiki/topics/market-signals.md`，且該頁的 `## 回顧結算` 回填屬 `/wiki-lint` 5h 主編工作（`.claude/rules/wiki-ingest-market-lint.md`）。

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
待查證命中處置：[已標訊 N 筆: list ／ 證據不足不動 M 筆 ／ 無命中]
轉知處置：[已處理 N 筆: H-id list ／ 不適用 M 筆（id＋一句理由）／ 無待接手]
來源歸因：[每筆一行 or 無]
```

主編依此格式彙整，確保不遺漏任何狀態變更。
