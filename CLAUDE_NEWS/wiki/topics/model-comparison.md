---
page: "topics/model-comparison"
kind: "topic"
status: "ongoing"
domain: "🤖 模型"
last_updated: "2026-08-20"
last_news_update: "2026-08-10"
status_main: "ongoing"
days_since_news: 12
inbound_links: 21
attribution_count: 15
attribution_last: "2026-08-10"
top_source: "reddit"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-08-29"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude 模型選型對照

**狀態：** ongoing
**領域：** 🤖 模型
**開始日期：** 2026-07-02
**最後更新：** 2026-08-20
**最後新聞更新：** 2026-08-10

> **最新對照更新**（2026-08-10）
> 公開陣容為 Fable 5（旗艦）> [[entities/opus-5|Opus 5]]（次旗艦，07-25 發布）> Sonnet 5（Claude Code 預設）> Sonnet 4.6 > Haiku 4.5；Opus 4.8 / 4.7 皆已被取代。
> Opus 5 上線後兩週的社群回饋轉為分歧（「過度自信」「不如跑分預期」，07-29～08-04，弱訊號無量化數字），見下方社群實測觀察。
> 新增「安全分類器評測」一節：社群報導 Auto 模式攔截危險指令準確率 89% vs 人工 13.6%（單一社群報導，非選型指標），見下方對應區塊。

---

## 摘要

**現行公開陣容：Fable 5 > Opus 5 > Sonnet 5 > Sonnet 4.6 > Haiku 4.5**（Opus 4.8 / Opus 4.7 已被取代，Mythos 5 僅限授權機構）。本頁回答一個問題：**「我該用哪個 Claude 模型？」**——只做橫向對照、情境推薦與可驗證的選型分界；各模型的爭議、時序、已知問題等深度資訊在各自的 entities 頁，定價細節在 [[entities/pricing]]。

## 快速選型表

| 模型 | 一句定位 | 定價（$/Mtok in/out）· Context | 最適合 |
|------|---------|------------------------------|--------|
| [[entities/fable-5\|Fable 5]] | 旗艦（Mythos 級公開版） | $10 / $50 · 1M | 跨多天的長期 agentic 工作流、deep reasoning、安全漏洞分析 |
| [[entities/opus-5\|Opus 5]] | 次旗艦（Max 預設 / Pro 最強） | $5 / $25（官方確認）· 1M | 數小時自主編碼、跨數十檔 refactor、複雜系統工程 |
| [[entities/sonnet-5\|Sonnet 5]] | 主力平衡（Claude Code 預設） | $2 / $10（促銷至 8/31）· 1M | 日常規模開發（分鐘～1 小時級）、tool use 密集、成本敏感 |
| Sonnet 4.6 | 前代主力 | $3 / $15（官方確認）· 1M | 已驗證穩定、尚未遷移的既有工作流 |
| Haiku 4.5 | 輕量 worker | $1 / $5（官方確認）· 200K | 即時互動、高頻批量分類、延遲與成本敏感的 sub-agent |

**不進表的選項：** [[entities/opus-4-8|Opus 4.8]]、[[entities/opus-4-7|Opus 4.7]] 皆已被取代，新採用一律改用 Opus 5（Fast Mode 已非 4.8 獨佔優勢）；[[entities/mythos|Mythos 5]] 為非公開陣容（僅限授權機構的無護欄安全研究），一般開發用途改選 Fable 5。三者的細節見下方「選型細節」。「不適合」的判準亦全數列於選型細節，每個模型一條。

> **換模型不是唯一旋鈕。** 官方明載「調 effort 通常比換模型更有效」（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)）：Opus 5 起手用預設 `effort: high`，只有最吃重的編碼／agentic 任務才上探 `xhigh`。`max` 並非越高越好（官方稱報酬遞減、簡單任務易 overthinking），換模型前先針對自己的 evals 跑一次 effort sweep——官方原文與社群措辭的落差見下方「Effort dial 細節」。

### 選型細節

