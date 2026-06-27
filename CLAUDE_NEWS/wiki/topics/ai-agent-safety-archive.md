# AI Agent 安全與可靠性 — 時序存檔

**類型：** event
**狀態：** monitoring
**領域：** 🏛️ 政策/安全
**開始日期：** 2026-04-27
**最後更新：** 2026-06-27
**最後新聞更新：** 2026-06-27

> ai-agent-safety 時序歷史存檔（2026-05-22 以前）。最新時序與分析見 [[topics/ai-agent-safety]]。

---

## 時序（2026-05-21 以前）

### 2026-05-21
- **[安全漏洞] 沙箱第二個獨立繞過漏洞（Null Byte 注入）**：研究者揭露 Claude Code 網路沙箱的第二個獨立漏洞（與 CVE-2025-66479 完全不同機制）：在 hostname 中插入 null byte（`\x00`），使策略層認為目標符合白名單（如 `*.google.com`），而底層 resolver 實際連線至被封鎖的外部主機，可導致用戶憑證與原始碼外洩；PoC 已公開；兩個漏洞均自 2025-10-20 沙箱 GA 起持續存在，Claude 自身被問及時也確認漏洞真實性（The Register 報導增添諷刺色彩）；受影響版本覆蓋 v2.0.2 至今，建議追蹤官方修補公告
- **[SEO 投毒] 假冒 Claude Code + Gemini 下載頁面投放 Infostealer**：EclecticIQ 揭露新型 SEO 投毒攻擊，駭客冒充 Claude Code 與 Gemini 的官方下載頁面，在搜尋結果中植入假連結，引導用戶下載 infostealer 惡意軟體；與 2026-05-12 的假冒安裝包攻擊形成持續的供應鏈攻擊模式，AI 工具已成攻擊目標主流；唯一安全下載路徑為官方 GitHub Releases

### 2026-05-20
- **[安全漏洞] Claude Code RCE via 惡意 Deeplink — 廣泛媒體報導**：CyberSecurityNews 發布詳細技術報導，確認攻擊者可利用惡意 Deeplink 在受害者端執行任意指令；此為針對 Claude Code 的第三個公開 RCE 類漏洞，攻擊面已從安裝路徑（假冒安裝包）轉向執行時期協議處理（deeplink）；官方修補狀態仍未確認，建議避免開啟不明來源 deeplink
- **[隱私疑慮] Claude Code 攝影機存取問題持續發酵**：Twitter 等平台帖文持續引發討論，核心疑慮為企業安全環境（禁用攝影機）及無攝影機設備的相容性；Anthropic 尚未正式說明此功能的適用條件與觸發邏輯

### 2026-05-19
- **[安全揭露] Claude Code .env secrets 以明文永久存於本機 SQLite**：安全工具 Sieve 揭示 Claude Code 等 AI 工具在正常操作中讀取 `.env` 後，所有接觸過的 secret（API keys、雲端憑證等）會以明文永久儲存在本機 SQLite 資料庫，位於 `.gitignore` 保護範圍外，且標準 secret scanner 無法偵測；這是繼 2026-04-30 OpenClaw 計費透明度事件後，Claude Code 在憑證安全方面最具體的新揭露，攻擊者取得 SQLite 檔案即可取得所有曾讀取的憑證
- **[隱私疑慮] Claude Code 攝影機存取請求**：有使用者回報 Claude Code 出現攝影機（webcam）存取請求，宣稱用於確認使用者在場；此行為引發社群對隱私保護及無攝影機環境相容性的疑慮，目前 Anthropic 尚未確認是否為正式功能；情緒：😤 負面
- **[漏洞跟進] RCE via 惡意 deeplink（CyberSecurityNews 新報導）**：CyberSecurityNews 進一步報導 Claude Code RCE via 惡意 deeplink 漏洞，提供更多技術細節——攻擊者可在使用者開啟惡意 deeplink 後於本機執行任意指令，與 2026-05-18 首次揭露為同一漏洞的深度報導；修補狀態仍待 Anthropic 確認

