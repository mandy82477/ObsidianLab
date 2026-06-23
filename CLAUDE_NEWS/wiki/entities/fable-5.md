# Claude Fable 5

**類型：** model
**狀態：** active（正式發布；Fable 5 / Mythos 5 因美國政府出口管制指令暫停全球存取）
**領域：** 🤖 模型
**首次出現：** 2026-06-09
**最後更新：** 2026-06-23
**最後新聞更新：** 2026-06-23

> **最新管制進展**（2026-06-23）
> Five Eyes 情報聯盟聯合聲明首度點名 Fable 5，同日中國 Zhipu GLM-5.2 主動接觸被封鎖用戶群填補市場空白；Claude Code 啟動 Fable 5 subagent 的個案回報訊號弱，尚待確認。

---

## 現況

Claude Fable 5 是 Anthropic 於 2026-06-09 發布的旗艦模型，為**史上首款向大眾開放的 Mythos 級模型**。Fable 5 與 Claude Mythos 5 共用相同的模型權重，差異在於 Fable 5 前置安全分類器——觸發時靜默 fallback 至 Claude Opus 4.8（Anthropic 稱不到 5% 的 session 受影響）。

**2026-06-13 重大事件**：美國政府以「國家安全出口管制」為由，下令 Anthropic 對所有外籍人士（含境外及境內外籍員工）停用 Fable 5 與 Mythos 5。Anthropic 於當日 5:21pm ET 收到指令，為確保合規對全體用戶停用兩款模型，其他模型不受影響。路透社、NYT、BBC、TechCrunch、WIRED 等主流媒體全面報導。

**2026-06-18–19 解禁進展**：Wired 深度調查（HN score 110）確認出口管制根本動機為 SK Telecom 中國關聯（Anthropic 先前授予 SK Telecom Mythos 存取權），加上 Amazon 研究人員向白宮舉報 Fable 5 越獄漏洞，兩件事疊加加速管制決定。Anthropic 國際總監 Chris Ciauri 在首爾記者會聲明「數日內恢復」，Bloomberg 另報導部分早期用戶仍保有存取權。見 [[entities/mythos]]。

**2026-06-23 最新**：Five Eyes 情報聯盟（英美澳加紐）發表聯合聲明點名前沿 AI 模型網路安全威脅，Fable 5 在出口管制脈絡下首度被五眼機構聯合提及。中國 Zhipu GLM-5.2 主動接觸被封鎖用戶群，填補市場空白。HN 有使用者回報 Claude Code 啟動 Fable 5 subagent 且自我識別為 Fable（訊號弱，score 4，尚待確認）。

**核心定位**：任務越複雜越長期，Fable 5 的優勢越明顯。在軟體工程、知識工作、視覺、科學研究等幾乎所有 benchmark 達到 SOTA。

| 指標 | 數值 |
|------|------|
| Input 定價 | $10 / 百萬 token |
| Output 定價 | $50 / 百萬 token |
| Context Window | 1,000,000 token |
| 最大 Output | 128,000 token |
| 免費期限 | 訂閱用戶至 2026-06-22 |

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

