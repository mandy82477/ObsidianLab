---
page: "topics/ai-agent-safety-archive"
kind: "topic"
type: "event"
status: "monitoring"
domain: "🏛️ 政策/安全"
last_updated: "2026-08-10"
last_news_update: "2026-06-27"
status_main: "monitoring"
days_since_news: 50
inbound_links: 7
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# AI Agent 安全與可靠性 — 時序存檔

**類型：** event
**狀態：** monitoring
**領域：** 🏛️ 政策/安全
**開始日期：** 2026-04-27
**最後更新：** 2026-08-10
**最後新聞更新：** 2026-06-27

> ai-agent-safety 時序歷史存檔（2026-05-22 以前）+ 技術彙整存檔（2026-05-18 以前，2026-07-01 遷入）。最新時序與分析見 [[topics/ai-agent-safety]]。

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
- **[重大漏洞] Claude Code RCE via 惡意 deeplink**：資安研究人員揭露 Claude Code 存在遠端程式碼執行（RCE）漏洞，攻擊者可透過精心構造的 deeplink 觸發任意指令執行（CyberSecurityNews 報導，05/17 19:20 UTC）；此為繼 CVE-2026-39861（symlink 沙箱逃逸）、1-click RCE（信任提示觸發）後，Claude Code 第三個公開 RCE 類漏洞；攻擊向量從信任提示轉移至 deeplink，意味著攻擊者正在系統性探索 Claude Code 的新攻擊面；**2026-08-10 查證：已修復。** 資安研究員 Joernchen（0day.click）於 2026-05-12 揭露此漏洞，根因為 `main.tsx` 中 `eagerParseCliFlag` 函式在應用程式完整初始化前搶先解析 `--settings` 等命令列旗標，攻擊者可將惡意 `--settings` payload 嵌入 deeplink 的 `q` 參數觸發任意指令執行；Anthropic 已於 **Claude Code 2.1.118** 版修復，改用上下文感知的參數解析區分 CLI 旗標與其值，徹底消除此注入介面（[CyberSecurityNews](https://cybersecuritynews.com/claude-code-rce-flaw/)）

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

## 技術彙整存檔（2026-05-18 以前）

> 以下條目原位於 [[topics/ai-agent-safety]] 的「技術彙整」區塊，因主頁篇幅過長（> 500 行）於 2026-07-01 遷移至此存檔；主頁僅保留近 4-6 週活躍條目。

### Claude Code .env Secrets 本機 SQLite 明文存儲（2026-05-19）

- **揭露來源**：安全工具 Sieve（macOS App Store）在提醒 Claude Code / Cursor 用戶時揭示此問題
- **問題描述**：Claude Code 在正常工作流程中讀取 `.env` 檔案後，所有接觸過的 secrets（API keys、雲端憑證、資料庫密碼等）會以明文永久儲存在本機 SQLite 資料庫
- **為何危險**：（1）SQLite 資料庫不在 `.gitignore` 保護範圍，意外 commit 即全面洩露；（2）標準 secret scanner（如 detect-secrets、gitleaks）不掃描此資料庫位置，無法偵測；（3）攻擊者取得機器存取（或惡意軟體）即可一次取得所有曾操作過的憑證
- **與憑證攻擊的關聯**：此漏洞與 2026-04-30 的憑證竊取攻擊向量直接相關——攻擊者無需攔截 API 呼叫，直接讀取 SQLite 即可取得所有憑證
- **防護建議**：定期清除 Claude Code 本機 SQLite 資料庫；生產憑證不應出現在開發機的 `.env` 中；使用專用 secret manager（AWS Secrets Manager、1Password CLI）替代 `.env` 傳遞方式

### Claude Code RCE via Deeplink（2026-05-18）

- **漏洞類型**：deeplink 觸發遠端程式碼執行（RCE）；攻擊者可透過精心構造的 deeplink URI 觸發 Claude Code 執行任意指令，無需使用者手動確認信任提示
- **與既有漏洞的區別**：與 CVE-2026-39861（symlink 沙箱逃逸）和 1-click RCE（信任提示）為獨立攻擊向量；deeplink 攻擊面代表攻擊者已從「軟體安裝路徑」（假冒安裝包、Google 廣告詐騙）延伸至「執行時期協議處理」
- **攻擊場景**：受害者開啟惡意 deeplink（可能來自 email、網頁、CI/CD 觸發等），Claude Code 在本機執行攻擊者指定的指令
- **當前狀態**：✅ 已修復（2026-08-10 查證）——資安研究員 Joernchen（0day.click）於 2026-05-12 揭露，根因為 `main.tsx` 的 `eagerParseCliFlag` 函式在應用程式完整初始化前搶先解析 `--settings` 等命令列旗標，攻擊者可將惡意 payload 嵌入 deeplink 的 `q` 參數觸發任意指令執行；已於 **Claude Code 2.1.118** 版修復，改用上下文感知的參數解析（[CyberSecurityNews](https://cybersecuritynews.com/claude-code-rce-flaw/)）
- **防護建議**：勿開啟不明來源的 deeplink；在確認修補前避免讓 Claude Code 在高權限環境（root、生產伺服器）執行

### CVE-2026-39861：沙箱逃逸漏洞（CVSS 7.7）（2026-05-08）

- **漏洞類型**：符號連結（symlink）沙箱逃逸，攻擊者可透過惡意 symlink 將檔案寫入工作區目錄以外的位置，突破 Claude Code 的工作區隔離機制
- **嚴重程度**：CVSS 7.7（高危），已取得正式 CVE 編號（CVE-2026-39861），詳見 [GitHub Advisory GHSA-vp62-r36r-9xqp](https://github.com/advisories/GHSA-vp62-r36r-9xqp)
- **修補狀態**：v2.1.64 已修補，dev.to 提供詳細自查指南確認受影響版本
- **雙重壓力**：此漏洞與 1-click RCE 信任提示事件同日在 HN 上版；社群諷刺 Anthropic 自家宣傳的頂級安全模型 Mythos 事先未能偵測到自身產品漏洞，對品牌可信度造成雙重打擊

### 1-click RCE：信任提示觸發遠端代碼執行 + Anthropic 回應危機（2026-05-08）

- **攻擊向量**：Claude Code 的信任提示（trust prompt）可被利用觸發一鍵遠端代碼執行（RCE），The Register 於 2026-05-07 報導
- **Anthropic 回應問題**：公開回應被社群概括為「不應該點確認（Shouldn't have clicked 'ok'）」，被批評為責怪使用者而非修復產品缺陷
- **信任危機升級**：CVE-2026-39861 + 1-click RCE 兩則安全事件同日在 HN 上版，部分社群認為 Anthropic 正在快速消耗開發者社群的信任

### 授權撤銷後 Session 紀錄持續出現（2026-05-06）

- **授權撤銷不等於 session 終止**：用戶撤銷 Claude Code 存取授權後，session 紀錄仍持續出現於使用量儀表板，涉及 `user:file_upload`、`user:ccr_inference` 等 scope；解除安裝並清除憑證後問題依然存在
- **Anthropic 客服未回應**：用戶回報此問題後 Anthropic 支援團隊兩週未回應，構成帳號安全管理的嚴重缺口
- **建議行動**：遭遇此問題應立即重置所有 API 金鑰、撤銷 OAuth Token（設定 → 連接應用程式），並持續監控 Anthropic 使用量儀表板

### Wire Trace 揭示 Auto 模式安全邊界（2026-05-07）

- **Auto 模式安全邊界為提示詞層**：研究者透過 wire trace 截獲 Claude Code 完整系統提示（約 13,000 字），發現「Auto 模式」的權限控制僅是提示詞層面的機制，並非底層沙箱強制約束；安全邊界仰賴 prompt 而非系統隔離
- **MCP 插件 context 耗損**：Figma 等 MCP 插件會大幅佔用 context window，插件越多 context 越快耗盡，間接影響 agent 判斷品質與安全決策
- **企業安全評估含義**：對企業部署 Claude Code 的安全評估具有重要參考價值——不能假設 Auto 模式提供底層沙箱保護，需在架構層補充額外隔離機制

### AI 生成程式碼大規模安全漏洞評測（2026-05-13）

- **評測規模**：研究者以靜態分析工具掃描 48 個由 Lovable、Bolt、Replit 等 AI 生成工具構建的公開應用程式，是目前少見的針對 AI 生成程式碼的大規模公開安全評測
- **主要發現（90% 存在至少一個安全漏洞）**：44% 存在驗證缺口（authentication gaps）；33% 存在可繞過 Row-Level Security 的 Postgres 函式；25% 存在 BOLA/IDOR 問題
- **行業意義**：直接挑戰「AI 快速開發即可上線」的假設；Claude Code 開發者應將安全審查納入標準 PR 流程，不應僅依賴 AI 的程式碼品質判斷
- **方法論侷限**：靜態分析工具只能偵測程式碼層面的已知漏洞模式，無法涵蓋所有執行時期安全問題；實際漏洞率可能更高

### Windows 環境危險系統操作（2026-05-03）

- **系統檔案操作風險**：Claude Code（Opus 4.7 Max effort）在 Windows 11 降級路徑測試中嘗試重命名系統檔案 `powershell.exe`，顯示 agent 在 Windows 環境的危險操作邊界存在盲點
- **平台差異性**：Unix 系統中常見的系統操作保護機制（檔案權限、sudoer 確認）在 Windows 中行為不同；Windows 環境的 agent 部署需額外設計危險系統操作的攔截規則
- **降級路徑測試風險**：此事件發生於測試「降級路徑」場景，意味著即使在設計測試場景下，agent 仍可能執行超出預期的危險操作

### 假冒 Claude Code 官方安裝包惡意軟體攻擊（2026-05-12）

- **多媒體同步確認**：Yahoo Tech、CSO Online、The Register 等多家資安媒體同步報導，攻擊已被研究人員確認成立；此為與 2026-05-10 Google 搜尋廣告木馬不同的獨立攻擊向量，顯示攻擊者正系統性覆蓋所有 Claude Code 安裝路徑
- **IElevator 機制**：攻擊者利用 Windows IElevator（Internet Explorer Elevation Service）進行權限提升，竊取 Chrome 等瀏覽器 Cookie 與開發者機密憑證
- **攻擊向量**：透過偽裝成官方 Claude Code 安裝程式的惡意軟體分發；Google 廣告詐騙（2026-05-10）+ 官方安裝包仿冒（2026-05-12）兩種向量並存，顯示攻擊組織化程度高
- **防護建議**：安裝 Claude Code 唯一安全路徑為 GitHub 官方 Releases（`github.com/anthropics/claude-code`）

### AI 驅動硬體故障注入攻擊（2026-05-12）

- **首個公開記錄案例**：研究團隊 Raelize 發布報告，記錄讓 Claude Code 完全掌控硬體工具、在無任何人工撰寫程式碼的情況下，自主重現 Espressif ESP32 SoC Secure Boot 硬體故障注入（Fault Injection）攻擊的全過程
- **攻擊自主性**：Claude Code 自主設計電壓故障脈衝時序、控制硬體工具、識別成功 bypass 條件，全程無人工程式碼干預
- **雙面性**：研究展示 AI 在硬體安全漏洞探索領域的顛覆性潛力，同時引發對 AI 自主硬體攻擊工具的隱憂

### Google 搜尋 Claude Code 廣告詐騙與木馬植入（2026-05-10）

- **供應鏈攻擊向量**：Google 搜尋「claude code」的第一筆廣告結果出現仿冒 Claude 官方網站，透過偽造官方設計語言的 PowerShell 安裝指令植入 Trojan:Win32/Kepavll!rfn
- **廣告排名機制被濫用**：惡意網站透過 Google 廣告排名高於官網，利用廣大用戶對搜尋首位的信任；仿冒網站採用官方設計語言，極難辨別
- **安裝防護建議**：安裝 Claude Code 等 AI 工具時，應直接前往官方網站（claude.ai）而非點擊搜尋廣告結果

### 無監督長時間 Agent 執行的真實風險（2026-05-13）

- **24 小時實驗**：開發者以 `--dangerously-skip-permissions` 標誌讓 Claude Code 完全自主運行 24 小時，API 帳單達 $400
- **帳單是最小問題**：作者指出更令人憂慮的是代理在無監督下執行了一連串預期之外的操作（超出預期操作範疇，而非惡意行為）
- **與 /loop 失控案例的比較**：2026-05-01 的 $6,000 /loop 失控聚焦費用面，此案例聚焦操作範疇面

### AI Agent 清空資料庫兩次 + 指令防火牆（2026-05-10）

- **事件描述**：開發者使用 Claude Code 建構客服 agent 期間，AI 在一週內兩度清空本機資料庫；事件觸發原因為 agent 誤判清理任務的操作範疇，與 2026-04-28 生產資料庫刪除事件屬同類模式
- **社群防護方案**：開發者因此自建「指令防火牆」（command firewall）作為安全攔截層，屬 `PreToolUse Hook` 防護概念的具體應用
- **官方沙箱呼應**：此案例恰好呼應 Anthropic 同日發布的 Claude Code Sandboxing 官方文件的必要性

### 計費透明度與 repo 內容掃描（OpenClaw，2026-04-30 指控，至今無官方技術說明）

- **OpenClaw 觸發機制**：Claude Code 在執行期間主動掃描 Git commit 訊息與文件內容，特定字串（已知：JSON 格式含 "OpenClaw"）會觸發請求拒絕或立即將 Extra Usage 衝至 100%，此行為從未在官方文件中揭露
- **隱性行為變更**：此類 repo 掃描行為若不透明，等同工具在用戶不知情下依內容改變執行策略，是計費信任危機的核心問題
- **Anthropic vs Google 安全標準差異**：Claude Code 的工作區信任邊界設計被 Anthropic 定義為「設計如此」，但 Google 對 Gemini CLI 類似行為評為 CVSS 10.0 並強制修補

### 用量失控與費用保護（2026-05-01）

- **/loop 指令無人看管風險**：單一 `/loop` 指令若在無監控情況下運行，可在 26 小時內累積 $6,000 費用（46 次迭代 + 長 session）；Anthropic 儀表板金額嚴重滯後，目前無即時消費通知機制
- **MCP 指令執行漏洞**：MCP（Model Context Protocol）的指令執行漏洞成為 VentureBeat 安全警示焦點，多 Agent 工作流中的攻擊面需要額外評估
- **雲端服務配額撤銷**：AWS Bedrock 可無預警將前沿模型配額歸零，企業客戶在雲端架構下的 AI 可用性面臨不透明的服務風險

### Context 壓縮時安全指令保留機制（2026-05-13）

- **更新來源**：Claude Code v2.1.139（2026-05-12）代理提示詞更新，要求在上下文摘要時完整保留安全相關指令（禁止操作規則、憑證處理規範等）
- **解決的問題**：過去 `/compact` 或 context 壓縮後，安全指令可能在摘要過程中被省略，導致壓縮後代理不再遵守特定安全約束
- **適用場景**：搭配 v2.1.139 的 `/goal` fire-and-forget 指令使用時，確保安全約束在整個任務生命週期內持續有效

### Claude Code Sandboxing 官方文件發布（2026-05-10）

- **官方文件正式化**：Anthropic 發布 Claude Code Sandboxing 官方文件，提供透過 OS 層級原語（primitives）對沙箱化 bash 工具實施檔案系統與網路隔離的具體做法
- **設計理念**：核心設計是在 session 開始時預先定義操作邊界，讓 Claude Code 在邊界內自由執行而無需逐指令授權確認，同時縮小意外破壞的半徑；與社群工具 SmolVM（沙盒容器化）的思路一致
- **對社群工具的意義**：官方文件的出現一定程度上補強了 SmolVM、Groundtruth 等社群工具所填補的需求，也為企業部署提供官方背書的安全邊界設計框架

### Claude Code v2.1.136「操作安全與如實回報」機制（2026-05-09）

- **系統提示大幅更新（+525 tokens）**：v2.1.136 在系統提示層新增逾 525 tokens 的安全規範，是 Anthropic 迄今最明確的 agent 行為規範化文件
- **不可逆操作確認機制**：對外部有影響的操作（網路請求、檔案系統修改）及不可逆操作，執行前須先獲取明確授權；刪除操作執行前需檢視目標內容，防止誤刪
- **如實回報義務（Truthful Reporting）**：必須如實回報跳過的步驟與未通過的測試，禁止隱藏失敗或選擇性回報成功
- **`hard_deny` 無條件封鎖類別**：代理自訂規則新增 `hard_deny` 類別，表示無條件的安全邊界封鎖；`soft_deny` 適用範圍相應縮小

### 憑證安全（2026-04-30）

- **AI coding agent 憑證竊取**：攻擊者已從「嘗試操控模型」轉向「竊取 agent 所使用的憑證」，API key、cloud credentials 是主要目標
- **ANTHROPIC_API_KEY 環境變數陷阱**：雲端環境設置此變數會導致 Claude Code 改走 API 計費，同時也是憑證暴露的風險點（見 [[entities/pricing]]）

---

## 相關實體

- [[topics/ai-agent-safety]] — 本頁主頁面（最新時序與分析）
- [[entities/claude-code]]
- [[entities/pricing]]
- [[topics/anthropic-government-policy]]