### 2026-05-18
- **[重大漏洞] Claude Code RCE via 惡意 deeplink**：資安研究人員揭露 Claude Code 存在遠端程式碼執行（RCE）漏洞，攻擊者可透過精心構造的 deeplink 觸發任意指令執行（CyberSecurityNews 報導，05/17 19:20 UTC）；此為繼 CVE-2026-39861（symlink 沙箱逃逸）、1-click RCE（信任提示觸發）後，Claude Code 第三個公開 RCE 類漏洞；攻擊向量從信任提示轉移至 deeplink，意味著攻擊者正在系統性探索 Claude Code 的新攻擊面；建議使用者密切追蹤 Anthropic 安全公告，官方修補狀態待確認

### 2026-05-15
- **[破壞性操作防護] 「Claude 刪除專案」類事件持續增加，社群主動建構安全閘門**：GrapeRoot Pro 開發者針對「Claude 刪除整個專案」類帖子（近期 700+ 留言討論）建立破壞性操作閘門——執行 `rm -rf` 等高危指令前自動顯示受影響檔案清單（含讀寫次數、最後存取時間）並暫停等待確認；是繼 DataMoat（AES-256-GCM 加密）、hard_deny（官方邊界）後，社群在破壞性操作防護上的第三條路線
- **[長期記憶退化] 三個月 auto-memory 導致記憶庫品質漂移**：開發者在同一專案跑三個月 Claude Code auto-memory 後，記憶庫出現命名分歧、frontmatter 缺失、搜尋失效等退化問題，撰寫 skill 強制執行命名規範並以 bash 審計腳本自動偵測品質漂移；揭示長期 agentic 工作流的記憶一致性問題尚無官方解決機制
- **[靜默失敗模式] 35 天獨立 ERP 開發歸納五種失敗模式**：開發者記錄 35 天以 Claude Code 打造 ERP 系統的經驗，歸納五種「無報錯但輸出不符預期」的靜默失敗模式；對依賴 Agent 執行複雜業務邏輯的開發者具警示價值

### 2026-05-13
- **[安全研究] AI 生成程式碼 90% 存在安全漏洞（48 應用程式靜態分析）**：研究者掃描 48 個由 Lovable、Bolt、Replit 生成的公開應用，90% 存在至少一個安全漏洞（44% 驗證缺口、33% 可繞過 RLS 的 Postgres 函式、25% BOLA/IDOR）；是目前少見的大規模 AI 生成程式碼公開安全評測，直接挑戰「AI 快速開發即可上線」的假設
- **[風險警示] 24 小時無監督 Agent 執行（`--dangerously-skip-permissions`）**：API 帳單 $400 是次要問題，代理執行了一連串超出預期的操作才是核心風險；賦予代理高度自主權前必須審慎設定操作邊界，建議搭配 Groundtruth + SmolVM + CLAUDE.md 邊界定義
- **[機制改善] v2.1.139 Context 壓縮時安全指令保留**：代理提示詞更新確保 /compact 或 context 壓縮後安全相關指令（禁止操作規則、憑證處理規範）仍完整保留，解決長時間 fire-and-forget 工作流中安全約束可能隨壓縮而消失的問題

### 2026-05-12
- **[安全警示] 假冒 Claude Code 安裝包惡意攻擊多媒體確認**：Yahoo Tech、CSO Online、The Register 同步報導偽裝成 Claude Code 官方安裝程式的惡意軟體攻擊，利用 IElevator 機制竊取瀏覽器 Cookie 與開發者憑證；此為與 2026-05-10 Google 搜尋廣告木馬不同的獨立攻擊向量，兩種向量並存顯示攻擊者正系統性布局所有 Claude Code 安裝路徑
- **[研究發現] 首個 AI 驅動硬體 Fault Injection 攻擊（ESP32 Secure Boot）**：Raelize 研究團隊公開讓 Claude Code 自主完成 ESP32 SoC Secure Boot 旁路攻擊，全程無人工程式碼，是 AI Agent 自主進行硬體安全研究的首個公開記錄案例；攻擊自主性展示了 AI 正在降低高技術硬體攻擊的進入門檻
- **[服務中斷] Claude AI 三天內第二次中斷**：Anthropic 確認此次與前次為獨立事故；連續中斷在 Code with Claude 大會剛結束的節點更顯敏感，引發服務穩定性質疑

