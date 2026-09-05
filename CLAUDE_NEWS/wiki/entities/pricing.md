---
page: "entities/pricing"
kind: "entity"
type: "policy"
status: "active（持續調整中）"
domain: "💼 商業"
last_updated: "2026-09-06"
last_news_update: "2026-09-05"
status_main: "active"
days_since_news: 1
parent: null
children: "['entities/pricing-archive']"
page_role: "hub"
days_since_news_subtree: 1
inbound_links: 135
attribution_count: 81
attribution_last: "2026-09-05"
top_source: "google-news"
pending_count: 2
pending_overdue: 0
pending_next_review: "2026-09-12"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Anthropic 訂閱方案與計費政策

**類型：** policy
**狀態：** active（持續調整中）
**領域：** 💼 商業
**首次出現：** 2026-04-25
**最後更新：** 2026-09-06
**最後新聞更新：** 2026-09-05

> **最新計費政策異動**（2026-09-06）
> - **09-14 起你的週配額變成現在的 83%**：+50% 加成 09-13 23:59 PT 到期（[官方說明中心](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion)），接手的是永久 +25%（08-29 官方 Bluesky 公告），換算後相對現在少約 17%。適用 Pro、Max、Team 與座位制 Enterprise。
> - **$100 過渡 credit 09-17 23:59 PT 到期即作廢**，不可續買、不轉存。
> - **四件計費事故仍未解**：續訂扣款後帳號停用、旗艦用量點數誤扣、升級付款流程作廢、$16.6M 帳務錯誤的退款未定。見「事故現在還在發生嗎」。

## 現況

**09-14 是下一個會動到你帳單的日子**：週配額換軌後水位約為現在的 83%，同一週還有過渡 credit 09-17 到期。兩者都不需要你做任何設定，但都會改變你這個月能用多少。

**2026-07-20 起，旗艦模型（現為 Fable 5）在訂閱體系中被切成兩層**：Max 與 Team premium 席位維持標配、上限為週用量的 50%；Pro 與 Team standard 席位改以 usage credits 按 API 費率付費，並發放一次性過渡 credit。此分界經 2026-08-08 官方 Help Center 查證確認，終結 07-18～21 間四則互相矛盾的媒體報導。對照見下方「我的方案現在有什麼」。

**09-14 之後你會少多少（換算法）**：官方不公布每週配額的絕對量，只在 `Settings > Usage` 顯示你自己的數字。**你會看到的變化**：09-14 之後做同樣份量的工作，`Settings > Usage` 的用量百分比會比現在多跑約 **20%**（1 ÷ 0.83）——這是唯一能自己對號的方式。**升到 Max 20x 能多拿多少，官方未載明，本站不推估**。

**你的選項**：什麼都不做（同樣工作用量百分比多跑約 20%）／把重活挪進 5 小時窗（該窗不受影響）／評估 Max 20x（增量官方未載明，本站不推估）。

其餘結構未變：所有付費方案仍為訂閱配額制——原定 2026-06-15 實施的「程式化用量（Agent SDK、`claude -p`）脫離訂閱、改按 API 費率計費」已於 **2026-06-16 暫停**，重新推行時間未定；2026-07-04 起企業方案可用支出控管（spend controls）。核心爭點：訂閱方案以人工互動為設計前提，大規模自動化工作流的長期計費方向尚未確定。

---

## 我的方案現在有什麼

> **資料截至 2026-08-22**（官方 Help Center 查證）。此表反映**訂閱月費**，非曾規劃但已暫停的 programmatic 信用池金額（見下方「計費切割風波」）。「訂閱內含／需另計費」的分界會隨陣容換代改變，模型名以當期實際情形填寫。

| 方案 | 月費 | 訂閱內含 | 需另計費 | 可領優惠 | 你該做的動作 |
|------|------|---------|---------|---------|------------|
| Free | $0 | 基本額度；旗艦存取未載 | — | — | 09-14 起週配額永久 +25% 不適用本方案（見下方週配額改版說明）|
| Pro | $20（年繳 $17／月）| 全模型，**旗艦除外** | **Fable 5** — $10/$50 per Mtok，走 usage credits | **已截止**：一次性 $100 過渡 credit 領取窗於 2026-08-02 關閉 | 已領者記得在 09-17 到期前用掉；至 `Settings > Usage` 確認 auto-reload 未開 |
| Max 5x | $100 | 全模型；**旗艦上限為週用量 50%** | 超出後走 usage credits | — | 留意旗艦誤要求購點問題（見事故區）|
| Max 20x | $200 | 同上，額度更高 | 同上 | — | 用量上限集體訴訟進行中 |
| Team standard seat | $20（年繳）／$25（月繳）每席 | 同 Pro | 同 Pro | 同 Pro | 同 Pro |
| Team premium seat | $100（年繳）／$125（月繳）每席 | 同 Max | 同 Max | — | — |
| Enterprise | 未公開報價 | 舊制席位制比照 standard／premium 分層 | 同對應層 | — | 2026-07-04 起可用支出控管 |

**⚠️ usage credits 是「用量上限失效開關」**：credits 為 opt-in、預設關閉（`Settings > Usage`）。**一旦開啟，方案用量上限就不再是硬停止**——Claude 會繼續回答並從 credits 扣款，體感與額度內完全相同，但每則超額回應都在計費。靠 Pro 硬上限控管支出者，領取過渡 credit 後務必確認 auto-reload 未開啟（auto-reload 每日兌換上限 $2,000）。（來源：[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)、[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)，2026-08-08 查證）

> **09-13／09-17 兩個到期時點的時分**（23:59 PT）為多家媒體引官方公告的一致轉述，官方說明中心原文本站尚未取得。

### 方案細節

