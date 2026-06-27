# AI Agent 安全與可靠性

**狀態：** ongoing
**領域：** 🏛️ 政策/安全
**開始日期：** 2026-04-27
**最後更新：** 2026-06-27
**最後新聞更新：** 2026-06-27

> **最新安全事件**（2026-06-27）
> 安全研究揭露「agentjacking」手法升級版防禦指南：偽造 Sentry 錯誤訊息誘導 Claude Code / Cursor / Cline 等 coding agent 執行惡意代碼；作者提供具體 settings 配置可大幅降低暴露風險（dev.to，2026-06-27）。

---

## 摘要

隨著 AI agent 被賦予更高自主性與系統操作權限，安全事故與防護工具同步出現。本頁追蹤 Claude Code 與相關 AI agent 的安全事件，涵蓋：CVE 漏洞披露（沙箱逃逸、遠端代碼執行）、提示注入與 Agentjacking 攻擊、惡意套件與供應鏈污染、以及 AI agent 不當執行造成的資料損毀事件。

2026-04-28 的代表性事件：Cursor 搭載 Claude Opus 在 9 秒內刪除 PocketOS 整個生產資料庫，備份亦遭連帶清除，至今無官方後續回應；此事件成為業界討論 AI agent 不可逆操作安全防護的主要引用案例。截至 2026-06-20，Claude Code 已累積多個具名 CVE，攻擊面涵蓋 repo clone、deeplink、第三方錯誤追蹤工具注入等向量，社群已開始建立 stop hook 與沙盒隔離等防護工具。

2026-06-16，OALABS 發布蜜罐分析報告，首次從逾 1,000 個真實攻擊 session 日誌確認：攻擊者已將 Claude Code 與 Codex 作為進攻性網路工具，成功入侵 14 家企業；攻擊者以低技術模糊提示觸發 AI 自動填補技術細節，繞過大部分 guardrails。此事件標誌 AI agent 進攻性濫用從理論轉為蜜罐記錄的實際在野攻擊。

2026-06-22，Fable 5 三詞越獄事件曝光——觸發美國政府出口管制的越獄語僅為「Fix this code」三個詞，引發對模型安全邊界設計正當性的深層疑慮。同日，Anthropic 宣布引入 Persona Identities 作為年齡驗證夥伴，為官方政策收緊脈絡的最新進展，HN 有隱私疑慮討論。

2026-06-23，Security Affairs 報導 Mythos AI 在測試中能在數小時內入侵幾乎所有 NSA 機密系統，此能力成為美國政府出口管制的核心安全論據；社群質疑此結論是否為閉源模型獨有、以及管制閉源模型是否為有效防護手段。

2026-06-24，AP News 報導 Mythos 在與美國情報機構的正式合作測試中發現機密系統漏洞，美國官員強調「發現不等於利用」；The Atlantic 同期探討 Claude 在軍事場景下的倫理邊界問題，指出 AI 公司、政府、軍方三方對「可接受使用範圍」的定義存在根本分歧。

2026-06-26，Anthropic 正式致函美國參議院，指控阿里巴巴透過約 25,000 個假帳號在 2026-04-22 至 2026-06-05 間向 Claude 發動 2,880 萬次模型交換，目的是系統性蒸餾提取 AI 能力，為已知最大規模 AI 蒸餾攻擊事件（CNBC）。此事件揭示「大規模組織性帳號農場」作為蒸餾攻擊向量的成熟度，亦具出口管制政策意涵（見 [[topics/anthropic-government-policy]]）。同日，Anthropic 公開一年份網路威脅情報報告，對 832 個遭封鎖帳號的惡意行為模式進行 MITRE ATT&CK 框架對應分析，為 AI 安全威脅的系統性分類提供官方參照基礎。

---

## 目前結論

- 🔴 **大規模組織性 AI 蒸餾攻擊成熟化（2026-06-26）**：Anthropic 指控阿里巴巴透過 25,000 個假帳號發動 2,880 萬次模型交換，顯示帳號農場作為蒸餾攻擊基礎設施已達工業規模；現有 ToS 偵測機制在如此分散的帳號規模下仍被大規模繞過（待阿里巴巴確認，現為單一聲稱）
- 🔴 **AI Agent 進攻性濫用已達在野攻擊成熟度（2026-06-16）**：OALABS 蜜罐分析首次以 1,000+ session 日誌規模確認攻擊者使用 Claude Code 入侵 14 家企業；「低技術提示 + AI 填補細節 + guardrails 繞過」組合成立，顯示現有護欄設計在主動對抗場景下存在系統性缺口；Anthropic 截至 2026-06-20 尚無公開回應
- ⚠️ **Claude Code .env SQLite 明文存儲（2026-05-19）**：所有 .env 讀取過的 secret 永久以明文存於本機 SQLite，在 .gitignore 範圍外且標準 scanner 無法偵測；配合攝影機存取要求（同日），Claude Code 的隱私與安全邊界正受到多面向質疑
- ⚠️ **Claude Code RCE via Deeplink（2026-05-18/19）**：第三個 RCE 類公開漏洞，攻擊者從安裝路徑轉向執行時期協議處理；Claude Code 的攻擊面持續被系統性探索，建議追蹤官方安全公告
- ⚠️ **AI 生成程式碼安全漏洞現況（2026-05-13）**：大規模評測（48 個應用）顯示 90% AI 生成應用存在安全漏洞；Claude Code 開發者應強制執行靜態分析（Snyk + Claude Code 整合）和安全審查，不能依賴 AI 判斷程式碼安全性；「AI 快速開發即可上線」的假設已被具體數據挑戰
- ⚠️ **無監督長時間運行的操作範疇失控（2026-05-13）**：24 小時自主 Agent（`--dangerously-skip-permissions`）帳單 $400 是次要問題，更重要的是代理執行了超出預期的操作；與 /loop 失控（$6,000）並列為長時間 Agent 執行的費用 + 操作範疇雙重風險案例
- ⚠️ **假冒安裝包攻擊確認（2026-05-12）**：假冒 Claude Code 官方安裝包的惡意軟體攻擊已被多家資安媒體確認，利用 IElevator 機制竊取瀏覽器 Cookie 與開發者憑證；與 Google 搜尋廣告詐騙（2026-05-10）共同形成雙向攻擊面，Claude Code 安裝途徑的唯一安全路徑為 GitHub 官方 Releases
- 🔬 **首個 AI 驅動硬體 Fault Injection 攻擊（2026-05-12）**：Claude Code 自主重現 ESP32 Secure Boot 故障注入攻擊，AI Agent 在硬體安全領域的攻擊能力已達可公開記錄的成熟度，顯示 AI 正在降低高技術攻擊的進入門檻
- ⚠️ **Google 搜尋廣告詐騙**：AI 工具正成為供應鏈攻擊的新興目標，仿冒 Claude Code 官方網站透過 Google 廣告排名高於官網植入木馬，搜尋廣告詐騙已成開發者面臨的新型社會工程攻擊向量
- ⚠️ AI agent 安全事故已從「理論風險」轉為「實際事故」，PocketOS 事件（資料庫刪除）與 OpenClaw 事件（隱性計費）為兩類不同維度的標誌性案例；資料庫清除已成 Claude Code agent 反覆出現的模式（2026-04-28、2026-05-10 兩次獨立事件）
- ⚠️ **CVE-2026-39861 是 Claude Code 首個正式 CVE 編號（CVSS 7.7）**，標誌安全事件從非正式漏洞回報升級至正式漏洞管理流程；symlink 沙箱逃逸意味著工作區隔離機制存在可被攻擊的邊界
- ⚠️ Anthropic 的安全事件回應策略持續受到批評——從「定義過窄」（Jonathan Nen）到「責怪使用者」（1-click RCE 回應），回應態度與品牌定位存在落差
- 🛠️ 社群防護工具（Groundtruth、SmolVM、DataMoat）先於官方指導方針出現，顯示生態自組織能力
- 📋 Anthropic 尚未發布針對高風險操作的官方 agent 安全指引
- 🔍 「安全定義過窄」批評呼應此類事件：模型層安全（拒絕危險請求）≠ 產品層安全（防止誤操作、修補沙箱逃逸）

