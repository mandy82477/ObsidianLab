---
page: "entities/opus-5"
kind: "entity"
type: "model"
status: "active（現行次旗艦；前代 Opus 4.8 已列 Legacy）"
domain: "🤖 模型"
last_updated: "2026-09-08"
last_news_update: "2026-09-03"
status_main: "active"
days_since_news: 8
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 8
inbound_links: 38
attribution_count: 24
attribution_last: "2026-08-28"
top_source: "reddit"
pending_count: 2
pending_overdue: 1
pending_next_review: "2026-09-12"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Opus 5

**類型：** model
**狀態：** active（現行次旗艦；前代 Opus 4.8 已列 Legacy）
**領域：** 🤖 模型
**首次出現：** 2026-07-25
**最後更新：** 2026-09-08
**最後新聞更新：** 2026-09-03

> **最新動態**（2026-09-03）
> Opus 5 連同其他世代模型出現錯誤率升高，官方當日 13:41 UTC 鎖定原因、同日 16:16 UTC 標記已解決（2026-09-07 查證，status.claude.com）；屬平台穩定性事件，非能力或定價變化。

---

## 現況

Opus 5 是**現行的次旗艦**：官方 2026-07-24 發布（本站 07-25 收錄，兩個日期都會看到），取代 [[entities/opus-4-8|Opus 4.8]]。兩代同價，Opus 5 的知識截止晚四個月。它在 Max、Team premium、Enterprise 隨用隨付與 API 上是預設的 Opus，但 Claude Code 的整體預設仍是 Sonnet。

自 2026-07-24 上線以來（截至 2026-09-07），社群累積的絕大多數是單一使用者觀感、沒有一則附測試方法或數字——例外見下方「這些數字之外」的 GitHub #77136（106 則留言、517 個反應）與 [[topics/code-quality-decline]] 已查證屬實的 GitHub #80988；官方那側公布了四個基準數字。兩邊各是什麼證據見下方「這些數字是誰量的」。牌價與方案內含見 [[entities/pricing]]，這份工作該用哪個模型見 [[topics/model-comparison]]。

---

## 你現在拿到的是什麼

> 本表比的是 Opus 這一代（4.8 vs 5）；Fable 這一代見 [[entities/fable-5]] 同名節。資料截至 2026-09-07（官方模型總覽頁、發布公告與說明中心查證）。一格一個換代時會問的問題，兩欄是兩代的答案。

| 這一格 | Opus 4.8（Legacy） | Opus 5（現行） | 官方出處（查證日） |
|---|---|---|---|
| 現在誰是預設 | 否，官方請你遷移到 Opus 5 | 是——但只是「預設的 Opus」；Claude Code 的整體預設仍是 Sonnet | 官方 What's new W30、說明中心（2026-09-07）|
| 牌價（輸入／輸出，每百萬 token）| $5 ／ $25 | $5 ／ $25（同價）| 官方模型總覽頁（2026-09-07）|
| 知識截止 | 2026-01 | 2026-05（晚四個月）| 官方模型總覽頁（2026-09-07）|
| 會不會停掉 | Legacy，退役**不早於 2027-05-28** | 退役**不早於 2027-07-24** | 官方模型總覽頁（2026-09-07）|
| 從舊代升上去會壞什麼 | —（基準世代） | 兩項：thinking 預設開啟；thinking 只有在 effort `high` 以下才關得掉 | 官方 Opus 5 模型頁（2026-09-07）|
| 官方推薦拿它做什麼 | 已不建議新採用 | 大多數工作先從 Opus 5 起手；調高 effort 仍不夠時才換 Fable 5.1 | 官方選型文件（2026-09-07）|
| 我的方案能不能用 | 同右，兩代同一套方案規則 | Max・Team premium・Enterprise 隨用隨付：預設就是它；Pro・Team standard：可用 | 官方公告與說明中心（2026-09-07）；Team standard 依 [[entities/pricing]]「同 Pro」推得 |

**表下細節**

