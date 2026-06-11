# Anthropic 訂閱方案與計費政策

**類型：** policy
**狀態：** active（持續調整中）
**領域：** 💼 商業
**最後更新：** 2026-06-10（Claude Fable 5 定價 $10/$50 per million token；6/22 後訂閱方案不再涵蓋 Fable 5）

---

## 計費架構（2026-06-15 起正式生效）

Anthropic 將使用場景切分為**兩條獨立計費軌道**：

### 軌道 1：互動式使用（Interactive）— 訂閱涵蓋

| 涵蓋範圍 | 說明 |
|---------|------|
| Claude.ai 網頁介面 | 人工驅動對話 |
| Claude Code 互動 session | 使用者在終端手動操作 |
| 一般 API 互動呼叫 | 人工觸發的請求 |

→ 費用包含在訂閱月費內，受「5 小時視窗速率上限」管控

---

### 軌道 2：程式化使用（Programmatic）— 信用池計費

| 涵蓋範圍 | 計費方式 |
|---------|---------|
| `claude -p`（headless / 非互動模式） | 按完整 API 費率，從信用池扣除 |
| Agent SDK 呼叫 | 同上 |
| Claude Code GitHub Actions | 同上 |
| 第三方 Agent SDK app（如 Zed、Conductor、T3 Code） | 同上 |

→ **不享任何訂閱折扣**，信用池用盡後需額外購買

---

## 方案對照表（2026-06-15 後）

| 方案 | 月費 | 互動用量 | Programmatic 信用池/月 |
|------|------|---------|----------------------|
| Free | $0 | 基本限制 | 無 |
| Pro | $20 | 標準 | $20（按 API 費率） |
| Max 5x | $50 | 5× Pro | $100（按 API 費率） |
| Max 20x | $200 | 20× Pro | $200（按 API 費率） |
| API only | 按量 | — | 直接按 API 費率 |

> **財務衝擊試算**：Max 5x 用戶若程式化使用達週配額 40%，換算 API 費率約需 **$1,000/月**（是月費的 20 倍）

> **過渡緩衝**：6/15 前 Anthropic 臨時將所有付費方案週用量上限**提高 50%**（至 7 月 13 日）

---

## 6/15 前建議行動

- [ ] 盤點所有 `claude -p`、Agent SDK、CI 自動化的月均用量
- [ ] 對照各方案信用池上限，評估是否足夠或需升級/備案
- [ ] 若使用 Zed、Conductor、T3 Code 等第三方工具，確認其計費切換說明
- [ ] 設定費用警報（Anthropic 儀表板有顯示延遲，建議自建監控腳本）

---

## 費用管控技巧

| 問題 | 建議對策 |
|------|---------|
| Agent 無限迴圈燒錢 | 工具層面設硬性費用上限；不依賴 Claude 自判 |
| 94% token 流向 Opus | 在 CLAUDE.md 設定分層模型路由（繁瑣任務指定 Haiku） |
| Session 重啟費用 $6–10 | 用本機圖資料庫索引取代每次重讀完整 codebase |
| 5 小時視窗浪費 | 預排一條輕量訊息提前啟動計時，確保工作時段完整使用 |
| Prompt cache 耗盡 | 監控 `~/.claude/projects/*.jsonl` 的 `cache_creation_input_tokens` |
| 儀表板金額嚴重滯後 | 自建腳本定期查詢 Anthropic API 用量，勿只看儀表板 |

---

## 重要政策變動紀錄

### 2026-06-09：Claude Fable 5 定價發布

- **Fable 5 定價**：$10 input / $50 output per million token（double Opus 4.8）；context window 1M；最大 output 128K
- **6/22 前含括於訂閱**：Pro / Max 訂閱用戶 6/22 前免費使用 Fable 5，之後改為消費制（enterprise consumption-based plan 或 API 直接計費）
- **Mythos 5**（無護欄完整版）：僅限授權用戶，定價比 Fable 5 更高，細節未公開
- **30 天資料保留政策**：Fable 5 / Mythos 5 所有流量（含 AWS Bedrock）強制保留 30 天，資料離開 AWS 安全邊界；企業應評估隱私影響

### 2026-05-23：模型別名退役警示

- **⚠️ claude-opus-4-20250514 與 claude-sonnet-4-20250514 退役（2026-06-15）**：Anthropic 確認這兩個模型版本將於 6/15 正式退役，使用舊版別名（如 `claude-opus-4-0`、`claude-sonnet-4-0`）的生產環境程式碼將開始失敗。需在 2026-06-14 前遷移至新版模型 ID（如 `claude-opus-4-5-20251001`、`claude-sonnet-4-6-20260101` 等）
- **Max 方案實質差異說明**：dev.to 分析文章確認 Max 方案不僅是「更多用量」，而是在 context window 長度、Claude Code 可用額度、優先排隊等方面有結構性不同；Max 5x（$100/月）vs Max 20x（$200/月）在 agentic 工作流上的差異尤其顯著

