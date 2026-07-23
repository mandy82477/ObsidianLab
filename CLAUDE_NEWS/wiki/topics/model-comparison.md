# Claude 模型選型對照

**狀態：** ongoing
**領域：** 🤖 模型
**開始日期：** 2026-07-02
**最後更新：** 2026-07-23
**最後新聞更新：** 2026-07-23

> **最新對照更新**（2026-07-20）
> GitHub Issue #79337（10 讚、35 留言）回報，Fable 5 免費期到期後的 07-20 當天，Max 方案一度被要求額外購買 usage credits 才能執行 Fable 5、並靜默降級至 Opus 4.8；症狀與同日 Anthropic Status 已證實的 Max 誤判事件吻合，官方已確認為誤判並建議重啟。Max/Team 方案存取政策本身（「轉為永久標配」vs「轉為計量存取」）仍有分歧報導，詳見 [[entities/pricing]]。公開陣容五級維持不變：Fable 5（旗艦）> Opus 4.8 > Sonnet 5（主力）> Sonnet 4.6 > Haiku 4.5。

---

## 摘要

**目前公開陣容五級維持不變（Fable 5 > Opus 4.8 > Sonnet 5 > Sonnet 4.6 > Haiku 4.5），07-08 官方公布的多模型協作基準是最新橫向比較資訊。** 本頁回答一個問題：**「我該用哪個 Claude 模型？」** 各模型的深度資訊（爭議、時序、已知問題）在各自的 entities 頁；本頁只做橫向對照與情境推薦，模型陣容變化時同步更新。

## 快速選型表

| 模型 | 定位 | 定價（in/out per Mtok）| Context | 最適合 | 不適合 | 狀態 |
|------|------|------|------|------|------|------|
| [[entities/fable-5\|Fable 5]] | 旗艦（Mythos 級公開版） | $10 / $50 | 1M | 多步驟複雜任務、長期 agentic 工作流、安全漏洞分析 | 日常短問答（太貴）；前沿 LLM 開發（護欄靜默降級） | ✅ 已解禁（免費期已於 **7/19 到期**；07-20 一度出現 Max 方案誤判需購買 credits 的 bug，官方已證實並建議重啟；Max/Team 後續存取政策（永久標配／計量存取）仍分歧，詳見 [[entities/pricing]]） |
| [[entities/opus-4-8\|Opus 4.8]] | 次旗艦 | ~$5 / $25（估計） | 1M | 大型 agentic 任務、1M context 長文件、Fast Mode 省時場景 | 追求穩定性的生產環境（曾有行為退步回報） | ✅ Active |
| [[entities/sonnet-5\|Sonnet 5]] | **主力平衡選項（Claude Code 預設）** | $2 / $10（促銷至 8/31） | 1M | agentic 工作流、Claude Code 日常、tool use 密集、成本敏感 | 需要 Mythos 級推理深度的極複雜任務 | ✅ Active（v2.1.197 預設） |
| Sonnet 4.6 | 前代主力 | 低於 Sonnet 5 正式價 | 200K | 已驗證穩定的既有工作流；偏好其互動個性者 | 新專案（Sonnet 5 促銷期 CP 值更高） | ✅ Active |
| Haiku 4.5 | 輕量 worker | 最低 | 200K | 混合架構低成本 subagent、批量簡單任務 | 複雜推理、長鏈 agentic 任務 | ✅ Active |
| [[entities/opus-4-7\|Opus 4.7]] | 已被取代（第三階） | 同 4.8 | 200K | agentic coding 仍有口碑 | 新採用（已有兩代後繼） | ⚠️ 已被取代 |
| [[entities/mythos\|Mythos 5]] | 無護欄完整版 | — | — | 授權機構的安全研究 | 一般開發用途（非此定位） | ✅ 已解禁（僅限授權機構/安全研究用途，非一般消費市場） |

## 情境推薦

