# Wiki 目錄

LLM 查詢此 wiki 時，**先讀這個檔案**找相關頁面，再讀具體頁面取得詳細資訊。

**最後更新：** 2026-05-15（拆分技術討論頁）| **頁面數：** 23

---

## 概覽

- [[overview]] — 當前 Claude / Anthropic 生態系整體局勢（每週更新）
- [[feature-radar]] — 新功能熱度追蹤、試用推薦與快速上手（每次 ingest 更新）

---

## Entities（實體頁）

| 頁面 | 類型 | 狀態 | 摘要 |
|------|------|------|------|
| [[entities/claude-code]] | product | active | Claude Code CLI 主頁：功能、已知問題、社群工具 |
| [[entities/opus-4-7]] | model | active（爭議）| Opus 4.7 發布細節、思考深度爭議、cache 問題 |
| [[entities/pricing]] | policy | 持續調整 | 訂閱方案、近期政策變動、token 成本注意事項 |
| [[entities/mythos]] | model | 限制存取 | 高能力安全模型，七週發現 2,000+ 漏洞 |
| [[entities/bugcrawl]] | feature | 測試中 | Anthropic 測試中的 Claude Code 漏洞偵測工具 |
| [[entities/project-deal]] | feature | 實驗中 | Anthropic Claude 代理人自主交易談判實驗，Opus vs Haiku 差異顯著 |
| [[entities/claude-design]] | feature | active（初期）| Anthropic AI 設計工具，首日社群反映幻覺多、風格偏移、Claude Code 整合差 |
| [[entities/claude-security]] | product | public beta | Claude Security 資安產品，情境化安全評估，整合於 Claude Code 開發環境 |
| [[entities/openclaw]] | product | 允許（信用池計費）| 第三方 agentic 工具，歷經禁令後 6/15 起恢復允許但改走信用池 API 費率計費 |
| [[entities/google-investment]] | event | resolved | Google 投資 400 億美元歷史記錄，含循環算力交易結構 |
| [[entities/managed-agents]] | feature | active（正式發布）| Managed Agents 官方框架：Dreaming 記憶整合、20 路並行子代理、Outcomes 規格驗證 |
| [[entities/boris-cherny]] | person | active | Claude Code 創始人，「Loops 是未來」設計哲學、「coding is solved」論戰、第三方工具邊界聲明 |
| [[entities/cat-wu]] | person | active | Claude Code 產品負責人，「AI 下一步是主動性（proactivity）」論述 |

---

## Topics（進行中議題）

| 頁面 | 狀態 | 摘要 |
|------|------|------|
| [[topics/code-quality-decline]] | monitoring | Claude Code 效能退步事件，Anthropic 已承認工程疏失 |
| [[topics/google-investment]] | resolved | ⚠️ 已遷移至 [[entities/google-investment]] |
| [[topics/competitor-landscape]] | ongoing | Google 祕密開發競品 + OpenCode 157K 分流 + DeepSeek clone 低成本替代生態 |
| [[topics/community-tech-patterns]] | ongoing | 社群技術應用趨勢：multi-agent、skills 設計、工具生態（70+ 工具）|
| [[topics/community-tech-discussions]] | ongoing | 社群技術討論趨勢：設計哲學辯論、實證研究、架構反思（HTML vs MD、Skill Atrophy 等）|
| [[topics/ai-agent-safety]] | ongoing | AI agent 安全：假冒安裝包 + AI 生成程式碼 90% 漏洞 + CVE-2026-39861 + 資料庫刪除事件 |
| [[topics/anthropic-government-policy]] | monitoring | Anthropic 政府與軍事政策：五角大廈排除事件、安全護欄堅持、白宮重啟談判（11 天無新進展）|

---

## 新增頁面的規則

- **新 entity**：被日報提及 2 次以上的模型、功能、人物 → 建立 `entities/xxx.md`
- **新 topic**：同一事件跨越 2 天以上 → 建立 `topics/xxx.md`
- 新增後在此表格加一行，並在 `log.md` 追加紀錄
