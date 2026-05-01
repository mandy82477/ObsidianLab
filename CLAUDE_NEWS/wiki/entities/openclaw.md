# OpenClaw

**類型：** product（第三方工具）
**狀態：** 受限（Anthropic 主動管控）
**首次出現：** 2026-04-25
**最後更新：** 2026-05-01

---

## 現況

OpenClaw 是一款第三方 Claude agentic 工具，設計用途為繞過或擴展 Claude 訂閱方案的配額限制，以達到更高用量的自動化使用。Anthropic 已透過多種機制對其進行主動管控，是 Anthropic 與第三方工具生態系摩擦的最具代表性案例。

---

## 意義分析

- **訂閱邊界爭議**：OpenClaw 存在的動機在於繞過訂閱方案的使用限制，代表用戶對配額設計的不滿轉化為技術繞過行動
- **計費透明度危機**：Claude Code 靜默掃描 repo 內容並改變計費行為，在用戶不知情的情況下執行，是帳單透明度的核心問題，見 [[topics/ai-agent-safety]]
- **工具生態摩擦**：Anthropic 主動管控第三方工具的模式（配額限制 + repo 掃描）可能影響整體社群工具生態的發展空間

---

## 相關實體

- [[entities/pricing]]（配額限制政策背景）
- [[entities/claude-code]]（異常計費行為）
- [[topics/ai-agent-safety]]（repo 掃描與計費透明度）

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-30]]

## 事件時序

### 2026-04-30：異常計費觸發行為（HN 近千則討論）
Claude Code 被發現存在異常行為：若 Git 提交訊息或文件內容中含有特定 JSON 格式的 "OpenClaw" 字串，工具會：
- 直接拒絕當次請求，或
- 立即將帳單的 Extra Usage 衝至 100%

此行為表明 Claude Code **正在主動掃描 repo 內容**並依此改變執行策略與計費結果，事件在 HN 引發近千則討論。Anthropic 至今未公開說明觸發條件是否屬預期設計，亦未提供任何官方聲明。

> ⚠️ **未解決**：Anthropic 未確認此為預期行為或 bug，缺乏透明說明。

### 2026-04-25：Anthropic 限制配額
Anthropic 明確限制 OpenClaw 等第三方 agentic 工具的使用配額。Claude Code 負責人 Boris Cherny 公開表示：

> 「訂閱方案的設計並非為這類第三方使用模式而生。」

此言論被視為 Anthropic 將持續提高第三方 agentic 工具門檻的明確信號。
