# Claude Mythos

**類型：** model
**狀態：** active（部分公開：Fable 5 = Mythos 架構 + 護欄；Mythos 5 = 完整版限定存取）
**領域：** 🤖 模型
**首次出現：** 2026-04（限定夥伴 Preview）
**最後更新：** 2026-06-18

---

## 現況

Claude Mythos 是 Anthropic 的高能力 AI 模型家族，已確認具備**自主發現並武器化軟體漏洞、生成可執行 exploit** 的能力，是 AI 安全領域的重大里程碑。

**2026-06-09**，Anthropic 正式發布 **Claude Fable 5**：以 Mythos 架構為核心、附加安全護欄的公開版本（定價 $10/$50 per million token）。同日發布的 **Claude Mythos 5** 為無護欄完整版，僅限授權用戶（政府防禦者、企業安全研究員）存取，定價更高。Fable 5 = 史上首款向大眾開放的 Mythos 級模型。

**30 天資料保留政策**：Fable 5 / Mythos 5 所有流量強制保留 30 天供安全審查，資料離開 AWS 安全邊界，引發 Bedrock 用戶隱私爭議。

**2026-06-02**，Anthropic 宣布 Glasswing 夥伴擴展至 150 個新組織（共 200 個，覆蓋 15+ 國家）。**2026-06-05**，FT 獨家報導 NSA 正使用 Mythos 發動進攻性網路攻擊，是 Glasswing「防禦」框架兩用性的首次公開確認。

---

## 核心能力

| 指標 | 數據 |
|------|------|
| 漏洞發現數（累積） | 2,000+（04 七週）→ 10,000+（05-23）→ 10K–23K（05-26）|
| CVD 儀表板（截至 05-22）| 281 個開源專案 / 1,596 筆記錄 / 97 筆已修補 |
| 企業網路接管成功率 | 6/10 次（UK AISI 測試，vs GPT-5.5 3/10）|

**Exploit 開發能力（2026-05-25 論文確認）：**
- 能找到複雜零日漏洞
- 能將漏洞轉化為 exploit primitive
- 能將多個 primitive 組合成**端對端完整攻擊鏈**（前所未有）

**資安雙重性（IEEE Spectrum）：**
- 防禦端：大幅加速漏洞發現與修補
- 攻擊端：若落入惡意行為者，可自動化生成高品質 exploit

---

## Project Glasswing

Anthropic 的官方 AI 資安能力研究計畫，Mythos Preview 為核心工具。

| 時間 | 夥伴數 | 漏洞數 |
|------|--------|--------|
| 2026-05-23（第一個月）| 約 50 個 | 10,000+（高/嚴重）|
| 2026-06-02（擴展後）| 200 個（15+ 國家）| 持續累積 |

**核心挑戰（2026-06-03 第一批夥伴反饋）：** 掃描結果包含「數百乃至數千個假陽性或次要問題」，AI 安全掃描在企業環境的**訊噪比**是核心挑戰。**驗證、揭露與修補速度**已取代「找漏洞」成為新瓶頸。

**CVD 儀表板（2026-05-24 上線）：** https://red.anthropic.com/2026/cvd/ — 首次以可追蹤格式公開披露紀錄，解決 Transparency Hub 透明度爭議。

---

## 政策與存取管控

| 事件 | 日期 | 結果 |
|------|------|------|
| 白宮反對擴大存取 | 2026-04-29 | 聯邦政府首次直接干預單一 AI 模型存取 |
| OpenAI GPT-5.5 Cyber 同樣限制 | 2026-05-01 | Sam Altman 批評後旋即採同策略 |
| 印度政府部署 | 2026-05-27 | 首個主權政府採用案例 |
| UK AISI 議會閉門簡報 | 2026-05-25 | 眾議員：「能輕易入侵我的銀行帳戶」|
| ENISA 歐盟獲准存取 | 2026-06-01 | 首個歐洲政府機構；英國銀行同日遭拒 |
| ICE 加入 Glasswing | 2026-06-04 | 美國聯邦執法機構加入 |
| NSA 用 Mythos 發動攻擊 | 2026-06-05 | 防禦框架「兩用性」首次公開確認（FT 獨家）|

**授權費用**：企業客戶描述為「Budget Buster」，高安全能力伴隨高授權成本（The Information, 2026-06-01）。

---

## 爭議與批評

