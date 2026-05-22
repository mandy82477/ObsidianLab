# Managed Agents

**類型：** feature
**狀態：** active（正式發布）
**首次出現：** 2026-04-28
**最後更新：** 2026-05-22

---

## 現況

Anthropic Managed Agents 是 Claude Platform 上的官方 Agent 框架，提供持久記憶、多路並行執行與可驗證輸出等功能。2026-04-28 首次加入跨會話記憶功能（正式公告）；2026-04-30 推出公開測試版，Anthropic 定位為「agentic AI 的 AWS」。

2026-05-06 在「Code with Claude」開發者大會上宣布重大更新，三項新能力同步推出：

- **Dreaming（夢境記憶整合）**：Agent 在任務間隙自動整理近期事件、萃取值得長期保留的資訊存入記憶，類似人類睡眠時的記憶鞏固機制；Anthropic 首次在官方架構層面解決長跑 Agent 的記憶持久性問題；目前限研究預覽版
- **20 路子代理並行**：最高支援 20 個子代理同時執行，突破過去 Agent Teams 的並行限制
- **Outcomes 規格驗證**：Agent 完成後自我驗證輸出是否符合預定規格文件（spec），代表 AI 代理設計從「盡力而為」走向「可驗證達標」的範式轉變

Python SDK v0.100.0 與 TypeScript SDK v0.95.0 同步新增 Managed Agents 原生支援（2026-05-06/07）。

2026-05-11 週，Managed Agents **正式發布**（從研究預覽升格），Anthropic 定義多代理協作的官方托管服務邊界。一位已自建 multi-agent 系統 70 天的開發者在 Reddit 分享實戰架構：以 Opus 作為決策層、OpenCode 作為工程師層、多個研究代理並行，並指出「**任務簡報的撰寫品質**才是多代理系統成敗的核心」，不依賴官方工具照樣可行；社群開始對官方托管方案與自組架構的功能差距進行系統性比較。

2026-05-13，**v2.1.140** 改善 Agent 工具的 `subagent_type` 參數匹配邏輯，支援大小寫不敏感及分隔符號不敏感（例如 `"Code Reviewer"` 可自動解析為 `code-reviewer`），降低多代理配置的摩擦。同日，Claude Code 創始人 Boris Cherny 公開了每晚讓**數千個 AI 子代理**執行「深度工作」的工作流架構，被 Business Insider 與 Let's Data Science 同步報導，是 Managed Agents 20 路並行能力在個人工作流中的極端應用案例，也是社群對大規模 agentic 工作流的最高需求驗證；見 [[entities/boris-cherny]]。

2026-05-19，Anthropic 在 Managed Agents 平台新增兩項企業重要能力：**自架沙箱（self-hosted sandboxes）** 讓企業客戶可在自有基礎設施上執行 agent 工作流，而非依賴 Anthropic 雲端沙盒，直接回應企業資料不出境與合規需求；**MCP 隧道（MCP tunnels）** 讓私有部署的 MCP 伺服器能安全連接 Claude Code agent，無需將內部服務暴露於公網。此兩項能力搭配 Proactive Workflows，標誌 Anthropic 全面布局企業私有雲 agent 部署場景。詳見 the-decoder.com 報導。

2026-05-18，Anthropic 正式公告兩項新能力：**Proactive Workflows**（主動式工作流程）讓 Agent 能夠自主排程並在適當時機主動觸發任務（而非等待用戶輸入），是 Claude Code 從「被動工具」轉型為「主動 Agent 平台」的關鍵里程碑；**Capability Curve** 提供 Agent 能力曲線追蹤機制，協助用戶和企業客戶評估 Agent 在不同任務類型的能力進展。此公告由 InfoQ 報導，與 Cat Wu 的「AI 的下一步是主動性（proactivity）」論述直接呼應；見 [[entities/cat-wu]]。