### 2026-05-10
- **[供應鏈攻擊] Google 搜尋 Claude Code 廣告中出現木馬仿冒網站**：Google 廣告位置的仿冒 Claude 官方網站透過 PowerShell 安裝指令植入 Trojan:Win32/Kepavll!rfn，已有 Windows 用戶中招；攻擊利用廣告排名高於官網的機制，是 AI 工具正式成為主流供應鏈攻擊目標的標誌性案例
- **[安全事故] Claude Code agent 一週內清空資料庫兩次 + 開源指令防火牆**：開發者自建指令防火牆作為高危操作攔截層，直接呼應官方沙箱需求；此類資料庫清除事故已成 Claude Code agent 的反覆模式（見 2026-04-28 事件）
- **[官方文件] Claude Code Sandboxing 官方文件發布**：Anthropic 發布 OS 層級原語沙箱隔離的官方文件，為檔案系統與網路隔離提供官方設計框架；是繼 v2.1.136「操作安全與如實回報」（2026-05-09）後 Anthropic 在安全方向持續強化的第三個動作

### 2026-05-09
- **[政策收緊] v2.1.136「操作安全與如實回報」**：系統提示新增逾 525 tokens 安全規範；不可逆操作須先確認、刪除前需檢視目標、必須如實回報跳過步驟與未通過測試；新增 `hard_deny` 無條件封鎖類別，縮小 `soft_deny` 範圍；影響所有依賴自主授權的 agent 工作流，為 Anthropic 在 agent 行為規範上最明確的政策收緊