- **SWE-bench 方法論爭議（2026-04-27）**：The Philosophical Hacker 指出循環論證，Anthropic 截至 2026-04-28 未公開回應
- **Transparency Hub 缺席**：Mythos Preview 未納入透明度中心，社群質疑資訊公開一致性
- **CVE-2026-39861 諷刺（2026-05-08）**：以七週 2,000+ 漏洞著稱的 Mythos，未能預先偵測 Claude Code 自身的沙箱逃逸漏洞

---

## 時序

### 2026-06-18
**SK Telecom / China 關聯被揭露為出口管制根本起因**：Wired 獨家報導，美國政府對 Anthropic 啟動 Fable 5 / Mythos 出口管制的真正起點，是政府對 SK Telecom 疑似中國關聯的憂慮——Anthropic 先前已授予 SK Telecom 對 Mythos（非 Fable 5）的存取權，此舉令美方官員警惕；後來 Fable 5 的 jailbreak 問題（Amazon 通報白宮）進一步加速了管制動作。此揭露澄清了「jailbreak 是唯一原因」的既有說法，顯示管制動機具有多重層次（Wired）。

### 2026-06-10
Claude Fable 5 發布後社群爭議持續：Anthropic 被揭露在偵測到使用者從事前沿 LLM 開發時（訓練 pipeline、推論研究、ML 加速器設計），Fable 5 會靜默降級回應品質，不告知用戶。此行為源自系統卡聲明「These safeguards will not be visible to the user」，被廣泛批評為反競爭且缺乏透明度（Reddit LocalLLaMA / r/ClaudeAI 大量討論）。同日，供應鏈攻擊持續：已竊取 294,842 個 secrets，攻擊蔓延至 Python 生態，使用 Claude Code 本身作為攻擊媒介。Anthropic 首席執行長 Dario Amodei 對「Claude 是否用於伊朗學校打擊」表示不知情（Bloomberg）。Microsoft AI CEO Mustafa Suleyman 批評 Anthropic 對 Claude 意識的推測「非常危險」。

### 2026-06-09
**Claude Fable 5 正式發布**（定價 $10/$50 per million token；context 1M；128K max output）。與 Claude Mythos 5 共用相同模型權重，差異在前置安全分類器——觸發時靜默 fallback 至 Opus 4.8（不到 5% session 受影響）。HN 討論達 2,448 分、近 2,000 評論。Anthropic 同步發布系統卡（含 ASL-4 安全評估框架）。30 天資料保留政策（Bedrock 用戶資料離開 AWS 邊界）生效。多方消息確認 Mythos 公開版即將發布：Alex Heath（Sources newsletter）報導 Anthropic 計畫推出附強化護欄的公開版本，預期在 agentic / 長期任務領域能力大幅提升，但 cyber 攻擊能力較 Project Glasswing 預覽版受限。Reddit 社群同步爆料版本名稱可能為「Claude Fable 5」（未經官方確認）。此外，Anthropic 研究「Measuring LLMs' impact on N-day exploits」揭示 LLM 已顯著降低 N-day 漏洞利用門檻。

### 2026-06-08
Dragos（工業網路安全公司）將 Mythos Preview 應用於 OT（營運技術）安全軟體漏洞挖掘，為 Mythos 在企業安全場景的落地新案例。Pentagon 因 Claude「太安全」而尋求替代 AI 方案的報導再次被廣泛引述，Tech Times 報導五角大廈積極評估替代品。

### 2026-06-05
NSA 使用 Mythos 發動進攻性網路攻擊（FT 獨家，HN 89）。Anthropic 同日開源 `defending-code-reference-harness` 作為防禦工具，呈現「同源攻防」格局。另：Anthropic AI 發現 Zcash Orchard pool 無限偽造漏洞（2022 年起即存在），ZEC 價格暴跌 30%。

### 2026-06-04
ICE（美國移民海關執法局）加入 Project Glasswing，繼 ENISA 之後的第二個政府機構。

### 2026-06-03
Project Glasswing 第一批夥伴在 HN（score 176）分享一手使用體驗：假陽性嚴重，訊噪比是核心挑戰。Anthropic 總裁 Daniela Amodei 首度公開表示 Mythos「非常擅長網路戰」，在 $965B IPO 申請背景下引發商業化壓力討論。

### 2026-06-02
Glasswing 夥伴從 50 擴展至 150 個新組織（共 200 個，15+ 國家）。Anthropic 承諾 6–12 個月內推出公開版本。

