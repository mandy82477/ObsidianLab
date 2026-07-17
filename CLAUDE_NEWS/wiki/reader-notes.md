# 讀者筆記收件匣

使用者透過「**記一下：…**」丟進的待處理想法（需求訊號、版面點子、待修內容等）。這是**待辦收件匣**，不是歷史記錄——處理完就標 ✅。

**格式：** `- [狀態] YYYY-MM-DD｜[類別]｜內容`（最新在上）
**狀態：** ⏳ 待處理 / ✅ 已納入 / 📌 留存（雜記專用，非待辦、不追蹤）
**類別：** 🎨 版面建議 ／ 🔍 興趣主題 ／ 📝 內容修正 ／ 🐞 缺陷流程 ／ 📓 雜記（日記/方向筆記，用 📌）

**消費（避免變死檔）：**
- `/wiki-weekly-review`（每週）掃描 ⏳ 項目：🔍 興趣主題 → 餵入「值得加碼追蹤」的**需求面證據**；🎨 版面建議、📝 內容修正 → 列給使用者或轉對應流程；處理完標 ✅。
- `/wiki-weekly-review` 同時讀 📌 📓 雜記作為「近期方向背景」（不需動作），並**清除距今 > 30 天的雜記**（日記性質，過期即除）。
- `/wiki-ingest`（每日，經 pipeline）順手提醒放置 **> 14 天**仍 ⏳ 的項目，避免積壓（📌 雜記不在提醒範圍）。
- 🐞 缺陷流程若當場修掉 → 走 `wiki/log.md` 的 Query 記錄（已完成的動作）；此處只放「待處理」的。

---

- [⏳] 2026-07-17｜🔍 興趣主題｜使用者關心 **Claude vs 開源競品（GLM / Qwen）的能力差距**——觸發自 07-17 商業諮詢對話（評估友人 20 萬台幣地端 AI server 套 Qwen 的商業模式）。**07-17 手動查證發現**：GLM-5.2（753B 總參數／40B active）FrontierSWE **74.4** vs Opus 4.8 **75.1**（僅差 0.7）、Terminal-Bench 2.1 81.0、SWE-bench Pro 62.1，為 Artificial Analysis Intelligence Index v4.1 **開源榜首**；Qwen3.5（397B）強在多模態／多語言／尺寸家族（edge→397B 全覆蓋），coding 讓給 GLM——**兩家旗艦互有勝負，非單向領先**。此結果**證實** [[topics/competitor-landscape]] 現存「GLM 5.2 據評測可比 Opus 4.8 high（Reddit 轉述 DataBricks，**待查證**）」該列方向正確。**與 07-12 GPT-5.6 條為同一結構缺口第二次撞牆**：評測型內容（HF 官方 model blog、Artificial Analysis、DeepLearning.AI The Batch）不在 pipeline 覆蓋 venue；惟本次來源**權威度高於 07-12 的對照型部落格**（含 zai-org 官方 blog + The Batch），07-12「不採信部落格數字、等官方」的決策前提，在開源競品這條線上**可能已滿足**。→ **待 weekly-review 判斷三題**：(a) 兩次撞牆是否已構成擴充 venue 的需求證據（或僅為臨時查詢，搜尋即可解）；(b) 若不擴充收錄，是否改採「**指路而非囤積**」——[[topics/model-comparison]] 加外部榜單連結區塊（benchmark 屬靜態參考資料、易凍結，收進 wiki 會觸發 `wiki-ingest-format.md`「指標表凍結」警示；連結零維護且永不過期）；(c) competitor-landscape 該列「待查證」已有外部佐證但**無日報進料**，是否需要 web-verified 來源標註機制以與日報來源區隔

- [⏳] 2026-07-12｜🔍 興趣主題｜使用者關心 **GPT-5.6 vs Claude 的比較討論**——目前 wiki 只有戰略/定位層（[[topics/competitor-landscape]] 的 ChatGPT Work/GPT-5.6 條，訴求價格·速度·生產力超越 Anthropic），缺工程師第一手實測跑分與 token 定價對照。**07-12 手動查證發現**：第一手跑分其實已大量發表（GPT-5.6 代號「Sol」+Terra/Ultra 分層；TerminalBench 2.1 Sol 88.8% vs Opus 4.8 78.9% vs Fable 5 84.3%；SWE-Bench Pro Fable 80.3% 反超 GPT 58.6%；Sol API 便宜 50%；OpenAI system card 承認 Sol「over-agency」），但都在對照型部落格（MindStudio/DataCamp/codersera/superframeworks 等），**不在 pipeline 覆蓋 venue**（Google News「Anthropic Claude」query 偏新聞媒體、抓不到評測部落格）。**使用者決策（07-12）：等官方數據再回填、不採信部落格數字；pipeline 先不擴充來源，觀察一週**。→ weekly-review（約 07-19 起）回看：官方 benchmark 或 HN/Reddit 是否延燒出可信第一手數字；venue 覆蓋缺口是否值得補精選 benchmark 來源。詳見 log.md 07-12 Query 條。**07-16 週度回顧查證**：模型／商業／社群三記者分頭查 07-09~07-13 日報，仍無官方 benchmark 或可信第一手數字（僅 ZDNET/Reuters 定性報導、Reddit 臆測；pi-coding-agent 成本數字屬別的產品）——維持 ⏳，下次回顧（07-19 後）再查

- [✅] 2026-07-09｜🔍 興趣主題｜使用者關心 Anthropic **股票/IPO 投資管道**——目前無公開市場管道，次級市場「幾乎無人願賣」（qz.com/Business Insider，估值傳 1.2 兆美元）；weekly-review 留意後續 IPO 時程、次級市場流動性變化、可否加開追蹤子區塊於 [[topics/anthropic-business]]（✅ 2026-07-12 週度回顧已於 [[topics/anthropic-business]] 加開「IPO 前瞻與估值追蹤」子區塊）

- [✅] 2026-07-07｜🔍 興趣主題｜想深入追蹤「**隱藏追蹤器**」技術線：v2.1.91 中國代理偵測程式碼 →「embedded spyware」指控 → 07-07 Anthropic 定調「實驗」；weekly-review 評估是否值得從 [[topics/ai-agent-safety]] 抽出獨立追蹤/深化（含混淆手法、與「hidden workspace」是否同一機制、出口管制關聯）（✅ 2026-07-12 週度回顧已拆出獨立頁 [[topics/safety-china-trust-dispute]]，整合技術指控＋外交/企業線五階段敘事）

- [📌] 2026-07-07｜📓 雜記｜**今天改動方向**：從「修單一產出值」轉向「修上游源頭＋防再犯」——日報程度詞須錨定原文（Elevated≠大規模）、callout 改覆寫不留前次、query-log 記錄缺陷驅動改動、reader-notes 收件匣捕捉需求；核心哲學：宣告≠執行（機制放 memory 才觸發）、每次提問當防再犯訊號。
