# Claude Mythos

**類型：** model
**狀態：** active（出口管制解除，2026-07-01 起全球恢復存取）
**領域：** 🤖 模型
**首次出現：** 2026-04（限定夥伴 Preview）
**最後更新：** 2026-07-26
**最後新聞更新：** 2026-07-26

> **最新進展（待核實）**（2026-07-25）
> Mashable 標題稱「Claude Mythos，或類似模型，可能對外公開發布」（僅標題可用，無內文），若屬實將是 Mythos 級模型首次脫離「授權機構限定」而走向一般大眾發布——目前公開陣容中扮演 Mythos 級公開角色的仍是 Fable 5（無護欄完整版 Mythos 5 僅限授權機構）。此說法尚無第二來源佐證，暫列為傳聞待核實；07-21 CNBC 報導稱 Fed 曾就 Mythos 發出警示但延遲數月才浮現，具體內容與時間點同樣待查證，政策/監管面完整分析見 [[topics/anthropic-government-policy]]，本頁僅記錄模型能力認知面動態。

---

## 現況

**2026-07-25 最新（待核實）**：Mashable 標題稱「Claude Mythos，或類似模型，可能對外公開發布」（[Google News/Mashable](https://mashable.com/tech/anthropic-mythos-might-get-public-release)），僅標題與轉址連結可用，無正文摘要，無法確認具體時程、是否為完整無護欄版本、或僅是 Fable 5 之外的另一款「Mythos 級但附加護欄」新版本。若屬實將是重大政策轉向——目前 Mythos 5（無護欄完整版）僅限授權機構，一般用戶的 Mythos 級入口只有 Fable 5；此則暫無第二來源佐證，列為傳聞待核實，後續有具體內容時再擴寫。

**2026-07-21（待核實）**：CNBC 報導（經 Google News RSS 轉載，僅標題可用，無法取得完整內文）指美國聯邦準備系統（Fed）曾針對 Mythos 發出警示，但相關訊息延遲數月才浮上檯面；具體警示內容、時間點與影響範圍均待查證，暫不排除與 07-13／07-16 已知事件系出同源、由不同媒體以不同角度報導的可能性（詳見下方「時序」）。

**當前狀態（2026-07-01 起）**：出口管制已全面解除，Mythos 5 可用範圍從機構白名單擴大為全球一般用戶；解禁交換條件為 Anthropic 承諾主動偵測安全風險、配合標準協議、通報惡意活動。管制事件歷時 18 天（2026-06-13 至 2026-07-01），完整經過見下方「時序」。

Claude Mythos 是 Anthropic 的高能力 AI 模型家族，已確認具備**自主發現並武器化軟體漏洞、生成可執行 exploit** 的能力，是 AI 安全領域的重大里程碑。2026-06-09 起分為兩個版本：**Claude Fable 5**（以 Mythos 架構為核心、附加安全護欄的公開版，史上首款向大眾開放的 Mythos 級模型，見 [[entities/fable-5]]）與 **Claude Mythos 5**（無護欄完整版）。

---

## 核心能力

> 數據截至 2026-05-26（出口管制期間 Project Glasswing 統計未再公布新一輪數字，非近期缺漏）

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

> 數據截至 2026-06-02；出口管制期間（06-13 起）未見官方新一輪 Glasswing 統計公布

| 時間 | 夥伴數 | 漏洞數 |
|------|--------|--------|
| 2026-05-23（第一個月）| 約 50 個 | 10,000+（高/嚴重）|
| 2026-06-02（擴展後）| 200 個（15+ 國家）| 持續累積 |

**核心挑戰（2026-06-03 第一批夥伴反饋）：** 掃描結果包含「數百乃至數千個假陽性或次要問題」，AI 安全掃描在企業環境的**訊噪比**是核心挑戰。**驗證、揭露與修補速度**已取代「找漏洞」成為新瓶頸。

**CVD 儀表板（2026-05-24 上線）：** https://red.anthropic.com/2026/cvd/ — 首次以可追蹤格式公開披露紀錄，解決 Transparency Hub 透明度爭議。

---

## 政策與存取管控

> 完整事件時序見下方 ## 時序。

| 事件 | 日期 | 結果 |
|------|------|------|
| 白宮反對擴大存取 | 2026-04-29 | 聯邦政府首次直接干預單一 AI 模型存取 |
| OpenAI GPT-5.5 Cyber 同樣限制 | 2026-05-01 | Sam Altman 批評後旋即採同策略 |
| 印度政府部署 | 2026-05-27 | 首個主權政府採用案例 |
| UK AISI 議會閉門簡報 | 2026-05-25 | 眾議員：「能輕易入侵我的銀行帳戶」|
| ENISA 歐盟獲准存取 | 2026-06-01 | 首個歐洲政府機構；英國銀行同日遭拒 |
| ICE 加入 Glasswing | 2026-06-04 | 美國聯邦執法機構加入 |
| Mythos 5 部分解禁（100+ 機構）| 2026-06-27 | 商務部長 Lutnick 致函確認；條件：受信任合作夥伴 + 安全措施 |
| NSA 用 Mythos 發動攻擊 | 2026-06-05 | 防禦框架「兩用性」首次公開確認（FT 獨家）|
| Nozomi Networks 加入 Glasswing | 2026-07-20 | 工業資安公司加入，協助強化 OT／IoT／cyber-physical systems 安全防護（Industrial Cyber，僅標題可用，❓ 待查證）|

**授權費用**：企業客戶描述為「Budget Buster」，高安全能力伴隨高授權成本（The Information, 2026-06-01）。

---

## 爭議與批評

- **SWE-bench 方法論爭議（2026-04-27）**：The Philosophical Hacker 指出循環論證，Anthropic 截至 2026-04-28 未公開回應
- **Transparency Hub 缺席**：Mythos Preview 未納入透明度中心，社群質疑資訊公開一致性
- **CVE-2026-39861 諷刺（2026-05-08）**：以七週 2,000+ 漏洞著稱的 Mythos，未能預先偵測 Claude Code 自身的沙箱逃逸漏洞

---

## 時序

### 解禁後（2026-06-27 起）

#### 2026-07-25
**Mashable：Claude Mythos 或類似模型可能對外公開發布（僅標題可用，待核實）**：
- Google News 轉載 Mashable 標題「Anthropic's Claude Mythos, or a model like it, to get public release」（[Google News/Mashable](https://mashable.com/tech/anthropic-mythos-might-get-public-release)）；RSS 僅提供標題與轉址連結，無正文摘要，無法確認具體時程、版本形態（完整無護欄版 vs 附加護欄新版本）或與現有 Fable 5 的關係
- 若屬實將是繼 Fable 5（2026-06-09，Mythos 架構附加護欄公開版）後，Mythos 級能力進一步向大眾開放的重大政策轉向；暫無第二來源佐證，待後續報導補充具體內容再擴寫分析

#### 2026-07-21
**CNBC：Fed 曾就 Mythos AI 模型發出警示，但延遲數月才浮現（僅標題可用，待核實）**：
- Google News 轉載 CNBC 標題「The Fed rang the alarm about Anthropic's Mythos AI model — but had to go months without it」（[Google News/CNBC](https://news.google.com/rss/articles/CBMikgFBVV95cUxOejZuVHE3NHBKYnY4N0VFS0U3M3JXd3pQeEJBemUyQ21BRTF6U3Vvc2JWVXdQQkdlUDVPYnN0OUZJRnpUNVh4NkhTUTRNT3NyTlhwaTJ1YmpBcm1PSUF5MUZhNjU0SnlLZ3VwdWR4X1MzalF1UDRjcWszR0daUmVtV01ibDQ1MWxBaVFfTWhJWmVpZ9IBlwFBVV95cUxPSmNOa05qbkpGTjB1YkFBZE5rNEZaMFcteW81SlRldGFvckpHRE0tdVI3RHlEa1FSWDVFSnRNbnNLSTBjQlRJSWpJZTZOSEhwU09lb1paM051X2k3ZzcyWXNPYTRrai1tRHdFSndVbS15MUlVWXNFQWtFZGNwM0ZIUVcxTmdPNUVWY2FrS0RWajJucGpDSk9v?oc=5)）；RSS 僅提供標題與轉址連結，無正文摘要，無法取得具體警示內容、發布時間點、延遲原因或影響範圍，暫列為待核實事件
- 若屬實，顯示金融監管機構對 Mythos 風險的關注已從加拿大金融監管機關（07-13）、摩根大通執行長 Dimon 公開表態（07-16），進一步擴散至美國聯邦準備系統層級；惟因僅有標題可用，不排除與已知的 07-13／07-16 事件系出同源、經不同媒體以不同角度報導的可能性，具體警示內容與時間軸待後續報導補充確認（待核實）

#### 2026-07-20
**csoonline.com：Mythos FAQ 專文（能力／存取／競爭者／影響），僅標題可用（❓ 待查證）**：
- Google News 轉載 csoonline.com 標題「Claude Mythos FAQ: Capabilities, access, competitors, implications」（[Google News/csoonline.com](https://news.google.com/rss/articles/CBMirgFBVV95cUxOaE10YjdGU2JoM2xVRC02Q3VRQkVOX3ZBVmVMY1hXbTUxNDgwTUZ5OVBMUUdLdWNPcEtfYUZVMS0xaTRYMWFWckU2eUNuZ251VHV2aF9wcU5GNUtReHE3QUlYODdPU2ZTN3pfaDhHWG84Ti1GZV9IMC05QWNrUVNqZHg5OUY2TEExWmZuQURTMi1Tb1duVUpyTW5uVVZfa0RFRnRjQVBPRFpmekxHQlE?oc=5)）；RSS 僅提供標題與轉址連結，無正文內容可用，無法取得具體 FAQ 問答內容
- 顯示主流資安科技媒體持續以整理性 FAQ 形式報導 Mythos 現況（能力、存取方式、競爭者、影響），惟本則缺乏可驗證的新事實，暫僅記錄標題存在，待內容曝光或後續報導再補充分析

#### 2026-07-16
**摩根大通執行長 Dimon：Mythos AI 風險是「真實問題」（Reuters／Google News，僅標題可用）**：
- Reuters 報導（經 Google News RSS 轉載，僅取得標題，無法取得完整內文細節），摩根大通執行長 Jamie Dimon 公開表示 Anthropic Mythos 模型所涉及的 AI 風險是「真實的問題」（real issue）（[Google News/Reuters](https://news.google.com/rss/articles/CBMiugFBVV95cUxQQllaMFNac0hQSGkxVzh2V2VmWk9YR3Q3eXdEYW05UDMyd2hGc0F5N0d2MUZNQ2UxbVNqdl9DcUpkVzNQZzJDQkNjZ0pwNDY3MDhHVTdwVEhEU1FFZHYxVEZITllpYTJ1R190YU1zN292LVBDemhUYkNTNmZ1T0ktb3U4ek1CeFZfOF9PUWpWakNRU05uRnNFZUNLdVNESU80eDBJOEFadms0Y0VCWXI5YUhMQ05lZFBqdGc?oc=5)）
- 這是繼 07-13 加拿大金融監管機關引用 Mythos 作為銀行業網路風險佐證後，金融業界對 Mythos 級模型風險認知持續升溫的最新一例；從監管機構正式文件延伸到具名金融業高管公開表態，顯示風險認知已從單一監管案例擴散至產業領袖層級。此則與安全政策記者條目重疊（風險評論之政策/監管面），本頁僅記錄模型認知動態面向，完整政策分析見 [[topics/anthropic-government-policy]]。

#### 2026-07-13
**加拿大金融監管機關引用 Claude Mythos 警告銀行網路風險（Reuters 獨家）**：
- Reuters 獨家報導（source_count=2），加拿大金融監管機關發給銀行業的網路風險警告信中，明確引用 Claude Mythos 作為佐證，電郵內容為報導依據；為 Mythos 2026-07-01 出口管制解禁後，監管機構首次在正式監管文件中點名其能力進行風險評估（Reuters，2026-07-13）
- 顯示金融監管機構已開始將 Mythos 級模型的高階網路攻擊協助能力，正式納入銀行業風險評估框架；出口管制解禁後「使用面」（跨國企業/政府採用）敘事之外，首次出現「監管面」（風險警示）後續發展，值得持續追蹤是否有其他國家監管機構跟進；政策/外交面完整分析見 [[topics/anthropic-government-policy]]

#### 2026-06-29
**美國政府正式許可恢復 Mythos 存取（信任合作夥伴）+ 中國 Z.Ai 聲稱對標**：
- **政府許可進一步確認**：qz.com 報導 Anthropic 正式獲得美國政府許可，可向特定信任合作夥伴恢復 Mythos 存取（[qz.com](https://qz.com/anthropic-mythos-5-clearance-trusted-partners-commerce-062926)）；此為繼 6/27 商務部長 Lutnick 致函後，政府鬆綁政策的進一步落實，Fable 5 全面解禁談判同步推進中
- **中國 Z.Ai 聲稱對標 Mythos（2026-06-24 指控，至今無後續）**：Reuters 報導（[Reuters](https://www.reuters.com/legal/litigation/chinas-360-says-it-has-developed-tools-match-anthropics-mythos-2026-06-24/)，HN score 8）中國 Z.Ai 與 360 聲稱已開發出可與 Mythos 匹敵的網路安全 AI 模型；Z.Ai 為新出現的宣稱方（360 已見於 6/24 條目）；兩家公司均未提供獨立 benchmark 驗證，近 14 天日報無相關後續報導佐證

#### 2026-06-28
**TechCrunch / Mashable 後續確認 Mythos 5 部分解禁 + 競品聲稱對標（Sakana Fugu / WSJ）**：
- **TechCrunch 補充細節**（HN n/a）：補充 Lutnick 致信收件人為 Anthropic **chief compute officer Tom Brown**（非此前部分媒體所述的聯合創辦人），確認 100+ 受信任機構範圍含其**非美籍員工**，是兩週禁令後的差異化部分鬆綁（[TechCrunch](https://techcrunch.com/2026/06/26/trump-admin-releases-anthropic-mythos-to-be-used-by-more-than-100-us-companies-agencies/)）；Mashable 同步報導（[Mashable](https://mashable.com/tech/claude-mythos-5-reinstated-by-us-government)）
- **Sakana AI Fugu**：日本 Sakana AI 發布 Fugu，聲稱可與 Fable 5 / Mythos Preview 比肩，支援 multi-agent API 協調其他模型（[TechCrunch](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/)，HN score 256）；與同日中國 360 Tulongfeng 聲明合看，亞洲 AI 新創正以出口禁令空檔加速追趕 Mythos 等級能力
- **WSJ：中國已在網路安全 AI 追上 Anthropic（2026-06-28 指控，至今無後續）**：WSJ 報導指中國在網路安全 AI 能力上已逼近 Anthropic，Tulongfeng 為代表案例（[WSJ](https://www.wsj.com/tech/ai/chinese-ai-anthropic-mythos-cybersecurity-574b02c2)，Reuters HN score 7）；此說法尚未有獨立 benchmark 驗證，近 14 天日報無相關後續報導佐證

#### 2026-06-27
**Mythos 5 部分解禁：美國商務部批准 100+ 機構有限存取**：
- 美國商務部正式批准 Anthropic 向 100+ 美國機構（含企業與聯邦機構）有限釋出 Mythos 5，前提條件為「受信任合作夥伴」認定，並需具備適當安全措施。商務部長 Howard Lutnick 透過致 Anthropic 聯合創辦人 Tom Brown 的信件正式確認此決定（[Semafor](https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies)、[CNBC](https://www.cnbc.com/2026/06/26/us-government-anthropic-claude-mythos5-ai.html)）。
- 此為 2026-06-13 出口管制令發布後首次官方鬆綁，Mythos 5 的存取範圍從先前少數 Glasswing 夥伴正式擴展至更廣泛的機構層級；Fable 5 全面解禁仍待談判。

### 出口管制期（2026-06-13 至 06-26）

#### 2026-06-24
**AP News：情報機構合作測試發現機密系統漏洞 + 中國 360 聲稱對標工具**：
- **AP News 報導 — 情報機構合作測試**：Anthropic Mythos 在與美國情報機構的授權合作測試中，數小時內發現美國機密系統漏洞；美國官員特別強調「發現」（find）不等於「利用」（exploit），試圖區隔能力確認與惡意使用（[AP News](https://apnews.com/article/anthropic-mythos-ai-classified-systems-vulnerabilities-testing-3e8762c0527c4d8ed657cbe48c84a718)）。此報導與 2026-06-23 Tom's Hardware 引述的 NSA 紅隊測試訊息相互印證，但強調這屬授權合作而非入侵事件
- **中國 360 聲稱對標工具**：Reuters 報導，中國網路安全公司 360 聲稱已開發出對標 Anthropic Mythos 的工具（[Reuters](https://www.reuters.com/legal/litigation/chinas-360-says-it-has-developed-tools-match-anthropics-mythos-2026-06-24/)）；此為繼 Zhipu GLM-5.2 聲明後，第二家中國公司公開宣稱追平 Mythos 的案例，中美 AI 網路安全能力競爭態勢進一步升溫

#### 2026-06-23
**Tom's Hardware：Mythos 紅隊測試數小時內突破 NSA 幾乎所有機密系統 + MIT Technology Review 三點分析**：
- **Tom's Hardware 報導**：Sen. Mark Warner（參議院情報委員會副主席）引述 NSA 局長 Gen. Joshua Rudd 的陳述，確認 Mythos 在紅隊測試中「數小時內突破 NSA 幾乎所有機密系統」。這是迄今最高層級、最具體的政府官員公開陳述，直接解釋出口管制的安全理由，也與 Tom's Hardware 同名報導互相呼應（[Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-powerful-mythos-ai-reportedly-breached-almost-all-nsa-classified-systems-within-a-few-hours-during-red-team-test-report-sheds-more-light-on-the-u-s-governments-sudden-ban-on-the-flagship-models)）
- **MIT Technology Review 三大觀察點**（[MIT Tech Review](https://www.technologyreview.com/2026/06/22/1139424/three-things-to-watch-amid-anthropics-latest-feud-with-the-government/)，2026-06-22）：
  1. **AI 安全定義爭議**：「安全」的定義在 Anthropic（對用戶無害）與政府（對國家安全無害）之間存在根本分歧，是出口管制衝突的深層矛盾
  2. **主權問題**：各國政府越來越關注對本國 AI 基礎設施的主權控制權
  3. **中國競爭窗口**：出口管制期間，Zhipu GLM-5.2 等中國模型加速填補被封鎖市場，管制可能適得其反地擴大中國 AI 的影響力

#### 2026-06-20
**全球媒體持續報導 + 境外付費帳號停用**：
- **國際媒體全面跟進**：Al Jazeera、DW.com、SiliconANGLE、dev.to 同步報導 Fable 5 / Mythos 出口禁令，核心敘事從「美國技術管制」擴大至「盟友間地緣政治緊張」與「AI Kill-Switch」爭議
- **境外付費用戶帳號停用**：確認有非美國 Claude 付費訂閱用戶在管制期間帳號遭停用，Mythos 可及性衝擊擴大至一般訂閱層
- **解禁預期**：承接 Ciauri 2026-06-18 首爾記者會「數日內恢復」聲明，後續見 [[entities/fable-5]]

#### 2026-06-19
**Wired 深度調查確認多重管制動機 + 解禁聲明 + 早期用戶豁免**：
- **SK Telecom 中國關聯確認為根本動機**（Wired HN score 110）：Anthropic 先前授予 SK Telecom 對 Mythos（非 Fable 5）的存取權，美方對 SK Telecom 中國關聯的疑慮是出口管制啟動的真正起點；後 Amazon 研究人員向白宮舉報 Fable 5 越獄漏洞，兩件事疊加加速管制動作，澄清「jailbreak 是唯一原因」的既有說法
- **Ciauri 首爾記者會**：Anthropic 國際總監宣稱「數日內恢復可用」
- **Bloomberg**：部分 Mythos 早期用戶在政府指令後仍保有存取權（早期用戶豁免）
- **Amazon 研究員角色確認**：Amazon 安全研究人員發現 Fable 5 越獄漏洞後直接向白宮通報，是出口管制的直接觸發原因之一（見 2026-06-14 事件記錄）

#### 2026-06-18
**SK Telecom / China 關聯被揭露為出口管制根本起因**：Wired 獨家報導，美國政府對 Anthropic 啟動 Fable 5 / Mythos 出口管制的真正起點，是政府對 SK Telecom 疑似中國關聯的憂慮——Anthropic 先前已授予 SK Telecom 對 Mythos（非 Fable 5）的存取權，此舉令美方官員警惕；後來 Fable 5 的 jailbreak 問題（Amazon 通報白宮）進一步加速了管制動作。此揭露澄清了「jailbreak 是唯一原因」的既有說法，顯示管制動機具有多重層次（Wired）。

### 管制前

#### 2026-06-10
Claude Fable 5 發布後社群爭議持續：Anthropic 被揭露在偵測到使用者從事前沿 LLM 開發時（訓練 pipeline、推論研究、ML 加速器設計），Fable 5 會靜默降級回應品質，不告知用戶。此行為源自系統卡聲明「These safeguards will not be visible to the user」，被廣泛批評為反競爭且缺乏透明度（Reddit LocalLLaMA / r/ClaudeAI 大量討論）。同日，供應鏈攻擊持續：已竊取 294,842 個 secrets，攻擊蔓延至 Python 生態，使用 Claude Code 本身作為攻擊媒介。Anthropic 首席執行長 Dario Amodei 對「Claude 是否用於伊朗學校打擊」表示不知情（Bloomberg）。Microsoft AI CEO Mustafa Suleyman 批評 Anthropic 對 Claude 意識的推測「非常危險」。

#### 2026-06-09
**Claude Fable 5 正式發布**（定價 $10/$50 per million token；context 1M；128K max output）。與 Claude Mythos 5 共用相同模型權重，差異在前置安全分類器——觸發時靜默 fallback 至 Opus 4.8（不到 5% session 受影響）。同日發布的 Claude Mythos 5 為無護欄完整版，僅限授權用戶（政府防禦者、企業安全研究員）存取，定價更高。HN 討論達 2,448 分、近 2,000 評論。Anthropic 同步發布系統卡（含 ASL-4 安全評估框架）。30 天資料保留政策（Fable 5 / Mythos 5 所有流量強制保留 30 天供安全審查，Bedrock 用戶資料離開 AWS 邊界）生效，引發 Bedrock 用戶隱私爭議。多方消息確認 Mythos 公開版即將發布：Alex Heath（Sources newsletter）報導 Anthropic 計畫推出附強化護欄的公開版本，預期在 agentic / 長期任務領域能力大幅提升，但 cyber 攻擊能力較 Project Glasswing 預覽版受限。Reddit 社群同步爆料版本名稱可能為「Claude Fable 5」（未經官方確認）。此外，Anthropic 研究「Measuring LLMs' impact on N-day exploits」揭示 LLM 已顯著降低 N-day 漏洞利用門檻。

#### 2026-06-08
Dragos（工業網路安全公司）將 Mythos Preview 應用於 OT（營運技術）安全軟體漏洞挖掘，為 Mythos 在企業安全場景的落地新案例。Pentagon 因 Claude「太安全」而尋求替代 AI 方案的報導再次被廣泛引述，Tech Times 報導五角大廈積極評估替代品。

#### 2026-06-05
NSA 使用 Mythos 發動進攻性網路攻擊（FT 獨家，HN 89）。Anthropic 同日開源 `defending-code-reference-harness` 作為防禦工具，呈現「同源攻防」格局。另：Anthropic AI 發現 Zcash Orchard pool 無限偽造漏洞（2022 年起即存在），ZEC 價格暴跌 30%。

#### 2026-06-04
ICE（美國移民海關執法局）加入 Project Glasswing，繼 ENISA 之後的第二個政府機構。

#### 2026-06-03
Project Glasswing 第一批夥伴在 HN（score 176）分享一手使用體驗：假陽性嚴重，訊噪比是核心挑戰。Anthropic 總裁 Daniela Amodei 首度公開表示 Mythos「非常擅長網路戰」，在 $965B IPO 申請背景下引發商業化壓力討論。

#### 2026-06-02
Glasswing 夥伴從 50 擴展至 150 個新組織（共 200 個，15+ 國家）。Anthropic 承諾 6–12 個月內推出公開版本。

#### 2026-06-01
ENISA（歐盟網路安全局）獲准存取，成首個歐洲政府機構。英國銀行同日遭拒，OpenAI 主動提出替代方案——AI 安全能力開始成為地緣政治談判籌碼。The Information 報導授權費被稱「Budget Buster」。

#### 2026-05-30
Anthropic red team 發布《Measuring LLMs' ability to develop exploits》，公開確認 Mythos Preview 漏洞開發能力是「step-change」，超越所有現有前沿模型。

#### 2026-05-29
Reuters 確認：Anthropic to roll out Claude Mythos in coming weeks（數週內面向公眾推出）。

#### 2026-05-27
印度政府宣布在網路安全計畫中部署 Mythos，首個主權政府採用案例。

#### 2026-05-26
10K–23K 漏洞數字媒體密集報導（Help Net Security / eWeek / PYMNTS / Techzine，數字分歧來自篩選門檻不同）。The Register / Gotrade / CyberSecurityNews 三家媒體同日確認公開釋出路線。

#### 2026-05-25
Anthropic 安全團隊發布 Exploit 評估完整論文（https://red.anthropic.com/2026/exploit-evals/）。Politico 引述美國議會閉門簡報：眾議員 Lou Correa 表示 Mythos 能輕易入侵其銀行帳戶；UK AISI 測試企業網路接管成功率 6/10。The Register 報導 Anthropic 準備釋出 Mythos 等級模型。

#### 2026-05-24
CVD 儀表板正式上線（281 個專案 / 1,596 筆記錄）。Claude Code app 字串洩露：「Access to the Claude Mythos model in Claude Code and Claude Security」，Anthropic 聲明初期仍限制存取。

#### 2026-05-23
Project Glasswing 第一個月報告：約 50 個夥伴、10,000+ 高危漏洞。安全團隊同步發布 Mythos exploit 開發能力評估報告，確認可組合完整攻擊鏈。

#### 2026-05-08
Claude Code CVE-2026-39861（CVSS 7.7）沙箱逃逸漏洞曝光，社群廣泛討論 Mythos 的諷刺性。見 [[topics/ai-agent-safety]]。

#### 2026-05-01
TechCrunch：Sam Altman 批評 Mythos 限制後，旋即宣布 OpenAI GPT-5.5 Cyber 採同策略，僅開放給關鍵防禦者。

#### 2026-04-29 / 04-30
Bloomberg / WSJ 報導白宮正式反對擴大 Mythos 存取，聯邦政府首次直接干預。Steve Blank 發文：「我們已打開潘朵拉的盒子」（HN 廣泛討論）。

#### 2026-04-27 / 04-28
The Philosophical Hacker 指出 SWE-bench 方法論循環論證，HN 再次精選持續擴散。IEEE Spectrum 報導：需程式碼隔離、執行沙盒、權限最小化才能安全部署。

#### 2026-04-25
七週測試發現 2,000+ 未知軟體漏洞，大量涉及加密貨幣基礎設施（Fox News / CoinDesk / Crypto Briefing 同步報導）。

#### 2026-04-24
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
- [Mashable：Claude Mythos, or a model like it, to get public release](https://mashable.com/tech/anthropic-mythos-might-get-public-release)（2026-07-25，僅標題可用，待核實）
- [[news/2026-07-26]]
