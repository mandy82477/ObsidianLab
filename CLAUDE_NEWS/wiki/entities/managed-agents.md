---
page: "entities/managed-agents"
kind: "entity"
type: "feature"
status: "beta（所有 API 帳號預設可用，須帶 beta header）"
domain: "🛠️ 工具/功能"
last_updated: "2026-09-11"
last_news_update: "2026-09-11"
status_main: "beta"
days_since_news: 1
parent: "topics/anthropic-agent-stack"
children: "[]"
page_role: "child"
days_since_news_subtree: 1
inbound_links: 33
attribution_count: 5
attribution_last: "2026-09-11"
top_source: "github"
pending_count: 1
pending_overdue: 1
pending_next_review: null
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Managed Agents

**類型：** feature
**狀態：** beta（所有 API 帳號預設可用，須帶 beta header）
**領域：** 🛠️ 工具/功能
**別名：** Anthropic Managed Agents, 受管代理
**上層：** [[topics/anthropic-agent-stack]]
**首次出現：** 2026-04-28
**最後更新：** 2026-09-11
**最後新聞更新：** 2026-09-11

> **最新動態**（2026-09-11）
> anthropic-sdk-python v1.5.0 新增 Managed Agents 的 auto mode 工具權限設定——是 05-22 以來四筆 SDK 更新中首次列出具體項目；細節仍待官方文件補充。

---

## 現況