| 你的情境 | 建議 | 理由 |
|---------|------|------|
| Claude Code 日常開發 | **Sonnet 5**（預設即是） | 效能接近 Opus 4.8、成本約 60%，1M context |
| 跨多天的複雜 agentic 任務 | **Fable 5** | 任務越複雜越長期優勢越明顯；免費期已於 7/19 到期，Max/Team 後續存取政策仍分歧（見 [[entities/pricing]]）；07-20 曾一度出現 Max 方案誤判需購買 credits 的 bug，官方已證實並建議重啟 |
| 資安審查 / 漏洞分析 | **Fable 5**（留意誤判） | 能力最強，但 07-02 起 Defense in Depth 分類器有誤判實測 |
| 需要壓成本的批量任務 | **Haiku 4.5 做 worker + Sonnet 5 做協調** | 社群驗證的混合架構模式 |
| 生產環境求穩 | **Sonnet 4.6 或 Sonnet 5** | Opus 4.8 曾有行為退步與 529 事件記錄 |

## Benchmark 對照（有來源者才列）

| 指標 | Fable 5 | Opus 4.8 | Sonnet 5 | 備注 |
|------|---------|----------|----------|------|
| SWE-bench Pro | SOTA（官方） | 69.2% | 接近 Opus 4.8（社群評測） | Sonnet 5 官方對比圖表有修改爭議（2026-07-02） |
| 綜合定位 | 幾乎所有 benchmark SOTA | 第三方評測曾小輸 Gemini 3.5 Flash（35.4 vs 34.8，主因指令遵循） | agentic / tool use 接近次旗艦 | 各數據測試日期與條件見各模型頁 |
| token 消耗／每任務成本 | 917 個 coding-agent 場景中以 0.9 分之差略勝 Opus 4.8，但 token 消耗約 2 倍（Reddit r/ClaudeAI，2026-06-12） | 基準對照組 | — | 「小勝」需連成本一起讀：分差小、代價大 |
| 多模型協作成本效益（orchestrator 模式）| Fable 5 調度 + 便宜模型執行：**46% 成本達 96% 效能**（官方基準，Reddit r/ClaudeAI 整理轉載，週熱門標記，來源貼文 2026-07-08，原始官方連結未附）| — | — | 與上一列「Fable 5 單獨執行 token 消耗約 2 倍」形成對照：協作模式可望大幅壓低整體成本，惟原始 benchmark 頁面尚未直接查證 |

> 數據截至 2026-07-09；詳細評測條件與矛盾結果並陳原則見各模型 entities 頁。
>
> **延伸閱讀（待補充量化數字）**：MarkTechPost（2026-07-14）發布 Sonnet 5 / Sonnet 4.6 / Opus 4.8 三模型 agentic coding benchmark、API 定價、成本效益取捨的完整對照文章，惟日報摘要僅標題級資訊、未附具體評測數字，暫列為外部延伸閱讀資源，待補充查證後再納入下方表格（Google News／MarkTechPost，2026-07-14；詳見 [[entities/sonnet-5]] 歷史記錄）。

### 社群實測觀察：Fable 5 vs GPT-5.6 Sol（並陳，混合評價，訊號偏弱）

| 觀察 | 結論 | 樣本條件 | 來源與日期 |
|------|------|---------|-----------|
| 多小時實測：速度更快、bug 更少 | Fable 5 勝出（速度／穩定性） | 個人用戶多小時使用比較，非量化 benchmark；標題直述「fable clearly beats in speed and less bugs」 | Reddit r/ClaudeCode「Fable > Sol 5.6 Ultra」，2026-07-14 |
| Sol 5.6 額度重置頻率（甚至每日兩次） | Sol 5.6 在額度重置機制上具使用體驗優勢 | 同一用戶主觀比較，非量化數字 | Reddit r/ClaudeCode「Fable > Sol 5.6 Ultra」，2026-07-14 |
| 相同 iOS 卡路里追蹤 App brief 對比（影片） | 無文字結論，僅影片示範，未附文字評測摘要 | 同一需求、不同模型輸出的並排展示 | Reddit r/ClaudeCode「GPT-5.6 Sol vs Claude Fable 5 on the same iOS calorie-tracker brief」，2026-07-14 |

**小結**：GPT-5.6 Sol vs Fable 5 的社群實測持續出現，本輪均為 r/ClaudeCode 單一使用者觀點，Reddit RSS score 恆 0（非跨平台佐證），訊號強度偏弱；速度與 bug 數量的主觀評價傾向 Fable 5 勝出，但 Sol 5.6 額度重置頻率被使用者視為明顯優勢——兩者呈現「能力 vs 配額體驗」的不同勝負軸，不構成單一結論，需更多獨立來源與量化 benchmark 佐證。

