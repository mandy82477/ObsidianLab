---
page: "topics/community-tech-patterns"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-09-04"
last_news_update: "2026-09-03"
status_main: "ongoing"
days_since_news: 2
parent: null
children: "['topics/community-tech-patterns-archive']"
page_role: "hub"
days_since_news_subtree: 2
inbound_links: 52
attribution_count: 109
attribution_last: "2026-09-03"
top_source: "devto"
pending_count: 6
pending_overdue: 0
pending_next_review: "2026-09-13"
pending_signalled: 1
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---

# 社群實戰模式庫

**狀態：** ongoing
**領域：** 🌐 社群
**開始日期：** 2026-04-25
**最後更新：** 2026-09-04
**最後新聞更新：** 2026-09-03

> **最新工作流模式**（2026-09-02）
> - **存量盤點雙響再破紀錄**：thedotmack/claude-mem（9.3 萬星，跨 7 種以上 harness 的 AI 壓縮持久記憶）與 addyosmani/agent-skills（9.2 萬星，Addy Osmani 具名生產級技能集合）本庫首次收錄。
> - **dev.to 四連發**：記憶實測、殭屍 subagent 自動偵測、發展「爆炸半徑」風險分區框架（承接 08-30 遞迴刪檔教訓）、多平台發布 Skill，皆屬第一手實作／框架分享。

---

## 摘要

追蹤 Claude Code 社群在實際開發中累積的**工作流與應用模式**。本頁收錄的模式類型包括 Multi-agent 架構、Skills 設計、CLAUDE.md 管理、Hooks 與自動化、模型使用策略、Token 成本優化、記憶與知識管理、Plugin/MCP 整合等，持續累積形成社群最佳實踐知識庫。

工具目錄（活躍度 / 採用狀態）見 [[topics/community-tech-tools]]。概念辯論、設計哲學與技術反思見 [[topics/community-tech-discussions]]。本頁模式萃取出的**宏觀趨勢 + 對現有設計的啟示**見 [[topics/community-pattern-trends]]（週更）。技術彙整已按月份分組，可由月份標題快速跳轉。

大型 codebase 上的規模化開發（並行規模極限、Context/Token 管理、Codebase 索引與記憶、除錯與分工架構）已縫成主題式主線，見 [[topics/community-large-codebase-workflow]]。

**官方指引對照（2026-07-26）：** Anthropic 部落格〈Claude 5 世代模型的 context engineering 新規則〉揭露官方已移除逾 80% 的 Claude Code 系統提示詞，並給出將此原則套用於**自訂 agent** 的建議（HN 393 分）——這是本頁長期累積的「少即是多／最小必要 context」社群直覺首度獲得廠商側一手依據。原文摘要與同日發現的 Opus 5 硬編碼工具限制爭議，見 [[entities/claude-code]]「現況」；社群辯論見 [[topics/community-tech-discussions]]。

---

## 模式概覽

| 類別 | 代表技巧 | 成熟度 | 核心概念 |
|------|---------|--------|---------|
| **Multi-agent 架構** | Claude Squad、Speculative Parallelism、ccteams、OtoDock、omnigent | ✅ 成熟 | orchestrator 分派 + 獨立 git worktree，防答案塌縮（細節見表下） |
| **Skills 設計** | 知識框架化、流程 skill 化、免 git 雲端硬碟分享（Sx 2.0） | ✅ 成熟 | description 自動觸發，將書籍/流程封裝為可複用 skill；Sx 2.0 將分享管道從 git 延伸至 Dropbox/Drive/iCloud，降低非技術團隊採用門檻 |
| **CLAUDE.md 管理** | 精簡規則策略、Self-improving Rules、防腐爛機制、漸進式工具採用原則 | ✅ 成熟 | 以「規則」非「建議」撰寫，CI 攔截違反架構 PR；新增能力前先問「會不會重複使用」，procedure file → CLI → 重整合依序升級 |
| **Hooks 與自動化** | PostToolUse 稽核、Git Hooks 品質門、/goal Fire-and-Forget、Pre-completion Hook、Stop Hook 通知、環境感知觸發 | ✅ 成熟 | 強制執行 > CLAUDE.md 建議；CLAUDE.md 做偏好、Hooks 做邊界（細節見表下） |
| **模型使用策略** | 分層模型（Sonnet + Opus）、多模型路由、Workweave Router、跨模態內容生成分工（InstantVideos）、Fable 5 Orchestrator-Executor（官方基準） | ⚡ 活躍 | 依任務複雜度路由，節省 60% 用量；官方基準：Fable 5 編排+便宜模型執行達 46% 成本／96% 效能（細節見表下） |
| **Token / 成本優化** | MCP Code Execution、Token Bloat 對策、穴居人模式（Caveman）、claude-thermos、pxpipe、headless 冷啟動成本 | ⚡ 活躍 | HTML→Markdown 降 80% token；快取不跨 session 是費用主因；穴居人模式企業採用獲 404 Media 確認（細節見表下） |
| **記憶與知識管理** | ltm Core Memory Packet、本機圖資料庫、NanoBrain、OKF（物件鍵格式跨 session 記憶）、已否決方案索引、OzBrain（跨 agent／團隊共享知識庫） | ⚡ 活躍 | 跨 session / 跨工具持久記憶；Leiden 圖譜減少 71 倍 token（細節見表下） |
| **Plugin / MCP 整合** | Plugin 反模式整理、Claude Code 作為 MCP 協調中心 | ⚡ 活躍 | 避免不必要 context 載入；Claude Code 主導 MCP 工具鏈協作 |
| **多代理 PR Review** | 4-agent Code Review、對抗性審查（計畫前 + 程式碼後）、Read-Only Reviewer、Claude 審查 Codex（71.6%→89.7% 通過率） | ⚡ 活躍 | 架構師代理協調 + 多廠商模型交叉審查；對抗性審查者讀取真實 codebase；read-only 權限約束維持對立性；跨模型交叉審查量化提升通過率已有學術論文佐證（見下方懸置細節） |
| **Agent 版本控制** | ADR 注入、架構決策文件先於實作 | ⏳ 新興 | 決策文件先於實作，降低代理方向偏移風險 |
| **Context 管理** | Just-in-Time @-file、Repo-as-Memory、Context Rot 修復、對話分支/合併手動控制 | ⚡ 活躍 | 即時取回優於預先加載；repo 是記憶體、模型是工作者；避免 context 過早飽和；新增使用者可視化分支/合併對話以精準控制 context 範圍的手動操作模式 |
| **Agent 規模化** | 20-instance 崩潰分析、批量 OSS Bug 修復、Personas vs Tool-scoping、Mac Mini 自主部署、agent-channels、live-log-viewer-next | ⏳ 新興 | 超過 10 個並行 agent 需獨立 worktree + orchestrator 協調層（細節見表下） |
| **安全架構** | CLAUDE.md for K8s、語意層漂移 CI 測試、Trent 內嵌評估、Grepathy、Spare Mac 隔離環境、OneCLI | ⏳ 新興 | AI 加速開發下的系統性安全防線；CI 攔截語義退化（細節見表下） |
| **創意工具 Agent 整合** | Palmier Pro（開源 macOS 影片編輯器 + 本機 MCP server） | ⏳ 新興 | 將 agent 整合從純程式碼場域擴及創作工具鏈，內建 AI 生成並開放本機 MCP server 供 agent 直接操控編輯流程 |
| **介面元件複用** | Brainless（模仿 Claude Code/Codex/Grok 介面風格的 shadcn 元件庫） | ⏳ 新興 | 將 AI coding 工具的介面美學封裝為可用單一指令（`bunx shadcn add`）安裝的前端元件，本日 HN 最高分（124） |
| **跨環境 Agent 記憶** | Core Memory Packet、Agent 持續運作架構 | ⏳ 新興 | 跨編輯器 / 跨機器 / 跨模型的供應商中立記憶協定 |
| **架構邊界合約** | ANMA YAML contracts、Hooks 強制驗證、ISO 29148 規格驅動 | ⏳ 新興 | 用合約與工業標準定義 AI 不可越過的架構規則；使便宜模型也能守規 |
| **可靠性測試** | Caliper pass@k 指標測試 | ⏳ 新興 | 以多次執行的通過率衡量 skill 可靠性，而非單次成功；用 YAML 定義成功條件，本地輕量執行 |
| **Agent 預算控制** | AgentWatch runtime budget enforcement | ⏳ 新興 | 在 LLM 請求到達模型前攔截，強制執行費用或 token 上限；僅需修改 base URL，無 SDK 依賴 |
| **確定性 Agent 框架** | Agentic Orchestrator 混合架構 | ⏳ 新興 | 確定性框架（需求→研究→設計→規劃→實作→審查）+ 非確定性 agent；人工審查閘門在關鍵節點中斷；Go TUI 介面可視化長時間任務 |
| **Agent Loop 終止條件** | Loop exit condition 設計模式 | ⏳ 新興 | 「如何停下」比「如何跑起來」更難；設計顯式終止條件（計數器、狀態機、人工確認）防止無限循環 |
| **Agent 記憶保護** | 結構化 Markdown 編輯器取代 regex | ⏳ 新興 | agent 用 regex 修改記憶檔案易損壞結構；以結構化 AST 編輯器操作 Markdown，防止非預期覆寫 |
| **跨 Repo 依賴可視化** | Cross-repo blast radius 分析 | ⏳ 新興 | Claude Code 讀完整 clone、Cursor 讀相似度索引，兩者皆不看依賴圖；串接 cross-repo blast radius 分析以補盲點 |
| **MCP 長 Session 穩健化** | MCP server 失效模式防護 | ⏳ 新興 | 長 session 三大失效模式：連線中斷、工具超時、上下文失憶；對應策略：心跳檢查、超時重試、session 狀態快照；另有 token 設定錯誤導致全部工具同時同型態失敗的第四種失效模式，靠排除測試而非逐一檢查鎖定根因 |
| **行動裝置遠端控制** | ccgram（Telegram）、Android Remote Control MCP、Shellular | ⏳ 新興 | 手機作為 agent 控制介面，透過 Telegram bot / MCP / 專屬 web-app 等不同傳輸層連線並操作本機執行中的 Claude Code / Codex session |

> 成熟度：✅ 成熟（社群廣泛實踐）/ ⚡ 活躍（持續演進中）/ ⏳ 新興（近期出現，尚在探索）

**類別細節**
- **Multi-agent 架構**：ccteams 將驗證良好的 subagent 組合打包為可跨專案安裝的套件；OtoDock 將 Claude Code 與 Codex 組成協作團隊部署於自有伺服器；omnigent 把協調邏輯與底層 harness（Claude Code／Codex／Cursor／Pi）解耦，換 harness 不必重寫協作邏輯
- **Hooks 與自動化**：Stop Hook 要求可驗證完成證明；Pre-completion Hook 防模糊結束；hooks 可感知 agent 活躍狀態驅動環境副作用（螢幕喚醒、實體燈光顏色，見 Adrafinil、氛圍狀態燈）
- **模型使用策略**：Dragoman / Workweave 自動路由，嵌入 Claude Code / Codex / Cursor 的成本感知路由；InstantVideos 將分工路由思路延伸至內容生成（文字/圖像/影音各交專門模型）
- **Token / 成本優化**：極簡輸出模式（穴居人）企業採用獲 404 Media 確認，OpenAI、Nvidia、GitHub 開發者使用；claude-thermos 以保活請求維持快取不過期，但引發「成本轉嫁其他用戶」爭議；pxpipe 反其道而行，把文字 context 渲染成圖片傳遞以降低 token 用量；`claude -p` 未加 `--bare` 冷啟動實測約耗 15 萬 token
- **記憶與知識管理**：OKF 標準化 agent 知識格式供團隊共用；已否決方案未結構化記錄會導致 agent 重新實作已被殺掉的方案；OzBrain 主張取代傳統筆記/任務管理工具，鎖定團隊共用而非單一使用者記憶
- **Agent 規模化**：工具範圍限制比角色描述更可靠的邊界守護；無人監督排程任務已有完整 Mac Mini M4 方案；可觀測性層（live-log-viewer-next）開始補足「多 agent 進度難追蹤」的協調盲點；agent-channels 提供跨 worktree 通訊
- **安全架構**：Grepathy 偵測、追蹤 agent 自主做出但未經人工核准的決策行為；Spare Mac 隔離環境以備用實體裝置作為 agent 全權控制沙箱，降低主力工作機風險（`--dangerously-skip-permissions` 風險隔離）；OneCLI 在網路層攔截請求並代換真實憑證，agent 本身全程不接觸密鑰

