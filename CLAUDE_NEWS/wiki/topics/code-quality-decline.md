---
page: "topics/code-quality-decline"
kind: "topic"
status: "ongoing（官方已說明工程疏失，恢復情況見下方摘要）"
domain: "🌐 社群"
last_updated: "2026-09-03"
last_news_update: "2026-08-29"
status_main: "ongoing"
days_since_news: 6
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 6
inbound_links: 31
attribution_count: 24
attribution_last: "2026-08-28"
top_source: "reddit"
pending_count: 3
pending_overdue: 0
pending_next_review: "2026-09-08"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code 效能退步事件

**狀態：** ongoing（官方已說明工程疏失，恢復情況見下方摘要）
**領域：** 🌐 社群
**開始日期：** 2026-03（推測）
**最後更新：** 2026-09-03
**最後新聞更新：** 2026-08-29

> **最近效能退步事件**（2026-08-28）
> 「Opus 5 上線後品質感知訊號群」累計第 14 則訊號：Reddit r/ClaudeCode 使用者質疑 Opus 5／Fable 5 表現遜於預期、指控遭「削弱」，無週熱門標記、score 不可信，方向與 08-22／08-26 的「A/B 測試降 effort」懷疑一致，僅計入現象延續，未提供新機制證據。

---

## 摘要

**當前狀態：** 官方已說明 4 月退步原因為工程疏失；❓ **待查證**（標 2026-08-10｜查 [[entities/claude-code]]、效能退步恢復、engineering missteps｜複 2026-09-13）｜**4 月效能退步是否已恢復**：已掃日報至 2026-09-02 無後續；官方頁面未查證；2026-06 下旬起投訴焦點轉向「token 消耗異常／成本暴增」——訊號鏈自 06-27 延燒至 07-13（共 17 天），累計九個獨立訊號（HN 熱議、$62,021 具名案例、四則 GitHub issue、兩則額度異常比例回報、07-13 Max 5x 額度消耗變快回報），且 07-08 首度出現具體技術機制觀察（cache 命中率下降），定調從「值得觀察」上調為「結構性未解問題」；仍無法斷定是模型真退步、計費計量問題、或 context/工具配置問題（詳見「Token 消耗異常訊號群」）；此前的「工具行為不一致」投訴（自訂編排路由失效、無障礙偏差）性質也不一，共同點是均非典型的模型能力退步，官方多未回應。

Claude Code 在 2026 年 3 月至 4 月間出現長達約一個月的效能明顯退步，引發大量開發者不滿。2026-04-24，Anthropic 首次正式承認此問題，說明原因為**工程疏失**（engineering missteps），並非刻意的模型行為調整。

---

## Token 消耗異常訊號群（2026-06 下旬起）

**訊號鏈自 06-27 延燒至 07-13（共 17 天），累計九個獨立訊號**（06-27 為早期 quota 焦慮訊號，見 [[topics/community-tech-discussions]]「額度焦慮系列」；07-01 起為明確的 token/成本異常主張）：

| 日期 | 訊號 | 來源 | 強度 |
|------|------|------|------|
| 2026-07-01 | 「Claude Code Just Got 5x More Expensive」：用戶回報原先兩天用量的 $50 配額現在一小時燒完 | Vincent Schmalbach blog（[原文](https://www.vincentschmalbach.com/claude-code-quietly-looks-5x-more-expensive/)，HN score 53） | 中高（HN score 53 達對照表中門檻）|
| 2026-07-01 | 獨立開發者單月燒 $62,021 token 的具名案例 | Reddit r/ClaudeAI（[原文](https://www.reddit.com/r/ClaudeAI/comments/1ukli2u/i_burned_62021_in_claude_tokens_in_june_solo_dev/)）| 個案但引發廣泛討論 |
| 2026-07-03 | GitHub issue #16856：升級至 2.1.1 版後 token 消耗速度較前版快 4 倍以上 | [GitHub Issues #16856](https://github.com/anthropics/claude-code/issues/16856) | 具體版本號可複現主張 |
| 2026-07-03 | GitHub issue #38335：Max 方案 session 額度自 3/23 起異常加速消耗；截至 07-09 累積 791 則留言、536 個讚，社群互動量最高條目之一 | [GitHub Issues #38335](https://github.com/anthropics/claude-code/issues/38335) | 高（留言數達對照表高門檻，且持續增長）|
| 2026-07-08 | GitHub issue #41506：Max 方案（$100/月）token 消耗量自 3/28-29 起在未變更設定下增加約 3-5 倍，累積 54 則留言、29 個讚 | [GitHub Issues #41506](https://github.com/anthropics/claude-code/issues/41506) | 高（留言數達對照表高門檻，與 #38335 同期同方向）|
| 2026-07-08 | 「Cache hit rate dropping by 20% doubles your agent's bills」：使用者以圖表分享 cache 命中率下降 20% 會讓 agent 帳單翻倍 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uqsah2/cache_hit_rate_dropping_by_20_doubles_your_agents_bills/)）| 首度提出具體技術機制，補足假說二的解釋空缺；圖片為主、文字說明有限，尚待第三方覆核（07-09～07-31 news 查無直接跟進，至今無後續） |
| 2026-07-08 | 「Claude Max (20x) weekly limit exhausted in less than a day」：Max 20x 方案週額度不到一天用盡 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/claude_max_20x_weekly_limit_exhausted_in_less/)）| 具體異常比例回報，與同日 GitHub 額度耗盡回報呼應 |
| 2026-07-09 | 「Claude Max 20x: Why did 27% of one session consume 7% of my entire weekly limit?」：單一 session 27% 的時間即消耗掉整週額度 7% | Reddit r/ClaudeAI（[原文](https://www.reddit.com/r/ClaudeAI/comments/1urqgqx/claude_max_20x_why_did_27_of_one_session_consume/)）| 具體異常比例回報，質疑額度計算機制本身 |
| 2026-07-13 | 「Usage limits getting lower」：Max 5x 訂閱用戶回報近一週用量額度消耗速度明顯變快，5 小時額度約 2 小時即用完 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1uve90h/usage_limits_getting_lower/)）| 單一貼文，方向與既有額度異常訊號一致（細節見表下）|
| 2026-08-25 | 「Is Claude Code intentionally burning more tokens now?」——隔 43 天再現同方向質疑 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1vxw3fi/is_claude_code_intentionally_burning_more_tokens/)，0 留言、無「週熱門」標記，score 不可信） | 第十則訊號，無新機制性證據 |

