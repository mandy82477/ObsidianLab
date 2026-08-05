---
page: "topics/enterprise-tool-tracker"
kind: "topic"
status: "ongoing"
domain: "💼 商業"
last_updated: "2026-08-05"
last_news_update: "2026-08-05"
status_main: "ongoing"
days_since_news: 0
inbound_links: 17
attribution_count: 6
attribution_last: "2026-08-05"
top_source: "google-news"
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 大型企業 AI 編碼工具使用追蹤

**狀態：** ongoing
**領域：** 💼 商業
**開始日期：** 2026-05-26
**最後更新：** 2026-08-05
**最後新聞更新：** 2026-08-05

> **最新企業採用異動**（2026-08-04）
> Fierce Biotech（source_count=2）二次報導 ICON 與 Anthropic 臨床試驗合作，與 07-29 Clinical Trials Arena 首報同一事件，屬媒體二次確認、非新增合作事實，詳見下方「企業工具使用現況」表 ICON 列備註更新。07-29 記錄之 ICON 首報、Cognizant 全球首要夥伴升級（07-28）、07-21 阿里巴巴 2.5萬假帳號封鎖說（❓ 未確認，疑似與蒸餾指控混淆）仍為近期重點。

## 摘要

**本月（2026-06）淨變化：** 3 家退出/縮減（Microsoft 成本、JPMorgan Chase 香港出口管制、Alibaba 安全疑慮）+ 1 家 API 客戶切換（Lindy → DeepSeek，成本），對 10+ 家新增/擴大採用（Globant、DataArt、Okta、Rubrik、加州州政府、Notion、Charleston Hospitality、Atlassian、JFrog、TCS、DXC、LG 等）。**淨增長態勢明確，但退出理由正從單一的「成本」擴散為「出口管制」與「安全疑慮」三軌並行**，後兩者不受 Anthropic 內部定價或效能改善控制。

追蹤各大型企業目前正在使用的 AI 編碼工具，以及工具選擇的變化軌跡。資料來源為公開報導與內部消息洩露，僅記錄有明確來源佐證的事實。

目前追蹤 33 家具名企業/機構（新增 ICON——臨床試驗/醫療研究產業首個具名採用案例；此前新增 Cognizant——升級為 Claude Partner Network 全球首要夥伴 Global Premier Partner），其中多數狀態為使用中（✅），4 家退出/切換（❌🔄，Microsoft 停用 Claude Code、JPMorgan Chase 香港分行因出口管制被迫退出、Lindy 100% 切換至 DeepSeek、Alibaba 因資安疑慮禁用 Claude Code 並明確改用內部工具 Qoder），Uber 縮減中（⚠️，成本管控）。新增 Alberta 省政府（加拿大）具名政府採用案例，20 小時掃描 4.66 億行程式碼完成資安審查，是繼加州州政府後另一個地方政府層級具體成效案例。整體趨勢：Claude API 企業與政府採用持續擴大，TCS、DXC、LG 等頂尖企業相繼全面入局；2026-06-29–06-30 單日/隔日湧現 Globant、DataArt、Okta、Rubrik、加州州政府等新一波具名案例，Partner Network 密集擴張（詳見 [[topics/anthropic-business]]）。同期 Lindy 案例顯示 API 客戶對成本敏感度高、可能因競品定價優勢流失。2026-06-21 Microsoft 確認在 Fable 5 封鎖期間加速退出 Claude Code，2026-06-22 The Jerusalem Post 跟進確認 Microsoft 正系統性降低對 Claude 依賴，GitHub Copilot 為主要替代方案。出口管制 + 成本壓力雙重因素持續影響頂尖企業工具選擇。

---

## 企業工具使用現況

> 狀態說明：✅ 使用中 ／ ⚠️ 縮減中 ／ 🔄 切換中 ／ ❌ 已退出 ／ ❓ 未確認
> 事件日期：狀態實際生效的時間點（❌ 為退出日、🔄 為切換日、✅ 為採用日）
> 確認日期：媒體報導或消息來源的日期

