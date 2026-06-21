# 大型企業 AI 編碼工具使用追蹤

**狀態：** ongoing
**領域：** 💼 商業
**開始日期：** 2026-05-26
**最後更新：** 2026-06-21

## 摘要

追蹤各大型企業目前正在使用的 AI 編碼工具，以及工具選擇的變化軌跡。資料來源為公開報導與內部消息洩露，僅記錄有明確來源佐證的事實。

目前追蹤 14 家企業（頂尖 7 家、大型 7 家），其中 12 家狀態為使用中（✅），1 家退出（❌，Microsoft 停用 Claude Code），1 家因出口管制被迫退出（❌，JPMorgan Chase 香港分行）。整體趨勢：Claude API 企業採用持續擴大，TCS、DXC、LG 等頂尖企業相繼全面入局；Atlassian 與 JFrog 則於 2026-06-18 同日新增採用。2026-06-21 Microsoft 確認在 Fable 5 封鎖期間加速退出 Claude Code，Codex 為主要替代方案；出口管制 + 成本壓力雙重因素持續影響頂尖企業工具選擇。

---

## 企業工具使用現況

> 狀態說明：✅ 使用中 ／ ⚠️ 縮減中 ／ 🔄 切換中 ／ ❌ 已退出 ／ ❓ 未確認
> 事件日期：狀態實際生效的時間點（❌ 為退出日、🔄 為切換日、✅ 為採用日）
> 確認日期：媒體報導或消息來源的日期

| 企業 | 規模 | AI 編碼工具 | 狀態 | 事件日期 | 備註 | 確認日期 |
|------|------|-----------|------|---------|------|---------|
| Atlassian | 大型 | Claude API | ✅ | 2026-06-18 | Claude Agent for Jira 正式推出，企業整合嵌入全球最大專案管理工具 | 2026-06-18 |
| JFrog | 大型 | Claude Code | ✅ | 2026-06-18 | Governed Claude Code Integration，提供企業級安全管控的 Claude Code 部署方案 | 2026-06-18 |
| JPMorgan Chase | 頂尖 | Claude API | ❌ | 2026-06-18 | 香港分行因美國出口管制指令被迫停止使用 Anthropic 服務（不含美國本部），是出口管制對頂尖金融機構的直接衝擊 | 2026-06-18 |
| DXC Technology | 頂尖 | Claude API | ✅ | 2026-06-12 | 多年全球聯盟；訓練數萬名 Claude 認證工程師；覆蓋銀行、航空、保險、政府等受嚴格合規監管行業 | 2026-06-12 |
| TCS（Tata Consultancy Services） | 頂尖 | Claude API | ✅ | 2026-06-11 | Global Premier Partnership；5 萬員工部署 Claude；同取得 Mythos Preview（Project Glasswing）存取 | 2026-06-11 |
| LG Group | 頂尖 | Claude API | ✅ | 2026-06-09 | LG 集團旗下全體關聯企業宣布採用 Anthropic Claude，韓國大型財閥全面入局企業 AI | 2026-06-09 |
| Rubrik | 大型 | Claude Code | ✅ | 2026-06-09 | 推出 Agent Cloud for Claude Code，將數據保護平台轉型為 AI agent；全球 GSI 同步入夥 | 2026-06-09 |
| AppFolio | 大型 | Claude API | ✅ | 2026-06-09 | Realm-X 套件接入 Claude，agent-to-agent 架構直接觸發房地產績效管理流程 | 2026-06-09 |
| ZoomInfo | 大型 | Claude API | ✅ | 2026-06-07 | 透過 GTM.AI 平台整合 Claude，建構 GTM Context Graph 企業銷售情報系統 | 2026-06-08 |
| Salesforce | 頂尖 | Claude Code | ✅ | — | 宣布 2027 年起不新增軟體工程師，直接點名 Claude Code 壓縮系統移轉成本 | 2026-06-06 |
| Microsoft | 頂尖 | Claude Code | ❌ | 2026-06-21 | Fable 5 封鎖期間宣布逐步停止讓內部工程師使用 Claude Code；自家 Codex 可能為替代方案；原預計 6/30 正式停用 | 2026-06-21 |
| Microsoft | 頂尖 | GitHub Copilot | ✅ | 2026-05-15 | 從 Claude Code 切換後採用 | 2026-05-25 |
| Amazon | 頂尖 | Claude Code | ✅ | 2026-05-05 | 雙軌並行，不押注單一供應商 | 2026-05-05 |
| Amazon | 頂尖 | OpenAI Codex | ✅ | 2026-05-05 | 與 Claude Code 同時部署 | 2026-05-05 |
| Uber | 頂尖 | Claude Code | ⚠️ | 2026-05-01 | 4 個月燒完全年 AI 預算，CTO 承認成本失控；COO 5/27 確認帶來 25% 生產力提升 | 2026-05-27 |
| Uber | 頂尖 | Cursor | ⚠️ | 2026-05-01 | 與 Claude Code 並行使用；四個月合計燒完整年 AI 預算，為成本失控具名案例之一 | 2026-06-02 |
| Fujitsu | 頂尖 | Claude API | ✅ | 2026-05-26 | 富士通與 Anthropic 簽署全球戰略合作協議，強化日本市場企業 AI 部署 | 2026-05-27 |
| Travelport | 大型 | Claude API | ✅ | 2026-05-27 | 與 Cognizant 三方合作，建構旅遊 AI 對話訂票系統 | 2026-05-27 |
| Nimble Gravity | 中型 | Claude API | ✅ | 2026-05-27 | 成立 Applied Anthropic Practice，專攻銀行、保險、金融服務業 AI 諮詢 | 2026-05-27 |
| UiPath | 大型 | Claude Code | ✅ | 2026-05-12 | RPA 平台雙工具整合 | 2026-05-12 |
| UiPath | 大型 | OpenAI Codex | ✅ | 2026-05-12 | 與 Claude Code 同時部署 | 2026-05-12 |
| Apple | 頂尖 | Claude API | ✅ | — | 外洩文件確認內部採用，非 Claude Code | 2026-05-01 |
| KPMG | 大型 | Claude API | ✅ | 2026-05-25 | 戰略合作，重新定義客戶服務 | 2026-05-25 |
| iCapital | 大型 | Claude API | ✅ | 2026-05-01 | 替代資產平台，為客戶建立 AI 工具 | 2026-05-01 |
| 哈佛 FAS | 大型 | Claude API | ✅ | 2026-04-28 | 取代 ChatGPT Edu，學術授權 | 2026-04-28 |