Anthropic Managed Agents 是 Claude Platform 上的官方 agent 框架（[概覽文件](https://platform.claude.com/docs/en/managed-agents/overview)）：持久記憶（含 Dreaming 記憶整合）、20 路並行子代理、Outcomes 規格驗證、Proactive Workflows、企業自架沙箱。**狀態為 beta**（自 2026-05-11 起，所有 API 帳號預設可用，須帶 `managed-agents-2026-04-01` beta header）——各零件成熟度不一：只有 `/goal` 已達正式發布，Dreaming 與 Agent View 仍是 research preview（Dreaming 另需申請並帶 `dreaming-2026-04-21` header），Proactive Workflows 與 Capability Curve 自 2026-05-18 公告後逾 100 天無進一步細節公布。Outcomes 讓規格文件成為執行時的強制依據（官方語「Specs become load-bearing」）。

實質新功能停在 2026-05-22；此後多筆為 SDK 版號擴充，多數官方 changelog 未列細節，2026-09-11 的 anthropic-sdk-python v1.5.0 首度列出具體項目——新增 auto mode 工具權限設定，惟功能細節仍待官方文件補充。獨立第三方生產環境回饋至今為零——本頁引用到的兩則使用案例，一則用的是自組架構、一則來自 Claude Code 創始人。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 要跑數小時以上、跨 session 保留狀態的工作流；需要資料不出境（自架沙箱） |
| 不適合 | 單次 30 分鐘內做得完、或不需保留跨 session 狀態的任務——`/goal` 就夠 |

> 跨功能的熱度對比見 [[feature-radar]]；跟其他官方 agent 形態怎麼挑、積木怎麼組，以及**計費算式與官方算例**（token 牌價＋$0.08／session-hr），見上層 [[topics/anthropic-agent-stack]]「選型細節」。

**為什麼只剩 🔥🔥**：近四週（08-09～09-06）只被提到兩天——一次是 SDK 版號、一次是別人拿它當對照組——沒有任何正向採用回報，實質新功能停在 05-22。
%% 維運備忘：2026-09-05 頁面健檢一次性下修。量測：python scripts/news_mentions.py --since 4w --any "Managed Agents" "受管代理" → 命中 08-20（版號無細節）、09-03（負向對照）。現行「連續 4 週零命中 −1 格」對本頁降 0 格，故為編輯判斷；上限式判準是否成法見 docs/page-audits/ledger.md 待裁決。feature-radar L226 已同步。%%

---

## 接下來看什麼

- **等哪個訊號**：Agent View 從研究預覽升格、Proactive Workflows／Capability Curve 補上細節公告、出現第一則獨立生產環境回饋。三者任一發生，本頁的零件表與熱度就會變。
- **你的選項**：(a) 什麼都不做，先用 `/goal` 把單 session 的完成條件立起來；(b) 只在需要資料不出境時評估自架沙箱；(c) 想要跨 session 記憶又不想綁平台，先看社群自組架構——但目前唯一的成本數字未附方法。

---

## 各零件現在到哪

資料截至 2026-09-06（狀態每週複查，以 [[feature-radar]] 為準）。

| 功能 | 說明 | 狀態 |
|------|------|------|
| 持久記憶（Memory） | 跨 session 保留 agent 知識與狀態 | 公開測試 |
| Dreaming | 任務間隙自動整理記憶，類似睡眠記憶鞏固 | 研究預覽 |
| 20 路並行子代理 | 最高 20 個子代理同時執行 | 公開測試 |
| Outcomes 規格驗證 | Agent 自我驗證輸出是否符合規格文件 | 公開測試 |
| Agent View | 統一面板管理所有並行 session 即時狀態（`claude agents`） | 研究預覽 |
| `/goal` 指令 | fire-and-forget 自動化，小型快速模型驗證完成條件 | 正式發布（v2.1.139） |
| Proactive Workflows | Agent 可主動排程並自動觸發任務，不需人工輸入即可啟動 | 公告（細節待確認，公告後逾 100 天無後續） |
| Capability Curve | Agent 能力曲線追蹤，評估不同任務類型能力進展 | 公告（細節待確認，公告後逾 100 天無後續） |
| 自架沙箱（Self-hosted Sandboxes） | 企業在自有基礎設施執行 agent 工作流，資料不出境 | 公開測試 |
| MCP 隧道（MCP Tunnels） | 私有 MCP 伺服器安全連接 Claude Code，無需暴露公網 | 公開測試 |

---

## 相關議題
- [[entities/claude-code]]（Managed Agents 整合於 Claude Code 工作流；SDK 版本流水與已知問題住該頁）
- [[topics/coding-workflow-guide]]（`/goal`、驗證階梯與內建 subagent 的實際用法）
- [[topics/official-community-gap]]（官方對應程度與社群缺口對照）
- [[topics/community-tech-patterns]]（社群工具 Dreamer 採用類似理念，早於官方功能出現）
- [[entities/pricing]]（訂閱配額與 Agent SDK 計費規則）

## 參考來源

- [[news/2026-07-17]]
- [[news/2026-04-28]]
- [[news/2026-04-30]]
- [[news/2026-05-07]]
- [[news/2026-05-11]]
- [[news/2026-05-12]]
- [[news/2026-05-13]]
- [[news/2026-05-19]]
- [[news/2026-05-16]]
- [Ars Technica 報導](https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/)
- [官方總覽文件](https://platform.claude.com/docs/en/managed-agents/overview)（2026-09-06 查證）
- [官方定價文件](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)（2026-09-06 查證）
- [官方 Dreaming 文件](https://platform.claude.com/docs/en/managed-agents/dreams)（2026-09-06 查證）
- [官方自架沙箱文件](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)（2026-09-06 查證）

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-09-11 | **anthropic-sdk-python v1.5.0** 新增 Managed Agents auto mode 工具權限設定，changelog 首度列出具體項目（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.5.0)）|
| 2026-09-03 | Reddit 貼文宣稱自建開源 agent 框架以同一模型達同準度、成本低最多 75%，未附測試方法與資料集（[原文](https://www.reddit.com/r/LocalLLaMA/comments/1w65ise/we_built_an_opensource_modelneutral_agent_harness/)）|
| 2026-08-19 | **anthropic-sdk-python v0.125.0** 新增 managed agents 的 web search 設定相關功能，官方 changelog 未列出具體項目（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.125.0)）|
| 2026-07-22 | **anthropic-sdk-python v0.118.0** 新增 Managed Agents API 支援，是否與 v0.117.0 dreaming 同批次擴充待確認 ❓ 待查證 ⟨Q-02⟩（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.118.0)）|
| 2026-07-16 | **anthropic-sdk-python v0.117.0** 新增「api: add support for dreaming」，即 Dreaming 記憶整合 API（官方 dreams 文件確認，見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0)）|
| 2026-07-01 | **anthropic-sdk-python v0.115.0** 新增 Managed Agents API 支援，開發者可透過官方 SDK 直接操作（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.115.0)）|
| 2026-05-22 | **自架沙箱完整參考文件發布**（via Reddit r/ClaudeAI 報告 v2.1.145 新增）：企業可在完全自有基礎設施部署受管代理（文件範圍見歷史細節）|
| 2026-05-19 | 新增**自架沙箱（self-hosted sandboxes）**與 **MCP 隧道（MCP tunnels）**：企業可於自有基礎設施執行 agent 工作流，私有 MCP 伺服器無需公開即可連接（the-decoder.com）|
| 2026-05-18 | InfoQ：Anthropic 於 Code With Claude 正式公告 **Proactive Workflows** 與 **Capability Curve** 兩項新能力（各自解什麼見歷史細節）|
| 2026-05-16 | dev.to 深度解析 Dreaming——Agent 於非活躍期間透過 Outcomes 與 Orchestration 自我優化，副標「How Agents Self-Improve While You Sleep」（見歷史細節）|
| 2026-05-13 | v2.1.140 的 `subagent_type` 改為大小寫與分隔符號不敏感（`"Code Reviewer"` → `code-reviewer`），降低配置摩擦；同期 Boris Cherny 公開每晚數千子代理工作流（見歷史細節）|
| 2026-05-12 | v2.1.139 新增 Agent View（Research Preview，多 session 管理面板，`claude agents`）與 `/goal` 指令，是邁向非同步工作流的里程碑 |
| 2026-05-11 | 正式發布（從研究預覽升格）；社群自建 70 天多代理架構開發者分享實戰：Opus 決策層 + OpenCode 工程師層 + 並行研究代理，核心結論是任務簡報品質決定系統成敗；官方 vs 社群自組方案的比較進入主流討論 |
| 2026-05-07 | Python SDK v0.100.0 + TypeScript SDK v0.95.0 新增 Managed Agents 原生支援，雙線同日發布 |
| 2026-05-06 | 「Code with Claude」大會宣布重大更新：Dreaming 記憶整合、20 路子代理並行、Outcomes 規格驗證 |
| 2026-04-30 | 公開測試版推出，Anthropic 定位為「agentic AI 的 AWS」，Managed Agents + Persistent Memory 同步開放 |
| 2026-04-28 | 首次正式宣布加入跨會話記憶功能 |

