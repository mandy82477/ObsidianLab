# Claude Code

**類型：** product
**狀態：** active
**首次出現：** 2025（正式推出）
**最後更新：** 2026-04-25

---

## 現況

Claude Code 是 Anthropic 的 AI 編碼 CLI 工具，支援 agentic 工作流程、MCP Server 整合、Hooks 機制與 Agent Teams。目前為最受開發者關注的 AI 編碼工具之一，但近期經歷了長達一個月的效能退步事件，Anthropic 已正式承認為工程疏失所致。

---

## 核心功能

- **CLAUDE.md** — 專案級別的 AI 指令設定
- **Hooks** — 在特定事件前後注入自定義邏輯（如：修改代碼後強制跑測試）
- **Skills** — 可複用的任務封裝單元，Claude 透過描述自動觸發
- **Agent Teams** — 多 agent 協作，目前僅支援 Claude 實例（社群已有 workaround）
- **MCP Servers** — 外部工具整合（注意：多個 MCP 可能導致每次訊息消耗 20k+ tokens）
- **Memories** — 跨 session 的持久記憶（Managed Agents Beta）

---

## 已知問題

- **Stop Hooks 被忽略**（2026-04-24 回報）：Claude 4.7 開始無視自訂 stop hooks，影響依賴 hooks 的自動化工作流程，屬行為退步（regression）
- **效能退步事件**：見 [[topics/code-quality-decline]]
- **MCP Token 消耗問題**：多個 MCP Server 併用時，每條訊息可能消耗 20,000+ tokens

---

## 版本歷史

| 日期 | 事件 |
|------|------|
| 2026-04-25 | 社群開發 CC-Canary 工具自動偵測效能漂移 |
| 2026-04-24 | Stop hooks 失效問題被回報（Claude 4.7） |
| 2026-04-24 | Anthropic 正式承認效能退步源於工程疏失 |
| 2026-04 | Google 開始秘密開發競品 |
| ~2026-03 | 效能退步開始，社群陸續察覺 |

---

## 競品

- **Google 未命名工具**：Google 聯合創辦人 Sergey Brin 親自主導，見 [[topics/competitor-landscape]]
- Cursor、Windsurf、GitHub Copilot 等

---

## 實用工具（社群開發）

- **[CC-Canary](https://github.com/delta-hq/cc-canary)** — 讀取 `~/.claude/projects/` JSONL log 偵測效能漂移
- **[claude-anyteam](https://github.com/JonathanRosado/claude-anyteam)** — 讓 Codex/Gemini 加入 Agent Teams
- **[Claude Code Manager](https://claude.ldlework.com/)** — Web UI 集中管理 CLAUDE.md、hooks、skills

---

## 相關議題

- [[topics/code-quality-decline]]
- [[topics/competitor-landscape]]

## 參考來源

- [[news/2026-04-25]]
