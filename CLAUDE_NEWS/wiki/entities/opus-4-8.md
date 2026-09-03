---
page: "entities/opus-4-8"
kind: "entity"
type: "model"
status: "active（已被取代，次旗艦地位由 Opus 5 接手）"
domain: "🤖 模型"
last_updated: "2026-08-29"
last_news_update: "2026-08-27"
status_main: "active"
days_since_news: 7
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 7
inbound_links: 12
attribution_count: 6
attribution_last: "2026-07-25"
top_source: "google-news"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Opus 4.8

**類型：** model
**狀態：** active（已被取代，次旗艦地位由 Opus 5 接手）
**領域：** 🤖 模型
**首次出現：** 2026-05-28
**最後更新：** 2026-08-29
**最後新聞更新：** 2026-08-27

> **最新進展**（2026-08-27）
> GitHub Issue 回報 Claude 4.7、4.8、5.0 與 Fable 日益預設重複修辭套路、難維持連貫散文，即使給明確風格指示仍難改善，跨模型代際共同問題（106 則留言、517 個反應）；完整記錄見 [[entities/opus-5]]。Opus 4.8 本身自 2026-07-25 起已由 [[entities/opus-5|Claude Opus 5]] 取代次旗艦地位（詳見下方「現況」）。

---

## 現況

**2026-08-27 最新**：GitHub Issue #77136 回報 Claude 4.7、4.8、5.0 與 Fable 日益預設輸出重複修辭套路、難維持連貫散文，即使給明確風格指示仍難改善，跨模型代際共同問題，已累積 106 則留言、517 個反應，尚無官方回應。完整記錄與最新社群回饋見 [[entities/opus-5]]「歷史記錄」（GitHub Issue #77136，2026-08-27）。

**2026-07-25**：Claude Opus 5 正式發布，取代 Opus 4.8 成為次旗艦、Claude Max 新預設模型、Claude Pro 最強模型（詳見 [[entities/opus-5]]）。近兩週的「Opus 5」傳聞（HackerNoon 07-24、TestingCatalog 07-23 等，見下方「下一代模型觀察」歷史記錄）就此獲得官方證實。Opus 4.8 本身能力與規格未變，仍是 Fable 5 護欄觸發時的 fallback 模型，但已不再是次高階公開模型的首選。

Claude Opus 4.8 於 2026-05-28 正式發布，同步推出 Dynamic Workflows（Research Preview）與 Fast Mode 降價，是 2026 年以來 Anthropic 發布規模最大的旗艦更新。**2026-06-09 Claude Fable 5 發布後，Opus 4.8 不再是最高階公開模型**，現作為 Fable 5 安全分類器觸發時的 fallback 模型（< 5% session 觸發）——出口管制期間（2026-06-13 至 07-01）Opus 4.8 曾是 Fable 5 全面下線時的唯一替代選項，管制已於 2026-07-01 解除，現行 fallback 角色改由 Fable 5「Defense in Depth」分類器觸發（詳見 [[entities/fable-5]]）。核心指標：SWE-bench Pro 69.2%（1M context window）；Fast Mode 速度為標準的 2.5 倍、費率降至前代的 1/3。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 大型 agentic 任務、multi-step 工作流、需要 1M context 的長文件處理 |
| 不適合 | 追求穩定性的生產環境（初期社群反映有行為退步）|

> 詳細最新熱度見 [[feature-radar]]

---

## 核心指標

| 項目 | 數值 |
|------|------|
| SWE-bench Pro | 69.2% |
| Context Window | 1M tokens |
| 定價 | 與 Opus 4.7 相同 |
| Fast Mode 速度 | 2.5× 標準速度 |
| Fast Mode 費用 | 前代的 1/3 |
| Dynamic Workflows 子代理上限 | 1,000 個平行子代理 |

---

## 新功能

### Dynamic Workflows（Research Preview）

允許 Claude Code CLI、Desktop 及 VS Code 擴充在單一 session 內動態撰寫 orchestration scripts，最多啟動 **1,000 個平行子代理**，處理超大規模工作：

- 跨 service 的 bug hunt
- 觸及數百個檔案的大型 migration
- 多角度壓力測試

**目前限制：** Research Preview，限 Max 方案用戶。見 [[feature-radar]]。

```bash
# Dynamic Workflows 在 Claude Code CLI 中自動啟用（Max 方案）
claude code "Migrate all legacy API endpoints in this monorepo"
```