2026-05-12，v2.1.139 新增兩項擴展多代理能力的重要功能：**Agent View**（Research Preview）提供統一面板管理所有並行 Claude Code 工作階段的即時狀態（執行中 / 等待輸入 / 已完成），執行 `claude agents` 啟用，解決過去需要手動管理多個終端機視窗的工作流痛點；**`/goal` 指令**實現 fire-and-forget 自動化，用戶設定可驗證的完成條件後，每輪執行結束由一個小型快速模型判斷條件是否成立、未達成則自動開始下一輪，適用於模組遷移、測試全通過等有明確終態的長時間任務，官方稱之為 Claude Code 正式具備「非同步工作流」能力。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 長時間跨 session、需可驗證輸出的 Production Agent |
| 不適合 | 快速原型、一次性任務、預算有限的個人開發者 |

> 詳細最新熱度與其他功能對比見 [[feature-radar]]

---

## 使用指南

### 最快上手：`/goal` 指令（v2.1.139+，無需 SDK）
```
# 在 Claude Code session 中輸入：
/goal [可機器驗證的完成條件]

# 範例：
/goal npm test 執行結果零失敗
/goal tsc --noEmit 零型別錯誤
/goal src/legacy/ 下所有 .js 檔案已轉換為 .ts 且不破壞測試
```
> 每輪執行結束後，由小型快速模型驗證條件是否成立；未達成自動繼續下一輪。

### 多 Session 管理：Agent View（v2.1.139+）
```bash
claude agents
# 面板顯示：▶ running / ⏸ waiting / ✓ done
```

### Python SDK（v0.100.0+）
```python
import anthropic, time

client = anthropic.Anthropic()

# 建立 Agent
agent = client.managed_agents.create(
    name="refactor-agent",
    model="claude-opus-4-20260501",
    instructions="你是一個 Python 重構專家，嚴格遵守 PEP8 規範"
)

# 建立任務，並指定可驗證的 Outcomes
task = client.managed_agents.tasks.create(
    agent_id=agent.id,
    prompt="重構 src/legacy/ 下所有函數，補上完整 type hints",
    outcomes=[
        "所有函數都有完整 type hints",
        "mypy src/ 執行零錯誤",
        "現有測試全數通過"
    ]
)

# 輪詢完成狀態
while task.status not in ["completed", "failed"]:
    time.sleep(10)
    task = client.managed_agents.tasks.retrieve(task.id)

print(f"Task {task.status}: {task.outcome_results}")
```

### TypeScript SDK（v0.95.0+）
```typescript
import Anthropic from '@anthropic-ai/sdk';
const client = new Anthropic();

const task = await client.managedAgents.tasks.create({
  agentId: agent.id,
  prompt: '重構 src/legacy/ 下所有函數',
  outcomes: ['mypy 零錯誤', '所有測試通過']
});

while (!['completed', 'failed'].includes(task.status)) {
  await new Promise(r => setTimeout(r, 10000));
  task = await client.managedAgents.tasks.retrieve(task.id);
}
```

### 關鍵注意事項
- **Outcomes 條件**請寫成可執行指令驗證的形式（`npm test`、`mypy`），避免主觀描述
- **Dreaming** 仍為 Research Preview，不建議用於生產關鍵路徑
- **社群替代方案**：Opus 決策層 + OpenCode 執行層的自組架構仍是可行選擇
- 社群核心洞察：「**任務簡報的撰寫品質才是多代理系統成敗的核心**」（Reddit 70 天自建 multi-agent 開發者，2026-05-11）

---

## 核心功能

