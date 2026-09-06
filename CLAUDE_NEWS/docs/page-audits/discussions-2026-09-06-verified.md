# 主編官方查證 — topics/community-tech-discussions（2026-09-06）

行號＝檔案原始行號（含 frontmatter）。本頁記的是社群「怎麼吵」，官方查證只對兩種句子：結論層把社群說法寫成事實的（L44–52），以及本週熱點把官方動作當標題的（L54–67）。

## 一、結論層與本週熱點的事實句對官方

| 頁面句（行） | 官方現況（逐字＋連結＋日期） | 判定 |
|---|---|---|
| L58「Claude 5 世代 context engineering 新規則（2026-07-26，HN 393）：Anthropic 官方揭露…移除逾 80% 的 Claude Code 系統提示詞」 | claude.com blog〈The new rules of context engineering for Claude 5 generation models〉，**2026-07-24**，Thariq Shihipar：「We removed over 80% of Claude Code's system prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our coding evaluations」；六條新規則：rules→judgement、examples→design interfaces、upfront→progressive disclosure、repeat→simple tool descriptions、CLAUDE.md memory→auto-memory、simple specs→rich references | ✅ 事實對；**日期 07-26 是 HN 討論日，官方發文 07-24**，頁面該分開寫；這則是官方一手內容（`wiki-ingest.md` 分流鐵則：官方工作流模式歸社群類，出處標官方） |
| L59「Extended Thinking 透明度揭露（06-23，HN 312）：thinking blocks 只有加密簽名、API 僅回摘要、完整輸出需企業協議——『審計軌跡』技術上無法自行核驗」 | platform 文件 thinking：「No `display` setting returns the raw chain of thought」；「Summarization is processed by a different model from the one you target」；`signature`＝「an encrypted copy of the full reasoning that you pass back unchanged」；「In rare cases where you need access to full thinking output, contact Anthropic sales」；Fable 5.1／5、Opus 5、Sonnet 5 等 `display` 預設 `"omitted"`（thinking 欄位空、只回 signature）；Fable 5.1／5 對誘出內部推理的請求可回 `stop_details.category: "reasoning_extraction"` 拒絕 | ✅ 三個機制句全對；**現況更進一步**：5 世代預設連摘要都不回（omitted），且 Fable 對「把推理寫進回答」會拒絕——頁面停在 06-23 的「僅回摘要」，比現況寬 |
| L49「安全假設需要重設：90% AI 生成程式碼漏洞」（無來源無日期） | 外部研究無「90%」：Veracode 2026 春季報告 **45%** 含 OWASP Top 10 漏洞（Java 72%）；OX Security **62%** 含設計缺陷或已知漏洞；CSA 研究：AI 輔助開發者 commit 3–4 倍、安全發現 **10 倍**；Georgia Tech Vibe Security Radar 74 CVE 可溯 AI 工具（2026-03）；iOS 198 款 app 98.9% 設定錯誤（範圍不同） | **撐不起**：全庫查不到 90% 的家（唯一可能是 iOS app 那個 98.9% 被四捨五入，但那是設定錯誤不是程式碼漏洞）。結論句改寫為「45–62% 含漏洞（Veracode／OX 2026）、安全發現 10 倍（CSA）」或降為（推論）並標待查 |
| L49「Auto 模式為提示詞層安全」 | code.claude.com permission-modes：「a second model, the classifier, reviews actions instead of you」；「blocking anything that escalates beyond your request, targets unrecognized infrastructure, or appears driven by hostile content Claude read」；boundaries「are not stored as rules. The classifier re-reads them from the transcript on each check, so a boundary can be lost if context compaction removes the message」；「For a hard guarantee, add a deny rule instead」；連續 3 次或總計 20 次 block 即退回提示 | ⚠️ 「提示詞層安全」是社群措辭，官方說法是**分類器模型審每個動作**，且官方自己明寫對話邊界可因壓縮遺失、硬保證要用 deny 規則——頁面的批評方向對、機制描述過簡；另 Pro／Max／Team 預設模式已是 auto（頁面未載） |
| L47／L62「Skill Atrophy…形成社群共識」「2026-06-10+」 | Anthropic research〈How AI assistance impacts the formation of coding skills〉（**2026-01**，RCT）：AI 組在剛用過概念的測驗「scored 17% lower…nearly two letter grades」；速度略快但未達顯著；「how someone used AI influenced how much information they retained」 | ⚠️ 本頁把它寫成社群共識，卻沒引 Anthropic 自己 01 月的 RCT——那是這條線唯一的一手量化證據，且結論比社群溫和（用法決定退化程度）。L95 節該補這一則 |
| L67／L113／L192「Loop Engineering 哲學：Boris Cherny 名言…PR review、測試、push 抽象為 loop」 | 原話（X／40 分鐘分享，二手轉述）：「I don't prompt Claude anymore. I have loops running that prompt Claude… My job is to write loops」；「Going from agents to loops is as big a jump as going from code to agents」；實例 `/loop 5m /babysit`、`/loop 30m /slack-feedback`、`/loop /post-merge-sweeper`、`/loop 1h /pr-pruner`；另 X 2026：Code Review 功能「Code output per Anthropic engineer is up 200% this year and reviews were the bottleneck」 | ✅ 名言方向對；**頁面沒有原句、沒有 `/loop` 指令對應**——`/loop` 是 Claude Code 內建指令（本站自己在用），哲學句該對到產品原語；X 一手抓不到，標二手 |
| L201／L252「HTML vs Markdown 輸出格式辯論（05-09，🔥🔥🔥🔥🔥 🌊延燒）」 | 無官方立場可查（純社群辯論）；`wiki-ingest-features.md` 准入表把「HTML 輸出背書」列為純策略表態不進 radar | — 官方無事可對；本題的查證是**頁內**：首見 05-09、四個月仍標 🌊延燒，保留規則說延燒永久保留，但「延燒」語意是「3 天以上持續」，四個月無新節點還標延燒＝假現在式（給健檢卡／設計者） |

## 二、給設計者

1. **本週熱點十則八則是 06 月**，且 L58 那則是官方發文（07-24）不是社群訊號——「本週」這個節名在騙人，而它是 index L102 鉤子送讀者來的第一眼。
2. **結論層五條裡兩條的數字撐不起**（90%、「社群共識」無一手），一條停在舊現況（thinking 僅回摘要→現在預設不回）。結論層若改成「哪幾場爭論有結論、哪幾場還在吵、證據硬度」的表，每列要有查證日與一手／二手欄。
3. **官方一手在這頁是稀缺品**：context engineering 新規則（07-24）、skill 形成 RCT（01 月）、thinking 文件、auto mode 文件——四份都能給對應爭論一個「官方怎麼說」欄，是本頁最缺的東西。
4. 蒸餾：2026-05（L984–1275）與 2026-06（L607–983）皆合格；HTML vs MD（05-09）、Skill Atrophy（06-10）、Extended Thinking（06-23）都住在這兩個月，搬走前熱門討論表「衍生」欄與本週熱點的指向要先改。
