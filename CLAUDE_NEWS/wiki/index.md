# Wiki 目錄

LLM 查詢此 wiki 時，**先讀這個檔案**找相關頁面，再讀具體頁面取得詳細資訊。

**最後更新：** 2026-07-02
---

## 近期異動

- [[topics/model-comparison]] — 2026-07-02：**新頁面**，模型選型對照：快速選型表 + 情境推薦 +（我該用哪個模型的單一入口）
- [[entities/fable-5]] — 2026-07-02：redeploy 隨附「Defense in Depth」新安全分類器，高風險 coding 請求 fallback 至 Opus 4.8；首日已有誤判負面實測
- [[entities/sonnet-5]] — 2026-07-02：官方對比圖表修改爭議（HN 討論可信度）+ 社群反映對 Sonnet 4.6 個性流失的主觀回饋
- [[topics/ai-agent-safety]] — 2026-07-02：中國代理偵測爭議升級為「embedded spyware」指控（版本號 2.1.91、混淆手法、system prompt 隱藏機制細節），社群單方指控待查證
- [[topics/anthropic-government-policy]] — 2026-07-02：Fable 5「Defense in Depth」機制作為出口管制解除後承諾的首次具體落實
- [[topics/anthropic-business]] — 2026-07-02：Anthropic-Samsung 客製晶片洽談（初步報導）、Blackstone 基金強勁月表現（初步報導）
- [[topics/competitor-landscape]] — 2026-07-02：Palantir CEO Karp 公開批評 Anthropic/OpenAI「竊取客戶 IP」，分析師調升 Palantir 評等
- [[entities/pricing]] — 2026-07-02：Max 方案升級誤扣費/客服退款爭議案例
- [[topics/community-tech-discussions]] — 2026-07-02：VS Code 使用率下降、AskUserQuestion 60 秒逾時、390M tokens 紀錄、thinking 停頓分心等中熱度討論
- [[topics/community-tech-patterns]] — 2026-07-02：氛圍狀態燈（hooks 驅動實體 LED 燈號提示 agent 狀態）新模式

### 2026-07-01
- [[entities/sonnet-5]]：**新頁面**，Claude Code v2.1.197 預設模型，1M context，$2/$10 per Mtok 促銷
- [[entities/claude-science]]：**新頁面**，科學家專用 AI 工作台正式發布
- [[entities/fable-5]]：**出口管制全面解除**，Pro/Max/Team 7/7 前 50% 配額，旗艦模型回歸
- [[entities/mythos]]：出口管制解除，全球恢復存取
- [[topics/anthropic-government-policy]]：Fable 5 / Mythos 5 出口管制全面解除，Anthropic 承諾三項義務（安全偵測/標準制定/惡意通報）
- [[topics/ai-agent-safety]]：Claude Code 隱寫術爭議（HN 2263，同形字符替換，Anthropic 承諾修復）+ CVE-2026-55407 DoS 漏洞
- [[entities/claude-code]]：v2.1.197 Sonnet 5 正式預設，SDK v0.115.0
- [[entities/pricing]]：Sonnet 5 促銷 $2/$10/Mtok（至 8/31）、Fable 5 7/7 後 usage-based billing
- [[topics/anthropic-business]]：Enterprise Gateway、Fable 5 正式協議、Amazon/Broadcom 資本市場連動
- [[feature-radar]]：新增 Sonnet 5（🔥🔥🔥🔥🔥）、Claude Science（🔥🔥）、Fable 5 解禁

---

## 概覽

- [[overview]] — 當前 Claude / Anthropic 生態系整體局勢（每週更新）
- [[feature-radar]] — 新功能熱度追蹤、試用推薦與快速上手（每次 ingest 更新）
- [[feature-radar-archive-2026-05]] — 2026-05 功能詳細條目封存

---

## Entities（實體頁）