- **旗艦分界的官方定義（2026-07-20 生效）**：Max 方案、Team premium seats、舊制席位制 Enterprise premium seats — Fable 5 為標配，可用「至多每週用量上限的 50%」且不額外收費；Pro 方案、Team standard seats、Enterprise standard seats — Fable 5 **不計入方案用量**，需以 usage credits 按 API 費率付費。先前將 Fable 5 納入方案週用量的促銷結束於 **2026-07-19 23:59:59 PT**
- **Pro／Team standard 過渡 credit（2026-08-22 官方查證，先前懸置已結案）**：金額 **$100**——Pro 為每帳戶 $100，Team 為每購買的 standard seat $100、每組織上限 $2,500。資格以 **2026-07-19 23:59:59 PT** 當下持有合格 Pro／Team standard 方案為準（免費試用不算）。**領取窗已於 2026-08-02 23:59 PT 關閉**，未領者不再補發；已領取的 credits 於 **2026-09-17 23:59 PT 到期**（促銷起算 60 天）。這批 credits **不限 Fable 5**，是一般 usage credits，任何模型都能用、方案用量觸頂時也能墊（來源：[Claude Fable 5 one-time free credits promotion](https://support.claude.com/en/articles/15862783)，2026-08-22 查證）。credits 用盡後可續買、改用其他模型、或升級 Max
- **credits 購買方式歧異（未收斂）**：官方寫「Add funds，自行輸入金額」，XenoSpectrum 則稱為固定包（$45 買 $50、$200 買 $250、$700 買 $1,000）。兩者對不上，媒體數字不採信，以官方為準
- **Pro 年繳**：$200 一次預付，折合 $17／月（來源：[claude.com/pricing](https://claude.com/pricing)，2026-08-08 查證）
- **印度在地化定價**：Pro 為 **Rs 2,000／月**（2026-07-13 生效，首個非美元在地化市場，回應 GitHub Issue #17432）；Max／Team／Enterprise 是否同步在地化未見報導
- **Max 5x 月費曾記載矛盾**：06-26 Reddit 貼文誤植 $50，已依 2026-05-14 xda-developers／dev.to 官方公告原文更正為 **$100**；該貼文「兩個 Max 5x = 一個 Max 20x」的價格假設有誤
- **Max 20x 用量上限集體訴訟進行中**：Karl Kahn 訴訟（2026-06-16 提起）指控實際僅 Pro 的 6–8 倍而非廣告的 20 倍
- **Team／Free／Enterprise 月費（2026-08-08 官方查證）**：Team 可混搭席位型別（mix and match），standard $20／premium $100（年繳，月繳各為 $25／$125），未見最低席位數規定；Free $0；Enterprise 未公開完整報價，頁面標示為「席位費＋依 API 費率計量」並提及 $20／席，實際價格需洽業務（來源：[claude.com/pricing](https://claude.com/pricing)）
- **Free／Pro 功能組成（2026-08-12 官方查證，原文於 Max 段落截斷）**：Free 含 web 搜尋、記憶、桌面擴充、connector；Pro 另含 Claude Code／Cowork／Design／Science、無限 projects、Research、更多模型選擇、Microsoft 365 整合。此為功能清單補充，不影響上表的月費／計費規則；Max／Team／Enterprise 段落待後續查證（來源：[claude.com/pricing](https://claude.com/pricing)）
- **各方案最強可用模型（2026-07-24 起）**：Opus 5 為 Pro 方案最強可用模型、Max 方案新預設模型（原為 Opus 4.8），見 [[entities/opus-5]]
- **Max 20x 的差異不只用量**：context window、Claude Code 額度、優先排隊等有結構性差異，非單純 Pro 的 20 倍
- **Enterprise 附加功能**：含 Compliance API、Enterprise Gateway 等；合作分級 Select／Preferred 差異未公開。Team 方案於 2026-06-19 官方速率翻倍時同步適用
- **usage credits 僅可在網頁版開通（2026-08-11 官方查證）**：官方說明中心 usage-credits 條目載明，行動 App（iOS／Android）訂閱者無法直接於 App 內開啟 usage credits，須改至網頁版 `Settings > Usage` 操作；額度用盡後可切換按量計費（API 標準費率）不中斷服務。此為既有「credits 為 opt-in、預設關閉」規則（見上方 2026-08-08 條目）的補充限制（來源：support.claude.com usage-credits 條目，2026-08-11）

---

## 一小時／一個月大概多少

本頁給的是「一小時多少」，[[topics/model-comparison#同一份工作，換設定差多少]] 給的是「這一件工作多少」。

> 本表假設：**一小時 agent 工作 ＝ 50k 輸入 ＋ 15k 輸出 token ＋ 一個 session-hour**，取自官方 Managed Agents 算例。只有 Opus 5 那列是官方算的，其餘是同一份工作量代入各自牌價的推算，**不是實測**。資料截至 2026-09-06（Managed Agents 為 beta，須 beta header）。

| 模型 | 一小時 | 一個月（每天 4 小時 × 22 天） | 這個數字哪來的 |
|------|--------|------|------|
| Opus 5 | $0.705 | 約 $62 | 官方算例逐字 |
| Fable 5.1 | 約 $1.33 | 約 $117 | 推算（$10/$50 牌價代入同一 token 量）|
| Sonnet 5 | 約 $0.33 | 約 $29 | 推算（$2/$10 牌價代入同一 token 量）|

**$100 買得到多少 API 用量**：以上表口徑（透過 Managed Agents 跑），$100 約等於 Fable 5.1 的 **75 小時**、Opus 5 的 **142 小時**；直接呼叫 API 沒有 $0.08 的 session-hour，同一份工作量約 **80 小時**與 **160 小時**。**這不是「訂閱划不划算」的答案**——Max 5x 的 $100 買的是週配額，其中旗艦（Fable 5）只能用到週用量的 50%，超出後一樣按 API 費率扣 usage credits（見上方「我的方案現在有什麼」）。兩種貨幣不可直接相除。

**這個表沒告訴你什麼**

- **你的實際 token 量不會是 50k／15k**。要估自己的，先用 `count_tokens` 量一次真實的 prompt，再照上表比例縮放。
- **一整個月的真實落差有人量過，數字比這裡大得多**：訂閱與純 API 之間最高 40 倍，具名企業案例與方法論見 [[topics/enterprise-cost-management]]，本頁不重複列。
- **上表沒有算乘數**。快取命中、Batch、資料落地都會再乘一次，見下方「通路與乘數」。
- **換一個模型跑同一件工作差多少**（含 tokenizer 換代讓同一段文字多產生約 30% token）不在本頁，見 [[topics/model-comparison#同一份工作，換設定差多少]]。

---

## 模型 API 定價現況

| 模型 | Input / Output per Mtok | 備注 |
|------|------|------|
| Claude Sonnet 5 | $2 / $10 | **標準定價（不再是促銷）**：原訂 2026-08-31 到期的入門價已於 2026-08-10 永久化，9/1 漲至 $3/$15 的計畫取消；Claude Code 新預設模型，相較 Opus 4.8 估計省 60% 成本 |
| Claude Fable 5.1 | **$10 / $50** | 與 Fable 5 同價（官方定價頁 2026-09-03 查證）；**快取命中 ×0.025**（其餘模型 ×0.1），Batch $5/$25。Mythos 5.1 同價但僅限授權機構 |
| Claude Fable 5 | $10 / $50 | Pro／Team standard 走此費率以 usage credits 計費；Max／Team premium 為標配（週用量 50% 內）。訂閱端分界見上方「我的方案現在有什麼」|
| Claude Opus 5 | **$5 / $25** | 官方文件逐字確認，與 Opus 4.8 相同；Fast mode 另計 $10/$50 |
| Claude Opus 4.8 | **$5 / $25** | 官方載明 Opus 5 定價「unchanged from Claude Opus 4.8」；2026-07-24 起次旗艦地位被 Opus 5 取代，各平台仍可用 |
| Claude Sonnet 4.6 | **$3 / $15** | 前代 Sonnet，官方列為 legacy 仍可用；1M context / 128k 輸出。（Sonnet 5 原訂 8/31 後回到此價位的計畫已取消）|
| Claude Haiku 4.5 | **$1 / $5** | 陣容中最低價；200K context / 64k 輸出（非 1M，與其餘四者不同）。適合高頻批量與延遲敏感的 sub-agent |

**Opus 5 定價「歧異」已解消（2026-08-08 官方查證）**：官方文件載明 **$5 / $25 per Mtok，「unchanged from Claude Opus 4.8」**。此前兩種說法其實同時成立——「為 Fable 5 的一半」（$5 vs $10）與 MarkTechPost「維持原 Opus 定價」（與 4.8 相同）是同一組數字的兩個對照對象。Fast mode（research preview，僅 Claude API）另計 **$10 / $50**（來源：[What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5)）。能力細節見 [[entities/opus-5]]、[[topics/model-comparison]]。

**本表數字之官方查證（2026-08-20）**：Fable 5 $10/$50、Opus 5 與 Opus 4.8 $5/$25、Sonnet 5 $2/$10、Sonnet 4.6 $3/$15、Haiku 4.5 $1/$5，均與官方模型總覽頁一致（[Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)，2026-08-20 查證）。**（2026-08-28 更正）** 此註原寫「8/31 之後的 $3/$15 走向待定」——該說法在寫下時就已過期：官方早於 **2026-08-10** 宣布 $2/$10 永久化、9/1 漲價取消。已無到期日可等。

**Fable 5.1／Mythos 5.1 快取費率新增（2026-09-02）**：官方定價文件載明兩版本的快取讀取／刷新費率為**標準輸入價的 0.025 倍**（標準快取命中乘數為 0.1 倍，見下方「通路與乘數」），長對話快取成本較前代最多省 75%。**（2026-09-03 更正）** 官方[定價頁](https://platform.claude.com/docs/en/about-claude/pricing)已載兩版本基礎定價 **$10 / $50 per Mtok**（與 Fable 5／Mythos 5 相同；Batch $5 / $25），上表已補列；長脈絡仍不加價、tokenizer 仍為 Claude 4.7 起導入的版本（尚無新世代 tokenizer 公告）。版本能力見 [[entities/fable-5]]。

> 模型能力與**同一份工作的實付換算**見 [[topics/model-comparison]]；此表只列牌價。
> **tokenizer 換代讓成本比較變難的具體數字**（約 +30% token）見 [[topics/model-comparison#同一份工作，換設定差多少]]，本頁不重複列。

---

## 當前生效的計費規則

計費事故與爭議見下方「事故現在還在發生嗎」。

%% 維運備忘：一條一規則，附來源日期；失效規則移除 %%

- **✅ 2026-09-13 到期（更正：非如期於 08-31 終止）｜Claude Code 週用量 +50% 促銷**：此促銷原訂 2026-05-13 起，歷經 06-22→07-07→07-12→07-19→08-18→**09-02（本次更正）**多次延長。08-29 官方公告曾記為「08-31 到期、不再延長」，但官方說明中心 **2026-09-02** 更新原文——「We've extended this promotion. Increased weekly limits now run through September 13, 2026.」——實際延長至 **2026-09-13**；09-14 起銜接下方「標準週配額永久 +25%」，兩者不留缺口。適用 **Pro、Max、Team**（來源：[Claude Code May–August 2026 Weekly Limits Promotion](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion)，2026-09-02 查證）
- **⏰ 2026-09-14 生效｜標準週配額永久調高 25%，但取消 +50% 加成 → 相較「加成期間」水位實際減少約 17%**：官方公告（Bluesky @anthropicbot，2026-08-29）自 2026-09-14 起將 Claude Code 標準週配額**永久**調高 **25%**，適用 **Pro、Max、Team 與座位制 Enterprise**；上方 +50% 促銷 09-13 屆滿後由本規則接手，不留缺口。換算 `1.25 ÷ 1.50 ≈ 0.833`——09-14 起實際可用週配額約為加成期間的 83%，**減少約 17%**（BleepingComputer〈Anthropic is cutting Claude Code's current weekly limits by 17 percent〉即以此為框架）。**你該做的事**：工作流若貼近週配額上限，09-14 前後應預期可用量下降，評估調整用量節奏或方案層級（來源：[Bluesky @anthropicbot](https://bsky.app/profile/anthropicbot.bsky.social/post/3muaaxs5nx424)、[BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/)，2026-08-29）
- **✅ Managed Agents 計費＝token＋session runtime（官方定價頁，2026-09-06 查證）**：token 依模型牌價（快取乘數、web search $10／1,000 次、`inference_geo` 1.1×、fast mode 溢價皆照 API 規則）；runtime **$0.08／session-hour**，只計 `running`
- 上條來源：[Managed Agents pricing](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)；`idle`／`rescheduling`／`terminated` 不計時，毫秒計量
- **Managed Agents 不適用 Batch 折扣與 partner 雲端**（Bedrock／Vertex 無此產品）；runtime 取代 code execution 的 container-hour，不重複收。官方算例：Opus 5 跑 1 小時、50k 輸入／15k 輸出 ≈ **$0.705**，40k 輸入走快取 ≈ $0.525
- **Managed Agents 框架整體仍 beta**（須 `managed-agents-2026-04-01` header；[overview](https://platform.claude.com/docs/en/managed-agents/overview)，2026-09-06 查證）；選型與零件成熟度見 [[entities/managed-agents]]
- **✅ 2026-07-20 生效｜旗艦模型的訂閱分界（官方文件已確認）**：Max 方案、Team premium seats、舊制席位制 Enterprise premium seats — Fable 5 為標配，可用至多**每週用量上限的 50%**，不額外收費；Pro 方案、Team standard seats、Enterprise standard seats — Fable 5 **不計入方案用量**，需以 usage credits 按 API 費率（$10/$50 per Mtok）付費。合格 Pro 與 Team standard seats 另有**一次性過渡 credit $100**（Team 每 standard seat $100、每組織上限 $2,500），領取窗已於 2026-08-02 關閉、已領 credits 於 2026-09-17 到期，且可用於任何模型（[官方促銷條目](https://support.claude.com/en/articles/15862783)，2026-08-22 查證）。先前將 Fable 5 納入方案週用量的促銷結束於 2026-07-19 23:59:59 PT（來源：[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)，2026-08-08 查證）
- **⚠️ usage credits 開啟後，方案用量上限不再是硬停止**：credits 為 opt-in、預設關閉，於 `Settings > Usage` 開關，可設 auto-reload（每日兌換上限 $2,000）。開啟後 Claude 會在額度用盡後繼續回答並從 credits 扣款，體感與額度內無異，但每則超額回應皆計費——靠方案硬上限控管支出者需主動確認此開關（來源：[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)，2026-08-08 查證）
- **訂閱配額制維持**：原定 2026-06-15 生效的 Agent SDK／`claude -p` 計費切割已於 2026-06-16 暫停，重新推行時間未定；Agent SDK、`claude -p`、第三方 Agent SDK app 用量持續計入訂閱配額，無需額外信用池（來源：2026-06-16、2026-06-18 DevOps.com）
- **1M context window 觸發獨立 API 計費通道**：即使儀表板顯示 0% 訂閱用量，1M context window 仍會產生額外費用（實例：2026-05-11 用戶 0% 用量下遭收取 $3.37 Extra Usage）。1M 的世代分界與控制權缺口見 [[topics/long-context-1m]]
- **`ANTHROPIC_API_KEY` 環境變數陷阱**：雲端環境（CI/CD、Docker、K8s）若設置此環境變數，所有 Claude Code 呼叫自動改走 API 計費通道而非訂閱配額（來源：2026-04-30）
- **企業支出控管功能上線（2026-07-04）**：具體控管粒度（部門／團隊層級、per-user、即時警報）尚未公開（來源：2026-07-04 Tech Times）
- **印度盧比在地化定價生效（2026-07-13）**：Pro 方案 **Rs 2,000／月**，為美國以外最大市場首次官方在地化定價；Max／Team／Enterprise 是否同步在地化未見報導（來源：2026-07-13～14 TechCrunch、NDTV、Times of India、bestmediainfo.com）
- **Max 用量上限爭議進入司法程序**：2026-06-16 集體訴訟指控 Max 5x／Max 20x 實際限制遠低於廣告宣稱（Max 20x 實測僅 Pro 的 6–8 倍），訴訟結果將影響方案信任度與可能的退款／調整義務（來源：2026-06-16 CNET、Decrypt）
- **✅ 內建工具的計費（官方定價頁，2026-09-06 查證）**：程式碼執行每月 1,550 小時免費，超出後 $0.05／小時；網頁搜尋 $10／1,000 次；網頁擷取免費
- **✅ Claude Security 跑 Mythos 5＝標準 token 計費**（Enterprise 方案內，無須加購；官方 blog 2026-08-21）

> **已失效並移除的規則**：Fable 5 免費使用期（2026-07-19 到期，已由上方 07-20 分界取代）。**更正（2026-09-02）**：先前記於本欄之「Claude Code 週用量 +50% 促銷已如期於 08-31 到期、未再延長」為誤植——官方 09-02 更新公告顯示該促銷實際延長至 2026-09-13，該規則現仍生效，已移回上方「當前生效的計費規則」。沿革見下方「重要政策變動紀錄」。

---

## 通路與乘數

上方三個區塊是**牌價**。實付金額還取決於兩件事：**走哪條通路**，以及**套了哪些乘數**——兩者都會讓帳單與牌價對不上。資料截至 **2026-09-03**（官方文件查證；本次新增 Fable 5.1／Mythos 5.1 的快取命中特例，其餘與 08-29 一致）。

### 通路：誰定價、怎麼開票

| 通路 | 誰營運 | 誰定價 | 計費單位 | 取不到的計費手段 |
|------|--------|--------|---------|----------------|
| Claude API（第一方） | Anthropic | Anthropic | 每 Mtok | — |
| Claude Platform on AWS | Anthropic | Anthropic（標準費率） | CCU（100 CCU＝$1） | fast mode |
| Amazon Bedrock | AWS | **AWS 自訂** | AWS 服務用量 | **Batch 折扣**、beta 功能 |
| Google Cloud／Vertex AI | Google | **Google 自訂** | Google 服務用量 | 見官方平台可用性 |
| Microsoft Foundry | Anthropic | Anthropic（標準費率） | CCU | — |

**通路細節**

- **partner 通路（Bedrock、Google Cloud）的絕對數字本頁不記**——費率由該平台自訂且會各自調整，抄下來即過期。查 [Bedrock 定價](https://aws.amazon.com/bedrock/pricing/)／[Google Cloud 定價](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models)
- **Bedrock 無 Message Batches API ⇒ 拿不到 50% 批次折扣**；亦不支援 `anthropic-beta` 標頭，compaction／context editing／task budgets 皆不可用——長脈絡的成本控制手段少一半
- **Claude Platform on AWS 組織固定於 Start 層且不自動升級**，月花費上限 $500，提額須聯繫 Anthropic 客戶代表；私有報價須在產生用量**前**接受，折扣不溯及既往
- **Claude Enterprise 經 AWS Marketplace 採購**是 claude.ai 聊天產品、不是 API 平台，於 claude.ai 管理，與上表五條通路無關
- **CCU 通路只能後付**（AWS／Foundry）：折扣不是降低單價，而是**同一筆用量換算出較少 CCU**呈現在帳單上

### 乘數：會互相疊乘

| 乘數 | 倍率 | 套用範圍 | 觸發條件 |
|------|------|---------|---------|
| 快取命中 | ×0.1（Fable 5.1／Mythos 5.1 為 **×0.025**） | 讀取的 token | 命中既有快取 |
| Batch API | ×0.5 | 輸入＋輸出 | 非即時工作負載 |
| 快取寫入（5 分／1 小時） | ×1.25／×2.0 | 寫入的 token | 建立快取 |
| 資料落地 | ×1.1 | **輸入、輸出、快取讀寫全部** | `inference_geo:"us"`；Azure 為 US Data Zone Standard；Claude 4.6 以後 |
| 地區端點 | ×1.1 | 全部 token | Bedrock／Google Cloud 用 regional 或 multi-region 端點 |
| 長脈絡（Claude 4.6 以後） | ×1.0 | — | **不加價**，900k 與 9k 同費率 |
| 長脈絡（Sonnet 4／4.5 世代） | ×2.0 輸入／×1.5 輸出 | 僅超過 200K 的請求 | 該世代 1M 為預覽功能 |
| Fast mode | 改為 $10／$50 | 取代基準費率 | 僅 Opus 5 與 4.8，僅第一方 API |

**乘數細節**

- **會疊乘**：例如 Batch ×0.5 與資料落地 ×1.1 同時成立時兩者相乘。往下的只有快取命中與 Batch
- **快取命中的特例**：Fable 5.1／Mythos 5.1 的命中／刷新費率為基準輸入價的 ×0.025（$0.25/Mtok），其餘所有模型維持 ×0.1；快取寫入倍率兩者相同（官方定價頁 Prompt caching 節，2026-09-03 查證）
- **長脈絡的分界是模型世代，不是「1M」這個功能**。Claude 4.6 以後內含 1M 且不加價（官方[定價頁](https://platform.claude.com/docs/en/about-claude/pricing) Long context pricing 節）；Sonnet 4／4.5 世代的 1M 為 public preview，[AWS 公告](https://aws.amazon.com/about-aws/whats-new/2025/08/anthropic-claude-sonnet-bedrock-expanded-context-window/)明載超過 20 萬 token 的 prompt 約為兩倍輸入價、1.5 倍輸出價。**兩代混用時，兩套規則會出現在同一份帳單上**
- **診斷法**：價差只在大請求出現 → 舊世代長脈絡溢價；小請求也貴同樣比例 → 資料落地或地區端點
- 模型之間「同一份工作換個模型差多少」的換算（含 tokenizer 換代的影響）不在本頁，見 [[topics/model-comparison#同一份工作，換設定差多少]]
- **1M 這個旋鈕本身**（世代分界為何長這樣、預設開啟能不能關、選定狀態保不保得住）另見 [[topics/long-context-1m]]

---

## 事故現在還在發生嗎

**一事故一列，只收 🔴、⛔、⚖️ 三種狀態；轉 ✅／⏸ 即移出表，條目留在下方事件流。本表上限 6 列，滿載時較新的活躍事故會暫時列在下方事件流（標「未列入總表」），一併掃一次才完整。** 狀態五值定義（供讀者對號）：🔴 未解＝官方未公開回應、也未載明修復版本；✅ 已修＝官方確認或載明修復版本；⛔ 官方拒修＝官方已明確表態不修；⚖️ 司法中＝已進入訴訟程序；⏸ 無後續＝距最後動態逾 90 天且無新回報，**但 ⚖️ 在判決或撤訴前一律留表，官方曾公開承認過的事故也不因時間轉 ⏸**（改標 ⛔ 或維持 🔴 到官方給出結果）。**這五值不看留言數，只看官方有沒有給出答案**——例如 #79337 最後動態 2026-08-07（距今逾 30 天）仍是 🔴，因為它未逾 90 天且官方無回應。

%% 維運備忘：上限與退場判準見 .claude/rules/wiki-ingest-commercial.md「pricing 事件流的上限與退場」 %%

| 事故 | 狀態 | 最後動態 | 你該做的事 |
|------|------|---------|-----------|
| HERMES.md 字串觸發靜默切 API 計費 | ⛔ 官方拒修 | 2026-04-25，官方確認為 bug 但拒絕退款 | commit 訊息避開該大寫字串；已被扣費者官方不退 |
| Anthropic 證實 $16.6M 帳務錯誤、企業多收 $1.7M（含南韓 $16.7M 個案） | 🔴 未解 | 2026-07-20 | 核對 7 月帳單有無異常扣款；退款與補救官方未載明 |
| Max 20x 實際用量與廣告宣稱落差 | ⚖️ 司法中 | 2026-06-16 集體訴訟，指實際僅 Pro 的 6–8 倍 | 依現況估算用量，不要以「20 倍」為預算基準 |
| Max 5x 續訂扣款完成後帳號遭停用 | 🔴 未解 | 2026-09-04，GitHub Issue #5088 累積 184 則留言 | 續訂後立刻確認帳號可用，留下扣款紀錄 |
| 升級付款流程 PaymentIntent 提前作廢 | 🔴 未解 | 2026-08-12，Issue #55982 累積 77 則留言 | 升級失敗時不要重複送出，先查有無重複授權 |
| 旗艦模型仍被要求額外用量點數 | 🔴 未解 | 2026-08-07，Issue #79337 累積 67 則留言，延燒逾 18 天 | 若被要求購點，先確認方案內的 50% 上限是否已用盡 |

**已結案三件（供對照）**：共用池機制（2026-08-22 官方確認）、Opus 5 定價兩說收斂（2026-08-08）、Sonnet 5 $2/$10 永久化（2026-08-10）。下方「事故與爭議」事件流每則事故標題前的符號就是它的狀態。

---

省錢技巧與具名企業案例見 [[topics/enterprise-cost-management]]。

---

## 重要政策變動紀錄

依主題分組，各組內日期倒序（最新在上）。

### 灰色市場與轉售現象

- 轉售商以最高 90% 折扣轉賣 Claude／Codex API 存取權，違反 Anthropic 消費者條款（禁止 resell、禁止分享帳號憑證）。
- 灰市管道「Poison Claude」已被兩獨立媒體證實會讓中間營運者讀取客戶傳送的全部 prompt——安全事件細節與可信度評估見 [[topics/ai-agent-safety]]。
- 🔎 **查無官方**（標 2026-08-10｜查 [[topics/ai-agent-safety]]、resale scope｜訊 2026-08-29｜複 2026-09-30）｜轉售規模與 Anthropic 執法回應均未見官方聲明或第三方媒體佐證。

### 事故與爭議（誤扣費、靜默計費改動、帳號安全）

#### 🔴 2026-09-04：GitHub Issue 累積 184 則留言——Max 5x 續訂扣款後帳號遭停用

- **GitHub Issue #5088（184 留言，2026-09-04 查證）**：Max 5x 續訂扣款完成後帳號隨即遭停用，無法使用已付費的方案；184 則為本頁計費爭議類目前最高（前次高點 77／67 則）。
- 出處：[GitHub #5088](https://github.com/anthropics/claude-code/issues/5088)
- **與既有事故的關係**：與 08-12 Issue #55982（升級流程 PaymentIntent 遭提前作廢）同屬「付款/帳務基礎設施層故障」而非「用量計費異常」，惟本則更嚴重——付款已扣款成功、帳號卻遭停用，使用者付了錢反而喪失服務存取權，是本頁目前記錄最直接侵害付費用戶權益的計費事故型態（推論）；機制面／官方是否回應修復詳見 [[entities/claude-code]] 已知問題，此處僅記計費/帳務面
- ❓ **待查證**（標 2026-09-04｜查 Max 5x、帳號停用｜複 2026-09-18）：停用成因（誤判詐欺續訂、系統 bug 或其他）、官方是否已修復或提供補償，均未見報導或官方回應；已掃日報至 2026-09-04 無後續，官方頁面未查證

#### ⚖️ 2026-08-31：HN 質疑「20x」用量宣稱的實質定義——只放大 5 小時視窗、非週上限，呼應既有 Max 20x 集體訴訟

- **Hacker News（2026-08-31 13:56 UTC）**：發文者指出，官方行銷所稱的「20x」用量提升（見 Max 20x 方案命名），實際只放大**單次 5 小時使用視窗**內的用量上限，並非字面上讀者直覺理解的「週用量整體上限的 20 倍」；發文者認為此行銷用語容易誤導，討論串中有留言提及已有針對用量宣稱的行銷不實訴訟（[HN https://news.ycombinator.com/item?id=49509882](https://news.ycombinator.com/item?id=49509882)）。
- **對照本頁既有紀錄**：Karl Kahn 於 2026-06-16 提起的集體訴訟指控 Max 20x **實際用量僅為 Pro 的 6–8 倍**、而非廣告的 20 倍（見方案細節「Max 20x 用量上限集體訴訟進行中」）。兩者是同一爭議的不同角度——訴訟問「20 倍算得對不對」，本則 HN 問「20 倍算的是哪個時間窗」，互為佐證但非同一指控，不可合併。
- **未解之處**：官方未見文件逐字定義「20x」的計算基準（5 小時視窗、日、週）；本則是否構成訴訟新增指控依據、或僅為社群側佐證討論，未見後續（單一 HN 討論串，score 未知，無主流媒體跟進）。

#### 🔴 2026-08-28：Reddit 整理十週時間軸——官方曾稱 Fable 5 將恢復訂閱內含，Pro 方案至今仍按 token 計費（承諾兌現追蹤見 [[topics/anthropic-commitments]]）

- **Reddit r/ClaudeAI（2026-08-28）**：使用者整理 Fable 5 計費爭議時間軸，指出官方曾表態 Fable 5 將恢復為訂閱內含，惟十週後 Pro 方案仍按 token 計費，情緒標記 😤。
- **對照本頁既有紀錄**：07-20 分界已經官方查證確認——Pro／Team standard seats 的 Fable 5 **設計上就是**不計入方案週用量、須以 usage credits 按 API 費率付費，並非暫時性故障。「十週」回推約落在 06 月中旬，早於 07-20 分界生效日；具體是哪一則官方表態、措辭為「將恢復」還是「維持既有分層」未見原文可查核，無法判定是否存在與現行分界矛盾的舊承諾。
- **與本頁定位的關係**：此為「官方承諾與現況落差」型讀者情緒，非計費事實的新資訊；承諾是否兌現追蹤見 [[topics/anthropic-commitments]]（原始官方表態尚待補列）。
- （不列入總表：承諾兌現追蹤在 [[topics/anthropic-commitments]]）

#### ✅ 2026-08-15：Fable 5／Opus 5 是否共用同一週用量池 → ✅ 官方確認共用，「50% 上限」是池內天花板不是額外配額（2026-08-22 查證結案）

- **Reddit r/ClaudeCode（2026-08-15）**：使用者質疑，若 Opus 5 與 Fable 5 共用同一週用量池，則 07-20 分界給 Max／Team premium 的「Fable 5 最多用到週用量 50% 且不額外收費」形同被 Opus 5 消耗架空，牴觸設計原意。
- **查證本頁既有紀錄**：07-20 分界僅明確 Fable 5 自身的計量規則（Max/Team premium 標配、Pro/Team standard 走 usage credits），**未見官方一手來源說明兩者是否共用計量池**——此為尚未回答過的問題，非既有紀錄矛盾。
- **✅ 官方答案（2026-08-22 查證）**：**共用同一池，貼文的直覺是對的，但推論的「牴觸設計」不成立。** 官方〈Claude Fable 5 on your plan〉逐字寫明 Fable 5「draws from your plan's regular weekly usage limits and uses them faster than other Claude models」，FAQ 另稱「your use of other models draws from the same usage limits and you can never use more than your weekly limit」——亦即 **50% 是同一池內的「Fable 5 最多能吃掉一半」天花板，本來就不是額外配額**。讀者要知道的實務結論：拿 Opus 5 跑滿週用量，Fable 5 那 50% 額度也跟著不見；反之亦然（來源：[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)，官方頁最後更新 2026-07-20，2026-08-22 查證；原始質疑 Reddit https://www.reddit.com/r/ClaudeCode/comments/1vozbmm/opus_5_and_fable_5_sharing_a_pool_isnt_that_a/）

#### 🔴 2026-08-14：Max 方案 session 額度自 3/23 起異常快速耗盡（本頁互動量最高配額回報）+ 社群質疑用量被暗中調降

- **GitHub Issue #38335（👍 543，2026-08-14 查證，CLI 使用情境）**：使用者回報 Claude Max 方案的 session 限制自 **2026-03-23** 起異常快速耗盡；543 個 👍 遠超一般收錄標準（本則為反應數非留言數，量級仍屬本頁近期配額類最高）。機制面見 [[entities/claude-code]] 已知問題；此處僅記配額／計費面：問題若屬實，代表配額計算自 3 月下旬起即可能有系統性異常，而非 07-20 旗艦分界後才出現的新問題（推論；根因、是否與 Issue #79337 同源均未見證實）（GitHub https://github.com/anthropics/claude-code/issues/38335）
- **Reddit r/ClaudeCode：質疑用量配合 8/19「50% 提升永久化」而暗中調降（單一貼文，未經證實）**：使用者質疑 Anthropic 暗中調降用量，以在傳聞的「50% 用量提升」8/19 永久生效前後製造對比（score=0，Reddit RSS 無讚數非低互動指標；屬使用者推測，非事實）。**查證本頁既有紀錄**：本頁記錄的「週用量 +50%」促銷（2026-06-15 起臨時提高、多次延長至 2026-07-19）已由 07-20 分界取代，**未見與「8/19 永久化」對應的官方公告**；貼文所稱「8/19」與既有時程（7/19）不吻合，可能指涉另一項未收錄的官方承諾，或屬時程誤記；具體指控查證見下方標記（Reddit r/ClaudeCode，2026-08-14）
- **✅ 08-18 官方公告部分澄清（是「延長至 8/31」，非「永久化」）**：08-18 官方公告證實「週用量 +50%」促銷持續延長中，**並未如本頁此前誤記般已於 07-19 失效**——貼文對促銷仍生效的直覺並非空穴來風。惟官方措辭為暫時延長至 **2026-08-31**，非永久政策。
- ❓ **待查證**（標 2026-08-14｜查 暗中調降用量、throttling｜複 2026-09-12）｜**貼文中「暗中調降用量以製造對比效果」的具體指控**仍未獲官方證實或否認，不因促銷延長本身而視為解決。已掃日報至 2026-08-29 無後續；官方頁面未查證
- （未列入總表：表滿載，2026-09-06）

#### 🔴 2026-08-12：升級方案付款流程新爆計費 bug——PaymentIntent 於確認完成前遭提前作廢

- **GitHub Issue #55982（77 留言、👍 26 反應，2026-08-12 查證）**：升級方案時付款流程失敗——PaymentIntent 在使用者確認付款前即被後端 `void_invoice` 作廢，導致升級無法完成；77 留言已達高互動標準，是本頁互動量最高的付款類 bug（GitHub https://github.com/anthropics/claude-code/issues/55982）
- **同日 Reddit 疑似相關回報（單一貼文，未經證實）**：r/ClaudeCode 用戶回報帳戶已有既有 credits，系統仍要求重新輸入付款資訊；是否與上述 PaymentIntent 作廢同源未見證實，各自獨立記錄（Reddit https://www.reddit.com/r/ClaudeCode/comments/1vm9chm/claude_asking_me_for_payment_details_to_use/）
- **與既有事故的關係（推論）**：本頁已記錄多起用量點數／帳務異常（08-07 Issue #79337、07-20 南韓 $16.7M 帳單等），本次首度集中在「升級付款流程本身失敗」而非「用量計費異常」，屬付款基礎設施層級的新故障面向

#### 🔴 2026-08-07：Fable 5 Max 方案用量點數異常追蹤更新——留言數攀升至 67，延燒逾 18 天

- **GitHub Issue #79337 互動量持續攀升**：**67 留言**（08-07 查證，較 07-25 的 42 留言攀升），延續追蹤自 07-20 Fable 5 成為 Max 標準模型第一天起爆發的用量點數異常，含此前記錄的「靜默降級 Opus 4.8」細節。**與既有事件的關係**：問題延燒逾 18 天，橫跨官方 07-20 Status「Max 誤判、重啟可解決」定性與 07-24（13 reactions）、07-25（42 留言、15 reactions）多輪查證；留言數持續攀升顯示影響擴大而非收斂，是本頁追蹤時間最長的未解計費／配額爭議（推論；官方是否修復、與「誤判」定性的關係均未見新公告釐清）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 🔴 2026-08-04：Reddit 回報 Max 20x 用量在未使用期間半小時內從 0% 衝到 100%，疑似配額計算異常

- **Reddit r/ClaudeAI 週熱門回報**：Max 20x 用量在**未使用 Claude 的情況下**半小時內從 0% 攀升至 100%（週熱門，2026-08-04）。**與既有已知問題的關聯（推論，待證實同源）**：症狀與 [[entities/claude-code]] 已記錄的 GitHub Issue #41788〈Max 20 plan: rate limit 100% exhausted within ~70 minutes after reset〉（版本迴歸 bug）高度相似，皆為用量在短時間、無明顯使用下被耗盡；兩者是否同根因、同批受影響用戶均未見交叉確認，不可合併（Reddit https://www.reddit.com/r/ClaudeAI/comments/1vf6i4y/max_20x_usage_went_from_0_to_100_in_half_an_hour/）
- （未列入總表：表滿載，2026-09-06）

#### 🔴 2026-08-02：Max 5x → Max 20x 訂閱升級持續失敗，與此前三起已知 issue 同源

- **GitHub Issue #55266**：Max 5x 升級至 Max 20x 失敗，系統回報「Unable to update subscription」；Issue 標題指此問題與此前三起 issue（#10832、#50710、#43118）「same pattern as」，暗示升級流程存在持續性而非一次性的系統問題。**與既有事件的關係**：本頁已多次記錄 Max 計費爭議（06-16 集體訴訟、07-02 升級介面誤導扣費、07-24/25 Fable 5 用量點數異常），本則獨立於「用量計量」之外，聚焦「升級操作本身無法完成」；長期未解可能直接阻擋用戶轉向高階方案，衝擊訂閱轉換率與客服負擔（推論；受影響規模、issue 建立時間、官方回應未見細節）（GitHub https://github.com/anthropics/claude-code/issues/55266）
- （未列入總表：表滿載，2026-09-06）

#### 🔴 2026-07-25：Fable 5 Max 方案異常追蹤更新——留言數攀升至 42，新增「靜默降級 Opus 4.8」細節

- **GitHub Issue #79337 互動量攀升 + 新增技術細節**：**42 留言、15 reactions**（07-25 查證，較 07-24 的 13 reactions 明顯攀升）。新增回報細節：受影響用戶反映系統除要求額外購買用量點數外，還會**靜默降級為 Opus 4.8**執行請求，使用者可能不知情地以為仍在用 Fable 5，實際計費與模型能力已改變。逾 5 天未見官方修復或說明，與 07-20 官方 Status「Max 誤判、重啟可解決」的定性落差持續擴大（推論，待官方回應）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 🔴 2026-07-24：Fable 5 Max 方案計費/配額執行異常持續逾 4 天未解（追蹤 07-20 誤判事件後續）

- **GitHub Issue #79337：Fable 5 成為 Max 標準模型後仍被要求額外用量點數**：13 reactions（2026-07-24 01:16 UTC 查證）。自 07-20 Fable 5 成為 Max 標準模型第一天起，Claude Code 反而要求額外購買 usage credits 才能使用，持續至少 4 天。**與既有事件的關係**：07-20 官方 Status 事件（tnypgb2jbqnq）將此類現象定性為「Max 方案誤判」、建議重啟即可解決；本 Issue 顯示問題未如官方所述經重啟消失。可能是（a）另一個持續性的配額執行 bug、或（b）官方「誤判已修正」的範圍未涵蓋此類個案，待官方釐清（推論，不可認定為同一根因或已解決）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 🔴 2026-07-20：南韓用戶收到 $16.7M 帳單疑似故障，與 07-12/13 已證實帳務錯誤規模相近

- **KED Global：南韓用戶收到 $16.7M 帳單**：報導一名南韓用戶收到 Claude 系統疑似故障產生的 **$16.7 百萬美元**帳單。**與既有事件的關係（推論，待證實）**：金額與 07-12/13 已記錄的「Anthropic 證實 1660 萬美元帳務錯誤」（Tech Times）高度接近（$16.6M vs $16.7M），可能是同一筆已證實錯誤的受害個案首次被具名地區媒體揭露；惟原文摘要遭 RSS 截斷，未見報導連結兩起事件，亦未見官方就此個案回應，**不可認定為同一事件**（Google News/KED Global）
- （狀態隨 07-12/13 條，推論為同一筆已證實錯誤的個案）

#### ✅ 2026-07-20：Fable 5 免費期到期後社群反映存取異常，含官方已證實的 Max 誤判事件

- **Reddit r/ClaudeAI：Max 方案用戶反映無法使用 Fable 5**：Reddit 用戶（score 0，Reddit RSS 抓取機制下分數不可信、僅單一來源）反映 Max 方案疑似無法存取 Fable 5。**與官方 Status 事件吻合**：時間點與 Anthropic Status 頁面同日（07-20 07:35 UTC）公告的「Max 方案用戶被誤判需使用點數才能存取 Fable 5」事件吻合，官方已確認為誤判並建議受影響用戶重啟；官方事件細節詳見 [[entities/claude-code]]（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v1g5yy/so_i_cant_use_fable_with_my_max_plan_ey/；Anthropic Status https://status.claude.com/incidents/tnypgb2jbqnq）
- **Reddit r/ClaudeAI：App 內 Pro 方案顯示異常消失（單一回報，未經證實）**：另一則 Reddit 貼文（score 0，僅單一來源）反映 App 內 Pro 方案顯示異常消失/變動，原因不明。**注意**：與上則 Max 誤判事件同日出現，但官方 Status 頁面僅證實 Max 方案誤判一事，本則 Pro 方案異常未見官方對應公告或其他來源佐證，暫不推論兩者為同一根因，僅並列記錄待後續查證（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v1hiu8/anthropic_nuked_the_pro_plans_on_the_app_for_some/）

#### 🔴 2026-07-12/13：Anthropic 證實 1660 萬美元帳務錯誤，稽核發現企業多收 170 萬美元

- **官方證實大規模帳務錯誤**：Tech Times 報導（20260712，於 07-13 日報顯示）Anthropic 證實一筆 1660 萬美元的帳務錯誤，稽核人員另發現企業客戶被多收 170 萬美元。**對信任度的意涵**：此前多次帳務爭議（HERMES.md bug、Max 升級誤導扣費、儀表板 0% 用量仍收費等）均為個案或社群自行發現，本次是官方證實的具體金額規模最大案例，可能強化企業客戶對 Anthropic 計費系統可靠性的疑慮，尤其在企業支出控管（spend controls）功能剛於 07-04 推出、企業成本敏感度已因競品定價戰而升高的背景下（推論）；具體受影響企業名單、退款機制未見報導（Tech Times https://www.techtimes.com/articles/320266/20260712/anthropic-confirms-166m-billing-error-auditors-find-17m-enterprise-overcharges.htm）

#### 🔴 2026-07-02：Max 升級誤扣費案例 + 客服/退款流程爭議

- **長期 Max 用戶反映升級介面誤導、退款無門**：Reddit r/ClaudeAI（score 未標，07/02 05:44 UTC）一則熱門貼文指出，長期 Max 用戶 5 月底將方案從 $100/月升級到 $200/月時，介面誤導其誤購 $200 credits（而非升級訂閱本身），事後找不到有效退款客服管道，一個多月問題未解決，貼文標題直指「Claude 客服是幾乎所有科技公司中最差的」。**對留存的意涵**：這是繼 [[topics/code-quality-decline]] 用戶退款訴求、6/16 Max 集體訴訟（見「計費切割風波」6/16 條目）之後，另一起具體指向「客服/退款流程缺失」而非「模型能力」的留存風險案例；升級付費流程的 UX 缺陷若造成非自願扣費，可能加劇既有集體訴訟的輿論壓力（推論）（Reddit https://www.reddit.com/r/ClaudeAI/comments/1uliph2/claude_truly_has_the_worst_customer_support_out/）
- **企業合作層級（Select vs Preferred）資訊不透明**：同日 Reddit r/ClaudeAI 另有使用者詢問 Anthropic 企業認證 Select 與 Preferred 合作層級的具體差異（純提問，無官方或社群解答內容）；此分級用語亦見於 [[topics/anthropic-business]] 6/30 DataArt「精選（Select）合作夥伴」條目，但兩層級的權益/門檻差異目前無公開資料，待補充（Reddit https://www.reddit.com/r/ClaudeAI/comments/1ulj6r4/partnership_levels_select_vs_preferred/）
- （未列入總表：表滿載，2026-09-06）

#### 🔴 2026-06-24：隱私政策更新 + 帳號盜刷事件

- **隱私政策更新，新增年齡或身份驗證條款**：Anthropic 更新隱私政策，新增年齡或身份驗證相關條款，2026-07-08 正式生效；影響範圍與具體執行細節未完整公開，用戶應於生效前查閱更新版條款
- **加州用戶帳號遭盜刷，歐元計費未授權費用**：ABC7 報導，加州用戶反映 Claude 帳號遭他人盜用，產生以歐元計費的未授權費用；顯示 Anthropic 計費帳號安全存在漏洞，建議用戶定期檢查帳號活動記錄（ABC7 2026-06-24）
- （未列入總表：距最後動態 74 天，09-22 起若無新回報轉 ⏸）

#### ✅ 2026-05-20：Claude Code 定價溝通混亂事件（Simon Willison 分析）

- **Claude Code 曾短暫顯示為 Max 方案專屬功能**：Anthropic 定價頁在毫無公告的情況下短暫顯示 Claude Code 為 Max 方案（$100–$200/月）專屬功能，引發社群恐慌後已撤回。Simon Willison 深度分析指出問題根源是 Anthropic 的定價溝通策略缺乏透明度。此事件發生於 2026-04-22 前後，但 HN 於 2026-05-19/20 再度廣泛討論，反映社群對 Anthropic 定價透明度的持續不滿
- **建議**：用戶應持續追蹤官方 [Choosing a Plan](https://www.anthropic.com/pricing) 頁面，而非依賴第三方資訊；Anthropic 任何定價頁更動均可能未經公告

#### ⏸ 2026-05-11：Pro 方案 0% 用量仍遭收費

用戶儀表板顯示 0% 情況下，2–3 個提示後被收取 $3.37 Extra Usage；根本問題：1M context window 觸發 API 計費通道，獨立於訂閱用量計量。Anthropic 尚未公告改善。

#### ⏸ 2026-05-05：提示快取窗口悄悄縮短（未公告）

Anthropic 於 4 月初靜默縮短預設 prompt cache 窗口，實質提高 token 消耗速度；為繼 Token 費用估算翻倍（2026-04-29）後第二次被社群自行發現的靜默計費改動。

**2026-04 事故（已封存）**：Token 費用預估靜默翻倍（04-29，⏸ 逾 90 天無後續）、Opus「圍牆內圍牆」事件已修正（04-28，✅）、HERMES.md 靜默計費 bug 官方確認但拒絕退款（04-25，⛔）。原始條目見 [[entities/pricing-archive#2026-04]]。

### 定價與促銷（模型定價、方案設計）

#### 2026-09-05：官方定價頁再爆大改版（新增110+／移除168+段）；同日媒體稱「Anthropic 重置 Claude 限制」（2026-09-06 查證：價格結構未變）

- **Official Docs（claude.com/pricing）機械頁面比對**：頁面新增逾 **110** 個段落（多為 Mtok 計價區間，如 $0.10、$0.20、$0.25、$0.30、$0.50）、移除逾 **168** 個段落（多為依企業人數規模分類的介紹文字，如「20–100 人」「100+ 人」）。
- **字數變化**：頁面整體字數由約 **24,384** 字縮減至約 **20,870** 字；改版後最終呈現方式尚待人工開啟頁面全文確認。
- **與 09-02 條目的關係**：09-02 已記錄同頁「同步大幅改版」但未附具體段落增減數字，本次為機械偵測到的更大規模改版，兩者是否為同一輪改版分次偵測無法從機械 diff 判斷。
- ✅ **已查證**（2026-09-06 查官方定價頁全文）：改版後價格結構已完整取得——牌價、Managed Agents、乘數、內建工具計費、CCU 制皆載於本頁對應各節。段落增減為呈現方式調整，未改變費率。
- **同日媒體標題（Google News／Pasquale Pillitteri）稱「Anthropic Resets Claude Limits」**：見於報導 GPT-6 Astra 上線 Pro／Enterprise／API 的文章副標，惟原文全文未能取得，無法確認具體異動內容。
- **促銷說明頁同日複查**：週用量促銷說明頁（May–August 2026）本次僅頁首／頁尾樣板文字變動，核心內容未見結構性變化；09-13 到期日暫無新證據需修正，惟本次比對範圍有限，不足以確認促銷是否仍生效

#### 2026-09-02：官方更正週用量促銷延長至 09-13（非如期於 08-31 終止）；定價文件新增 Fable 5.1／Mythos 5.1 快取費率；印度盧比訴求互動再攀升

- **Official Docs（support.claude.com）更正促銷狀態**：Claude Code 週用量 +50% 促銷再度延長，新到期日 **2026-09-13**（原記 2026-08-31 到期），適用 Pro、Max、Team。原文：「We've extended this promotion. Increased weekly limits now run through September 13, 2026.」**更正本頁既有記錄**：08-29 條目曾記「促銷如期於 08-31 終止、不再延長」，本次官方更新顯示該促銷實際上又獲延長，並非終止；上方「當前生效的計費規則」與「已失效並移除的規則」均已同步修正（來源：[Claude Code May–August 2026 Weekly Limits Promotion](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion)，2026-09-02）
- **Official Docs（platform.claude.com/docs/en/about-claude/pricing）新增快取費率**：定價頁更新反映 Claude Fable 5.1、Claude Mythos 5.1 的快取讀取／刷新費率降至**標準輸入價的 0.025 倍**（標準快取讀取為 0.1 倍），長對話情境下快取成本較前代最多省下 75%；方案與定價頁（claude.com/pricing）同步大幅改版（新增/移除多段定價說明，完整差異未見比對）。**與模型頁的關係**：Fable 5.1／Mythos 5.1 為官方定價文件首度出現的具體版本號，此前僅見於 08-28 Reddit 社群臆測（[[entities/fable-5]] 懸置標記）；本則為一手來源，強力佐證兩版本已存在。本頁僅記錄快取乘數，兩版本完整基礎 $/Mtok 定價未見公布，暫不列入上方「模型 API 定價現況」表；此快取乘數變動屬本頁「通路與乘數」節範疇，待納入該節乘數對照表（來源：[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、[claude.com/pricing](https://claude.com/pricing)，2026-09-02）
- **GitHub Issue #17432 留言數更新**：留言數由 08-17 查證的 212 增至 **213**，本次首度記錄 reactions 達 **628 👍**（本輪商業類條目互動量最高之功能請求）；訴求內容不變——使用者要求 Anthropic 仿照 OpenAI（ChatGPT）、Google（Gemini）推出印度盧比定價方案，涵蓋 Claude Pro 與 Claude Code 兩項訂閱。與既有記錄相同：07-13 官方回應僅確認 Pro 方案訂閱定價，Claude Code 涵蓋範圍缺口依然存在（GitHub https://github.com/anthropics/claude-code/issues/17432，2026-09-01）

#### 2026-08-29：官方公告週配額改版——09-14 起標準週配額永久 +25%，但 08-31 起不再延續 +50% 促銷，實際減少約 17%

- **官方公告**：Anthropic 官方（[Bluesky @anthropicbot](https://bsky.app/profile/anthropicbot.bsky.social/post/3muaaxs5nx424)）宣布自 **2026-09-14** 起將 Claude Code 標準週配額**永久**調高 **25%**，適用 **Pro、Max、Team 與座位制 Enterprise** 方案；同時本頁已追蹤逾三個月的「週用量 +50% 促銷」（見上方「當前生效的計費規則」）如期於 **2026-08-31** 到期、不再延長。
- **對讀者的實際影響（換算）**：`1.25 ÷ 1.50 ≈ 0.833`——09-14 起的永久週配額約為現行 +50% 加成水位的 83%，即**相較「目前」實際減少約 17%**；BleepingComputer 標題〈Anthropic is cutting Claude Code's current weekly limits by 17 percent〉即以此框架報導，多家媒體同步跟進。
- **與既有沿革的關係**：+50% 促銷自 2026-05-13 起歷經 06-22→07-07→07-12→07-19→08-18 五度延長，本次是首度明確終止且改以「永久」而非「促銷」形式接手，性質從「暫時加成」轉為「基準值調整」——讀者不應再期待第六次延長。
- **來源**：[Bluesky @anthropicbot](https://bsky.app/profile/anthropicbot.bsky.social/post/3muaaxs5nx424)、[BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/)，2026-08-29
- **08-31 跟進（非新事實，社群／媒體評論延燒）**：Hacker News 社群貼文（08-31）與 Android Headlines 分析文章同步討論此次改版，兩者均沿用官方已確認之「相較目前水位實際減少約 17%」換算數字，未提出新增數字；Android Headlines 將此定性為「悄悄降規」（quiet nerf），HN 討論串則拿 OpenAI Codex 的配額調整方式相比。**兩者均為社群/媒體評論或推算，非官方新公告**——17% 換算本身已於 08-29 由官方公告＋BleepingComputer 官方測算確認，本則僅補充後續輿論反應層面，不改變上方已記錄之官方規則內容（[Hacker News](https://twitter.com/ClaudeDevs/status/2093742322525810912)；[Android Headlines](https://www.androidheadlines.com/2026/08/anthropic-claude-code-weekly-limits-update.html)，2026-08-31）

#### 2026-08-21：官方查證更正——3,500 萬美元為 Defender Advantage Fund（資助修補開源漏洞組織），非企業導入 Mythos 5 的額度；企業導入本身按標準 token 計費

- **事實更正（2026-09-06 查證）**：四方媒體報導誤把「$35M」與「企業導入 Mythos 5」併為一事，實為兩件事：$35M 是 **Defender Advantage Fund**，資助修補開源漏洞的組織，非企業導入額度。
- 出處：[Anthropic Blog](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)，2026-08-21。
- **企業導入 Mythos 5 掃描本身**：Claude Enterprise 方案可在 Claude Security 產品線跑 Mythos 5 漏洞掃描，**按既有方案的標準 token 用量計費，無須加購**；模型能力釋出面詳見 [[entities/mythos]]，產品功能細節見 [[entities/claude-security]]。
- **與「我的方案現在有什麼」表的關係**：兩件事皆非該表涵蓋的一般訂閱方案優惠，不列入表內。

#### 2026-08-21：Techzine 報導 Anthropic 允許企業將 AI 資料存放於自有雲端環境（單一來源，後於 09-03 由官方 EFS 公告確認）

- **Techzine Global（2026-08-21 07:46 UTC）**：報導稱 Anthropic 讓企業客戶可將 AI 資料存放在自有雲端環境，僅標題可用，未見實作機制（是否限特定雲端商、涵蓋哪些模型／方案）、生效時間或官方公告連結。
- **與下方 08-20 資料保留政策報導的關係**：時間相近、同屬企業資料治理，但措辭不同（一稱「自有雲端存放」、一稱「保留政策調整」），標題層級無從判斷是同一政策的兩種描述或兩項獨立變動。**後續（2026-09-03）**：官方 09-01 的 EFS 公告同時涵蓋兩者（資料留在客戶自有雲端＝Anthropic 端不留存）。
- **企業資料存放於自有雲端環境——官方已確認（2026-09-03 查證）**：Anthropic 09-01 公告 Enterprise Frontier Safeguards（EFS），明載企業用量資料存放於**客戶自行控制的雲端基礎設施**而非 Anthropic 端；EFS 免費，自 2026 年秋季起分階段對企業客戶開放。08-21 Techzine 標題所述即此政策的預告（[Anthropic Blog](https://www.anthropic.com/news/enterprise-frontier-safeguards)，2026-09-01；詳見 [[topics/anthropic-business]]「戰略合作」EFS 條目）

#### 2026-08-20：路透社／彭博社（消息人士）報導 Anthropic 計畫調整企業資料保留政策（未經官方證實）

- **Reuters（19:34 UTC）／Bloomberg（17:51 UTC）同日報導**：兩家均引述消息人士稱 Anthropic 計畫調整企業客戶的資料保留政策；Bloomberg 標題聚焦「進階 AI」的適用範圍。兩則僅標題與極簡導言可用，調整內容（保留天數增減、涵蓋模型範圍、生效時間）未見細節。
- **與既有「30 天資料保留政策」的關係（見 2026-06-09 條目）**：本頁已記錄 Fable 5／Mythos 5 流量（含 AWS Bedrock）強制保留 30 天；本則「計畫調整」是否針對此政策、方向為何均未見細節，不可推定延長或縮短。
- **與競品動態的呼應**：同期 The Register／TechCrunch 報導 OpenAI 祭出「零資料保留」（zero data retention）承諾搶攻 Anthropic 企業客戶，被解讀為競爭回應，詳見 [[topics/competitor-landscape]]「OpenAI ChatGPT Work / GPT-5.6」子區塊。
- **企業資料保留政策調整——官方版本為 EFS（2026-09-03 查證）**：08-20 Reuters／Bloomberg 匿名消息稱 Anthropic 計畫調整企業資料保留政策；官方 09-01 公告的 Enterprise Frontier Safeguards 即其落地形式——資料留在客戶自有雲端、Anthropic 端不留存，並搭配濫用偵測。官方公告**未載**媒體先前傳的「保留天數」數字，該口徑僅為媒體稱（Reuters、Bloomberg），不得視為官方數字（[Anthropic Blog](https://www.anthropic.com/news/enterprise-frontier-safeguards)，2026-09-01；詳見 [[topics/anthropic-business]]「戰略合作」EFS 條目）

#### 2026-08-19：DevOps.com 稱「暫時性用量提升」當晚到期，與週用量 +50% 促銷延長是否同一時程尚無法確認

- ✅ **已查證**（2026-09-06）：DevOps.com 所稱「當晚（08-19）到期」與 08-18 官方確認的延長，為**同一促銷的當期到期日被延長**——促銷歷次到期日 07-19→08-18 前後→08-31→09-13，DevOps.com 報導描述的正是其中一次到期日交接點，之後即被延長，與本頁時序不矛盾。
- **與既有記錄的關係**：目前生效的計費規則仍以 08-18 官方公告為準——+50% 促銷持續至 2026-08-31，見上方「當前生效的計費規則」。本則「暫時性用量提升」若確為獨立的另一項時程調整（如 05-19 記錄的「5 小時使用量加倍」類臨時優惠），到期後額度是否縮減仍待官方文件或後續報導證實。

#### 2026-08-18：Claude Code 週用量 +50% 促銷再度延長至 2026-08-31，Google News 另傳「滾動限額加倍」但用詞與官方數字不一致

- **官方確認再延長**：Hacker News 轉載 support.claude.com 公告（276 分，2026-08-18 17:02 UTC）確認 Claude Code 週用量 +50% 促銷再度延長，運作期間由原訂 **2026-05-13** 起延續至 **2026-08-31**；適用 Pro／Max／Team 及舊制席位制 Enterprise 使用者，**Free 方案與消耗制（consumption-based）Enterprise seat 不適用**；僅調升週用量上限，**5 小時用量上限不受影響**；符合資格帳號自動套用，無需使用者操作。
- **更正本頁既有記錄**：本頁 07-12 條目曾將此促銷與 Fable 5 免費期一併記為「同步延至 7/19」到期，07-21 Reddit 週熱門貼文當時已提示 Claude Code 另有獨立的、約 2026-08-19 到期的延伸方案（見下方 07-21 條目）。本次官方公告證實兩者確為**兩條獨立時程**：Fable 5 免費期確於 07-19 到期並由 07-20 分界取代（不受影響、如常記錄）；週用量 +50% 促銷則持續延長至今，**並未於 07-19 終止**。已同步修正上方「當前生效的計費規則」。
- **Geeky Gadgets：「滾動限額加倍」，用詞與官方「+50%」數字不一致**：Google News／Geeky Gadgets（2026-08-18 11:20 UTC）標題稱「Anthropic Doubles Claude Code Rolling Limits for Paid Plans」，原文僅標題層級可用。時間點與適用對象（付費方案）均與上述官方公告高度重疊，判斷為**同一波政策調整的媒體轉述**，但「加倍（100%）」與官方明載的「+50%」數字不一致——不採信「加倍」數字，以官方 support.claude.com 公告的 +50% 為準；若後續證實為另一項獨立於本次延長的配額調整，需另行查證區分（Google News/Geeky Gadgets）。

#### 2026-08-17：印度盧比定價訴求 GitHub Issue #17432 留言數再攀升，Claude Code 涵蓋範圍仍未見官方確認

- **留言數更新**：GitHub Issue #17432〈Feature Request: India-Specific Pricing Plans (INR) for Claude & Claude Code〉留言數由 07-29 查證的 210 增至 **212**（reactions 未見本次查證更新）。
- **與 07-13 官方回應的範圍缺口依然存在**：07-13 印度盧比計價公告僅確認 Pro 訂閱定價，原始訴求同時提及的 **Claude Code** 是否同步在地化仍未見報導。互動量在官方回應後持續攀升（07-03 留言 205 → 07-29 210 → 08-17 212），可能反映此缺口，也可能只是舊討論串持續累積，無從確認（僅記錄現象）。
- **用詞界定**：本則為使用者訴求延續，**非**官方新公告（GitHub https://github.com/anthropics/claude-code/issues/17432）。

#### 2026-08-10：Claude Sonnet 5 入門定價 $2/$10 永久化，9/1 漲至 $3/$15 的計畫取消（2026-08-26 補記，日報未收錄）

- **官方公告**：Anthropic 官方帳號宣布「making Claude Sonnet 5's introductory pricing permanent」——Sonnet 5 於 6 月發布時載明 $2/$10 per Mtok 為入門價、有效期至 2026-08-31，該價格**維持不變**；原定 2026-09-01 起調至 $3/$15（各降幅 50% 的漲幅）**不會發生**（部分媒體記為 08-11）
- **官方文件佐證（2026-08-26 查證）**：官方模型總覽頁 Sonnet 5 定價欄現為 `$2 / input MTok, $10 / output MTok`，**已無任何 introductory／temporary／到期字樣**；官方定價文件另載明該價格「is now the standard price」
- **⚠️ 收錄延遲**：此則為官方定價變動，但**本站日常追蹤的新聞來源於 08-10～08-26 全數未提及**——官方公告發布於 X 與官方說明中心，兩者皆非本站例行監看範圍。結果是本頁在漲價日前 5 天仍掛著「⏰ 08-31 到期」倒數，讀者會據以做錯誤的成本決策
- **連帶更正**：本頁「模型 API 定價現況」表、「⏰ 倒數中」、[[feature-radar]]、[[topics/model-comparison]]、[[entities/sonnet-5]] 的到期敘述已於 2026-08-26 一併上修
- **缺口已修補（2026-08-28）**：官方 API 定價頁（`platform.claude.com/docs/en/about-claude/pricing`，即記載本次變動的那一頁）已納入官方文件監看清單；同時官方頁的變更偵測由「只說變了」升級為列出新增／移除的段落——本次這種「少了一句到期字樣」的移除型變動，先前的偵測方式看不出來

#### 2026-08-11：官方文件補充 usage credits 僅限網頁版開通，pricing 頁確認 Free 方案功能範圍

- **官方 usage-credits 條目補充限制**：support.claude.com 說明中心確認行動 App 訂閱者無法直接於 App 內開啟 usage credits，須改至網頁版操作；額度用盡後可切換按量計費（API 標準費率）不中斷。詳見上方「方案細節」新增條目
- **claude.com/pricing 確認方案分層**：官方定價頁列出 Free／Pro／Max 各方案，Pro 明確標示涵蓋 Claude Code／Cowork／Design／Science，與 2026-08-12 已記錄之「Free／Pro 功能組成補充」屬同一份官方頁面的不同時點查證，不重複記錄

#### 2026-08-08：官方 Help Center 查證，07-18～21 四方矛盾報導收斂（✅ 已收斂）

- **查證動機**：本頁自 07-18 起累積四則互相矛盾的媒體報導（Tech Times「Max 永久」／Dawn「50% 上限」／the-decoder「Pro 導向 API 計費」／Reddit「轉為 metered」），懸置 20 天無官方澄清。日報來源不含 `support.claude.com`，媒體轉述始終只有標題層級，故直接查證官方說明中心原文。
- **官方結論（[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)）**：2026-07-20 生效。Max 方案／Team premium seats／舊制席位制 Enterprise premium seats — Fable 5 標配，可用至多**週用量上限的 50%**，不額外收費；Pro 方案／Team standard seats／Enterprise standard seats — Fable 5 **不計入方案用量**，改以 usage credits 按 API 費率付費。先前促銷結束於 **2026-07-19 23:59:59 PT**。合格 Pro 與 Team standard seats「qualify for a one-time credit to help with the change」。
- **四則矛盾報導其實各對一半**：Tech Times「Max 永久」✅（Max 確為標配）、Dawn「50% 上限」✅（標配確有 50% 週上限）、Reddit「轉為 metered」✅（但那是講 Pro）—— 三則各自描述不同 seat 層級卻都未指明層級，才被記成互斥（推論）。
- **一次性 credit 金額 ✅ 已於 2026-08-22 官方查證為 $100（此前僅媒體數字）**：官方促銷條目載明 Pro 每帳戶 $100、Team 每 standard seat $100（每組織上限 $2,500），領取窗 2026-08-02 關閉、credits 2026-09-17 到期、不限 Fable 5 可用於任何模型（[官方條目](https://support.claude.com/en/articles/15862783)）。先前 XenoSpectrum／XDA／nerdzap 的 $100 說法事後證實正確，但當時無官方佐證，本頁按分級紀律標為媒體數字屬正確處置。credits 購買方式亦有歧異——官方寫「Add funds 自行輸入金額」，XenoSpectrum 稱固定包（$45 買 $50／$200 買 $250／$700 買 $1,000），以官方為準。
- **usage credits 的隱性風險（[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)）**：credits 為 opt-in、預設關閉（`Settings > Usage`），可設 auto-reload（每日兌換上限 $2,000）。開啟後方案用量上限不再是硬停止——Claude 繼續回答並從 credits 扣款，體感與額度內無異。此即 08-01 XDA「多數人從沒注意到」報導所指的計費異動（見下方同組條目），至此獲官方文件佐證。
- **官方 Help Center 未把此事寫進 Release notes**：[Release notes](https://support.claude.com/en/articles/12138966-release-notes) 只記模型發布與功能（07-24 Opus 5、07-09 Reflect、07-01 Fable 5 恢復），方案／配額／計費改制不在其中——代表即使把該頁納為來源，此類異動仍抓不到（流程缺口見 `wiki/log.md` 2026-08-08 Query 條目）。

#### 2026-08-01：XDA 報導多數用戶未留意 Fable 5 免費促銷已悄悄改變計費方式（媒體視角補充，非新事實）

- **XDA：免費促銷附帶靜默計費異動，多數用戶未察覺**：XDA 文章稱先前 Fable 5 相關的 $100 免費體驗促銷附帶改變了 Claude 計費方式，多數使用者並未留意。**與既有事實的關係（推論，待證實是否同一事件）**：本頁已記錄 Fable 5 免費期歷經多次延長（06-09→07-01→07-07/08→07-12→07-19）後轉為 usage-based billing；本則僅標題可用，無費率、額度換算或生效時間等新細節，無法確認是同一轉換事件或另一項獨立異動。若為同一事件，本則的獨特角度是「多數用戶未察覺計費已變」的認知落差，呼應本頁一貫記錄的「靜默計費改動損傷信任」風險（見 [[topics/anthropic-business]]「商業風險」表）（Google News/XDA）

#### 2026-07-29：印度盧比定價訴求 GitHub Issue #17432 互動持續攀升，距官方 07-13 回應已 16 天

- **互動量新高**：GitHub Issue #17432〈Feature Request: India-Specific Pricing Plans (INR) for Claude & Claude Code〉留言數由 07-09 查證的 205 增至 **210**、reactions 由 **598** 增至 **613**，遠超「高」門檻（GitHub Issue ≥50 留言）。
- **與已回應事實的張力（非官方政策異動）**：Anthropic 於 07-13 推出印度盧比計價（Pro 方案 Rs 2,000/月，見下方條目），當時視為對此訴求的官方首度回應。惟 issue 原始訴求同時提及 **Claude 與 Claude Code**，07-13 公告僅確認 Pro 訂閱定價，Max/Team/Enterprise 與 Claude Code 是否同步在地化未見報導；互動量在官方回應後仍攀升，可能反映此範圍缺口，也可能只是舊討論串持續累積，兩者均無從確認（僅記錄現象）。
- **用詞界定**：本則為使用者訴求延續，**非**「Anthropic 將推出新方案」——尚無官方聲明承諾進一步異動（GitHub https://github.com/anthropics/claude-code/issues/17432）。

#### 2026-07-24：Claude Opus 5 發布，官方稱定價為 Fable 5 的一半，與此前 MarkTechPost「維持原定價」說法方向不一致

- **官方公告**：Anthropic 發布 Claude Opus 5（[官方公告](https://www.anthropic.com/news/claude-opus-5)，2026-07-24 16:57 UTC，Hacker News 1587 分），稱定價為 Fable 5 的一半，相同成本下效能較 Opus 4.8 大幅提升；現為 Max 方案新預設模型、Pro 方案最強可用模型，取代 Opus 4.8 次旗艦地位。**與既有訊號的落差**：MarkTechPost（2026-07-14，見 [[topics/model-comparison]] 延伸閱讀）此前稱 Opus 5 將「維持原 Opus 定價」，與「砍半」方向不同；官方公告未給 $/Mtok 數字，以 Fable 5 $10/$50 推算半價約 $5/$25，屬讀者端推算而非官方確認。**後續（2026-08-08 查證、2026-08-20 複查一致）**：官方文件載明 **$5 / $25**，「unchanged from Claude Opus 4.8」——推算獲證實，兩則報導的方向差異隨之解消（同一組數字的兩個對照對象）。見上方「模型 API 定價現況」；能力面見 [[entities/opus-5]]。

#### 2026-07-21：Reddit 週熱門回顧 Fable 5 免費期延長史，社群觀察指向 Max／Team Standard 轉為計量存取

- **延期歷史彙整 + Max/Team Premium 稱轉為計量存取**：r/artificial 週熱門貼文（2026-07-20 07:56 UTC）整理 Fable 5 免費存取期限延後歷程（6/22→7/7→7/12→7/19），並指出 7/20 起 Max 與 Team Premium 方案轉為**計量存取（metered）**。**與既有矛盾訊號的關係**：本則社群來源方向與既有 07-19 Tech Times「Max 永久」說法相反，較接近 Dawn「用量上限 50%」與 07-18 Startup Fortune／the-decoder.com「收緊 Max/Team Premium 配額」的方向；惟本則僅為 Reddit 週熱門貼文，非官方公告，與既有官方層級矛盾報導並列記錄，不可視為官方定案（推論）。
- **Claude Code 額外延伸方案提醒**：同則貼文提醒讀者 Claude Code 另有 **2026-08-19** 到期的延伸方案值得關注，暗示 Claude Code 訂閱層與 Fable 5 免費期為兩條獨立的計費時程；具體延伸方案內容未見報導細節，待後續補充。
- **07-17 早期信號（回溯記錄）**：r/artificial 週熱門貼文（2026-07-17 18:48 UTC，標題帶問號，非確認事實）反映部分月付 $200 的 Claude.ai Max 用戶回報 Fable 5 存取遭停用；早於 07-18 官方訊號分歧報導兩天出現，可視為社群端最早察覺存取異動的訊號，但當時未經證實（推論：與 07-18/07-19/07-20 後續報導方向一致，顯示社群端偵測先於媒體確認）（Reddit r/artificial）

#### 2026-07-19：免費期到期日當天，Fable 5 存取政策再添兩則標題層級報導，仍未消解矛盾

- **Tech Times：「Max 永久、Pro Credits-only」（2026-08-10 官方查證確認屬實）**：標題稱 Claude Fable 5 訂閱限制調整為「Max 方案轉為永久提供、Pro 方案改為 Credits-only」。經 2026-08-08 官方 Help Center 查證（見上方「官方 Help Center 查證」段），此標題所述**方向正確**：Max 方案／Team premium seats 確為標配（不脫離、"permanent" 意指不下架），Pro 方案／Team standard seats 確改為 usage credits 按 API 費率計費——與 07-18 Startup Fortune／the-decoder.com「Pro 導向 API 計費」方向一致，兩則報導確實是同一政策的「方案別拆解」，非互斥（[Tech Times](https://www.techtimes.com/articles/320905/20260718/claude-fable-5-ends-subscription-limbo-permanent-max-credits-only-pro.htm)，2026-07-18）
- **Dawn：「併入 Max、Team Premium，用量上限 50%」**：標題稱 Anthropic 將把 Fable 5 模型以「50% 用量上限」的方式併入 Max、Team Premium 方案。**與 Tech Times 報導的落差**：若 Max 方案是「永久提供」（Tech Times），與本則「50% 用量上限」的描述無法完全對照——「永久」可能指存取權限本身不下架，「50% 上限」則可能指配額分配比例，兩者未必互斥，但缺乏官方公告確認具體機制（Google News/Dawn，07-18 12:50 UTC）
- **⚠️ 不擇一呈現**：本頁採「如實記錄矛盾」原則，兩則新報導均為標題層級資訊，與 07-18 已記錄的矛盾訊號一併保留，待官方於免費期到期後進一步公告釐清。

#### 2026-07-18：Fable 5 存取政策訊號分歧——「收緊限制」vs「設為永久」同日並存

- **收緊限制方向**：Startup Fortune（「Anthropic Limits Claude Fable 5 Access as It Runs Out of Compute」）與 the-decoder.com（另有媒體同步報導，「Anthropic slashes Claude Fable 5 limits in Max and Team Premium and pushes Pro users toward API pricing」）同日報導，Anthropic 因運算資源吃緊，大幅縮減 Max 與 Team Premium 方案的 Fable 5 使用配額，並將 Pro 方案用戶導向改用 API 計費。**與 Meta 運算力租賃洽談的呼應（推論）**：同日 [[topics/anthropic-business]] 記錄 Meta 據報洽談以 100 億美元規模租賃運算力予 Anthropic，兩則報導共同指向「Anthropic 運算需求已超出現有供給」的同一根因——對外租算力、對內收緊高階模型配額，是同一資源缺口下的一體兩面（推論）。
- **設為永久方向（矛盾訊號）**：Simon Willison 部落格同日（06:00 UTC，早於上述兩則收緊限制報導）引述官方 `@claudeai` Twitter 帳號發布內容，標題為「Claude make Fable 5 permanent」（將 Fable 5 設為永久）；原文於標題引述後即截斷，無更多細節可查證。
- **⚠️ 如實記錄矛盾，不擇一呈現**：兩則方向相反的報導同日出現，可能反映（a）官方公告本身存在時間差或表述模糊、（b）「設為永久」specifically 指某項功能/免費層級的一部分而非整體 Fable 5 免費存取、或（c）媒體對同一份公告有不同解讀。目前生效的免費期到期日仍為 **2026-07-19**（見上方「當前生效的計費規則」），實際政策走向待 7/19 前後官方進一步公告釐清。

#### 2026-07-17：交易員押注 Fable 5 免費期將第四度延長（市場猜測，非官方，07-18 獨立來源佐證）

- **市場押注，非官方公告**：Proactive financial news 報導交易員押注 Anthropic 將第四度延長 Claude Fable 5 免費使用期限。**注意**：此為財經媒體對交易員市場行為的報導，非 Anthropic 官方公告，目前生效的到期日仍為 **2026-07-19**（見上方「當前生效的計費規則」），未見變動。
- **07-18 獨立來源佐證**：Yahoo Finance UK（另有媒體同步報導）獨立報導同一押注方向，強化此市場預期訊號的傳播度，非新增事實。
- **對既有延長序列的意涵（推論）**：Fable 5 免費期已延長三次（06-09 原訂 6/22 → 07-01 明確 7/7 → 07-07/08 延至 7/12 → 07-12 再延至 7/19），交易員押注第四度延長顯示市場預期 Anthropic 對 usage-based billing 轉換將持續採取謹慎策略，與既有「Anthropic 對 Fable 5 計費轉換態度謹慎」的判斷（見 07-12 條目）方向一致；惟押注本身不構成事實依據，7/19 後實際走向仍待官方公告確認（Google News/Proactive financial news）

#### 2026-07-13/14：印度盧比在地化定價正式推出，回應長期社群訴求（重大）

- **官方推出印度盧比計價，Pro 方案 Rs 2,000/月**：TechCrunch、NDTV、Times of India、bestmediainfo.com 同步報導，Anthropic 為美國以外最大市場印度啟動盧比計價，Pro 方案訂為每月 **Rs 2,000**。**對採用率的意涵**：是官方首度正式回應下方 07-03 條目記錄的 GitHub Issue #17432（reactions 598、留言 205，長期無官方回應）印度在地化定價訴求，若能提升印度市場訂閱轉換率，將直接驗證此前「未回應在地化定價將影響全球最大開發者社群之一的轉換率」的推論；具體匯率換算基準、是否同步適用 Max/Team/Enterprise 方案未見報導細節，待後續補充（NDTV「Anthropic Starts India Pricing For Claude AI, Pro Plan At Rs 2,000」；TechCrunch「Anthropic starts localizing Claude pricing for India, its biggest market after the US」）
- **API 定價跨供應商比較難度浮上檯面（The Register）**：Google News/The Register（多家媒體同步報導）分析指出 Anthropic tokenizer 設計較複雜，使 API 定價與跨供應商成本估算更難以直接比較；僅標題式報導，無具體量化細節，惟此議題與印度盧比在地化定價同日出現，共同凸顯 Anthropic 全球定價透明度議題（推論：一為訂閱端在地化，一為 API 端可比性，兩者性質不同，不宜混為一談）
- **社群對 Fable 5 訂閱去留持續揣測（非官方，無新事實）**：Reddit r/ClaudeCode（2026-07-14，無週熱門標記）用戶詢問 Fable 5 是否會退出訂閱方案改為純點數（credit-based）付費，反映月付 $100 訂閱用戶對加購點數的不滿；同時 Reddit r/ClaudeAI · 週熱門（2026-07-10）另一貼文推論，隨 OpenAI Sol 上市成為同級競品，現階段將 Fable 5 移出訂閱方案的可能性不高，如同 Opus 4.5 上市後未被移出訂閱方案的先例。**注意**：兩則均為社群揣測，非官方公告，與上方「Fable 5 免費使用期限延長至 7/19 後是否轉 usage-based billing」的既有未決問題方向一致，可視為市場對該懸而未決政策的持續關注訊號（推論）（Reddit r/ClaudeCode；Reddit r/ClaudeAI）

#### 2026-07-12：週用量 +50% 促銷再延長至 7/19，Fable 5 免費期同步順延

- **官方公告**：Anthropic 官方公告（Hacker News 轉載，support.claude.com，2026-07-12 18:01 UTC）將原訂 5–7 月週用量 +50% 促銷再延長，效期由 7/13 延至 **2026-07-19**；適用範圍限定 **Pro／Max／Team 及舊制（席位制）Enterprise 方案**，**Free 方案與用量制 Enterprise 席位不適用**，5 小時額度不受影響。
- **Fable 5 免費期同步順延**：Fable 5 原訂 7/12 到期的免費使用期限（Pro/Max/Team 每週配額含 50% 用量）隨此公告同步延至 **7/19**，為繼 06-09（原訂 6/22）、07-01（明確 7/7）、07-07/08（延至 7/12）之後第三度延後轉為 usage-based billing 的時程。
- **競爭角度（推論）**：Google News/The Economic Times、Simon Willison（2026-07-12）分析指出，此次延長與 GPT-5.6 Sol 被業界認為屬同級模型有關，Anthropic 可能藉延後轉付費時程維持促銷期間對用戶的競爭吸引力；模型能力面比較詳見 [[entities/fable-5]]、[[topics/model-comparison]]。
- **注意**：連續三次延後同一到期日顯示 Anthropic 對 Fable 5 計費轉換採取謹慎策略（呼應既有 07-07/08 條目判斷），本次是首次明確與競品能力對標掛鉤的延後理由。

#### 2026-07-10：Wired 報導聚焦「Anthropic 要消費者為 Fable 5 付費」

- **媒體視角補充，非新政策**：Wired 報導「Anthropic Wants You to Pay Up for Claude Fable 5」，聚焦 Anthropic 要求消費者為使用 Fable 5 額外付費的趨勢。**注意**：此報導呼應既有 07-01（7/7 起 usage-based billing 生效）與 07-07/08（免費期限延長至 7/12）已記錄的政策時程，未見新的定價數字或時程異動，屬媒體對既有政策走向的解讀補充（Wired，2026-07-09 18:30 UTC）

#### 2026-07-07～08：Fable 5 免費使用期限再延長 5 天至 7 月 12 日

- **官方延長免費期**：Times of India、Forbes 報導 Anthropic 將 Claude Fable 5 免費使用期限再延長 5 天，由原定 2026-07-07 延至 **2026-07-12**；Pro/Max/Team 每週配額含 50% Fable 5 用量的過渡期同步順延。**注意**：這是繼 06-09（原定 6/22 轉消費制）、07-01（明確 7/7 為 usage-based billing 生效日）之後第二次延後轉換時程，顯示 Anthropic 對 Fable 5 計費模式轉換採取謹慎、分批延後的策略，可能反映對用戶留存或計費系統就緒度的顧慮（推論）（Times of India https://timesofindia.indiatimes.com/technology/tech-news/anthropic-extends-claude-fable-5-free-offer-till-july-12-eligibility-and-other-details-explained/articleshow/132255396.cms；Forbes https://www.forbes.com/sites/sandycarter/2026/07/07/claude-fable-5-extends-by-five-more-days-10-moves-to-make-now/）

#### 2026-07-04：企業版 Claude 支出控管（spend controls）功能上線

- **官方推出企業支出控管功能**：Tech Times 報導（07-04），企業導入 agentic AI 後帳單頻繁超出預算成為普遍痛點，Anthropic 針對企業客戶推出 Claude 支出控管功能協助管理成本。**注意**：報導僅描述功能定位，未揭露具體控管粒度（部門/團隊層級預算上限、per-user 報表、即時警報等 [[topics/enterprise-cost-management]] 長期呼籲的功能是否齊備）；是官方首次針對企業成本失控問題推出產品化解法，而非僅靠配額縮減或計費政策調整（推論：對正面臨 Uber 式成本失控的企業客戶構成留存誘因）。詳見 [[topics/anthropic-business]]、[[topics/enterprise-cost-management]]（Tech Times https://www.techtimes.com/articles/319687/20260704/claude-enterprise-spend-controls-arrive-agentic-ai-bills-blow-past-budgets.htm）

#### 2026-07-03：印度盧比定價需求（✅ 已於 2026-07-13 獲官方回應，見上方 07-13/14 條目）

- **GitHub Issue 要求 INR 在地化定價方案（持續發酵，互動量攀升）**：印度用戶在 `anthropic/claude-code` Issue #17432 要求 Anthropic 推出盧比計價方案，比照 OpenAI（ChatGPT）、Google（Gemini）已有的在地化定價。互動量持續攀升：留言數維持 **205**、reactions 由 👍594 增至 **598**（2026-07-09 查證），為近期社群需求類 issue 中互動量顯著較高者之一。**注意**：純社群 feature request，Anthropic 至今（07-09）仍無官方回應或時程承諾；若 Anthropic 未來跟進在地化定價，將直接影響印度市場（全球最大 AI 開發者社群之一）的訂閱轉換率（推論）（GitHub https://github.com/anthropics/claude-code/issues/17432）
- **✅ 已解決（2026-07-13 更新）**：Anthropic 於 07-13 正式推出印度盧比計價（Pro 方案 Rs 2,000/月），為此需求首次獲得官方正式回應，長期無回應狀態結束；詳見上方「2026-07-13/14：印度盧比在地化定價正式推出」條目

#### 2026-07-02：第三方實測確認 Sonnet 5 促銷定價，籲設為預設路由模型

- **dev.to 第一手定價實測**：作者計算確認 Anthropic 已將 Sonnet 5 以 $2/$10（每百萬 token）廣泛開放，優惠將持續至 **2026-08-31**，與官方 07-01 公告數字一致；文章建議開發者應將 Sonnet 5 設為**預設路由模型**而非僅作為用量上限的備援，以最大化促銷期內的成本節省（dev.to https://dev.to/tokenmixai/i-did-the-math-on-claude-sonnet-5-the-60-opus-discount-is-real-but-temporary-31pf）
- **注意**：優惠當時明確為「temporary」，8/31 後走向未見公告 —— **後續（2026-08-10）：Anthropic 宣布此定價永久化，取消 9/1 漲價，本則的到期風險已解除**（見下方 2026-08-10 條目）

#### 2026-07-01：Claude Sonnet 5 促銷定價 + Fable 5 計費架構調整

- **Claude Sonnet 5 促銷定價**：$2/Mtok（輸入）、$10/Mtok（輸出），發布時載明有效期至 2026-08-31（**該到期日後於 2026-08-10 取消，定價永久化**）；Claude Code 用戶以此定價使用新預設模型，相較 Opus 4.8 估計省 60% 成本。**對採用率的意涵**：若 Claude Code 預設路由切換至 Sonnet 5，重度使用者的月均 API 費用可能顯著降低，有助於緩解近期配額縮減導致的訂閱留存壓力（推論）。
- **Fable 5 計費架構調整**：Pro/Max/Team 方案 2026-07-07（7/7）前每週配額含 50% Fable 5；2026-07-07 後改為 usage-based billing（依用量計費）；Enterprise 方案需聯繫帳戶主管確認條件；定價細節另行公告。**注意**：此架構意味 7/7 後 Pro/Max 訂閱用戶使用 Fable 5 將不再包含在訂閱配額內，須另計費用；對重度使用 Fable 5 的用戶構成成本衝擊風險（推論）。**與 06-09 舊公告銜接說明**：06-09 條目記錄 Fable 5「6/22 前含括於訂閱、之後改為消費制」，本次公告明確 6/22–7/7 為過渡期（每週配額仍含 50% Fable 5），7/7 才是 usage-based billing 正式生效日；兩則公告方向一致、非互相矛盾，但 Anthropic 並未使用「過渡期」字眼，此銜接判斷為由兩則公告推得（推論）。此調整與同日公布的 Sonnet 5 促銷定價同屬毛利率相關政策，對公司財務面的意涵詳見 [[topics/anthropic-business]]。

#### 2026-06-26：Max 5x × 2 vs Max 20x × 1 方案分析

- **社群發現：兩個 Max 5x 帳號可並行兩個 session，性價比策略受關注**：Reddit 用戶（r/ClaudeAI）分析指出，雙 Max 5x 帳號架構可**同時**運行兩個獨立的 Claude Code session，對需要並行工作流的獨立開發者而言可能更具彈性，單一 Max 20x 帳號無法同時跑兩個 session（Reddit https://www.reddit.com/r/ClaudeAI/comments/1ug6kjv/two_max_5x_accounts_cost_the_same_as_one_20x_and/）
- **⚠️ 價格更正**：原始 Reddit 貼文與本頁前版將 Max 5x 誤植為 $50/月（兩個合計 $100 = 一個 Max 20x）；查證 2026-05-14 官方政策公告原文（xda-developers、dev.to）確認 **Max 5x 實際為 $100/月、Max 20x 為 $200/月**，兩個 Max 5x（$200）與一個 Max 20x（$200）費用相同，而非原貼文所述的 Max 5x×2 = Max 20x×1 的低價組合；性價比論點仍成立（可並行兩個 session），但費用比較基準已修正
- **適用場景**：主要利好獨立開發者與小型團隊；企業用戶因合規與帳號管理需求，不一定適合多帳號架構（多帳號合規邊界見「計費切割風波」2026-05-17 條目）
- **注意**：此為社群分析，Anthropic 官方未就多帳號策略表態；使用前仍需確認 ToS 合規邊界

#### 2026-06-09：Claude Fable 5 定價發布

- **Fable 5 定價**：$10 input / $50 output per million token（double Opus 4.8）；context window 1M；最大 output 128K
- **6/22 前含括於訂閱**：Pro / Max 訂閱用戶 6/22 前免費使用 Fable 5，之後改為消費制（enterprise consumption-based plan 或 API 直接計費）
- **Mythos 5**（無護欄完整版）：僅限授權用戶，定價比 Fable 5 更高，細節未公開
- **30 天資料保留政策**：Fable 5 / Mythos 5 所有流量（含 AWS Bedrock）強制保留 30 天，資料離開 AWS 安全邊界；企業應評估隱私影響
- **AWS Bedrock 強制 provider data sharing（2026-06-21 新增）**：AWS Bedrock 的 Fable 5 model card 顯示，客戶須同意啟用 `anthropic.model-invocation-logging`（即 provider data sharing），Anthropic 可存取推理日誌；金融、醫療等受嚴格資料合規監管的行業在採購決策前需評估此條件（dev.to 2026-06-21）

#### 2026-05-23：模型別名退役警示

- **⚠️ claude-opus-4-20250514 與 claude-sonnet-4-20250514 退役（2026-06-15）**：Anthropic 確認這兩個模型版本將於 6/15 正式退役，使用舊版別名（如 `claude-opus-4-0`、`claude-sonnet-4-0`）的生產環境程式碼將開始失敗。需在 2026-06-14 前遷移至新版模型 ID（如 `claude-opus-4-5-20251001`、`claude-sonnet-4-6-20260101` 等）
- **Max 方案實質差異說明**：dev.to 分析文章確認 Max 方案不僅是「更多用量」，而是在 context window 長度、Claude Code 可用額度、優先排隊等方面有結構性不同；Max 5x（$100/月）vs Max 20x（$200/月）在 agentic 工作流上的差異尤其顯著

#### 2026-05-13：Anthropic 定價主導權強勁

The Information 報導企業客戶即使面對成本上漲仍持續採用；Anthropic API 定價策略短期維持強勢。

### 配額與速率

#### 2026-08-21：Reddit 回報本次配額重置後 token 分配出現明顯變化（單一貼文，2026-08-21 指控，已掃日報至 2026-09-06 無後續；官方頁面未查證）

- **r/ClaudeCode（2026-08-21 09:26 UTC）**：使用者回報本次配額重置後，token 分配出現明顯變化，貼文未附具體帳號數據、變化方向（增加或減少）或方案別；Reddit RSS 抓取 score 恆為 0，非真實低互動指標，亦未見「週熱門」標記，暫不視為已具系統性訊號強度的個案。
- **與既有配額異常回報的呼應（推論）**：與本頁已記錄之多起配額/用量異常回報（如 08-14 Max 方案 session 額度異常耗盡、08-12「用量限制遭調降」疑慮）同屬「使用者感受配額被調整、官方未公告」的重複性模式，惟本則未提供具體方案別或變化方向，訊號強度較既有紀錄更弱。
- **配額重置機制是否有變動**：僅單一 Reddit 回報（https://www.reddit.com/r/ClaudeCode/comments/1vubdkb/huge_change_in_token_allocation_this_reset/），官方至今無對應公告。

#### 2026-08-12：官方文件釐清 usage limits 與 length limits 為兩種不同機制；同日再現「用量限制遭調降？」社群疑慮（單一貼文，2026-08-12 指控，已掃日報至 2026-09-06 無後續；官方頁面未查證）

- **官方 Help Center：《How do usage and length limits work?》（2026-08-12 查證）**：官方文件說明 usage limits（隨對話長度、複雜度、啟用功能、模型、effort 等級等變動的「額度」）與 length limits（單則訊息／對話長度上限）是兩種不同概念；不同方案（Pro／Max／Team 等）的額度規則亦不同。此文件首度明確說明 usage limits 具動態性，而非固定額度（來源：[How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)）
- **同日 Reddit 疑慮（單一貼文，未經證實）**：r/ClaudeCode 用戶反映近幾天用量額度消耗速度明顯變快，詢問是否遭調降限額；無官方回應佐證，亦未見其他來源佐證（Reddit https://www.reddit.com/r/ClaudeCode/comments/1vm9135/did_anthropic_decreased_the_usage_limit/）
- **與官方文件的潛在關聯（推論，非官方回應）**：若 usage limits 確實隨對話複雜度／effort 等級動態變動（見上方官方說明），使用者感受到的「額度消耗變快」有可能源於任務型態改變而非官方調降限額；惟官方文件未直接回應本則貼文的具體指控，限額本身是否曾調整不可視為已解釋。

#### 2026-07-22：Reddit 週熱門質疑 Anthropic 宣稱的用量提升未反映於實際體驗（單一貼文，2026-07-22 指控，已掃日報至 2026-08-14 無後續；官方頁面未查證）

- **r/ClaudeAI 週熱門貼文**：標題稱「Anthropic Claims 50% usage boost that doesn't exist」，質疑官方宣稱的 50% 用量提升未反映在使用體驗；純圖片型貼文，無帳號數據或官方公告連結佐證。**與既有 +50% 促銷的關係（推論，待證實）**：不確定指涉的是本頁已記錄、07-19 到期的「週配額 +50% 過渡期促銷」，或另一項未見於日報的官方宣稱；若為前者，則與 05-16 已記錄的「Max 20x 用量上限未生效（數學實證）」同屬「官方宣告與實際體驗落差」的重複模式。本則達 Reddit 週熱門「低」門檻但無數據佐證，僅記錄為該落差模式的又一社群訊號（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v3d8iz/anthropic_claims_50_usage_boost_that_doesnt_exist/）

#### 2026-07-16：週用量配額疑似再度提前重置（單一回報，2026-07-16 指控，已掃日報至 2026-08-14 無後續；官方頁面未查證）

- **Reddit r/ClaudeCode 回報週用量提前重置**：一位 Max 用戶回報週用量原約 41%、正常重置日為週二，當日卻提前歸零。單一回報，Reddit RSS 下 score 恆為 0（不代表真實互動量），未標「週熱門」，近 14 天日報無其他來源佐證，暫不升級為系統性訊號（Reddit https://www.reddit.com/r/ClaudeCode/comments/1uxzlyx/did_anyone_elses_claude_code_weekly_usage_reset/）
- **與既有現象呼應**：與 2026-05-16 記錄的「週用量配額意外提前重置（bug 或後端調整）」方向一致，顯示此類配額計時異常非單一事件，近兩個月至少兩次獨立回報（推論，無法確認是否同一根因）

#### 2026-07-07～10：Max 方案額度異常快速耗盡、token 消耗增加 3–5 倍（持續發酵，官方無回應）

- **GitHub Issue #38335（792 留言，2026-07-10 查證）**：反映 Max 方案 CLI session 額度自 2026-03-23 起異常快速耗盡，為近期社群互動量最高的計費類 issue 之一；留言數 07-08（790）→ 07-09（791）→ 07-10（792）持續微幅增加，社群互動已趨於高原期，官方仍無明確回應（GitHub https://github.com/anthropics/claude-code/issues/38335）
- **GitHub Issue #41506（54 留言/29 讚）**：反映 Max（$100/月）方案 token 消耗自 3 月底起增加約 3–5 倍，未見對應功能或用量增加可解釋此漲幅（GitHub https://github.com/anthropics/claude-code/issues/41506）
- **Reddit r/ClaudeAI：「Claude Max 20x: Why did 27% of one session consume 7% of my entire weekly limit?」（2026-07-09）**：使用者具體質疑單一 session 中 27% 的時間消耗掉整週額度 7%，用量計量比例明顯失衡，與 GitHub #38335 反映的異常耗盡現象方向一致
- **Reddit r/ClaudeCode：「Claude Max (20x) weekly limit exhausted in less than a day」**：使用者回報週額度不到一天即用盡（Reddit https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/）
- **對留存的意涵**：多則獨立訊號（2 個高互動 GitHub issue + 2 則 Reddit 貼文）方向一致，指向 Max 方案的用量計量或消耗速率可能存在系統性異常，而非個案；與既有 06-16 Max 集體訴訟（廣告 20 倍實測僅 6–8 倍）同屬「用量承諾與實際體驗落差」的信任問題，Anthropic 至今（07-09）尚未提供官方解釋或修復時程（推論）
- **正面反例（同期出現）**：Reddit r/ClaudeAI · 週熱門（2026-07-09）「5 hour and weekly limits have been reset. Thanks Anthropic!」一則貼文回報 5 小時與週用量額度已被重置並表達感謝；與上述額度異常耗盡投訴同期出現，方向相反，可能反映用戶端因帳號、時段或所屬方案不同而體驗分化，非全面性的正面或負面訊號（推論）

#### 2026-06-30：配額再次縮減（社群反映，Anthropic 無官方公告）

- **社群集體反映配額縮減**：Reddit r/ClaudeCode 多個討論串，訂閱用戶集體反映 Claude Code 配額再次縮減，不滿高漲；Anthropic 無官方公告，縮減幅度與觸發機制不明。結構上，這是 6/16 計費暫停後改以調降配額（而非計費改制）控管成本的另一路徑（推論）。**對採用率的意涵**：重度用戶持續感受配額壓縮可能加速評估競品，「配額縮減 → 不滿 → 切換」的漏斗對訂閱留存構成風險（推論）（Reddit https://old.reddit.com/r/ClaudeCode/comments/1uim4jb/this_is_a_message_for_anthropic_bring_back_the/）
- **注意**：無具名企業規模數據，此條目為訂閱用戶個人反映，非企業層級案例。

**2026-05 配額事故（已封存）**：臨時用量提升優惠＋企業帳單三倍警訊（05-19）、Max 20x 上限未生效數學實證＋促銷時序整理（05-16）、Opus API 速率悄悄調降（05-10）、SpaceX 算力到位速率翻倍（05-07–09）。原始條目見 [[entities/pricing-archive#2026-05]]。

### 計費切割風波（Agent SDK / `claude -p` 訂閱脫鉤，2026-06-16 暫停）

%% 維運備忘：本節已凍結，只減不增；到期日 2027-03-05（本日 +180 天），屆時複查政策是否重啟並決定本節去留 %%

#### 2026-06-18：Agent SDK 計費持續觀望中，B2B 定價差距引發分析

- **DevOps.com 確認計費暫停持續**：DevOps.com 報導 Anthropic 尚未宣布 Agent SDK 計費調整的新時程，訂閱配額維持現狀；社群開發者持續觀望（DevOps.com 2026-06-18）
- **SaaStr 分析：個人 vs 企業 API 定價差距懸殊**：個人用戶以 $20-$200/月訂閱 Claude 即可完成大量工作，而企業 API 呼叫一次要 $1，最多差距可達數十倍；SaaStr 文章指出這使老牌 B2B 軟體廠商面臨根本性競爭劣勢（SaaStr 2026-06-18）
- **HN 社群 AI 花費調查**：HN 討論串顯示 AI 編碼費用分佈極廣——從每月數十美元到超過 $100,000 的全自動化重度用戶均有；反映出 AI 工具從個人玩具到企業基礎設施的多層需求（HN 2026-06-18）

#### 2026-06-17：Ars Technica 深度報導計費暫停始末

- **Ars Technica 詳細報導**：完整梳理 5/13 計費切割公告至 6/16 緊急喊停的事件全貌——背景是重度 Agent SDK 使用者與第三方 app 開發者（Zed、Conductor、T3 Code 等）的強烈反彈；官方 `claude -p` 使用者亦受影響；Ars Technica 指出此決策對依賴 Agent SDK 的第三方 app 開發者商業模式衝擊最大（Ars Technica 2026-06-16）
- **政策現狀**：Agent SDK、`claude -p`、第三方 app 繼續使用訂閱配額，無需額外信用池；週配額過渡性提高 50%（至 7 月 13 日）仍持續

#### 2026-06-16：Agent SDK 計費政策暫停 + Claude Max 集體訴訟

- **Agent SDK 計費切割暫停**：Anthropic 寄信給用戶宣布暫停原定 6/16 生效的計費切割政策，訂閱配額維持現狀，無需領取信用點數。「正在調整方案以更好支持用戶使用方式」，重新推行時間未定（HN score 30，多個討論串）
- **Claude Max 集體訴訟**：原告 Karl Kahn 在北加州聯邦地院提起集體訴訟，指控 Claude Max 5x 與 Max 20x 方案實際使用限制遠低於廣告宣稱。$200/月 Max 20x 實際僅提供 Pro 的 6–8 倍用量，而非廣告的 20 倍；Max 5x 亦類似（CNET、Decrypt 報導）
- **AI 價格戰壓力**：WSJ 分析 AI 定價戰加劇，部分重度用戶比較後發現 DeepSeek $20/月（按用量）等效用途的成本遠低於 Claude Max，引發訂閱價值討論

#### 2026-05-21：6/15 計費影響持續發酵，社群替代方案成熟

- **clarp（drop-in claude -p 替代品）**：開發者開源 clarp，在本地啟動隱藏 PTY 的 Claude Code 互動 CLI，並透過唯讀代理攔截 Anthropic API 串流，重建 `claude -p` 行為；多數專案只需改一個 binary 名稱即可遷移至互動計費軌道，是 6/15 後最直接的工作流保全方案
- **vibe-skill（57M tokens 節省，成本降逾九成）**：開發者開源 vibe-skill，讓 Claude 負責規劃與 diff 審查，實際撰碼任務委派給 Mistral Vibe（低成本執行層）；10 天實測節省 57M tokens，成本降逾九成，Claude 品質的規劃輸出基本保留；是 6/15 計費壓力下最具代表性的混合策略落地案例
- **atrium 工作區設計含 6/15 預案**：macOS 工作區管理工具 atrium 在設計動機中明確提及「規避 6/15 API 計量鎖定」，顯示 6/15 政策已開始影響工具設計決策
- **dev.to 分析文章**：「Anthropic Is Splitting Claude Code's Billing — What It Means for Dev Teams Using Agents」整理 6/15 後對依賴 print mode 自動化工作流程的開發團隊衝擊，clarp 和 vibe-skill 均在文章中被引用為社群因應方案

#### 2026-05-17：`claude -p` 計費衝擊持續、多帳號架構合規紅線

- **`claude -p` 計費調整後的工作流適應**：dev.to 出現以 AI agent 第一人稱視角記錄 6/15 計費規則調整後如何重新設計自動化工作流的文章，代表計費政策變更對長期用戶的實際衝擊仍在延續，開發者正積極找因應方案
- **多帳號 Claude Code 架構合規邊界明確**：文章詳細比較兩種多帳號 Claude Code 使用架構，明確指出其中一種已被 Anthropic 視為違反使用條款（ToS），提醒規模化使用需求的開發者在帳號管理策略上需注意合規邊界；目前僅知「其中一種被禁」，未公開具體判斷標準

#### 2026-05-15：6/15 計費變更社群反應、第三方工具衝擊、官方回應

- **社群情緒**：約六成負面（Max 5x $100 信用池對重度 agent 用量嚴重不足）、兩成理解、兩成觀望
- **受衝擊工具**：Zed、Conductor、T3 Code、Superset；Lanes 聲明不受影響；Zed 已發布應對說明
- **官方回應**：Ars Technica 專訪 Claude Code 產品主管，說明「lean harness」設計哲學，社群認為說明仍不足
- **灰色地帶**：VS Code 擴充套件用量是否計入新信用池，Anthropic 尚未明確答覆
- **Ungate 工具出現**：宣稱可將 Max 訂閱用量路由至 Cursor（$100 = $2,000 API 等值）；**使用前確認 ToS**

#### 2026-05-14：正式宣布 Programmatic 計費分離

Anthropic 宣布 6/15 起 `claude -p`、Agent SDK、Claude Code GitHub Actions 及第三方 Agent SDK app 完全脫離訂閱，改為獨立信用池，按完整 API 費率計費。主要後續效應：
- 部分用戶宣告取消訂閱，轉向 Codex 或 Gemini（見 [[topics/competitor-landscape]]）
- 社群開發者發布 `claude-pee` 繞過工具（PTY 終端模擬），Anthropic 尚未回應
- OpenClaw 等第三方工具恢復，但改走信用池計費（見 [[entities/openclaw]]）

#### 2026-04-25：第三方 Agentic 工具配額限制

The Verge 報導 Anthropic 限制 OpenClaw 等工具；Claude Code 負責人 Boris Cherny：「訂閱方案的設計並非為這類第三方使用模式而生。」（預示 6/15 政策的早期信號）

#### 原定計費架構設計（2026-05-14 公告，2026-06-16 暫停，保留供歷史參考）

⚠️ 此計費架構已於 2026-06-15 暫停、尚未生效，以下為原定設計，當前計費仍依現行方案。

> **2026-06-16 更新**：Anthropic 宣布暫停原定 6/16 生效的 Agent SDK 計費切割政策。目前 Agent SDK、`claude -p`、第三方 Agent SDK 應用的用量仍維持原訂閱配額制，無需額外信用池。重新推行時間未定，將提前通知。

Anthropic 將使用場景切分為**兩條獨立計費軌道**：

**軌道 1：互動式使用（Interactive）— 訂閱涵蓋**

| 涵蓋範圍 | 說明 |
|---------|------|
| Claude.ai 網頁介面 | 人工驅動對話 |
| Claude Code 互動 session | 使用者在終端手動操作 |
| 一般 API 互動呼叫 | 人工觸發的請求 |

→ 費用包含在訂閱月費內，受「5 小時視窗速率上限」管控

**軌道 2：程式化使用（Programmatic）— 信用池計費**

| 涵蓋範圍 | 計費方式 |
|---------|---------|
| `claude -p`（headless / 非互動模式） | 按完整 API 費率，從信用池扣除 |
| Agent SDK 呼叫 | 同上 |
| Claude Code GitHub Actions | 同上 |
| 第三方 Agent SDK app（如 Zed、Conductor、T3 Code） | 同上 |

→ **不享任何訂閱折扣**，信用池用盡後需額外購買

**方案對照表（2026-06-15 後）**

| 方案 | 月費 | 互動用量 | Programmatic 信用池/月 |
|------|------|---------|----------------------|
| Free | $0 | 基本限制 | 無 |
| Pro | $20 | 標準 | $20（按 API 費率） |
| Max 5x | $100 | 5× Pro | $100（按 API 費率） |
| Max 20x | $200 | 20× Pro | $200（按 API 費率） |
| API only | 按量 | — | 直接按 API 費率 |

> **財務衝擊試算**：Max 5x 用戶若程式化使用達週配額 40%，換算 API 費率約需 **$1,000/月**（是月費的 10 倍）

> **過渡緩衝**：6/15 前 Anthropic 臨時將所有付費方案週用量上限**提高 50%**（至 7 月 13 日）

**6/15 計費切割回顧（已暫停）**：原定 2026-06-15 生效的計費切割政策於 **2026-06-16 宣布暫停**，以下為當時社群的主要因應建議，保留供未來政策重啟時參考：

- 盤點所有 `claude -p`、Agent SDK、CI 自動化的月均用量
- 對照各方案信用池上限，評估是否足夠或需升級/備案
- 若使用 Zed、Conductor、T3 Code 等第三方工具，確認其計費切換說明
- 設定費用警報（Anthropic 儀表板有顯示延遲，建議自建監控腳本）

### 成本案例與優化

- **訂閱制對 API 計費的價差已由三個獨立方法論量化在 40–44 倍區間**：Quesma（40 倍，2026-08-11）、modelplane.ai（44 倍，2026-07-23）、cookbook-meter 使用量換算（2026-08-14）互相佐證。
- 具名企業案例、省錢策略與完整時序見 [[topics/enterprise-cost-management]]，本頁不重複列。
- 個人層級費用失控事件（$6,000 徹夜運行、30 天 $514 成本分析等）已併入該頁時序。

---

## 相關議題

- [[topics/competitor-landscape]]（用戶因費用轉向 Codex / Gemini）
- [[topics/code-quality-decline]]（用戶因品質下滑要求退款或降級）
- [[entities/openclaw]]（第三方工具計費政策演變）
- [[topics/enterprise-cost-management]]（企業規模成本案例、省錢策略）

## 參考來源

事件出處見各條目內文連結；2026-04-25 起各日日報均有覆蓋。

- [官方說明文件](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [官方定價頁](https://www.anthropic.com/pricing)
