---
page: "topics/code-quality-decline"
kind: "topic"
status: "ongoing（2026-04 那次官方已結案；06 月起的兩條線官方未回應）"
domain: "🌐 社群"
last_updated: "2026-09-07"
last_news_update: "2026-09-03"
status_main: "ongoing"
days_since_news: 4
parent: null
children: "['topics/code-quality-decline-archive']"
page_role: "hub"
days_since_news_subtree: 4
inbound_links: 30
attribution_count: 24
attribution_last: "2026-08-28"
top_source: "reddit"
pending_count: 2
pending_overdue: 0
pending_next_review: "2026-09-08"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code 效能退步事件

**狀態：** ongoing（2026-04 那次官方已結案；06 月起的兩條線官方未回應）
**領域：** 🌐 社群
**開始日期：** 2026-03（推測）
**最後更新：** 2026-09-07
**最後新聞更新：** 2026-09-03

> **三條線，只有一條有官方說法**（2026-09-03）
> 09-03 全模型錯誤率升高、同日排除，屬服務穩定性事件不是退步。04 月那次官方認了也修了；06 月起的 token 異常與 07-25 起的 Opus 5 品質觀感，到今天都沒有官方說法。

---

## 摘要

「Claude 變笨了」在本頁拆成三條線分開看：2026-04 那次是真的，官方認了也修了；06 月下旬起的 token 消耗異常與 07-25 起的 Opus 5 品質觀感，官方到今天沒有說法。三條線沒有一條有版本前後的對照實驗，你能拿到最硬的證據是自己的 session log。

**在你量任何東西之前，先知道一件事：你釘不住你選的模型。** `--model` 只吃 family 名（opus／sonnet），不接受帶日期的版本 id，`.claude/settings.json` 也沒有鎖版設定；官方 2026-02-23 的 issue #27892 以 not planned 關閉。所以「換個模型就好」「回舊版就好」這兩個直覺，機制上都不成立——四種機制見下方「模型釘選：你選的不一定算數」。

**你的選項**：先量一次自己的用量再下結論（見「怎麼自己量一次」）；帳單變多不一定等於模型變差，週配額換軌（09-14 生效）與幾件未解的計費爭議見 [[entities/pricing]]；想等官方對 06／07 兩批給說法，本頁會記。

---

## 三條線現在到哪

> 資料截至 2026-09-07。「現在還在嗎」看的是官方說明與 GitHub issue 的開關狀態，不看討論熱度。
%% 維運備忘：上限 4 列、現有三列固定不移除、入口與退場判準見 .claude/rules/wiki-ingest-community.md「code-quality-decline 的三張表」第 1 條 %%

