# Claude Code

**類型：** product
**狀態：** active
**首次出現：** 2025（正式推出）
**最後更新：** 2026-05-08

---

## 現況

Claude Code 是 Anthropic 的 AI 編碼 CLI 工具，支援 agentic 工作流程、MCP Server 整合、Hooks 機制與 Agent Teams。目前為最受開發者關注的 AI 編碼工具之一。近期接連出現效能退步事件（已承認工程疏失）、HERMES.md 靜默計費 bug、API 金鑰外洩漏洞、Auto Compact 失效等問題，安全性與可靠性受到集中審視。v2.1.121 新增 MCP `alwaysLoad` 選項，Runhouse 團隊透過股權收購加入 Anthropic 以強化 agentic 基礎架構。2026-05-03 加入 macOS 電腦使用（computer use）功能，Claude Code 與 Claude Cowork 均可直接控制 macOS 桌面的滑鼠與鍵盤，從純程式碼助理擴展為全桌面自動化代理。2026-05-04 重大事件：Anthropic 因人為疏失導致 Claude Code 原始碼外洩，已向各平台發出逾 8,100 次 DMCA 下架請求，引發 AI 生成程式碼版權歸屬的法律辯論，社群分支「Claw-Code」隨之誕生；社群亦發現 Claude Cowork/Desktop 悄悄支援任意第三方 LLM（OpenAI、Gemini、本地模型、企業閘道 Bedrock/Vertex/Foundry），無任何官方公告；Claude Connectors 透過 MCP 擴展至創意工作軟體（Adobe、Blender、Ableton、Affinity、Autodesk Fusion）。2026-05-05 重大進展：Amazon 正式向全體企業員工推出 Claude Code（與 OpenAI Codex 並行），成為大型企業雙品牌 AI 編碼工具並行部署的首例；v2.1.128 發布（`/color` 隨機配色、`/mcp` 顯示各伺服器工具數量）。Claude Code 創始人 Boris Cherny 在 podcast 中宣示「Loops（迴圈執行）是 AI 編碼的未來」，首次公開闡明 Claude Code 的設計哲學核心。2026-05-06 新進展：v2.1.128/129 自動推送至 VS Code 後造成 Windows 用戶 extension 完全無法啟動的嚴重 regression（createRequire polyfill hardcoded build path + Mantle endpoint 認證失效），v2.1.131 已緊急修復，數小時內即回應大量 Reddit 回報；Claude Code 累積 GitHub Stars 達 121,000，成為 AI coding assistant 中增長最具話題性的案例；Python SDK v0.99.0 與 TypeScript SDK v0.94.0 同步發布，新增 workspace 定向功能；Claude Security 從封閉預覽移至公開 Beta，開發者現可在 Claude Code 工作流中直接使用 AI 驅動安全審查功能。Boris Cherny 再次公開宣示「軟體工程已死」，強調 Anthropic 內部已無傳統軟體工程師職位，引發業界廣泛論戰。2026-05-07 重大進展：Anthropic 在「Code with Claude」開發者大會上宣布 Managed Agents 重大升級，包含「Dreaming」記憶整合機制（Agent 在任務間隙自動鞏固記憶）、最高 20 路子代理並行，以及 Outcomes 規格驗證功能，標誌 Agent 框架正式邁向有狀態生產級設計；Python SDK v0.100.0 與 TypeScript SDK v0.95.0 同步新增 Managed Agents 原生支援（見 [[entities/managed-agents]]）。Anthropic 同日宣布與 SpaceX 達成算力合作，即日起 Claude Code Pro/Max 用戶五小時視窗速率上限翻倍、取消尖峰時段降速，API Tier 4+ 用戶速率限制同步提升。v2.1.132 新增 `CLAUDE_CODE_SESSION_ID` 環境變數至 Bash 工具子行程（hooks 可追蹤當前 session）及 `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` 選項。研究者透過 wire trace 截獲 Claude Code 完整系統提示（約 13,000 字），發現 MCP 插件大幅佔用 context window，且「Auto 模式」的權限控制僅是提示詞層面機制，並非底層沙箱強制約束；Claude Code 透過 AWS Bedrock 接入時再次出現功能異常，新功能同步落差問題持續存在。2026-05-08 重大事件：CVE-2026-39861（CVSS 7.7）沙箱逃逸漏洞曝光，攻擊者可透過符號連結（symlink）將檔案寫入工作區目錄以外，已在 v2.1.64 修補，所有舊版用戶應立即升級；同時 Anthropic 對「一鍵 RCE」信任提示問題的公開回應被社群概括為「不應該點確認」，責怪使用者的態度在兩則安全負面消息同日上版的背景下引爆批評，品牌可信度面臨雙重壓力；社群更諷刺 Anthropic 自家宣傳的頂級安全模型 Mythos 事先未能偵測到自身產品漏洞。v2.1.133 同日發布，新增 `worktree.baseRef` 設定（`fresh` | `head`），讓使用者可控制 `--worktree`、`EnterWorktree` 及代理隔離工作樹要從 `origin/<default>` 分支還是本地 `HEAD` 建立。Boris Cherny 在「Code with Claude」大會宣稱「寫程式問題已被解決」並表示厭倦「vibe coding」一詞，言論在 Business Insider、HN、YouTube 等多平台引發廣泛討論，社群反應兩極。Claude Cowork 的 Linux 沙箱持續無法啟動（帳號層級隱性故障），Anthropic 狀態頁顯示正常但問題仍在，暫無官方回應。Claude Sonnet 4.8 外洩資訊出現（Geeky Gadgets 報導），暗示下一代 Sonnet 可能即將到來，官方尚未確認。

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
- **原始碼外洩與 DMCA 風波**（2026-05-04 持續延燒）：Anthropic 因人為疏失導致 Claude Code 原始碼外洩，已向各平台發出逾 8,100 次 DMCA 下架請求，引發 AI 生成程式碼版權歸屬的法律辯論；社群以外洩程式碼為基礎重建的「Claw-Code」分支隨之誕生，影響已超出技術層面。
- **撤銷授權後 session 紀錄持續出現**（2026-05-06 回報）：用戶撤銷 Claude Code 存取授權後，session 紀錄仍持續出現於使用量儀表板，涉及 `user:file_upload`、`user:ccr_inference` 等 scope；解除安裝並清除憑證後問題依然存在，Anthropic 客服兩週未回應。建議立即重置所有 API 金鑰並監控帳號用量；見 [[topics/ai-agent-safety]]
- **Bedrock 功能相容性落差（持續）**（2026-05-07 再次回報）：Claude Code 透過 AWS Bedrock 接入時功能異常，社群指出 Bedrock 與 Anthropic 直接服務的新功能同步速度慣常落後，每次新功能發布後的相容性落差問題已成常態。
- **CVE-2026-39861 沙箱逃逸漏洞**（2026-05-08 公開）：CVSS 7.7 高危漏洞，攻擊者可透過符號連結（symlink）將檔案寫入工作區目錄以外；已在 v2.1.64 修補，所有使用舊版本的用戶應立即升級；自查方式詳見 [GitHub Advisory GHSA-vp62-r36r-9xqp](https://github.com/advisories/GHSA-vp62-r36r-9xqp)；見 [[topics/ai-agent-safety]]
- **Claude Cowork Linux 沙箱啟動失敗**（2026-05-07 回報）：用戶回報 Claude Cowork 的 Linux 沙箱在多台電腦重新安裝後持續無法啟動，Anthropic 狀態頁顯示正常，疑為帳號層級隱性故障，目前無官方回應。

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
- **[Semble](https://github.com/MinishLab/semble)** — 針對大型代碼庫的 Claude Code agent 搜尋效率工具，結合 Model2Vec 靜態嵌入、BM25 與 RRF 重排序，宣稱比 grep 少用 98% 的 token；無需 API 金鑰，解決 agent 搜尋失敗後退化為讀整個檔案的問題
- **[Kirikiri](https://news.ycombinator.com/item?id=47996198)** — 以 Flutter + dartssh2 打造的 iOS 開源 app，透過連接 Google Cloud Shell 或 SSH 伺服器遠端執行 Claude Code，以浮動按鈕取代軟體鍵盤常用指令
- **[JupyterLab Claude Code Extension](https://github.com/stellarshenson/jupyterlab_claude_code_extension)** — 開源 JupyterLab 擴充套件，讓資料科學家直接在 Jupyter 環境使用 Claude Code，無需切換至獨立終端機
- **[Prism MCP](https://www.reddit.com/r/ClaudeAI/comments/1t3gdif/)** — VS Code 擴充套件，透過 MCP 將語言伺服器（LSP）語義導航能力接入 Claude Code，讓 AI 以語義方式瀏覽代碼庫而非依賴 grep；已發布於 VS Code Marketplace
- **[claudely](https://www.reddit.com/r/ClaudeAI/comments/1t38e7c/)** — 在保留 Claude Code 完整插件生態（Skills、MCP、Hooks）的前提下，將後端切換至 LM Studio/Ollama/llama.cpp，無需修改主配置文件
- **[Smithy](https://github.com/smithy-ai/smithy-ai)** — 讓開發者從 Jira、GitLab 或 Forgejo 直接觸發容器化 Claude Code 工作階段，每個 issue 對應獨立容器分支，完成後自動開 PR、回應 CI 並整合 PR 回饋
- **[Patina](https://www.reddit.com/r/ClaudeAI/comments/1t3eurx/)** — 開源 CLI（MIT，已上 npm），透過「retro loop」機制自動維護 CLAUDE.md，防止 AI harness 配置「腐化」（修正行為復發、規則膨脹失焦）
- **[TradingAgents Plugin](https://github.com/lucemia/trading-agents-plugin)** — 將多代理股票分析框架改寫為 Claude Code 插件，在現有 Claude 訂閱下免額外 API 費用執行 7 個並行/序列分析子代理（技術面、基本面、投資組合管理等）
- **[SprintiQ](https://github.com/SprintiQ-Incorporated/sprintiq)** — 開源 sprint 規劃工具，專為 Claude Code 設計，使用 Supabase 與 Anthropic API，自行部署約需 10–15 分鐘；社群對「AI agent 是否需要 sprint planning」存在爭議
- **[Claude Relay](https://github.com/innestic/claude-relay)** — plugin，讓同時開啟的多個本地 Claude Code session（前端、後端、infra）可以互相傳訊查詢，省去人工跨 session 複製貼上
- **[Memex](https://memex-cli.vercel.app/)** — 透過本地 RAG 與離線 embedding 為 Claude 提供跨對話持久記憶，所有資料留存本機，以 MCP 方式接入，無需上傳雲端或額外 API 金鑰
- **[Claude-Find](https://github.com/Cavinooo/claude-find)** — 解決 `/resume` 只能依第一條訊息或自訂名稱篩選的痛點，讓重度用戶可用語義搜尋快速定位過去 session 的決策脈絡，注入現有 session
- **[Askdiff](https://github.com/narghev/askdiff)** — 在 GitHub PR 風格的 diff 介面中，讓開發者可直接對生成程式碼的同一個 Claude Code session 提問（點擊行號），串流取得原始決策理由，解決 code review 時的 context 切換痛點
- **[Rudel](https://app.rudel.ai/wrapped)** — 分析 2 萬筆以上 Claude Code/Codex session metadata，從一致性、強度、repo 廣度、成本密度等維度萃取出 9 種 AI 程式設計師原型，以 Spotify Wrapped 風格互動卡片呈現；資料顯示 4% session 使用了 skills，26% 在早期就被放棄
- **[Claudette](https://utensils.io/claudette/)** — 開源桌面工具，讓每個 Claude Code agent 擁有獨立的 git worktree、session 與終端機，實現 speculative parallelism 工作流（多分支同時執行、無衝突切換）；社群顯示已有開發者手動實踐類似做法數月，工具化需求確實存在
- **[claude-smart](https://github.com/ReflexioAI/claude-smart)** — 開源 Claude Code 外掛，透過將用戶糾正（correction）泛化為跨專案通用規則來解決「同樣錯誤一犯再犯」的問題，聲稱 context footprint 遠低於 claude-mem；社群評價褒貶不一
- **[Dreamer](https://www.reddit.com/r/ClaudeAI/comments/1t5cirj/)** — 開源專案，透過 MCP server 讓 agent 提交短期記憶，再由排程工作整合進長期記憶並更新 AGENTS.md 與 skills，靈感來自 Claude 的 dream mode，支援任意 coding agent
- **[BrowserCode](https://www.reddit.com/r/ClaudeAI/comments/1t67idl/)** — 將 Claude Code 移植至瀏覽器，透過 WebAssembly 運行並支援行動裝置，讓無法安裝 CLI 的環境（iPad、公司鎖定設備）也能使用 Claude Code 核心功能
- **[/qu /ans 跨 session 通訊插件](https://www.reddit.com/r/ClaudeAI/comments/1t65lfq/)** — 讓兩個 Claude Code 工作階段互相通訊：新終端輸入 `/qu` 撥出，舊終端輸入 `/ans` 接聽，直接交換問答，省去人工跨 session 複製貼上
- **[recap](https://github.com/madebywelch/recap)** — 掃描過去 N 天的 Claude Code 與 Codex 對話紀錄，找出開發者遭遇陌生概念的片段，自動產出說明摘要，協助對抗因 AI 加速開發而導致的技能退化（skill atrophy）
- **[Kstack](https://github.com/kubetail-org/kstack)** — 將 Kubernetes 常見除錯任務打包成 Claude Code skill 組（`/investigate`、`/audit-security`、`/audit-outdated`），讓直接在 Claude Code 內監控與排查 K8s 叢集問題成為可能
- **[Claudy](https://www.reddit.com/r/ClaudeAI/comments/1t738bi/)** — 以 Rust 撰寫的 Claude Code 擴充工具，支援多供應商設定檔一鍵切換（Anthropic、Gemini、Codex 等）、本地代理 MCP 橋接及 token 用量分析，解決原生 CLI 在多模型環境配置繁瑣的問題
- **[DataMoat](https://github.com/max-ng/datamoat)** — 以 AES-256-GCM 加密將 AI 代理工作記錄保存為本機私有資產，支援搜尋、重用與移交，vault 金鑰及記錄資料完全留在使用者機器上，適合有資料安全顧慮的企業開發者
- **[4-agent Code Review Workflow](https://www.reddit.com/r/ClaudeAI/comments/1t71wrm/)** — 開源的 4 代理程式碼審查工作流：一位架構師代理（僅協調、不直接產出意見）加三位來自不同模型廠商的專家代理，最終審查意見必須有具體證據支撐，可包裝為 MCP 伺服器供 Claude Code 呼叫替代 CodeRabbit，MIT 授權
- **[awesome-ux-skills](https://github.com/tommyjepsen/awesome-ux-skills)** — 以 Nielsen 和 Shape of AI 等 UX 原則為基礎的 Claude Code 技能集，供設計導向工程師重複使用，減少每次重查設計規範的時間成本

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
- [[news/2026-05-04]]
- [[news/2026-05-05]]
- [[news/2026-05-06]]
- [[news/2026-05-07]]
- [[news/2026-05-08]]

## 版本歷史

| 日期 | 事件 |
|------|------|
| 2026-05-08 | v2.1.133：新增 `worktree.baseRef` 設定（`fresh` \| `head`），讓使用者可控制 `--worktree`、`EnterWorktree` 及代理隔離工作樹要從 `origin/<default>` 分支還是本地 `HEAD` 建立，提供更靈活的多工作樹管理策略 |
| 2026-05-08 | CVE-2026-39861（CVSS 7.7）沙箱逃逸漏洞公開（symlink 逃逸），v2.1.64 已修補；同日爆出 1-click RCE 信任提示問題，Anthropic 回應被批為責怪使用者；見 [[topics/ai-agent-safety]] |
| 2026-05-08 | 新工具：Claudy（Rust 多供應商設定管理 + MCP 橋接）、DataMoat（AES-256-GCM 工作記錄加密保存）、4-agent Code Review（架構師 + 三模型專家審查，MIT）、awesome-ux-skills（Nielsen 等 UX 原則技能集）|
| 2026-05-08 | Claude Sonnet 4.8 外洩資訊出現（Geeky Gadgets 報導），官方尚未確認下一代 Sonnet 規格 |
| 2026-05-07 | v2.1.132：新增 `CLAUDE_CODE_SESSION_ID` 環境變數至 Bash 工具子行程（hooks 可追蹤當前 session）；新增 `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` 選項，供需要控制終端顯示行為的環境使用 |
| 2026-05-07 | Python SDK v0.100.0 里程碑：新增 Managed Agents 多路並行支援；TypeScript SDK v0.95.0 同步新增 Managed Agents API 支援；兩者同日發布 |
| 2026-05-07 | Managed Agents 重大更新（Code with Claude 大會）：Dreaming 記憶整合、最高 20 路子代理並行、Outcomes 規格驗證，標誌 Agent 框架從無狀態走向有狀態；見 [[entities/managed-agents]] |
| 2026-05-07 | SpaceX 算力合作：Pro/Max 五小時視窗速率上限翻倍、取消尖峰降速；API Tier 4+ 速率限制提升；見 [[entities/pricing]] |
| 2026-05-07 | 新工具：BrowserCode（WebAssembly 瀏覽器 + 行動裝置支援）、/qu /ans 跨 session 通訊插件、Kstack（K8s 監控/除錯/安全審計 skill pack）、recap（AI 對話知識點摘要，主動對抗 skill atrophy） |
| 2026-05-06 | v2.1.131 緊急修復：v2.1.128/129 自動推送後 Windows VS Code extension 完全無法啟動（createRequire polyfill hardcoded build path）+ Mantle endpoint 認證失效；數小時內因 Reddit 大量回報而緊急回應 |
| 2026-05-06 | Python SDK v0.99.0 + TypeScript SDK v0.94.0 同步發布，新增 client 層 workspace 定向功能（同一 SDK 實例可針對指定 workspace 發出請求），雙線同日維持功能同步節奏 |
| 2026-05-06 | Claude Code 累積 121,000 GitHub Stars，分析文章探討為何開發者跳過傳統 IDE 直接使用 CLI 工具 |
| 2026-05-06 | Claude Security 從封閉預覽移至公開 Beta，開發者可在 Claude Code 工作流中直接使用 AI 驅動的安全審查功能，無需另行安裝工具；見 [[entities/claude-security]] |
| 2026-05-06 | 新工具：Claudette（每個 agent 獨立 git worktree + session + 終端機的 speculative parallelism 工作流）、claude-smart（將糾正泛化為跨專案通用規則的自我改進插件）、Dreamer（MCP team memory server，支援任意 coding agent） |
| 2026-05-05 | Amazon 正式向全體企業員工部署 Claude Code 與 OpenAI Codex（雙品牌並行），軟體開發體驗 VP Jim Haughwout 內部公告；AI 編碼工具進入大型企業標配部署階段 |
| 2026-05-05 | v2.1.128：`/color`（無參數）隨機選取 session 顯示顏色；`/mcp` 顯示各伺服器工具數量並標記 0 工具連線伺服器；`--plugin-dir` 行為調整 |
| 2026-05-05 | Boris Cherny（Claude Code 創始人）在 podcast 中宣示：已 100% 用 Claude Code 取代手動編碼；「Loops（迴圈執行）是 AI 編碼的未來」，而非單次對話補全 |
| 2026-05-05 | 新工具：SprintiQ（sprint 規劃）、Claude Relay（多 session 互通）、Memex（本地 RAG 持久記憶，MCP）、Claude-Find（語義 session 搜尋）、Askdiff（diff 介面直問同一 session）、Rudel（9 種 AI 程式設計師原型分析） |
| 2026-05-04 | 原始碼外洩事件持續擴大：Anthropic 已向各平台發出逾 8,100 次 DMCA 下架請求，引發 AI 生成程式碼版權歸屬法律辯論，社群分支「Claw-Code」誕生 |
| 2026-05-04 | Claude Cowork/Desktop 悄悄加入支援任意第三方 LLM 功能（OpenAI、Gemini、本地模型、Bedrock/Vertex/Foundry 企業閘道），無任何官方公告，由社群自行發現 |
| 2026-05-04 | Claude Connectors 透過 MCP 擴展至創意工作軟體：Adobe（After Effects/Photoshop/Illustrator）、Blender、Ableton Live、Affinity、Autodesk Fusion |
| 2026-05-04 | Claude API 全球直接存取正式開放，擴大全球服務覆蓋範圍 |
| 2026-05-04 | 新工具：Semble（code search 比 grep 少 98% token）、Kirikiri（iOS mobile IDE）、JupyterLab 擴充套件、Prism MCP（VS Code LSP 橋接）、claudely（本地 LLM 無痛切換）、Smithy（issue tracker 觸發容器化 session）、Patina（CLAUDE.md 維護 CLI） |
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
