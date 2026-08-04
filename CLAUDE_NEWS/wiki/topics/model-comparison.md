# Claude 模型選型對照

**狀態：** ongoing
**領域：** 🤖 模型
**開始日期：** 2026-07-02
**最後更新：** 2026-08-04
**最後新聞更新：** 2026-07-29

> **最新對照更新**（2026-07-25）
> **陣容重大變化**：Anthropic 於 2026-07-25 正式發布 [[entities/opus-5|Claude Opus 5]]，終結近兩週的傳聞（詳見 [[entities/opus-4-8]] 歷史記錄），取代 Opus 4.8 成為次旗艦——官方稱編碼與知識工作評測（Frontier-Bench、GDPval-AA）逼近 Fable 5、資安任務仍落後 Mythos 5、定價官方稱為 Fable 5 一半（推算約 $5/$25，非官方逐字確認數字；MarkTechPost 07-14「維持原價」說法方向不一致，兩者是否指向同一數字待官方定價頁證實，見 [[entities/pricing]]），現為 Claude Max 新預設模型、Claude Pro 最強模型。公開陣容更新為：Fable 5（旗艦）> **Opus 5（次旗艦，新）** > Sonnet 5（主力）> Sonnet 4.6 > Haiku 4.5；Opus 4.8 降級為已被取代。

---

## 摘要

**2026-07-25，Anthropic 發布 Claude Opus 5，取代 Opus 4.8 成為次旗艦**——公開陣容更新為 Fable 5 > Opus 5 > Sonnet 5 > Sonnet 4.6 > Haiku 4.5（Opus 4.8 / Opus 4.7 皆已被取代）。Opus 5 官方稱編碼與知識工作評測逼近 Fable 5、資安任務仍落後 Mythos 5，定價定位見下方表格與 [[entities/pricing]]。本頁回答一個問題：**「我該用哪個 Claude 模型？」** 各模型的深度資訊（爭議、時序、已知問題）在各自的 entities 頁；本頁只做橫向對照與情境推薦，模型陣容變化時同步更新。

## 快速選型表

| 模型 | 定位 | 定價（in/out per Mtok）| Context | 最適合 | 不適合 | 狀態 |
|------|------|------|------|------|------|------|
| [[entities/fable-5\|Fable 5]] | 旗艦（Mythos 級公開版） | $10 / $50 | 1M | 跨多天長期 agentic 工作流、deep reasoning、安全漏洞分析 | 日常短問答改 Sonnet 5；前沿 LLM 開發（護欄降級）| ✅ 已解禁（免費期 7/19 已到期，見下方註記） |
| [[entities/opus-5\|Opus 5]] | 次旗艦（新，2026-07-25 發布） | ~$5 / $25（推算，非官方逐字確認） | 1M | 數小時自主編碼、跨數十檔 refactor、複雜系統工程 | 資安首選讓給 Fable 5；日常小任務改 Sonnet 5；重度 workflow 先實測（見選型細節）| ✅ Active（Max 新預設、Pro 最強） |
| [[entities/sonnet-5\|Sonnet 5]] | 主力平衡選項（Claude Code 預設） | $2 / $10（促銷至 8/31） | 1M | 日常規模開發、tool use 密集、成本敏感 | 大型 refactor／數小時 agent 改 Opus 5；高頻批次改 Haiku 4.5 | ✅ Active（v2.1.197 預設） |
| Sonnet 4.6 | 前代主力 | 低於 Sonnet 5 正式價 | 200K | 已驗證穩定的既有工作流 | 新專案啟動改 Sonnet 5 | ✅ Active |
| Haiku 4.5 | 輕量 worker | 最低 | 200K | 即時互動、高頻批量分類、延遲成本敏感 | 多步驟規劃／跨檔案推理改 Sonnet 5 起 | ✅ Active |
| [[entities/opus-4-8\|Opus 4.8]] | 已被取代（次旗艦地位由 Opus 5 接手） | ~$5 / $25（估計） | 1M | 尚未遷移者的既有工作流延續 | 新採用改 Opus 5（Fast Mode 已非獨佔優勢） | ⚠️ 已被取代 |
| [[entities/opus-4-7\|Opus 4.7]] | 已被取代 | 同 4.8 | 200K | 既有 agentic coding 工作流延續 | 新採用改 Opus 5／Sonnet 5 | ⚠️ 已被取代 |
| [[entities/mythos\|Mythos 5]] | 無護欄完整版 | — | — | 授權機構安全研究、滲透測試 | 一般開發用途（非公開陣容，改選 Fable 5） | ✅ 已解禁（僅限授權機構） |

