# Wiki 操作日誌

Append-only 紀錄。每次 ingest、query 或 lint 都在此追加一條。
格式：`## [YYYY-MM-DD] 類型 | 說明`

---

## 2026-05-31 Ingest | news/2026-05-31.md

- 來源日報：`news/2026-05-31.md`（50 則，5/6 來源；Anthropic $965B Series H 超越 OpenAI、"We contain Claude" 工程部落格、Opus 4.8 Thinking 900K context drain、ultracode 70 agent 實測、Claude Code Source Deep Dive VI & VII）
- 更新頁面：
  - `entities/opus-4-8.md`：新增 Thinking 40–60 倍 context drain（900K cache tokens/turn）；ultracode 70 agent 4 階段 pipeline 實測；更新歷史記錄；更新最後更新 2026-05-31
  - `topics/anthropic-business.md`：新增 2026-05-31 時序（"We contain Claude" 工程部落格 + Bloomberg 責任創新平衡報導）；更新最後更新 2026-05-31
  - `topics/community-tech-tools.md`：新增 4 個工具（claude-code-proxy / Lite-Harness / Arch-Decision / claude-skills）；更新最後更新 2026-05-31
  - `topics/community-tech-discussions.md`：熱門討論新增 4 條（Thinking context drain / 自動模型路由需求 / 10 Plugin 成本 / Progressive Disclosure 三層架構）；更新最後更新 2026-05-31
  - `feature-radar.md`：更新最後更新 2026-05-31（Thinking drain 量化確認）
  - `wiki/index.md`：更新最後更新 2026-05-31
- 新增頁面：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/opus-4-8.md | ✅ 通過（新增負面紀錄，歷史記錄格式一致）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend，結構清晰）|
  | topics/community-tech-tools.md | ✅ 通過（4 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（熱門討論 prepend，格式符合）|
  | feature-radar.md | ✅ 通過（僅更新最後更新欄位）|

---

## 2026-05-30 Ingest | news/2026-05-30.md

- 來源日報：`news/2026-05-30.md`（76 則，6 來源；v2.1.158 Auto mode 擴展 Bedrock/Vertex/Foundry、UltraCode 1.7M token bug、Anthropic 削減未授權平台清單、Mythos exploit eval 正式發布、Wired Chris Olah 長文）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.158（Auto mode on Bedrock/Vertex/Foundry）；更新最後更新 2026-05-30
  - `entities/opus-4-8.md`：新增 UltraCode 1.7M token bug、Qwen distillation 爭議、德語品質退步；更新歷史記錄；更新最後更新 2026-05-30
  - `entities/mythos.md`：新增 2026-05-30 exploit eval 正式發布（red.anthropic.com）；更新最後更新 2026-05-30
  - `entities/chris-olah.md`：新增 Wired 長文《The Vatican's Man Inside Anthropic》段落；更新最後更新 2026-05-30
  - `topics/anthropic-business.md`：新增 2026-05-30 時序（Anthropic 削減未授權平台清單）；更新最後更新 2026-05-30
  - `topics/community-tech-tools.md`：新增 3 個工具（claude-handoff-guard / cartographer-skill / dotpi）；更新最後更新 2026-05-30
  - `topics/community-tech-discussions.md`：熱門討論新增 3 條（UltraCode bug / Qwen 爭議 / AI 社會模擬）；技術彙整新增 2 個段落；更新最後更新 2026-05-30
  - `feature-radar.md`：全覽表新增 v2.1.158（🔥🔥 ✅）；Dynamic Workflows 降級為 ❌（UltraCode bug）；更新最後更新 2026-05-30
- 新增頁面：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過（版本更新，格式一致）|
  | entities/opus-4-8.md | ✅ 通過（負面清單補充，結構清晰）|
  | entities/mythos.md | ✅ 通過（新增段落，不影響現有結構）|
  | entities/chris-olah.md | ✅ 通過（新增段落，獨立可讀）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend，摘要無需更新）|
  | topics/community-tech-tools.md | ✅ 通過（3 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（熱門討論 prepend，技術彙整 prepend）|
  | feature-radar.md | ✅ 通過（全覽表更新，試用價值降級有說明）|
- 本日新增工具：claude-handoff-guard / cartographer-skill / dotpi（共 3 個，累積 139 個）
- feature-radar 更新：v2.1.158（🔥🔥 ✅）、Dynamic Workflows 降級（❌ UltraCode bug）

---

## 2026-05-29 Ingest | news/2026-05-29.md

- 來源日報：`news/2026-05-29.md`（97 則，6 來源；Claude Opus 4.8 發布 HN 1662、$65B Series H 融資 $965B 估值、Dynamic Workflows Research Preview、Claude Code v2.1.156 修復 thinking blocks 400 錯誤、Andrej Karpathy 確認加入 Anthropic + Eureka Labs 解散、MarginLab SWE-bench-Pro 追蹤發現升版前效能下降）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.156（修復 Opus 4.8 thinking blocks 400 錯誤）；更新最後更新 2026-05-29
  - `entities/opus-4-8.md`：**新建頁面**，Opus 4.8 完整發布細節、Dynamic Workflows、Fast Mode、社群初期反映
  - `entities/mythos.md`：新增 2026-05-29 Reuters 確認「Mythos 數週內公開推出」；更新最後更新 2026-05-29
  - `entities/andrej-karpathy.md`：確認加入 Anthropic（移除待核實標注）；補充 Eureka Labs 解散；新增 2026-05-29 歷史記錄；更新最後更新 2026-05-29
  - `topics/anthropic-business.md`：更新摘要與指標表（估值 $965B、ARR $47B、$65B Series H）；戰略合作新增 Samsung/SK Hynix、Apollo/Blackstone；新增 2026-05-29 時序；更新最後更新 2026-05-29
  - `topics/code-quality-decline.md`：新增 2026-05-29 時序（MarginLab 升版前效能下降、thinking blocks 400 錯誤、4.8 行為退步投訴）；更新最後更新 2026-05-29
  - `feature-radar.md`：全覽表新增 Opus 4.8（🔥🔥🔥🔥🔥 ⚡）、Dynamic Workflows（🔥🔥🔥🔥 ⏳）、v2.1.156（🔥🔥 ✅）；最新功能新增 Opus 4.8 + Dynamic Workflows + Fast Mode 完整條目；更新最後更新 2026-05-29
  - `topics/community-tech-tools.md`：新增 4 個工具（AISlop / ktx / Headroom / OpenHive）；更新最後更新 2026-05-29
  - `wiki/index.md`：新增 entities/opus-4-8；頁面數 34→35；更新最後更新 2026-05-29
- 新增頁面：`entities/opus-4-8.md`（1 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/opus-4-8.md | ✅ 通過（新建，摘要清晰，熱度表緊接摘要）|
  | entities/claude-code.md | ✅ 通過（版本更新，格式一致）|
  | entities/mythos.md | ✅ 通過（新增段落，不影響現有結構）|
  | entities/andrej-karpathy.md | ✅ 通過（狀態更新，歷史記錄補充）|
  | topics/anthropic-business.md | ✅ 通過（指標表更新，時序 prepend）|
  | topics/code-quality-decline.md | ✅ 通過（時序 prepend）|
  | feature-radar.md | ✅ 通過（新功能置頂，格式一致）|
  | topics/community-tech-tools.md | ✅ 通過（4 工具插入表頭）|
- 本日新增工具：AISlop / ktx / Headroom / OpenHive（共 4 個，累積 136 個）
- feature-radar 更新：Opus 4.8（🔥🔥🔥🔥🔥 ⚡）、Dynamic Workflows（🔥🔥🔥🔥 ⏳ Research Preview）、v2.1.156（🔥🔥 ✅）

---

## 2026-05-28 Query | 建立 topics/anthropic-business.md

- 新增頁面：`topics/anthropic-business.md`（Anthropic 商業健康度）
  - 內容範圍：企業採用率（34.4% Ramp AI Index）、PMF 觀察（Simon Willison HN 970）、財務信號（17 倍訂閱補貼）、商業風險（Microsoft 退出）、戰略合作（富士通/KPMG）
  - 來源整合自：news/2026-05-28、news/2026-05-27、news/2026-05-25、news/2026-05-23、news/2026-05-15、news/2026-05-13
- 更新頁面：
  - `topics/community-tech-discussions.md`：Simon Willison PMF 條目 `衍生` 欄補上 `[[topics/anthropic-business]]`
  - `wiki/index.md`：新增 topics/anthropic-business，頁面數 33→34

---

## 2026-05-28 Ingest | news/2026-05-28.md

- 來源日報：`news/2026-05-28.md`（75 則，6 來源；Simon Willison HN 970 PMF 論述、Anthropic 米蘭辦公室、Claude Code v2.1.153、Cisco LLM Security Leaderboard Anthropic 8/10、企業預算壓力密集信號、SpaceX Colossus 6 個月短期租約澄清、ChatGPT-5.5 DeepSWE 超越 Opus 4.7）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.153（skipLfs + npm 版本通知）至最新版本表格與版本歷史；更新最後更新 2026-05-28
  - `entities/claude-security.md`：新增 2026-05-28 Cisco LLM Security Leaderboard（Anthropic 8/10）；更新參考來源；更新最後更新 2026-05-28
  - `topics/community-tech-tools.md`：新增 6 個工具（NotifAI、Workplane、CCW、harmont-cli、Zorilla、token-xray）；更新 Token 成本不透明痛點至 2026-05-28；更新最後更新 2026-05-28
  - `topics/enterprise-cost-management.md`：新增 2026-05-28 時序（Benzinga/CFO.com 預算放緩、Reddit Uber 分析、$200 方案 17× 補貼）；更新最後更新 2026-05-28
  - `topics/community-tech-discussions.md`：熱門討論新增 Simon Willison PMF（HN 970，🔥🔥🔥🔥🔥 ☄️閃現）；技術彙整新增 PMF 條目；更新最後更新 2026-05-28
  - `feature-radar.md`：全覽表新增 v2.1.153 skipLfs 條目（🔥 ⚡）；更新最後更新 2026-05-28
- 新增頁面：無
- 呈現品質：✅ 通過（所有更新頁面摘要清晰，關鍵資訊前置）
- feature-radar 更新：v2.1.153 加入全覽表（低熱度，實用性 ⚡ 有條件推薦）
- 本日新增工具：NotifAI / Workplane / CCW / harmont-cli / Zorilla / token-xray（共 6 個，累積 132 個）

---

## 2026-05-27 Ingest | news/2026-05-27.md

- 來源日報：`news/2026-05-27.md`（86 則，6 來源；Claude Code v2.1.152 Coordinator 模式、Anthropic 韓國首爾辦公室、富士通戰略合作、Uber COO 25% 生產力確認、Bloomberg 企業不安報導、Boris Cherny Platformer 專訪）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.152（Coordinator 模式 + `/code-review --fix` + Worker 代理人指令 +4,566 tokens）；版本歷史新增 2026-05-27 條目；更新最後更新 2026-05-27
  - `entities/boris-cherny.md`：新增「軟體工程師的終結」Platformer 專訪（2026-05-27）；更新最後更新 2026-05-27
  - `entities/mythos.md`：新增印度政府測試 Mythos 政府網路安全計畫（首個主權政府採用案例）；更新最後更新 2026-05-27
  - `topics/enterprise-tool-tracker.md`：Uber 備註更新（COO 確認 25% 生產力）；新增 Fujitsu、Travelport、Nimble Gravity 三個企業條目；Claude API 採用數 4→7；新增 2026-05-27 時序；更新最後更新 2026-05-27
  - `topics/community-tech-tools.md`：新增 9 個工具（Minicor、claude-handoff-revive、STAX IDE、claude-workflow-composer、Vibeshub、timeglass.ai、KittyHTML、Claude Usage Tray、ADHDStack）；更新 3 個痛點洞察近期工具至 2026-05-27；更新最後更新 2026-05-27
  - `feature-radar.md`：新增 Coordinator 模式 + `/code-review --fix`（v2.1.152，熱度 🔥🔥🔥🔥，試用價值 ✅）；全覽表新增條目；更新最後更新 2026-05-27
