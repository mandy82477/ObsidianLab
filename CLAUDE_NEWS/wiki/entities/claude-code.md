# Claude Code

**類型：** product
**狀態：** active
**首次出現：** 2025（正式推出）
**最後更新：** 2026-04-27

---

## 現況

Claude Code 是 Anthropic 的 AI 編碼 CLI 工具，支援 agentic 工作流程、MCP Server 整合、Hooks 機制與 Agent Teams。目前為最受開發者關注的 AI 編碼工具之一。近期接連出現效能退步事件（已承認工程疏失）、HERMES.md 靜默計費 bug、API 金鑰外洩漏洞，安全性與可靠性受到集中審視。

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

- **HERMES.md 計費路由 bug**（2026-04-25 回報）：git commit 歷史中含大寫字串「HERMES.md」會觸發靜默切換至 API 額外計費，完全繞過 Max 方案配額；Anthropic 確認為 bug 但拒絕退款，已知損失達 $200。見 [[entities/pricing]]
- **主題模式不跟隨系統**（issue #2990）：`auto` 主題僅在啟動時偵測一次，不會即時同步 macOS dark/light 切換；社群 workaround：WezTerm + Lua 事件鉤子
- **Stop Hooks 被忽略**（2026-04-24 回報）：Claude 4.7 開始無視自訂 stop hooks，影響依賴 hooks 的自動化工作流程，屬行為退步（regression）
- **效能退步事件**：見 [[topics/code-quality-decline]]
- **MCP Token 消耗問題**：多個 MCP Server 併用時，每條訊息可能消耗 20,000+ tokens
- **API 金鑰外洩漏洞**（2026-04-27 報導）：Claude Code 在自動化流程中可能將 API 金鑰洩漏至公開套件倉庫（npm 等），TechTalks 報導，等待 Anthropic 官方回應
- **Usage Policy 隨機拒絕**（Opus 4.7 以來）：Claude Code 頻繁出現無明確觸發條件的 Usage Policy 拒絕；官方建議切換至 `/model claude-sonnet-4-20250514` 作為緩解手段；見 [[entities/opus-4-7]]
- **版本管理不透明**（2026-04-27）：執行 `claude update` 後版本從 2.1.120 降回 2.1.119，疑似靜默撤版，官方 changelog 與索引資訊不一致
- **Mac 卸載不完整**：依官方教學卸載後，macOS 仍殘留「Claude Code URL Handler」應用程式

---

## 版本歷史

| 日期 | 事件 |
|------|------|
| 2026-04-27 | API 金鑰外洩漏洞被媒體報導：可能在自動化流程中洩漏至 npm 等公開倉庫 |
| 2026-04-27 | HERMES.md 計費 bug 引發更廣泛媒體關注，確認損失達 $200，等待修復 |
| 2026-04-27 | 版本從 2.1.120 回滾至 2.1.119，疑似靜默撤版 |
| 2026-04-27 | 28 個滲透測試子代理人開源工具 pentest-ai-agents 釋出 |
| 2026-04-26 | HERMES.md 計費路由 bug 曝光，Anthropic 確認但拒絕退款 |
| 2026-04-26 | Anthropic 測試 Bugcrawl 漏洞偵測工具，見 [[entities/bugcrawl]] |
| 2026-04-26 | Anthropic 工程部落格詳解 Claude Research 多代理架構設計 |
| 2026-04-26 | 多個社群工具發布：Claude Squad（多人協作）、mux0（多 agent 終端）、agent-order（Codex+Claude PRD 協作） |
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
- **[Claude Squad](https://www.reddit.com/r/ClaudeAI/comments/1svmpkv/)** — 多人協作編碼，每人以自己的 Claude Code 作為 agent，orchestrator 分派平行任務並合併分支
- **[mux0](https://mux0.com/)** — 開源 macOS 終端機，側邊欄即時顯示多 agent 執行狀態（running / idle / needs input）
- **[agent-order](https://github.com/btahir/agent-order)** — 讓 Codex 與 Claude 各自寫 PRD 再互相批判，避免答案向先開口方塌縮
- **[EvanFlow](https://github.com/evanklem/evanflow)** — TDD 驅動的 Claude Code 迭代迴圈，16 個技能 + 2 個子代理人，每步驟設有人工確認節點，不自動 commit
- **[Relay](https://github.com/basegraphhq/relay-plugin)** — 強制 Claude Code 在寫程式前深入對齊問題定義的插件，將 Plan Mode 的提問層級從「實作細節」拉升至「問題本質」（MIT 授權）
- **[pentest-ai-agents](https://github.com/evanklem/pentest-ai-agents)** — 28 個專為滲透測試設計的 Claude Code 子代理人，資安工作流程整合
- **[modularity](https://github.com/vladikk/modularity)** — 架構層級插件，採用 Balanced Coupling 模型分析軟體模組化設計，防止 AI 加速代碼生成的同時技術債累積速度加快
- **[Rapunzel](https://github.com/salmanjavaid/rapunzel)** — 樹狀標籤頁「代理人瀏覽器」，集中管理 Claude Code / Codex / Gemini 多個同時運行的 AI 代理
- **[SmolVM](https://github.com/CelestoAI/SmolVM)** — 本機沙盒環境，讓 Claude Code / Codex 在完全隔離的容器中執行，保護宿主系統，單指令啟動
- **[Groundtruth](https://github.com/vnmoorthy/groundtruth)** — Stop Hook，強制 Claude Code 在宣告「完成」前提供可驗證的執行證明，解決自信宣稱成功但實際未驗證的問題
- **[OpenCode-power-pack](https://github.com/waybarrios/opencode-power-pack)** — 將 Anthropic 官方 11 個 Claude Code 技能移植至 OpenCode，打破工具平台綁定

---

## 相關議題

- [[topics/code-quality-decline]]
- [[topics/competitor-landscape]]

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-26]]
- [[news/2026-04-27]]