> **換模型不是唯一旋鈕**：官方文件明載「調整 effort 通常比換模型更有效」（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)）。Opus 5 起手建議用預設 `effort: high`，只有最吃重的編碼／agentic 任務才需上探 `xhigh`——升級模型前，先確認是否該先調 effort。**`effort` 並非「越高越好」**：官方 migration guide（[migration-guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)，2026-07-29 查核）明載 `max` 效果「可能出現報酬遞減，且在較簡單任務上容易 overthinking」，並建議「換模型前先針對自己的 evals 重新跑一次 effort sweep，而非沿用舊模型的設定」；Reddit 社群 07-25 一則週熱門貼文提出更強烈說法——「超過 high 後（即 xhigh／max）程式碼任務分數會下降」，並稱官方 migration guide 本身即有此說明。經查證，migration guide 原文僅止於「報酬遞減／overthinking」的**定性**描述，未見具體分數或「高於 high 即單調下降」的明確文字，兩者存在措辭落差；具體下降幅度待查證，不可推算。詳見下方「Opus 5 早期社群反應」表格。

### 選型細節

- **Fable 5**：官方定位 long-running agents／long-horizon agentic tasks（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），適合**跨多天**的長期 agentic 工作流、deep reasoning、advanced research、安全漏洞分析。不適合日常短問答或單次改動小的任務（改選 Sonnet 5，成本大幅降低）；不適合前沿 LLM 開發（護欄靜默降級）；07-02 起有 Defense in Depth 分類器誤判實測，需人工複核。**狀態細節**：免費期已於 **7/19 到期**；07-20 一度出現 Max 方案誤判需購買 credits 的 bug，官方已證實並建議重啟；Max/Team 後續存取政策（永久標配／計量存取）仍分歧報導中，詳見 [[entities/pricing]]。
- **Opus 5**：官方定位 multihour autonomous coding agents／large-scale refactoring（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），硬邊界是**比日常大一級、但不到跨多天**：數小時自主執行的編碼 agent、跨數十檔的大規模 refactor、複雜系統工程、vision-heavy 工作流、computer use；Claude Max/Pro 目前最強可用模型。不適合日常規模的 Claude Code 開發（改選 Sonnet 5，成本更低且已足夠）；不適合資安/滲透測試等安全導向任務（官方自陳仍落後 Mythos 5；一般使用者拿不到 Mythos 5，公開陣容中資安首選為 Fable 5〔留意 Defense in Depth 分類器誤判〕，Opus 5 為次選）；不適合跨多天的極長時任務（改選 Fable 5）。**重度 subagent／workflow 工作流建議先實測**：Claude Code 2.1.219/220 疑有僅針對 Opus 5 的硬編碼工具限制，未經官方證實，見 [[entities/claude-code]]。
- **Sonnet 5**：官方定位 code generation／agentic tool use（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），適合 Claude Code **日常規模**開發（單次任務多在分鐘到一小時級）、tool use 密集、成本敏感；v2.1.197 起為 Claude Code 預設。不適合比日常規模更大的任務：跨數十檔 refactor、數小時自主 agent（改選 Opus 5）；不適合高頻批量且延遲敏感的場景（改選 Haiku 4.5，單位成本更低）。
- **Sonnet 4.6**：適合已驗證穩定、尚未遷移的既有工作流；不適合新專案啟動（改選 Sonnet 5，促銷期至 8/31 CP 值更高，見 [[entities/pricing]]）。
- **Haiku 4.5**：官方定位 real-time applications／sub-agent tasks（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），適合**即時互動**應用、高頻批量分類/簡單任務、延遲與成本敏感、仍需一定推理力的 sub-agent worker；不適合需要多步驟規劃或跨檔案關聯推理的複雜任務（改選 Sonnet 5 起）。
- **Opus 4.8**：已被取代（第三階，次旗艦地位由 Opus 5 接手），僅適合尚未遷移者的既有工作流延續；不建議新採用（已有 Opus 5 接手次旗艦地位，改選 Opus 5）——Fast Mode 非其獨佔優勢，官方文件確認 Opus 5 與 Opus 4.8 皆支援 fast mode。
- **Opus 4.7**：已被取代（第四階），僅適合 agentic coding 口碑良好的既有工作流延續；不建議新採用（已有 Opus 5 / Sonnet 5 等多代後繼，改選其一）。
- **Mythos 5**：無護欄完整版，僅適合獲授權機構的安全研究、滲透測試等無護欄需求場景；不適合一般開發用途（非公開陣容選項；一般使用者改選 Fable 5 作為資安首選，留意分類器誤判風險）。僅限授權機構/安全研究用途，非一般消費市場。
- **定價備注**：官方稱 Opus 5 定價為 Fable 5 一半，推算約 $5 / $25（以 Fable 5 $10/$50 換算，**非官方逐字確認的具體數字**）；MarkTechPost（07-14）另稱 Opus 5「維持原 Opus 定價」，與官方「砍半」方向不一致——兩說法是否指向同一數字，待官方定價頁公布逐項 $/Mtok 數字才能核實，不可逕自視為已釐清，詳見 [[entities/pricing]]。

