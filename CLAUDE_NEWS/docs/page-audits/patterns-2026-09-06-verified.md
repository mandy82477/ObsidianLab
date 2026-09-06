# 主編官方查證 — topics/community-tech-patterns（2026-09-06）

行號＝檔案原始行號（含 frontmatter）。本頁是社群產物，官方查證的對象不是「社群說了什麼」，而是頁面把社群模式對到哪個官方功能時，那個官方功能**現在**長什麼樣（reader-notes L18／L45：學術術語 ↔ Claude Code 機制 ↔ 社群配置）。

## 一、官方 subagent 文件（[code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)，無標示更新日）

| 學術詞／頁面用語 | 官方現況（逐字） | 對頁面的意義 |
|---|---|---|
| **誰負責拆分（decomposition）** | 「Claude automatically delegates tasks based on the task description in your request, the `description` field in subagent configurations, and current context」——**主 agent 決定何時委派**，使用者只能用 description 裡的「use proactively」鼓勵 | 頁面「誰負責拆分：human／強 planner」表要對上這句：官方預設是**模型拆**，人只設邊界 |
| **巢狀深度** | 預設可到主對話下**三層**；到深度上限時「Claude Code withholds the `Agent` tool from every subagent except a fork」；`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` 關閉 | 學術對照表「階層式 orchestration」那格有官方對應（2.1.217 關→2.1.219 開到 3，見 P2 verified 第六節） |
| **fork（繼承脈絡的子代理）** | 「inherits the entire conversation so far instead of starting fresh」；「Forks skip both filters and receive the main conversation's exact tool pool」；`/subtask` 起（v2.1.212+） | 社群「Speculative Parallelism／答案塌縮」那類模式的官方原語 |
| **背景執行預設** | 「Where fork mode is on … Claude Code runs the subagent in the background, forks and non-fork subagents alike」；fork mode 互動 session 預設 on；背景子代理工具集較小、權限提示全浮到主 session | 對讀者 Q1「跟兩個月前差在哪」的官方答案之一（2.1.232 起） |
| **agent 間通訊原語** | 子代理收到 system reminder 列出 `main` 與所有具名 agent，皆為 `SendMessage` 的合法 `to`（v2.1.206+）；「Claude uses the `SendMessage` tool with the agent's ID or name as the `to` field to resume it」 | 學術「communication primitive」那欄：官方已有點對點訊息＋續用（resume），不只是 return value |
| **agent teams／cross-session** | 文件分兩頁：agent teams（「a coordinated team of sessions Claude spawns and supervises」）與 cross-session messaging（「separate sessions that pass messages to each other」） | 見第二節 |

## 二、agent teams 與 cross-session messaging（[agent-teams](https://code.claude.com/docs/en/agent-teams)、[cross-session-messaging](https://code.claude.com/docs/en/cross-session-messaging)）

| 學術詞／頁面用語 | 官方現況（逐字） | 對頁面的意義 |
|---|---|---|
| **agent teams 的狀態** | 「Agent teams are experimental and disabled by default」，需 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`；「This page describes agent teams as of v2.1.178」；`TeamCreate`／`TeamDelete` 「Both tools no longer exist」 | 頁面若把 agent teams 當成熟功能或還寫 TeamCreate，就是過期；社群 orchestrator 模式對照這裡要標「實驗性」 |
| **subagent vs team 的官方分界** | 「Subagents report results back to the main agent. In agent teams, teammates share a task list, claim work, and communicate directly with each other」；Token cost：subagent「Lower」、team「Higher: each teammate is a separate Claude instance」 | 學術「orchestrator-worker vs peer collaboration」對照的官方版本；頁面「選型」欄可直接引用 |
| **誰拆任務（team）** | 「The lead breaks work into tasks and assigns them to teammates automatically」；自領：「after finishing a task, a teammate picks up the next unassigned, unblocked task on its own」；claim 用 file locking | 「誰負責拆分」表要加一列：team 模式＝lead 拆＋teammate 自領 |
| **teammate 脈絡** | 「The lead's conversation history does not carry over」；載入 CLAUDE.md、MCP、skills＋spawn prompt | 與 fork（繼承全脈絡）形成官方的兩極，社群「context handoff」模式落在中間 |
| **團隊規模建議** | 「Start with 3-5 teammates」；「Three focused teammates often outperform five scattered ones」；「5-6 tasks per teammate」 | 社群「幾個 agent 最好」的討論有官方基準可比 |
| **官方限制** | 「No nested teams」、「One team per session」、「Lead is fixed」、in-process teammate 不能背景 subagent、`/resume` 不還原 teammate | 學術「階層式多層 orchestration」在 team 層官方明講做不到，只能靠 subagent 巢狀（≤3 層） |
| **cross-session messaging** | 「Claude uses two tools … `ListAgents` to discover … and `SendMessage` to deliver」；v2.1.224+（Windows 2.1.234+），「on with nothing to enable」；「A message is a piece of text … never the sender's conversation history or files」；送到他機經 Anthropic 伺服器、同機走 socket | 社群「多 session 協作／worktree 並行」模式的官方原語；訊息不能代批權限（「It can't approve anything」） |
| **通訊安全邊界** | 「Claude Code tells the receiving agent the message came from another Claude session, not from you」；auto mode 的 classifier 先審再送 | 社群模式若讓 agent 互批任務，官方架構明確擋掉 |

## 三、給設計者

1. 學術對照表 3 列、「誰負責拆分」表 4 列都是 static 且無官方欄的查證日——官方 subagent 文件已能填「官方對應／官方預設」欄，這是本頁最缺的一手。
2. 技術彙整 2026-05／06 分組已空（早已蒸餾）、07 月 50 條距今 2 個月未達門檻——本波**無合格蒸餾時段**，厚度要靠結論層不靠搬家。
3. Q1「跟兩個月前差在哪」官方側的答案就在 changelog 2.1.212→2.1.261（fork／subtask、背景預設、巢狀深度、SendMessage 名冊、cross-session 2.1.224）——頁面若只記社群工具名，會漏掉「官方把哪些社群模式收編成原語」這一層，而那正是 official-community-gap 頁的題，兩頁分工要在此劃線。
4. 官方自己給了三層階梯：subagent（結果回主 agent）→ agent teams（共享任務表、互傳訊息、實驗性）→ cross-session（獨立 session 傳純文字）。頁面的模式分類若能對到這三層，讀者選型就有官方座標；目前頁面的分類軸是社群自創的。