**歷史細節**
- **自架沙箱參考文件（2026-05-22）**：文件涵蓋 worker 輪詢機制、環境金鑰管理、webhook 喚醒設定、監控方案及客戶自管安全責任，標誌企業化部署從「支援」走向「完整文件化」。
- **Proactive Workflows 與 Capability Curve（2026-05-18）**：前者讓 Agent 可主動（而非被動等待觸發）排程並執行任務，與 Cat Wu「AI 的下一步是主動性（proactivity）」論述一致；後者提供能力曲線追蹤，協助評估 Agent 在不同任務類型的能力進展。
- **dev.to 技術解析（2026-05-16）**：Code with Claude 大會功能的首篇深度技術解析，對關注 agent 長期自主執行行為的開發者有參考價值。
- **Boris Cherny 的數千子代理工作流（2026-05-13）**：由 Business Insider 等主流媒體報導，是 Managed Agents 大規模並行能力的極端現實應用案例（見 [[entities/boris-cherny]]）。

**懸置細節**
- ⟨Q-02⟩ ❓ **待查證**（標 2026-08-10｜查 anthropic-sdk-python、Managed Agents API）：v0.118.0 changelog 未列出具體項目，是否與 v0.117.0 dreaming 支援同批次擴充尚未確認；Dreaming 本身已由官方 dreams 文件確認（2026-09-06 查證），僅 v0.118.0 內容不明待查。