## 情境推薦

| 你的情境 | 建議 | 依據（一句話） |
|---------|------|------|
| Claude Code 日常開發 | **Sonnet 5**（預設即是） | 官方 coding／agents 主力定位；v2.1.197 起預設，1M context |
| 想要接近旗艦效能但成本減半 | **Opus 5**（新） | 官方稱評測逼近 Fable 5、定價約半價（推算 $5/$25）；發布首日穩定性待觀察 |
| 跨多天的複雜 agentic 任務 | **Fable 5** | 917 場景中以 0.9 分險勝 Opus 4.8，但 token 消耗約 2 倍；免費期已於 7/19 到期 |
| 資安審查 / 漏洞分析 | 一般使用者：**Fable 5**（首選）→ 次選 **Opus 5**；Mythos 5 僅授權機構可用 | Fable 5 能力最強但有分類器誤判實測；Opus 5 官方自陳落後 Mythos 5（非公開選項） |
| 需要壓成本的批量任務 | **Haiku 4.5 + Sonnet 5 協調**；或 **Fable 5 調度 + 便宜模型執行** | 官方基準：Fable 5 調度模式 46% 成本達 96% 效能；依預算取捨 |
| 生產環境求穩 | **Sonnet 4.6 或 Sonnet 5** | Opus 4.8 有行為退步／529 記錄；Opus 5 僅發布 1 天，穩定性未知 |

### 情境推薦細節