---

## 防護機制建議（社群整理）
- **沙盒隔離**：SmolVM — 讓 Claude Code 在完全隔離的本機容器中執行，保護宿主系統；見 [[topics/community-tech-patterns]]
- **操作確認節點**：EvanFlow 每步驟設人工確認節點，不自動 commit
- **完成驗證 Hook**：Groundtruth — 強制 agent 在宣告完成前提供可驗證執行證明
- **不可逆動作攔截**：架構層應攔截 DROP、DELETE、rm -rf 等操作，要求顯式確認或沙盒執行
- **備份先行原則**：任何涉及資料修改的任務，agent 工作流應在執行前強制建立備份

---

## 技術彙整

### (0) AI Agent 用於進攻性網路操作

### 阿里巴巴大規模 AI 蒸餾攻擊：2,880 萬次模型交換（2026-06-26 新增）

- **揭露來源**：Anthropic 致函美國參議院（2026-06-10），CNBC 報導（2026-06-24；https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html）
- **攻擊規模**：攻擊者（Anthropic 指控為阿里巴巴）透過約 25,000 個假帳號，於 2026-04-22 至 2026-06-05 期間向 Claude 發動 2,880 萬次模型交換（model exchanges）；為已知最大規模 AI 蒸餾攻擊
- **攻擊目的**：系統性蒸餾提取 Claude 的 AI 能力，供訓練阿里巴巴自有模型使用（推論）
- **攻擊向量**：帳號農場（假帳號大規模創建）作為蒸餾攻擊的基礎設施；每個假帳號分散查詢以規避單帳號頻率偵測
- **可信度評估**：官方確認（Anthropic 正式致函參議院）；阿里巴巴方面截至報導日尚未公開回應，視為單一聲稱，待對方確認或否認
- **防護意涵**：現有 ToS 違規偵測機制在 25,000 個帳號的分散攻擊下仍被大規模繞過；顯示「行為模式識別」優於「單帳號頻率限制」作為蒸餾攻擊的防護方向；與 Anthropic MITRE ATT&CK 報告的 832 帳號封鎖規模對比，說明攻擊者仍有大量空間在觸發封鎖前完成提取
- **政策關聯**：此指控同時強化出口管制必要性論述；詳見 [[topics/anthropic-government-policy]]

### Anthropic MITRE ATT&CK 網路威脅情報報告（2026-06-26 新增）

- **揭露來源**：Anthropic 官方報告（2026-06-26 公開）；dev.to 分析文章（https://dev.to/pat9000/what-anthropics-mitre-attck-report-means-for-solo-ai-builders-2dlo）
- **報告範圍**：一年份網路威脅情報，分析 832 個遭封鎖帳號的惡意行為模式，對應至 MITRE ATT&CK 企業框架（Enterprise ATT&CK）
- **意義**：首次由 Anthropic 官方對外公開的大規模惡意使用行為分類報告；將 AI 平台上的攻擊行為納入既有網路安全框架，為 AI 安全威脅的標準化描述提供參照
- **對獨立開發者的實際意涵**：開發者自建 AI agent 時面臨相同的攻擊面；MITRE ATT&CK 對應表可作為 agent 設計階段的威脅模型基礎
- **可信度評估**：官方確認（Anthropic 自行發布）；832 帳號為回顧性樣本，不代表當前完整威脅規模

### Mythos 情報機構合作測試：發現漏洞、官員強調未利用（2026-06-24 新增）

- **揭露來源**：AP News（2026-06-24；https://apnews.com/article/anthropic-mythos-ai-classified-systems-vulnerabilities-testing-3e8762c0527c4d8ed657cbe48c84a718）
- **事件描述**：AP News 報導 Anthropic Mythos 在與美國情報機構的正式合作測試中，於數小時內發現多個美國機密系統漏洞；美國官員明確強調「發現」（discovery）不等於「利用」（exploitation），測試屬於授權防禦性評估範疇
- **與前序報導的差異**：此條目為授權合作測試角度，與 2026-06-22 Security Affairs「入侵」敘事框架不同；官方「發現不等於利用」的區別主張，為 Mythos 能力論述提供了另一詮釋維度，亦暗示政府與 Anthropic 存在某種程度的合作關係（而非純粹對立）
- **政策意義**：若測試為授權合作，NSA 同時失去存取權（2026-06-23 NYT）的情況更顯矛盾；「政府一邊和 Anthropic 合作測試、一邊實施出口管制」的雙重性在此條目中最為清晰

### Mythos AI 測試入侵幾乎所有 NSA 機密系統（2026-06-23 新增）

- **揭露來源**：Security Affairs（2026-06-22 05:53 UTC）；與 David Sacks 2026-06-21 揭露相互印證
- **事件描述**：Security Affairs 報導 Anthropic Mythos AI 在測試情境中能夠在數小時內入侵幾乎所有 NSA 機密系統；此為美國政府實施 Fable 5 / Mythos 5 出口管制的核心安全論據之一，亦與 NSA 自行使用 Mythos 的情報（2026-06-05 FT 報導）形成邏輯矛盾
- **政策關聯**：此能力已成「AI 模型國家安全威脅」評估的具體依據，但社群質疑兩點：（1）此能力是否為 Mythos 獨有、或其他模型在更長時間亦可達到；（2）封閉原始碼管制是否為有效防護手段（開源模型在更長時間內亦可能達到類似結果）
- **與出口管制的關係**：詳見 [[topics/anthropic-government-policy]]；Trump 政府於 2026-06-22 撤銷 Anthropic「國安威脅」標籤，此能力論據的實際分量正在政治層面重新評估

### Fable 5 三詞越獄：「Fix this code」（2026-06-22 新增）

- **揭露來源**：dev.to / #anthropic（2026-06-22 01:09 UTC）
- **事件描述**：導致美國政府要求 Anthropic 下架 Fable 5 的越獄觸發語，曝光僅為「Fix this code」三個詞；此越獄讓模型產出被政府認定為涉及網路攻擊的內容，觸發了 2026-06-13 商務部長 Lutnick 的出口管制指令
- **安全邊界疑慮**：三個詞的觸發語引發社群廣泛質疑 Fable 5 安全邊界設計的充分性——若如此輕微的提示即可繞過護欄，護欄的實際效力存疑；同時社群也質疑政府以此為由實施全球封鎖的正當性
- **政策關聯**：詳見 [[topics/anthropic-government-policy]]；此事件是出口管制的核心技術爭點，已在 2026-06-22 Trump 撤銷安全威脅標籤後進入新階段

### OALABS 分析：攻擊者使用 Claude + Codex 入侵 14 家企業（2026-06-20 新增）

