# 社群工具目錄

**狀態：** ongoing
**領域：** 🌐 社群
**開始日期：** 2026-04-25
**最後更新：** 2026-07-04

> **最新工具動態**（2026-07-04）
> 07-03 額度焦慮情緒串催生兩款用量監控小工具：LimitBar（macOS 選單列即時額度顯示，source_count 2）與 claude-needs-input（終端機標籤變色提示需要輸入，source_count 2）；同日 CCLimitPing（同一 repo 於 06-07、07-03 兩度 Show HN）更新為最新版本說明並去重合併。本次 lint 汰除 25 筆逾 30 天無後續的 ⏳ 條目（2026-06-01～06-03 首次出現的工具，含 Claudinho、100cc、DepsGuard 等）。

---

## 摘要

追蹤 Claude Code 社群發布的工具、插件與 skill 專案。此頁為 lint 專用，由 /wiki-lint 定期策展；每日 ingest 不更新此頁。日常工作流模式見 [[topics/community-tech-patterns]]，概念辯論見 [[topics/community-tech-discussions]]。

官方功能見 [[feature-radar]]。

---

## 痛點洞察

工具類型的分布揭示開發者最在意的問題。以下是從工具密度歸納的主要痛點與深層原因。

**狀態說明：** 🔥 持續升溫（近 14 天有新工具） / 🌙 冷卻觀望（無新工具但未解決） / ✅ 官方解決 / ⚡ 社群收斂（最佳實踐穩定，工具潮退）

| 痛點主題 | 代表工具 | 本質問題 | 狀態 | 近期工具 |
|---------|---------|---------|------|---------|
| Token 成本不透明 | Tokenyst、CostHawk、TokenShield、PrismoDev、engramx、agent-estimate、token-xray、agentgraphed、context-analyzer、permafrost、Claumon、Claustrophobic、AgentPace、Parcle、token-warden、Pi Extension、LimitBar | 自主 agent 讓帳單不可預測；Parcle 新增 agent 共享記憶層減少重複 context；AgentPace 燃燒速率趨勢可視化；Pi Extension 跨工具 AI credits 最大化；LimitBar 新增 Fable 專屬額度即時顯示，回應 07 月初額度焦慮情緒串 | 🔥 持續升溫 | 2026-07-03 |
| 跨 session 記憶歸零 | ltm、Memex、draft CLI、LockedIn、VIR、CoreMem | 無官方標準，每個新 session 從零開始 | 🔥 持續升溫 | 2026-05-27 |
| 多 agent 協調混亂 | agent-baton、cdesktop、AnyFrame、agent-teamflow、Superset、BeamWeaver | 官方 Managed Agents 已部分解決，但社群仍補缺口；BeamWeaver 以 Elixir OTP 原生提供 graph workflow 與 checkpoint 機制 | 🔥 持續升溫 | 2026-06-19 |
| CLAUDE.md 規則失效 | Writ、Caliber、Patina | 規則被忽略、過多規則耗 token、跨工具無標準 | 🌙 冷卻觀望 | 2026-05-12 |
| 多模型鎖定防禦 | Dragoman、Claudy、claudely、clarp、vibe-skill、Rayline | 6/15 計費切割後供應商依賴防禦反應加速；Rayline 新增 subagent 層級模型路由 | 🔥 持續升溫 | 2026-06-09 |
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

## 值得關注的工具

高門檻精選層：採用為 ✅ 廣泛採用，或 HN score ≥ 50 / Launch HN。其餘工具見下方完整目錄。

### 用量 / 費用監測