- 新增頁面：無
- 呈現品質：✅ 通過（所有更新頁面前段清晰，關鍵資訊可獨立閱讀）
- feature-radar 更新：新增 Coordinator 模式 + `/code-review --fix` 功能條目
- 本日新增工具：Minicor / claude-handoff-revive / STAX IDE / claude-workflow-composer / Vibeshub / timeglass.ai / KittyHTML / Claude Usage Tray / ADHDStack（共 9 個，累積 126 個）

---

## 2026-05-26 Ingest | news/2026-05-26.md

- 來源日報：`news/2026-05-26.md`（83 則，6 來源；Pope Leo XIV 封論梵蒂岡事件、Mythos 公開釋出確認、Notion 整合三大 AI 編碼工具、企業安全整合 28 項、MCP 優化工具湧現）
- 更新頁面：
  - `entities/mythos.md`：狀態更新為「公開化中」；新增 05/26 媒體密集報導（Help Net Security 10K / eWeek 23K / PYMNTS / Techzine）與 The Register + Gotrade + CyberSecurityNews 三方確認公開釋出；更新最後更新 2026-05-26
  - `entities/claude-security.md`：新增 05/26 Varonis Claude Compliance API 整合（AI 治理 + 資料存取合規）、Forcepoint 延伸至 Claude Enterprise、Anthropic 28 項企業安全整合；更新最後更新 2026-05-26
  - `topics/community-tech-tools.md`：新增 5 個工具（skills-for-humanity、PrismCat、Agent Launch、AWO、AI Agent Token Cost Calculator）；更新痛點洞察表（Token 成本不透明、多 agent 協調混亂）；總工具數：117；更新最後更新 2026-05-26
  - `topics/community-tech-discussions.md`：新增 4 條熱門討論（Claude Code 效能衰退量化、Trading Peace for Pace、軟體工廠時機辯論、非技術 Vibecoding）；新增 2 個技術彙整段落（OpenTelemetry 量化、Trading Peace 情緒代價）；更新最後更新 2026-05-26
  - `topics/anthropic-government-policy.md`：新增梵蒂岡封論事件（Chris Olah 出席 Magnifica Humanitas 揭幕）；更新時序；狀態改為 monitoring；更新最後更新 2026-05-26
  - `feature-radar.md`：本日無新使用者端功能；BioMysteryBench 為研究評測發布；更新最後更新 2026-05-26
- 新增頁面：
  - `entities/chris-olah.md`：Anthropic 共同創辦人、梵蒂岡演講事件、可解釋性研究背景
- 呈現品質：✅ 通過（所有更新頁面前段清晰，關鍵資訊可獨立閱讀）
- feature-radar 更新：本日無新功能條目新增
- 本日新增工具：skills-for-humanity / PrismCat / Agent Launch / AWO / AI Agent Token Cost Calculator（共 5 個，累積 117 個）

---

## 2026-05-26 手動建頁 | enterprise-tool-tracker

- 新增頁面：`topics/enterprise-tool-tracker.md`（大型企業 AI 編碼工具使用追蹤）
- 初始資料：10 家企業、4 個工具、含市場分層觀察
- 加入 `wiki/CLAUDE.md` 觸發規則（企業工具採用新聞 → 自動更新此頁）
- 更新 `wiki/index.md`（頁面數 31→32）

---

## 2026-05-25 Ingest | news/2026-05-25.md

- 來源日報：`news/2026-05-25.md`（70 則，6 來源；Claude Code v2.1.150 遠端注入披露、Mythos Exploit Eval 論文正式發布、Microsoft 宣布 6/30 完全停用 Claude Code、MCP 帳單 73% 來自工具調用）
- 更新頁面：
  - `entities/mythos.md`：新增 Exploit Eval 論文正式發布（red.anthropic.com/2026/exploit-evals/）；UK AISI 6/10 企業網絡接管測試數據；Politico 議會閉門簡報；The Register 公開化路線確認；更新最後更新 2026-05-25
  - `entities/claude-code.md`：更新 v2.1.150 版本歷史，加入遠端系統提示注入爭議（Bootstrap API + GrowthBook tengu_heron_brook flag）；更新最後更新 2026-05-25
  - `topics/ai-agent-safety.md`：新增 Claude Code v2.1.150 遠端系統提示注入機制披露（Bootstrap API + GrowthBook 60s 更新）至技術彙整；更新最後更新 2026-05-25
  - `topics/enterprise-cost-management.md`：Microsoft 章節更新為「完全停用（6 月 30 日）」；新增 MCP 工具調用 73% 隱性成本案例；更新最後更新 2026-05-25
  - `topics/community-tech-tools.md`：新增 2 個工具（archmcp、Smriti）；總工具數：112；更新最後更新 2026-05-25
  - `topics/community-tech-discussions.md`：新增 4 條熱門討論（遠端注入、Yabby、MCP 帳單 73%、TDD 60% 違規）；新增 4 個技術彙整段落；更新最後更新 2026-05-25
  - `feature-radar.md`：本日無新使用者端功能；更新最後更新 2026-05-25
- 呈現品質：✅ 通過（所有更新頁面前段清晰，關鍵數字可獨立閱讀）
- feature-radar 更新：本日無新功能條目新增
- 本日新增工具：archmcp / Smriti（共 2 個，累積 112 個）

---

## 2026-05-24 Ingest | news/2026-05-24.md

- 來源日報：`news/2026-05-24.md`（51 則，6 來源；Glasswing CVD 儀表板、小企業 Skills、Mythos string leak、JSONL session 知識化、cache miss 量化）
- 更新頁面：
  - `entities/mythos.md`：新增 CVD 儀表板正式上線（red.anthropic.com/2026/cvd/，281 專案/1,596 漏洞/97 修補）；新增 Mythos 準備登陸 Claude Code 與 Claude Security（app 字串洩露）；更新最後更新 2026-05-24
  - `entities/claude-security.md`：新增 2026-05-24 歷史記錄（Mythos string leak）；更新最後更新 2026-05-24
  - `topics/community-tech-tools.md`：新增 4 個工具（CC-Wiki、Fleet、aco-system、Claude Code CLI Web Terminal）；更新痛點洞察表（多 agent 協調更新至 05-24）；總工具數：110
  - `topics/community-tech-discussions.md`：新增 3 條熱門討論（cache miss 12.5x、686 skills 導航、JSONL session 知識化）；新增對應技術彙整段落；更新時序與參考來源
  - `topics/enterprise-cost-management.md`：更新現況表（加入 cache miss 12.5x 量化數據）；更新最後更新 2026-05-24
  - `feature-radar.md`：新增「小企業 Skills」條目（31 個官方 Skills，🔥🔥🔥 推薦）；更新最後更新 2026-05-24
- 呈現品質：✅ 通過（所有更新頁面前段清晰，關鍵數字可獨立閱讀）
- feature-radar 更新：已新增小企業 Skills 條目
- 本日新增工具：CC-Wiki / Fleet / aco-system / Claude Code CLI Web Terminal（共 4 個）

---

## 2026-05-24 工具目錄全面重構 | community-tech-tools

- 工具資格審查（依 2026-05-20 入選規則逐一評估全部 109 筆）：
  - 移除 `Snyk + Claude Code` — 商業公司整合公告，無 HN/Reddit 社群討論
  - 移除 `OpticOdds MCP` — 商業運動賠率 API，無公開 repo/demo，純廣告性工具
  - 移除 `TradingAgents Plugin` — 訂閱制付費服務，非社群開源工具
  - 保留其餘 106 個（均有 Show HN / Reddit / 多來源驗證）
- 頁面結構調整：
  - 將 `## 痛點洞察` 從頁尾移至 `## 指標說明` 之前（關鍵分析前置）
  - `## 指標說明` 新增類型清單與入選標準欄位
- 類型標籤標準化：原 40+ 種雜亂類型統一為 10 個類別（多 Agent / 記憶工具 / 費用監測 / 工作流 / 整合工具 / 搜尋/診斷 / 安全工具 / IDE/終端 / Skills / 其他）
- 採用欄格式統一：`⏳ 觀望中` 統一改為 `⏳`
- Web Reader 同步更新（app.js）：
  - 新增 `⚠️ 存疑` 篩選按鈕（原有統計但無法篩選）
  - 頁面載入時自動按採用狀態降序排列（✅ → ⚡ → ⏳ → ⚠️）
  - 修正找表邏輯：依欄位標題找工具表，避免誤用痛點洞察表
- 呈現品質：⚠️ 已修復（頁面結構重整、類型統一、關鍵資訊前置）
- 總工具數：106

---

## 2026-05-23 工具目錄清理 | community-tech-tools 品質審查

- 背景：依新制入選門檻（HN score ≥ 30 或評論 ≥ 5 / Show HN 自動入選 / 2+ 獨立來源）重新審查全部工具
- 移除 12 個不符標準的條目：
  - `lipstyk` — 無日期、無 URL、無可追蹤來源
  - `claude-anyteam` — 無日期、無 URL、無可追蹤來源
  - `Linear+Lanes MCP` — 無日期、無 URL、無可追蹤來源
  - `WezTerm 主題同步` — 無日期、無 URL（純設定技巧，非獨立工具）
  - `shipcheck` — 2026-05-17 日報無此工具記錄
  - `cv-claw` — 任何日報均無此工具記錄
  - `HiveTerm` — 僅出現在 2026-05-12 今日聚焦摘要，無專文、無 URL
  - `Mneme HQ` — 僅 dev.to 發布，無 HN/Reddit 討論
  - `QA Skills（24 個）` — 僅 dev.to 發布，無 HN/Reddit 討論
  - `Code Quest` — 無公開 URL，無 HN/Reddit 討論
  - `AI 命名一致性 OSS` — 僅 dev.to 發布，無 HN/Reddit 討論
  - `unitmux` — 僅 dev.to 發布，無 HN/Reddit 討論
- 同步更新：
  - `痛點洞察` 表格移除 HiveTerm 引用
  - `AI 輔助開發的長期副作用` 移除 `AI 命名一致性` 工具引用（保留概念描述）
- 總工具數：~108（移除後）

---

## 2026-05-22 Ingest | news/2026-05-22.md

- 來源日報：`news/2026-05-22.md`（36 則，含 v2.1.148、Managed Agents 自架沙箱文件、DeepSeek 全棧競品、$6,000 帳單事件、Karpathy 加入 Anthropic、多個新工具）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.148 版本表、更新 現況 最新版本、新增 2026-05-22 歷史記錄
  - `entities/managed-agents.md`：新增 2026-05-22 自架沙箱完整文件發布歷史記錄
  - `topics/competitor-landscape.md`：DeepSeek Clone 區塊升級為 DeepSeek 正式競品條目；新增 Alibaba Qwen3.7-Max；新增 2026-05-22 時序
  - `topics/community-tech-tools.md`：新增 11 個工具（Runtime、agent-teamflow、Runner、Proof Loop、agent-estimate、engramx、DPlex、Mneme HQ、ChunkHound v5.1、videowright、QA Skills）；更新痛點洞察表
  - `topics/community-tech-patterns.md`：新增 2026-05-22 時序（Spec-Driven Dev、agent fleet 5 步驟、CLAUDE.md 自我演化、Angular 13 規則、零 NPM 插件）
  - `topics/community-tech-discussions.md`：新增 3 個熱門討論（LLMs 虛假忙碌、逐行審查文化、CLAUDE.md 自我演化）；新增 2 個技術彙整條目
  - `topics/enterprise-cost-management.md`：新增 $6,000 個人事件案例；新增 Karpathy 最小 context 原則；新增 2026-05-22 時序
  - `wiki/feature-radar.md`：自架沙箱熱度升至 🔥🔥🔥🔥（文件完整發布）