| 線（最後動態） | 官方說了什麼（日期） | 現在還在嗎 | 你能先做什麼 |
|---|---|---|---|
| **2026-03～04 效能退步**（2026-04-24） | 官方〈An update on recent Claude Code quality reports〉2026-04-23：三件各自獨立的工程變更，各有各的修法（見表下） | 已結案（[#41930](https://github.com/anthropics/claude-code/issues/41930) 於 2026-04-24 關閉） | 還停在 2026-04 之前的版本就先升版；三個修法各自的版本見表下 |
| **token 消耗異常**（2026-08-25） | 無官方專文 | 還在（[#65687](https://github.com/anthropics/claude-code/issues/65687) 仍開啟，最後更新 2026-08-21） | 先量一次自己的用量再判斷，見「怎麼自己量一次」；帳單面見 [[entities/pricing]] |
| **Opus 5 上線後的品質觀感**（2026-08-28） | 無官方回應 | 還在（[#77136](https://github.com/anthropics/claude-code/issues/77136) 最後更新 2026-09-03、[#83510](https://github.com/anthropics/claude-code/issues/83510) 最後更新 2026-08-28，兩則皆開啟） | 十五則裡十二則是單一使用者觀感，不足以據此換模型；逐則見 [[entities/opus-5]]「這些數字是誰量的」 |

**這張表怎麼讀**

- **04 月三個成因各自的修法**（官方 04-23 原文）：預設 reasoning effort 由 high 調為 medium（03-04 起，04-07 回復，v2.1.116）；thinking 內容每輪被清掉（03-26～04-10，v2.1.101）；system prompt 長度限制使評測掉約 3%（04-16～20，04-20 服務端回復，與版本號無關）。
- 官方原文的用語是「three separate engineering changes」。中文媒體寫成「工程疏失」，那是轉述，不是官方說的話。
- **09-03 全模型錯誤率升高**：12:43 UTC 起 Sonnet 5、Opus 5／4.8／4.6、Fable 5／5.1 與 Mythos 皆受影響，同日 16:16 UTC 排除（[Anthropic Status](https://status.claude.com/incidents/461yvfrzpwtt)）。屬服務穩定性事件，不是上表三條線之一。

## 怎麼自己量一次

沒有官方或第三方在同一組任務上做過版本前後的對照，所以「是不是真的變差了」目前只有一個可靠的答案來源：你自己的 session log。三步，每步一個動作。

1. **量什麼**：`~/.claude/projects/` 下每個專案的 JSONL session log，裡面有每次對話用了哪個模型、幾輪、多少 token。訂閱端的水位看 `Settings > Usage` 的百分比。
2. **跟什麼比**：挑同一個 repo、同一類任務的兩段 session——一段是你覺得正常的那幾週，一段是現在。不要跨 repo 比，context 規模差一個量級，結論就沒有意義。
3. **多少算異常**：社群工具 CC-Canary 直接讀上述路徑做漂移偵測，給三個判定值 `HOLDING`（穩定）／`SUSPECTED REGRESSION`（疑似退步）／`CONFIRMED REGRESSION`（確認退步），可直接拿來當自己的判斷線（工具目錄見 [[topics/community-tech-tools]]）。

**限制先說在前面**：CC-Canary 比的是你自己的歷史，不是「4.7 對 4.8」——版本前後的對照實驗至今沒有工具承接。本站唯一一則第三方連續量測是 2026-05 MarginLab 每日跑 SWE-bench-Pro，對象是 Opus 4.7、不是 Opus 5（原始記錄見 [[topics/code-quality-decline-archive#2026-05]]）。另一條路是人工存證：2026-08-12 起有開發者把 bug、退化與設定異常整理成公開檔案，附上 HackerOne 回報紀錄。

本庫沒有把 CC-Canary 列為推薦工具（社群工具目錄對這個症狀還沒有首選）——它給你的是自己跟自己比的一條線，不是外部基準。

**🧰 現在就能下的解**：先量 context 組成再怪工具（[[topics/community-large-codebase-workflow]] 線 2）；社群工具目錄的決策表目前沒有對應「感覺變笨、想先量測歸因」的列。%% —（決策表暫無對應列｜候選症狀：感覺變笨，想先量測歸因） %%

---

## Token 消耗異常訊號群（2026-06 下旬起）

**表上 10 則，從 06-27 到 08-25。** 沒有一則帶測試方法或版本前後對照；最硬的兩則是 GitHub 上帶可重現標籤、留言破百的 issue，最弱的幾則是連互動數都取不到的單一貼文。三種解釋互不排斥，見下方假說表。

| 日期 | 訊號 | 來源 | 證據硬度 |
|------|------|------|------|
| 2026-07-01 | 「Claude Code Just Got 5x More Expensive」：用戶回報原先兩天用量的 $50 配額現在一小時燒完 | Vincent Schmalbach blog（[原文](https://www.vincentschmalbach.com/claude-code-quietly-looks-5x-more-expensive/)） | `單一貼文（HN 53 分）` |
| 2026-07-01 | 獨立開發者單月燒 $62,021 token 的具名案例 | Reddit r/ClaudeAI（[原文](https://www.reddit.com/r/ClaudeAI/comments/1ukli2u/i_burned_62021_in_claude_tokens_in_june_solo_dev/)）| `具名個案（單一，非可複現統計）` |
| 2026-07-03 | GitHub issue #16856：升級至 2.1.1 版後 token 消耗速度較前版快 4 倍以上 | [GitHub Issues #16856](https://github.com/anthropics/claude-code/issues/16856) | `GitHub issue（可重現，73 則留言）` |
| 2026-07-03 | GitHub issue #38335：Max 方案 session 額度自 3/23 起異常加速消耗；截至 07-09 累積 791 則留言、536 個讚，社群互動量最高條目之一 | [GitHub Issues #38335](https://github.com/anthropics/claude-code/issues/38335) | `GitHub issue（791 則留言、536 個讚，07-09 數）` |
| 2026-07-08 | GitHub issue #41506：Max 方案（$100/月）token 消耗量自 3/28-29 起在未變更設定下增加約 3-5 倍，累積 54 則留言、29 個讚 | [GitHub Issues #41506](https://github.com/anthropics/claude-code/issues/41506) | `GitHub issue（54 則留言、29 個讚）` |
| 2026-07-08 | 「Cache hit rate dropping by 20% doubles your agent's bills」：使用者以圖表分享 cache 命中率下降 20% 會讓 agent 帳單翻倍 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uqsah2/cache_hit_rate_dropping_by_20_doubles_your_agents_bills/)）| `單一貼文（圖為主，本群唯一機制解釋）` |
| 2026-07-08 | 「Claude Max (20x) weekly limit exhausted in less than a day」：Max 20x 方案週額度不到一天用盡 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/claude_max_20x_weekly_limit_exhausted_in_less/)）| `單一貼文（無互動數）` |
| 2026-07-09 | 「Claude Max 20x: Why did 27% of one session consume 7% of my entire weekly limit?」：單一 session 27% 的時間即消耗掉整週額度 7% | Reddit r/ClaudeAI（[原文](https://www.reddit.com/r/ClaudeAI/comments/1urqgqx/claude_max_20x_why_did_27_of_one_session_consume/)）| `單一貼文（帶具體比例）` |
| 2026-07-13 | 「Usage limits getting lower」：Max 5x 訂閱用戶回報近一週用量額度消耗速度明顯變快，5 小時額度約 2 小時即用完 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uve90h/usage_limits_getting_lower/)）| `單一貼文（無互動數）` |
| 2026-08-25 | 「Is Claude Code intentionally burning more tokens now?」——隔 43 天再現同方向質疑 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1vxw3fi/is_claude_code_intentionally_burning_more_tokens/)） | `單一貼文（無互動數）` |

**證據硬度五值（由來源決定，不由結論多強決定）：** 官方一手／GitHub issue（附留言數，可重現者標明）／具名個案／單一貼文（附真實互動數）／單一貼文（無互動數）。

**表格細節**
- **07-13「Usage limits getting lower」**：07-14～07-31 未見同一主張的第二來源；同方向的 07-21 GitHub issue #29579「16% 用量即觸發 rate limit」（153 則留言）完整追蹤在 [[entities/claude-code]] 已知問題。
- **08-25「intentionally burning more tokens」**：質疑近幾個月是否要燒更多 token 才能完成同樣的任務；無數字、無版本號，只說明這個現象還在。

### 三種解釋，目前各自站在哪

> 三種解釋互不排斥。有新證據時改寫的是格子，不是加一種解釋。
%% 維運備忘：三列固定不增減；被排除者改寫「已排除（日期＋依據）」仍留表，見規則檔第 3 條 %%

| 解釋 | 支持證據 | 還排除不掉的部分 |
|------|---------|-----------------|
| **模型真的退步**（同任務要更多輪次／token）| #16856 指名版本號（2.1.1），最接近「版本行為改變」的一則 | 沒有版本前後的對照實驗，全部是主觀感受加帳單金額（推論）|
| **計費或計量改變**（token 怎麼算變了，不是真的用更多）| $62,021 具名案例＋07-08「cache 命中率下降 20% 帳單翻倍」的機制描述 | 官方未說明計費機制或 cache 命中率變化的成因（推論）|
| **你這端的配置**（orchestration、MCP 工具或 context 管理造成的浪費）| #38335 與 06-26「自訂編排路由失效」同屬「工具行為不一致」 | 沒有任何一則「改完設定就恢復正常」的回報（推論）|

**假說細節**

- **模型真的退步**：若近期版本在等量任務上確實需要更多 tool call 或更長 thinking，會直接反映成 token 上升。目前沒有官方或第三方在同一組 prompt 上做版本前後的用量對照。
- **計費或計量改變**：$62,021 案例與「5x 更貴」報導講的是帳單與配額速度，不是任務品質；cache 命中率若因 context 結構或後端調度而下降，重算的 token 會直接推高帳單，模型能力不必真的變差。
- **你這端的配置**：multi-agent 與 MCP 工具疊加的成本是 [[topics/community-tech-discussions]] 已記錄的問題；若真是 context 腐蝕或配置問題，理論上調 CLAUDE.md、少一層 subagent 就會緩解，但至今沒有人回報緩解成功。

**目前的說法**：十則回報方向一致、來源獨立，但沒有一則帶測試方法或版本前後對照，三種解釋都排除不掉。官方對這一批沒有專文，[#65687](https://github.com/anthropics/claude-code/issues/65687) 到 2026-08-21 仍開啟。08-25 那則沒有互動數也沒有新機制，只說明現象還在。

---

## Opus 5 上線後品質觀感（2026-07-25 起）

[[entities/opus-5]] 於 2026-07-24 上線後，本頁累積 **15 則**訊號：下表五種主張收 14 則，另一則（effort 旋鈕非單調）已證偽，見表下。收料起點是 Opus 5 的上線日，不是「這些抱怨都指向 Opus 5」——其中六則沒有指名模型版本。十四則裡十二則是單一使用者觀感，另兩則有外部依據（一則第三方基準待查證、一則 GitHub issue 已查證屬實）。逐則原文與 Opus 5 這個模型自己的官方基準見 [[entities/opus-5]]「這些數字是誰量的」；本頁只記它作為第三條退步線的狀態。

> 一種主張一列，同一批貼文不會在兩列各算一次。
%% 維運備忘：上限 6 列、新貼文只改最後動態與則數、逾 90 天無新事實即移出，逐則原文留時序，見規則檔第 4 條 %%

| 主張 | 則數 | 最後動態 | 證據硬度 |
|---|---|---|---|
| **泛化變慢／變囉唆**（不指名模型版本）| 6 | 2026-08-26「I miss the old Claude Code」 | 單一貼文（HN 25 分）＋五則無互動數貼文 |
| **Opus 5 過度自信、難以調教** | 3 | 2026-08-13「rage-inducing to use」 | 單一貼文（其中一則登上該週熱門榜）|
| **懷疑正在被 A/B 測試降 effort** | 3 | 2026-08-28「Is it even legal…nerf」 | 單一貼文（其中一則登上該週熱門榜，查證過程無法覆核）|
| **第三方工具評測** | 1 | 2026-08-25 Sonar benchmark ❓ 待查證 ⟨Q-01⟩ | 僅標題可用，數字未見報導 |
| **二進位對 Opus 5 的硬編碼限制** | 1 | 2026-07-26（已查證屬實，見 [[topics/community-tech-discussions]]）| GitHub issue #80988 |

**懸置細節**

- ⟨Q-01⟩ ❓ **待查證**（標 2026-08-25｜查 Sonar、code quality benchmark）：HackerNoon「Claude Opus 5 Code Quality: What Sonar's Benchmark Reveals」（僅標題可用）——查實的話會是這條線上唯一一則第三方量化評測，其餘 14 則都是主觀回報。

**兩件要講清楚的事**

- **effort 旋鈕「非單調」的說法不成立**：2026-07-29 一則 Reddit 貼文稱 effort 超過 `high` 後編碼分數反而下降、並稱官方 migration guide 自承此事。
- 2026-08-08 查官方文件後判定不成立——官方明載 Opus 5 把額外 effort 轉成更好結果的可靠度高於歷代 Opus（比對見 [[entities/opus-5]]）。本頁先前把它當成「唯一一筆官方確認的行為特性變化」，那是錯的。
- **這條線和「context 腐蝕」那場爭論不是同一件事**：「越用越笨是模型退步還是 context 腐蝕」已在 [[topics/community-tech-discussions]]「現在吵到哪」吵出共識（context 腐蝕）。本頁不重判那場爭論，只記官方對這 15 則到今天沒有回應。

---

## 模型釘選：你選的不一定算數（2026-02 起）

**這不是單一 bug，是「你宣告的模型選擇不被保證」在四種機制上重複發生**——沒有鎖版能力（設計面）、picker 狀態不保持（實作面）、計費壓力下被換掉（商業面）、能力無預告移除（產品面）。四個節點橫跨 2026-02 至 2026-07，彼此獨立、來源不同：

- **設計面（2026-02-23，GitHub issue #27892，⛔ 官方以 not planned 關閉）**：`--model` 只接受 family 名稱（opus／sonnet），不接受版本 pin id；`.claude/settings.json` 也沒有鎖版設定；一旦被自動升版就沒有回頭路（[GitHub #27892](https://github.com/anthropics/claude-code/issues/27892)）。
- **實作面（2026-04-10，GitHub issue #46221，已關閉為 #45978 重複）**：Opus 4.6 1M context 變體從 model picker 消失、被 200k 取代；預設在你沒動手的情況下改成 Sonnet 4.6；進行中的 session 被中途降級；就算手動選回 1M，下次 `/model` 那個選項又不見了（[GitHub #46221](https://github.com/anthropics/claude-code/issues/46221)）。
- **商業面（2026-07-25）**：Fable 5 的計費壓力下，超出上限會被換成 Opus 4.8。**這一項官方已改**：Anthropic 於 2026-06-11 對 Wired 承認當初的取捨錯了，並把回退改成會通知你（見 [[entities/fable-5]]）。仍有爭議的是換模型之後的計費算得對不對（[[entities/pricing]]）。
- **產品面（2026-05-21）**：extended thinking 能力在沒有預告的情況下從 Claude Code 移除（見 [[entities/claude-code]] 已知問題）。

**你會看到的後果**：一名開發者連續 36 天記錄使用數據，量出不同模型間高達 11.5 倍的效率差距，並觀察到模型有時在沒有明確通知下被換掉——同一筆工作跑在哪個模型上，會直接改變你的花費與完成時間。

**只有單一來源的具體宣稱（2026-08-04）：** r/ClaudeCode 一則貼文宣稱以實測記錄四種繞過模型釘選的方式，並稱 Sonnet 4.6 遭無預告移除。該貼文所指的**現象**方向與上述四個節點一致，但貼文獨有的「4 measured bypass vectors」與「Sonnet 4.6 silently removed」**具體技術細節**至今只有這一個來源、無第二來源核對，本頁只採計現象，不採計其量化宣稱（[Reddit 原文](https://www.reddit.com/r/ClaudeCode/comments/1vf7uv5/model_pinning_is_completely_broken_in_claude_code/)）。❓ **待查證**（標 2026-08-10｜查 bypass vectors、silently removed｜複 2026-09-13）｜**貼文的具體量化宣稱**（2026-08-04 單一 Reddit 來源）：截至 2026-09-07 未見第二來源。

**這件事會改到你的成本估算**：[[topics/model-comparison]] 的實付成本換算假設你跑在你選的模型上，而 #46221 記錄的正是「選定狀態無法保持」。在那頁做模型或 context 的成本比較之前，先確認釘選成不成立（1M 這一項的完整脈絡見 [[topics/long-context-1m]]）。

---

## 技術彙整

- **社群把證據做成基礎設施（forensic archive，2026-08-12）**：一名開發者把數月來蒐集的 Claude Code bug、模型退化與設定異常整理成公開存檔，附上 HackerOne 回報紀錄（[原文](https://www.reddit.com/r/ClaudeCode/comments/1vm9igt/i_made_a_forensic_archive_for_claude_failures/)）。意義不只是又一則抱怨：零散貼文第一次被整理成可被引用的檔案，與 2026-04-25 的 CC-Canary（自動偵測）形成人工存證與自動偵測兩條路。
- **Stop hooks 失效**：Claude 4.7 起無視自訂 stop hooks，與整體效能退步是兩件事，機制層面官方未公開說明；狀態以 [[entities/claude-code]] 已知問題為準。
- **自訂編排路由失效（2026-06-26）**：相同的自訂 orchestration 設定，OpenCode 能穩定路由到自訂 providers 的 agents，Claude Code 不行；屬工具行為不一致，不是模型能力退步。

---

## 目前結論

- 🔍 三條線只有 2026-04 那一條有官方說法，另外兩條到今天沒有——各自到哪一格見上方「三條線現在到哪」。
- 🔴 沒有任何一條線有版本前後的對照實驗；你能拿到最硬的證據是自己的 session log——**你可以：** 照「怎麼自己量一次」量一輪再下結論。
- ⛔ 「換個模型就好」「回舊版就好」機制上不成立，官方 2026-02-23 已把鎖版需求以 not planned 關閉——**你可以：** 見「模型釘選：你選的不一定算數」，估成本前先確認釘選成不成立。
- ⚠️ 帳單變多不等於模型變差：週配額換軌（09-14 生效），另有數件計費爭議未解——**你可以：** 先到 [[entities/pricing]] 對一次自己的帳，再回來看模型。
- ✅ Boris Cherny 於 2026-04-23 事後報告承諾的 50+ 修復，社群自 2026-05-03 起的逐項驗證未見完成結果；本站於 2026-09-07 停止追蹤這一條，改以上表第一列的 issue 狀態為準。

> ✅ 已有結果／🔴 現在仍無解／⛔ 官方明說不做／⚠️ 會被誤判成模型問題的事／🔍 還在等答案。

---

## 影響範圍

- 用 Claude Code 跑 agentic 自動化的開發者：受影響的是每次任務的 token 與時間，量法見「怎麼自己量一次」。
- 依賴自訂 hooks 注入確定性邏輯的工作流：stop hooks 自 Claude 4.7 起被忽略，屬獨立問題，見 [[entities/claude-code]] 已知問題。
- 因品質或帳單而考慮降級、退訂的付費用戶：計費面見 [[entities/pricing]]。

---

## 相關實體

本頁答的是「哪幾條退步線官方回應了、哪幾條沒有，以及你怎麼自己量」。相鄰的頁各答一題，不重複：

- [[entities/claude-code]]「現在會咬到你的」——現在什麼壞了、誰會遇到、怎麼繞（逐個 issue）
- [[entities/opus-5]]「這些數字是誰量的」——Opus 5 這個模型的官方基準與社群觀感（逐則原文）
- [[feature-radar]]「從你現在的版本升上去，會遇到什麼」——升上去會壞什麼；你沒升版卻覺得變慢，才是本頁
- [[entities/pricing]]「事故現在還在發生嗎」——帳單被扣錯、配額換軌；token 燒得比以前快在本頁
- [[topics/community-tech-discussions]]「現在吵到哪」——「越用越笨是模型退步還是 context 腐蝕」那場觀念之爭
- [[topics/model-comparison]]、[[topics/long-context-1m]]、[[entities/opus-4-7]]、[[entities/opus-4-8]]——以上四頁是本頁事實的上下游：選型與成本換算、1M 這個旋鈕、以及兩代舊模型自己的頁。

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [[news/2026-05-03]]
- [[news/2026-05-05]]
- [[news/2026-05-09]]
- [[news/2026-07-01]]
- [[news/2026-07-03]]
- [[news/2026-07-08]]
- [[news/2026-07-09]]
- [[news/2026-07-26]]
- [[news/2026-07-29]]
- [[news/2026-07-30]]
- [[news/2026-08-12]]
- [[news/2026-08-26]]
- [CC-Canary GitHub](https://github.com/delta-hq/cc-canary)
- [Anthropic's definition of safety is too narrow](https://jonathannen.com/anthropic-safety-too-narrow/)

## 時序（最新在上，按月分組）

### 2026-09

#### 2026-09-03
- **全模型錯誤率升高，同日排除**：12:43 UTC 起 Sonnet 5 錯誤率升高，Mythos、Fable 5／5.1、Opus 5／4.8／4.6 一併受影響，13:41 UTC 鎖定原因、16:16 UTC 標記解決；影響 claude.ai、API、Claude Code 與 Cowork。屬服務穩定性事件，非能力或計費變化（[Anthropic Status](https://status.claude.com/incidents/461yvfrzpwtt)）

### 2026-08

#### 2026-08-28
- **「Is it even legal for Anthropic to nerf its models this hard?」**：r/ClaudeCode 貼文質疑 Opus 5、Fable 5 表現遜於預期，指控模型遭「削弱」；無互動數可佐證，方向與 08-22／08-26「懷疑正在被 A/B 測試降 effort」一致，只說明這個現象還在（來源：[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1w0t53b/is_it_even_legal_for_anthropic_to_nerf_its_models/)）

#### 2026-08-26
- **「Opus 5 上線後品質感知訊號群」首度出現「懷疑正在被即時 A/B 測試」直接主張**：r/ClaudeCode 貼文「I can tell when I'm being A/B tested with nerfd models」稱可依 Claude 是否跳出「這次 session 表現如何」回饋彈窗判斷自己是否被分到降規模測試模型；同日補記 08-22 r/artificial 週熱門貼文「I spent the morning digging into Anthropic so I could write it up properly」，作者稱查閱一手資料後認為 Anthropic 似乎正在 Claude Code 上 A/B 測試降低 effort 的版本，兩者方向一致；均無具體量化數字或版本號，但與 07-25 官方 migration guide 自承 effort dial 非單調現象呼應，是本訊號群首次從「效能感受變差」進展到「懷疑正在被主動測試」的主張（來源：[Reddit「nerfd models」](https://www.reddit.com/r/ClaudeCode/comments/1vystw3/i_can_tell_when_im_being_ab_tested_with_nerfd/)、[Reddit「digging into Anthropic」](https://www.reddit.com/r/artificial/comments/1vvjmmo/i_spent_the_morning_digging_into_anthropic_so_i/)）
- **「I miss the old Claude Code」：泛化「新模型變慢」抱怨，附真實 HN 分數**：部落格作者比較年初與近期使用經驗，稱換用新模型後同任務要花更久時間才真正開始寫程式；HN score 25（本訊號群少見的真實分數），惟未點名具體模型版本，僅可佐證「泛化變慢」現象持續，不歸入特定模型爭議（來源：[alexkras.com](https://alexkras.com/focus-is-the-main-feature-why-i-miss-the-old-claude-code/)）

#### 2026-08-25
- **「Token 消耗異常訊號群」沉寂 43 天後再現**：r/ClaudeCode 貼文「Is Claude Code intentionally burning more tokens now?」質疑近幾個月是否要燒更多 token 才能完成同樣的任務；無互動數可佐證，屬該群自 07-13 以來第十則，沒有新的機制證據，只說明現象還在（來源：[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1vxw3fi/is_claude_code_intentionally_burning_more_tokens/)）

#### 2026-08-20（週熱門重浮上，原發時間較早）
- **「Claude is Losing Me After Being Heavy User Since Release」**：r/ClaudeAI 重度使用者發文表達對 Claude 逐漸失望的心情，具體抱怨內容未見於本次摘要；週熱門標記，屬「Opus 5 上線後品質感知訊號群」第十則訊號，僅計入現象延續（來源：[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vqsas9/claude_is_losing_me_after_being_heavy_user_since/)）

#### 2026-08-19
- **「過去兩週表現反覆不穩」**：r/ClaudeCode 貼文「I've never felt Claude been degraded for so long before」，使用者反映過去兩週 Claude 表現反覆不穩、多半比平常差，詢問是否為運算資源問題；無互動數可佐證，無具體量化數字或版本號，屬「Opus 5 上線後品質感知訊號群」第九則訊號，只說明現象還在（來源：[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1vshkrf/)）

#### 2026-08-13（補記，08-15 日報收錄）
- **「幾乎令人惱火」：已依官方建議調整仍無法馴服 Opus 5**：r/ClaudeAI 貼文「Opus 5 is actually almost rage-inducing to use.」，使用者稱已依官方建議調整、試過各種全域 CLAUDE.md 設定，仍無法讓 Opus 5 行為符合期待；週熱門標記，但無具體量化數字，屬「Opus 5 上線後品質感知訊號群」第八則訊號，只說明現象還在（來源：[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vn8ml6/opus_5_is_actually_almost_rageinducing_to_use/)）

#### 2026-08-14
- **「泛化品質下滑」投訴延續，兩則新增均為單一 Reddit 來源**：r/ClaudeCode 同日兩則獨立貼文——「Serious question regarding CC quality」指近 3 個月「大幅」（MASSIVE）品質下滑、不限特定模型、內文提及 Opus 5 尤其令人失望（原文截斷）；「Claude Code got slower since I upgraded from Pro to Max」反映升級後 session 時長變為 3 倍、任務難度與規模未變。兩者皆無互動數可佐證、無跨平台佐證，屬「Opus 5 上線後品質感知訊號群」第六、七則訊號，只說明現象還在，未提供新的機制性證據（來源：[Reddit「CC quality」](https://www.reddit.com/r/ClaudeCode/comments/1vo3ygk/serious_question_regarding_cc_quality_no_hate_or/)、[Reddit「got slower」](https://www.reddit.com/r/ClaudeCode/comments/1vo3y1g/claude_code_got_slower_since_i_upgraded_from_pro/)）

#### 2026-08-12
- **社群發起「forensic archive」證據存檔**：r/ClaudeCode 用戶將數月來遇到的 Claude Code bug、模型退化、設定異常整理成公開存檔，含 HackerOne 回報紀錄；單一社群來源、無「週熱門」標記，score 不可信，但意義是把品質下滑的證據從零散貼文升級為可被引用的系統化存證，與 CC-Canary（2026-04-25，自動化偵測）形成人工彙整＋自動化偵測並行的兩條路徑，詳見「技術彙整」（來源：[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1vm9igt/i_made_a_forensic_archive_for_claude_failures/)）

#### 2026-08-04
- **模型釘選繞過主張（現象已獲跨機制佐證，具體宣稱仍單一來源）**：Reddit r/ClaudeCode 貼文宣稱記錄四種繞過 Claude Code 模型釘選機制的方式，並稱 Sonnet 4.6 遭靜默移除；2026-08-09 查證發現「模型釘選不可靠／靜默降級」現象已有兩則早於此貼文的獨立 GitHub issue 佐證（#27892、#46221），詳見「模型釘選／靜默降級 訊號群」子區塊；但該貼文獨有的「4 measured bypass vectors」量化宣稱仍僅單一 Reddit 來源、無「週熱門」標記，未經覆核（來源：[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1vf7uv5/model_pinning_is_completely_broken_in_claude_code/)）

### 2026-07

#### 2026-07-30
- **「Opus 5 is not as good as i thought」**：使用者原先依跑分預期 Opus 5 優於 Fable 5，實際使用後認為仍有落差；單一 Reddit 貼文，屬「Opus 5 上線後品質感知訊號群」第五則訊號（來源：[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1var15k/opus_5_is_not_as_good_as_i_thought/)）

#### 2026-07-29
- **「越用越笨」與「過度自信」雙投訴同日出現**：r/ClaudeCode 兩則獨立貼文——「Is Claude getting dumber (or am I getting smarter)?」反映回答變得反覆、囉唆、過度確認；「Has anyone been able to tame Opus 5?」反映 Opus 5 對 codebase 理解與使用者意圖判斷過度自信、常篤定但錯；均為單一貼文、score 不可信，屬「Opus 5 上線後品質感知訊號群」（來源：[Reddit「getting dumber」](https://www.reddit.com/r/ClaudeCode/comments/1v9u98q/is_claude_getting_dumber_or_am_i_getting_smarter/)、[Reddit「tame Opus 5」](https://www.reddit.com/r/ClaudeCode/comments/1v9u8ev/has_anyone_been_able_to_tame_opus_5/)）

#### 2026-07-26
- **Claude Code 二進位對 Opus 5 硬編碼行為限制**：討論指出 2.1.219／220 版編譯二進位內建僅針對 Opus 5 的系統提示，除非使用者明確要求否則不得呼叫 AgentTool、workflows、deep-research；社群觀察，未經官方證實；已完整收錄於 [[topics/community-tech-discussions]]，本頁列為「Opus 5 上線後品質感知訊號群」第二則訊號（來源：Reddit r/ClaudeCode，經 HN 轉載 score 18）

#### 2026-07-25
- **一則貼文稱 Opus 5 effort dial 非單調，該說法已證偽**：2026-07-29 r/artificial 週熱門討論指 effort 旋鈕超過「high」後編碼分數反而下降、並稱官方 migration guide 自承；該說法已於 2026-08-08 經官方文件證偽，見上方「Opus 5 上線後品質觀感」（來源：[Reddit r/artificial](https://www.reddit.com/r/artificial/comments/1v60pga/opus_5s_effort_dial_is_not_monotonic_above_high/)）

#### 2026-07-09
- **Max 20x 額度異常比例回報**：Reddit 用戶質疑 Max 20x 方案中單一 session 27% 的時間即消耗掉整週額度 7%，與同期 GitHub #38335 額度異常回報呼應（該 issue 累積留言數同日增至 791 則）；訊號鏈持續延燒（來源：[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1urqgqx/claude_max_20x_why_did_27_of_one_session_consume/)）

#### 2026-07-08
- **訊號群補上具體技術機制與兩則異常比例回報**：Reddit「cache 命中率下降 20% 導致 agent 帳單翻倍」首度為「計費/計量問題」假說提供技術描述；同日另有「Max 20x 方案週額度不到一天用盡」回報；加上 GitHub issue #41506 回報 Max 方案（$100/月）token 消耗量自 3 月底起在未變更設定下增加約 3-5 倍（累積 54 則留言、29 個讚）；三者與 07-03 的 #38335、07-01 的兩則社群訊號方向一致，訊號密度使定調上調為「結構性未解問題」；官方尚未回應（來源：[GitHub Issues #41506](https://github.com/anthropics/claude-code/issues/41506)、[Reddit cache 命中率](https://www.reddit.com/r/ClaudeCode/comments/1uqsah2/cache_hit_rate_dropping_by_20_doubles_your_agents_bills/)、[Reddit Max 20x 週額度](https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/claude_max_20x_weekly_limit_exhausted_in_less/)）

#### 2026-07-04
- **Plan mode 逾時自動代答 + 整體變慢投訴延續**：Reddit r/ClaudeCode 用戶（兩則獨立回報）反映 plan mode 逾時後自動選擇非預期選項，並主觀感受近期回應變慢、能力下降；與 07-02 已記錄的 AskUserQuestion 60 秒逾時自動代答爭議（見 [[topics/community-tech-discussions]]）屬同一「逾時代答破壞決策體驗」機制的延續投訴，「變慢/能力下降」部分仍屬主觀感受，無 benchmark 或版本號佐證（來源：[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1und5g7/claude_code_cli_is_getting_harder_to_use_plus/)）

#### 2026-07-03
- **Token 消耗異常訊號群成形**：GitHub issue #16856（2.1.1 版 token 消耗達 4 倍以上）與 issue #38335（Max 方案額度自 3/23 起異常消耗，大量留言）同日浮上，與 07-01 的兩則社群訊號（HN「5x 更貴」、$62,021 具名案例）共同構成四個獨立來源的成本異常訊號群；詳見「Token 消耗異常訊號群」子區塊；官方尚未回應（GitHub Issues）

#### 2026-07-01
- **Claude Code 成本暴漲討論爆發**：Vincent Schmalbach 發文「Claude Code Just Got 5x More Expensive」登上 HN（score 53），同日 Reddit 出現獨立開發者單月燒 $62,021 token 的具名案例；社群懷疑與模型切換或計費方式變更有關；詳見 [[topics/community-tech-discussions]] 對應條目

### 2026-06

#### 2026-06-26

- **自訂 Agent 編排路由失效**：用戶反映 Claude Code 無法可靠路由到自訂 orchestration 中的自訂 providers agents，OpenCode 同設定可穩定執行；問題指向 Claude Code 編排機制的行為不一致性，非模型能力問題；官方尚未回應（Reddit r/ClaudeAI）

#### 2026-06-18

- **LLM 無障礙偏差（Claude Code issue #56079）**：開發者 Aaron Gustafson 揭露：在 CLAUDE.md 已明確指定 WCAG 2.2 AA 規格的專案中，Claude Code 仍將無障礙修復視為可選取捨。模型自述原因是在追求「coding speed」時 accessibility 被降級；Aaron Gustafson 評論此為「值觀優先序偏差」而非知識不足。此偏差複製了人類工程師「稍後再修無障礙」的習慣，AI 未改善既有偏見（2026-06-20 持續追蹤中）

### 2026-05（總結；原始條目已移出）

- **這是「靜默的日常效能變化」第一次被文件化的月份。** MarginLab 每日跑 SWE-bench-Pro，量到 Opus 4.7 在 Opus 4.8 發布前連續五天出現統計顯著的 pass rate 下降、發布後立刻恢復——對象是 4.7，不是 Opus 5。
- 另一名開發者連續 36 天記錄使用數據，量出模型間 11.5 倍效率差距，並觀察到模型被無預告換掉。
- 有人以三週結構化 session log 記錄 Opus 4.7／Sonnet 4.6 在同一專案上持續失敗，是當時最有文件支撐的一則退步投訴，官方未回應。
- 同月 Opus 4.8 升版後的 `thinking blocks` 400 錯誤已由 v2.1.156 修復。
- 原始條目見 [[topics/code-quality-decline-archive#2026-05]]

### 2026-03～04（總結；原始條目已移出）

- **這是三條線裡唯一有官方答案的一段。** 2026-03 起使用者開始察覺異常，04 月大量回報湧入，Anthropic 於 04-23 發文說明三件各自獨立的工程變更並各自修復，同時重置所有訂閱者用量；本站於 04-24 收錄。
- 三個修法各自的版本見上方「三條線現在到哪」表下。
- 同月社群推出 CC-Canary 開始自動偵測效能漂移；Boris Cherny 的事後報告承諾 50+ 修復項目，逐項驗證的結果見上方「目前結論」最後一條。
- 當時流傳的「Opus 4.7 參數約 4T、少於 4.6 的 5.3T」一組數字，經 2026-08-26 查證論文原文後不成立。
- 原始條目見 [[topics/code-quality-decline-archive#2026-03～04]]