| 工具 | 採用 | 亮點 |
| --- | --- | --- |
| **Claude Usage Widget** | ✅ | 跨 Windows/macOS 桌面小工具，即時顯示 session 用量、週配額與 token 統計 |
| **Usage4Claude 3.0.0** | ✅ | macOS 選單列用量追蹤，新增 Codex 支援，憑證存 Keychain |
| **Chrome 用量監控擴充** | ✅ | 瀏覽器即時顯示 token、context、cache 倒數與速率限制 |
| [**ktx**](https://github.com/Kaelio/ktx) | ⏳（HN 79）| Data agent context 層，補足 data warehouse 隱性知識，降低 SQL 幻覺 |

### 多 Agent / 並行協調

| 工具 | 採用 | 亮點 |
| --- | --- | --- |
| **Harness** | ✅ | 多 Git worktree 並行管理多個 Claude Code agent |
| [**Claude Squad**](https://www.reddit.com/r/ClaudeAI/comments/1svmpkv/) | ✅ | 多人多 agent 並行，orchestrator 分派任務並合併分支 |
| [**Omar**](https://omar.tech) | ✅ | TUI 儀表板統一管理 100 個 agent，支援層級化管理 |

### 工作流 / 品質保障

| 工具 | 採用 | 亮點 |
| --- | --- | --- |
| **CC-Canary** | ✅ | 讀 session log 自動偵測效能漂移，HERMES.md bug 後受重視 |
| [**AISlop**](https://github.com/scanaislop/aislop) | ⏳（HN 61）| hook 每次 tool call 後自動掃 AI code smells（空 catch、dead code） |
| [**Intuned**](https://intunedhq.com) | ⏳（Launch HN 110）| YC S22，agent 驅動瀏覽器自動化，automation 以程式碼執行並自我修復 |

### 記憶 / 知識圖譜

| 工具 | 採用 | 亮點 |
| --- | --- | --- |
| **graphify** | ✅ | Leiden 偵測建程式碼知識圖譜，71 倍 token 減少，40k stars |

### IDE / 終端

| 工具 | 採用 | 亮點 |
| --- | --- | --- |
| [**mux0**](https://mux0.com/) | ✅ | 開源 macOS 終端，側邊欄即時顯示多 agent 狀態 |

### 模型路由

| 工具 | 採用 | 亮點 |
| --- | --- | --- |
| [**Workweave Router**](https://github.com/workweave/router) | ⚡（HN 181）| 嵌入 Claude Code / Codex / Cursor 的成本感知自動路由，依任務難度降階選模型，實測成本降 40%+ |

### 環境 / 部署

| 工具 | 採用 | 亮點 |
| --- | --- | --- |
| [**machine0**](https://machine0.io) | ⏳（HN 88）| 一鍵建立/快照持久化 NixOS/Ubuntu VM，適合雲端開發環境 |
| [**Minicor**](https://www.minicor.com/) | ⚡（HN 98）| YC P26，AI 整合無 API 桌面系統（Windows RPA）的可擴展基礎設施 |

### UI 工具

| 工具 | 採用 | 亮點 |
| --- | --- | --- |
| [**bulk-delete-claude-chat**](https://github.com/MatteoLeonesi/bulk-delete-claude-chat) | ⚡（HN 56）| 補足 Claude 網頁版缺乏的批量刪除對話功能 |

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
| [**LimitBar**](https://mikaweiss6.gumroad.com/l/limitbar) | 用量監控 | ⏳ | 2026-07-03 | macOS 選單列 app，每 60 秒輪詢 Anthropic 端點即時顯示 Claude 用量限制（含 Fable 專屬額度），原生 Swift/AppKit 單一二進位 < 1MB，讀取用量端點不消耗 token；Show HN score 2，source_count 2 |
| [**claude-needs-input**](https://github.com/rickardstureborg/claude-needs-input) | 工作流 | ⏳ | 2026-07-03 | 終端機標籤在 Claude Code 需要輸入時脈動變橙色（完成則變綠），用 Haiku + 規則判斷阻塞式 vs 收尾式提問；緩解 AskUserQuestion 60 秒逾時痛點（可搭配 `--disallowed-tools AskUserQuestion`）；Show HN score 3，source_count 2 |
| [**autoharness**](https://github.com/tigerless-labs/autoharness) | Skills | ⏳ | 2026-06-30 | 自學習、自維護的 Claude Code skill 層，旨在讓 agent 能持續優化自身工作流程；Show HN |
| [**second-opinion**](https://github.com/kmcheung12/second-opinion) | 多 Agent | ⏳ | 2026-06-30 | Claude Code skill，在 session 中途向其他模型（Claude、opencode）諮詢第二意見，自動整合相關 context 並支援追問；支援 claude-to-claude、claude-to-opencode、opencode-to-claude 呼叫；Show HN |
| [**Statuslin.es**](https://statuslin.es) | 社群資源 | ⏳ | 2026-06-30 | 社群自建 Claude Code status line 分享網站，所有 status line 在真實容器中渲染截圖驗證，可瀏覽與提交自訂狀態列設定；Show HN score 13 |
| [**Claudete**](https://claudete.co) | 多 Agent | ⏳ | 2026-06-28 | macOS 原生多 Claude Code 實例管理器；解決重開機後 session 中斷問題，提供 flexible grid、1–5 欄切換，針對同時運行多個 agent 的使用者設計；Show HN |
| [**ai-whisper**](https://ai-creed.dev/projects/ai-whisper/) | 多 Agent | ⏳ | 2026-06-28 | 雙 agent（Claude + Codex 或其他組合）共享「baton」輪流持有執行權，evaluator 在每輪完成後把關品質；支援 spec-driven-development、複雜 bug 修復等結構化工作流；Show HN |
| [**Adrafinil**](https://github.com/kageroumado/adrafinil) | 工作流 | ⏳ | 2026-06-28 | Mac 半開蓋保活工具，用 Claude Code hooks 偵測 agent 活躍狀態才觸發 `pmset disablesleep 1`，agent 完成後自動釋放；智慧條件觸發，非強制常開；Show HN score 113 |
| [**AgentWatch**](https://agent-watch.dev/) | 費用監測 | ⏳ | 2026-06-28 | 攔截 LLM 請求層的 runtime budget enforcement，支援 OpenAI / Anthropic / Gemini；修改 base URL 即接入，附不可竄改審計軌跡；防止 runaway agent 費用暴增；Show HN score 7 |
| [**Workweave Router**](https://github.com/workweave/router) | 模型路由 | ⚡ | 2026-06-27 | 成本感知模型路由器，作為 Anthropic/OpenAI 相容 endpoint 運作，依請求難度自動路由模型；起因 Opus 4.7 tokenizer 改版後成本大漲；實測成本降 40%+；Show HN score 181 |
| [**Verity**](https://verity.md) | 工作流 | ⏳ | 2026-06-27 | Codacy 開源的自癒式 Claude Code review gate，每次 agent 執行後自動修復不安全或不乾淨的代碼，並將學習記憶用於下一次 run；`npm install -g @codacy/verity-cli`；Show HN |
| [**TBD**](https://github.com/cheapsteak/tbd) | 多 Agent | ⏳ | 2026-06-27 | Mac 原生 CLI-forward coding agent multiplexer，強調「使用者能手動做的，都要能透過 CLI 讓 agent 自動做」，可搭配 agent-channels 實現跨 worktree 通訊；Show HN |
| [**Prompt Foundry**](https://marketplace.visualstudio.com/items?itemName=sdevries.prompt-foundry) | context 管理工具 | ⏳ | 2026-06-19 | VS Code / Cursor 擴充套件，透過子 prompt 組合 + MCP server 保持 context 新鮮，解決大型 codebase 中 AI 遵循慣有模式導致 context 失效的問題；Show HN |
| [**Sqim**](https://www.sqim.dev/) | 行動開發工具 | ⏳ | 2026-06-19 | 支援 Claude Code、Codex 等 coding agent 從 CLI 直接安裝 iOS 建置到 iPhone，無需 VPN；Show HN |
| [**Everything Claude Code microVM**](https://www.jurniti.com/templates/ecc) | 部署模板 | ⏳ | 2026-06-19 | 一鍵將 @affaan 的 Everything Claude Code 設定（64 agents、261 skills）部署到獨立 microVM，約 3 分鐘內可用；Show HN |
| [**Pi Extension**](https://github.com/sathish316/pi-omniagent-extensions/) | 成本管理工具 | ⏳ | 2026-06-19 | 跨 Cursor、Codex、Claude Code 最大化 AI credits 的瀏覽器擴充套件，使用 ACP 協定；Show HN |
| [**BeamWeaver**](https://github.com/caudena/beam_weaver) | Agent 框架 | ⏳ | 2026-06-19 | Elixir 原生 agent 框架（OTP-native），支援 agents/tool calling/graph workflow/checkpoints/retries，內建 Anthropic adapter，含 WeaveScope 可觀測性；Show HN |
| [**job-search**](https://github.com/agent-data/job-search) | Skills | ⏳ | 2026-06-18 | 開源 Claude Code 插件：學習使用者求職偏好、從 LinkedIn 抓取即時職缺並生成個人化日報，選配每日排程自動執行；Show HN |
| [**LegalRabbit DOCX**](https://github.com/LegalRabbit-AI/legalrabbit-docx-claude-plugin) | 整合工具 | ⏳ | 2026-06-18 | Cowork/Codex DOCX 插件；透過 docx↔HTML 雙向轉換讓 AI 只操作 HTML，減少 2-5 倍 token 消耗，特別適合法律文件紅線審閱；Show HN |
| [**AI Commander**](https://aicommander.dev/) | 整合工具 | ⏳ | 2026-06-18 | 讓 Claude Code 等 AI Agent 以 TeamViewer 方式遠端連線並在使用者機器執行 shell 指令，無需開放 SSH 端口或 VPN；支援 Windows/Mac/Linux；Show HN |
| [**Gorchestra**](https://github.com/jgennari/gorchestra) | 多 Agent | ⏳ | 2026-06-18 | 手機遠端控制無限量 Codex / Claude agents；WebServer + SQLite 持久化；支援 Codex 圖片上傳；macOS brew 安裝；Show HN |
| [**Pagecast**](https://github.com/Amal-David/pagecast) | 整合工具 | ⏳ | 2026-06-18 | Claude Code / Codex 生成的 HTML/Markdown 報告一鍵發布至 Cloudflare Pages，支援穩定 URL、重新發布、watch mode；可替代 Claude Artifacts；Show HN |
| [**Parcle**](https://parcle.ai/) | 費用監測 | ⏳ | 2026-06-18 | Agent 共享記憶層：索引操作情境，讓 agent 在每個任務取得小範圍相關記憶而非重讀全部 context，宣稱減少 60%+ token 消耗；Show HN |
| [**token-warden**](https://github.com/vukkt/token-warden) | 費用監測 | ⏳ | 2026-06-18 | Claude Code token 節省插件；HN score 4（flagged）|
| [**AgentPace**](https://festudio.net/agentpace/) | 費用監測 | ⏳ | 2026-06-17 | macOS 選單列 app，視覺化 Claude Code 和 Codex 使用趨勢與燃燒速率；幫助規劃剩餘配額，避免提前耗盡；Show HN |
| [**Mira**](https://github.com/miracodeai/mira) | 工作流 | ⏳ | 2026-06-17 | 開源自架 AI 程式碼審查器；BYOK（Anthropic / OpenAI / 本地 LLM）；平均審查 77 秒（vs Greptile 5 分鐘）；代碼不離開自有基礎設施；Show HN |
| [**cc-reflection**](https://provi.me/cc-reflection) | 工作流 | ⏳ | 2026-06-17 | 利用 Claude Code EDITOR hook（Ctrl-G）插入 fzf 控制面板，讓 hook 不只是「編輯 prompt」，而是可執行反思種子展開、agent 強化 prompt 等操作的控制中心；HN score 3 |
| [**Offload**](https://github.com/ToxicPine/offloads) | 多 Agent | ⏳ | 2026-06-17 | 跨裝置任務轉移；`/offload` 前綴讓任務在 Mac Mini / VPS 上執行；含 env key 安全傳輸、gh 登入確認、dev server 安全穿透；支援 OpenCode + OpenRouter；HN score 3 |
| [**Kevin**](https://github.com/hvardhan878/kevin) | Skills | ⏳ | 2026-06-17 | 模仿《辦公室》Kevin Malone 風格的 Claude Code 外掛，壓縮輸出省 90% 成本、少 93% 程式碼行；`/plugin install kevin@kevin`；HN score 3 |
| [**AptSelect**](https://aptselect.com) | 整合工具 | ⏳ | 2026-06-17 | 本地優先 LLM 並行測試平台；一次 prompt 同時送 OpenAI、Anthropic、Mistral、Gemini；批次 CSV 評估；手動評分；API key 以 OS keyring 加密；本地 SQLite 儲存；HN score 2 |
| [**claude_code_vs**](https://github.com/firish/claude_code_vs) | IDE/終端 | ⏳ | 2026-06-16 | Visual Studio（非 VS Code）官方 Claude Code 整合空白，社群開發者自建；支援原生 diff 查看器（accept/reject）、自動共享 C#/C++ 編譯錯誤；Show HN score 19 |
| [**Spotlight**](https://www.backplanes.com/) | 監控工具 | ⏳ | 2026-06-16 | 即時顯示 Claude Code 與 Codex 執行狀態，靈感來自作者遭遇 `rm -rf root`、誤部署至 prod 等意外；Show HN score 8 |
| [**Devloop**](https://devloop.sh) | 工作流 | ⏳ | 2026-06-16 | 讓 Codex 實作、Claude Code 對抗性審查（或反過來），循環直到所有驗收標準通過；解決「同模型家族無法客觀審查自身輸出」；macOS；Show HN score 3 |
| [**machine0**](https://machine0.io) | 整合工具 | ⏳ | 2026-06-16 | 一鍵建立、配置、快照持久化 NixOS/Ubuntu VM（CLI 操作）；對 NixOS-as-code 有一流支援；適合 Claude Code 雲端開發環境；Show HN score 88 |
| [**HashMeterAi**](https://github.com/Hash-7777/HashMeterAi) | 費用監測 | ⏳ | 2026-06-16 | 本地優先 AI token 使用量儀表板，涵蓋 Claude Code、Codex、Kimi、Qwen CLI 等，統一監控並提供成就系統；Show HN score 3 |
| [**The Engineer**](https://github.com/FarzamMohammadi/the-engineer) | Agent 框架 | ⏳ | 2026-06-15 | 從 GitHub Issue 到 Merged PR 全流程 agent，整合 Claude Code / OpenCode / Codex；解決 AI coding 工具缺乏「端對端軟體工程」能力的痛點；Show HN score 7 |
| [**Canopy**](https://github.com/juliensimon/canopy) | 多 Agent | ⏳ | 2026-06-15 | macOS 平行沙盒 Claude Code session，多個 worktree 同時執行不互相干擾；Show HN（[flagged]）|
| [**Conan**](https://www.conan.sh/) | 監控工具 | ⏳ | 2026-06-15 | macOS 原生 live HUD，即時顯示 Claude Code 的 timeline（每個 tool call）、context window 用量、token 吞吐量；$29 一次性付款；Show HN score 1 |
| [**zero-1**](https://github.com/thomscoder/zero-1) | 整合工具 | ⏳ | 2026-06-15 | 自然語言生成並即時修改 API endpoints；支援 Claude Code 測試自己生成的程式碼；Show HN score 2 |
| [**bulk-delete-claude-chat**](https://github.com/MatteoLeonesi/bulk-delete-claude-chat) | UI 工具 | ⚡ | 2026-06-13 | 解決 Claude 網頁版缺乏批量刪除對話功能的痛點；自動捲動、全選、刪除（對比 ChatGPT 已有內建批量刪除）；HN score 56 |
| [**cc-pool**](https://github.com/yasyf/cc-pool) | 費用監測 | ⏳ | 2026-06-13 | 預測性負載均衡跨多個 Claude 帳號分配請求，適用高吞吐量 Claude Code 場景；Show HN |
| [**Janus**](https://github.com/kmcheung12/janus) | 整合工具 | ⏳ | 2026-06-13 | MCP 工具，同步收集瀏覽器互動事件與終端輸出整合為事件流，讓 agent 理解 UI 發生了什麼再決定修改方向；Show HN |
| [**TaskPrio**](https://taskprio.com/) | 任務管理 | ⏳ | 2026-06-13 | MCP-native 任務隊列，讓多個 Claude Code / Cursor agent 共享優先排序 backlog，透過 `get_next_task` 依序自動執行，無需 orchestration 膠水代碼；Show HN |
| [**AVP（Agent Vault Proxy）**](https://github.com/inflightsec/agent-vault-proxy) | 安全工具 | ⚡ | 2026-06-12 | 解決 coding agent 持有 API key 的安全風險；placeholder + 最後一刻注入方案，agent 環境中只保存 placeholder，真實金鑰由代理在 wire 層面即時替換；從根本上消除洩露風險；HN Show HN |
| [**Claustrophobic**](https://claustrophobic.xyz) | 費用監測 | ⏳ | 2026-06-12 | 解決 Claude Code 單一訂閱用量上限問題，將多個 Claude 訂閱視為「房間」，自動切換至剩餘額度最多的帳號繼續同一 session；Show HN score（觀望中）|
| [**Workplane**](https://workplane.co) | 整合工具 | ⚡ | 2026-06-12 | 解決 Claude/Codex 輸出的 .md/.html 檔案難以分享問題；可讓 agent 和人類共同協作，支援版本回滾與 MCP 整合；MCP 相容，Claude Desktop、Claude Code、OpenClaw 均可存取共享資料夾；Show HN |
| [**Claumon**](https://github.com/fabioconcina/claumon) | 費用監測 | ⏳ | 2026-06-11 | Gamma process 統計模型預測 Claude Code 用量上限，提供精確可信區間；Go 語言單一二進位，無依賴；HN score 4 |
| [**Foyer**](https://github.com/get-foyer/foyer) | 學習工具 | ⏳ | 2026-06-11 | Claude Code 執行等待期間顯示 agents 正在處理的相關學習內容；早期 MVP；Show HN score 6 |
| [**ShellShot**](https://github.com/APIANT/shellshot) | IDE/終端 | ⏳ | 2026-06-11 | 熱鍵截圖並加注送入 Claude Code CLI；支援 iPad-to-Mac 無線傳輸；圖片針對 token 效率最佳化；Show HN score 2 |
| [**5dive**](https://github.com/5dive-com/5dive) | 多 Agent | ⏳ | 2026-06-11 | 從 Telegram 管理和驅動多個 Claude Code agents；Show HN（已被 flagged）|
| [**Vaportrail**](https://github.com/B33BMO/vaportrail) | 工作流 | ⏳ | 2026-06-11 | Claude Code、Codex 和 OpenCode 的執行記錄工具；已新增 Gemini CLI 和 Aider 支援；Show HN（已被 flagged）|
| [**claude-quota**](https://github.com/grzegorz-raczek-unit8/claude-quota) | IDE/終端 | ⏳ | 2026-06-10 | macOS 選單列即時顯示 Claude Code 配額用量（視覺量規），Show HN score 45 |
| [**OpenYabby**](https://github.com/OpenYabby/OpenYabby) | 多 Agent | ⏳ | 2026-06-10 | 語音控制的多 agent 協調器，整合 Claude Code，支援複雜任務語音驅動自動化；Show HN |
| [**agent-pd**](https://github.com/varmabudharaju/agent-pd/blob/master/README.md) | 安全工具 | ⏳ | 2026-06-10 | 零 token 消耗的子 agent 審計工具，偵測 Claude Code 中的流氓子 agent 行為；Show HN score 6 |
| [**claudefeed**](https://github.com/yeet-src/claudefeed) | 安全工具 | ⏳ | 2026-06-10 | 即時 audit log：監控 Claude Code 每個命令、檔案操作、網路連線；Show HN score 4 |
| [**agentgraphed**](https://github.com/sudomichael/agentgraphed) | 費用監測 | ⏳ | 2026-06-10 | 本地 SQLite 索引所有 Claude Code 對話，提供智能標題、Resume 按鈕、context 分析；Show HN score 3 |
| [**context-analyzer**](https://github.com/manavgup/context-analyzer) | 費用監測 | ⏳ | 2026-06-10 | Context window 使用率分析工具，追蹤工具、compaction、skills、互動的 context 消耗；Show HN score 2 |
| [**permafrost**](https://github.com/jianzhichun/permafrost) | 費用監測 | ⏳ | 2026-06-10 | 凍結 Claude Code prompt 前綴以利用快取，宣稱降低 DeepSeek 費用 64%；Show HN score 3 |
| [**Lanes v0.43.0**](https://lanes.sh/blog/claude-fable-5) | 多 Agent | ⏳ | 2026-06-10 | 並行 agent session 工具更新支援 Claude Fable 5，說明 Fable 5 fallback 機制 |
| [**ktx**](https://github.com/Kaelio/ktx) | 工作流 | ⏳ | 2026-06-10 | Data agent context 層，解決 AI 在 data warehouse 生成「valid 但 incorrect SQL」問題，提供 deprecated columns、業務規則等隱性知識；聲稱為 Anthropic 內部分析引擎開源版，支援 LLM-driven analytics；Show HN score 79 |
| [**Rayline**](https://rayline.ai/) | 模型路由 | ⏳ | 2026-06-09 | Claude Code 相容 LLM gateway，攔截內部路由；主 agent 跑 Opus、subagent 路由至便宜模型或本地模型；確定性設定（非 LLM 決策）；Show HN score 11 |
| [**Guardian Runtime**](https://github.com/ashp15205/guardian-runtime) | 安全工具 | ⏳ | 2026-06-09 | 本地 FinOps + 安全 proxy（localhost:8080），提供 API 硬性預算上限（防 retry 暴衝）、API key/PII 洩漏即時偵測、Terse Mode（宣稱降低輸出 token 成本 40–70%）；支援 OpenAI/Anthropic/Gemini；Show HN |
| [**CapaKit**](https://capakit.com/) | 安全工具 | ⏳ | 2026-06-09 | Sandbox AI coding agent 完整生命週期（建置到執行），監控 build 階段依賴安裝行為，防止 secrets baked into config 與 npm install 惡意腳本；Show HN score 4 |
| [**Storytime**](https://1ps0.info/storytime/) | 工作流 | ⏳ | 2026-06-09 | Claude Code continuity 工具：`/storytime` 指令產生增量文件集合，保存 domain lens 與上下文跨 session 延續；作者日常驅動工具；Show HN score 1 |
| [**cc-bridge**](https://github.com/Incultnitollc/claude-code-live-bridge) | 多 Agent | ⏳ | 2026-06-09 | 兩個 Claude Code 視窗透過單一 JSONL 檔案即時互通；Show HN score 2（[flagged]）|
| [**RunAPI**](https://runapi.ai/) | 整合工具 | ⏳ | 2026-06-09 | 一個 API key 存取 AI video/image/music/LLM；提供 MCP server + CLI skills，可直接在 Claude Code 整合 Kling/Suno/Flux/Gemini/DeepSeek；Show HN score 3 |
| [**Intuned**](https://intunedhq.com) | 工作流 | ⏳ | 2026-06-09 | YC S22；AI agent 驅動的瀏覽器自動化平台，automation 以程式碼執行，agent 自動維護（healing）；Launch HN score 110 |
| [**Levi**](https://ttanv.github.io/levi/) | Agent 框架 | ⏳ | 2026-06-08 | 開源 AlphaEvolve 複現系統；支援 Claude Code / Codex，成本比現有開源框架低達 35 倍；Show HN score 2 |
| [**Claude Code Status Line**](https://www.aimhuge.com/blog/claude-code-status-line) | IDE/終端 | ⏳ | 2026-06-08 | Claude Code status bar 顯示 ctx 使用率、rate-limit 倒數（燃盡計時）、模型選擇與 git branch；HN score 7 |
| [**xword-pipeline**](https://github.com/ekorbia/xword-pipeline) | 創意生成 | ⏳ | 2026-06-09 | Rust fill-engine + Claude clue-writer 生成 NYT 風格填字遊戲；含 QA 審查步驟；Show HN score 3 |
| [**Agam**](https://github.com/CrypticCortex/agam) | 記憶管理 | ⏳ | 2026-06-09 | Activation-based（非向量檢索）Claude Code 長期記憶架構；實驗性；Show HN 入選 |
| [**ARouter**](https://github.com/sricola/arouter) | 模型路由 | ⏳ | 2026-06-09 | OpenAI/Anthropic drop-in proxy，支援成本降低與 failover；社群建議說明與 LiteLLM 差異；Show HN score 2 |
| [**Copilot Vulnerability Harness**](https://github.com/davidreis97/defending-code-reference-harness-copilot) | 安全/漏洞發現 | ⏳ | 2026-06-09 | Anthropic `defending-code-reference-harness` 的 GitHub Copilot CLI 移植版；無 Claude Code 也能執行自主漏洞發現；HN score 1 |
| [**Maggy**](https://www.reddit.com/r/ClaudeAI/comments/1tzqg8i/what_started_as_a_claude_code_scaffolding_repo_is/) | Agent SDK | ⏳ | 2026-06-09 | 由 Claude Code scaffolding repo 演進的全功能開源 AI harness |
| [**dbmachine**](https://github.com/kenm47/dbmachine) | 全棧框架 | ⏳ | 2026-06-09 | Claude 作為後端與前端，僅保留 DB 與 plumbing；「local Supabase with Claude as interface」概念；Show HN 入選 |
| [**makememe**](https://github.com/dhruvmehra/makememe) | 創意工具 | ⏳ | 2026-06-09 | Claude Code meme 生成 CLI，可觸發於 CI 結果或 release；Show HN score 1 |
| [**Lobsteady**](https://lobsteady.com) | 訂閱代理 | ⏳ | 2026-06-09 | $20/月固定費用，讓 Claude Pro/Max 訂閱在 Slack/Discord/Telegram 使用；代理訂閱流量，避免 API 帳單；Show HN score 1 |
| [**CCLimitPing**](https://github.com/wavever/CCLimitPing) | Rate limit 管理 | ⏳ | 2026-07-03 | 讓 Claude Code 與 Codex 的 rate limit 視窗保持連續，5 小時限制解除瞬間自動觸發 continue，防止因斷線導致配額浪費；同 repo 於 06-07 首次 Show HN（score 1）後於 07-03 因額度焦慮情緒串再度 Show HN（score 2） |
| [**Kite Markdown**](https://www.kitemarkdown.com/) | 閱讀工具 | ⏳ | 2026-06-07 | Mac 原生 Markdown 閱讀器，QuickLook 整合，特別為大量閱讀 AI 生成 .md 檔案設計，一次性購買無訂閱；Show HN score 2 |
| [**Lathe**](https://github.com/devenjarvis/lathe) | 學習工具 | ⏳ | 2026-06-07 | 用 LLM 輔助學習新領域而非代勞，生成帶有 source 引用、side-notes 與習題的互動式教學，強制用戶親手輸入程式碼；Show HN score 2 |
| [**Ccgs**](https://github.com/ingram-technologies/claude-git-sessions) | Session 管理 | ⏳ | 2026-06-07 | 透過 Git orphan branch 在團隊間分享 Claude Code session，智慧重寫絕對路徑，支援跨裝置 `--resume` 接續工作；Show HN score 6 |
| [**Sandfence**](https://github.com/sheremetyev/sandfence) | 安全/沙箱 | ⏳ | 2026-06-06 | macOS 原生沙箱工具，限制 Claude Code 與 Codex 對系統資源的存取；Show HN score 1 |
| [**Lazarus**](https://github.com/ExpressGradient/lazarus) | Agent SDK | ⏳ | 2026-06-06 | 長任務 coding agent，以單一 Python runtime 為唯一工具，模型自行撰寫 Python 執行所有操作（inspect/read/edit/test）；針對 FrontierSWE benchmark 設計；HN score 1 |
| [**Busbar**](https://github.com/MattJackson/busbarAI) | 模型路由 | ⏳ | 2026-06-06 | 單一 Rust 二進位 LLM gateway，整合 Anthropic/OpenAI/Gemini/Bedrock/Cohere 6 種協議，客戶端無感知負載均衡；Show HN score 1 |
| [**Local MCP**](https://www.local-mcp.com/en) | 整合工具 | ⏳ | 2026-06-06 | 本地 MCP server，整合 Mail/Calendar/Contacts/Teams/Outlook/Excel 等桌面應用；支援 Claude/ChatGPT/Cursor，GDPR/CCPA 合規；Show HN score 2 |
| [**Zedra**](https://github.com/tanlethanh/zedra) | 遠端控制 | ⏳ | 2026-06-06 | Rust/GPUI 打造的手機控制面板，透過 P2P QUIC/UDP 遠端控制桌面 Claude Code/Codex，支援 iOS/Android 及 Mac/Linux/Windows CLI；Show HN score 2 |
| [**Lich**](https://github.com/RPate97/lich) | 多 Agent | ⏳ | 2026-06-06 | Worktree-aware 本地開發棧協調器，讓每個 coding agent 各自擁有獨立環境（port、DB、log），解決並行代理開發基礎設施衝突；Show HN score 6 |
| [**Gito v4.1.0**](https://github.com/Nayjest/Gito/releases/tag/v4.1.0) | 程式碼審查 | ⏳ | 2026-06-06 | AI 程式碼審查工具，新增 Claude Code 與 Gemini CLI 支援；Show HN score 2 |
| [**FirstDraft**](https://firstdraft.run) | CI/自動化 | ⏳ | 2026-06-05 | AI workers 自動監看 Jira、認領任務、push branch、開 draft PR；支援 Claude Code + Codex；Show HN score 3 |
| [**Claude-o-meter**](https://github.com/joshcarter/claude-o-meter) | 用量監控 | ⏳ | 2026-06-05 | 仿 1980s Corvette 儀錶的 token 燃燒率顯示；紅線 = 剛好在 5 小時結束時耗盡 tokens；Show HN score 2 |
| [**Resume**](https://pennyroyaltea.github.io/resume/) | Session 管理 | ⏳ | 2026-06-05 | CLI 管理 Claude Code + Codex sessions；支援 session 篩選與切換；Show HN score 2 |
| [**Boxes.dev**](https://boxes.dev) | 雲端 IDE | ⏳ | 2026-06-04 | 每個 Claude Code/Codex agent 都有獨立雲端主機，徹底解決 localhost 並行限制；支援手機直接使用；Show HN score 7 |
| [**agent-browser-shield**](https://github.com/pixiebrix/agent-browser-shield) | 安全/防護 | ⏳ | 2026-06-04 | 瀏覽器擴充保護 AI agent 免受網頁暗黑模式（假庫存、誘導點擊）操縱；Show HN score 7 |
| [**Ano**](https://ano.chat) | 團隊溝通 | ⏳ | 2026-06-04 | 輕量 Slack 替代品，以 Claude Code 為內建 assistant；本地優先；Show HN score 6 |
| [**Nori-skillsets**](https://github.com/tilework-tech/nori-skillsets) | Config 管理 | ⏳ | 2026-06-04 | 在不同 agent（Claude Code↔Codex）或不同場景（debug/feature）之間切換 skill 配置；Show HN score 2 |
| [**AI Gauge**](https://github.com/jpajak/ai-gauge) | 用量監控 | ⏳ | 2026-06-04 | 桌面監控 Claude/Codex/Copilot 用量上限，統一顯示 session 與週用量；Show HN score 2 |
| [**Minicor**](https://www.minicor.com/) | 工作流 | ⚡ | 2026-05-27 | YC P26 新創，AI 公司整合無 API 桌面系統（Windows RPA）的可擴展基礎設施；HN score 98 |
| [**Superset**](https://github.com/superset-sh/superset) | 多 Agent | ⚡ | 2026-05-23 | YC P26 開源 agentic IDE，可同時平行運行 Claude Code、Codex、OpenCode 等，底層以 git worktree 隔離各 agent 工作區，解決多 agent 並行的 terminal 混亂問題；Show HN 發布 |
| [**VIR**](https://www.reddit.com/r/ClaudeAI/comments/1tlcai2/) | 記憶工具 | ⚡ | 2026-05-23 | 背景讀取 `~/.claude/projects` 所有 JSONL session 檔，分類萃取知識（pattern/gotcha/decision/tool），寫入 Obsidian vault 並透過 MCP 讓 Claude Code 存取，解決 session 記憶歸零問題 |
| [**CoreMem**](https://coremem.app) | 記憶工具 | ⚡ | 2026-05-23 | 集中管理跨 agent、跨 session 的 context（專案細節、寫作風格、技術偏好），可透過 URL、Chrome extension、MCP、VS Code plugin 讓任何 AI 工具存取 |
| [**Shortcuts Playground**](https://www.macstories.net/stories/introducing-shortcuts-playground/) | Skills | ⚡ | 2026-05-23 | Claude Code / Codex 開源 plugin，用自然語言描述即可生成 Apple Shortcuts；MacStories 出品，完整文件化，直接指向 plugin repo 即可安裝；Show HN 發布 |
| [**agent-teamflow**](https://www.reddit.com/r/ClaudeAI/comments/1tkl3z6/) | 多 Agent | ⚡ | 2026-05-22 | 9 個 slash commands + 分支命名慣例，讓多位開發者的 Claude Code agent 平行運作且不互相踩踏，每人有獨立 staging 分支；實習生開源 |
| [**Proof Loop**](https://github.com/LeoStehlik/proof-loop) | 工作流 | ⚡ | 2026-05-22 | 針對 agent 謊報任務完成的問題：要求設定驗收標準、分離建構者與驗證者角色、每項標準記錄 PASS/FAIL/UNKNOWN 結果並附證據；Show HN 發布 |
| [**agent-estimate**](https://github.com/kiloloop/agent-estimate) | 費用監測 | ⚡ | 2026-05-22 | 解決「Claude Code 估算時間基於人類速度訓練資料」問題，以 PERT 方法論搭配 agent 速度乘數，提供 XS–XL 任務分類及可靠度警示；Show HN 發布 |
| [**engramx**](https://www.reddit.com/r/ClaudeAI/comments/1tka3no/) | 費用監測 | ⚡ | 2026-05-22 | context 過濾層，防止 session 重讀整個 repo 導致帳單暴增；引用 Karpathy 「最小必要 context」原則，已有 Skill Pack v4.0.0（89.1% token 減少）實測記錄 |
| [**DPlex**](https://www.reddit.com/r/ClaudeAI/comments/1tkhd3l/) | IDE/終端 | ⚡ | 2026-05-22 | 針對 AI 輔助開發設計的終端機多工器，解決多個 Claude Code / Copilot CLI session 跨視窗管理的狀態消失問題，重啟後可還原完整佈局 |
| [**ChunkHound v5.1**](https://www.reddit.com/r/ClaudeAI/comments/1tkkxmk/) | 搜尋/診斷 | ⚡ | 2026-05-22 | 更新：MCP 多客戶端共用單一 DuckDB 連線、搜尋結果改為 token 效率更高的 Markdown 格式，新增 Elixir/Dart/Lua/SQL/HTML/CSS 語言支援 |
| [**clarp**](https://www.reddit.com/r/ClaudeAI/comments/1tj2exk/claude_p_is_moving_to_metered_pricing_on_june_15/) | 費用監測 | ⚡ | 2026-05-21 | `claude -p` drop-in 替代品，本地 PTY + 唯讀 API 代理，規避 6/15 計量計費，多數專案只需更換 binary 名稱 |
| [**vibe-skill**](https://www.reddit.com/r/ClaudeAI/comments/1tjfyh0/i_used_claude_code_to_build_while_delegating/) | 費用監測 | ⚡ | 2026-05-21 | Claude 負責規劃 + diff 審查，實際撰碼委派 Mistral Vibe；10 天實測節省 57M tokens，成本降逾 90% |
| [**TokenShield**](https://www.npmjs.com/package/@curatedmcp/tokenshield) | 費用監測 | ⚡ | 2026-05-20 | 本地 Node.js proxy，攔截送往 api.anthropic.com 的請求並去除重複的 tool_result 內容（同一檔案多次被讀等情況），宣稱可減少 40–70% 的 Claude Code 費用；npmjs 發布 |
| [**Logbox**](https://github.com/struct-dot-ai/logbox) | 整合工具 | ⚡ | 2026-05-20 | 將 dev server log 導入本地 SQLite，再透過 MCP 讓 Claude Code 直接查詢，解決 Claude 無法即時追蹤 log 流的問題；Show HN 發布 |
| [**PrismoDev**](https://github.com/shanirsh/prismodev) | 搜尋/診斷 | ⚡ | 2026-05-20 | 掃描本地 Claude Code / Codex session log，找出 context bloat 來源（過大的 CLAUDE.md、重複 tool output、broad repo exploration 等），不需 API key，本地離線運行；Show HN 發布 |
| [**mdviewer**](https://github.com/rajatarya/mdviewer) | 其他 | ⚡ | 2026-05-20 | 100% 用 AI coding agent 完成的原生 macOS Markdown 閱覽器，支援 Obsidian 延伸語法、Mermaid、數學公式，以 Tauri 2（Rust + webview）打造，無 Electron 依賴；Show HN 發布 |
| [**cdesktop**](https://www.reddit.com/r/ClaudeAI/comments/1thlxrw/cdesktop_opensource_claude_code_desktop/) | 多 Agent | ⚡ | 2026-05-19 | 開源桌面應用，單一 UI 整合 Claude Code、Codex、Gemini CLI 等 5 個 coding agent，支援 OpenRouter、DeepSeek 等 20+ 第三方模型預設，`npx` 執行，填補官方不支援第三方模型的缺口 |
| [**AnyFrame**](https://anyfrm.com) | 安全工具 | ⚡ | 2026-05-18 | 為 Claude Code/Codex 提供微 VM 沙盒環境，一次定義 Agent（repo + 安裝指令 + skills + MCP）並快取映像檔，支援 Python SDK 或 Web 介面，可整合 Linear/Sentry MCP；Show HN 發布 |
| [**agent-baton**](https://www.reddit.com/r/ClaudeAI/comments/1tgel55/) | 費用監測 | ⚡ | 2026-05-18 | 利用 Anthropic 使用量 API + Claude Code hook，在觸及速率上限前主動發出警告並轉移進行中的工作，解決 Claude Code 靜默中斷的長期痛點 |
| [**LockedIn**](https://www.reddit.com/r/ClaudeAI/comments/1tg8yg6/) | 記憶工具 | ⚡ | 2026-05-18 | Claude Code 插件（1 路由技能 + 6 子技能），在 session 中持續記錄開發者工作脈絡，下次對話的 Claude 可直接繼承上次進度，無需重新說明背景 |
| **Claude Usage Widget** | 費用監測 | ✅ | 2026-05-18 | 浮動桌面小工具，讀取 Anthropic 速率限制 API 標頭，即時顯示 5 小時 session 使用量（含色彩進度條）、每週配額、token 輸入輸出統計，每 5 秒更新，支援 Windows + macOS |
| [**CostHawk 排行榜**](https://costhawk.ai/leaderboard) | 費用監測 | ⚡ | 2026-05-16 | 公開 token 消耗排行榜，比較 Claude Code / Codex / Cursor 用戶用量，不儲存 prompt |
| [**Dragoman**](https://github.com/asakin/dragoman) | 多 Agent | ⚡ | 2026-05-13 | 多模型路由 CLI，依問題類型自動路由至 Perplexity/Gemini/Ollama，支援 4 模型並行 + Claude 彙整 |
| [**Cocall.ai**](https://www.reddit.com/r/ClaudeAI/comments/1tbz13b/) | 整合工具 | ⚡ | 2026-05-13 | AI 代理撥打外線電話，遇不確定問題自動暫停詢問使用者再繼續，全雙工語音，支援 IVR 導航 |
| [**Writ**](https://www.reddit.com/r/ClaudeAI/comments/1tb047p/) | 工作流 | ⚡ | 2026-05-12 | Neo4j 知識圖譜 5 階段 Pipeline 自動擷取相關規則集，解決 CLAUDE.md 被忽略 + 無關規則耗 token 雙重問題 |
| [**ltm**](https://www.reddit.com/r/ClaudeAI/comments/1tb0nwk/) | 記憶工具 | ⚡ | 2026-05-12 | Core Memory Packet JSON 協定，跨編輯器 / 跨機器 / 跨模型的供應商中立 Agent 記憶 |
| [**Usage4Claude 3.0.0**](https://www.reddit.com/r/ClaudeAI/comments/1tazqpg/) | 費用監測 | ✅ | 2026-05-12 | 開源 macOS 選單列用量追蹤，3.0.0 版新增 Codex 追蹤，憑證存 Keychain |
| **CC-Canary** | 工作流 | ✅ | 2026-05-12 | 讀取 session log 自動偵測效能漂移，HERMES.md bug 後更受重視 |
| **adamsreview** | 工作流 | ⚡ | 2026-05-11 | 多代理 PR review，平行子代理 + 多階段驗證，作者聲稱比官方 /review、/ultrareview、CodeRabbit 捕捉更多真實 bug |
| **vibe-log-cli** | 工作流 | ⚡ | 2026-05-11 | Claude Code 插件自動生成每日 / 每週開發工作摘要，適合 vibe coding 長期用戶 |
| **Tokenyst** | 費用監測 | ⚡ | 2026-05-10 | Claude Code pay-as-you-go 任務層級 token 預算設定，每次提示後即時顯示剩餘額度與使用比例 |
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
| [**Claude Relay**](https://www.reddit.com/r/ClaudeAI/comments/1tb0nwk/) | 多 Agent | ⚡ | 2026-05-05 | 讓多個本地 Claude Code session 互相傳訊查詢，省去人工跨 session 複製貼上 |
| **Memex** | 記憶工具 | ⚡ | 2026-05-05 | 本地 RAG + 離線 embedding 持久記憶，MCP 接入，所有資料留存本機無需雲端 |
| **Claude-Find** | 搜尋/診斷 | ⚡ | 2026-05-05 | 語義搜尋跨 session 決策脈絡，解決 /resume 只能依名稱篩選的痛點 |
| **Askdiff** | 工作流 | ⚡ | 2026-05-05 | diff 介面直接問生成此程式碼的 Claude Code session，串流取得原始決策理由 |
| [**Omar**](https://omar.tech) | IDE/終端 | ✅ | 2026-05-02 | TUI 儀表板統一管理 100 個 Claude Code Agent，支援層級化 Agent 管理 |
| **graphify** | 記憶工具 | ✅ | 2026-05-02 | Leiden 偵測建程式碼知識圖譜，71 倍 token 減少，26 天 450k+ 下載 40k stars |
| [**NanoBrain**](https://nanobrain.app/) | 記憶工具 | ⚡ | 2026-05-02 | git-backed Markdown 知識庫，< 50ms append，整合 Gmail/Calendar/Slack |
| **Council** | 多 Agent | ⚡ | 2026-05-02 | 並行執行 claude+codex+gemini 同一 prompt，主持模型彙整並標記分歧 |
| **Chrome 用量監控擴充** | 費用監測 | ✅ | 2026-05-02 | 即時顯示 token 數、context 使用量、prompt cache 倒數、速率限制進度條 |
| **Caliber** | 工作流 | ⚡ | 2026-05-02 | 跨工具 AI config 統一管理（CLAUDE.md/.cursor/rules/AGENTS.md），本週 888 stars |
| **Governor** | 費用監測 | ⚠️ | 2026-05-02 | Token 浪費優化插件，效果存疑（HN 社群質疑基準測試粗糙，未評估輸出品質） |
| [**Semble**](https://github.com/MinishLab/semble) | 搜尋/診斷 | ⚡ | 2026-05-04 | 專為 Claude Code 等 Agent 優化的程式碼搜尋工具，結合 Model2Vec 靜態嵌入 + BM25 融合檢索，宣稱比 grep 節省 98% token；Show HN 發布 |
| **Kirikiri** | IDE/終端 | ⚡ | 2026-05-04 | iOS 開源 mobile IDE，Flutter+dartssh2，透過 SSH/Google Cloud Shell 執行 Claude Code |
| **Prism MCP** | 整合工具 | ⚡ | 2026-05-04 | VS Code LSP 橋接 Claude Code，讓 AI 以語義方式瀏覽程式碼（已上 Marketplace） |
| **claudely** | 多 Agent | ⚡ | 2026-05-04 | 保留 Claude Code 生態的前提下切換至 Ollama/LM Studio/llama.cpp，無需改主配置 |
| **Smithy** | 整合工具 | ⚡ | 2026-05-04 | 從 Jira/GitLab/Forgejo 觸發容器化 Claude Code session，自動開 PR、響應 CI |
| **Patina** | 工作流 | ⚡ | 2026-05-04 | CLAUDE.md retro loop 維護 CLI，防止 AI harness 配置「腐化」（MIT，已上 npm） |
| **Pilot Shell** | 工作流 | ⚡ | 2026-05-04 | /spec（TDD）、/fix（複雜度偵測自動中止）、/prd（需求文件）三指令工程紀律框架 |
| **Throttle Meter** | 費用監測 | ⚡ | 2026-04-30 | macOS menubar 用量計，即時顯示 5h 滾動窗口與週配額 |
| **Brifly** | 記憶工具 | ⚡ | 2026-04-30 | Claude Code 跨 session 持久記憶層，支援多人協作 |
| **Mneme** | 工作流 | ⚡ | 2026-04-30 | repo-native ADR 注入，CI 攔截違反架構的 PR |
| **Nimbalyst** | 多 Agent | ⚡ | 2026-04-30 | 多 agent 視覺化工作台，WYSIWYG diff 逐一審核各 Agent 修改 |
| **Trent** | 安全工具 | ⚡ | 2026-04-30 | Claude Code 內嵌架構層安全評估，補足 CVE 掃描對業務邏輯的盲點 |
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
| [**Claude Squad**](https://www.reddit.com/r/ClaudeAI/comments/1svmpkv/) | 多 Agent | ✅ | 2026-04-26 | 多人多 agent 並行開發，orchestrator 分派任務並合併分支 |
| [**mux0**](https://mux0.com/) | IDE/終端 | ✅ | 2026-04-26 | 開源 macOS 終端，側邊欄即時顯示多 agent 狀態 |

---

## 參考來源

- [[topics/community-tech-patterns]] — 工作流模式與技術做法
- [[topics/community-tech-discussions]] — 概念辯論與設計哲學
- [[topics/official-community-gap]] — 官方 vs 社群缺口分析
- [[feature-radar]] — 官方功能熱度雷達
