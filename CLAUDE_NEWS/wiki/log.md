# Wiki 操作日誌

Append-only 紀錄。每次 ingest、query 或 lint 都在此追加一條。
格式：`## [YYYY-MM-DD] 類型 | 說明`

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