| 企業 | 規模 | AI 編碼工具 | 狀態 | 事件日期 | 備註 | 確認日期 |
|------|------|-----------|------|---------|------|---------|
| ICON（NASDAQ: ICLR） | 大型（全球臨床研究委外機構 CRO）| Claude API | ✅ | 2026-07-29 | Clinical Trials Arena（source_count=2）報導 ICON 與 Anthropic 合作，將 Claude AI 整合進臨床試驗流程；為醫療研究/CRO 產業首個具名採用案例，延續近期 Optum（07-14，健康服務業）之後醫療垂直產業另一深化案例（推論）；具體整合範疇、合約規模未見細節，僅標題層級資訊（Google News/Clinical Trials Arena）。**08-04 二次確認**：Fierce Biotech（source_count=2）跟進報導同一合作案，未見新增細節，屬媒體二次確認（Google News/Fierce Biotech） | 2026-08-04（首見 2026-07-29）|
| Cognizant | 頂尖 | Claude API | ✅ | 2026-07-28 | Anthropic Blog 官方公告：雙方擴大既有合作，Cognizant 將 Claude 用於自身建置並為客戶運行的系統，橫跨製造業、生命科學、保險等產業；將 Claude 嵌入自身商業與工程平台、打造「Claude 認證」（Frontier Certified）人才梯隊，並升級為 Claude Partner Network 的全球首要夥伴（Global Premier Partner）；延續近期 TCS、DXC 等頂尖 IT 服務商全面深化合作模式（推論）；具體合約規模未見細節（Anthropic Blog https://www.anthropic.com/news/cognizant-anthropic；Google News/Seeking Alpha 同日跟進） | 2026-07-28 |
| Grasshopper Bank | 中型（銀行，聚焦金融科技產業）| Claude API（MCP 整合） | ✅ | 2026-07-15 | Financial IT 報導 Grasshopper Bank 成為首家列入 Anthropic MCP（Model Context Protocol）目錄的銀行，象徵金融業對 MCP 生態系統的具名採用起點；具體整合規模、應用場景未見細節（僅標題可用，Google News 轉址）| 2026-07-15 |
| Alberta 省政府（加拿大） | 政府（省級） | Claude Code | ✅ | 2025 | 加拿大 Alberta 省技術與創新部門自 2025 年起使用 Claude Code（含 Opus、Sonnet 模型）審查系統；20 小時內掃描 4.66 億行程式碼，完成資安漏洞盤點與修補、建立新工具；Anthropic Blog 官方案例研究，為具名政府採用新增一筆（Digital Watch Observatory 跟進） | 2026-07-07 |
| Meta | 頂尖 | Claude | ❓ | — | 傳出限制工程師使用 Claude，原文節錄未提供具體來源連結、規模範圍或生效日期（2026-07-06 指控，至今無後續——近 14 天日報未見獨立媒體跟進確認或反駁）| 2026-07-06 |
| Alibaba | 頂尖 | Claude Code → Qoder（內部工具） | ❌ | 2026-07-10 | 傳出以「疑似後門風險」/ 資安疑慮為由禁止員工職場使用 Claude Code，生效日確認為 2026-07-10（The Indian Express 07-05 跟進報導提供具體生效日期）；PYMNTS、Benzinga、BeInCrypto 三獨立媒體（07-07）確認**明確改用內部工具 Qoder**，此前僅知禁令未知替代方案；來源指控未經 Anthropic 證實，多家媒體跟進（American Bazaar、Seeking Alpha、Crypto News、WTVB、TechCrunch 07-04）；首個以「安全疑慮」為由退出的具名企業案例，區別於此前的成本（Microsoft）與出口管制（JPMorgan）兩類退出理由；安全指控本身詳見 [[topics/ai-agent-safety]]；**（07-21 待查證）**tech-insider.org 另稱因偵測 2.5萬假帳號而封鎖，惟此數字與 06-25 Anthropic 蒸餾攻擊指控中的假帳號數字相同，可能為單一非主流媒體混淆兩起不同事件，暫不採信為封鎖新理由 | 2026-07-07 |
| Lindy | 中型（AI 新創） | Claude API → DeepSeek | 🔄 | 2026-06-29 | CEO Flo Crivello 公開宣告 100% 流量從 Claude 切換至 DeepSeek，每月省下數百萬美元；「最省錢 > 最強模型」趨勢最具名案例，屬 API 客戶成本敏感度案例（詳見 [[topics/enterprise-cost-management]]、[[topics/competitor-landscape]]） | 2026-06-29 |
| 加州州政府 | 政府（州級） | Claude API | ✅ | 2026-06-29 | 州長 Newsom 與 Anthropic 正式簽署協議，Claude 進入加州州政府應用；迄今最明確的美國地方政府採用案例（詳見 [[topics/anthropic-business]]） | 2026-06-29 |
| Globant（NYSE: GLOB） | 頂尖 | Claude API | ✅ | 2026-06-30 | 與 Anthropic 結盟推出 Claude 驅動的 AI Pods，重新定義企業 AI 交付模式；上市公司，覆蓋全球多行業客戶（詳見 [[topics/anthropic-business]]） | 2026-06-30 |
| DataArt | 大型 | Claude API | ✅ | 2026-06-30 | 加入 Anthropic Claude Partner Network，成為服務軌道精選（Select）合作夥伴（詳見 [[topics/anthropic-business]]） | 2026-06-30 |
| Okta | 大型 | Claude API | ✅ | 2026-06-30 | 與 Anthropic 在 XAA（跨應用 agent 認證）、MCP 協定整合及 Glasswing 安全框架展開合作，為 agentic 工作流提供身份驗證基礎建設（詳見 [[topics/anthropic-business]]） | 2026-06-30 |
| Rubrik（NYSE: RBRK） | 大型 | Claude Code | ✅ | 2026-06-30 | 發布 Claude Code 專用 AI agent 與安全層，強化企業環境安全防護；2026-06-09 已有 Agent Cloud 前例，本次為 Claude Code 專屬深化（詳見 [[topics/anthropic-business]]） | 2026-06-30 |
| Notion | 大型 | Claude Agents + Cursor | ✅ | 2026-06-25 | 正式整合 Claude Agents 與 Cursor 作為外部 agent，進入工作區協作流程；協作 SaaS 平台原生 AI agent 採用案例 | 2026-06-25 |
| Charleston Hospitality Group | 中型 | Claude API | ✅ | 2026-06-22 | 加入 Anthropic Claude 企業 AI 網路；餐旅業具名採用案例 | 2026-06-22 |
| Atlassian | 大型 | Claude API | ✅ | 2026-06-18 | Claude Agent for Jira 正式推出，企業整合嵌入全球最大專案管理工具 | 2026-06-18 |
| JFrog | 大型 | Claude Code | ✅ | 2026-06-18 | Governed Claude Code Integration，提供企業級安全管控的 Claude Code 部署方案 | 2026-06-18 |
| JPMorgan Chase | 頂尖 | Claude API | ❌ | 2026-06-18 | 香港分行因美國出口管制指令被迫停止使用 Anthropic 服務（不含美國本部），是出口管制對頂尖金融機構的直接衝擊 | 2026-06-18 |
| DXC Technology | 頂尖 | Claude API | ✅ | 2026-06-12 | 多年全球聯盟；訓練數萬名 Claude 認證工程師；覆蓋銀行、航空、保險、政府等受嚴格合規監管行業 | 2026-06-12 |
| TCS（Tata Consultancy Services） | 頂尖 | Claude API | ✅ | 2026-06-11 | Global Premier Partnership；5 萬員工部署 Claude；同取得 Mythos Preview（Project Glasswing）存取 | 2026-06-11 |
| LG Group | 頂尖 | Claude API | ✅ | 2026-06-09 | LG 集團旗下全體關聯企業宣布採用 Anthropic Claude，韓國大型財閥全面入局企業 AI | 2026-06-09 |
| Rubrik（NYSE: RBRK） | 大型 | Claude Code | ✅ | 2026-06-09 | 推出 Agent Cloud for Claude Code，將數據保護平台轉型為 AI agent；全球 GSI 同步入夥 | 2026-06-09 |
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
| Claude Code | 6 使用中（Amazon、UiPath、Rubrik、JFrog、Salesforce、Alberta 省政府）+ 1 縮減中（Uber）+ 2 退出（Microsoft、Alibaba → Qoder） | ⚠️ 成本壓力 + Fable 5 封鎖衝擊 + 安全疑慮新增退出理由；✅ 政府採用具體成效案例增加（Alberta 4.66 億行/20hr） | 缺乏企業層級預算管控；Fable 5 出口管制加速部分企業評估替代方案；Alibaba 案例顯示「疑似後門」指控也可能成為退出理由（指控未經證實），且已確認具體替代方案（Qoder） |
| Claude API | 25（Apple、KPMG、iCapital、哈佛、Fujitsu、Travelport、Nimble Gravity、ZoomInfo、LG Group、AppFolio、Salesforce Claude API、TCS、DXC Technology、Atlassian、JPMorgan Chase 美國本部、Charleston Hospitality Group、Notion、加州州政府、Globant、DataArt、Okta、Grasshopper Bank、Cognizant、ICON）+ 1 退出中（Lindy → DeepSeek） | 🟢 快速擴張（政府/合規/服務業縱深加深，新增醫療研究 CRO 產業、金融科技銀行、大型 IT 服務商全球首要夥伴）；⚠️ 部分 API 客戶因成本敏感轉向競品 | — |
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

