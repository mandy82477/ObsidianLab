# Stainless

**類型：** product
**狀態：** acquired（服務關閉中）
**領域：** 💼 商業
**首次出現：** 2026-05-19
**最後更新：** 2026-05-20

---

## 現況

Stainless 是成立於 2022 年的 SDK 與 MCP 伺服器生成工具公司，負責生成所有 Anthropic 官方 SDK（Python、TypeScript 等），並已將其 OpenAPI 編譯器擴展至生成 MCP 伺服器。2026-05-18/19，Anthropic 宣布收購 Stainless，傳聞金額逾 **$300M**，消息橫跨 Hacker News、Reddit、InfoWorld 多個平台密集討論。

**2026-05-20 重大更新**：收購後 Anthropic **隨即宣布關閉 Stainless 服務**，對外提供的第三方 SDK 生成服務 2026 年 9 月起正式停止。原本依賴 Stainless 自動生成 SDK 的客戶——包括 OpenAI、Google 等大型平台——需在 9 月前找到替代方案。HN 討論串（「Ask HN: What are Stainless users doing now that Anthropic has killed it?」）引發廣泛討論。社群替代方案：**Ironic**（可從 OpenAPI spec 生成 SDK 及 MCP server，強調 API 契約測試）已作為替代品迅速出現。

| 指標 | 現況（2026-05-19）|
|------|------|
| 傳聞收購金額 | ~$300M+ |
| 核心資產 | 官方 SDK 生成 + MCP 伺服器生成能力 |
| MCP SDK 月下載量 | 9,700 萬次 |
| 生產環境 MCP 伺服器數 | ~10,000 個 |
| 服務關閉日期 | 2026 年 9 月（對外服務） |
| 社群替代方案 | Ironic（OpenAPI → SDK + MCP 生成，強調契約測試）|
| 媒體層級 | HN、Reddit、InfoWorld 密集報導 |

---

## 核心功能

- **OpenAPI → SDK 編譯器**：從 OpenAPI 規格自動生成高品質、慣用語法的多語言 SDK
- **OpenAPI → MCP 伺服器生成**：將同一 OpenAPI 規格同時編譯為 MCP 伺服器，讓任何服務可直接被 Claude Code 等 AI agent 呼叫
- **官方 Anthropic SDK 維護**：Anthropic Python SDK、TypeScript SDK 均由 Stainless 工具鏈生成與維護

## 戰略意義

社群分析指出此次收購的核心價值在 MCP 端：MCP SDK 月下載量達 9,700 萬次、生產環境伺服器約 10,000 個，掌控 MCP 伺服器生成能力等同於掌控 Agent 時代的核心基礎設施入口。此舉將讓 Anthropic 能：

1. **統一 SDK + MCP 工具鏈**：開發者使用同一規格同時生成客戶端 SDK 和 MCP 伺服器
2. **加速生態建設**：降低第三方服務接入 Claude 生態的技術門檻
3. **掌控標準制定**：在 MCP 伺服器生成層建立事實標準，影響整個 agent 生態發展方向

## 相關議題

- [[entities/managed-agents]]（MCP 與 Managed Agents 整合）
- [[entities/claude-code]]（Claude Code 是 MCP 最大消費方）

## 參考來源

- [[news/2026-05-19]]
- [Anthropic acquires Stainless](https://www.anthropic.com/news/anthropic-acquires-stainless)

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-05-20 | HN Ask HN 討論串「What are Stainless users doing now?」；社群替代方案 Ironic 迅速出現；受影響客戶（OpenAI、Google 等）開始尋找替代方案 |
| 2026-05-19 | Anthropic 宣布收購後隨即宣布對外服務 2026 年 9 月起關閉；原依賴 Stainless 的第三方 SDK 客戶進入緊急切換階段 |
| 2026-05-18/19 | Anthropic 宣布收購 Stainless，傳聞金額逾 $300M；消息跨 HN、Reddit、InfoWorld 密集報導；社群分析核心價值在 MCP 伺服器生成能力 |