### 2026-06-23
**Five Eyes 聯合聲明 + Zhipu GLM-5.2 接觸被封鎖用戶 + HN 社群問「Fable 回來了嗎？」**：
- **Five Eyes 情報聯盟聲明**：英美澳加紐五眼情報機構發表聯合聲明，警告「足以顛覆政府的 AI 模型距今僅數月」，Fable 5 等前沿模型帶來的網路安全威脅首次被五眼機構聯合點名（[The Guardian](https://www.theguardian.com/technology/2026/jun/22/anthropic-claude-fable-ai-model-artificial-intelligence-national-security)，2026-06-22）
- **Zhipu GLM-5.2 趁機接觸被封鎖用戶**：Anthropic 出口管制後，中國 AI 公司 Zhipu 的 GLM-5.2 主動接觸遭 Fable 5 封鎖的用戶群，試圖填補存取空白（[SCMP](https://www.scmp.com/tech/article/3358067/how-anthropics-fable-5-shutdown-could-help-chinas-zhipu-glm-52-gain-ground)）；此為繼 6/22 Zhipu 競爭聲明後，中方市場動作的具體落地
- **Fortune 歐洲高管警告**：Fortune 報導歐洲企業高管對 Fable 5 出口管制深感焦慮，原話：「This is the least crazy AI is ever going to be」，暗示前沿 AI 能力擴張不會停止，監管只是拖延
- **HN：「Fable 回來了嗎？」（score 4）**：有使用者在 Hacker News 發帖回報，Claude Code 在工作流中啟動了一個 Fable 5 subagent 且未報錯，且該 subagent 自我識別為 Fable（[HN](https://news.ycombinator.com/item?id=48629948)）；訊號微弱（score 4），尚無法確認是部分解禁、快取問題或邊緣豁免案例

### 2026-06-22
**「Fix this code」三詞越獄機制公開 + Zhipu 聲稱 2026 年追上 Fable 5**：
- **三詞越獄細節首次公開**：dev.to 文章揭露引發出口管制的 Fable 5 越獄機制——「Fix this code」三個字即可繞過安全控制。這是美國政府「護欄不可靠」論點與 Amazon 研究人員向白宮通報漏洞的具體指向，是管制事件核心技術事實的首次公開說明（[dev.to](https://dev.to/peremptory/the-fable-5-jailbreak-was-three-words-long-457j)）
- **Zhipu 競爭聲明**：中國 AI 公司 Zhipu 創辦人向馬斯克聲稱，其 GLM-5.2 將在 2026 年追上 Anthropic Fable 5 的能力水平（South China Morning Post，[SCMP](https://www.scmp.com/tech/article/3357926/china-ai-ready-match-anthropics-fable-5-musk-zhipus-tang-clash-over-glm-52-rise)）；是中美 AI 競爭背景下，Fable 5 作為中國追趕目標首次被具名企業公開宣示的案例

### 2026-06-20
**全球媒體反應升溫 + 境外付費帳號遭停用**：
- **多國主流媒體跟進報導**：Al Jazeera（出口禁令加劇盟友緊張）、DW.com（全球關切美國限制 Anthropic AI 存取）、SiliconANGLE（「Trump 削弱 Anthropic」）、dev.to（「美國政府強制關閉 Fable 5 和 Mythos 5：第一個 AI Kill-Switch」）同步報導，凸顯管制事件在美國以外持續發酵
- **境外付費用戶帳號停用**：有確認案例顯示非美國 Claude 付費訂閱用戶在 Fable 5 / Mythos 管制期間帳號遭停用，進一步衝擊 Anthropic 境外用戶可及性
- **解禁預期持續**：承接昨日 Ciauri「數日內恢復」聲明，待 Commerce 部正式解封通知

### 2026-06-19
**解禁近況 + Wired 深度調查 + 早期用戶豁免**：
- **Wired 深度調查（HN score 110）** 確認 SK Telecom 中國關聯是出口管制的根本動機：Anthropic 先前授予 SK Telecom 對 Mythos（非 Fable 5）的存取權，美方對 SK Telecom 中國關聯的疑慮觸發審查；此後 Amazon 研究人員向白宮揭露 Fable 5 的越獄漏洞，兩件事疊加加速了管制決定，澄清「jailbreak 是唯一原因」的既有說法
- **Ciauri 首爾記者會**：Anthropic 國際總監 Chris Ciauri 與 Anthropic Korea 代表 Choi Ki-young 在首爾 Conrad 飯店召開記者會，聲明「非常有信心模型將在數日內恢復可用」
- **Bloomberg**：部分 Mythos 早期用戶在美國政府指令後仍保有存取權（早期用戶豁免）
- **印度 AI 主權討論**：TechCrunch 報導，Fable 5 / Mythos 停用引發印度 AI 主權辯論，尤其 Anthropic 與 TCS 企業合作宣布同日發生停用事件，凸顯依賴美國技術的地緣政治風險
- **程式能力評測**：Towards Data Science 發布 Fable 5（Mythos）程式設計能力評測

### 2026-06-18
**「數日內解禁」——SK Telecom / China 關聯首次曝光**：Anthropic 國際業務總監 Chris Ciauri 在首爾記者會表示「非常有信心模型將在數日內恢復可用」。同日 Wired 獨家報導揭露出口管制的根本起因：美國政府關切 SK Telecom 與中國的關聯，在 Anthropic 授予 SK Telecom 存取 Mythos（非 Fable 5）後啟動審查；Amazon 研究人員在 Fable 5 中發現的 jailbreak 進一步加速了管制決定。Politico 分析出口管制可能違法，國會議員要求政府說明。Anthropic 已向商務部長 Lutnick 提交解封提案（New York Post）。摩根大通香港分行被迫切斷 Anthropic 存取（Financial Times），是出口管制對具名頂尖企業的首批直接衝擊案例。

### 2026-06-17
**G7 峰會無豁免，談判再度破裂**：Wired 報導週一 Commerce 部工作組會談結束，出口管制仍未解除。政府持續主張 Fable 5 護欄可被繞過以存取 Mythos 的攻擊性網路安全能力；Anthropic 再次否認此論點屬實。G7 國家（包括英國首相 Starmer 的「carve-out」請求）一概遭拒，Trump 政府明確表示 G7 盟友也不在豁免範圍內（NY Post、Euronews、Politico EU）。TechCrunch 報導：這次最新爭端諷刺地可能對 Anthropic 的銷售有利——五月 Anthropic 企業市佔首度超越 OpenAI（Ramp 數據），650 億美元融資、IPO 申請均在管制前完成。The Guardian 評論：Fable 5 事件是「AI 潘朵拉盒已開」的象徵，出口管制無法真正遏止能力擴散，需要全球集體行動。

### 2026-06-16
**爭議焦點：Dario 被控拒絕修復 jailbreak + 用戶依賴感爆發**：Trump 顧問 David Sacks 在 X 上表示，美國政府曾提前警告 Anthropic Fable 5 被 jailbreak，但 Dario Amodei 拒絕修復也拒絕下架；Anthropic 回應稱該 jailbreak「並不嚴重」。TechCrunch 深度報導分析：此次出口管制從一開始就與 jailbreak 無關，而是更廣泛的出口管制架構問題（Dario 個人定義是否屬「外籍人士」）。白宮本週一協商已啟動。《The Atlantic》評論 Trump 政府持續升溫對 Anthropic 的戰爭，稱美國可能因此在 AI 競賽中落後。Reddit 大量用戶反映 Fable 5 下線後「無法回頭用舊模型」，分享對其他模型效果的落差感受。AI 價格戰分析指出此事件對 Anthropic 與 OpenAI 的商業壓力同步升溫。

### 2026-06-15
**Axios 爆料「人際衝突」為主因，Stratechery 長文點名安全論述是雙面刃。**
**協商持續推進 + 媒體深挖「個性衝突」**：Axios 報導內部消息稱 Anthropic 員工以「They screwed us」描述與白宮的關係，爆料主因是人際衝突（personality clash）而非純粹政策分歧。WSJ 同日報導 Anthropic 派遣多名高層員工赴華府與白宮官員緊急協商，試圖解除出口管制。Stratechery 長文分析（Ben Thompson，HN 128 分）：Fable 在親身體驗中「留下極深印象」，同時犀利指出 Anthropic 的安全論述是把雙面刃——使政府有現成正當性強制干預。加拿大總理 Carney 公開警告此事件顯示「過度依賴大型 AI 模型」的地緣政治風險。《經濟學人》評 Trump 的封鎖決策「反覆無常且混亂」。開發者社群出現非技術人員（PMM）展示 60 天使用 Claude Code 獨立完成多個商業專案、收入 $4K 的案例，引發對「非技術角色護城河消失」的廣泛討論。

### 2026-06-14
**Amazon Jassy 直報白宮成為管制直接觸發原因，EU 與印度 AI 主權爭議同步浮現。**
**出口管制事件後續：更多細節浮現 + 國際影響擴大**：Axios 揭露 Anthropic 僅有 90 分鐘執行撤架命令（下午 5:21pm ET 收到指令）。The Verge / WSJ 報導：Amazon 安全研究顯示 Fable 5 可透過一系列提示詞生成可用於網路攻擊的資訊，Amazon CEO Andy Jassy 直接向白宮官員通報，成為管制指令的直接觸發原因。Semafor 報導：白宮動機之一是中國關聯組織疑似存取 Mythos 5 的情報。TechCrunch 報導：Politico 分析此事件暴露歐盟 AI 主權弱點，EU 執委會宣布正在評估實際影響；印度科技界（Anthropic 第二大市場）重燃 AI 自主辯論，Anthropic 剛宣布與 TCS 的企業合作隨即受衝擊。社群層面：用戶抱怨 Opus 4.6 在書籍編輯任務上與 Fable 5 差距明顯，尋求替代 prompt 策略。美國戰爭部長 Hegseth 公開就此發表聲明但無法提供具體理由，社群批評「最無能政府」。Forbes 探討 Anthropic 是否需要提供 Fable 5 退款。

### 2026-06-13
**Trump 政府下令停用，Anthropic 90 分鐘內對全體用戶關閉存取；Anthropic 安全論述反成政府援引依據。**
**美國政府出口管制指令**：Trump 政府以「國家安全授權」發布出口管制指令，要求 Anthropic 停用 Fable 5 與 Mythos 5 對所有外籍人士的存取，包含美國境內外籍員工。Anthropic 於下午 5:21pm ET 收到指令，為確保合規對全體用戶停用兩款模型——即使這代表美國用戶也無法繼續使用。指令未提供具體國家安全顧慮說明。TechCrunch 分析：Anthropic 對 Fable 5「太危險」的安全論述，反而成為政府援引的理由，是「AI 安全敘事的意外後果」。社群熱議 Anthropic 安全立場與政府干預之間的弔詭關係（Reddit 用戶整理時序：Anthropic 主張自己有資格決定誰能用最強模型，政府隨即接管了這個決定）。Fable 5 在下線前的 72 小時窗口期，開發者展示了大量編碼成果：單次對話生成 2,319 行遊戲、10 小時打造多人棋藝平台、Go decimal 函式庫效能超越市場最快工具 35%。

### 2026-06-12
Jailbreak 持續爭議：有人再次聲稱破解成功，Anthropic 官方出面駁斥該說法。社群測試數據顯示 Fable 5 在對話中使用「honest」一詞比率（1.79%）為各代模型最高，引發對模型行為與誠實性設計的討論。Anthropic 在上市 48 小時內撤回了 Fable 5 的研究存取限制（前一日政策）。917 個 coding-agent 場景測試：Fable 5 以 0.9 分之差略勝 Opus 4.8，但 token 消耗約 2 倍（Reddit r/ClaudeAI）。

### 2026-06-11
政策撤回事件：Anthropic 就隱性 LLM 研究限制政策道歉，承認「做了錯誤的取捨」，改為可見防護措施（Wired 報導）。多個 Jailbreak PoC 公開流傳（Pliny、0xSufi）。資安研究者護欄過激爭議持續延燒（HN 512 分）。Microsoft 內部律師建議禁用（Times of India、PYMNTS）。OpenAI 考慮降價應對 Anthropic 競爭（WSJ/CNBC）。TCS 宣布與 Anthropic 建立 Global Premier Partnership，5 萬員工使用 Claude。Claude Corps 公益計畫發布。

### 2026-06-10
發布後第一天社群討論爆發：靜默降級爭議、30 天資料保留爭議、供應鏈攻擊威脅升高、Microsoft AI CEO 批評 Anthropic 意識論述、多個工具社群跟進（Lanes v0.43.0 加入 Fable 5 支援）。

### 2026-06-09
正式發布。HN score 2,448，近 2,000 評論。6/22 前含括於訂閱方案。