- **Claude Code 日常開發**：官方定位為 coding／agents／enterprise workflows 的主力（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)）；Claude Code v2.1.197 起為預設模型（2026-07-01 起，見 [[entities/sonnet-5]]）；1M context、成本敏感場景下 agentic 效能足夠日常規模。
- **想要接近旗艦效能但成本減半**：官方稱編碼與知識工作評測（Frontier-Bench、GDPval-AA）逼近 Fable 5、定價官方稱為 Fable 5 一半（推算約 $5/$25，非官方逐字確認數字，2026-07-25 發布）；官方定位對應 multihour autonomous coding agents／large-scale refactoring 這類「比日常大一級、未達跨多天」的區間；發布首日，長期穩定性待觀察。
- **跨多天的複雜 agentic 任務**：官方定位 long-running agents／long-horizon agentic tasks（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)）；917 個 coding-agent 場景中以 0.9 分之差略勝 Opus 4.8，但 token 消耗約 2 倍（Reddit r/ClaudeAI，2026-06-12，需連成本一起讀）；免費期已於 7/19 到期，Max/Team 後續存取政策仍分歧（見 [[entities/pricing]]）；07-20 曾一度出現 Max 方案誤判需購買 credits 的 bug，官方已證實並建議重啟。
- **資安審查 / 漏洞分析**：Fable 5 能力最強，但 07-02 起 Defense in Depth 分類器有誤判實測；Opus 5 官方文件（2026-07-25）自陳資安任務仍落後 Mythos 5，但 Mythos 5 非公開陣容選項，不能拿來當作 Opus 5 的淘汰理由。
- **需要壓成本的批量任務**：Haiku 4.5 官方定位即為 sub-agent tasks／cost-sensitive deployments needing strong reasoning（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），搭配 Sonnet 5 協調為社群驗證的混合架構模式，調度成本較低；Fable 5 調度數字為官方基準（46% 成本達 96% 效能，Reddit r/ClaudeAI 整理轉載，週熱門標記，2026-07-08，原始官方連結未附），惟調度端本身較貴。兩者取捨：Fable 5 調度效能更好、Sonnet 5 調度更省成本，依預算選擇。
- **生產環境求穩**：Opus 4.8 曾有行為退步與 529 事件記錄（見 [[entities/opus-4-8]] 歷史記錄）；Opus 5 發布僅一天（2026-07-25），暫無穩定性資料；Sonnet 4.6/5 已累積較長驗證週期。

## Benchmark 對照（有來源者才列）

> **陣容說明**：下表為 **Opus 5 發布前**的陣容對照（Fable 5 / Opus 4.8 / Sonnet 5）。Opus 4.8 已於 2026-07-25 被 [[entities/opus-5|Opus 5]] 取代次旗艦地位，Opus 5 尚無自己的對照欄——**Opus 5 的對應 benchmark 數據待補**，暫不橫向比較。

| 指標 | Fable 5 | Opus 4.8 | Sonnet 5 | 備注 |
|------|---------|----------|----------|------|
| Opus 5 綜合定位（2026-07-25 發布，新） | 逼近但未超越（官方稱，Frontier-Bench／GDPval-AA）；另有標題稱「勝過」，待驗證（見下方細節） | 已被取代（次旗艦地位由 Opus 5 接手，官方稱相同成本下效能大幅提升） | — | 資安落後 Mythos 5；定價約半價（推算，未逐字確認）；兩則報導定價方向不一致（見下方細節） |
| SWE-bench Pro | SOTA（官方） | 69.2% | 接近 Opus 4.8（社群評測） | Sonnet 5 官方對比圖表有修改爭議（2026-07-02）；Opus 5 官方評測改用 Frontier-Bench/GDPval-AA，尚無 SWE-bench Pro 數字對照 |
| 綜合定位 | 幾乎所有 benchmark SOTA | 第三方評測曾小輸 Gemini 3.5 Flash（35.4 vs 34.8，主因指令遵循） | agentic / tool use 接近次旗艦 | 各數據測試日期與條件見各模型頁 |
| token 消耗／每任務成本 | 917 個 coding-agent 場景中以 0.9 分之差略勝 Opus 4.8，但 token 消耗約 2 倍（Reddit r/ClaudeAI，2026-06-12） | 基準對照組 | — | 「小勝」需連成本一起讀：分差小、代價大 |
| 多模型協作成本效益（orchestrator 模式）| Fable 5 調度 + 便宜模型執行：**46% 成本達 96% 效能**（官方基準，Reddit r/ClaudeAI 整理轉載，週熱門標記，來源貼文 2026-07-08，原始官方連結未附）| — | — | 與上一列「Fable 5 單獨執行 token 消耗約 2 倍」形成對照：協作模式可望大幅壓低整體成本，惟原始 benchmark 頁面尚未直接查證 |

