# Claude Code 效能退步事件

**狀態：** monitoring（官方已說明，待驗證恢復）
**開始日期：** 2026-03（推測）
**最後更新：** 2026-04-26

---

## 摘要

Claude Code 在 2026 年 3 月至 4 月間出現長達約一個月的效能明顯退步，引發大量開發者不滿。2026-04-24，Anthropic 首次正式承認此問題，說明原因為**工程疏失**（engineering missteps），並非刻意的模型行為調整。

---

## 時序（最新在上）

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
- [CC-Canary GitHub](https://github.com/delta-hq/cc-canary)
