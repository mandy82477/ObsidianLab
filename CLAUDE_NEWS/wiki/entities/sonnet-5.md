---
page: "entities/sonnet-5"
kind: "entity"
type: "model"
status: "active（正式發布）"
domain: "🤖 模型"
last_updated: "2026-09-02"
last_news_update: "2026-07-31"
status_main: "active"
days_since_news: 36
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 36
inbound_links: 9
attribution_count: 3
attribution_last: "2026-07-31"
top_source: "google-news"
pending_count: 2
pending_overdue: 1
pending_next_review: "2026-11-26"
pending_signalled: 0
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Sonnet 5

**類型：** model
**狀態：** active（正式發布）
**領域：** 🤖 模型
**首次出現：** 2026-07-01
**最後更新：** 2026-09-02
**最後新聞更新：** 2026-07-31

> **最新動態**（2026-07-31）
> Anthropic Status 通報 Claude Sonnet 5 效能降級（degraded performance），06:18 UTC 起偵測、07:04 UTC 確認事件已解決，歷時約 46 分鐘，無需採取行動。Reddit r/ClaudeAI 出現對應事件 Megathread，內容與官方一致，屬社群對同一事件的跟進，非獨立事件。定價與 Opus 5 發布後的定位變化未受影響，詳見下方「現況」。

---

## 現況

**2026-07-31 最新**：Anthropic Status 通報 Sonnet 5 效能降級，06:18 UTC 起偵測、07:04 UTC 確認已解決，歷時約 46 分鐘；Reddit r/ClaudeAI 出現對應事件 Megathread（0 留言，可能因剛發布尚未累積），內容與官方一致，屬社群對同一事件的跟進，非獨立事件。事件不影響模型能力或定價，屬穩定性範疇。

**2026-07-25**：dev.to 分析文章重申 Sonnet 5 促銷定價的 60% 折扣「real but temporary」，未提供新數字（[[entities/pricing]] 有完整定價細節）；同日 [[entities/opus-5|Claude Opus 5]] 正式發布，Sonnet 5 本身定位不受影響。

Claude Sonnet 5 於 2026-07-01 正式發布，定位為 Anthropic **最 agentic 的 Sonnet 模型**，在 reasoning、tool use、coding、knowledge work 等多個面向均有顯著提升，效能接近 Opus 4.8。

**與 [[entities/fable-5]] 的定位差異**：Fable 5（2026-09-01 起為 5.1）是最高階旗艦（Mythos 級推理能力，適合最複雜的多步驟任務）；Sonnet 5 則是主力平衡選項——以約 60% 的成本換取接近 Opus 4.8 的效能，適合日常 agentic 工作流與成本敏感場景，非追求極致推理深度的定位。

**Claude Code 預設模型**：Claude Code v2.1.197 起已將 Sonnet 5 設為預設模型，取代前一代 Sonnet 版本。

**定價**：$2/$10 per Mtok（input/output）。發布時為入門促銷價、載明 2026-08-31 到期，**已於 2026-08-10 官方永久化為標準價**，原訂 9/1 調至 $3/$15 的計畫取消（官方模型總覽頁 2026-08-26 查證：定價欄已無任何到期字樣）。社群稱此定價較 Opus 4.8 省約 60% 成本，形成「cost reset for AI agents」的討論；Opus 4.8 本身 API 定價未見官方逐項公布數字，完整定價彙整見 [[entities/pricing]]。

**1M context window**：原生支援 100 萬 token 上下文，與 Fable 5 / Opus 4.8 相同。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ✅ 廣泛推薦 |
| 最適合 | agentic 工作流、Claude Code 日常使用、tool use 密集任務、成本敏感場景 |
| 不適合 | 需要 Mythos 級推理深度的極複雜長期任務（此時考慮 Opus 4.8） |

> 詳細最新熱度見 [[feature-radar]]

## 使用指南

**快速上手（Claude Code）：**
```
# Claude Code v2.1.197 已預設使用 Sonnet 5，無需指定
claude

# 明確指定：
claude --model claude-sonnet-5-20260701
```

**注意事項：**
- $2/$10 per Mtok 為標準價，無到期日（2026-08-10 永久化；原載 2026-08-31 到期）
- 效能接近 Opus 4.8，但 60% 成本差距使其在 agentic 工作流中具備明顯性價比優勢
- 1M context 原生支援，適合整個 codebase 的大型 agentic 任務

## 核心能力

- **Agentic 定位**：reasoning、tool use、coding、knowledge work 全面提升，是 Anthropic 目前最強 agentic Sonnet
- **效能 vs Opus 4.8**：社群多篇評測確認在 agentic 任務上效能接近 Opus 4.8，60% 成本差距
- **1M token context**：原生支援，無需外部管理
- **Claude Code 預設**：v2.1.197 起為 Claude Code 預設模型

