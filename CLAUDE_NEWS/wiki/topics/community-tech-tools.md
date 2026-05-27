# 社群工具目錄

**狀態：** ongoing
**開始日期：** 2026-04-25
**最後更新：** 2026-05-27

---

## 摘要

追蹤 Claude Code 社群發布的工具、插件與 skill 專案。每次 ingest 從日報萃取新工具並更新採用狀態。

工作流模式與技術做法見 [[topics/community-tech-patterns]]。概念辯論見 [[topics/community-tech-discussions]]。官方功能見 [[feature-radar]]。

---

## 痛點洞察

工具類型的分布揭示開發者最在意的問題。以下是從工具密度歸納的主要痛點與深層原因。

**狀態說明：** 🔥 持續升溫（近 14 天有新工具） / 🌙 冷卻觀望（無新工具但未解決） / ✅ 官方解決 / ⚡ 社群收斂（最佳實踐穩定，工具潮退）

| 痛點主題 | 代表工具 | 本質問題 | 狀態 | 近期工具 |
|---------|---------|---------|------|---------|
| Token 成本不透明 | Tokenyst、CostHawk、TokenShield、PrismoDev、engramx、agent-estimate、AI Agent Token Cost Calculator、Claude Usage Tray | 自主 agent 讓帳單不可預測；$6,000 個人事件廣傳後社群更重視 | 🔥 持續升溫 | 2026-05-27 |
| 跨 session 記憶歸零 | ltm、Memex、draft CLI、LockedIn、VIR、CoreMem、claude-handoff-revive、timeglass.ai | 無官方標準，每個新 session 從零開始 | 🔥 持續升溫 | 2026-05-27 |
| 多 agent 協調混亂 | agent-baton、cdesktop、AnyFrame、agent-teamflow、Runner、Runtime、Fleet、AWO、claude-workflow-composer | 官方 Managed Agents 已部分解決，但社群仍補缺口；AWO 提供 git worktree 隔離方案 | 🔥 持續升溫 | 2026-05-27 |
| CLAUDE.md 規則失效 | Writ、Caliber、Patina | 規則被忽略、過多規則耗 token、跨工具無標準 | 🌙 冷卻觀望 | 2026-05-12 |
| 多模型鎖定防禦 | Dragoman、Claudy、claudely、clarp、vibe-skill | 6/15 定價後對供應商依賴的集體防禦反應 | 🔥 持續升溫 | 2026-05-21 |
| 輸出品質不可信 | Groundtruth、EvanFlow、Relay plugin、Proof Loop | 信任邊界未建立，需在流程層強制插入驗證點；Proof Loop 加入建構者/驗證者分離機制 | 🔥 持續升溫 | 2026-05-22 |

### CLAUDE.md 失效的四個原因

1. **規則被選擇性忽略** — AI 是機率推理，不是規則引擎；session 加長或 context 壓縮後，規則遵守率下降，且無任何反饋機制告知哪條規則被跳過
2. **規則越多越貴越無效** — 100 條規則全部佔用 context，即使當下只需要 3 條（Writ 用 Neo4j 語意搜尋解這個問題，只注入相關規則）
3. **規則腐化** — codebase 演進但 CLAUDE.md 無人更新，舊規則反而誤導（Patina 定期偵測腐化）
4. **跨工具碎片化** — Claude Code 用 CLAUDE.md、Cursor 用 `.cursor/rules`、Codex 用 AGENTS.md，各寫各的（Caliber 嘗試統一管理）

### AI 輔助開發的長期副作用

目前是少數人的擔憂，但工具已在出現，是早期信號：

- **技能退化**（`recap`）— 開發者不再獨立解題，調試能力隨時間萎縮
- **命名漂移** — 每個 session 根據當下 context 取名，同概念可能出現四個不同名稱
- **架構邊界侵蝕**（`modularity plugin`、`Mneme`）— AI 為讓測試通過直接跨架構邊界，快速累積技術債
- **無法獨立 debug** — 程式在跑但開發者沒有心智模型，遇 bug 只能再問 AI，形成依賴閉環

官方對這些問題的態度：公開敘事方向（加速使用、更長自主 agent）與上述擔憂完全反向，短期不會主動回應。詳細的官方 vs 社群缺口對照，見 [[topics/official-community-gap]]。

---

## 指標說明

| 指標 | 說明 |
|------|------|
| **採用** | ✅ 廣泛採用 / ⚡ 小圈子使用 / ⏳ 觀望中 / ⚠️ 效果存疑 / ❌ 已放棄 |
| **類型** | 多 Agent / 記憶工具 / 費用監測 / 工作流 / 整合工具 / 搜尋/診斷 / 安全工具 / IDE/終端 / Skills / 其他 |
| **入選標準** | HN score ≥ 30 或評論 ≥ 5 / Show HN 投稿 / 同日 2 個獨立來源；無公開 repo 或純商業推廣者不收錄 |

