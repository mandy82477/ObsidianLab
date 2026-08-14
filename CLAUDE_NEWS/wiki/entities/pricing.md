---
page: "entities/pricing"
kind: "entity"
type: "policy"
status: "active（持續調整中）"
domain: "💼 商業"
last_updated: "2026-08-14"
last_news_update: "2026-08-14"
status_main: "active"
days_since_news: 0
inbound_links: 99
attribution_count: 50
attribution_last: "2026-08-14"
top_source: "google-news"
pending_count: 2
pending_overdue: 0
pending_next_review: "2026-08-24"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Anthropic 訂閱方案與計費政策

**類型：** policy
**狀態：** active（持續調整中）
**領域：** 💼 商業
**首次出現：** 2026-04-25
**最後更新：** 2026-08-14
**最後新聞更新：** 2026-08-14

> **最新計費政策異動**（2026-08-14）
> - **高互動 bug：Max 方案 session 額度自 3/23 起異常快速耗盡**：GitHub Issue #38335（👍 543，CLI 使用情境）反映 Max 方案的 session 限制自 2026-03-23 起異常快速耗盡；為本頁目前互動量最高的配額類回報，詳見「事故與爭議」新增。
> - **社群質疑：用量是否為配合 8/19 促銷「永久化」而暗中調降（單一貼文，未經證實）**：Reddit r/ClaudeCode 使用者質疑 Anthropic 是否正暗中調降用量，以便在傳聞中「50% 用量提升轉為永久」的 8/19 前後製造對比效果；score=0（Reddit RSS 天生無讚數），單一未經證實貼文，且查證本頁既有紀錄未見與「8/19 永久化」直接對應的官方承諾，性質存疑，詳見「事故與爭議」新增。
> - **08-12 記錄之 PaymentIntent 提前作廢 bug（Issue #55982）、usage limits／length limits 官方區分、企業定價落差量化案例仍為近期重點**，詳見下方「事故與爭議」「配額與速率」「成本案例與優化」。

## 現況

**2026-07-20 起，旗艦模型（現為 Fable 5）在訂閱體系中被切成兩層**：Max 與 Team premium 席位維持標配、上限為週用量的 50%；Pro 與 Team standard 席位改以 usage credits 按 API 費率付費，並發放一次性過渡 credit。此分界於 2026-08-08 由官方 Help Center 查證確認，終結 07-18～21 間四則媒體互相矛盾的報導。詳細對照見下方「我的方案現在有什麼」。

其餘計費結構未變：所有付費方案用量仍維持原訂閱配額制——原定 2026-06-15 實施的「程式化用量（Agent SDK、`claude -p`）脫離訂閱、改按 API 費率計費」政策已於 **2026-06-16 宣布暫停**，重新推行時間未定；2026-07-04 起企業方案可用支出控管（spend controls）。核心爭點：Anthropic 訂閱方案設計以人工互動為前提，大規模自動化工作流的長期計費方向尚未確定。

---

## 我的方案現在有什麼

> **資料截至 2026-08-08**（官方 Help Center 查證）。此表反映**訂閱月費**，非曾規劃但已暫停的 programmatic 信用池金額（見「計費架構」節）。「訂閱內含／需另計費」的分界會隨陣容換代改變，模型名以當期實際情形填寫。

| 方案 | 月費 | 訂閱內含 | 需另計費 | 可領優惠 | 你該做的動作 |
|------|------|---------|---------|---------|------------|
| Free | $0 | 基本額度；旗艦存取未載 | — | — | 週用量 +50% 促銷不適用本方案 |
| Pro | $20（年繳 $17／月）| 全模型，**旗艦除外** | **Fable 5** — $10/$50 per Mtok，走 usage credits | **一次性過渡 credit**（官方未列金額；媒體稱 $100）| 領完至 `Settings > Usage` 確認 auto-reload 未開 |
| Max 5x | $100 | 全模型；**旗艦上限為週用量 50%** | 超出後走 usage credits | — | 留意旗艦誤要求購點問題（見事故區）|
| Max 20x | $200 | 同上，額度更高 | 同上 | — | 用量上限集體訴訟進行中 |
| Team standard seat | $20（年繳）／$25（月繳）每席 | 同 Pro | 同 Pro | 同 Pro | 同 Pro |
| Team premium seat | $100（年繳）／$125（月繳）每席 | 同 Max | 同 Max | — | — |
| Enterprise | 未公開報價 | 舊制席位制比照 standard／premium 分層 | 同對應層 | — | 2026-07-04 起可用支出控管 |

**⚠️ usage credits 是「用量上限失效開關」**：credits 為 opt-in、預設關閉（`Settings > Usage`）。**一旦開啟，方案用量上限就不再是硬停止**——Claude 會繼續回答並從 credits 扣款，體感與額度內完全相同，但每則超額回應都在計費。靠 Pro 硬上限控管支出者，領取過渡 credit 後務必確認 auto-reload 未開啟（auto-reload 每日兌換上限 $2,000）。（來源：[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)、[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)，2026-08-08 查證）

### 方案細節

