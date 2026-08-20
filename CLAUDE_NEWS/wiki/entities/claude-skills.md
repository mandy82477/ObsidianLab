---
page: "entities/claude-skills"
kind: "entity"
type: "feature"
status: "active"
domain: "🛠️ 工具/功能"
last_updated: "2026-08-19"
last_news_update: "2026-08-19"
status_main: "active"
days_since_news: 1
inbound_links: 5
attribution_count: 9
attribution_last: "2026-08-19"
top_source: "github"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-09-02"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Skills

**類型：** feature
**狀態：** active
**領域：** 🛠️ 工具/功能
**首次出現：** 2026-04-27
**最後更新：** 2026-08-19
**最後新聞更新：** 2026-08-19

> **最新官方動態**（2026-08-19）
> 官方技能庫（anthropics/skills）目錄異動：昨日新增的 `claude-academy-guide` 今日改名為 `academy-guide`（原名同步從目錄移除），`discernment-nudge` 不變；官方 repo 未附說明文字，改名理由與內容用途待後續版本或官方文件補齊。

---

## 現況

Anthropic 目前把 Skills 定位為官方六大「控制層」之一：把常用工作流程（如程式碼審查、安全審計、前端設計）封裝成描述文件，Claude 依語意自動判斷何時載入執行，使用者不需手動下指令；**但 2026-07-19（v2.1.215）起 `/verify` 與 `/code-review` 兩項技能改為例外**，不再自動觸發，須使用者手動呼叫指令才會執行（詳見下方「官方 Skills 生態一覽」）。2026-06-21 官方部落格《七種指令傳遞方法》正式將其納入決策框架，釐清 Skills 與 CLAUDE.md、rules、subagents、hooks、output styles、system prompt append 之間的定位差異。

官方近期最大手筆是 2026-05-24 發布的「31 個小企業 Skills」技能包，首日下載達 38.2 萬次，顯示 Skills 生態已從工程師專屬工具擴張至一般商業使用者；2026-06-05 官方部落格《Lessons from building Claude Code: How we use skills》進一步公開內部數百個 Skills 的實戰心得（什麼值得做成 skill、如何結構化、何時分享），是目前最權威的官方 Skills 設計指南。**官方目前尚未提供正式的 skill 分享／同步平台或市集機制**——現有的技能發現與安裝介面（如 Claudinho）都是第三方工具，社群也曾提出「Anthropic 建了 skill runtime 卻沒有創作者變現機制」的落差（見下方第三方生態動態）。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ✅ 廣泛採用 |
| 最適合 | 想把重複工作流程封裝成可重用單元的 Claude Code 重度使用者、需要跨專案共用架構護欄／審查規範的團隊 |
| 不適合 | 只需簡單問答、不需要重複工作流程的輕量使用者（skill 即使不觸發也會佔用額外 token，見「注意事項」） |

> 詳細最新熱度見 [[feature-radar]]

## 使用指南

最小可用範例：在專案內建立 `.claude/skills/<skill-name>/SKILL.md`，用 frontmatter 描述 skill 用途，Claude 會依描述語意判斷何時自動載入。

```markdown
---
name: code-review-checklist
description: 在 PR 或 diff review 前，依團隊規範檢查命名、測試覆蓋率與安全疑慮
---

# Code Review Checklist

1. 檢查函式命名是否符合專案慣例
2. 確認新增邏輯有對應測試
3. 掃描是否引入明文密鑰或不安全的字串拼接
```

將此目錄提交進 repo（`.claude/skills/`），任何人 clone 專案後 Claude Code 會自動載入，達到架構護欄效果（社群實測案例見 2026-05-20）。也可搭配 `--safe-mode` 旗標（v2.1.169 起）在排查問題時一鍵停用所有 skills、hooks、MCP 等客製化設定。

## 官方 Skills 生態一覽

