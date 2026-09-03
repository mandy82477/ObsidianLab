---
page: "topics/skill-interest-watch"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-09-02"
last_news_update: "2026-09-02"
update_freq: "🗓️ 每日快照（機器產出；「本週竄升」以七日星數差計）"
status_main: "ongoing"
days_since_news: 1
inbound_links: 2
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 興趣類別 skill 榜

**狀態：** ongoing
**開始日期：** 2026-09-03
**領域：** 🌐 社群
**更新頻率：** 🗓️ 每日快照（機器產出；「本週竄升」以七日星數差計）
**最後更新：** 2026-09-02
**最後新聞更新：** 2026-09-02

> **本頁是什麼**（2026-09-02 快照）
> 針對讀者指定的類別（8 類可用 GitHub 辨識），每天到 GitHub 問「這一類現在誰最熱、本週誰竄上來」。本頁是**感測層**（機器、規模、零判斷）；**判斷層**在 [[topics/community-tech-tools]]——該裝哪個、證據多強、為什麼。每類末的「本庫判斷 →」是唯一的橋（單向：榜連 tools，tools 不抄榜）。**星數是規模不是品質**。

---

## 怎麼讀

| 欄 | 意思 |
|---|---|
| 目前前 5 | 該類別 query 命中的 repo 依星數排序，星數為快照當日值 |
| 本週竄升 | 七日內星數增量 ≥ 200 者，依增量排序；資料來自各發現窗每日記錄的星史檔 |
| 📰 | 本庫日報或清倉帳本已報導過 |
| 🧭 | 本庫已有判斷——該 repo 出現在 [[topics/community-tech-tools]]（決策表／速查／目錄） |

> ⚠️ 星史檔目前只涵蓋 0 天（需 7 天），「本週竄升」欄尚在冷啟動，本週先只看「目前前 5」。

## A. 開發實務（按流程階段，對應 [[topics/coding-workflow-guide]]）

### 專案設定／CLAUDE.md 生成（對應 [[topics/coding-workflow-guide]] 第 1 段）

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) 🧭 📰 | 209,607 | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's ob |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) 📰 | 12,552 | All parts of Claude Code's system prompt, 27 builtin tool descriptions, sub agent prompts  |
| [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | 6,006 | One CLAUDE.md file. Keeps Claude responses terse. Reduces output verbosity on heavy workfl |
| [gadievron/raptor](https://github.com/gadievron/raptor) | 3,696 | Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By  |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | 2,615 | Shared starter template configuration and CLAUDE.md memory bank system for Claude Code |

本庫判斷 → 見 [[topics/community-tech-tools]]（🧭 者已有證據等級與一句為什麼）

### codebase 探索與理解（對應 [[topics/coding-workflow-guide]] 第 2a 段）

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) 🧭 📰 | 113,898 | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowled |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) 🧭 📰 | 81,328 | Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) 🧭 📰 | 69,265 | Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemi |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | 46,886 | GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowl |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 41,868 | High-performance code intelligence MCP server. Indexes codebases into a persistent knowled |

本庫判斷 → 見 [[topics/community-tech-tools]]（🧭 者已有證據等級與一句為什麼）

