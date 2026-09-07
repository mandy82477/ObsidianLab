---
page: "entities/fable-5"
kind: "entity"
type: "model"
status: "active（現行世代為 Fable 5.1；Fable 5 為 Legacy，官方載明退役不早於 2027-06-09）"
domain: "🤖 模型"
last_updated: "2026-09-07"
last_news_update: "2026-09-04"
status_main: "active"
days_since_news: 3
parent: null
children: "['entities/fable-5-archive']"
page_role: "hub"
days_since_news_subtree: 3
inbound_links: 42
attribution_count: 32
attribution_last: "2026-09-04"
top_source: "google-news"
pending_count: 5
pending_overdue: 0
pending_next_review: "2026-09-09"
pending_signalled: 1
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Fable 5 與 5.1

**類型：** model
**狀態：** active（現行世代為 Fable 5.1；Fable 5 為 Legacy，官方載明退役不早於 2027-06-09）
**領域：** 🤖 模型
**別名：** Fable 5, Fable 5.1, Claude Fable 5.1
**首次出現：** 2026-06-09
**最後更新：** 2026-09-07
**最後新聞更新：** 2026-09-04

> **最新進展**（2026-09-01）
> Fable 5.1 GA 發布並取代 5.0 成為現行旗艦：同價、快取讀取便宜 75%、知識截止晚 5 個月；Fable 5 轉為 Legacy，官方載明退役不早於 2027-06-09。

---

## 現況

現行世代是 **Fable 5.1**（2026-09-01 GA）；**Fable 5 仍可呼叫但已列為 Legacy**，官方建議遷移。兩者都是 Mythos 級模型的公開版——與同世代 Mythos 共用模型權重，差別在 Fable 前置了安全分類器，判定高風險時**會通知你**並改由 Opus 4.8 回答。

出口管制已於 2026-06-30 解除、07-01 起全球恢復存取，現在不影響你拿不拿得到；政府那條線之後怎麼走見 [[topics/anthropic-government-policy]]。方案內含什麼、超出怎麼算見 [[entities/pricing]]。

## 你現在拿到的是什麼

> 資料截至 2026-09-07（官方模型頁與說明中心查證）。一格一個你會問的問題，兩欄是兩代的答案。

| 這一格 | Fable 5（Legacy） | Fable 5.1（現行） | 官方出處（查證日） |
|---|---|---|---|
| 現在誰是預設 | 否 | 是——Claude Code v2.1.257 起 Fable 預設即 5.1 | [[feature-radar]] 版本階梯（2026-09-04）|
| 牌價（輸入／輸出，每百萬 token）| $10 ／ $50 | $10 ／ $50（同價）| 官方模型總覽頁（2026-09-07）|
| 快取讀取 | 基礎輸入價 ×0.1（$1）| ×0.025（$0.25）——便宜 75% | 官方定價頁（2026-09-07）|
| 知識截止 | 2026-01 | 2026-06 | 官方模型總覽頁（2026-09-07）|
| 會不會停掉 | Legacy，退役**不早於 2027-06-09**，官方建議遷移 5.1 | 退役不早於 2027-09-01 | 官方模型總覽頁（2026-09-07）|
| 官方推薦拿它做什麼 | 同右（官方已改推 5.1）| 高要求推理與長期 agentic 工作；Opus 5 調高 effort 仍不夠時 | 官方選型文件（2026-09-07）|
| 我的方案能不能用 | Max 與 Team premium：週用量 50% 內免費；Pro 與 standard：走 usage credits | 同左，兩代同一套規則 | 官方說明中心（2026-09-07）→ [[entities/pricing]] |

**表下細節**

- **兩代共用一套方案規則**：官方說明中心寫「Fable 5 and Fable 5.1 are available on all paid plans」，但「拿得到」不等於「方案內含」——Pro 拿得到，是走 usage credits 付費。2026-07-19 到期的那檔免費促銷只適用 Fable 5，5.1 從未納入。
- **Context 與輸出長度兩代相同**：1,000,000 token context、128,000 token 最大輸出。1M 這個旋鈕本身的計費與可見性見 [[topics/long-context-1m]]。
- **5.1 新增反萃取（anti-distillation）機制**，防止他人萃取權重或行為訓練競品（官方 2026-09-01 公告）。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦（2026-09-07 判定）|
| 最適合 | 跨多天的長期 agentic 工作流、多步驟深推理、安全漏洞分析 |
| 不適合 | 日常短問答（成本過高）；分散式訓練基建、加速器設計這類前沿 LLM 開發（分類器會擋，見下一節）|

> 本表跟著 [[feature-radar]] 全覽表的現行世代那一列走；最新熱度以 [[feature-radar]] 為準。

## 護欄會怎麼改寫你的請求

送進去的請求若被前置安全分類器判為高風險，**你會收到通知**，該次請求改由 Opus 4.8 回答，不是安靜地把品質調低（官方 2026-06-30〈Redeploying Claude Fable 5〉：「Users will be notified if a request to Fable 5 is blocked」）。2026-06-09 發布時的「降級且不告知」已於 06-11 由官方道歉撤回。

| 會踩到的類別 | 具體是什麼 | 誰最容易誤觸 | 你能先做什麼 |
|---|---|---|---|
| 資安（cybersecurity）| 攻擊性資安任務 | **日常 coding 與 debugging 也會較常被誤標**（官方自己寫明的代價）| 看到通知就接受 Opus 4.8 的答案，或把安全審查拆成不觸發的小步驟 |
| 生物與化學 | 高風險生物、化學請求 | 做相關研究的人 | 2026-08-07 官方更新分類器後生物領域誤判約降 85%，再遇到就換問法 |
| 模型萃取（distillation）| 取得權重或行為以訓練競品 | 想拿它的輸出訓練自己模型的人 | 沒有繞法 |
| 窄範圍前沿 LLM 開發 | 分散式訓練基建、ML 加速器設計、非標準晶片的 kernel 開發 | 做這三類工程的人 | 沒有繞法，這類工作改用其他模型 |

**表下細節**

