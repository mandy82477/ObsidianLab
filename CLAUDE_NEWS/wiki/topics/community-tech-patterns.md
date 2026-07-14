# 社群實戰模式庫

**狀態：** monitoring
**領域：** 🌐 社群
**開始日期：** 2026-04-25
**最後更新：** 2026-07-14
**最後新聞更新：** 2026-07-14

> **最新工作流模式**（2026-07-14）
> Anthropic 官方公布第一方基準數據：Fable 5 編排、便宜模型執行的多模型工作流可在 46% 成本下達 96% 效能，且今日已可在 Claude Code 直接使用；同日另補入 Sx 2.0（免 git 雲端硬碟分享 skill）與 Mr. Meeseeks／aloud 語音提示小趨勢觀察（HN 130 分為本日社群條目最高分）。

---

## 摘要

追蹤 Claude Code 社群在實際開發中累積的**工作流與應用模式**。本頁收錄的模式類型包括 Multi-agent 架構、Skills 設計、CLAUDE.md 管理、Hooks 與自動化、模型使用策略、Token 成本優化、記憶與知識管理、Plugin/MCP 整合等，持續累積形成社群最佳實踐知識庫。

工具目錄（活躍度 / 採用狀態）見 [[topics/community-tech-tools]]。概念辯論、設計哲學與技術反思見 [[topics/community-tech-discussions]]。本頁模式萃取出的**宏觀趨勢 + 對現有設計的啟示**見 [[topics/community-pattern-trends]]（週更）。技術彙整已按月份分組，可由月份標題快速跳轉。

---

## 模式概覽

| 類別 | 代表技巧 | 成熟度 | 核心概念 |
|------|---------|--------|---------|
| **Multi-agent 架構** | Claude Squad、Speculative Parallelism、ccteams（套件化團隊配置） | ✅ 成熟 | orchestrator 分派 + 獨立 git worktree，防答案塌縮；ccteams 將驗證良好的 subagent 組合打包為可跨專案安裝的套件 |
| **Skills 設計** | 知識框架化、流程 skill 化、免 git 雲端硬碟分享（Sx 2.0） | ✅ 成熟 | description 自動觸發，將書籍/流程封裝為可複用 skill；Sx 2.0 將分享管道從 git 延伸至 Dropbox/Drive/iCloud，降低非技術團隊採用門檻 |
| **CLAUDE.md 管理** | 精簡規則策略、Self-improving Rules、防腐爛機制 | ✅ 成熟 | 以「規則」非「建議」撰寫，CI 攔截違反架構 PR |
| **Hooks 與自動化** | PostToolUse 稽核、Git Hooks 品質門、/goal Fire-and-Forget、deploy/migration 保護、Pre-completion Hook、Stop Hook 音效通知、Hooks 環境感知條件觸發（Adrafinil、氛圍狀態燈） | ✅ 成熟 | 強制執行 > CLAUDE.md 建議；Stop Hook 要求可驗證完成證明；CLAUDE.md 做偏好、Hooks 做邊界；Pre-completion Hook 防模糊結束；hooks 可感知 agent 活躍狀態驅動環境副作用（螢幕喚醒、實體燈光顏色） |
| **模型使用策略** | 分層模型（Sonnet + Opus）、多模型路由、Workweave Router、跨模態內容生成分工（InstantVideos）、Fable 5 Orchestrator-Executor（官方基準） | ⚡ 活躍 | 依任務複雜度路由，節省 60% 用量；Dragoman / Workweave 自動路由；嵌入 Claude Code / Codex / Cursor 的成本感知路由；InstantVideos 將分工路由思路延伸至內容生成（文字/圖像/影音各交專門模型）；Anthropic 官方基準證實 Fable 5 編排 + 便宜模型執行可達 46% 成本／96% 效能 |
| **Token / 成本優化** | MCP Code Execution、Token Bloat 對策、本機圖資料庫索引、穴居人模式（Caveman）企業採用 | ⚡ 活躍 | HTML→Markdown 降 80% token；快取不跨 session 是費用主因；極簡輸出模式（穴居人）企業採用獲 404 Media 確認，OpenAI、Nvidia、GitHub 開發者使用 |
| **記憶與知識管理** | ltm Core Memory Packet、本機圖資料庫、NanoBrain、OKF（物件鍵格式跨 session 記憶） | ⚡ 活躍 | 跨 session / 跨工具持久記憶；Leiden 圖譜減少 71 倍 token；OKF 標準化 agent 知識格式供團隊共用 |
| **Plugin / MCP 整合** | Plugin 反模式整理、Claude Code 作為 MCP 協調中心 | ⚡ 活躍 | 避免不必要 context 載入；Claude Code 主導 MCP 工具鏈協作 |
| **多代理 PR Review** | 4-agent Code Review、對抗性審查（計畫前 + 程式碼後）、Read-Only Reviewer | ⚡ 活躍 | 架構師代理協調 + 多廠商模型交叉審查；對抗性審查者讀取真實 codebase；read-only 權限約束維持對立性 |
| **Agent 版本控制** | ADR 注入、架構決策文件先於實作 | ⏳ 新興 | 決策文件先於實作，降低代理方向偏移風險 |
| **Context 管理** | Just-in-Time @-file、Repo-as-Memory、Context Rot 修復 | ⚡ 活躍 | 即時取回優於預先加載；repo 是記憶體、模型是工作者；避免 context 過早飽和 |
| **Agent 規模化** | 20-instance 崩潰分析、批量 OSS Bug 修復、Personas vs Tool-scoping、Mac Mini 自主 agent 部署、TBD（HN 4，agent-channels 跨 worktree 通訊）、live-log-viewer-next（平行 agent 即時對話地圖） | ⏳ 新興 | 超過 10 個並行 agent 需獨立 worktree + orchestrator 協調層；工具範圍限制比角色描述更可靠的邊界守護；無人監督排程任務已有完整 Mac Mini M4 方案；可觀測性層開始補足「多 agent 進度難追蹤」的協調盲點 |
| **安全架構** | CLAUDE.md for K8s、語意層漂移 CI 測試、Trent 內嵌評估 | ⏳ 新興 | AI 加速開發下的系統性安全防線；CI 攔截語義退化 |
| **跨環境 Agent 記憶** | Core Memory Packet、Agent 持續運作架構 | ⏳ 新興 | 跨編輯器 / 跨機器 / 跨模型的供應商中立記憶協定 |
| **架構邊界合約** | ANMA YAML contracts、Hooks 強制驗證、ISO 29148 規格驅動 | ⏳ 新興 | 用合約與工業標準定義 AI 不可越過的架構規則；使便宜模型也能守規 |
| **可靠性測試** | Caliper pass@k 指標測試 | ⏳ 新興 | 以多次執行的通過率衡量 skill 可靠性，而非單次成功；用 YAML 定義成功條件，本地輕量執行 |
| **Agent 預算控制** | AgentWatch runtime budget enforcement | ⏳ 新興 | 在 LLM 請求到達模型前攔截，強制執行費用或 token 上限；僅需修改 base URL，無 SDK 依賴 |
| **確定性 Agent 框架** | Agentic Orchestrator 混合架構 | ⏳ 新興 | 確定性框架（需求→研究→設計→規劃→實作→審查）+ 非確定性 agent；人工審查閘門在關鍵節點中斷；Go TUI 介面可視化長時間任務 |
| **Agent Loop 終止條件** | Loop exit condition 設計模式 | ⏳ 新興 | 「如何停下」比「如何跑起來」更難；設計顯式終止條件（計數器、狀態機、人工確認）防止無限循環 |
| **Agent 記憶保護** | 結構化 Markdown 編輯器取代 regex | ⏳ 新興 | agent 用 regex 修改記憶檔案易損壞結構；以結構化 AST 編輯器操作 Markdown，防止非預期覆寫 |
| **跨 Repo 依賴可視化** | Cross-repo blast radius 分析 | ⏳ 新興 | Claude Code 讀完整 clone、Cursor 讀相似度索引，兩者皆不看依賴圖；串接 cross-repo blast radius 分析以補盲點 |
| **MCP 長 Session 穩健化** | MCP server 失效模式防護 | ⏳ 新興 | 長 session 三大失效模式：連線中斷、工具超時、上下文失憶；對應策略：心跳檢查、超時重試、session 狀態快照 |
| **行動裝置遠端控制** | ccgram（Telegram）、Android Remote Control MCP、Shellular | ⏳ 新興 | 手機作為 agent 控制介面，透過 Telegram bot / MCP / 專屬 web-app 等不同傳輸層連線並操作本機執行中的 Claude Code / Codex session |

> 成熟度：✅ 成熟（社群廣泛實踐）/ ⚡ 活躍（持續演進中）/ ⏳ 新興（近期出現，尚在探索）

---

## 技術彙整

### 2026-07

#### Fable 5 Orchestrates, Cheap Models Execute：官方基準 46% 成本達 96% 效能的多模型工作流模式（2026-07-14）

- **核心模式：** Anthropic 官方（透過 ClaudeDevs 討論串）公布多模型工作流的第一方基準數據：由 Fable 5 負責任務協調（orchestrate）、便宜模型負責實際執行（execute）的分工架構，可在僅 46% 成本下達到 96% 的效能表現；此模式並非未來規劃，而是可直接在 Claude Code 中設定使用的現行做法
- **與既有模式的關係：** 與既有「模型使用策略」類別下社群自建的分層模型路由（Sonnet + Opus）、Workweave Router 同屬「依任務複雜度分流節省成本」思路，差異在於這是 Anthropic 官方發布的第一方基準數據，將社群長期實務直覺量化為具體數字（46% 成本／96% 效能），並明確定調為「編排者–執行者」（orchestrator-executor）角色分工架構，而非單純模型選型
- **來源：** 「Anthropic just benchmarked "Fable 5 orchestrates, cheap models execute": 96% of the performance at 46% of the cost. You can run this pattern in Claude Code today」— Reddit r/ClaudeAI（週熱門；轉述原始 ClaudeDevs 討論串發布的官方第一方數據，本頁未直接讀取 ClaudeDevs 原始貼文全文，細節數字待查證）
- **成熟度：** ⚡ 活躍（官方背書 + 量化基準數據，可直接複現於 Claude Code；今日首見，尚待後續社群跟進實測驗證）

#### 語音提示／語音輸出小趨勢觀察：Mr. Meeseeks 語音提示外掛（HN 130，本日最高分）與 aloud TTS 輸出工具並現（2026-07-14）

- **核心模式：** thephw/claude-meseeks 讓 Claude Code 在長對話準備結束話題時播放 Mr. Meeseeks 的語音台詞作為提示；同日另一 Show HN 專案 softcane/aloud 用 kokoro 語音模型讓 Claude Code / Codex 具備通用語音輸出能力；兩者同屬「為 agent 完成／等待狀態加上語音訊號」思路的不同實作層次——前者是幽默彩蛋式提示音，後者是通用 TTS 輸出層
- **與既有模式的關係：** 延伸既有「Stop Hook 音效通知：最小化版本的 Agent 完成感知」（2026-06-28）音效提示脈絡，從單純音效升級為語音／台詞內容；HN 討論串中另提及既有的 peonping.com 多聲音包方案，顯示「agent 狀態語音化」已累積至少三個獨立實作（peonping、Mr. Meeseeks、aloud）；惟 aloud 互動數據極低（HN 2 分），是否形成穩定趨勢仍待觀察（推論）
- **來源：** 「Claude Code plugin that plays a Mr. Meeseeks voice line whene Claude is waiting」— Hacker News（GitHub thephw/claude-meseeks，score 130，本日社群條目最高分）；「Show HN: Giving Claude Code and codex its voice using kokoro」— Hacker News（GitHub softcane/aloud，score 2）
- **成熟度：** ⏳ 新興（單日集中出現兩則相關工具，尚無跨專案採用數據，是否形成穩定模式待後續觀察）

#### Sx 2.0：透過 Dropbox / Google Drive / iCloud 免 git 分享 Claude/Codex Skill（2026-07-14）

