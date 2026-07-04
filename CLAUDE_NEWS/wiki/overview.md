# Claude / Anthropic 生態系概覽

**最後更新：** 2026-07-04

---

## 當前局勢

出口管制解除後的「蜜月期」很短：Fable 5 / Mythos 5 於 7/1 全面恢復，但短短兩天內就爆出**「embedded spyware」指控**與**Alibaba 因疑似後門風險禁用 Claude Code**，安全信任問題從「政府管制」轉移到「產品本身是否可信」。

**解禁落地**：出口管制封鎖期確認為 18–19 天，Anthropic 履行承諾之一——Fable 5 redeploy 隨附「Defense in Depth」新安全分類器，高風險 coding 請求自動 fallback 至 Opus 4.8（首日已有誤判負面實測）。7/7 前 Pro/Max/Team 享 50% 配額，7/7 後轉為 usage-based billing（**倒數中**，詳見 [[feature-radar]]）。

**信任危機（新）**：7/2 Reddit 出現指控稱 Claude Code 自 2.1.91 版起偷偵測使用者是否透過代理連線、是否位於中國，並將判斷結果隱藏於 system prompt 回傳，同時疑似混淆該段程式碼（「embedded spyware」），目前僅單方指控待查證。7/3 Alibaba 以「疑似後門風險」為由禁用 Claude Code（Reuters 報導，多媒體跟進），是首個具名大型企業因安全疑慮（而非成本或授權）退出的案例，FT 同日報導 Anthropic 正封堵中國企業間接存取漏洞。

**模型**：Claude Sonnet 5（7/1 發布，Claude Code 預設，1M context，促銷 $2/$10/Mtok 至 8/31）已有社群「個性流失」的主觀回饋，官方對比圖表修改也引發資料呈現可信度質疑。Mythos 5 政策解禁後定位為「僅限授權機構/安全研究用途，非一般消費市場」。

**商業側寫**：The Information 報導 Anthropic 與三星洽談客製 AI 晶片代工，同時 Palantir CEO Alex Karp 公開批評 Anthropic/OpenAI「竊取客戶 IP」，防務市場競爭浮上檯面；The Verge 跟進報導 Anthropic 自行開發藥物的野心。

---

## 主要模型現況

| 模型 | 狀態 | 備注 |
|------|------|------|
| **Claude Fable 5** | 🟢 全面恢復 | 出口管制 7/1 解除；新增 Defense in Depth 安全分類器（高風險 coding 請求 fallback 至 Opus 4.8）；Pro/Max/Team 7/7 前 50% 配額，7/7 後 usage-based；$10/$50 per M token |
| **Claude Sonnet 5** | 🟢 預設模型 | Claude Code 預設；1M context；$2/$10 per Mtok（促銷至 8/31）；社群反映對 Sonnet 4.6 個性流失有主觀負評 |
| **Claude Mythos 5** | 🟢 全面恢復（政策限定）| 出口管制 7/1 解除；僅限授權機構/安全研究用途，非一般消費市場 |
| Claude Opus 4.8 | ✅ Active | SWE-bench Pro 69.2%、1M context；作為 Fable 5 高風險請求的 fallback 目的地 |
| Claude Sonnet 4.6 | ✅ Active | 仍可選用；社群部分懷念其互動個性 |
| Claude Haiku 4.5 | ✅ Active | 企業混合架構低成本 worker |

> 快速選型與情境推薦見 **[[topics/model-comparison]]**

---

## 進行中議題

### 🔴 高度關注

1. **[[topics/ai-agent-safety]] — Claude Code 信任危機（「embedded spyware」指控 + Alibaba 後門疑慮）**
   - 2026-07-02：Reddit 指控 Claude Code 2.1.91+ 偷偵測代理/地區並隱藏回傳，單方指控待查證
   - 2026-07-03：Alibaba 以「疑似後門風險」禁用 Claude Code（Reuters，HN 313）
   - 詳細技術分析見 [[topics/ai-agent-safety]]；企業面影響見 [[topics/enterprise-tool-tracker]]

2. **[[topics/anthropic-government-policy]] — 出口管制解除後續**
   - 封鎖期確認 18–19 天；FT 報導 Anthropic 封堵中國企業間接存取漏洞
   - Defense in Depth 為解禁承諾首次具體落實；Legion 訴訟等衍生支線持續觀察

3. **[[topics/anthropic-commitments]] — 承諾兌現追蹤（新）**
   - 「Anthropic 說過要做的事做了嗎」單一入口：隱寫術修復 🔴、解禁三承諾 🟡 等 5 條追蹤中

4. **[[topics/anthropic-business]] — 商業版圖擴張與爭議並行**
   - Samsung 客製晶片洽談（初步報導）；Palantir CEO 公開批評「竊取客戶 IP」
   - The Verge 藥物開發野心跟進；大廠員工進駐客戶辦公室新模式

### 🟡 持續追蹤

5. **[[entities/pricing]] — 計費與定價爭議**
   - Max 方案升級誤扣費/退款案例；印度 INR 在地化定價需求無官方回應（GitHub 👍584）
   - 7/7 Fable 5 計費轉換倒數中，詳見 [[feature-radar]]

6. **[[topics/enterprise-tool-tracker]] — 企業工具版圖變動**
   - Alibaba 疑後門風險退出（❌）；Microsoft 縮減中；企業信任分歧擴大

7. **[[topics/competitor-landscape]] — 競品與市場評價**
   - Palantir Karp 批評 + 分析師調升評等；中國競品持續追趕