- 新增 entities：`entities/andrej-karpathy.md`（Karpathy 加入 Anthropic，待官方核實）
- feature-radar 更新：自架沙箱完整文件發布，熱度升至 🔥🔥🔥🔥
- 呈現品質：
  - `entities/claude-code.md` ✅ 通過
  - `entities/managed-agents.md` ✅ 通過
  - `topics/competitor-landscape.md` ✅ 通過
  - `topics/community-tech-tools.md` ✅ 通過
  - `topics/community-tech-patterns.md` ✅ 通過
  - `topics/community-tech-discussions.md` ✅ 通過
  - `topics/enterprise-cost-management.md` ✅ 通過
  - `wiki/feature-radar.md` ✅ 通過
  - `entities/andrej-karpathy.md` ✅ 通過

---

## 2026-05-21 Lint

- 修正矛盾：無
- 補連結：無（project-deal.md 已於前次 session 補上連結，確認非孤立）
- 狀態更新：無（所有 ongoing/monitoring 頁面均在 14 天閾值內）
- 遷移至 entities：無
- 新增 entities：無
- 呈現品質：
  - `entities/opus-4-7.md` ⚠️ 已修復：「Claude Code 高 Token 模式」條目誤置於 ## 相關議題，已移至 ## 社群觀點
  - `topics/official-community-gap.md` ⚠️ 已修復：移除 LLM 操作指令「每次 ingest 後評估…」（移至 CLAUDE.md 規則）
  - `topics/ai-agent-safety.md` ⚠️ 已修復：合併 ## 技術彙整（新增）至主要 ## 技術彙整，消除重複標題
- 超長頁面（> 500 行）：`topics/community-tech-patterns.md`（682 行）— 使用者選擇稍後處理（📋 待辦）
- CLAUDE.md 健檢：
  - 行數：352 行（原 406 行，本次簡化後；閾值 150 行）
  - 矛盾：無
  - 引用驗證：`**靈感來源：**` 欄位在 community-tech-patterns.md 未找到 → 已修正規則說明（patterns.md 用主題段落格式，不需補此欄位）
  - 遵守率：呈現品質審查 0/3（log 未含標記）→ 已修正：新增 log.md 呈現品質欄位規定
  - 過期規則（> 60 天）：無（最舊規則 [加入: 2026-04-25] = 26 天）
  - 簡化：已執行（壓縮「快速上手」+ 「聚合器 Pipeline 架構」章節，節省 54 行）
- overview.md：已更新（2026-05-15 → 2026-05-21，涵蓋 Stainless 收購、deeplink RCE、.env SQLite 漏洞、Claude Design 上線）

---

## 2026-05-21 Ingest | news/2026-05-21.md

- 來源日報：`news/2026-05-21.md`（35 則，含 v2.1.146、sandbox bypass #2、Opus 退化、vibe-skill、SEO poisoning）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.146（/code-review 更名、auto mode AskUserQuestion）+ sandbox bypass #2 null byte + Opus 4.6 extended thinking 移除
  - `topics/ai-agent-safety.md`：新增 2026-05-21（sandbox bypass #2 + SEO poisoning EclecticIQ）
  - `topics/code-quality-decline.md`：新增 2026-05-21（Opus 3 週結構化記錄）
  - `topics/community-tech-tools.md`：新增 5 工具（atrium、clarp、vibe-skill、Claude Orchestra、the-knowledge-guy）+ 痛點洞察更新
  - `topics/community-tech-discussions.md`：HTML vs Markdown 熱度升至 🔥🔥🔥🔥🔥，模式改為 🌊延燒
  - `entities/pricing.md`：新增 2026-05-21（clarp、vibe-skill、atrium 等 6/15 應對方案）
  - `topics/competitor-landscape.md`：新增 2026-05-21（vibe-skill 多 LLM 分流 + DeepSeek harness 招募）
  - `topics/community-tech-patterns.md`：新增 2026-05-21 時序（vibe-skill、Claude Orchestra、atrium、the-knowledge-guy）
  - `wiki/feature-radar.md`：新增 /code-review 指令（v2.1.146）；HTML 熱度升至 🔥🔥🔥🔥🔥
- 呈現品質：
  - `entities/claude-code.md` ✅ 通過
  - `topics/ai-agent-safety.md` ✅ 通過
  - `topics/code-quality-decline.md` ✅ 通過
  - `topics/community-tech-tools.md` ✅ 通過
  - `topics/community-tech-discussions.md` ✅ 通過
  - `entities/pricing.md` ✅ 通過
  - `topics/competitor-landscape.md` ✅ 通過
  - `topics/community-tech-patterns.md` ✅ 通過
  - `wiki/feature-radar.md` ✅ 通過
- 新增 entities：無
- feature-radar 更新：已更新（/code-review 新增；HTML 熱度調升）

---

## 2026-05-20 Schema 升級 | community-tech-tools 表格重構

- 變更：`topics/community-tech-tools.md` 工具表格 schema 調整
  - 移除 `活躍` 欄（🟢/🟡/🔴 指標）：舊指標測量「最近是否出現在日報」，但常用工具本就不頻繁出現，導致全部顯示過期，設計缺陷
  - 新增 `首次出現` 欄（YYYY-MM-DD）：記錄工具首次進入 wiki 的日報日期，提供時間脈絡
  - 工具名稱新增可點擊連結：格式 `[**ToolName**](url)`，URL 從日報原文擷取；無 URL 者保持 `**ToolName**`
  - 移除重複的 Semble 條目（原在兩處出現，合併為一，首次出現更正為 2026-05-04）
- 更新：`CLAUDE.md` 新增 `community-tech-tools 工具新增規則` 章節，規範未來 ingest 時的工具欄格式（含 URL 取得方式、首次出現日期、採用初始值）
- 統計：共 ~90 個工具條目已完成格式更新；有 URL 的工具約 30 個，其餘填 `—` 待後續補充

---

## 2026-05-20 Ingest

- 來源日報：[[news/2026-05-20]]
- 更新頁面：
  - `entities/claude-code.md`（新增 v2.1.145；新增攝影機存取問題與 RCE deeplink 至已知問題；更新最後更新日期）
  - `entities/stainless.md`（重大更新：服務關閉公告；新增 Ironic 替代方案；更新狀態與歷史記錄）
  - `topics/ai-agent-safety.md`（新增 2026-05-20 時序：RCE deeplink 廣泛報導、攝影機存取議題持續；更新最後更新日期）
  - `entities/opus-4-7.md`（新增 2026-05-20：Claude Code max effort 優異 vs 一般對話體驗弱化分歧）
  - `topics/community-tech-tools.md`（新增 5 工具：TokenShield、Logbox、PrismoDev、claude-autopilot、mdviewer）
  - `topics/community-tech-patterns.md`（新增 2026-05-20 時序：engramx 89.1% token 減少、repo 架構護欄、35 agent 協調、multi-agent review 41% 不一致）
  - `topics/community-tech-discussions.md`（HTML vs Markdown 更新為 🌋重燃 + 熱度 +1；新增 multi-agent review 可靠性、auto-memory 副作用、skill creator economy 討論）
  - `entities/pricing.md`（新增 2026-05-20：Claude Code 定價溝通混亂事件 Simon Willison 分析）
  - `wiki/feature-radar.md`（新增 HTML 輸出官方背書、claude agents --json；更新全覽表）
- 新增頁面：無
- 摘要：今日最重要事件為 Stainless 收購後隨即宣布服務關閉（9 月停止對外服務，OpenAI/Google 等客戶急尋替代），Claude Code RCE deeplink 漏洞持續報導，Anthropic 官方 Blog 正式背書 HTML 取代 Markdown 作為 agent 輸出格式（設計策略轉向），claude agents --json 新增多層 agent 識別能力。社群工具爆發（TokenShield/Logbox/PrismoDev）聚焦 token 節省，multi-agent review 可靠性遭實測挑戰（41% 不一致）

---

## 2026-05-19 新頁面建立

- 新增頁面：`entities/stainless.md`
- 原因：Anthropic 宣布收購 Stainless（傳聞 $300M+），首次出現且為重大企業事件，具體業務（官方 SDK + MCP 伺服器生成）構成戰略基礎設施
- 更新：`wiki/index.md`（頁面數 26→27，新增目錄條目）

---

## 2026-05-19 Ingest

- 來源日報：[[news/2026-05-19]]
- 更新頁面：
  - `entities/stainless.md`（新建：Anthropic 收購 Stainless，$300M+，MCP 伺服器生成能力戰略意義）
  - `topics/ai-agent-safety.md`（新增 2026-05-19 時序：.env SQLite 明文、webcam 存取疑慮、RCE deeplink 跟進報導；新增技術彙整：.env SQLite 明文存儲；更新目前結論）
  - `entities/claude-code.md`（新增 v2.1.144；更新版本歷史 2026-05-19；更新最後更新日期）
  - `entities/managed-agents.md`（新增 2026-05-19：自架沙箱 + MCP 隧道；核心功能表格新增 4 項）
  - `entities/pricing.md`（新增 2026-05-19：臨時 5h x2 + 50% 週上限提升；企業成本壓力持續）
  - `topics/enterprise-cost-management.md`（新增 2026-05-19 時序：Microsoft 六個月內測揭露、企業帳單三倍 HN 討論；更新目前結論）
  - `topics/competitor-landscape.md`（新增 2026-05-19 時序：Microsoft 內部測試全貌 dev.to 深度揭露）
  - `topics/community-tech-tools.md`（新增 3 工具：Claude Soul、cdesktop、InsForge）
  - `topics/community-tech-patterns.md`（新增 2026-05-19 時序：1000h 工作流、SEO pipeline、Android 惡意軟體 RE、Anthropic 內部報告、新工具）
  - `topics/community-tech-discussions.md`（新增 3 討論：MCP context bloat 量化、Claude 隱藏 bug、靜默失敗五種模式；新增 MCP Context Bloat 技術彙整）
  - `wiki/feature-radar.md`（新增自架沙箱 + MCP 隧道 + /resume 兩個功能條目；更新全覽表）
- 新增頁面：`entities/stainless.md`
- 摘要：今日最重要事件為 Anthropic 收購 Stainless（$300M+，MCP 伺服器生成控制權），Claude Code 安全多面爆發（.env SQLite 明文、webcam 隱私、RCE deeplink 持續報導），Microsoft 六個月內部測試全貌揭露（開發者愛它但財務殺了它），Managed Agents 自架沙箱 + MCP 隧道企業功能上線。社群首次量化 MCP context bloat（9 伺服器 = 38k tokens），AI 工具可靠性問題（靜默隱藏 bug、靜默失敗）密集出現。

---

## 2026-05-18 新頁面建立

- 新增頁面：`topics/enterprise-cost-management.md`
- 原因：企業規模 Claude 成本管理議題跨越多天且升至財經媒體層級，現有 pricing.md（政策面）與 community-tech-patterns.md（個人工法面）均未覆蓋「企業採用成本結構挑戰」此角度
- 更新：`wiki/index.md`（頁面數 25→26，新增目錄條目）

---

## 2026-05-18 Ingest

- 來源日報：[[news/2026-05-18]]
- 更新頁面：
  - `topics/ai-agent-safety.md`（新增 2026-05-18 時序：Claude Code RCE via deeplink；新增技術彙整；更新目前結論）
  - `topics/competitor-landscape.md`（新增 2026-05-18 時序：Microsoft 遷移媒體確認、Uber 預算 Forbes 報導、Codex 超越文章、混搭工作流）
  - `entities/managed-agents.md`（新增 2026-05-18：Proactive Workflows + Capability Curve 官方公告）
  - `entities/pricing.md`（新增 2026-05-18：Uber 企業成本警示、Opus+Sonnet 混合策略）
  - `topics/community-tech-tools.md`（新增 6 工具：Semble、AnyFrame、Agetor、agent-baton、LockedIn、Claude Usage Widget）
  - `topics/community-tech-patterns.md`（新增 2026-05-18 時序：角色分工 6.7 倍加速、多操作員架構、速率上限轉移、62.5 分鐘 cache 規則、逆向工程惡意軟體）
  - `topics/community-tech-discussions.md`（新增 3 討論：/compact 設計決策遺忘、知識圖譜實際效益存疑、14 條反駁規則工具包）
  - `wiki/feature-radar.md`（新增 Proactive Workflows + Capability Curve 條目；更新全覽表）