---

## 工具競爭態勢（企業視角）

> **說明：** Claude Code = Anthropic 的 CLI 編碼工具；Claude API = Anthropic API 整合（企業自建應用）

| 工具 | 企業採用數 | 趨勢 | 主要阻力 |
|------|----------|------|---------|
| Claude Code | 5 使用中（Amazon、Uber、UiPath、Rubrik、JFrog）+ 1 退出（Microsoft） | ⚠️ 成本壓力 + Fable 5 封鎖衝擊 | 缺乏企業層級預算管控；Fable 5 出口管制加速部分企業評估替代方案 |
| Claude API | 15（Apple、KPMG、iCapital、哈佛、Fujitsu、Travelport、Nimble Gravity、ZoomInfo、LG Group、AppFolio、Salesforce Claude API、TCS、DXC Technology、Atlassian、JPMorgan Chase 美國本部） | 🟢 快速擴張 | — |
| GitHub Copilot | 1（Microsoft） | 🟢 Microsoft 背書 | 生態鎖定 |
| OpenAI Codex | 2（Amazon、UiPath） | 🟢 快速成長 | — |
| Cursor | 1（Uber） | ⚠️ 新創份額下滑 | 成本管控困難；企業級功能不如 Claude Code |

---

## 市場分層觀察

- **頂尖企業（>10 萬員工）**：成本是最大決策因子。Microsoft 退出、Uber 警戒，Amazon 雙軌分散風險
- **大型企業（1–10 萬員工）**：分兩類——工程工具（UiPath 同時用 Claude Code + Codex）與 API 整合（KPMG、iCapital、哈佛、Travelport、Nimble Gravity 用 Claude API 自建應用）
- **新創圈**：Business Insider（2026-05-23）確認 Claude Code 已取得主導地位，Cursor 份額下滑

---

## 對 agent 開發者的選型影響

Claude Code 是工程師日常編碼工具（CLI），成本隨使用量線性成長，大量使用時易失控；Claude API 是企業自建 AI 應用的基礎，成本可透過產品設計控制。同樣是採用 Anthropic，風險結構完全不同。

---

## 時序

### 2026-06-21
- **Microsoft 宣布逐步停止內部使用 Claude Code**：時間點正值 Fable 5 封鎖期間，Microsoft 宣布將逐步停止讓內部工程師使用 Claude Code；自家 Codex 被認為是主要替代方案；此前已有 6/30 退出計畫，今日確認退出進度加快（MSN / Google News 2026-06-21）

### 2026-06-20
- **JPMorgan Chase 香港封鎖 Anthropic — 跟進報導確認**：Private Banker International 跟進報導（Google News 2026-06-19）再次確認 JPMorgan Chase 香港員工被封鎖使用 Anthropic AI 模型，原因為美國出口管制；FT 首報（2026-06-18）後跨媒體跟進，顯示此事件在金融服務業引發廣泛關注

### 2026-06-19
- **Atlassian Claude Agent for Jira 推出**：Atlassian 正式推出 Claude Agent for Jira 企業整合，將 Claude 嵌入全球最大專案管理工具（Google News 2026-06-18）
- **JFrog Governed Claude Code Integration 上線**：DevOps 平台 JFrog 推出企業級安全管控的 Claude Code 整合，可追蹤使用情況並設定治理策略（simplywall.st 2026-06-18）

### 2026-06-18
- **JPMorgan Chase 香港切斷 Anthropic 存取**：Financial Times 報導，全球最大銀行之一的香港辦公室因美國出口管制指令被迫停止使用 Anthropic 服務；是出口管制對具名頂尖金融機構的首個直接衝擊案例，顯示法規層面對企業工具使用的外部強制效應（Financial Times）