8. **[[topics/recursive-self-improvement]] — AI 遞歸自我改進**（monitoring）
   - Claude 已負責 Anthropic 80–90% 生產程式碼；全球「煞車踏板」呼籲未見新進展

---

## 近兩週重大事件（2026-06-21 至 2026-07-03）

| 日期 | 事件 | 影響 |
|------|------|------|
| 07-03 | **Alibaba 以疑似後門風險禁用 Claude Code**（Reuters，多媒體跟進） | 🔴 首個安全信任驅動的企業退出 |
| 07-03 | FT：Anthropic 封堵中國企業間接存取漏洞 | 🔴 出口管制執行細節 |
| 07-03 | 出口管制封鎖期媒體確認為「19 天」 | 🟡 政策落地確認 |
| 07-02 | **「Anthropic embedded spyware in Claude Code」指控**（Reddit/HN，單方待查證） | 🔴 信任危機起點 |
| 07-02 | Fable 5 Defense in Depth 首日誤判實測（化學問答/資安審查） | 🟡 解禁承諾落實但有摩擦 |
| 07-02 | Sonnet 5 官方對比圖表修改爭議 | 🟡 資料呈現可信度 |
| 07-02 | Anthropic-Samsung 客製晶片洽談（初步報導）| 💼 硬體布局訊號 |
| 07-02 | Palantir CEO Karp 批評 Anthropic/OpenAI「竊取客戶 IP」 | 🔴 防務市場摩擦 |
| 07-01 | **Fable 5 / Mythos 5 出口管制全面解除** | 🟢 里程碑解封 |
| 07-01 | **Claude Sonnet 5 正式發布**（預設模型，1M context，$2/$10 促銷） | 🔥🔥🔥🔥🔥 新旗艦 |
| 07-01 | **Claude Science 發布**（科學家 AI 工作台，Anthropic 宣布自行開發藥物） | 🔥🔥 新產品線 |
| 06-28 | Mozilla 0din 揭露 Claude Code 提示注入漏洞 | 🔴 安全 |
| 06-28 | Mythos 5 擴大解禁（100+ 機構） | 🟢 解封持續 |
| 06-27 | Mythos 5 部分解禁（Lutnick 批准 100+ 美國機構） | 🟢 轉折點 |
| 06-24 | Claude Tag 正式發布（Slack-native AI 隊友） | 🔥🔥🔥 官方新功能 |
| 06-22 | Trump 宣布 Anthropic 不再是國安威脅 | 🟡 政治障礙移除 |
| 06-22 | Anthropic × Micron 戰略合作 | 💼 基礎設施結盟 |

> 06-21 前完整事件時序見各 topics 頁面「時序」區塊。

---

## 社群工具生態

社群工具目錄（[[topics/community-tech-tools]]）持續策展中，本輪新增額度監控類工具（LimitBar、claude-needs-input）回應 Fable 5 計費轉換前的焦慮情緒；汰除 25 筆逾 30 天無後續的 ⏳ 條目。

- 🔥🔥🔥 **額度/成本監控**（LimitBar / CCLimitPing / claude-needs-input）— 7/7 計費轉換前需求集中湧現
- 🔥🔥 **Agent 協調與路由**（Workweave Router / Gorchestra）— 成本感知自動路由需求持續
- 🌊延燒 **AskUserQuestion 60 秒逾時討論** — 社群對自動代答體驗的爭議延燒中

> 功能熱度評分與試用推薦見 **[[feature-radar]]**；社群趨勢週更見 **[[topics/community-pattern-trends]]**

---

## 商業動態

- **信任面**：Alibaba 禁用（疑後門風險）+ embedded spyware 指控，是本週最大變數，可能影響企業採用率
- **競爭**：Palantir Karp 批評 Anthropic/OpenAI「竊取客戶 IP」；Samsung 客製晶片洽談顯示硬體布局野心
- **安全**：Claude Code 信任危機（2.1.91+ 代理偵測爭議升級為 spyware 指控）；出口管制執行漏洞持續被堵
- **計費**：Sonnet 5 促銷 $2/$10/Mtok 至 8/31；Fable 5 7/7 起 usage-based billing（倒數中）；Max 方案誤扣費案例浮現

---

## 功能試用推薦（快速查閱）

| 功能 | 熱度 | 推薦 |
|------|------|------|
| Claude Sonnet 5（預設模型）| 🔥🔥🔥🔥🔥 | ✅ 推薦（agentic 效能接近 Opus 4.8，注意個性流失回饋）|
| Fable 5 Defense in Depth | 🔥🔥🔥 | ⚡ 有條件推薦（高風險 coding 請求可能被誤判轉 Opus 4.8）|
| Claude Code Artifacts | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦（適合 PR 摘要、儀表板分享）|
| AskUserQuestion 60s 逾時 | 🔥🔥 | ⚠️ 已知問題，留意自動代答風險 |

> 完整功能熱度評分、升版風險與倒數中事件見 **[[feature-radar]]**

---

## 社群情緒指標

- HN 討論熱度：🔥🔥🔥🔥 高（embedded spyware 指控 + Alibaba 禁用 + AskUserQuestion 逾時）
- Reddit 情緒：😤 焦慮／不信任上升（信任危機 + 額度轉換前焦慮）
- 開發者工具活躍度：📈 持續高（額度監控工具集中湧現）
- 信任指標：↘↘ 加速下降（首次出現具名企業因「安全疑慮」而非成本退出）
- 競爭壓力：🟡 中（出口管制解除後 Fable/Mythos 回歸，但信任危機可能抵銷部分優勢）
