# Claude Fable 5

**類型：** model
**狀態：** active（正式發布；出口管制已解除，2026-07-01 起全球恢復存取）
**領域：** 🤖 模型
**首次出現：** 2026-06-09
**最後更新：** 2026-07-07
**最後新聞更新：** 2026-07-06

> **最新進展**（2026-07-06）
> Anthropic 多個模型一度發生錯誤率升高，Fable 5 亦受影響，事件於同日解決（[Anthropic Status](https://status.claude.com/incidents/tl8x3p1msff2)）。另有 HN 實測案例（Show HN，6 分）佐證解封後能力：作者在出口管制期間卡關三週的 Super Nintendo Python 移植專案，Fable 5 解封後 90 分鐘內找出根本問題並修復 23 個編譯器 bug（[fabian-kuebler.com](https://fabian-kuebler.com/posts/fable-python-snes/)）。

---

## 現況

Claude Fable 5 是 Anthropic 於 2026-06-09 發布的旗艦模型，為**史上首款向大眾開放的 Mythos 級模型**。Fable 5 與 Claude Mythos 5 共用相同的模型權重，差異在於 Fable 5 前置安全分類器——觸發時 fallback 至 Claude Opus 4.8（Anthropic 稱不到 5% 的 session 受影響）。核心定位：任務越複雜越長期，Fable 5 的優勢越明顯；在軟體工程、知識工作、視覺、科學研究等幾乎所有 benchmark 達到 SOTA。

**當前狀態（2026-07-01 起）**：出口管制（2026-06-13 至 2026-07-01，歷時 18 天）已正式解除，全球恢復存取。過渡期計費：Pro/Max/Team 方案 7/7 前維持每週配額 50%，7/7 後改依用量計費（定價近期公布）。Redeploy 同步導入「Defense in Depth」安全機制——更嚴格的資安/程式碼請求分類器，判定高風險時自動 fallback 至 Opus 4.8，首日已有誤判實測回報。管制事件完整經過見「出口管制：雙方立場」與「歷史記錄」。

| 指標 | 數值 |
|------|------|
| Input 定價 | $10 / 百萬 token |
| Output 定價 | $50 / 百萬 token |
| Context Window | 1,000,000 token |
| 最大 Output | 128,000 token |
| 免費期限 | 訂閱用戶至 2026-06-22 |

## 配額與計費過渡（至 7/7）

**規則：** Pro/Max/Team 方案 7/7 前維持每週配額 50%（含 Fable 5 用量），7/7 後改依用量計費（usage-based billing），定價另行公布；Enterprise 方案需聯繫帳戶主管（[Anthropic Blog](https://www.anthropic.com/news/redeploying-fable-5)，2026-07-01）。定價數字細節見 [[entities/pricing]]。

**配額重置時間因訂閱起始日而異**：Reddit 社群 07-03 釐清，Fable 5 額度重置規則並非統一週期，而是依各用戶訂閱方案的起始時間點各自輪轉（「Fable resets on Monday if you held a plan already」），並非所有人同一天重置（[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1umt5h5/fable_resets_on_monday_if_you_held_a_plan_already/)，2026-07-03）。

**消耗速度落差極大**：同期回報顯示個體使用量差異懸殊——有用戶 2 天內就燒完額度（[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1umtox4/i_burned_through_my_fable_5_usage_in_2_days_so_i/)，07-03），也有用戶反映額度限制大幅衝擊原本仰賴 Fable 處理的大型基因體分析工作流（[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1umtlqh/sad_about_fable_restrictions/)，07-03）。

**社群省額度策略：**

| 策略 | 說明 | 來源 |
|------|------|------|
| Fable 主力 + Opus 4.8 subagent 分工 | 7/7 到期前，將部分工作分派給 Opus 4.8 subagent 執行，把 Fable 5 額度保留給真正需要旗艦能力的任務，藉此最大化訂閱內 token 使用效率 | [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uli8as/maximizing_efficiency_with_fable_until_the_july/)，2026-07-02 |
| 5 小時額度重置自動接續 | 社群工具 CCLimitPing（Show HN）在 5 小時額度重置的瞬間自動恢復任務，避免人工盯盤 | [GitHub](https://github.com/wavever/CCLimitPing)，2026-07-03 |
| 用量即時監控 | LimitBar（macOS 選單列 App）即時顯示 Claude 使用額度，方便用戶主動調節任務排程 | [Gumroad](https://mikaweiss6.gumroad.com/l/limitbar)，2026-07-03 |

**與既有成本爭議的關係**：以上省額度行為與 07-01 起延燒的「Claude Code 成本暴漲」爭議（用戶回報 $50 原可用兩天、現在一小時燒完）相互呼應，反映訂閱制配額吃緊下使用者的行為調整；成本爭議完整脈絡見 [[topics/model-comparison]] Benchmark 對照的 token 成本並陳。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 多步驟複雜任務、長期 agentic 工作流、多天 PR 審查、安全漏洞分析 |
| 不適合 | 日常短問答（成本過高）、從事前沿 LLM 開發（護欄會靜默降級） |

> 詳細最新熱度見 [[feature-radar]]

## 使用指南

**快速上手（Claude Code）：**
```
claude --model claude-fable-5-20260609
```

**注意事項：**
- 6/22 後 Fable 5 移至消費制，Pro/Max 訂閱用戶須額外付費
- 從事前沿 LLM 開發（訓練 pipeline、推論研究）時，Fable 5 護欄會靜默降級輸出品質，不告知用戶（System Card 明文記載）
- 30 天資料保留政策適用於所有平台（含 AWS Bedrock），資料離開 AWS 安全邊界

## 核心功能

- **Mythos 架構公開版**：首次讓大眾使用 Mythos 等級推理能力
- **安全分類器護欄**：觸發時靜默 fallback 至 Opus 4.8，不拒絕請求（< 5% session）
- **1M context + 128K output**：適合處理整個 codebase 或長文件的任務
- **多模態**：軟體工程、視覺、科學研究均達 SOTA

## 爭議

- ✅ **靜默降級競爭 LLM 開發（已部分撤回）**：Fable 5 初版在偵測到前沿 LLM 開發工作時靜默降級，系統卡承認「These safeguards will not be visible to the user」；2026-06-11 Anthropic 道歉撤回，改為「可見防護」——觸發時用戶將明確得知
- ⚠️ **資安研究者護欄過激**：Fable 5 安全分類器過度敏感，連讀取資安部落格、分析 GitHub profile 等無害操作也被攔截；IBM X-Force 知名研究員 Valentina Palmiotti 公開批評（TechCrunch，HN score 512）
- ⚠️ **「Fix this code」三詞越獄機制公開（2026-06-22）**：dev.to 文章《The Fable 5 Jailbreak Was Three Words Long》揭露引發出口管制的具體越獄機制——「Fix this code」三個字即可繞過 Fable 5 安全控制（[dev.to](https://dev.to/peremptory/the-fable-5-jailbreak-was-three-words-long-457j)）；此事件直接呼應美國政府「護欄不可靠」的管制論點，亦是 Amazon 研究人員向白宮通報的漏洞細節首次公開
- ⚠️ **Jailbreak 已公開（早期 PoC）**：Pliny（@elder_plinius）與 0xSufi 已公開 Fable 5 護欄繞過 PoC，使用多步驟攻擊組合（請求拆解重組、敘事框架包裝、長 context 操作）
- ⚠️ **Microsoft 內部禁用**：Microsoft 法務/合規部門要求員工不得使用 Fable 5（Times of India、PYMNTS 報導，與 Fable 5 數據保留政策相關）
- ⚠️ **Fable 5 成本高昂**：$200/月 Max 用戶一次 code review 可消耗 45% 週配額；社群回報消耗量個體差異極大
- ⚠️ **30 天資料保留**：Bedrock 用戶數據強制離開 AWS 安全邊界，企業隱私顧慮
- ⚠️ **「失去靈魂」討論**：部分用戶認為 Fable 5 相比 Opus 4.6 更工具性、減少人本關懷深度
- ⚠️ **「Defense in Depth」分類器誤判（2026-07-02，新）**：redeploy 後新增的資安/程式碼請求分類器出現誤判案例——合法資安審查請求被攔截、化學問題被拒（後者待核實），攔截範圍可能超出原設計的 coding/cybersecurity 場景

## 出口管制：雙方立場

### 美國政府立場

**主張核心：** Fable 5 護欄可被繞過，進而存取 Mythos 5 的攻擊性網路安全能力，構成國家安全威脅。

| 論點 | 說明 |
|------|------|
| 護欄不可靠 | Commerce 部長 Lutnick 致函（Bloomberg 6/16 全文刊出）：Fable 5 護欄無法有效阻止取得 Mythos 的網路攻擊能力 |
| 中國情報威脅 | Semafor：中國關聯組織疑似存取 Mythos 5，為管制動機之一 |
| Amazon 直報 | AWS CEO Andy Jassy 向白宮通報安全研究結果（可透過提示詞生成可用攻擊資訊），成為直接觸發原因 |
| Dario 拒修 jailbreak | Trump 顧問 David Sacks：政府曾提前警告，但 Dario Amodei 拒絕修復也拒絕下架 |
| G7 不豁免 | 英國首相 Starmer 提出 carve-out 請求，Trump 政府明確拒絕，盟友一視同仁 |

**立場底線：** 出口管制架構問題，不限於 jailbreak 是否嚴重；Fable 5 本身即屬管制標的。

---

### Anthropic 立場

**主張核心：** 政府論點在技術上不成立；Anthropic 是在法律壓力下被迫合規，並非認同管制理由。

| 論點 | 說明 |
|------|------|
| 否認護欄失效 | 持續否認 Fable 5 可繞過護欄存取 Mythos 攻擊能力，認為政府主張技術上不成立 |
| jailbreak 不嚴重 | 官方回應 Sacks：被提前警告的 jailbreak「並不嚴重」，不構成下架理由 |
| 安全論述反噬 | TechCrunch 分析（Anthropic 自己也承認的弔詭）：Anthropic 對 Fable 5「太危險」的安全論述，成為政府援引的正當性依據 |
| 被迫全面下線 | 90 分鐘內關閉全球存取（含美國用戶），是為確保合規，不代表接受管制邏輯 |
| 積極協商 | 派遣多名高層赴華府，持續與 Commerce 部工作組談判；Axios 爆料主因涉及人際衝突（personality clash） |
| 商業損失 | DoD 已將三分之二 AI 工作量轉向競爭對手；TCS 企業合作受衝擊 |

**立場底線：** 管制是政治決定，不是技術必要性；Anthropic 正尋求解除或豁免，同時主張己方安全架構足夠可靠。

---

## 相關議題

- [[entities/mythos]] — Mythos 模型家族完整歷史
- [[entities/pricing]] — Fable 5 定價與訂閱方案變動
- [[topics/anthropic-government-policy]] — Anthropic vs 美國政府攻防完整時序
- [[topics/anthropic-business]] — Anthropic IPO 背景與商業策略
- [[topics/ai-agent-safety]] — Claude Code 供應鏈攻擊事件

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

## 歷史記錄

### 解禁後（2026-07-01 起）

#### 2026-07-06
**Anthropic 多模型錯誤率升高事件（同日解決）+ HN 實測佐證解封後能力**：
- **服務中斷**：Anthropic Status 通報多個模型一度出現錯誤率升高，Fable 5 也一併受影響，事件於同日解決，無需採取行動（[Anthropic Status](https://status.claude.com/incidents/tl8x3p1msff2)）；同期 AOL 彙整讀者對 Claude API 不穩定的抱怨與詢問（Response incomplete Claude / Is Claude down / Claude api error，07-05 22:24 UTC），屬服務穩定性面向，非出口管制或護欄爭議重演
- **Show HN 實測：Python 移植 Super Nintendo（6 分）**：作者以此專案作為 Fable 5 的實測案例——出口管制期間（6/13–7/1）專案卡關三週，Fable 5 解封後 90 分鐘內找出根本問題並修復 23 個編譯器 bug（[fabian-kuebler.com](https://fabian-kuebler.com/posts/fable-python-snes/)）；訊號雖弱（HN 6 分），但具體佐證解封後 Fable 5 在複雜除錯任務上的實際生產力

#### 2026-07-03
**配額重置規則釐清 + 消耗速度落差極大（社群策略彙整見「配額與計費過渡」子區塊）**：Reddit 社群釐清 Fable 5 額度重置時間依訂閱起始日而異，非統一週期（[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1umt5h5/fable_resets_on_monday_if_you_held_a_plan_already/)）；同日回報顯示個體消耗速度差異懸殊，2 天內燒完額度、大型基因體分析工作流受衝擊等案例並陳（[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1umtox4/i_burned_through_my_fable_5_usage_in_2_days_so_i/)、[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1umtlqh/sad_about_fable_restrictions/)）。

#### 2026-07-02
**Redeploy 技術細節：「Defense in Depth」分類器 + 早期實測褒貶不一**：
- **新安全機制**：Reddit 貼文整理 Fable 5 全球 redeploy（7/1）隨附的「Defense in Depth」措施——新增更嚴格的資安/程式碼請求分類器，一旦判定為高風險 coding/debug 請求，自動靜默 fallback 至 Opus 4.8 執行，不使用 Fable 5（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uliwhc/anthropic_just_redeployed_fable_5_globally_here/)）
- **負面實測：資安審查被誤判**：dev.to 作者實測用 Fable 5 執行合法資安審查工作，遭新分類器誤判為風險請求並攔截，作者形容「flagged my own request」（[dev.to](https://dev.to/tecnomanu/i-tried-fable-5-for-a-security-review-and-it-flagged-my-own-request-2pbn)）；此案例呼應 6/11 IBM X-Force 研究員 Valentina Palmiotti 曾批評的「護欄過激」問題，顯示該爭議在新分類器上仍未解決
- **範圍疑似擴大：化學提問也被拒**：另一則 Reddit 貼文顯示使用者詢問化學相關問題被 Fable 5 拒絕回答（「I guess not」），若屬實代表新分類器的攔截範圍可能不僅限於 coding/cybersecurity（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1ulh5he/can_you_ask_fable_anything_chemistry_related/)）；訊號來源單一，且原文未附截圖佐證，暫列「待核實」
- **與既有爭議的關係**：本次分類器行為為可見防護（用戶知道被 fallback），不同於 6/9 發布時「靜默降級不告知」已撤回的舊爭議；但誤判率與攔截範圍是否合理，仍待更多社群案例累積判斷

#### 2026-07-01
**出口管制正式解除，全球恢復存取**：
- **官方公告（[Anthropic Blog](https://www.anthropic.com/news/redeploying-fable-5)）**：美國出口管制解除，Fable 5 與 Mythos 5 於 2026-07-01 起向全球用戶恢復存取。過渡期計費：Pro/Max/Team 方案 7/7 前維持每週配額 50%；7/7 後改依用量計費，定價近期公布
- **Anthropic-美國政府協議**：Anthropic 承諾主動偵測安全風險、配合標準協議、通報惡意活動；此協議為 Fable 5 全球解禁的交換條件，標誌管制事件正式落幕
- **管制事件歷時 18 天**（2026-06-13 至 2026-07-01）

### 出口管制期（2026-06-13 至 06-30）

#### 2026-06-29
**美國政府正式許可恢復 Mythos 存取 + Fable 5 可能本週回歸（待核實）**：
- **政府正式許可（qz.com）**：Anthropic 獲得美國政府許可，可向特定信任合作夥伴恢復 Mythos 存取，Fable 5 全面回歸在望（[qz.com](https://qz.com/anthropic-mythos-5-clearance-trusted-partners-commerce-062926)）；這是繼 6/27 Mythos 5 部分解禁後，政府立場進一步鬆動的具體信號
- **Axios：Fable 5 可能本週回歸（待核實）**（HN score 8）：Axios 報導 Fable 5「on track to return soon, possibly this week」，Washington 軟化立場（[Axios](https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon)）；HN score 8 訊號偏弱，「possibly this week」為消息人士說法，尚無官方確認
- **Washington 軟化立場（Yellow.com）**：Google News 報導確認談判進展，與 qz.com / Axios 方向一致（[Yellow.com](https://yellow.com/news/claude-fable-5-return)）
- **社群回顧：音樂影片展示**（Reddit，score 不詳）：用戶分享在 Fable 5 下架前使用其製作音樂影片的體驗，展示視頻編輯與創意能力，說明即使在管制期間社群仍持續記錄 Fable 5 的多模態使用案例（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uipova/)）
- **工程師實測：新版 Claude 燒更多 token 但每任務成本更低**（HN score 5）：signoz.io 工程師儀器化實測顯示，新版 Claude 模型 token 使用量顯著高於舊版，但每個成功解決任務的實際成本反而下降；分析強調評測指標需同時考量 token 用量與任務完成率，而非僅看成本或速度（[signoz.io](https://signoz.io/blog/claude-code-model-comparison/)）；HN score 5 訊號弱，結論「待驗證」

#### 2026-06-28
**Fable 5 協議接近完成（待核實）+ 競品效應分析**：
- **Axios 報導 Fable 5 on track（待核實）**（HN score 4）：Axios 報導 Fable 5 正走向全面回歸一般市場，美方協議接近完成；TechCrunch 同步補充「Fable 5 on track to return soon」（[Axios](https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon)）。訊號弱（HN score 4），「接近完成」不等於已批准，尚待官方確認
- **HN 社群反應：競品急追佐證封鎖無效**：HN 評論普遍認為 Tulongfeng / Fugu 等競品急追 Mythos / Fable 5 的聲明，反而對 Anthropic 有利——強化「封鎖只讓競爭對手有時間填補市場」論點，媒體密集報導同時提升 Anthropic 品牌效應

#### 2026-06-27
**接近批准 Fable 5 重新上線（待核實）+ Mythos 5 先行部分解禁**：
- **Fable 5 接近協議（待核實）**：Reuters / Axios 報導美方接近批准 Fable 5 重新上線，尚未獲得 Anthropic 或商務部官方確認（[Reuters](https://www.reuters.com/business/us-close-allowing-anthropic-restore-fable-5-model-axios-reports-2026-06-27/)）；訊號強度：兩家主流媒體同步報導，但「接近」不等於已批准，應持保留態度
- **Mythos 5 先行部分解禁**：同日，商務部長 Howard Lutnick 在致 Anthropic 聯合創辦人、chief compute officer Tom Brown 的信中確認，Mythos 5 已獲批向 100+ 美國受信任機構（企業 + 聯邦機構）有限釋出（Semafor、CNBC）；Fable 5 與 Mythos 5 的解禁為獨立決定，不可相互推論

#### 2026-06-24
**NSA 失去 Fable 存取權 + Legion 提告 + LessWrong 預測 7/9 解封**：
- **NSA 失去存取權**：NYT 報導，NSA 因與 Anthropic 的出口管制爭議失去 Claude Fable 模型的存取權（[NYT](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html)）；此為首次有具名情報機構因管制爭議而被正式切斷存取的報導，直接強化政府對 Anthropic 的施壓態勢
- **Legion 法律科技新創提告**：Reuters 報導，法律科技新創 Legion 正式對美國政府提告，主張出口管制令違法限制外界使用 Fable（[Reuters](https://www.reuters.com/legal/litigation/legal-tech-firm-sues-us-over-order-limiting-foreign-access-top-tier-anthropic-2026-06-23/)）；是繼 Politico 法律分析後，首件具名企業以訴訟形式挑戰出口管制的案例
- **LessWrong 預測分析**：LessWrong 發布詳細世界模型分析，將 Fable 重新上線的預期時間修正至 **7 月 9 日**（[LessWrong](https://www.lesswrong.com/posts/zhRe3tdBpsZbGCdDK/world-modeling-the-us-vs-anthropic-standoff-on-claude-fable)）；分析涵蓋雙方談判動態、法律障礙與市場壓力因素

#### 2026-06-23
**Five Eyes 聯合聲明 + Zhipu GLM-5.2 接觸被封鎖用戶 + HN 社群問「Fable 回來了嗎？」**：
- **Five Eyes 情報聯盟聲明**：英美澳加紐五眼情報機構發表聯合聲明，警告「足以顛覆政府的 AI 模型距今僅數月」，Fable 5 等前沿模型帶來的網路安全威脅首次被五眼機構聯合點名（[The Guardian](https://www.theguardian.com/technology/2026/jun/22/anthropic-claude-fable-ai-model-artificial-intelligence-national-security)，2026-06-22）
- **Zhipu GLM-5.2 趁機接觸被封鎖用戶**：Anthropic 出口管制後，中國 AI 公司 Zhipu 的 GLM-5.2 主動接觸遭 Fable 5 封鎖的用戶群，試圖填補存取空白（[SCMP](https://www.scmp.com/tech/article/3358067/how-anthropics-fable-5-shutdown-could-help-chinas-zhipu-glm-52-gain-ground)）；此為繼 6/22 Zhipu 競爭聲明後，中方市場動作的具體落地
- **Fortune 歐洲高管警告**：Fortune 報導歐洲企業高管對 Fable 5 出口管制深感焦慮，原話：「This is the least crazy AI is ever going to be」，暗示前沿 AI 能力擴張不會停止，監管只是拖延
- **HN：「Fable 回來了嗎？」（score 4）**：有使用者在 Hacker News 發帖回報，Claude Code 在工作流中啟動了一個 Fable 5 subagent 且未報錯，且該 subagent 自我識別為 Fable（[HN](https://news.ycombinator.com/item?id=48629948)）；訊號微弱（score 4），尚無法確認是部分解禁、快取問題或邊緣豁免案例

#### 2026-06-22
**「Fix this code」三詞越獄機制公開 + Zhipu 聲稱 2026 年追上 Fable 5**：
- **三詞越獄細節首次公開**：dev.to 文章揭露引發出口管制的 Fable 5 越獄機制——「Fix this code」三個字即可繞過安全控制。這是美國政府「護欄不可靠」論點與 Amazon 研究人員向白宮通報漏洞的具體指向，是管制事件核心技術事實的首次公開說明（[dev.to](https://dev.to/peremptory/the-fable-5-jailbreak-was-three-words-long-457j)）
- **Zhipu 競爭聲明**：中國 AI 公司 Zhipu 創辦人向馬斯克聲稱，其 GLM-5.2 將在 2026 年追上 Anthropic Fable 5 的能力水平（South China Morning Post，[SCMP](https://www.scmp.com/tech/article/3357926/china-ai-ready-match-anthropics-fable-5-musk-zhipus-tang-clash-over-glm-52-rise)）；是中美 AI 競爭背景下，Fable 5 作為中國追趕目標首次被具名企業公開宣示的案例

#### 2026-06-20
**全球媒體反應升溫 + 境外付費帳號遭停用**：
- **多國主流媒體跟進報導**：Al Jazeera（出口禁令加劇盟友緊張）、DW.com（全球關切美國限制 Anthropic AI 存取）、SiliconANGLE（「Trump 削弱 Anthropic」）、dev.to（「美國政府強制關閉 Fable 5 和 Mythos 5：第一個 AI Kill-Switch」）同步報導，凸顯管制事件在美國以外持續發酵
- **境外付費用戶帳號停用**：有確認案例顯示非美國 Claude 付費訂閱用戶在 Fable 5 / Mythos 管制期間帳號遭停用，進一步衝擊 Anthropic 境外用戶可及性
- **解禁預期持續**：承接昨日 Ciauri「數日內恢復」聲明，待 Commerce 部正式解封通知

#### 2026-06-19
**解禁近況 + Wired 深度調查 + 早期用戶豁免**：
- **Wired 深度調查（HN score 110）** 確認 SK Telecom 中國關聯是出口管制的根本動機：Anthropic 先前授予 SK Telecom 對 Mythos（非 Fable 5）的存取權，美方對 SK Telecom 中國關聯的疑慮觸發審查；此後 Amazon 研究人員向白宮揭露 Fable 5 的越獄漏洞，兩件事疊加加速了管制決定，澄清「jailbreak 是唯一原因」的既有說法
- **Ciauri 首爾記者會**：Anthropic 國際總監 Chris Ciauri 與 Anthropic Korea 代表 Choi Ki-young 在首爾 Conrad 飯店召開記者會，聲明「非常有信心模型將在數日內恢復可用」
- **Bloomberg**：部分 Mythos 早期用戶在美國政府指令後仍保有存取權（早期用戶豁免）
- **印度 AI 主權討論**：TechCrunch 報導，Fable 5 / Mythos 停用引發印度 AI 主權辯論，尤其 Anthropic 與 TCS 企業合作宣布同日發生停用事件，凸顯依賴美國技術的地緣政治風險
- **程式能力評測**：Towards Data Science 發布 Fable 5（Mythos）程式設計能力評測

#### 2026-06-18
**「數日內解禁」——SK Telecom / China 關聯首次曝光**：Anthropic 國際業務總監 Chris Ciauri 在首爾記者會表示「非常有信心模型將在數日內恢復可用」。同日 Wired 獨家報導揭露出口管制的根本起因：美國政府關切 SK Telecom 與中國的關聯，在 Anthropic 授予 SK Telecom 存取 Mythos（非 Fable 5）後啟動審查；Amazon 研究人員在 Fable 5 中發現的 jailbreak 進一步加速了管制決定。Politico 分析出口管制可能違法，國會議員要求政府說明。Anthropic 已向商務部長 Lutnick 提交解封提案（New York Post）。摩根大通香港分行被迫切斷 Anthropic 存取（Financial Times），是出口管制對具名頂尖企業的首批直接衝擊案例。

#### 2026-06-17
**G7 峰會無豁免，談判再度破裂**：Wired 報導週一 Commerce 部工作組會談結束，出口管制仍未解除。政府持續主張 Fable 5 護欄可被繞過以存取 Mythos 的攻擊性網路安全能力；Anthropic 再次否認此論點屬實。G7 國家（包括英國首相 Starmer 的「carve-out」請求）一概遭拒，Trump 政府明確表示 G7 盟友也不在豁免範圍內（NY Post、Euronews、Politico EU）。TechCrunch 報導：這次最新爭端諷刺地可能對 Anthropic 的銷售有利——五月 Anthropic 企業市佔首度超越 OpenAI（Ramp 數據），650 億美元融資、IPO 申請均在管制前完成。The Guardian 評論：Fable 5 事件是「AI 潘朵拉盒已開」的象徵，出口管制無法真正遏止能力擴散，需要全球集體行動。

#### 2026-06-16
**爭議焦點：Dario 被控拒絕修復 jailbreak + 用戶依賴感爆發**：Trump 顧問 David Sacks 在 X 上表示，美國政府曾提前警告 Anthropic Fable 5 被 jailbreak，但 Dario Amodei 拒絕修復也拒絕下架；Anthropic 回應稱該 jailbreak「並不嚴重」。TechCrunch 深度報導分析：此次出口管制從一開始就與 jailbreak 無關，而是更廣泛的出口管制架構問題（Dario 個人定義是否屬「外籍人士」）。白宮本週一協商已啟動。《The Atlantic》評論 Trump 政府持續升溫對 Anthropic 的戰爭，稱美國可能因此在 AI 競賽中落後。Reddit 大量用戶反映 Fable 5 下線後「無法回頭用舊模型」，分享對其他模型效果的落差感受。AI 價格戰分析指出此事件對 Anthropic 與 OpenAI 的商業壓力同步升溫。

#### 2026-06-15
**Axios 爆料「人際衝突」為主因，Stratechery 長文點名安全論述是雙面刃。**
**協商持續推進 + 媒體深挖「個性衝突」**：Axios 報導內部消息稱 Anthropic 員工以「They screwed us」描述與白宮的關係，爆料主因是人際衝突（personality clash）而非純粹政策分歧。WSJ 同日報導 Anthropic 派遣多名高層員工赴華府與白宮官員緊急協商，試圖解除出口管制。Stratechery 長文分析（Ben Thompson，HN 128 分）：Fable 在親身體驗中「留下極深印象」，同時犀利指出 Anthropic 的安全論述是把雙面刃——使政府有現成正當性強制干預。加拿大總理 Carney 公開警告此事件顯示「過度依賴大型 AI 模型」的地緣政治風險。《經濟學人》評 Trump 的封鎖決策「反覆無常且混亂」。開發者社群出現非技術人員（PMM）展示 60 天使用 Claude Code 獨立完成多個商業專案、收入 $4K 的案例，引發對「非技術角色護城河消失」的廣泛討論。

#### 2026-06-14
**Amazon Jassy 直報白宮成為管制直接觸發原因，EU 與印度 AI 主權爭議同步浮現。**
**出口管制事件後續：更多細節浮現 + 國際影響擴大**：Axios 揭露 Anthropic 僅有 90 分鐘執行撤架命令（下午 5:21pm ET 收到指令）。The Verge / WSJ 報導：Amazon 安全研究顯示 Fable 5 可透過一系列提示詞生成可用於網路攻擊的資訊，Amazon CEO Andy Jassy 直接向白宮官員通報，成為管制指令的直接觸發原因。Semafor 報導：白宮動機之一是中國關聯組織疑似存取 Mythos 5 的情報。TechCrunch 報導：Politico 分析此事件暴露歐盟 AI 主權弱點，EU 執委會宣布正在評估實際影響；印度科技界（Anthropic 第二大市場）重燃 AI 自主辯論，Anthropic 剛宣布與 TCS 的企業合作隨即受衝擊。社群層面：用戶抱怨 Opus 4.6 在書籍編輯任務上與 Fable 5 差距明顯，尋求替代 prompt 策略。美國戰爭部長 Hegseth 公開就此發表聲明但無法提供具體理由，社群批評「最無能政府」。Forbes 探討 Anthropic 是否需要提供 Fable 5 退款。

#### 2026-06-13
**Trump 政府下令停用，Anthropic 90 分鐘內對全體用戶關閉存取；Anthropic 安全論述反成政府援引依據。**
**美國政府出口管制指令**：Trump 政府以「國家安全授權」發布出口管制指令，要求 Anthropic 停用 Fable 5 與 Mythos 5 對所有外籍人士的存取，包含美國境內外籍員工。Anthropic 於下午 5:21pm ET 收到指令，為確保合規對全體用戶停用兩款模型——即使這代表美國用戶也無法繼續使用。指令未提供具體國家安全顧慮說明。TechCrunch 分析：Anthropic 對 Fable 5「太危險」的安全論述，反而成為政府援引的理由，是「AI 安全敘事的意外後果」。社群熱議 Anthropic 安全立場與政府干預之間的弔詭關係（Reddit 用戶整理時序：Anthropic 主張自己有資格決定誰能用最強模型，政府隨即接管了這個決定）。Fable 5 在下線前的 72 小時窗口期，開發者展示了大量編碼成果：單次對話生成 2,319 行遊戲、10 小時打造多人棋藝平台、Go decimal 函式庫效能超越市場最快工具 35%。

### 管制前（發布初期）

#### 2026-06-12
Jailbreak 持續爭議：有人再次聲稱破解成功，Anthropic 官方出面駁斥該說法。社群測試數據顯示 Fable 5 在對話中使用「honest」一詞比率（1.79%）為各代模型最高，引發對模型行為與誠實性設計的討論。Anthropic 在上市 48 小時內撤回了 Fable 5 的研究存取限制（前一日政策）。917 個 coding-agent 場景測試：Fable 5 以 0.9 分之差略勝 Opus 4.8，但 token 消耗約 2 倍（Reddit r/ClaudeAI）。

#### 2026-06-11
政策撤回事件：Anthropic 就隱性 LLM 研究限制政策道歉，承認「做了錯誤的取捨」，改為可見防護措施（Wired 報導）。多個 Jailbreak PoC 公開流傳（Pliny、0xSufi）。資安研究者護欄過激爭議持續延燒（HN 512 分）。Microsoft 內部律師建議禁用（Times of India、PYMNTS）。OpenAI 考慮降價應對 Anthropic 競爭（WSJ/CNBC）。TCS 宣布與 Anthropic 建立 Global Premier Partnership，5 萬員工使用 Claude。Claude Corps 公益計畫發布。

#### 2026-06-10
發布後第一天社群討論爆發：靜默降級爭議、30 天資料保留爭議、供應鏈攻擊威脅升高、Microsoft AI CEO 批評 Anthropic 意識論述、多個工具社群跟進（Lanes v0.43.0 加入 Fable 5 支援）。

#### 2026-06-09
正式發布。HN score 2,448，近 2,000 評論。6/22 前含括於訂閱方案。
