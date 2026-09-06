# 主編官方查證 — topics/anthropic-government-policy（2026-09-06）

行號為檔案原始行號（含 frontmatter）。記者與 agent 無 web 工具，本檔對照「頁面 vs 一手現況」。

## 一、三筆懸置可結案或更正

| 頁面位置 | 頁面現況 | 一手現況 | 處置 |
|---|---|---|---|
| L96／L488「香港金融機構 Claude 存取限制（成因未明）」 | Yahoo Finance 08-20，成因未明 | **Anthropic 不允許香港與中國大陸存取**（區域政策）。Goldman：稍早查出其 Anthropic 合約不涵蓋香港而自行切斷。OKX：8 月初企業帳號被 Anthropic 短暫停權，OKX 稱部分員工在港使用「可能未完全符合區域存取政策」，帳號已恢復、香港員工請求改導向其他模型（[Bloomberg 08-19](https://www.bloomberg.com/news/articles/2026-08-19/crypto-firm-okx-bars-claude-use-in-hong-kong-after-suspension)、cryptobriefing、FinanceFeeds） | ✅ 結案：成因＝Anthropic 區域存取政策，非政府動作；對讀者的意義是**香港客戶不在許可區**，這是產品層事實該進「目前局勢」首列 |
| L34／L65／L250／L451 Sanders 法案「數年徒刑、僅標題可用」（NDTV 09-05） | 只有標題 | **09-03** Sanders（參）＋ Greg Casar（眾）提出 **Ban Artificial Superintelligence Act**：永久禁止超智慧 AI、凍結先進 AI 開發直到新設內閣級監管機構訂出安全規範，違者**最高 20 年**徒刑；法案點名 OpenAI、Meta、Anthropic 未履行早前承諾；與 OpenAI 宣布 GPT-6 Astra 同日（Decrypt、IBTimes、TechTimes 09-04） | 更正：日期 09-03、刑期「最高 20 年」、法案名與共同提案人；狀態＝提案，未進委員會（本輪未查） |
| L68／L107／L178／L258 五角大廈黑名單裁定違法（08-27／28） | 已記：Rita F. Lin 裁定違法、即時解除；09-04 FedScoop 部門態度不一 | 一致。補：判決理由「unlawful retaliation」違反第一修正案、「arbitrary and capricious」（CNN 08-27、NPR 08-28）；**第二案（D.C. 巡迴上訴法院，針對國防部另一條規則）仍待判**（TechCrunch 08-28） | ✅ 一致；補「第二案待判」為下一個政策事件（Q4 的答案之一） |

## 二、Q2「對產品有沒有實際影響」的錨

- 冷讀者 A 已指出：真正影響產品的是頁面表格第 72 列「高風險 cybersecurity／coding 請求自動 fallback 至 Opus 4.8，上線首日誤判合法安全審查」——本輪未另查官方；健檢卡應把它列為 Q2 主答案並交下一輪查證。
- 出口管制：06-12 商務部對 Mythos 5／Fable 5 實施、06-30 解除（頁面寫 07-01 全面解除，一天之差可能是時區或生效日，記者可核）。
- 05-01 五角大廈八家機密 AI 合約排除 Anthropic——頁面攻防紀錄應有，健檢卡核對。

## 三、給設計者

1. 「目前局勢（截至 2026-09-05）」是 34 列 mixed 表且無機制，節名帶日期——這是本頁的「事故表」，該照 pricing／ai-agent-safety 的結論表形狀重做：一變數一列、狀態、對讀者的影響、下一個時點。
2. 香港那筆從「成因未明」變成「區域政策」後，是全頁唯一直接打到讀者（產品可用性）的事實，應上首列。
3. 人物頁六個（chris-olah／tom-brown／chris-ciauri／dario-amodei／tino-cuellar／bernanke）供料零、停滯兩三個月——節點三問要認真答；冷讀者 A 說人物頁對六題幫助接近零。

## 四、Defense in Depth fallback 官方原文（Q2 的錨，UTC 05:4x）

[Anthropic「Redeploying Claude Fable 5」2026-06-30](https://www.anthropic.com/news/redeploying-fable-5)：安全分類器判定為潛在有害的 cybersecurity 請求「the request will instead be sent to Opus 4.8」；「Users will be notified if a request to Fable 5 is blocked」；Amazon 報告所述特定技術「blocked in over 99% of cases」；官方明認代價「flagging benign requests more often during routine coding and debugging tasks」。**適用範圍只寫 Fable 5，未提 Fable 5.1**（09-01 發布）——頁面若寫成「現行」要標「Fable 5；5.1 是否沿用未見官方說明」。此即冷讀者兩輪都指的「唯一會改到你用的 Claude 的政府相關後果」，家應在本頁「會改到你用的 Claude」一節，並雙向指 [[entities/fable-5]]。