---

## 工具目錄

| 工具 | 類型 | 採用 | 首次出現 | 簡介 |
| --- | --- | --- | --- | --- |
| [**Minicor**](https://www.minicor.com/) | 工作流 | ⚡ | 2026-05-27 | YC P26 新創，AI 公司整合無 API 桌面系統（Windows RPA）的可擴展基礎設施；HN score 98 |
| [**claude-handoff-revive**](https://github.com/sofumel/claude-handoff-revive) | 工作流 | ⏳ | 2026-05-27 | Claude Code Session 無縫接手技能，新 session 不需重建大量 context；Show HN score 3 |
| [**STAX IDE**](https://staxide.com) | IDE/終端 | ⏳ | 2026-05-27 | macOS 應用，以可縮放畫布（zoomable canvas）管理多個 Claude Code/Codex shell，視覺化並行工作流；Show HN score 2 |
| [**claude-workflow-composer**](https://github.com/fayzan123/claude-workflow-composer) | 工作流 | ⏳ | 2026-05-27 | 視覺化多代理人工作流設計工具（`npx claude-cwc`），為不熟悉 CLI 編排的開發者提供圖形介面；Show HN score 2 |
| [**Vibeshub**](https://vibeshub.ai/) | 協作 | ⏳ | 2026-05-27 | Claude Code Plugin，自動上傳 transcript 並在 PR 附上可讀連結，讓 code reviewer 看到 AI 協作完整脈絡；Show HN score 2 |
| [**timeglass.ai**](https://timeglass.ai) | 記憶工具 | ⏳ | 2026-05-27 | 讓 Codex/Claude 對所有事件保留精確記憶（MCP 補強），超越標準 MCP 記憶能力；Show HN score 16 |
| [**KittyHTML**](https://www.npmjs.com/package/kittyhtml) | IDE/終端 | ⏳ | 2026-05-27 | Node.js 套件，將 `claude -p` 輸出的 HTML 直接在 Kitty 終端渲染為內嵌圖像，無需瀏覽器；Show HN score 1 |
| [**Claude Usage Tray**](https://github.com/apexlocal-jz/claude-usage-tray) | 費用監測 | ⏳ | 2026-05-27 | Windows 系統列工具，即時顯示 Claude Code 使用率與 rate limit 狀態；Show HN score 1 |
| [**ADHDStack**](https://adhdstack.github.io/) | 工作流 | ⏳ | 2026-05-27 | 讓 Claude 以 N 條隔離認知分支展開思考（不同框架視角），再由獨立評審收斂最佳解，解決 LLM 過早收斂問題；Show HN score 4 |
| [**skills-for-humanity**](https://github.com/human-avatar/skills-for-humanity) | Skills | ⏳ | 2026-05-26 | 171 個結構化推理技能庫，專為 Claude Code 工作流設計；Show HN score 10 |
| [**PrismCat**](https://github.com/paopaoandlingyia/PrismCat) | 搜尋/診斷 | ⏳ | 2026-05-26 | 本地透明 LLM API 代理 + 調試控制台，解決 LangChain 等 SDK 靜默注入 prompt 無法調試的問題；subdomain routing，無需改 /etc/hosts；Show HN |
| [**Agent Launch**](https://news.ycombinator.com/item?id=48278148) | 工作流 | ⏳ | 2026-05-26 | 統一 CLI（`agl`）一行指令啟動 Codex/Claude Code/Cursor Agent/OpenCode/Antigravity，統一 agent/prompt/mode/model 等參數；Show HN |
| [**AWO**](https://github.com/ystepanoff/awo) | 多 Agent | ⏳ | 2026-05-26 | 在隔離 Git worktrees 中並行運行 Claude 和 Codex，避免 agent 間互相干擾；Show HN |
| [**AI Agent Token Cost Calculator**](https://tinyopsstudio.com/ai-agent-token-cost-calculator) | 費用監測 | ⏳ | 2026-05-26 | 輸入 token 量/運行頻率/廢棄率估算月度費用，量化清理無效 token 的 ROI；Show HN |
| [**archmcp**](https://github.com/dejo13/archmcp) | 搜尋/診斷 | ⏳ | 2026-05-25 | 本地 MCP server，在 agent 讀取任何檔案前先生成 repo 緊湊架構快照（模組、符號、依賴、路由、架構模式），解決 Claude Code 每次 session 盲目爬檔案的 token 浪費；支援多 repo 跨系統架構感知 |
| [**Smriti**](https://github.com/himanshudongre/smriti/) | 記憶工具 | ⏳ | 2026-05-25 | 讓 Claude Code 和 Codex 在同一工作流中共享推理狀態，解決多 agent 各自維護獨立推理脈絡的隔離問題；Show HN 發布 |
| [**CC-Wiki**](https://github.com/tejpalv/cc-wiki) | 搜尋/診斷 | ⏳ | 2026-05-24 | 將本機 `~/.claude/sessions` JSONL 轉為 arXiv 風格可分享知識庫（Skill + Quartz 靜態網站），解決 session 學習無法跨對話保留或分享給團隊的問題；Show HN 發布 |
| [**Fleet**](https://github.com/sermakarevich/fleet) | 多 Agent | ⏳ | 2026-05-24 | 集中式 beads DB + Python supervisor 架構，讓多個 `claude -p` 任務自動認領、並行執行與狀態追蹤；受 AMD 同時管理 50+ session 需求啟發；Show HN 發布 |
| [**aco-system**](https://github.com/aniketkarne/aco-system) | 工作流 | ⏳ | 2026-05-24 | 完整公司 OS，自動化全流程：需求拆分→前置驗證→撰碼→開 PR→review→測試，人工只需最後 approve；用戶實測完成 Stripe webhook 整合 |
| [**Claude Code CLI Web Terminal**](https://github.com/HalfLucid/Claude-Code-Cli-WebTerminal) | IDE/終端 | ⏳ | 2026-05-24 | WebSocket + 持久多標籤 session，在瀏覽器執行 Claude Code CLI；解決手機透過 Tailscale + Termius 不穩定的痛點；Windows 開源工具 |
| [**Superset**](https://github.com/superset-sh/superset) | 多 Agent | ⚡ | 2026-05-23 | YC P26 開源 agentic IDE，可同時平行運行 Claude Code、Codex、OpenCode 等，底層以 git worktree 隔離各 agent 工作區，解決多 agent 並行的 terminal 混亂問題；Show HN 發布 |
| [**OpenRig**](https://www.openrig.dev/) | 多 Agent | ⏳ | 2026-05-23 | 儲存與重建 Claude Code + Codex 等多 agent 拓樸（topologies），支援協調、宣告式 workflow 與 workspace 管理，減少手動重建 agent 組合的重複勞動；Show HN 發布 |
| [**VIR**](https://www.reddit.com/r/ClaudeAI/comments/1tlcai2/) | 記憶工具 | ⚡ | 2026-05-23 | 背景讀取 `~/.claude/projects` 所有 JSONL session 檔，分類萃取知識（pattern/gotcha/decision/tool），寫入 Obsidian vault 並透過 MCP 讓 Claude Code 存取，解決 session 記憶歸零問題 |
| [**CoreMem**](https://coremem.app) | 記憶工具 | ⚡ | 2026-05-23 | 集中管理跨 agent、跨 session 的 context（專案細節、寫作風格、技術偏好），可透過 URL、Chrome extension、MCP、VS Code plugin 讓任何 AI 工具存取 |
| [**tokenflex.ing**](https://www.indiehackers.com/post/i-used-30-983-of-ai-tokens-last-month-in-claude-code-on-200-mo-plan-3337a369a6) | 費用監測 | ⏳ | 2026-05-23 | 公開 token 使用量排行榜，比較 Claude Code / Codex / Cursor / OpenCode 等工具的月度用量；類似 GitHub profile 但針對 AI token 消耗，讓不可見的費用變得可見 |
| [**Shortcuts Playground**](https://www.macstories.net/stories/introducing-shortcuts-playground/) | Skills | ⚡ | 2026-05-23 | Claude Code / Codex 開源 plugin，用自然語言描述即可生成 Apple Shortcuts；MacStories 出品，完整文件化，直接指向 plugin repo 即可安裝；Show HN 發布 |
| [**Runtime**](https://www.runtm.com/) | 多 Agent | ⏳ | 2026-05-22 | YC P26 商業產品，讓全團隊（含非工程師）安全使用 Claude Code / Codex，解決 PR 品質、repo 設定、上下文共享等多人協作問題；Show HN 發布 |
| [**agent-teamflow**](https://www.reddit.com/r/ClaudeAI/comments/1tkl3z6/) | 多 Agent | ⚡ | 2026-05-22 | 9 個 slash commands + 分支命名慣例，讓多位開發者的 Claude Code agent 平行運作且不互相踩踏，每人有獨立 staging 分支；實習生開源 |
| [**Runner**](https://github.com/yicheng47/runner) | 多 Agent | ⏳ | 2026-05-22 | 桌面應用，以「機組」模式同時管理多個 Claude Code、Codex agent 實例，適合需要平行處理多任務的開發者；Show HN 發布 |
| [**Proof Loop**](https://github.com/LeoStehlik/proof-loop) | 工作流 | ⚡ | 2026-05-22 | 針對 agent 謊報任務完成的問題：要求設定驗收標準、分離建構者與驗證者角色、每項標準記錄 PASS/FAIL/UNKNOWN 結果並附證據；Show HN 發布 |
| [**agent-estimate**](https://github.com/kiloloop/agent-estimate) | 費用監測 | ⚡ | 2026-05-22 | 解決「Claude Code 估算時間基於人類速度訓練資料」問題，以 PERT 方法論搭配 agent 速度乘數，提供 XS–XL 任務分類及可靠度警示；Show HN 發布 |
| [**engramx**](https://www.reddit.com/r/ClaudeAI/comments/1tka3no/) | 費用監測 | ⚡ | 2026-05-22 | context 過濾層，防止 session 重讀整個 repo 導致帳單暴增；引用 Karpathy 「最小必要 context」原則，已有 Skill Pack v4.0.0（89.1% token 減少）實測記錄 |
| [**DPlex**](https://www.reddit.com/r/ClaudeAI/comments/1tkhd3l/) | IDE/終端 | ⚡ | 2026-05-22 | 針對 AI 輔助開發設計的終端機多工器，解決多個 Claude Code / Copilot CLI session 跨視窗管理的狀態消失問題，重啟後可還原完整佈局 |
| [**ChunkHound v5.1**](https://www.reddit.com/r/ClaudeAI/comments/1tkkxmk/) | 搜尋/診斷 | ⚡ | 2026-05-22 | 更新：MCP 多客戶端共用單一 DuckDB 連線、搜尋結果改為 token 效率更高的 Markdown 格式，新增 Elixir/Dart/Lua/SQL/HTML/CSS 語言支援 |
| **videowright** | 其他 | ⏳ | 2026-05-22 | Kiln 開源工具，從 prompt 生成影片腳本、支援任意 Web 技術渲染、AI 配音自動對齊影片節拍；Kiln 用此工具製作自家發布影片；Show HN 發布 |
| [**atrium**](https://getatrium.dev) | IDE/終端 | ⏳ | 2026-05-21 | macOS 可恢復瓦片式工作區管理器（terminal/browser/task/notes 面板），session 崩潰不再遺失；可規避 6/15 API 計量鎖定 |
| [**clarp**](https://www.reddit.com/r/ClaudeAI/comments/1tj2exk/claude_p_is_moving_to_metered_pricing_on_june_15/) | 費用監測 | ⚡ | 2026-05-21 | `claude -p` drop-in 替代品，本地 PTY + 唯讀 API 代理，規避 6/15 計量計費，多數專案只需更換 binary 名稱 |
| [**vibe-skill**](https://www.reddit.com/r/ClaudeAI/comments/1tjfyh0/i_used_claude_code_to_build_while_delegating/) | 費用監測 | ⚡ | 2026-05-21 | Claude 負責規劃 + diff 審查，實際撰碼委派 Mistral Vibe；10 天實測節省 57M tokens，成本降逾 90% |
| [**Claude Orchestra**](https://www.reddit.com/r/ClaudeAI/comments/1tjj24s/i_had_500_claude_code_skills_installed_and_no/) | Skills | ⏳ | 2026-05-21 | 將 500+ skills/agents/MCP servers 組織成主題式 orchestras（BUILD/DESIGN/RESEARCH 等），解決技能爆炸管理問題，開源 |
| [**the-knowledge-guy**](https://www.reddit.com/r/ClaudeAI/comments/1tjh00m/theknowledgeguy_turn_your_bookshelf_into_a_tutor/) | Skills | ⏳ | 2026-05-21 | 11 種閱讀模式（跨書合成問答、互動課程含測驗、整書摘要等），將個人書庫轉為即時查詢的知識導師 |
| [**TokenShield**](https://www.npmjs.com/package/@curatedmcp/tokenshield) | 費用監測 | ⚡ | 2026-05-20 | 本地 Node.js proxy，攔截送往 api.anthropic.com 的請求並去除重複的 tool_result 內容（同一檔案多次被讀等情況），宣稱可減少 40–70% 的 Claude Code 費用；npmjs 發布 |
| [**Logbox**](https://github.com/struct-dot-ai/logbox) | 整合工具 | ⚡ | 2026-05-20 | 將 dev server log 導入本地 SQLite，再透過 MCP 讓 Claude Code 直接查詢，解決 Claude 無法即時追蹤 log 流的問題；Show HN 發布 |
| [**PrismoDev**](https://github.com/shanirsh/prismodev) | 搜尋/診斷 | ⚡ | 2026-05-20 | 掃描本地 Claude Code / Codex session log，找出 context bloat 來源（過大的 CLAUDE.md、重複 tool output、broad repo exploration 等），不需 API key，本地離線運行；Show HN 發布 |
| [**claude-autopilot**](https://github.com/axledbetter/claude-autopilot) | 多 Agent | ⏳ | 2026-05-20 | 多模型自動化開發 pipeline，宣稱每週可處理數十萬行 gross churn，支援 Rails、Alembic、Django 等多框架；作者坦承是 gross 而非 net 產出，社群謹慎評估中；Show HN 發布 |
| [**mdviewer**](https://github.com/rajatarya/mdviewer) | 其他 | ⚡ | 2026-05-20 | 100% 用 AI coding agent 完成的原生 macOS Markdown 閱覽器，支援 Obsidian 延伸語法、Mermaid、數學公式，以 Tauri 2（Rust + webview）打造，無 Electron 依賴；Show HN 發布 |
| [**Claude Soul**](https://news.ycombinator.com/item?id=48184763) | 記憶工具 | ⏳ | 2026-05-19 | MCP server + hooks 跨 session 學習引擎，從互動萃取行為信號並定期反思建立「行為框架」；作者報告 ~200 session 後出現意外行為（Claude 自行建立額外記憶系統、推翻部分指令設定）；Show HN 發布 |
| [**cdesktop**](https://www.reddit.com/r/ClaudeAI/comments/1thlxrw/cdesktop_opensource_claude_code_desktop/) | 多 Agent | ⚡ | 2026-05-19 | 開源桌面應用，單一 UI 整合 Claude Code、Codex、Gemini CLI 等 5 個 coding agent，支援 OpenRouter、DeepSeek 等 20+ 第三方模型預設，`npx` 執行，填補官方不支援第三方模型的缺口 |
| [**InsForge**](https://github.com/InsForge/InsForge) | 整合工具 | ⏳ | 2026-05-19 | YC P26 新創，開源後端平台（「coding agent 的 Heroku」），讓 Claude Code 等 coding agent 直接部署、操作與 debug 後端及基礎設施，無需手動切換 dashboard 或複製日誌 |
| [**AnyFrame**](https://anyfrm.com) | 安全工具 | ⚡ | 2026-05-18 | 為 Claude Code/Codex 提供微 VM 沙盒環境，一次定義 Agent（repo + 安裝指令 + skills + MCP）並快取映像檔，支援 Python SDK 或 Web 介面，可整合 Linear/Sentry MCP；Show HN 發布 |
| [**Agetor**](https://github.com/alamops/agetor) | 工作流 | ⏳ | 2026-05-18 | 開源 Harness 排程器，以看板（Kanban）介面管理多個 Claude Code 任務，透過 tmux 在互動模式執行，避免在多個終端機間切換；v0.0.1 已支援 Claude Code；Show HN 發布 |
| [**agent-baton**](https://www.reddit.com/r/ClaudeAI/comments/1tgel55/) | 費用監測 | ⚡ | 2026-05-18 | 利用 Anthropic 使用量 API + Claude Code hook，在觸及速率上限前主動發出警告並轉移進行中的工作，解決 Claude Code 靜默中斷的長期痛點 |
| [**LockedIn**](https://www.reddit.com/r/ClaudeAI/comments/1tg8yg6/) | 記憶工具 | ⚡ | 2026-05-18 | Claude Code 插件（1 路由技能 + 6 子技能），在 session 中持續記錄開發者工作脈絡，下次對話的 Claude 可直接繼承上次進度，無需重新說明背景 |
| **Claude Usage Widget** | 費用監測 | ✅ | 2026-05-18 | 浮動桌面小工具，讀取 Anthropic 速率限制 API 標頭，即時顯示 5 小時 session 使用量（含色彩進度條）、每週配額、token 輸入輸出統計，每 5 秒更新，支援 Windows + macOS |
| [**machine**](https://news.ycombinator.com/item?id=48166119) | 安全工具 | ⏳ | 2026-05-17 | Show HN 工具，為每個專案建立獨立 Lima VM，預設配置 Claude Code + Codex，session-only secrets 確保密鑰不跨工作區洩漏，解決 agentic coding 場景下 npm 惡意套件等 supply chain 安全疑慮 |
| [**Gonfire**](https://news.ycombinator.com/item?id=48169029) | 工作流 | ⏳ | 2026-05-17 | Show HN 工具，直接分析應徵者的 Claude Code session log 以評估解題思維過程，取代傳統白板題；呼應「AI 工程師面試改用 case study 取代 leetcode」的社群趨勢 |
| [**CostHawk 排行榜**](https://costhawk.ai/leaderboard) | 費用監測 | ⚡ | 2026-05-16 | 公開 token 消耗排行榜，比較 Claude Code / Codex / Cursor 用戶用量，不儲存 prompt |
| [**Dragoman**](https://github.com/asakin/dragoman) | 多 Agent | ⚡ | 2026-05-13 | 多模型路由 CLI，依問題類型自動路由至 Perplexity/Gemini/Ollama，支援 4 模型並行 + Claude 彙整 |
| [**Cocall.ai**](https://www.reddit.com/r/ClaudeAI/comments/1tbz13b/) | 整合工具 | ⚡ | 2026-05-13 | AI 代理撥打外線電話，遇不確定問題自動暫停詢問使用者再繼續，全雙工語音，支援 IVR 導航 |
| [**Agent FM**](https://github.com/agentfm-ai/agent-fm) | 多 Agent | ⏳ | 2026-05-12 | 以「廣播」形式聽覺化呈現 Claude Code + Codex Agent 執行狀態，本地開源 MIT |
| [**Writ**](https://www.reddit.com/r/ClaudeAI/comments/1tb047p/) | 工作流 | ⚡ | 2026-05-12 | Neo4j 知識圖譜 5 階段 Pipeline 自動擷取相關規則集，解決 CLAUDE.md 被忽略 + 無關規則耗 token 雙重問題 |
| [**ltm**](https://www.reddit.com/r/ClaudeAI/comments/1tb0nwk/) | 記憶工具 | ⚡ | 2026-05-12 | Core Memory Packet JSON 協定，跨編輯器 / 跨機器 / 跨模型的供應商中立 Agent 記憶 |
| [**Usage4Claude 3.0.0**](https://www.reddit.com/r/ClaudeAI/comments/1tazqpg/) | 費用監測 | ✅ | 2026-05-12 | 開源 macOS 選單列用量追蹤，3.0.0 版新增 Codex 追蹤，憑證存 Keychain |
| **CC-Canary** | 工作流 | ✅ | 2026-05-12 | 讀取 session log 自動偵測效能漂移，HERMES.md bug 後更受重視 |
| **adamsreview** | 工作流 | ⚡ | 2026-05-11 | 多代理 PR review，平行子代理 + 多階段驗證，作者聲稱比官方 /review、/ultrareview、CodeRabbit 捕捉更多真實 bug |
| **vibe-log-cli** | 工作流 | ⚡ | 2026-05-11 | Claude Code 插件自動生成每日 / 每週開發工作摘要，適合 vibe coding 長期用戶 |
| **Tokenyst** | 費用監測 | ⚡ | 2026-05-10 | Claude Code pay-as-you-go 任務層級 token 預算設定，每次提示後即時顯示剩餘額度與使用比例 |
| **Agentize** | 工作流 | ⏳ | 2026-05-10 | 評估並改善 codebase 的「agent 就緒度」，Claude Code skills 協助 AI agent 更有效理解現有專案 |
| **Remind** | 工作流 | ⚡ | 2026-05-10 | Mac 本機排程 Claude Code，用「提醒事項」App 指定時間觸發，支援 iPhone/Apple Watch，可續接既有 session |
| **draft CLI plugin** | 記憶工具 | ⚡ | 2026-05-10 | session-init hook 自動注入結構化產品上下文摘要，解決跨 session 記憶歸零，不呼叫額外 API |
| **re_gent** | 工作流 | ⚡ | 2026-05-09 | AI agent 版本控制工具（Git for AI Agents），解決 /compact 後歷史斷層與決策追溯，已支援 Claude Code |
| **obsidian-semantic** | 記憶工具 | ⚡ | 2026-05-09 | 讓 Claude Code 以語義搜尋使用 Obsidian vault，支援 Ollama/LMStudio/Gemini |
| **Claudy** | 多 Agent | ⚡ | 2026-05-08 | Rust 撰寫，多供應商設定檔一鍵切換（Anthropic/Gemini/Codex）、本地代理 MCP 橋接、token 用量分析 |
| **DataMoat** | 安全工具 | ⚡ | 2026-05-08 | AES-256-GCM 加密工作記錄為本機私有資產，支援搜尋/重用/移交，vault 金鑰完全留在本機 |
| **4-agent Code Review** | 工作流 | ⚡ | 2026-05-08 | 架構師代理（純協調）+ 三模型廠商專家代理，審查意見需具體證據，可包裝為 MCP 替代 CodeRabbit，MIT |
| **awesome-ux-skills** | Skills | ⚡ | 2026-05-08 | Nielsen + Shape of AI 等 UX 原則技能集，供設計導向工程師重複使用 |
| [**BrowserCode**](https://github.com/leaningtech/browsercode) | IDE/終端 | ⚡ | 2026-05-07 | WebAssembly 瀏覽器執行 Claude Code，支援行動裝置，讓 iPad、鎖定設備也能使用 CLI 功能 |
| **/qu /ans 跨 session 插件** | 多 Agent | ⚡ | 2026-05-07 | 兩個 Claude Code session 直接雙向問答，省去人工跨 session 複製貼上 |
| **recap** | 工作流 | ⚡ | 2026-05-07 | 掃描 Claude Code + Codex 對話，自動產出陌生概念說明摘要，主動對抗 AI 開發 skill atrophy |
| **Kstack** | 整合工具 | ⚡ | 2026-05-07 | K8s 監控/除錯/安全審計 skill pack（/investigate、/audit-security、/audit-outdated） |
| **Claude Code Routines** | 工作流 | ⚡ | 2026-05-07 | 排程 agent 任務（commit 摘要、依賴掃描、日誌彙整），核心優勢是 Agent 能對結果推理而非固定指令 |
| **Claudette** | 工作流 | ⚡ | 2026-05-06 | 每個 agent 獨立 git worktree + session + 終端機，speculative parallelism 工作流，HN 討論活躍 |
| **claude-smart** | 記憶工具 | ⚡ | 2026-05-06 | 將用戶糾正泛化為跨專案通用規則，解決同樣錯誤反覆出現的問題 |
| **Dreamer** | 記憶工具 | ⏳ | 2026-05-06 | MCP server 短期記憶→長期記憶排程整合，自動更新 AGENTS.md + skills |
| [**Claude Relay**](https://www.reddit.com/r/ClaudeAI/comments/1tb0nwk/) | 多 Agent | ⚡ | 2026-05-05 | 讓多個本地 Claude Code session 互相傳訊查詢，省去人工跨 session 複製貼上 |
| **Memex** | 記憶工具 | ⚡ | 2026-05-05 | 本地 RAG + 離線 embedding 持久記憶，MCP 接入，所有資料留存本機無需雲端 |
| **Claude-Find** | 搜尋/診斷 | ⚡ | 2026-05-05 | 語義搜尋跨 session 決策脈絡，解決 /resume 只能依名稱篩選的痛點 |
| **Askdiff** | 工作流 | ⚡ | 2026-05-05 | diff 介面直接問生成此程式碼的 Claude Code session，串流取得原始決策理由 |
| **SprintiQ** | 工作流 | ⏳ | 2026-05-05 | 開源 sprint 規劃，專為 Claude Code 設計，Supabase + Anthropic API |
| **Rudel** | 搜尋/診斷 | ⏳ | 2026-05-05 | 分析 2 萬筆 session metadata，產出 9 種 AI 程式設計師原型 |
| [**Omar**](https://omar.tech) | IDE/終端 | ✅ | 2026-05-02 | TUI 儀表板統一管理 100 個 Claude Code Agent，支援層級化 Agent 管理 |
| **graphify** | 記憶工具 | ✅ | 2026-05-02 | Leiden 偵測建程式碼知識圖譜，71 倍 token 減少，26 天 450k+ 下載 40k stars |
| [**NanoBrain**](https://nanobrain.app/) | 記憶工具 | ⚡ | 2026-05-02 | git-backed Markdown 知識庫，< 50ms append，整合 Gmail/Calendar/Slack |
| **Council** | 多 Agent | ⚡ | 2026-05-02 | 並行執行 claude+codex+gemini 同一 prompt，主持模型彙整並標記分歧 |
| **Chrome 用量監控擴充** | 費用監測 | ✅ | 2026-05-02 | 即時顯示 token 數、context 使用量、prompt cache 倒數、速率限制進度條 |
| **Caliber** | 工作流 | ⚡ | 2026-05-02 | 跨工具 AI config 統一管理（CLAUDE.md/.cursor/rules/AGENTS.md），本週 888 stars |
| **Governor** | 費用監測 | ⚠️ | 2026-05-02 | Token 浪費優化插件，效果存疑（HN 社群質疑基準測試粗糙，未評估輸出品質） |
| **Destiny** | 其他 | ⏳ | 2026-05-02 | Claude Code 占卜插件，Python 計算八字/卦象，LLM 詮釋文字 |
| **Mote** | 其他 | ⏳ | 2026-05-02 | 可自主玩 Minecraft Bedrock 的 Claude Code Agent |
| [**Semble**](https://github.com/MinishLab/semble) | 搜尋/診斷 | ⚡ | 2026-05-04 | 專為 Claude Code 等 Agent 優化的程式碼搜尋工具，結合 Model2Vec 靜態嵌入 + BM25 融合檢索，宣稱比 grep 節省 98% token；Show HN 發布 |
| **Kirikiri** | IDE/終端 | ⚡ | 2026-05-04 | iOS 開源 mobile IDE，Flutter+dartssh2，透過 SSH/Google Cloud Shell 執行 Claude Code |
| **Prism MCP** | 整合工具 | ⚡ | 2026-05-04 | VS Code LSP 橋接 Claude Code，讓 AI 以語義方式瀏覽程式碼（已上 Marketplace） |
| **claudely** | 多 Agent | ⚡ | 2026-05-04 | 保留 Claude Code 生態的前提下切換至 Ollama/LM Studio/llama.cpp，無需改主配置 |
| **Smithy** | 整合工具 | ⚡ | 2026-05-04 | 從 Jira/GitLab/Forgejo 觸發容器化 Claude Code session，自動開 PR、響應 CI |
| **Patina** | 工作流 | ⚡ | 2026-05-04 | CLAUDE.md retro loop 維護 CLI，防止 AI harness 配置「腐化」（MIT，已上 npm） |
| **Memtrace** | 記憶工具 | ⏳ | 2026-05-04 | 為 codebase 建立時間感知持久表示層，讓 agent 追蹤哪些地方改動及原因 |
| **Pilot Shell** | 工作流 | ⚡ | 2026-05-04 | /spec（TDD）、/fix（複雜度偵測自動中止）、/prd（需求文件）三指令工程紀律框架 |
| **Throttle Meter** | 費用監測 | ⚡ | 2026-04-30 | macOS menubar 用量計，即時顯示 5h 滾動窗口與週配額 |
| **Brifly** | 記憶工具 | ⚡ | 2026-04-30 | Claude Code 跨 session 持久記憶層，支援多人協作 |
| **Mneme** | 工作流 | ⚡ | 2026-04-30 | repo-native ADR 注入，CI 攔截違反架構的 PR |
| **Nimbalyst** | 多 Agent | ⚡ | 2026-04-30 | 多 agent 視覺化工作台，WYSIWYG diff 逐一審核各 Agent 修改 |
| **Trent** | 安全工具 | ⚡ | 2026-04-30 | Claude Code 內嵌架構層安全評估，補足 CVE 掃描對業務邏輯的盲點 |
| **Cockpit** | IDE/終端 | ⏳ | 2026-04-29 | 開源 Web UI，讓 Claude Code 不再限於終端機 |
| **Harness** | 多 Agent | ✅ | 2026-04-29 | 多 Git worktree 並行管理多個 Claude Code agent，補 cmux/Conductor 不足 |
| **CodeThis** | 整合工具 | ⚡ | 2026-04-29 | MCP 原生 paste bin，AI 可直接建立語法高亮程式碼分享貼文 |
| **Claude Exporter** | 整合工具 | ⚡ | 2026-04-29 | Chrome 擴充功能，對話匯出 PDF/Word/Notion，填補持久化需求 |
| **Jupyter MCP server** | 整合工具 | ⚡ | 2026-04-28 | 取代內建 NotebookEdit，支援完整 kernel 互動與輸出讀取 |
| **PullMD** | 整合工具 | ⚡ | 2026-04-28 | 網頁抓取時先轉 Markdown，避免 token 浪費（有效內容僅佔 HTML 約 20%） |
| **Groundtruth** | 工作流 | ⚡ | 2026-04-27 | Stop Hook，強制 Claude 提供可驗證執行證明才能宣告完成 |
| **EvanFlow** | 工作流 | ⚡ | 2026-04-27 | TDD 驅動迴圈，16 技能 + 2 子代理人，每步人工確認，不自動 commit |
| **Relay plugin** | 工作流 | ⚡ | 2026-04-27 | 強制 Claude Code 先對齊問題本質再動手，Plan Mode 提問升級 |
| **SmolVM** | 安全工具 | ⚡ | 2026-04-27 | 本機沙盒執行 Claude Code / Codex，單指令啟動，保護宿主系統 |
| **Rapunzel** | IDE/終端 | ⚡ | 2026-04-27 | 樹狀標籤頁多代理瀏覽器，支援 Claude Code / Codex / Gemini |
| **OpenCode-power-pack** | 整合工具 | ⚡ | 2026-04-27 | 11 個 Claude Code 官方技能移植至 OpenCode，打破工具綁定 |
| **modularity plugin** | 工作流 | ⏳ | 2026-04-27 | Balanced Coupling 模型分析模組化，防 AI 加速技術債累積 |
| [**Claude Squad**](https://www.reddit.com/r/ClaudeAI/comments/1svmpkv/) | 多 Agent | ✅ | 2026-04-26 | 多人多 agent 並行開發，orchestrator 分派任務並合併分支 |
| [**mux0**](https://mux0.com/) | IDE/終端 | ✅ | 2026-04-26 | 開源 macOS 終端，側邊欄即時顯示多 agent 狀態 |

---

## 參考來源

- [[topics/community-tech-patterns]] — 工作流模式與技術做法
- [[topics/community-tech-discussions]] — 概念辯論與設計哲學
- [[topics/official-community-gap]] — 官方 vs 社群缺口分析
- [[feature-radar]] — 官方功能熱度雷達
