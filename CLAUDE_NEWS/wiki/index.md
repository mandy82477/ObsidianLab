# Wiki 目錄

**角色：** 地圖——讀一次就知道該去哪頁（哲學見 `wiki/CLAUDE.md`「資訊架構哲學」）
**收：** 慢變的路由事實——頁面存在、領域、狀態、一句鉤子
**不收：** 快變事實（日期／熱度／近況→頁面標頭，盤點用 Grep）；異動紀錄（→ [[log]]）；每日新聞（→ `news/`）
**讀法：** 整讀（本檔的存在意義就是便宜的一次讀）；查詢分流見 `wiki/CLAUDE.md`「搜尋策略」

**最後更新：** 2026-08-28


---

## 概覽

- [[overview]] — 當前 Claude / Anthropic 生態系整體局勢（🗓️ 週更）
- [[feature-radar]] — 新功能熱度追蹤、試用推薦與快速上手（每日更新）
- [[feature-radar-archive-2026-05]] — 2026-05 功能詳細條目封存

---

## Entities（實體頁）

| 頁面 | 類型 | 領域 | 狀態 | 摘要 |
|------|------|------|------|------|
| [[entities/sonnet-5]] | model | 🤖 模型 | active | Claude Sonnet 5：Claude Code v2.1.197 預設模型，1M context，$2/$10 per Mtok 標準價（08-10 永久化），agentic 效能接近 Opus 4.8 |
| [[entities/claude-science]] | product | 🛠️ 工具/功能 | active | Claude Science：科學家專用 AI 工作台，整合研究工具套件、可稽核 artifact、彈性運算資源；Anthropic 宣布自行開發藥物 |
| [[entities/claude-code]] | product | 🛠️ 工具/功能 | active | Claude Code CLI 主頁：功能、已知問題、社群工具 |
| [[entities/opus-5]] | model | 🤖 模型 | active | Claude Opus 5：新次旗艦，2026-07-25 發布，編碼/知識工作評測逼近 Fable 5，定價定位待彙整，現為 Claude Max 新預設模型、Claude Pro 最強模型 |
| [[entities/opus-4-8]] | model | 🤖 模型 | active（已被取代） | Opus 4.8：SWE-bench Pro 69.2%、1M context、Dynamic Workflows（1,000 子代理）、Fast Mode 1/3 費用；次旗艦地位已於 2026-07-25 由 [[entities/opus-5]] 接手 |
| [[entities/opus-4-7]] | model | 🤖 模型 | active（已被取代）| Opus 4.7 發布細節、思考深度爭議、cache 問題 |
| [[entities/pricing]] | policy | 💼 商業 | active | 訂閱方案、近期政策變動、token 成本注意事項；印度盧比定價 07-13 已回應 Pro 方案（Rs 2,000/月），Claude Code 涵蓋範圍仍未見官方確認（issue #17432 留言 212） |
| [[entities/mythos]] | model | 🤖 模型 | active（已解禁） | 高能力安全模型；2026-07-01 出口管制解除，全球恢復存取；僅限授權機構/安全研究用途，非一般消費市場 |
| [[entities/bugcrawl]] | feature | 🛠️ 工具/功能 | beta | Anthropic 測試中的 Claude Code 漏洞偵測工具 |
| [[entities/claude-design]] | feature | 🛠️ 工具/功能 | active（初期）| Anthropic AI 設計工具，首日社群反映幻覺多、風格偏移、Claude Code 整合差 |
| [[entities/claude-security]] | product | 🛠️ 工具/功能 | beta | Claude Security 資安產品，情境化安全評估，整合於 Claude Code 開發環境 |
| [[entities/openclaw]] | product | 🛠️ 工具/功能 | active | 第三方 agentic 工具，歷經禁令後 6/15 起恢復允許但改走信用池 API 費率計費 |
| [[entities/google-investment]] | event | 💼 商業 | resolved | Google 投資 400 億美元歷史記錄，含循環算力交易結構 |
| [[entities/managed-agents]] | feature | 🛠️ 工具/功能 | active（正式發布）| Managed Agents 官方框架：Dreaming 記憶整合、20 路並行子代理、Outcomes 規格驗證 |
| [[entities/bernanke]] | person | 👤 人物 | active | 前聯準會主席，2026-07-09 加入 Anthropic 長期利益信託（Long-Term Benefit Trust）董事會 |
| [[entities/boris-cherny]] | person | 👤 人物 | active | Claude Code 創始人，「Loops 是未來」設計哲學、「coding is solved」論戰、第三方工具邊界聲明；07-17 稱同時執行數千個 Claude Code agent（報導未經獨立確認） |
| [[entities/chris-ciauri]] | person | 👤 人物 | active | Anthropic 國際業務總監；首爾記者會宣布 Fable 5 / Mythos 解禁信心（2026-06-18）|
| [[entities/john-jumper]] | person | 👤 人物 | active | 諾貝爾化學獎得主（AlphaFold），2026-06-19 離開 Google DeepMind 加入 Anthropic（Reuters 確認）|
| [[entities/cat-wu]] | person | 👤 人物 | active | Claude Code 產品負責人，「AI 下一步是主動性（proactivity）」論述 |
| [[entities/andrej-karpathy]] | person | 👤 人物 | active | 近期加入 Anthropic，CLAUDE.md 四條規則、「最小必要 context」費用控管原則 |
| [[entities/fiona-fung]] | person | 👤 人物 | active | Anthropic 工程副總裁；「Claude Code 讓工程師更孤獨；coding 不再是瓶頸」論述（2026-06-22） |
| [[entities/tom-brown]] | person | 👤 人物 | active | Anthropic 聯合創辦人（GPT-3 共同作者）；2026-06-25 接管 Fable 5 出口管制與白宮談判 |
| [[entities/dario-amodei]] | person | 👤 人物 | active | Anthropic CEO：政府監管立場、企業文化論述、Code with Claude 大會現場宣布速率政策 |
| [[entities/teresa-carlson]] | person | 👤 人物 | active（待核實）| 前 Microsoft、AWS 高管；2026-07-07 加入 Anthropic 主導公部門（public sector）業務（FedScoop）|
| [[entities/chris-olah]] | person | 👤 人物 | active | Anthropic 共同創辦人、AI 可解釋性研究先驅；2026-05-26 梵蒂岡封論揭幕演講 |
| [[entities/opencode]] | product | 🛠️ 工具/功能 | active（快速成長）| Claude Code 主要開源替代品，157K 開發者分流，OpenCode-power-pack 移植官方 11 個 skills |
| [[entities/claude-tag]] | feature | 🛠️ 工具/功能 | active | Claude Tag：Slack-native AI 協作工具，可讀取頻道上下文、跨 session 記憶、主動完成任務；Anthropic 內部 65% 程式碼由其生成 |
| [[entities/claude-skills]] | feature | 🛠️ 工具/功能 | active | Claude Skills：官方 Skills 產品線與生態單一入口——六大控制層之一，官方小企業/教師技能包、平台支援、第三方移植動態；設計面歸 [[topics/community-tech-patterns]] |
| [[entities/fable-5]] | model | 🤖 模型 | active（已解禁）| Claude Fable 5：首款 Mythos 級公開模型，$10/$50 per M token；7/1 解禁，Pro/Max/Team 7/7 前享 50% 配額，7/7 後 usage-based billing |
| [[entities/tom-blomfield]] | person | 👤 人物 | active（待核實）| 前 Monzo 共同創辦人，2026-07-13 加入 Anthropic（Business Insider 單一來源，AI compute／Y Combinator 背景）|
| [[entities/claude-for-teachers]] | product | 🛠️ 工具/功能 | active | Anthropic 面向美國通過認證 K-12 教師的免費方案，開放進階 Claude 功能與教學技能庫，對接全美 50 州學術標準 |
| [[entities/tino-cuellar]] | person | 👤 人物 | active | Anthropic 首任 Chief Global Affairs Officer（2026-08-05 到任），前 Carnegie Endowment for International Peace 總裁、加州最高法院大法官 |
| [[entities/robert-mahari]] | person | 👤 人物 | active（待核實）| Anthropic 新設「Claude for Legal」部門負責人（2026-08-07 任命，Legal IT Insider、Law.com 同日獨立報導，僅標題可用，過往經歷 ❓ 待查證 ⟨Q-01⟩）|
| [[entities/jensen-huang]] | person | 👤 人物 | active（待核實）| Nvidia 執行長；2026-08-27 傳出對投資 OpenAI／Anthropic 的規模表示「後悔」（Yahoo Finance 單一來源，後悔方向 ❓ 待查證）|
| [[entities/amir-salek]] | person | 👤 人物 | active（待核實）| Anthropic 延攬前 Google 自研晶片計畫創辦人（2026-08-23，The Times of India 單一來源，僅標題可用，過往經歷與職掌待查證）|