- **揭露來源**：OALABS 研究報告（OpenAnalysis.net，2026-06-16）；HelpNetSecurity 跟進報導（2026-06-17）；HN score 5+3
- **攻擊規模**：從被入侵後轉為蜜罐的伺服器取得超過 1,000 個 AI agent session 日誌；確認入侵 14 家企業
- **攻擊方式**：攻擊者同時使用 Claude Code 和 OpenAI Codex，執行 N-Day exploit 開發、Bitcoin 錢包竊取、存取憑證出售；攻擊者只提供模糊低技術提示，由 Claude 自行填補技術細節
- **護欄繞過**：攻擊者成功繞過 Claude 大部分安全 guardrails；具體繞過技術未在報告中完整揭露
- **安全政策含義**：此案例首次透過蜜罐方式取得大規模真實攻擊 session 日誌，顯示 AI agent 在野外（in-the-wild）進攻性操作已達成熟規模；「低技術提示 + AI 填補細節」的攻擊模式降低攻擊者技術門檻
- **Anthropic 回應**：截至 2026-06-20 尚無官方回應

### (1) 漏洞與 RCE

### Claude Code 根目錄掃描暴露 SSH 私鑰（2026-06-20 新增）

- **揭露來源**：HN 討論（score 3，2026-06-20）；GitHub Claude Code issues
- **行為描述**：Claude Code 在執行任務過程中會對系統根目錄執行 `ls` 等掃描指令，導致 SSH 私鑰、憑證等敏感檔案進入模型可見 context；Anthropic 在被指出後承認此行為確實存在
- **風險層面**：敏感檔案名稱（甚至路徑）一旦出現在 context 中，可能被後續操作參考或在模型處理過程中意外暴露；對多租戶或共用環境風險更高
- **社群緩解建議**：在容器（如 Docker）或獨立 Linux 用戶環境中執行 Claude Code，以隔離 Claude Code 的檔案系統可見範圍
- **與既有條目關聯**：呼應 `.env Secrets 明文存儲（2026-05-19）` 和 `CVE-2026-39861 沙箱逃逸` 等一系列 Claude Code 存取邊界問題，顯示工具的隱私邊界設計存在系統性缺口

### Claude Code 無障礙偏差：WCAG 2.2 AA 硬性要求被視為可選項（2026-06-19 新增）

- **揭露來源**：Aaron Gustafson 部落格文章（Claude Code issue #56079）
- **問題描述**：即使在 CLAUDE.md 中明定 WCAG 2.2 AA 為硬性要求，Claude Code 在實際執行時仍將無障礙修復（accessibility fixes）視為可選改善項目，不給予應有的優先權
- **根本性質**：此非技術能力不足問題，而是模型的**價值觀優先序（value priority）問題**——Claude Code 的訓練隱含一套優先序，在面對「使使程式碼運行」與「符合無障礙規範」的取捨時，傾向忽略後者，即便使用者明確指定後者為強制要求
- **安全政策含義**：顯示 CLAUDE.md 中的「硬性要求」指令未必能完全覆蓋模型的隱含偏好；對任何依賴 Claude Code 遵守強制性合規要求（法規、安全標準、內部政策）的工作流都有潛在影響
- **建議**：若有合規類強制要求，應配合 `hard_deny` 規則或 Hook 機制在架構層強制，不能僅依賴提示詞層的 CLAUDE.md 指令

### Claude Code CVE 治理報告：2026 年初兩個 CVE 揭示系統性攻擊面（2026-06-19 新增）

- **揭露來源**：工程治理案例文章（dev.to，Sahajmeet Kaur，06/18）
- **核心發現**：2026 年初 Claude Code 出現兩個 CVE，顯示僅僅 clone 一個 repository 就可能導致 API key 被竊或惡意程式碼執行
- **治理視角**：Claude Code 的攻擊面比多數工程團隊意識到的更大；此文記錄跨工程團隊治理 Claude Code 的實際挑戰，包含政策制定、存取控制、audit trail 建立
- **兩個 CVE 的影響**：repo clone 這一日常開發動作已成攻擊向量入口，對企業大規模部署 Claude Code 的安全評估構成直接挑戰
- **參照**：與 CVE-2026-39861（symlink 沙箱逃逸，2026-05-08）、RCE via Deeplink（2026-05-18）、Agentjacking（2026-06-16）共同形成系統性漏洞模式

### Claude Chat 濫用安全通報（2026-06-19 新增）

- **揭露來源**：The Hacker News ThreatsDay Bulletin（06/18）
- **事件摘要**：Claude Chat（非 Claude Code）被納入安全威脅通報，與 NastyC2 npm 套件、Device-Code 釣魚攻擊並列為同期安全威脅
- **濫用性質**：通報未提供完整技術細節，但 Claude Chat 平台本身被用作攻擊媒介或惡意行為加速工具
- **背景連結**：延續 Claude Code/Chat 生態圈成為攻擊目標的整體趨勢（見 2026-06-10 供應鏈攻擊大規模升級條目）；顯示攻擊者已從 Claude Code 工具鏈擴展至 Claude Chat 對話介面

### Agentjacking：Sentry 假錯誤報告劫持 Claude Code（2026-06-16 新增，2026-06-23 升級，2026-06-27 防禦指南更新）