| 功能 | 說明 | 狀態 |
|------|------|------|
| 持久記憶（Memory） | 跨 session 保留 agent 知識與狀態 | 公開測試 |
| Dreaming | 任務間隙自動整理記憶，類似睡眠記憶鞏固 | 研究預覽 |
| 20 路並行子代理 | 最高 20 個子代理同時執行 | 公開測試 |
| Outcomes 規格驗證 | Agent 自我驗證輸出是否符合規格文件 | 公開測試 |
| Agent View | 統一面板管理所有並行 session 即時狀態（`claude agents`） | 研究預覽 |
| `/goal` 指令 | fire-and-forget 自動化，小型快速模型驗證完成條件 | 正式發布（v2.1.139） |
| Proactive Workflows | Agent 可主動排程並自動觸發任務，無需等待使用者輸入 | 公開測試 |
| Capability Curve | Agent 能力曲線追蹤，評估不同任務類型能力進展 | 公開測試 |
| 自架沙箱（Self-hosted Sandboxes） | 企業在自有基礎設施執行 agent 工作流，資料不出境 | 公開測試 |
| MCP 隧道（MCP Tunnels） | 私有 MCP 伺服器安全連接 Claude Code，無需暴露公網 | 公開測試 |

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
- [[news/2026-05-11]]
- [[news/2026-05-12]]
- [[news/2026-05-13]]
- [[news/2026-05-19]]
- [[news/2026-05-16]]
- [Ars Technica 報導](https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/)

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-05-22 | **自架沙箱完整參考文件發布**（via Reddit r/ClaudeAI 報告 v2.1.145 新增）：完整文件涵蓋 worker 輪詢機制、環境金鑰管理、webhook 喚醒設定、監控方案及客戶自管安全責任；企業可在完全自有基礎設施上部署受管代理，標誌 Claude Code 企業化部署從「支援」走向「完整文件化」 |
| 2026-05-19 | 新增**自架沙箱（self-hosted sandboxes）**與 **MCP 隧道（MCP tunnels）**：企業客戶可在自有基礎設施執行 agent 工作流，私有 MCP 伺服器無需公開即可連接 Claude Code；the-decoder.com 報導 |
| 2026-05-18 | InfoQ 報導「Code With Claude Announces Managed Agents, Proactive Workflows, Capability Curve」，Anthropic 正式公告 **Proactive Workflows** 與 **Capability Curve** 兩項新能力：Proactive Workflows 讓 Agent 可主動（而非被動等待觸發）排程並執行任務，與 Cat Wu 「AI 的下一步是主動性（proactivity）」論述一致；Capability Curve 提供 Agent 能力曲線追蹤機制，協助用戶評估 Agent 在不同任務類型的能力進展 |
| 2026-05-16 | dev.to 深度文章分析 Managed Agents 三項功能的技術機制：聚焦 Dreaming 機制——Agent 在非活躍期間如何透過 Outcomes 與 Orchestration 進行自我優化，副標「How Agents Self-Improve While You Sleep」；是 Code with Claude 大會功能的首篇深度技術解析，對關注 agent 長期自主執行行為的開發者有參考價值 |
| 2026-05-13 | v2.1.140 改善 `subagent_type` 大小寫不敏感及分隔符號不敏感匹配（`"Code Reviewer"` → `code-reviewer`），降低多代理配置摩擦；Boris Cherny 公開每晚讓數千個 AI 子代理執行「深度工作」的工作流，被 Business Insider 等主流媒體報導，是 Managed Agents 大規模並行能力的極端現實應用案例 |
| 2026-05-12 | v2.1.139 新增 Agent View（Research Preview，統一多 session 管理面板，`claude agents`）與 `/goal` 指令（fire-and-forget 自動化，小型快速模型驗證完成條件），是 Claude Code 邁向真正非同步工作流的關鍵里程碑 |
| 2026-05-11 | 正式發布（從研究預覽升格）；社群自建 70 天多代理架構開發者分享實戰：Opus 決策層 + OpenCode 工程師層 + 並行研究代理，核心結論是任務簡報品質決定系統成敗；官方 vs 社群自組方案的比較進入主流討論 |
| 2026-05-07 | Python SDK v0.100.0 + TypeScript SDK v0.95.0 新增 Managed Agents 原生支援，雙線同日發布 |
| 2026-05-06 | 「Code with Claude」大會宣布重大更新：Dreaming 記憶整合、20 路子代理並行、Outcomes 規格驗證 |
| 2026-04-30 | 公開測試版推出，Anthropic 定位為「agentic AI 的 AWS」，Managed Agents + Persistent Memory 同步開放 |
| 2026-04-28 | 首次正式宣布加入跨會話記憶功能 |