- **核心模式：** Sx 2.0 讓非技術團隊透過既有雲端硬碟（Dropbox、Google Drive、iCloud 等）分享 Claude/Codex 的 skill vault，不需依賴 git 版控知識；2.0 版新增 Mac/Windows/Linux 原生 app 與 Skill Evals 擴充系統，vault 格式重構為可直接作為 Claude 或 Codex plugin 使用
- **與既有模式的關係：** 屬「Skills 設計模式」類別下新的**分享／分發**取向，與既有 ccteams（npm 套件化 subagent 團隊，2026-07-11）同屬「降低 skill/subagent 配置重複勞動」思路，差異在於 ccteams 面向技術團隊（npm 生態），Sx 2.0 面向非技術團隊（免 git、雲端硬碟同步）
- **來源：** 「Show HN: Sx 2.0 – Share AI skills with your team through a Dropbox folder」— Hacker News（score 39，達互動門檻對照表「中」門檻）
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
- **來源：** [Show HN: Devthropology – Better Insights for GitHub Repos](https://devthropology.com/demo)（Hacker News Show HN，34 分）
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

#### Agentic Orchestrator：確定性框架 + 非確定性 Agent 混合架構（2026-06-30）

- **核心模式：** DoorDash 開源的長時間 coding agent 編排 TUI（Go 語言），將 agent 工作流切分為確定性階段（需求釐清 → 研究 → 設計 → 多階段規劃 → 實作 → 審查），每個階段由人工審查閘門控制是否繼續；非確定性的 LLM 只在每個階段內部執行（[GitHub doordash-oss/agentic-orchestrator](https://github.com/doordash-oss/agentic-orchestrator)；HN Show HN score 13，06-30）
- **解決的問題：** 長時間 agent 任務缺乏可見性和可控性；agent 自主執行 8 小時的「黑盒感」讓工程師難以信任輸出——可視化各階段進度並在關鍵節點插入人工決策點，降低大型任務失控風險
- **設計亮點：** 明確分離「確定性工作流編排（框架）」與「非確定性 LLM 執行（agent）」——框架掌管任務順序與人工閘門，agent 掌管每個階段的具體執行；一個使用者報告 8 小時連續使用無問題
- **與既有模式的差異：** 既有 multi-agent 框架（Aharness、ANMA）著重 agent 間的協調與邊界合約；Agentic Orchestrator 著重「人機混合審查的 stage gate」——人類在框架中是一等公民而非觀察者
- **成熟度：** ⏳ 新興
- **訊號強度：** HN Show HN score 13，DoorDash 工程團隊出品，有完整 Go 實作

#### Loop Exit Condition：Agent 循環終止設計模式（2026-06-30）

- **核心模式：** 明確設計 agent loop 的終止條件——「如何停下」是長時間 agent 工作流中最容易被忽視、最難正確設計的部分；終止條件設計不良是 runaway agent 的主要根因（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ujqht2/running_claude_in_a_loop_is_the_easy_part_getting/)，06-30）
- **解決的問題：** 「跑起來容易，停下難」——社群普遍能讓 agent 進入循環，但終止邏輯複雜：成功條件、失敗條件、最大重試次數、人工介入觸發點，每一個設計錯誤都可能導致無限循環或過早終止
- **已知終止條件設計方向：**
  - 計數器：最大迴圈次數上限（防 runaway）
  - 狀態機：定義合法的終止狀態（success/failure/timeout）
  - 人工確認閘門：關鍵決策前要求人工確認
  - 自評估：agent 在每輪結束後評估「任務是否完成」（需防幻覺——agent 容易錯誤自評為完成）
- **與 AgentWatch 的關係：** AgentWatch 是預算層的強制截斷（runtime enforcement）；Loop exit condition 是業務邏輯層的合法終止設計——兩者互補，都是 runaway agent 防護的必要元件
- **成熟度：** ⏳ 新興（概念廣泛共識，但系統化最佳實踐尚未收斂）
- **訊號強度：** Reddit r/ClaudeAI 社群討論，無具體工具但有廣泛共鳴

#### 結構化 Markdown 編輯器：防止 Agent 記憶損壞的架構模式（2026-06-30）

- **核心模式：** agent 需要修改 Markdown 記憶檔案時，改用結構化編輯器（AST 層操作）取代 regex 字串替換；regex 在 Markdown 結構複雜時（嵌套清單、代碼塊、YAML front matter）容易造成非預期覆寫或格式損壞（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ujqbwy/my_agent_kept_destroying_its_own_memory_file_with/)；另提供 hosted 無本地磁碟版本，06-30）
- **解決的問題：** 開發者發現 agent 使用 regex 修改記憶檔案，在處理嵌套結構時反覆破壞檔案格式；損壞的記憶檔案導致後續 session 無法正確讀取跨 session 知識，造成 cascade failure
- **實作方向：** 使用 Markdown AST（如 remark/unified 生態）定位並修改特定節點，保留周圍結構；也可使用 section-level 操作（定位標題、替換整個 section 內容）取代字元層 regex
- **與既有記憶架構的關係：** OKF（物件鍵格式）著重記憶內容的格式標準化；此模式著重記憶操作的安全性——是記憶管理的防禦性基礎設施
- **成熟度：** ⏳ 新興
- **訊號強度：** Reddit r/ClaudeAI，開發者開源解決方案並提供 hosted 版本

#### Cross-repo Blast Radius 分析：補足 Claude Code 與 Cursor 的依賴圖盲點（2026-06-30）