| 面向 | 內容 | 日期 |
|------|------|------|
| 機制本身 | 可重複使用的任務封裝單元，Claude 依描述語意自動觸發，無需手動呼叫；採「漸進式揭露」三層架構（啟動只讀名稱+簡述，命中後才載入完整內容），兼顧 token 效率與觸發準確度 | 官方設計揭露 2026-05-31 |
| 官方 skills bundle | 新增 `academy-guide`（2026-08-18 以 `claude-academy-guide` 之名新增，2026-08-19 改名，原名同步移除）、`discernment-nudge`；官方 repo 未附說明文字，用途待補 | 2026-08-19（改名） |
| | 官方核心 11 個 Skills（代碼審查、安全審計、前端設計等），首見於社群移植而非官方公告本身 | 2026-04-27（移植事件） |
| | 官方發布「31 個小企業 Skills」技能包，首日下載 38.2 萬次 | 2026-05-24 |
| | Claude for Teachers 教學技能庫（美國認證 K-12 教師專用），詳見 [[entities/claude-for-teachers]] | 2026-07-15 |
| 平台支援 | security-guidance plugin 全面開放給所有 Claude Code 用戶（非僅 Enterprise），寫碼時即時偵測漏洞——首次將企業安全功能下放一般開發者工作流 | 2026-05-27 |
| | v2.1.169 新增 `--safe-mode` 旗標／`CLAUDE_CODE_SAFE_MODE` 環境變數，一鍵停用含 skills 在內的所有客製化設定 | 2026-06-09 |
| | v2.1.178：Skills 在巢狀子 Agent 中可正常運作（搭配新版 `Tool(param:value)` permission 語法） | 2026-06-16 |
| 官方設計指南 | 《Lessons from building Claude Code: How we use skills》——內部數百個 Skills 的實戰心得 | 2026-06-05 |
| | 《七種指令傳遞方法》——Skills 與 CLAUDE.md/rules/subagents/hooks/output styles/system prompt append 六層控制的定位框架 | 2026-06-21 |
| 分享／同步機制 | ✅ **已有官方市集**（2026-08-08 查證官方文件更正）：`claude-plugins-official`（Anthropic 策展，首次互動啟動時自動註冊）與 `claude-plugins-community`（第三方送審後上架，需自行 `/plugin marketplace add`）；目錄另可於 [claude.com/plugins](https://claude.com/plugins) 瀏覽，送審有自動驗證與安全篩查。**創作者變現機制仍缺** | 市集已就位；變現無官方時程 |
| | Enterprise 方案可開啟 skill／plugin 安全掃描（beta），第三方 skill／plugin 上傳或編輯時自動檢查惡意內容 | 2026-08-06 |
| 行為變更 | v2.1.215：`/verify` 與 `/code-review` 兩項官方技能不再由 Claude 自動觸發，須使用者手動呼叫指令才會執行；與上方「機制本身」列所述「依描述語意自動觸發、無需手動呼叫」的通則產生例外，依賴自動驗證/審查的既有工作流需改為顯式呼叫，無過渡期即刻生效。詳見 [[entities/claude-code]] 版本表 | 2026-07-19 |

## 第三方生態動態

- **OpenCode-power-pack**：2026-04-27 移植 Anthropic 官方 11 個 skills 至 OpenCode，打破官方插件僅限 Claude Code 環境的相容性限制，詳見 [[entities/opencode]]
- **Claudinho**：2026-06-03 上線的 Claude Skills 探索與安裝介面，鎖定非技術用戶「技能難以發現、難以評估價值」的痛點；為第三方工具，非官方產物
- **創作者變現缺口**：2026-05-20 社群開發者指出 Anthropic 建立了 skill runtime 卻無創作者變現機制，自製 skill 只能免費開源分享，無法商業化（推論：這是官方生態目前最明顯的結構性缺口之一）
- ❓ **待查證**（標 2026-08-19｜查 200000 tokens、The New Stack｜複 2026-09-02）｜**The New Stack 報導某 Claude Code skill 在回答任何問題之前就先耗掉 20 萬 token**（Google News 轉載，2026-08-18 報導）：原文僅標題層級可用，未見具體是哪個 skill、成因是否為漸進式揭露機制未生效或 skill 本身設計不當，亦未見是否為官方或第三方 skill；若屬實則是與本頁「漸進式揭露三層架構」設計初衷（節省 token）相牴觸的反例，惟細節待補

## 相關議題

- [[topics/coding-workflow-guide]] — 開發流程各階段該下哪個 skill、探索 codebase 與寫下結果的實戰對照

- [[topics/community-tech-patterns]]（skill 設計模式、踩坑經驗與社群自製 skill 案例——如何寫 skill、何時該封裝、實測「74 個 skill 只有 3 個真正改變行為」等一手心得皆記錄於該頁，本頁不重複收錄）
- [[entities/claude-code]]（Skills 為六大控制層之一；版本更新與已知問題見該頁版本表）
- [[entities/opencode]]（OpenCode-power-pack 移植官方 skills 案例）
- [[entities/claude-for-teachers]]（教學技能庫）
- [[topics/official-community-gap]]（Skills 透明度缺口——`ask_user_input_v0` 靜默限制問題與 subagent 意外衍生行為，反映官方「自動完成優先」設計哲學與開發者「透明可控」期望的落差）

## 參考來源

- [Anthropic Blog: Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)（2026-06-05）
- [Anthropic Blog: The seven methods for delivering instructions](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)（2026-06-21）
- [OpenCode-power-pack – Claude Code skills ported to OpenCode](https://github.com/waybarrios/opencode-power-pack)（2026-04-27）
- [Claude Code v2.1.169 Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.169)（2026-06-09）
- [Claude Code v2.1.178 Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.178)（2026-06-16）
- [Show HN: Claudinho — Find and Install Claude Skills](https://www.claudinho.xyz/)（2026-06-03）
- [[news/2026-04-27]]、[[news/2026-05-17]]、[[news/2026-05-20]]、[[news/2026-05-24]]、[[news/2026-05-27]]、[[news/2026-05-31]]、[[news/2026-06-05]]、[[news/2026-06-09]]、[[news/2026-06-16]]、[[news/2026-06-21]]、[[news/2026-07-15]]、[[news/2026-08-18]]、[[news/2026-08-19]]

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-08-19 | 官方技能庫目錄核對：`claude-academy-guide`（08-18 新增）改名為 `academy-guide`，原名同步從目錄移除；The New Stack 報導某 Claude Code skill 在回答問題前耗掉 20 萬 token，僅標題可用，已標待查證 |
| 2026-08-18 | 官方技能庫（anthropics/skills）新增 2 項：`claude-academy-guide`、`discernment-nudge`；官方 repo 未附說明文字，用途待補 |
| 2026-07-15 | Claude for Teachers 教學技能庫發布，向美國認證 K-12 教師免費開放（詳見 [[entities/claude-for-teachers]]） |
| 2026-06-21 | 官方部落格《七種指令傳遞方法》，將 Skills 納入 CLAUDE.md／rules／subagents／hooks／output styles／system prompt append 六層控制決策框架 |
| 2026-06-16 | v2.1.178：Skills 在巢狀子 Agent 中可正常運作，搭配新版 `Tool(param:value)` permission 語法 |
| 2026-06-09 | v2.1.169：新增 `--safe-mode` 旗標與 `CLAUDE_CODE_SAFE_MODE` 環境變數，一鍵停用含 skills 在內的所有客製化設定 |
| 2026-06-05 | 官方部落格《Lessons from building Claude Code: How we use skills》，公開內部數百個 Skills 的實戰心得 |
| 2026-05-31 | 社群整理官方 Skills 設計指南揭露的「漸進式揭露」三層架構（啟動只讀名稱+簡述，命中後才載入完整內容） |
| 2026-05-27 | security-guidance plugin 全面開放給所有 Claude Code 用戶（非僅 Enterprise），首次將企業安全功能下放一般開發者工作流 |
| 2026-05-24 | 官方發布「31 個小企業 Skills」技能包，首日下載達 38.2 萬次 |
| 2026-05-20 | 社群指出 Anthropic 建立了 skill runtime 卻無創作者變現機制的結構性缺口 |
| 2026-05-17 | Claude Skills 靜默覆蓋指令爭議浮現：`ask_user_input_v0` 硬性限制（最多 3 問題／4 選項）與 subagent 意外衍生行為，引發社群對機制透明度的系統性質疑 |
| 2026-04-27 | OpenCode-power-pack 移植 Anthropic 官方 11 個 skills 至 OpenCode，是本頁追蹤到的最早生態事件 |