### 2026-08

#### 2026-08-04
- **[媒體二次確認，非新增合作事實] Fierce Biotech 跟進報導 ICON 與 Anthropic 臨床試驗合作**：Fierce Biotech（source_count=2）報導與 07-29 Clinical Trials Arena 首報同一事件，未見新增合作細節，詳見上方使用現況表 ICON 列更新（Google News/Fierce Biotech）

### 2026-07

#### 2026-07-29
- **ICON 與 Anthropic 合作，將 Claude AI 整合進臨床試驗流程**：Clinical Trials Arena（source_count=2）報導，詳見上方使用現況表新增列（Google News/Clinical Trials Arena）
- **[市場反應追蹤，非新增合作事實] Cognizant（CTSH）股價於 07-28 合作公告後第二日再漲 8%**：TipRanks 報導 Cognizant 股價在與 Anthropic 的 Claude 合作宣布後第二天上漲 8%，為既有 07-28 Cognizant 全球首要夥伴升級案（見上方使用現況表 Cognizant 列）的投資人反應追蹤，僅標題可用，具體合作細節未見新增（Google News/TipRanks）

#### 2026-07-28
- **Cognizant 與 Anthropic 擴大既有合作，升級為 Global Premier Partner**：Anthropic Blog 官方公告，Cognizant 將 Claude 用於自身建置並為客戶運行的系統，橫跨製造業、生命科學、保險等產業，並將 Claude 嵌入自身商業與工程平台、打造「Claude 認證」（Frontier Certified）人才梯隊，同步升級為 Claude Partner Network 的全球首要夥伴（Global Premier Partner）；延續近期 TCS（06-11）、DXC（06-12）等頂尖 IT 服務商全面深化合作模式（推論），詳見上方使用現況表新增列與 [[topics/anthropic-business]]（Anthropic Blog https://www.anthropic.com/news/cognizant-anthropic；Google News/Seeking Alpha 同日跟進，未見新增細節）