- **旗艦分界的官方定義（2026-07-20 生效）**：Max 方案、Team premium seats、舊制席位制 Enterprise premium seats — Fable 5 為標配，可用「至多每週用量上限的 50%」且不額外收費；Pro 方案、Team standard seats、Enterprise standard seats — Fable 5 **不計入方案用量**，需以 usage credits 按 API 費率付費。先前將 Fable 5 納入方案週用量的促銷結束於 **2026-07-19 23:59:59 PT**
- **Pro 過渡 credit**：官方原文僅稱「eligible Pro and Team standard seats qualify for a one-time credit to help with the change」，**未載金額、未載到期日**；$100 一說來自媒體（XenoSpectrum、XDA、nerdzap），官方文件未確認。credits 用盡後可續買、改用其他模型、或升級 Max
- **credits 購買方式歧異（未收斂）**：官方寫「Add funds，自行輸入金額」，XenoSpectrum 則稱為固定包（$45 買 $50、$200 買 $250、$700 買 $1,000）。兩者對不上，媒體數字不採信，以官方為準
- **Pro 年繳**：$200 一次預付，折合 $17／月（來源：[claude.com/pricing](https://claude.com/pricing)，2026-08-08 查證）
- **印度在地化定價**：Pro 為 **Rs 2,000／月**（2026-07-13 生效，首個非美元在地化市場，回應 GitHub Issue #17432）；Max／Team／Enterprise 是否同步在地化未見報導
- **Max 5x 月費曾記載矛盾**：06-26 Reddit 貼文誤植 $50，已依 2026-05-14 xda-developers／dev.to 官方公告原文更正為 **$100**；該貼文「兩個 Max 5x = 一個 Max 20x」的價格假設有誤
- **Max 20x 用量上限集體訴訟進行中**：Karl Kahn 訴訟（2026-06-16 提起）指控實際僅 Pro 的 6–8 倍而非廣告的 20 倍
- **Team／Free／Enterprise 月費（2026-08-08 官方查證）**：Team 可混搭席位型別（mix and match），standard $20／premium $100（年繳，月繳各為 $25／$125），未見最低席位數規定；Free $0；Enterprise 未公開完整報價，頁面標示為「席位費＋依 API 費率計量」並提及 $20／席，實際價格需洽業務（來源：[claude.com/pricing](https://claude.com/pricing)）
- **Free／Pro 功能組成補充（2026-08-12 官方查證，原文於 Max 方案段落截斷）**：Free 方案含 web 搜尋、記憶、桌面擴充、connector；Pro 方案另含 Claude Code／Cowork／Design／Science、無限 projects、Research、更多模型選擇、Microsoft 365 整合。此為功能清單補充，不影響上方六欄表的月費／計費規則；完整原文（含 Max／Team／Enterprise 段落）待後續查證（來源：[claude.com/pricing](https://claude.com/pricing)）
- **各方案最強可用模型（2026-07-24 起）**：Opus 5 為 Pro 方案最強可用模型、Max 方案新預設模型（原為 Opus 4.8），見 [[entities/opus-5]]
- **Max 20x 的差異不只用量**：context window、Claude Code 額度、優先排隊等有結構性差異，非單純 Pro 的 20 倍
- **Enterprise 附加功能**：含 Compliance API、Enterprise Gateway 等；合作分級 Select／Preferred 差異未公開。Team 方案於 2026-06-19 官方速率翻倍時同步適用
- **usage credits 僅可在網頁版開通（2026-08-11 官方查證）**：官方說明中心 usage-credits 條目載明，行動 App（iOS／Android）訂閱者無法直接於 App 內開啟 usage credits，須改至網頁版 `Settings > Usage` 操作；額度用盡後可切換按量計費（API 標準費率）不中斷服務。此為既有「credits 為 opt-in、預設關閉」規則（見上方 2026-08-08 條目）的補充限制（來源：support.claude.com usage-credits 條目，2026-08-11）

---

## 模型 API 定價現況

| 模型 | Input / Output per Mtok | 備注 |
|------|------|------|
| Claude Sonnet 5 | $2 / $10 | 促銷定價，有效期至 2026-08-31；Claude Code 新預設模型，相較 Opus 4.8 估計省 60% 成本 |
| Claude Fable 5 | $10 / $50 | Pro／Team standard 走此費率以 usage credits 計費；Max／Team premium 為標配（週用量 50% 內）。訂閱端分界見上方「我的方案現在有什麼」|
| Claude Opus 5 | **$5 / $25** | 官方文件逐字確認，與 Opus 4.8 相同；Fast mode 另計 $10/$50 |
| Claude Opus 4.8 | **$5 / $25** | 官方載明 Opus 5 定價「unchanged from Claude Opus 4.8」；2026-07-24 起次旗艦地位被 Opus 5 取代，各平台仍可用 |

**Opus 5 定價「歧異」已解消（2026-08-08 官方查證）**：官方文件載明 **$5 / $25 per Mtok，且「unchanged from Claude Opus 4.8」**。此前並存的兩種說法**其實同時成立**——「為 Fable 5 的一半」（$5 vs $10）與 MarkTechPost「維持原 Opus 定價」（與 4.8 相同）講的是同一組數字的兩個對照對象，並非矛盾。Fast mode（research preview，僅 Claude API）另計 **$10 / $50**（來源：[What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5)）。能力細節見 [[entities/opus-5]]、[[topics/model-comparison]]。

> 模型能力與評測細節見 [[topics/model-comparison]]；此表僅列價格。
> **注意（2026-07-14）**：The Register 分析指出 Anthropic tokenizer 設計較為複雜，使 API 定價與跨供應商成本估算更難以直接比較（標題式報導，無進一步量化細節，source_count=2）。
> **注意（2026-07-18）**：MakeUseOf 報導 Claude 存在「最便宜的 API 模式」，每項任務僅需幾分錢成本，但多數使用者不知其存在；報導未點名具體模式或模型（推測涉及 Haiku 或 Batch API），僅標題層級資訊，待後續補充具體費率（Google News/MakeUseOf）。

---

## 當前生效的計費規則

一條一規則，附來源日期；失效規則移除，計費事故與爭議見下方「事故與爭議」分組。

- **✅ 2026-07-20 生效｜旗艦模型的訂閱分界（官方文件已確認）**：Max 方案、Team premium seats、舊制席位制 Enterprise premium seats — Fable 5 為標配，可用至多**每週用量上限的 50%**，不額外收費；Pro 方案、Team standard seats、Enterprise standard seats — Fable 5 **不計入方案用量**，需以 usage credits 按 API 費率（$10/$50 per Mtok）付費。合格 Pro 與 Team standard seats 另有**一次性過渡 credit**；🔎 **查無官方**（標 2026-08-10｜查 過渡 credit、standard seat）｜**過渡 credit 金額與到期日**：官方文件未載具體金額與到期日。先前將 Fable 5 納入方案週用量的促銷結束於 2026-07-19 23:59:59 PT（來源：[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)，2026-08-08 查證）
- **⚠️ usage credits 開啟後，方案用量上限不再是硬停止**：credits 為 opt-in、預設關閉，於 `Settings > Usage` 開關，可設 auto-reload（每日兌換上限 $2,000）。開啟後 Claude 會在額度用盡後繼續回答並從 credits 扣款，體感與額度內無異，但每則超額回應皆計費——靠方案硬上限控管支出者需主動確認此開關（來源：[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)，2026-08-08 查證）
- **⏰ 2026-08-31 到期：Claude Sonnet 5 促銷定價（$2/$10 per Mtok）**：官方明確定性為「temporary」促銷，相較 Opus 4.8 估計省 60% 成本；dev.to 第三方實測（2026-07-02）確認此定價並建議設為預設路由模型。8/31 後定價走向未見公告（來源：2026-07-01、2026-07-02）
- **訂閱配額制維持**：原定 2026-06-15 生效的 Agent SDK／`claude -p` 計費切割已於 2026-06-16 暫停，重新推行時間未定；Agent SDK、`claude -p`、第三方 Agent SDK app 用量持續計入訂閱配額，無需額外信用池（來源：2026-06-16、2026-06-18 DevOps.com）
- **1M context window 觸發獨立 API 計費通道**：即使儀表板顯示 0% 訂閱用量，1M context window 仍會產生額外費用（實例：2026-05-11 用戶 0% 用量下遭收取 $3.37 Extra Usage）
- **`ANTHROPIC_API_KEY` 環境變數陷阱**：雲端環境（CI/CD、Docker、K8s）若設置此環境變數，所有 Claude Code 呼叫自動改走 API 計費通道而非訂閱配額（來源：2026-04-30）
- **企業支出控管功能上線（2026-07-04）**：具體控管粒度（部門／團隊層級、per-user、即時警報）尚未公開（來源：2026-07-04 Tech Times）
- **印度盧比在地化定價生效（2026-07-13）**：Pro 方案 **Rs 2,000／月**，為美國以外最大市場首次官方在地化定價；Max／Team／Enterprise 是否同步在地化未見報導（來源：2026-07-13～14 TechCrunch、NDTV、Times of India、bestmediainfo.com）
- **Max 用量上限爭議進入司法程序**：2026-06-16 集體訴訟指控 Max 5x／Max 20x 實際限制遠低於廣告宣稱（Max 20x 實測僅 Pro 的 6–8 倍），訴訟結果將影響方案信任度與可能的退款／調整義務（來源：2026-06-16 CNET、Decrypt）

> **已失效並移除的規則**：週用量 +50% 過渡期促銷（2026-07-19 到期）、Fable 5 免費使用期（2026-07-19 到期，已由上方 07-20 分界取代）。沿革見下方「重要政策變動紀錄」。

---

## **費用管控技巧 ★**

| 問題 | 建議對策 |
|------|---------|
| 常規任務仍用旗艦模型 Fable 5 燒錢 | 常規/簡單任務改路由至 Sonnet 5，降低 token 成本（Geeky Gadgets 建議，2026-07-16，媒體建議非官方公告）|
| Agent 無限迴圈燒錢 | 工具層面設硬性費用上限；不依賴 Claude 自判 |
| 94% token 流向 Opus | 在 CLAUDE.md 設定分層模型路由（繁瑣任務指定 Haiku） |
| Session 重啟費用 $6–10 | 用本機圖資料庫索引取代每次重讀完整 codebase |
| 5 小時視窗浪費 | 預排一條輕量訊息提前啟動計時，確保工作時段完整使用 |
| Prompt cache 耗盡 | 監控 `~/.claude/projects/*.jsonl` 的 `cache_creation_input_tokens` |
| 儀表板金額嚴重滯後 | 自建腳本定期查詢 Anthropic API 用量，勿只看儀表板 |

---

## 計費架構（2026-06-15 政策暫停）

原定 6/15 生效的「程式化用量（Agent SDK、`claude -p`）脫離訂閱、改按 API 費率計費」雙軌架構，已於 2026-06-16 宣布暫停，當前所有付費方案維持原訂閱配額制。原定的雙軌設計、方案對照表與社群因應建議，已整併至下方「重要政策變動紀錄 → 計費切割風波」末尾的「原定計費架構設計」條目，供政策重啟時參考。

---

## 重要政策變動紀錄

依主題分組，各組內日期倒序（最新在上）。

### 灰色市場與轉售現象

#### 2026-08-09：轉售套利已證實有隱私外洩代價——「Poison Claude」灰市轉售帳號，營運者可讀取每位客戶的所有 prompt

- **商業視角摘要**：08-03 記錄的灰市轉售觀察（低度信號，未達收錄門檻）在 08-05～08-06 出現具體印證——灰市管道「Poison Claude」以折扣價轉賣 Claude 帳號存取，服務營運者可看到每位客戶傳送的所有 prompt。安全事件細節與可信度評估見 [[topics/ai-agent-safety]]，此頁不重複維護。
- **讀者意涵**：便宜轉售管道的實際代價不只是違反 Anthropic 消費者條款（第 3 條禁止 resell、第 2 條禁止分享帳號憑證），而是已被兩獨立媒體（Help Net Security／The Hacker News）證實的隱私外洩風險——中間營運者可讀取全部 prompt 內容。折扣幅度（媒體稱最高 90%）與轉售規模均未見官方數字或執法回應。
- **與雙軌計費邏輯的張力**：仍為推論——若轉售規模擴大，形同以訂閱價格取得 API 存取權轉售牟利，繞開「訂閱補貼人工使用、程式化用量按 API 費率」的雙軌設計（見下方「計費架構」節），惟規模尚無官方或第三方數據佐證。

#### 2026-08-03：Show HN 揭露中國轉售商以最高 90% 折扣轉賣 Claude/Codex API 存取權（社群觀察，低度信號，未達收錄門檻）

- **貼文內容**：Hacker News Show HN 貼文（score 4、source_count=2，**未達互動門檻對照表「低」門檻 ≥10 分**，收錄僅因涉及計費灰色地帶而具警示價值，非達標準收錄）指出，中國轉售商正以最高 **90%** 折扣轉賣 Claude 與 OpenAI Codex 的 API 存取權；發文者稱部分業者使用開源專案（如 Sub2API）將批量購買的訂閱方案轉換為 API 存取權出售，並列舉數個轉售平台名稱（如 ddshub.cc、yunwu.api）。
- **ToS 已查證（2026-08-08）**：轉售行為明確違反 Anthropic 消費者條款——第 3 條禁止「resell the Services」，第 2 條禁止分享帳號登入資訊、API key 或帳號憑證（[consumer terms](https://www.anthropic.com/legal/consumer-terms)）。🔎 **查無官方**（標 2026-08-10｜查 [[topics/ai-agent-safety]]、resale scope）｜**轉售規模與 Anthropic 執法回應**：具體折扣百分比是否普遍、轉售規模、Anthropic 是否已知悉或採取執法行動，均未見官方聲明或第三方媒體佐證，**僅為單一低互動 HN 貼文的一手陳述，不可視為確認事實**；「90% off」為原貼文自述，非日報查證數字。
- **與既有計費邏輯的潛在張力（推論）**：若此類轉售規模擴大，可能繞開 Anthropic「訂閱補貼人工使用、程式化用量按 API 費率」的雙軌計費邏輯（見下方「計費架構」節），以訂閱價格取得 API 存取權轉售牟利，形同套利灰色地帶；惟目前僅一則低分社群貼文，尚無規模或官方回應佐證，需持續觀察是否有後續報導佐證（Hacker News https://news.ycombinator.com/item?id=49151751）

### 事故與爭議（誤扣費、靜默計費改動、帳號安全）

#### 2026-08-14：Max 方案 session 額度自 3/23 起異常快速耗盡（本頁互動量最高配額回報）+ 社群質疑用量被暗中調降

- **GitHub Issue #38335（👍 543，2026-08-14 查證，CLI 使用情境）**：使用者回報 Claude Max 方案的 session（工作階段）限制自 **2026-03-23** 起異常快速耗盡；543 個 👍 反應遠超 GitHub Issue 高門檻（≥50 留言對照表，本則為反應數非留言數，量級仍屬本頁近期配額類回報互動量最高者）。功能記者同步處理機制面（詳見 [[entities/claude-code]] 已知問題，若已收錄）；此處僅記配額/計費面：問題若屬實，代表訂閱方案配額計算自 3 月下旬起可能存在系統性異常，而非近期（07-20 旗艦分界後）才出現的新問題（推論，具體根因、是否與既有 Fable 5 用量點數異常 Issue #79337 同源，均未見報導或官方回應證實）（GitHub https://github.com/anthropics/claude-code/issues/38335）
- **Reddit r/ClaudeCode：使用者質疑用量是否配合 8/19「50% 提升永久化」而暗中調降（單一貼文，未經證實）**：使用者發文質疑 Anthropic 是否正暗中調降用量，以便在傳聞中「50% 用量提升」政策於 8/19 轉為永久生效前後製造對比效果（score=0，Reddit RSS 天生無讚數非低互動指標，但為單一未經證實貼文，屬使用者質疑／推測，非既定事實）。**查證本頁既有紀錄**：本頁已記錄之「週用量 +50%」促銷（2026-06-15 起臨時提高，多次延長至 2026-07-19 到期）已由 07-20 旗艦模型訂閱分界取代（見上方「已失效並移除的規則」），**未見與「8/19 永久化」直接對應的官方承諾或公告**；該 Reddit 貼文所稱「8/19」與本頁既有促銷時程（7/19 到期）不吻合，可能指涉另一項未被本頁收錄的官方承諾，或屬使用者對時程的誤記/混淆，需主編查證是否有獨立於本頁既有紀錄的「8/19」相關官方訊息（Reddit r/ClaudeCode，2026-08-14）

#### 2026-08-12：升級方案付款流程新爆計費 bug——PaymentIntent 於確認完成前遭提前作廢

- **GitHub Issue #55982（77 留言、👍 26 反應，2026-08-12 查證）**：反映用戶升級方案時付款流程失敗——PaymentIntent 在使用者確認付款前，就被後端 `void_invoice` 提前作廢，導致升級持續無法完成；77 留言已達 GitHub Issue 高門檻（≥50 留言對照表），是本頁近期新出現、互動量最高的付款類 bug（GitHub https://github.com/anthropics/claude-code/issues/55982）
- **同日 Reddit 出現疑似相關回報（單一貼文，未經證實）**：r/ClaudeCode 用戶回報，即便帳戶已有既有付款額度（credits），系統仍要求重新輸入付款資訊；是否與上述 PaymentIntent 作廢問題同源，兩者未見官方或報導證實關聯，暫各自獨立記錄，不合併為單一事件（Reddit https://www.reddit.com/r/ClaudeCode/comments/1vm9chm/claude_asking_me_for_payment_details_to_use/）
- **與既有事故的關係（推論）**：本頁「事故與爭議」已記錄多起用量點數／帳務異常（08-07 Issue #79337、07-20 南韓 $16.7M 疑似故障帳單等），本次首度集中在「升級付款流程本身失敗」而非「用量計費異常」，屬付款基礎設施層級的新故障面向

#### 2026-08-07：Fable 5 Max 方案用量點數異常追蹤更新——留言數攀升至 67，延燒逾 18 天

- **GitHub Issue #79337 互動量持續攀升**：GitHub Issue（08-07 查證：**67 留言**，較 07-25 查證時的 42 留言持續攀升）延續追蹤自 07-20 Fable 5 成為 Max 方案標準模型第一天起爆發的用量點數異常，含此前已記錄之「靜默降級 Opus 4.8」細節。**與既有事件的關係**：問題自 07-20 首次曝光起已延燒超過 18 天，橫跨官方 07-20 Status「Max 誤判、重啟可解決」定性、07-24（13 reactions）、07-25（42 留言、15 reactions）多輪查證，留言數持續攀升顯示問題規模與影響持續擴大而非收斂，是本頁目前追蹤時間最長的未解計費/配額爭議（推論，官方是否已著手修復或此問題與既有「誤判」定性的關係，均未見新公告釐清）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 2026-08-04：Reddit 回報 Max 20x 用量在未使用期間半小時內從 0% 衝到 100%，疑似配額計算異常

- **Reddit r/ClaudeAI 週熱門回報**：使用者發文指出 Max 20x 方案用量在**未使用 Claude 的情況下**，半小時內從 0% 攀升至 100%（Reddit，週熱門，達互動門檻對照表「低」門檻，2026-08-04）。**與既有已知問題的關聯（推論，待證實同源）**：症狀與功能記者已記錄於 [[entities/claude-code]] 已知問題的 GitHub Issue #41788〈Max 20 plan: rate limit 100% exhausted within ~70 minutes after reset〉（版本迴歸 bug）高度相似——皆描述用量上限在短時間、無明顯使用下被耗盡；惟本則 Reddit 貼文與該 GitHub Issue 是否為同一根因、同一批受影響用戶，均未見報導或貼文本身交叉確認，不可逕自合併認定為單一事件（Reddit https://www.reddit.com/r/ClaudeAI/comments/1vf6i4y/max_20x_usage_went_from_0_to_100_in_half_an_hour/）

#### 2026-08-02：Max 5x → Max 20x 訂閱升級持續失敗，與此前三起已知 issue 同源

- **GitHub Issue #55266**：使用者從 Claude Max 5x 方案升級至 Max 20x 方案時失敗，系統回報「Unable to update subscription」；Issue 標題明確指出此問題與此前三起已回報 issue（#10832、#50710、#43118）「同一模式（same pattern as）」，暗示 Max 方案升級流程存在持續性、非一次性的系統問題。**與既有事件的關係**：本頁已多次記錄 Max 方案相關計費爭議（06-16 集體訴訟指控用量上限不實、07-02 升級介面誤導扣費案例、07-24/25 Fable 5 用量點數異常），本則是另一起獨立於「用量計量」之外、聚焦「升級操作本身無法完成」的技術性故障；若此問題長期未解，可能直接阻擋用戶從低階方案轉向高階付費方案，對訂閱轉換率與客服負擔構成潛在影響（推論，具體受影響用戶規模、issue 建立時間、官方回應未見報導細節）（GitHub https://github.com/anthropics/claude-code/issues/55266）

#### 2026-07-25：Fable 5 Max 方案異常追蹤更新——留言數攀升至 42，新增「靜默降級 Opus 4.8」細節

- **GitHub Issue #79337 互動量攀升 + 新增技術細節**：GitHub Issue（07-25 查證：**42 留言、15 reactions**，較 07-24 查證時的 13 reactions 明顯攀升）持續追蹤自 07-20 Fable 5 成為 Max 方案標準模型第一天起爆發的用量點數異常。新增回報細節：受影響用戶反映系統除要求額外購買用量點數外，還會**靜默降級為 Opus 4.8**執行實際請求，可能導致使用者在不知情下誤以為仍在使用 Fable 5、實際計費與模型能力已改變。問題延續至今已逾 5 天未見官方修復或說明，與 07-20 官方 Status「Max 誤判、重啟可解決」的定性落差持續擴大（推論，待官方回應）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 2026-07-24：Fable 5 Max 方案計費/配額執行異常持續逾 4 天未解（追蹤 07-20 誤判事件後續）

- **GitHub Issue #79337：Fable 5 成為 Max 標準模型後仍被要求額外用量點數**：GitHub Issue（13 reactions，2026-07-24 01:16 UTC 查證）指出，自 07-20 Fable 5 成為 Max 方案標準模型第一天起，Claude Code 反而要求使用者額外購買用量點數（usage credits）才能使用，問題持續至少 4 天。**與既有事件的關係**：07-20 已記錄之官方 Status 事件（tnypgb2jbqnq）將此類現象定性為「Max 方案誤判」，並建議受影響用戶重啟即可解決；本則 Issue 顯示問題並未如官方所述經重啟即消失，不排除是（a）該 Issue 反映另一個持續性的配額執行 bug、或（b）官方「誤判已修正」的範圍未涵蓋此類個案，兩者關係待官方進一步釐清（推論，不可逕自認定為同一根因或已解決）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 2026-07-20：南韓用戶收到 $16.7M 帳單疑似故障，與 07-12/13 已證實帳務錯誤規模相近

- **KED Global 報導南韓用戶收到 Claude 開出的 1,670 萬美元帳單**：KED Global 報導一名南韓用戶收到 Claude 系統疑似故障產生的 **$16.7 百萬美元**帳單。**與既有事件的關係（推論，待證實）**：金額規模與 07-12/13 已記錄「Anthropic 證實 1660 萬美元帳務錯誤」（Tech Times）高度接近（$16.6M vs $16.7M），不排除是同一筆已證實錯誤的具體受害個案首次被具名地區媒體揭露，但原文摘要遭 RSS 截斷，未見報導明確連結兩起事件、亦未見 Anthropic 官方就此單一用戶案例回應，**不可逕自認定為同一事件**，僅記錄金額相近之巧合或關聯待後續查證（Google News/KED Global）

#### 2026-07-20：Fable 5 免費期到期後社群反映存取異常，含官方已證實的 Max 誤判事件

- **Reddit r/ClaudeAI：Max 方案用戶反映無法使用 Fable 5**：Reddit 用戶（score 0，Reddit RSS 抓取機制下不可信為互動門檻，source_count=1）反映 Max 方案疑似無法存取 Fable 5。**與官方 Status 事件吻合**：時間點與 Anthropic Status 頁面同日（07-20 07:35 UTC）公告的「Max 方案用戶被誤判需使用點數才能存取 Fable 5」事件吻合，官方已確認為誤判並建議受影響用戶重啟；官方事件細節由功能記者同步記錄於 [[entities/claude-code]]（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v1g5yy/so_i_cant_use_fable_with_my_max_plan_ey/；Anthropic Status https://status.claude.com/incidents/tnypgb2jbqnq）
- **Reddit r/ClaudeAI：App 內 Pro 方案顯示異常消失（單一回報，未經證實）**：另一則 Reddit 貼文（score 0，source_count=1）反映 App 內 Pro 方案顯示異常消失/變動，原因不明。**注意**：與上則 Max 誤判事件同日出現，但官方 Status 頁面僅證實 Max 方案誤判一事，本則 Pro 方案異常未見官方對應公告或其他來源佐證，暫不推論兩者為同一根因，僅並列記錄待後續查證（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v1hiu8/anthropic_nuked_the_pro_plans_on_the_app_for_some/）

#### 2026-07-12/13：Anthropic 證實 1660 萬美元帳務錯誤，稽核發現企業多收 170 萬美元

- **官方證實大規模帳務錯誤**：Tech Times 報導（20260712，於 07-13 日報顯示）Anthropic 證實一筆 1660 萬美元的帳務錯誤，稽核人員另發現企業客戶被多收 170 萬美元。**對信任度的意涵**：此前多次帳務爭議（HERMES.md bug、Max 升級誤導扣費、儀表板 0% 用量仍收費等）均為個案或社群自行發現，本次是官方證實的具體金額規模最大案例，可能強化企業客戶對 Anthropic 計費系統可靠性的疑慮，尤其在企業支出控管（spend controls）功能剛於 07-04 推出、企業成本敏感度已因競品定價戰而升高的背景下（推論）；具體受影響企業名單、退款機制未見報導（Tech Times https://www.techtimes.com/articles/320266/20260712/anthropic-confirms-166m-billing-error-auditors-find-17m-enterprise-overcharges.htm）

#### 2026-07-02：Max 升級誤扣費案例 + 客服/退款流程爭議

- **長期 Max 用戶反映升級介面誤導、退款無門**：Reddit r/ClaudeAI（score 未標，07/02 05:44 UTC）一則熱門貼文指出，長期 Max 用戶 5 月底將方案從 $100/月升級到 $200/月時，介面誤導其誤購 $200 credits（而非升級訂閱本身），事後找不到有效退款客服管道，一個多月問題未解決，貼文標題直指「Claude 客服是幾乎所有科技公司中最差的」。**對留存的意涵**：這是繼 [[topics/code-quality-decline]] 用戶退款訴求、6/16 Max 集體訴訟（見「計費切割風波」6/16 條目）之後，另一起具體指向「客服/退款流程缺失」而非「模型能力」的留存風險案例；升級付費流程的 UX 缺陷若造成非自願扣費，可能加劇既有集體訴訟的輿論壓力（推論）（Reddit https://www.reddit.com/r/ClaudeAI/comments/1uliph2/claude_truly_has_the_worst_customer_support_out/）
- **企業合作層級（Select vs Preferred）資訊不透明**：同日 Reddit r/ClaudeAI 另有使用者詢問 Anthropic 企業認證 Select 與 Preferred 合作層級的具體差異（純提問，無官方或社群解答內容）；此分級用語亦見於 [[topics/anthropic-business]] 6/30 DataArt「精選（Select）合作夥伴」條目，但兩層級的權益/門檻差異目前無公開資料，待補充（Reddit https://www.reddit.com/r/ClaudeAI/comments/1ulj6r4/partnership_levels_select_vs_preferred/）

#### 2026-06-24：隱私政策更新 + 帳號盜刷事件

- **隱私政策更新，新增年齡或身份驗證條款**：Anthropic 更新隱私政策，新增年齡或身份驗證相關條款，2026-07-08 正式生效；影響範圍與具體執行細節未完整公開，用戶應於生效前查閱更新版條款
- **加州用戶帳號遭盜刷，歐元計費未授權費用**：ABC7 報導，加州用戶反映 Claude 帳號遭他人盜用，產生以歐元計費的未授權費用；顯示 Anthropic 計費帳號安全存在漏洞，建議用戶定期檢查帳號活動記錄（ABC7 2026-06-24）

#### 2026-05-20：Claude Code 定價溝通混亂事件（Simon Willison 分析）

- **Claude Code 曾短暫顯示為 Max 方案專屬功能**：Anthropic 定價頁在毫無公告的情況下短暫顯示 Claude Code 為 Max 方案（$100–$200/月）專屬功能，引發社群恐慌後已撤回。Simon Willison 深度分析指出問題根源是 Anthropic 的定價溝通策略缺乏透明度。此事件發生於 2026-04-22 前後，但 HN 於 2026-05-19/20 再度廣泛討論，反映社群對 Anthropic 定價透明度的持續不滿
- **建議**：用戶應持續追蹤官方 [Choosing a Plan](https://www.anthropic.com/pricing) 頁面，而非依賴第三方資訊；Anthropic 任何定價頁更動均可能未經公告

#### 2026-05-11：Pro 方案 0% 用量仍遭收費

用戶儀表板顯示 0% 情況下，2–3 個提示後被收取 $3.37 Extra Usage；根本問題：1M context window 觸發 API 計費通道，獨立於訂閱用量計量。Anthropic 尚未公告改善。

#### 2026-05-05：提示快取窗口悄悄縮短（未公告）

Anthropic 於 4 月初靜默縮短預設 prompt cache 窗口，實質提高 token 消耗速度；為繼 Token 費用估算翻倍（2026-04-29）後第二次被社群自行發現的靜默計費改動。

#### 2026-04-29：Token 費用預估翻倍（靜默修訂）

Business Insider 報導 Anthropic 低調調高 Claude Code 預期 Token 費用估算值一倍，無官方公告。

#### 2026-04-28：Opus「圍牆內圍牆」事件（已修正）

Pro 用戶無預告須額外購買才能使用 Opus；Anthropic 事後澄清 Pro 仍可存取，但信任損失已造成。

#### 2026-04-25：HERMES.md 靜默計費 Bug

git commit 歷史出現大寫字串「HERMES.md」會觸發靜默切換至 API 額外計費模式，已知損失單日 $200；Anthropic 確認為 bug 但**拒絕退款**。
**立即行動**：`git log --all | grep -i HERMES`
來源：[GitHub Issue #53262](https://github.com/anthropics/claude-code/issues/53262)

### 定價與促銷（模型定價、方案設計）

#### 2026-08-11：官方文件補充 usage credits 僅限網頁版開通，pricing 頁確認 Free 方案功能範圍

- **官方 usage-credits 條目補充限制**：support.claude.com 說明中心確認行動 App 訂閱者無法直接於 App 內開啟 usage credits，須改至網頁版操作；額度用盡後可切換按量計費（API 標準費率）不中斷。詳見上方「方案細節」新增條目
- **claude.com/pricing 確認方案分層**：官方定價頁列出 Free／Pro／Max 各方案，Pro 明確標示涵蓋 Claude Code／Cowork／Design／Science，與 2026-08-12 已記錄之「Free／Pro 功能組成補充」屬同一份官方頁面的不同時點查證，不重複記錄

#### 2026-08-08：官方 Help Center 查證，07-18～21 四方矛盾報導收斂（✅ 待查證結案）

- **查證動機**：本頁自 07-18 起累積四則互相矛盾的媒體報導（Tech Times「Max 永久」／Dawn「50% 上限」／the-decoder「Pro 導向 API 計費」／Reddit「轉為 metered」），懸置 20 天無官方澄清。日報來源不含 `support.claude.com`，媒體轉述始終只有標題層級，故直接查證官方說明中心原文。
- **官方結論（[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)）**：2026-07-20 生效。Max 方案／Team premium seats／舊制席位制 Enterprise premium seats — Fable 5 標配，可用至多**週用量上限的 50%**，不額外收費；Pro 方案／Team standard seats／Enterprise standard seats — Fable 5 **不計入方案用量**，改以 usage credits 按 API 費率付費。先前促銷結束於 **2026-07-19 23:59:59 PT**。合格 Pro 與 Team standard seats「qualify for a one-time credit to help with the change」。
- **四則矛盾報導其實各對一半**：Tech Times「Max 永久」✅（Max 確為標配）、Dawn「50% 上限」✅（標配確有 50% 週上限）、Reddit「轉為 metered」✅（但那是講 Pro）—— 三則各自描述不同 seat 層級卻都未指明層級，才被記成互斥（推論）。
- **一次性 credit 金額為媒體數字，非官方**：官方原文未載金額與到期日；$100 一說來自 XenoSpectrum、XDA、nerdzap。credits 購買方式亦有歧異——官方寫「Add funds 自行輸入金額」，XenoSpectrum 稱固定包（$45 買 $50／$200 買 $250／$700 買 $1,000），以官方為準。
- **usage credits 的隱性風險（[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)）**：credits 為 opt-in、預設關閉（`Settings > Usage`），可設 auto-reload（每日兌換上限 $2,000）。開啟後方案用量上限不再是硬停止——Claude 繼續回答並從 credits 扣款，體感與額度內無異。此即 08-01 XDA「多數人從沒注意到」報導所指的計費異動（見下方同組條目），至此獲官方文件佐證。
- **官方 Help Center 未把此事寫進 Release notes**：[Release notes](https://support.claude.com/en/articles/12138966-release-notes) 只記模型發布與功能（07-24 Opus 5、07-09 Reflect、07-01 Fable 5 恢復），方案／配額／計費改制不在其中——代表即使把該頁納為來源，此類異動仍抓不到（流程缺口見 `wiki/log.md` 2026-08-08 Query 條目）。

#### 2026-08-01：XDA 報導多數用戶未留意 Fable 5 免費促銷已悄悄改變計費方式（媒體視角補充，非新事實）

- **XDA：免費促銷附帶靜默計費異動，多數用戶未察覺**：XDA（具一定知名度之科技媒體）發表文章稱先前 Fable 5 相關的 $100 免費體驗促銷，附帶改變了 Claude 計費方式的細節，且多數使用者並未留意到此變化。**與既有事實的關係（推論，待證實是否為同一事件）**：本頁已詳盡記錄 Fable 5 免費使用期限歷經多次延長（06-09→07-01→07-07/08→07-12→07-19）後於到期日轉為 usage-based billing（見上方 07-19/20 條目），本則僅標題可用，未提供具體費率、額度換算或生效時間等新細節，無法確認是否即指同一轉換事件、或另一項未見於既有記錄的獨立計費異動；若為同一事件，本則補充的獨特角度是「多數用戶未察覺計費已變」的讀者認知落差，呼應本頁一貫記錄的「靜默計費改動損傷信任」既有商業風險（見 [[topics/anthropic-business]]「商業風險」表）（Google News/XDA）

#### 2026-07-29：印度盧比定價訴求 GitHub Issue #17432 互動持續攀升，距官方 07-13 回應已 16 天

- **互動量新高**：GitHub Issue #17432〈Feature Request: India-Specific Pricing Plans (INR) for Claude & Claude Code〉留言數由 07-09 查證的 205 增至 **210**、reactions 由 **598** 增至 **613**，維持高互動門檻（互動門檻對照表「高」：GitHub Issue ≥50 留言即達標，本則遠超）。
- **與已回應事實的張力（需留意，非官方政策異動）**：本頁已記錄 Anthropic 於 07-13 正式推出印度盧比計價（Pro 方案 Rs 2,000/月，見下方 07-13/14 條目），當時視為對此 issue 訴求的官方首度回應。惟本 issue 標題與原始訴求同時提及 **Claude 與 Claude Code** 兩者，07-13 官方公告目前僅確認 Pro 方案訂閱定價，Max/Team/Enterprise 及 Claude Code 本身是否同步在地化未見報導；互動量在官方回應後仍持續攀升，可能反映此範圍缺口，也可能只是舊討論串持續累積讚數，兩種可能性均無法從現有資料確認（不可推測，僅記錄現象）。
- **用詞界定**：本則為使用者訴求延續，**非**「Anthropic 將推出新方案」——尚無官方聲明承諾進一步異動（GitHub https://github.com/anthropics/claude-code/issues/17432）。

#### 2026-07-24：Claude Opus 5 發布，官方稱定價為 Fable 5 的一半，與此前 MarkTechPost「維持原定價」說法方向不一致

- **官方公告**：Anthropic 正式發布 Claude Opus 5（[官方公告](https://www.anthropic.com/news/claude-opus-5)，2026-07-24 16:57 UTC，Hacker News 1587 分），稱其定價為 Fable 5 的一半，相同成本下效能相較前代 Opus 4.8 大幅提升；現為 Claude Max 方案新預設模型、Claude Pro 方案最強可用模型，取代 Opus 4.8 次旗艦地位。**與既有訊號的落差**：MarkTechPost（2026-07-14，見 [[topics/model-comparison]] 延伸閱讀）此前曾稱 Opus 5 將「維持原 Opus 定價」，與官方本次「砍半」的說法方向不同；官方公告本身未提供具體 $/Mtok 數字，若以現行 Fable 5 $10/$50 定價推算，半價約為 $5/$25，但此為讀者端推算，非官方逐字確認的數字，待官方定價頁更新後進一步核實（推論，不可逕自視為官方定案數字）。能力面詳見 [[entities/opus-5]]。

#### 2026-07-21：Reddit 週熱門回顧 Fable 5 免費期延長史，社群觀察指向 Max／Team Standard 轉為計量存取

- **延期歷史彙整 + Max/Team Premium 稱轉為計量存取**：r/artificial 週熱門貼文（2026-07-20 07:56 UTC）整理 Fable 5 免費存取期限延後歷程（6/22→7/7→7/12→7/19），並指出 7/20 起 Max 與 Team Premium 方案轉為**計量存取（metered）**。**與既有矛盾訊號的關係**：本則社群來源方向與既有 07-19 Tech Times「Max 永久」說法相反，較接近 Dawn「用量上限 50%」與 07-18 Startup Fortune／the-decoder.com「收緊 Max/Team Premium 配額」的方向；惟本則為 Reddit 週熱門貼文（達互動門檻對照表「低」門檻），非官方公告，與既有官方層級矛盾報導並列記錄，不可視為官方定案（推論）。
- **Claude Code 額外延伸方案提醒**：同則貼文提醒讀者 Claude Code 另有 **2026-08-19** 到期的延伸方案值得關注，暗示 Claude Code 訂閱層與 Fable 5 免費期為兩條獨立的計費時程；具體延伸方案內容未見報導細節，待後續補充。
- **07-17 早期信號（回溯記錄）**：r/artificial 週熱門貼文（2026-07-17 18:48 UTC，標題帶問號，非確認事實）反映部分月付 $200 的 Claude.ai Max 用戶回報 Fable 5 存取遭停用；早於 07-18 官方訊號分歧報導兩天出現，可視為社群端最早察覺存取異動的訊號，但當時未經證實（推論：與 07-18/07-19/07-20 後續報導方向一致，顯示社群端偵測先於媒體確認）（Reddit r/artificial）

#### 2026-07-19：免費期到期日當天，Fable 5 存取政策再添兩則標題層級報導，仍未消解矛盾

- **Tech Times：「Max 永久、Pro Credits-only」（2026-08-10 官方查證確認屬實）**：標題稱 Claude Fable 5 訂閱限制調整為「Max 方案轉為永久提供、Pro 方案改為 Credits-only」。經 2026-08-08 官方 Help Center 查證（見上方「官方 Help Center 查證」段），此標題所述**方向正確**：Max 方案／Team premium seats 確為標配（不脫離、"permanent" 意指不下架），Pro 方案／Team standard seats 確改為 usage credits 按 API 費率計費——與 07-18 Startup Fortune／the-decoder.com「Pro 導向 API 計費」方向一致，兩則報導確實是同一政策的「方案別拆解」，非互斥（[Tech Times](https://www.techtimes.com/articles/320905/20260718/claude-fable-5-ends-subscription-limbo-permanent-max-credits-only-pro.htm)，2026-07-18）
- **Dawn：「併入 Max、Team Premium，用量上限 50%」**：標題稱 Anthropic 將把 Fable 5 模型以「50% 用量上限」的方式併入 Max、Team Premium 方案。**與 Tech Times 報導的落差**：若 Max 方案是「永久提供」（Tech Times），與本則「50% 用量上限」的描述無法完全對照——「永久」可能指存取權限本身不下架，「50% 上限」則可能指配額分配比例，兩者未必互斥，但缺乏官方公告確認具體機制（Google News/Dawn，07-18 12:50 UTC）
- **⚠️ 不擇一呈現**：本頁採「如實記錄矛盾」原則，兩則新報導均為標題層級資訊，與 07-18 已記錄的矛盾訊號一併保留，待官方於免費期到期後進一步公告釐清。

#### 2026-07-18：Fable 5 存取政策訊號分歧——「收緊限制」vs「設為永久」同日並存

- **收緊限制方向**：Startup Fortune（「Anthropic Limits Claude Fable 5 Access as It Runs Out of Compute」）與 the-decoder.com（source_count=2，「Anthropic slashes Claude Fable 5 limits in Max and Team Premium and pushes Pro users toward API pricing」）同日報導，Anthropic 因運算資源吃緊，大幅縮減 Max 與 Team Premium 方案的 Fable 5 使用配額，並將 Pro 方案用戶導向改用 API 計費。**與 Meta 運算力租賃洽談的呼應（推論）**：同日 [[topics/anthropic-business]] 記錄 Meta 據報洽談以 100 億美元規模租賃運算力予 Anthropic，兩則報導共同指向「Anthropic 運算需求已超出現有供給」的同一根因——對外租算力、對內收緊高階模型配額，是同一資源缺口下的一體兩面（推論）。
- **設為永久方向（矛盾訊號）**：Simon Willison 部落格同日（06:00 UTC，早於上述兩則收緊限制報導）引述官方 `@claudeai` Twitter 帳號發布內容，標題為「Claude make Fable 5 permanent」（將 Fable 5 設為永久）；原文於標題引述後即截斷，無更多細節可查證。
- **⚠️ 如實記錄矛盾，不擇一呈現**：兩則方向相反的報導同日出現，可能反映（a）官方公告本身存在時間差或表述模糊、（b）「設為永久」specifically 指某項功能/免費層級的一部分而非整體 Fable 5 免費存取、或（c）媒體對同一份公告有不同解讀。目前生效的免費期到期日仍為 **2026-07-19**（見上方「當前生效的計費規則」），實際政策走向待 7/19 前後官方進一步公告釐清。

#### 2026-07-17：交易員押注 Fable 5 免費期將第四度延長（市場猜測，非官方，07-18 獨立來源佐證）

- **市場押注，非官方公告**：Proactive financial news 報導交易員押注 Anthropic 將第四度延長 Claude Fable 5 免費使用期限。**注意**：此為財經媒體對交易員市場行為的報導，非 Anthropic 官方公告，目前生效的到期日仍為 **2026-07-19**（見上方「當前生效的計費規則」），未見變動。
- **07-18 獨立來源佐證**：Yahoo Finance UK（source_count=2）獨立報導同一押注方向，強化此市場預期訊號的傳播度，非新增事實。
- **對既有延長序列的意涵（推論）**：Fable 5 免費期已延長三次（06-09 原訂 6/22 → 07-01 明確 7/7 → 07-07/08 延至 7/12 → 07-12 再延至 7/19），交易員押注第四度延長顯示市場預期 Anthropic 對 usage-based billing 轉換將持續採取謹慎策略，與既有「Anthropic 對 Fable 5 計費轉換態度謹慎」的判斷（見 07-12 條目）方向一致；惟押注本身不構成事實依據，7/19 後實際走向仍待官方公告確認（Google News/Proactive financial news）

#### 2026-07-13/14：印度盧比在地化定價正式推出，回應長期社群訴求（重大）

- **官方推出印度盧比計價，Pro 方案 Rs 2,000/月**：TechCrunch（source_count=2）、NDTV、Times of India、bestmediainfo.com 同步報導，Anthropic 為美國以外最大市場印度啟動盧比計價，Pro 方案訂為每月 **Rs 2,000**。**對採用率的意涵**：是官方首度正式回應下方 07-03 條目記錄的 GitHub Issue #17432（reactions 598、留言 205，長期無官方回應）印度在地化定價訴求，若能提升印度市場訂閱轉換率，將直接驗證此前「未回應在地化定價將影響全球最大開發者社群之一的轉換率」的推論；具體匯率換算基準、是否同步適用 Max/Team/Enterprise 方案未見報導細節，待後續補充（NDTV「Anthropic Starts India Pricing For Claude AI, Pro Plan At Rs 2,000」；TechCrunch「Anthropic starts localizing Claude pricing for India, its biggest market after the US」）
- **API 定價跨供應商比較難度浮上檯面（The Register）**：Google News/The Register（source_count=2）分析指出 Anthropic tokenizer 設計較複雜，使 API 定價與跨供應商成本估算更難以直接比較；僅標題式報導，無具體量化細節，惟此議題與印度盧比在地化定價同日出現，共同凸顯 Anthropic 全球定價透明度議題（推論：一為訂閱端在地化，一為 API 端可比性，兩者性質不同，不宜混為一談）
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
- **注意**：優惠明確為「temporary」，8/31 到期後定價走向未見官方公告，屆時是否延續或調升需留意（見「⏰ 倒數中」風險提示）

#### 2026-07-01：Claude Sonnet 5 促銷定價 + Fable 5 計費架構調整

- **Claude Sonnet 5 促銷定價**：$2/Mtok（輸入）、$10/Mtok（輸出），有效期至 2026-08-31；Claude Code 用戶以此定價使用新預設模型，相較 Opus 4.8 估計省 60% 成本。**對採用率的意涵**：若 Claude Code 預設路由切換至 Sonnet 5，重度使用者的月均 API 費用可能顯著降低，有助於緩解近期配額縮減導致的訂閱留存壓力（推論）。
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

#### 2026-08-12：官方文件釐清 usage limits 與 length limits 為兩種不同機制；同日再現「用量限制遭調降？」社群疑慮

- **官方 Help Center：《How do usage and length limits work?》（2026-08-12 查證）**：官方文件說明 usage limits（隨對話長度、複雜度、啟用功能、模型、effort 等級等變動的「額度」）與 length limits（單則訊息／對話長度上限）是兩種不同概念；不同方案（Pro／Max／Team 等）的額度規則亦不同。此文件首度明確說明 usage limits 具動態性，而非固定額度（來源：[How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)）
- **同日 Reddit 疑慮（單一貼文，未經證實）**：r/ClaudeCode 用戶反映近幾天用量額度消耗速度明顯變快，詢問是否遭調降限額；無官方回應佐證，亦未見其他來源佐證（Reddit https://www.reddit.com/r/ClaudeCode/comments/1vm9135/did_anthropic_decreased_the_usage_limit/）
- **與官方文件的潛在關聯（推論，非官方回應）**：若 usage limits 確實隨對話複雜度／effort 等級動態變動（見上方官方說明），使用者感受到的「額度消耗變快」有可能源於任務型態改變而非官方調降限額；惟官方文件未直接回應本則貼文的具體指控，也未證實或否認限額本身是否曾調整，不可視為已解釋

#### 2026-07-22：Reddit 週熱門質疑 Anthropic 宣稱的用量提升未反映於實際體驗（單一貼文，2026-07-22 指控，至今無後續——近 14 天日報未見其他來源佐證或官方回應）

- **r/ClaudeAI 週熱門貼文**：貼文標題稱「Anthropic Claims 50% usage boost that doesn't exist」，質疑官方宣稱的 50% 用量提升並未實際反映在使用體驗中；純圖片型貼文，未附具體帳號數據或官方公告連結佐證。**與既有 +50% 促銷的關係（推論，待證實）**：不確定是否指涉上方「當前生效的計費規則」已記錄、已於 07-19 到期的「週配額 +50% 過渡期促銷」，或另一項未見於日報的官方宣稱；若指涉前者，則與 05-16 已記錄「Max 20x 用量上限未生效（數學實證）」同屬「官方宣告與實際體驗存在落差」的重複性模式（推論）。本則達互動門檻對照表 Reddit 週熱門「低」門檻，但無具體數據佐證，暫不視為新增可查證事實，僅記錄為既有落差模式的又一社群訊號（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v3d8iz/anthropic_claims_50_usage_boost_that_doesnt_exist/）

#### 2026-07-16：週用量配額疑似再度提前重置（單一回報，2026-07-16 指控，至今無後續）

- **Reddit r/ClaudeCode 回報週用量提前重置**：一位 Claude Max 訂閱用戶回報，原本週用量約 41%、正常重置日為週二，但當日用量卻提前歸零，並詢問是否有其他用戶遇到相同情況；貼文為單一回報，Reddit RSS 抓取機制下 score 恆為 0（不代表真實互動量），未標記「週熱門」，近 14 天日報亦未見其他來源佐證或後續報導，暫不升級為系統性訊號（Reddit https://www.reddit.com/r/ClaudeCode/comments/1uxzlyx/did_anyone_elses_claude_code_weekly_usage_reset/）
- **與既有現象呼應**：與 2026-05-16 已記錄的「週用量配額意外提前重置（bug 或後端調整）」現象方向一致，顯示此類配額計時異常並非單一事件，近兩個月內至少出現兩次獨立回報（推論，兩次間隔近兩個月，無法確認是否為同一根因）

#### 2026-07-07～10：Max 方案額度異常快速耗盡、token 消耗增加 3–5 倍（持續發酵，官方無回應）

- **GitHub Issue #38335（792 留言，2026-07-10 查證）**：反映 Max 方案 CLI session 額度自 2026-03-23 起異常快速耗盡，為近期社群互動量最高的計費類 issue 之一；留言數 07-08（790）→ 07-09（791）→ 07-10（792）持續微幅增加，社群互動已趨於高原期，官方仍無明確回應（GitHub https://github.com/anthropics/claude-code/issues/38335）
- **GitHub Issue #41506（54 留言/29 讚）**：反映 Max（$100/月）方案 token 消耗自 3 月底起增加約 3–5 倍，未見對應功能或用量增加可解釋此漲幅（GitHub https://github.com/anthropics/claude-code/issues/41506）
- **Reddit r/ClaudeAI：「Claude Max 20x: Why did 27% of one session consume 7% of my entire weekly limit?」（2026-07-09）**：使用者具體質疑單一 session 中 27% 的時間消耗掉整週額度 7%，用量計量比例明顯失衡，與 GitHub #38335 反映的異常耗盡現象方向一致
- **Reddit r/ClaudeCode：「Claude Max (20x) weekly limit exhausted in less than a day」**：使用者回報週額度不到一天即用盡（Reddit https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/）
- **對留存的意涵**：多則獨立訊號（2 個高互動 GitHub issue + 2 則 Reddit 貼文）方向一致，指向 Max 方案的用量計量或消耗速率可能存在系統性異常，而非個案；與既有 06-16 Max 集體訴訟（廣告 20 倍實測僅 6–8 倍）同屬「用量承諾與實際體驗落差」的信任問題，Anthropic 至今（07-09）尚未提供官方解釋或修復時程（推論）
- **正面反例（同期出現）**：Reddit r/ClaudeAI · 週熱門（2026-07-09）「5 hour and weekly limits have been reset. Thanks Anthropic!」一則貼文回報 5 小時與週用量額度已被重置並表達感謝；與上述額度異常耗盡投訴同期出現，方向相反，可能反映用戶端因帳號、時段或所屬方案不同而體驗分化，非全面性的正面或負面訊號（推論）

#### 2026-06-30：配額再次縮減（社群反映，Anthropic 無官方公告）

- **社群集體反映 Claude Code 使用配額縮減**：Reddit r/ClaudeCode 出現多個討論串，訂閱用戶集體反映 Claude Code 使用配額再次縮減，不滿情緒高漲。Anthropic 未發布任何官方公告，縮減幅度與觸發機制不明。從結構性判斷，此為 6/16 計費暫停後 Anthropic 透過調降配額而非計費改制來控管成本的另一路徑（推論）。**對採用率的意涵**：重度訂閱用戶若持續感受配額壓縮，可能加速評估競品替代方案；「配額縮減 → 配額不滿 → 切換」的漏斗效應對 Anthropic 訂閱留存構成風險（推論）（Reddit https://old.reddit.com/r/ClaudeCode/comments/1uim4jb/this_is_a_message_for_anthropic_bring_back_the/）
- **注意**：無具名企業規模數據，此條目為訂閱用戶個人反映，非企業層級案例。

#### 2026-05-19：臨時用量提升優惠、企業成本壓力持續

- **Anthropic 臨時用量提升**：部分使用者收到 Anthropic 提供的臨時優惠——5 小時使用量加倍（x2）+ 每週上限提高 50%；社群反應熱烈，積極利用有限期額度進行密集開發；此舉可能是為緩解近期用量限制帶來的用戶不滿，或配合 Max 方案促銷；具體受惠條件 Anthropic 未公開說明
- **企業帳單達雲端費用三倍**：HN 討論串揭示多家企業月 AI 工具費用已達雲端 SaaS 費用三倍，部分企業即將全面停用 Claude Code 並禁止個人方案；顯示用量暴增 + 計費透明度不足的問題仍在持續（見 [[topics/enterprise-cost-management]]）

#### 2026-05-16：Max 用量上限未實際生效、社群促銷驗證、成本焦慮高峰

- **Max 20x 用量上限未生效（數學實證）**：一位 Max 20x 重度用戶以計算明確證明——5/6 宣佈的 2 倍 session 上限與 5/13 宣佈的 1.5 倍週用量上限均未在其帳號生效；客服零回應；多位用戶跟進驗證，顯示「宣告即生效」與實際體驗可能存在系統性落差
- **社群系統驗證 Anthropic 促銷時序**：Reddit 用戶系統整理 2025 年 8 月以來所有官方用量促銷完整時序（對照官方來源），引發對方案透明度的廣泛質疑，討論串聚焦「宣告與實際生效」之間的落差
- **Lanes.sh 說明 6/15 影響範圍**：Lanes.sh 因架構不同而未受波及，並提供清楚分析：Zed、Conductor、T3 Code、superset.sh 等建構於 Agent SDK 之上的平台的 Max 5x 訂閱用戶實際可用量大幅縮水
- **API 費用焦慮達本週最顯著高峰**：同日出現多篇 Claude Code API 費用優化指南（7 種降費策略、不改代碼省 10–30%、bootstrapped 創業者費用管控討論、Claude Code 替代方案整理），顯示開發者對 API 費用的集體焦慮達近期峰值
- **週用量配額意外提前重置（bug 或後端調整）**：部分用戶反映在正常重置日前週配額意外歸零，原重置日期未變（等同一輪額外免費用量）；不清楚是後端調整副作用或 bug；社群擔心用量可能被「追回」
- **「用 credit 包裝的漲價」批評**：部分開發者在優化指南中明確指出 6/15 公告本質是 API token 上限收緊而非計費重組；Anthropic 對此立場無官方回應

#### 2026-05-10：Opus API 速率限制悄悄調降

ServeTheHome 首報；與 SpaceX 算力到位（Sonnet 速率翻倍）同時期出現，顯示差異化模型速率管理。

#### 2026-05-07–09：SpaceX 算力到位，速率上限翻倍

三項變更同步生效：Pro/Max Claude Code 五小時視窗速率翻倍、取消 Pro/Max 尖峰時段降速、API Tier 4+ 速率提升。Dario Amodei 在 Code with Claude 大會現場宣布。

### 計費切割風波（Agent SDK / `claude -p` 訂閱脫鉤，2026-06-16 暫停）

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

#### 2026-08-11：Quesma 部落格量化訂閱制 vs API 計費落差最高達 40 倍，Pylon CEO 三天內意外花費 $4,000

- **HN 討論（score 31，達互動門檻對照表「中」門檻，2026-08-11）**：Quesma 部落格文章指出，相同 token、相同模型下，Claude Code 訂閱制與純 API 計費之間的價差最高可達 **40 倍**；一年前 $20/月方案已夠用，如今官方建議的「入門」方案已是 $100/月（Hacker News/quesma.com https://quesma.com/blog/claude-code-pricing-for-enterprise/）
- **Pylon CEO 具名案例**：Pylon CEO Marty Kausas 公開表示三天內意外花費 **$4,000**，凸顯企業用戶對 API 計費模式的成本可預測性不足；具名企業案例彙整見 [[topics/enterprise-cost-management]]
- **The Information 佐證**：文中引述報導指多家企業實際帳單較原先預期高出 **2–3 倍**，與本頁既有「計費儀表板滯後、透明度不足」結構性問題方向一致
- **Uber 時間軸補充**：文章重申 Uber 於 **2025 年 12 月**導入 Claude Code、**2026 年 4 月**即燒完全年 AI coding 預算，為既有 Uber 案例（05-02／05-18，Forbes）補上具體月份，非新事件
- **與 07-23 既有案例的對照（推論）**：與 07-23 已記錄「一手部落格實測——綁定方案改走純 API 計費，月費暴增至約 44 倍，推估補貼倍數約 13 倍」量級相近（40 倍 vs 44 倍），兩則獨立來源方向一致，均指向訂閱制對 API 計費的補貼倍數落在 40–44 倍區間，補強原本單一樣本的可信度

#### 2026-07-23：一手部落格實測——綁定方案改走純 API 計費，月費暴增至約 44 倍，推估補貼倍數約 13 倍

- **modelplane.ai 部落格（經 Hacker News 討論，19 分）**：作者任職於 Upbound，記錄團隊一名工程師將 Opus 4.8 的使用管道從公司 Team 綁定方案（約 $125/月）改為透過 opencode 直連 Anthropic API 計費後，同樣工作量下單月花費暴增至約 **$5,500**（約為原月費的 44 倍），作者據此推估 Anthropic 目前綁定方案的實際補貼倍數約 **13 倍**，並質疑此補貼能持續多久。**與既有補貼估計的關係**：與既有 token-xray（2026-05-28）計算之「Max $200/月方案隱性補貼 17 倍」估計方法不同（一為 Team 綁定方案對比純 API 計費、一為 Max 20x 方案對比 API 等值用量換算），但方向一致，均指向 Anthropic 訂閱方案對重度使用者提供兩位數倍率的補貼；補貼可持續性的商業風險詳見 [[topics/anthropic-business]]「財務狀況」表（Hacker News/modelplane.ai，https://modelplane.ai/blog/ai-coding-subsidy-multiple）

#### 2026-06-16：Claude Code on AWS Bedrock 首日成本實測 $8.43

- **第一手成本實測**：開發者記錄改用 AWS Bedrock 執行 Claude Code 第一天即產生 **$8.43** 費用，分享設定預算警示的經驗；動機是規避 Anthropic 原生訂閱方案的 5 小時 session 與週用量上限（見上方「配額與速率」爭議）（dev.to https://dev.to/aws-builders/how-my-first-claude-code-on-aws-bedrock-experiment-cost-me-843-in-just-one-day-1835）
- **注意**：屬個人開發者單日數據，未見長期追蹤或企業規模驗證；Bedrock 走 API 費率計費，脫離訂閱配額限制的同時亦脫離訂閱補貼，長期成本需視實際用量規模評估

#### 2026-05-18：Uber 企業成本警示、Opus+Sonnet 混合策略

- **Uber 燒光 2026 全年 AI 預算 — Forbes 深度報導**：Forbes 確認 Uber 工程師大規模使用 Claude Code，四個月耗盡全年 AI 預算；Uber CTO 承認效益顯著但成本失控；此事件揭示企業 AI 工具採購在缺乏細粒度使用量控管工具下的系統性成本風險，可能加速 Anthropic 推出企業層級的預算管理機制；engram v3.4.0 同日推出 `/engram:cost` 即時 token 監控回應類似需求
- **「Opus 規劃 + Sonnet 執行」成本優化策略熱議**：社群討論以 Opus 4.7 處理需要深度推理的規劃階段，再切換至 Sonnet 4.6 執行具體任務，從而降低整體 token 費用；此策略本質是利用模型能力差異進行任務分層，是 6/15 計費調整後成本優化的新主流方向；見 [[news/2026-05-18]]

#### 2026-05-12：費用透明度三連擊

- **Ultra Review 費用落差**：每次 $100–140（適用 50–100 個檔案 PR），但官方估算顯示 $5–20；相差數倍
- **Max 5x ROI 分析**：正常月 API 等值 $159；高峰月（密集 Claude Code）高達 $6,600；訂閱節省最高 65 倍
- **第三方平台 Max 20x ToS 風險**：以第三方 $100/月使用更高階方案，封禁風險不明

#### 2026-05-11：Claude Code 30 天 $514 詳細成本分析

50 個工作階段真實數據；同作者提供配額管理完整指南（2026 版），為目前社群最完整的長期費用追蹤案例。

#### 2026-05-10：Pay-as-you-go Session 費用 $6–10 的成因

Prompt cache 不跨 session，每次重啟需重讀大量相同檔案。對策：本機圖資料庫索引（LLM 生成 codebase 關係圖）、Tokenyst（任務層級 token 預算工具）。

#### 2026-05-06：三起費用議題同日爆發

- **GitHub Copilot Pro+ 對 Opus 27 倍加價**：推動開發者比較直接 API 成本
- **94% Token 流向 Opus**：Claude Code 預設路由問題，可在 CLAUDE.md 設定分層路由解決
- **Agent 工具迴圈帳單失控三案例**：yarn.lock 衝突 £400、agent daemon $500；需工具層面費用硬上限

#### 2026-05-03：AI 代理帳單失控進入主流媒體

Claude Code 代理無監督運作一夜燒掉數百至數千美元成為主流議題；Anthropic 儀表板金額嚴重滯後問題持續未改善。

#### 2026-05-02：Uber 企業案例——四個月燒光全年 AI 預算

工程師月均費用 $500–2,000；95% 工程師使用 AI 工具；70% 提交代碼來自 AI；CTO 表示明年將重建 AI 預算策略。為業界大規模部署最完整的成本一手數據。

#### 2026-05-01：$6,000 單夜燒掉

`/loop` 指令遺忘後無人看管執行 46 次（26 小時）；Anthropic 儀表板金額嚴重滯後，缺乏即時消費通知。

#### 2026-04-30：雲端環境 `ANTHROPIC_API_KEY` 計費陷阱

雲端環境設置此環境變數時，所有 Code 呼叫自動改走 API 計費通道。**立即行動**：檢查 CI/CD、Docker、K8s 環境是否有此變數。

---

## 宏觀趨勢

⚠️ 此趨勢判斷於 2026-06-16 政策暫停後暫時擱置，待政策重啟確認。

Anthropic 的計費方向明確：**訂閱方案僅涵蓋人工互動使用，自動化工作流必須自行負擔 API 費用**。6/15 政策是此方向的正式成文化，非突發轉向。企業大規模部署須預先規劃人均月費上限與即時費用警報機制。

---

## Token 成本注意事項

- 多個 MCP Server 併用時，每條訊息可能消耗 **20,000+ tokens**
- 切換至 Opus 4.7 會清除整個 prompt cache，導致額外 token 成本

---

## 相關議題

- [[topics/competitor-landscape]]（用戶因費用轉向 Codex / Gemini）
- [[topics/code-quality-decline]]（用戶因品質下滑要求退款或降級）
- [[entities/openclaw]]（第三方工具計費政策演變）

## 參考來源

事件出處見各條目內文連結；2026-04-25 起各日日報均有覆蓋。

- [官方說明文件](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [官方定價頁](https://www.anthropic.com/pricing)
