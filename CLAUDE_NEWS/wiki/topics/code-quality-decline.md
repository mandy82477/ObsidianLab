# Claude Code 效能退步事件

**狀態：** monitoring（官方已說明，待驗證恢復）
**領域：** 🛠️ 工具/功能
**開始日期：** 2026-03（推測）
**最後更新：** 2026-07-01
**最後新聞更新：** 2026-06-26

> **最近效能退步事件**（2026-06-26）
> 用戶回報 Claude Code 自訂編排路由失效：相同 orchestration 設定下 OpenCode 穩定執行，但 Claude Code 無法可靠路由到自訂 providers 的 agents；問題指向工具行為不一致性，官方尚未回應。

---

## 摘要

**當前狀態：** 官方已說明 4 月退步原因為工程疏失，恢復情況待驗證；近期投訴轉向「工具行為不一致」，但性質不一：自訂編排路由失效屬 context/工具配置層問題，無障礙偏差則被開發者定性為模型「values problem」（優先序偏差）而非配置或知識缺口；兩者共同點是均非典型的模型能力退步，官方多未回應。

Claude Code 在 2026 年 3 月至 4 月間出現長達約一個月的效能明顯退步，引發大量開發者不滿。2026-04-24，Anthropic 首次正式承認此問題，說明原因為**工程疏失**（engineering missteps），並非刻意的模型行為調整。

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
- ⚠️ Stop hooks 失效為獨立問題，是否已修復待確認
- ⚠️ 信任侵蝕已從「效能品質」擴大至「定價透明度、計量準確性、基礎設施可靠性」，形成結構性問題
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
- [CC-Canary GitHub](https://github.com/delta-hq/cc-canary)
- [Anthropic's definition of safety is too narrow](https://jonathannen.com/anthropic-safety-too-narrow/)

## 時序（最新在上）

### 2026-06-26

- **自訂 Agent 編排路由失效**：用戶反映 Claude Code 無法可靠路由到自訂 orchestration 中的自訂 providers agents，OpenCode 同設定可穩定執行；問題指向 Claude Code 編排機制的行為不一致性，非模型能力問題；官方尚未回應（Reddit r/ClaudeAI）

### 2026-06-18

- **LLM 無障礙偏差（Claude Code issue #56079）**：開發者 Aaron Gustafson 揭露：在 CLAUDE.md 已明確指定 WCAG 2.2 AA 規格的專案中，Claude Code 仍將無障礙修復視為可選取捨。模型自述原因是在追求「coding speed」時 accessibility 被降級；Aaron Gustafson 評論此為「值觀優先序偏差」而非知識不足。此偏差複製了人類工程師「稍後再修無障礙」的習慣，AI 未改善既有偏見（2026-06-20 持續追蹤中）

### 2026-05-29

- **Opus 4.7 升版前一週效能下降（MarginLab SWE-bench-Pro 追蹤）**：MarginLab 每日對 Claude Code 執行 SWE-bench-Pro 追蹤，發現 Opus 4.7 在 [[entities/opus-4-8|Opus 4.8]] 發布前**連續五天**呈現統計顯著的 pass rate 下降，發布後立即恢復。此為「靜默的日常效能變化」模式的又一次文件化案例——launch benchmark 只呈現發布當下數字，無法捕捉前後的漸進變化（來源：https://marginlab.ai/blog/claude-code-degraded-before-opus-4-8/）
- **thinking blocks 400 錯誤**：Opus 4.8 升版後，多名用戶回報 `API Error: 400 thinking or redacted_thinking blocks cannot be modified` 錯誤；v2.1.156 已修復，workaround 為 `/exit` 後 resume session（見 [[entities/claude-code]]）
- **4.8 行為退步投訴**：部分用戶反映 Opus 4.8 比 4.7 更差——obsessive tool use，傾向以 "pecl scripts" 處理簡單文件操作（來源：Reddit r/ClaudeAI）

### 2026-05-21
- **Opus 退化三週結構化記錄**：用戶以三週結構化 session log（含 metacognitive 欄位）記錄 Opus 4.7 / Sonnet 4.6 在複雜本地 AI 記憶體專案（Qdrant + Neo4j + Graphiti）上的持續失敗，並記錄到競品模型成功捕捉 Claude 遺漏的錯誤；是目前 r/ClaudeAI 最具文件支撐的退化投訴案例，Anthropic 未回應

### 2026-05-09
- **靜默模型切換（11.5 倍效率差距）**：開發者持續 36 天記錄 Claude Code 使用數據，量化出不同模型間 11.5 倍的效率差距，並觀察到模型有時靜默切換（silent model switching）且無明確通知；對有成本意識的長期用戶是重要的監控警示，建議搭配 Throttle Meter 或 session log 監控實際模型使用情況

### 2026-05-05
- **Opus 4.7 退步討論再升溫**：dev.to 文章《Claude Opus 4.7 Is a Regression》引發討論，部分開發者聲稱 Opus 4.7 在編碼任務中不如 4.6，已主動回退舊版；與 4/30 的「後設化退步」批評相互呼應；見 [[entities/opus-4-7]]

### 2026-05-03
- **[社群問責] 4/23 事後報告 50+ 修復社群獨立驗證**：社群開發者主動逐一驗證 Claude Code 負責人 Boris Cherny 在 4/23 發布的事後報告中承諾的超過 50 項修復，提供獨立於官方的實測評估。此為少見的社群對官方承諾進行系統性問責的行動，驗證結果正逐步揭露哪些修復已落實、哪些仍有差距。

### 2026-04-30
- **Opus 4.7「後設化」退步**：重度 Max 20x 用戶直言 Opus 4.7 嚴重退步，過度「後設化」無法直接回答問題；學術研究（arxiv 2604.24827）估算 Opus 4.7 參數約 4T，疑似少於 Opus 4.6 的 5.3T，社群失望情緒持續累積
- **Claude Projects 對話消失**：重度使用者三度遭遇整天的創作對話無故消失，無法搜尋找回，呼籲改善 Projects 資料保留機制

### 2026-04-29
- **Speed Bumps 頻率增加**：多位長期使用者回報 Claude Code 本週起明顯增加中途暫停詢問的頻率，即使簡單任務也頻繁打斷工作流程，社群猜測與系統層級的行為調整有關，但目前無官方說明
- **Max 方案 API 錯誤**：高價訂閱用戶遭遇內部 API 錯誤，Anthropic 支援 AI 卻持續建議排查 VPN 等不相關問題，無法識別實際服務故障，引發對支援品質的強烈批評

### 2026-04-28
- **「Anthropic 安全定義過窄」批評**：Jonathan Nen 發文指出 Anthropic 的安全關注過度聚焦在模型行為，忽視產品可靠性、定價策略與溝通透明度；以四月 Claude Code 品質問題與 Pro 用戶 Opus 存取爭議為佐證，文章在技術社群引發強烈共鳴，HN 登上精選話題。
- **信任侵蝕進入結構性階段**：定價不透明（Opus 圍牆事件）+ 使用量計量異常 + 基礎設施可靠性問題（Auto Compact 失效、Prompt Cache Race Condition）在同日密集出現，社群對平台可靠性的質疑已超出「效能退步」的原始邊界，擴大為對 Anthropic 整體產品治理的不信任。

### 2026-04-25
- 社群推出 **CC-Canary** 工具，透過讀取 `~/.claude/projects/` JSONL session log 自動偵測效能漂移，提供 HOLDING / SUSPECTED REGRESSION / CONFIRMED REGRESSION 等判定等級

### 2026-04-24
- **Anthropic 正式公開說明**：承認工程疏失導致效能退步（Fortune、XDA 等媒體同步報導）
- **Stop hooks 失效問題獨立回報**：Claude 4.7 開始無視自訂 stop hooks，屬獨立的行為退步（regression），與效能下滑為不同問題
- HN 討論串累積近 80 則留言

### 2026-04（早期）
- 大量開發者在 Reddit r/ClaudeAI、Hacker News 回報效能下滑
- 社群質疑是否為刻意調整（RLHF 過度修正、成本考量等），Anthropic 長期未正式回應

### 2026-03（推測）
- 效能退步開始，早期用戶開始察覺異常
