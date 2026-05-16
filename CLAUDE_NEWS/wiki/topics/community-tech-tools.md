# 社群工具目錄

**狀態：** ongoing
**開始日期：** 2026-04-25
**最後更新：** 2026-05-16

---

## 摘要

追蹤 Claude Code 社群發布的工具、插件與 skill 專案。每次 ingest 從日報萃取新工具並更新活躍度與採用狀態。

工作流模式與技術做法見 [[topics/community-tech-patterns]]。概念辯論見 [[topics/community-tech-discussions]]。官方功能見 [[feature-radar]]。

---

## 指標說明

| 指標 | 說明 |
|------|------|
| **活躍** | 🟢 7 天內出現 / 🟡 8–14 天未出現 / 🔴 15 天以上未出現 / ⚫ 已淘汰 |
| **採用** | ✅ 廣泛採用 / ⚡ 小圈子使用 / ⏳ 觀望中 / ⚠️ 效果存疑 / ❌ 已放棄 |

---

## 工具目錄

| 工具 | 類型 | 活躍 | 採用 | 簡介 |
|------|------|------|------|------|
| **Omar** | 終端工具 | 🟢 | ✅ | TUI 儀表板統一管理 100 個 Claude Code Agent，支援層級化 Agent 管理 |
| **graphify** | 知識圖譜 | 🟢 | ✅ | Leiden 偵測建程式碼知識圖譜，71 倍 token 減少，26 天 450k+ 下載 40k stars |
| **Claude Squad** | 協作工具 | 🟢 | ✅ | 多人多 agent 並行開發，orchestrator 分派任務並合併分支 |
| **mux0** | 終端工具 | 🟢 | ✅ | 開源 macOS 終端，側邊欄即時顯示多 agent 狀態 |
| **CC-Canary** | 監測工具 | 🟢 | ✅ | 讀取 session log 自動偵測效能漂移，HERMES.md bug 後更受重視 |
| **Dragoman** | 路由工具 | 🟢 | ⚡ | 多模型路由 CLI，依問題類型自動路由至 Perplexity/Gemini/Ollama，支援 4 模型並行 + Claude 彙整 |
| **Cocall.ai** | MCP 工具 | 🟢 | ⚡ | AI 代理撥打外線電話，遇不確定問題自動暫停詢問使用者再繼續，全雙工語音，支援 IVR 導航 |
| **HiveTerm** | 多 Agent 工作站 | 🟢 | ⚡ | 單一介面管理多個 Claude Code Agent 工作階段，支援任務分派與進度追蹤 |
| **Writ** | 規則強制工具 | 🟢 | ⚡ | Neo4j 知識圖譜 5 階段 Pipeline 自動擷取相關規則集，解決 CLAUDE.md 被忽略 + 無關規則耗 token 雙重問題 |
| **adamsreview** | 工作流 | 🟢 | ⚡ | 多代理 PR review，平行子代理 + 多階段驗證，作者聲稱比官方 /review、/ultrareview、CodeRabbit 捕捉更多真實 bug |
| **Tokenyst** | 監測工具 | 🟢 | ⚡ | Claude Code pay-as-you-go 任務層級 token 預算設定，每次提示後即時顯示剩餘額度與使用比例 |
| **Snyk + Claude Code** | 安全工具 | 🟢 | ⚡ | 60 秒整合 Snyk，對 AI 產出程式碼即時掃描 SQL injection/XSS/金鑰外洩，在進入 repo 前攔截 |
| **Caliber** | 工具 | 🟢 | ⚡ | 跨工具 AI config 統一管理（CLAUDE.md/.cursor/rules/AGENTS.md），本週 888 stars |
| **TradingAgents Plugin** | 多代理 | 🟢 | ⚡ | 7 子代理股票分析（技術面/基本面/投資組合），訂閱內免額外 API 費用 |
| **Code Quest** | Web UI | 🟡 | ⚡ | Claude Code 網頁互動模式 UI，針對 6/15 計費調整設計，最大化訂閱利用效率 |
| **CostHawk 排行榜** | 監測工具 | 🟡 | ⚡ | 公開 token 消耗排行榜，比較 Claude Code / Codex / Cursor 用戶用量，不儲存 prompt |
| **Council** | 多模型 | 🟡 | ⚡ | 並行執行 claude+codex+gemini 同一 prompt，主持模型彙整並標記分歧 |
| **NanoBrain** | 知識庫 | 🟡 | ⚡ | git-backed Markdown 知識庫，< 50ms append，整合 Gmail/Calendar/Slack |
| **Chrome 用量監控擴充** | 監測工具 | 🟡 | ✅ | 即時顯示 token 數、context 使用量、prompt cache 倒數、速率限制進度條 |
| **Claudette** | 工作流 | 🟡 | ⚡ | 每個 agent 獨立 git worktree + session + 終端機，speculative parallelism 工作流，HN 討論活躍 |
| **re_gent** | 版本控制 | 🟡 | ⚡ | AI agent 版本控制工具（Git for AI Agents），解決 /compact 後歷史斷層與決策追溯，已支援 Claude Code |
| **Kstack** | K8s 工具 | 🟡 | ⚡ | K8s 監控/除錯/安全審計 skill pack（/investigate、/audit-security、/audit-outdated） |
| **Claude Code Routines** | 自動化工具 | 🟡 | ⚡ | 排程 agent 任務（commit 摘要、依賴掃描、日誌彙整），核心優勢是 Agent 能對結果推理而非固定指令 |
| **Claudy** | 多供應商工具 | 🟡 | ⚡ | Rust 撰寫，多供應商設定檔一鍵切換（Anthropic/Gemini/Codex）、本地代理 MCP 橋接、token 用量分析 |
| **DataMoat** | 安全工具 | 🟡 | ⚡ | AES-256-GCM 加密工作記錄為本機私有資產，支援搜尋/重用/移交，vault 金鑰完全留在本機 |
| **4-agent Code Review** | 工作流 | 🟡 | ⚡ | 架構師代理（純協調）+ 三模型廠商專家代理，審查意見需具體證據，可包裝為 MCP 替代 CodeRabbit，MIT |
| **ltm** | 記憶工具 | 🟡 | ⚡ | Core Memory Packet JSON 協定，跨編輯器 / 跨機器 / 跨模型的供應商中立 Agent 記憶 |
| **recap** | 反技能退化 | 🟡 | ⚡ | 掃描 Claude Code + Codex 對話，自動產出陌生概念說明摘要，主動對抗 AI 開發 skill atrophy |
| **Usage4Claude 3.0.0** | 監測工具 | 🟡 | ✅ | 開源 macOS 選單列用量追蹤，3.0.0 版新增 Codex 追蹤，憑證存 Keychain |
| **draft CLI plugin** | 記憶工具 | 🟡 | ⚡ | session-init hook 自動注入結構化產品上下文摘要，解決跨 session 記憶歸零，不呼叫額外 API |
| **BrowserCode** | 瀏覽器工具 | 🟡 | ⚡ | WebAssembly 瀏覽器執行 Claude Code，支援行動裝置，讓 iPad、鎖定設備也能使用 CLI 功能 |
| **Claude Relay** | 多 session | 🟡 | ⚡ | 讓多個本地 Claude Code session 互相傳訊查詢，省去人工跨 session 複製貼上 |
| **Memex** | 記憶工具 | 🟡 | ⚡ | 本地 RAG + 離線 embedding 持久記憶，MCP 接入，所有資料留存本機無需雲端 |
| **Claude-Find** | 搜尋工具 | 🟡 | ⚡ | 語義搜尋跨 session 決策脈絡，解決 /resume 只能依名稱篩選的痛點 |
| **Askdiff** | code review | 🟡 | ⚡ | diff 介面直接問生成此程式碼的 Claude Code session，串流取得原始決策理由 |
| **Remind** | 排程工具 | 🟡 | ⚡ | Mac 本機排程 Claude Code，用「提醒事項」App 指定時間觸發，支援 iPhone/Apple Watch，可續接既有 session |
| **Smithy** | CI/CD | 🟡 | ⚡ | 從 Jira/GitLab/Forgejo 觸發容器化 Claude Code session，自動開 PR、響應 CI |
| **Patina** | 維護工具 | 🟡 | ⚡ | CLAUDE.md retro loop 維護 CLI，防止 AI harness 配置「腐化」（MIT，已上 npm） |
| **Semble** | 搜尋工具 | 🟡 | ⚡ | code search 比 grep 少 98% token，Model2Vec + BM25 + RRF，無需 API 金鑰 |
| **Kirikiri** | 行動工具 | 🟡 | ⚡ | iOS 開源 mobile IDE，Flutter+dartssh2，透過 SSH/Google Cloud Shell 執行 Claude Code |
| **Prism MCP** | IDE 整合 | 🟡 | ⚡ | VS Code LSP 橋接 Claude Code，讓 AI 以語義方式瀏覽程式碼（已上 Marketplace） |
| **claudely** | 後端切換 | 🟡 | ⚡ | 保留 Claude Code 生態的前提下切換至 Ollama/LM Studio/llama.cpp，無需改主配置 |
| **Nimbalyst** | 協作工具 | 🟡 | ⚡ | 多 agent 視覺化工作台，WYSIWYG diff 逐一審核各 Agent 修改 |
| **Throttle Meter** | 監測工具 | 🟡 | ⚡ | macOS menubar 用量計，即時顯示 5h 滾動窗口與週配額 |
| **Mneme** | 架構工具 | 🟡 | ⚡ | repo-native ADR 注入，CI 攔截違反架構的 PR |
| **Brifly** | 工作流 | 🟡 | ⚡ | Claude Code 跨 session 持久記憶層，支援多人協作 |
| **Trent** | 安全工具 | 🟡 | ⚡ | Claude Code 內嵌架構層安全評估，補足 CVE 掃描對業務邏輯的盲點 |
| **SmolVM** | 安全工具 | 🟡 | ⚡ | 本機沙盒執行 Claude Code / Codex，單指令啟動，保護宿主系統 |
| **Rapunzel** | 終端工具 | 🟡 | ⚡ | 樹狀標籤頁多代理瀏覽器，支援 Claude Code / Codex / Gemini |
| **CLAUDE.md for K8s** | 安全工具 | 🟡 | ⚡ | 13 條規則防止 Claude 產出不安全 K8s 配置，系統性安全防護框架 |
| **Jupyter MCP server** | 整合工具 | 🟡 | ⚡ | 取代內建 NotebookEdit，支援完整 kernel 互動與輸出讀取 |
| **PullMD** | MCP 工具 | 🟡 | ⚡ | 網頁抓取時先轉 Markdown，避免 token 浪費（有效內容僅佔 HTML 約 20%） |
| **Harness** | 工作流 | 🟡 | ✅ | 多 Git worktree 並行管理多個 Claude Code agent，補 cmux/Conductor 不足 |
| **Groundtruth** | 工作流 | 🟡 | ⚡ | Stop Hook，強制 Claude 提供可驗證執行證明才能宣告完成 |
| **EvanFlow** | 工作流 | 🟡 | ⚡ | TDD 驅動迴圈，16 技能 + 2 子代理人，每步人工確認，不自動 commit |
| **Relay plugin** | 工作流 | 🟡 | ⚡ | 強制 Claude Code 先對齊問題本質再動手，Plan Mode 提問升級 |
| **agent-order** | 工作流 | 🟡 | ⚡ | Codex + Claude 各自獨立寫 PRD 再互相批判，防止答案塌縮 |
| **lipstyk** | 品質工具 | 🟡 | ⚡ | 靜態分析 AI 生成程式碼特有模式 |
| **claude-anyteam** | 整合工具 | 🟡 | ⚡ | 讓 Codex/Gemini 加入 Claude Code Agent Teams |
| **awesome-ux-skills** | 設計工具 | 🔴 | ⚡ | Nielsen + Shape of AI 等 UX 原則技能集，供設計導向工程師重複使用 |
| **OpticOdds MCP** | 垂直整合 | 🔴 | ⏳ | 首個透過 MCP 向 Claude Desktop 提供即時運動賠率資料的 API |
| **obsidian-semantic** | 知識工具 | 🔴 | ⚡ | 讓 Claude Code 以語義搜尋使用 Obsidian vault，支援 Ollama/LMStudio/Gemini |
| **unitmux** | 終端工具 | 🔴 | ⚡ | tmux 環境下 Claude Code 的懸浮視窗，讓輸入介面不干擾編輯器視角 |
| **claude-smart** | 記憶工具 | 🔴 | ⚡ | 將用戶糾正泛化為跨專案通用規則，解決同樣錯誤反覆出現的問題 |
| **Dreamer** | 記憶工具 | 🔴 | ⏳ | MCP server 短期記憶→長期記憶排程整合，自動更新 AGENTS.md + skills |
| **SprintiQ** | 規劃工具 | 🔴 | ⏳ | 開源 sprint 規劃，專為 Claude Code 設計，Supabase + Anthropic API |
| **Rudel** | 分析工具 | 🔴 | ⏳ | 分析 2 萬筆 session metadata，產出 9 種 AI 程式設計師原型 |
| **/qu /ans 跨 session 插件** | 多 session | 🔴 | ⚡ | 兩個 Claude Code session 直接雙向問答，省去人工跨 session 複製貼上 |
| **Memtrace** | 記憶工具 | 🔴 | ⏳ | 為 codebase 建立時間感知持久表示層，讓 agent 追蹤哪些地方改動及原因 |
| **Pilot Shell** | 工作流 | 🔴 | ⚡ | /spec（TDD）、/fix（複雜度偵測自動中止）、/prd（需求文件）三指令工程紀律框架 |
| **Agentize** | 工作流 | 🔴 | ⏳ | 評估並改善 codebase 的「agent 就緒度」，Claude Code skills 協助 AI agent 更有效理解現有專案 |
| **vibe-log-cli** | 自動化工具 | 🔴 | ⚡ | Claude Code 插件自動生成每日 / 每週開發工作摘要，適合 vibe coding 長期用戶 |
| **Agent FM** | 監測工具 | 🔴 | ⏳ | 以「廣播」形式聽覺化呈現 Claude Code + Codex Agent 執行狀態，本地開源 MIT |
| **Cockpit** | 工具 | 🔴 | ⏳ | 開源 Web UI，讓 Claude Code 不再限於終端機 |
| **CodeThis** | MCP 工具 | 🔴 | ⚡ | MCP 原生 paste bin，AI 可直接建立語法高亮程式碼分享貼文 |
| **Claude Exporter** | 工具 | 🔴 | ⚡ | Chrome 擴充功能，對話匯出 PDF/Word/Notion，填補持久化需求 |
| **Linear+Lanes MCP** | 整合工具 | 🔴 | ⚡ | issue-to-code 一鍵流程，Claude Code 直接讀取 Linear 待辦票 |
| **OpenCode-power-pack** | 整合工具 | 🔴 | ⚡ | 11 個 Claude Code 官方技能移植至 OpenCode，打破工具綁定 |
| **WezTerm 主題同步** | 環境配置 | 🔴 | ⚡ | Lua 事件鉤子實現 dark/light 即時同步（issue #2990 暫行方案） |
| **modularity plugin** | 架構工具 | 🔴 | ⏳ | Balanced Coupling 模型分析模組化，防 AI 加速技術債累積 |
| **流程 skill 化** | 工作流 | 🔴 | ✅ | 將多步驟設定流程包裝為單一 skill 取代 README |
| **AI 命名一致性 OSS** | 品質工具 | 🔴 | ⚡ | 強制 Claude Code 等 AI 工具維持一致命名與風格，解決命名漂移技術債 |
| **Destiny** | 趣味工具 | 🔴 | ⏳ | Claude Code 占卜插件，Python 計算八字/卦象，LLM 詮釋文字 |
| **Mote** | 創意工具 | 🔴 | ⏳ | 可自主玩 Minecraft Bedrock 的 Claude Code Agent |
| **Governor** | 工具 | 🔴 | ⚠️ | Token 浪費優化插件，效果存疑（HN 社群質疑基準測試粗糙，未評估輸出品質） |

---

## 參考來源

- [[topics/community-tech-patterns]] — 工作流模式與技術做法
- [[topics/community-tech-discussions]] — 概念辯論與設計哲學
- [[feature-radar]] — 官方功能熱度雷達
