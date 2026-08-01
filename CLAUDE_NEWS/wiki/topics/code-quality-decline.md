# Claude Code 效能退步事件

**狀態：** monitoring（官方已說明，待驗證恢復）
**領域：** 🛠️ 工具/功能
**開始日期：** 2026-03（推測）
**最後更新：** 2026-08-01
**最後新聞更新：** 2026-07-13

> **最近效能退步事件**（2026-07-13）
> Token 消耗異常訊號群自 06-27（quota 重置需手動 continue 的早期焦慮訊號，見 [[topics/community-tech-discussions]]）延燒至 07-13，共 17 天持續出現同方向訊號，累計已達九個獨立來源：GitHub issue #38335（Max 方案額度異常消耗，截至 07-09 累積 791 則留言、536 個讚，社群互動量最高條目之一）、issue #41506（3-5 倍消耗異常）、issue #16856（2.1.1 版 4 倍消耗）、HN「5x 更貴」、$62,021 具名案例、07-08~07-09 三則訊號（cache 命中率下降 20%、Max 20x 週額度不到一天用盡、單一 session 27% 時間耗掉週額度 7%），加上 07-13 新訊號：Reddit r/ClaudeCode 回報 Max 5x 訂閱近一週額度消耗速度變快，5 小時額度約 2 小時即用完（單一貼文，尚待第三方覆核）。仍無法排除是計費/計量問題而非模型能力退步（詳見下方子區塊）。

---

## 摘要

**當前狀態：** 官方已說明 4 月退步原因為工程疏失，恢復情況待驗證；2026-06 下旬起投訴焦點轉向「token 消耗異常／成本暴增」——訊號鏈自 06-27 延燒至 07-13（共 17 天），累計九個獨立訊號（HN 熱議、$62,021 具名案例、四則 GitHub issue、兩則額度異常比例回報、07-13 Max 5x 額度消耗變快回報），且 07-08 首度出現具體技術機制觀察（cache 命中率下降），定調從「值得觀察」上調為「結構性未解問題」；仍無法斷定是模型真退步、計費計量問題、或 context/工具配置問題（詳見「Token 消耗異常訊號群」）；此前的「工具行為不一致」投訴（自訂編排路由失效、無障礙偏差）性質也不一，共同點是均非典型的模型能力退步，官方多未回應。

Claude Code 在 2026 年 3 月至 4 月間出現長達約一個月的效能明顯退步，引發大量開發者不滿。2026-04-24，Anthropic 首次正式承認此問題，說明原因為**工程疏失**（engineering missteps），並非刻意的模型行為調整。

---

## Token 消耗異常訊號群（2026-06 下旬起）

**訊號鏈自 06-27 延燒至 07-13（共 17 天），累計九個獨立訊號**（06-27 為早期 quota 焦慮訊號，見 [[topics/community-tech-discussions]]「額度焦慮系列」；07-01 起為明確的 token/成本異常主張）：