- **兩代同價，但實付不一定同**：$5／$25 兩代相同；同一份文字換代後算出來的 token 量與 effort 設定都會改變帳單，換算見 [[topics/model-comparison]]「同一份工作，換設定差多少」。
- **effort 在 Opus 5 比前幾代更關鍵**：官方寫預設為 `high`，且它把額外 effort 轉成更好結果的可靠度高於歷代 Opus。換模型前先對自己的題目跑一次 effort 比較。
- **1M context 的方案分界**：官方在 API、Max、Team、Enterprise 列出 Opus 5 的 1M 視窗，Pro 未列；Claude Code 需 v2.1.219 以上。1M 這個旋鈕本身見 [[topics/long-context-1m]]。
- **Fast mode**：速度 2.5 倍、費率為基礎價兩倍（$10／$50），Opus 5 與 4.8 都支援，Opus 4.7 已不支援。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦（2026-09-07 判定）|
| 最適合 | 數小時、沒人盯著也要跑完的編碼任務；跨數十檔 refactor；複雜系統工程 |
| 不適合 | 日常規模開發（改 Sonnet 5）；跨多天的極長任務（改 Fable 5.1）；資安滲透測試（仍落後 Mythos 5）|

> 本表跟著 [[feature-radar]] 全覽表 Opus 5 那一列走；最新熱度以 [[feature-radar]] 為準。

---

## 這些數字是誰量的

> 資料截至 2026-09-07。上表是官方在發布公告與模型頁上自己挑出來公布的成績——CursorBench 3.2、ARC-AGI 3、OSWorld 2.0 是公開基準，但分數由 Anthropic 自行提交、未見第三方複跑；自 2026-07-24 上線以來，社群沒有交出任何一則帶測試方法或數字的獨立複測。

| 官方拿來說的基準 | 官方宣稱的結果 |
|---|---|
| Frontier-Bench v0.1 | 超越所有受測對手 |
| CursorBench 3.2 | 與 Fable 5 最佳成績差距在 0.5% 以內，每項任務成本一半 |
| ARC-AGI 3 | 為次佳者的三倍 |
| OSWorld 2.0 | 超越 Fable 5，成本為三分之一 |

**這幾個數字之外**

- **官方自陳的邊界**：資安任務上 Opus 5 仍落後 [[entities/mythos|Mythos 5]]，這一句同樣出自官方發布公告。
- **五則「變差了」型貼文**（07-30、08-07、08-13、08-20、08-28）：全是單一使用者觀感，無案例、無數字、無測試方法；其中兩則原文已不可取得。逐則見下方「歷史記錄」。
- **一則反向回饋**（08-27）：稱 Opus 5 被要求改寫時的解釋比 4.8 清楚。同樣是單一貼文。
- **一則「effort 超過 high 反而變差」**（07-29）：**已由官方文件推翻**，官方寫 Opus 5 把額外 effort 轉成更好結果的可靠度高於歷代 Opus。
- **一則跨模型的重複修辭套路**（GitHub #77136，106 則留言、517 個反應，08-27）：4.7、4.8、5 與 Fable 同時出現，不是 Opus 5 獨有；追蹤見 [[entities/claude-code]]。
- **一則第三方跨家指數**（Artificial Analysis，2026-08-10 一次性查證）：當時 Opus 5 在綜合指數微幅領先 Fable 5，數字與當時的比較見下方 07-26 那一則；**現在的跨家排名以 [[topics/model-task-leaderboard]] 為準**，本頁不留跨家分數。

**所以呢**：官方那四個數字全部由 Anthropic 自己提交、沒有人複跑過；社群到今天也沒有一則量化實測能印證或推翻它。要別人量過的跨家排名去 [[topics/model-task-leaderboard]]；要決定這份工作用哪個模型去 [[topics/model-comparison]]；「有沒有系統性退步」這條線的狀態去 [[topics/code-quality-decline]]。

---

## 核心功能

- **兩個 breaking change（從 Opus 4.8 升上來）**：thinking 預設開啟；thinking 只有在 effort `high` 以下才關得掉
- **effort 比前幾代更關鍵**：預設 `high`，官方稱它把額外 effort 轉成更好結果的可靠度高於歷代 Opus
- **提示注入抵抗力**：Claude Code 創辦人 Boris Cherny 稱其為當時最難被攻破的模型（單一具名表態、無第三方複測，2026-07-25），見 [[entities/boris-cherny]]
- **SDK 支援**：`anthropic-sdk-python` v0.120.0、`anthropic-sdk-typescript` sdk-v0.115.0（2026-07-24 上架，早於官方公告數小時）

---

## 相關議題