> 數據截至 2026-07-09（Opus 5 綜合定位列例外，為 2026-07-25 發布當日資料）；詳細評測條件與矛盾結果並陳原則見各模型 entities 頁。
>
> **延伸閱讀（待補充量化數字）**：MarkTechPost（2026-07-14）發布 Sonnet 5 / Sonnet 4.6 / Opus 4.8 三模型 agentic coding benchmark、API 定價、成本效益取捨的完整對照文章，惟日報摘要僅標題級資訊、未附具體評測數字，暫列為外部延伸閱讀資源，待補充查證後再納入下方表格（Google News／MarkTechPost，2026-07-14；詳見 [[entities/sonnet-5]] 歷史記錄）。

#### Benchmark 細節：Opus 5 綜合定位

- **Fable 5 欄**：官方稱 Opus 5 編碼與知識工作評測（Frontier-Bench、GDPval-AA）逼近但未超越 Fable 5；07-26 MLQ.ai／PCMag 標題另稱 Opus 5「tops」Fable 5（AI Benchmark Index、agentic search），僅標題層級、與官方框架略有出入，待驗證，詳見 [[entities/opus-5]]。
- **備注欄**：資安任務上 Opus 5 仍落後 Mythos 5（官方自陳，一般使用者拿不到 Mythos 5，公開陣容資安首選為 Fable 5）；定價官方稱為 Fable 5 一半（推算約 $5/$25，非官方逐字確認數字）；the-decoder.com「減半」與 MarkTechPost「維持原價」兩則報導方向仍不一致，尚未證實為同一數字，詳見 [[entities/pricing]]。

### 社群實測觀察：Fable 5 vs GPT-5.6 Sol（並陳，混合評價，訊號偏弱）

| 觀察 | 結論 | 樣本條件 | 來源與日期 |
|------|------|---------|-----------|
| 多小時實測：速度更快、bug 更少 | Fable 5 勝出（速度／穩定性） | 個人用戶多小時使用比較，非量化 benchmark；標題直述「fable clearly beats in speed and less bugs」 | Reddit r/ClaudeCode「Fable > Sol 5.6 Ultra」，2026-07-14 |
| Sol 5.6 額度重置頻率（甚至每日兩次） | Sol 5.6 在額度重置機制上具使用體驗優勢 | 同一用戶主觀比較，非量化數字 | Reddit r/ClaudeCode「Fable > Sol 5.6 Ultra」，2026-07-14 |
| 相同 iOS 卡路里追蹤 App brief 對比（影片） | 無文字結論，僅影片示範，未附文字評測摘要 | 同一需求、不同模型輸出的並排展示 | Reddit r/ClaudeCode「GPT-5.6 Sol vs Claude Fable 5 on the same iOS calorie-tracker brief」，2026-07-14 |

**小結**：GPT-5.6 Sol vs Fable 5 的社群實測持續出現，本輪均為 r/ClaudeCode 單一使用者觀點，Reddit RSS score 恆 0（非跨平台佐證），訊號強度偏弱；速度與 bug 數量的主觀評價傾向 Fable 5 勝出，但 Sol 5.6 額度重置頻率被使用者視為明顯優勢——兩者呈現「能力 vs 配額體驗」的不同勝負軸，不構成單一結論，需更多獨立來源與量化 benchmark 佐證。

### 社群實測觀察：GPT-5.6 Sol vs Opus 4.8 vs Grok 4.5（三方同題，⚠️ 時效性下降）

> **⚠️ 時效性提示**：本輪測試對象 Opus 4.8 已於 **2026-07-25** 被 [[entities/opus-5|Opus 5]] 取代次旗艦定位（詳見上方陣容變化）。此筆數據反映的是**舊陣容**下的表現，讀者不應把 Opus 4.8 的結果誤讀為當前 Claude 陣容（Fable 5 / Opus 5 / Sonnet 5）的代表，僅作為歷史對照保留。