| 日期 | 訊號 | 來源 | 強度 |
|------|------|------|------|
| 2026-07-01 | 「Claude Code Just Got 5x More Expensive」：用戶回報原先兩天用量的 $50 配額現在一小時燒完 | Vincent Schmalbach blog（[原文](https://www.vincentschmalbach.com/claude-code-quietly-looks-5x-more-expensive/)，HN score 53） | 中高（HN score 53 達對照表中門檻）|
| 2026-07-01 | 獨立開發者單月燒 $62,021 token 的具名案例 | Reddit r/ClaudeAI（[原文](https://www.reddit.com/r/ClaudeAI/comments/1ukli2u/i_burned_62021_in_claude_tokens_in_june_solo_dev/)）| 個案但引發廣泛討論 |
| 2026-07-03 | GitHub issue #16856：升級至 2.1.1 版後 token 消耗速度較前版快 4 倍以上 | [GitHub Issues #16856](https://github.com/anthropics/claude-code/issues/16856) | 具體版本號可複現主張 |
| 2026-07-03 | GitHub issue #38335：Max 方案 session 額度自 3/23 起異常加速消耗；截至 07-09 累積 791 則留言、536 個讚，社群互動量最高條目之一 | [GitHub Issues #38335](https://github.com/anthropics/claude-code/issues/38335) | 高（留言數達對照表高門檻，且持續增長）|
| 2026-07-08 | GitHub issue #41506：Max 方案（$100/月）token 消耗量自 3/28-29 起在未變更設定下增加約 3-5 倍，累積 54 則留言、29 個讚 | [GitHub Issues #41506](https://github.com/anthropics/claude-code/issues/41506) | 高（留言數達對照表高門檻，與 #38335 同期同方向）|
| 2026-07-08 | 「Cache hit rate dropping by 20% doubles your agent's bills」：使用者以圖表分享 cache 命中率下降 20% 會讓 agent 帳單翻倍 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uqsah2/cache_hit_rate_dropping_by_20_doubles_your_agents_bills/)）| 首度提出具體技術機制，補足假說二的解釋空缺；圖片為主、文字說明有限，尚待第三方覆核（07-09～07-31 news 查無直接跟進，至今無後續） |
| 2026-07-08 | 「Claude Max (20x) weekly limit exhausted in less than a day」：Max 20x 方案週額度不到一天用盡 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/claude_max_20x_weekly_limit_exhausted_in_less/)）| 具體異常比例回報，與同日 GitHub 額度耗盡回報呼應 |
| 2026-07-09 | 「Claude Max 20x: Why did 27% of one session consume 7% of my entire weekly limit?」：單一 session 27% 的時間即消耗掉整週額度 7% | Reddit r/ClaudeAI（[原文](https://www.reddit.com/r/ClaudeAI/comments/1urqgqx/claude_max_20x_why_did_27_of_one_session_consume/)）| 具體異常比例回報，質疑額度計算機制本身 |
| 2026-07-13 | 「Usage limits getting lower」：Max 5x 訂閱用戶回報近一週用量額度消耗速度明顯變快，5 小時額度約 2 小時即用完 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uve90h/usage_limits_getting_lower/)）| 單一貼文、無評論數據佐證，方向與既有額度異常訊號一致，尚待第三方覆核（07-14～07-31 news 無同一主張的直接覆核，但 07-21 GitHub issue #29579「16% 用量即觸發 rate limit」153 則留言延續同一「額度異常消耗」大主題方向一致，屬功能記者已知問題追蹤範疇，本頁不重複收錄細節） |

**核心分析：三種假說目前證據各支持什麼**

| 假說 | 支持證據 | 尚無法排除的部分 |
|------|---------|-----------------|
| **模型真退步**（同任務需要更多輪次 / token 才能完成）| 若 4.8 或近期模型版本在等量任務上確實需要更多 tool call 或更長 thinking，將直接反映為 token 消耗上升；#16856 明確指向版本號（2.1.1）而非泛稱時間點，較貼近「版本行為改變」框架 | 缺乏官方或第三方在同一 prompt 集合上做版本前後 token 用量對照（benchmark 層級證據）；目前全部是用戶主觀感受 + 帳單金額，非受控實驗（推論）|
| **計費／計量問題**（token 計數方式改變，而非實際用量增加）| $62,021 案例與「5x 更貴」報導都聚焦帳單/配額消耗速度而非任務品質下降；07-08「cache 命中率下降 20% 帳單翻倍」首度提供具體技術機制——若 prompt caching 命中率因 context 結構變化或後端調度改變而下降，重複計算的 token 會直接反映為帳單增加，不需模型能力真的變差；07-09「單一 session 27% 時間耗掉週額度 7%」進一步指向額度計算本身可能存在非線性放大；[[topics/community-tech-discussions]] 技術彙整已記錄社群懷疑「agent 模式的 token 計費方式變更」與「subagent 呼叫計費細節未透明揭示」| Anthropic 未就計費機制或 cache 命中率變化做出官方說明；cache 命中率下降的根因（使用者 context 結構改變 vs 後端調度變更）尚未釐清；無法排除只是使用習慣改變（如更多 subagent/parallel session）導致實際消耗上升（推論）|
| **Context／工具配置問題**（用戶端 orchestration、MCP 工具或 context 管理不當導致的浪費）| #38335 的「Max 方案額度異常消耗」與本頁 2026-06-26「自訂編排路由失效」屬同類型「工具行為不一致」訊號；multi-agent／MCP 工具調用疊加成本是 [[topics/community-tech-discussions]] 已記錄的系統性問題；cache 命中率下降若源於使用者端 context 結構變化（如頻繁插入不同前綴內容），亦可能是配置問題而非後端變更 | 若確為 context 腐蝕或配置問題，理論上應可透過調整 CLAUDE.md／減少 subagent 層級緩解，但目前無用戶回報「調整配置後消耗恢復正常」的驗證案例（推論）|

**目前立場：** 訊號鏈自 06-27（quota 焦慮早期訊號）延燒至 07-13，跨 17 天持續出現同方向訊號且來源獨立，密度已足以將定調從「值得觀察」上調為**「結構性未解問題」**——三種假說均有部分支持證據且互不排斥，07-08 起新增的 cache 命中率機制觀察與兩則額度異常比例回報，首度讓「計費/計量問題」假說有了具體技術描述，07-13 再添一則 Max 5x 額度消耗變快回報但仍屬單一貼文，但仍缺乏官方說明或受控實驗佐證。截至 2026-07-13，Anthropic 尚未對此訊號群做出官方回應。與 [[topics/community-tech-discussions]] 對應的「Claude Code 成本 5x 暴漲」與「額度焦慮系列」條目互相引用，細節不重複展開。

---

## 技術彙整

- **自訂編排路由失效（Reddit r/ClaudeAI，2026-06-26）**：用戶反映相同的自訂 orchestration 設定，OpenCode 能穩定路由到自訂 providers 的 agents，但 Claude Code 無法可靠執行相同路由；問題未見官方說明；此為工具行為不一致問題，非模型能力退步，但影響依賴自訂 agent 編排的工作流（來源：[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ug7sz4/claude_code_ignores_my_custom_orchestration_and/)）
- **LLM 無障礙偏差（Claude Code issue #56079，2026-06-18）**：即使 CLAUDE.md 明確要求 WCAG 2.2 AA，Claude Code 仍將無障礙修復視為「可選取捨」而非需求；模型自解釋：在追求「coding speed」時 accessibility 被降為次要優先；這是「values problem」而非知識問題，與人類工程師的相同偏見如出一轍（Aaron Gustafson blog；2026-06-20 仍在追蹤中）
- **Session log 路徑**：`~/.claude/projects/` 存放 JSONL 格式的 session log，CC-Canary 透過此路徑讀取歷史資料進行效能比對
- **CC-Canary 判定等級**：`HOLDING`（穩定）／`SUSPECTED REGRESSION`（疑似退步）／`CONFIRMED REGRESSION`（確認退步）
- **Stop hooks 失效**：Claude 4.7 起無視自訂 stop hooks，與整體效能退步為獨立問題，機制層面尚未公開說明
- **靜默模型切換（Silent Model Switching）**：開發者記錄 36 天使用數據，發現模型有時在無明確通知的情況下靜默切換，用戶無法確知實際使用的模型版本；不同模型間效率差距高達 11.5 倍，靜默切換可能導致效率和成本的非預期變化；與 2026-04-27「版本管理不透明」（執行 claude update 靜默撤版）議題相呼應，顯示 Anthropic 在模型與版本透明度上的系統性不足
- **Anthropic 說明原因**：engineering missteps（工程疏失），非刻意的模型行為調整（非 RLHF 過度修正）

---

## 目前結論

- ✅ Anthropic 已承認問題為工程疏失
- ✅ Boris Cherny 在 4/23 發布事後報告，承諾 50+ 修復項目
- 🔍 社群開發者正逐一驗證 50+ 修復是否落實（2026-05-03 開始，最終結果待觀察）
- 🔴 Stop hooks 失效為獨立問題，[[entities/claude-code]] 已知問題列表確認截至 2026-07-11 仍未修復（非僅社群指控）
- ⚠️ 信任侵蝕已從「效能品質」擴大至「定價透明度、計量準確性、基礎設施可靠性」，形成結構性問題
- 🔴 「token 消耗異常」訊號群自 06-27 延燒至 07-13（共 17 天，九個獨立來源），密度已達「結構性未解問題」，尚無法判定模型真退步 vs 計費/計量問題 vs context/工具配置問題，Anthropic 未回應
- 📊 CC-Canary 可作為持續監測工具

---

## 影響範圍

- 依賴 Claude Code 進行 agentic 自動化的開發者
- 使用自訂 hooks 注入確定性邏輯的工作流程（stop hooks 問題）
- 付費用戶的訂閱降級潮（見 [[entities/pricing]]）

---

## 相關實體

- [[entities/claude-code]]
- [[entities/opus-4-7]]
- [[entities/opus-4-8]]
- [[entities/pricing]]

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [[news/2026-05-03]]
- [[news/2026-05-05]]
- [[news/2026-05-09]]
- [[news/2026-07-01]]
- [[news/2026-07-03]]
- [[news/2026-07-08]]
- [[news/2026-07-09]]
- [CC-Canary GitHub](https://github.com/delta-hq/cc-canary)
- [Anthropic's definition of safety is too narrow](https://jonathannen.com/anthropic-safety-too-narrow/)

## 時序（最新在上，按月分組）

### 2026-07

#### 2026-07-09
- **Max 20x 額度異常比例回報**：Reddit 用戶質疑 Max 20x 方案中單一 session 27% 的時間即消耗掉整週額度 7%，與同期 GitHub #38335 額度異常回報呼應（該 issue 累積留言數同日增至 791 則）；訊號鏈持續延燒（來源：[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1urqgqx/claude_max_20x_why_did_27_of_one_session_consume/)）

#### 2026-07-08
- **訊號群補上具體技術機制與兩則異常比例回報**：Reddit「cache 命中率下降 20% 導致 agent 帳單翻倍」首度為「計費/計量問題」假說提供技術描述；同日另有「Max 20x 方案週額度不到一天用盡」回報；加上 GitHub issue #41506 回報 Max 方案（$100/月）token 消耗量自 3 月底起在未變更設定下增加約 3-5 倍（累積 54 則留言、29 個讚）；三者與 07-03 的 #38335、07-01 的兩則社群訊號方向一致，訊號密度使定調上調為「結構性未解問題」；官方尚未回應（來源：[GitHub Issues #41506](https://github.com/anthropics/claude-code/issues/41506)、[Reddit cache 命中率](https://www.reddit.com/r/ClaudeCode/comments/1uqsah2/cache_hit_rate_dropping_by_20_doubles_your_agents_bills/)、[Reddit Max 20x 週額度](https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/claude_max_20x_weekly_limit_exhausted_in_less/)）

#### 2026-07-04
- **Plan mode 逾時自動代答 + 整體變慢投訴延續**：Reddit r/ClaudeCode 用戶（source_count 2）反映 plan mode 逾時後自動選擇非預期選項，並主觀感受近期回應變慢、能力下降；與 07-02 已記錄的 AskUserQuestion 60 秒逾時自動代答爭議（見 [[topics/community-tech-discussions]]）屬同一「逾時代答破壞決策體驗」機制的延續投訴，「變慢/能力下降」部分仍屬主觀感受，無 benchmark 或版本號佐證（來源：[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1und5g7/claude_code_cli_is_getting_harder_to_use_plus/)）

#### 2026-07-03
- **Token 消耗異常訊號群成形**：GitHub issue #16856（2.1.1 版 token 消耗達 4 倍以上）與 issue #38335（Max 方案額度自 3/23 起異常消耗，大量留言）同日浮上，與 07-01 的兩則社群訊號（HN「5x 更貴」、$62,021 具名案例）共同構成四個獨立來源的成本異常訊號群；詳見「Token 消耗異常訊號群」子區塊；官方尚未回應（GitHub Issues）

#### 2026-07-01
- **Claude Code 成本暴漲討論爆發**：Vincent Schmalbach 發文「Claude Code Just Got 5x More Expensive」登上 HN（score 53），同日 Reddit 出現獨立開發者單月燒 $62,021 token 的具名案例；社群懷疑與模型切換或計費方式變更有關；詳見 [[topics/community-tech-discussions]] 對應條目

### 2026-06

#### 2026-06-26

- **自訂 Agent 編排路由失效**：用戶反映 Claude Code 無法可靠路由到自訂 orchestration 中的自訂 providers agents，OpenCode 同設定可穩定執行；問題指向 Claude Code 編排機制的行為不一致性，非模型能力問題；官方尚未回應（Reddit r/ClaudeAI）

#### 2026-06-18

- **LLM 無障礙偏差（Claude Code issue #56079）**：開發者 Aaron Gustafson 揭露：在 CLAUDE.md 已明確指定 WCAG 2.2 AA 規格的專案中，Claude Code 仍將無障礙修復視為可選取捨。模型自述原因是在追求「coding speed」時 accessibility 被降級；Aaron Gustafson 評論此為「值觀優先序偏差」而非知識不足。此偏差複製了人類工程師「稍後再修無障礙」的習慣，AI 未改善既有偏見（2026-06-20 持續追蹤中）

### 2026-05

#### 2026-05-29

- **Opus 4.7 升版前一週效能下降（MarginLab SWE-bench-Pro 追蹤）**：MarginLab 每日對 Claude Code 執行 SWE-bench-Pro 追蹤，發現 Opus 4.7 在 [[entities/opus-4-8|Opus 4.8]] 發布前**連續五天**呈現統計顯著的 pass rate 下降，發布後立即恢復。此為「靜默的日常效能變化」模式的又一次文件化案例——launch benchmark 只呈現發布當下數字，無法捕捉前後的漸進變化（來源：https://marginlab.ai/blog/claude-code-degraded-before-opus-4-8/）
- **thinking blocks 400 錯誤**：Opus 4.8 升版後，多名用戶回報 `API Error: 400 thinking or redacted_thinking blocks cannot be modified` 錯誤；v2.1.156 已修復，workaround 為 `/exit` 後 resume session（見 [[entities/claude-code]]）
- **4.8 行為退步投訴**：部分用戶反映 Opus 4.8 比 4.7 更差——obsessive tool use，傾向以 "pecl scripts" 處理簡單文件操作（來源：Reddit r/ClaudeAI）

#### 2026-05-21
- **Opus 退化三週結構化記錄**：用戶以三週結構化 session log（含 metacognitive 欄位）記錄 Opus 4.7 / Sonnet 4.6 在複雜本地 AI 記憶體專案（Qdrant + Neo4j + Graphiti）上的持續失敗，並記錄到競品模型成功捕捉 Claude 遺漏的錯誤；是目前 r/ClaudeAI 最具文件支撐的退化投訴案例，Anthropic 未回應

#### 2026-05-09
- **靜默模型切換（11.5 倍效率差距）**：開發者持續 36 天記錄 Claude Code 使用數據，量化出不同模型間 11.5 倍的效率差距，並觀察到模型有時靜默切換（silent model switching）且無明確通知；對有成本意識的長期用戶是重要的監控警示，建議搭配 Throttle Meter 或 session log 監控實際模型使用情況

#### 2026-05-05
- **Opus 4.7 退步討論再升溫**：dev.to 文章《Claude Opus 4.7 Is a Regression》引發討論，部分開發者聲稱 Opus 4.7 在編碼任務中不如 4.6，已主動回退舊版；與 4/30 的「後設化退步」批評相互呼應；見 [[entities/opus-4-7]]

#### 2026-05-03
- **[社群問責] 4/23 事後報告 50+ 修復社群獨立驗證**：社群開發者主動逐一驗證 Claude Code 負責人 Boris Cherny 在 4/23 發布的事後報告中承諾的超過 50 項修復，提供獨立於官方的實測評估。此為少見的社群對官方承諾進行系統性問責的行動，驗證結果正逐步揭露哪些修復已落實、哪些仍有差距。

### 2026-04

#### 2026-04-30
- **Opus 4.7「後設化」退步**：重度 Max 20x 用戶直言 Opus 4.7 嚴重退步，過度「後設化」無法直接回答問題；學術研究（arxiv 2604.24827）估算 Opus 4.7 參數約 4T，疑似少於 Opus 4.6 的 5.3T，社群失望情緒持續累積
- **Claude Projects 對話消失**：重度使用者三度遭遇整天的創作對話無故消失，無法搜尋找回，呼籲改善 Projects 資料保留機制

#### 2026-04-29
- **Speed Bumps 頻率增加**：多位長期使用者回報 Claude Code 本週起明顯增加中途暫停詢問的頻率，即使簡單任務也頻繁打斷工作流程，社群猜測與系統層級的行為調整有關，但目前無官方說明
- **Max 方案 API 錯誤**：高價訂閱用戶遭遇內部 API 錯誤，Anthropic 支援 AI 卻持續建議排查 VPN 等不相關問題，無法識別實際服務故障，引發對支援品質的強烈批評

#### 2026-04-28
- **「Anthropic 安全定義過窄」批評**：Jonathan Nen 發文指出 Anthropic 的安全關注過度聚焦在模型行為，忽視產品可靠性、定價策略與溝通透明度；以四月 Claude Code 品質問題與 Pro 用戶 Opus 存取爭議為佐證，文章在技術社群引發強烈共鳴，HN 登上精選話題。
- **信任侵蝕進入結構性階段**：定價不透明（Opus 圍牆事件）+ 使用量計量異常 + 基礎設施可靠性問題（Auto Compact 失效、Prompt Cache Race Condition）在同日密集出現，社群對平台可靠性的質疑已超出「效能退步」的原始邊界，擴大為對 Anthropic 整體產品治理的不信任。

#### 2026-04-25
- 社群推出 **CC-Canary** 工具，透過讀取 `~/.claude/projects/` JSONL session log 自動偵測效能漂移，提供 HOLDING / SUSPECTED REGRESSION / CONFIRMED REGRESSION 等判定等級（工具目錄見 [[topics/community-tech-tools]]）

#### 2026-04-24
- **Anthropic 正式公開說明**：承認工程疏失導致效能退步（Fortune、XDA 等媒體同步報導）
- **Stop hooks 失效問題獨立回報**：Claude 4.7 開始無視自訂 stop hooks，屬獨立的行為退步（regression），與效能下滑為不同問題；截至 2026-07-11，[[entities/claude-code]] 已知問題仍將此列為 🔴 未修復（非僅指控）
- HN 討論串累積近 80 則留言

#### 2026-04（早期）
- 大量開發者在 Reddit r/ClaudeAI、Hacker News 回報效能下滑
- 社群質疑是否為刻意調整（RLHF 過度修正、成本考量等），Anthropic 長期未正式回應

### 2026-03

#### 2026-03（推測）
- 效能退步開始，早期用戶開始察覺異常
