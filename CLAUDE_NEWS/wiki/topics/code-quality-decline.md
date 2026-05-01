# Claude Code 效能退步事件

**狀態：** monitoring（官方已說明，待驗證恢復）
**開始日期：** 2026-03（推測）
**最後更新：** 2026-04-30

---

## 摘要

Claude Code 在 2026 年 3 月至 4 月間出現長達約一個月的效能明顯退步，引發大量開發者不滿。2026-04-24，Anthropic 首次正式承認此問題，說明原因為**工程疏失**（engineering missteps），並非刻意的模型行為調整。

---

## 時序（最新在上）

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

---

## 技術彙整

- **Session log 路徑**：`~/.claude/projects/` 存放 JSONL 格式的 session log，CC-Canary 透過此路徑讀取歷史資料進行效能比對
- **CC-Canary 判定等級**：`HOLDING`（穩定）／`SUSPECTED REGRESSION`（疑似退步）／`CONFIRMED REGRESSION`（確認退步）
- **Stop hooks 失效**：Claude 4.7 起無視自訂 stop hooks，與整體效能退步為獨立問題，機制層面尚未公開說明
- **Anthropic 說明原因**：engineering missteps（工程疏失），非刻意的模型行為調整（非 RLHF 過度修正）

---

## 目前結論

- ✅ Anthropic 已承認問題為工程疏失
- ⚠️ 尚不清楚具體的修復時程與驗證方式
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
- [[entities/pricing]]

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [CC-Canary GitHub](https://github.com/delta-hq/cc-canary)
- [Anthropic's definition of safety is too narrow](https://jonathannen.com/anthropic-safety-too-narrow/)