- **5.1 誤觸更少**：官方 2026-09-01 公告把「更少誤判」列為換代理由之一（媒體轉述，2026-09-07 查證）；資安領域是否同步改善，官方仍未逐項說明。
- **分類器刻意調得保守**：官方〈Improving Fable 5 Safeguards〉原文寫 deliberately tuned to be cautious，並稱 Amazon 通報的那項特定技術已擋下逾 99%。被擋的比例，官方在 2026-06-09 發布時稱不到 5% 的 session。
- **這件事對你的產品做了什麼**（政府談判換來的承諾落到你手上長什麼樣）見 [[topics/anthropic-government-policy]]「政府動作對你的產品做了什麼」；那一節也寫出你的選項。
- **機制沿革**：06-09 發布版對前沿 LLM 開發降級且不告知（System Card），06-11 官方道歉改為可見防護；07-02 隨解禁導入 Defense in Depth 分類器，首日即有合法資安審查被誤攔的公開案例。

## 使用指南

**快速上手（Claude Code）：** 用 `/model` 選 Fable；Claude Code v2.1.257 起預設就是 5.1。要指定特定版本的 model id，見官方模型總覽頁（id 會隨版本更新，本頁不抄）。

**注意事項：**
- 方案內含與 usage credits 的分界見 [[entities/pricing]]；Max 與 Team premium 為標配（週用量 50% 內），Pro 與 standard 走 usage credits。
- 前沿 LLM 開發、攻擊性資安、生物化學、模型萃取四類請求會觸發分類器，見上一節。
- 30 天資料保留政策適用於所有平台（含 AWS Bedrock），資料離開 AWS 安全邊界。

## 核心功能

- **多模型協作數字（社群整理轉載，2026-07-08）**：「Fable 5 orchestrates, cheap models execute」——由 Fable 5 調度、便宜模型執行，宣稱以 46% 成本達到 96% 效能。此數字經 Reddit 整理轉載，**原始官方發布連結未見**，本站列為社群轉載而非官方基準。
- **Mythos 架構公開版**：首次讓大眾使用 Mythos 等級推理能力
- **1M context + 128K output**：適合處理整個 codebase 或長文件的任務
- **多模態**：軟體工程、視覺、科學研究均達 SOTA

## 爭議

> 🔴 現在還會遇到｜⚠️ 有爭論、官方無結論｜✅ 官方已處理