### 2026-05-21：6/15 計費影響持續發酵，社群替代方案成熟

- **clarp（drop-in claude -p 替代品）**：開發者開源 clarp，在本地啟動隱藏 PTY 的 Claude Code 互動 CLI，並透過唯讀代理攔截 Anthropic API 串流，重建 `claude -p` 行為；多數專案只需改一個 binary 名稱即可遷移至互動計費軌道，是 6/15 後最直接的工作流保全方案
- **vibe-skill（57M tokens 節省，成本降逾九成）**：開發者開源 vibe-skill，讓 Claude 負責規劃與 diff 審查，實際撰碼任務委派給 Mistral Vibe（低成本執行層）；10 天實測節省 57M tokens，成本降逾九成，Claude 品質的規劃輸出基本保留；是 6/15 計費壓力下最具代表性的混合策略落地案例
- **atrium 工作區設計含 6/15 預案**：macOS 工作區管理工具 atrium 在設計動機中明確提及「規避 6/15 API 計量鎖定」，顯示 6/15 政策已開始影響工具設計決策
- **dev.to 分析文章**：「Anthropic Is Splitting Claude Code's Billing — What It Means for Dev Teams Using Agents」整理 6/15 後對依賴 print mode 自動化工作流程的開發團隊衝擊，clarp 和 vibe-skill 均在文章中被引用為社群因應方案

### 2026-05-20：Claude Code 定價溝通混亂事件（Simon Willison 分析）