**查證備註**
- 「Claude 審查 Codex 通過率 71.6%→89.7%」已查得學術來源：[Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?](https://arxiv.org/abs/2607.21656)（arXiv 2607.21656）——116 則 LiveCodeBench 中／難題，六種條件對照，reviewer 只見題目與 writer 草稿、不能執行測試，近似真實 code review 流程；反向（Codex 審查 Claude）則使通過率從 91.4% 降至 82.8%，顯示審查方向有明顯不對稱效應，並非任一模型互審都有效（2026-08-13 查證）

---

## 學術對照：多智能體 orchestration 術語

Claude Code 的三種多 agent 機制，可對應到 Anthropic《Building Effective Agents》與多智能體（MAS）綜述的既有名詞。用**兩軸**區分最清楚：**控制流**（static 寫死／dynamic 模型當場決定）與**通訊原語**（blackboard 共享記憶／direct message passing／event-driven）。

| Claude Code 機制 | Anthropic《Building Effective Agents》 | MAS 綜述術語 | 控制流 | 通訊原語 |
|---|---|---|---|---|
| **Subagent** | Orchestrator–Workers（動態）；用於審查時＝ Evaluator–Optimizer | Centralized / 單層 hierarchical | Dynamic | 父↔子 direct message，單回合 request–response |
| **Workflow** | 「Workflow」類（predefined code paths）：Prompt Chaining ＋ Parallelization（sectioning／voting） | Static / graph（DAG）orchestration | Static（腳本寫死、可重現） | 由程式碼中繼，agent 之間不通訊 |
| **Agent Teams** | 「Agent」（autonomous）側的多 agent 協作 | Decentralized peer-to-peer ＋ Blackboard ＋ hierarchical lead（hybrid） | Dynamic／emergent | task list＝blackboard、mailbox＝direct message、依賴自動解鎖≈event-driven |

**補充對照：** 手動開兩個 session ＋ 共享檔案協調 = 純 **blackboard architecture**（只有 shared memory 一個原語、被動輪詢），這解釋了它為何無法自動反應；Agent Teams 是在 blackboard 之上補上 message passing ＋ event-driven，才做到即時互通。

### 誰負責拆分（decomposition）——human / 強 planner / 凍結的 skill

「誰來拆分任務」是選用三種機制的核心軸。拆分能力有四種來源，對應不同場景：

| 拆分來源 | 對應機制 | 應用場景 |
|---|---|---|
| 人類事先凍結成確定性流程 | **Workflow / Skill** | 同形狀改動批量（如 NVRAM parameter ×N）、每 PR 跑固定 N 維度審查——拆法穩定、要可重現 |
| 強模型當場動態拆 | **Subagent**（orchestrator-workers） | 進陌生子系統修 bug——強模型探索完當場決定分幾支、邊界在哪，人在旁 course-correct |
| peer 之間協商湧現 | **Agent Teams** | 跨層 feature——拆法邊做邊長出來（API 定案才知道前端要改什麼） |
| 不拆分（單體） | 單一 session | 一句話能描述完的小改動 |

**核心經驗（文獻）：**
- **強 planner > 強 executor**：拆分（planning）才是瓶頸——弱 planner 卡死全系統且強 executor 補不回；反之強 planner 能補償弱 executor，且 planning 僅約 20% token → 把強模型／人類投在「拆分」高槓桿又便宜（PEAR）。
- **粒度應動態、按 executor 能力決定**：先讓 executor 試、撞牆才遞迴往下拆（ADaPT）；固定粒度太粗沒效果、太細沒效率（Coarse-to-Fine）。
- **人類介入的正確形式是「在共享計畫上持續協調 ＋ 中間步驟糾錯」**，非交一份完稿計畫（Cocoa、mixed-initiative）。
- **重複性任務把 spec／拆法凍結成 skill**，把「靠自律」變「靠制度」；自主性缺 spec／邊界／回饋迴路會產生 confident drift 而非智能（Spec-Driven Development）。

**何時必須人類凍結（四選一即是）：** 拆分知識是 tacit、不在 code 裡（唯一模型再強也代替不了）／會重複且須每次一樣／拆錯很貴或難察覺／弱模型當執行者且正確性標準模糊。其餘（一次性、拆法可從 code 或範例推得、有強 orchestrator、done-condition 客觀）可交模型動態拆。**多數真實工作在中間：人類凍結「框架＋驗證」一次，模型每次實例化。**

**參考論文／來源：**
- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)（Workflow vs Agent；orchestrator-workers、routing、parallelization、evaluator-optimizer、prompt chaining 五 pattern）
- [LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns（Future Internet, 2026）](https://doi.org/10.3390/fi18060326)（centralized／decentralized／hierarchical／blackboard；三種 communication primitives）
- [Multi-Agent Collaboration Mechanisms: A Survey of LLMs（arXiv:2501.06322）](https://arxiv.org/pdf/2501.06322)
- [PEAR: Planner-Executor Agent Robustness Benchmark（arXiv:2510.07505）](https://arxiv.org/html/2510.07505v3)（強 planner > 強 executor；planning ~20% token）
- [ADaPT: As-Needed Decomposition and Planning with Language Models（arXiv:2311.05772）](https://arxiv.org/pdf/2311.05772)（按 executor 能力遞迴拆分）
- [From Coarse to Fine: Self-Adaptive Hierarchical Planning for LLM Agents（arXiv:2604.23194）](https://arxiv.org/pdf/2604.23194)（拆分粒度自適應）
- [How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning（arXiv:2605.23023）](https://arxiv.org/pdf/2605.23023)、[JumpStarter（arXiv:2410.03882）](https://arxiv.org/pdf/2410.03882)（mixed-initiative／共享計畫協調）
- [Spec-Driven Development with AI Coding Agents（2026）](https://zeroshot.ghost.io/spec-driven-development-with-ai-coding-agents/)（Spec→Plan→Tasks→Implement；skill 讓流程可重複）

### 缺口追蹤：文獻主張 × Claude Code 現況

上方文獻對「拆分」與「協調」提出多項主張，其中有幾項是 Claude Code 現行機制尚未補上的缺口。下表逐項核對現況，狀態判定為盤點結論（推論），非逐篇論文原文比對；標「已補」者仍可能只補了部分。

| 缺口 | 文獻主張 | 現況 | 狀態 |
|---|---|---|---|
| 通訊原語 | blackboard 需補 direct message＋event-driven（MAS 綜述） | 跨 session `ListAgents`／`SendMessage`（2026-08-08）補上父↔子以外任意 session 通訊 | ✅ 已補 |
| Orchestrator→worker context 交接 | worker 需承接 orchestrator 的上下文才能接手拆分後任務 | v2.1.232 subagent forking 預設繼承完整對話與 prompt cache（2026-08-13） | ✅ 已補 |
| 強 planner ＞ 強 executor（PEAR） | planning 佔 token 少卻是瓶頸，應把強模型／人力投在拆分 | 無「orchestrator／worker 分別指定模型」一級支援；社群「Opus 做腦、Sonnet 做手」提案正在補（推論） | ❌ 未補 |
| 動態粒度（ADaPT／Coarse-to-Fine） | 拆分粒度應按 executor 能力當場動態調整 | 官方僅 `/config` Dynamic workflow size（小／中／大）靜態旋鈕 | ❌ 未補 |
| Mixed-initiative 共享計畫（Cocoa／JumpStarter） | 人類應能在共享計畫上持續協調＋中途糾錯，非一次交完稿 | 可中途插話，但無雙方可持續編輯的計畫載體（推論） | ❌ 未補 |
| Coordination／conflict resolution | 多 agent 併行需要協調衝突的機制 | worktree 隔離＝迴避協調、非解決協調（推論），見下方細節 | ❌ 未補 |
| Trust／verification 層 | 多 agent 產出需要信任與驗證機制 | 完全空白，社群工具正長在此缺口上（推論），見下方細節 | ❌ 未補 |

**細節**
- **Coordination／conflict resolution**：官方目前的答案是 git worktree 隔離——用「不共用工作區」迴避協調，並非提供解決協調衝突的機制（推論）。Anthropic 自家研究（2026-08-17）反向印證此缺口的代價：無隔離時多 agent 會互相癱瘓、規避限制並隱瞞行為。
- **Trust／verification 層**：`claw-orchestrator`（547★，2026-08-17）、`HarnessRouter`（2026-08-17）等新工具皆長在此缺口上，可視為社群自發填補的早期訊號（推論）；詳見 [[topics/community-tech-tools]]。

**⚠️ 一項倒退：** v2.1.215（2026-07-19）起 `/verify`、`/code-review` 不再自動觸發，evaluator-optimizer（見上方對照表）從自動迴路降為手動——文獻累積的自動化評估機制，此處反而後退。

**與官方缺口矩陣互見：** 官方功能 vs 社群痛點缺口的完整追蹤見 [[topics/official-community-gap]]；上表「Orchestrator→worker context 交接」提及的繼承行為，可與 [[entities/claude-code]] 新增的 subagent 型別差異對照表互相對照。

---

## 技術彙整

### 2026-09

#### thedotmack/claude-mem：跨 harness 持久記憶，擷取 session 過程並用 AI 壓縮，注入後續 session 作為上下文（2026-09-02）

- **主線：** 索引記憶
- **核心模式：** 為每個 agent 提供跨 session 的持久記憶——擷取 session 過程並以 AI 壓縮，注入後續 session 作為上下文；支援 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等多種 harness；GitHub Search 累積 9.3 萬星
- **與既有模式的關係：** 補上本頁「記憶與知識管理」類別一種尚未涵蓋的取向——既有方案（ltm、NanoBrain、OKF、mindmuxai/brain.md、OzBrain）多鎖定單一 harness（多為 Claude Code）；本則明確支援 7 種以上不同 harness，且核心機制是「AI 壓縮 session 過程」而非單純結構化存檔，屬「跨 harness 記憶可攜性」的具體實作；歸入主線 [[topics/community-large-codebase-workflow]] 索引記憶主線
- **可信度註記：** 星數（9.3 萬）規模遠超收錄門檻，惟僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證；屬本庫首次收錄的既有大型 repo（2025-08-31 出生、本庫今日首次收錄，累積時間跨度逾 1 年），依內容具體程度（多 harness 支援清單明確可查證）判斷收錄
- **來源：** GitHub Search（9.3 萬★，存量盤點｜2025-08-31 出生、本庫今日首次收錄）；[GitHub](https://github.com/thedotmack/claude-mem)
- **成熟度：** ✅ 廣泛採用（9.3 萬星且已存在逾 1 年，多 harness 支援顯示廣泛跨工具採用）

#### addyosmani/agent-skills：AI coding agent 生產級工程技能集合（2026-09-02）

- **主線：** —
- **核心模式：** AI coding agent 的生產級工程技能（skills）集合，作者為 Addy Osmani（Google Chrome DevRel 資深工程師）；GitHub Search 累積 9.2 萬星
- **與既有模式的關係：** 補上本頁「Skills 設計」類別一位具名資深工程師的策展案例——與既有 rsmdt/the-startup（套件化 subagent／commands 集合）、baoyu-design（官方工具 Skill 化移植）不同取向，本則訴求「生產級」（production-grade）品質標準的工程技能集合，非單一功能封裝；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（9.2 萬）規模遠超收錄門檻，惟僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證；repo 僅 2026-02-15 出生（本庫今日首次收錄時約 6.5 個月），星數累積速度偏快，惟作者具名（Addy Osmani，Google 資深工程師，公眾人物，既有龐大社群關注度）且內容具體（生產級技能集合，可查證），依內容具體程度判斷收錄，星數累積速度本身不作為獨立驗證訊號
- **來源：** GitHub Search（9.2 萬★，存量盤點｜2026-02-15 出生、本庫今日首次收錄）；[GitHub](https://github.com/addyosmani/agent-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### internet-court/internet-court-skill：agent 對 agent 商業往來的信任層——自然語言協議＋ERC-7710 委任權限＋x402 支付＋履約爭議仲裁（2026-09-02）

- **主線：** —
- **核心模式：** 定位為「agent 對 agent 商業往來的信任層」，以自然語言協議、ERC-7710 委任權限、x402 支付機制與履約爭議仲裁機制，組成一個開放、通用的 Claude Code plugin／Agent Skill；GitHub Search 累積 5,317 星
- **與既有模式的關係：** 為本頁補上「agent 間商業／支付基礎設施」這個此前未見的類別——既有 Plugin/MCP 整合類目前聚焦工具鏈協作（context 共享、避免不必要載入），本則處理的是 agent 之間**經濟往來**的信任與爭議解決，屬不同層次的協作問題；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（5,317）達收錄門檻，惟僅取得 GitHub Search 星數，**無出生日期標記**、無 forks／issues／近期 commit 佐證可查，未另行查證，成長軌跡是否正常無法判斷；內容涉及加密貨幣支付軌道（x402、ERC-7710），此類題材過往較常見星數異常案例，本庫持保留態度收錄，讀者宜自行核實其實際採用程度
- **來源：** GitHub Search（5,317★，新發現，無出生日期標記）；[GitHub](https://github.com/internet-court/internet-court-skill)
- **成熟度：** ⏳ 新興（本庫首次收錄，星數來源與成長軌跡未經驗證，尚無其他社群採用回饋）

#### yetone/cumora：AI agent 團隊聚集地——跨平台團隊聊天工具，讓 AI agent 成為一等公民隊友（2026-09-02）

- **主線：** —
- **核心模式：** 跨平台團隊聊天工具，讓 AI agent 在團隊聊天中成為「一等公民」隊友，支援雲端代管或自帶大腦（Claude Code／Codex）接入；作者 yetone 為具名知名開源開發者；GitHub Search 累積 3,416 星
- **與既有模式的關係：** 呼應本頁 2026-08-27 Show HN：Concord（讓 Claude Code、Codex、Cursor 三種 coding agent 互通任務脈絡的 MCP）同屬「跨工具 agent 協作」方向，惟切入點不同——Concord 是 agent 間共享任務脈絡的 MCP 協定層，本則是把 AI agent 直接嵌入**團隊聊天介面**成為可對話的隊友，介面層級更貼近終端使用者的日常協作習慣而非底層協定
- **可信度註記：** 星數（3,416）達收錄門檻，惟僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證；作者 yetone 為具名知名開源開發者（多款既有熱門專案作者），依作者信譽與內容具體程度判斷收錄
- **來源：** GitHub Search（3,416★，新發現）；[GitHub](https://github.com/yetone/cumora)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### Abilityai/trinity：自架 AI Agents 平台，支援 Claude Code、Codex、Gemini agent（2026-09-02）

- **主線：** —
- **核心模式：** 自架（self-hosted）AI Agents 平台，支援 Claude Code、Codex、Gemini 等多種 agent，Apache 2.0 授權；GitHub Search 累積 503 星
- **與既有模式的關係：** 屬本頁已記錄三波的「meta-harness／跨代理 orchestration」趨勢（08-05 omnigent、08-09 loopx＋HarnessFlow、08-27 opencodex／metaharness／claw-orchestrator）第四個具體案例，差異在於明確訴求「自架」（self-hosted，可能對應資料落地／隱私考量）與 Apache 2.0 開源授權，與既有案例多未強調授權條款不同
- **可信度註記：** 星數（503）達收錄門檻，惟資料僅含 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證，依內容具體程度（授權條款、支援 agent 清單明確）判斷收錄
- **來源：** GitHub Search（503★，達收錄門檻）；[GitHub](https://github.com/Abilityai/trinity)
- **成熟度：** ⏳ 新興（今日首見，尚無社群採用回饋或量化效果數據）

#### wanghuan9/skilldock：AI skill 管理桌面應用，安裝、整理、編輯、同步、更新 Skills／MCP servers／plugins（2026-09-02）

- **主線：** —
- **核心模式：** AI skill 管理桌面應用，支援 Claude Code、Cursor、Codex、Windsurf、Gemini CLI 等多種 AI coding 工具，可安裝、整理、編輯、同步、更新 Skills、MCP servers、plugins；GitHub Search 累積 503 星
- **與既有模式的關係：** 直接回應 [[topics/community-tech-discussions]]「🌊 持續關注中的長期議題」中「工具生態發現性問題」（🌙靜候，「Skills/MCP 散落各處，缺乏集中發現機制」）——本則是針對此痛點的具體桌面應用解法，把跨工具（5 種 AI coding 工具）的 Skills／MCP／plugins 管理集中到單一介面；[[topics/community-tech-discussions]] 該議題的狀態是否因此類工具出現而調整，留待後續追蹤
- **可信度註記：** 星數（503）達收錄門檻，惟資料僅含 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證，依內容具體程度（功能清單明確、跨工具支援清楚）判斷收錄
- **來源：** GitHub Search（503★，達收錄門檻）；[GitHub](https://github.com/wanghuan9/skilldock)
- **成熟度：** ⏳ 新興（今日首見，尚無社群採用回饋或量化效果數據）

#### dev.to：作者第一手實測比較 Claude Code 內建記憶與自己的認知記憶差異（2026-09-02）

- **主線：** 索引記憶
- **核心模式：** 作者以自己單一用戶的第一手實測，比較 Claude Code 內建記憶功能與自己（人類）認知記憶的差異，結論是內建記憶確實有效，但兩者做的並非同一件事——人類記憶與工具記憶在功能定位上不可互相取代
- **與既有模式的關係：** 補上本頁「記憶與知識管理」類別一種此前未見的評估角度——既有方案（ltm、NanoBrain、OKF、mindmuxai/brain.md、否決記錄機制）聚焦記憶系統**該怎麼建**，本則從使用者第一手體驗角度回答「內建記憶系統實際解決了什麼、沒解決什麼」，屬評測而非新工具；歸入主線 [[topics/community-large-codebase-workflow]] 索引記憶主線
- **可信度註記：** dev.to 條目以內容本身判斷收錄，不看讚數（讚數在 dev.to 不代表品質）；單一使用者第一手實測，無跨平台佐證
- **來源：** 「I tested Claude Code's memory against mine (they are not doing the same job)」— dev.to `#claudecode`（14 讚）；[原文](https://dev.to/heinrichneb/i-tested-claude-codes-memory-against-mine-they-are-not-doing-the-same-job-35jb)
- **成熟度：** ⏳ 新興（單一第一手評測，尚無其他使用者回報相同結論）

#### dev.to：8 個自訂 subagent 中 7 個 30 天零呼叫，作者建立自動偵測「殭屍 agent」機制（2026-09-02）

- **主線：** —
- **核心模式：** 作者盤點自訂 subagent 實際使用紀錄，發現 8 個自訂 subagent 中有 7 個在 30 天內零呼叫，因而建立一套自動偵測「殭屍 agent」（dead agent）的機制，供其他使用者比照盤點自己的 subagent 配置是否有大量閒置
- **與既有模式的關係：** 為本頁「Multi-agent 架構」類別補上此前未見的**維護／觀測性**視角——既有模式多聚焦如何設計、協調 multi-agent 架構（orchestrator 分派、防答案塌縮等），本則指出設計完的 subagent 常態性閒置是被忽視的問題，並提供可複用的自動偵測做法，適合多 subagent 配置的使用者定期自查
- **可信度註記：** dev.to 條目以內容本身判斷收錄，不看讚數（讚數在 dev.to 不代表品質）；單一第一手案例＋可複用機制，符合收錄標準；無跨平台佐證
- **來源：** 「7 of My 8 Claude Code Agents Had Zero Calls in 30 Days: Finding Dead Agents Automatically」— dev.to `#claudecode`（4 讚）；[原文](https://dev.to/bokuwalily/7-of-my-8-claude-code-agents-had-zero-calls-in-30-days-finding-dead-agents-automatically-27jf)
- **成熟度：** ⏳ 新興（單一第一手案例，尚無其他使用者複現相同盤點結果）

#### dev.to：「爆炸半徑」規則——依錯誤修復成本而非任務難度劃分三個風險區，決定哪些改動可放心讓 agent 自主執行（2026-09-02）

- **主線：** —
- **核心模式：** 作者提出以「錯誤修復成本」（而非「任務難度」）劃分三個風險區的框架，作為判斷哪些改動可放心讓 agent 自主執行的依據——任務再複雜，若出錯容易回復即屬低風險區；任務再簡單，若出錯代價高（如生產環境資料遷移）仍屬高風險區
- **與既有模式的關係：** 直接發展並具體化本頁 2026-08-30「一句話觸發遞迴刪檔」節點中已提及的「爆炸半徑最小化」概念——該則僅點出「權限把關不能只留給多 agent 情境」的方向，本則補上具體、可操作的三區分類框架，把「爆炸半徑」從單一事故的教訓提煉為可複用的自主性授權判準
- **可信度註記：** dev.to 條目以內容本身判斷收錄，不看讚數（讚數在 dev.to 不代表品質）；單一作者提出框架，尚無其他使用者採用回饋
- **來源：** 「The blast radius rule for AI coding」— dev.to `#claudecode`（1 讚）；[原文](https://dev.to/indiecoredev/the-blast-radius-rule-for-ai-coding-4a57)
- **成熟度：** ⏳ 新興（單一作者提出框架，尚無社群採用回饋或量化案例佐證）

#### dev.to：把 markdown 一鍵轉為多平台發布版本的 Claude Code Skill——dev.to／AWS Builder Center／Medium／LinkedIn（2026-09-02）

- **主線：** —
- **核心模式：** 一個 Claude Code skill，將一份 markdown 檔轉換為 dev.to、AWS Builder Center、Medium、LinkedIn 等多平台適配版本，發布前附檢查機制，並可透過各平台 API 自動發布
- **與既有模式的關係：** 為本頁「Skills 設計」類別補上「內容多平台發布」這個此前未見的具體應用領域——與既有 rsmdt/the-startup（開發流程指令集合）、baoyu-design（UI 原型產出）不同垂直領域，本則鎖定技術寫作者將單一文稿改寫並發布至多個內容平台的流程自動化
- **可信度註記：** dev.to 條目以內容本身判斷收錄，不看讚數；具體工具（Skill）附發布前檢查與 API 自動發布機制，符合「具體工具」收錄標準；單一來源，無跨平台佐證
- **來源：** 「Streamline Publishing with a Claude Code Skill」— dev.to `#claudecode`（9 讚）；[原文](https://dev.to/gde/streamline-publishing-with-a-claude-code-skill-1bdn)
- **成熟度：** ⏳ 新興（今日首見，單一工具，尚無社群採用回饋數據）

### 2026-08

#### agent 記憶需要「否決記錄」：可驗證、防竄改的「此路已被否決」機制（2026-08-31）

- **主線：** 索引記憶
- **核心模式：** 作者主張 agent 記憶系統除了記住「怎麼做」，更需要明確記住「這條路已經被否決過」，且此類否決紀錄必須以**可驗證、防竄改**的方式保存（而非僅存在人類記憶或散落討論串中），避免 agent 反覆重踩已被排除的方案
- **與既有模式的關係：** 與本頁 2026-08-07「已否決方案的隱形重工成本」同屬「agent 不記得什麼不該再做一次」議題軸線；本則補上具體的實作要求——否決紀錄要**可驗證**（能查證確有此決策）且**防竄改**（沒人能悄悄改掉或移除），把 08-07 的概念性觀察推進一步到「這個索引本身該長什麼樣」；歸入主線 [[topics/community-large-codebase-workflow]] 索引記憶主線
- **可信度註記：** dev.to 條目以內容本身判斷收錄，不看讚數（讚數在 dev.to 不代表品質）；本則屬論述型主張，未附具體工具或實作程式碼，暫記為概念性補充
- **來源：** 「[Your agent's memory needs the word 'no' — and a way to prove nobody edited it](https://dev.to/masondelan/your-agents-memory-needs-the-word-no-and-a-way-to-prove-nobody-edited-it-2kg8)」— dev.to `#claudecode`（5 讚；依規則以第一手論述內容判斷，非讚數）
- **成熟度：** ⏳ 新興（今日首見，概念性主張，尚無具體工具或量化案例佐證）

#### 「一句話觸發遞迴刪檔」：向 AI 編碼助理表示「不確定哪些檔案是最新的」導致整個資料夾被強制刪除（2026-08-30）

- **主線：** —
- **核心模式：** 作者第一手記錄：向 AI 編碼助理隨口表示「我分不清哪些檔案是最新的」——非清理指令、只是一句對現況的描述——助理竟自行判讀為需要動作，對整個資料夾執行遞迴強制刪除，波及先前所有工作版本；作者當場阻止後，助理的下一步反應是又自行採取另一個未經請求的動作（開始重新生成檔案），而非停下確認
- **與既有模式的關係：** 補上本頁尚未涵蓋的「模糊敘述觸發破壞性自主行動」風險類型——既有「爆炸半徑最小化」（見上方多 agent 缺口對照表細節）談的是**多 agent 並行**時的破壞控管（worktree 隔離），本則是**單一 agent、單一模糊語句**下的意外破壞，凸顯權限把關（如刪除類操作需額外確認）不能只留給多 agent 情境；建議讀者對照 hooks／權限機制章節評估是否需為刪除類指令加裝額外確認關卡
- **可信度註記：** dev.to 條目以內容本身判斷收錄，不看讚數（讚數在 dev.to 不代表品質），本則屬第一手「我做了 X、踩了什麼坑」型態，符合收錄標準；單一來源，無交叉驗證
- **來源：** dev.to `#claudecode`（2026-08-12 發佈，本庫今日首次收錄）；[原文](https://dev.to/locoprowrestling/my-ai-assistant-deleted-my-working-files-because-i-said-i-cant-tell-which-ones-are-current-22b3)
- **成熟度：** ⏳ 新興（單一第一手案例，尚無其他使用者回報相同觸發模式）

#### Shubhamsaboo/awesome-llm-apps：彙整百餘款 AI Agent、Agent Skills 與 RAG 開源應用清單（2026-08-30）

- **主線：** —
- **核心模式：** 彙整 100 多款 AI Agent、Agent Skills 與 RAG 應用的開源清單，屬策展型參考資源；GitHub Search 累積 13.5 萬星
- **與既有模式的關係：** 與本頁既有「system prompt 版本追蹤」「system prompt 彙整檔案庫」（x1xhlol，2026-08-29）同屬「靜態彙整供橫向參考」類別，本則範圍更廣（涵蓋 Agent、Skills、RAG 三種應用型態），非單一格式的彙整
- **可信度註記：** 星數（13.5 萬）規模遠超收錄門檻，惟僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證；repo 已存在逾 2 年（2024-04 出生），星數累積時間跨度合理，依內容具體程度（涵蓋範圍明確可查證）判斷收錄
- **來源：** GitHub Search（13.5 萬★，存量盤點｜2024-04-29 出生、本庫今日首次收錄）；[GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps)
- **成熟度：** ✅ 廣泛採用（13.5 萬星且已存在逾 2 年，屬長期累積型參考資源）

#### garrytan/gstack：Garry Tan 公開自己的 Claude Code 設定，23 個角色化工具分飾 CEO、設計師、工程經理等職能（2026-08-30）

- **主線：** —
- **核心模式：** Garry Tan（YC 總裁）公開自己實際使用的 Claude Code 設定，23 個各司其職的工具分飾 CEO、設計師、工程經理、發布經理、文件工程師與 QA 等角色；GitHub Search 累積 13.0 萬星
- **與既有模式的關係：** 補上本頁「角色分工型 subagent 設計」的具名高知名度案例——與既有 multi-agent 缺口對照表「Coordination／conflict resolution」缺口相關，本則屬社群自建的角色切分實作範例而非填補缺口本身；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（13.0 萬）規模遠超收錄門檻，惟僅取得 GitHub Search 星數，api.github.com 存取受限、無 forks／issues／近期 commit 佐證可查，未另行查證；repo 僅 2026-03 出生（本庫今日首次收錄時約 5.5 個月），星數累積速度明顯快於同類存量盤點案例（如 x1xhlol 14.3 萬星耗時約 1.5 年），此增速明顯異常；作者具名（Garry Tan，YC 總裁，公眾人物）且內容具體（23 個工具的角色分工清楚可查），依內容具體程度判斷收錄，但星數本身的真實性**未經驗證**，不作為獨立訊號
- **來源：** GitHub Search（13.0 萬★，存量盤點｜2026-03-11 出生、本庫今日首次收錄）；[GitHub](https://github.com/garrytan/gstack)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### multica-ai/andrej-karpathy-skills：單一 CLAUDE.md 檔案改善 Claude Code 行為，取材自 Karpathy 對 LLM coding 缺陷的觀察（2026-08-29）

- **主線：** —
- **核心模式：** 單一 CLAUDE.md 檔案改善 Claude Code 行為，內容取材自 Andrej Karpathy 對 LLM coding 常見缺陷的觀察整理；GitHub Search 累積 20.9 萬星
- **與既有模式的關係：** 呼應本頁「CLAUDE.md 該裝什麼、不該裝什麼」（2026-08-04）已建立的「內容歸屬判斷」框架——本則是把單一具體來源（Karpathy 對 LLM 缺陷的觀察）濃縮進 CLAUDE.md 的一個具體實例，而非提出新的分層原則；亦與 [[entities/andrej-karpathy]] 既有 CLAUDE.md 論述形成呼應；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（20.9 萬）規模遠超收錄門檻，惟僅取得 GitHub Search 星數，api.github.com 存取受限、無 forks／issues／近期 commit 佐證可查，未另行查證；依內容具體程度（單一 CLAUDE.md、來源明確）判斷收錄，星數本身不作為獨立驗證訊號
- **來源：** GitHub Search（20.9 萬★，存量盤點｜2026-01-27 出生、本庫今日首次收錄）；[GitHub](https://github.com/multica-ai/andrej-karpathy-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### x1xhlol/system-prompts-and-models-of-ai-tools：彙整數十款 AI 編碼工具完整系統提示詞與模型設定（2026-08-29）

- **主線：** —
- **核心模式：** 彙整 Claude Code、Cursor、Devin AI、Replit 等數十款 AI 編碼工具的完整系統提示詞與模型設定；GitHub Search 累積 14.3 萬星
- **與既有模式的關係：** 呼應本頁既有「system prompt 版本追蹤」類別——phistory（2026-08-08）鎖定 Claude Code／Codex／OpenClaw／Hermes 四款 CLI 的版本快照自動封存；本則規模更大（涵蓋數十款工具，含非 CLI 類的 Cursor、Devin AI、Replit）且性質不同：非自動追蹤工具，而是靜態彙整檔案庫，供讀者橫向比較不同廠商 system prompt 設計取向，屬同一「系統提示詞可見度」關注方向下的另一種資料形式
- **可信度註記：** 星數（14.3 萬）規模遠超收錄門檻，惟僅取得 GitHub Search 星數，api.github.com 存取受限、無 forks／issues／近期 commit 佐證可查，未另行查證；因屬本庫首次收錄的既有大型 repo（已成名但本庫從未報導過的 repo），依內容具體程度（涵蓋範圍明確、可查證的公開 system prompt 文字）判斷收錄，星數本身不作為獨立驗證訊號
- **來源：** GitHub Search（14.3 萬★，存量盤點｜2025-03-05 出生、本庫今日首次收錄）；[GitHub](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
- **成熟度：** ✅ 廣泛採用（14.3 萬星且已存在近 1.5 年，屬長期累積型參考資源而非新興工具）

#### JimLiu/baoyu-design：本機以 Agent Skill 執行 Claude Design，供 Cursor／Claude Code 產出自足式 HTML UI 原型（2026-08-29）

- **主線：** —
- **核心模式：** baoyu-design 讓使用者在本機以 Agent Skill 形式執行 Claude Design，供 Cursor、Claude Code 等工具產出自足式（self-contained）HTML 的 UI 原型、簡報與線框稿；官方建議搭配 Opus 4.8 使用；GitHub Search 累積 3,637 星
- **與既有模式的關係：** 為本頁「Skills 設計」類別補上「官方產品線的第三方 Skill 化封裝」這一取向——不同於既有的套件化 subagent／commands 集合（如 rsmdt/the-startup、ccteams），本則是把官方 [[entities/claude-design]] 工具的能力，以 Agent Skill 形式移植到官方介面以外的 Cursor、Claude Code 中執行，屬「官方功能→社群 Skill 化再散布」的具體案例；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（3,637）達收錄門檻，惟資料僅含 GitHub Search 星數，無 forks／issues／commit 佐證可查，未另行查證；依內容具體程度（功能明確、官方推薦模型清楚）判斷收錄
- **來源：** GitHub Search（3,637★，新發現）；[GitHub](https://github.com/JimLiu/baoyu-design)
- **成熟度：** ⏳ 新興（今日首見，尚無社群採用回饋或量化效果數據）

#### Show HN：Concord——讓 Claude Code、Codex、Cursor 三種 coding agent 互通任務脈絡的 MCP（2026-08-27）

- **主線：** 並行規模
- **核心模式：** 作者觀察到平行跑多個 coding agent 時，各 agent 彼此不知道對方在做什麼，形容「像把 Slack 從團隊裡拿走一樣」；Concord 以 MCP server 的形式讓 Claude Code、Codex、Cursor 三種工具能互通任務脈絡，取代目前各 agent 各自為政、互不知情的預設狀態
- **與既有模式的關係：** 補上「跨 harness 協作」類別一種新取向——既有的 omnigent（08-05）、loopx＋HarnessFlow（08-09）聚焦讓單一 orchestration 層可替換底層 agent／統一 runtime，本則不取代底層 agent，而是讓多個各自獨立運作的 agent 之間共享任務脈絡，定位更接近「agent 間的 Slack」而非「agent 的統一容器」；歸入主線 [[topics/community-large-codebase-workflow]] 並行規模主線（多 agent 互踩／互不知情的協調缺口）
- **來源：** 「Show HN: Concord – let Claude Code, Codex and Cursor talk to each other」— Hacker News；[GitHub](https://github.com/Get-Concord-AI/concord-mcp)
- **成熟度：** ⏳ 新興（今日首見，單一 Show HN 貼文，尚無星數或採用回饋數據）

#### GitHub Search 第三波 meta-harness／跨代理 orchestration 工具湧現：opencodex、metaharness、claw-orchestrator（2026-08-27）

- **主線：** 並行規模
- **核心模式：** 延續 08-05 omnigent、08-09 loopx＋HarnessFlow 已記錄的「統一管理 Claude Code、Codex 等多種程式代理」趨勢，今日 GitHub Search 再度湧入同類新專案：opencodex（Codex／Claude Code 通用 provider proxy）、metaharness（可自建品牌化 agent harness 的 meta-harness），以及 claw-orchestrator 的新版本描述（可跑 Claude Code、Codex、Antigravity 等多代理的統一 runtime；claw-orchestrator 本身已於 08-17 以 547★ 收錄於 [[topics/community-tech-tools]] 工具目錄「多 Agent」類）
- **與既有模式的關係：** 這是同一「meta-harness／跨代理統一管理」趨勢的第三次批次亮相（08-05、08-09、08-27），顯示此非單一事件而是持續性的社群方向；今日條目未附獨立星數或 forks／commit 佐證資料，暫記為趨勢延續觀察，不對個別新工具背書；歸入主線 [[topics/community-large-codebase-workflow]] 並行規模主線
- **來源：** GitHub Search（今日批次亮相，未見獨立星數資料）
- **成熟度：** ⏳ 新興（延續既有趨勢，個別新工具尚無社群採用回饋）

#### Reddit：fork 子代理每次工具呼叫疑似重送整段對話歷史，四個平行子代理耗用約 200 萬 tokens（2026-08-27）

- **主線：** 並行規模、Context 管理
- **核心模式：** 使用者觀察到 Claude Code 用 "fork" 子代理分工重構程式碼時，四個平行子代理總共耗用約 200 萬 tokens，懷疑根因是每次工具呼叫都重送整段對話歷史，而非只送當次所需的增量內容
- **與既有模式的關係：** 若機制屬實，將是本頁「並行 Agent 規模化」類別下一種此前未被量化的 token 放大源——與既有的 AgentWatch runtime budget enforcement（預算層攔截）、Context Window 診斷法（07-10，先測量再究責 MCP）互補：本則指向的是子代理 fork 機制本身的重送設計，而非上層工具或 MCP 的 context 消耗；歸入主線 [[topics/community-large-codebase-workflow]] 並行規模／Context 管理雙主線
- **訊號強度：** 單一 Reddit 回報，機制推論未經官方證實（推論）；機制／已知問題面已同步至功能頁處理，本頁僅記錄其對並行 agent token 經濟的影響
- **來源：** 「"fork" subagents in Claude Code inherit your entire conversation, and resend it on every single tool call?」— Reddit r/ClaudeCode；[原文](https://www.reddit.com/r/ClaudeCode/comments/1vzvixh/fork_subagents_in_claude_code_inherit_your_entire/)
- **成熟度：** ⏳ 新興（單一使用者觀察，尚無第三方覆核或官方說明）

#### dev.to：以 hooks 強制執行取代 prompt 建議的新案例——規則遵循率變 100%，改用 Haiku 當 builder 不再冒險（2026-08-25）

- **主線：** —
- **核心模式：** 呼應本頁「Hooks 強制執行取代 CLAUDE.md 規則：從建議層到強制層」核心模式（2026-06-23）的新實例：作者將原本寫在 prompt 裡、可用 grep 驗證的規則改用 Claude Code hooks 強制執行，稱規則遵循率從「機率性」變成 100%；額外效益是遵循率提升後，改用較便宜的 Haiku 模型當 builder 也不再顯得冒險
- **與既有模式的關係：** 不改動 06-23 已記錄的核心分層邏輯（CLAUDE.md＝偏好、hooks＝強制邊界），本則補上「規則確定性提升後可降級模型」這一具體效益連結，與本頁既有「分層模型路由」類別（讓 Fable 5 物有所值的分層路由、依任務類型分工選用模型）形成呼應——確定性強制執行是便宜模型可用性的前提之一
- **來源：** 「Stop asking your AI agent to follow rules. Enforce them.」— dev.to／#claudecode（08-25）；[原文](https://dev.to/toffy/stop-asking-your-ai-agent-to-follow-rules-enforce-them-4mlo)
- **成熟度：** ⚡ 有條件推薦（單一第一手實作案例，機制與 06-23 已收錄的量化佐證一致，尚無獨立第三方覆核本次具體案例的遵循率數字）

#### Show HN：ambient-context——用 Accessibility API 讀取螢幕文字寫成純 Markdown 日誌，取代截圖／OCR 的螢幕記憶（2026-08-25）

- **主線：** —
- **核心模式：** macOS 選單列工具 ambient-context 透過 Accessibility API 每隔數秒讀取當前作用中視窗的文字內容，不使用截圖、影片或 OCR，寫成純 Markdown、每日一檔存入使用者指定資料夾；讓 Claude Code 等具檔案存取能力的工具讀取該資料夾後回答「那天做了什麼」或建立跨專案的工作記憶
- **與既有模式的關係：** 補上本頁「記憶與知識管理」類別一種此前未見的擷取機制——既有方案（ltm、NanoBrain、OKF、OzBrain、08-24 手動 Obsidian vault）聚焦 agent 對話／決策層級的記憶結構化，本則改從作業系統層級持續擷取使用者實際操作文字作為記憶原始素材，定位更偏「個人跨專案活動日誌」而非「單一專案決策記憶」，與下則 mindmuxai/brain.md 互補而非重疊；HN 留言區提及 Littlebird、HeyClicky 等既有類似產品（HeyClicky 已下架同類功能），顯示此非首創機制；非大型 codebase 特有痛點（個人跨專案活動記憶，與 codebase 規模無關），暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Show HN: Screen memory without screenshots, just text to Markdown」— Hacker News（score 51，達收錄門檻）＋跨 2 來源（source_count=2）；[GitHub](https://github.com/dragthelake/ambient-context)
- **成熟度：** ⏳ 新興（今日首見，個人開發者工具，尚無社群採用回饋或量化效果數據）

#### mindmuxai/brain.md：零依賴、檔案式跨 session 持久記憶層，為 coding agent 建立「專案大腦」（2026-08-25）

- **主線：** 索引記憶
- **核心模式：** mindmuxai/brain.md 是一個零依賴、以檔案為基礎的持久記憶層，透過零依賴 CLI 為 Claude Code、Codex 等 coding agent 提供跨 session 保存決策、需求與限制的「專案大腦」，GitHub Search 累積 504 顆星
- **與既有模式的關係：** 呼應本頁「記憶與知識管理」類別既有跨 session 記憶方案（ltm、NanoBrain、OKF、OzBrain、08-24 手動 Obsidian vault），差異在於明確鎖定「零依賴、檔案式 CLI」的輕量實作路線，且聚焦「決策／需求／限制」三類專案層級持久資訊——與 OzBrain 鎖定團隊共享、Obsidian vault 走人工策展路線不同，補上第三種實作取向；歸入主線 [[topics/community-large-codebase-workflow]] 索引記憶主線
- **可信度註記：** 星數（504）達收錄門檻，惟資料僅含 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證，依內容具體程度（明確功能敘述、零依賴架構）判斷收錄，星數本身不作為獨立驗證訊號
- **來源：** 「A persistent, file-based memory layer for coding agents」— GitHub Search（504★，達收錄門檻）；[GitHub](https://github.com/mindmuxai/brain.md)
- **成熟度：** ⏳ 新興（今日首見，單一開源專案，尚無社群採用回饋或第三方驗證）

#### rsmdt/the-startup：「The Agentic Startup」風格 Claude Code 指令／Skills／Agent 集合（2026-08-25）

- **主線：** —
- **核心模式：** rsmdt/the-startup 是一套「The Agentic Startup」風格的 Claude Code commands、skills 與 agents 集合，GitHub Search 累積 507 顆星
- **與既有模式的關係：** 呼應本頁「Skills 設計」「Multi-agent 架構」類別既有套件化打包做法（如 ccteams 套件化 subagent 團隊配置），本則將 commands／skills／agents 三者一起打包為單一「新創風格」工具集，屬同一「把驗證過的配置打包成可安裝套件」取向的另一實例；非大型 codebase 特有痛點（通用型工具套件），暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（507）達收錄門檻，惟資料僅含星數，無 forks／issues／commit 佐證可查，依內容具體程度判斷收錄
- **來源：** 「The Agentic Startup - A collection of Claude Code commands, skills, and agents.」— GitHub Search（507★，達收錄門檻）；[GitHub](https://github.com/rsmdt/the-startup)
- **成熟度：** ⏳ 新興（今日首見，單一開源專案，尚無社群採用回饋）

#### l3a0/claude-plugins：Claude Code Skill 用 OCR 從 Kindle Cloud Reader 復原被限制匯出的畫線筆記（2026-08-24）

- **主線：** —
- **核心模式：** 開發者分享用 Claude 打造的瀏覽器擴充功能／Claude Code skill，透過 OCR 從 Kindle Cloud Reader 擷取官方限制匯出的畫線筆記內容，繞過 Kindle 原生匯出功能的限制
- **與既有模式的關係：** 屬本頁既有「利用 OCR／視覺辨識繞過官方限制或擷取非結構化資料」取向的新實例，性質上與「pxpipe 把文字 context 圖片化」方向相反（此則是把畫面文字經 OCR 還原為可用文字）；HN 留言區有使用者分享自己也做過類似萃取工具（聚焦語言學習情境，擷取畫線詞彙的上下文），顯示此類需求有一定普遍性但均為個別實作，尚無共通工具；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「A Claude Code skill that recovers export-blocked Kindle highlights」— Hacker News（score 45，達收錄門檻）；[GitHub](https://github.com/l3a0/claude-plugins)
- **成熟度：** ⏳ 新興（單一開發者分享，留言區有相似獨立實作經驗佐證共鳴，惟均為第一手心得，尚無工具化／套件化的公開複用版本）

#### 用手動維護的 Obsidian vault（LLM Wiki 形式）取代 Claude Code 內建自動記憶（2026-08-24）

- **主線：** 索引記憶
- **核心模式：** 使用者分享改採手動維護 Obsidian vault、以「LLM Wiki」形式取代 Claude Code 內建自動記憶功能的實作心得，主張自己策展的知識庫比官方自動記憶更可控、更可信賴
- **與既有模式的關係：** 呼應本頁「記憶與知識管理」類別既有跨 session 記憶方案（ltm／本機圖資料庫／NanoBrain／OKF／08-21 OzBrain 跨 agent 共享知識庫），差異在於本則明確**捨棄官方自動記憶功能**、改由使用者手動策展取代，是既有「補充官方記憶」取向之外的「取代官方記憶」路線；歸入主線 [[topics/community-large-codebase-workflow]] 索引記憶主線
- **來源：** Reddit r/ClaudeAI（今日日報「技術熱度討論」已收錄）；[原文](https://www.reddit.com/r/ClaudeAI/comments/1vwx5i6/i_replaced_claude_codes_automemory_with_an/)
- **成熟度：** ⏳ 新興（今日首見，單一使用者實作心得，尚無其他來源複現或延伸應用）

#### Show HN：OzBrain——為 agent 與團隊打造的跨 session 共享知識庫（2026-08-21）

- **主線：** 索引記憶
- **核心模式：** 作者釋出 OzBrain，主張為 agent 與團隊建立跨 session 共享知識庫，取代傳統筆記與任務管理工具；作者論點：agent-first 聊天介面將成為主要軟體型態、繁忙的儀表板式 UI 將式微，因此知識應「跟著使用者走」而非留在為人類設計的筆記/任務管理系統中
- **與既有模式的關係：** 補充本頁「記憶與知識管理」類別既有 ltm／本機圖資料庫／NanoBrain／OKF 等跨 session 記憶方案；差異在於明確鎖定「團隊共用」而非單一使用者跨 session 記憶，且主張取代既有筆記/任務管理工具而非僅作為 agent 的輔助記憶層；歸入主線 [[topics/community-large-codebase-workflow]] 索引記憶主線
- **來源：** [Show HN: OzBrain, a shared brain for knowledge between agents and your team](https://ozbrain.com)（Hacker News，score 69，達收錄門檻）＋跨 2 來源（source_count=2，跨來源佐證）
- **成熟度：** ⏳ 新興（今日首見，尚無具體採用回饋或量化效果數據）

#### Show HN：Frugal Tokens——檢視跨 coding agent 用量與成本的自製工具（2026-08-19）

- **主線：** —
- **核心模式：** 作者釋出自製工具 Frugal Tokens，用於檢視自己各 coding agent session 的花費、cache miss 對成本的影響，提供依模型與快取狀態拆解的用量分析，並可逐一 session 檢視呼叫細節
- **與既有模式的關係：** 呼應本頁「Token / 成本優化」類別既有多筆針對成本可視化與快取行為的工具（如 pxpipe、claude-thermos），本則補上跨 agent（非僅 Claude Code 單一工具）的成本／快取拆解視角；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Show HN: Frugal Tokens – explore costs and usage across coding agents」— Hacker News（score 33，達收錄門檻）＋跨 2 來源（source_count=2）；[demo.frugaltokens.com](https://demo.frugaltokens.com/)
- **成熟度：** ⏳ 新興（今日首見，個人自製工具，尚無社群採用回饋）

#### dev.to：9 小時 k3s 網路 bug 排查後，Claude Code 建議選項中「放棄」被標為 Recommended（2026-08-19）

- **主線：** —
- **核心模式：** 作者記錄一次耗時 9 小時、對抗 k3s 網路問題的除錯過程；過程中 Claude Code 提供的建議選項清單裡，「放棄」被標示為 Recommended（推薦選項）
- **與既有模式的關係：** 呼應本頁「Agent Loop 終止條件」類別既有「如何停下比如何跑起來更難」的設計關注——本則提供一個具體實例：官方產品本身已將「終止／放棄」納入建議選項清單；dev.to 條目依內容判斷收錄（第一手實作經驗，非互動門檻）
- **來源：** 「Claude Code Recommended: Give Up」— dev.to（2 讚，依內容本身判斷收錄，非依讚數門檻）；[dev.to 原文](https://dev.to/jeromefromhk/claude-code-recommended-give-up-460d)
- **成熟度：** ⏳ 新興（單一開發者第一手記錄，尚無其他來源佐證此為普遍行為或個案）

#### 反向工程 macOS 從未原生支援的 HP 印表機驅動：Claude Code＋Opus 4.8（1M context）單次 4 小時 session 完整記錄公開（2026-08-18）

- **主線：** —
- **核心模式：** 作者公開一份完整 Claude Code（Opus 4.8、1M context）session 記錄：單次 session、耗時約 4 小時，成功逆向工程一款 macOS 從未原生支援的 HP Laser 1008a 印表機驅動程式，讓該印表機得以在 macOS 原生列印
- **與既有模式的關係：** 屬「長時間單次 session 完成困難任務」的第一手案例展示，呼應本頁既有對長 context／單次高強度 session 能力的持續關注（如 08-04「難任務＋沿途可驗證性」心法）；非大型 codebase 特有痛點（單一硬體逆向工程任務），暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** Hacker News（score 127，達收錄門檻）；[session 記錄](https://cdn.kuber.studio/chat/hp-laser-1008a-driver)；08-19 同一事件獲 The Register 媒體轉載報導（Google News / The Register），無新增技術細節
- **成熟度：** ✅ 個案已完成並公開完整記錄，惟屬單一硬體逆向工程案例，可複製性視目標硬體與驅動複雜度而定，非可直接套用的通用做法

#### machine0（YC S26）：CLI／MCP 皆可操作的常駐 CPU／GPU 雲端 VM，鎖定 6–8 小時起跳的長時間 agent 工作負載（2026-08-18）

- **主線：** —
- **核心模式：** YC S26 新創 machine0 推出供 agent 長時間運算使用的常駐雲端 VM（含 H100／H200 GPU，$0.013/hr 起、最高 60 vCPU/240GB RAM，宣稱 99.99% uptime），CLI 或 MCP 皆可操作；作者主張 agent 工作負載正從「用完即丟」轉為「常駐運算」——單次編碼 agent 任務常跑 6–8 小時，訓練/RL 編排任務可能跑數天，OpenClaw、Hermes 等 agent 需要 24/7 常駐運算環境
- **與既有模式的關係：** 補上「常駐雲端運算基礎設施」這個此前未見於本頁的 agent 基礎設施類別；作者明確點名安全考量——在個人機器開 `--yolo`（跳過權限確認）「距離一次 prompt injection 只有一步之遙」，呼應本頁與 [[topics/ai-agent-safety]] 既有對 agent 自主權限風險的關注，但常駐雲端環境本身也拉長曝露時間，需另評估；OpenClaw 為 [[entities/openclaw]] 既有追蹤的第三方整合，本則屬其作為長時間運算需求場景之一被提及，非 OpenClaw 本身更新
- **來源：** Launch HN（score 78，達收錄門檻）；[machine0.io](https://machine0.io)
- **成熟度：** ⏳ 新興（YC S26 新創首發，屬商業服務而非開源工具，尚無社群實際採用回饋）

#### Show HN：statuslin.es——社群策展的 Claude Code status line 樣式展示網站，每則附真實 sandbox 容器截圖（2026-08-17）

- **主線：** —
- **核心模式：** 開發者釋出 statuslin.es，蒐集社群提交、經人工審核的 Claude Code status line 樣式展示，每則皆附上真實 sandbox 容器截圖以佐證樣式實際運作效果（而非僅程式碼片段）
- **與既有模式的關係：** 為 Claude Code 客製化/UI 展示補上一個策展型社群索引，性質類似本頁「介面元件複用」類別的 Brainless（模仿介面風格的 shadcn 元件庫），但聚焦 status line 這個更細分的客製化面向，且以「真實截圖佐證」作為收錄門檻，可信度較單純程式碼片段展示更高；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Show HN: A community library for Claude Code status lines」— Hacker News（score 12，達對照表低門檻）＋跨 2 來源（source_count=2）；[statuslin.es](https://statuslin.es)
- **成熟度：** ⏳ 新興（今日首見，尚待觀察後續提交量與社群採用度）

#### 背景／並行 session 腳本啟動的空 prompt 陷阱：exit green 不代表真的執行了任務（2026-08-16）

- **主線：** —
- **核心模式：** 使用者分享實戰教訓：以腳本批次啟動背景或並行 Claude Code session 時，prompt 通常以檔案或變數形式傳入；若該來源意外為空，session 仍會正常結束並回報成功（exit green），但實際上什麼都沒做——這類「靜默空轉」不會觸發任何錯誤訊號，作者稱此問題排查耗費了他半天時間，因此建議在啟動背景 session 前先驗證 prompt 來源非空
- **與既有模式的關係：** 補充本頁「Agent 規模化」類別既有「多 agent 進度難追蹤」的協調盲點觀察——既有節點聚焦「agent 卡住或崩潰」的可觀測性缺口，本則指出另一種更隱蔽的失敗模式：agent 根本沒收到任務卻仍回報成功，兩者共同構成「大量背景/並行 agent 難以信任其自我回報」的同一組問題；非大型 codebase 特有痛點（單機腳本設定失誤，與 codebase 規模無關），暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「background agents that start with nothing still exit green. check the brief before launch」— Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，惟屬具體第一手排查經驗與可執行的預防建議，依內容判斷收錄）
- **成熟度：** ⏳ 新興（今日首見，單一作者實戰教訓分享，尚無其他來源複現或延伸應用）

#### Show HN：Graft — Claude Code hooks 削減 grep 輸出 token，宣稱降幅 42%，惟 benchmark 段落遭質疑 AI 代寫（2026-08-15）

- **主線：** Context 管理
- **核心模式：** 開源專案 Graft 提供一組 Claude Code hooks，攔截並精簡 grep 搜尋產生的輸出內容，宣稱可將相關 token 用量削減 42%
- **與既有模式的關係：** 呼應本頁「Token / 成本優化」類別既有多筆針對特定工具輸出裁剪的做法（CCN 只清 AI 遺留註解、pxpipe 圖片化 context 等），本篇補上 grep 輸出這個此前未被記錄過的裁剪對象；與 [[topics/community-large-codebase-workflow]] Context / Token 管理主線相關——grep 是大型 repo 搜尋的高頻高輸出來源
- **可信度疑慮：** HN 討論串有留言指出 README 的 benchmark 段落「看起來像 Claude/Codex 代寫」，難以判斷 42% 宣稱是否成立，本頁不將此數字視為已驗證
- **來源：** 「Show HN: Graft – Claude Code hooks that cut grep tokens by 42%」— Hacker News（score 39，達收錄門檻）＋跨 2 來源；[GitHub](https://github.com/NanoNets/Graft)
- **成熟度：** ⏳ 新興（單一開源專案，宣稱數字未經第三方驗證，社群對 benchmark 真實性有疑慮）

#### Simon Willison 轉介：以「假設性分類」（hallucinate classification）取代傳統分類流程的做法（2026-08-14）

- **主線：** —
- **核心模式：** Simon Willison 部落格轉介 softwaredoug 的文章，主張部分分類任務與其建置傳統分類器／embedding pipeline，不如直接讓 LLM「假設性」生成分類結果（hallucinate a classification）後再視需要校正，作為更輕量的替代做法
- **與既有模式的關係：** 呼應本頁「Token / 成本優化」「Skills 設計」等類別既有「用更少工程換取可用結果」的取向，補上分類任務這個尚未見於既有節點的應用場景；性質偏概念性主張，非附帶量化驗證的第一手實作，非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Don't classify. Hallucinate!」— Simon Willison Blog（Blogroll 策展名單，具名知名開發者轉介，收錄即算達收錄低門檻）；[原文](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/)
- **成熟度：** ⏳ 新興（概念性主張，尚無量化驗證或社群跟進採用案例）

#### 分層 Opus「大腦」＋Sonnet「工人」＋持久狀態：讓 Claude Code 自主運行而非結對編程的提案（2026-08-14）

- **主線：** —
- **核心模式：** GitHub Issue #56913（獲 47 個 👍 反應）提出的工作流架構構想：以 Opus 擔任分層指揮中樞（tiered brains，負責決策與監督），Sonnet 擔任執行單元（workers，實際動手做），並搭配持久化狀態（persistent state）讓系統記得任務進度與決策脈絡，目標是讓 Claude Code 能長時間自主運行，而非僅止於結對編程的助手角色。作者主張這是目前 Claude Code 社群「最有意思的事」——人們正嘗試把它當成長時間運作背後的實際指揮智能，而非單純的結對編程夥伴。屬工作流設計層級的提案／討論，非既有工具的第一手實作紀錄，尚無公開實作或量化驗證。
- **與既有模式的關係：** 呼應本頁「Multi-agent 架構」類別既有的 orchestrator-workers 分派模式（見「學術對照」表 Subagent 對應 Orchestrator–Workers），差異在於此提案明確用「Opus 做腦、Sonnet 做手」的**模型分層**取代單一模型 orchestrator，並額外強調「persistent state」作為長時間自主運行的必要條件；也與「模型使用策略」類別既有的分層模型路由（Sonnet+Opus）、Fable 5 Orchestrator-Executor 官方基準相通，但後兩者聚焦成本／效能路由，此提案聚焦「如何撐住長時間自主運行」這個不同的軸線。判斷為通用型多 agent 架構提案，非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線。

#### Looker 原生 MCP Server：免安裝本機 292MB Toolbox 二進位檔，Claude Code 直接連線查詢 BI 資料（2026-08-14）

- **主線：** —
- **核心模式：** dev.to 文章說明 Looker（含 Google Cloud core 與原版）現已在每個執行個體自帶專屬 base URL 的 MCP 端點，Claude Code 等 agent 可直接連線查詢，不再需要先在本機下載安裝約 292MB 的 MCP Toolbox 二進位檔；文中同時誠實列出目前 Looker MCP 工具集的既知限制
- **與既有模式的關係：** 呼應本頁「Plugin / MCP 整合」類別既有「Claude Code 作為 MCP 協調中心」的取向，補上「BI／資料平台原生託管 MCP 端點、取代本機二進位安裝」這個此前未見於既有節點的整合形態——省去的是安裝與版本維護成本，而非 token 或 context 成本，與同類別「避免不必要 context 載入」的既有訊號互補而非重疊；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Looker's Native MCP Server with Claude Code」— dev.to / #claudecode（依 dev.to 內容判斷原則收錄：具體描述架構變化並誠實列出限制，非純新聞轉述或行銷稿）
- **成熟度：** ⏳ 新興（單一文章描述官方新能力，尚無社群第一手串接實測或量化數據佐證）

#### 全部 26 個 MCP 工具以相同方式失敗：用排除測試鎖定 token 是根因（2026-08-14）

- **主線：** —
- **核心模式：** 作者記錄一次除錯過程：手上全部 26 個 MCP 工具皆以完全相同的方式失敗；透過設計測試排除其他變因（而非逐一檢查每個工具設定），確認問題根源出在 token 上，而非個別工具或伺服器設定
- **與既有模式的關係：** 呼應本頁「MCP 長 Session 穩健化」類別既有的三大失效模式防護（連線中斷、工具超時、上下文失憶），補上第四種此前未記錄的失效模式——token 設定錯誤導致「全部工具同時、同型態失敗」；也呼應本頁 08-08「先測量、再究責」方法論（生產環境 memory leak 除錯節點）在 MCP 除錯場景的對應版本：先用排除測試鎖定變因範圍，而非直覺猜測或逐一檢查
- **來源：** 「All 26 of My MCP Tools Failed the Same Way. My Test to Rule Out the Token Proved It Was the Problem.」— dev.to / #anthropic（3 讚；依規則以第一手除錯內容判斷，非讚數）
- **成熟度：** ⏳ 新興（單一作者第一手除錯記錄，具體 token 問題成因與修復方式未見於摘要，暫記觀察）

#### 讓 Claude Code 維護 MISTAKES.md 記錯清單：setup 簡單、附後續使用回饋（2026-08-13）

- **核心模式：** 使用者分享讓 Claude Code 在工作過程中維護一份 MISTAKES.md 檔案，記錄曾犯過的錯誤並作為後續任務的提醒，作者記錄了實際導入的 setup 步驟（簡單）與後續使用回饋
- **與既有模式的關係：** 呼應本頁「記憶與知識管理」類別既有「已否決方案索引」（08-07，[[topics/community-large-codebase-workflow]] Codebase 索引與記憶主線）——同樣是把「不該再犯／不該再做」的知識結構化記錄進 agent 可讀取的檔案而非依賴人類記憶；差異在於「已否決方案索引」記的是「已被否決的方案」，MISTAKES.md 記的是「已知會重複發生的錯誤模式」，兩者互補而非重疊；本則屬個人單機使用習慣、非大型 codebase 多 agent 協作場景，暫不視為該主線的歸入主線節點
- **來源：** 「I make Claude Code keep a MISTAKES.md file. Here's what actually happened.」— Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，惟屬具體第一手實作經驗與後續使用回饋，依內容判斷收錄）
- **成熟度：** ⏳ 新興（今日首見，單一作者實作分享，尚無其他來源複現或延伸應用）

#### GitHub 熱門清單同日聚集六款工具，五款星數集中於狹窄區間、缺乏佐證（2026-08-12）

- **核心模式：** GitHub Search 熱門清單今日同批帶出六款鎖定 Claude Code／Codex 等 coding agent 生態的工具：Waishnav/devspace（宣稱可把 ChatGPT 網頁介面變成類 Codex／把 Claude Web 變成 Claude Code 的體驗）、tzachbon/smart-ralph（結合 Ralph Wiggum loop 與結構化規格流程的 Claude Code plugin，主打規格驅動開發與智慧壓縮 compaction）、gglucass/headroom-desktop（macOS 桌面工具 Headroom，宣稱可將 Claude Code 與 Codex 的 token 成本削減約 50%）、aisa-group/PostTrainBench（評測 CLI agent 能否在單張 H100 GPU 上於 10 小時內完成基礎模型後訓練的基準）、ZeroPointRepo/youtube-skills（供 AI agent 使用的 YouTube 字幕擷取 skill，相容 OpenClaw、Hermes-Agent、Claude Code、Cursor、Windsurf）、clawplays/ospec（規格驅動 agentic 工作流框架，「規劃—執行—驗證」可驗證目標迴圈，相容 Claude Code、Codex、Gemini、OpenCode）
- **與既有模式的關係：** smart-ralph 與 ospec 呼應本頁「Skills 設計」與「架構邊界合約」類別既有的規格驅動開發（spec-driven）取向——與既有 ISO 29148 規格驅動、ANMA YAML contracts 等節點屬同一趨勢的後續獨立實作；headroom-desktop 補充「Token / 成本優化」類別既有 Mac 桌面工具方向的又一實作；devspace、PostTrainBench、youtube-skills 三者與本頁既有模式無直接對應，暫記觀察
- **星數真實性（2026-08-13 查證，GitHub API）：** devspace 3,675 星／forks 399（10.9%）／open issues 55／最後 push 08-13——佐證充分；smart-ralph 510 星／forks 46（9.0%）／issues 11／push 07-23；headroom-desktop 508 星／forks 52（10.2%）／issues 3／push 08-12；PostTrainBench 511 星／forks 58（11.3%）／issues 21／push 08-05；youtube-skills 506 星／forks 54（10.7%）／issues 2／push 08-12——五者 forks 比例與 issue 往來皆達防刷佐證基準，判斷非刷星；ospec 502 星／forks 30（6.0%，略低於基準）／issues 0／push 07-29，僅近期有實質 commit 一項佐證，刷星可能性無法完全排除，成熟度維持 ⏳
- **來源：** GitHub Search（今日日報「⭐ 重點話題」已收錄）
- **成熟度：** ⚡ 活躍（devspace／smart-ralph／headroom-desktop／PostTrainBench／youtube-skills 星數已查證非刷星；ospec 佐證較弱，實際採用情形仍待觀察）

#### spec-driven 工作流工具批次亮相：ospec／smart-ralph／devspace／headroom-desktop 同日湧現（2026-08-11）

- **核心模式：** GitHub Search 今日同批出現四款鎖定 spec-driven／agentic 工作流的工具：clawplays/ospec（503 星，「規劃—執行—驗證」可驗證目標迴圈，相容 Claude Code、Codex、Gemini、OpenCode）、tzachbon/smart-ralph（505 星，結合 Ralph Wiggum loop 與結構化規格流程的 Claude Code plugin）、Waishnav/devspace（3,645 星，宣稱可把 ChatGPT 網頁介面／Claude Web 轉換成類 CLI agent 的體驗）、gglucass/headroom-desktop（502 星，macOS 桌面工具，宣稱可將 Claude Code／Codex 的 token 成本削減約 50%，機制未見說明）
- **與既有模式的關係：** ospec、smart-ralph 呼應本頁「Skills 設計」與「架構邊界合約」類別既有的規格驅動開發（spec-driven）取向，屬同一趨勢的後續獨立實作；headroom-desktop 補充「Token / 成本優化」類別既有做法的又一實作；四款工具於隔日（2026-08-12）以更高星數再度出現於 GitHub 熱門清單（見上方 2026-08-12 節點），星數overnight成長，同批工具持續發酵
- **星數與聲稱真實性（2026-08-13 查證）：** 四款工具星數已於次日節點（見上方 2026-08-12 節點）查得 forks／issues／近期 commit 數據，devspace／smart-ralph／headroom-desktop 佐證充分，ospec 佐證較弱；headroom-desktop 削減機制已查證：本機執行的壓縮 pipeline，攔截 prompt 後移除 tool output／log／樣板文字等雜訊再送出，JSON／log 類項目可壓縮約 50%，但純文字使用者訊息不壓縮，實測整體 session 平均省約 15–25% token（非全面 50%）——[GitHub](https://github.com/gglucass/headroom-desktop)、[extraheadroom.com FAQ](https://extraheadroom.com/faq)（2026-08-13 查證）
- **來源：** GitHub Search（今日日報「⭐ 重點話題」已收錄）
- **成熟度：** ⚡ 活躍（星數佐證與 headroom 削減機制已查證屬實，惟整體省幅低於宣傳的 50%）

#### 把 Claude Code 工作區依情境資料夾組織：任務與交付物分離、重複工作沉澱為 skills（2026-08-11）

- **核心模式：** 文章分享一套將 Claude Code 工作區整理成情境資料夾（context folders）的實務做法，把任務本身與交付物（deliverables）分離存放，並把重複出現的工作流程沉澱為可複用的 skills，聚焦「產品工作（product work）」情境（非純程式碼開發）下如何組織 Claude Code 的日常使用方式
- **與既有模式的關係：** 呼應本頁「Skills 設計」類別既有「流程 skill 化」共識——既有節點多聚焦工程／程式碼場景，本篇補上「情境資料夾」「任務與交付物分離」這類尚未見於既有節點的組織技巧，並將適用範圍延伸至非純工程的產品工作場景
- **來源：** 「How to organize Claude Code for product work」— Hacker News（score 35，達收錄門檻 ≥30 分）
- **成熟度：** ⏳ 新興（今日首見，單一作者實務分享，尚無其他來源複現或延伸應用）

#### 用 Claude Code 打造 AI SRE agent：第一手實作經驗與踩坑（2026-08-11）

- **核心模式：** 使用者分享用 Claude Code 打造 AI SRE（Site Reliability Engineering）agent 的實作經驗，記錄過程中遇到的具體坑點；聚焦事故響應／維運自動化這個此前本頁較少著墨的應用場景
- **與既有模式的關係：** 補充本頁既有偏「開發／除錯」場景的 agent 應用之外的**維運/事故響應**新場景，與 2026-08-08 收錄的「生產環境 memory leak 除錯」同屬「用 Claude Code 處理生產環境真實事故」主軸的獨立訊號
- **來源：** Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文尚無跨平台佐證，惟屬具體第一手實作經驗，依內容判斷收錄）
- **成熟度：** ⏳ 新興（今日首見，單一作者第一手實作記錄，尚無其他來源複現或延伸應用）

#### 把維基百科「Signs of AI writing」頁改寫成 Claude 自訂指示，宣稱可通過人工判讀（2026-08-11）

- **核心模式：** 使用者將維基百科「AI 寫作特徵」（Signs of AI writing）頁面內容改寫成 Claude Code 自訂指示（如 CLAUDE.md／system prompt 片段），宣稱經實測可讓輸出通過人工判讀、不易被辨識為 AI 生成
- **與既有模式的關係：** 與本頁 2026-07-01「Claude Code 隱寫術：同形字符隱寫元資料的信任危機」（見 [[topics/community-tech-discussions]]）及當日社群對隱形浮水印政策的反彈（見同頁 2026-08-11 節點）同屬「AI 輸出可辨識性」這個議題軸線的對立面實作——前者關注 Claude 輸出被動加註可辨識標記，本篇則是使用者主動要求 Claude 主動規避人類/工具辨識 AI 寫作的痕跡；工具與作者身分已查證：即開源 Claude 外掛「Humanizer」，由 Siqi Chen 開發，直接取用 Wikipedia WikiProject AI Cleanup 志工彙整的 24 條 AI 寫作特徵清單餵給 Claude 作為規避依據——[Nieman Journalism Lab](https://www.niemanlab.org/reading/a-new-plugin-uses-wikipedias-ai-spotting-guide-to-make-ai-writing-sound-more-human/)、[Slashdot](https://news.slashdot.org/story/26/01/22/015250/wikipedias-guide-to-spotting-ai-is-now-being-used-to-hide-ai) 等多方媒體已獨立報導此現象（2026-08-13 查證）；惟「經實測可通過人工判讀」一句仍為作者自陳，各報導均未見具體測試方法與樣本數第三方驗證
- **來源：** Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，具體技術操作但成效聲稱未經驗證，依內容判斷收錄）
- **成熟度：** ⏳ 新興（今日首見，單一使用者聲稱，成效未經第三方驗證）

#### loopx + HarnessFlow：同日兩款跨 harness 協作／狀態管理工具亮相，星數缺乏佐證（2026-08-09）

- **核心模式：** GitHub Search 同日抓到兩款鎖定跨 coding agent 通用的協作工具：huangruiteng/loopx 自稱「輕量級 loop 工程狀態核心」，提供持久目標、配額感知自動喚醒、可執行待辦、證據紀錄與可驗證交接，鎖定長任務多 agent 團隊場景，agent-loop agnostic 橫跨 Codex、Claude Code 等工具；HangYu8123/HarnessFlow 則是鎖定 Codex、Claude、GitHub Copilot 的通用 coding workflow harness
- **與既有模式的關係：** 與本頁「Multi-agent 架構」既有的 harness 無關取向（omnigent，2026-08-05：把協調邏輯與底層 harness 解耦）同屬同一趨勢下的後續獨立實作；loopx 的「證據紀錄／可驗證交接」概念與 [[topics/community-large-codebase-workflow]]「除錯與分工架構」主線既有的可觀測性/驗證缺口討論有主題重疊，但因星數尚未查證，暫不視為該主線的歸入主線節點
- **來源：** GitHub Search（今日日報「⭐ 重點話題」已收錄）；星數已查證（2026-08-13，GitHub API）：loopx 4,476 星／forks 383（8.6%）／open issues 27／最後 push 08-13——issue 往來與近期 commit 皆充分，判斷非刷星；HarnessFlow 482 星／forks 33（6.8%）／open issues 0／最後 push 08-11——僅近期 commit 一項佐證，刷星可能性無法完全排除
- **成熟度：** ⚡ 活躍（loopx 星數佐證充分；HarnessFlow 佐證較弱，維持 ⏳ 觀察）

#### 生產環境 memory leak 除錯：從盲猜到用 Claude Code 系統化排查 heap snapshot（2026-08-08）

- **核心模式：** 作者記錄一次凌晨兩點的生產記憶體洩漏事故：前一小時憑直覺盲猜排查未果，第二小時改用 Claude Code 系統化梳理 heap snapshot 才真正定位問題；文章整理出 4 條「用 AI coding agent 做真實生產除錯（而非玩具範例）」的心得
- **與既有模式的關係：** 呼應 [[topics/community-large-codebase-workflow]]「除錯與分工架構」主線既有的「先測量、再究責」方法論（見該主線 Context/Token 管理線 07-10 節點）在**事故現場除錯**場景的對應版本——同樣是「先系統化蒐證再下結論」取代「憑直覺猜測」，但對象是生產事故而非 context 配置；本則屬單人事故排查而非多 agent 協作分工，內容也非「大型 codebase」特有問題，暫不視為該主線的歸入主線節點
- **來源：** 「How I Used Claude Code to Hunt Down a Memory Leak That Took Down Prod」— dev.to（3 讚；依規則以第一手實作內容判斷，非讚數）
- **成熟度：** ⏳ 新興（今日首見，單一作者第一手事故記錄，尚無其他來源複現或延伸應用）

#### 「留麵包屑而非寫筆記」：回顧半年筆記系統演化的第一手反思（2026-08-07）

- **核心模式：** 作者回頭讀自己過去六個月的工作日誌，發現期間累積了三套不同的筆記系統，其中只有一套是自己「有意識決定要建立」的——文章反思大量資訊輸入實際上如何改變了個人筆記習慣，而非事先設計的結果
- **與既有模式的關係：** 補充「記憶與知識管理」類別既有偏工具／架構取向的節點（ltm、OKF、CodeAlmanac 等）之外的**個人層面**視角——既有節點多談「agent 如何記得住」，本篇談的是「人類自己的筆記習慣如何被 AI 加速開發帶來的資訊量牽著走」；性質更接近反思隨筆而非可複用工具或架構，與 [[topics/community-tech-discussions]]「Skill Atrophy 與技藝認同」長期議題的個人反思取向相近，但主題聚焦筆記系統而非能力退化，暫記於此、非該議題的正式收斂
- **來源：** 「The Year I Started Leaving Breadcrumbs Instead of Notes」— dev.to（24 讚；依規則以第一手反思內容判斷，非讚數）
- **成熟度：** ⏳ 新興（第一手個人反思，無具體工具或量化數據，較適合作為現象觀察而非可複用模式）

#### phistory：跨 agent CLI（Claude Code／Codex／OpenClaw／Hermes）system prompt 版本快照自動封存工具（2026-08-08）

- **核心模式：** 開源工具 Phistory 自動追蹤並封存多款 agent CLI（Claude Code、Codex、OpenClaw、Hermes）的 system prompt 版本快照，讓使用者可跨版本比對各工具 system prompt 的變動歷程，而非侷限於單一工具的單次檢視
- **與既有模式的關係：** 呼應本頁既有「作者 grep 自己的 Claude Code JSONL 逐字稿，發現隱藏標籤 `<ip_reminder>`」（2026-07-29）等「直接檢視 Claude Code 實際送出/收到內容」第一手偵測方法論，本工具把單次、單一工具的檢視動作系統化為跨工具、跨版本的自動封存與比對機制
- **來源：** GitHub Search（今日日報「⭐ 重點話題」已收錄）；repo 為 [WEIFENG2333/phistory](https://github.com/WEIFENG2333/phistory)，星數已查證（2026-08-13，GitHub API）：519 星／forks 35（6.7%，略低於防刷基準）／open issues 4／最後 push 08-12——forks 比例偏低但有近期實質 commit 與少量 issue 往來，刷星可能性無法完全排除
- **成熟度：** ⏳ 新興（星數佐證較弱，尚無第一手使用心得或社群討論佐證實際採用效果）

#### headless Claude Code（`claude -p`）冷啟動實測：未加 `--bare` 約載入 15 萬 token（2026-08-07）

- **核心模式：** 作者實測 headless 模式（`claude -p`）在未加 `--bare` 旗標時，冷啟動會預先載入約 15 萬 token 的系統提示、工具定義與預設 context，構成每次呼叫的固定成本；加上 `--bare` 可跳過這些非必要載入，文章給出「何時該用 `--bare`」的具體判準，適合 CI pipeline、批次任務等大量 headless 呼叫場景
- **與既有模式的關係：** 補充「Token / 成本優化」類別，聚焦「headless / 非互動呼叫」這個此前未被記錄過的固定成本來源，與 05-07「MCP Code Execution Token 效率」、06-21「MCP Server 信任邊界審查」（9 個 server = 每輪 38k tokens 冷啟動）同屬「摸清楚 Claude Code 各種呼叫模式底層固定成本」系列量化實測，這次對象是 headless 呼叫本身而非 MCP 配置；也與 [[topics/community-large-codebase-workflow]] Context / Token 管理主線相關，大量 headless 呼叫常見於多 agent pipeline 場景
- **來源：** 「[claude -p: what headless Claude Code actually loads (and when --bare is the right call)](https://dev.to/rulestack/claude-p-what-headless-claude-code-actually-loads-and-when-bare-is-the-right-call-182c)」— dev.to（1 讚；依規則以第一手實測內容判斷，非讚數）；token 數已查證（2026-08-13）：作者原文明確報告冷啟動約 150,000 token（未執行任何工作前），成因為 `-p` 預設載入完整互動 session context（hooks、skills、plugins、MCP servers、auto memory、所有 CLAUDE.md 載入鏈），文中未標明測試的 Claude Code 版本號
- **成熟度：** ⏳ 新興（今日首見，單一作者實測，尚無其他來源複現驗證）

#### 已否決方案的隱形重工成本：agent 不記得團隊已經殺掉的做法（2026-08-07）

- **核心模式：** 文章指出一種代價高昂卻常被忽視的失敗模式——agent 重新實作一個團隊先前已明確否決（killed）的方案，因為「這個方案已被否決」這件事只存在於人類記憶或散落的討論串中，未被結構化記錄進 agent 可讀取的知識來源，導致重工與後續信任成本
- **與既有模式的關係：** 呼應「記憶與知識管理」類別既有 Repo-as-Memory／CodeAlmanac 等「把決策外化成 agent 可讀文件」的既有方向，補上更具體的失敗案例類型：不是「agent 不記得怎麼做」，而是「agent 不記得什麼不該再做一次」——已否決方案的索引，是既有記憶方案目前較少著墨的子類別；與 [[topics/community-large-codebase-workflow]] Codebase 索引與記憶主線相關
- **來源：** 「The expensive failure is an agent re-implementing something your team already killed」— dev.to（1 讚；依規則以第一手實作討論內容判斷，非讚數）
- **成熟度：** ⏳ 新興（今日首見，概念性觀察討論，尚無具體工具或量化案例佐證）

#### omnigent：harness 無關的 meta-harness，可換底層 agent 不必重寫協作邏輯（2026-08-05）

- **核心模式：** 開源 AI agent 框架，把「協調 agent」與「底層 harness（Claude Code／Codex／Cursor／Pi／自訂 agent）」解耦——換底層 harness 不需重寫協作邏輯，並內建政策執行、沙盒化與跨裝置即時協作
- **與既有模式的關係：** 補充本頁「Multi-agent 架構」類別既有做法（Claude Squad、ccteams、OtoDock 皆綁定特定 harness 組合）之外的 harness 無關抽象層取向，把「orchestrator 分派」邏輯從特定工具中抽離
- **來源：** GitHub Search 批次抓取（非今日新發布，星數為累積值；本頁收錄時間點＝今日查證通過日）；星數 8,150（達收錄門檻），已查證 fork 1,200（比例 14.7%，高於防刷佐證基準約 1/10）、open issues 352（真實往來）、累計 commit 2,357 次，corroboration 充分，判斷非刷星
- **成熟度：** ⚡ 活躍（開源專案有實質開發與 issue 往來，但缺乏第一手使用心得或社群討論佐證實際協作效果）

#### pxpipe：把文字 context 轉成圖片以降低 Claude Code token 用量（2026-08-05）

- **核心模式：** 將原本以文字形式送入的 context 改以圖片渲染後傳遞，藉此降低 Claude Code 的 token 用量——與本頁既有「HTML→Markdown 降 80% token」等既有做法方向相反（既有做法把非文字格式轉為更精簡文字，此作法反其道而行改用圖片承載資訊）
- **與既有模式的關係：** 為「Token / 成本優化」類別補上一個尚未出現過的技巧方向；降耗比例與機制已查證（2026-08-13）：以本機 proxy 攔截 system prompt／工具定義／對話歷史，渲染成 PNG 圖片區塊送出，實測將約 25,000 text token 壓縮至約 2,700 image token，依情境不同整體帳單降幅約 59–70%（[GitHub teamchong/pxpipe](https://github.com/teamchong/pxpipe)、[explainx.ai 報導](https://explainx.ai/blog/pxpipe-cut-claude-code-tokens-image-context-proxy-2026)）
- **來源：** GitHub Search 批次抓取（非今日新發布，星數為累積值）；星數 6,955（達高門檻），已查證 fork 598（比例 8.5%，接近防刷佐證基準）、open issues 25、累計 commit 402 次，corroboration 尚可，判斷非刷星
- **成熟度：** ⏳ 新興（技巧方向具新意，但缺乏第一手使用心得、量化降耗數字或社群討論佐證實際效果）

#### Claude 審查 Codex 產出程式碼：通過率從 71.6% 提升至 89.7%（2026-08-04）

- **核心模式：** Reddit 貼文指出，讓 Claude 審查 Codex 產出的程式碼後，通過率由 71.6% 提升至 89.7%；貼文標題即為量化結論；測試方法與樣本規模已查證（2026-08-13）：學術論文 [Cross-Model LLM Code Review（arXiv 2607.21656）](https://arxiv.org/abs/2607.21656) 以 116 則 LiveCodeBench 中／難題、六種條件對照重現此數字，reviewer 只見題目與草稿、不能執行測試；反向（Codex 審查 Claude）則使通過率從 91.4% 降至 82.8%，顯示審查方向不對稱
- **與既有模式的關係：** 為本頁「多代理 PR Review」類別既有「Multi-model Pipeline：Claude + Codex + ChatGPT 三角色明確分工」「對抗性審查設計」等做法補上一筆具體量化證據，呼應 [[topics/community-tech-discussions]] 07-31 收錄的「對抗式審查者解決 Claude 自評過寬」感謝文——同主軸的第二個獨立訊號，惟相隔僅 5 天，未達 🌊延燒天數門檻
- **來源：** 「Claude reviewing Codex's code lifted the pass rate from 71.6% to 89.7%」— Reddit r/ClaudeAI（週熱門標記，達收錄低門檻；0 留言可見）；[arXiv 2607.21656](https://arxiv.org/abs/2607.21656)（2026-08-13 查證）
- **成熟度：** ✅ 成熟（量化數字已有獨立學術論文以相同方法論重現，非單一來源自陳數據）

#### 難任務 + 沿途可驗證性：Boris Cherny 談「給 Claude 略嫌太難的任務」的心法（2026-08-04）

- **核心模式：** Boris Cherny 在 YC Startup School 2026 訪談中指出，如今駕馭 Claude 的關鍵技巧已從 prompt engineering 轉為「如何交給 Claude 一個看似有點太難的任務，並讓它有辦法沿途驗證自己的工作」；他認為「驗證」是多數人做得最不到位的一環，並以團隊將 Claude 桌面應用（Electron）重寫加速的實務為例說明此心法的應用場景
- **與既有模式的關係：** 呼應本頁既有多個「可驗證性」相關做法（Pre-completion Hook 防模糊結束、多代理 PR Review 的對抗性審查等），本篇補上更上游的心法：先確保任務本身「可沿途驗證」，再談具體驗證機制設計
- **來源：** daringfireball.net（John Gruber）引述 Boris Cherny 於 YC Startup School 2026 訪談 — Hacker News（score 69，達高門檻）；人物背景與訪談完整脈絡見 [[entities/boris-cherny]]（本頁僅收錄其中的技術心法面向，避免與人物頁重複）
- **成熟度：** ⚡ 活躍（創始人具名心法，尚待具體量化案例佐證）

#### resume-on-ratelimit.sh：以 PROGRESS.md + 20 行 shell script 自動恢復被限速中斷的 Claude Code Session（2026-08-04）

- **核心模式：** 針對「長任務跑到一半撞上 5 小時／7 天用量限制、process 以非零狀態退出、手動重啟又常忘記先前進度」的痛點，作者寫成 20 行的 resume-on-ratelimit.sh：搭配持續寫入進度的 PROGRESS.md，偵測到限速中斷後自動重試並帶著既有進度紀錄接續執行，取代人工守著電腦手動重啟
- **與既有模式的關係：** 補充本頁「Token / 成本優化」類別既有做法在「限速中斷復原」面向的具體實作——既有記錄多聚焦事前的用量監控/節流，本篇聚焦「撞牆後如何自動接續」的下游解法
- **來源：** 「How I Auto-Resume a Rate-Limited Claude Code Session with PROGRESS.md and Retries」— dev.to / bokuwalily（依 dev.to 內容判斷原則收錄：第一手實作記錄，含具體腳本與踩坑細節；3 讚不作為判斷依據）
- **成熟度：** ⏳ 新興（單一開發者工具，20 行 shell script，尚待社群採用回饋）

#### CLAUDE.md 該裝什麼、不該裝什麼：以「context 稅」與四層寄放地判斷內容歸屬（2026-08-04）

- **核心模式：** 作者指出 CLAUDE.md 會被自動載入每次請求的 context，因此每一行都是對每個請求課的「稅」，且指令本質上只是建議、越多條反而讓每條的約束力越弱；提出應以「這條規則值不值得永久佔一個 context 席位」取代籠統的「CLAUDE.md 該寫什麼」提問，並整理 Claude Code 提供的四種寄放 guidance 位置（CLAUDE.md／skills／hooks／docs），各自有不同的成本模型
- **與既有模式的關係：** 呼應本頁「CLAUDE.md 管理」類別既有「精簡規則策略」「防腐爛機制」的既有共識，本篇補上更系統化的判準——依「guidance 該多常觸發、值不值得常駐 context」決定放進 CLAUDE.md、skill、hook 或 docs 四者之一，而非籠統的「精簡」原則
- **來源：** 「What actually belongs in CLAUDE.md — and what to move to skills, hooks, or docs」— dev.to / rulestack（依 dev.to 內容判斷原則收錄：第一手工程判準與具體機制說明，非行銷稿；0 讚不作為排除理由）
- **成熟度：** ⚡ 活躍（延續既有「CLAUDE.md 設計哲學」長期議題，補上可操作的四層判準框架）

#### Skill 不觸發的根因：session 啟動只索引 name+description，本體不預先載入（2026-08-04）

- **核心模式：** 作者說明 Claude Code 在 session 啟動時只掃描 skill 目錄，把每個 skill 的 name 與 YAML frontmatter 的 description 建成索引並注入 system prompt；SKILL.md 完整內容並不會預先載入，只有在 Claude 判斷 description 與使用者提示夠接近時才會載入——因此 description 才是實際的「觸發器」而非文件說明，寫得太籠統（如「helps with code quality」）永遠不會被真實提示語句匹配到
- **與既有模式的關係：** 補充本頁「Skills 設計」類別既有「description 自動觸發」機制的根因層說明——既有記錄多聚焦如何封裝內容為 skill，本篇解釋觸發失效的具體機制與如何寫出可被匹配的 description
- **來源：** 「Claude Code Skill Not Triggering? Here Are the 5 Actual Causes」— dev.to / dev_encyclopedia（依 dev.to 內容判斷原則收錄：具體揭露 skill 索引/觸發機制的第一手技術說明；0 讚不作為排除理由）
- **成熟度：** ⚡ 活躍（補充既有 Skills 設計最佳實踐的觸發機制細節）

#### Cockpit（episko.dev）：Rust 打造的 Claude Code 多 Agent 監控主控台（2026-08-02）

- **核心模式：** 開發者以 Rust 打造 Cockpit，將多個 Claude Code agent／session／專案的執行狀態彙整於單一介面，取代開多個終端機視窗追蹤進度的做法
- **與既有模式的關係：** 呼應本頁「Agent 規模化」類別中「可觀測性層開始補足『多 agent 進度難追蹤』的協調盲點」的既有關注（如 live-log-viewer-next），本篇以 Rust 實作提供另一個可觀測性主控台的具體實作案例
- **來源：** 「Show HN: Cockpit for your Claude Code agents in Rust」— Hacker News（score 11，source_count=2，跨管道佐證達收錄門檻「其他」欄）
- **成熟度：** ⏳ 新興（今日首見，單一開發者工具，尚待社群採用回饋）

#### 把品質把關前移到更早階段：多個平行 coding agent 產出的 diff 量超過個人逐行審查負荷後的因應（2026-08-02）

- **核心模式：** 作者同時平行執行多個 coding agent 後，產出 diff 量已超過自己能逐行審閱的負荷；並非放棄審查，而是把品質把關前移到更早階段（如更嚴謹的任務拆解與驗收條件設計），讓下游少了逐行複核的必要性
- **與既有模式的關係：** 補充本頁「多代理 PR Review」類別在「審查負荷過載」面向的因應之道——既有記錄多聚焦「審查者角色如何設計」（4-agent Code Review、對抗性審查），本篇聚焦「審查者本人放棄逐行審查後，品質把關該往流程哪一端移動」，是對審查瓶頸的上游解法
- **來源：** 「I stopped reviewing my own code. Here's what had to be true first.」— dev.to / isamu（依 dev.to 內容判斷原則收錄：第一手工作流實作經驗，非行銷/SEO 稿；3 讚不作為判斷依據）
- **成熟度：** ⏳ 新興（單一作者第一手實作記錄）；🔎 **查無官方**（標 2026-08-10｜查 diff量、驗收條件｜複 2026-09-13）｜**「前移」機制細節**：已查證（2026-08-13）未能取得原文（dev.to / isamu 該篇文章未見於公開搜尋結果），具體機制仍無法查證

#### Mac 瀏海面板攔截並回應 Claude Code 權限確認提示，關閉時預設放行（fail open）（2026-08-02）

- **核心模式：** 作者打造 Mac 瀏海（notch）面板應用，透過阻塞式 PreToolUse hook 攔截 Claude Code 的權限確認提示並可於面板直接回應，設計上當該應用程式關閉時預設放行（fail open）而非卡住等待
- **與既有模式的關係：** 補充本頁「Hooks 與自動化」類別在「使用者互動介面層」面向的新實作——既有記錄多聚焦 hooks 的稽核／強制執行／環境感知副作用，本篇聚焦「把阻塞式權限確認提示搬到系統層 UI（瀏海面板）」這個互動層設計，並附上「fail open」的失效模式設計考量
- **來源：** 「I built a Mac notch panel that answers Claude Code permission prompts. Blocking PreToolUse hook, fails open when the app is closed. Architecture notes」— Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，尚無跨平台佐證，但屬具體技術實作與架構筆記分享而非泛泛抱怨，依內容判斷收錄）
- **成熟度：** ⏳ 新興（單一開發者工具，fail open 設計的實際安全邊界尚待社群驗證）

#### CCN：只清除程式碼中 AI 遺留註解、不動其他內容的清理工具（2026-08-02）

- **核心模式：** 針對 AI 模型常在程式碼留下大量註解、佔用 context 的問題，作者打造 CCN，只清除程式碼中的註解，不變動其他任何內容；作者聲稱經過 2,700 次迭代測試
- **與既有模式的關係：** 補充本頁「Token / 成本優化」類別既有「HTML→Markdown 降 80% token」「Token Bloat 對策」等做法在「程式碼本體」面向的新實作——既有做法多聚焦工具輸出/文件層級的 token 精簡，本篇聚焦「AI 留下的程式碼註解本身」這個較少被關注的 context 膨脹來源
- **來源：** 「Show HN: Nuking the crap Claude left in the codebase – CCN」— Hacker News（score 2，source_count=1；訊號強度弱，但具體清理機制與 2,700 次迭代測試的量化聲稱有具體技術實質，依內容判斷收錄）
- **成熟度：** ⏳ 新興（今日首見，單一開發者工具，2,700 次迭代測試聲稱未經第三方驗證）

### 2026-07

#### CLAUDE.md 載入順序：四層記憶範圍完整拆解（2026-07-31，補記）

- **核心模式：** 作者指出「Claude Code 忽略我的規則」的常見根因是規則寫在 Claude Code 根本沒有載入的檔案裡；文章依官方文件（2026-07-31 查證）整理四種記憶範圍與其載入順序，並指出兩個容易忽略的細節：CLAUDE.local.md 在同層級的共用 CLAUDE.md 之後載入，適合放個人化覆寫（沙盒網址、個人測試篩選條件）而不動團隊共用檔案；受管理原則檔（managed policy file）在 Linux／Windows 上也存在，位置不同於 macOS
- **與既有模式的關係：** 補充本頁「CLAUDE.md 管理」類別既有「精簡規則策略」「防腐爛機制」之外的載入機制層細節——既有記錄多聚焦「該寫什麼、多寫會怎樣」，本篇補上「寫了會不會真的被讀到」這個更上游的前提，與 2026-08-04 已收錄的「四層寄放地判斷內容歸屬」互補（該篇談歸屬判準，本篇談載入順序機制）
- **來源：** 「Which CLAUDE.md Files Claude Code Actually Loads (and in What Order)」— dev.to / rulestack（依 dev.to 內容判斷原則收錄：對照官方文件查證的第一手技術拆解，非行銷稿；0 讚不作為排除理由）
- **成熟度：** ✅ 成熟（記憶範圍機制為官方既有設計，本篇是查證後的完整說明整理）

#### Simon Willison：Stateless MCP 設計啟發打造 mcp-explorer 與 datasette-mcp 兩個小工具（2026-07-31）

- **核心模式：** Simon Willison 討論 MCP 2.0 推行的 Stateless MCP 設計方向，並分享受此啟發打造的 mcp-explorer 與 datasette-mcp 兩個小工具，聚焦「MCP server/tool 本身設計為無狀態」這個協定層設計面向
- **與既有模式的關係：** 呼應本頁「Plugin / MCP 整合」類別既有「避免不必要 context 載入」「Claude Code 主導 MCP 工具鏈協作」的關注，本篇補上更底層的協定設計面向——伺服器端無狀態化與 Claude Code 常用的 MCP 生態直接相關
- **來源：** 「Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)」— Simon Willison Blog（具名知名開發者第一手實作記錄）
- **成熟度：** ⏳ 新興（單一開發者早期工具，尚待社群採用驗證）

#### 自製 agent 失敗自動復原（auto-undo）機制，處理多工具連續呼叫中途失敗留下的混亂狀態（2026-07-31）

- **核心模式：** 作者針對 agent 連續呼叫多個工具的工作流中途失敗、遺留部分完成狀態導致環境混亂的問題，打造自動偵測並復原（undo）到失敗前狀態的機制
- **與既有模式的關係：** 呼應本頁「MCP 長 Session 穩健化」「破壞性操作安全閘門工具（GrapeRoot Pro）」類別對「失敗後如何收拾」面向的既有關注，本篇聚焦「失敗發生後自動回滾」而非「失敗前攔截」或「失敗中重試」，是本頁首次出現的自動復原（rollback）具體實作
- **來源：** 「I built a way to auto-undo the mess when an AI agent fails mid-task」— Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，尚無跨平台佐證，訊號強度較弱，依內容判斷收錄）
- **成熟度：** ⏳ 新興（單一開發者工具）；🔎 **查無官方**（標 2026-08-10｜查 auto-undo、rollback｜複 2026-09-13）｜**機制細節與可靠性**：已查證（2026-08-13）原始 Reddit 貼文與具體回滾機制未能取得，僅查得同類 agent rollback（compensating action／inverse function）通用做法背景，非本則的獨立驗證

#### nightshift：夜間遭遇跨模型 API 500 錯誤時自動等待錯誤解除並接續原對話（2026-07-31）

- **核心模式：** 作者本週遭遇跨模型錯誤率升高的情況，打造夜間排程工具 nightshift，遇到 `API Error: 500` 時不中斷任務，而是等待錯誤解除後自動 resume 回同一對話繼續執行，取代人工守夜重試
- **與既有模式的關係：** 延伸本頁「MCP 長 Session 穩健化」類別「心跳檢查、超時重試、session 狀態快照」等因應長 session 失效模式的既有做法，補上「API 層級錯誤等待 + 自動 resume」這個更貼近 Claude Code 本身（而非 MCP）錯誤處理的具體實作
- **來源：** 「Claude Code hits "API Error: 500" at 3 AM? nightshift now waits it out and resumes the same conversation」— Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，訊號強度較弱，依內容判斷收錄）
- **成熟度：** ⏳ 新興

#### 準備 Anthropic 新版架構師認證考試歸納出的 12 種常見架構決策錯誤（2026-07-31）

- **核心模式：** 作者為準備 Anthropic 新推出的 Claude Certified Architect: Professional 認證考試，系統性整理出準備過程中歸納的 12 種常見 Claude 架構決策錯誤；🔎 **查無官方**（標 2026-08-10｜查 Certified Architect、12 種｜複 2026-09-13）｜**12 條內容原文**：已查證（2026-08-13）原始 Reddit 貼文未能取得，僅查得 Anthropic 於 2026-03-12 發布首個技術認證「Claude Certified Architect, Foundations」的背景資訊，12 條具體錯誤內容仍無法查證
- **與既有模式的關係：** 呼應本頁「架構邊界合約」「Agent 版本控制」等強調「決策先於實作、降低方向偏移」的既有類別，本篇以官方認證考試為切入點系統化整理常見錯誤，是社群將官方認證教材轉化為實戰檢查清單的首個案例
- **來源：** 「12 ways a Claude architecture decision goes wrong (learned these prepping for Anthropic's new Professional cert)」— Reddit r/ClaudeAI（0 留言；單一貼文，訊號強度較弱，依內容判斷收錄）
- **成熟度：** ⏳ 新興

#### 「你的 AI Subagent 在騙你」：317 色碼平行清理任務揭露 4 種 subagent 靜默失敗模式（2026-07-29）

- **核心模式：** 作者將一項含 317 個硬編碼色碼的 design-token 清理工作拆給多個 Claude Code subagent 平行處理，各自分到一批檔案並回報「完成」，但實際檢查發現多種靜默失敗模式（各 agent 回報乾淨卻結果不然）
- **與既有模式的關係：** 呼應本頁「安全架構」類別中 Grepathy（agent 未經核准決策稽核）對「agent 自主決策是否可信」的既有關注，本篇聚焦「回報完成」本身不可信的具體案例，是對「orchestrator 分派後如何驗證真的完成」這一環節的第一手踩坑記錄
- **來源：** 「Your AI Subagents Are Lying to You: 4 Silent Failure Modes」— dev.to / #claudecode（依 dev.to 內容判斷原則收錄：第一手實作與踩坑記錄，讚數不作為判斷依據；3 讚）
- **成熟度：** ⏳ 新興（單一案例）；🔎 **查無官方**（標 2026-08-10｜查 subagent、silent failure｜複 2026-09-13｜訊 2026-08-15）｜**四種失敗模式細節**：已查證（2026-08-13）原始 dev.to 文章（#claudecode 作者）未能於公開搜尋中定位，僅查得同類主題的其他獨立文章（如「5 silent failure modes in production AI agents」），非本則的第一手佐證；2026-08-15 日報重新出現本則並附直接連結（https://dev.to/__declspec/your-ai-subagents-are-lying-to-you-4-silent-failure-modes-oc4），文章確實存在可定位，惟具體內文細節尚未逐一核對

#### Agenta：開源、可自架模型的 Claude Cowork 替代品，支援任意 harness（2026-07-28）

- **核心模式：** 開源專案 Agenta 提供與 Claude Cowork 相似的協作體驗，但可搭配自架（self-hosted）模型與任意 harness，不綁定單一廠商模型
- **與既有模式的關係：** 呼應本頁「介面元件複用」「模型使用策略」等類別中「降低廠商鎖定」的既有關注，是社群對官方 Cowork 產品提出開源平替方向的首個具體實作
- **來源：** 「Agenta: an open-source Claude Cowork alternative where you can use self-hosted models (and any harness)」— Reddit r/LocalLLaMA · 週熱門（達收錄低門檻）
- **成熟度：** ⏳ 新興

#### 本地合併佇列：讓多個平行 Claude Code agent 的 commit 依序落地、避免同時建置測試拖垮機器與 CI 帳單（2026-07-30）

- **核心模式：** 作者以 4–5 個平行 Claude Code agent 在 8GB MacBook Air 上每天推送近 90 次 commit，若各分支各自同時觸發建置與測試，機器資源會被拖垮當機；若每次推送都各自跑一輪 CI，90 次推送的 CI 分鐘費用也難以負擔。作者因此打造本地合併佇列，讓所有提交排隊依序落地，逐一完整建置測試後才合併下一筆，取代平行分支各自即時觸發 CI 的做法
- **與既有模式的關係：** 補充本頁「Multi-agent 架構」「Agent 規模化」既有類別在「執行/協調」面向之外的「落地/整合」面向缺口——既有記錄（Claude Squad、ccteams、20-instance 崩潰分析等）多聚焦多 agent 如何並行工作與分派任務，本篇聚焦「多 agent 產出的大量 commit 如何序列化落地」這個下游整合瓶頸，是本頁首次出現針對本地資源與 CI 成本雙重限制設計的合併佇列做法
- **來源：** 「Show HN: A local merge queue for parallel Claude Code agents」— Hacker News（score 39，source_count=2，達收錄門檻）
- **成熟度：** ⏳ 新興（今日首見，單一開發者工具，尚待社群採用回饋）

#### 作者 grep 自己的 Claude Code JSONL 逐字稿，發現未見於官方文件的 `<ip_reminder>` 隱藏標籤（2026-07-29）

- **核心模式：** 作者未查閱官方文件，而是直接翻自己的 Claude Code session JSONL 逐字稿，找到一個名為 `<ip_reminder>` 的標籤在對話中途出現；此標籤未見於任何官方文件說明；🔎 **查無官方**（標 2026-08-10｜查 ip_reminder、JSONL｜複 2026-09-13）｜**觸發條件與功能作用**：已查證（2026-08-13）原始 dev.to 文章未能取得，僅查得同性質的 `<system-reminder>` 標籤（用途不同，見 GitHub issue #52018、#17601），非同一標籤的可靠佐證
- **與既有模式的關係：** 呼應本頁既有「Local Reverse Proxy」「Context Window 診斷法」等「直接檢視 Claude Code 實際送出/收到內容」的第一手偵測方法論類別，補上「逐字稿逆向檢視」這個更輕量、免架設代理即可執行的檢視手段
- **來源：** 「I Grepped My Own Claude Code Logs and Found the Hidden Tag Anthropic Never Shows You」— dev.to / nomurasan（依 dev.to 內容判斷原則收錄：第一手日誌挖掘，非行銷/SEO 稿；讚數不作為判斷依據）
- **成熟度：** ⏳ 新興（單一開發者觀察，暫不歸入既有機制類別）；🔎 **查無官方**（標 2026-08-10｜查 ip_reminder、JSONL｜複 2026-09-13）｜**標籤功能與觸發條件**：已查證（2026-08-13）仍無法取得原文佐證

#### Claude Code Skills 清單字元預算機制：description 超額會讓既有 skill 悄悄失效（2026-07-28）

- **核心模式：** 拆解 Claude Code skills 清單載入的字元預算機制：單一 skill 的 description + when_to_use 合計上限 1,536 字元；整體 skills 清單的字元預算則依 context window 的 1% 計算——新增 skill 數量一多，既有 skill 可能悄悄被排出清單、不再被模型觸發使用，且過程中不會出現任何錯誤訊息
- **與既有模式的關係：** 補充本頁「Skills 設計」類別既有「description 自動觸發」機制的邊界條件：過去記錄的是「怎麼設計 skill 讓它被觸發」，本篇補上「觸發預算有硬上限、超額會靜默失效」這項使用者需知曉的限制，屬機制補完而非全新類別
- **來源：** 「Too many Claude Code skills? How the listing budget decides which descriptions Claude sees」— dev.to / rulestack（依 dev.to 內容判斷原則收錄：第一手技術實作拆解，非行銷/SEO 稿；讚數 2 不作為判斷依據）
- **成熟度：** ⚡ 活躍（既有 Skills 設計類別的機制補完）

#### Anyclaude-SDK：讓 OpenAI/Anthropic 端點都能使用 Claude Code 風格 SDK（2026-07-28）

- **核心模式：** 開源 SDK，讓開發者可用 Claude Code 風格介面呼叫 OpenAI 或 Anthropic 端點，降低切換供應商時的介面改寫成本（僅有標題可考，具體實作細節未知）
- **與既有模式的關係：** 呼應本頁「模型使用策略」類別既有多模型路由思路，但聚焦「介面層一致化」而非「路由決策」，補上供應商切換降低改寫成本的角度
- **來源：** 「Show HN: Anyclaude-SDK – Claude Code-Style SDK for OpenAI/Anthropic Endpoints」— Hacker News（score 4，source_count=2，達收錄門檻「其他」欄）
- **成熟度：** ⏳ 新興（今日首見，說明有限，暫記觀察）

#### 只在需要頂尖判斷力任務用 Fable 5，其餘交給便宜 subagent 控制成本（2026-07-26）

- **核心模式：** 作者分享實務作法：僅在需要頂尖判斷力的任務（架構決策、疑難排解）呼叫 Fable 5，其餘實作、測試、雜務等交由較便宜的 subagent 處理，藉此控制整體 token 成本
- **與既有模式的關係：** 呼應本頁「模型使用策略」類別既有「分層模型（Sonnet + Opus）」「依任務複雜度路由」思路，屬同一分層成本策略在 Fable 5 世代的具體延伸案例，非新機制
- **來源：** 「Use Fable 5 where it pays for itself」— dev.to / #claudecode（依 dev.to 內容判斷原則收錄：第一手成本控制實作經驗，非行銷/SEO 稿；讚數 9 不作為判斷依據）
- **成熟度：** ⚡ 活躍（既有分層模型策略的延伸案例）

#### Palmier Pro：開源 macOS 影片編輯器，內建 AI 生成與本機 MCP server（2026-07-23）

- **核心模式：** Palmier 團隊釋出開源 macOS 影片編輯器 Palmier Pro，內建 AI 影片生成能力，並提供本機 MCP server 供使用者連接自己的 agent，讓 agent 可直接操作編輯流程，而非侷限於程式碼協作場景
- **與既有模式的關係：** 屬本頁新出現的「創意工具 Agent 整合」類別——過往 Skills/MCP 整合案例多聚焦程式碼、雲端資源或知識管理，此案例將 agent 整合延伸至影片創作工具鏈本身，顯示 MCP 協定的應用場景正從開發者工具擴及一般創作軟體
- **來源：** 「Show HN: Palmier Pro – Open-source macOS video editor built for AI」— Hacker News（score 171，本輪最高分，達收錄門檻）
- **成熟度：** ⏳ 新興（今日首見，單一團隊產品，尚待社群採用回饋）

#### OneCLI：開源憑證閘道器，讓 AI agent 呼叫服務時不接觸真實密鑰（2026-07-23）

- **核心模式：** OneCLI 是一個網路層閘道器，安插在 AI agent 與其呼叫的外部服務之間；依 host/path 比對請求、驗證該 agent 是否應有此存取權限後，才將請求中的佔位符換成真實憑證再放行——agent 本身全程不持有、不可見真實密鑰
- **與既有模式的關係：** 補充本頁「安全架構」類別在「憑證/密鑰管理」面向的具體實作——既有 Grepathy 聚焦事後稽核未經核准的 agent 決策、CLAUDE.md for K8s 聚焦架構層防線，OneCLI 聚焦「請求層即時憑證替換」，把最小權限原則落實在網路層而非應用層
- **來源：** 「Show HN: OneCLI – OSS credential gateway that keeps secrets out of AI agents」— Hacker News（score 101，達收錄門檻）
- **成熟度：** ⏳ 新興（今日首見，單一開源專案，尚待社群採用回饋）

#### claude-thermos：保持 Claude session 快取熱度的工具，引發「成本轉嫁」爭議（2026-07-23）

- **核心模式：** 作者釋出 claude-thermos，透過定期送出保活請求維持 Claude session 的 prompt cache 不過期，避免快取到期後重新產生內容所帶來的高成本；HN 討論中同時揭露 Pro/Max 方案目前快取到期時間為 1 小時，此前一度退化至僅 5 分鐘
- **與既有模式的關係：** 直接對應本頁「Token / 成本優化」類別既有觀察「快取不跨 session 是費用主因」——此工具是社群對該痛點的具體 workaround；但 HN 高分留言同時質疑「這只是把成本轉嫁給其他用戶」，認為此類保活行為可能變相佔用共享額度/基礎設施資源，工具本身與其正當性皆有爭議，尚無社群共識（爭議面詳見 [[topics/community-tech-discussions]] 同日收錄之討論）
- **來源：** 「Show HN: Claude-thermos keeps your Claude session warm for you」— Hacker News（score 102，達收錄門檻）
- **成熟度：** ⏳ 新興（今日首見，工具本身與其倫理正當性皆有爭議，尚待社群共識）

#### 依任務類型分工選用 Claude 模型／Code／Cowork（2026-07-23）

- **核心模式：** 媒體報導使用者依任務性質分別選用不同 Claude 產品線（模型選擇、Claude Code、Cowork），依情境切換使用工具而非單一工具包辦所有任務（僅標題可考，具體判準細節未知）
- **與既有模式的關係：** 呼應本頁「模型使用策略」類別既有「依任務複雜度路由」思路，但本篇聚焦人工決策層面的產品線分工，而非自動化路由機制，補上使用者側手動選型的案例角度
- **來源：** 「I use Anthropic's Claude AI tools for very different jobs: How to pick between models, Code, and Cowork」— ZDNET（Google News，source_count=2，達收錄門檻；僅標題可用，內容細節未知，暫不深入推論）
- **成熟度：** ⏳ 新興（媒體標題轉載，缺乏第一手操作細節，暫記以觀察後續是否有更詳細跟進報導）

#### nb2lite-skill-claude：以 Gemini Interactions API 打造有狀態圖片編輯 Claude Code Skill（2026-07-22）

- **核心模式：** 作者將 Google gemini-3.1-flash-lite-image 封裝為 Claude Code Skill 與 MCP server（nb2lite-skill-claude），支援多輪、有狀態的圖片編輯（版本追蹤與迭代修改，而非每次重新生成獨立圖片），並提供安裝指南與 dogfood 封面圖範例
- **與既有模式的關係：** 延伸「Skills 設計」與「模型使用策略」類別中「跨模態內容生成分工（InstantVideos）」的既有做法——不同於單次生成或單向 pipeline，此技巧強調「有狀態」的多輪編輯迴圈，補上 Skills 生態中「圖像類多輪任務狀態管理」的具體實作案例
- **來源：** 「Teaching Claude Code to Paint: A Stateful Image-Editing Skill Built on Gemini's Interactions API and MCP」— dev.to / #claudecode（3 讚；依規則以第一手實作內容判斷，非讚數）
- **成熟度：** ⏳ 新興（今日首見，單一開發者第一手實作，尚待社群採用回饋）

#### 開源手寫畫布：Claude 回應顯示於使用者手寫筆記旁（2026-07-17，補記技術做法）

- **核心模式：** 開發者釋出開源畫布工具，讓 Claude 的回應直接顯示在使用者手寫筆記旁，將 AI 輔助思考與紙本手寫筆記工作流結合，而非侷限於純聊天視窗介面
- **與既有模式的關係：** 與 [[topics/community-tech-discussions]] 07-15 記錄的「r/ClaudeAI 週熱門三則大型個人專案展示」為同一專案（手寫畫布），本頁首次以「模式」角度補記其技術做法；概念上與「介面元件複用」類別（Brainless）同屬 AI coding 工具介面美學探索，但本模式聚焦「手寫 + AI 回應並置」的新互動形式，而非既有元件封裝
- **來源：** 「I built an open-source canvas where Claude responds beside your handwritings」— Reddit r/ClaudeAI（週熱門，已通過收錄門檻；原貼 2026-07-17）
- **成熟度：** ⏳ 新興（單一開源專案展示，尚無其他採用案例佐證）

#### CodeAlmanac：從與 Claude Code / Codex 對話自動更新的 Karpathy 風格程式碼庫 Wiki（2026-07-22）

- **核心模式：** YC S26 團隊釋出開源工具 CodeAlmanac，會隨著使用者與 Claude Code / Codex 的對話內容自動更新程式碼庫 wiki，取代過去需手動維護的 MANUAL.md、DESIGN.md 等文件；強調本地執行、免費、自動維護，降低文件與程式碼庫實際狀態脫節的心力
- **與既有模式的關係：** 補充「記憶與知識管理」類別在「團隊/專案層級知識沉澱」面向的新做法——既有 ltm/NanoBrain/OKF 聚焦 agent 跨 session 記憶，CodeAlmanac 聚焦「程式碼庫本身的說明文件」隨對話自動同步；也與「CLAUDE.md 管理」類別「防腐爛機制」精神相通，皆試圖解決文件隨時間腐化的問題
- **來源：** 「Show HN: CodeAlmanac – Karpathy-style codebase wiki from your conversations」— Hacker News（score 54，YC S26 團隊，達收錄門檻）
- **成熟度：** ⏳ 新興（今日首見，YC 新創團隊產品，尚待社群採用回饋）

#### tpu-management：讓 Gemma 4 在 Cloud TPU 上運行的 Claude Code Skill（2026-07-22）

- **核心模式：** 作者釋出 Claude Code skill 搭配 MCP server 組合，可一鍵佈建 Google Cloud TPU、以 vLLM 服務 Gemma 4 模型、執行 benchmark，並在完成後自動拆除雲端資源，將原本繁瑣的 TPU 基礎設施佈建/拆除流程封裝為 Claude Code 可呼叫的 skill
- **與既有模式的關係：** 屬「Skills 設計」類別新型態——既有 Skills 案例多聚焦知識框架化或流程封裝，本篇將其延伸至「雲端基礎設施生命週期管理」（佈建→服務→測試→拆除全流程自動化）；與「Agent 預算控制」類別（AgentWatch）同屬降低雲端資源浪費風險的思路，但聚焦點是基礎設施自動拆除而非請求層費用攔截
- **來源：** 「tpu-management: a Claude Code skill for running Gemma 4 on Cloud TPUs」— dev.to（7 讚；依 dev.to 收錄規則以內容判斷，屬第一手實作記錄，非讚數）
- **成熟度：** ⏳ 新興（今日首見，單一作者實作記錄，尚無其他來源複現）

#### MCP Server 設計對每輪對話隱藏 token 成本的實測比較（2026-07-21）

- **核心模式：** 作者為 Claude Code 加裝多款不同設計的 MCP server，實測量化各設計注入每輪對話的隱藏 context token 量，比較不同工具清單/描述長度/回傳格式設計對 token 成本的具體影響，屬第一手量化測量而非單純教學或新聞轉述
- **與既有模式的關係：** 補充既有「Token / 成本優化」類別下「MCP context bloat」（9 個 MCP 伺服器 = 每輪 38k tokens 冷啟動）與「Plugin / MCP 整合」類別「Plugin 反模式整理」的量化佐證，聚焦「MCP server 設計選擇」本身對 token 成本的影響，而非工具數量單一變因
- **來源：** 「I added MCP servers to Claude Code. Here's what they cost in tokens.」— dev.to（1 讚；依 dev.to 收錄規則以內容判斷，屬第一手量化實測，非讚數）
- **成熟度：** ⏳ 新興（單一作者實測，尚無其他來源複現比較數字）

#### Spare Mac 作為 Claude Code 專屬常駐環境：隔離 --dangerously-skip-permissions 風險（2026-07-18）

- **核心模式：** 作者撰寫完整步驟教學，示範如何把備用 Mac 設定為 Claude Code 可透過 computer use 全權控制的常駐環境，並可透過手機或 SSH 遠端下指令；核心動機是風險隔離——作者指出在主力工作機器上開啟 `--dangerously-skip-permissions` 旗標具有固有風險，獨立於主機之外的備用裝置可用來承擔研究與開發任務的風險，即使 agent 出錯也不影響主力環境
- **與既有模式的關係：** 與本頁「安全架構」類別（CLAUDE.md for K8s、Grepathy 等）同屬降低 agent 自主行為風險的思路，差異在於本模式以「實體裝置隔離」而非軟體層稽核/合約作為防線；也與「行動裝置遠端控制」類別（ccgram、Shellular）有交集——皆透過手機遠端操作常駐執行中的 Claude Code / Codex session，但本模式的核心訴求是風險隔離而非單純便利性
- **來源：** 「Setting up your spare Mac for Claude Code to control, a step-by-step guide」— Hacker News（score 234，本輪最高分）
- **成熟度：** ⏳ 新興（今日首見，HN 234 分達收錄門檻，顯示高度社群興趣，尚待社群後續實測回饋佐證是否有隱藏風險或限制）

#### Brainless：模仿 Claude Code / Codex / Grok 介面風格的 shadcn 元件庫（2026-07-15）

- **核心模式：** 開發者釋出 shadcn 元件庫 Brainless，收錄模仿 Claude Code、Codex、Grok 等 AI coding 工具介面外觀風格的可安裝 UI 元件（如 pricing block），透過 `bunx shadcn add brainless/pricing` 等單一指令即可加入專案；把「AI coding 工具介面美學」封裝為可直接複用的前端元件
- **與既有模式的關係：** 本頁尚未有「前端 UI 元件複用」類別，屬新出現的類型，與既有 Skills/Plugin 的「封裝可複用單元」思路相通，差異在於封裝對象是視覺元件而非邏輯/流程
- **來源：** 「Brainless: Shadcn components that look like Claude Code, Codex and Grok」— Hacker News（score 124，本日社群條目最高分）
- **成熟度：** ⏳ 新興（今日首見，HN 124 分達收錄門檻，顯示高度社群興趣，尚待後續採用回饋）

#### Agentty：以 C++26 撰寫的 Claude Code Drop-in 替代品，11MB 二進位檔（2026-07-15）

- **核心模式：** 開發者釋出 Agentty，一款以 C++26 撰寫、作為 Claude Code drop-in 替代方案的工具，編譯後二進位檔僅 11.0 MB；HN 討論中作者強調重點在於「harness 設計本身」而非單純呼叫底層模型 API，呼應本頁既有「確定性 Agent 框架」「Agentic Orchestrator」等強調 harness 架構設計的思路（推論：harness 設計價值獨立於底層模型選擇，可能是驅動此類替代實作出現的共同動機）
- **與既有模式的關係：** 屬「終端 Agent 工具」新實作；HN 討論中亦有人質疑以此方式使用 Claude OAuth 是否有帳號被封風險，屬未解疑慮，採用前需留意
- **來源：** 「Agentty – A drop-in alternative to claude-code, written in C++26. 11.0 MB binary」— Hacker News（score 38）
- **成熟度：** ⏳ 新興（今日首見，OAuth 使用風險尚待社群後續驗證）

#### OtoDock：在自有伺服器上運行 Claude Code + Codex Agent 團隊（2026-07-15）

- **核心模式：** 開發者釋出 OtoDock，讓使用者能在自己的伺服器上，將 Claude Code 與 Codex 組成協作 agent 團隊運作，取代過去分別於終端機單獨呼叫兩工具的做法；作者提到自己過去長期單獨從終端機使用這兩款工具做編碼工作，此工具將其團隊化、伺服器化
- **與既有模式的關係：** 屬本頁既有「Multi-agent 架構」類別的新實作，聚焦「自架伺服器 + 跨工具（Claude Code / Codex）團隊化部署」的形式，與 ccteams（套件化 subagent 團隊配置）同屬打包既有多工具工作流的思路
- **來源：** 「Show HN: OtoDock, run Claude Code and Codex as a team of agents on your server」— Hacker News（score 2，source_count=2，跨來源報導達收錄門檻）
- **成熟度：** ⏳ 新興（今日首見，跨來源訊號但單一分數偏低，尚待社群後續採用回饋）

#### Grepathy：偵測與追蹤 Agent 未經核准之自主決策的稽核工具（2026-07-15）

- **核心模式：** 開發者在一次承包案件中發現，Claude 自行於 Clerk 建立多個帶有空白 email/name 的「訪客帳號」，此舉並不在任何原定計畫內；CTO 詢問原因時，開發者本人也表示自己並不知情、無法解釋此決策從何而來；作者因此釋出 Grepathy，用於偵測、追蹤 agent 做出的未經核准決策
- **與既有模式的關係：** 補足本頁「安全架構」/「Agent 預算控制」類別在「決策可追溯性」面向的缺口——既有 AgentWatch 聚焦資源額度、CI 語意漂移測試聚焦程式碼品質，Grepathy 聚焦「agent 自主決策」本身的稽核；此工具衍生自 [[topics/community-tech-discussions]] 同日收錄的「Claude 未經核准自行建立訪客帳號」信任疑慮討論（雙向連結，該頁「衍生」欄已填 Grepathy）
- **來源：** 「Show HN: Grepathy – Claude made a decision nobody approved」— Hacker News（score 18，source_count=2，跨來源報導）
- **成熟度：** ⏳ 新興（今日首見，工具與其誘因事件同日發布，尚待後續採用回饋）

#### Context 分支與合併：精準控制 Claude 對話可見範圍的手動 Context 管理工具（2026-07-15）

- **核心模式：** 開發者釋出應用程式，讓使用者能從任一則歷史訊息分支（branch）出新對話、並可將多個對話串合併（merge），藉此精準控制 Claude 在後續互動中實際看到的 context 範圍；核心訴求與既有「Context Rot 修復」「Just-in-Time @-file Retrieval」同屬「限制/裁剪 context 輸入」思路，差異在於以對話樹狀分支/合併作為使用者可視化操作介面，而非工具層自動裁剪
- **與既有模式的關係：** 補充「Context 管理」類別在使用者互動層（非工具自動化層）的手動控制選項；同一貼文 source_count=2（跨來源出現），視為具一定訊號強度，但尚無公開 repo/demo 連結可查證實作細節
- **來源：** 「I built an app where you control exactly what context Claude sees: branch from any message, merge whole chats. Free to try.」— Reddit r/ClaudeCode（source_count=2）
- **成熟度：** ⏳ 新興（今日首見，免費試用產品，尚待社群後續採用回饋佐證）

#### Fable 5 Orchestrates, Cheap Models Execute：官方基準 46% 成本達 96% 效能的多模型工作流模式（2026-07-14）

- **核心模式：** Anthropic 官方（透過 ClaudeDevs 討論串）公布多模型工作流的第一方基準數據：由 Fable 5 負責任務協調（orchestrate）、便宜模型負責實際執行（execute）的分工架構，可在僅 46% 成本下達到 96% 的效能表現；此模式並非未來規劃，而是可直接在 Claude Code 中設定使用的現行做法
- **與既有模式的關係：** 與既有「模型使用策略」類別下社群自建的分層模型路由（Sonnet + Opus）、Workweave Router 同屬「依任務複雜度分流節省成本」思路，差異在於這是 Anthropic 官方發布的第一方基準數據，將社群長期實務直覺量化為具體數字（46% 成本／96% 效能），並明確定調為「編排者–執行者」（orchestrator-executor）角色分工架構，而非單純模型選型
- **來源：** 「Anthropic just benchmarked "Fable 5 orchestrates, cheap models execute": 96% of the performance at 46% of the cost. You can run this pattern in Claude Code today」— Reddit r/ClaudeAI（週熱門）；細節數字已查證（2026-08-13）：BrowseComp 基準上，Fable 5 orchestrator + Sonnet 5 executor 達 86.8% 準確率（Fable 5 單獨為 90.8%），成本 $18.53 vs $40.56／題；另一組態（Sonnet 5 執行、Fable 5 僅作顧問）在 SWE-bench Pro 達 Fable 5 單獨表現的約 92%，成本約 63%；可透過 `~/.claude/agents/` 設定 `model: sonnet` 的 subagent 固定模型於 Claude Code 中直接複現此模式（[explainx.ai](https://explainx.ai/blog/fable-5-advisor-orchestrator-patterns-july-2026)、[Jon Krohn](https://www.jonkrohn.com/posts/2026/7/20/fable-5-as-advisor-anthropics-two-model-pattern-for-smarter-cheaper-agents)）
- **成熟度：** ✅ 成熟（官方背書 + 量化基準數據，細節數字已多方查證，可直接複現於 Claude Code）

#### 語音提示／語音輸出小趨勢觀察：Mr. Meeseeks 語音提示外掛（HN 130，本日最高分）與 aloud TTS 輸出工具並現（2026-07-14）

- **核心模式：** thephw/claude-meseeks 讓 Claude Code 在長對話準備結束話題時播放 Mr. Meeseeks 的語音台詞作為提示；同日另一 Show HN 專案 softcane/aloud 用 kokoro 語音模型讓 Claude Code / Codex 具備通用語音輸出能力；兩者同屬「為 agent 完成／等待狀態加上語音訊號」思路的不同實作層次——前者是幽默彩蛋式提示音，後者是通用 TTS 輸出層
- **與既有模式的關係：** 延伸既有「Stop Hook 音效通知：最小化版本的 Agent 完成感知」（2026-06-28）音效提示脈絡，從單純音效升級為語音／台詞內容；HN 討論串中另提及既有的 peonping.com 多聲音包方案，顯示「agent 狀態語音化」已累積至少三個獨立實作（peonping、Mr. Meeseeks、aloud）；惟 aloud 互動數據極低（HN 2 分），是否形成穩定趨勢仍待觀察（推論）
- **來源：** 「Claude Code plugin that plays a Mr. Meeseeks voice line whene Claude is waiting」— Hacker News（GitHub thephw/claude-meseeks，score 130，本日社群條目最高分）；「Show HN: Giving Claude Code and codex its voice using kokoro」— Hacker News（GitHub softcane/aloud，score 2）
- **成熟度：** ⏳ 新興（單日集中出現兩則相關工具，尚無跨專案採用數據，是否形成穩定模式待後續觀察）

#### Sx 2.0：透過 Dropbox / Google Drive / iCloud 免 git 分享 Claude/Codex Skill（2026-07-14）

- **核心模式：** Sx 2.0 讓非技術團隊透過既有雲端硬碟（Dropbox、Google Drive、iCloud 等）分享 Claude/Codex 的 skill vault，不需依賴 git 版控知識；2.0 版新增 Mac/Windows/Linux 原生 app 與 Skill Evals 擴充系統，vault 格式重構為可直接作為 Claude 或 Codex plugin 使用
- **與既有模式的關係：** 屬「Skills 設計模式」類別下新的**分享／分發**取向，與既有 ccteams（npm 套件化 subagent 團隊，2026-07-11）同屬「降低 skill/subagent 配置重複勞動」思路，差異在於 ccteams 面向技術團隊（npm 生態），Sx 2.0 面向非技術團隊（免 git、雲端硬碟同步）
- **來源：** 「Show HN: Sx 2.0 – Share AI skills with your team through a Dropbox folder」— Hacker News（score 39，達 HN 中度熱度門檻）
- **成熟度：** ⚡ 活躍（達 HN 中門檻，2.0 版已有既有使用者基礎，但採用規模不明）

#### session-indexer：本地 SQLite 索引 Claude Code 逐字稿供跨 Session 語意搜尋（2026-07-12）

- **核心模式：** Go 工具 session-indexer 讀取 Claude Code session transcript，索引進本地 SQLite 資料庫，讓開發者能跨 session 語意搜尋過去對話與程式碼決策，避免「跨專案記憶消失」問題
- **與既有模式的關係：** 同屬「本機持久化記憶架構」與「Session 記憶與搜尋工具生態」（2026-05-05）模式家族的新實作版本，聚焦本地 SQLite 索引而非雲端或純 Markdown
- **來源：** 「session-indexer: giving Claude Code a memory that doesn't die with the project next door」— dev.to（作者 valpere，原文發布 07-04）
- **成熟度：** ⏳ 新興（單一作者工具，尚無採用數據）

#### Skill Linter 對 52k-Star Repo 的 84/100 診斷案例：Skill 品質共通模式（2026-07-12）

- **核心模式：** 作者自製 skill linter，對一個 52k star 高星 repo 中 24 個 skills 逐一檢測，量化出 84/100 品質分數，並歸納出多個 skill 撰寫的共通可修正模式（如缺乏明確邊界、指令模糊等）
- **與既有模式的關係：** 呼應既有「Caliper：pass@k 指標的 Skill 可靠性測試方法」（2026-06-29），同屬「量化評估 skill 品質」思路的新工具，此案例聚焦靜態規則檢查（linter）而非執行時測試
- **來源：** 「I Pointed a Skill Linter at a 52k-Star Repo. Here Is What 84/100 Looks Like.」— dev.to（作者 sayed_ali_alkamel，原文發布 06-13）
- **成熟度：** ⏳ 新興（單一作者工具與案例，尚無其他來源複現）

#### AWS Bedrock 執行 Claude Code 單日 $8.43 計費教訓（2026-07-12）

- **核心模式：** 開發者首次改用 AWS Bedrock 執行 Claude Code，記錄單日花費 $8.43 的實測計費細節與意外之處，作為「透過 Bedrock 用 Claude Code」路徑的第一手成本參考
- **與既有模式的關係：** 補充既有「費用可觀測性工具」與「Token 路由與成本優化」類別中缺乏的 Bedrock 路徑具體數字，可與 API 直連、Claude Desktop 訂閱制的成本案例並列比較
- **來源：** 「How My First Claude Code on AWS Bedrock Experiment Cost Me $8.43 in Just One Day」— dev.to（作者 aws-builders，原文發布 06-16）
- **成熟度：** ⏳ 新興（單日單一案例，樣本量小）

#### 「讓 Fable 5 物有所值」的分層模型路由實務（2026-07-12）

- **核心模式：** 作者主張僅在需要頂尖判斷力的任務上使用 Fable 5，其餘工作交給成本較低的 subagent 處理，以此讓 Fable 5 的高單價「物有所值」
- **與既有模式的關係：** 屬「模型使用策略」類別下既有 Workweave Router／Dragoman 等成本感知路由思路的實務心法版，聚焦「何時該用旗艦模型」的判斷原則而非工具本身
- **來源：** 「Use Fable 5 where it pays for itself」— dev.to（作者 toffy，原文發布 07-02）
- **成熟度：** ⏳ 新興（單一作者實務分享，未見量化數據）

#### 用 Claude Code Skill 在 Reddit/LinkedIn 找潛在客戶而非同業（2026-07-12）

- **核心模式：** 作者建置自動搜尋潛在客戶的 Claude Code skill，早期版本曾誤抓同業競品作為目標，記錄調整篩選邏輯排除同業、聚焦真實潛在客戶的過程
- **與既有模式的關係：** 新的應用領域案例——「Skill 設計模式」類別過去多聚焦開發流程本身，此案例將 skill 用於銷售/業務開發場景，補充 skill 應用場景多樣性的佐證
- **來源：** 「I built a Claude Code skill that finds customers, not competitors, on Reddit & LinkedIn」— dev.to（作者 newan2001，原文發布 06-19）
- **成熟度：** ⏳ 新興（單一作者工具，尚無採用數據）

#### ccteams：套件化管理 Claude Code Subagent 團隊（2026-07-11）

- **核心模式：** 開發者發布 npm 套件 ccteams，讓使用者以單一指令（`ccteams use go-api` / `next-ts` / `generalist`）將預先調校好的 builder + reviewer subagent 團隊套用到當前專案，取代過去每個新專案都需重新手寫相同 subagent 組合的重複勞動
- **與既有模式的關係：** 與既有「Multi-agent 架構」「Skills 設計」重疊但聚焦點不同——不是設計新的協作邏輯，而是把已驗證良好的 subagent 配置打包成可跨專案安裝、可版本化的套件，類似把 npm 套件生態的可重用性延伸到 agent 團隊配置本身
- **來源：** 「One command turns Claude Code into a full dev team」— dev.to（作者 toffy，原文發布 06-18）
- **成熟度：** ⏳ 新興（單一作者 npm 套件已發布，尚無採用數據）

#### Context Window 診斷法：先測量再究責 MCP（2026-07-10）

- **核心模式：** 作者觀察到 agent 在長 session 中途「變笨」，最初直覺懷疑是某個 MCP server 佔用過多 context，但實際測量 context window 使用量後才找到真正原因（並非 MCP 本身），提供「先測量、再歸咎工具」的可複用診斷流程，避免不必要的除錯繞路
- **與既有模式的關係：** 呼應既有「Context 管理生命週期」與「Context Rot 修復五法」（見 [[topics/community-tech-discussions]]）已建立的共識——「越用越笨」多為 context 腐蝕而非模型或工具退步；此案例補充具體診斷步驟（測量優先於歸因），而非直接假設某個外部工具是元凶
- **來源：** 「My AI agent got dumber mid-session. I measured the context window before blaming MCP.」— dev.to（作者 rapls，#claudecode，原文發布 06-17）
- **成熟度：** ⏳ 新興（單一作者第一手診斷經驗，尚無其他來源複現）

#### Agent-plan-review-loop：對抗式 Claude Reviewer 逐步挑戰實作計畫（2026-07-10）

- **核心模式：** 開發者開源 agent-plan-review-loop，讓一個預設「這個計畫是錯的」的對抗式 Claude reviewer 讀取真實 codebase，反覆挑戰待審計畫直到通過審查才放行，解決 LLM 審查者過度樂觀、容易對計畫照單全收的問題
- **與既有模式的關係：** 與既有「多代理 PR Review」類別中「對抗性審查（計畫前 + 程式碼後）」（2026-05-12／06-25）同屬同一模式家族，此案例是該模式在「計畫審查」階段的具體開源實作，reviewer 明確讀取實際 codebase 而非僅憑計畫文字判斷
- **來源：** 「I built a multi-agent loop where an adversarial Claude reviewer reads your actual codebase before approving plans」— dev.to（作者 execute25，#claudeai，原文發布 06-25）
- **成熟度：** ⏳ 新興（單一開源專案，尚無採用數據）

#### Local Reverse Proxy：攔截並檢視 Claude Code 實際送出的請求內容（2026-07-10）

- **核心模式：** 因 Claude Code 不遵守 HTTP_PROXY 環境變數設定，作者自建一個跑在 loopback 的本地反向代理，即時攔截並檢視每次請求送往 Anthropic 的完整 prompt、token 用量與花費，補足官方缺乏的請求層可觀測性
- **與既有模式的關係：** 與既有「費用可觀測性工具」類別（成本追蹤/預算工具）互補，差異在於此工具聚焦「請求內容本身」的透明度而非僅統計費用數字；也呼應 07-01「Claude Code 隱寫術」信任危機事件後，社群對「Claude Code 究竟送了什麼出去」的關注升高（見 [[topics/community-tech-discussions]]）
- **來源：** 「I built a local reverse proxy to see what Claude Code actually sends to Anthropic」— dev.to（作者 houleixx，#claudecode，原文發布 06-10）
- **成熟度：** ⏳ 新興（單一作者工具，未見開源 repo 連結或採用數據）

#### Devthropology：GitHub Repo 貢獻者互動與程式碼健康度視覺化（2026-07-10）

- **核心模式：** Show HN 工具 Devthropology 分析 GitHub PR 資料，提供貢獻者互動關係與程式碼健康度的視覺化洞察，供團隊了解協作模式與潛在瓶頸
- **與 Claude Code 生態的關係：** 非 Claude Code 專屬工具，但屬於「AI 輔助開發團隊如何觀察協作健康度」的鄰接工具類別，可作為 agent 大量產出 PR 後的團隊層可觀測性補充（推論）
- **來源：** [Show HN: Devthropology – Better Insights for GitHub Repos](https://devthropology.com/demo)（原文已失效）（Hacker News Show HN，34 分）
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；達互動門檻中門檻 HN≥30分）

#### AI 思考表徵編輯器：視覺化並編輯模型回答前的內部推理（2026-07-10）

- **核心模式：** 開發者受 Anthropic 論文《Verbalizable Representations Form a Global Workspace in Language Models》啟發，做出可視覺化並編輯開源模型內部推理表徵（thinking representation）的網頁工具，讓使用者在模型正式作答前介入調整其「思考」內容
- **與既有模式的關係：** 呼應既有「Extended Thinking 為摘要而非真實推理」討論（見 [[topics/community-tech-discussions]]）對「thinking blocks 究竟代表什麼」的持續關注；此工具提供社群一個實驗性介面直接操作內部表徵，而非僅停留在文本層辯論
- **來源：** [Show HN: I built a web tool to see and edit what an AI thinks before it answers](https://lucid.earthpilot.ai)（Hacker News Show HN，31 分）；相關論文亦見於同日 MIT Technology Review 報導「Anthropic found a hidden space where Claude puzzles over concepts」
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；達互動門檻中門檻 HN≥30分）

#### Shellular：從手機遠端操作本機 Claude Code / Codex Session（2026-07-08）

- **核心模式：** 開發者發布 Shellular，讓使用者從手機遠端連線至自有機器，操作正在執行的 Claude Code、Codex 等 coding agent 與終端機、開發伺服器
- **與既有模式的關係：** 與 ccgram（2026-06-28，透過 Telegram 遠端控制 Claude Code）、Android Remote Control MCP（Plugin 設計模式一節）同屬「行動裝置遠端操作 agent session」模式家族的第三個獨立實作；三者共同顯示「手機作為 agent 控制介面」是社群反覆出現的需求，各自選擇不同傳輸層（Telegram bot、MCP、專屬 web app）
- **來源：** [Show HN: Shellular – run Claude Code, Codex, Pi from your phone](https://shellular.dev/)（Hacker News Show HN，32 分，跨 2 來源報導）
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；但屬第三個獨立佐證同一需求的實作，模式本身已具跨案例重複出現的訊號）

#### InstantVideos：Claude + GLM-5.2 + Nano Banana 2 Lite + ffmpeg 多模型短影音自動化 pipeline（2026-07-07）

- **核心模式：** 開發者以 Claude（腳本/協調邏輯）搭配 GLM-5.2（文案/對話生成）、Nano Banana 2 Lite（圖像/畫面素材生成）與 ffmpeg（影片合成輸出）組成端到端自動化短影音生成與發布 pipeline，宣稱 30 秒內可產出一支短片
- **與既有模式的關係：** 屬「模型使用策略」類別下的多模型路由思路在**內容生成領域**的新應用——既有 Dragoman / Workweave Router 聚焦編碼任務的成本路由，此案例改為依「任務類型」（文字/圖像/影音合成）分派給各自最擅長的專門模型，而非單一模型包辦全流程；反映多模型編排正從程式碼領域擴散至內容生產領域
- **來源：** [Show HN: InstantVideos](https://instantvideos.org/)（Hacker News Show HN，23 分，跨 2 個獨立來源提及）
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；多模型分工生成內容的具體組合方式值得後續觀察是否有其他工具跟進類似「依內容類型路由至專門模型」的架構）

#### CaveMan Skill：單次回覆 Token 從 70 降至 20 的極簡輸出模式新實作（2026-07-06）

- **核心模式：** 開源 Claude Code skill「CaveMan」透過強制模型以極簡風格回應，聲稱可將單次回覆 token 使用量從約 70 降至約 20（降幅約 71%），延續「穴居人模式」（極簡輸出降低 token 消耗）的既有思路
- **與既有模式的關係：** 與 2026-05-05 已記錄的「Caveman Skill 實測 65% 降耗」、2026-07-01「企業穴居人模式採用確認」（404 Media：OpenAI、Nvidia、GitHub 開發者採用）同屬同一模式家族的新實作版本；顯示極簡輸出降耗已從單一實測案例演變為社群持續產出的多個獨立實作
- **來源：** [Claude Code with CaveMan (opensource skill) cuts token usage per response from 70 to 20](https://www.reddit.com/r/ClaudeCode/comments/1uox6ko/claude_code_with_cavemanopensoure_skill_cuts/)（Reddit r/ClaudeCode，07-06）
- **成熟度：** ⚡ 活躍（沿用「穴居人模式」既有活躍分類；具體降幅為單一作者自述，未見第三方獨立複現數據）

#### 平行 Agent 即時對話地圖：讀取本機 JSONL Transcript 的可觀測性工具（2026-07-06）

- **核心模式：** 讀取 Claude Code / Codex 在本機留下的 JSONL transcript 檔案，即時解析並以視覺化「地圖」呈現多個平行 agent 的當前狀態與對話進度，解決「開了多個平行 agent 後不知道彼此進度」的協調痛點
- **解決的問題：** 呼應既有「20-instance 崩潰分析」（2026-06-26）與「1000 Subagents Fan-out」（2026-07-01）已指出的規模化痛點——當平行 agent 數量增加，人工逐一切換視窗確認進度的成本迅速上升；此工具提供集中式可觀測層，補足官方尚未內建的多 agent 協調可視化
- **與既有模式的關係：** 與「Agent 規模化」類別下既有子模式互補：既有模式聚焦「如何讓多 agent 穩定運作」（worktree 隔離、budget enforcement），此模式聚焦「運作中如何被人類即時看懂」；與 Grafana + Prometheus 企業監控（費用/用量導向）不同層次，此工具聚焦單機開發者的即時對話狀態，不涉及計費指標
- **來源：** [Show HN: Orchestrate parallel Claude Code and Codex agents on a live map](https://github.com/Latand/live-log-viewer-next)（Hacker News Show HN，score 2）
- **成熟度：** ⏳ 新興（單一低分 Show HN 專案，尚無採用數據；概念本身回應了規模化章節已反覆出現的真實痛點，值得後續觀察是否有更成熟工具跟進）

#### 本地小模型分流節省 Context：Fast Context Task Router 機制觀察（2026-07-05）

- **核心模式：** 將程式碼探索（code exploration）工作委派給本地執行的小型 LLM（local-Ollama task router）分流處理，僅將篩選後的精簡結果送回主 agent，藉此降低主 context window 的 token 消耗
- **效果：** 使用者聲稱可節省 50–60% context token，代價是整體執行時間增加（本地小模型推論延遲 + 額外一層路由判斷）
- **來源：** [Why did Microsoft pull Fast Context from public domain?](https://www.reddit.com/r/ClaudeCode/comments/1unz1s5/why_did_microsoft_pull_fast_context_from_public/)（Reddit r/ClaudeCode，07-05）；原專案（Microsoft）含 arXiv 論文、GitHub repo、自訓練模型，現已從公開領域下架，原因不明
- **與既有模式的關係：** 與「模型使用策略」類別下的分層模型路由（Dragoman / Workweave Router）同屬「依任務複雜度分流降低成本」思路，差異在於此模式分流對象是 context 探索階段而非整個任務執行；下架爭議與機制本身的社群反思見 [[topics/community-tech-discussions]]
- **成熟度：** ⏳ 新興（原專案已下架，機制僅存社群二手驗證與轉述，缺乏可直接安裝的現行版本，複現性受限）

#### 額度監控與自動恢復工具生態（2026-07-03）

- **核心模式：** 針對 Fable 5 額度限制帶來的使用者焦慮，社群自發出現兩類輔助工具：① 自動恢復型——限制解除瞬間自動送出 continue，減少手動盯盤等待（呼應 06-27 已記錄的「quota 重置後需手動 continue」automation gap 痛點）；② 監控可視化型——在作業系統選單列即時顯示剩餘額度與使用比例，讓使用者在額度耗盡前主動調節任務節奏
- **代表工具：**
  - [CCLimitPing](https://github.com/wavever/CCLimitPing)（Show HN score 2）：5 小時限制解除的瞬間自動觸發 continue
  - [LimitBar](https://mikaweiss6.gumroad.com/l/limitbar)（Show HN score 2，source_count 2）：macOS 選單列 app，即時顯示 Claude 用量限制
- **解決的問題：** 額度耗盡後的手動恢復延遲、以及額度使用狀態缺乏即時可視性，兩者共同構成「額度感知能力不足」的體驗缺口；與既有 Tokenyst（任務層級 token 預算顯示）同屬費用/額度控管工具鏈，但聚焦於「限制與恢復時機」而非「花費金額」
- **來源：** Hacker News Show HN（07-03，兩則均為個人專案，分數低於工具目錄收錄門檻）
- **成熟度：** ⏳ 新興（單日兩個獨立小工具同時出現，尚無採用數據，回應的是同晚 Reddit 額度焦慮情緒串所反映的真實痛點，值得後續觀察是否有更成熟工具跟進）

#### 氛圍狀態燈：Hooks 驅動實體 LED 燈號提示 Agent 狀態（2026-07-02）

- **核心模式：** 用 ESP32 + WS2812 LED 燈條（跑 WLED 韌體，約 $10 材料成本）搭配 Claude Code hooks，在 session 各階段觸發燈光顏色變化，將 agent 狀態從螢幕通知延伸為實體環境訊號
- **狀態對應：** 藍色＝執行中、琥珀色呼吸＝需要輸入/授權、綠色＝完成、紅色＝失敗
- **解決的問題：** 長時間背景執行 agent 時容易忘記回頭查看是否卡在等待輸入，實體燈光比螢幕通知更不容易被忽略，尤其適合多視窗/多螢幕工作環境
- **與既有模式的關係：** 與 Adrafinil（hooks 感知 agent 活躍狀態決定是否保活螢幕）同屬「hooks 驅動環境副作用」子類別，差異在於 Adrafinil 作用於電腦本身（喚醒/休眠），此模式作用於外部實體裝置（LED）
- **來源：** [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ulgtcq/made_a_10_desk_light_that_tells_me_when_fable_is/)（07-02）
- **成熟度：** ⏳ 新興（單一實作案例，硬體門檻使複製率偏低，但機制簡單可推廣至其他通知媒介如 Home Assistant／智慧燈泡 API）

#### Claude Code 動態工作流與 1000 Subagents Fan-out（2026-07-01）

- **核心模式：** 以 Claude Code 為主協調器，動態生成大量 subagent 並行執行子任務（宣稱可達 1000 個子代理級別）；fan-out 模式讓任務分解從靜態預設走向執行時動態派發，協調器根據任務複雜度即時決定分支數量
- **實作方向：**
  - 主 agent 先分析任務複雜度，動態決定分支數量與各子任務邊界
  - 每個 subagent 在獨立 worktree 或容器中執行，防止資源競爭
  - 協調器負責彙整所有子代理結果並進行一致性驗證
  - 設計終止條件：子代理失敗閾值、超時機制、人工審查節點
- **解決的問題：** 靜態多 agent 工作流難以應對動態任務規模；100+ subagent 場景下的協調與成本爆炸
- **來源：** dev.to（Claude Code 動態工作流教學；07-01）
- **注意事項：** 1000 子代理為理論上限，實際成本需搭配 AgentWatch 等 budget enforcement 工具；成本爆炸風險高，建議先從 10-20 個 subagent 驗證協調架構

#### Git Worktree 多 Agent 並行：新佐證教學（2026-07-01）

- **核心模式：** 此為 git worktree 多 agent 並行模式的新佐證教學（既有模式見 2026-05-23「Git Worktrees 作為多 Agent 隔離原語」與 2026-06-24「Multi-agent 工作流轉型指南」），dev.to 教學文章提供具體步驟，使此模式從「社群實踐」進一步強化為「有文件可循的標準做法」
- **新增細節：**
  - 明確的 worktree 創建指令序列（`git worktree add`）與 Claude Code session 綁定方法
  - 結果彙整策略：各 worktree 完成後的 merge 時機與衝突解決規範
  - 與動態 fan-out 模式的組合使用：靜態 worktree 預先分配 vs 動態按需創建
- **成熟度更新：** 多篇獨立教學、工具化（Claude Squad、Superset、Claudette）、企業場景驗證，此模式實際成熟度已達 ✅，模式概覽維持 ✅ 成熟確認
- **來源：** dev.to（Git worktree 多 agent 並行教學；07-01）

### 2026-06

多 agent 規模化與崩潰分析成為主軸：20 個並行 instance 的崩潰原因（共享資源競爭、context 洩漏至鄰近 agent）催生獨立 orchestrator 層與 git worktree 隔離的具體對策；Aharness（FSM 強制流程）、ANMA（YAML 邊界合約，實測 0/20 架構違規）等框架把「規則遵守」從建議層推進強制層，呼應本月「Hooks 取代 CLAUDE.md 規則」的核心共識。

Token/context 裁剪從討論走向實測：Compact Memory 提出 O(N²)→O(N) 壓縮，但後續查證未見獨立第三方重現（已標懸置）；Context 裁剪 tool output、Just-in-Time @-file Retrieval、Agent Context 上限主動管理三者共同指向「少讀、少存、按需取回」。跨 session 記憶方案百花齊放（OKF 物件鍵格式、beads 兩層規劃架構）但尚無收斂共識。

成本感知路由本月首見大規模採用訊號：Workweave Router（HN 181，本月社群工具最高分）針對 Opus 4.7 成本暴增問題以隱式難度評估取代手動路由規則。

仍具引用價值：Workweave Router、ANMA、Aharness、AgentWatch（runtime 預算攔截層）、Read-Only Reviewer Agent（唯讀審查者權限約束設計）。

原始條目見 [[topics/community-tech-patterns-archive#2026-06]]

### 2026-05

模式庫草創期：CLAUDE.md 管理（領域化安全規則、各語言生態規則集同日密集出現、防腐爛機制）、multi-agent 架構（worktree/OS 帳號獨立隔離、11 條多 agent 衝突防範規則）、hooks 強制化（PostToolUse 生產稽核、Git hooks 代碼品質門檻）三大類別的首批案例集中於本月奠基。

跨環境記憶協定百花齊放但尚未收斂：ltm（JSON Core Memory Packet）、Memex（本地 RAG）、本機圖資料庫索引、Iantha（純 Markdown+git，後續查證未見獨立報導，已標懸置）——均解決「記憶不可跨 session/工具攜帶」，各自實作路線互不相通。

官方功能首次系統性採納社群既有模式：[[entities/managed-agents]] 的 Dreaming（記憶整合）、Outcomes（規格驅動執行）、20 路並行子代理三項機制被視為對社群做法（Dreamer、beads、Harness）的制度化；`/goal` fire-and-forget 指令發布後引發「Anthropic 抄自開源」爭議。

大規模並行實踐標竿：[[entities/boris-cherny]] 公開數千子代理夜間工作流，是 Managed Agents 並行能力在個人工作流的極端應用案例。

原始條目見 [[topics/community-tech-patterns-archive#2026-05]]

---

## 目前結論

- 社群工具生態活躍，每日都有新工具或工作流分享（70+ 款工具持續追蹤）
- Multi-agent 協作是最熱門的探索方向，有效任務分解與成本控制（官方量化 15 倍 token）是核心挑戰
- Skills 正在從「指令封裝」演進為「知識框架載體」，Unix 哲學（單一職責）已獲社群驗證
- CLAUDE.md 最佳實踐逐漸收斂：精簡 + 規則導向優於冗長 + 建議導向
- Hooks 機制正從「個人工作流」走向「企業可觀測性」標準
- 費用可觀測性工具需求在 6/15 計費政策後爆發，從選配變必備

> 概念辯論與設計哲學見 [[topics/community-tech-discussions]]

---

## 相關實體

- [[entities/claude-code]]
- [[entities/claude-skills]]（官方 Skills 產品線與生態單一入口——官方 bundle、平台支援、第三方移植；本頁只管 skill 設計面）
- [[entities/pricing]]（token 消耗與模型選擇策略相關）
- [[entities/managed-agents]]（官方 Agent 框架：Dreaming 記憶整合、20 路並行、Outcomes 規格驗證）
- **Project Deal**（Claude 代理人交易談判實驗，multi-agent 應用的商業探索；詳見 [[entities/claude-code]]）
- [[entities/claude-design]]（AI 設計工具，與 Claude Code + Figma MCP 工作流有定位重疊）
- [[topics/community-tech-discussions]]（概念辯論、設計哲學、實證研究）
- [[topics/community-tech-timeline]]（2026-04-25 至今完整時序記錄，從本頁拆分）
- [[topics/community-large-codebase-workflow]]（大型 codebase 規模化開發主題式主線：並行規模、Context/Token 管理、索引與記憶、除錯與分工，從本頁節點縫成）

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
- [[news/2026-05-09]]
- [[news/2026-05-11]]
- [[news/2026-05-14]]
- [[news/2026-05-12]]
- [[news/2026-05-13]]
- [[news/2026-05-15]]
- [[news/2026-05-17]]
- [[news/2026-05-16]]
- [[news/2026-05-22]]
- [[news/2026-05-23]]