- ✅ **生物安全防護誤判大幅降低（2026-08-07，官方）**：Anthropic 官方部落格宣布更新生物安全分類器，測試顯示各產品面「生物相關降級」（誤判 fallback 至 Opus 4.8）情形減少約 85%；呼應下方「資安研究者護欄過激」等既有護欄過敏爭議，本次為官方對其中生物領域誤判的具體修復進展，資安領域的過敏問題是否同步改善未提及（[Anthropic Blog](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards)，2026-08-07）
- ⚠️ **資安研究者護欄過激**：Fable 5 安全分類器過度敏感，連讀取資安部落格、分析 GitHub profile 等無害操作也被攔截；IBM X-Force 知名研究員 Valentina Palmiotti 公開批評（TechCrunch，HN score 512）
- ⚠️ **「Fix this code」三詞越獄機制公開（2026-06-22）**：dev.to 文章《The Fable 5 Jailbreak Was Three Words Long》揭露引發出口管制的具體越獄機制——「Fix this code」三個字即可繞過 Fable 5 安全控制（[dev.to](https://dev.to/peremptory/the-fable-5-jailbreak-was-three-words-long-457j)）；此事件直接呼應美國政府「護欄不可靠」的管制論點，亦是 Amazon 研究人員向白宮通報的漏洞細節首次公開
- ⚠️ **Jailbreak 已公開（早期 PoC）**：Pliny（@elder_plinius）與 0xSufi 已公開 Fable 5 護欄繞過 PoC，使用多步驟攻擊組合（請求拆解重組、敘事框架包裝、長 context 操作）
- ⚠️ **Microsoft 內部禁用**：Microsoft 法務/合規部門要求員工不得使用 Fable 5（Times of India、PYMNTS 報導，與 Fable 5 數據保留政策相關）
- ⚠️ **Fable 5 成本高昂**：$200/月 Max 用戶一次 code review 可消耗 45% 週配額；社群回報消耗量個體差異極大
- ⚠️ **30 天資料保留**：Bedrock 用戶數據強制離開 AWS 安全邊界，企業隱私顧慮
- ⚠️ **「失去靈魂」討論**：部分用戶認為 Fable 5 相比 Opus 4.6 更工具性、減少人本關懷深度
- ⚠️ **「Defense in Depth」分類器誤判（2026-07-02，新）**：redeploy 後新增的資安/程式碼請求分類器出現誤判案例——合法資安審查請求被攔截、化學問題被拒（後者範圍已於 2026-08-26 查證確認不限於 coding/cybersecurity，見下方歷史記錄 2026-07-02）
- 🔴 **Fable 5 advisor 跨全部 session 顯示 unavailable**：完整追蹤與最新互動數見 [[entities/claude-code]] 已知問題（GitHub #73365）
- 🔴 **Max 方案被要求另購 usage credits 才能跑 Fable 5**：計費面見 [[entities/pricing]]、缺陷追蹤見 [[entities/claude-code]]；1M 變體引發的通用問題見 [[topics/long-context-1m]]
- ⚠️ **「太危險」分級受競品追平質疑**：r/ClaudeCode 使用者認為 Fable 5 被「削弱」後只比 Opus 4.8 聰明一點，開源模型已追上「太危險」等級能力（單一社群貼文，未附測試方法）；分類爭議的安全政策脈絡見 [[topics/ai-agent-safety]]，此處僅記能力落差角度

## 相關議題

- [[entities/mythos]] — 同一權重的無護欄版，只開放信任機構；誰拿得到、拿去做什麼
- [[entities/pricing]] — 我的方案內含什麼、超出後怎麼算、一小時大概多少
- [[topics/model-comparison]] — 這份工作該用哪個模型（Fable 5.1 vs Opus 5 vs Sonnet 5）
- [[topics/anthropic-government-policy]] — 政府那條線會不會讓你哪天用不到、或用到被改派的版本
- [[entities/claude-code]] — Claude Code 現在有什麼毛病（Fable 相關的 issue 追蹤在這）
- [[topics/long-context-1m]] — 1M context 這個旋鈕本身的計費與可見性
- [[topics/ai-agent-safety]] — 護欄被繞過、越獄與提示注入這類攻擊面（本頁爭議節那幾條的安全政策脈絡）

## 參考來源

- [[news/2026-06-09]]
- [[news/2026-06-10]]
- [[news/2026-06-11]]
- [[news/2026-06-12]]
- [[news/2026-06-13]]
- [[news/2026-06-14]]
- [[news/2026-06-15]]
- [[news/2026-06-16]]
- [[news/2026-06-17]]
- [[news/2026-06-18]]
- [Anthropic 官方公告](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [System Card PDF](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf)
- [資料保留政策](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)
- [[news/2026-08-11]]
- [GitHub Issue #77136：跨模型代際重複修辭套路問題](https://github.com/anthropics/claude-code/issues/77136)（2026-08-27）
- [[news/2026-08-15]]
- [[news/2026-08-19]]
- [Google News/Futurism：Nobody Wants Anthropic's Best AI Model Anymore](https://news.google.com/rss/articles/CBMingFBVV95cUxQcktnOVJUTlRkVG53NHl6ZlR4RFhTekx1ZlQ4cmRRZVROMG5vZzZNR0cwandpVlhfM3MzQnhNTEZDX0pQR1dfOVF2SnhJcmkwYWtaZXJGZF9LVlBKQ1cxRHdLeHFuZzlBR2FpT3JEb05QUTJGQ3JUQzlYeGlrRlJrQkNrdzFMR1F3WThfdW5wb1RwUkI4a2d0a2RWSWxKZw?oc=5)（2026-08-26，僅標題可用）
- [Google News/tech-insider.org：Claude Fable 5 vs Opus 5 vs GPT-5.6 Sol: $1,125 Gap](https://news.google.com/rss/articles/CBMiekFVX3lxTE1lT2hvNTRuTm5IVEt4WG5vV3BMQmxLdmZHX2lubDN4SzRvczBYblBJVFMteHM4V3UtM1l2NFZQYWFvbEZmaFVxdFIwSmlvRkpwc29KQzdOUXNPRWFpcDJyLWhDd0VfUkdlQ0Y3Vzk0MzBaUWtuanFLc1FR?oc=5)（2026-08-26，僅標題可用）
- [Reddit：Is it even legal for Anthropic to nerf its models this hard?](https://www.reddit.com/r/ClaudeCode/comments/1w0t53b/is_it_even_legal_for_anthropic_to_nerf_its_models/)（2026-08-28）
- [Reddit：Do you guys think that Fable 5.1 is actually dropping today](https://www.reddit.com/r/ClaudeCode/comments/1w0v676/do_you_guys_think_that_fable_51_is_actually/)（2026-08-28）
- [[news/2026-08-28]]
- [Anthropic Blog：Claude Fable 5.1 and Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)（2026-09-01）
- [Anthropic Document：Claude Fable 5.1／Mythos 5.1 System Card](https://www.anthropic.com/document/claude-fable-5-1-mythos-5-1-system-card)（2026-09-01）
- [Official Docs：API 模型定價（快取讀取費率）](https://platform.claude.com/docs/en/about-claude/pricing)（2026-09-02 查證）
- [Official Docs：Claude Fable 5 on your plan（世代交接後方案內含範圍）](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)（2026-09-02 查證）
- [[news/2026-09-01]]
- [[news/2026-09-02]]

## 歷史記錄

### 解禁後（2026-07-01 起）

#### 2026-09-04
**費馬最後定理形式化證明（官方 2026-09-07 查證：使用內部研究模型，非 Fable 5 或 5.1）**：
- **Anthropic 官方研究文章**：Claude 歷時 11 天完成費馬最後定理的電腦驗證證明。官方寫明用的是「內部研究模型，約略相當 Fable 5.1」，不是 Fable 5 或 5.1 本身，本頁僅作參考記錄（[Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem)，2026-09-04；歸屬 2026-09-07 查證）
- 長期主導此形式化工作的 Xena Project 作者 [[entities/kevin-buzzard]] 於部落格公開表示「被 Anthropic 搶先」，指出 Anthropic 走的是 Darmon–Diamond–Taylor 於 1995 年闡述的 Wiles–Taylor–Wiles 證明路徑並開發 Fontaine 理論，此題也是 Freek Wiedijk 百大形式化挑戰清單最後完成的一項（[Xena Project](https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/)，2026-09-04；人物背景查證日 2026-09-05）
- SingularityHub 報導 Claude 已能自主操作實驗室設備執行科學實驗，與費馬定理證明同屬「長期自主研究任務」訊號，惟兩者是否為同一脈絡未經證實（Google News/SingularityHub，2026-09-04）
- Reddit r/artificial 週熱門討論串彙整 Claude Fable 5.1 與 Mythos 5.1 基準測試結果，惟摘要未載具體分數，原始數字待查證（Reddit / r/artificial · 週熱門，2026-09-01）
- **服務中斷（非模型特定）**：同日 Anthropic、OpenAI、xAI 三家模型服務上午同時發生罕見中斷，三方對外皆未說明確切成因，原文未指名受影響的具體 Claude 模型，是否與下方 09-03 多模型錯誤率事件相關亦未經證實（[Wired](https://www.wired.com/story/nobody-is-saying-why-openai-and-anthropic-had-outages-today/)，2026-09-04）

#### 2026-09-03
**Anthropic 狀態頁：多款模型錯誤率升高（截至資料蒐集時尚未標記為已解決）**：
- Fable 5.1／5 與 Mythos、Opus 全系列同時錯誤率升高。官方 13:41 UTC 鎖定原因，**14:38 UTC 仍未標記已解決**；同時段 Reddit r/ClaudeCode 湧入中斷回報（[Anthropic Status](https://status.claude.com/incidents/461yvfrzpwtt)；[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1w69016/claude_code_server_down_for_a_long_time_now_will/)，2026-09-03）
- 屬穩定性事件，非能力或定價變化；Sonnet 5 同日另有一起獨立事件已於 12:56 UTC 解決，完整記錄見 [[entities/sonnet-5]]

#### 2026-09-02
**多家媒體跟進報導，成本降幅說法不一（並陳不選邊）＋ 官方文件確認方案內含範圍**：
- 官方說明中心頁面〈Claude Fable 5 on your plan〉大幅改版（22,010 字 → 22,697 字），新增「Claude Fable 5 and Claude Fable 5.1 are available on all paid plans (Pro, Max, Team, and Enterprise)」「Claude API: Access to Fable 5 and Fable 5.1 is billed at standard API rates」等段落，並移除舊版純 Fable 5 專屬內容，反映世代交接後方案內含範圍的變化；定價細節留給 [[entities/pricing]]（[Official Docs](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)，2026-09-02）
- MarkTechPost 報導 Fable 5.1／Mythos 5.1 在 Terminal-Bench-Science 得分 **52.6%**，並稱快取讀取成本降 75%（與官方定價頁 0.025 倍換算一致，見 09-01 條目）
- **成本降幅各家說法不一，未見單一媒體逐項拆解**：the-decoder.com 稱「最多降 45%」、Pasquale Pillitteri 稱「25% 更便宜」、Yellow.com 稱快取讀取為 $0.25、MarkTechPost／VentureBeat／WinBuzzer 稱快取讀取降 75%——各數字可能對應不同計費項目（整體成本 vs 快取讀取單項），本頁不選邊，具體定價換算留給 [[entities/pricing]] 與 [[topics/model-comparison#同一份工作，換設定差多少]] 查證（Google News 綜合，2026-09-01～02）
- Wccftech 報導 Samsung 將其晶片設計工作押注於 Claude Code（與本次發布同日報導，具體採用細節、是否具名確認未見原文佐證）
- ❓ 待查證 ⟨Q-01⟩ **TechCrunch：新版「更便宜、限制更少」**：標題稱 Fable 5.1「cheaper, less restrictive」，僅標題可用，具體所指未經證實（詳見「懸置細節」）
- **GitHub Issue #79337 逾 6 週未解**：07-20 首次回報的「Max 方案需額外 usage credits 才能執行 Fable 5、靜默降級至 Opus 4.8」事件持續延燒，累積留言數已增至 **76 則**、reaction 增至 **26 個**，距官方 07-20「確認為誤判並建議重啟」的結論已逾 6 週仍未見官方後續說明或關閉 issue，顯示問題可能非單次誤判；計費/配額面向見 [[entities/pricing]]（[GitHub Issues](https://github.com/anthropics/claude-code/issues/79337)，2026-09-02 02:12 UTC）

#### 2026-09-01
**Claude Fable 5.1 與 Claude Mythos 5.1 正式發布**：
- Anthropic 官方公告，Fable 5.1 與 Mythos 5.1 為**同一模型的不同防護層級**——Fable 5.1 一般可用（GA），Mythos 5.1 僅開放信任機構存取，其防護「專為資安與生命科學工作設計」（官方原文：「Claude Fable 5.1 and Claude Mythos 5.1 are the same model, but with different levels of safeguards. Fable 5.1 is generally available, while Mythos 5.1 is available only through our trusted access programs; its safeguards are specifically designed to support work in cybersecurity and the life sciences.」）；此為 08-28 社群傳聞（見上方「歷史記錄」08-28 條目）的官方證實
- 官方稱其為「coding 與知識工作最先進的模型」，研究能力對科學進展已展現初步貢獻潛力；新增**反萃取（anti-distillation）機制**——防範他人萃取模型權重／行為用以訓練競品
- HN 討論達 **1,338 分**，屬近期官方公告中互動度最高之一（[Anthropic Blog](https://www.anthropic.com/claude-fable-and-mythos-5-1)，2026-09-01）
- **System Card 同步發布**：官方公布 Fable 5.1／Mythos 5.1 完整 System Card 文件（HN 16 分）（[Anthropic Document](https://www.anthropic.com/document/claude-fable-5-1-mythos-5-1-system-card)，2026-09-01）
- **The New Stack：隱形浮水印偵測盲區**：報導指出 Fable 5.1 的隱形浮水印機制仍存在開發者無法忽視的偵測盲區，具體技術細節未見完整摘要（Google News/The New Stack，2026-09-01）
- **Fortune：反萃取機制解析**：深入解析 Fable 5.1／Mythos 5.1 能力與新增反萃取防護機制設計（Google News/Fortune，2026-09-01）
- **AWS 上線**：AWS 官方部落格宣布 Claude Fable 5.1 於 AWS 上線可用（Google News/AWS，2026-09-01）
- **Simon Willison 首日實測**：知名獨立開發者 Simon Willison（慣例以「畫一隻騎腳踏車的鵜鶘」測試新模型）記錄 Fable 5.1 首日實測心得，稱其「sets a new standard for coding, knowledge work, and long...」（原文摘要於此處截斷，完整脈絡未查證）（Blog/Simon Willison，2026-09-01）
- **定價面**：官方定價頁同步更新，快取讀取（cache hit）與 refresh 費率由基礎輸入價的 0.1 倍降至 **0.025 倍**（原文：「Cache hits and refreshes on Claude Fable 5.1 and Claude Mythos 5.1 are priced at 0.025x the base input price」）；細節見 [[entities/pricing]]（[Official Docs](https://platform.claude.com/docs/en/about-claude/pricing)，2026-09-02）

#### 2026-08-28
**Reddit 質疑串：「Anthropic 是否在削弱模型」**：r/ClaudeCode 貼文「Is it even legal for Anthropic to nerf its models this hard?」，使用者抱怨 Opus 5 與 Fable 5 在 Claude Code 中的實際表現遜於預期，質疑模型遭「削弱」（nerf）；單一使用者觀感回報，無具體案例或量化數字佐證，延續 08-13「rage-inducing」、08-20「smoking gun」等已記錄的社群觀感分歧模式（完整同類記錄見 [[entities/opus-5]]「歷史記錄」）（[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1w0t53b/is_it_even_legal_for_anthropic_to_nerf_its_models/)，2026-08-28）。

❓ 待查證 ⟨Q-02⟩ **Fable 5.1 是否即將發布**：Reddit 傳聞疑似已被路由至新版本測試，無官方佐證（詳見「懸置細節」）。**後續（2026-09-01）**：Anthropic 官方正式發布 Claude Fable 5.1 與 Claude Mythos 5.1，證實社群傳聞屬實；詳見上方「現況」與下方本節 2026-09-01 條目（[Anthropic Blog](https://www.anthropic.com/claude-fable-and-mythos-5-1)，2026-09-01）。

#### 2026-08-27
**GitHub Issue #77136：跨模型代際重複修辭套路問題**：開發者回報 Claude 4.7、4.8、5.0 與 Fable 日益出現重複修辭、難以維持連貫散文的問題，即使給出明確風格指示仍難改善；已累積 106 則留言、517 個反應，尚無官方回應。此為**跨模型代際的共同問題**（非 Fable 5 獨有），完整記錄見 [[entities/opus-5]]「歷史記錄」（[GitHub Issue #77136](https://github.com/anthropics/claude-code/issues/77136)，2026-08-27）。

同日官方說明文件〈Claude Fable 5 on your plan〉重申存取依方案分流（Max 方案優先存取），與 08-19 已查證記錄的規則一致，無新資訊，不重複記錄計費細節（詳見 [[entities/pricing]]）。

#### 2026-08-26
**Futurism：企業轉向更便宜替代模型、Anthropic 旗艦採用意願下滑（僅標題可用）**：Google News 轉載 Futurism 標題〈Nobody Wants Anthropic's Best AI Model Anymore Now That There Are Way Cheaper Alternatives〉；RSS 僅提供標題與轉址連結，無正文可查證具體採用數據、樣本或方法論。與上方 08-18 analyticsindiamag.com〈Almost Nobody Is Using Anthropic's Fable 5〉標題主題相近，惟來源、標題涵蓋範圍（泛稱「最強模型」vs 明確指名 Fable 5）皆不完全相同，暫不合併視為同一事實的兩次獨立確認，亦不做因果推論。❓ 待查證 ⟨Q-03⟩ **企業轉向更便宜替代方案的具體佐證**：僅標題可用，無採用數據或方法論佐證（詳見「懸置細節」）

**tech-insider.org 模板化定價比較標題（僅標題可用，模型能力面）**：同日另有 tech-insider.org（經 Google News 轉載）發布標題《Claude Fable 5 vs Opus 5 vs GPT-5.6 Sol: $1,125 Gap [2026]》，比較 Fable 5、[[entities/opus-5|Opus 5]] 與競品 GPT-5.6 Sol 定價；同站另有一篇比較 Opus 5 與 Grok 4.6、Gemini 3.1 Pro 的同系列標題，記於 [[entities/opus-5]]。本則僅標題可用、無正文，「$1,125 Gap」具體數字未經查證，不採信為事實；如經查證，具體定價數字應留給 [[entities/pricing]] 記錄。❓ 待查證 ⟨Q-04⟩ **Fable 5 vs Opus 5 vs GPT-5.6 Sol 的 $1,125 差距計算基準**：僅標題可用，計算基準未經查證（詳見「懸置細節」）

**官方說明文件〈Claude Fable 5 on your plan〉重新抓取，內容未變（非新事件）**：官方頁面本輪被重新抓取，經比對內容與 08-19 已查證版本一致，仍為 7/19 促銷到期後的既定分流規則，非新公告；不重複記錄，計費細節仍以 [[entities/pricing]] 為準。

#### 2026-08-19
**官方說明文件更新確認促銷結束日與分流政策（與 2026-08-08 查證結果一致）**：Anthropic 官方說明文件更新〈Claude Fable 5 on your plan〉頁面，明載先前促銷（允許用戶最多以週訂閱額度 50% 免費使用 Fable 5）已於 **2026-07-19 23:59:59 PT** 結束（並非早期 2026-07-01 公告所稱的 7/7）。促銷結束後：Max 方案、Team 方案 premium seat、舊制（legacy seat-based）Enterprise 方案 premium seat，Fable 5 成為方案標準內含項目；Pro 方案、Team 方案 standard seat、舊制 Enterprise 方案 standard seat，Fable 5 改以 pay-as-you-go usage credits 計費；目前所有付費方案（Pro/Max/Team/Enterprise）皆可使用 Fable 5。本次官方文件與 2026-08-08 Help Center 查證所得的分流結論一致；官方引文為「On Max plans, premium seats on Team plans, and premium seats on legacy seat-based Enterprise plans, Fable 5 will be a standard part of your plan. On Pro plans, standard seats on Team plans, and standard seats on legacy seat-based Enterprise plans, Fable 5 will run on pay-as-you-go usage credits.」。計費規則細節（含週用量 50% 上限是否延續等定價面問題）詳見 [[entities/pricing]]（Official Docs，2026-08-19）。

❓ 待查證 ⟨Q-05⟩ **單一來源報導稱 Fable 5「幾乎無人使用」**：僅標題可用，無採用數據或方法論佐證（詳見「懸置細節」）。**與其他條目的關係**：本則報導日期與同日「Claude Code 週用量促銷延長」報導、以及上方 08-19 官方文件確認的 07-19 促銷到期時間點相近，但原文未提供因果證據，本頁不做因果推論，僅並列記錄。2026-08-26 另有 Futurism 報導呼應類似主題但範圍不完全相同，見下方「2026-08-26」條目，兩則不合併視為同一事實。

#### 2026-08-15
**Anthropic Status：錯誤率一度升高（同日解決）**：Anthropic Status 通報 Fable 5 於 2026-08-14 20:00 至 2026-08-15 00:11 UTC 錯誤率升高，事件已解決，無需採取行動（[Anthropic Status](https://status.claude.com/incidents/hdynq1pc0fn8)，2026-08-15）。

**Reddit 週熱門：企業端為何不採用 Fable 5？（開放式討論，無具名案例）**：r/ClaudeAI 週熱門貼文討論企業端採用 Fable 5 的阻力何在；原文未提供具名企業案例或量化數據，屬開放式社群討論，暫列觀察，未達 `enterprise-tool-tracker.md` 具名企業收錄門檻（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vnj1xq/why_arent_businesses_using_fable_5/)，週熱門，2026-08-15）。

#### 2026-08-11
**未發布研究版 Claude 意外改進黎曼假設 zeta 函數下界紀錄（研究里程碑，非 Fable 5 本體）**：Anthropic 官方部落格公告，一個**未發布的研究版 Claude**（非現行 Fable 5 產品版本）在嘗試證明黎曼假設（Riemann hypothesis）未果的過程中，意外改進了「黎曼 zeta 函數零點滿足該假設比例」的長期下界紀錄，該紀錄先前已維持 87 年未被突破；The Times of India 另有跟進報導，指研究者感謝 Claude 協助解開此一長年數學猜想相關進展。此為 Anthropic 內部研究能力展示（HN 211 分、4 個獨立來源轉載），與 Fable 5 產品版本或其部署狀態無直接關聯，僅記為 Anthropic 前沿數學研究能力的里程碑參考（[Anthropic Blog](https://www.anthropic.com/research/riemann-zeta)、The Times of India，2026-08-11）。

**媒體延續報導（無新增技術細節）**：TechSpot 於 2026-08-13 刊出〈Anthropic's Claude tried to solve the Riemann hypothesis and found something new instead〉，敘事（嘗試證明黎曼假設未果、過程中取得新數學進展）與上則 08-11 Anthropic 官方部落格公告高度吻合，判斷為同一事件的媒體接力報導，非獨立新事件；Google News RSS 僅提供標題，無正文可查證是否含超出官方原文的新細節（Google News/TechSpot，單一來源，2026-08-13）。

#### 2026-08-07
**官方更新生物安全防護，「生物相關降級」減少約 85%**：Anthropic 官方部落格公告《Improving Fable 5's biology safeguards》，宣布更新 Fable 5 的生物安全防護（biology safeguards）。測試顯示，此次更新使各產品面「生物相關降級」（誤判觸發 fallback 至 Opus 4.8）情形減少約 85%（官方原文：「this update reduced biology-related fallbacks by about 85% across our product surfaces」）。實務影響：日常健康／教育類問題（判讀檢驗報告、理解症狀、學習生物學教育內容）預期更少被誤判降級；醫療專業人員在臨床任務上將能獲得 Fable 5 更多協助（官方原文：「Healthcare professionals will be able to receive more support from Fable 5 on clinical tasks」）。此為官方對「資安研究者護欄過激」「Defense in Depth 分類器誤判」等既有護欄過敏爭議中，生物領域面向的具體修復進展；資安/程式碼領域的過敏問題官方本次公告未提及是否同步改善（[Anthropic Blog](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards)，2026-08-07）。

**Astra security／The Register「放寬 Fable 5 限制」即為同日生物安全防護更新**（2026-08-07 報導，2026-08-10 查證）：The Register 同日報導《OpenAI pledges to add Astra security as Anthropic loosens Fable's leash》，經查全文確認「loosens leash」具體所指為官方部落格同日公告的生物安全防護更新——Anthropic 放寬 Fable 5 對生物相關提示的護欄拒答（fallback）頻率，與上一則 08-07 生物安全防護公告為**同一事件**，非另一項獨立放寬措施（[The Register](https://www.theregister.com/ai-and-ml/2026/08/08/openai-pledges-to-add-astra-security-as-anthropic-loosens-fables-leash/5285161)，2026-08-08）。

#### 2026-07-31
**法官質疑聯邦政府「供應鏈風險」禁令正當性，與 Fable 5 出口管制為不同政策線**（2026-08-10 官方/媒體查證）：Hacker News 轉載 Bloomberg 報導《Judge Voices Doubt US Has Justified Its Ban on Anthropic AI》，查得全文確認：聯邦法官 Rita F. Lin 認為川普政府未充分證明將 Anthropic 列為「供應鏈風險」的正當性，稱以「Anthropic 公開批評國防部」作為禁令理由「令人憂慮」；爭議根源是 Anthropic 與美國國防部合約談判破裂，Anthropic 拒絕其 AI 被用於大規模監控或致命武器鎖定／開火決策。此案為**聯邦機構採購/使用限制爭議**，與 Fable 5 晶片**出口管制**（已於 2026-07-01 解除）是兩條獨立政策線，不應合併記錄；與 2026-06-24 Legion 提告出口管制令一案是否同一訴訟程序仍未經證實，不可逕自合併。完整法律論證內容與政策脈絡見 [[topics/anthropic-government-policy]]（[Bloomberg](https://www.bloomberg.com/news/articles/2026-07-30/judge-voices-doubt-us-has-justified-its-ban-on-anthropic-ai)、[HN 討論](https://news.ycombinator.com/item?id=49117486)，2026-07-30/31）。

**終局判決（2026-08-28，🔴→✅ 結案）**：Rita F. Lin 法官裁定國防部「供應鏈風險」黑名單違法且毫無根據，即時解除禁令；The Register 指出黑名單當初所依據的 Claude「能力」實際上並不存在，為判決翻案的關鍵理由之一（Reuters／Washington Post，2026-08-28）。此案終局結果與 Fable 5 晶片出口管制（已於 2026-07-01 解除）仍是兩條獨立政策線，本則僅摘記模型面關聯；完整判決分析、後續 Anthropic 與國防部合作動向見 [[topics/anthropic-government-policy]]「## 現在有哪幾條線在動」與「## 三個戰場」🪖 軍事合約段落。

#### 2026-07-24
**GitHub Issue #79337 持續追蹤：reaction 增至 13 個 + 新技術細節「已儲存模型 claude-fable-5[1m]」**：07-20 首次回報的 Max 方案誤判事件持續有讀者互動，reaction 數由 10 個增至 13 個（留言數維持 35 則、暫無更新資料）；本次追蹤新揭露受影響帳號的已儲存模型設定為 `claude-fable-5[1m]`，即 1M context 變體，有助釐清受影響的具體模型設定範圍。官方已於 07-20 確認為誤判並建議重啟，此結論未變，計費/配額面向詳見 [[entities/pricing]]（[GitHub Issues](https://github.com/anthropics/claude-code/issues/79337)，2026-07-24 01:16 UTC）。**後續（2026-09-02）**：issue 仍未關閉，留言數已增至 76 則、reaction 增至 26 個，距 07-20「已確認為誤判並建議重啟」的結論已逾 6 週，顯示問題非單次誤判或已復發；詳見下方「歷史記錄」2026-09-02 條目。

**社群觀點：「太危險」分級與競品追平能力的落差（單一來源，社群觀點）**：Reddit r/ClaudeCode 使用者認為 Fable 5 被「削弱」後感覺只比 Opus 4.8 聰明一點，開源模型已追上原本被列為「太危險」等級的模型能力（[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1v56yic/open_source_model_at_par_with_fable/)，2026-07-24，單一來源、score 恆 0）。同期另有 r/ClaudeAI 週熱門貼文（原貼 2026-07-18），一名自稱基因學/神經科學研究者質疑 Fable/Mythos「對科學研究太危險」的分類，認為自身分析 RNA 等用途與生物恐怖主義完全無關；此則安全分級爭議完整脈絡見 [[topics/ai-agent-safety]]，本頁僅並列記錄競品/能力落差角度。兩則均為個人觀點，非量化評測，不構成能力結論。

**（已排除）「Fable 5 min cache」貼文**：另有 r/ClaudeCode 圖片型貼文僅標題提及快取時間偏短，無正文內容佐證，單一來源，證據不足，本輪不予記錄。

#### 2026-07-20
**GitHub Issue #79337：Max 方案誤判需購買 usage credits 才能執行 Fable 5，session 靜默降級至 Opus 4.8（官方已證實為誤判，非未修復）**：GitHub Issue 回報，2026-07-20（issue 原文稱為 Fable 5 正式成為 Max 方案標準配置的第一天）當天，Claude Code 一度拒絕在 Max 方案上執行 Fable 5，提示需購買額外「usage credits」，並將 session 靜默降級至 Opus 4.8；累積 10 個 reaction、35 則留言（[GitHub Issues](https://github.com/anthropics/claude-code/issues/79337)，2026-07-20）。**與既有事件的關係**：時間點與症狀（Max 方案 + 要求點數 + 涉及 Fable 5）與同日 Anthropic Status 公告的「Max 方案用戶被誤判需使用點數才能存取 Fable 5」事件高度吻合，官方已證實為誤判並建議受影響用戶重啟；本則 GitHub Issue 可能是同一起誤判事件經由另一管道的獨立回報，惟兩則來源未見官方明確互相對應確認，不逕自視為同一 issue（推論）。「Fable 5 正式成為 Max 方案標準配置」一說源自 issue 原文框架，與同期 [[entities/pricing]] 記錄的 Max/Team 存取政策分歧報導（07-19 Tech Times「轉為永久」vs 07-20 Reddit 週熱門「轉為計量存取」）需並陳看待，尚無官方公告一次性釐清「標配」的具體條件與計費方式；額度與計費爭議完整脈絡見 [[entities/pricing]]。

#### 2026-07-13
**Anthropic 拒絕說明延長原因，暗示與 Cursor 內部發現有關（推論）**：The New Stack 報導標題直指「Anthropic extends Fable 5 again — and won't talk about what developers found inside Cursor」，指出 Anthropic 拒絕說明本次延長是否與開發者在 Cursor 中發現的問題有關；Forbes 同日另一篇報導同樣說明存取限制延長，但未提供新細節。此為推測性報導，暗示延長原因可能另有隱情，但缺乏具體佐證，標「（推論）」（Google News／The New Stack、Google News／Forbes，2026-07-13）。

**多家媒體重複確認延長至 7/19（無新日期變化）**：Forbes（Tyler Roush）、Help Net Security、Economic Times、Forbes（Sandy Carter）等多家媒體同日重複報導 Fable 5 存取限制延長至 2026-07-19 一事，內容與 07-12 記錄的同一事件一致，未出現新的日期或條件變化，僅為跨媒體多來源重複確認（[Forbes](https://www.forbes.com/)、[Help Net Security](https://www.helpnetsecurity.com/)、[Economic Times](https://economictimes.indiatimes.com/)，2026-07-13）。

#### 2026-07-12
**存取限制再度延長至 7/19**：Anthropic 將 Fable 5 存取限制再次延長，由原訂 7/12 延至 2026-07-19（Google News/The Economic Times，2026-07-12 18:08 UTC）。[Simon Willison 部落格「Fable gets another bump」](https://simonwillison.net/2026/Jul/12/bump/#atom-everything)（2026-07-12 21:20 UTC）第一手記錄並指出，延後原因與競品 GPT-5.6 Sol 被業界視為明顯屬於 Fable／Mythos 同級模型有關，暗示 Anthropic 觀察競品定位後才決定存取政策走向；免費期限與計費細節見 [[entities/pricing]]。

#### 2026-07-10
**GitHub Issue #73365：Advisor 角色全面 unavailable（🔴 未修復）**：Fable 5 advisor（Opus 4.8 main 底下的 advisor 角色）在所有 Claude Code session 中皆顯示「unavailable」，版本 v2.1.198，累積 50 則留言、100 個讚，情緒 😤。此為 Claude Code 呼叫層面的可用性問題，已同步記入 [[entities/claude-code]] 已知問題。

#### 2026-07-09
**官方基準：「Fable 5 orchestrates, cheap models execute」— 46% 成本達 96% 效能**：Reddit 使用者整理 Anthropic 官方公布的多模型協作模式基準數字，指出以 Fable 5 負責任務調度（orchestrator）、由較便宜模型負責實際執行，可用 46% 的成本達到 96% 的效能水準；此模式現可在 Claude Code 中直接套用（Reddit r/ClaudeAI，週熱門標記，來源貼文日期 2026-07-08 19:17 UTC）。屬官方基準數據轉述，原始發布連結未附於本則貼文，暫未直接查證官方原始頁面。**後續（2026-09-07）**：本站核查未見原始官方發布連結，此數字改列為社群整理轉載，非官方基準。

#### 2026-07-08
**免費期限延長至 7/12 + zero-shot coding 實測**：
- **免費期再延長**：Anthropic 將 Fable 5 免費使用期限再延展 5 天，延至 2026-07-12（[Times of India](https://timesofindia.indiatimes.com/technology/tech-news/anthropic-extends-claude-fable-5-free-offer-till-july-12-eligibility-and-other-details-explained/articleshow/132255396.cms)、[Forbes](https://www.forbes.com/sites/sandycarter/2026/07/07/claude-fable-5-extends-by-five-more-days-10-moves-to-make-now/)，2026-07-07~08）；定價與資格細節見 [[entities/pricing]]
- **XDA zero-shot coding 實測**：作者以 Fable 5 進行 zero-shot（一次性）程式生成測試，並反思為何 Anthropic 選擇對 Fable 5 施加更嚴格的存取限制（[XDA](https://www.xda-developers.com/i-used-claude-fable-5-for-zero-shot-coding-and-understood-why-anthropic-locked-it-down/)）

#### 2026-07-06
**Anthropic 多模型錯誤率升高事件（同日解決）+ HN 實測佐證解封後能力**：
- **服務中斷**：Anthropic Status 通報多個模型一度出現錯誤率升高，Fable 5 也一併受影響，事件於同日解決，無需採取行動（[Anthropic Status](https://status.claude.com/incidents/tl8x3p1msff2)）；同期 AOL 彙整讀者對 Claude API 不穩定的抱怨與詢問（Response incomplete Claude / Is Claude down / Claude api error，07-05 22:24 UTC），屬服務穩定性面向，非出口管制或護欄爭議重演
- **Show HN 實測：Python 移植 Super Nintendo（6 分）**：作者以此專案作為 Fable 5 的實測案例——出口管制期間（6/12–6/30）專案卡關三週，Fable 5 解封後 90 分鐘內找出根本問題並修復 23 個編譯器 bug（[fabian-kuebler.com](https://fabian-kuebler.com/posts/fable-python-snes/)）；訊號雖弱（HN 6 分），但具體佐證解封後 Fable 5 在複雜除錯任務上的實際生產力

#### 2026-07-03
**配額重置規則釐清 + 消耗速度落差極大（社群策略彙整見「配額與計費過渡」子區塊）**：Reddit 社群釐清 Fable 5 額度重置時間依訂閱起始日而異，非統一週期（[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1umt5h5/fable_resets_on_monday_if_you_held_a_plan_already/)）；同日回報顯示個體消耗速度差異懸殊，2 天內燒完額度、大型基因體分析工作流受衝擊等案例並陳（[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1umtox4/i_burned_through_my_fable_5_usage_in_2_days_so_i/)、[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1umtlqh/sad_about_fable_restrictions/)）。

#### 2026-07-02
**Redeploy 技術細節：「Defense in Depth」分類器 + 早期實測褒貶不一**：
- **新安全機制**：Reddit 貼文整理 Fable 5 全球 redeploy（7/1）隨附的「Defense in Depth」措施——新增更嚴格的資安/程式碼請求分類器，一旦判定為高風險 coding/debug 請求，自動靜默 fallback 至 Opus 4.8 執行，不使用 Fable 5（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uliwhc/anthropic_just_redeployed_fable_5_globally_here/)）
- **負面實測：資安審查被誤判**：dev.to 作者實測用 Fable 5 執行合法資安審查工作，遭新分類器誤判為風險請求並攔截，作者形容「flagged my own request」（[dev.to](https://dev.to/tecnomanu/i-tried-fable-5-for-a-security-review-and-it-flagged-my-own-request-2pbn)）；此案例呼應 6/11 IBM X-Force 研究員 Valentina Palmiotti 曾批評的「護欄過激」問題，顯示該爭議在新分類器上仍未解決
- **範圍確認擴大：化學／生物提問同樣被拒**（2026-08-26 查證）：Reddit 貼文顯示使用者詢問化學相關問題被 Fable 5 拒答（「I guess not」）（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1ulh5he/can_you_ask_fable_anything_chemistry_related/)）。此非孤例——Anthropic 發言人向 The Verge 表示公司**刻意將防護調得過度保守**，以攔下多數與生物工作相關的查詢，並自陳護欄「平均在不到 5% 的 session 觸發」；The Verge 實測到細胞膜、粒線體、prion、mRNA 疫苗、花粉症、抗生素抗藥性等基礎題均被拒。化學面則以**分離程序＋特定化合物／產率／設備配置**最易觸發，一般蒸餾與教學層級提問多半放行。**Anthropic 已承認此調校「是錯的取捨」**，承諾揭露拒答原因並放寬生物類觸發條件。攔截範圍因此確認**不限於 coding/cybersecurity**，原「疑似」二字已可移除
- **與既有爭議的關係**：本次分類器行為為可見防護（用戶知道被 fallback），不同於 6/9 發布時「靜默降級不告知」已撤回的舊爭議；但誤判率與攔截範圍是否合理，仍待更多社群案例累積判斷

#### 2026-07-01
**出口管制正式解除，全球恢復存取**：
- **官方公告（[Anthropic Blog](https://www.anthropic.com/news/redeploying-fable-5)）**：美國出口管制解除，Fable 5 與 Mythos 5 於 2026-07-01 起向全球用戶恢復存取。過渡期計費：Pro/Max/Team 方案 7/7 前維持每週配額 50%；7/7 後改依用量計費，定價近期公布
- **Anthropic-美國政府協議**：Anthropic 承諾主動偵測安全風險、配合標準協議、通報惡意活動；此協議為 Fable 5 全球解禁的交換條件，標誌管制事件正式落幕
- **管制解除**：2026-06-30 宣布、07-01 全球恢復（天數口徑見 [[topics/anthropic-government-policy]]）

**懸置細節**

- ⟨Q-01⟩ ❓ **待查證**（標 2026-09-02｜查 techcrunch.com、less restrictive）：TechCrunch 標題稱 Fable 5.1「cheaper, less restrictive」，僅標題可用，「限制更少」具體所指未經證實（Google News/TechCrunch，2026-09-01）
- ⟨Q-02⟩ ❓ **待查證**（標 2026-08-29｜查 Fable 5.1、1w0v676｜複 2026-09-12｜訊 2026-09-02）：Reddit r/ClaudeCode 討論 Fable 5.1 是否即將發布，部分回覆稱疑似已被路由至新版本測試，純屬社群臆測，無官方公告或版本號佐證（Reddit，2026-08-28）
- ⟨Q-03⟩ ❓ **待查證**（標 2026-08-26｜查 Futurism、cheaper alternatives｜複 2026-09-09）：Futurism 標題稱企業轉向更便宜替代方案，僅標題可用，無採用數據、案例或方法論佐證（Google News/Futurism，2026-08-26）
- ⟨Q-04⟩ ❓ **待查證**（標 2026-08-26｜查 tech-insider.org、GPT-5.6 Sol｜複 2026-09-09）：tech-insider.org 標題稱三模型定價差 $1,125，僅標題可用，計算基準未經查證（Google News/tech-insider.org，2026-08-26）
- ⟨Q-05⟩ ❓ **待查證**（標 2026-08-26｜查 analyticsindiamag.com、Almost Nobody｜複 2026-09-09）：analyticsindiamag.com 標題稱 Fable 5「幾乎無人使用」，RSS 摘要未附正文，採用數據、統計方法、對比基準均未見報導（Google News，2026-08-18）

### 2026-06（發布與出口管制期）

- 2026-06-09 Fable 5 發布：首款向大眾開放的 Mythos 級模型，$10／$50、1M context、128K 輸出，與 Mythos 5 共用權重、差在前置安全分類器。
- 2026-06-10～11 護欄爭議：System Card 揭露對前沿 LLM 開發降級且不告知，官方 06-11 道歉並改為可見防護。
- 2026-06-13 美國政府要求停售，Anthropic 90 分鐘內關閉全球存取（含美國用戶）。
- 2026-06-16 Commerce 部長 Lutnick 致函（Bloomberg 全文刊出）主張護欄無法阻止取得 Mythos 的網路攻擊能力；Anthropic 否認該主張在技術上成立。
- 2026-06-18 Wired 揭露 SK Telecom 的中國關聯是管制的真正起點；Amazon 安全研究員向白宮通報是直接觸發原因。
- 2026-06-22 越獄機制公開：dev.to 揭露「Fix this code」三個字即可繞過控制。
- 2026-06-30 管制解除、07-01 起全球恢復存取，同時導入 Defense in Depth 分類器。
- 雙方立場的完整論點、逐日經過與商業衝擊（DoD 轉單、G7 不豁免、赴華府協商）見下方連結；攻防的家是 [[topics/anthropic-government-policy]]。

原始條目見 [[entities/fable-5-archive#2026-06]]；雙方立場的兩張表見 [[entities/fable-5-archive#出口管制：雙方立場]]。