❓ **待查證**（標 2026-08-10｜查 Terminal-Bench、leaderboard）｜**Sonnet 5 Terminal-Bench 排名未確認**：社群評測提及 Sonnet 5 在 Terminal-Bench 2.1（2026-06）leaderboard 有排名，且「#1 仍為外界無法取用的型號」，但缺乏具體名次數字與來源連結，暫不列為已確認核心能力。

## 爭議

- **官方 BrowseComp 對比圖表換版（爭議已落地，2026-08-26 查證）**：Anthropic 於 **2026-06-30 以 changelog 更正**替換了 Sonnet 5 的 BrowseComp 成本效能圖——原圖未套用其標準 agentic-search 方法論，新圖改用 Sonnet 5 system card 設定（10M token 預算、compaction、programmatic tool calling），成本軸上限也從約 $10 拉到 $50。官方定調為**方法論更正**，非挑選有利數據；批評方（[vincentschmalbach.com](https://www.vincentschmalbach.com/anthropic-changed-sonnet-5-chart-after-it-made-sonnet-look-bad/)，HN score 3）認為敘事從「Sonnet 落後 Opus」變成「花得夠多就有用」。**該文未提供修改前後圖表的存檔對照**，換版事實與官方理由則有 changelog 可稽；讀者可自行判斷方法論更正是否合理，本頁不代為裁定
- ⚠️ **個性/語氣不如 Sonnet 4.6（主觀回饋）**：Reddit 多位使用者反映 Sonnet 5 智力提升但互動個性流失——Sonnet 4.6 原本較有個性、懂得對話節奏、簡短回應精準，Sonnet 5 感覺更像通用「help」助手而非有特色的對話夥伴（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ulf5xc/something_important_was_lost_between_sonnet_46/)）；屬主觀體驗回饋，非量化評測，與 Fable 5「失去靈魂」討論（見 [[entities/fable-5]] 爭議區）呈現類似的世代模型「個性 vs 能力」取捨模式（推論）
- ⚠️ **回應內容重複（弱訊號，2026-07-09）**：Reddit r/ClaudeCode 使用者詢問是否也遇到 Sonnet 5 回應內容重複的情形；貼文無 score（Reddit RSS 恆 0，非跨平台佐證），暫僅列為待觀察訊號，不構成已驗證問題

## 相關議題

- [[entities/fable-5]] — 現任最高階公開模型；Sonnet 5 為次階平衡選項，定位差異見上方「現況」
- [[entities/opus-4-8]] — Opus 4.8 能力對比（Sonnet 5 效能接近 Opus 4.8，Opus 4.8 已於 2026-07-25 被 [[entities/opus-5|Opus 5]] 取代次旗艦地位）
- [[entities/opus-5]] — 2026-07-25 發布的新次旗艦，與 Sonnet 5 分屬不同定位（次旗艦 vs 主力平衡選項）
- [[entities/pricing]] — 完整定價與促銷方案細節
- [[entities/claude-code]] — Claude Code v2.1.197 更新

## 參考來源

- [Anthropic Blog：Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)（2026-07-01）
- [[news/2026-07-01]]

## 歷史記錄

