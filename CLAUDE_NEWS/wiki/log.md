# Wiki 操作日誌

Append-only 紀錄。每次 ingest、query 或 lint 都在此追加一條。
格式：`## [YYYY-MM-DD] 類型 | 說明`

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