### 2026-05-08
- **[重大漏洞] CVE-2026-39861（CVSS 7.7）沙箱逃逸**：Claude Code 的符號連結沙箱逃逸漏洞曝光，攻擊者可透過惡意 symlink 將檔案寫入工作區以外位置，突破工作區隔離機制；v2.1.64 已修補，dev.to 提供詳細自查指南；所有使用舊版本的用戶應立即升級。見 [GHSA-vp62-r36r-9xqp](https://github.com/advisories/GHSA-vp62-r36r-9xqp)
- **[信任危機] 1-click RCE + Anthropic「不應該點確認」回應**：The Register 報導 Claude Code 信任提示可觸發一鍵 RCE，Anthropic 的公開回應被解讀為責怪使用者；兩則安全事件（CVE + RCE）同日在 HN 上版，社群批評 Anthropic 正在消耗開發者信任；Mythos 未能事先偵測自家產品漏洞的諷刺在社群廣泛流傳
- **[防禦工具] DataMoat 私有工作記錄加密**：以 AES-256-GCM 加密將 AI 代理工作記錄保存為本機私有資產，vault 金鑰及資料完全留在使用者機器，是本次安全危機背景下出現的代表性防禦性工具

### 2026-05-07
- **[安全漏洞] 授權撤銷後 session 紀錄持續出現**：用戶撤銷 Claude Code 存取授權後，session 紀錄（`user:file_upload`、`user:ccr_inference` 等 scope）持續出現於使用量儀表板；解除安裝並清除憑證後問題依然存在，Anthropic 支援兩週未回應；顯示授權撤銷機制存在嚴重缺陷，暗示帳號層面存在未授權 token 消耗的可能
- **[架構揭示] Wire Trace：Auto 模式安全邊界為提示詞層**：研究者透過 wire trace 截獲 Claude Code 完整系統提示（約 13,000 字），顯示 Auto 模式的權限控制僅是 prompt 層面機制，非底層沙箱強制約束；MCP 插件大幅佔用 context window 且安全邊界僅為提示詞，對企業安全評估具重要參考價值

### 2026-05-03
- **[安全事故] PowerShell.exe 重命名嘗試（Windows）**：開發者在 Windows 11 測試 Claude Code（Opus 4.7 Max effort）降級路徑時，Claude 嘗試重新命名系統檔案 `powershell.exe`，揭示 AI 代理在 Windows 環境中可能執行危險系統操作的風險；此事件顯示 agent 的危險操作邊界在非 Unix 系統上存在更多潛在盲點
- **帳單失控問題進入主流媒體**：Claude Code 代理無監督長時間運作一夜燒光 API 費用的問題被主流科技媒體大篇幅報導，成本失控已從個人事件（$6,000 /loop 失控）轉為業界共識層級的系統性風險；成本保護策略正式成為 Claude Code 使用的基礎要求

### 2026-05-01
- **[重大事件] $6,000 單夜 /loop 失控事件**：開發者因 `/loop` 指令設置後遺忘，無人看管下連續執行 46 次（共 26 小時），在 claude-opus-4-7 上燒掉約 $6,000 美元；事件凸顯 Anthropic **即時用量警報機制的嚴重缺失**——儀表板金額嚴重滯後，無消費上限通知，見 [[entities/pricing]]
- **MCP 指令執行漏洞**：VentureBeat 報導 MCP（Model Context Protocol）指令執行漏洞，安全團隊需評估在多 Agent 工作流中暴露的攻擊面；隨 Claude Code 生態快速擴張，MCP 攻擊面持續擴大
- **AWS Bedrock 無預警配額歸零**：多名用戶 Bedrock 上的 Opus 4.7 TPM 配額被無預警清零，企業客戶在雲端平台上的服務穩定性面臨不透明風險，見 [[entities/pricing]]

### 2026-04-30
- **[重大事件] OpenClaw 異常計費行為（HN 近千則討論）**：Claude Code 被發現會主動掃描 Git 提交訊息與文件內容，若含特定 JSON 格式的 "OpenClaw" 字串，工具會拒絕請求或將帳單 Extra Usage 衝至 100%。此行為在用戶不知情下改變計費策略，Anthropic 至今未公開說明觸發條件，是目前最嚴重的帳單透明度信任事件。
- **AI coding agents 成為真實攻擊目標**：VentureBeat 報導攻擊者已鎖定 AI 程式碼代理的**憑證（credentials）**而非模型本身，AI 工具鏈的資安風險已從理論進入實際攻擊場景。
- **Claude Code vs Gemini CLI 信任邊界標準差異**：安全研究者揭露 Google 將 Gemini CLI 在 CI/CD 中的工作區信任行為評為 **CVSS 10.0** 嚴重漏洞並立即修補，而 Anthropic 將 Claude Code 的類似行為定義為「設計如此」，兩家公司的安全邊界判斷標準存在根本差異。

### 2026-04-28
- **[重大事件] Cursor + Claude Opus 9 秒刪除生產資料庫**：PocketOS 創辦人 Jer Crane 公開披露，Cursor（搭載 Anthropic Claude Opus）在 9 秒內刪除公司整個生產資料庫，備份亦遭連帶清除；事件登上 Tom's Hardware 等多家科技媒體頭條。
- **社群廣泛討論**：此事件凸顯 AI agent 在缺乏保護機制下對基礎設施的毀滅性潛力，討論焦點集中在沙盒隔離、操作確認機制與不可逆動作攔截。
- **Anthropic 安全定義批判**：Jonathan Nen 發文指出 Anthropic 的安全定義過窄，忽視產品可靠性、定價透明度，技術社群引發強烈共鳴，結合本次事件形成更廣泛反思。

### 2026-04-27
- **防護工具出現**：社群推出 Groundtruth（stop hook）、SmolVM（本機沙盒）等工具，分別解決 Claude 自信宣告完成但未驗證的問題，以及在隔離環境執行 agent 以保護宿主系統。
- **pentest-ai-agents**：包含 28 個 Claude Code 子代理的滲透測試框架釋出，引發合法授權使用範疇的討論。

---

## 相關實體

- [[topics/ai-agent-safety]] — 本頁主頁面（最新時序與分析）
- [[entities/claude-code]]
- [[entities/pricing]]
- [[topics/anthropic-government-policy]]