- [[entities/fable-5]] — 現任旗艦；官方說法是「Opus 5 調高 effort 仍不夠時」才換過去
- [[entities/opus-4-8]] — 前代次旗艦，現為 Legacy；它現在還在當誰的 fallback
- [[entities/mythos]] — 同權重的無護欄版，資安任務上仍領先 Opus 5
- [[entities/sonnet-5]] — Claude Code 的整體預設，日常規模開發的首選
- [[entities/pricing]] — 牌價 $5／$25、我的方案內含什麼、一小時大概多少
- [[topics/model-comparison]] — 這份工作該用哪個模型、換一個實付差多少
- [[topics/model-task-leaderboard]] — 跨家排名，現在誰在前面
- [[entities/managed-agents]] — 拿 Opus 5 跑長時間任務要花多少、該用哪一種代理形態
- [[entities/claude-code]] — Claude Code 現在有什麼毛病（#77136 這類 issue 的追蹤在這）
- [[entities/boris-cherny]] — 提示注入抵抗力聲明的來源
- [[topics/ai-agent-safety]] — 未發布的「Model 2」對齊疑慮的完整脈絡
- [[feature-radar]] — 這禮拜官方動了什麼、熱度現在幾格

## 參考來源

- [Claude Opus 5 官方公告](https://www.anthropic.com/news/claude-opus-5)（2026-07-24/25）
- [Claude Opus 5 System Card](https://www.anthropic.com/claude-opus-5-system-card)
- [anthropic-sdk-python v0.120.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.120.0)
- [anthropic-sdk-typescript sdk-v0.115.0](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.115.0)
- [MLQ.ai：Tops AI Benchmark Index at Half the Cost of Fable 5](https://mlq.ai/news/anthropic-launches-claude-opus-5-tops-ai-benchmark-index-at-half-the-cost-of-fable-5/)（2026-07-26）
- [PCMag：Tops Fable 5 on Agentic Search](https://www.pcmag.com/news/anthropics-newest-ai-model-opus-5-is-now-available)（2026-07-26）
- [EdTech Innovation Hub：Anthropic releases Claude Opus 5 at same price as Opus 4.8](https://news.google.com/rss/articles/CBMinwFBVV95cUxOUExpODBocm5KMzF1WjlIREJrZEFFWG9KZVVqQVpZeVhBQndwbm9xZ19VQm5CODNfc2xvd0hfd18weDNON2pKV3JWOGQ0bEd5X2VMMzdqaXlfTzZnX1FSa3NERWxNa0ctWkx4YVctMGZKUDlkVUFrU0hMUjVDU1VKb0lkazlrckZXUFB6OVpOWGxYOVpqODJqY25qZlZYNDA?oc=5)（2026-07-26）
- [Reddit r/artificial：Opus 5's effort dial is not monotonic above "high"](https://www.reddit.com/r/artificial/comments/1v60pga/opus_5s_effort_dial_is_not_monotonic_above_high/)（週熱門，2026-07-25）
- [官方 migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)（查核日 2026-07-29）
- [Reddit：Opus 5 is not as good as i thought](https://www.reddit.com/r/ClaudeCode/comments/1var15k/opus_5_is_not_as_good_as_i_thought/)（2026-07-30，無週熱門標記，score 不可信）
- [Reddit：I defended Opus 5 - and then I realised otherwise](https://www.reddit.com/r/ClaudeAI/comments/1vibkny/i_defended_opus_5_and_then_i_realised_otherwise/)（週熱門，2026-08-07）
- [Reddit：Finally. Could this be the smoking gun that makes Opus less load-bearing?](https://www.reddit.com/r/ClaudeCode/comments/1vt6gf8/finally_could_this_be_the_smoking_gun_that_makes/)（週熱門，2026-08-20，僅標題可用）
- [[news/2026-07-25]]、[[news/2026-07-26]]、[[news/2026-07-28]]、[[news/2026-07-29]]、[[news/2026-07-30]]、[[news/2026-08-07]]、[[news/2026-08-15]]、[[news/2026-08-23]]
- [Google News/tech-insider.org：Claude Opus 5 vs Grok 4.6 vs Gemini 3.1 Pro: $19 Gap](https://news.google.com/rss/articles/CBMigwFBVV95cUxNWkVkQU8xS2pPWVFZS2RMemJCQ0JFVnZyZFBia28xMlNlWWNPVFB2eHhxdVhBTWJJRFFmaDlOUU9IcGJUWDlBU0phQUhUUEFGRG51NkttME9tMTl0X1dsV2piR2lsQTZOeURZQV8yRExlTE93cFF2U1hYbUFTZGNRUTIxcw?oc=5)（2026-08-26，僅標題可用）
- [GitHub Issue #77136：repetitive rhetorical tics across Claude 4.7/4.8/5.0/Fable](https://github.com/anthropics/claude-code/issues/77136)（2026-08-27）
- [Reddit：Unpopular opinion: Opus 5 language just became better in communication](https://www.reddit.com/r/ClaudeAI/comments/1vzvcc4/unpopular_opinion_opus_5_language_just_became/)（2026-08-27）
- [Reddit：Is it even legal for Anthropic to nerf its models this hard?](https://www.reddit.com/r/ClaudeCode/comments/1w0t53b/is_it_even_legal_for_anthropic_to_nerf_its_models/)（2026-08-28）
- [Reddit：A comparison of Opus 5, 4.7, and 4.6 running a code review](https://www.reddit.com/r/ClaudeCode/comments/1w0uyu7/a_comparison_of_opus_5_47_46_running_a_code/)（2026-08-28）
- [[news/2026-08-28]]

## 歷史記錄

> 表格是索引，每一則的完整說明與來源在下方。❓ ⟨Q-01⟩ 這類記號代表「這一則我們還沒查到答案」，完整說明同樣在下方。

| 日期 | 事件 |
|------|------|
| 2026-09-03 | Anthropic 狀態頁：多款模型錯誤率升高，同日 16:16 UTC 已解決（2026-09-07 查證）|
| 2026-08-28 | Reddit 質疑「Anthropic 是否削弱模型」；另有三模型 code review 比較 ❓待查證⟨Q-01⟩ |
| 2026-08-27 | GitHub Issue #77136：跨模型代際重複修辭套路；同日另有回饋稱表達方式較 4.8 改善 |
| 2026-08-26 | tech-insider.org 定價比較標題「$19 Gap」，計算基準 ❓待查證⟨Q-02⟩ |
| 2026-08-14 | Anthropic 八月風險報告揭露未發布「Model 2」，官方稱無釋出計畫（見 [[topics/ai-agent-safety]]） |
| 2026-08-11 | SitePoint 開發者效能評測——**2026-09-07 查證：內文的 context、牌價、發布年皆與官方不符，不採信** |
| 2026-08-08 | Reddit「PSA」提醒 WebFetch 研究可能捏造統計數字與引述，單一使用者回報 |
| 2026-07-30・08-07・08-13・08-20 | 社群觀感分歧四則：皆單一貼文、無量化；08-20 與 07-30 原文已不可取得，2026-09-07 放棄追查 |
| 2026-07-29 | Reddit 稱 effort 旋鈕「非單調」——**2026-08-08 官方文件證偽**，說法不成立 |
| 2026-07-26 | MLQ.ai／PCMag「tops」標題——**2026-08-10 第三方基準查證屬實**；定價「同價」與「減半」兩說法經查證皆成立 |
| 2026-07-25 | 正式發布（官方日期 07-24），取代 Opus 4.8；HN 1587 分 |
| 2026-07-24 | Reddit 週熱門稱長時間任務表現最佳、low effort 成本效益高，無量化數字佐證 |

**歷史記錄細節**

- **2026-09-03**：Opus 5／4.8／4.6 與 Fable、Mythos 全系列同時錯誤率升高。官方 13:41 UTC 鎖定原因，**同日 16:16 UTC 標記已解決**（2026-09-07 查證）。屬穩定性事件，非能力或定價變化；跨模型完整記錄見 [[entities/fable-5]]（[Anthropic Status](https://status.claude.com/incidents/461yvfrzpwtt)；[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1w69016/claude_code_server_down_for_a_long_time_now_will/)，2026-09-03）

- **2026-08-28**：Reddit r/ClaudeCode 質疑串「Is it even legal for Anthropic to nerf its models this hard?」，使用者抱怨 Opus 5 與 Fable 5 在 Claude Code 中的實際表現遜於預期，質疑模型遭「削弱」；單一使用者觀感回報，無量化數字佐證，延續 08-13、08-20 已記錄的社群觀感分歧模式（[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1w0t53b/is_it_even_legal_for_anthropic_to_nerf_its_models/)，2026-08-28）
  - 同日另有 Reddit 貼文比較 Opus 5、4.7、4.6 在同一份 code review 提示下的表現，情緒中性，僅標題可用；⟨Q-01⟩ ❓ **待查證**（標 2026-08-29｜查 1w0uyu7、code review｜複 2026-09-12）｜**三模型 code review 比較結果具體內容與數字**：RSS 摘要僅標題可用，未見測試方法或分數揭露（[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1w0uyu7/a_comparison_of_opus_5_47_46_running_a_code/)，2026-08-28）
- **2026-08-27**：GitHub Issue #77136 回報 Opus 5（連同 Opus 4.7、4.8、Fable 5）日益預設重複修辭套路、難維持連貫散文，即使給明確風格指示仍難改善；106 則留言、517 個反應，尚無官方回應。同日 Reddit「不受歡迎的意見」貼文稱 Opus 5 表達方式較 4.8 有改善（要求改寫時解釋更清楚），與前述問題並非直接矛盾，並陳記錄（[GitHub Issue #77136](https://github.com/anthropics/claude-code/issues/77136)；[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vzvcc4/unpopular_opinion_opus_5_language_just_became/)，2026-08-27）
- **2026-08-26**：tech-insider.org（經 Google News 轉載）發布模板化定價比較標題《Claude Opus 5 vs Grok 4.6 vs Gemini 3.1 Pro: $19 Gap [2026]》，比較 Opus 5 與競品 Grok 4.6、Gemini 3.1 Pro 定價；同站同日另有《Claude Fable 5 vs Opus 5 vs GPT-5.6 Sol: $1,125 Gap [2026]》，記於 [[entities/fable-5]]。本則僅標題可用、無正文，「$19 Gap」具體數字未經查證，不採信為事實；如經查證應留給 [[entities/pricing]] 記錄。⟨Q-02⟩ ❓ **待查證**（標 2026-08-26｜查 tech-insider.org、$19 Gap｜複 2026-09-09）｜**Opus 5 vs Grok 4.6 vs Gemini 3.1 Pro 的 $19 差距計算基準**：僅標題可用，未見正文說明計算方式（per-token／月費等）（[Google News/tech-insider.org](https://news.google.com/rss/articles/CBMigwFBVV95cUxNWkVkQU8xS2pPWVFZS2RMemJCQ0JFVnZyZFBia28xMlNlWWNPVFB2eHhxdVhBTWJJRFFmaDlOUU9IcGJUWDlBU0phQUhUUEFGRG51NkttME9tMTl0X1dsV2piR2lsQTZOeURZQV8yRExlTE93cFF2U1hYbUFTZGNRUTIxcw?oc=5)，2026-08-26）
- **2026-08-20**：Reddit r/ClaudeCode 週熱門標題稱「終於出現讓 Opus 不再是工作流『必要依賴』的證據」；原文只有圖片預覽卡片，2026-08-23 與 2026-09-07 兩次都取不到正文，本站放棄追查（[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1vt6gf8/finally_could_this_be_the_smoking_gun_that_makes/)，週熱門，2026-08-20）
  - 同日社群另有一則熱議是 Claude Code 的 effort 數值顯示方式測試，官方澄清為服務端設定改變了數值顯示、非調低使用者選的 effort 等級——兩件事不同，不應混為一談。
- **2026-08-14**：Anthropic 發布八月風險報告（部分遮蔽 PDF），首度揭露尚未發布的「Model 2」，Axios 報導官方稱目前無釋出更強模型的計畫；報告自陳內部 AI R&D 速度尚未達到「無 AI 協助情況下的兩倍」（自陳量測困難）。對齊疑慮面完整脈絡見 [[topics/ai-agent-safety]]，本頁僅記模型陣容面（[Hacker News](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf)，55 分；[SiliconANGLE](https://siliconangle.com/2026/08/14/anthropic-details-unreleased-model-2-new-alignment-concerns-latest-ai-risk-report/)；[Axios](https://www.axios.com/2026/08/14/anthropic-model-2-ai-risk)，2026-08-14）
- **2026-08-13**：Reddit r/ClaudeAI 週熱門貼文「Opus 5 is actually almost rage-inducing to use」：作者稱已依官方建議調整並試過各種全域 CLAUDE.md 設定，仍無法讓 Opus 5 的行為符合期待；單一使用者回報，無具體案例或量化數字佐證，延續 08-07～08-08 已記錄的社群觀感分歧（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vn8ml6/opus_5_is_actually_almost_rageinducing_to_use/)，週熱門，2026-08-13）
- **2026-08-11**：SitePoint 刊出針對開發者的 Claude Opus 5 效能評測整理。**2026-09-07 查證：該文寫的 context 上限、每百萬 token 牌價與發布年份三項皆與官方不符，本站不採信其數據**（Google News／SitePoint，2026-08-11）
- **2026-08-08**：Reddit r/ClaudeAI 週熱門貼文「PSA: Be careful letting Claude use WebFetch for research」：作者請 Opus 5 研究 AI agent 記憶架構時，發現其以 WebFetch 生成看似真實、實則捏造的具體統計數字、百分比與引述，提醒他人使用 WebFetch 做研究時需小心查核；單一使用者回報、無具體案例引文或跨來源佐證，列為待社群驗證的可靠性觀察，非量化評測結論（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vim8b7/psa_be_careful_letting_claude_use_webfetch_for/)，週熱門，2026-08-08）
- **2026-08-07**：Reddit r/ClaudeAI 週熱門貼文「I defended Opus 5 - and then I realised otherwise」稱作者原本認為 Opus 5 是目前最「奇特獨特」的模型、稱讚其思考過程（reasoning trace）而非單純能力，深入分析其思考過程後改變了看法；原文於「actually reading through and analysing it's thought process I find fascinati...」處截斷，具體轉折方向（趨向更正面或更負面）不可考。與 07-29～08-04 已記錄的「過度自信」「不如跑分預期」「令人挫折」負向回饋屬同一波「上線兩週後社群重新評估」現象，惟本則聚焦 reasoning trace 角度且結論方向不明，暫列觀察、不代入評測結論（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vibkny/i_defended_opus_5_and_then_i_realised_otherwise/)，週熱門，2026-08-07）
- **2026-07-30**：Reddit r/ClaudeCode 貼文稱作者原先看跑分認為 Opus 5 優於 Fable 5，實際使用後覺得仍有落差，並提到遇上「minor」問題；該貼文無週熱門標記、分數不可信（[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1var15k/opus_5_is_not_as_good_as_i_thought/)，2026-07-30）
  - 原文在「minor」處截斷，2026-08-10 與 2026-09-07 兩次都取不到後續內容，具體所指與落差幅度本站放棄追查；本則不代入任何評測結論。
- **2026-07-29**：Reddit r/artificial 週熱門貼文稱 Opus 5 的 effort 旋鈕「非單調」——超過 `high` 後（`xhigh`／`max`）程式碼任務分數反而下降，並稱官方 migration guide 本身即有此說明；**2026-08-08 查證官方文件後判定此說法不成立**——[What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) 明載「Claude Opus 5 converts additional effort into better results more reliably than any earlier Opus model」，並將 test-time compute scaling（效果隨 effort 提升直到 `max`）列為主要能力改進；官方對 `xhigh`／`max` 的唯一告誡是「須設較大 `max_tokens`」，以及 `thinking: disabled` 在 `xhigh`／`max` 會回 400。未見任何「高於 high 即單調下降」文字，社群措辭比官方原文更強烈——核心說法已證偽，無下降幅度可言，完整比對見 [[topics/model-comparison]]
- **2026-07-26**：MLQ.ai／PCMag 媒體標題分別稱 Opus 5「Tops AI Benchmark Index」「Tops Fable 5 on Agentic Search」——**2026-08-10 第三方基準查證屬實**：Artificial Analysis Intelligence Index Opus 5 60.7% vs Fable 5 59.9%，GDPval-AA v2／AA-Briefcase 亦領先；EdTech Innovation Hub 報導稱 Opus 5 與 Opus 4.8 同價發布，與 MarkTechPost「維持原定價」方向一致——**2026-08-08 官方查證確認兩說皆成立**：$5/$25 per Mtok，官方逐字載明「unchanged from Claude Opus 4.8」，同時也確為 Fable 5（$10/$50）的一半，兩種描述指的是同一組數字的不同對照對象（見 [[entities/pricing]]）；Reddit r/ClaudeAI 週熱門貼文提及第三方 benchmark 平台 MineBench.ai 有 Fable 5 vs Opus 5 差異討論——**2026-08-08 查證後不可採信**：MineBench 測的是 3D voxel 空間推理（與編碼／agentic 能力無關），榜上查無 Fable 5 或 Opus 5 條目
- **2026-07-25**：正式發布，取代 Opus 4.8 成為 Claude Max 新預設模型、Claude Pro 最強模型；HN score 1587；SDK（Python/TypeScript）同步加入模型支援；Boris Cherny 稱其為最難被提示注入攻破的模型
- **2026-07-24**：Reddit r/ClaudeAI 週熱門貼文稱 Opus 5 於長時間任務（long-horizon task）表現最佳、Low effort 設定下成本效益極高，屬單一社群主觀評價，無量化數字佐證
