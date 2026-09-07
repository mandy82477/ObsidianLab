# 主編官方查證 — entities/fable-5（2026-09-07）

行號＝檔案原始行號（含 frontmatter）。查證對象：現況節（L40–56）、熱度表（L58–66）、配額過渡節（L69）、爭議節（L107）、index L76 鉤子。一手來源：platform 模型頁、anthropic.com 公告、support.claude.com。

## 一、頁面事實對官方

| 頁面句（行） | 官方現況（逐字＋來源） | 判定 |
|---|---|---|
| L51 表「Input $10／Output $50／1M context／128K output」 | platform `models/fable-5/overview`：**Legacy**，「Although Claude Fable 5 is still available, you should consider migrating to Claude Fable 5.1」；$10／$50、1M、128K；cache read $1／MTok；Retirement「Not sooner than June 9, 2027」；knowledge cutoff Jan 2026 | ✅ 數字對；**狀態欄缺「Legacy」與退役下限 2027-06-09**——讀者 Q2「會不會下線」的官方答案就是這一行 |
| L44「2026-09-01 發布 Fable 5.1（GA，向所有 Fable 5 用戶開放）」 | anthropic.com〈Introducing Claude Fable 5.1 and Claude Mythos 5.1〉09-01；models overview：Fable 5.1 $10／$50 同價、**cache read 2.5%（$0.25／MTok，Fable 5 為 10%＝$1）**、knowledge cutoff Jun 2026（Fable 5 為 Jan 2026）、Retirement「Not sooner than September 1, 2027」；「Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short」 | ✅；頁面沒寫 5.1 與 5 的**三個差異**（cache read 降 75%、知識截止 +5 個月、官方推薦用途）——Q2「要不要換」的答案 |
| L46「首款向大眾開放的 Mythos 級模型，與 Mythos 5 共用權重，差異在前置安全分類器」 | fable-5 overview「Fable vs. Mythos」：「Claude Mythos 5 is offered separately, by invitation only, for defensive cybersecurity workflows as part of Project Glasswing. It shares Claude Fable 5's specifications and pricing; Claude Fable 5 includes safety classifiers that can decline requests, and Claude Mythos 5 does not」 | ✅ 一致 |
| L65「不適合：從事前沿 LLM 開發（**護欄會靜默降級**）」；L107 爭議 | 〈Redeploying Claude Fable 5〉06-30：「**Users will be notified** if a request to Fable 5 is blocked, and the request will instead be sent to Opus 4.8」；support〈Why Claude switched models in your conversation with Fable 5 or Fable 5.1〉；觸發類別：cybersecurity、biology and chemistry、distillation，及「a narrow set of frontier LLM development tasks, such as distributed training infrastructure, ML accelerator design, and kernel development for certain non-standard chips」；〈Improving Fable 5 Safeguards〉：分類器「deliberately tuned to be cautious… sometimes benign requests will trigger」；Fable 5.1 公告主打「fewer false positives」（MacRumors 09-01 轉述） | ⚠️ **「靜默」與官方相反**：官方說會通知並回退到 Opus 4.8（support 有專文）。頁面該改成「觸發分類器時通知並改由 Opus 4.8 回答」，並列出四個觸發類別；5.1 宣稱誤觸減少是換代理由之一 |
| L49「出口管制 06-13 至 07-01 已解除」 | 〈Statement on the US government directive to suspend access〉06-13；〈Redeploying Claude Fable 5〉06-30：「As of June 30, the export controls on Fable 5 and Mythos 5 have been lifted. Fable 5 will be available starting July 1 to users globally on the Claude Platform, Claude.ai, Claude Code, and Claude Cowork」 | ✅ 一致；解除日精確說法是 06-30 宣布、07-01 恢復 |
| L49／L69「免費期 07-19 到期；Pro／Max 分流」；index L76「7/7 前享 50% 配額，7/7 後 usage-based billing」 | support〈Claude Fable models on your plan〉：「On the Max plan, premium seats on the Team plan, and premium seats on the seat-based Enterprise plan… you can use up to 50% of your weekly usage limits on Fable models at no extra cost」；「On Pro plans, standard seats… both models run on pay-as-you-go usage credits」；「A promotion ended on July 19, 2026 at 11:59:59 PM PT, and it applied to Fable 5 only. Claude Fable 5.1 was never part of it」 | ✅ 分流對；**index 鉤子過期**（7/7 那版是 06-30 公告的原訂，實際延到 07-19，且現在是常態分流不是促銷）；Q1 的官方答案＝Max 50% 週配額內免費、Pro 用 usage credits，5 與 5.1 同規則 |
| L42「09-04 費馬最後定理 11 天自主證明（模型版本未指名）」 | anthropic.com/research〈Formalizing Fermat's Last Theorem〉09-04：「a general-purpose internal research model roughly comparable to Claude Fable 5.1」；13M 行 Lean、30,300 定理、約 60 億 output token、數十個並行 agent、08-07 起跑 | ⚠️ **不是 Fable 5 的事件**：官方明寫內部研究模型「約略相當 5.1」。放在本頁「現況」第一段是跑錯家；歸屬 Fable 5.1 頁（若有）或 mythos／研究線，本頁至多一句指路 |
| L58 熱度表 🔥🔥🔥🔥🔥 | feature-radar 全覽表為熱度單一家（第 4 波定稿）；本頁表是跨頁同步值 | — 由設計者對 radar 現值核；features 規則檔「熱度降溫」同步條款適用 |

## 二、給設計者

1. **本頁的「現在」有四個日期並排**（09-04、09-01、06-09、07-20），而讀者三題的官方答案各只有一句：拿得到嗎（Max 50%／Pro credits）、要不要換（5.1 同價、cache 便宜 75%、知識新 5 個月、誤觸少；5 為 Legacy 至少活到 2027-06-09）、管制還影響嗎（不影響，06-30 解除）。結論表就是這三行。
2. **考題分群**（09-07 新判準）：本頁實際在答四群——模型本身（價格／方案／換代）、出口管制事件（06-13～07-01，已結案，攻防在 gov-policy 頁）、護欄與回退（觸發類別、通知、5.1 改善）、費馬事件（不屬本頁）。管制事件 200 行歷史記錄是死案歸檔候選；護欄群若要獨立成子頁看它有沒有自己的時序（06-30 分類器更新、5.1 誤觸減少）。
3. **「靜默降級」是本頁最軟卻最醒目的一句**，官方文件與 support 專文都說會通知。改寫時把四個觸發類別寫進「誰會遇到」。
4. **Fable 5.1 沒有頁**：models 規則檔負責頁面表只列 fable-5；5.1 的差異現在只能寫在本頁。設計者判：本頁改名為「Fable 5 世代」涵蓋 5／5.1（一頁答一個問題群），或另開 5.1 頁——後者是新增頁＝裁決點。
