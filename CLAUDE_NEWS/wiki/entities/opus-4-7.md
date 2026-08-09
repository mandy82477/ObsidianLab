---
page: "entities/opus-4-7"
kind: "entity"
type: "model"
status: "active（已被取代，第三階旗艦）"
domain: "🤖 模型"
last_updated: "2026-07-19"
last_news_update: "2026-07-19"
status_main: "active"
days_since_news: 22
inbound_links: 11
attribution_count: 4
attribution_last: "2026-07-19"
top_source: "hacker-news"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Opus 4.7

**類型：** model
**狀態：** active（已被取代，第三階旗艦）
**領域：** 🤖 模型
**首次出現：** 2026-04-24
**最後更新：** 2026-07-19
**最後新聞更新：** 2026-07-19

> **最新已知問題**（2026-07-18）
> GitHub Issue 回報 Opus 4.7 在處理較長 payload 時，會把舊版 XML tool-use 格式混入 JSON tool call 中，累積 33 則留言、34 個讚同反應，尚無官方回應（[GitHub Issue #49747](https://github.com/anthropics/claude-code/issues/49747)，詳見「已知問題與爭議」）。

---

## 現況

**當前狀態：** 已被 Opus 4.8 / Fable 5 取代，現為第三階旗艦；agentic coding 場景仍有口碑，一般對話評價分歧。

Claude Opus 4.7 於 2026-04-24 正式發布，已相繼被 Opus 4.8（2026-05-28）與 Fable 5（2026-06-09）取代，現為第三階旗艦，不再是 Anthropic 最高階公開模型。伴隨發布的還有 Rate Limits API（管理員可程式化查詢速率限制）與 Managed Agents Memory Beta（在 `managed-agents-2026-04-01` 請求標頭下啟用）。

然而，該模型在社群中引發大量爭議，主要集中在定價策略與自適應思考深度的問題。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | Claude Code max-effort agentic coding、有明確結構的多步驟 agent 工作流 |
| 不適合 | 一般對話 Q&A、需可控思考深度的任務、探索性非結構化文本任務 |

> 詳細最新熱度見 [[feature-radar]]

---

## 已知問題與爭議

### XML tool-use 格式混入 JSON tool call（2026-07-18 回報）（🔴 未修復）
GitHub Issue 回報 Opus 4.7 在處理較長 payload 時，會把舊版 XML tool-use 格式混入 JSON tool call 中，造成工具呼叫解析異常；累積 33 則留言、34 個讚同反應，尚無官方回應（[GitHub Issue #49747](https://github.com/anthropics/claude-code/issues/49747)）。

### 529 Overloaded 大規模中斷（2026-06-21~22）
Anthropic 官方確認 Opus 4.7（及 Opus 4.8、4.6、Sonnet 4.6）於 2026-06-21 至 22 間出現 elevated error rates（HTTP 529 Overloaded）；另有全球約 90 分鐘完整中斷。Max Plan 用戶反映自上週起錯誤持續激增，尤以 coding tasks 與 Claude Code 受影響最重。此為 Opus 4.7 仍在線期間受影響的大規模服務事件（[cybersecuritynews.com](https://cybersecuritynews.com/anthropic-claude-ai-outage/)）。

### Token 消耗量顯著高於 4.6（2026-06-25 社群實測）（仍存在）
Reddit r/ClaudeAI 討論（2026-06-25）：使用者實測 Opus 4.7 在相同工作量下比 Opus 4.6 消耗更多 token，討論涉及 extended thinking 的隱性成本與用量控制策略。此問題與「Thinking 模式 context 快速耗盡」的 Opus 4.8 觀察互相呼應，指向 Anthropic 近期旗艦模型 thinking 路徑存在系統性高 token 消耗設計（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1ufanmj/did_anyone_else_notice_47_burns_way_more_tokens/)）。

### 思考深度不可控（仍存在）
Opus 4.7 由模型自行決定思考深度，而非由使用者控制。社群反映在需要深度推理的問題上，模型有時給出淺薄回應。這與使用者對「旗艦模型」的期待存在落差。

### 定價門檻提高（仍存在）
- 使用 Claude Code 存取 Opus 模型的**額外用量**現需 **Pro 以上方案**才能啟用
- 見 [[entities/pricing]]

### Usage Policy 隨機觸發拒絕（2026-04-26 以來）（仍存在）
Hacker News 多名用戶反映自 Opus 4.7 版本以來，Claude Code 頻繁出現隨機觸發 Usage Policy 拒絕的錯誤，無明確觸發條件。官方暫時建議切換至 `/model claude-sonnet-4-20250514` 作為緩解手段；根本原因尚未公開說明。

### Prompt Cache 問題（仍存在）
從其他模型切換至 Opus 4.7 時，整個 prompt cache 會被清除，對大型專案造成顯著的 token 成本增加。另有 Race Condition 問題：連續兩次 API 呼叫第二個請求約有 40% cache miss 機率，等待 2 秒可緩解（見 [[entities/claude-code]] 已知問題）。

### 生物/生技問題過度拒絕（2026-04-28 回報）（仍存在）
使用者向 Opus 詢問抗原腸道傳遞的**學術問題**時，遭平台以「違反使用政策」直接拒絕；批評者認為此類過度保守的過濾機制正在妨礙合法科學研究，且錯誤判定標準不透明。

### 效能退步與參數規模爭議（2026-04-30）（仍存在）
重度 Max 20x 訂戶發文直言 Opus 4.7 **嚴重退步**，主要問題是過度「後設化」——每個回覆都像在撰寫論文，無法直接回答問題。配合學術研究（arxiv 2604.24827）對模型參數量的估算：
- **Opus 4.7 估算：約 4T 參數**（疑似少於 Opus 4.6 的 5.3T）
- 若屬實，Opus 4.7 在參數規模上實為「降規」，與「旗艦模型」定位相悖
- Anthropic 未公開回應此估算數字

> ⚠️ **（2026-04-30 指控，至今無後續）**：arxiv 2604.24827 對 Opus 4.7 參數規模的估算，近 14 天日報無相關後續報導或官方回應，暫無法進一步驗證。

### 開發者回退 4.6 事件（2026-05-05 討論浮現）（仍存在）

dev.to 文章《Claude Opus 4.7 Is a Regression》在社群引發討論，部分開發者聲稱 Opus 4.7 在實際編碼任務中表現不如 4.6，已主動回退舊版本。分析：
- 此類「新模型退步」週期性出現，與 2026-04-30 的「後設化退步」批評相互呼應
- 原文標題具一定誇大成分，具體差異高度依賴使用情境（尤其是 vibe coding vs 研究型任務）
- 結合 2026-05-01 的 4.5→4.7 躍升感知討論，形成一致的社群觀察：Opus 4.7 升版感受因任務類型差異明顯

### Opus 4.7 提示詞行為世代性轉變（2026-05-11 社群發現）（仍存在）

一篇精讀 Anthropic 官方 31 頁提示詞指南的文章指出：Claude Opus 4.7 對指令的解讀**更趨字面（literal）**，4.6 時代有效的模糊通用提示（如「review this contract」、「analyze this code」）在 4.7 下表現明顯下滑，需要更明確的指令設計才能維持輸出品質。此轉變屬**世代性行為差異**，非 bug，而是刻意設計調整：
- 通用、隱含語境的提示在 4.7 的效果較 4.6 下降
- 需明確說明「做什麼」和「不做什麼」才能保持原有品質
- 依賴 4.6 era 提示的所有現有 prompt 工程實踐需系統性重新審視
- Anthropic 官方 31 頁提示詞指南（2026 年版）是最權威的參考依據

### Fortify 安全掃描修復失敗（2026-05-02 以來）（仍存在）
多名使用者以 Opus 4.7 Max effort 搭配 VSCode 嘗試修復 Fortify 安全掃描的高/嚴重等級漏洞時多次失敗，尤其輸入驗證類問題成功率極低。社群正向 Anthropic 徵求有效 prompt 策略，顯示 Opus 4.7 在安全漏洞自動修復這類需要高精確度的任務上存在可靠性問題。

### Tool/Connector Schema 洩漏（2026-04-27）（仍存在）
Claude Chat（Opus 4.7）在每則訊息末尾附加完整的 function schema 及 userStyle 內容，屬帳號層級污染，目前無官方修復（見 [[entities/claude-code]] 已知問題）。

### Opus 存取「圍牆內圍牆」事件（2026-04-28，已修復）
Anthropic 未事先公告即要求 Pro 用戶另購 Extra Usage 才能使用 Opus，事後已澄清 Pro 用戶仍可存取。見 [[entities/pricing]]。

### Transparency Hub 缺席（仍存在）
社群發現 Anthropic 未將 Opus 4.7 與 Mythos Preview 納入透明度中心（Transparency Hub），引發對資訊公開一致性的質疑。

---

## 研究發現：Opus 4.6 內部隱藏推理空間「J-space」（2026-07-12）

Anthropic 研究團隊使用名為 **J-lens** 的可解釋性工具，在 **Claude Opus 4.6**（非 4.7）內部發現一個稱為「J-space」的隱藏空間，模型在此空間中會「醞釀概念」，可能揭露其接下來要輸出的內容——即模型在生成最終回應之前，內部已存在一層可被觀測的中間推理表徵（[Hacker News](https://news.ycombinator.com)，2026-07-12 12:13 UTC，原文 technologyreview.com，「Anthropic found a hidden space where Claude puzzles over concepts」）。

**社群跟進（同日）**：Reddit r/LocalLLaMA 使用者將同一分析方法套用到開源模型 **Qwen3-8B** 做對照實驗，發文「Anthropic found Claude reasoning in silence (J-space) — we ran the same lens on open Qwen3-8B」（2026-07-12 14:22 UTC）；此為社群首次嘗試在開源模型上重現此可解釋性發現，尚待更多結果驗證是否為 Transformer 架構的通用現象或 Anthropic 模型特有機制。

**第二個獨立跟進實驗（2026-07-13）**：另一位獨立研究者在 [Reddit r/MachineLearning（週熱門）](https://www.reddit.com/r/MachineLearning/comments/1uv5l75/evaluating_jspace_entropy_as_an_error_predictor/) 發文，將 J-space entropy 作為錯誤預測指標，橫跨 7 個資料集在 **Qwen3-4B**（與上則 Qwen3-8B 不同規模）上進行評估。至此已有兩個獨立社群跟進實驗分別在 Qwen3-8B、Qwen3-4B 上驗證 J-space 概念，顯示此可解釋性方法正吸引開源社群跨模型規模覆現（推論）。

**記錄位置說明**：Opus 4.6 目前無獨立 entities 頁，此發現與本頁既有大量 Opus 4.6 對照內容（見「使用場景共識」）相關，暫記於此；若後續累積更多獨立於 4.7 的 Opus 4.6 動態，將評估另立頁面。

**MIT Technology Review 審慎解讀（2026-07-13）**：MIT Technology Review 發表〈What Anthropic's latest AI discovery does—and doesn't show〉，對上述 J-space 發現採取較審慎的態度，區分該研究實際證明了什麼、又還未能證明什麼；具體區分細節未見於本則摘要，暫列標題級記錄，待後續報導補充量化內容或方法論限制時再擴寫（[Google News／MIT Technology Review](https://www.technologyreview.com)，2026-07-13）。

---

## 同步發布功能

- **Rate Limits API**：允許管理員以程式化方式查詢當前速率限制
- **Managed Agents Memory Beta**：跨 session 持久記憶，透過請求標頭 `managed-agents-2026-04-01` 啟用

---

## 社群觀點

> 「Opus 4.7 可以用一個改變來拯救：讓使用者控制思考深度，而非模型自行決定。」
> — Reddit r/ClaudeAI

HN 討論（2026-04-27）顯示社群對 Sonnet 與 Opus 實際差距看法分歧：部分重度使用者認為兩者表現相近，但也有人指出 **Opus 在 context 不完整時明顯更穩定**，Sonnet 的非預期失誤率達 20–35%。此討論與隨機 Usage Policy 拒絕問題同步出現，使部分用戶暫時轉回 Sonnet。

Reddit 討論（2026-04-28）有開發者分享從 Opus 切換至 Sonnet 4.6 的實測對比：以 30% 月預算完成相當於前週 73% 預算的工作量，且程式碼品質更佳；關鍵在於調整 agent 工作流程設計，而非單純換模型。另有研究顯示 Opus 4.7 在三種 effort 等級（medium / high / xhigh）下拒絕姿態完全一致，**effort 僅影響回答深度，不影響安全邊界**（見 [[topics/community-tech-patterns]]）。

---

## 使用場景共識

### Claude Code 高 Token 模式 vs 一般對話體驗分歧（2026-05-20 社群回報）

Reddit r/ClaudeAI 實測分享：Opus 4.7 在 **Claude Code 搭配 max effort 模式**下表現亮眼，被評為目前最強的 agentic coding 體驗；但在**一般對話（chat）**中，即使開啟 adaptive thinking，仍有用戶認為不如 4.6 Extended 精準，且出現假設與幻覺問題。這印證了「Opus 4.7 是 agentic task 優先設計」的社群觀察——其設計目標可能是高 token、多步驟的 agent 工作流，而非傳統對話式 Q&A。

### Claude 4.7 vs 4.6 使用場景社群共識形成（2026-05-17）

開發者直接與 Claude 4.7 對話詢問兩版本差異，得出的使用場景區分框架開始在 r/ClaudeAI 形成社群共識：
- **Opus 4.7**：適合有明確結構的任務——代碼生成、agent 工作流、工具呼叫、需要精確格式輸出的場景
- **Opus 4.6（Sonnet 4.6）**：適合需要「填補空白」的探索性文本——文獻綜述、開放式分析、需要類人洞察的非結構化任務

此框架為近期「4.7 退步 vs 4.6 更好」的社群爭論提供了結構性解釋：差異並非能力退步，而是模型針對不同任務類型的設計取捨；也呼應 2026-05-11 發現的「4.7 更趨字面解讀」行為轉變。

### Opus 4.7 研究任務評價（2026-05-02）

一篇非主流評測文章力排「Opus 4.7 比前代更笨」的主流評價，指出 Opus 4.7 在**研究類任務**表現優異。作者認為過度冗長的問題源自使用場景不匹配（vibe coding 的快速回應 vs. 深度研究的詳盡分析），而非能力退步。評論區意見明顯分歧，但提供了 Opus 4.7 在特定任務場景下的正面評估資料點，補充了「後設化退步」批評的另一面。

### GPT-5.5 vs Opus 4.7 基準測試（2026-05-01）

開發者以 **Zod** 與 **graphql-go-tools** 兩個真實開源 repo 進行 56 個實際 coding 任務測試：
- **Opus 4.7**：寫出更精簡的 patch
- **GPT-5.5**：patch 更常通過 code review
- 作者強調不同 repo 結果可能不同，建議以自有資料跑測試，避免以此作為通用結論

### 4.5 → 4.7 版本躍升感知（2026-05-01）

使用 Claude Code 讓模型操作完整 repo 並執行終端指令的開發者表示，從 4.5 到 4.7 幾乎感受不到明顯躍升。社群討論指出對於一般全端 web 開發，版本差異可能不如官方宣稱明顯。此觀察與「後設化退步」問題（見上方效能退步條目）相互印證。

---

## 相關議題

- [[entities/opus-4-8]]（後繼旗艦，已取代 4.7）
- [[entities/fable-5]]（現任最高階公開模型）
- [[topics/code-quality-decline]]
- [[entities/pricing]]

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-05-20]]
- [[news/2026-04-27]]
- [[news/2026-04-28]]
- [[news/2026-04-30]]
- [[news/2026-05-02]]
- [[news/2026-05-03]]
- [[news/2026-05-05]]
- [[news/2026-05-11]]
- [[news/2026-05-17]]
- [[news/2026-07-19]]
