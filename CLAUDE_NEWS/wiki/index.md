# Wiki 目錄

LLM 查詢此 wiki 時，**先讀這個檔案**找相關頁面，再讀具體頁面取得詳細資訊。

**最後更新：** 2026-05-29 | **頁面數：** 35

---

## 概覽

- [[overview]] — 當前 Claude / Anthropic 生態系整體局勢（每週更新）
- [[feature-radar]] — 新功能熱度追蹤、試用推薦與快速上手（每次 ingest 更新）

---

## Entities（實體頁）

| 頁面 | 類型 | 狀態 | 摘要 |
|------|------|------|------|
| [[entities/claude-code]] | product | active | Claude Code CLI 主頁：功能、已知問題、社群工具 |
| [[entities/opus-4-8]] | model | active | Opus 4.8：SWE-bench Pro 69.2%、1M context、Dynamic Workflows（1,000 子代理）、Fast Mode 1/3 費用 |
| [[entities/opus-4-7]] | model | active（爭議）| Opus 4.7 發布細節、思考深度爭議、cache 問題 |
| [[entities/pricing]] | policy | 持續調整 | 訂閱方案、近期政策變動、token 成本注意事項 |
| [[entities/mythos]] | model | 公開化中 | 高能力安全模型；10K–23K 漏洞（三媒體確認）；The Register/Gotrade/CyberSecurityNews 三方確認透過 Claude Code 公開釋出 |
| [[entities/bugcrawl]] | feature | 測試中 | Anthropic 測試中的 Claude Code 漏洞偵測工具 |
| [[entities/project-deal]] | feature | 實驗中 | Anthropic Claude 代理人自主交易談判實驗，Opus vs Haiku 差異顯著 |
| [[entities/claude-design]] | feature | active（初期）| Anthropic AI 設計工具，首日社群反映幻覺多、風格偏移、Claude Code 整合差 |
| [[entities/claude-security]] | product | public beta | Claude Security 資安產品，情境化安全評估，整合於 Claude Code 開發環境 |
| [[entities/openclaw]] | product | 允許（信用池計費）| 第三方 agentic 工具，歷經禁令後 6/15 起恢復允許但改走信用池 API 費率計費 |
| [[entities/google-investment]] | event | resolved | Google 投資 400 億美元歷史記錄，含循環算力交易結構 |
| [[entities/managed-agents]] | feature | active（正式發布）| Managed Agents 官方框架：Dreaming 記憶整合、20 路並行子代理、Outcomes 規格驗證 |
| [[entities/stainless]] | product | acquired | Anthropic 以 ~$300M 收購，官方 SDK + MCP 伺服器生成商，MCP 生態基礎設施控制點 |
| [[entities/boris-cherny]] | person | active | Claude Code 創始人，「Loops 是未來」設計哲學、「coding is solved」論戰、第三方工具邊界聲明 |
| [[entities/cat-wu]] | person | active | Claude Code 產品負責人，「AI 下一步是主動性（proactivity）」論述 |
| [[entities/andrej-karpathy]] | person | active（待核實）| 近期加入 Anthropic，CLAUDE.md 四條規則、「最小必要 context」費用控管原則 |
| [[entities/chris-olah]] | person | active | Anthropic 共同創辦人、AI 可解釋性研究先驅；2026-05-26 梵蒂岡封論揭幕演講 |
| [[entities/opencode]] | product | active（快速成長）| Claude Code 主要開源替代品，157K 開發者分流，OpenCode-power-pack 移植官方 11 個 skills |

---

## Topics（進行中議題）

| 頁面                                     | 狀態         | 摘要                                                             |
| -------------------------------------- | ---------- | -------------------------------------------------------------- |
| [[topics/code-quality-decline]]        | monitoring | Claude Code 效能退步事件，Anthropic 已承認工程疏失                           |
| [[topics/google-investment]]           | resolved   | ⚠️ 已遷移至 [[entities/google-investment]]                         |
| [[topics/competitor-landscape]]        | ongoing    | Google 祕密開發競品 + OpenCode 157K 分流 + DeepSeek clone 低成本替代生態      |
| [[topics/community-tech-tools]]        | ongoing    | 社群工具目錄：132 工具的活躍度、採用狀態追蹤                                       |
| [[topics/community-tech-patterns]]     | ongoing    | 社群技術模式：multi-agent、skills 設計、工作流最佳實踐                           |
| [[topics/community-tech-discussions]]  | ongoing    | 社群技術討論趨勢：設計哲學辯論、實證研究、架構反思（HTML vs MD、Skill Atrophy 等）          |
| [[topics/ai-agent-safety]]             | ongoing    | AI agent 安全：Claude Code v2.1.150 遠端系統提示注入披露（GrowthBook 60s 更新）+ 假冒安裝包 + 資料庫刪除事件 |
| [[topics/anthropic-government-policy]] | monitoring | Anthropic 政府與軍事政策：五角大廈排除事件、安全護欄堅持、白宮重啟談判（11 天無新進展）             |
| [[topics/official-community-gap]]      | ongoing    | 官方功能 vs 社群痛點缺口矩陣：哪些痛點官方正在解決、哪些結構性缺席                            |
| [[topics/enterprise-cost-management]]  | ongoing    | 企業規模採用 Claude 的成本結構挑戰：Uber/Microsoft 案例、缺失工具、因應策略                            |
| [[topics/enterprise-tool-tracker]]     | ongoing    | 大型企業 AI 編碼工具使用追蹤：Microsoft/Amazon/Uber/Apple 等企業當前工具選擇與變化軌跡                  |
| [[topics/community-tech-timeline]]     | ongoing    | 社群技術應用趨勢完整時序（2026-04-25 至今），從 community-tech-patterns 拆分                         |
| [[topics/anthropic-business]]          | ongoing    | Anthropic 商業健康度：企業採用率 34.4%、17 倍訂閱補貼、PMF 觀察、Microsoft 退出風險 |

---

## 新增頁面的規則

- **新 entity**：被日報提及 2 次以上的模型、功能、人物 → 建立 `entities/xxx.md`
- **新 topic**：同一事件跨越 2 天以上 → 建立 `topics/xxx.md`
- 新增後在此表格加一行，並在 `log.md` 追加紀錄
