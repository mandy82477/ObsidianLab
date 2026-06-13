# Anthropic 政府與軍事政策

**狀態：** monitoring
**領域：** 🏛️ 政策/安全
**開始日期：** 2026-05-01
**最後更新：** 2026-06-13

---

## 摘要

2026-05-01，Anthropic 因堅持在軍事用途中納入安全護欄，被排除在美國國防部與 7 家 AI 公司的機密網路部署協議之外。此事件標誌著 Anthropic 的安全優先立場首次與聯邦政府大規模部署需求發生直接衝突，並引發白宮重啟談判。

---

## 技術彙整

### 五角大廈排除 Anthropic 事件

- **協議範圍**：美國國防部與 SpaceX、OpenAI、Google、Microsoft、NVIDIA、AWS、Reflection 共 7 家公司簽署 AI 機密網路部署協議
- **排除原因**：Anthropic 堅持軍事用途須納入**安全護欄（safety guardrails）**，雙方對軍事應用的安全管控存在根本分歧
- **後續進展**：白宮在 Anthropic 宣布多項技術突破後已重啟談判，顯示技術能力仍是政府合作的核心籌碼
- **關聯事件**：Mythos 的高能力與 Anthropic 對安全護欄的堅持，可能是影響談判框架的背景因素；見 [[entities/mythos]]

### 梵蒂岡教宗封論：Anthropic 的倫理對話路線（2026-05-26）

教宗良十四世（Pope Leo XIV）發布首份 AI 主題封論《Magnifica Humanitas》，Anthropic 共同創辦人 **[[entities/chris-olah|Chris Olah]]** 受邀出席梵蒂岡揭幕演講，成為唯一受邀的 AI 公司代表：

- 封論立場：呼籲對 AI 進行嚴格監管；批判「權力文化」（culture of power）驅動的 AI 競賽；要求 AI 開發者以公共利益為先而非以利潤為先
- Chris Olah 演講主旨：AI 發展必須由大科技公司以外的力量引導；強調透明度與廣泛社會對話
- 媒體覆蓋：AP News、Reuters、NYT、WashPost、NDTV、Fast Company 等主流媒體大篇幅報導（HN score 81）
- 政策意涵：Anthropic 明確選擇梵蒂岡路線（國際倫理框架）而非白宮路線（政府合約）；Anthropic 「安全優先、倫理優先」的品牌定位在全球宗教社群中得到背書

此事件是繼五角大廈排除事件後，Anthropic 在「政府合作路線 vs 倫理對話路線」上選擇的另一次明確訊號。

### Anthropic 安全立場的政策含義

- 此事件是繼白宮反對擴大 Mythos 存取（2026-04-29）之後，Anthropic 與聯邦政府的第二次重大政策摩擦
- 兩次事件顯示：Anthropic 的安全優先立場同時引發「政府想要更多存取但被拒」（Mythos）與「政府合作因護欄要求而破局」（五角大廈）兩種相反方向的張力
- 相比之下，OpenAI、Google、Microsoft 的商業優先取向使其更易達成政府合作

---

## 目前結論

- ⚠️ Anthropic 安全優先立場對政府市場有實質代價：短期損失大型政府合約機會
- 🔄 白宮重啟談判顯示 Anthropic 的技術能力仍具足夠吸引力
- 📊 此局面可能長期塑造 Anthropic 的市場定位：企業/科研市場優先，政府/軍事市場需更多談判

---

## 相關實體

- [[entities/mythos]]（政府關係的前置事件）
- [[topics/competitor-landscape]]（排除事件改變 Anthropic 與競品在政府市場的相對地位）

## 參考來源