- 新增頁面：無
- 摘要：今日最重要事件為 Claude Code RCE deeplink 漏洞（第三個 RCE 類漏洞）、Microsoft 遷移至 Copilot CLI 獲主流媒體確認、Uber 企業成本案例登上 Forbes、Proactive Workflows 官方公告。社群湧現 6 個新工具，聚焦速率監控與 Agent 沙盒。/compact 設計決策遺忘和知識圖譜效益存疑是本日最具反思價值的討論。

---

## 2026-05-17 Ingest（補充 2）

- 來源日報：[[news/2026-05-17]]
- 更新頁面：
  - `topics/community-tech-tools.md`（新增 4 個工具：machine、cv-claw、shipcheck、Gonfire；更新最後更新日期至 2026-05-17）
  - `topics/community-tech-patterns.md`（補充 2026-05-17 新工具列表：加入 machine、cv-claw、Gonfire）
- 新增頁面：無
- 摘要（補充 2）：工具目錄補入今日 Show HN 新工具——machine（per-project VM 安全隔離）、cv-claw（Skill 履歷生成器）、shipcheck（session log 費用與安全審計）、Gonfire（session log 面試評估）。

## 2026-05-17 Ingest（補充）

- 來源日報：[[news/2026-05-17]]
- 更新頁面（補充本次第一次 ingest 遺漏項目）：
  - `entities/claude-code.md`（補入：Anthropic API 500 Internal Server Error 已知問題、shipcheck 工具至費用監控列表、Gonfire 工具至工作流輔助列表、版本歷史 2026-05-17 補充條目）
  - `entities/opus-4-7.md`（新增 2026-05-17：Claude 4.7 vs 4.6 使用場景社群共識形成；更新最後更新日期）
  - `topics/competitor-landscape.md`（新增 2026-05-17 時序：Microsoft 授權取消 techbuzz.ai 報導 + Adobe Lightroom Linux 移植正向案例；更新最後更新日期）
- 新增頁面：無
- 摘要（補充）：Microsoft 授權取消故事由非主流媒體再度報導（可信度待核實）；Claude 4.7 vs 4.6 使用場景共識在社群清晰化（4.7=結構化任務，4.6=探索性寫作）；Anthropic API 500 跨模型服務中斷事件記錄；兩款 session log 分析新工具（shipcheck 安全審計、Gonfire 面試評估）補入工具目錄。

## 2026-05-17 Ingest

- 來源日報：[[news/2026-05-17]]
- 更新頁面：
  - `entities/claude-code.md`（新增 2026-05-17：Adobe Lightroom Linux 移植案例、持久性自主 agent 系統、Claude Skills 靜默覆蓋問題、context 管理 4 工具、多帳號合規紅線、shipcheck 新工具；更新最後更新日期）
  - `entities/pricing.md`（新增 2026-05-17：`claude -p` 計費衝擊持續、多帳號架構合規邊界明確）
  - `topics/community-tech-patterns.md`（新增 2026-05-17 時序：Skills-as-dotfiles + 子代理派生、Generator-Evaluator 12 輪對抗迭代、持久性自主 agent 系統、context 4 工具實踐、CSS 規格先行設計稿轉碼、100 平行 agent 行銷診斷、SSH + Claude Chat 伺服器存取、Grounded Code 方法論系列、Adobe Lightroom Linux 移植、shipcheck 新工具）
  - `topics/community-tech-discussions.md`（新增 CLAUDE.md/AGENTS.md 維護效益辯論、Claude Skills 靜默覆蓋兩個新討論；更新 Context 管理熱度 🔥🔥→🔥🔥🔥、模式 ☄️閃現→🌊延燒；新增 Skills 機制邊界技術彙整；新增 2026-05-17 時序）
  - `topics/official-community-gap.md`（新增 2026-05-17 Ingest 更新：Skills 透明度缺口新證據、CLAUDE.md 失效缺口持續驗證）
  - `wiki/feature-radar.md`（更新最後更新日期；本日無官方新功能發布）
- 新增頁面：無
- 摘要：Claude Skills 靜默覆蓋指令與子代理派生問題為本日最熱門技術議題，呼應官方社群缺口矩陣「CLAUDE.md 規則失效」欄位；CLAUDE.md/AGENTS.md 維護效益辯論（HN）引發廣泛共鳴；社群自主 agent 工程達高複雜度里程碑；context 管理 4 工具實踐廣泛流傳；多帳號 ToS 合規紅線明確。

---

## 2026-05-16 Ingest