**表格細節**
- **07-13「Usage limits getting lower」**：尚待第三方覆核——07-14～07-31 news 無同一主張的直接覆核，但 07-21 GitHub issue #29579「16% 用量即觸發 rate limit」153 則留言延續同一「額度異常消耗」大主題方向一致，屬功能記者已知問題追蹤範疇，本頁不重複收錄細節
- **08-25「intentionally burning more tokens」**：使用者質疑近幾個月來 Claude Code 是否比過去消耗更多 token 才能完成相同任務；單一貼文、無具體數字或版本號佐證，屬本訊號群自 07-13 沉寂 43 天後的第十則訊號，僅計入現象延續

**核心分析：三種假說目前證據各支持什麼**

| 假說 | 支持證據 | 尚無法排除的部分 |
|------|---------|-----------------|
| **模型真退步**（同任務需要更多輪次 / token 才能完成）| #16856 明確指向版本號（2.1.1），較貼近「版本行為改變」框架（細節見表下） | 缺乏版本前後受控對照，全為主觀感受（推論，細節見表下）|
| **計費／計量問題**（token 計數方式改變，而非實際用量增加）| $62,021 案例＋07-08「cache 命中率下降 20% 帳單翻倍」首次提供具體機制（細節見表下） | 官方未說明計費機制或 cache 命中率變化根因（推論，細節見表下）|
| **Context／工具配置問題**（用戶端 orchestration、MCP 工具或 context 管理不當導致的浪費）| #38335 與 06-26「自訂編排路由失效」同類「工具行為不一致」訊號（細節見表下） | 無用戶回報「調整配置後恢復正常」的驗證案例（推論）|

**假說細節**
- **模型真退步**：若 4.8 或近期模型版本在等量任務上確實需要更多 tool call 或更長 thinking，將直接反映為 token 消耗上升。缺乏官方或第三方在同一 prompt 集合上做版本前後 token 用量對照（benchmark 層級證據）；目前全部是用戶主觀感受 + 帳單金額，非受控實驗
- **計費／計量問題**：$62,021 案例與「5x 更貴」報導都聚焦帳單/配額消耗速度而非任務品質下降；07-08「cache 命中率下降 20% 帳單翻倍」首度提供具體技術機制——若 prompt caching 命中率因 context 結構變化或後端調度改變而下降，重複計算的 token 會直接反映為帳單增加，不需模型能力真的變差；07-09「單一 session 27% 時間耗掉週額度 7%」進一步指向額度計算本身可能存在非線性放大；[[topics/community-tech-discussions]] 技術彙整已記錄社群懷疑「agent 模式的 token 計費方式變更」與「subagent 呼叫計費細節未透明揭示」。Anthropic 未就計費機制或 cache 命中率變化做出官方說明；cache 命中率下降的根因（使用者 context 結構改變 vs 後端調度變更）尚未釐清；無法排除只是使用習慣改變（如更多 subagent/parallel session）導致實際消耗上升
- **Context／工具配置問題**：multi-agent／MCP 工具調用疊加成本是 [[topics/community-tech-discussions]] 已記錄的系統性問題；cache 命中率下降若源於使用者端 context 結構變化（如頻繁插入不同前綴內容），亦可能是配置問題而非後端變更。若確為 context 腐蝕或配置問題，理論上應可透過調整 CLAUDE.md／減少 subagent 層級緩解，但目前無用戶回報「調整配置後消耗恢復正常」的驗證案例

**目前立場：** 訊號鏈自 06-27（quota 焦慮早期訊號）延燒至 07-13，跨 17 天持續出現同方向訊號且來源獨立，密度已足以將定調從「值得觀察」上調為**「結構性未解問題」**——三種假說均有部分支持證據且互不排斥，07-08 起新增的 cache 命中率機制觀察與兩則額度異常比例回報，首度讓「計費/計量問題」假說有了具體技術描述，07-13 再添一則 Max 5x 額度消耗變快回報但仍屬單一貼文，但仍缺乏官方說明或受控實驗佐證。訊號鏈其後沉寂 43 天，08-25 再度出現同方向質疑（單一貼文、無具體數字），僅計入現象延續，未提供新證據，三種假說的證據強度分布未變。截至 2026-08-25，Anthropic 尚未對此訊號群做出官方回應。與 [[topics/community-tech-discussions]] 對應的「Claude Code 成本 5x 暴漲」與「額度焦慮系列」條目互相引用，細節不重複展開。

---

**🧰 現在就能下的解**：—（這個症狀目前還沒有成熟到可推薦單一工具，量測起點見本頁訊號群｜候選症狀：感覺變笨，想先量測歸因）——社群現有起點是 CC-Canary（讀 session log 偵測效能漂移，見 [[topics/community-tech-tools]] 工具目錄）與「先量 context 組成再怪工具」原則（[[topics/community-large-codebase-workflow]] 線 2），但「版本前後受控對照」尚無工具承接。

## Opus 5 上線後品質感知訊號群（2026-07-25 起）

[[entities/opus-5]] 於 2026-07-24 上線後，三週內累積七則獨立訊號，構成**第三條分析線**——與上方「token 消耗異常」訊號群（聚焦帳單/計費）、以及 [[topics/community-tech-discussions]] 記錄的「Context Rot 修復五法」社群共識（聚焦「越用越笨幾乎都是 context 腐蝕，非模型退步」）皆不同，這條線聚焦**模型本身的能力/行為特性**，且首次出現官方確認等級的證據。