| 頁面 | 類型 | 領域 | 狀態 | 摘要 |
|------|------|------|------|------|
| [[entities/sonnet-5]] | model | 🤖 模型 | active | Claude Sonnet 5：Claude Code v2.1.197 預設模型，1M context，$2/$10 per Mtok 促銷至 8/31，agentic 效能接近 Opus 4.8 |
| [[entities/claude-science]] | product | 🛠️ 工具/功能 | active | Claude Science：科學家專用 AI 工作台，整合研究工具套件、可稽核 artifact、彈性運算資源；Anthropic 宣布自行開發藥物 |
| [[entities/claude-code]] | product | 🛠️ 工具/功能 | active | Claude Code CLI 主頁：功能、已知問題、社群工具 |
| [[entities/opus-4-8]] | model | 🤖 模型 | active | Opus 4.8：SWE-bench Pro 69.2%、1M context、Dynamic Workflows（1,000 子代理）、Fast Mode 1/3 費用 |
| [[entities/opus-4-7]] | model | 🤖 模型 | active（已被取代）| Opus 4.7 發布細節、思考深度爭議、cache 問題 |
| [[entities/pricing]] | policy | 💼 商業 | active | 訂閱方案、近期政策變動、token 成本注意事項 |
| [[entities/mythos]] | model | 🤖 模型 | active（已解禁） | 高能力安全模型；2026-07-01 出口管制解除，全球恢復存取；仍維持軍事用途限制存取 |
| [[entities/bugcrawl]] | feature | 🛠️ 工具/功能 | beta | Anthropic 測試中的 Claude Code 漏洞偵測工具 |
| [[entities/claude-design]] | feature | 🛠️ 工具/功能 | active（初期）| Anthropic AI 設計工具，首日社群反映幻覺多、風格偏移、Claude Code 整合差 |
| [[entities/claude-security]] | product | 🛠️ 工具/功能 | beta | Claude Security 資安產品，情境化安全評估，整合於 Claude Code 開發環境 |
| [[entities/openclaw]] | product | 🛠️ 工具/功能 | active | 第三方 agentic 工具，歷經禁令後 6/15 起恢復允許但改走信用池 API 費率計費 |
| [[entities/google-investment]] | event | 💼 商業 | resolved | Google 投資 400 億美元歷史記錄，含循環算力交易結構 |
| [[entities/managed-agents]] | feature | 🛠️ 工具/功能 | active（正式發布）| Managed Agents 官方框架：Dreaming 記憶整合、20 路並行子代理、Outcomes 規格驗證 |
| [[entities/boris-cherny]] | person | 👤 人物 | active | Claude Code 創始人，「Loops 是未來」設計哲學、「coding is solved」論戰、第三方工具邊界聲明 |
| [[entities/chris-ciauri]] | person | 👤 人物 | active | Anthropic 國際業務總監；首爾記者會宣布 Fable 5 / Mythos 解禁信心（2026-06-18）|
| [[entities/john-jumper]] | person | 👤 人物 | active | 諾貝爾化學獎得主（AlphaFold），2026-06-19 離開 Google DeepMind 加入 Anthropic（Reuters 確認）|
| [[entities/cat-wu]] | person | 👤 人物 | active | Claude Code 產品負責人，「AI 下一步是主動性（proactivity）」論述 |
| [[entities/andrej-karpathy]] | person | 👤 人物 | active（待核實）| 近期加入 Anthropic，CLAUDE.md 四條規則、「最小必要 context」費用控管原則 |
| [[entities/fiona-fung]] | person | 👤 人物 | active | Anthropic 工程副總裁；「Claude Code 讓工程師更孤獨；coding 不再是瓶頸」論述（2026-06-22） |
| [[entities/tom-brown]] | person | 👤 人物 | active | Anthropic 聯合創辦人（GPT-3 共同作者）；2026-06-25 接管 Fable 5 出口管制與白宮談判 |
| [[entities/dario-amodei]] | person | 👤 人物 | active | Anthropic CEO：政府監管立場、企業文化論述、Code with Claude 大會現場宣布速率政策 |
| [[entities/chris-olah]] | person | 👤 人物 | active | Anthropic 共同創辦人、AI 可解釋性研究先驅；2026-05-26 梵蒂岡封論揭幕演講 |
| [[entities/opencode]] | product | 🛠️ 工具/功能 | active（快速成長）| Claude Code 主要開源替代品，157K 開發者分流，OpenCode-power-pack 移植官方 11 個 skills |
| [[entities/claude-tag]] | feature | 🛠️ 工具/功能 | active | Claude Tag：Slack-native AI 協作工具，可讀取頻道上下文、跨 session 記憶、主動完成任務；Anthropic 內部 65% 程式碼由其生成 |
| [[entities/fable-5]] | model | 🤖 模型 | active（已解禁）| Claude Fable 5：首款 Mythos 級公開模型，$10/$50 per M token；7/1 解禁，Pro/Max/Team 7/7 前享 50% 配額，7/7 後 usage-based billing |