#### 2026-07-21
- **[❓ 未確認，單一非主流媒體，疑似與蒸餾指控混淆] tech-insider.org：阿里巴巴據稱因偵測 2.5萬假帳號封鎖 Claude Code**：tech-insider.org（source_count=2）報導阿里巴巴以偵測到 2.5 萬個虛假帳號為由封鎖 Claude Code 存取。**注意**：阿里巴巴已於 07-03/07-10 因「疑似後門風險」封鎖 Claude Code 並改用 Qoder（見上方使用現況表 Alibaba 列，狀態 ❌ 已退出）；本則報導的「2.5萬假帳號」數字與 06-25 Anthropic 指控阿里巴巴蒸餾攻擊所用的假帳號數字（詳見 [[topics/competitor-landscape]]）完全相同，高度疑似報導方將「Alibaba 封鎖 Claude Code」與「Anthropic 指控 Alibaba 蒸餾攻擊」兩起不同事件的細節混淆或誤植；來源為單一非主流媒體且細節有限，暫不視為新增獨立事件或狀態變更，僅於既有 Alibaba 列備註補充待查證標記（tech-insider.org）

#### 2026-07-15
- **Grasshopper Bank 成為首家列入 Anthropic MCP 目錄的銀行**：Financial IT 報導 Grasshopper Bank 成為首家列入 Anthropic MCP（Model Context Protocol）目錄的銀行，為金融業具名採用 MCP 生態系的起點案例；具體整合規模、應用場景未見細節（僅標題可用，Google News 轉址）（Google News/Financial IT）