- **Fable 5**：官方定位 long-running agents／long-horizon agentic tasks（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），適合**跨多天**的長期工作流、deep reasoning、advanced research、安全漏洞分析。**不適合**日常短問答或單次改動小的任務（改選 Sonnet 5，成本大幅降低）；不適合前沿 LLM 開發（護欄靜默降級）；07-02 起有 Defense in Depth 分類器誤判實測，需人工複核。**存取狀態**：免費期已於 **2026-07-19 到期**；07-20 起 Max／Team premium 為標配（上限週用量 50%）、**Pro／Team standard 需以 usage credits 按 $10/$50 per Mtok 付費**（官方 Help Center，2026-08-08 查證）。Pro 用戶選用前先確認是否願意離開訂閱硬上限。另 07-20 曾出現 Max 誤判需購買 credits 的 bug（#79337 至 08-07 仍延燒）。詳見 [[entities/pricing]]。
- **Opus 5**：官方定位 multihour autonomous coding agents／large-scale refactoring（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），硬邊界是**比日常大一級、但不到跨多天**：數小時自主執行的編碼 agent、跨數十檔的大規模 refactor、複雜系統工程、vision-heavy 工作流、computer use；為 Claude Max/Pro 目前最強可用模型。**不適合**日常規模的 Claude Code 開發（改選 Sonnet 5，成本更低且已足夠）；不適合資安／滲透測試導向任務（官方自陳仍落後 Mythos 5，但一般使用者拿不到 Mythos 5——公開陣容資安首選為 Fable 5〔留意分類器誤判〕，Opus 5 為次選）；不適合跨多天的極長時任務（改選 Fable 5）。**重度 subagent／workflow 工作流建議先實測**：Claude Code 2.1.219/220 疑有僅針對 Opus 5 的硬編碼工具限制（不得呼叫 AgentTool／workflows／deep-research，除非明確要求），未經官方證實，見 [[entities/claude-code]]。
- **Sonnet 5**：官方定位 code generation／agentic tool use（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），適合 Claude Code **日常規模**開發、tool use 密集、成本敏感；v2.1.197 起為 Claude Code 預設。**不適合**比日常規模更大的任務：跨數十檔 refactor、數小時自主 agent（改選 Opus 5）；不適合高頻批量且延遲敏感的場景（改選 Haiku 4.5）。
- **Sonnet 4.6**：**$3 / $15 per Mtok、1M context、128k 輸出**（官方模型總覽頁，2026-08-20 查證；官方列為 legacy，仍可用）。適合已驗證穩定、尚未遷移的既有工作流；**不適合**新專案啟動——Sonnet 5 促銷期至 8/31 為 $2/$10，同 context 同輸出上限而更便宜，促銷結束後兩者同價，屆時仍應選 Sonnet 5。見 [[entities/pricing]]。
- **Haiku 4.5**：官方定位 real-time applications／sub-agent tasks（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），適合即時互動、高頻批量分類、延遲與成本敏感又需一定推理力的 sub-agent worker；**$1 / $5 per Mtok、200K context、64k 輸出**（官方模型總覽頁，2026-08-20 查證）。**不適合**多步驟規劃或跨檔案關聯推理（改選 Sonnet 5 起）；也**不適合**需要吃進大量 context 的任務——本表五個模型只有它是 200K，其餘四者皆為 1M，單檔或單次輸入超過約 15 萬字就必須改選 Sonnet 5 以上。
- **Opus 4.8 / Opus 4.7（已被取代）**：僅適合尚未遷移者的既有工作流延續，不建議新採用——次旗艦地位已由 Opus 5 接手，Fast Mode 亦非 4.8 獨佔優勢（官方文件確認 Opus 5 與 4.8 皆支援 fast mode）。Opus 4.7 另有 200K context 上限與思考深度議題，見 [[entities/opus-4-7]]。
- **Mythos 5（非公開陣容）**：無護欄完整版，僅供獲授權機構的安全研究、滲透測試；一般使用者取不到，不可作為公開陣容模型的淘汰基準——公開陣容資安首選為 Fable 5。
- **定價備注**：Opus 5 為 **$5 / $25 per Mtok**，官方模型總覽頁逐字確認（2026-08-08 首次查證，2026-08-20 複查一致），與 Opus 4.8 相同。發布當週媒體「為 Fable 5 一半」與「維持原 Opus 定價」兩種說法**其實同時成立**——同一組數字的兩個對照對象，非矛盾。本表全部五個定價皆為官方數字，無推算值。沿革與 Fast mode 另計 $10/$50 見 [[entities/pricing#模型 API 定價現況]]。

## 情境推薦

| 你的情境 | 建議 | 依據 |
|---------|------|------|
| Claude Code 日常開發 | **Sonnet 5**（預設即是） | 官方 coding／agents 主力定位；v2.1.197 起預設 |
| 想接近旗艦效能但成本減半 | **Opus 5** | 官方稱評測逼近 Fable 5；$5/$25 為 Fable 5 的一半（2026-08-08 官方確認）|
| 跨多天的複雜 agentic 任務 | **Fable 5** | 917 場景以 0.9 分險勝 Opus 4.8，但 token 約 2 倍 |
| 資安審查 / 漏洞分析 | **Fable 5**（首選）→ 次選 **Opus 5** | Fable 5 能力最強惟有分類器誤判；Mythos 5 非公開選項 |
| 需要壓成本的批量任務 | **Haiku 4.5 + Sonnet 5 協調**，或 **Fable 5 調度 + 便宜模型執行** | 官方基準：Fable 5 調度 46% 成本達 96% 效能 |
| 生產環境求穩 | **Sonnet 4.6 或 Sonnet 5** | Opus 5 上線首兩週有多起錯誤率事件與分歧評價 |

### 情境推薦細節

- **Claude Code 日常開發**：官方定位為 coding／agents／enterprise workflows 主力（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)）；Claude Code v2.1.197 起為預設（2026-07-01，見 [[entities/sonnet-5]]）；1M context，agentic 效能足夠日常規模。
- **想接近旗艦效能但成本減半**：官方稱編碼與知識工作評測（Frontier-Bench、GDPval-AA）逼近 Fable 5，定價為 Fable 5 的一半（$5/$25 vs $10/$50，官方確認；2026-07-25 發布）；適用區間為 multihour autonomous coding／large-scale refactoring 這類「比日常大一級、未達跨多天」的任務。
- **跨多天的複雜 agentic 任務**：官方定位 long-running agents／long-horizon agentic tasks；917 個 coding-agent 場景中以 0.9 分之差略勝 Opus 4.8，但 token 消耗約 2 倍（Reddit r/ClaudeAI，2026-06-12，需連成本一起讀）。存取狀態與免費期見上方 Fable 5 選型細節。
- **資安審查 / 漏洞分析**：Fable 5 能力最強，但 07-02 起有 Defense in Depth 分類器誤判實測；Opus 5 官方文件（2026-07-25）自陳資安任務仍落後 Mythos 5，惟 Mythos 5 非公開選項，不構成 Opus 5 的淘汰理由。
- **需要壓成本的批量任務**：Haiku 4.5 官方定位即 sub-agent tasks／cost-sensitive deployments needing strong reasoning（[choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)），搭配 Sonnet 5 協調為社群驗證的混合架構，調度端成本較低；Fable 5 調度的 46% 成本達 96% 效能為官方基準（Reddit r/ClaudeAI 整理轉載，週熱門標記，2026-07-08，原始官方連結未附）。取捨：Fable 5 調度效能更好、Sonnet 5 調度更省。
- **生產環境求穩**：Opus 5 上線首日（07-25～26）Anthropic Status 連續 4 起模型錯誤率升高事件、07-28 再 1 起，皆於數十分鐘至約 1 小時內排除（Anthropic Status，2026-07-26／07-28）；社群自 07-29 起累積「過度自信」「不如跑分預期」等分歧回饋（弱訊號，見下方社群實測觀察）。Opus 4.8 另有行為退步與 529 記錄（見 [[entities/opus-4-8]]）；Sonnet 4.6/5 已累積較長驗證週期。

## Benchmark 對照（有來源者才列）

> **表格範圍與新鮮度**：本表為 **Opus 5 發布前**陣容（Fable 5 / Opus 4.8 / Sonnet 5）的對照，**數據截至 2026-07-09**（已逾 21 天未有新數據，讀者請視為歷史對照）。Opus 5 尚無同口徑的橫向數據——官方評測改用 Frontier-Bench／GDPval-AA，**Opus 5 數據待補**，暫不塞入本表。
>
> **Opus 5 的定位結論（不入表，因無同口徑對照）**：官方版結論見上方「選型細節」與情境推薦。07-26 MLQ.ai／PCMag 標題稱 Opus 5「tops」Fable 5，**2026-08-10 第三方基準查證屬實**：Artificial Analysis Intelligence Index Opus 5 60.7% 領先 Fable 5 59.9%，GDPval-AA v2（+114 Elo）、AA-Briefcase（+146 Elo，成本再低 54%）亦領先；官方「逼近未超越」是自有基準的保守表述，非與第三方數字矛盾。詳見 [[entities/opus-5]]。

| 指標 | Fable 5 | Opus 4.8 | Sonnet 5 |
|------|---------|----------|----------|
| SWE-bench Pro | SOTA（官方） | 69.2% | 接近 Opus 4.8（社群評測） |
| 綜合定位 | 幾乎所有 benchmark SOTA | 第三方評測曾小輸 Gemini 3.5 Flash（35.4 vs 34.8） | agentic / tool use 接近次旗艦 |
| token 消耗／每任務成本 | 917 場景以 0.9 分略勝 4.8，token 約 2 倍 | 基準對照組 | — |
| 多模型協作（orchestrator） | 調度 + 便宜模型執行：46% 成本達 96% 效能 | — | — |

**表格細節：**

- **SWE-bench Pro**：Sonnet 5 官方對比圖表有修改爭議（2026-07-02，見 [[entities/sonnet-5]]）；Opus 5 尚無 SWE-bench Pro 數字可對照。
- **綜合定位**：Opus 4.8 第三方小輸 Gemini 3.5 Flash 主因為指令遵循；各數據測試日期與條件見各模型 entities 頁。
- **token 消耗**：「小勝」需連成本一起讀——分差 0.9、token 代價約 2 倍（Reddit r/ClaudeAI，2026-06-12，社群整理）。
- **多模型協作**：官方基準，經 Reddit r/ClaudeAI 整理轉載（週熱門標記，來源貼文 2026-07-08，原始官方連結未附，尚未直接查證）。與上一列形成對照：協作模式可望大幅壓低整體成本。
- **延伸閱讀（2026-08-10 補齊量化數字）**：MarkTechPost（2026-07-13）Sonnet 5 / Sonnet 4.6 / Opus 4.8 三模型對照——Sonnet 5 於所有已公布指標超越 Sonnet 4.6（SWE-bench Pro 63.2%、OSWorld-Verified 81.2%、HLE 57.4%），拉近與 Opus 4.8（SWE-bench Pro 69.2%、OSWorld-Verified 83.4%）的差距；定價 Sonnet 5 早鳥 $2/$10（至 8/31，其後 $3/$15）vs Opus 4.8 $5/$25。成本效益取捨：low／medium effort 下 Sonnet 5 最划算，但 xhigh effort 因輸出 token 量大增，成本可能超過 Opus 4.8（[MarkTechPost](https://www.marktechpost.com/2026/07/13/anthropic-claude-sonnet-5-vs-sonnet-4-6-vs-opus-4-8-agentic-coding-benchmarks-api-pricing-and-cost-performance-tradeoffs-compared/)，2026-07-13）。

### 社群實測觀察（弱訊號，未達決策級）

以下均為單一使用者回報、標題級資訊或無量化結論的並排展示，**不構成可決策的評測依據**；正式數字以官方 Frontier-Bench／GDPval-AA 與上方對照表為準。

| 實測 | 結論（含訊號強度） | 來源與日期 |
|------|------------------|-----------|
| Fable 5 vs GPT-5.6 Sol（多小時個人使用） | Fable 5 速度更快、bug 更少；但 Sol 5.6 額度重置更頻繁（甚至每日兩次）——「能力 vs 配額體驗」兩軸各勝，非量化。單一使用者，弱 | Reddit r/ClaudeCode「Fable > Sol 5.6 Ultra」，2026-07-14 |
| 同一 iOS 卡路里 App brief 並排（影片） | 僅影片示範，無文字評測結論。單一使用者，弱 | Reddit r/ClaudeCode，2026-07-14 |
| Opus 5 長時任務心得 | 稱 long-horizon 表現最佳、low effort 成本效益高，**無 benchmark 數字**。單一使用者（週熱門），弱 | Reddit r/ClaudeAI「Opus 5 results are really shocking!!」，2026-07-24 |
| Opus 5 effort dial 非單調 | ❌ **官方文件反證**（2026-08-08 查證）：官方載明 effort 提高可更可靠轉換為更好結果、直到 `max`，未見任何「高於 high 即下降」敘述。社群說法不成立 | Reddit r/artificial，2026-07-25；[官方 migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)，查核 2026-07-29 |
| MineBench.ai 上 Fable 5 vs Opus 5 差異 | ⚠️ **查證後不可採信**（2026-08-08）：測的是空間推理非編碼能力，且榜上查無兩模型，見下方細節。單一貼文（週熱門），弱 | Reddit r/ClaudeAI，2026-07-26；[minebench.ai](https://minebench.ai/) 2026-08-08 查證 |
| Opus 5 上線兩週後的體感回饋 | 三則負向回報：「過度自信」（07-29）、「不如跑分預期」（07-30）、「令人挫折」（08-04），皆無量化數字。多則獨立貼文但同平台，弱～中 | Reddit r/ClaudeCode，2026-07-29 / 07-30 / 08-04 |

**Effort dial 細節：** 原始貼文於「至少在程式碼任務上看起來這樣做…」處截斷；經查證官方 migration guide（2026-07-29 查核）僅載明 `max` 效果「可能報酬遞減、在較簡單任務上容易 overthinking」，屬**定性**描述，未見具體分數或「高於 high 即單調下降」的文字——社群措辭比官方原文更強烈。核心「非單調」說法已於 2026-08-08 由官方 [What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) 證偽（見上表），故不存在可查證的下降幅度。

**小結：** Opus 5 發布後兩週的社群訊號由「首日正面驚喜」轉為分歧（過度自信、與跑分落差），但全數無量化佐證，僅記錄動向、不進快速選型表；Fable 5 vs GPT-5.6 Sol 亦無單一結論。另有一筆已失效的歷史對照：Reddit r/ClaudeAI「同 100 則前端需求測 GPT-5.6 Sol / Opus 4.8 / Grok 4.5」（週熱門，2026-07-23）作者公開 300 筆產出但未給文字結論，且測試對象 Opus 4.8 已被取代，不反映當前陣容。

### token 成本：兩個方向相反的實測結果（並陳，不選邊）

| 觀察 | 結論（含樣本與訊號強度） | 來源與日期 |
|------|----------------------|-----------|
| 儀器化實測：token 倍增（Sonnet 4.6 288 萬→Opus 4.8 606 萬）但每任務成本降 19.8%（$1.26→$1.01） | Terminal-Bench 10 任務、OpenTelemetry 儀器化，各任務跑一輪；多出的 token 多為便宜的 cache 讀取，非全新處理。HN score 5，中（有具體方法與數字，但單輪未重複） | [signoz.io](https://signoz.io/blog/claude-code-model-comparison/)，2026-08-10 查證 |
| 用戶回報：$50 額度原可用兩天，現在一小時內燒完 | 懷疑新模型刻意提高 quota 消耗；另有 5x 費用暴增回報。個人主觀對照帳單、非儀器化，弱 | [Vincent Schmalbach](https://www.vincentschmalbach.com/claude-code-quietly-looks-5x-more-expensive/)，2026-07-01；[GitHub Issue #62476](https://github.com/anthropics/claude-code/issues/62476) |

**矛盾之處：** 前者是受控測量（同任務對比新舊模型），後者是用戶主觀感受同一模型近期帳單變化，測的不是同一件事——不直接互斥，但共同指向「新一代模型 token 消耗與實際成本的關係，社群尚無共識」。相關省額度策略見 [[entities/fable-5]]。

## 跨模型／跨語言行為研究（官方，非選型指標）

Anthropic 研究部落格於 2026-07-15 發布〈Claude's values across models and languages〉，探討使用者提出**沒有普遍正確答案的問題**時（如「該不該接受新工作」），Claude 在不同模型版本與語言之間的價值觀回應差異（[Anthropic Research](https://www.anthropic.com/research/claude-values-models-languages)，2026-07-15；HN 32 分）。

**性質說明：** 屬模型行為／對齊研究，非可用功能也非 benchmark 分數，**不影響本頁選型建議**；因涉及跨模型比較而記於本頁。原文未附樣本語言清單、模型清單或量化差異數字，暫列標題級記錄。

## 安全分類器評測（社群報導，非選型指標）

Reddit r/ClaudeAI 週熱門貼文〈Anthropic Flips Claude Code to Auto Mode by Default Aug 14〉稱引一項對 1,053 名付費測試者的對照研究：Auto 模式攔截危險指令準確率 **89%**，人工逐一審核僅 **13.6%**；貼文標題另稱「blocks 80%+ ... humans only 14%」，與內文 TL;DR 數字（89% / 13.6%）不完全一致，兩組數字並陳，不擇一（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vjqcvf/anthropic_flips_claude_code_to_auto_mode_by/)，週熱門，2026-08-09）。

**訊號強度：單一社群報導。** ❓ **待查證**（標 2026-08-15｜查 1053名、13.6%）｜**對照研究來源與方法未經官方證實**：原始對照研究是否經 Anthropic 官方發布、測試方法與「危險指令」的認定標準均未附連結佐證，除樣本規模（1,053 名付費測試者）外的條件不可考（2026-08-09 報導）。此為 Claude Code Auto 模式背後分類器的安全行為評測，與模型間選型（Fable 5 / Opus 5 / Sonnet 5…）無直接對應關係，不進快速選型表；Auto 模式預設化本身（生效日期 08-14、開關機制）由 [[entities/claude-code]] 追蹤，本頁僅記錄評測數字本身。

## 外部評測榜單

Claude 家內選型看上方情境推薦；跨家比較（GLM、Qwen、Kimi 等開源模型與 GPT-5.6 等非 Anthropic 閉源模型，含畫圖／影片等非文字模型）本頁不記快照分數（會過期誤導），改按任務類型給「該看哪個活榜單」的對照；**各榜每週抓取的領先者快照（含更多任務類型）見 [[topics/model-task-leaderboard]]**：

| 你想做的任務 | 該看的榜 | 訊號類型 |
|---|---|---|
| 寫 code、改專案（coding agent） | [SWE-bench 官方榜](https://www.swebench.com/)、[Aider Polyglot](https://aider.chat/docs/leaderboards/) | 官方 benchmark／coding 實戰 |
| 寫文案、聊天、翻譯等文字工作 | [LMArena](https://lmarena.ai/) | 人類盲測 Elo |
| 畫圖（文生圖） | [Artificial Analysis 圖像榜](https://artificialanalysis.ai/image/leaderboard/text-to-image)（LMArena 亦有圖像 Arena） | 人類盲測 Elo |
| 生成影片／語音 | [Artificial Analysis 影片榜](https://artificialanalysis.ai/video/leaderboard/text-to-video)、同站 Speech Arena | 人類盲測 Elo |
| 選 API：能力×價格×速度權衡 | [Artificial Analysis](https://artificialanalysis.ai/) | 綜合指數 |
| 大家實際在用什麼 | [OpenRouter Rankings](https://openrouter.ai/rankings) | 真實 API 用量（用錢投票） |

> 外部連結僅供參考，非本 wiki 收錄事實；數字會隨時間變動，wiki 不記錄快照分數以免過期誤導。本 wiki 聚焦 Claude/Anthropic 生態系內的評測與定位分析。

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