---

## Topics（進行中議題）

> Topics 頁面本身無「類型」欄位，故表格僅三欄（領域 / 狀態 / 摘要），為刻意設計差異（Entities 四欄含類型）。

| 頁面 | 領域 | 狀態 | 摘要 |
|------|------|------|------|
| [[topics/model-comparison]] | 🤖 模型 | ongoing | 模型選型對照：「我該用哪個模型」單一入口——快速選型表、情境推薦、benchmark 對照（陣容變化時同步更新） |
| [[topics/code-quality-decline]] | 🛠️ 工具/功能 | monitoring | Claude Code 效能退步事件，Anthropic 已承認工程疏失 |
| [[topics/competitor-landscape]] | 💼 商業 | monitoring | Google 祕密開發競品 + OpenCode 157K 分流 + DeepSeek clone 低成本替代生態 |
| [[topics/community-tech-tools]] | 🌐 社群 | ongoing | 社群工具目錄：189 工具的活躍度、採用狀態追蹤 |
| [[topics/community-tech-patterns]] | 🌐 社群 | monitoring | 社群實戰模式庫（日更）：multi-agent、skills 設計、工作流最佳實踐的可複用做法 |
| [[topics/community-pattern-trends]] | 🌐 社群 | ongoing | 社群趨勢觀察（週更）：從模式庫萃取的宏觀層——5 條成形趨勢的熱度曲線 + 對現有設計的啟示 |
| [[topics/community-tech-discussions]] | 🌐 社群 | ongoing | 社群技術討論趨勢：設計哲學辯論、實證研究、架構反思（HTML vs MD、Skill Atrophy 等） |
| [[topics/ai-agent-safety]] | 🏛️ 政策/安全 | ongoing | AI agent 安全：中國代理偵測程式碼爭議（v2.1.91+，待確認）+ GitHub Repo prompt injection 多媒體確認 + 假冒安裝包 |
| [[topics/ai-agent-safety-archive]] | 🏛️ 政策/安全 | monitoring | AI Agent 安全時序歷史存檔（2026-05-22 以前）；主頁 [[topics/ai-agent-safety]] 瘦身分流 |
| [[topics/anthropic-government-policy]] | 🏛️ 政策/安全 | monitoring | Anthropic 政府政策攻防：出口管制主線已於 2026-07-01 解除，剩餘承諾落實、歐洲據點爭奪、Legion 訴訟等衍生支線持續觀察 |
| [[topics/official-community-gap]] | 🛠️ 工具/功能 | monitoring | 官方功能 vs 社群痛點缺口矩陣：哪些痛點官方正在解決、哪些結構性缺席 |
| [[topics/enterprise-cost-management]] | 💼 商業 | monitoring | 企業規模採用 Claude 的成本結構挑戰：Uber/Microsoft 案例、缺失工具、因應策略 |
| [[topics/enterprise-tool-tracker]] | 💼 商業 | ongoing | 大型企業 AI 編碼工具使用追蹤：Microsoft/Amazon/Uber/Apple 等企業當前工具選擇與變化軌跡；07-01 補齊 Rubrik/Okta/Globant/DataArt/加州州政府/Lindy 等最新動態 |
| [[topics/community-tech-timeline]] | 🌐 社群 | monitoring | 社群技術應用趨勢完整時序（2026-04-25 至今），從 community-tech-patterns 拆分 |
| [[topics/anthropic-business]] | 💼 商業 | ongoing | Anthropic 商業健康度：企業採用率 34.4%、17 倍訂閱補貼、PMF 觀察、Microsoft 退出風險 |
| [[topics/recursive-self-improvement]] | 🏛️ 政策/安全 | ongoing | AI 遞歸自我改進與全球暫停呼籲：Claude 已寫 80-90% Anthropic 程式碼、工程師代碼產出 8×、全球 AI 煞車踏板呼籲 |
| [[topics/ai-talent-flow]] | 💼 商業 | ongoing | AI 實驗室人才流動與對各公司影響：DeepMind 淨流失（Jumper/Adler/Pritzel）、Anthropic 主要承接、OpenAI 次要承接 |
