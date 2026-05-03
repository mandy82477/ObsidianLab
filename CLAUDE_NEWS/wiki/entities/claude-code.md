# Claude Code

**類型：** product
**狀態：** active
**首次出現：** 2025（正式推出）
**最後更新：** 2026-05-03

---

## 現況

Claude Code 是 Anthropic 的 AI 編碼 CLI 工具，支援 agentic 工作流程、MCP Server 整合、Hooks 機制與 Agent Teams。目前為最受開發者關注的 AI 編碼工具之一。近期接連出現效能退步事件（已承認工程疏失）、HERMES.md 靜默計費 bug、API 金鑰外洩漏洞、Auto Compact 失效等問題，安全性與可靠性受到集中審視。v2.1.121 新增 MCP `alwaysLoad` 選項，Runhouse 團隊透過股權收購加入 Anthropic 以強化 agentic 基礎架構。2026-05-03 加入 macOS 電腦使用（computer use）功能，Claude Code 與 Claude Cowork 均可直接控制 macOS 桌面的滑鼠與鍵盤，從純程式碼助理擴展為全桌面自動化代理。

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
- **Auto Compact 失效**（2026-04-28 回報）：context window 滿載後 Auto Compact 未自動觸發，手動執行 `/compact` 亦失效，導致整個 session 鎖死；即使重購額外用量並重啟工具問題仍未解決
- **Prompt Cache Race Condition**（2026-04-27 確認）：連續兩次呼叫 `client.messages.create()` 時，第二個請求約有 40% 機率發生 cache miss；在兩次呼叫之間等待 2 秒可穩定解決；已由 Anthropic 工程師確認追蹤中。見 [Issue #1451](https://github.com/anthropics/anthropic-sdk-python/issues/1451)
- **Tool/Connector Schema 洩漏**（2026-04-27 回報）：Claude Chat（Opus 4.7）在每則訊息末尾附加完整 function schema 及 userStyle 內容，跨對話串持續存在且疑為帳號層級污染，更換新對話串或關閉 userStyle 均無法完全解決，目前無官方修復
- **Speed Bumps 增加**（2026-04-29 回報）：多位長期使用者反映本週起 Claude Code 明顯增加中途暫停詢問的頻率，即使簡單任務也頻繁打斷工作流程，社群猜測與系統層級的行為調整有關，無官方說明
- **OpenClaw 異常計費行為**（2026-04-30，HN 近千則討論）：若 Git 提交訊息或文件內容中含特定 JSON 格式的 "OpenClaw" 字串，Claude Code 會直接拒絕請求，或將帳單 Extra Usage 衝至 100%；表明 Claude Code 正主動掃描 repo 內容並據此改變計費策略，Anthropic 至今未公開說明
- **ANTHROPIC_API_KEY 雲端計費陷阱**（2026-04-30）：雲端環境設置此環境變數時，所有呼叫自動改走 API 計費通道，見 [[entities/pricing]]
- **Claude Projects 對話消失**（2026-04-30 回報）：重度使用者三度遭遇整天的創作對話無故消失，在記錄中留下日期空白，且無法透過搜尋找回
- **Session 歷史 30 天自動刪除**（2026-05-01 確認）：Claude Code 預設在 30 天後自動刪除 session `.jsonl` 歷史檔；可透過 `npx agentinit agent set claude cleanupPeriodDays 365` 將保留期間延長至 365 天
- **AGENTS.md 規範不支援**（2026-05-02，GitHub issue #6235）：Claude Code 目前仍不支援業界漸趨標準化的 `AGENTS.md` 規範，導致跨工具（如 Cursor、GitHub Copilot）協作時面臨配置互操作問題。

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
- **[PullMD](https://www.reddit.com/r/ClaudeAI/comments/1sxzlh6/pullmd_gave_claude_code_an_mcp_server_so_it_stops/)** — MCP server，抓取網頁時先將 HTML 轉換為乾淨 Markdown，避免浪費 token 處理 cookie banner 等無用內容（一般文章有效內容僅佔原始 HTML 約 20%）
- **[Cockpit](https://github.com/alexjbarnes/cockpit)** — 開源 Web UI，讓使用者不再受限於終端機環境操作 Claude Code
- **[Harness](https://github.com/frenchie4111/harness)** — 在多個 Git worktree 上並行管理多個 Claude Code agent，作者對現有工具（cmux、Conductor）不滿而自行開發
- **[CodeThis](https://codethis.dev/)** — MCP 原生 paste bin，支援 100+ 語言語法高亮，AI 可透過 MCP server 直接建立貼文；免費版含 REST API 與 MCP，Pro 方案 $9/月
- **[Claude Exporter](https://chromewebstore.google.com/detail/claude-exporter-claude-ch/mhckealbblinipeplfddmbcohdidkfjf)** — Chrome 擴充功能，可將 Claude 對話匯出為 PDF、Word、Google Docs 或 Notion，支援自訂字型，無需帳號
- **[Throttle Meter](https://www.reddit.com/r/ClaudeAI/comments/1t0aw95/)** — macOS menubar 工具，從 `~/.claude/projects/*.jsonl` 即時計算 session 用量與週配額，無遙測，MIT 授權
- **[Brifly](https://www.getbrifly.com/)** — Claude Code 持久記憶層，儲存專案架構知識讓 AI 跨 session 記住上下文，支援多人協作
- **[Mneme](https://www.reddit.com/r/ClaudeAI/comments/1t0acsf/)** — repo-native CLI，將架構決策（ADR）存於程式碼庫旁並在 Claude 呼叫前自動注入，支援 CI 攔截違反架構的 PR
- **[Nimbalyst](https://github.com/Nimbalyst/nimbalyst)** — 多 Agent 視覺化工作台，支援 Claude Code/Codex/Opencode，含 WYSIWYG diff 逐一審核各 Agent 修改
- **[Trent](https://trent.ai/solutions/claude-code-security/)** — Claude Code 內嵌架構層安全評估，情境化判斷應用邏輯安全性，補足 CVE 掃描盲點
- **[Omar](https://omar.tech)** — TUI 儀表板，可在終端機統一管理大規模 Claude Code Agent 群（宣稱支援 100 個同時運行的 Agent），支援 Agent 層級化管理（類似公司組織架構）
- **[graphify](https://github.com/graphify-dev/graphify)** — Claude Code 插件，透過 Leiden 社群偵測建立程式碼知識圖譜，宣稱每次查詢可減少 71 倍 token 用量；26 天內達 450k+ 下載、40k stars（GitHub #2），社群發現非預期用途：SQL schema、Obsidian vault、學術論文
- **[NanoBrain](https://nanobrain.app/)** — git-backed Markdown 個人知識庫，透過 hook 在 session 結束時進行低延遲（< 50ms）append，整合 Gmail、Google Calendar、Slack 等資料來源定時匯入；適合需要跨 AI Agent 共享長期知識的場景
- **[Council](https://council.armstr.ng/)** — 開源 CLI，自動偵測系統上安裝的 claude、codex、gemini 並平行執行同一 prompt，最後由一個「主持人」模型彙整回答並標記分歧點；MIT 授權
- **[Destiny](https://github.com/xodn348/destiny)** — Claude Code 占卜插件，輸入生日後執行 `/destiny` 取得今日運勢；底層用 Python 計算八字/卦象/五行，確保結果可驗證，文字詮釋層才交由 LLM 生成
- **[Mote](https://www.reddit.com/r/ClaudeAI/comments/1t16urg/)** — 可自主在 Minecraft Bedrock 中遊玩的 Claude Code Agent，另提供 wizard 工具讓任何人只用一個 `.md` 檔案即可創建類似 Agent
- **[Governor](https://github.com/0xhimanshu/governor)** — 宣稱可減少 Claude Code token 浪費的插件；HN 社群質疑其基準測試過於粗糙，僅統計 token 數量而未評估模型輸出品質是否同步下降，效果待嚴謹驗證
- **[Caliber](https://www.reddit.com/r/artificial/comments/1t1o3qa/)** — 開源 AI 代理配置管理工具，統一版本控制 CLAUDE.md、.cursor/rules、AGENTS.md 等跨工具配置文件；本週突破 888 stars，正向社群徵集功能需求
- **[TradingAgents Plugin](https://github.com/lucemia/trading-agents-plugin)** — 將多代理股票分析框架改寫為 Claude Code 插件，在現有 Claude 訂閱下免額外 API 費用執行 7 個並行/序列分析子代理（技術面、基本面、投資組合管理等）

---

## 相關議題

- [[topics/code-quality-decline]]
- [[topics/competitor-landscape]]
- [[topics/ai-agent-safety]]
- [[entities/claude-design]]（AI 設計工具，與 Claude Code 整合尚不完善）
- [[entities/openclaw]]（第三方 agentic 工具，Anthropic 主動管控中）

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-26]]
- [[news/2026-04-27]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [[news/2026-05-02]]
- [[news/2026-05-03]]

## 版本歷史

| 日期 | 事件 |
|------|------|
| 2026-05-03 | macOS 電腦使用（computer use）功能上線：Claude Code / Claude Cowork 可直接控制 macOS 桌面滑鼠與鍵盤，升格為全桌面自動化代理 |
| 2026-05-03 | 新工具：TradingAgents Plugin（免額外 API 費的 7 子代理股票分析框架，訂閱內執行）|
| 2026-05-02 | AGENTS.md 規範不支援（GitHub issue #6235）：跨工具（Cursor/Copilot）配置互操作缺口浮現 |
| 2026-05-02 | 新工具：Governor（token 浪費優化插件，HN 社群存疑）、Caliber（888 stars，統一管理 CLAUDE.md/.cursor/rules/AGENTS.md） |
| 2026-05-02 | v2.1.126：`/model` 選擇器現在從 gateway 的 `/v1/models` 端點列出模型（適用於 `ANTHROPIC_BASE_URL` 自訂 gateway 場景）；新增 `claude project purge` 指令 |
| 2026-05-02 | 社群工具：Omar（100 agent TUI 管理）、graphify（知識圖譜插件 450k+ 下載）、NanoBrain（git-backed 知識庫）、Council（多模型並行 CLI）、Destiny（占卜技能）、Mote（Minecraft agent）|
| 2026-05-02 | GameMaker 正式啟用 Claude Code 整合（AI 輔助遊戲開發工作流程），iCapital 金融平台採用 Anthropic 技術 |
| 2026-04-30 | GameMaker 宣布整合 Claude Code，為遊戲開發者提供 AI 輔助工作流程 |
| 2026-04-30 | v2.1.124 系統提示更新：新增「File modification detected」預算超出提醒機制（+166 tokens）；v2.1.126 精簡核心身份指令（-87 tokens） |
| 2026-04-30 | Claude Security 公開測試版推出，情境化安全評估直接整合於 Claude Code；見 [[entities/claude-security]] |
| 2026-04-30 | TypeScript SDK v0.92.0：改善 Managed API 相關功能 |
| 2026-04-30 | Anthropic 定位為「agentic AI 的 AWS」：Managed Agents + Persistent Memory 公開測試版 |
| 2026-04-29 | Anthropic 發布官方「Champion Kit」：為推動企業採用 Claude Code 的工程師設計，含 30 天推廣計畫、常見疑慮應對話術與分享素材 |
| 2026-04-29 | 社群工具：Cockpit（Web UI）、Harness（多 worktree 並行 agent）、CodeThis（MCP paste bin）、Claude Exporter（匯出至 PDF/Word/Notion）|
| 2026-04-28 | v2.1.121 發布：MCP `alwaysLoad` 選項（設為 true 跳過 tool-search 延遲）、`claude plugin prune` 清除舊外掛 |
| 2026-04-28 | Runhouse 團隊股權收購：分散式 AI 基礎設施與計算編排專家加入 Anthropic，強化 agentic 工作流底層架構 |
| 2026-04-28 | Auto Compact 失效事件被回報，session 鎖死問題無法通過重啟解決 |
| 2026-04-28 | Anthropic 為 Managed Agents 加入跨會話記憶功能（正式公告） |
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