#### 2026-07-08
- **Alibaba 禁用 Claude Code 事件再獲媒體確認，定調升溫為中美 AI 資安爭端**：Yahoo Finance（07-08）跟進報導阿里巴巴禁用 Anthropic Claude Code 事件，將其定調為中美 AI 資安爭端升溫的一環；未提供禁令細節、生效日或替代方案的新事實，僅補充「地緣政治爭端」框架，維持既有 ❌ 已退出狀態與 07-10 生效日不變（Yahoo Finance https://finance.yahoo.com/technology/ai/articles/alibaba-bans-anthropics-claude-code-175649089.html）

#### 2026-07-07
- **阿里巴巴禁用 Claude 改用內部工具 Qoder（三媒體確認）**：PYMNTS、Benzinga、BeInCrypto 三獨立媒體確認阿里巴巴以資安疑慮禁止員工使用 Anthropic Claude，並**明確指示改用內部工具 Qoder**；此前僅知禁令與 07-10 生效日，本次補上具體替代方案細節，是繼 Microsoft（GitHub Copilot）、JPMorgan（出口管制被迫）之後，第三個「退出 Claude → 明確替代工具」的具名案例（Benzinga https://www.benzinga.com/markets/tech/26/07/60297708/alibaba-reportedly-bans-anthropics-claude-for-employees-citing-security-risks-directs-them-to-use-qoder-instead）
- **Alberta 省政府具名採用：20 小時掃描 4.66 億行程式碼**：Anthropic Blog 官方案例研究揭露，加拿大 Alberta 省技術與創新部門自 2025 年起使用 Claude Code（含 Opus、Sonnet 模型）進行系統資安審查，20 小時內完成 4.66 億行程式碼掃描，並建立漏洞盤點、修補與新工具；是繼加州州政府（Newsom 協議）後另一個具體量化成效的地方政府採用案例（Anthropic Blog https://www.anthropic.com/news/alberta-government-claude-cybersecurity；Digital Watch Observatory 跟進）

#### 2026-07-06
- **Meta 傳出限制工程師使用 Claude（未確認）**：日報補充提及 Meta 限制工程師使用 Claude，惟未提供具體來源連結、規模範圍或生效日期，暫列為 ❓ 未確認狀態，待後續獨立媒體報導確認後更新（若確認屬實，將是繼 Alibaba 安全疑慮、Microsoft 成本、JPMorgan Chase 出口管制後第四種退出/縮限驅動因素的具名頂尖科技企業案例）
- **小型企業改用 Claude 自建工作流取代 Salesforce**：The Information 報導部分小型企業改用 Claude 自建工作流取代 Salesforce，反映企業軟體採購行為變化；報導未點名具體企業或提供規模數字，暫不單獨列入使用現況表，僅記錄為採購行為觀察（The Information https://www.theinformation.com/articles/small-firms-use-claude-quit-salesforce）

#### 2026-07-05
- **Alibaba 禁令生效日確認為 7/10**：The Indian Express 跟進報導，確認阿里巴巴將於 2026-07-10 起正式禁止員工使用 Claude Code，作為美中 AI 競爭加劇下的因應措施；提供 07-03 Reuters 獨家報導以來首個具體生效日期，此前僅知禁令已宣布但無明確時間點；事件日期欄已由報導日 07-03 更新為生效日 07-10（The Indian Express https://indianexpress.com/article/technology/artificial-intelligence/alibaba-ban-claude-code-us-china-ai-10772429/）

#### 2026-07-03
- **Alibaba 傳出禁止員工職場使用 Claude Code（疑似後門風險）**：Reuters 獨家報導（HN score 313，source_count 5），Alibaba 以「疑似後門風險」為由禁止員工在職場使用 Claude Code；指控來源未經 Anthropic 證實。是繼 Microsoft（成本，06-21）、JPMorgan Chase 香港（出口管制，06-18）後第三個具名企業退出案例，也是首次以「安全疑慮」為退出理由，區別於此前的成本與法規兩類驅動因素；此事件亦與 6/24–6/29 Anthropic 指控阿里巴巴大規模蒸餾攻擊 Claude 模型的爭端同期發生，雙方關係持續緊張（詳見 [[topics/anthropic-business]] 相關時序、安全面向見 [[topics/ai-agent-safety]]）（Reuters https://www.reuters.com/world/china/alibaba-ban-claude-code-workplace-over-alleged-backdoor-risks-source-says-2026-07-03/）

### 2026-06