| 日期 | 訊號 | 來源 | 訊號強度 |
|------|------|------|---------|
| 2026-07-25 | effort 旋鈕超過「high」後編碼分數反而下降，**Anthropic 官方 migration guide 自承**（細節見表下） | Reddit r/artificial（[原文](https://www.reddit.com/r/artificial/comments/1v60pga/opus_5s_effort_dial_is_not_monotonic_above_high/)，週熱門，見 [[news/2026-07-29]]） | **官方確認**（官方文件自承，非社群推測或猜測性 benchmark）|
| 2026-07-26 | 2.1.219／220 版二進位內建僅針對 Opus 5 的兩行系統提示，限制呼叫 AgentTool／workflows／deep-research（細節見表下） | Reddit r/ClaudeCode，HN 轉載（score 18）；已收錄 [[topics/community-tech-discussions]] | 單一社群觀察（未經官方證實）|
| 2026-07-29 | 「Is Claude getting dumber (or am I getting smarter)?」：使用者反映 Claude／Claude Code 回答變得反覆、囉唆、過度確認 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1v9u98q/is_claude_getting_dumber_or_am_i_getting_smarter/)，無「週熱門」標記、score 不可信，見 [[news/2026-07-29]]） | 單一社群回報 |
| 2026-07-29 | 「Has anyone been able to tame Opus 5?」：使用者反映 Opus 5 有「過度自信」傾向，對 codebase 理解與使用者意圖判斷常顯得篤定但未必正確 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1v9u8ev/has_anyone_been_able_to_tame_opus_5/)，見 [[news/2026-07-29]]） | 單一社群回報 |
| 2026-07-30 | 「Opus 5 is not as good as i thought」：使用者原先依跑分預期 Opus 5 優於 Fable 5，實際使用後認為仍有落差 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1var15k/opus_5_is_not_as_good_as_i_thought/)，見 [[news/2026-07-30]]） | 單一社群回報 |
| 2026-08-14 | 「Serious question regarding CC quality」：近 3 個月觀察到 Claude Code 品質「大幅」（MASSIVE）下滑，不限特定模型，內文提及 Opus 5 表現尤其令人失望（原文截斷） | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1vo3ygk/serious_question_regarding_cc_quality_no_hate_or/)，無「週熱門」標記、score 不可信） | 單一社群回報 |
| 2026-08-14 | 「Claude Code got slower since I upgraded from Pro to Max」：升級後 session 時長變為 3 倍，任務難度、規模與專案皆未變 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1vo3y1g/claude_code_got_slower_since_i_upgraded_from_pro/)，無「週熱門」標記、score 不可信） | 單一社群回報 |
| 2026-08-13 | 「Opus 5 is actually almost rage-inducing to use.」：使用者稱已依官方建議調整、試過各種全域 CLAUDE.md 設定，仍無法讓 Opus 5 行為符合期待 | Reddit r/ClaudeAI（[原文](https://www.reddit.com/r/ClaudeAI/comments/1vn8ml6/opus_5_is_actually_almost_rageinducing_to_use/)，週熱門標記，達收錄低門檻） | 單一社群回報（週熱門達低門檻，惟無具體量化數字） |
| 2026-08-19 | 「I've never felt Claude been degraded for so long before」：使用者反映過去兩週 Claude 表現反覆不穩，多半比平常差，詢問是否為運算資源問題 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1vshkrf/)，0 留言、無「週熱門」標記，score 不可信） | 單一社群回報（無具體量化數字或版本號，僅主觀感受描述） |
| 2026-08-19（週熱門重浮上，原發時間較早） | 「Claude is Losing Me After Being Heavy User Since Release」：重度使用者發文表達對 Claude 逐漸失望的心情，具體抱怨內容未見於本次摘要 | Reddit r/ClaudeAI（[原文](https://www.reddit.com/r/ClaudeAI/comments/1vqsas9/claude_is_losing_me_after_being_heavy_user_since/)，週熱門標記，達收錄低門檻） | 單一社群回報（僅標題可考，無具體量化數字或版本號） |
| 2026-08-25 | 「Claude Opus 5 Code Quality: What Sonar's Benchmark Reveals」：程式碼品質分析工具 Sonar 對 Opus 5 生成程式碼進行基準測試，具體結果 ❓ 待查證 ⟨Q-01⟩ | Google News/HackerNoon（僅標題可用） | 待查證（第三方工具評測，具體數字未見報導）|
| 2026-08-22（週熱門，08-26 收錄） | 「I spent the morning digging into Anthropic...」：作者懷疑 Anthropic 正在 A/B 測試降低 effort 版本（細節見表下） | Reddit r/artificial（[原文](https://www.reddit.com/r/artificial/comments/1vvjmmo/i_spent_the_morning_digging_into_anthropic_so_i/)，週熱門標記，達收錄低門檻） | 單一社群回報（週熱門達低門檻，惟查證過程無法覆核；細節見表下）|
| 2026-08-26 | 「I can tell when I'm being A/B tested with nerfd models」：使用者稱可依 Claude 是否跳出「這次 session 表現如何」回饋彈窗，判斷自己是否被分到降規模測試模型版本 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1vystw3/i_can_tell_when_im_being_ab_tested_with_nerfd/)，0 留言、無「週熱門」標記，score 不可信） | 單一社群回報（與同日 r/artificial 貼文方向一致，兩者互為呼應但均無具體量化數字或版本號）|
| 2026-08-26 | 「I miss the old Claude Code」：部落格作者比較年初與近期使用經驗，稱換用新模型後同任務要花更久時間才真正開始寫程式，直指「有大量 pre-work」；未點名具體模型版本 | Hacker News（[原文](https://alexkras.com/focus-is-the-main-feature-why-i-miss-the-old-claude-code/)，HN score 25，達收錄低門檻） | 本訊號群少見附真實 HN 分數的訊號（多數既有訊號 score 不可信）；未指名模型版本，無法歸入特定模型的品質爭議，僅可佐證「泛化變慢」現象持續 |
| 2026-08-28 | 「Is it even legal for Anthropic to nerf its models this hard?」：使用者質疑 Opus 5 與 Fable 5 在 Claude Code 中表現遜於預期，指控模型遭「削弱」 | Reddit r/ClaudeCode（[原文](https://www.reddit.com/r/ClaudeCode/comments/1w0t53b/is_it_even_legal_for_anthropic_to_nerf_its_models/)，無「週熱門」標記、score 不可信） | 單一社群回報（無具體量化數字或版本號），與 08-22／08-26「A/B 測試降 effort」主張同方向，僅計入現象延續 |

**懸置細節**
- ⟨Q-01⟩ ❓ **待查證**（標 2026-08-25｜查 Sonar、code quality benchmark）：HackerNoon 標題「Claude Opus 5 Code Quality: What Sonar's Benchmark Reveals」僅標題可用，程式碼品質分析工具 Sonar 對 Opus 5 生成程式碼的基準測試具體評測數字、樣本規模與測試方法論均未見報導；若查得具體數字，將是本訊號群目前唯一的量化／第三方工具評測證據（現有 10 則社群訊號均為主觀回報，無量化數字）。

**表格細節**
- **07-25 effort dial**：原標題「Opus 5's effort dial is not monotonic. Above "high", coding scores go down, and Anthropic's own migration guide says so.」——effort 旋鈕超過「high」後，編碼任務分數反而下降，Anthropic 官方 migration guide 自承此現象
- **07-26 二進位硬編碼**：討論指出 Claude Code 2.1.219／220 版編譯二進位內建僅針對 Opus 5 的兩行系統提示：除非使用者明確要求，否則不得呼叫 AgentTool、不得使用 workflows 或 deep-research；討論者認為此舉可能不成比例限制 Opus 5 能力發揮；已收錄於 [[topics/community-tech-discussions]]「討論指出 Claude Code 二進位對 Opus 5 存在硬編碼行為限制」，本頁不重複展開細節
- **08-22「spent the morning digging」**：作者稱查閱一手資料與討論串後認為，Anthropic 似乎正在 Claude Code 上 A/B 測試降低運算力度（effort）的版本，與同日「nerfd models」貼文方向一致；「查閱的一手資料」具體內容未見於摘要，無法覆核查證過程；與 07-25 官方 migration guide 自承 effort dial 非單調現象呼應，是本訊號群首次出現「懷疑正在被即時 A/B 測試」的直接主張，而非僅描述效能感受

**第三種假說的定位：** 上方「三種假說」表格圍繞 token 消耗展開（模型真退步／計費計量／context 工具配置），且截至 07-13 三者均無官方確認等級證據。本訊號群提供的是**不同維度**的證據——不是「消耗了多少 token」，而是「模型行為本身是否有可驗證的特性變化」。07-25 的 effort dial 非單調現象尤其關鍵：這是**目前全頁唯一一筆官方自己承認的行為特性變化**（其餘皆為社群主張或用戶主觀感受），性質上比既有三種假說的證據都更硬。

**（推論）這條線可能挑戰的既有共識：** [[topics/community-tech-discussions]] 記錄的社群共識「Claude 越用越笨幾乎都是 context 腐蝕而非模型退步」，隱含假設「模型本身沒有變」，變化只在使用者端的 context 管理。但 07-25 的官方確認顯示，至少在 effort 設定這個維度上，模型行為本身確有非直覺、非單調的特性——若使用者誤以為「調高 effort＝更好」而觸發此現象，表面上會呈現與 context rot 相同的「感覺變笨」症狀，但根因是模型設定使用不當，而非 context 管理問題，也不是模型「退步」。三者現階段仍難以區分：07-29～07-30 的三則主觀感受回報，無法排除是 context rot、也無法排除是 effort dial 誤用、更無法排除是單純的模型能力落差感（相對 Fable 5 跑分預期）。截至 08-19，樣本量已擴大但訊號強度未變（10 則訊號，其中 8 則為單一 Reddit 貼文、score 不可信；08-13「幾乎令人惱火」、08-14「近 3 個月大幅下滑」「升級 Pro→Max 後 session 時長變 3 倍」、08-19「過去兩週表現反覆不穩」、08-19「Claude is Losing Me」五則陸續加入，仍延續同一「泛化品質下滑」抱怨方向，未提供新的機制性證據），尚不足以推翻既有 context rot 共識，僅提示「並非所有『變笨』投訴都能簡化為 context 管理問題」，需持續觀察。08-22～08-26 新增三則訊號（累計 13 則）：兩則首度從「感覺變差」進展到「懷疑正在被即時 A/B 測試降低 effort」的直接主張（r/artificial 週熱門、r/ClaudeCode），性質上比既有主觀感受回報更接近可調查的具體機制假說，但仍缺乏可驗證測試方法或版本號佐證；另一則（HN score 25，真實分數）泛化抱怨新模型「開始寫程式前」耗時變長，未點名模型版本，僅佐證現象持續而非提供新機制證據。08-28 新增第 14 則訊號（r/ClaudeCode，無週熱門標記、score 不可信）：泛化質疑 Opus 5／Fable 5 遭「削弱」，未提供具體版本號或量化數字，方向與既有 A/B 測試懷疑一致，僅計入現象延續。

---

## 模型釘選／靜默降級 訊號群（2026-02 起）`[2026-08-09 查證新增]`

**這不是單一 bug，是「使用者宣告的模型選擇不被保證」在四種不同機制上重複發生**——缺乏鎖版能力（設計面）、picker 狀態不保持（實作面）、計費驅動降級（商業面）、能力靜默移除（產品面）。四個節點橫跨 2026-02 至 2026-07，彼此獨立、來源不同，構成同一主題的重複證據：

- **設計面缺口（2026-02-23，GitHub issue #27892，⛔ 官方以 not planned 關閉）**：`--model` 旗標僅接受 family 名稱（如 opus / sonnet），不接受版本 pin id；`.claude/settings.json` 亦無鎖版設定；使用者一旦被自動升版即無回退路徑。Anthropic 將此 issue 標記 not planned 並關閉，機制層面自始未規劃鎖版能力（[GitHub #27892](https://github.com/anthropics/claude-code/issues/27892)）。
- **實作面缺口（2026-04-10，GitHub issue #46221，已關閉為 #45978 重複）**：Opus 4.6 1M context 變體從 model picker 消失、被 Opus 4.6 200k 取代；預設在使用者未操作下靜默改為 Sonnet 4.6；進行中的 session 遭中途降級；即使手動選回 1M 變體，下次 `/model` 該選項仍會消失——選定狀態無法保持（[GitHub #46221](https://github.com/anthropics/claude-code/issues/46221)）。
- **商業面驅動（2026-07-25）**：Fable 5 計費壓力下，Opus 4.8 被靜默降級處理，細節見 [[entities/pricing]]。
- **產品面移除（2026-05-21）**：extended thinking 能力在未預告情況下自 Claude Code 移除，細節見 [[entities/claude-code]] 已知問題。

**未經佐證的具體宣稱（2026-08-04，單一 Reddit 來源，待觀察）：** r/ClaudeCode 貼文宣稱以實測記錄四種繞過模型釘選機制的方式，並稱 Sonnet 4.6 遭靜默移除；此貼文所指的「模型釘選不可靠／靜默降級」**現象**方向與上述四則已獨立佐證的節點一致，但貼文獨有的「4 measured bypass vectors」與「Sonnet 4.6 silently removed」**具體技術細節**仍僅有單一 Reddit 來源、無「週熱門」標記、近 14 天 news 查無第二來源覆核——佐證及於現象，不及於該貼文的具體量化宣稱，措辭上不可視為對其全部內容的背書（來源：[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1vf7uv5/model_pinning_is_completely_broken_in_claude_code/)）。

**對選型的影響：** 這一缺口讓成本估算的前提失效——[[topics/model-comparison]] 的實付成本換算假設你跑在你選的模型上，但上述 #46221 記錄的正是「1M context 變體從 picker 消失、選定狀態無法保持」。**在該頁做模型／context 的成本比較前，先確認釘選是否成立**（1M 這一項的完整脈絡見 [[topics/long-context-1m]]）；跨世代的成本差距（新舊 tokenizer 同文字差約 30%）大於多數人願意承受的靜默切換誤差。

**目前定位：** 四種機制橫跨六個月，均指向「使用者宣告的模型選擇不被保證兌現」這一系統性缺口，而非單次意外。08-04 的 Reddit 貼文延續同一現象方向；❓ **待查證**（標 2026-08-10｜查 bypass vectors、silently removed｜複 2026-09-13）｜**貼文具體量化宣稱**（2026-08-04 單一 Reddit 來源）：已掃日報至 2026-09-02 無後續；官方頁面未查證；本頁僅計入現象層級的第五個獨立訊號，不採計其具體技術細節。

---

## 技術彙整

- **自訂編排路由失效（Reddit r/ClaudeAI，2026-06-26）**：用戶反映相同的自訂 orchestration 設定，OpenCode 能穩定路由到自訂 providers 的 agents，但 Claude Code 無法可靠執行相同路由；問題未見官方說明；此為工具行為不一致問題，非模型能力退步，但影響依賴自訂 agent 編排的工作流（來源：[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ug7sz4/claude_code_ignores_my_custom_orchestration_and/)）
- **LLM 無障礙偏差（Claude Code issue #56079，2026-06-18）**：即使 CLAUDE.md 明確要求 WCAG 2.2 AA，Claude Code 仍將無障礙修復視為「可選取捨」而非需求；模型自解釋：在追求「coding speed」時 accessibility 被降為次要優先；這是「values problem」而非知識問題，與人類工程師的相同偏見如出一轍（Aaron Gustafson blog；2026-06-20 仍在追蹤中）
- **社群證據基礎設施化（forensic archive，2026-08-12）**：一名開發者將數月來蒐集的 Claude Code bug、模型退化、設定異常整理成公開存檔，並附上 HackerOne 回報紀錄（[原文](https://www.reddit.com/r/ClaudeCode/comments/1vm9igt/i_made_a_forensic_archive_for_claude_failures/)，Reddit r/ClaudeCode，08-12 09:44 UTC，單一社群來源、無「週熱門」標記，score 不可信）。意義不只是「又一則抱怨」：這是社群第一次把零散的品質下滑貼文**升級為系統化、可被引用的證據基礎設施**，與本頁「Token 消耗異常訊號群」在 07-13 已定調的「訊號密度已達結構性未解問題」是同一敘事的下一步——先前只是密度夠高，現在開始有人主動蒐集、結構化、公開化以供他人引用查證；與 2026-04-25 出現的 CC-Canary（自動化效能漂移偵測工具）互為呼應，一為自動化偵測、一為人工彙整存證，顯示社群對「品質下滑」的應對已從個別抱怨走向工具化與存證化並行的兩條路徑。
- **Session log 路徑**：`~/.claude/projects/` 存放 JSONL 格式的 session log，CC-Canary 透過此路徑讀取歷史資料進行效能比對
- **CC-Canary 判定等級**：`HOLDING`（穩定）／`SUSPECTED REGRESSION`（疑似退步）／`CONFIRMED REGRESSION`（確認退步）
- **Stop hooks 失效**：Claude 4.7 起無視自訂 stop hooks，與整體效能退步為獨立問題，機制層面尚未公開說明
- **靜默模型切換（Silent Model Switching）**：開發者記錄 36 天使用數據，發現模型有時在無明確通知的情況下靜默切換，用戶無法確知實際使用的模型版本；不同模型間效率差距高達 11.5 倍，靜默切換可能導致效率和成本的非預期變化；與 2026-04-27「版本管理不透明」（執行 claude update 靜默撤版）議題相呼應，顯示 Anthropic 在模型與版本透明度上的系統性不足；此現象已於 08-09 查證取得跨機制獨立佐證，詳見「模型釘選／靜默降級 訊號群」子區塊
- **Anthropic 說明原因**：engineering missteps（工程疏失），非刻意的模型行為調整（非 RLHF 過度修正）

---

## 目前結論

- ✅ Anthropic 已承認問題為工程疏失
- ✅ Boris Cherny 在 4/23 發布事後報告，承諾 50+ 修復項目
- 🔍 社群開發者正逐一驗證 50+ 修復是否落實（2026-05-03 開始，最終結果待觀察）
- 🔴 Stop hooks 失效為獨立問題，[[entities/claude-code]] 已知問題列表確認截至 2026-07-11 仍未修復（非僅社群指控）
- ⚠️ 信任侵蝕已從「效能品質」擴大至「定價透明度、計量準確性、基礎設施可靠性」，形成結構性問題
- 🔴 「token 消耗異常」訊號群自 06-27 延燒至 07-13（共 17 天，九個獨立來源），密度已達「結構性未解問題」，尚無法判定模型真退步 vs 計費/計量問題 vs context/工具配置問題，Anthropic 未回應；沉寂 43 天後 08-25 再現同方向單一貼文質疑，僅計入現象延續
- 🟡 Opus 5 上線後（07-25～08-26）浮現第三條分析線「模型行為特性本身」，首見官方確認等級證據（effort dial 非單調），（推論）可能局部挑戰既有「多為 context rot」共識，惟樣本量小（13 則，多數單一 Reddit 貼文），08-14～08-19 再添四則同方向抱怨但無新機制性證據；08-22～08-26 首度出現兩則獨立來源直接主張「懷疑正在被即時 A/B 測試降低 effort」（而非僅描述效能變差感受），與 07-25 官方 effort dial 證據呼應但仍缺乏可驗證測試方法或版本號佐證，尚待更多獨立來源覆核
- 📊 CC-Canary 可作為持續監測工具；2026-08-12 起社群另闢人工彙整路線（forensic archive），與自動化偵測並行，顯示品質下滑證據的蒐集正逐步基礎設施化

---

## 影響範圍

- 依賴 Claude Code 進行 agentic 自動化的開發者
- 使用自訂 hooks 注入確定性邏輯的工作流程（stop hooks 問題）
- 付費用戶的訂閱降級潮（見 [[entities/pricing]]）

---

## 相關實體

- [[entities/claude-code]]
- [[entities/opus-4-7]]
- [[entities/opus-4-8]]
- [[entities/opus-5]]
- [[entities/pricing]]
- [[topics/model-comparison]]

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

### 2026-08

#### 2026-08-28
- **「Is it even legal for Anthropic to nerf its models this hard?」**：r/ClaudeCode 貼文質疑 Opus 5、Fable 5 在 Claude Code 中表現遜於預期，指控模型遭「削弱」；無「週熱門」標記、score 不可信，屬「Opus 5 上線後品質感知訊號群」第 14 則訊號，方向與 08-22／08-26「懷疑正在被 A/B 測試降 effort」一致，僅計入現象延續（來源：[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1w0t53b/is_it_even_legal_for_anthropic_to_nerf_its_models/)）

#### 2026-08-26
- **「Opus 5 上線後品質感知訊號群」首度出現「懷疑正在被即時 A/B 測試」直接主張**：r/ClaudeCode 貼文「I can tell when I'm being A/B tested with nerfd models」稱可依 Claude 是否跳出「這次 session 表現如何」回饋彈窗判斷自己是否被分到降規模測試模型；同日補記 08-22 r/artificial 週熱門貼文「I spent the morning digging into Anthropic so I could write it up properly」，作者稱查閱一手資料後認為 Anthropic 似乎正在 Claude Code 上 A/B 測試降低 effort 的版本，兩者方向一致；均無具體量化數字或版本號，但與 07-25 官方 migration guide 自承 effort dial 非單調現象呼應，是本訊號群首次從「效能感受變差」進展到「懷疑正在被主動測試」的主張（來源：[Reddit「nerfd models」](https://www.reddit.com/r/ClaudeCode/comments/1vystw3/i_can_tell_when_im_being_ab_tested_with_nerfd/)、[Reddit「digging into Anthropic」](https://www.reddit.com/r/artificial/comments/1vvjmmo/i_spent_the_morning_digging_into_anthropic_so_i/)）
- **「I miss the old Claude Code」：泛化「新模型變慢」抱怨，附真實 HN 分數**：部落格作者比較年初與近期使用經驗，稱換用新模型後同任務要花更久時間才真正開始寫程式；HN score 25（達收錄低門檻，本訊號群少見的真實分數），惟未點名具體模型版本，僅可佐證「泛化變慢」現象持續，不歸入特定模型爭議（來源：[alexkras.com](https://alexkras.com/focus-is-the-main-feature-why-i-miss-the-old-claude-code/)）

#### 2026-08-25
- **「Token 消耗異常訊號群」沉寂 43 天後再現**：r/ClaudeCode 貼文「Is Claude Code intentionally burning more tokens now?」質疑近幾個月來 Claude Code 是否比過去消耗更多 token 才能完成相同任務；0 留言、無「週熱門」標記，score 不可信，屬「Token 消耗異常訊號群」自 07-13 以來第十則訊號，僅計入現象延續，不提供新機制性證據（來源：[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1vxw3fi/is_claude_code_intentionally_burning_more_tokens/)）

#### 2026-08-20（週熱門重浮上，原發時間較早）
- **「Claude is Losing Me After Being Heavy User Since Release」**：r/ClaudeAI 重度使用者發文表達對 Claude 逐漸失望的心情，具體抱怨內容未見於本次摘要；週熱門標記，達收錄低門檻，屬「Opus 5 上線後品質感知訊號群」第十則訊號，僅計入現象延續（來源：[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vqsas9/claude_is_losing_me_after_being_heavy_user_since/)）

#### 2026-08-19
- **「過去兩週表現反覆不穩」**：r/ClaudeCode 貼文「I've never felt Claude been degraded for so long before」，使用者反映過去兩週 Claude 表現反覆不穩、多半比平常差，詢問是否為運算資源問題；0 留言、無「週熱門」標記，score 不可信，無具體量化數字或版本號，屬「Opus 5 上線後品質感知訊號群」第九則訊號，僅計入現象延續（來源：[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1vshkrf/)）

#### 2026-08-13（補記，08-15 日報收錄）
- **「幾乎令人惱火」：已依官方建議調整仍無法馴服 Opus 5**：r/ClaudeAI 貼文「Opus 5 is actually almost rage-inducing to use.」，使用者稱已依官方建議調整、試過各種全域 CLAUDE.md 設定，仍無法讓 Opus 5 行為符合期待；週熱門標記，達收錄低門檻，但無具體量化數字，屬「Opus 5 上線後品質感知訊號群」第八則訊號，僅計入現象延續（來源：[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vn8ml6/opus_5_is_actually_almost_rageinducing_to_use/)）

#### 2026-08-14
- **「泛化品質下滑」投訴延續，兩則新增均為單一 Reddit 來源**：r/ClaudeCode 同日兩則獨立貼文——「Serious question regarding CC quality」指近 3 個月「大幅」（MASSIVE）品質下滑、不限特定模型、內文提及 Opus 5 尤其令人失望（原文截斷）；「Claude Code got slower since I upgraded from Pro to Max」反映升級後 session 時長變為 3 倍、任務難度與規模未變。兩者皆無「週熱門」標記、score 不可信、無跨平台佐證，屬「Opus 5 上線後品質感知訊號群」第六、七則訊號，僅計入現象延續，未提供新的機制性證據（來源：[Reddit「CC quality」](https://www.reddit.com/r/ClaudeCode/comments/1vo3ygk/serious_question_regarding_cc_quality_no_hate_or/)、[Reddit「got slower」](https://www.reddit.com/r/ClaudeCode/comments/1vo3y1g/claude_code_got_slower_since_i_upgraded_from_pro/)）

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
- **Opus 5 effort dial 非單調，官方 migration guide 自承**：週熱門討論指出 effort 旋鈕超過「high」後編碼分數反而下降，Anthropic 官方 migration guide 本身即載明此現象；為「Opus 5 上線後品質感知訊號群」中唯一官方確認等級證據，詳見「Opus 5 上線後品質感知訊號群」子區塊（來源：[Reddit r/artificial · 週熱門](https://www.reddit.com/r/artificial/comments/1v60pga/opus_5s_effort_dial_is_not_monotonic_above_high/)）

#### 2026-07-09
- **Max 20x 額度異常比例回報**：Reddit 用戶質疑 Max 20x 方案中單一 session 27% 的時間即消耗掉整週額度 7%，與同期 GitHub #38335 額度異常回報呼應（該 issue 累積留言數同日增至 791 則）；訊號鏈持續延燒（來源：[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1urqgqx/claude_max_20x_why_did_27_of_one_session_consume/)）

#### 2026-07-08
- **訊號群補上具體技術機制與兩則異常比例回報**：Reddit「cache 命中率下降 20% 導致 agent 帳單翻倍」首度為「計費/計量問題」假說提供技術描述；同日另有「Max 20x 方案週額度不到一天用盡」回報；加上 GitHub issue #41506 回報 Max 方案（$100/月）token 消耗量自 3 月底起在未變更設定下增加約 3-5 倍（累積 54 則留言、29 個讚）；三者與 07-03 的 #38335、07-01 的兩則社群訊號方向一致，訊號密度使定調上調為「結構性未解問題」；官方尚未回應（來源：[GitHub Issues #41506](https://github.com/anthropics/claude-code/issues/41506)、[Reddit cache 命中率](https://www.reddit.com/r/ClaudeCode/comments/1uqsah2/cache_hit_rate_dropping_by_20_doubles_your_agents_bills/)、[Reddit Max 20x 週額度](https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/claude_max_20x_weekly_limit_exhausted_in_less/)）

#### 2026-07-04
- **Plan mode 逾時自動代答 + 整體變慢投訴延續**：Reddit r/ClaudeCode 用戶（source_count 2）反映 plan mode 逾時後自動選擇非預期選項，並主觀感受近期回應變慢、能力下降；與 07-02 已記錄的 AskUserQuestion 60 秒逾時自動代答爭議（見 [[topics/community-tech-discussions]]）屬同一「逾時代答破壞決策體驗」機制的延續投訴，「變慢/能力下降」部分仍屬主觀感受，無 benchmark 或版本號佐證（來源：[Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1und5g7/claude_code_cli_is_getting_harder_to_use_plus/)）

#### 2026-07-03
- **Token 消耗異常訊號群成形**：GitHub issue #16856（2.1.1 版 token 消耗達 4 倍以上）與 issue #38335（Max 方案額度自 3/23 起異常消耗，大量留言）同日浮上，與 07-01 的兩則社群訊號（HN「5x 更貴」、$62,021 具名案例）共同構成四個獨立來源的成本異常訊號群；詳見「Token 消耗異常訊號群」子區塊；官方尚未回應（GitHub Issues）

#### 2026-07-01
- **Claude Code 成本暴漲討論爆發**：Vincent Schmalbach 發文「Claude Code Just Got 5x More Expensive」登上 HN（score 53），同日 Reddit 出現獨立開發者單月燒 $62,021 token 的具名案例；社群懷疑與模型切換或計費方式變更有關；詳見 [[topics/community-tech-discussions]] 對應條目

### 2026-06

#### 2026-06-26

- **自訂 Agent 編排路由失效**：用戶反映 Claude Code 無法可靠路由到自訂 orchestration 中的自訂 providers agents，OpenCode 同設定可穩定執行；問題指向 Claude Code 編排機制的行為不一致性，非模型能力問題；官方尚未回應（Reddit r/ClaudeAI）

#### 2026-06-18

- **LLM 無障礙偏差（Claude Code issue #56079）**：開發者 Aaron Gustafson 揭露：在 CLAUDE.md 已明確指定 WCAG 2.2 AA 規格的專案中，Claude Code 仍將無障礙修復視為可選取捨。模型自述原因是在追求「coding speed」時 accessibility 被降級；Aaron Gustafson 評論此為「值觀優先序偏差」而非知識不足。此偏差複製了人類工程師「稍後再修無障礙」的習慣，AI 未改善既有偏見（2026-06-20 持續追蹤中）

### 2026-05

#### 2026-05-29

- **Opus 4.7 升版前一週效能下降（MarginLab SWE-bench-Pro 追蹤）**：MarginLab 每日對 Claude Code 執行 SWE-bench-Pro 追蹤，發現 Opus 4.7 在 [[entities/opus-4-8|Opus 4.8]] 發布前**連續五天**呈現統計顯著的 pass rate 下降，發布後立即恢復。此為「靜默的日常效能變化」模式的又一次文件化案例——launch benchmark 只呈現發布當下數字，無法捕捉前後的漸進變化（來源：https://marginlab.ai/blog/claude-code-degraded-before-opus-4-8/）
- **thinking blocks 400 錯誤**：Opus 4.8 升版後，多名用戶回報 `API Error: 400 thinking or redacted_thinking blocks cannot be modified` 錯誤；v2.1.156 已修復，workaround 為 `/exit` 後 resume session（見 [[entities/claude-code]]）
- **4.8 行為退步投訴**：部分用戶反映 Opus 4.8 比 4.7 更差——obsessive tool use，傾向以 "pecl scripts" 處理簡單文件操作（來源：Reddit r/ClaudeAI）

#### 2026-05-21
- **Opus 退化三週結構化記錄**：用戶以三週結構化 session log（含 metacognitive 欄位）記錄 Opus 4.7 / Sonnet 4.6 在複雜本地 AI 記憶體專案（Qdrant + Neo4j + Graphiti）上的持續失敗，並記錄到競品模型成功捕捉 Claude 遺漏的錯誤；是目前 r/ClaudeAI 最具文件支撐的退化投訴案例，Anthropic 未回應

#### 2026-05-09
- **靜默模型切換（11.5 倍效率差距）**：開發者持續 36 天記錄 Claude Code 使用數據，量化出不同模型間 11.5 倍的效率差距，並觀察到模型有時靜默切換（silent model switching）且無明確通知；對有成本意識的長期用戶是重要的監控警示，建議搭配 Throttle Meter 或 session log 監控實際模型使用情況

#### 2026-05-05
- **Opus 4.7 退步討論再升溫**：dev.to 文章《Claude Opus 4.7 Is a Regression》引發討論，部分開發者聲稱 Opus 4.7 在編碼任務中不如 4.6，已主動回退舊版；與 4/30 的「後設化退步」批評相互呼應；見 [[entities/opus-4-7]]

#### 2026-05-03
- **[社群問責] 4/23 事後報告 50+ 修復社群獨立驗證**：社群開發者主動逐一驗證 Claude Code 負責人 Boris Cherny 在 4/23 發布的事後報告中承諾的超過 50 項修復，提供獨立於官方的實測評估。此為少見的社群對官方承諾進行系統性問責的行動，驗證結果正逐步揭露哪些修復已落實、哪些仍有差距。

### 2026-04

#### 2026-04-30
- **Opus 4.7「後設化」退步**：重度 Max 20x 用戶直言 Opus 4.7 嚴重退步，過度「後設化」無法直接回答問題；當時另引學術研究（arxiv 2604.24827）稱 Opus 4.7 參數約 4T、少於 Opus 4.6 的 5.3T，**該組數字經 2026-08-26 查證論文原文後不成立**（論文未給 Opus 4.7 估算，見 [[entities/opus-4-7]]），本則僅保留「社群失望情緒累積」此一社群訊號
- **Claude Projects 對話消失**：重度使用者三度遭遇整天的創作對話無故消失，無法搜尋找回，呼籲改善 Projects 資料保留機制

#### 2026-04-29
- **Speed Bumps 頻率增加**：多位長期使用者回報 Claude Code 本週起明顯增加中途暫停詢問的頻率，即使簡單任務也頻繁打斷工作流程，社群猜測與系統層級的行為調整有關，但目前無官方說明
- **Max 方案 API 錯誤**：高價訂閱用戶遭遇內部 API 錯誤，Anthropic 支援 AI 卻持續建議排查 VPN 等不相關問題，無法識別實際服務故障，引發對支援品質的強烈批評

#### 2026-04-28
- **「Anthropic 安全定義過窄」批評**：Jonathan Nen 發文指出 Anthropic 的安全關注過度聚焦在模型行為，忽視產品可靠性、定價策略與溝通透明度；以四月 Claude Code 品質問題與 Pro 用戶 Opus 存取爭議為佐證，文章在技術社群引發強烈共鳴，HN 登上精選話題。
- **信任侵蝕進入結構性階段**：定價不透明（Opus 圍牆事件）+ 使用量計量異常 + 基礎設施可靠性問題（Auto Compact 失效、Prompt Cache Race Condition）在同日密集出現，社群對平台可靠性的質疑已超出「效能退步」的原始邊界，擴大為對 Anthropic 整體產品治理的不信任。

#### 2026-04-25
- 社群推出 **CC-Canary** 工具，透過讀取 `~/.claude/projects/` JSONL session log 自動偵測效能漂移，提供 HOLDING / SUSPECTED REGRESSION / CONFIRMED REGRESSION 等判定等級（工具目錄見 [[topics/community-tech-tools]]）

#### 2026-04-24
- **Anthropic 正式公開說明**：承認工程疏失導致效能退步（Fortune、XDA 等媒體同步報導）
- **Stop hooks 失效問題獨立回報**：Claude 4.7 開始無視自訂 stop hooks，屬獨立的行為退步（regression），與效能下滑為不同問題；截至 2026-07-11，[[entities/claude-code]] 已知問題仍將此列為 🔴 未修復（非僅指控）
- HN 討論串累積近 80 則留言

#### 2026-04（早期）
- 大量開發者在 Reddit r/ClaudeAI、Hacker News 回報效能下滑
- 社群質疑是否為刻意調整（RLHF 過度修正、成本考量等），Anthropic 長期未正式回應

### 2026-03

#### 2026-03（推測）
- 效能退步開始，早期用戶開始察覺異常