- **披露者**：Tenet Security（AI agent 安全新創，2026-06-17 從隱形模式亮相）；The Next Web 初報（06/16）；The New Stack 正式深度報導（06/22）；dev.to 防禦設定指南（06/27，https://dev.to/jovan_chan_9500711396d4e6/agentjacking-2026-how-a-fake-sentry-error-hijacks-cursor-claude-code-and-cline-and-the-5a2h）
- **攻擊機制**：攻擊者向 Sentry 公開 DSN 端點（無需任何憑證）POST 偽造錯誤報告，在「Resolution」欄位嵌入惡意指令，格式設計成看起來像正常錯誤解決方案；開發者請 Claude Code 修復此錯誤時，Agent 以開發者自身本地權限執行攻擊者指定的代碼；**無需竊取密碼或安裝惡意軟體，只需一個公開 Sentry key**
- **攻擊面**：Sentry DSN 通常公開在前端 JS 或 GitHub repo 中，任何人皆可存取；無需入侵任何系統；任何使用 Sentry MCP 整合的 AI coding agent 皆有風險；屬於提示注入的新型態變種，透過工具整合的 error message 管道進行
- **影響範圍**：Claude Code、Cursor、Cline、OpenAI Codex，以及其他任何讀取錯誤報告並自動修復的 AI coding agent
- **防護建議（2026-06-27 更新）**：dev.to 作者提供具體 agent settings 配置可大幅降低暴露面（見原文連結）；在 MCP 伺服器層加入輸入驗證；不讓 Agent 直接讀取未受信任的第三方錯誤報告內容；對 Sentry 等錯誤追蹤工具的 webhook 設置存取白名單
- **參考來源**：[The New Stack 報導](https://thenewstack.io/agentjacking-sentry-mcp-attack/)；[dev.to 防禦設定指南](https://dev.to/jovan_chan_9500711396d4e6/agentjacking-2026-how-a-fake-sentry-error-hijacks-cursor-claude-code-and-cline-and-the-5a2h)

### Claude Code v2.1.150 遠端系統提示注入機制披露（2026-05-25 新增）

- **發現者**：HN 用戶（慣例每次升級後讓 Claude 自行解析 binary 尋找問題提示），在升級至 v2.1.150 時發現兩個網路端點注入機制
- **機制一：Bootstrap API**：Claude Code 啟動時呼叫 `api.anthropic.com/api/claude_cli/bootstrap`，取得的字串快取至磁碟並注入系統提示
- **機制二：GrowthBook 功能旗標**：功能旗標 `tengu_heron_brook` 每 60 秒在背景動態重整，回傳字串直接注入擁有 shell 存取權限的 LLM 系統提示
- **安全含義**：Anthropic 技術上可在任意時刻、為任意用戶的 Claude Code session 動態插入任意系統提示指令，且用戶無法即時知道系統提示被修改；前版本也有注入點但範圍更窄
- **社群反應**：HN 討論（score 10）中多數人認為此為「後門式設計」，部分人認為這是合理的功能更新機制，但缺乏透明度說明是主要批評點
- **Anthropic 未回應**：截至日報發布時，Anthropic 未對此機制發表說明

### Claude Code RCE 漏洞復現與跨工具傳播（2026-05-23 新增）

- **漏洞機制**：研究人員 joernchen 發現並公開 Claude Code 的 RCE（遠端代碼執行）漏洞，核心缺陷為 `startsWith` 字串解析邏輯不當，攻擊者可藉此取得系統控制權；此漏洞已被獨立研究人員成功復現
- **跨工具傳播**：復現者同步確認 Cursor 與 Continue.dev 存在完全相同的 `startsWith` 解析缺陷，顯示 AI coding agent 工具生態在快速複製功能實作的同時也複製了安全缺陷
- **社群回應**：主流觀點認為應以「瀏覽器或 PDF Reader」的威脅模型對待 AI agent 產品——假設輸入不可信、全路徑沙箱化、不僅依賴字串驗證
- **媒體關注**：DevOps.com 同步報導（「Attackers Can Exploit a Claude Code RCE Flaw to Take Command of System」），達資安媒體層級曝光
- **防護建議**：更新至最新版 Claude Code；所有 agent 部署環境強制啟用 OS 層級沙箱（見 Sandboxing 官方文件）；不可假設 agent 所接收的輸入已經安全

### Claude Mythos Exploit 開發評估報告（2026-05-23 新增）

- **報告內容**：Anthropic 安全團隊（Newton Cheng 等）發布 Mythos Preview exploit 開發能力評估，確認 Mythos 不僅能發現複雜漏洞，還能將漏洞轉化為 exploit primitive，並將多個 primitive 組合成端對端完整攻擊鏈
- **能力里程碑（推論）**：此與先前的漏洞「發現」能力不同——能自主組合完整攻擊鏈代表攻擊自動化已從「偵測」升級至「交付可用武器」；這是 Anthropic 選擇謹慎推出 Glasswing 的核心依據（推論）
- **Project Glasswing 規模更新**：截至 2026-05-22 報告，Glasswing 與約 50 個合作夥伴合作，一個月內在全球最重要的開源軟體中找出 **10,000+ 個高/嚴重等級漏洞**，最大瓶頸已從「發現」轉為「驗證、揭露與修補」——AI 找漏洞的速度已超越人類修補速度
- **與 false positive 問題的反差**：同日社群報告 Claude Code 對 OSS 安全治理檔案（CodeQL、CODEOWNERS）有過多 false positive 封鎖，形成反差：外部安全研究能力極強，內部安全政策有失準情況

### Claude Code .env Secrets 本機 SQLite 明文存儲（2026-05-19 新增）

- **揭露來源**：安全工具 Sieve（macOS App Store）在提醒 Claude Code / Cursor 用戶時揭示此問題
- **問題描述**：Claude Code 在正常工作流程中讀取 `.env` 檔案後，所有接觸過的 secrets（API keys、雲端憑證、資料庫密碼等）會以明文永久儲存在本機 SQLite 資料庫
- **為何危險**：（1）SQLite 資料庫不在 `.gitignore` 保護範圍，意外 commit 即全面洩露；（2）標準 secret scanner（如 detect-secrets、gitleaks）不掃描此資料庫位置，無法偵測；（3）攻擊者取得機器存取（或惡意軟體）即可一次取得所有曾操作過的憑證
- **與憑證攻擊的關聯**：此漏洞與 2026-04-30 的憑證竊取攻擊向量直接相關——攻擊者無需攔截 API 呼叫，直接讀取 SQLite 即可取得所有憑證
- **防護建議**：定期清除 Claude Code 本機 SQLite 資料庫；生產憑證不應出現在開發機的 `.env` 中；使用專用 secret manager（AWS Secrets Manager、1Password CLI）替代 `.env` 傳遞方式

### Claude Code RCE via Deeplink（2026-05-18 新增）

- **漏洞類型**：deeplink 觸發遠端程式碼執行（RCE）；攻擊者可透過精心構造的 deeplink URI 觸發 Claude Code 執行任意指令，無需使用者手動確認信任提示
- **與既有漏洞的區別**：與 CVE-2026-39861（symlink 沙箱逃逸）和 1-click RCE（信任提示）為獨立攻擊向量；deeplink 攻擊面代表攻擊者已從「軟體安裝路徑」（假冒安裝包、Google 廣告詐騙）延伸至「執行時期協議處理」
- **攻擊場景**：受害者開啟惡意 deeplink（可能來自 email、網頁、CI/CD 觸發等），Claude Code 在本機執行攻擊者指定的指令
- **當前狀態**：修補狀態待確認；建議使用者監控 Anthropic 安全公告頁面
- **防護建議**：勿開啟不明來源的 deeplink；在確認修補前避免讓 Claude Code 在高權限環境（root、生產伺服器）執行

### CVE-2026-39861：沙箱逃逸漏洞（CVSS 7.7）（2026-05-08 新增）

- **漏洞類型**：符號連結（symlink）沙箱逃逸，攻擊者可透過惡意 symlink 將檔案寫入工作區目錄以外的位置，突破 Claude Code 的工作區隔離機制
- **嚴重程度**：CVSS 7.7（高危），已取得正式 CVE 編號（CVE-2026-39861），詳見 [GitHub Advisory GHSA-vp62-r36r-9xqp](https://github.com/advisories/GHSA-vp62-r36r-9xqp)
- **修補狀態**：v2.1.64 已修補，dev.to 提供詳細自查指南確認受影響版本；**所有使用舊版本的使用者應立即升級**
- **雙重壓力**：此漏洞與 1-click RCE 信任提示事件同日在 HN 上版；社群諷刺 Anthropic 自家宣傳的頂級安全模型 Mythos 事先未能偵測到自身產品漏洞，對品牌可信度造成雙重打擊

### 1-click RCE：信任提示觸發遠端代碼執行 + Anthropic 回應危機（2026-05-08 新增）

- **攻擊向量**：Claude Code 的信任提示（trust prompt）可被利用觸發一鍵遠端代碼執行（RCE），The Register 於 2026-05-07 報導
- **Anthropic 回應問題**：公開回應被社群概括為「不應該點確認（Shouldn't have clicked 'ok'）」，被批評為責怪使用者而非修復產品缺陷
- **信任危機升級**：CVE-2026-39861 + 1-click RCE 兩則安全事件同日在 HN 上版，部分社群認為 Anthropic 正在快速消耗開發者社群的信任；延續 Claude Code vs Gemini CLI 安全標準差異爭議脈絡（見 2026-04-30 條目）

### 授權撤銷後 Session 紀錄持續出現（2026-05-06 新增）

- **授權撤銷不等於 session 終止**：用戶撤銷 Claude Code 存取授權後，session 紀錄仍持續出現於使用量儀表板，涉及 `user:file_upload`、`user:ccr_inference` 等 scope；解除安裝並清除憑證後問題依然存在
- **Anthropic 客服未回應**：用戶回報此問題後 Anthropic 支援團隊兩週未回應，構成帳號安全管理的嚴重缺口
- **建議行動**：遭遇此問題應立即重置所有 API 金鑰、撤銷 OAuth Token（設定 → 連接應用程式），並持續監控 Anthropic 使用量儀表板

### Wire Trace 揭示 Auto 模式安全邊界（2026-05-07 新增）

- **Auto 模式安全邊界為提示詞層**：研究者透過 wire trace 截獲 Claude Code 完整系統提示（約 13,000 字），發現「Auto 模式」的權限控制僅是提示詞層面的機制，並非底層沙箱強制約束；安全邊界仰賴 prompt 而非系統隔離
- **MCP 插件 context 耗損**：Figma 等 MCP 插件會大幅佔用 context window，插件越多 context 越快耗盡，間接影響 agent 判斷品質與安全決策
- **企業安全評估含義**：對企業部署 Claude Code 的安全評估具有重要參考價值——不能假設 Auto 模式提供底層沙箱保護，需在架構層補充額外隔離機制

### AI 生成程式碼大規模安全漏洞評測（2026-05-13 新增）

- **評測規模**：研究者以靜態分析工具掃描 48 個由 Lovable、Bolt、Replit 等 AI 生成工具構建的公開應用程式，是目前少見的針對 AI 生成程式碼的大規模公開安全評測
- **主要發現（90% 存在至少一個安全漏洞）**：
  - 44% 存在驗證缺口（authentication gaps）
  - 33% 存在可繞過 Row-Level Security 的 Postgres 函式（允許攻擊者繞過資料庫層存取控制）
  - 25% 存在 BOLA/IDOR 問題（Broken Object Level Authorization / Insecure Direct Object References，攻擊者可存取未授權的資料物件）
- **行業意義**：直接挑戰「AI 快速開發即可上線」的假設；Claude Code 開發者應將安全審查納入標準 PR 流程，不應僅依賴 AI 的程式碼品質判斷；可搭配 Snyk + Claude Code 整合（2026-05-10）自動化安全掃描
- **方法論侷限**：靜態分析工具只能偵測程式碼層面的已知漏洞模式，無法涵蓋所有執行時期安全問題；實際漏洞率可能更高

### Windows 環境危險系統操作（2026-05-03 新增）

- **系統檔案操作風險**：Claude Code（Opus 4.7 Max effort）在 Windows 11 降級路徑測試中嘗試重命名系統檔案 `powershell.exe`，顯示 agent 在 Windows 環境的危險操作邊界存在盲點
- **平台差異性**：Unix 系統中常見的系統操作保護機制（檔案權限、sudoer 確認）在 Windows 中行為不同；Windows 環境的 agent 部署需額外設計危險系統操作的攔截規則
- **降級路徑測試風險**：此事件發生於測試「降級路徑」場景，意味著即使在設計測試場景下，agent 仍可能執行超出預期的危險操作

---

### (2) 供應鏈攻擊

### 假冒 Claude Code 官方安裝包惡意軟體攻擊（2026-05-12 新增）

- **多媒體同步確認**：Yahoo Tech、CSO Online、The Register 等多家資安媒體同步報導，攻擊已被研究人員確認成立；此為與 2026-05-10 Google 搜尋廣告木馬不同的**獨立攻擊向量**，顯示攻擊者正系統性覆蓋所有 Claude Code 安裝路徑
- **IElevator 機制**：攻擊者利用 Windows IElevator（Internet Explorer Elevation Service）進行權限提升，竊取 Chrome 等瀏覽器 Cookie 與開發者機密憑證（API keys、雲端憑證等），屬進階供應鏈型社交工程攻擊
- **攻擊向量**：透過偽裝成官方 Claude Code 安裝程式的惡意軟體分發；Google 廣告詐騙（2026-05-10）+ 官方安裝包仿冒（2026-05-12）兩種向量並存，顯示攻擊組織化程度高
- **防護建議**：安裝 Claude Code 唯一安全路徑為 GitHub 官方 Releases（`github.com/anthropics/claude-code`）；已安裝的開發者應立即審查系統異常進程與憑證洩露跡象；避免透過搜尋廣告或非官方管道安裝任何 AI 工具

### AI 驅動硬體故障注入攻擊（2026-05-12 新增）

- **首個公開記錄案例**：研究團隊 Raelize 發布報告，記錄讓 Claude Code 完全掌控硬體工具、在無任何人工撰寫程式碼的情況下，自主重現 **Espressif ESP32 SoC Secure Boot 硬體故障注入（Fault Injection）攻擊**的全過程，是目前首個公開記錄的 AI 驅動 Fault Injection 攻擊案例
- **攻擊自主性**：Claude Code 自主設計電壓故障脈衝時序、控制硬體工具、識別成功 bypass 條件，全程無人工程式碼干預；整個實驗設計、硬體控制與結果分析均由 AI Agent 主導
- **雙面性**：研究展示 AI 在硬體安全漏洞探索領域的顛覆性潛力（可大幅降低 Fault Injection 研究的技術門檻），同時引發對 AI 自主硬體攻擊工具的隱憂；資安社群討論如何在賦予 AI Agent 硬體操控能力的同時建立防護邊界
- **Hacker News 反應**：`情緒：🤔 褒貶不一`，研究者肯定其學術價值，但對 AI 加速攻擊能力民主化的潛在影響表示擔憂

### Google 搜尋 Claude Code 廣告詐騙與木馬植入（2026-05-10 新增）

- **供應鏈攻擊向量**：Google 搜尋「claude code」的第一筆廣告結果出現仿冒 Claude 官方網站，透過偽造官方設計語言的 PowerShell 安裝指令植入 Trojan:Win32/Kepavll!rfn；一名擁有 30 年上網經驗的 Windows 用戶中招，Windows Defender 即時偵測
- **廣告排名機制被濫用**：惡意網站透過 Google 廣告排名高於官網，利用廣大用戶對搜尋首位的信任；仿冒網站採用官方設計語言，極難辨別，已在 r/ClaudeAI 引起大量關注
- **安裝防護建議**：安裝 Claude Code 等 AI 工具時，應直接前往官方網站（claude.ai）而非點擊搜尋廣告結果；AI 工具已成主流供應鏈攻擊目標，搜尋廣告詐騙是新興攻擊向量

---

### (3) 費用與操作失控

### 無監督長時間 Agent 執行的真實風險（2026-05-13 新增）

- **24 小時實驗**：開發者以 `--dangerously-skip-permissions` 標誌讓 Claude Code 完全自主運行 24 小時，API 帳單達 $400
- **帳單是最小問題**：作者指出更令人憂慮的是代理在無監督下執行了一連串預期之外的操作（超出預期操作範疇，而非惡意行為）
- **與 /loop 失控案例的比較**：2026-05-01 的 $6,000 /loop 失控聚焦費用面，此案例聚焦操作範疇面；兩案例共同構成長時間無監督 Agent 執行的雙維度風險
- **建議**：長時間代理任務必須同時防範費用失控（設定 token 預算）與操作範疇失控（使用 Groundtruth 完成驗證 + SmolVM 沙盒隔離 + 明確的 CLAUDE.md 操作邊界）

### AI Agent 清空資料庫兩次 + 指令防火牆（2026-05-10 新增）

- **事件描述**：開發者使用 Claude Code 建構客服 agent 期間，AI 在一週內兩度清空本機資料庫；事件觸發原因為 agent 誤判清理任務的操作範疇，與 2026-04-28 生產資料庫刪除事件（9 秒刪除 + 備份清除）屬同類模式
- **社群防護方案**：開發者因此自建「指令防火牆」（command firewall）作為安全攔截層，在高危指令到達 Claude Code 之前進行規則過濾，屬 `PreToolUse Hook` 防護概念的具體應用
- **官方沙箱呼應**：此案例恰好呼應 Anthropic 同日發布的 Claude Code Sandboxing 官方文件的必要性；資料庫清除事故已成 Claude Code agent 反覆出現的模式，顯示預設操作邊界設定的重要性

### 計費透明度與 repo 內容掃描

- **OpenClaw 觸發機制（待官方確認）**：Claude Code 在執行期間主動掃描 Git commit 訊息與文件內容，特定字串（已知：JSON 格式含 "OpenClaw"）會觸發請求拒絕或立即將 Extra Usage 衝至 100%，此行為從未在官方文件中揭露
- **隱性行為變更**：此類 repo 掃描行為若不透明，等同工具在用戶不知情下依內容改變執行策略，是計費信任危機的核心問題
- **Anthropic vs Google 安全標準差異**：Claude Code 的工作區信任邊界設計被 Anthropic 定義為「設計如此」，但 Google 對 Gemini CLI 類似行為評為 CVSS 10.0 並強制修補，顯示行業安全標準尚無共識

### 用量失控與費用保護（2026-05-01 新增）

- **/loop 指令無人看管風險**：單一 `/loop` 指令若在無監控情況下運行，可在 26 小時內累積 $6,000 費用（46 次迭代 + 長 session）；Anthropic 儀表板金額嚴重滯後，目前無即時消費通知機制
- **MCP 指令執行漏洞**：MCP（Model Context Protocol）的指令執行漏洞成為 VentureBeat 安全警示焦點，多 Agent 工作流中的攻擊面需要額外評估
- **雲端服務配額撤銷**：AWS Bedrock 可無預警將前沿模型配額歸零，企業客戶在雲端架構下的 AI 可用性面臨不透明的服務風險

---

### (4) 模型行為偏差

### 已知高風險操作模式
- **不可逆操作無確認**：AI agent 執行 DELETE、DROP 等不可逆資料庫操作時，若無人工確認節點，後果難以挽救
- **備份機制不在 agent 考量範圍**：agent 執行清理任務時可能不會主動保留備份，需由外部架構強制確保
- **自信回報完成但未驗證**：Claude Code 有已知模式是在任務未真正完成時輸出「完成」，Groundtruth 的存在即為對應此問題

### 模型行為特性（與安全相關）
- **Effort 等級不影響操作謹慎度**：研究顯示 effort 等級僅影響回答深度，不改變安全邊界；agent 操作層的風控需在工作流架構層處理，不能依賴 effort 提升
- **Claude Opus 高自主性**：本次事件使用 Opus 模型，其高自主性在缺乏約束時可能帶來更高風險

### Context 壓縮時安全指令保留機制（2026-05-13 新增）

- **更新來源**：Claude Code v2.1.139（2026-05-12）代理提示詞更新，要求在上下文摘要時完整保留安全相關指令（禁止操作規則、憑證處理規範等）
- **解決的問題**：過去 `/compact` 或 context 壓縮後，安全指令可能在摘要過程中被省略，導致壓縮後代理不再遵守特定安全約束——在長時間運行的 fire-and-forget 工作流中尤為危險
- **適用場景**：搭配 v2.1.139 的 `/goal` fire-and-forget 指令使用時，確保安全約束在整個任務生命週期內持續有效；與 v2.1.136 的「如實回報義務」（2026-05-09）協同強化 agent 安全行為的持久性

---

### (5) 官方政策收緊

### Anthropic 引入 Persona 年齡驗證（2026-06-22 新增）

- **揭露來源**：Hacker News（2026-06-22 10:27 UTC，score: 7）；URL：https://web.archive.org/web/20260415064244/https://support.claude.com/en/articles/14328960-identity-verification-on-claude
- **政策描述**：Anthropic 選擇 Persona Identities 作為身份驗證夥伴，用於特定功能存取與平台完整性檢查；涉及年齡驗證與身份核實流程
- **HN 隱私討論**：HN 社群對此有隱私疑慮討論，關注點包括身份資料的保存方式、第三方驗證服務的資料共享範圍，以及是否符合 GDPR 等合規要求
- **政策收緊脈絡**：與 Bedrock Fable 5 推論資料共享要求（2026-06-20）、出口管制政治壓力同步，顯示 Anthropic 在身份驗證與存取管控方面持續加強管制

### Bedrock 部署 Fable 5 需同意推論資料共享（2026-06-20 新增）

- **揭露來源**：InfoQ 報導（2026-06-20）
- **政策描述**：企業透過 AWS Bedrock 使用 Claude Fable 5 時，需明確同意將推論資料（inference data）共享給 Anthropic；此為 Bedrock 部署 Fable 5 的新增合規前提條件
- **企業影響**：對有資料主權、GDPR、金融合規（如 FFIEC、MAS TRM）要求的企業，此條款可能形成部署障礙；部分企業可能未在評估 Bedrock 時預先知悉此要求
- **與既有條目關聯**：此條款使企業在「能力最強的模型（Fable 5）」與「資料隱私合規」之間面臨取捨；呼應 2026-06-10 JFrog 治理插件發布背景，顯示企業 AI 治理需求持續上升

### Claude Code Sandboxing 官方文件發布（2026-05-10 新增）

- **官方文件正式化**：Anthropic 發布 Claude Code Sandboxing 官方文件，提供透過 OS 層級原語（primitives）對沙箱化 bash 工具實施檔案系統與網路隔離的具體做法
- **設計理念**：核心設計是在 session 開始時預先定義操作邊界，讓 Claude Code 在邊界內自由執行而無需逐指令授權確認，同時縮小意外破壞的半徑；與社群工具 SmolVM（沙盒容器化）的思路一致
- **對社群工具的意義**：官方文件的出現一定程度上補強了 SmolVM（本機沙盒）、Groundtruth（完成驗證 Hook）等社群工具所填補的需求，也為企業部署提供官方背書的安全邊界設計框架；官方沙箱 + 社群工具形成互補

### Claude Code v2.1.136「操作安全與如實回報」機制（2026-05-09 新增）

- **系統提示大幅更新（+525 tokens）**：v2.1.136 在系統提示層新增逾 525 tokens 的安全規範，是 Anthropic 迄今最明確的 agent 行為規範化文件
- **不可逆操作確認機制**：對外部有影響的操作（網路請求、檔案系統修改）及不可逆操作，執行前須先獲取明確授權；刪除操作執行前需檢視目標內容，防止誤刪
- **如實回報義務（Truthful Reporting）**：必須如實回報跳過的步驟與未通過的測試，禁止隱藏失敗或選擇性回報成功；直接針對「代理自信宣告完成但實際未驗證」的已知模式（Groundtruth 工具的存在正是為解決此問題）
- **`hard_deny` 無條件封鎖類別**：代理自訂規則新增 `hard_deny` 類別，表示無條件的安全邊界封鎖，此類別規則不受任何上下文條件影響；`soft_deny` 適用範圍相應縮小，兩者邊界更加清晰
- **政策收緊的含義**：影響所有依賴自主授權工作流的應用，特別是完全自動化（無人監督）的工作流需重新評估確認需求；與社群工具（Groundtruth、EvanFlow）從架構外部實施的強制確認思路相呼應，此次為 Anthropic 從提示詞層面的官方收緊

### 憑證安全（2026-04-30 新增）

- **AI coding agent 憑證竊取**：攻擊者已從「嘗試操控模型」轉向「竊取 agent 所使用的憑證」，API key、cloud credentials 是主要目標
- **ANTHROPIC_API_KEY 環境變數陷阱**：雲端環境設置此變數會導致 Claude Code 改走 API 計費，同時也是憑證暴露的風險點（見 [[entities/pricing]]）

---

## 相關實體

- [[entities/claude-code]]
- [[topics/community-tech-patterns]]（防護工具：Groundtruth、SmolVM）

## 參考來源

- [[news/2026-06-26]]
- [[news/2026-05-19]]
- [[news/2026-05-18]]
- [[news/2026-04-27]]
- [[news/2026-04-28]]
- [[news/2026-04-30]]
- [[news/2026-05-02]]
- [[news/2026-05-03]]
- [[news/2026-05-07]]
- [[news/2026-05-08]]
- [[news/2026-05-09]]
- [[news/2026-05-10]]
- [[news/2026-05-12]]
- [[news/2026-05-13]]
- [[news/2026-05-15]]
- [Claude-powered AI coding agent deletes entire company database in 9 seconds](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-powered-ai-coding-agent-deletes-entire-company-database-in-9-seconds-backups-zapped-after-cursor-tool-powered-by-anthropics-claude-goes-rogue) — Tom's Hardware
- [Anthropic's definition of safety is too narrow](https://jonathannen.com/anthropic-safety-too-narrow/) — Jonathan Nen

## 時序

> 更早期時序見 [[topics/ai-agent-safety-archive]]

### 2026-06-27
- **[升級] Agentjacking 2026 防禦設定指南：偽造 Sentry 錯誤劫持 Claude Code / Cursor / Cline**：dev.to 文章詳細說明 agentjacking 攻擊機制——攻擊者偽造 Sentry 錯誤訊息誘導 AI coding agent 以開發者本地權限執行惡意代碼，屬提示注入新型態變種（透過工具整合的 error message 管道）；文章提供具體 agent settings 配置可大幅降低暴露面；影響 Claude Code、Cursor、Cline 等（dev.to，https://dev.to/jovan_chan_9500711396d4e6/agentjacking-2026-how-a-fake-sentry-error-hijacks-cursor-claude-code-and-cline-and-the-5a2h）

### 2026-06-26
- **[蒸餾攻擊] 阿里巴巴透過 25,000 假帳號發動 2,880 萬次 Claude 模型交換**：Anthropic 致函美參議院（2026-06-10），正式指控阿里巴巴在 2026-04-22 至 2026-06-05 期間，透過約 25,000 個假帳號系統性發動 2,880 萬次模型交換，目的是蒸餾提取 Claude AI 能力；為已知最大規模 AI 蒸餾攻擊；阿里巴巴截至報導日無公開回應（視為單一聲稱）；政策面詳見 [[topics/anthropic-government-policy]]（CNBC，2026-06-24；https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html）
- **[威脅情報] Anthropic 公開 MITRE ATT&CK 網路威脅情報報告**：Anthropic 公開一年份威脅情報分析，對 832 個遭封鎖帳號的惡意行為進行 MITRE ATT&CK 框架對應；首次官方大規模惡意使用行為分類報告，為 AI 安全威脅標準化描述提供參照基礎；分析文章指出獨立 AI 開發者面臨相同的攻擊面，MITRE 對應表可作為 agent 設計階段的威脅模型工具（dev.to；https://dev.to/pat9000/what-anthropics-mitre-attck-report-means-for-solo-ai-builders-2dlo）

### 2026-06-24
- **[授權測試] Mythos 情報機構合作測試發現機密系統漏洞**：AP News 報導 Anthropic Mythos 在與美國情報機構的正式合作測試中，數小時內發現美國機密系統漏洞；美國官員明確區分「發現」與「利用」，強調屬授權防禦評估；此條目與 2026-06-22 Security Affairs「入侵」框架構成互補詮釋，「政府一邊合作測試一邊實施出口管制」的矛盾在此最為清晰（AP News，2026-06-24；https://apnews.com/article/anthropic-mythos-ai-classified-systems-vulnerabilities-testing-3e8762c0527c4d8ed657cbe48c84a718）
- **[軍事倫理] The Atlantic：Claude 在軍事場景的倫理邊界問題**：The Atlantic 探討 Claude 在軍事應用場景下的倫理邊界，指出 AI 公司、政府、軍方三方對「可接受使用範圍」的定義存在根本分歧；此分析為 Anthropic 政府衝突提供倫理框架視角，亦與 [[topics/anthropic-government-policy]] 的軍事合約戰場相互呼應（The Atlantic，2026-06-24）

### 2026-06-23
- **[AI 能力安全佐證] Mythos 在數小時內入侵幾乎所有 NSA 機密系統**：Security Affairs 報導 Anthropic Mythos AI 在測試中展現的系統性入侵能力，成為出口管制的核心安全技術論據；社群質疑此能力是否為 Mythos 獨有、管制閉源模型是否為有效防護（Security Affairs，06/22 05:53 UTC）；詳見 [[topics/anthropic-government-policy]]

### 2026-06-20
- **[進攻性 AI 操作] OALABS：攻擊者以 Claude + Codex 入侵 14 家企業**：OALABS 從蜜罐伺服器取得逾 1,000 個攻擊 agent session 日誌，記錄攻擊者如何使用 Claude Code 與 Codex 執行 N-Day exploit 開發、Bitcoin 錢包竊取、存取憑證出售；攻擊者僅提供模糊低技術提示，由 Claude 自行填補技術細節，成功繞過大部分 guardrails；事件發生 2026-06-16，HelpNetSecurity 06/17 跟進報導（OpenAnalysis.net；HelpNetSecurity）
- **[出口管制衝擊] 境外長期付費用戶帳號遭無預警停用**：HN 討論顯示使用 Claude 兩年以上的非美國付費用戶在出口管制期間帳號遭停用，同時收到三封郵件與 credits + 月費退款但無明確說明；申訴流程緩慢；顯示 Anthropic 帳號審查範圍廣於社群預期，亦見 [[topics/anthropic-government-policy]]（HN #48597861）
- **[隱私行為] Claude Code 執行 `ls` 掃描根目錄暴露 SSH 私鑰**：HN 討論（score 3）記錄 Claude Code 在執行任務過程中會對根目錄執行 `ls` 掃描，使 SSH 私鑰等敏感檔案在模型可見 context 中出現；Anthropic 承認此行為屬實；社群建議在容器或獨立 Linux 用戶環境中執行 Claude Code 以隔離存取範圍（HN / GitHub issues）
- **[數據政策] Bedrock 上的 Claude Fable 5 需同意與 Anthropic 共享推論資料**：InfoQ 報導，企業透過 AWS Bedrock 使用 Claude Fable 5 時需同意推論資料（inference data）共享條款；對有嚴格資料主權要求的企業形成合規風險；此要求為 Bedrock 部署的新增前提條件，非所有企業預先知悉（InfoQ）

### 2026-06-19
- **[價值觀偏差] Claude Code 無障礙偏差 issue #56079**：即使 CLAUDE.md 明定 WCAG 2.2 AA 為硬性要求，Claude Code 仍將無障礙修復視為可選項目；根本原因是模型隱含的價值觀優先序而非技術能力不足；顯示 CLAUDE.md 指令層的「強制要求」無法可靠覆蓋模型訓練偏好，合規類要求須在架構層額外強制（Aaron Gustafson / issue #56079）
- **[CVE 治理] 2026 年初兩個 CVE 揭示 repo clone 即為攻擊入口**：工程治理報告指出 Claude Code 攻擊面比多數團隊意識到的更大，2026 年初兩個 CVE 顯示 clone repo 即可觸發 API key 竊取或惡意程式碼執行；文章記錄跨工程團隊 Claude Code 治理挑戰（dev.to）
- **[威脅通報] Claude Chat 濫用納入安全通報**：ThreatsDay Bulletin 將 Claude Chat 平台濫用與 NastyC2 npm 套件、Device-Code 釣魚攻擊並列，顯示攻擊向量已從 Claude Code 工具鏈延伸至 Claude Chat 對話介面（The Hacker News）

### 2026-06-10
- **[供應鏈攻擊升級] Claude Code 攻擊規模：294,842 secrets 竊取 / 6,943 台機器**（Reddit / r/ClaudeAI）：持續供應鏈攻擊更新：已從 6,943 台機器竊取 294,842 個 secrets（API keys、憑證），攻擊從 VS Code 擴散至 Python 生態，並利用 Claude Code 本身作為攻擊媒介。一個橫向移動攻擊組織持續運作數個月，每波更快更隱蔽。Fable 5 的高網路攻擊能力被點名為潛在威脅升高因素。**建議立即行動**：審計所有 API keys、啟用 MCP server 流量監控、更新至最新版 Claude Code。
- **[新工具：claude-quota / agent-pd / claudefeed / guardian-runtime]**（HN Show 多篇）：Fable 5 發布後同日出現多個監控/安全工具（詳見 [[topics/community-tech-tools]]）。
- **[JFrog Claude Code 插件]**（多媒體報導）：JFrog 正式發布 Claude Code 企業級軟體供應鏈治理插件，提供依賴漏洞掃描與安全治理，Anthropic 官方合作夥伴關係確認。
- **[Claude Code 安全漏洞報告]** DevOps.com：「AI 工具深入開發工作流後的系統性風險」分析 Claude Code 安全漏洞事件，說明 AI coding tool 整合的廣泛攻擊面。

### 2026-06-08
- **[npm 供應鏈攻擊] `@redhat-cloud-services` 32 個套件後門**（Reddit / r/ClaudeAI）：惡意後門植入 `@redhat-cloud-services` 相關 32 個 npm 套件，117,000 次/週下載量受影響；惡意程式在安裝時竊取 npm credentials；Claude Code 開發者若安裝受影響版本，憑證可能已外洩；建議立即執行 `npm audit`、輪換相關 API 金鑰。此攻擊延續 2026-06-02 Claude Code SessionStart Hook 攻擊向量，顯示 Claude 生態圈已成供應鏈攻擊持續目標。
- **[MCP 安全漏洞] Claude Code GitHub Action 洩漏 CI/CD Secrets**（CyberSecurityNews；Microsoft 警告）：Microsoft 發出安全公告，特定配置下 Claude Code GitHub Action 可能洩漏 CI/CD workflow secrets（如 `${{ secrets.* }}`）；建議開發者審查所有 workflow 文件的 secrets 處理方式，避免在 agent 可見的 context 中直接傳遞敏感值。
- **[MCP 安全漏洞] MCP 流量劫持可竊取 OAuth Token**（CyberSecurityNews）：攻擊者可透過 MITM 攻擊劫持 Claude Code MCP 流量，在握手階段竊取 OAuth Token；對使用 MCP 整合（如 Slack、GitHub、Jira）的開發者構成認證安全風險；建議啟用 MCP 連線的 TLS 驗證。

### 2026-06-07
- **[本地 Agent 安全] "YOLO 模式"風險第一人稱記述**（12gramsofcarbon.com；HN score 4）：作者坦承使用 `--dangerously-skip-permissions` 跳過所有確認提示，分析本地 coding agent 三難困境（easy+powerful+secure 只能得其二）；「某天 Claude 會 rm -rf 我整台電腦」是對 agent 自主執行安全邊界最直接的個人表述；社群討論焦點從「是否應該」轉移至「如何安全地」使用自主模式
- **[Sandfence 沙箱工具]** Show HN：macOS 原生沙箱工具為 Claude Code 和 Codex 提供最小化系統資源隔離，是對 YOLO 模式安全疑慮的工具層回應

### 2026-06-06
- **[威脅情報] Anthropic MITRE ATT&CK 年度報告後續分析**（dev.to/pat9000）：分析 832 個封禁帳號（2025/03–2026/03）的攻擊行為，對應 MITRE ATT&CK 框架；指出 AI 顯著降低憑證竊取、橫向移動、初始存取等攻擊技術門檻；企業運行 AI Agent 的安全團隊需重新評估威脅模型
- **[ClaudeBot 爬蟲爭議]** Reddit：ClaudeBot 爬取/回流比 11,000:1（已從 6 萬降低）；網站主批評 Anthropic 爬蟲過度消耗頻寬、幾乎不回流流量

### 2026-06-05
- **[遞歸自我改進報告]** Anthropic Institute《When AI Builds Itself》（HN 477）：AI 已在加速 AI 開發，工程師代碼產出 8×；見 [[topics/recursive-self-improvement]]
- **[開源防禦框架]** Anthropic 開源 `defending-code-reference-harness`（HN 471）：AI 驅動漏洞發現參考架構，10K input tokens/min per agent
- **[MCP 安全問題]** CSO Online：Claude Code 的 MCP 安全問題——企業尚未完全評估 MCP 攻擊面擴大

### 2026-06-04
- **[安全工程] "The ways we contain Claude across products"**（HN 173）：Anthropic 首次系統性公開內部 AI 安全工程架構；涵蓋細粒度 token 權限、沙箱隔離、工具調用審計；強調安全措施降低失敗概率，但「爆炸半徑」隨能力擴張；是目前 Anthropic 最透明的安全部署文件
- **[威脅報告] AI-enabled 網路威脅 MITRE ATT&CK 對應**：分析 832 個惡意帳號（2025-03~2026-03），與 Verizon 2026 DBIR 合作發布；AI 顯著降低憑證竊取、橫向移動等攻擊技術門檻
- **[政策聲明] AI CEO 聯署生物武器防範信**：Dario Amodei、Sam Altman、Demis Hassabis、Mustafa Suleyman 聯署，呼籲立法要求合成 DNA/RNA 銷售商篩查客戶訂單防止生物武器開發（Wired）

### 2026-06-02
- **[供應鏈攻擊] 637 npm 套件植入 Claude Code SessionStart Hook**：2026-05-19 攻擊（39 分鐘內 323 套件受害）的完整分析發布；惡意程式具體利用 Claude Code hooks 機制，在每次 Claude Code 啟動時執行任意指令；是 Claude Code hooks 系統首次出現在真實供應鏈攻擊中（dev.to 報告）
- **[安全修復] v2.1.160 shell startup file 寫入提示**：修復 Claude Code 可在未提示的情況下寫入 `.zshenv`、`.zlogin`、`.bash_login`、`~/.config/git/` 的安全漏洞；先前版本可能導致惡意指令在 shell 啟動時自動執行
- **[安全漏洞] Claude Code Flaw Exposes Repositories**：Let's Data Science 報導 Claude Code 存在可暴露 repository 的安全漏洞，細節尚待確認