### 規劃與拆解（對應 [[topics/coding-workflow-guide]] 第 3 段）

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [github/spec-kit](https://github.com/github/spec-kit) | 133,053 | 💫 Toolkit to help you get started with Spec-Driven Development |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 67,046 | Spec-driven development (SDD) for AI coding assistants. |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) 📰 | 64,604 | A light-weight and powerful meta-prompting, context engineering and spec-driven developmen |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | 7,771 | A powerful meta-prompting, context engineering and spec-driven development system that ena |
| [buildermethods/agent-os](https://github.com/buildermethods/agent-os) | 5,363 | Agent OS is a system for injecting your codebase standards and writing better specs for sp |

本庫判斷 → 見 [[topics/community-tech-tools]]（🧭 者已有證據等級與一句為什麼）

### Code review（對應 [[topics/coding-workflow-guide]] 第 5 段）

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 57,773 | Git with a cup of tea! Painless self-hosted all-in-one software development service, inclu |
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 31,106 | Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codeb |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 21,826 | Fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: d |
| [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | 10,854 | Agent IDE that enables you to manage fleets of coding agents. It comes with an agentic orc |
| [reviewdog/reviewdog](https://github.com/reviewdog/reviewdog) | 9,558 | 🐶 Automated code review tool integrated with any code analysis tools regardless of program |

本庫判斷 → 見 [[topics/community-tech-tools]]（🧭 者已有證據等級與一句為什麼）

### 規則維護不腐爛（CLAUDE.md 跟上改動）（對應 [[topics/coding-workflow-guide]] 第 8 段）

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [steipete/agent-rules](https://github.com/steipete/agent-rules) | 5,694 | Rules and Knowledge to work better with agents such as Claude Code or Cursor |
| [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | 4,282 | AI-Driven Life Cycle (AI-DLC) adaptive workflow steering rules for AI coding agents |
| [dromara/liteflow](https://github.com/dromara/liteflow) | 3,844 | Lightweight, fast, stable, programmable component-based rule engine — where AI Agents orch |
| [gadievron/raptor](https://github.com/gadievron/raptor) | 3,696 | Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By  |
| [intellectronica/ruler](https://github.com/intellectronica/ruler) | 2,907 | Ruler — apply the same rules to all coding agents |

本庫判斷 → 見 [[topics/community-tech-tools]]（🧭 者已有證據等級與一句為什麼）

## B. 治理（管 agent 的需求）

### multi-agent orchestration

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [stablyai/orca](https://github.com/stablyai/orca) | 59,856 | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with you |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | 32,963 | OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more |
| [revfactory/harness](https://github.com/revfactory/harness) | 8,881 | A meta-skill that designs domain-specific agent teams, defines specialized agents, and gen |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | 8,361 | Project management skill system for Agents that uses GitHub Issues and Git worktrees for p |
| [ZSeven-W/openpencil](https://github.com/ZSeven-W/openpencil) | 5,790 | The world's first open-source AI-native vector design tool and the first to feature concur |

本庫判斷 → 見 [[topics/community-tech-tools]]「我卡在這裡」的「一堆 agent 在跑，看不到誰卡住」列

### LLM 知識庫／文件策展／知識傳承

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 14,888 | Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with a |
| [PleasePrompto/notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp) 📰 | 3,385 | MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation |
| [cyberagiinc/DevDocs](https://github.com/cyberagiinc/DevDocs) | 2,105 | Completely free, private, UI based Tech Documentation MCP server. Designed for coders and  |
| [trailofbits/claude-code-config](https://github.com/trailofbits/claude-code-config) | 2,095 | Opinionated defaults, documentation, and workflows for Claude Code at Trail of Bits |
| [timescale/pg-aiguide](https://github.com/timescale/pg-aiguide) | 1,830 | MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools  |

本庫判斷 → 見 [[topics/community-tech-tools]]（🧭 者已有證據等級與一句為什麼）

### 資料源韌性與監測

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS) | 15,909 | A free, self-hostable news aggregator… |
| [finaldie/auto-news](https://github.com/finaldie/auto-news) | 905 | A personal news aggregator to pull information from multi-sources + LLM (ChatGPT/Gemini/Ol |
| [CyberShadow/DFeed](https://github.com/CyberShadow/DFeed) | 386 | D news aggregator, newsgroup client, web newsreader and IRC bot |
| [janlukasschroeder/realtime-newsapi](https://github.com/janlukasschroeder/realtime-newsapi) | 373 | Financial News Aggregator - Real Time & Query API for Financial News |
| [SuYxh/ai-news-aggregator](https://github.com/SuYxh/ai-news-aggregator) | 331 | 🤖 AI News Aggregator - 自动聚合 80+ AI/科技资讯源，支持 RSS 订阅导入，智能过滤 AI 相关内容，双语标题翻译，每 2 小时自动更新 |

本庫判斷 → 見 [[topics/community-tech-tools]]（🧭 者已有證據等級與一句為什麼）

## 無法用 GitHub 辨識的需求（指路）

以下需求兩輪 query 校準皆被巨頭洗版或 0 命中——不是還沒調好，是**感測器裝錯層**：治理型需求是讀者講痛點的語言（「它說做完了但沒做」），在 HN／dev.to 全文，不在 repo 描述。本頁不掛空榜；答案在判斷層：

| 需求 | 本庫判斷 |
|---|---|
| 實作期攔錯（hook／lint／型別） | 見 [[topics/community-tech-tools]]「我卡在這裡」的「CLAUDE.md 寫了它不聽」列 |
| 測試與驗證（含 evidence-gated done） | 見 [[topics/community-tech-tools]]「我卡在這裡」的「它說做完了，但根本沒做」列 |
| 除錯與靜默失敗偵測 | 候選症狀「感覺變笨，想先量測歸因」掛在 [[topics/code-quality-decline]]，決策表尚未開列（≥2 頁需求證據門檻） |
| git／commit 衛生自動化 | 見 [[topics/community-tech-tools]]「我卡在這裡」的「多個 agent 在同一 repo 互相覆蓋」列 |

---

## 參考來源

- 設定檔與 query 校準紀錄：`data/skill_interest_watch.json`；產出腳本 `scripts/skill_interest_snapshot.py`
- 星史：`data/repo_star_history.csv`（各發現窗每日記錄，保留 60 天）