| 觀察 | 結論 | 樣本條件 | 來源與日期 |
|------|------|---------|-----------|
| 相同 100 則前端需求，三模型同題測試 | 作者公開全部 300 筆產出供比較，未見文字版總結論（僅並陳結果） | 三模型同題測試，屬並排展示非量化 benchmark；Reddit RSS score 恆 0，非跨平台佐證 | Reddit r/ClaudeAI「[I gave GPT-5.6 Sol, Claude Opus 4.8, and Grok 4.5 the same 100 frontend briefs—here are all 300 results](https://www.reddit.com/r/ClaudeAI/comments/1uyb1i9/i_gave_gpt56_sol_claude_opus_48_and_grok_45_the/)」（週熱門），2026-07-23 |

**小結**：此為單一作者的並排產出展示，非評分式 benchmark，訊號強度偏弱（Reddit 週熱門標記但無量化結論文字）；且測試對象 Opus 4.8 已因 Opus 5 發布退居「已被取代」狀態，此筆數據的參考價值隨陣容更新而下降，僅供歷史對照。

### 社群實測觀察：Opus 5 早期社群反應（發布首日起，弱訊號、無量化數字）

| 觀察 | 結論 | 樣本條件 | 來源與日期 |
|------|------|---------|-----------|
| 使用者稱 Opus 5 於長時間任務（long-horizon task）表現最佳，Low effort 設定下成本效益極高 | 主觀正面評價，**無具體 benchmark 數字佐證** | 單一 Reddit 使用者心得分享，非量化測試；Reddit RSS score 恆 0，週熱門標記 | Reddit r/ClaudeAI「Opus 5 results are really shocking!!」（週熱門），2026-07-24 |
| 第三方 benchmark 平台 MineBench.ai 出現 Fable 5 vs Opus 5 差異討論 | **具體分數/差異細節待查證**——日報僅擷取到標題與縮圖，無法確認測試方法或數字，不可推算 | 僅標題可用，正文未擷取 | Reddit r/ClaudeAI「Differences Between Fable 5 and Opus 5 on MineBench.ai」（週熱門），2026-07-26 |
| 使用者稱 Opus 5 的 effort 旋鈕「非單調」——超過 `high`（即 `xhigh`／`max`）後編碼任務分數反而下降，並稱官方 migration guide 本身即說明此現象 | **具體下降幅度待查證**；社群措辭比官方定性描述更強烈，落差待驗證（見下方細節） | 單一 Reddit 貼文（週熱門標記），內容於關鍵處截斷；已比對官方 migration guide 原文 | Reddit r/artificial「Opus 5's effort dial is not monotonic above "high"...」（週熱門），2026-07-25；[官方 migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)，查核日 2026-07-29 |

**Effort dial 細節：** 原始貼文於「至少在程式碼任務上看起來這樣做...」處截斷；經查證官方 migration guide（2026-07-29 查核）僅載明 `max` 效果「可能報酬遞減、在較簡單任務上容易 overthinking」，屬**定性**描述，未見具體分數或「高於 high 即單調下降」的明確文字——社群措辭比官方原文更強烈，此落差待驗證，不可逕自採信社群版本的因果強度。

**小結**：Opus 5 發布首日（07-24）起社群陸續出現效能相關討論，本輪三則均為標題層級、截斷內容或無量化佐證的主觀回報，訊號強度弱，不構成可決策的評測依據。effort 非單調一說經比對官方 migration guide 原文，僅能確認「`max` 效果報酬遞減、易 overthinking」的定性描述，社群「高於 high 即單調下降」的具體措辭尚未見官方數字佐證，兩者落差已於上方「換模型不是唯一旋鈕」callout 註明。正式評測數字仍以官方 Frontier-Bench／GDPval-AA（見 [[entities/opus-5]]）與上方對照表為準；本表僅記錄社群觀感存在此一動向，不進入快速選型表或情境推薦。

### token 成本：兩個方向相反的實測結果（並陳，不選邊）

| 觀察 | 結論 | 樣本條件 | 來源與日期 |
|------|------|---------|-----------|
| 儀器化實測：新版模型 token 用量顯著更高，但**每任務總成本反而下降** | 需同時看 token 用量與任務完成率，不能只看單位成本或速度 | 工程師以 signoz.io 自建儀表板對比新舊版 Claude 模型；HN score 5（訊號偏弱，結論標「待驗證」） | [signoz.io](https://signoz.io/blog/claude-code-model-comparison/)，2026-06-29 |
| 用戶回報：**$50 額度原可用兩天，現在一小時內燒完** | 懷疑新模型（4.8）刻意提高 quota 消耗；成本暴增趨勢延燒至社群多篇貼文（費用 5x 暴增回報、企業採「穴居人模式」壓縮輸出降本）| 個人用戶主觀對照前後月份帳單，非儀器化測量；未附詳細 log | [Vincent Schmalbach 部落格](https://www.vincentschmalbach.com/claude-code-quietly-looks-5x-more-expensive/)，2026-07-01；[GitHub Issue #62476](https://github.com/anthropics/claude-code/issues/62476) |

**矛盾之處**：前者是受控測量（同任務對比新舊模型的 token 用量與完成率），後者是用戶主觀感受同一模型（Opus 4.8/Fable 5）近期的帳單變化，兩者測的不是同一件事——不構成直接互斥，但都指向「新一代模型的 token 消耗與實際成本之間的關係，社群尚無共識」。Fable 5 配額吃緊的相關社群省額度策略見 [[entities/fable-5]] 「配額與計費過渡（原訂 7/7，現已順延至 7/19）」子區塊。

## 跨模型／跨語言行為研究（官方，非選型指標）

Anthropic 研究部落格於 2026-07-15 發布〈Claude's values across models and languages〉，探討使用者向 Claude 提出**沒有普遍正確答案的問題**時（例如「該不該接受新工作」「如何處理與朋友的衝突」），Claude 在不同模型版本與不同語言之間展現的價值觀回應差異（[Anthropic Research](https://www.anthropic.com/research/claude-values-models-languages)，2026-07-15；Hacker News 累積 32 分）。

**性質說明：** 這是模型行為／對齊研究，非可用功能、也非 benchmark 分數，**不影響本頁「該用哪個模型」的選型建議**；因研究涉及跨模型、跨語言比較而非單一模型，記錄於本頁而非個別 entities 頁。原文摘要僅提供研究主題與範例問題，未附具體樣本語言清單、模型清單或量化差異數字，暫列標題級記錄，待後續報導或原始研究補充細節時再擴寫。

## 外部評測榜單

wiki 內建的模型評測數字有時效性限制（見上方各表格「數據截至」標註）。若需要更即時、涵蓋更廣的跨模型（含 GLM、Qwen、Kimi 等開源模型與 GPT-5.6 等非 Anthropic 閉源模型）評測對照，可參考：

- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/) — 涵蓋開源與閉源模型的綜合能力評測，含 FrontierSWE、Terminal-Bench 等 coding/agentic 子項
- [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — 開源模型專用評測榜單，適合追蹤 GLM / Qwen / Kimi 等開源競品

> 外部連結僅供參考，非本 wiki 收錄事實；數字本身會隨時間變動，wiki 不記錄快照分數以免過期誤導。本 wiki 聚焦 Claude/Anthropic 生態系內的評測與定位分析。

## 相關實體

- [[entities/fable-5]] · [[entities/opus-5]] · [[entities/opus-4-8]] · [[entities/sonnet-5]] · [[entities/opus-4-7]] · [[entities/mythos]]
- 功能熱度與升版建議：[[feature-radar]]
- 定價細節：[[entities/pricing]]

## 時序（陣容變化）

- 2026-07-25：**Opus 5 發布**，取代 Opus 4.8 成為次旗艦、Claude Max 新預設模型、Claude Pro 最強模型
- 2026-07-01：Sonnet 5 發布（Claude Code 預設）；Fable 5 / Mythos 5 解禁
- 2026-06-13：Fable 5 / Mythos 5 出口管制停用（至 06-30）
- 2026-06-09：Fable 5 發布，Opus 4.8 退居次旗艦
- 2026-05-28：Opus 4.8 發布
- 2026-04-24：Opus 4.7 發布