### token 成本：兩個方向相反的實測結果（並陳，不選邊）

| 觀察 | 結論 | 樣本條件 | 來源與日期 |
|------|------|---------|-----------|
| 儀器化實測：新版模型 token 用量顯著更高，但**每任務總成本反而下降** | 需同時看 token 用量與任務完成率，不能只看單位成本或速度 | 工程師以 signoz.io 自建儀表板對比新舊版 Claude 模型；HN score 5（訊號偏弱，結論標「待驗證」） | [signoz.io](https://signoz.io/blog/claude-code-model-comparison/)，2026-06-29 |
| 用戶回報：**$50 額度原可用兩天，現在一小時內燒完** | 懷疑新模型（4.8）刻意提高 quota 消耗；成本暴增趨勢延燒至社群多篇貼文（費用 5x 暴增回報、企業採「穴居人模式」壓縮輸出降本）| 個人用戶主觀對照前後月份帳單，非儀器化測量；未附詳細 log | [Vincent Schmalbach 部落格](https://www.vincentschmalbach.com/claude-code-quietly-looks-5x-more-expensive/)，2026-07-01；[GitHub Issue #62476](https://github.com/anthropics/claude-code/issues/62476) |

**矛盾之處**：前者是受控測量（同任務對比新舊模型的 token 用量與完成率），後者是用戶主觀感受同一模型（Opus 4.8/Fable 5）近期的帳單變化，兩者測的不是同一件事——不構成直接互斥，但都指向「新一代模型的 token 消耗與實際成本之間的關係，社群尚無共識」。Fable 5 配額吃緊的相關社群省額度策略見 [[entities/fable-5]] 「配額與計費過渡（原訂 7/7，現已順延至 7/19）」子區塊。

## 跨模型／跨語言行為研究（官方，非選型指標）

Anthropic 研究部落格於 2026-07-15 發布〈Claude's values across models and languages〉，探討使用者向 Claude 提出**沒有普遍正確答案的問題**時（例如「該不該接受新工作」「如何處理與朋友的衝突」），Claude 在不同模型版本與不同語言之間展現的價值觀回應差異（[Anthropic Research](https://www.anthropic.com/research/claude-values-models-languages)，2026-07-15；Hacker News 累積 32 分）。

**性質說明：** 這是模型行為／對齊研究，非可用功能、也非 benchmark 分數，**不影響本頁「該用哪個模型」的選型建議**；因研究涉及跨模型、跨語言比較而非單一模型，記錄於本頁而非個別 entities 頁。原文摘要僅提供研究主題與範例問題，未附具體樣本語言清單、模型清單或量化差異數字，暫列標題級記錄，待後續報導或原始研究補充細節時再擴寫。

## 外部評測榜單

wiki 內建的模型評測數字有時效性限制（見上方各表格「數據截至」標註）。若需要更即時、涵蓋更廣的跨模型（含 GLM、Qwen、Kimi 等開源模型與 GPT-5.6 等非 Anthropic 閉源模型）評測對照，可參考：

- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/) — 涵蓋開源與閉源模型的綜合能力評測，含 FrontierSWE、Terminal-Bench 等 coding/agentic 子項
- [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — 開源模型專用評測榜單，適合追蹤 GLM / Qwen / Kimi 等開源競品

> 外部連結僅供參考，非本 wiki 收錄事實；數字本身會隨時間變動，wiki 不記錄快照分數以免過期誤導。本 wiki 聚焦 Claude/Anthropic 生態系內的評測與定位分析。

## 相關實體

- [[entities/fable-5]] · [[entities/opus-4-8]] · [[entities/sonnet-5]] · [[entities/opus-4-7]] · [[entities/mythos]]
- 功能熱度與升版建議：[[feature-radar]]
- 定價細節：[[entities/pricing]]

## 時序（陣容變化）

- 2026-07-01：Sonnet 5 發布（Claude Code 預設）；Fable 5 / Mythos 5 解禁
- 2026-06-13：Fable 5 / Mythos 5 出口管制停用（至 06-30）
- 2026-06-09：Fable 5 發布，Opus 4.8 退居次旗艦
- 2026-05-28：Opus 4.8 發布
- 2026-04-24：Opus 4.7 發布