#### 2026-06-30
- **Partner Network 單日四項擴張：Globant AI Pods、DataArt 精選夥伴、Okta XAA 安全整合、Rubrik Claude Code 安全層**：Globant（NYSE: GLOB）與 Anthropic 結盟推出 Claude 驅動的 AI Pods 企業交付框架；DataArt 加入 Claude Partner Network 服務軌道精選夥伴；Okta 與 Anthropic 在 XAA（跨應用 agent 認證）、MCP 及 Glasswing 安全框架合作；Rubrik（NYSE: RBRK）發布 Claude Code 專用 AI agent 與安全層。四案例同日出現，顯示 Anthropic 生態系統化攻略 IT 服務、身份管理、資安三個企業採購決策環節（詳見 [[topics/anthropic-business]]）

#### 2026-06-29
- **加州州政府正式採用 Claude（Newsom 協議）**：加州州長 Gavin Newsom 與 Anthropic 簽署協議，Claude 正式進入加州州政府應用；是 Anthropic 繼聯邦機構（Mythos 5 解禁）後，美國地方政府層級最具代表性的採用案例（Politico，詳見 [[topics/anthropic-business]]）
- **Lindy 100% 流量從 Claude 切換至 DeepSeek**：AI 新創 Lindy 的 CEO Flo Crivello 公開宣告完成全量切換，每月節省數百萬美元；是「最省錢 > 最強模型」趨勢中最具名、規模最大的具名 API 客戶流失案例，代表 Anthropic 在應用層失去具名大型客戶（CNBC，詳見 [[topics/enterprise-cost-management]]、[[topics/competitor-landscape]]）

#### 2026-06-25
- **Notion 整合 Claude Agents 與 Cursor 作為外部 agent**：Notion 正式將 Claude Agents 與 Cursor 作為外部 agent 納入工作區協作流程，是協作 SaaS 平台首次將 AI coding agent 整合為原生工作流節點（letsdatascience.com https://letsdatascience.com/news/notion-integrates-claude-agents-into-workspaces-f0ad6afb）

#### 2026-06-23
- **Charleston Hospitality Group 加入 Anthropic Claude AI 網路**：SCBiz 報導（2026-06-22），南卡羅萊納州餐旅集團正式加入 Anthropic Claude 企業 AI 網路，為餐旅業首個具名採用案例，新增為中型企業追蹤對象

#### 2026-06-22
- **Microsoft 減少 Claude 依賴——國際媒體跟進確認**：The Jerusalem Post（Google News 2026-06-22）跟進報導「Microsoft reduces its reliance on Claude」，為前一日 MSN / Google News 初報的媒體後續確認；目前 Microsoft Claude Code 狀態 ❌ 已退出（事件日期 2026-06-21），GitHub Copilot 為主要替代方案

#### 2026-06-21
- **Microsoft 宣布逐步停止內部使用 Claude Code**：時間點正值 Fable 5 封鎖期間，Microsoft 宣布將逐步停止讓內部工程師使用 Claude Code；自家 Codex 被認為是主要替代方案；此前已有 6/30 退出計畫，今日確認退出進度加快（MSN / Google News 2026-06-21）

#### 2026-06-20
- **JPMorgan Chase 香港封鎖 Anthropic — 跟進報導確認**：Private Banker International 跟進報導（Google News 2026-06-19）再次確認 JPMorgan Chase 香港員工被封鎖使用 Anthropic AI 模型，原因為美國出口管制；FT 首報（2026-06-18）後跨媒體跟進，顯示此事件在金融服務業引發廣泛關注

#### 2026-06-19
- **Atlassian Claude Agent for Jira 推出**：Atlassian 正式推出 Claude Agent for Jira 企業整合，將 Claude 嵌入全球最大專案管理工具（Google News 2026-06-18）
- **JFrog Governed Claude Code Integration 上線**：DevOps 平台 JFrog 推出企業級安全管控的 Claude Code 整合，可追蹤使用情況並設定治理策略（simplywall.st 2026-06-18）

#### 2026-06-18
- **JPMorgan Chase 香港切斷 Anthropic 存取**：Financial Times 報導，全球最大銀行之一的香港辦公室因美國出口管制指令被迫停止使用 Anthropic 服務；是出口管制對具名頂尖金融機構的首個直接衝擊案例，顯示法規層面對企業工具使用的外部強制效應（Financial Times）