### 2026-07-31
**Degraded performance 事件（同日解決，約 46 分鐘）**：Anthropic Status 通報 Claude Sonnet 5 效能降級，2026-07-31 06:18 UTC 起偵測，07:04 UTC 確認事件已解決，無需採取行動（[Anthropic Status](https://status.claude.com/)）。Reddit r/ClaudeAI 同步出現對應 Megathread「Megathread for New Claude Incident: Degraded performance on Claude Sonnet 5 on Jul 31, 2026」，互動 0 留言（可能因剛發布尚未累積），內容與官方 Status 一致，屬社群對同一事件的跟進討論，非獨立事件。屬穩定性事件，非能力或定價變化，與本頁 07-07、07-08 已記錄的同類型錯誤率事件屬同一模式。

### 2026-07-25
**dev.to 重申促銷折扣「real but temporary」+ Opus 5 同日發布**：dev.to 作者 tokenmixai 於〈I Did the Math on Claude Sonnet 5. The 60% Opus Discount Is Real, But Temporary.〉一文中指出，Anthropic 已將 Sonnet 5 以促銷定價廣泛開放至 2026-08-31，與既有 $2/$10 per Mtok 資訊一致，未提供新的定價數字（定價細節見 [[entities/pricing]]）。同日 Anthropic 正式發布 [[entities/opus-5|Claude Opus 5]]，取代 Opus 4.8 成為次旗艦；Sonnet 5 本身的 Claude Code 預設模型定位不受影響。

### 2026-07-14
**MarkTechPost 三模型深度比較（Sonnet 5 vs Sonnet 4.6 vs Opus 4.8）**：MarkTechPost 發布文章〈Anthropic Claude Sonnet 5 vs Sonnet 4.6 vs Opus 4.8: Agentic Coding Benchmarks, API Pricing, and Cost-Performance Tradeoffs Compared〉，涵蓋三模型的 agentic coding 基準測試、API 定價與成本效益取捨分析；本則日報摘要僅提供標題級資訊，未附具體評測數字，暫列為外部延伸閱讀資源，待後續補充量化內容時再擴寫（Google News／MarkTechPost，2026-07-14）。完整選型對照見 [[topics/model-comparison]]。

### 2026-07-09
**媒體「正式發布」報導 + 評測分數/定價初步數字**（2026-08-26 查證，部分結案）：Mashable 於 07-09 03:41 UTC 報導 Anthropic「finally, officially launches Claude Sonnet 5」，與既有 07-01 官方發布日重疊；tech-insider.org 同日另發文宣稱評測分數達 57 分、API 成本較前代減半（"Claude Sonnet 5 Debuts: 57 Score, Half the API Cost"，13:10 UTC）。查證結果：

- **「正式發布」非新事件**：官方發布公告為 2026-06-30 美西／本庫採計之 07-01（[Anthropic Blog](https://www.anthropic.com/news/claude-sonnet-5)、TechCrunch 同日），Mashable 07-09 一文屬遲到報導，**不構成第二次發布**
- **「API 成本減半」屬實**：$2/$10 per Mtok 對前代 Sonnet 4.6 的 $3/$15 為降價，對 Opus 4.8 的 $5/$25 更省約 60%；該價已於 2026-08-10 永久化（見 [[entities/pricing]]）
- 🔎 **查無官方**（標 2026-08-26｜查 tech-insider.org、57 Score｜複 2026-11-26）｜**「57 分」的 benchmark 名稱**：官方模型頁與發布公告均未見此數字，原文亦未指明測的是哪個 benchmark，**不採信為評測事實**；tech-insider.org 為模板化標題農場型來源（同站另有多篇 "X vs Y: $N Gap" 系列，見 [[entities/fable-5]]），本庫不以其數字入表

此外 Reddit r/ClaudeCode 出現「回應內容重複」的弱訊號回報（score 恆 0，見「爭議」區）。

### 2026-07-08
**錯誤率再度升高（同日解決）**：Anthropic Status 通報 Sonnet 5 錯誤率一度升高，於 06:40 UTC 解決，無需採取行動（[Anthropic Status](https://status.claude.com/incidents/n3v83qmtlbqm)）；另有 07-07 23:46 UTC 一起「部分模型請求錯誤率升高」事件同日解決。屬穩定性事件，非能力或定價變化。

### 2026-07-02
**發布次日爭議：圖表可信度質疑 + 個性流失回饋**：
- **官方圖表換版爭議**：HN 文章指 Anthropic 換掉讓 Sonnet 5 表現不佳的官方對比圖（[vincentschmalbach.com](https://www.vincentschmalbach.com/anthropic-changed-sonnet-5-chart-after-it-made-sonnet-look-bad/)，HN score 3）；2026-08-26 查證確認換版屬實，官方 06-30 changelog 說明為 BrowseComp 方法論更正，細節見上方 [[#爭議]]
- **個性流失回饋**：Reddit 多位使用者反映 Sonnet 5 相較 Sonnet 4.6 智力提升但互動個性/語氣弱化，感覺更通用化（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1ulf5xc/something_important_was_lost_between_sonnet_46/)），屬主觀體驗，非量化評測

### 2026-07-01
**正式發布**：Claude Sonnet 5 正式上線，定位最 agentic Sonnet。效能接近 Opus 4.8，促銷定價 $2/$10 per Mtok 至 2026-08-31（該到期日後於 08-10 取消）。Claude Code v2.1.197 設為預設模型。Terminal-Bench 2.1（2026-06）有明確排名；社群稱「cost reset for AI agents」（多篇社群評測，待具體 benchmark 連結補充）。

### 2026-07-07
**錯誤率一度升高（同日解決）**：Anthropic Status 通報 Claude Sonnet 5 錯誤率升高（Elevated errors），事件於 07:37 UTC 解決，無需採取行動（[Anthropic Status](https://status.claude.com/incidents/hh9hj15mxkrx)）。屬穩定性事件，非能力或定價變化。
