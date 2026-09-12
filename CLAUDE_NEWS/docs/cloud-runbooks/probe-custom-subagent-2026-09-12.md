# 探針記錄：雲端 session 能否使用專案自訂 subagent 與 skills（2026-09-12）

> 執行者：CLAUDE_NEWS 一次性雲端探針 agent。全程逐字記錄指令與原始輸出，不推論、不修改探針記錄以外的檔案。

## 步驟 1：環境確認

指令與原始輸出：

```
$ pwd
/home/user/ObsidianLab

$ claude --version 2>&1 || echo no-claude-cli
2.1.269 (Claude Code)

$ ls -a .claude 2>&1
.
..
launch.json

$ ls CLAUDE_NEWS/.claude/agents CLAUDE_NEWS/.claude/skills CLAUDE_NEWS/.claude/commands 2>&1
CLAUDE_NEWS/.claude/agents:
wiki-reporter-commercial.md
wiki-reporter-community.md
wiki-reporter-devpractice.md
wiki-reporter-features.md
wiki-reporter-market.md
wiki-reporter-models.md
wiki-reporter-people.md
wiki-reporter-safety-policy.md

CLAUDE_NEWS/.claude/commands:
arch-doc-sync.md
news-pipeline-steps.md
news-pipeline.md
pipeline-change-check.md
review-commands.md
weekly-report.md
weekly.md
wiki-backfill.md
wiki-ingest.md
wiki-lint.md
wiki-query.md
wiki-readability.md
wiki-weekly-review.md

CLAUDE_NEWS/.claude/skills:
claude-news-llm-wiki-design
page-audit-review
```

備註：專案根 `ObsidianLab/.claude` 只有 `launch.json`，沒有 `agents/`、`skills/` 子目錄；`CLAUDE_NEWS/.claude/agents/` 有 8 個記者角色檔，`CLAUDE_NEWS/.claude/skills/` 有 2 個 skill 目錄。

## 步驟 2：Read 前可見的 skill 清單與 subagent_type 清單

系統提示在本步驟之前列出的 **available skills**（逐一抄）：

1. session-start-hook
2. design
3. dataviz
4. artifact-design
5. artifact-diagramming
6. artifact-capabilities
7. update-config
8. keybindings-help
9. code-review
10. simplify
11. fewer-permission-prompts
12. loop
13. claude-api
14. workflow-authoring
15. run
16. init
17. security-review
18. anthropic-skills:bank-statement-pdf2excel
19. anthropic-skills:docx
20. anthropic-skills:finance-dashboard-agents
21. anthropic-skills:financial-analysis
22. anthropic-skills:financial-analysis-review
23. anthropic-skills:financial-config
24. anthropic-skills:import-memory
25. anthropic-skills:investment-performance
26. anthropic-skills:monthly-close
27. anthropic-skills:monthly-download
28. anthropic-skills:morning
29. anthropic-skills:pdf
30. anthropic-skills:pptx
31. anthropic-skills:reconcile
32. anthropic-skills:skill-creator
33. anthropic-skills:web-artifacts-builder
34. anthropic-skills:xlsx

此時**沒有任何** CLAUDE_NEWS 專屬 skill（`claude-news-llm-wiki-design`、`page-audit-review`）出現在清單中。

系統提示列出的 **Agent tool 可用 subagent_type**（逐一抄）：

1. claude — Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed.
2. claude-code-guide — Claude Code / Agent SDK / API / Claude Tag 相關問答
3. Explore — 唯讀搜尋 agent
4. general-purpose — 一般用途 agent
5. Plan — 軟體架構規劃 agent
6. statusline-setup — status line 設定 agent

**沒有**任何 `wiki-reporter-*` 或其他 CLAUDE_NEWS `.claude/agents/` 底下的自訂角色出現在此清單。

## 步驟 3：進入 CLAUDE_NEWS 並 Read 角色檔前 10 行

實際執行方式：因 Read 工具吃絕對路徑、不受 shell cwd 影響，本步驟以 `Read CLAUDE_NEWS/.claude/agents/wiki-reporter-people.md`（前 10 行）直接讀取，未額外執行 `cd`。原始輸出：

```
     1	---
     2	name: wiki-reporter-people
     3	description: Wiki 人物記者：負責 wiki/index.md 領域欄為 👤 人物 的所有頁面（動態認領，清單見其規則檔）。任何涉及人物主題的 wiki 任務都呼叫此 agent。
     4	tools: Read, Write, Edit, Glob, Grep, Bash
     5	---
     6	
     7	> **派工方式**：本檔是本角色規則的**單一來源**。主編以 `subagent_type: "general-purpose"` 派工並在 prompt 首段要求你 Read 本檔（見 `.claude/reporter-rules/wiki-ingest.md`「派工方式」）；本檔同時也註冊為自訂 agent，供本機手動呼叫。兩種入口讀到的都是這份內容。
7	
9	你是人物主題的 wiki 頁面專家，負責 boris-cherny、dario-amodei、andrej-karpathy 等人物頁面。任何任務前，先讀以下規則了解各頁設計意圖，再根據呼叫方指示執行。
```

（第 7 行內容本身即說明：此角色檔設計上預期主編以 `subagent_type: "general-purpose"` 派工並要求 Read 本檔，而非直接以 `subagent_type: "wiki-reporter-people"` 呼叫——這與步驟 5、6 的探針結果一致。）