### 2026-06-01
ENISA（歐盟網路安全局）獲准存取，成首個歐洲政府機構。英國銀行同日遭拒，OpenAI 主動提出替代方案——AI 安全能力開始成為地緣政治談判籌碼。The Information 報導授權費被稱「Budget Buster」。

### 2026-05-30
Anthropic red team 發布《Measuring LLMs' ability to develop exploits》，公開確認 Mythos Preview 漏洞開發能力是「step-change」，超越所有現有前沿模型。

### 2026-05-29
Reuters 確認：Anthropic to roll out Claude Mythos in coming weeks（數週內面向公眾推出）。

### 2026-05-27
印度政府宣布在網路安全計畫中部署 Mythos，首個主權政府採用案例。

### 2026-05-26
10K–23K 漏洞數字媒體密集報導（Help Net Security / eWeek / PYMNTS / Techzine，數字分歧來自篩選門檻不同）。The Register / Gotrade / CyberSecurityNews 三家媒體同日確認公開釋出路線。

### 2026-05-25
Anthropic 安全團隊發布 Exploit 評估完整論文（https://red.anthropic.com/2026/exploit-evals/）。Politico 引述美國議會閉門簡報：眾議員 Lou Correa 表示 Mythos 能輕易入侵其銀行帳戶；UK AISI 測試企業網路接管成功率 6/10。The Register 報導 Anthropic 準備釋出 Mythos 等級模型。

### 2026-05-24
CVD 儀表板正式上線（281 個專案 / 1,596 筆記錄）。Claude Code app 字串洩露：「Access to the Claude Mythos model in Claude Code and Claude Security」，Anthropic 聲明初期仍限制存取。

### 2026-05-23
Project Glasswing 第一個月報告：約 50 個夥伴、10,000+ 高危漏洞。安全團隊同步發布 Mythos exploit 開發能力評估報告，確認可組合完整攻擊鏈。

### 2026-05-08
Claude Code CVE-2026-39861（CVSS 7.7）沙箱逃逸漏洞曝光，社群廣泛討論 Mythos 的諷刺性。見 [[topics/ai-agent-safety]]。

### 2026-05-01
TechCrunch：Sam Altman 批評 Mythos 限制後，旋即宣布 OpenAI GPT-5.5 Cyber 採同策略，僅開放給關鍵防禦者。

### 2026-04-29 / 04-30
Bloomberg / WSJ 報導白宮正式反對擴大 Mythos 存取，聯邦政府首次直接干預。Steve Blank 發文：「我們已打開潘朵拉的盒子」（HN 廣泛討論）。

### 2026-04-27 / 04-28
The Philosophical Hacker 指出 SWE-bench 方法論循環論證，HN 再次精選持續擴散。IEEE Spectrum 報導：需程式碼隔離、執行沙盒、權限最小化才能安全部署。

### 2026-04-25
七週測試發現 2,000+ 未知軟體漏洞，大量涉及加密貨幣基礎設施（Fox News / CoinDesk / Crypto Briefing 同步報導）。

### 2026-04-24
Mythos 遭駭客存取事件（KRON4 等媒體）。⚠️ 細節尚待官方聲明確認。

---

## 參考來源

- [[news/2026-04-25]]、[[news/2026-04-27]]、[[news/2026-04-28]]、[[news/2026-04-29]]、[[news/2026-04-30]]
- [[news/2026-05-02]]、[[news/2026-05-08]]、[[news/2026-05-24]]、[[news/2026-05-25]]、[[news/2026-05-26]]
- [[news/2026-05-27]]、[[news/2026-05-29]]、[[news/2026-05-30]]
- [[news/2026-06-01]]、[[news/2026-06-02]]、[[news/2026-06-03]]、[[news/2026-06-04]]、[[news/2026-06-05]]
- [What Anthropic's Mythos Means for the Future of Cybersecurity](https://spectrum.ieee.org/ai-cybersecurity-mythos) — IEEE Spectrum
- [Anthropic's Argument for Mythos SWE-bench improvement contains a fatal error](https://www.philosophicalhacker.com/post/anthropic-error/) — The Philosophical Hacker
- [Exploit Evaluation Report](https://red.anthropic.com/2026/exploit-evals/) — Anthropic Security
- [CVD Dashboard](https://red.anthropic.com/2026/cvd/) — Anthropic