#### 2026-06-12
- **DXC Technology 全球聯盟**：Anthropic 宣布與 DXC Technology 建立多年全球合作關係，DXC 將訓練「數萬名」Claude 認證前線工程師，把 Claude 導入其服務的銀行、航空公司、保險公司、製造業和政府機構；是 Anthropic 迄今最大規模的企業系統整合合作（Anthropic Blog）

#### 2026-06-11
- **TCS Global Premier Partnership**：TCS（Tata Consultancy Services）與 Anthropic 宣布 Global Premier Partnership，向 5 萬名員工推廣 Claude；TCS 同時取得 Project Glasswing Mythos Preview 存取資格；是已知最大單一企業員工 Claude 部署案例（MoneyControl、TechCrunch、Reuters）

#### 2026-06-09
- **LG Group 全面採用 Claude**：LG 集團旗下各關聯企業宣布採用 Anthropic Claude，為亞太市場最大單一財閥入局（thelec.net）
- **Rubrik Agent Cloud for Claude Code**：Rubrik 推出 Agent Cloud，將數據保護平台轉型為 AI agent，讓 Claude Code 可直接調用 Rubrik 的備份與恢復能力；全球系統整合商（Cognizant、Wipro、Deloitte 等）加入合作夥伴計畫（Business Wire、Yahoo Finance）
- **AppFolio + Claude A2A 整合**：房地產管理平台 AppFolio 連接 Realm-X 套件至 Claude，建立 agent-to-agent 連接讓 Claude 直接執行房地產績效管理動作（Business Insider）

#### 2026-06-08
- **ZoomInfo 整合 Claude 至 GTM.AI 平台**：ZoomInfo 透過 GTM Context Graph 將 Claude 嵌入其企業銷售情報平台，作為 go-to-market AI 系統的核心推理引擎（Let's Data Science）

#### 2026-06-06
- **Salesforce 宣布停招工程師**：Salesforce 宣布 2027 年起不新增軟體工程師，Claude Code 壓縮系統移轉成本為具名原因；是首家公開宣布 AI 工具取代工程師招募的頂尖科技企業

#### 2026-06-04
- **Microsoft AI 主管批 Anthropic 太貴（Bloomberg）**：Kevin Scott（Microsoft AI 主管）公開表示 Anthropic 定價過高；是繼 6/30 退出決定後，Microsoft 官方對 Anthropic 定價的首次直接點名

#### 2026-06-03
- **Uber 用量上限確認（Bloomberg 獨家）**：Bloomberg 報導 Uber 已正式對 Claude Code 等 AI 工具設定用量上限；是首個明確執行用量管控的大型具名企業

#### 2026-06-02
- **Uber 燒完整年預算**：Space Daily 確認 Uber 四個月燒完 2026 整年 AI 工具預算（Claude Code + Cursor）；與 COO 5/27 確認的 25% 生產力提升形成「效果好但成本更好」的矛盾敘事（Microsoft 退出後續進度已由 06-21/06-22 條目取代，見上方）

### 2026-05

#### 2026-05-27
- **Uber COO 確認 25% 生產力提升**：Andrew Macdonald 公開表示 Claude Code + ChatGPT 帶來 25% 生產力提升，但成本問題持續（Times of India）
- **富士通與 Anthropic 簽署戰略合作**：全球範圍企業 AI 部署協議（Yahoo Finance、CX Today、Fujitsu Global）
- **Travelport + Cognizant + Anthropic**：三方合作建構旅遊 AI 對話訂票系統（PR Newswire）
- **Nimble Gravity 成立 Applied Anthropic Practice**：專攻銀行、保險、金融服務業 AI 諮詢（PR Newswire）

#### 2026-05-25
- **Microsoft 宣布 6/30 完全停用 Claude Code**：Cybernews 報導，原因是數月內燒完整年 AI 預算

#### 2026-05-12
- **UiPath 同時整合 Claude Code 與 Codex**：RPA 龍頭進入 AI 編碼工具市場，雙平台策略

#### 2026-05-05
- **Amazon 雙品牌並行部署**：全體員工同時開放 Claude Code 與 Codex

#### 2026-05-01
- **Apple 內部採用 Claude 確認**：外洩文件，企業滲透觸及科技業頂層
- **Uber 成本問題首報**：Forbes 後於 5/18 深度確認

### 2026-04

#### 2026-04-28
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