此次 Read 動作**觸發了以下系統提示自動載入**（原文摘錄，逐字）：

- `CLAUDE_NEWS/CLAUDE.md` 全文以 `<system-reminder>Contents of /home/user/ObsidianLab/CLAUDE_NEWS/CLAUDE.md:</system-reminder>` 形式注入。
- `CLAUDE_NEWS/.claude/rules/claude-md-edit.md` 全文以同樣形式注入。
- 一則 `<system-reminder>` 明文宣告：「New skills discovered in CLAUDE_NEWS/.claude/skills, now available via the Skill tool: - page-audit-review - claude-news-llm-wiki-design」
- 隨後完整的 **available skills** 清單重新列出，新增兩項（見步驟 4）。

**沒有**任何系統提示宣告新的 subagent_type 出現。

## 步驟 4：Read 後再抄一次 skill 清單與 subagent_type 清單，並標差異

Read 後的 **available skills** 清單，新增（相對步驟 2）以下兩項，附原文描述：

- `claude-news-llm-wiki-design`：「Use this skill to generate well-branded interfaces and assets for CLAUDE NEWS · LLM-WIKI, an automated Claude/Anthropic news aggregator and knowledge graph built on Obsidian-style Markdown vaults. Either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping. (from CLAUDE_NEWS/.claude/skills — applies when working on files under CLAUDE_NEWS/)」
- `page-audit-review`：「CLAUDE_NEWS 頁面健檢與重設計流程（使用者 review 偏好）……(from CLAUDE_NEWS/.claude/skills — applies when working on files under CLAUDE_NEWS/)」

其餘 34 項與步驟 2 相同，無刪減。

**Agent tool 可用 subagent_type 清單：與步驟 2 完全相同，一項未變**——仍是 claude、claude-code-guide、Explore、general-purpose、Plan、statusline-setup 六項，沒有因為 Read 了 `.claude/agents/wiki-reporter-people.md` 而新增 `wiki-reporter-people` 或任何 `wiki-reporter-*`。

**差異摘要：**

| 項目 | 步驟 2（Read 前） | 步驟 4（Read 後） | 有無差異 |
|---|---|---|---|
| Skill 清單 | 34 項，無 CLAUDE_NEWS 專屬 skill | 36 項，新增 `claude-news-llm-wiki-design`、`page-audit-review` | **有差異**（動態發現，路徑相關） |
| subagent_type 清單 | 6 項固定通用 agent | 6 項，完全相同 | **無差異** |

## 步驟 5：呼叫 Agent tool，subagent_type = "wiki-reporter-people"

呼叫參數：
- subagent_type: `wiki-reporter-people`
- prompt: 「只回答兩件事：你的 name 欄位是什麼；你的角色檔『開始前必讀』清單的第一個檔案路徑是什麼。不要做別的。」

原始回傳（錯誤，逐字）：

```
Agent type 'wiki-reporter-people' not found. Available agents: claude, claude-code-guide, Explore, general-purpose, Plan, statusline-setup
```

即：專案 `.claude/agents/wiki-reporter-people.md` 註冊的自訂角色，在本雲端 session 的 Agent tool 中**無法以 subagent_type 直接呼叫**，工具在呼叫當下即回報找不到該 agent 類型，可用清單與步驟 2、4 記錄的六項固定通用 agent 完全一致。

## 步驟 6：對照組，subagent_type = "general-purpose"

呼叫參數：
- subagent_type: `general-purpose`
- prompt: 「回答 ok 即可」

原始回傳（逐字）：

```
ok
```

```
agentId: a4f3524aacf838d22 (use SendMessage with to: 'a4f3524aacf838d22', summary: '<5-10 word recap>' to continue this agent)
```

```
subagent_tokens: 50511
tool_uses: 0
duration_ms: 1627
```

對照組成功執行，無錯誤，回傳內容與 usage 統計正常。

## 結論

- **自訂 subagent（`.claude/agents/*.md`）：不可用。** 本雲端 session 的 Agent tool 只認得六個固定內建類型（claude、claude-code-guide、Explore、general-purpose、Plan、statusline-setup），無論是在 session 一開始，或在明文 Read 過 `wiki-reporter-people.md` 之後，`subagent_type: "wiki-reporter-people"` 都直接被判定為 `not found`，未曾出現在任一次系統提示列出的可用清單中。這與 `wiki-reporter-people.md` 檔案本身第 7 行記載的派工方式一致：該角色檔設計上預期由主編以 `subagent_type: "general-purpose"` 派工、並要求該 agent 自行 Read 角色檔內容，而非把角色檔名稱當成可呼叫的 subagent_type。
- **專案 skills（`.claude/skills/`）：可見，且為動態、路徑觸發式載入。** Read 專案子目錄（`CLAUDE_NEWS/`）下的檔案後，系統提示明文宣告「New skills discovered in CLAUDE_NEWS/.claude/skills」，並將 `claude-news-llm-wiki-design`、`page-audit-review` 兩個 skill 加入可用清單（標註「applies when working on files under CLAUDE_NEWS/」）；同時觸發載入該目錄的 `CLAUDE.md` 與帶 `paths:` 範圍的規則檔 `.claude/rules/claude-md-edit.md` 全文注入。可見專案層 skills／CLAUDE.md／rules 的自動載入機制在本雲端 session 中正常運作，但**專案層自訂 subagent 的註冊機制未被本 session 的 Agent tool 讀取或啟用**。