### Fast Mode

Opus 4.8 的 Fast Mode（2.5× 速度）費用降至前代的 **1/3**，顯著降低高速推論的成本門檻。

### 使用者可控任務努力程度

claude.ai 用戶現可調節 Claude 在任務上投入的努力程度，不再完全由模型自行決定。

---

## 社群評價

### 正面
- HN score 1662（發布後 24 小時最高討論量）
- Dynamic Workflows 被視為 Claude Code 工作流的重大突破
- Fast Mode 降價受到廣泛歡迎

### 負面（待觀察）
- ⚠️ **第三方對比評測失利（2026-06-24）**：RuntimeWire 對 Opus 4.8 與 Gemini 3.5 Flash 進行評測，最終分數 35.4 對 34.8 由 Gemini 略勝；Gemini 在四項任務贏三項。Claude 的失分主因是 messy-orders-to-json 任務中輸出含 Markdown code fence，違反 JSON-only 指令；分析師指出此為指令遵循失誤，非能力差距，HN score 3（低討論量，參考價值有限）
- ⚠️ **跨平台高錯誤率事件（2026-06-24）**：Claude Opus 4.8 出現跨 API、Claude Code 與 Console 的高錯誤率，Anthropic 正在調查中（[dev.to](https://dev.to/damogallagher/claude-opus-48-is-seeing-elevated-errors-across-api-claude-code-and-console-1g9a)）；影響範圍較 6/22 更廣
- ⚠️ **529 Overloaded 大規模事件（2026-06-21~22）**：Anthropic 官方確認 Opus 4.8（及 4.7、4.6、Sonnet 4.6）出現 elevated error rates；另有全球約 90 分鐘中斷；Max Plan 用戶反映自 06/21 起錯誤持續激增，coding tasks 與 Claude Code 受影響尤重（[cybersecuritynews.com](https://cybersecuritynews.com/anthropic-claude-ai-outage/)）
- ⚠️ Reddit 部分用戶反映 4.8 引入奇怪的 "pecl scripts" 行為，強制使用自訂工具做簡單文件修改
- ✅ "thinking blocks cannot be modified" 400 錯誤：v2.1.156 已修復（[[entities/claude-code]]）
- ⚠️ MarginLab SWE-bench-Pro 追蹤發現：Opus 4.7 在 4.8 發布前一週有統計顯著下降，發布後立即恢復（見 [[topics/code-quality-decline]]）
- ⚠️ **UltraCode 嚴重 bug（2026-05-30）**：Dynamic Workflows 用戶回報 1.7M tokens 消耗後零輸出；8 個子代理陷入退化迴圈（結果未快取、多次重新部署）；Anthropic 無退款機制；建議生產環境設定嚴格 token 上限
- ⚠️ **Thinking 模式 context window 超快耗盡（2026-05-31）**：用戶實測 Opus 4.8 + Thinking 每輪最高寫入 **900,000 cache tokens**，Opus 4.7 僅 14,000–34,000（40–60 倍差距）；重度工作流需全面重新評估 session 設計
- ⚠️ **ultracode 模式 70 agent 實測（2026-05-31）**：用戶請求「deep search」後系統自動生成約 70 個 agent 跑四階段 pipeline；展示 Dynamic Workflows 規模上限，但引發 context 耗盡與費用可控性的實際討論
- ⚠️ **德語品質退步（2026-05-29–30）**：德語用戶反映文法異常、Max Thinking 模式過慢；整體感覺不及 Opus 4.6 穩定（Reddit）
- ⚠️ **Qwen distillation 爭議（2026-05-29–30）**：社群截圖流傳 Opus 4.8 自稱 Alibaba Qwen；主流判斷為 proxy 詐騙服務而非真實 distillation（HN score 20）

---

## 與前代比較

| 指標 | Opus 4.7 | Opus 4.8 |
|------|---------|---------|
| SWE-bench Pro | — | 69.2% |
| Context Window | 200K | 1M tokens |
| Dynamic Workflows | ❌ | ✅ Research Preview |
| Fast Mode 費用 | 基準 | 1/3 |
| 定價 | 基準 | 同價 |

---

## 相關議題
- [[entities/opus-5]]（2026-07-25 發布，取代 Opus 4.8 成為次旗艦，官方稱相同成本下效能大幅提升）
- [[entities/fable-5]]（現任最高階公開模型；Opus 4.8 為其護欄觸發時的 fallback）
- [[entities/sonnet-5]]（2026-07-01 發布，效能接近 Opus 4.8 但成本低約 60%）
- [[topics/code-quality-decline]]（升版前效能下降事件）
- [[entities/opus-4-7]]（前代模型）
- [[topics/anthropic-business]]（同步融資公告背景）
- [[entities/claude-code]]（Dynamic Workflows 整合）
- [[feature-radar]]（功能熱度追蹤）

## 參考來源
- [[news/2026-05-29]]
- [Claude Opus 4.8 官方公告](https://www.anthropic.com/news/claude-opus-4-8)
- [Dynamic Workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

## 下一代模型觀察：「Opus 5」傳聞（✅ 已於 2026-07-25 獲官方證實，詳見 [[entities/opus-5]]）

以下歷史記錄保留傳聞階段的原始查證過程，供時序參考；Opus 5 現況與能力細節請見 [[entities/opus-5]]，不在此頁重複維護。

**2026-07-24**：HackerNoon 分析近期網路流傳的 Claude Opus 5 傳聞截圖，指出「通過了截圖測試，卻未通過 API 合約層級的驗證」；與 07-13 dev.to 分析方向一致。**2026-07-25 官方正式發布 Opus 5，此傳聞真偽問題已由發布本身解答，不再懸置**（[Google News/HackerNoon](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRF9EUHUybk1zS3N5T0lNdUYyVHJ1ZVl3bktrUjZZSWVQUUU3c0t0Tzh1UFdXYTdITHpRYUJJVmJ2SVhrNko1eHdUdDNHNzRtRk1xdUd0Qk81ZkRiQUNpeVVVUHhnTDZXelFhcnNOYzhsVUxGWFUwYjZJUnk3cXRpUEExalhmVi01X0w4LTVTRmZHUmMtRkJzc0ZOelJnVkVk?oc=5)，2026-07-24）。

**2026-07-23**：TestingCatalog AI News 報導 Anthropic 正在為可能的 Claude Opus 5 推出做準備（[Google News/TestingCatalog AI News](https://news.google.com/rss/articles/CBMikAFBVV95cUxQRWYtODJYNVFKWk5UUXlaN0UtdTl6c2tRMlBrR0IwQ0Y1Y1htUWowSWJ6N0o0d2k4aEdqdzRQM1dzZXZwT3FhNjQ5bDhxNHV4LVVpZVJyLWd0TjFtZFpkS3RCbzlHMVdjOUc4LTQzSkFSZENpd25JQTBfWmZBMk0yZFkwaW1HNEpHT3RaLTV0RDg?oc=5)，2026-07-23）——**由 2026-07-25 正式發布確認**。

**2026-07-13**：dev.to 作者 tokenmixai 於〈I Traced 4 Claude Opus 5 Signals. The Release Date Still Isn't Real Yet.〉一文中，比對 Anthropic 模型型錄、定價文件與過往發布節奏，認為「Opus 5」的存在具一定可信度，但強調坊間流傳的確切發布日期與跑分數字目前均缺乏佐證（"Opus 5 is plausible, but every exact date and benchmark circulating today is unsupported."）。單一 dev.to 分析文章，非官方訊號（[dev.to](https://dev.to/tokenmixai/i-traced-4-claude-opus-5-signals-the-release-date-still-isnt-real-yet-2f2j)，2026-07-13）。此連結於 2026-07-16 補齊（原始記錄僅有泛用網域連結）。**存在性問題已由 2026-07-25 官方發布解答。**

**2026-07-20（市場推測，非官方公告）**：Proactive financial news（經 Google News 轉載，僅標題可用）報導〈Traders bet Anthropic will ship new Claude Opus model within days〉，指金融交易者押注 Anthropic 將於數日內推出新款 Claude Opus 模型（[Google News/Proactive financial news](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQUmt3Y0UyM1FRN3RYVkFvV1VrNXlpRW9BR0t4bkh3bGZ4VTdRVTF4M3RvdkQ2LTduSjlDRW5mSV9ZVHM5SW1qNkFDZkpLYUJjMmp1R0tWNUhzLWtHd3h6cW9TcWpmNjh2ZHVNcWJuRHZhNXU5c0cwd0hkMWpyRVZNRW5CQ2o3Z2dmNVhRUFlyLWVtRENnU3dEUmtCeUl6em5OdWVHdlZXSUpERjV0b3llZVRaVTVubUxXdlJwR3hBWUE4bGZaN2NnY3d3eXdjaUoyT0E?oc=5)）。**已由 2026-07-25 正式發布證實。**

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-08-27 | GitHub Issue #77136：跨模型代際重複修辭套路問題（詳見上方「現況」與 [[entities/opus-5]]） |
| 2026-07-25 | **✅ 官方證實：Claude Opus 5 正式發布**，取代 Opus 4.8 成為次旗艦、Claude Max 新預設模型、Claude Pro 最強模型；終結近兩週傳聞（詳見 [[entities/opus-5]]） |
| 2026-07-24 | **Opus 5 傳聞通過截圖測試，未通過 API 合約測試**：指出流傳截圖看似可信，但缺乏可程式化驗證的 API 層級證據——已由隔日官方發布證實 |
| 2026-07-23 | **Anthropic 正為潛在 Opus 5 推出做準備**：未提供具體時間或型號細節——已由 07-25 官方發布證實 |
| 2026-07-21 | 舊「Qwen distillation」爭議經媒體重提，冠以「蒸餾雙標」框架，詳見下方懸置細節 ⟨Q-01⟩ |
| 2026-07-20 | 市場傳聞 Anthropic 數日內將推出新 Claude Opus 型號——已由 07-25 官方發布證實 |
| 2026-07-09 | 錯誤率一度升高（同日解決）：03:50 UTC 確認已解決；同期 Reddit 反映近期體驗轉佳（弱訊號） |
| 2026-06-24 | 第三方評測：Gemini 3.5 Flash 35.4 vs Opus 4.8 34.8 略勝，指令遵循失誤所致（詳見上方「社群評價」） |
| 2026-06-24 | 跨平台高錯誤率事件：API、Claude Code、Console 三平台皆受影響，範圍較 6/22 更廣（詳見上方「社群評價」） |
| 2026-06-22 | 529 Overloaded 事件：全球約 90 分鐘中斷，Max Plan 用戶錯誤激增（詳見上方「社群評價」） |
| 2026-06-22 | Quake 瀏覽器版程序生成關卡：GitHub Copilot + Opus 4.8 編譯 WebAssembly 版本（[leereilly.net](https://leereilly.net/quakelike/)）|
| 2026-05-31 | Thinking 模式 context drain 量化：每輪最高 900K cache tokens（4.7 僅 14K–34K），引發費用可控性討論 |
| 2026-05-30 | UltraCode 嚴重 bug：1.7M tokens 消耗無輸出、無退款；Qwen distillation 爭議（主流否定）；v2.1.158 擴展至 Bedrock/Vertex/Foundry |
| 2026-05-29 | v2.1.156 修復 thinking blocks 400 錯誤；社群混合反映（行為退步投訴 + 大型任務好評）|
| 2026-05-28 | 正式發布，HN 1662 分；Dynamic Workflows Research Preview 同步推出；Fast Mode 降至前代 1/3 費用 |

**懸置細節**
- ⟨Q-01⟩ **2026-08-10 官方／第三方媒體查證**：查得 TipRanks 全文（非僅標題），確認非單純舊事重炒。核心事實：Anthropic 於 2026-06-10 致函美國參議院銀行委員會，指控與 Alibaba Qwen Lab 有關的操作者對 Claude 發動迄今最大規模蒸餾攻擊（約 25,000 個詐騙帳號、28.8M 次交流，2026-04-22 至 06-05 間）；隨後開發者發現 Claude Opus 4.8 在部分語言測試中會自稱是 Qwen，媒體以此建構「Anthropic 對外指控蒸餾、自身卻疑似蒸餾對手」的雙標敘事。多方技術分析（含 [blog.kilo.ai](https://blog.kilo.ai/p/did-claude-opus-48-distill-alibabas)）認為較可能的解釋並非真實蒸餾，而是訓練資料汙染／提示脆弱性／proxy 路由造成的中文語系身份錯亂 bug——與上方 05-30 條目「proxy 詐騙服務假冒 Claude」判斷方向一致，屬同一根因的延伸報導而非獨立新事件（[TipRanks](https://www.tipranks.com/news/anthropic-faces-distillation-hypocrisy-backlash-as-claude-claims-to-be-alibabas-qwen-ai)，2026-07-21）