- **核心模式：** Claude Code 讀取完整 clone、Cursor 讀取相似度索引，但兩者都無法看到跨 repo 的依賴圖（blast radius）；透過串接外部依賴圖工具，分析一個變更會影響多少下游 repo 或服務（[dev.to](https://dev.to/danielwe/claude-code-reads-your-clone-cursor-reads-similarity-neither-sees-the-graph-487i)，06-30）
- **解決的問題：** AI 編碼工具在單一 repo 內表現良好，但跨 repo 依賴可視性差——修改一個共用函式庫時，無法知道有哪些下游服務會受影響（blast radius 不透明）
- **實作方向：** 在 Claude Code session 開始前，先執行 blast radius 分析（如 `nx graph`、Gradle dependency tree、自建依賴圖），將結果注入 context；讓 agent 在執行前知道「修改這個函式會影響 N 個服務」
- **注意事項：** 依賴圖的維護成本高，需定期更新才能反映真實依賴狀態（推論）；此方案不改變 Claude Code 本身，是 pre-session context 注入策略
- **成熟度：** ⏳ 新興
- **訊號強度：** dev.to 文章，有具體技術分析，但無 HN/Reddit 討論驗證

#### MCP Server 長 Session 失效模式與穩健化策略（2026-06-30）

- **核心模式：** MCP server 在長時間 session 中有三大常見失效模式，各需對應穩健化策略（[dev.to](https://dev.to/ursula_harrell_32416a7c42/building-reliable-claude-code-workflows-with-mcp-servers-pon)，06-30）
- **三大失效模式：**
  - **連線中斷（Connection Drop）：** MCP server 在長 session 中無聲斷線，Claude Code 繼續呼叫已失效工具得到靜默失敗；對應：心跳檢查 + 自動重連
  - **工具超時（Tool Timeout）：** 慢速工具（如資料庫查詢、外部 API）在 agent loop 中累積延遲；對應：設定超時閾值 + 重試策略
  - **上下文失憶（Context Amnesia）：** 長 session 後 MCP server 的 stateful context 與 Claude 的理解出現分歧；對應：在關鍵節點快照 session 狀態，必要時重置 server
- **與既有 MCP 討論的差異：** 既有討論（MCP 成本結構、工具選擇混亂）著重「工具過多」的靜態問題；此模式著重「長時間運行」的動態穩定性問題——是 agent pipeline 生產化的必要考量
- **成熟度：** ⏳ 新興
- **訊號強度：** dev.to 文章，有系統性分析框架，尚無大規模社群驗證

#### AgentWatch：請求攔截層的 Runtime Budget Enforcement（2026-06-29）

- **核心模式：** 在 LLM 請求到達模型前攔截並強制執行預算限制（token 數或費用上限）；超過預算則拒絕請求或回傳錯誤，防止 runaway agent 持續消耗資源（[agent-watch.dev](https://agent-watch.dev/)；HN Show HN score 7）
- **實作方向：** 修改 base URL 指向 AgentWatch proxy；支援 OpenAI、Anthropic、Gemini API；無 SDK 依賴，不需修改應用程式碼；可設定每個 session 或全局的費用/token 上限
- **解決的問題：** Agent 失控（runaway）是多 agent 架構的已知風險——循環呼叫、錯誤重試、無終止條件均可導致費用暴增；此方案在請求層設置硬邊界，比應用層 guard 更可靠
- **與既有模式的差異：** 既有 budget 控制策略（Token 成本優化、模型路由）著重「用更少 token 完成任務」；AgentWatch 著重「超過上限直接截斷」——是防禦性邊界，不是優化策略
- **注意事項：** 截斷中途任務可能導致 partial state；需配合 checkpoint 機制設計才能安全使用（推論）；HN score 7，有公開網站，尚無社群大規模驗證
- **成熟度：** ⏳ 新興
- **訊號強度：** HN Show HN score 7，有公開網站

#### Caliper：pass@k 指標的 Skill 可靠性測試方法（2026-06-29）

- **核心模式：** 以 pass@k（執行 k 次，至少成功 1 次的比率）衡量 Claude Code / Codex skills 的可靠性，而非單次執行成功率；用 YAML 定義任務的成功條件，本地輕量執行（[GitHub](https://github.com/edonadei/caliper)；HN Show HN score 3）
- **實作方向：** 以 YAML 格式描述 skill 的輸入、預期輸出、成功判定條件；執行多次取通過率；pass@k 越高代表 skill 的可靠性越高
- **解決的問題：** 「跑一次成功 ≠ 可靠」——非確定性 LLM 輸出在生產環境需要統計意義上的可靠性評估，而非單次 demo
- **與既有模式的差異：** 既有測試模式（Judge Gate、語意漂移 CI）著重「正確性驗證」；pass@k 著重「穩定性分布」——後者更適合用來選擇 skill 設計方案
- **成熟度：** ⏳ 新興
- **訊號強度：** HN Show HN score 3，有公開 repo，概念清晰可直接採用

#### beads + Claude Code 兩層工作規劃架構（2026-06-29）

- **核心模式：** 以 beads（或類似高層規劃工具）進行任務分解和工作規劃，再搭配 Claude Code 執行具體開發工作；規劃層（人類或工具）處理「做什麼」，執行層（Claude Code）處理「怎麼做」（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uiri45/nice_workflow_in_claude_code/)）
- **解決的問題：** 直接讓 Claude Code 處理高層規劃，容易在方向性決策上偏移或遺漏邊界案例；分層後規劃層保持人類主導，執行層充分利用 Claude Code 的自動化能力
- **設計分層：** 與「任務開始前先 Interview」模式（2026-06-25）互補：beads 在外部規劃，Interview 模式在 session 內部澄清；beads 的外部規劃輸出可作為 Claude Code session 的高品質初始 context 注入
- **注意事項：** beads 工具本身的採用訊號有限；核心模式（規劃/執行分層）概念已在社群多處出現（/specs 目錄、Agentic 目錄結構等），beads 是此模式的一種實作選擇
- **成熟度：** ⏳ 新興（模式概念有效；具體工具組合待更多驗證）
- **來源：** [Reddit r/ClaudeAI 討論](https://www.reddit.com/r/ClaudeAI/comments/1uiri45/nice_workflow_in_claude_code/)

#### Agent Context 上限主動管理：56KB 問題與即時截斷策略（2026-06-29）

- **核心模式：** 主動為 agent 設定 context 讀取上限，避免「為回答單一問題讀取 56KB 文件」的低效行為；核心做法是在 task 設計時明確約束 agent 可讀取的最大 context 量（[dev.to](https://dev.to/enjoy_kumawat/my-ai-agent-read-56-kb-to-answer-one-question-i-made-it-stop-34g5)）
- **實作方向：** 在工具設計或 hook 層設定讀取上限（行數、字元數）；搭配索引 / 摘要層讓 agent 先查索引再決定是否全讀；明確在 CLAUDE.md 或 skill 描述中指定「不需要讀取整個檔案」的場景
- **解決的問題：** Agent 為確保「完整性」傾向讀取整個文件，但大量場景只需讀取相關片段；過度讀取既消耗 token 又降低 context 訊噪比
- **與既有模式的差異：** Just-in-Time @-file（2026-06-26）著重「何時取回」；本模式著重「取回多少」——兩者結合形成完整的 context 精準注入策略
- **成熟度：** ⏳ 新興

#### Hooks 環境感知條件觸發：依 Agent 活躍狀態驅動系統副作用（2026-06-28）

- **核心模式：** 用 Claude Code hooks 偵測 agent 是否正在執行，依此決定是否觸發系統層副作用（如 `pmset disablesleep 1`）；典型應用：Adrafinil 解決 Mac 半開蓋走動時 agent 被睡眠中斷的問題，只在 agent 工作時保活，完成後自動釋放（[GitHub](https://github.com/kageroumado/adrafinil)；HN score 113）
- **與既有模式的差異：** 既有 hooks 模式（PostToolUse 稽核、Pre-completion Hook）以 hooks 執行業務邏輯（規則驗證、輸出格式）；此模式以 hooks 回讀 agent 狀態來決定副作用是否觸發——從「規則執行觸發器」升格為「環境感知條件觸發器」
- **應用延伸（推論）：** 相同模式可延伸至其他環境感知場景：依 agent 活躍狀態控制 Slack DND、資源分配、冷卻提醒；任何「只在 agent 工作時才需要的副作用」均可套用
- **成熟度：** ⚡ 活躍（HN 113 顯示真實痛點，解法可直接使用）
- **訊號強度：** HN Show HN score 113，有公開 repo，可直接複製

#### OKF：物件鍵格式跨 Session Agent 記憶（2026-06-28）

- **核心模式：** 以「物件鍵格式（Object Key Format，OKF）」標準化 Claude Code agent 在 session 之間傳遞的知識結構；讓 agent 產生的記憶片段可攜、可讀，適合團隊共用同一個 Claude Code 工作流（[dev.to](https://dev.to/scaccogatto/okf-for-claude-code-structured-portable-memory-your-agent-and-team-can-read-4ocn)，06-28）
- **與既有模式的差異：** 既有跨 session 記憶方案（ltm Core Memory Packet、本機圖資料庫）偏向工具驅動；OKF 是格式標準（純 Markdown 可讀），不依賴特定工具實作，偏向「規約」而非「框架」
- **適用場景：** 多人共用 Claude Code 工作流、需要 agent 知識在 session 間保持一致性的長期專案
- **注意事項：** 文章為個人分享，無 HN 訊號，尚待社群驗證複現性
- **成熟度：** ⏳ 新興

#### Stop Hook 音效通知：最小化版本的 Agent 完成感知（2026-06-28）

- **核心模式：** 透過 Claude Code `stop` hook 在 agent 完成時觸發系統音效，讓開發者立即得知可繼續操作，無需輪詢終端輸出；是 hooks 最低門檻的實用應用案例（[dev.to](https://dev.to/anand_rathnas_d5b608cc3de/i-made-claude-code-ding-when-its-done-and-it-changed-my-workflow-5e35)，06-27）
- **實作方向：** 在 Claude Code 設定中加入 `stop` hook，呼叫 `afplay` / `paplay` 播放提示音；可擴展為系統通知（macOS `osascript`、Linux `notify-send`）
- **解決的問題：** agent 執行時開發者切換至其他工作，需要知道何時返回；音效比輪詢終端更低認知成本
- **設計分層：** 與 Adrafinil 的「環境感知條件觸發」構成一組：Adrafinil 是 agent 開始時的環境感知，stop hook 音效是 agent 結束時的環境通知
- **成熟度：** ⚡ 活躍（原理簡單，可即時複製）

#### ccgram：透過 Telegram 遠端控制 Claude Code Sessions（2026-06-28）

- **核心模式：** 透過 tmux + ccgram 讓 Claude Code sessions 在 Telegram 可視、可控；sessions 繼續在本地終端機真實執行，Telegram 作為遠端控制介面；v4.3.0 更新（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhogpe/ccgram_v430_control_claude_code_and_shell_from/)，06-27）
- **適用場景：** 離開電腦時監控長時間 agent 任務、行動裝置臨時介入正在執行的 session
- **與既有模式的差異：** 既有遠端控制方案（iOS app 接力）依賴官方 claude.ai 介面；ccgram 走 Telegram，適合已有 Telegram bot 生態的用戶，且可同時控制 Claude Code + 一般 shell 工作階段
- **注意事項：** Reddit 來源，無 HN score；需要 Telegram bot 配置，安全邊界需自行評估
- **成熟度：** ⏳ 新興

#### Workweave Router：成本感知嵌入式模型路由（2026-06-27）

- **核心模式：** 在 Claude Code / Codex / Cursor 工作流中嵌入智能路由層，依請求難度自動選擇最佳模型；主要動機是解決 Opus 4.7 成本暴增問題，透過自動降階讓簡單任務走低成本模型（[GitHub](https://github.com/workweave/router)；HN score 181）
- **訊號強度：** HN 181 為本週社群工具中最高分，有公開 repo，採用訊號明確
- **與既有模式的差異：** Dragoman（2026-05-13）採用顯式規則路由；Workweave 主打隱式難度評估，無需手動設定路由規則；多模型路由從「手動策略」走向「自動決策」
- **注意事項：** 路由判斷依據未公開技術細節；「最佳模型」的定義由路由器自身決定，存在黑盒風險（推論）

#### Mac Mini M4 無人監督自主 Agent 完整部署方案（2026-06-27）

- **核心模式：** 將 Claude Code 配置為全自主 agent 在 Mac Mini M4 上執行無人監督排程任務，涵蓋事件觸發、自動 commit、完整閉環（[dev.to](https://dev.to/clawlabs/how-to-run-claude-code-as-an-autonomous-agent-on-a-mac-mini-3ld1)）
- **與既有模式的差異：** 既有「Agent 持續運作架構」（2026-05-03）偏向架構設計原則；此方案提供 Mac Mini M4 的具體配置步驟，是首個以消費級硬體為目標的完整無人監督部署指南
- **適用場景：** 個人或小型團隊的夜間自動化任務、CI 替代方案、定期維護工作流

#### Read-Only Reviewer Agent：無編輯權限的對立審查者（2026-06-26）

- **核心模式：** 主 agent 負責撰寫程式碼，reviewer agent 只能讀取、不能編輯；「無編輯權限」是設計的核心約束，保持審查者的對立性，能捕捉主 agent 放過的問題
- **實作方向：**
  - 主 agent 完成一個任務單元後，呼叫 reviewer agent 讀取變更
  - reviewer agent 不持有任何編輯工具（write/edit），強制其只輸出審查意見
  - 主 agent 收到意見後決定是否採納，維持決策責任歸屬清晰
- **解決的問題：** 若 reviewer 也能編輯，會傾向直接修改而非提供批評意見；權限約束使「對立性」可持續，避免 reviewer 降格為第二個 implementer
- **設計分層：** 此模式是「對抗性審查設計（做法 A）」的權限約束強化版；前者著重審查者讀取真實 codebase，本模式著重工具範圍限制確保對立性可持續
- **成熟度：** ⏳ 新興
- **來源：** ["Read-Only Reviewer Agents Catch What Your Main Agent Waves Through"](https://dev.to/greymothjp/read-only-reviewer-agents-catch-what-your-main-agent-waves-through-3ggc)（dev.to，06-26）
- **相關工具（HN 4）：** Verity（verity.md）——在 agent run 後自動執行審查並修復不安全代碼，定位為「自愈層」而非「審查層」；HN score 4，修復準確率無獨立驗證，附記待觀察。

#### Repo-as-Memory / Stop Using the Model as Your Memory（2026-06-26）

- **核心模式：** 框架提出「模型不保存狀態，repo 才是記憶體；模型是工作者（worker）」——已確定的決策應外化到 repo（CLAUDE.md、spec 檔、ADR），而非依賴模型在對話中記住
- **實作方向：**
  - 凡「已決定的事情」（架構選擇、技術約束、命名規則）立即寫入 repo 的指定檔案
  - 不依賴模型跨 session 記憶既有決策；每個 session 從 repo 注入確定性 context
  - 將此框架視為 Claude Code 許多架構決策的底層推論依據
- **解決的問題：** 依賴模型記住已決定的事情，會導致模型在後續 session 重做已解決問題、忽略既有約束；context 腐蝕的根源之一
- **設計分層（推論）：** 此框架統一解釋了 CLAUDE.md、`/specs` 目錄、ADR 等多種已有模式的共同動機——「repo 即記憶體」是這些實踐背後的底層哲學
- **成熟度：** ⚡ 活躍
- **來源：** ["Your Repo Is the Memory, Your Model Is the Worker"](https://dev.to/greymothjp/your-repo-is-the-memory-your-model-is-the-worker-3e09)（dev.to，06-26）；["Stop Using the Model as Your Memory"](https://dev.to/greymothjp/stop-using-the-model-as-your-memory-4nbi)（dev.to，06-26）

#### Just-in-Time @-file Retrieval：避免預先加載所有檔案（2026-06-26）

- **核心模式（反模式揭露）：** 預先 @-mention 所有「可能」用到的檔案是反模式，導致 session 上下文過重退化（context rot）；正確做法是「即時取回（just-in-time retrieval）」——只在需要時才取回相關檔案
- **實作方向：**
  - 不要在 session 開始時一次性載入所有可能相關的檔案
  - 讓 Claude 在執行任務過程中根據需要主動請求或取回檔案
  - 搭配 CLAUDE.md 描述 codebase 結構（目錄索引），而非直接注入所有原始碼
- **解決的問題：** 預先加載造成 context window 過早飽和，早期注入的約束被後來的內容稀釋；使用者分享切換後顯著改善
- **成熟度：** ⚡ 活躍
- **來源：** [Reddit r/ClaudeAI 討論](https://www.reddit.com/r/ClaudeAI/comments/1ug70ov/preloading_files_to_be_safe_was_quietly_rotting/)（06-26）

#### Personas vs Tool-Scoping：Multi-Agent 設計選擇（2026-06-26）

- **核心模式：** Multi-agent 設計的兩條路線——角色導向（Personas：CEO / EM / QA 分工）vs 工具範圍限制（Tool-scoping：每個 agent 只掛載其職責所需的工具）；作者選擇後者
- **實作方向（工具範圍限制）：**
  - 每個 agent 的工具清單對應其實際責任範圍（reviewer 不掛 write 工具、部署 agent 不掛 codebase 讀取工具）
  - 工具範圍限制比角色描述更可靠：模型可以忽略「你是 QA」的身份描述，但無法呼叫未掛載的工具
  - 角色（persona）可作為輔助提示，但邊界守護應依賴工具範圍，不是角色描述
- **設計分層：** 此選擇與「Read-Only Reviewer Agent」模式形成互補——前者是工具範圍限制的具體應用，本模式提供設計框架層的對比分析
- **成熟度：** ⏳ 新興
- **來源：** ["Personas vs. Tool-scoping: Where I Landed Differently from gstack"](https://dev.to/greymothjp/personas-vs-tool-scoping-where-i-landed-differently-from-gstack-gld)（dev.to，06-26）

#### 批量 OSS Bug 修復：識別相同形狀的 Bug（2026-06-26）

- **核心模式：** 一天內向多個知名開源專案（zod、NestJS、Fastify、Scrapy、Pygments 等）提交約 28 個 PR，核心技術是「識別相同形狀的 bug」後批量複製修復策略
- **實作方向：**
  - 先識別一類 bug 的「形狀」（觸發條件、影響範圍、修復模式）
  - 使用 Claude Code 跨 repo 套用相同的修復邏輯，一天內完成大量 PR 提交
  - 適合於標準化的程式庫缺陷（型別處理、邊界條件、錯誤處理路徑等）
- **解決的問題：** 開源貢獻的高摩擦成本（理解 codebase、修復、測試、提交）可透過「批量化相同形狀修復」大幅攤薄
- **成熟度：** ⏳ 新興
- **來源：** ["I Found 30 Mergeable OSS Bugs in a Day: They Were All the Same Shape"](https://dev.to/greymothjp/i-found-30-mergeable-oss-bugs-in-a-day-they-were-all-the-same-shape-5c86)（dev.to，06-26）

#### 20 個 Claude Code 並行 Instance 的崩潰原因與對策（2026-06-26）

- **核心模式：** 從 4 個並行 agent 擴展到 20 個時的崩潰分析；主要崩潰原因包括：共享資源競爭（git lock、資料庫連線）、context 洩漏至鄰近 agent、缺乏協調層的任務分派
- **實作方向：**
  - 每個 agent 分配獨立 git worktree，完全隔離檔案系統操作
  - 設計明確的 orchestrator 層負責任務分派與結果彙整，避免 agent 間直接通訊
  - 從小規模（4 個）漸進擴展，每次倍增時測試協調機制是否持續有效
- **成熟度：** ⏳ 新興
- **來源：** ["Why 20 Claude Code Instances Break Down and What to Do"](https://dev.to/jcamarate/why-20-claude-code-instances-break-down-and-what-to-do-2i5j)（dev.to，06-26）

#### 任務開始前先 Interview：讓 Claude Code 問問題再動手（2026-06-25）

- **核心模式：** 在正式開始任何 agentic coding 任務前，強制 Claude Code 先向使用者提問澄清需求，確認方向後才開始執行；避免「方向錯誤」這個 agentic coding 中最昂貴的失誤
- **實作方向：**
  - 在 CLAUDE.md 或任務 prompt 的開頭指示 Claude：「在開始任何實作之前，先問我 3–5 個關鍵問題」
  - 問題應覆蓋：目標邊界、技術偏好、現有限制、成功條件
  - 收到完整回答後再啟動 agentic 工作流
- **解決的問題：** Agentic coding 的最大成本不是 token，而是方向錯誤後的回滾重來；早期澄清可大幅縮短無效執行時間
- **設計分層（推論）：** 此模式是「規格驅動開發」的最小化實作——對話式 spec 收集取代書面文件，適合輕量任務
  - **進階規格格式（無 HN 分數）：** ISO/IEC/IEEE 29148 SRS 格式（The system shall [action] [condition] [measurable criteria]）可作為 Interview 收集需求後的書面化框架；適合大型任務，對非技術 PM 門檻較高（Reddit r/ClaudeAI，06-22）。
- **注意事項：** 過度提問會拖慢節奏；適用於需求模糊或跨多檔案變更的任務，簡單單一任務不必強制執行
- **訊號：** 單一經驗談，無機制驗證，待社群佐證
- **來源：** ["I Made Claude Code Interview Me Before Writing Code"](https://dev.to/florian_ilia/i-made-claude-code-interview-me-before-it-writes-any-code-2p7f)（dev.to，Florian Ilia，06-25）

#### 對抗性審查設計：計畫階段 vs 程式碼完成後（兩種做法對照）（2026-05-12 / 2026-06-25）

- **共同目標：** 引入對抗性角色，打破 LLM 的樂觀偏差（affirmative bias）——Claude 面對模糊規格時傾向以最少衝突的方式解讀任務，導致靜默失敗（silent failure）；單一 Claude 實例自審自批無法有效揭露問題
- **做法 A — 計畫前審查（2026-06-25，Adversarial Claude Reviewer）：**
  - Agent A（實作者）提出實作計畫
  - Agent B（審查者）實際讀取真實 codebase，針對計畫提出具體反例、邊界案例與風險點（而非基於抽象描述做樂觀假設）
  - 計畫須通過審查者的挑戰後，實作者才開始執行；可設定輪數（如 2 輪）後由 orchestrator 裁定
  - 與 Aharness（FSM 強制流程）結合可使對抗輪次強制執行
  - **來源：** ["I Built a Multi-agent Loop Where an Adversarial Claude Reviewer Reads Your Actual Codebase Before Approving Plans"](https://dev.to/execute25/i-built-a-multi-agent-loop-where-an-adversarial-claude-reviewer-reads-your-actual-codebase-before-2d8n)（dev.to，06-24）
- **做法 B — 程式碼後審查（2026-05-12）：**
  - 第一個 Claude 負責起草任務 kickoff 文件；第二個 Claude 扮演批評者，事先挑毛病（指出可能失敗的場景、模糊假設、潛在依賴衝突）
  - 執行前先讓兩個 Claude 達成共識；作者追蹤六個生產專案後報告此工作流顯著降低執行後的靜默失敗率，特別是在長時間任務和規格不完整的場景
  - 與 agent-order（Codex + Claude 各自獨立寫 PRD 再互相批判）類似概念，但此做法聚焦同一模型的雙實例角色分工（起草者 vs 批評者）
- **比較：** 做法 A 防止問題在設計階段產生（審查者讀取真實 codebase 是關鍵差異）；做法 B 在計畫草稿階段捕捉模糊假設；兩者可串接使用——先以做法 B 收斂規格再以做法 A 驗證實作計畫
- **共同注意事項：** 審查者提示詞設計是核心難點；需校準「挑戰強度」避免過度拒絕所有計畫

#### Pre-completion Hook：防止 Claude Code 以模糊語句提前結束任務（2026-06-25）

- **核心模式：** 設置 pre-completion hook，偵測 Claude Code 輸出中的模糊結束語句（如「say the word」、「separate fix」、「if it ever bites」），攔截並要求真正完成任務後再結束
- **量化數據：** 作者報告每日實際觸發數十次，顯示此類模糊結束行為在日常使用中頻率極高
- **實作方向：**
  - 設定 Stop Hook（或 pre-completion hook）掃描最後一輪 Claude 輸出
  - 維護模糊結束語句的 pattern list（「if this ever becomes a problem」、「a separate task」、「let me know if」等）
  - 偵測到 pattern 時，返回 non-zero exit code，強制 Claude 繼續執行而非結束
  - 可搭配 Stop Hook 要求可驗證完成證明（測試通過、檔案存在等）
- **解決的問題：** Claude Code 的「提前結束」anti-pattern——用「讓我知道如果…」代替真正解決問題；在長任務中尤其常見，因為 Claude 在接近 context limit 時傾向「延後處理」
- **與既有模式的關係：** 呼應「Hooks 強制執行取代 CLAUDE.md 規則」的核心原則；是 Stop Hook 強制完成驗證的具體實作案例
- **注意事項：** 需持續維護 pattern list；部分「延後」可能確實合理（真正範疇外的問題），需設計豁免機制
- **來源：** ["I Made a Claude Code Hook That Ensures the Whole Task Is Completed"](https://www.reddit.com/r/ClaudeAI/comments/1uf9ubb/i_made_a_claude_code_hook_that_ensures_the_whole/)（Reddit r/ClaudeAI，06-25）

#### Repo 慣例注入 Plugin：讓 Claude Code 在編輯前自動了解 codebase 風格（2026-06-25）

- **核心模式：** Plugin 靜態分析 repo，萃取 coding convention（import 庫選擇、命名風格、檔案結構），並在每次編輯操作前自動注入相關 context，讓 Claude Code 從「陌生」變「熟悉」
- **支援語言：** TypeScript、Ruby、Python（已確認）
- **實作方向：**
  - Plugin 分析 repo 現有程式碼，提取一致性規則（例如：此 repo 使用 `axios` 而非 `fetch`；目錄結構模式）
  - 在 Claude Code 每次 Edit/Write 工具呼叫前，注入對應的 context snippet
  - 可設定「慣例置信度閾值」，只注入有足夠樣本支撐的規則
- **解決的問題：** Claude Code 在不熟悉的 codebase 中常選錯 library、命名不一致、忽略既有模式；CLAUDE.md 手動維護負擔高且容易過時；此 plugin 讓慣例提取自動化
- **與既有模式的關係：** 補充「Plugin / MCP 整合」類別，是 CLAUDE.md 管理的自動化替代方案；與「Repo-context injection」思路一致，但更細粒度
- **注意事項：** 靜態分析可能誤判過渡期程式碼（既有程式碼中的 legacy 模式）；注入過多 context 反而增加 token 成本
- **來源：** ["Made a Claude Code Plugin That Learns Your Repo's Coding Conventions"](https://www.reddit.com/r/ClaudeAI/comments/1uf9u9d/made_a_claude_code_plugin_that_learns_your_repos/)（Reddit r/ClaudeAI，06-25）

#### Multi-model Pipeline：Claude + Codex + ChatGPT 三角色明確分工（2026-06-25）

- **核心模式：** 三模型各司其職：Claude Code 負責架構規劃與複雜推理；Codex 自主建功能（autonomous feature building）；ChatGPT 處理快速網路查詢（quick web lookup）；模型間有明確交接協定
- **實作方向：**
  - 定義每個模型的「職責範圍」與「移交條件」（handoff trigger）
  - Claude Code 作為 orchestrator，決定哪些子任務交給 Codex 或 ChatGPT
  - 交接時傳遞結構化的任務摘要（非完整 context），控制 token 成本
  - 建立統一的輸出格式，讓各模型產出可直接被下游消費
- **解決的問題：** 單一模型在所有任務上均衡表現的假設失效；不同模型在不同任務上有能力差異，混用可提升整體效能並降低成本
- **與既有模式的關係：** 延伸「多 LLM 協作架構哲學」（270+ 分歧日誌）與「cc-fleet orchestrator 模式」；本案例提供三模型的具體角色定義，比既有討論更具操作性
- **注意事項：** 多模型 pipeline 的測試與除錯複雜度顯著高於單模型；跨廠商模型的 prompt 格式差異需要逐一適配；成本追蹤需跨平台整合
- **來源：** ["I Run Claude, Codex, and ChatGPT in a Single Pipeline"](https://www.reddit.com/r/ClaudeAI/comments/1uf9n1r/i_run_claude_codex_and_chatgpt_in_a_single/)（Reddit r/ClaudeAI，06-25）

#### Multi-agent 工作流轉型指南：從「單一提示反覆法」到真正並行工作流（2026-06-24）

- **核心模式：** 多 agent 並行工作的根本前提是每個 agent 擁有獨立的工作空間（worktree 或容器），否則代理間互相覆蓋導致工作流崩潰
- **實作方向：**
  - 為每個並行 agent 分配獨立 git worktree 或容器，避免共享工作目錄
  - 從「單一提示 → 等待 → 調整」的線性迴圈，重構為「任務分解 → 並行派發 → 彙整驗證」的多 agent 流程
  - 任務邊界定義先於 agent 派發：各 agent 的輸入/輸出契約需明確，避免介面漂移
- **解決的問題：** 「用 AI 當 autocomplete」的舊範式在複雜任務中的瓶頸；AI agent 排隊等待造成的效能損耗
- **補充發現（Vibe coding under constraint）：** 在 Lean 4 嚴格型別系統下進行 vibe coding 的實測顯示，AI 的主要盲點是資源限制（記憶體、檔案描述符），而非邏輯錯誤——型別系統的強制約束反而填補了 AI 的邏輯漏洞
- **注意事項：** 工作空間隔離帶來額外的協調成本；需設計跨 agent 的結果彙整機制
- **來源：** ["Stop Using AI Like Autocomplete: A Developer's Guide to Multi-Agent Workflows"](https://dev.to/harshdeepsingh13/stop-using-ai-like-autocomplete-a-developers-guide-to-multi-agent-workflows-c1k)（dev.to）；["Want AI to Work in Parallel? First Give Each One Its Own Workspace"](https://dev.to/kanfu-panda/want-ai-to-work-in-parallel-first-give-each-one-its-own-workspace-40ch)（dev.to）；["Vibe Coding under Constraint"](https://ngrislain.github.io/projects/2026-6-22-vibe-under-constraint/)（HN）

#### Aharness：有限狀態機強制 Agent 工作流狀態轉換（2026-06-23）

- **核心模式：** 以有限狀態機（FSM）定義 AI agent 工作流，強制狀態轉換路徑，防止 process drift；agent 只能依照預定義的狀態圖移動，不可跳過或自行繞過中間狀態
- **實作方向：**
  - 以 TypeScript 定義狀態節點、轉換條件與觸發動作
  - 每個狀態對應明確的 AI agent 動作集合，狀態之外的動作被拒絕
  - 轉換條件可設為同步驗證（確認前一步驟完成）或非同步事件驅動
- **解決的問題：** AI agent 在多步驟工作流中「漂移」——跳步、重複、或在無明確終止條件時無限循環；長 session 中 agent 逐漸偏離初始設計路徑
- **與既有模式的關係：** 與 ANMA 架構邊界合約互補——ANMA 約束代碼生成邊界，Aharness 約束執行流程邊界；比 Loop Engineering 哲學更進一步，從「設計 loop」進化到「強制 loop 路徑」
- **注意事項：** HN score 4，社群曝光度早期；FSM 定義本身需維護成本；過度複雜的狀態圖可能成為新型設定負債**待觀察（2026-06-28）：** HN 4，FSM 概念有差異化但社群驗證度低，2026-09-26 前無後續跟進將縮減為附記。
- **來源：** Aharness（github.com/Alfredvc/aharness，HN score 4，06-23）

#### Compact Memory：解決 AI Agent O(N²) Context Token 浪費（2026-06-23）

- **核心模式：** 以「緊湊記憶（compact memory）」取代每輪重送完整 transcript 的傳統做法；只保留當前任務所需的語意摘要，剔除冗餘歷史，將多輪 agent 的額外 context token 消耗從 O(N²) 降至接近 O(N)
- **量化數據：** dev.to 基準測試：多數 AI agent 每輪重送完整 transcript，在多輪任務造成 62.8%–85.9% 額外 context token；compact memory 方案可顯著削減此開銷（附可執行 benchmark）
- **實作方向：**
  - 每輪 agent 行動後，提取並壓縮關鍵狀態（已完成步驟、待辦項目、關鍵決策）為摘要
  - 下一輪以摘要取代完整歷史作為 context 輸入
  - 保留「最近 N 輪」原始內容以維持短期連貫性，更早的歷史則壓縮
- **解決的問題：** 傳統 agent loop 設計將全量 transcript 傳遞，隨輪數增加 token 成本呈平方增長；大型多輪任務中成本不可控
- **與既有模式的關係：** 呼應 Context Rot 修復五法中的「壓縮歷史」策略；比 /compact 指令更系統化，可程式化控制壓縮時機與粒度
- **注意事項：** 摘要過於激進可能造成語意失真，需設計摘要品質驗證機制；benchmark 為社群個人測試，大規模驗證待確認
- **來源：** "The Hidden O(N²) Tax in AI Agent Loops: Measured with a Benchmark You Can Run"（dev.to/saihmadmin，06-23）

#### Hooks 強制執行取代 CLAUDE.md 規則：從建議層到強制層（2026-06-23）

- **核心模式：** 將「必須執行」的規則從 CLAUDE.md 文字建議層，遷移至 hooks 程序強制層；CLAUDE.md 保留偏好、風格與上下文描述，hooks 接管不可違背的操作邊界
- **實作方向：**
  - 識別 CLAUDE.md 中哪些規則是「LLM 偶爾遵守」（適合保留在 CLAUDE.md），哪些是「必須 100% 執行」（遷移至 hooks）
  - 具體 hooks 遷移案例：
    - deploy 腳本保護：PreToolUse hook 攔截部署命令
    - migration 資料夾防寫：文件系統操作前驗證路徑
    - formatter 強制：PostToolUse hook 在代碼寫入後自動執行
  - 使用 hook exit code 精細控制：Block（拒絕）/ Modify（修改後放行）/ Allow（放行）
- **解決的問題：** CLAUDE.md 規則的機率性遵守；規則越多、遵守率越低的「規則熵增」問題（參考 CLAUDE.md 精簡 296→142 行品質反升實證）
- **量化佐證：** ANMA 使用 hooks + contracts 達到 0/20 架構違規（vs 無約束時 13/19 違規）
- **設計分層（推論）：** CLAUDE.md = 知識與偏好（LLM 自主判斷）；Hooks = 邊界強制（程序保證）
- **來源：** "I stopped writing rules in CLAUDE.md and started writing hooks"（Reddit r/ClaudeAI，06-22）；ANMA（github.com/anma-labs/anma，HN score 3，06-22）

#### ANMA 架構邊界合約：讓便宜模型也能守規的強制機制（2026-06-22）

- **核心模式：** 以 YAML 合約（contracts）明確定義架構邊界，搭配 CLAUDE.md 與 Hooks 強制驗證；使 Haiku 4.5 等低成本模型在嚴格規則下也能正確運作，無需昂貴旗艦模型
- **實作方向：**
  - 在 `.anma/contracts/` 下定義 YAML 格式的架構規則（如「禁止直接呼叫資料庫、必須透過 Repository 層」）
  - 將合約規則注入 CLAUDE.md，使 AI 知曉邊界
  - 以 Pre-tool Hook 或 PostToolUse Hook 攔截違規行為，阻止代碼寫入
- **量化數據：** 無 ANMA 時 13/19 測試案例違反架構規則；有 ANMA 後 0/20 違規（來源測試）
- **解決的問題：** AI coding agent 在追求速度時系統性地繞過架構約束；CLAUDE.md 建議層無法阻止 agent 的快捷路徑行為
- **適用場景：** 有明確分層架構（Clean Architecture、DDD）的企業級專案；需要讓成本較低的模型參與生產代碼生成的場景
- **注意事項：** HN score 3，社群接受度尚早期；YAML 合約需與實際架構同步維護，否則成為新型設定負債
- **來源：** Show HN: ANMA, boundary contracts for cheaper AI coding agents（github.com/anma-labs/anma，HN score 3，06-22）
- **相關視角（HN 2）：** "I Built an MCP Server in 200 Lines of Go"（medium.com/dev-genius）——將 MCP endpoint 視為 AI 時代的 API contract，200 行 Go 示範最小實作；核心「合約優先」概念已由 ANMA 覆蓋。

#### 平行 Agent 模式：串行 vs 並行工作流效能差距（2026-06-21）

- **核心模式：** 將 agent 工作流從串行（一次做一件事）重構為並行（同時執行多個獨立子任務），可顯著提升整體吞吐量並縮短等待時間
- **實作方向：**
  - 識別任務相依圖（DAG），找出可平行執行的分支（如：同時搜尋多個資料來源、同時執行多份測試）
  - 使用 Sub-agent 或 Multi-agent 架構分派平行工作，各 agent 擁有獨立 context 避免干擾
  - Orchestrator agent 負責合併各子 agent 結果，並處理衝突與整合邏輯
- **解決的問題：** LLM 在串行工作流中的「等待」成本高昂——一個 agent 等待 API 回應或 IO 操作時，整個流程停滯；並行化可將等待時間轉為有效工作
- **適用場景：** 多資料來源研究任務、並行測試執行、獨立模組同步開發；不適合強相依的線性任務（後一步需要前一步輸出）
- **注意事項：** 並行 sub-agent 各自消耗 token；需估算並行成本是否優於串行節省的時間；cc-fleet 模式（廉價模型執行、Opus 設計）可降低並行成本
- **來源：** dev.to/kanfu-panda（2026-06-21）；cc-fleet（HN score 3）

#### Agent Loop 事件驅動：以觸發條件取代 sleep 輪詢（2026-06-21）

- **核心模式：** Agent loop 不應無條件 sleep 等待，而應改用事件驅動（event-driven）設計——只在有實際工作時才喚醒 agent，避免 5 分鐘以上的定期 sleep 帶來的 token 浪費與 context 過期問題
- **實作方向：**
  - 以佇列（queue）、webhook、檔案監聽或 diff 偵測作為喚醒條件，取代 `sleep(300)`
  - 若條件不成立，agent 直接退出或等待訊號，不進入 Claude 呼叫
  - 搭配 Stop Hook 設計明確的完成條件，防止 loop 無限運行
- **解決的問題：** `sleep 5 分鐘` 後喚醒仍需重建 context，且消耗 token 確認「是否有工作」；長期 idle 的 agent 累積大量「確認無工作」的 token 費用
- **適用場景：** PR review bot、CI/CD 監聽型 agent、定時輪詢類自動化任務；不適合需即時互動的對話型 session
- **與既有模式的關係：** 延伸自 Loop Engineering 模式（2026-06-19），強調「觸發條件設計」是 loop 品質的關鍵
- **來源：** dev.to/mjmirza "Stop Sleeping Your Agent Loop"（2026-06-21）

#### MCP Server 信任邊界審查：連接 MCP 即擴大攻擊面（2026-06-21）

- **核心模式：** 連接 MCP Server 給 agent 賦予「手」的同時，也給陌生人開了一扇門；每個 MCP 連接都需要明確的信任評估，而非預設信任
- **實作方向：**
  - 最小掛載原則：只掛載當前任務需要的 MCP，任務結束後移除
  - 審查 MCP Server 來源：優先使用官方或有公開稽核的 server；自建 server 需限制執行範圍
  - 隔離敏感操作：涉及檔案系統、網路請求、程式碼執行的 MCP，需明確限制 agent 可觸發的操作範圍
  - 搭配 Pre-tool Hook 驗證：在 MCP 工具呼叫前執行安全檢查（參考 Hooks 強制執行機制模式）
- **解決的問題：** MCP 連接帶來的攻擊面包括：惡意 MCP server 注入指令、MCP tool 被提示注入利用（如 Agentjacking/Sentry DSN 攻擊向量）、意外觸發高風險操作
- **適用場景：** 所有使用 MCP 工具的 Claude Code 工作流，尤其是有網路請求或系統寫入權限的情境
- **注意事項：** MCP context bloat（9 個 server = 38k token 冷啟動）是效能問題；信任邊界是安全問題——兩者都要分別處理
- **來源：** dev.to/rapls "Connecting an MCP server gives your agent hands..."（2026-06-21）

#### CLAUDE.md 規則總量上限：每新規則必刪一條（2026-06-20）

- **核心模式：** 對 CLAUDE.md 規則數量設定硬上限，每新增一條必須主動刪除一條舊規則，防止設定熵增（configuration entropy）
- **實作方向：**
  - 設定個人上限（如 15 條）並在新增前審視現有規則是否仍有效
  - 評估問：「這條規則最後一次真正影響 agent 行為是什麼時候？」無答案則候選刪除
  - 搭配版本控制，刪除規則前 commit 保留歷史
- **解決的問題：** 規則堆積後 agent 遵守率下降；過長的 CLAUDE.md 稀釋每條指令的有效性（「296→142 行品質反升」社群實證）
- **適用場景：** 個人長期維護的 Claude Code 工作環境；不適合需要頻繁增加領域規則的專案型使用（上限設定應因人而異）
- **來源：** dev.to/mjmirza（2026-06-20）

#### Context 裁剪 Tool Output 策略（2026-06-20）

- **核心模式：** 解決 Claude Code 長 session 退化的關鍵不是「加更多 context」，而是主動裁剪 tool output，防止 context 腐蝕（context rot）
- **實作方向：**
  - 限制工具輸出長度（截斷或摘要化 tool 回應，而非全量塞入 context）
  - 分 session 隔離不同任務，避免無關 context 跨任務污染
  - 任務重置前先保存關鍵摘要，再開新 session
  - 壓縮對話歷史：以摘要替代原始對話流
- **解決的問題：** 「Claude 越用越笨」現象；3 小時以上任務中途失憶、計劃漂移
- **適用場景：** 長 session 的 agentic 任務、多工具協同工作流、CI/CD 自動化 agent
- **注意：** 與 spec-driven development 結合效果更好——先有規格文件，再讓 agent 在精簡 context 下執行（dev.to/kenimo49；Reddit r/ClaudeAI）
- **大型 Repo 優化（HN 9）：** Git Lazy Mount（github.com/mohsen1/git-lazy-mount）——AI session 按需 fetch 大型 repo，附 sgrep 繞過全量 grep；HN score 9，適用 1GB+ monorepo，採用訊號待確認，附記待觀察。

#### Loop Engineering：條件觸發的 Claude 執行設計（2026-06-19，更新 2026-06-20）

- **核心模式：** 不讓 Claude 持續輪詢，而是設計「只在有實際工作時才觸發」的執行迴圈；解決 agent idle 時浪費 token 與上下文的問題
- **實作方向：** 在 loop 入口加入工作偵測條件（如佇列非空、事件觸發、diff 存在），條件不成立時 agent 直接 sleep 或退出，不進入 Claude 呼叫
- **具體工作流抽象（2026-06-20 補充）：** Boris Cherny 名言「我不再 prompt Claude，我寫 loop 讓 loop 去 prompt」的完整拆解——PR review、測試、push 等可拆解為觸發條件 + 執行步驟 + 結果驗證三段 loop；「設計 loop」取代「設計 prompt」是哲學升級（techstackups.com guide）
- **適用場景：** CI/CD 監聽型 agent、PR review bot、定時輪詢類任務；不適合需即時響應的互動式 session
- **與既有模式的關係：** 延伸自 Boris Cherny「Loops 是未來」論述，但強調「有意義的迴圈」而非無條件輪轉（Reddit r/ClaudeAI）

#### Self-rewriting CRM：AI agent 驅動的自我重構應用架構（2026-06-19）

- **核心模式：** 應用系統以 AI agent 為改寫引擎，使用者以自然語言描述需求，系統動態重寫自身邏輯而無需傳統開發介入
- **具體案例：** 開發者建置的 CRM 系統，非開發者可直接描述「希望追蹤客戶最後聯繫日期」等需求，agent 自動生成並整合相應欄位與邏輯
- **架構要素：** 需要嚴格的 schema validation、rollback 機制、人工確認節點，避免 agent 修改破壞核心業務邏輯
- **限制與風險：** 適合邊界清晰的 CRUD 類功能擴充；複雜關聯邏輯或安全敏感操作不宜自動重寫（推論）（Reddit r/ClaudeAI）
- **訊號：** 單一經驗談，無機制驗證，待社群佐證

#### Spec-driven Development CLI：規格驅動開發工具鏈（2026-06-19）

- **核心模式：** 透過 CLI 工具強制要求開發者先撰寫規格文件才能執行 AI 代碼生成，以工具層約束取代文化層自律
- **工具實例：** opsx spec-driven-development-toolkit，整合 Claude Code、OpenCode、Codex，在無規格文件的情況下拒絕執行代碼生成指令
- **解決的問題：** Boris Cherny「coding is solved」後社群對 vibe coding 的反思——無規格的 AI 代碼容易偏離實際需求並累積技術債
- **注意：** 對應工具（opsx）已被 HN flagged，社群接受度尚待觀察（GitHub davidpv/opsx-spec-driven-development-toolkit）
- **訊號：** 單一經驗談，無機制驗證，待社群佐證

#### Multi-agent 工作流

- **任務分解是核心難點**：社群詢問如何有效運用 20 個平行 Claude 實例，顯示 agentic 思維的學習曲線仍高
- **污染防止原則**：多 agent 協作時，讓各 agent 先獨立完成再互相審查，避免先看到他人答案後的收斂偏差（agent-order 的核心設計）
- **分支合併策略**：Claude Squad 以 orchestrator Claude 負責分派任務與合併 git 分支，而非讓各 agent 直接操作主分支

#### Skills 設計模式

- **觸發機制**：Skills 透過描述（description）自動觸發，適合封裝有明確情境的任務
- **知識框架化**：將外部知識（書籍、文件）轉為 skills，讓 Claude 在對話中自動引用對應框架
- **流程替代 README**：複雜設定流程包裝為 skill，比 README 更可靠且可持續維護
- **工具鏈封裝（HN 2）：** staffengineer.dev 將 OrbStack + Doppler + DigitalOcean 完整工作流封裝為 skills，強調「確定性高於靈活性」——setup 類 skill ROI 最高。

#### 模型使用策略

- **分層模型**：Sonnet 主力 + Opus 諮詢，節省約 60% 用量（未經獨立驗證）
- **推理強度 vs 安全邊界**：高推理強度不會放寬安全限制，兩者獨立控制
- ~~**Context window 縮減**：舊版模型將回退至 200k context~~（已被取代：Claude Code v2.1.197 起 Sonnet 5 為預設模型，原生 1M context window，見 [[entities/sonnet-5]]、[[entities/claude-code]]；此條目保留作為歷史記錄，不再適用）
- **嵌入式成本感知路由**（Workweave Router，2026-06-27）：依請求難度自動路由到最佳模型，無需手動規則；解決 Opus 4.7 成本暴增問題，HN score 181 為近期社群工具最高分之一

#### CLAUDE.md 設計原則

- **精簡優於詳盡**：CLAUDE.md 保持精簡（parsh 案例），以「規則」（rule）而非「建議」（suggestion）撰寫，有效減少 AI 冗余代碼與行為漂移
- **問題定義先於實作**：Relay plugin 的核心洞見 — Plan Mode 提問層級若停在「實作細節」，AI 常繞過問題本質直接動手；拉升至「為什麼這樣設計」層級效果顯著
- **人工確認節點**：EvanFlow 每步驟設有確認節點，不自動 commit；此模式在需要嚴謹品質控制的場景比全自動化更受信賴


#### API 使用模式

- **Batch API 不適合 agent**：每筆 batch 需 90–120 秒，互動式 agent 5 輪對話變成 10 分鐘等待；Batch API 僅適合後台非同步任務（offline 評估、大批量處理）
- **Prompt Cache Race Condition**：連續兩次呼叫間隔過短（< 2 秒），第二次 cache miss 機率約 40%；生產環境應在 cache-dependent 呼叫間加入延遲（見 [[entities/claude-code]]）
- **網頁抓取 token 效率**：直接傳入 HTML 有效內容佔比約 20%，轉換為乾淨 Markdown 後可節省約 80% 的 token 消耗

#### Plugin 設計模式

- **避免不必要 context 載入**：最常見反模式是在每次對話開頭載入大量無關 context，直接消耗大量 token 配額
- **5 個通用設計模式**（2026-04-28 社群整理）：觸發條件明確化、context 最小化、step 拆分、成本監測、人工確認節點
- **Scrum 工作流轉外掛**：將固定流程轉為插件的實際成本對比顯示，設計不良的插件成本可達設計良好版本的數倍
- **實體控制擴展（Reddit）：** Android Remote Control MCP 新版（r/ClaudeAI）——Claude 控制 Android 手機任意 app，新版支援 Claude.ai / WebView；無 HN 分數，Reddit 分享，適用移動端 UI 自動化測試。


#### 費用可觀測性工具（Cost Observability）

- **Grafana + Prometheus 企業監控整合**（2026-05-14）：把 Claude Code 用量視為可觀測的系統指標，以 SRE 式監控 dashboard 追蹤開發者行為數據；在官方 OpenTelemetry 底層之上建立企業級 dashboard，是目前官方尚未內建的監控整合層；企業部署 Claude Code 時的標準監控模式
- **官方趨勢觀察：** Anthropic 已提供原生 OpenTelemetry 支援作為底層（`CLAUDE_CODE_ENABLE_TELEMETRY=1`，v2.1.75，feature-radar 2026-06-03），未來官方是否會進一步提供內建 dashboard 或企業監控整合尚不明確；Grafana 子模式的長期必要性取決於官方在此方向的推進速度。

#### 知識圖譜應用

- **Leiden 社群偵測建立程式碼知識圖譜**（graphify）：26 天達 450k+ 下載、40k stars，宣稱每次查詢可減少 71 倍 token 用量；意外使用場景包括 SQL schema、Obsidian vault、學術論文，顯示知識圖譜在非純程式碼領域也有廣泛應用
- **git-backed Markdown 知識庫**（NanoBrain）：< 50ms append 延遲透過 hook 在 session 結束時更新，整合 Gmail/Google Calendar/Slack，是目前完整度最高的 AI Agent 跨工具共享知識庫方案


#### Hooks 精細化控制

- **PreToolUse 四種 exit code**：Block（阻止工具執行）、Allow（放行）、Modify（修改工具輸入後放行）、Error（視為工具執行失敗）；官方文件僅介紹基礎用法，四種 exit code 的實際差異遠超文件描述，影響攔截、允許、修改等場景的設計決策
- **PreToolUse 是一台小型狀態機**：每次工具調用前皆可插入判斷邏輯，結合 exit code 可實現精細的工具調用治理

### 2026-05

#### Token 路由與成本優化（2026-05-02）

- **CLAUDE.md 路由規則委派低優先任務**：透過 CLAUDE.md 路由規則，將批量文件讀取、樣板生成等繁瑣任務委派給 $0.02/call 的低成本模型（如 Kimi K2.5），在不升級訂閱的前提下大幅提升 Pro 額度使用效率
- **異質模型路由的關鍵設計**：任務特性決定路由目標；對話性推理走高能力模型，批量機械性任務走低成本模型；可在同一 CLAUDE.md 用條件規則控制


#### CLAUDE.md 領域化安全規則（2026-05-03）

- **技術棧專用防護規則**：針對 Kubernetes 的 13 條 CLAUDE.md 規則，防止 Claude 產出 latest tag 使用、缺少資源限制、過度授予 cluster-admin 等高風險配置；顯示 CLAUDE.md 已從通用指令發展至特定技術棧的系統性安全防護框架
- **可複用安全規則庫**：K8s 規則的整理模式可推廣至其他高風險領域（資料庫操作、IaC 配置、CI/CD 管線），將領域知識轉為 CLAUDE.md 規則是安全工程化的新思路


#### Multi-agent CLAUDE.md 衝突防範（2026-05-05）

- **11 條多 agent CLAUDE.md 最佳實踐**：針對多個並行 Claude Code session 可能產生的衝突整理出 11 條規則，涵蓋：獨立工作區邊界定義、禁止跨 agent 直接修改共享狀態、明確指定 merge 責任的 orchestrator 角色、每個 agent 的讀/寫範圍白名單等；對已採用多 agent 工作流的開發者是即戰力指南
- **P2P 加密多 agent 聊天室**：兩位開發者各自執行本地 Claude Code session，並接入同一個 P2P 加密聊天室，讓 AI 代理互相協商前後端規劃細節，人類僅負責監督與介入；被社群視為「非正式多 agent 協作」的具體可行實作

#### Session 記憶與搜尋工具生態（2026-05-05）

- **Session 語義搜尋**（Claude-Find）：解決 `/resume` 僅支援第一條訊息或名稱篩選的痛點；每月累積數百個 session 的重度用戶可用語義搜尋定位過去決策脈絡，並注入現有 session
- **本地 RAG 持久記憶**（Memex）：本地 RAG + 離線 embedding，所有資料留存本機，以 MCP 接入，無需額外 API 金鑰；直接解決雲端 AI 記憶的隱私疑慮
- **多 session 互通**（Claude Relay）：plugin 形式讓同時開啟的多個 Claude Code session（前後端、infra）互相傳訊查詢，省去人工複製貼上；開發者指出「我自己才是那個最慢的環節」


#### Token 大量降耗策略集中出現（2026-05-05）

- **7 個降耗實務技巧**（KDNuggets）：Claude Code 高 token 成本主要來自膨脹的 context（歷史訊息、已讀檔案、工具輸出、CLAUDE.md），而非單次 prompt 長度；降耗應從 context 管理入手，而非壓縮 prompt
- **Caveman Skill 實測 65% 降耗**：評測一個宣稱可削減 65% token 的 Claude Code skill，作者實測後效果顯著，但節省幅度依使用情境差異較大；對訂閱配額告急的用戶具參考價值，與 4/29 的「兩字 prompt vs 複雜外掛」基準測試形成對照
- **企業「穴居人模式」採用確認**（2026-07-01，404 Media）：企業透過極簡輸出插件要求 AI 以最少文字回應，OpenAI、Nvidia、GitHub 開發者已採用；將 Caveman 模式從「個人省費技巧」提升至「企業級降本策略」，與 Caveman Skill 65% 實測互相印證；[報導](https://www.404media.co/companies-are-making-claude-and-codex-talk-like-cavemen-to-stop-ais-soaring-costs/)（404 Media；HN score 4）

#### Backend 替換模式（2026-05-04）

- **環境變數後端切換**（DeepClaude 模式）：僅需修改 `ANTHROPIC_BASE_URL` 等少數環境變數，即可將 Claude Code 的 agent loop 導向其他 LLM 後端（如 DeepSeek V4 Pro）；HN 543 則討論凸顯社群對低成本替換的高度需求，雖然 DeepSeek 官方文件早已說明此方法，顯示這屬於「已知但被廣泛重新發現」的功能
- **本地 LLM 無侵入切換**（claudely）：在保留 Claude Code 完整插件生態（Skills、MCP、Hooks）的前提下切換後端至 Ollama/LM Studio/llama.cpp，無需修改主配置文件，讓開發者兼得生態完整性與本地模型的低成本優勢

#### CLAUDE.md 防腐爛機制（2026-05-04）

- **CLAUDE.md「腐化」問題成為主題**：長期使用 Claude Code 後，CLAUDE.md 常出現修正過的行為再次復發、規則膨脹失焦等「腐化」現象
- **Retro Loop 機制**（Patina CLI，MIT，已上 npm）：透過「回顧循環」定期回顧並更新 AI harness 設定，移除過時規則、整合新規則，防止配置腐化
- **腐化的根本原因**：規則是否仍有效缺乏持續驗證機制；規則只增不減；修復後無回歸測試確保規則仍適用

#### Agent Context 新鮮度問題（2026-05-04）

- **長 session 中 agent 重複讀同一檔案**：Claude Code 在長工作階段中不斷重讀相同文件、不記得程式碼修改歷史，造成重複工作與上下文喪失
- **時間感知代碼庫表示層**（Memtrace）：為 codebase 建立持久的時間感知表示（time-aware representation），讓 agent 能追蹤「哪些地方改了、為什麼改」，而非每次重讀猜測；此概念直接對抗 stateless agent 的核心缺陷

#### 結構化 Agent 框架設計（2026-05-04）

- **Pilot Shell 三指令框架**：
  - `/spec`：TDD 完整流程，規格優先於實作
  - `/fix`：含複雜度自動偵測，超出標準修復路徑時自動中止，防止 agent 過度施工
  - `/prd`：需求文件生成
  - 定位在「輕量但有工程紀律」的中間地帶，兼顧自動化與人工控制

#### 本機持久化記憶架構（2026-05-08）

- **Local stack MCP 整合、39ms 檢索**：開發者分享自建本機持久化記憶層：本地向量資料庫 + MCP 整合，實現 39ms 快速檢索；同時解決每次對話從零開始，以及記憶庫成長後大量消耗 token 的雙重痛點
- **架構核心原則**：避免將全部記憶注入 context（token 消耗過高），改以語義查詢按需取回相關片段；本機方案同時解決雲端記憶的隱私疑慮，與 Memex 思路相近但強調自建可控性
- **意義**：是對 Managed Agents Dreaming 官方解法的社群自建補充，在等待官方成熟前已形成可用架構
- **輕量替代（HN 6）：** Iantha（kiloloop.com/iantha/）——純 Markdown + git 存儲，自動提取時間性任務跨 session 持久保存，無需向量 DB；HN score 6，識別準確度待驗證，附記待觀察。


#### Managed Agents 架構模式（2026-05-07）

- **Dreaming 記憶整合機制**：Agent 在任務間隙自動整理近期事件、萃取值得長期保留的資訊存入記憶，類似人類睡眠時的記憶鞏固；Anthropic 首次在官方架構層面解決長跑 Agent 的記憶持久性問題（對比：社群工具 Dreamer、NanoBrain 先行實現類似理念）
- **Outcomes 規格驅動執行**：規格文件（spec）成為 Agent 執行時的強制依據而非參考文件，Agent 需在完成後自我驗證輸出是否符合預定目標，是「Spec-Driven Development」原則的官方制度化；與 2026-05-02 社群整理的「規格驅動開發」趨勢相呼應
- **20 路並行子代理**：官方框架層面首次支援 20 個子代理同時執行，使 agent 任務分解（multi-agent）從社群工具（Harness、Claudette）走向官方原生支援
- **Claude Code Routines vs cron job**：Routines 與傳統 cron job 的核心差異在於 Agent 能對結果進行推理而非只執行固定指令——每晚自動摘要當天 commit、每週掃描過期依賴、每日彙整錯誤日誌趨勢等場景均已有開發者實踐


#### Git Log 作為除錯首要步驟（2026-05-07）

- **Claude Code 自動讀取 git log 除錯**：觀察到 Claude Code 在除錯任務時自動讀取 git log，以描述性 commit message（取代 "wip"、"fixed stuff"）讓 Agent 在幾秒內縮小問題範圍；此行為可透過良好 commit 習慣主動利用
- **多 session 協作技巧**：搭配 git worktree 讓多個 session 在不同分支上協作，git log 成為各 session 間共享 context 的天然媒介

#### MCP Code Execution Token 效率（2026-05-07）

- **MCP server 過多導致 context 在第一條訊息前就半滿**：大量 MCP 伺服器的靜態工具列表佔用大量 context；以 MCP code execution 取代靜態工具列表的方案，讓 Agent 動態獲取能力，兼顧擴展性與 token 效率，適合正在評估 MCP 架構規模的團隊

#### 跨 Session 通訊插件（2026-05-07）

- **雙向 session 問答橋**：開發者自製插件讓兩個 Claude Code 工作階段互相通訊：新終端輸入 `/qu` 撥出，舊終端輸入 `/ans` 接聽；與 Claude Relay（多 session 廣播傳訊）不同，此插件聚焦雙向問答，更適合跨 session 即時決策諮詢的場景

#### Speculative Parallelism 工作流（2026-05-06）

- **每個 agent 擁有獨立 git worktree + session + 終端機**（Claudette）：開源桌面工具讓每個 Claude Code agent 擁有完全隔離的環境，實現 speculative parallelism 工作流——多個分支可同時執行且無衝突；社群顯示已有開發者手動實踐類似做法數月，工具化使這個模式變得可複用


#### Hooks 強制執行機制（2026-05-06）

- **PostToolUse 強制執行 Claude 可能略過的步驟**：透過在 PostToolUse 等工作流節點觸發 shell 指令，可強制執行 Claude 可能「自行判斷可略過」的步驟（程式碼格式化、自動 commit、強制測試）；解決 agent 「自以為完成」的核心痛點，是比 CLAUDE.md 指令更可靠的行為約束機制
- **Hooks vs CLAUDE.md 的本質差別**：CLAUDE.md 是「建議」，模型可選擇忽略；Hooks 是「強制執行」，透過 shell 指令保證執行，適合不允許跳過的關鍵流程節點

#### CLAUDE.md 語言生態規則集爆發（2026-05-06）

- **各語言專用規則集同日密集出現**（olivia_craft + natevoss 等）：dev.to 同日出現 5+ 篇針對特定語言的 CLAUDE.md 規則集：Rails（防止 legacy 模式）、Kotlin（coroutine 安全）、Flutter/Dart（防脆弱行動端程式碼）、Scala（慣用函數式）、Modern C++（防 1998 風格）、CLI bug 除錯後整理的 4 條實戰規則；社群正在各語言生態快速建立 AI 導向開發規範
- **趨勢意義**：CLAUDE.md 語言專用化，從「通用 AI 指令框架」演進為「語言生態特定的安全防護與風格守衛工具」；產量和速度的加速預示一個社群驅動的 CLAUDE.md 規則庫生態正在成形


#### Claude Code 作為 MCP 協調中心（2026-05-06）

- **MCP Hub 模式**：將 Claude Code 作為 n8n、瀏覽器 LLM 介面等多個自動化平台的 MCP 協調中心，讓多個自動化工具統一透過 Claude Code 控制；適合需要整合多個自動化工具並統一介面的開發者，是 Claude Code 從「coding assistant」延伸為「自動化協調中心」的具體實踐

#### Self-improving Rules（2026-05-06）

- **將糾正（correction）泛化為通用規則**（claude-smart）：現有記憶體方案只存事實、無法捕捉用戶糾正；透過將糾正泛化為跨專案通用規則，解決「同樣錯誤一犯再犯」的問題；與 claude-mem 的差異在於 context footprint 更小，但是否能準確泛化糾正仍有爭議


#### PostToolUse 生產稽核日誌模式（2026-05-09）

- **企業部署的可觀測性解法**：利用 Claude Code 的 `PostToolUse` hook 在生產環境建立完整稽核日誌，逐筆記錄工具呼叫的 Bash 指令與目標 repo，解決「代理上週三下午 3 點到底執行了什麼」的可觀測性痛點
- **適用場景**：企業部署、合規要求（SOC2/ISO 27001）、事後審計，任何需要完整 agent 操作記錄的場景；可結合 re_gent（AI agent 版本控制）形成完整稽核鏈
- **實作模式**：`PostToolUse` hook 在每次工具呼叫後以 append 方式寫入日誌，記錄 timestamp、指令、目標 repo、執行結果；此為 Hooks 機制的企業生產級應用案例

#### Git Hooks 強制代碼品質（2026-05-09）

- **AGENTS.md / CLAUDE.md 中強制安裝 pre-commit / husky**：在 AGENTS.md 或 CLAUDE.md 中明確要求代理安裝並遵守 git hooks，讓 CI 層面對 AI 代理產出的程式碼進行強制品質控管
- **具體門檻**：提案設定每檔最多 600 行與 McCabe 複雜度上限 10，防止 AI 加速開發同時帶來的複雜度失控
- **關鍵原則**：代理絕不使用 `--no-verify`（除非用戶明確確認），將 git hook 從「建議」升格為「強制防線」；延續「Hooks vs CLAUDE.md 本質差別」（2026-05-06）的設計理念，將強制執行範圍延伸至版本控制邊界

#### 架構決策記錄（ADR）+ Claude Code（2026-05-09）

- **54 份 ADR 35 天**：作者在 35 天內產出 54 份架構決策記錄（ADR），主張在撰寫任何程式碼前先完成決策文件，每個功能有對應的 ADR 才開始 Claude Code 協作
- **與 Claude Code 工作流整合**：先完成 ADR 再讓 Claude Code 實作，有效降低代理方向偏移的風險；與 Mneme（repo-native ADR 注入）工具理念一致
- **方法論一脈相承**：「決策文件先於實作」與「問題定義先於實作」（Relay plugin）和「規格驅動開發」（2026-05-02）的社群共識一致，顯示 agent 工作流方法論正在走向成熟的規範化收斂

#### 本機圖資料庫降低 Session Token 成本（2026-05-10）

- **快取不跨 session 是費用主因**：每次新 session 因 prompt cache 不跨 session 需重新讀取大量相同檔案，是 pay-as-you-go 用戶 session 費用達 $6–10 的主要原因（類似 2026-05-05 的 token 降耗討論，但更聚焦 session 成本結構）
- **圖資料庫索引解法**：建立本機圖資料庫（graph database）索引整個 codebase，讓模型只讀取結構化摘要而非原始檔案；不使用 AST 或向量，而以 LLM 生成關係圖的方式具有創意，成功大幅壓低 session 費用
- **任務層級 token 預算**：Tokenyst 讓 Claude Code pay-as-you-go 用戶在任務層級設定 token 預算，每次提示後即時顯示剩餘額度與使用比例，是費用控管工具鏈的新補充

#### Multi-agent 研究調查團隊架構（2026-05-10）

- **六代理分工**：作者以六個功能各異的 agent（Scout、分析師、撰寫員等）打造「AI 企業應用案例地圖」，目前已累積逾 250 個真實案例
- **實務驗證意義**：此案例在大量 multi-agent 理論討論中提供可驗證的實務實作，展示 multi-agent 架構在知識蒐集與整理任務上的具體生產力；與 2026-05-01 的 Omar（100 agent TUI 管理）不同，聚焦在「任務驅動型 agent 分工」而非「管理介面」


#### AI Agent 語意層漂移 CI 測試（2026-05-11）

- **問題定義**：AI agent 在多日執行中可能悄悄偏離預期行為（語意層漂移 / semantic drift），傳統 CI 測試無法偵測
- **六秒 CI 測試**：作者分享如何用一個**僅需六秒**的 CI 測試偵測 agent 的語意層漂移，防止代理在不知情情況下偏離目標行為；方法論：在 CI 流程中定期對代理發送探針任務並比對輸出分布，用統計指標而非固定預期值判斷行為是否偏移
- **實踐價值**：對長期運行的 Claude Code agent 工作流（如 vibe coding loop、每日排程任務），語意漂移偵測是尚未被廣泛解決的 QA 盲點

#### 多代理 PR Review 超越官方工具（2026-05-11）

- **adamsreview 設計**：以平行子代理、多階段驗證與 JSON 持久狀態執行 PR review；每個子代理從不同角度（安全性、邏輯正確性、效能、可維護性）獨立審查，最終交叉彙整
- **作者聲稱效果**：在自測中比官方 /review、/ultrareview、CodeRabbit 及 Greptile 捕捉到更多真實 bug，同時誤報率更低；並支援與 Codex CLI 組成 ensemble review
- **生態意義**：官方 PR review 工具已存在的情況下，社群以多代理架構做出差異化，顯示 Claude Code 插件生態正走向深度定制，間接壓力測試官方工具的品質上限；需獨立驗證作者聲稱的效果

#### CLAUDE.md 記憶規則驗證技巧（2026-05-11）

- **金絲雀規則（canary rule）**：在記憶或 CLAUDE.md 中埋入特定「金絲雀指令」（如要求 Claude 在每則回應前加上特定奇特前綴），可快速驗證 Claude 是否確實載入並執行了記憶規則；若前綴未出現即可判定記憶未生效
- **直接詢問專案設定**：詢問 Claude「目前載入的專案設定內容是什麼」，可立即確認 CLAUDE.md 是否被正確解讀；搭配金絲雀規則，兩招形成 10 秒快速一致性檢查
- **適用場景**：對依賴 CLAUDE.md 或記憶系統的自動化工作流尤為重要，是社群自 CLAUDE.md candidate-context 架構揭示（2026-05-10）後催生的實用對策

#### AGENTS.md 跨工具插件簡報（2026-05-11）

- **統一配置文件**：以 AGENTS.md 作為跨工具（Claude Code、Cursor、GitHub Copilot 等）的統一插件簡報文件，讓不同 AI 工具共享相同的代理人配置說明，降低跨工具整合的設定重複成本
- **Kobiton 案例**：Kobiton 在跨工具自動化測試環境中實踐此模式，不同 AI 工具共享同一份代理配置，顯示 AGENTS.md 有潛力成為跨工具 AI 配置的業界標準
- **與 CLAUDE.md 的關係**：CLAUDE.md 是 Claude Code 專屬指令，AGENTS.md 是跨工具通用的代理簡報文件；兩者定位互補，AGENTS.md 解決的是工具綁定問題，CLAUDE.md 解決的是 Claude 特定行為調優問題

#### `/goal` Fire-and-Forget 自動化模式（2026-05-12）

- **官方新功能**：v2.1.139 推出的 `/goal` 指令代表 Claude Code 首次具備真正的 fire-and-forget 能力；用戶設定可驗證的完成條件後，每輪執行結束由一個小型快速模型判斷條件是否成立——未達成則自動開始下一輪，無需人工介入
- **適用場景邊界**：設計上適合有明確終態的長時間任務（模組遷移完成、所有測試通過、API 端點全部回應 200），不適合開放式或目標模糊的任務
- **社群反應**：Reddit 對 `/goal` 的反應熱烈，多名用戶形容這是「Claude Code 首個真正的 fire-and-forget 循環」，此版本包含 104 項變更；見 [[entities/managed-agents]]
- **Anthropic 抄自開源爭議**：部分社群成員指出 `/goal` 的概念早已在 OpenClaw 等社群工具中實現，質疑 Anthropic 是否長期觀察開源社群後直接內建功能而未給予信用，Anthropic 未回應

#### Writ 規則強制執行（Neo4j 知識圖譜 Pipeline）（2026-05-12）

- **問題**：Claude Code 常忽略 CLAUDE.md 中的規則，原因之一是 CLAUDE.md 作為 candidate-context（`<system-reminder>`）可被模型跳過；同時載入所有規則也因無關規則佔用 token 而降低精準度
- **Writ 的解法**：透過五階段 Neo4j 知識圖譜 Pipeline，在每次工具呼叫前自動擷取與當前任務語義最相關的規則子集，只注入相關規則，兼顧規則遵守率與 token 效率
- **技術架構**：以 Neo4j 儲存規則及其語義關係，每次任務啟動時依 context 做圖遍歷，找出相關規則集；比純 CLAUDE.md 文字比對更具選擇性，比全量載入更省 token
- **意義**：是「CLAUDE.md 強制執行」與「規則過多導致 token 浪費」這個雙重困境的社群工程解法，與官方 Hooks 機制（強制執行）和 CLAUDE.md（建議）的層次設計形成互補

#### 跨環境 Agent 記憶協定（ltm / Core Memory Packet）（2026-05-12）

- **現有方案的根本缺陷**：CLAUDE.md、`.cursor/rules`、AGENTS.md 等現有 agent 記憶方案均為 Markdown 文件，無法在不同編輯器、不同機器、不同 AI 模型之間攜帶和同步
- **ltm 的設計**：基於 JSON 協定（Core Memory Packet）的 Agent 記憶工具，設計上實現供應商中立的持久化記憶；Core Memory Packet 包含結構化的 agent 記憶資料（任務歷史、學習到的偏好、已知約束），可在任何支援該協定的工具間交換
- **跨環境攜帶性**：相比 Markdown 記憶方案，ltm 的 JSON 結構可被任何工具解析，不依賴特定 AI 工具的指令解讀機制
- **與其他記憶工具的定位差異**：Memex（本地 RAG）、NanoBrain（git-backed Markdown）、Dreamer（MCP → AGENTS.md 整合）均聚焦單一環境內的記憶持久化；ltm 的差異化在於跨工具、跨機器的記憶可攜性

#### 多模型路由工作流（Dragoman）（2026-05-13）

- **依問題類型路由模型**：開源 CLI 工具 Dragoman（約 800 行）讓 Claude Code 依問題類型自動路由至不同專業模型——新聞/時事查詢 → Perplexity；複雜推理 → Gemini；本機運算 → Ollama；Claude 作為整合層統整最終回答
- **4 模型並行 + 彙整**：支援四個模型同時執行相同 prompt，最後由 Claude 統整並標記分歧點；延續 Council（並行多模型）的設計理念，但聚焦 Claude Code 工作流整合而非一次性 prompt 比較
- **API 金鑰安全設計**：API 金鑰透過 1Password/Keychain 解析，完全不進入 Claude context，是 API 金鑰管理的安全最佳實踐範例
- **意義**：多模型協作架構從「實驗性」走向「工具化」；與 Token 路由策略（2026-05-02）的 CLAUDE.md 路由規則取向不同，聚焦不同工具的能力互補而非成本優化
- **相關工具（HN 1）：** cc-fleet（github.com/ethanhq/cc-fleet）——讓 Claude Code 作為 orchestrator 調度異質 LLM worker，HN score 1，採用訊號不足，附記待觀察。

#### 電話 MCP：AI 代理與實體通話整合（2026-05-13）

- **Cocall.ai 架構**：AI 代理撥打外線電話，遇到不確定的問題時自動暫停，轉回詢問使用者後再繼續通話；採用全雙工語音模型，支援 IVR 導航（按鍵選單）與電話轉接
- **人機協作模式**：不同於完全自主代理，此工具強調「遇到邊界問題暫停確認」的人機協作設計，是 Agent 操作確認節點概念在實體世界的延伸
- **意義**：是目前少見的 AI 代理從數位世界延伸至實體通話世界的案例；MCP 生態持續向現實世界操作延伸（繼 OpticOdds MCP、Cocall 等），顯示 Claude Code 生態已超出純開發工具範疇

#### Token Bloat 系統性對策（2026-05-13）

- **測試執行器輸出精簡**：Claude Code 用量限制促使開發者深入審計 context 消耗，作者聚焦測試執行器輸出，提出只保留「測試是否通過、哪項失敗、失敗位置」的精簡策略；預告這是系列文章的第一篇
- **根本問題框架化**：Token bloat 的主要來源是 context 膨脹（歷史訊息、測試輸出、工具回傳），而非 prompt 本身；系統性降耗需從 context 生命週期管理入手——此系列代表社群正在以系統化方式解決 token 效率問題，繼 token 降耗策略（2026-05-05）之後的更深度演進

#### 大規模子代理工作流實踐（2026-05-13）

- **Boris Cherny 的數千個子代理工作流**：Claude Code 創始人公開每晚讓數千個 AI 子代理執行「深度工作」的工作流，是 Managed Agents 20 路並行子代理能力在個人工作流中的極端應用，展示大規模 agentic 模式的可行邊界
- **與官方工具的正向回饋**：此工作流建立在 v2.1.140 改善的 subagent_type 匹配（大小寫不敏感）與 Agent View（統一 session 管理）基礎之上，顯示官方功能更新與社群使用案例之間的正向回饋；社群需求驗證官方功能優先序，官方工具降低社群工作流門檻
- **社群討論帶動**：被主流媒體（Business Insider、Let's Data Science）大幅報導後，社群對大規模並行代理架構的討論密度顯著提升；見 [[entities/boris-cherny]]、[[entities/managed-agents]]


#### Agent 持續運作架構（2026-05-03）

- **VPS 雙代理持續運作**：兩個 Claude Code 代理在 VPS 的 tmux session 中持續運作，自動開 PR 並發布 Discord 狀態更新，代理間可相互協調；架構概念類似「Claude Code 版 docker-compose」
- **OS 用戶隔離爆炸半徑**：每個代理使用獨立 OS 用戶，比容器化更輕量但仍能有效限制單一代理失控時的影響範圍，是 agent 架構設計的實踐案例

#### Git Worktrees 作為多 Agent 隔離原語（2026-05-23）

- **獨立工作樹隔離**：每個 Claude Code agent 運行在各自的 git worktree 中，擁有獨立的工作目錄、staged changes 和本地狀態，確保並行 agent 之間完全不互相干擾
- **比 OS 用戶更輕量**：相比雙代理 VPS 架構使用獨立 OS 用戶隔離（2026-05-03），git worktree 不需要 OS 層面的帳號管理，是更輕量的隔離原語，特別適合 CI/CD 或本機多任務場景
- **Superset 框架的底層機制**：社群工具 Superset（2026-05-23 首見）使用 git worktree 自動為每個並行 Claude Code 實例分配獨立工作區，將此模式工具化；與 FleetView 的概念類似，但聚焦在 worktree 而非 session 可見性
- **爆炸半徑最小化**：即使某個 agent 在本地 worktree 做了破壞性操作（例如誤刪文件），不影響主 branch 與其他 worktree；合併前可 review 全部 diff，強制加入人工審查節點
- **適用場景**：同時跑多個 feature branch、平行測試不同實作方案、CI 環境中不同 PR 的並行驗證

#### Framework-Specific CLAUDE.md 設計（2026-05-23）

- **框架防呆規則**：「CLAUDE.md for Svelte: 13 Rules」展示了針對單一框架（Svelte）客製化 CLAUDE.md 的方法論——明確列出「禁止使用 React 思維」（禁 JSX、禁 useState、禁 useEffect）的負面規則，防止 Claude Code 將訓練資料中 React 佔比過高的偏好帶入 Svelte 開發
- **負面規則的力量**：相比「請使用 Svelte 的 reactive statements」，「不要使用 useState」更能有效阻止 Claude Code 回退至 React 慣例；這延伸了「精簡 CLAUDE.md」（2026-04-25）的討論——精簡不只是少寫，而是寫對類型的規則
- **框架差異放大問題**：框架差距越大（例如 React → Svelte），模型產生慣性錯誤的頻率越高；框架特定 CLAUDE.md 的必要性與框架獨特性正相關
- **可複用範本化**：13 條規則格式結構化，社群可以複製並依自己的框架（Vue、Solid、HTMX）調整——這是 CLAUDE.md 最佳實踐從個人做法走向社群共享範本的跡象

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
- [[entities/pricing]]（token 消耗與模型選擇策略相關）
- [[entities/managed-agents]]（官方 Agent 框架：Dreaming 記憶整合、20 路並行、Outcomes 規格驗證）
- **Project Deal**（Claude 代理人交易談判實驗，multi-agent 應用的商業探索；詳見 [[entities/claude-code]]）
- [[entities/claude-design]]（AI 設計工具，與 Claude Code + Figma MCP 工作流有定位重疊）
- [[topics/community-tech-discussions]]（概念辯論、設計哲學、實證研究）
- [[topics/community-tech-timeline]]（2026-04-25 至今完整時序記錄，從本頁拆分）

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