- 來源日報：[[news/2026-05-16]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.143 plugin 依賴強制執行；GitHub Copilot 新應用競爭；Anthropic 尋找下一個突破性產品；新工具：Code Quest、CostHawk、AI 引用稽核 MCP、answering machine MCP；更新現況與版本歷史）
  - `entities/pricing.md`（新增 2026-05-16：Max 20x 用量上限未生效數學實證、社群促銷時序整理、Lanes.sh 影響範圍說明、費用焦慮集體高峰、週配額意外重置 bug、「credit 包裝漲價」批評）
  - `entities/managed-agents.md`（新增 2026-05-16 歷史記錄：dev.to Dreaming 機制深度技術分析）
  - `topics/competitor-landscape.md`（新增 2026-05-16 時序：GitHub Copilot 新應用明確對標 Claude Code、Anthropic 尋找下一個突破性產品；更新摘要）
  - `topics/community-tech-discussions.md`（新增「harness 變差了」辯論、Agentic RAG + eval harness 兩個新討論；更新熱門討論表格、技術彙整、時序）
  - `topics/community-tech-patterns.md`（新增 2026-05-16 時序：費用焦慮高峰、Custom base URL、Agentic RAG、X 演算法文件化、非工程師 MCP 六個月心得；新增 Code Quest / CostHawk 工具）
  - `wiki/feature-radar.md`（新增 v2.1.143 Plugin 依賴關係強制執行條目；更新全覽表）
- 新增頁面：無
- 摘要：Claude Code v2.1.143 plugin 依賴強制執行為最重要技術更新；GitHub Copilot 正面對標 Claude Code 是競品競爭升級訊號；6/15 計費後遺症延燒（Max 用量上限未生效數學實證、促銷透明度質疑、費用優化文章集中爆發）；「harness 變差了」論點為近期「Claude Code 退步感」提供結構性反論。

---

## 2026-05-15 Ingest

- 來源日報：[[news/2026-05-15]]
- 更新頁面：
  - `entities/pricing.md`（新增 2026-05-15：社群情緒分析（60% 負面）、第三方工具衝擊（Zed/Conductor/Superset）、Ars Technica 官方訪談、VS Code 計費歸屬不明、Ungate 工具 ToS 風險）
  - `entities/claude-code.md`（v2.1.142 `claude agents` 8 旗標；「Claude Code at Scale」官方大型 codebase 指南；Microsoft 取消內部授權；新工具 PlanBridge/my-time-has-come/Ungate；更新現況說明）
  - `topics/competitor-landscape.md`（新增 2026-05-15 時序：Microsoft 取消授權轉推 Copilot CLI；Anthropic 企業採用率首次超越 OpenAI（34.4% vs 32.3%）；第三方工具分化；摘要更新）
  - `topics/community-tech-patterns.md`（新增 2026-05-15 時序：MCP 麥克風語音整合/破壞性操作安全閘門/長期 auto-memory 品質管理/平行子代理成本分析/monk 靜默模式 skill/PlanBridge 行內評審/CLAUDE.md 精簡反思/Claude Code vs Cursor 比較）
  - `topics/ai-agent-safety.md`（新增 2026-05-15 時序：「Claude 刪除專案」安全閘門/長期記憶退化/35 天 ERP 靜默失敗模式）
  - `wiki/feature-radar.md`（新增 `claude agents` v2.1.142 細粒度旗標條目 🔥🔥；更新全覽表）
- 新增頁面：無
- 摘要：Anthropic 6/15 計費變更持續延燒（第三方工具分化、60% 社群負評、官方訪談補充說明）；Microsoft 取消內部 Claude Code 授權轉推 Copilot CLI 標誌企業市場首次正面競爭；Ramp AI Index 首次顯示 Anthropic 企業採用率超越 OpenAI（34.4% vs 32.3%）；社群大量湧現記憶管理、安全防護與 Token 節省工具。

---

## 2026-05-14 Ingest

- 來源日報：[[news/2026-05-14]]
- 更新頁面：
  - `entities/pricing.md`（2026-05-14 重大政策：6/15 起 programmatic 用量剝離訂閱方案，改為信用池（Pro $20 / Max 5x $100 / Max 20x $200），按完整 API 費率計費；週限制臨時提高 50% 至 7/13；claude-pee 繞過工具出現；開發者強烈反彈及轉換競品）
  - `entities/claude-code.md`（v2.1.141 terminalSequence + CLAUDE_CODE_PLUGIN_PRE；/loop・/batch・/background 官方文件上線；Cat Wu 訪問 AI 主動性論述；新工具：Ledger/Clawdmeter/Grafana Dashboard/agent-html-skills/Lanes v0.39；版本歷史 2026-05-14 兩條、2026-05-13 v2.1.141 一條）
  - `entities/openclaw.md`（狀態更新：受限→允許（信用池計費）；新增 2026-05-14 事件：恢復允許但改走信用池）
  - `wiki/feature-radar.md`（/goal 熱度升至 🔥🔥🔥🔥🔥；新增 /loop・/batch・/background 條目 🔥🔥🔥🔥；更新全覽表）
  - `topics/community-tech-patterns.md`（新增 2026-05-14 時序：費用可觀測性工具爆發/多 LLM 混合架構/claude-pee PTY 繞過/雙向 HTML 工件/週末 PoC/commit 學習技能；新增技術彙整：費用可觀測性工具、多 LLM 混合架構條目）
  - `topics/competitor-landscape.md`（新增 2026-05-14 時序：政策驅動分流 + 多 LLM 混合策略）
- 新增頁面：無
- 摘要：Anthropic 宣布 6/15 起 programmatic 用量全面剝離訂閱方案（信用池制）為最大事件，引發開發者強烈反彈、claude-pee 繞過工具誕生、多 LLM 混合策略討論加速；官方 /loop・/batch・/background 指令文件同步上線，標誌 Claude Code 正式轉向 agent 開發平台定位。

---

## 2026-05-13 Lint

- 修正矛盾：
  - `overview.md`：全面重寫（反映 2026-05-08 至 2026-05-13 共 5 天重大事件，原版停在 2026-05-08）；新增「功能試用推薦」快速查閱表格；更新競品數據（157K OpenCode）、算力到位（SpaceX Colossus 1）、安全事件（假冒安裝包 + 90% 漏洞評測）
- 補連結：
  - `entities/claude-security.md` → 新增頂部 feature-radar 熱度標籤（🔥🔥🔥 / ⚡）與 [[feature-radar]] 連結
  - `wiki/overview.md` → 在社群工具生態與功能試用推薦區塊補上 [[feature-radar]] 連結（共 2 處）
  - `topics/community-tech-patterns.md` → 確認已有 [[entities/claude-design]] 連結（lint 前已正確）
- 狀態更新：
  - `topics/anthropic-government-policy.md`：`ongoing` → `monitoring`（2026-05-02 至今 11 天無新進展，白宮談判狀態不明）
- 遷移至 entities：無
- 新增 entities：無（掃描所有頁面，無未建頁面被提及 3+ 次的新名稱）
- feature-radar.md 更新：
  - Agent View 條目補充 v2.1.140 `subagent_type` 不敏感匹配改善
  - Managed Agents 條目補充 Boris Cherny 數千子代理工作流（2026-05-13）
  - Claude Security 試用價值升級：⏳ 觀望 → ⚡ 有條件推薦（AI 生成程式碼 90% 漏洞評測確認資安審查需求，熱度 🔥🔥 → 🔥🔥🔥）
  - 全覽表 Claude Security 欄同步更新
- overview.md：已全面重寫（反映 2026-04-25 至 2026-05-13 局勢，含 agentic AI 生產化加速、安全信任多點爆發、分流訊號具體化）

---

## 2026-05-13 Ingest

- 來源日報：[[news/2026-05-13]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.140 subagent_type 大小寫不敏感匹配改善；Boris Cherny 數千個子代理工作流報導；Dragoman/Cocall.ai/Claudy macOS session 管理版/PullMD v2.4.1 新工具；AI 生成程式碼 90% 安全漏洞研究警示；版本歷史 2026-05-13 三條）
  - `entities/boris-cherny.md`（新增：每晚數千個 AI 子代理工作流公開報導（2026-05-13）；更新最後更新日期）
  - `entities/pricing.md`（新增：Anthropic 定價主導權強勁——The Information 報導企業客戶吸收成本上漲）
  - `entities/managed-agents.md`（現況補充 Boris Cherny 數千子代理工作流 + v2.1.140 改善；歷史記錄 2026-05-13）
  - `topics/ai-agent-safety.md`（新技術彙整三節：AI 生成程式碼 90% 安全漏洞評測 / 24 小時無監督 Agent 執行風險 / Context 壓縮安全指令保留；目前結論新增兩條；2026-05-13 時序三條）
  - `topics/community-tech-patterns.md`（新技術彙整五節：多模型路由 Dragoman / 電話 MCP Cocall.ai / Token Bloat 精簡策略 / 大規模子代理工作流 / AI 生成程式碼安全審查；熱門應用新增 Dragoman/Cocall.ai；2026-05-13 時序）
- 新增頁面：無
- 摘要：Claude Code 創始人 Boris Cherny 公開「數千個夜間子代理」工作流成為本週最受矚目的 agentic AI 案例；AI 生成程式碼安全漏洞大規模評測（48 應用 90% 有漏洞）直接挑戰快速開發上線假設；v2.1.140 的 subagent_type 大小寫不敏感匹配降低多代理配置摩擦；Anthropic 定價強勁（企業客戶吸收成本上漲）標誌市場競爭力持續擴大。

---

## 2026-05-13 Schema 升級 | Feature Radar 新增

- 新增頁面：`wiki/feature-radar.md`（功能熱度雷達，含熱度評分、試用推薦、快速上手指南）
- 更新頁面：`entities/managed-agents.md`（新增「熱度與試用價值」、「使用指南」區塊，包含 `/goal`、Agent View、Python/TypeScript SDK 範例）
- 更新 `wiki/index.md`（新增 feature-radar 入口，頁面數 21）
- 更新 `CLAUDE.md`（schema 新增 feature-radar 更新規則、feature entity 必填區塊規範）
- 摘要：建立功能熱度追蹤系統，未來每次 ingest 自動維護；已回填 2026-04-25 至 2026-05-12 期間共 13 項功能的熱度評分與試用推薦

---

## 2026-05-12 Ingest

- 來源日報：[[news/2026-05-12]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.139 Agent View + `/goal`；假冒安裝包 IElevator 攻擊；服務中斷；UiPath/Signadot 整合；ESP32 Fault Injection 研究；OpenCode 157K 分流；checkpoint commits 污染 git history 已知問題；新工具：HiveTerm/Writ/Agent FM/Usage4Claude 3.0.0/ltm；版本歷史 2026-05-12 四條）
  - `entities/pricing.md`（Ultra Review $100–140 vs $5–20 費用透明度爭議；Max 5x 正常月 $159 vs 高峰月 $6,600 ROI 分析；第三方平台 ToS 風險討論）
  - `entities/managed-agents.md`（Agent View + `/goal` 加入核心功能表；現況補充 v2.1.139 非同步工作流能力；歷史記錄 2026-05-12）
  - `topics/ai-agent-safety.md`（新技術彙整：假冒安裝包 IElevator 機制 + AI 驅動硬體 Fault Injection；目前結論新增兩條；2026-05-12 時序）
  - `topics/community-tech-patterns.md`（新技術彙整 5 節：/goal fire-and-forget/對抗性審查/Writ Neo4j Pipeline/ltm 跨環境記憶/Context 管理瓶頸/Checkpoint Commits；熱門應用新增：HiveTerm/Writ/Agent FM/Usage4Claude 3.0.0/ltm；2026-05-12 時序）
  - `topics/competitor-landscape.md`（OpenCode 157K 開發者數據更新；UiPath/Signadot 整合；摘要更新；2026-05-12 時序）
- 新增頁面：無
- 摘要：v2.1.139 的 Agent View + `/goal` 指令是 Claude Code 邁向真正非同步多 agent 工作流的關鍵里程碑；假冒安裝包（IElevator 機制）與 Google 廣告木馬並存，Claude Code 安裝路徑的供應鏈攻擊態勢持續升級；逾 15.7 萬開發者轉向 OpenCode 是目前最具體的競品分流量化數據；Ultra Review 費用透明度（$100–140 vs 宣傳的 $5–20）延續 Anthropic 計費信任危機；AI 驅動 ESP32 Fault Injection 攻擊是 AI 自主硬體安全研究能力的里程碑案例。

---

## 2026-05-11 Ingest

- 來源日報：[[news/2026-05-11]]
- 更新頁面：
  - `entities/managed-agents.md`（正式發布升格狀態；社群 70 天自建多代理架構案例；官方 vs 社群架構比較進入主流討論；2026-05-11 歷史記錄）
  - `entities/claude-code.md`（現況補充 Managed Agents 正式發布 + Desktop vs Cowork 定位混淆 + 插件生態密集爆發；新工具：adamsreview / vibe-log-cli / academic-research-skills；版本歷史 2026-05-11）
  - `entities/opus-4-7.md`（新增已知問題：Opus 4.7 提示詞行為世代性轉變，4.7 更趨字面解讀，4.6 通用指令效果下降）
  - `entities/pricing.md`（新增：Pro 方案 0% 使用量仍被收取 $3.37 extra usage；$514/30 天費用分析 + 配額管理指南）
  - `topics/community-tech-patterns.md`（新增技術彙整：Judge Gate 語意級品質驗證 / AI agent 語意漂移 CI 測試 / 多代理 PR review / CLAUDE.md 記憶驗證兩招 / AGENTS.md 跨工具插件簡報 / agent skill 商業價值評估；熱門應用新增 adamsreview / vibe-log-cli；2026-05-11 時序）
- 新增頁面：無
- 摘要：Managed Agents 本週正式發布標誌官方 multi-agent 托管服務進入正式階段；Claude Code 費用管理成為最熱議焦點（$514/30 天分析、Pro 0% 仍被收費、配額透明度問題）；「Judge Gate」概念揭示自主編程代理語意驗證盲點；Opus 4.7 提示詞行為世代性轉變（更趨字面）確認，所有現有 prompt 工程實踐需重新審視。

---

## 2026-05-10 Ingest

- 來源日報：[[news/2026-05-10]]
- 更新頁面：
  - `entities/claude-code.md`（CLAUDE.md 作為 candidate-context 架構揭示；Claude Code Sandboxing 官方文件；Google 搜尋木馬仿冒事件；Lobotomized Claude Code 社群工具；新工具：Remind/draft CLI plugin/Tokenyst/Agentize；已知問題新增 CLAUDE.md candidate-context；版本歷史新增 2026-05-10 兩條）
  - `entities/pricing.md`（Opus API 速率限制調降；Pay-as-you-go session 費用 $6–10 成因與壓低策略）
  - `topics/ai-agent-safety.md`（新增技術彙整：Google 搜尋廣告詐騙與木馬/AI agent 清空資料庫兩次+指令防火牆/Claude Code Sandboxing 官方文件；更新目前結論加入供應鏈攻擊警示；2026-05-10 時序）
  - `topics/community-tech-patterns.md`（新增技術彙整：本機圖資料庫降低 session token 成本/multi-agent 研究調查團隊/Claude Code 架構解析系列/三層疊加式 AI Code Review；熱門應用新增 Remind/draft CLI plugin/Snyk+Claude Code/Tokenyst/Agentize；2026-05-10 時序）
- 新增頁面：無
- 摘要：Google 搜尋廣告出現 Claude Code 木馬仿冒網站（已有用戶中招）是最大安全事件；CLAUDE.md 作為 candidate-context 的架構揭示直接解釋「指令被忽略」的長期痛點；Anthropic 發布 Sandboxing 官方文件；Opus API 速率限制調降與社群 session 費用控管方案同步浮現。

---

## 2026-05-09 Ingest

- 來源日報：[[news/2026-05-09]]
- 更新頁面：
  - `entities/claude-code.md`（Windows IDE 擴充套件 Windows 全面無法載入事件；v2.1.136 操作安全+如實回報機制 +525 tokens + `hard_deny` 類別；v2.1.138 internal fixes；新工具：re_gent/unitmux/obsidian-semantic；已知問題新增 Windows IDE 擴充套件失載）
  - `entities/pricing.md`（SpaceX Colossus 1 正式到位確認：300MW 電力 + Claude API 速率上限加倍，更新標題至 2026-05-09）
  - `topics/ai-agent-safety.md`（新增技術彙整：v2.1.136「操作安全與如實回報」機制；2026-05-09 時序：`hard_deny` 類別 + 不可逆操作確認 + 如實回報義務）
  - `topics/community-tech-patterns.md`（新增技術彙整：HTML vs Markdown 輸出格式辯論/PostToolUse 稽核日誌模式/Git Hooks 強制代碼品質/re_gent AI agent 版本控制/54 ADR 35 天/obsidian-semantic 語義 vault 搜尋；熱門應用新增 re_gent/unitmux/obsidian-semantic；2026-05-09 時序）
  - `topics/code-quality-decline.md`（新增技術彙整：靜默模型切換 silent model switching + 11.5 倍效率差距；2026-05-09 時序）
- 新增頁面：無
- 摘要：Anthropic 正式接入 SpaceX Colossus 1 220,000 GPU 為最大基礎設施事件；v2.1.136「操作安全與如實回報」（+525 tokens + `hard_deny`）是 agent 行為規範的實質性收緊；Windows IDE 擴充套件再度全面失效（Linux 路徑硬編碼）；HTML vs Markdown 輸出格式辯論與靜默模型切換（11.5 倍效率差距）為本日兩大社群技術話題。

---

## 2026-05-08 Lint

- 修正矛盾：
  - `entities/google-investment.md`：移除重複的 2026-04-27 時序條目（內容完全重複，保留第一份）
  - `entities/pricing.md`：`最後更新` 欄位從 2026-05-07 更正為 2026-05-08（2026-05-08 ingest 有更新此頁）
- 補連結（孤立頁面修正）：
  - `topics/community-tech-patterns.md` → 在「相關實體」補上 `[[entities/managed-agents]]`（新頁面 2026-05-07 建立後未反映在此頁）
  - `entities/claude-code.md` → 在「相關議題」補上 `[[entities/boris-cherny]]`
- 狀態更新：無
- 遷移至 entities：無（`topics/google-investment.md` 已在上次 lint 遷移）
- 新增 entities：
  - `entities/boris-cherny.md`（Claude Code 創始人，10+ 次跨頁提及，涵蓋 Loops 設計哲學、「coding is solved」論戰、4/23 事後報告、第三方工具邊界聲明）
- overview.md：已全面重寫（反映 2026-04-25 至 2026-05-08 局勢，含 CVE 安全危機、SpaceX 算力合作、Managed Agents 升級、競品壓力轉折點）

---

## 2026-05-08 Ingest

- 來源日報：[[news/2026-05-08]]
- 更新頁面：
  - `entities/claude-code.md`（CVE-2026-39861 CVSS 7.7 沙箱逃逸漏洞 + 1-click RCE 信任危機；v2.1.133 `worktree.baseRef` 設定；Boris Cherny「coding is solved」/ 反「vibe coding」；Claude Cowork Linux 沙箱啟動失敗；Claude Sonnet 4.8 外洩；新工具：Claudy/DataMoat/4-agent Code Review/awesome-ux-skills；已知問題新增 CVE-2026-39861 與 Cowork 沙箱故障）
  - `entities/pricing.md`（SpaceX Colossus 220,000 GPU 細節補充；2026-05-08 多媒體跟進報導確認）
  - `entities/mythos.md`（新增：CVE 諷刺觀察——Mythos 未能預警自家產品漏洞，成社群質疑安全一致性的新論據）
  - `topics/ai-agent-safety.md`（新增技術彙整：CVE-2026-39861 細節 + 1-click RCE 信任危機；更新目前結論；2026-05-08 時序：CVE/RCE/DataMoat 防禦工具）
  - `topics/community-tech-patterns.md`（新增技術彙整：本機持久化記憶 39ms/120 提示詞模式實證研究/3.77億 token 極端案例/三種整合模式框架/Boris Cherny 術語演化；更新熱門應用：Claudy/DataMoat/4-agent Code Review/awesome-ux-skills/OpticOdds MCP；2026-05-08 時序）
- 新增頁面：無
- 摘要：CVE-2026-39861（CVSS 7.7）沙箱逃逸 + 1-click RCE 信任危機是最大安全事件，Anthropic「責怪使用者」的回應態度加劇批評；SpaceX Colossus 220,000 GPU 算力合作細節確認；Boris Cherny「coding is solved」+ 反「vibe coding」在多平台引發社群兩極反應；120 提示詞模式實證研究是本日最具方法論價值的社群貢獻。

---

## 2026-05-07 Ingest

- 來源日報：[[news/2026-05-07]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.132 發布；Managed Agents 重大更新 Dreaming/20路/Outcomes；Python SDK v0.100.0 + TypeScript SDK v0.95.0；SpaceX 算力合作速率翻倍；Wire trace 揭示 13K 基礎提示詞；Bedrock 再次異常；授權撤銷後 session 持續出現；新工具：BrowserCode/跨session插件/recap/Kstack）
  - `entities/pricing.md`（SpaceX 算力合作：Pro/Max 五小時速率上限翻倍、取消尖峰降速、API Tier 4+ 提升；Max 5x 用戶週限制可能同步調高，待官方確認）
  - `topics/community-tech-patterns.md`（新技術彙整：Skill Atrophy 反思與對策、Managed Agents 架構模式、Wire Trace 架構侷限、Git Log 除錯首要步驟、MCP Code Execution Token 效率、跨 Session 通訊插件；熱門應用新增：BrowserCode/qu-ans插件/recap/Kstack/Claude Code Routines；2026-05-07 時序）
  - `topics/competitor-landscape.md`（DeepSeek V4 替換 Claude Opus 4 30 天實測；Cursor 全面轉換 Claude Code 六個月比較；2026-05-07 時序）
  - `topics/ai-agent-safety.md`（授權撤銷後 session 紀錄持續出現技術彙整；Wire Trace 揭示 Auto 模式安全邊界為提示詞層；2026-05-07 時序）
- 新增頁面：`entities/managed-agents.md`（Dreaming 記憶整合、20 路子代理並行、Outcomes 規格驗證，Code with Claude 大會重大更新）
- 摘要：Anthropic + SpaceX 算力合作為最大商業事件（Pro/Max 速率翻倍），Managed Agents 三大更新（Dreaming/20路/Outcomes）標誌 Agent 框架從無狀態轉有狀態，Wire trace 揭示 Auto 模式安全僅為提示詞層是最重要的安全資訊，社群 skill atrophy 反思與授權撤銷後 session 持續出現的安全隱患同步浮現。

---

## 2026-05-06 Ingest

- 來源日報：[[news/2026-05-06]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.131 緊急修復 Windows VS Code regression；Python/TypeScript SDK v0.99.0/v0.94.0 workspace 定向；Claude Code 121K stars；Claude Security 公開 Beta；新工具：Claudette、claude-smart、Dreamer；Boris Cherny「軟體工程已死」第二波）
  - `entities/pricing.md`（GitHub Copilot 27x Opus 加價比較；94% token 流向錯誤模型；工具迴圈帳單爆衝三案例：yarn.lock £400 + daemon $500）
  - `entities/claude-security.md`（dev.to 深度介紹文章，公開 Beta 媒體報導持續擴大）
  - `topics/competitor-landscape.md`（DeepSeek Claude Code clone 8,700 stars；DeepClaude 17x 成本替代方案；Claude Code 121K stars 里程碑；Boris Cherny 第二波論戰）
  - `topics/community-tech-patterns.md`（新技術彙整：Speculative Parallelism 工作流、Skills Unix 哲學、Hooks 強制執行機制、CLAUDE.md 語言規則集爆發、Agentic 組織協調挑戰、MCP Hub 模式、Self-improving rules；新工具：Claudette/claude-smart/Dreamer；2026-05-06 時序）
- 新增頁面：無
- 摘要：v2.1.131 緊急修復 Windows VS Code regression 為最大運維事件；費用管理危機多點同步爆發（Copilot 27x 加價、94% token 誤路由、工具迴圈爆衝）；DeepSeek clone 8,700 stars + DeepClaude 17x 低成本替代生態加速形成；CLAUDE.md 語言規則集爆發（5 個語言單日密集出現）標誌社群規範建立進入加速期。

---

## 2026-05-05 Ingest

- 來源日報：[[news/2026-05-05]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.128 發布；Amazon 全員部署 Claude Code；Boris Cherny「Loops 是未來」哲學；新工具：SprintiQ/Claude Relay/Memex/Claude-Find/Askdiff/Rudel）
  - `entities/pricing.md`（提示快取窗口縮短靜默改動；Ollama vs 訂閱成本比較熱議；token 降耗技巧主流化）
  - `entities/opus-4-7.md`（4.7 退步討論浮現；部分開發者回退 4.6）
  - `topics/competitor-landscape.md`（Codex 下載量首次超越 Claude Code 1397% 週增；Amazon 雙品牌並行部署；DeepClaude 替代方案發酵）
  - `topics/community-tech-patterns.md`（Boris Cherny Loops 哲學；多 session 工具鏈 Claude Relay/Memex/Claude-Find/Askdiff；Multi-agent CLAUDE.md 11 條衝突防範規則；Playwright CLI vs npx token 陷阱；token 降耗策略集中出現；LinkedIn skill human-in-the-loop 架構；Rudel session 分析）
  - `topics/code-quality-decline.md`（Opus 4.7 退步討論再升溫）
- 新增頁面：無
- 摘要：OpenAI Codex 單週下載量首次超越 Claude Code（+1397% vs -38%）是最大競爭事件；Anthropic 悄悄縮短提示快取窗口（未公告）延續透明度爭議；Amazon 雙品牌並行部署凸顯企業端多供應商策略成主流；社群工具呈現「session 管理工具鏈化」趨勢（Claude Relay + Memex + Claude-Find + Askdiff 四工具形成完整管理生態）。

---

## 2026-05-04 Ingest

- 來源日報：[[news/2026-05-04]]
- 更新頁面：
  - `entities/claude-code.md`（原始碼外洩/8100 DMCA/Claw-Code 新增；Claude Cowork 第三方 LLM 支援；Claude Connectors 擴展至創意工作軟體；新工具 Semble/Kirikiri/JupyterLab Extension/Prism MCP/claudely/Smithy/Patina；版本歷史 2026-05-04 條目更新）
  - `entities/pricing.md`（Pro 試用 7 天結束說明不一致；Amazon Bedrock 授權即時過期問題；Claude 5 小時滾動視窗機制與預排程技巧）
  - `topics/community-tech-patterns.md`（2026-05-04 時序：DeepClaude/Semble/Kirikiri/JupyterLab Extension/Prism MCP/claudely/Smithy/Patina/「放棄嗎重置效應」/CLAUDE.md for Java/Memtrace/Pilot Shell/Claude Connectors 創意工作；新技術彙整：Backend 替換模式、CLAUDE.md 防腐爛機制、Agent Context 新鮮度問題、結構化 Agent 框架設計、Agent Supervision 哲學；熱門應用表新增 8 項工具）
  - `topics/competitor-landscape.md`（2026-05-04 時序：Claude Desktop/Cowork 第三方 LLM 支援重大變化、Claude Connectors 創意工作軟體、Haiku 4.5 73.3% SWE-bench；摘要更新：競爭格局轉向多模型平台）
- 新增頁面：無
- 摘要：Claude Code 原始碼外洩引發 8100+ DMCA 與 Claw-Code 誕生為最大事件；Claude Cowork/Desktop 悄悄支援任意第三方 LLM 代表競爭格局從「Claude vs. others」轉向「多模型接入層」；社群工具生態新一波爆發（7 款新工具），CLAUDE.md 防腐爛與 Agent Context 新鮮度成為本週社群技術討論新主題。

---

## 2026-05-03 Ingest

- 來源日報：[[news/2026-05-03]]
- 更新頁面：
  - `entities/claude-code.md`（macOS computer use 功能上線；新工具 TradingAgents Plugin；版本歷史更新）
  - `entities/pricing.md`（帳單失控問題主流化；本地 LLM 替代失敗案例）
  - `entities/opus-4-7.md`（Fortify 安全掃描修復失敗；研究任務正面評價）
  - `topics/community-tech-patterns.md`（2026-05-03 時序：macOS computer use、91k ERP 案例、8 tips、雙代理 VPS 框架、K8s CLAUDE.md 規則、AI 命名一致性 OSS、TradingAgents Plugin、40 技能系統、開發者身份認同；新技術彙整：CLAUDE.md 領域化安全規則、AI 程式碼一致性、AI 大規模開發案例、Agent 持續運作架構；熱門應用表更新）
  - `topics/ai-agent-safety.md`（PowerShell.exe 重命名事件；帳單失控主流化；技術彙整新增 Windows 環境危險操作）
  - `topics/code-quality-decline.md`（4/23 事後報告 50+ 修復社群獨立驗證行動；目前結論更新）
- 新增頁面：無
- 摘要：Claude Code 加入 macOS computer use 能力為最大功能更新；社群主動問責 Boris Cherny 4/23 事後報告的 50+ 承諾修復；PowerShell.exe 重命名事件揭示 Windows 環境 agent 安全盲點；開發者身份認同議題持續發酵。

---

## 2026-05-02 Ingest（第二次，補充最新版日報）

- 來源日報：[[news/2026-05-02]]（本次為更新版日報，與第一次 ingest 所處理版本不同）
- 更新頁面：
  - `entities/claude-code.md`（新增已知問題：AGENTS.md 規範不支援 issue #6235；新工具：Governor、Caliber）
  - `entities/pricing.md`（Uber 企業案例：$500–$2,000/月/工程師，四個月燒光全年 AI 預算）
  - `topics/community-tech-patterns.md`（2026-05-02 時序：PreToolUse Hooks 四 exit code、Token 路由策略、Governor、Caliber、記憶體防漂移框架、規格驅動開發、CLAUDE.md 跨 repo 傳播、sudo MCP 插件；新技術彙整：Hooks 精細化控制、Token 路由、記憶體治理、Spec-Driven Dev、CLAUDE.md 跨 repo）
  - `topics/competitor-landscape.md`（2026-05-02 時序：OpenCode 被 XDA 認可為可行替代方案、OpenClaw 禁令持續發酵；新增 OpenCode 競品追蹤）
- 新增頁面：無
- 摘要：Uber 四個月燒光全年 AI 預算（$500–$2K/月/工程師）成為業界成本管控標誌性案例；OpenCode 崛起為 Anthropic 政策收緊後的主流替代方案；社群工具方向轉向治理與優化（記憶防漂移、規格驅動、跨工具 config 管理）。

---

## 2026-05-02 Ingest（第一次）

- 來源日報：[[news/2026-05-02]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.126 細節、session 30 天自動刪除、Omar/graphify/NanoBrain/Council/Destiny/Mote 新工具）
  - `entities/claude-security.md`（全 Enterprise 開放細節：Git 歷史讀取、跨檔案資料流追蹤、推理式驗證）
  - `entities/pricing.md`（$6,000 /loop 失控事件、帳號停用計費爭議、Bedrock 配額歸零、Max 方案 60% 消耗、50% 費用節省方案）
  - `entities/mythos.md`（OpenAI Cyber 限制存取事件：Altman 批評 Anthropic 後採同樣策略）
  - `entities/opus-4-7.md`（GPT-5.5 vs Opus 56 task 基準測試、4.5→4.7 躍升感知討論）
  - `entities/google-investment.md`（gigawatt 等級算力預購）
  - `topics/community-tech-patterns.md`（2026-05-01 時序：Omar、graphify、Chrome 用量擴充、NanoBrain、Council、50% 費用節省、Destiny、Mote；新技術彙整：知識圖譜、session 歷史保留、封閉技能批判）
  - `topics/ai-agent-safety.md`（$6,000 /loop 失控、MCP 指令執行漏洞、Bedrock 配額歸零）
  - `topics/competitor-landscape.md`（五角大廈排除 Anthropic、Apple 採用 Claude、Uber 燒光預算、iCapital、The Atlantic AI 泡沫報導）
- 新增頁面：`topics/anthropic-government-policy.md`
- 摘要：五角大廈因安全護欄分歧排除 Anthropic 為最大事件（白宮已重啟談判）；Claude Security 正式全面開放 Enterprise 公測；graphify 26 天衝上 GitHub #2 顯示知識圖譜工具需求爆發；/loop 失控 $6,000 事件引爆 Anthropic 用量警報機制批評；Apple 採用 Claude 顯示頂層科技企業滲透加速。

---

## 2026-05-01 Lint

- 修正矛盾：無
- 補連結（孤立頁面修正）：
  - `entities/project-deal.md` → 在 `topics/community-tech-patterns.md` 相關實體加入連結
  - `entities/claude-design.md` → 在 `topics/community-tech-patterns.md` 相關實體加入連結；在 `entities/claude-code.md` 相關議題加入連結
- 狀態更新：`topics/google-investment.md` 狀態維持 resolved，已遷移
- 遷移至 entities：`topics/google-investment.md` → `entities/google-investment.md`（保留原頁重定向提示）
- 新增 entities：
  - `entities/openclaw.md`（第三方 agentic 工具，被提及 3+ 次：配額限制 + 異常計費 + claude-code 已知問題）
  - `entities/google-investment.md`（從 topics/ 遷移）
- overview.md：已全面重寫（反映 2026-04-25 至 2026-04-30 局勢）

---

## 2026-04-30 Ingest

- 來源日報：[[news/2026-04-30]]
- 更新頁面：
  - `entities/mythos.md`（WSJ 白宮報導更多細節、五角大廈角力、Dark Reading 資安產業分析）
  - `entities/pricing.md`（ANTHROPIC_API_KEY 雲端計費陷阱、Pro 餘額消失、長 context 快取隱性成本）
  - `entities/claude-code.md`（OpenClaw 異常計費、v2.1.124/2.1.126 系統提示分析、GameMaker 整合、Managed Agents AWS 定位、Throttle Meter/Brifly/Mneme/Nimbalyst/Trent 等工具、Projects 對話消失）
  - `entities/opus-4-7.md`（退步報告、arxiv 4T 參數估算）
  - `topics/ai-agent-safety.md`（OpenClaw 計費觸發機制、AI agent 憑證竊取攻擊、Claude Code vs Gemini CLI 信任邊界標準差異）
  - `topics/code-quality-decline.md`（Opus 4.7 後設化退步、Projects 對話消失）
  - `topics/competitor-landscape.md`（Codex 社群能見度調查、GameMaker 整合、BrowserCode 瀏覽器化趨勢）
  - `topics/community-tech-patterns.md`（2026-04-30 時序、7 款新工具入熱門應用表、多 LLM 協作架構技術彙整）
- 新增頁面：`entities/claude-security.md`
- 摘要：OpenClaw 異常計費事件（HN 近千則討論）引爆帳單透明度信任危機；白宮介入 Mythos 管控的細節持續擴大（Anthropic 自稱世界未準備好）；Claude Security 公開測試版標誌 Anthropic 正式跨足 AI 資安產品市場；帳單透明度問題從多個角度（OpenClaw/API KEY 計費/餘額消失/快取成本）同步爆發。

---

## 2026-04-29 Ingest

- 來源日報：[[news/2026-04-29]]
- 更新頁面：
  - `entities/mythos.md`（白宮反對擴大 Mythos 存取、Steve Blank「潘朵拉盒子」文章）
  - `entities/pricing.md`（$900B 估值融資洽談、Token 費用估算翻倍、Max 方案 API 錯誤）
  - `entities/claude-code.md`（Champion Kit、Speed Bumps 問題、Cockpit/Harness/CodeThis/Claude Exporter 四款新工具）
  - `topics/code-quality-decline.md`（Speed Bumps 增加、Max 支援 AI 失靈）
  - `topics/competitor-landscape.md`（Codex vs Claude Code 生產環境比較）
  - `topics/community-tech-patterns.md`（Champion Kit、Cockpit、Harness、CodeThis、Claude Exporter、Caveman 基準測試）
- 新增頁面：無
- 摘要：白宮介入 Mythos 存取管控為最大事件；Anthropic 靜默將 Claude Code token 費用估算翻倍引發企業預算警示；單日四款社群工具（Cockpit/Harness/CodeThis/Claude Exporter）湧現顯示生態仍活躍；Caveman 基準測試挑戰「複雜外掛優於兩字 prompt」的直覺假設。

---

## 2026-04-28 Ingest

- 來源日報：[[news/2026-04-28]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.121 發布、Runhouse acqui-hire、Auto Compact 失效、Prompt Cache Race Condition、Tool Schema 洩漏、PullMD 新工具）
  - `entities/pricing.md`（Opus 圍牆事件及修正、20x 計量異常、Auto Compact 鎖死、$1T 估值）
  - `entities/opus-4-7.md`（Opus 圍牆事件、生物問題拒絕、effort 研究、Sonnet 替代數據）
  - `entities/mythos.md`（SWE-bench 方法論爭議擴散至 HN）
  - `topics/code-quality-decline.md`（安全定義過窄批評、信任侵蝕結構性分析）
  - `topics/community-tech-patterns.md`（Jupyter MCP、Batch API、PullMD、Sonnet 工作流、Plugin 設計模式、effort 研究）
  - `topics/competitor-landscape.md`（哈佛改用 Claude、XDA 四工具比較、雪梨辦公室）
- 新增頁面：`topics/ai-agent-safety.md`
- 摘要：Cursor + Claude Opus 9 秒刪除生產資料庫為最大事件；Opus 圍牆政策引發信任危機（雖事後修正）；Anthropic 商業擴張加速（Sydney 辦公室、哈佛採用、Runhouse 收購、$1T 估值）；多個基礎設施可靠性問題（Prompt Cache Race、Auto Compact 失效、Schema 洩漏）同日密集出現。

---

## [2026-04-27] ingest (補充) | 日報 15:44 UTC 重跑版本（44 篇）

- 來源日報：[[news/2026-04-27]]（更新版，44 篇，新增 Show HN 工具與 Claude Design 相關內容）
- 更新頁面：
  - `topics/community-tech-patterns.md`（新增 Rapunzel、SmolVM、Groundtruth、OpenCode-power-pack、APFS worktree、Doom MCP 實驗、學習技能模組）
  - `entities/claude-code.md`（新增 Rapunzel / SmolVM / Groundtruth / OpenCode-power-pack 工具）
  - `entities/mythos.md`（IEEE Spectrum 安全部署要求後續報導）
  - `topics/google-investment.md`（AWS + Anthropic & Meta 合作）
- 新增頁面：`entities/claude-design.md`
- 摘要：Show HN 工具大爆發（Groundtruth、SmolVM、Rapunzel）驗證新 HN 來源設定有效；Claude Design 首日社群評價偏負面，系統提示詞遭反向工程。

---

## [2026-04-27] ingest | 每日日報更新

- 來源日報：[[news/2026-04-27]]
- 更新頁面：
  - `entities/claude-code.md`（API 金鑰外洩漏洞、Usage Policy 隨機拒絕、版本回滾、Mac 卸載不完整、新社群工具 EvanFlow/Relay/pentest-ai-agents/modularity）
  - `entities/pricing.md`（Max 方案多工配額不足、Google 投資定價指標意義）
  - `entities/mythos.md`（SWE-bench 方法論循環論證爭議、Project Glasswing）
  - `entities/opus-4-7.md`（Usage Policy 隨機拒絕、Sonnet vs Opus 社群比較數據）
  - `topics/google-investment.md`（投資確認報導、CoreWeave 算力合作）
  - `topics/competitor-landscape.md`（HackerNoon AI 護城河分析、Claude vs GPT 比較討論）
  - `topics/community-tech-patterns.md`（EvanFlow、Relay、parsh 策略、modularity、effort 數據、CLAUDE.md 最佳實踐）
- 新增頁面：`entities/project-deal.md`
- 摘要：Google 400 億投資正式確認、Claude Code 安全問題（API 金鑰外洩 + HERMES.md 計費 bug）持續發酵、Mythos SWE-bench 方法論遭學術質疑、Project Deal 代理人交易實驗引發法律與商業討論。

---

## [2026-04-26] 新增頁面 | community-tech-patterns

- 手動新增：`topics/community-tech-patterns.md`
- 用途：追蹤社群技術應用趨勢，每次 ingest 從「💬 技術熱度討論」區塊累積萃取
- 已回填 2026-04-25 與 2026-04-26 兩天的內容

---

## [2026-04-26] ingest | 每日日報更新

- 來源日報：[[news/2026-04-26]]
- 更新頁面：
  - `entities/claude-code.md`（HERMES.md bug、Bugcrawl、新社群工具 Claude Squad / mux0 / agent-order）
  - `entities/pricing.md`（HERMES.md 靜默計費、token burn、OpenClaw 配額限制）
  - `entities/mythos.md`（七週發現 2,000+ 漏洞）
  - `topics/competitor-landscape.md`（Google 競品消息二度登 HN）
- 新增頁面：`entities/bugcrawl.md`
- 摘要：HERMES.md 計費 bug 曝光為最大新聞，Mythos 漏洞發現能力獲多媒體報導，Claude Code 社群工具生態持續擴張。

---

## [2026-04-25] init | Wiki 初始化建立

初始化 wiki 結構，根據 `news/2026-04-25.md` 內容建立以下頁面：

**新建 entities：**
- `entities/claude-code.md`
- `entities/opus-4-7.md`
- `entities/pricing.md`
- `entities/mythos.md`

**新建 topics：**
- `topics/code-quality-decline.md`
- `topics/google-investment.md`
- `topics/competitor-landscape.md`

**新建 overview：**
- `overview.md`

---

## 2026-05-15 Re-ingest（品質審查補跑）

- 來源日報：[[news/2026-05-15]]（已於同日 Ingest 處理，本次為品質審查補跑）
- 更新頁面：
  - `entities/pricing.md`（完整重構：以 6/15 互動式 vs 程式化雙軌計費架構為核心，新增方案對照表、費用管控技巧、6/15 前行動清單；歷史政策紀錄保留但壓縮）
- 新增機制：
  - `CLAUDE.md` 新增「Wiki 頁面呈現品質標準」（必須修復 + 警示觸發重構規則）
  - `wiki-ingest.md` 新增 Step 4b 呈現品質審查（強制核對）
  - `wiki-lint.md` 新增 Step 3e 呈現品質審查（全頁面掃描）
  - `.claude/settings.local.json` 新增 PostToolUse Hook（markdownlint-cli2 自動掃描）
  - 新增 `/wiki-backfill` 與 `/wiki-digest` 指令
- 呈現品質審查結果：
  - `entities/claude-code.md`（336 行）✅ 通過——版本歷史以表格壓縮，功能分主題區塊
  - `entities/pricing.md`（210 行）✅ 通過——重構後計費架構清晰置頂，表格呈現
  - `topics/competitor-landscape.md`（160 行）✅ 通過
  - `topics/ai-agent-safety.md`（239 行）✅ 通過——技術彙整按主題組織，時序含 [tag] 分類
  - `topics/community-tech-patterns.md`（836 行）📋 待辦——過大，建議 lint 時將舊 時序 條目壓縮進 技術彙整；當前結構可讀，不阻礙使用
- 摘要：本次補跑以建立呈現品質審查機制為主，並完成 pricing.md 架構重構，使 6/15 計費雙軌制在頁面頂部即可讀懂。

---

## 2026-05-15 Lint

- 修正矛盾：無
- 補連結：
  - 新建 `entities/cat-wu.md`（Cat Wu 被 claude-code.md × 2 + community-tech-patterns.md × 2 + feature-radar.md 提及共 5 次，達建頁閾值）
  - `entities/claude-code.md` → 補上 `[[entities/cat-wu]]`（近期重要更新 + 相關議題兩處）
  - `topics/community-tech-patterns.md` → 2026-05-15 及 2026-05-14 兩筆 Cat Wu 提及補 wikilink
- 狀態更新：無（所有 ongoing/monitoring 狀態確認無需調整）
- 遷移至 entities：無
- 新增 entities：`entities/cat-wu.md`（Claude Code 產品負責人，AI 主動性論述）
- 呈現品質：
  - `topics/competitor-landscape.md` ⚠️ 已修復：16 個連續日期條目新增 3 個主題分組（企業競爭白熱化 / Codex 崛起與分流 / 早期格局）
  - `topics/community-tech-patterns.md` 📋 待辦：836 行過大，最舊 4 個時序條目（2026-04-25 至 2026-04-28）待壓縮至技術彙整；工作量過大，記錄待辦，次週 lint 處理
  - 其餘所有頁面（12 entities + 4 topics）✅ 通過
- overview.md：已全面重寫（反映 2026-05-14/15 計費政策、Microsoft 授權取消、Cat Wu proactivity 論述、Ramp 企業超越數據）

## 2026-05-15 拆分 community-tech-patterns

- 原因：community-tech-patterns.md 達 836 行，技術彙整混入應用（工具/工作流）與討論（哲學/辯論/實證）兩種性質
- 新增頁面：`topics/community-tech-discussions.md`（技術討論趨勢）
- 移出條目（24 項）：effort 等級與模型行為、多 LLM 協作架構、工具生態痛點、封閉技能生態批判、規格驅動開發、記憶體治理與行為漂移防範、AI 程式碼一致性問題、AI 大規模開發案例、Boris Cherny「Loops 是未來」、Agent Supervision 哲學、Skills Unix 哲學、Agentic 工作流組織協調挑戰、Wire Trace 架構侷限、120 提示詞實證研究、Token 用量極端案例、整合模式選擇框架、Boris Cherny 反 vibe coding、Skill Atrophy 反思、HTML vs Markdown、Claude Code 架構深度解析、三層 Code Review、Judge Gate、Context 管理核心瓶頸、AI 生成程式碼安全審查必要性
- 結果：patterns.md 836→716 行；discussions.md 244 行（新）
- 更新：index.md（頁數 22→23）、community-tech-patterns.md（摘要、目前結論、相關實體）

## 2026-05-16 熱門討論表格擴充

- 變更：`topics/community-tech-discussions.md` 熱門討論表格新增 `模式` 欄（☄️閃現/🌊延燒/🌸落幕/🌋重燃/🌙靜候）與 `衍生` 欄
- 補連結：HTML vs Markdown 討論 → 衍生 `agent-html-skills`；Skill Atrophy → 衍生 `recap 工具`；多 LLM 協作 → 衍生 `Opus+DeepSeek 混合架構`
- 新增規則：`CLAUDE.md` 補入 community-tech-patterns ↔ community-tech-discussions 雙向連結規則、模式判斷規則（含重燃偵測邏輯）
- 確認 emoji 方案：重燃模式採 🌋（火山重燃）

## 2026-05-17 新增 official-community-gap + community-tech-tools 痛點洞察

- 新增頁面：`topics/official-community-gap.md` — 官方功能 vs 社群痛點缺口矩陣，含 9 個痛點、收斂程度評估、結構性原因分析與預測指標
- 更新頁面：`topics/community-tech-tools.md` — 新增 `## 痛點洞察` 區塊，含痛點主題表格、CLAUDE.md 失效四原因、AI 輔助開發副作用分析；參考來源新增 official-community-gap 連結
- 更新：`index.md`（頁數 24→25，新增 official-community-gap 條目）
- Web reader：wiki 首頁新增「官方 vs 社群缺口分析」卡片


---

## 2026-05-23 Lint

- 修正矛盾：
  - `topics/code-quality-decline.md`：最後更新欄位未從 2026-05-09 更新至 2026-05-21（2026-05-21 ingest 遺漏）→ 已修正
  - `topics/anthropic-government-policy.md`：監測狀態文字「11 天無新進展」→「21 天無新進展」→ 已修正；最後更新更新至 2026-05-22
- 補連結：
  - `entities/google-investment` 孤立（無其他頁面連結）→ 已在 `topics/competitor-landscape.md` 技術彙整補入 wikilink
  - `entities/andrej-karpathy`（本次 ingest 新建）→ 已在 `topics/community-tech-discussions.md` 相關實體補入 wikilink
- 狀態更新：無（anthology-government-policy 狀態維持 monitoring，21 天仍在追蹤）
- 遷移至 entities：無
- 新增 entities：`entities/opencode.md`（OpenCode 開源替代，27 次提及、10 個檔案）；已在 competitor-landscape.md 補入 wikilink
- 呈現品質：
  - 超長頁面 `topics/community-tech-patterns.md`（695 行）✅ 拆分完成：
    - 保留 `community-tech-patterns.md`（403 行）：摘要、模式概覽、技術彙整、結論、相關實體
    - 新建 `topics/community-tech-timeline.md`（~310 行）：2026-04-25 至 2026-05-22 完整時序
    - 兩頁互相補上 wikilink；patterns.md 補入 `[[news/2026-05-22]]` 參考來源
  - 其餘頁面：✅ 通過（各頁面於 ingest 時已執行品質審查）
- 超長頁面（> 500 行）：community-tech-patterns.md（695 行）→ 已拆分（見呈現品質）
- CLAUDE.md 健檢：
  - 行數：99 行（原 353 行，拆分後；閾值 150 行）✅ 大幅精簡
  - 拆分：wiki 規則（~270 行）移至新建 `wiki/CLAUDE.md`；技能檔案更新載入點
  - 矛盾：無
  - 引用驗證：所有 CLAUDE.md 引用的欄位/結構均已遷移至 wiki/CLAUDE.md，保持有效
  - 遵守率：✅ 全部通過（見 2026-05-22 Ingest 呈現品質欄）
  - 過期規則（> 60 天）：無（最舊規則 [加入: 2026-04-25] = 28 天）
  - 簡化：已執行（wiki 規則全部移至 wiki/CLAUDE.md；skills 更新 Step 1/2 明確載入）
- overview.md：已更新（2026-05-21 → 2026-05-22，涵蓋 DeepSeek 全棧競品、$6K 費用事件、Karpathy 加入、Managed Agents 文件完整化）

## 2026-05-23 時序整體修復

- **觸發原因：** 使用者反映「WIKI頁面時序混亂，請整體檢查」
- **掃描範圍：** 全部 entities/（16頁）+ topics/（11頁）
- **已修復（共 6 頁）：**
  - `topics/competitor-landscape.md`：2026-05-22 + 2026-05-21 誤排在 2026-05-19 後面 → 已修正為最新在前；section header 日期範圍同步更新
  - `entities/google-investment.md`：時序區塊 2026-05-01 誤排在 2026-04-27 後面 → 已調整為最新在前
  - `entities/boris-cherny.md`：公開言論區塊日期錯亂（2026-05-05→05-06→05-13→05-08…）→ 統一改為最新在前
  - `topics/community-tech-tools.md`：四處錯亂：May-21（5條）、May-16（2條）誤放表格末尾；Apr-30（5條）排在 Apr-29 後；Apr-28（2條）排在 Apr-27 後 → 全部移至正確位置
  - `topics/community-tech-discussions.md`：熱門討論表格多處日期錯亂（05-20×3 排在 05-09 後、05-13 排在 05-08 前等）→ 統一按日期最新在前重排；並恢復誤刪的 Boris "coding is solved" 05-08 延燒條目
- **確認無誤（✅ 正確順序）：**
  - enterprise-cost-management.md、code-quality-decline.md、ai-agent-safety.md、managed-agents.md：✅
  - community-tech-timeline.md：✅（2026-05-22 在頂，往下遞減）
  - claude-code.md 版本歷史 + 歷史記錄：✅
  - community-tech-discussions.md 技術彙整：✅
  - pricing.md、openclaw.md、stainless.md、claude-security.md、andrej-karpathy.md：✅
  - 其餘單一/少量日期頁面（bugcrawl、project-deal、claude-design、cat-wu、mythos 主題性分段）：✅ 無排序問題

---

## 2026-05-23 Ingest | news/2026-05-23.md

- 來源日報：`news/2026-05-23.md`（74 則；含 Claude Code RCE CVE-2026-39861、Microsoft 企業授權取消、Project Glasswing 10K+ 漏洞、Opus 4/Sonnet 4 退役 6/15、新工具 Superset/OpenRig/VIR/CoreMem/tokenflex.ing/Shortcuts Playground、$30B 融資、多人協調困境討論）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.150（基礎設施改善）；新增 RCE 警示與 Opus 4/Sonnet 4 退役 6/15 至 開發者須知；更新 現況 最新版本
  - `topics/ai-agent-safety.md`：新增 Claude Code RCE 跨工具傳播（2026-05-23）；新增 Mythos Exploit 開發評估報告（2026-05-23）；更新 最後更新
  - `topics/enterprise-cost-management.md`：新增 2026-05-23 時序（tokenflex.ing $30,983、API 帳單 3x、Microsoft 授權取消確認）
  - `topics/competitor-landscape.md`：新增 2026-05-23 時序（Business Insider Claude 贏新創、Microsoft 確認、RCE 跨工具傳播）
  - `topics/community-tech-tools.md`：新增 6 工具（Superset、OpenRig、VIR、CoreMem、tokenflex.ing、Shortcuts Playground）；更新 痛點洞察 表（跨 session 記憶歸零項目新增 VIR/CoreMem）
  - `topics/community-tech-discussions.md`：LLMs 虛假忙碌 模式改為 🌊延燒；新增 Solo 爽、團隊亂 熱門討論（2026-05-23）；新增對應技術彙整條目
  - `entities/mythos.md`：新增 Project Glasswing 一個月更新（10K+ 漏洞，修補速度成新瓶頸）；新增 Mythos Exploit 開發能力評估（exploit primitives + 端對端攻擊鏈）；更新 最後更新
  - `entities/pricing.md`：新增 2026-05-23 模型別名退役警示（Opus 4/Sonnet 4 June 15）；更新 最後更新
  - `topics/community-tech-patterns.md`：新增 Git Worktrees 作為多 Agent 隔離原語（2026-05-23）；新增 Framework-Specific CLAUDE.md 設計（2026-05-23）；更新 最後更新
  - `wiki/feature-radar.md`：v2.1.150 為基礎設施改善，無新使用者功能；更新 最後更新
- 新增 entities：無
- feature-radar 更新：本日無新功能（v2.1.150 infra-only）
- 呈現品質：
  - `entities/claude-code.md` ✅ 通過
  - `topics/ai-agent-safety.md` ✅ 通過
  - `topics/enterprise-cost-management.md` ✅ 通過
  - `topics/competitor-landscape.md` ✅ 通過
  - `topics/community-tech-tools.md` ✅ 通過
  - `topics/community-tech-discussions.md` ✅ 通過
  - `entities/mythos.md` ✅ 通過
  - `entities/pricing.md` ✅ 通過
  - `topics/community-tech-patterns.md` ✅ 通過
  - `wiki/feature-radar.md` ✅ 通過