**懸置細節**
- ⟨Q-01⟩ ❓ **待查證**（標 2026-08-10｜查 [[entities/robert-mahari]]、過往經歷）：Legal IT Insider、Law.com 兩則報導僅標題可用，Robert Mahari 過往具體背景與資歷尚未確認。

---

## Topics（進行中議題）

> Topics 頁面本身無「類型」欄位，故表格僅三欄（領域 / 狀態 / 摘要），為刻意設計差異（Entities 四欄含類型）。

| 頁面 | 領域 | 狀態 | 摘要 |
|------|------|------|------|
| [[topics/model-comparison]] | 🤖 模型 | ongoing | 模型選型對照：「我該用哪個模型」單一入口——快速選型表、情境推薦、benchmark 對照（陣容變化時同步更新） |
| [[topics/model-task-leaderboard]] | 🤖 模型 | ongoing | 🗓️ 週更 任務 × 跨家模型領先者快照：「做某類任務目前哪家最強」——寫 code／文案／畫圖／改圖／影片／情商／幻覺率等 18 類任務的活榜單每週速讀＋各榜評比方式索引 |
| [[topics/anthropic-commitments]] | 🏛️ 政策/安全 | monitoring | 承諾兌現追蹤：「Anthropic 說過要做的事做了嗎」——官方承諾/拒絕建檔，狀態變化時由每日 ingest 更新 |
| [[topics/code-quality-decline]] | 🛠️ 工具/功能 | ongoing | Claude Code 效能退步事件，Anthropic 已承認工程疏失 |
| [[topics/competitor-landscape]] | 💼 商業 | ongoing | Google 祕密開發競品 + OpenCode 157K 分流 + DeepSeek clone 低成本替代生態 |
| [[topics/community-tech-tools]] | 🌐 社群 | ongoing | 🗓️ 週更策展：社群工具目錄——58 工具的活躍度、採用狀態追蹤（每日 ingest 不更新） |
| [[topics/community-tech-patterns]] | 🌐 社群 | ongoing | 社群實戰模式庫（日更）：multi-agent、skills 設計、工作流最佳實踐的可複用做法 |
| [[topics/community-large-codebase-workflow]] | 🌐 社群 | ongoing | 🗓️ 週更 大型 codebase 規模化開發主線——每條線先給「現在的答案」，再列子問題表；節點證據在模式庫 |
| [[topics/community-pattern-trends]] | 🌐 社群 | ongoing | 🗓️ 週更：社群趨勢觀察——從模式庫萃取的宏觀層，7 條成形趨勢的熱度曲線 + 對現有設計的啟示 |
| [[topics/community-tech-discussions]] | 🌐 社群 | ongoing | 社群技術討論趨勢：設計哲學辯論、實證研究、架構反思（HTML vs MD、Skill Atrophy 等） |
| [[topics/safety-china-trust-dispute]] | 🏛️ 政策/安全 | monitoring | 中美 AI 工具信任對峙：中國代理偵測程式碼/隱寫術指控 → Alibaba/Meta 禁用 → 中國官方「後門」警示 vs Anthropic 07-10 首度公開否認（2026-07-12 自 ai-agent-safety / government-policy 拆出）|
| [[topics/ai-agent-safety]] | 🏛️ 政策/安全 | ongoing | AI agent 安全：GitHub Repo prompt injection 多媒體確認 + 假冒安裝包 + CVE/DoS 漏洞（中國信任對峙已分流至 [[topics/safety-china-trust-dispute]]）|
| [[topics/ai-agent-safety-archive]] | 🏛️ 政策/安全 | monitoring | AI Agent 安全時序歷史存檔（2026-05-22 以前）；主頁 [[topics/ai-agent-safety]] 瘦身分流 |
| [[topics/anthropic-government-policy]] | 🏛️ 政策/安全 | ongoing | Anthropic 政府政策攻防：出口管制主線已於 2026-07-01 解除，剩餘承諾落實、歐洲據點爭奪、Legion 訴訟等衍生支線持續觀察（中國信任對峙已分流至 [[topics/safety-china-trust-dispute]]）|
| [[topics/official-community-gap]] | 🛠️ 工具/功能 | ongoing | 官方功能 vs 社群痛點缺口矩陣：哪些痛點官方正在解決、哪些結構性缺席；08-16 起持續有新缺口/矩陣更新，08-22 lint 回升 |
| [[topics/coding-workflow-guide]] | 🛠️ 工具/功能 | ongoing | 🗓️ 週更 程式開發實戰手冊：我現在在做這件事，該下哪個 skill、它會做什麼、有什麼坑——以流程階段為軸（官方技能不按開發領域切） |
| [[topics/enterprise-cost-management]] | 💼 商業 | ongoing | 企業規模採用 Claude 的成本結構挑戰：Uber/Microsoft 案例、缺失工具、因應策略；08-14 新增成本管控動態，08-22 lint 回升 |
| [[topics/enterprise-tool-tracker]] | 💼 商業 | ongoing | 大型企業 AI 編碼工具使用追蹤：Microsoft/Amazon/Uber/Apple 等企業當前工具選擇與變化軌跡；07-03 Alibaba 以疑似後門風險禁用 Claude Code（❌ 退出） |
| [[topics/community-tech-timeline]] | 🌐 社群 | monitoring | 社群技術應用趨勢完整時序（2026-04-25 至今），從 community-tech-patterns 拆分 |
| [[topics/anthropic-business]] | 💼 商業 | ongoing | Anthropic 商業健康度：企業採用率 34.4%、17 倍訂閱補貼、PMF 觀察、Microsoft 退出風險；07-03 藥物開發野心（The Verge）、大廠員工進駐客戶模式 |
| [[topics/recursive-self-improvement]] | 🏛️ 政策/安全 | ongoing | AI 遞歸自我改進：官方《Risk Report August 2026》（08-14）首度就內部 AI R&D 加速幅度提供量化區間自評，並確認 Model 2 暫無釋出計畫；08-22 lint 回升 |
| [[topics/ai-talent-flow]] | 💼 商業 | ongoing | AI 實驗室人才流動與對各公司影響：Google DeepMind 高層與核心研究員異動（事件 08-05，08-13 查證補記），Anthropic 主要承接；08-22 lint 回升 |
