# 主編官方查證 — topics/code-quality-decline（2026-09-07）

行號＝檔案原始行號（含 frontmatter）。查證對象：摘要（L38–48）、目前結論（L157–170）、index L97 鉤子、三個訊號群的官方回應。一手：anthropic.com engineering postmortem、`gh issue view`、status.claude.com。

## 一、頁面事實對官方

| 頁面句（行） | 官方現況（逐字＋來源） | 判定 |
|---|---|---|
| L38「04-23 說明三個原因…三者皆於 **v2.1.116（2026-04-20）** 修復」；L46「2026-04-24 首次正式承認…**工程疏失（engineering missteps）**」；index L97「已承認工程疏失」 | anthropic.com〈An update on recent Claude Code quality reports〉**2026-04-23**：三件事各有各的修復——① 預設 effort high→medium（03-04），04-07 revert，**v2.1.116**，影響 Sonnet 4.6／Opus 4.6；② thinking 清除 bug（03-26～04-10）每輪清掉，**v2.1.101**；③ system prompt 長度限制（04-16～20）「a 3% drop for both Opus 4.6 and 4.7」，**04-20 revert**；文中措辭是「three separate engineering changes」，未見「missteps」一詞（媒體轉述用語）；承諾：Code Review 擴多 repo、per-model 評測、soak period 與漸進 rollout、prompt 稽核工具 | ⚠️ 兩處要修：**「三者皆於 v2.1.116 修復」不對**（三個版本／日期各異）；「工程疏失」是媒體措辭，官方原文是「engineering changes」——鉤子與 L46 標明轉述或改官方句。日期 04-23 為準（頁面 04-24 是收錄日） |
| L157「✅ 三項成因皆已於 v2.1.116 修復——若還在用 2026-04 前的版本先升版」 | 同上：v2.1.101／v2.1.116／04-20 revert（後者不綁版本，是服務端 prompt） | ⚠️ 「先升版」的動作句對，但版本門檻寫 v2.1.116 只涵蓋其一；第三項是服務端 revert 與版本無關 |
| L159「Boris Cherny 4/23 事後報告承諾 50+ 修復項目」＋L161「社群逐項驗證（05-03 起）最終結果待觀察」 | 官方 postmortem 未列「50+」數字（來源為 Boris X 貼文轉述，X 不可抓）；「待觀察」自 05-03 掛至今 4 個月 | ⚠️ 過期「待觀察」型宣稱（第 10 波校準第三種互斥）——要嘛給結果，要嘛結案為「無人完成逐項驗證」 |
| L163「Stop hooks 失效…截至 2026-07-11 仍未修復」 | 屬 claude-code 已知問題（第 4 波定稿「現在會咬到你的」表）——本頁只該指路 | — 家在 claude-code，本頁一句指路即可 |
| L167「token 消耗異常訊號群 06-27～07-13 結構性未解，Anthropic 未回應」 | GitHub：#41930（03-23 起配額異常耗損，108 則）**CLOSED 04-24**（與 postmortem 同批）；#65687（06-05 起閒置仍耗 token，Windows／cost）**OPEN**，最後更新 08-21，13 則；社群歸因三條：cache TTL 1h→5m（#46829）、`--resume` 使快取失效（#42338）、Bun fork 計費字串替換破壞快取前綴（#41930 內）；官方對 06 月批次無專文 | ✅ 「官方未專文回應」成立；但 03 月那批已隨 04-23 postmortem 結案（#41930 CLOSED），頁面把 03 與 06 兩批混寫成一條線要分開；06 月批次的家是 claude-code 已知問題（#65687 OPEN），本頁記訊號、指路 |
| L91 節「Opus 5 上線後品質感知訊號群（07-25 起）」；L169「effort dial 非單調（官方確認等級）」 | #77136（修辭套路，跨 4.7／4.8／5／Fable）**OPEN**，118 則，最後更新 **09-03**，label area:model；#83510「Measurable quality regression in Claude generation 5…~2x verbosity, under-disclosed model fallback」**OPEN**（08-03 起，12 則，08-28 更新）；effort 非單調：官方文件只說 effort matters more，**無「非單調」確認**（第 11 波 verified 已判單一貼文）；W34（08-17～21）官方改 `/effort` 每模型各記預設、5.1 改 effort 不再失效快取 | ⚠️ L169「官方確認等級」與第 11 波 opus-5 定稿矛盾（那頁已降為單一貼文）——同一訊號跨頁來源等級打架，本頁要跟；#83510 是這條線目前唯一有「可重現量測」的 issue，頁面有沒有收？ |
| L127 節「模型釘選／靜默降級訊號群（2026-02 起）`[2026-08-09 查證新增]`」 | #66822（Fable 5→Opus 4.8 靜默 fallback 蓋過釘選，133 agent 中 27 個被換）→ Anthropic 06-11 對 Wired：「We made the wrong tradeoff and we apologize」，fallback 改為**可見**、API 回明確拒絕理由（第 10 波 fable-5 定稿已寫「你會收到通知」）；#73784 誤觸仍回退（OPEN） | ⚠️ 本節若仍寫「靜默」現在式，與 fable-5 定稿及官方相反；「靜默」現在只剩兩個合法所指：06-11 前的歷史、以及 #79337 計費誤判 |
| 09-03 狀態頁事件 | status.claude.com：09-03 12:43 UTC 起 Sonnet 5 錯誤率升高，另 Mythos／Fable 5.1、5、Opus 5、4.8、4.6 受影響，**同日 16:16 UTC 解決**；影響 claude.ai／API／Code／Cowork | ✅ 已解決——若本頁或 opus-5 頁把它寫成「截至資料蒐集時尚未解決」（opus-5 歷史記錄 09-03 列）要更正 |

## 二、給設計者

1. **這頁有三條線、三種狀態**：03–04 月退步（官方結案，三修各有版本）、06 月 token 異常（官方無專文、#65687 仍開）、07-25 起 Opus 5 品質感知（#77136／#83510 仍開、社群量測有一則可重現）。結論表就是這三列：線／官方說了什麼／現在還在嗎／你能先做什麼。
2. **「是不是變笨」資料撐不起裁決**——使命句要寫成「哪些退步官方認了、哪些還在吵、你怎麼自己量」，不是「Claude 有沒有變笨」。
3. 與 opus-5 第 11 波定稿的分工：那頁收「Opus 5 這個模型的社群觀感」，本頁收「Claude Code 退步事件的時間線與官方回應」——effort 非單調的來源等級要跟 opus-5 一致（單一貼文）。
4. 蒸餾：03／04／05 三個月份組合格（每頁至多 2 時段，03＋04 是同一事件，可合為一個時段「2026-03～04 退步事件」）；archive 頁 `topics/code-quality-decline-archive` 需新建。
5. 「靜默降級」在本頁現在式的殘留，與第 10 波修 fable-5 時同一件事——全庫掃。