- **Claude Code 曾短暫顯示為 Max 方案專屬功能**：Anthropic 定價頁在毫無公告的情況下短暫顯示 Claude Code 為 Max 方案（$100–$200/月）專屬功能，引發社群恐慌後已撤回。Simon Willison 深度分析指出問題根源是 Anthropic 的定價溝通策略缺乏透明度。此事件發生於 2026-04-22 前後，但 HN 於 2026-05-19/20 再度廣泛討論，反映社群對 Anthropic 定價透明度的持續不滿
- **建議**：用戶應持續追蹤官方 [Choosing a Plan](https://www.anthropic.com/pricing) 頁面，而非依賴第三方資訊；Anthropic 任何定價頁更動均可能未經公告

### 2026-05-19：臨時用量提升優惠、企業成本壓力持續

- **Anthropic 臨時用量提升**：部分使用者收到 Anthropic 提供的臨時優惠——5 小時使用量加倍（x2）+ 每週上限提高 50%；社群反應熱烈，積極利用有限期額度進行密集開發；此舉可能是為緩解近期用量限制帶來的用戶不滿，或配合 Max 方案促銷；具體受惠條件 Anthropic 未公開說明
- **企業帳單達雲端費用三倍**：HN 討論串揭示多家企業月 AI 工具費用已達雲端 SaaS 費用三倍，部分企業即將全面停用 Claude Code 並禁止個人方案；顯示用量暴增 + 計費透明度不足的問題仍在持續（見 [[topics/enterprise-cost-management]]）

### 2026-05-18：Uber 企業成本警示、Opus+Sonnet 混合策略

- **Uber 燒光 2026 全年 AI 預算 — Forbes 深度報導**：Forbes 確認 Uber 工程師大規模使用 Claude Code，四個月耗盡全年 AI 預算；Uber CTO 承認效益顯著但成本失控；此事件揭示企業 AI 工具採購在缺乏細粒度使用量控管工具下的系統性成本風險，可能加速 Anthropic 推出企業層級的預算管理機制；engram v3.4.0 同日推出 `/engram:cost` 即時 token 監控回應類似需求
- **「Opus 規劃 + Sonnet 執行」成本優化策略熱議**：社群討論以 Opus 4.7 處理需要深度推理的規劃階段，再切換至 Sonnet 4.6 執行具體任務，從而降低整體 token 費用；此策略本質是利用模型能力差異進行任務分層，是 6/15 計費調整後成本優化的新主流方向；見 [[news/2026-05-18]]

### 2026-05-17：`claude -p` 計費衝擊持續、多帳號架構合規紅線

- **`claude -p` 計費調整後的工作流適應**：dev.to 出現以 AI agent 第一人稱視角記錄 6/15 計費規則調整後如何重新設計自動化工作流的文章，代表計費政策變更對長期用戶的實際衝擊仍在延續，開發者正積極找因應方案
- **多帳號 Claude Code 架構合規邊界明確**：文章詳細比較兩種多帳號 Claude Code 使用架構，明確指出其中一種已被 Anthropic 視為違反使用條款（ToS），提醒規模化使用需求的開發者在帳號管理策略上需注意合規邊界；目前僅知「其中一種被禁」，未公開具體判斷標準

### 2026-05-16：Max 用量上限未實際生效、社群促銷驗證、成本焦慮高峰

- **Max 20x 用量上限未生效（數學實證）**：一位 Max 20x 重度用戶以計算明確證明——5/6 宣佈的 2 倍 session 上限與 5/13 宣佈的 1.5 倍週用量上限均未在其帳號生效；客服零回應；多位用戶跟進驗證，顯示「宣告即生效」與實際體驗可能存在系統性落差
- **社群系統驗證 Anthropic 促銷時序**：Reddit 用戶系統整理 2025 年 8 月以來所有官方用量促銷完整時序（對照官方來源），引發對方案透明度的廣泛質疑，討論串聚焦「宣告與實際生效」之間的落差
- **Lanes.sh 說明 6/15 影響範圍**：Lanes.sh 因架構不同而未受波及，並提供清楚分析：Zed、Conductor、T3 Code、superset.sh 等建構於 Agent SDK 之上的平台的 Max 5x 訂閱用戶實際可用量大幅縮水
- **API 費用焦慮達本週最顯著高峰**：同日出現多篇 Claude Code API 費用優化指南（7 種降費策略、不改代碼省 10–30%、bootstrapped 創業者費用管控討論、Claude Code 替代方案整理），顯示開發者對 API 費用的集體焦慮達近期峰值
- **週用量配額意外提前重置（bug 或後端調整）**：部分用戶反映在正常重置日前週配額意外歸零，原重置日期未變（等同一輪額外免費用量）；不清楚是後端調整副作用或 bug；社群擔心用量可能被「追回」
- **「用 credit 包裝的漲價」批評**：部分開發者在優化指南中明確指出 6/15 公告本質是 API token 上限收緊而非計費重組；Anthropic 對此立場無官方回應

### 2026-05-15：6/15 計費變更社群反應、第三方工具衝擊、官方回應

- **社群情緒**：約六成負面（Max 5x $100 信用池對重度 agent 用量嚴重不足）、兩成理解、兩成觀望
- **受衝擊工具**：Zed、Conductor、T3 Code、Superset；Lanes 聲明不受影響；Zed 已發布應對說明
- **官方回應**：Ars Technica 專訪 Claude Code 產品主管，說明「lean harness」設計哲學，社群認為說明仍不足
- **灰色地帶**：VS Code 擴充套件用量是否計入新信用池，Anthropic 尚未明確答覆
- **Ungate 工具出現**：宣稱可將 Max 訂閱用量路由至 Cursor（$100 = $2,000 API 等值）；**使用前確認 ToS**

### 2026-05-14：正式宣布 Programmatic 計費分離

Anthropic 宣布 6/15 起 `claude -p`、Agent SDK、Claude Code GitHub Actions 及第三方 Agent SDK app 完全脫離訂閱，改為獨立信用池，按完整 API 費率計費。主要後續效應：
- 部分用戶宣告取消訂閱，轉向 Codex 或 Gemini（見 [[topics/competitor-landscape]]）
- 社群開發者發布 `claude-pee` 繞過工具（PTY 終端模擬），Anthropic 尚未回應
- OpenClaw 等第三方工具恢復，但改走信用池計費（見 [[entities/openclaw]]）

### 2026-05-13：Anthropic 定價主導權強勁

The Information 報導企業客戶即使面對成本上漲仍持續採用；Anthropic API 定價策略短期維持強勢。

### 2026-05-12：費用透明度三連擊

- **Ultra Review 費用落差**：每次 $100–140（適用 50–100 個檔案 PR），但官方估算顯示 $5–20；相差數倍
- **Max 5x ROI 分析**：正常月 API 等值 $159；高峰月（密集 Claude Code）高達 $6,600；訂閱節省最高 65 倍
- **第三方平台 Max 20x ToS 風險**：以第三方 $100/月使用更高階方案，封禁風險不明

### 2026-05-11：Pro 方案 0% 用量仍遭收費

用戶儀表板顯示 0% 情況下，2–3 個提示後被收取 $3.37 Extra Usage；根本問題：1M context window 觸發 API 計費通道，獨立於訂閱用量計量。Anthropic 尚未公告改善。

### 2026-05-11：Claude Code 30 天 $514 詳細成本分析

50 個工作階段真實數據；同作者提供配額管理完整指南（2026 版），為目前社群最完整的長期費用追蹤案例。

### 2026-05-10：Opus API 速率限制悄悄調降

ServeTheHome 首報；與 SpaceX 算力到位（Sonnet 速率翻倍）同時期出現，顯示差異化模型速率管理。

### 2026-05-10：Pay-as-you-go Session 費用 $6–10 的成因

Prompt cache 不跨 session，每次重啟需重讀大量相同檔案。對策：本機圖資料庫索引（LLM 生成 codebase 關係圖）、Tokenyst（任務層級 token 預算工具）。

### 2026-05-07–09：SpaceX 算力到位，速率上限翻倍

三項變更同步生效：Pro/Max Claude Code 五小時視窗速率翻倍、取消 Pro/Max 尖峰時段降速、API Tier 4+ 速率提升。Dario Amodei 在 Code with Claude 大會現場宣布。

### 2026-05-06：三起費用議題同日爆發

- **GitHub Copilot Pro+ 對 Opus 27 倍加價**：推動開發者比較直接 API 成本
- **94% Token 流向 Opus**：Claude Code 預設路由問題，可在 CLAUDE.md 設定分層路由解決
- **Agent 工具迴圈帳單失控三案例**：yarn.lock 衝突 £400、agent daemon $500；需工具層面費用硬上限

### 2026-05-05：提示快取窗口悄悄縮短（未公告）

Anthropic 於 4 月初靜默縮短預設 prompt cache 窗口，實質提高 token 消耗速度；為繼 Token 費用估算翻倍（2026-04-29）後第二次被社群自行發現的靜默計費改動。

### 2026-05-03：AI 代理帳單失控進入主流媒體

Claude Code 代理無監督運作一夜燒掉數百至數千美元成為主流議題；Anthropic 儀表板金額嚴重滯後問題持續未改善。

### 2026-05-02：Uber 企業案例——四個月燒光全年 AI 預算

工程師月均費用 $500–2,000；95% 工程師使用 AI 工具；70% 提交代碼來自 AI；CTO 表示明年將重建 AI 預算策略。為業界大規模部署最完整的成本一手數據。

### 2026-05-01：$6,000 單夜燒掉

`/loop` 指令遺忘後無人看管執行 46 次（26 小時）；Anthropic 儀表板金額嚴重滯後，缺乏即時消費通知。

### 2026-04-30：雲端環境 `ANTHROPIC_API_KEY` 計費陷阱

雲端環境設置此環境變數時，所有 Code 呼叫自動改走 API 計費通道。**立即行動**：檢查 CI/CD、Docker、K8s 環境是否有此變數。

### 2026-04-29：Token 費用預估翻倍（靜默修訂）

Business Insider 報導 Anthropic 低調調高 Claude Code 預期 Token 費用估算值一倍，無官方公告。

### 2026-04-28：Opus「圍牆內圍牆」事件（已修正）

Pro 用戶無預告須額外購買才能使用 Opus；Anthropic 事後澄清 Pro 仍可存取，但信任損失已造成。

### 2026-04-25：HERMES.md 靜默計費 Bug

git commit 歷史出現大寫字串「HERMES.md」會觸發靜默切換至 API 額外計費模式，已知損失單日 $200；Anthropic 確認為 bug 但**拒絕退款**。
**立即行動**：`git log --all | grep -i HERMES`
來源：[GitHub Issue #53262](https://github.com/anthropics/claude-code/issues/53262)

### 2026-04-25：第三方 Agentic 工具配額限制

The Verge 報導 Anthropic 限制 OpenClaw 等工具；Claude Code 負責人 Boris Cherny：「訂閱方案的設計並非為這類第三方使用模式而生。」（預示 6/15 政策的早期信號）

---

## 宏觀趨勢

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

- [[news/2026-04-25]]
- [[news/2026-04-26]]
- [[news/2026-04-27]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [[news/2026-05-02]]
- [[news/2026-05-03]]
- [[news/2026-05-04]]
- [[news/2026-05-05]]
- [[news/2026-05-06]]
- [[news/2026-05-07]]
- [[news/2026-05-08]]
- [[news/2026-05-09]]
- [[news/2026-05-10]]
- [[news/2026-05-11]]
- [[news/2026-05-12]]
- [[news/2026-05-13]]
- [[news/2026-05-14]]
- [[news/2026-05-15]]
- [[news/2026-05-16]]
- [官方說明文件](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