### 2026-06-12
- **DXC Technology 全球聯盟**：Anthropic 宣布與 DXC Technology 建立多年全球合作關係，DXC 將訓練「數萬名」Claude 認證前線工程師，把 Claude 導入其服務的銀行、航空公司、保險公司、製造業和政府機構；是 Anthropic 迄今最大規模的企業系統整合合作（Anthropic Blog）

### 2026-06-11
- **TCS Global Premier Partnership**：TCS（Tata Consultancy Services）與 Anthropic 宣布 Global Premier Partnership，向 5 萬名員工推廣 Claude；TCS 同時取得 Project Glasswing Mythos Preview 存取資格；是已知最大單一企業員工 Claude 部署案例（MoneyControl、TechCrunch、Reuters）

### 2026-06-09
- **LG Group 全面採用 Claude**：LG 集團旗下各關聯企業宣布採用 Anthropic Claude，為亞太市場最大單一財閥入局（thelec.net）
- **Rubrik Agent Cloud for Claude Code**：Rubrik 推出 Agent Cloud，將數據保護平台轉型為 AI agent，讓 Claude Code 可直接調用 Rubrik 的備份與恢復能力；全球系統整合商（Cognizant、Wipro、Deloitte 等）加入合作夥伴計畫（Business Wire、Yahoo Finance）
- **AppFolio + Claude A2A 整合**：房地產管理平台 AppFolio 連接 Realm-X 套件至 Claude，建立 agent-to-agent 連接讓 Claude 直接執行房地產績效管理動作（Business Insider）

### 2026-06-08
- **ZoomInfo 整合 Claude 至 GTM.AI 平台**：ZoomInfo 透過 GTM Context Graph 將 Claude 嵌入其企業銷售情報平台，作為 go-to-market AI 系統的核心推理引擎（Let's Data Science）

### 2026-06-06
- **Salesforce 宣布停招工程師**：Salesforce 宣布 2027 年起不新增軟體工程師，Claude Code 壓縮系統移轉成本為具名原因；是首家公開宣布 AI 工具取代工程師招募的頂尖科技企業

### 2026-06-04
- **Microsoft AI 主管批 Anthropic 太貴（Bloomberg）**：Kevin Scott（Microsoft AI 主管）公開表示 Anthropic 定價過高；是繼 6/30 退出決定後，Microsoft 官方對 Anthropic 定價的首次直接點名

### 2026-06-03
- **Uber 用量上限確認（Bloomberg 獨家）**：Bloomberg 報導 Uber 已正式對 Claude Code 等 AI 工具設定用量上限；是首個明確執行用量管控的大型具名企業

### 2026-06-02
- **Microsoft 退出確認（多媒體）**：Times of India、Space Daily 再次確認 Microsoft Experiences + Devices 部門 6/30 停用 Claude Code，引導數千工程師轉用 GitHub Copilot；IPO 宣布前夕成為最具代表性的企業退出案例
- **Uber 燒完整年預算**：Space Daily 確認 Uber 四個月燒完 2026 整年 AI 工具預算（Claude Code + Cursor）；與 COO 5/27 確認的 25% 生產力提升形成「效果好但成本更好」的矛盾敘事

### 2026-05-27
- **Uber COO 確認 25% 生產力提升**：Andrew Macdonald 公開表示 Claude Code + ChatGPT 帶來 25% 生產力提升，但成本問題持續（Times of India）
- **富士通與 Anthropic 簽署戰略合作**：全球範圍企業 AI 部署協議（Yahoo Finance、CX Today、Fujitsu Global）
- **Travelport + Cognizant + Anthropic**：三方合作建構旅遊 AI 對話訂票系統（PR Newswire）
- **Nimble Gravity 成立 Applied Anthropic Practice**：專攻銀行、保險、金融服務業 AI 諮詢（PR Newswire）

### 2026-05-25
- **Microsoft 宣布 6/30 完全停用 Claude Code**：Cybernews 報導，原因是數月內燒完整年 AI 預算

### 2026-05-12
- **UiPath 同時整合 Claude Code 與 Codex**：RPA 龍頭進入 AI 編碼工具市場，雙平台策略

### 2026-05-05
- **Amazon 雙品牌並行部署**：全體員工同時開放 Claude Code 與 Codex

### 2026-05-01
- **Apple 內部採用 Claude 確認**：外洩文件，企業滲透觸及科技業頂層
- **Uber 成本問題首報**：Forbes 後於 5/18 深度確認

### 2026-04-28
- **哈佛 FAS 以 Claude 取代 ChatGPT Edu**：學術機構結構性轉換

---

## 相關實體

- [[topics/competitor-landscape]]
- [[topics/enterprise-cost-management]]
- [[entities/claude-code]]

## 參考來源

- [[news/2026-05-27]]
- [[news/2026-05-25]]
- [[news/2026-05-18]]
- [[news/2026-05-15]]
- [[news/2026-05-12]]
- [[news/2026-05-05]]
- [[news/2026-05-01]]
- [[news/2026-04-28]]
