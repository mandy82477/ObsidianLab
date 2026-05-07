# Managed Agents

**類型：** feature
**狀態：** active（研究預覽）
**首次出現：** 2026-04-28
**最後更新：** 2026-05-07

---

## 現況

Anthropic Managed Agents 是 Claude Platform 上的官方 Agent 框架，提供持久記憶、多路並行執行與可驗證輸出等功能。2026-04-28 首次加入跨會話記憶功能（正式公告）；2026-04-30 推出公開測試版，Anthropic 定位為「agentic AI 的 AWS」。

2026-05-06 在「Code with Claude」開發者大會上宣布重大更新，三項新能力同步推出：

- **Dreaming（夢境記憶整合）**：Agent 在任務間隙自動整理近期事件、萃取值得長期保留的資訊存入記憶，類似人類睡眠時的記憶鞏固機制；Anthropic 首次在官方架構層面解決長跑 Agent 的記憶持久性問題；目前限研究預覽版
- **20 路子代理並行**：最高支援 20 個子代理同時執行，突破過去 Agent Teams 的並行限制
- **Outcomes 規格驗證**：Agent 完成後自我驗證輸出是否符合預定規格文件（spec），代表 AI 代理設計從「盡力而為」走向「可驗證達標」的範式轉變

Python SDK v0.100.0 與 TypeScript SDK v0.95.0 同步新增 Managed Agents 原生支援（2026-05-06/07）。

---

## 核心功能

| 功能 | 說明 | 狀態 |
|------|------|------|
| 持久記憶（Memory） | 跨 session 保留 agent 知識與狀態 | 公開測試 |
| Dreaming | 任務間隙自動整理記憶，類似睡眠記憶鞏固 | 研究預覽 |
| 20 路並行子代理 | 最高 20 個子代理同時執行 | 公開測試 |
| Outcomes 規格驗證 | Agent 自我驗證輸出是否符合規格文件 | 公開測試 |

---

## 架構意義

- **有狀態設計**：Dreaming 解決長跑 Agent 的記憶持久性問題，是 Anthropic 首次在官方架構層面處理此問題，相比社群工具（Dreamer、NanoBrain、Memex）更具平台整合性
- **可驗證達標**：Outcomes 將規格文件（spec）提升為執行時的強制依據，「Specs become load-bearing」是官方描述；代表 Agent 設計範式從靠模型自由發揮轉向工程化可驗證
- **規模化能力**：20 路並行子代理組合 Dreaming 記憶，使生產級 Agent 工作流成為可能

---

## 相關議題

- [[entities/claude-code]]（Managed Agents 整合於 Claude Code 工作流）
- [[topics/community-tech-patterns]]（社群工具 Dreamer 採用類似理念，早於官方功能出現）

## 參考來源

- [[news/2026-04-28]]
- [[news/2026-04-30]]
- [[news/2026-05-07]]
- [Ars Technica 報導](https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/)

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-05-07 | Python SDK v0.100.0 + TypeScript SDK v0.95.0 新增 Managed Agents 原生支援，雙線同日發布 |
| 2026-05-06 | 「Code with Claude」大會宣布重大更新：Dreaming 記憶整合、20 路子代理並行、Outcomes 規格驗證 |
| 2026-04-30 | 公開測試版推出，Anthropic 定位為「agentic AI 的 AWS」，Managed Agents + Persistent Memory 同步開放 |
| 2026-04-28 | 首次正式宣布加入跨會話記憶功能 |