- [[news/2026-05-02]]
- [[news/2026-05-26]]
- [Reuters 報導](https://www.reuters.com/business/retail-consumer/pentagon-reaches-agreements-with-leading-ai-companies-2026-05-01/)
- [Chris Olah Vatican Remarks](https://www.anthropic.com/news/chris-olah-pope-leo-encyclical) — Anthropic Blog
- [AP News：Pope calls for robust regulation of AI](https://apnews.com/article/pope-ai-tech-trump-vatican-anthropic-d92d0108730d146baa46da041b8523da)

## 時序

### 2026-06-13
- **[重大事件] 美國政府出口管制：Fable 5 / Mythos 5 對所有外籍人士停用** Trump 政府引用「國家安全授權」發布出口管制指令，要求 Anthropic 停用 Fable 5 與 Mythos 5 對所有外籍人士（包含美國境內外籍員工）的存取；Anthropic 當日 5:21pm ET 收到指令，為確保合規對全體用戶停用兩款模型，其他模型不受影響；指令未提供具體國家安全顧慮說明（Anthropic 官方聲明；Axios、Reuters、NYT、BBC、TechCrunch、WIRED、The Guardian 等主流媒體全面報導，HN score 2,662）。
- **[分析] 安全論述反噬（TechCrunch）**：Anthropic 對 Fable 5「最危險模型」的安全定性論述，反而為政府援引出口管制提供了現成理由；社群熱議「Anthropic 主張只有自己有資格決定誰能用 Mythos 模型，政府隨即接管了這個決定」。
- **[地緣政治影響]** Zoho 創辦人 Sridhar Vembu 稱此事件為「全球化已死」的象徵；India 用戶（Anthropic 第二大市場，6.6% 流量）因最具技術價值的模型下線而首當其衝；Anthropic 的「安全論述可供政府援引」邏輯，未來可能影響其他前沿模型的存取政策。

### 2026-06-11
- **[Dario Amodei 呼籲政府監管模型發布]** Bloomberg 報導 Anthropic CEO Dario Amodei 接受採訪表示政府應有權阻止危險 AI 模型發布；社群注意到此立場明顯針對中國競爭者（百度、阿里、DeepSeek），被批評為「監管套利」；Anthropic 同時呼籲不應妨礙州級 AI 法律（Reuters，r/ClaudeAI）
- **[Anthropic 呼籲美國不阻止州 AI 法律]** Reuters 報導 Anthropic 向美國國會呼籲：若無聯邦標準，不應阻止各州 AI 法規；強調需要強制性安全測試要求

### 2026-06-09
- **[Trump 政府否認 Anthropic 黑名單報復]** Reuters：川普政府否認 Anthropic AI 黑名單一事存在非法報復，此聲明背景是 Anthropic IPO 申請期間政府合約受阻的持續爭議，外界對政府 AI 採購政策透明度的質疑未見消散

### 2026-06-08
- **[五角大廈替換 Claude] 因「太安全」尋求替代**（Tech Times；Tech Times 報導）：五角大廈官員積極尋找可替代 Claude 的 AI 模型，原因是 Claude 的安全護欄在戰場場景中限制過多。此為 2026-05-01 五角大廈排除事件的後續，顯示分歧未解決。

### 2026-06-05
- **[NSA 攻擊使用 Mythos]** FT 獨家（HN 89）：NSA 正在使用 Anthropic Mythos 發動進攻性網路攻擊——Glasswing「防禦」框架的兩用性首次公開確認
- **[白宮緩和]** Reuters：白宮與 Anthropic（曾被列「安全風險」）在 IPO 前緩和緊張關係
- **[Hegseth 確認]** Politico：Hegseth（美國防部長）再次確認 Anthropic 的安全風險認定，壓力未完全解除
- **[遞歸自我改進呼籲]** Anthropic 呼籲全球 AI 暫停，Jack Clark 稱需要「brake pedal」；見 [[topics/recursive-self-improvement]]

### 2026-06-01
- **[Mythos EU 部署]** Anthropic 向 ENISA（歐盟網路安全局）提供 Mythos 存取，為首個獲准的歐洲政府機構；英國銀行遭拒，OpenAI 主動接觸提出替代方案（FT、MLex、BBC）
- **[政治獻金]** NYT：Anthropic 與 OpenAI 成為 2026 年期中選舉最大 AI 科技獻金方，兩者公開對立

### 2026-05-26
- **[重大事件] 梵蒂岡封論揭幕**：Chris Olah 出席教宗良十四世《Magnifica Humanitas》封論發布活動，Anthropic 成為唯一受邀 AI 公司；封論呼籲嚴格監管、以公共利益優先；AP News、Reuters、NYT、WashPost 等主流媒體全面報導

### 2026-05-01
- **[重大事件] 五角大廈協議排除 Anthropic**：國防部與 7 家 AI 公司簽署機密網路部署協議，Anthropic 因堅持安全護欄要求被排除
- **白宮重啟談判**：Anthropic 宣布技術突破後，白宮重啟與 Anthropic 的相關談判，後續走向仍不明確
