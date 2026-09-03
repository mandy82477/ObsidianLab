---
page: "topics/community-tech-tools"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-09-03"
last_news_update: "2026-09-02"
update_freq: "🗓️ 週更（每週策展一次；更新日期停留數天屬正常節奏）"
status_main: "ongoing"
days_since_news: 2
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 2
inbound_links: 28
attribution_count: 3
attribution_last: "2026-09-02"
top_source: "user-query"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群工具目錄

**狀態：** ongoing
**領域：** 🌐 社群
**更新頻率：** 🗓️ 週更（每週策展一次；更新日期停留數天屬正常節奏）
**開始日期：** 2026-04-25
**最後更新：** 2026-09-03
**最後新聞更新：** 2026-09-02

> **最新改版**（2026-09-03）
> 「不綁症狀的精選」區退役——規模型清單（誰大、誰在漲）改看 [[topics/skill-interest-watch]] 的每日榜；本頁只留**判斷**：症狀決策表、推薦細節、Skills 速查、工具目錄。

---

## 摘要

**我卡住了，社群有什麼能救？** 本頁把社群工具依「症狀」排列，每個症狀給一個首選、一條改用分界、一個帶日期的證據等級。
按開發流程階段找官方做法見 [[topics/coding-workflow-guide]]；做法背後的機制與實測見 [[topics/community-tech-patterns]]；概念辯論見 [[topics/community-tech-discussions]]；官方功能見 [[feature-radar]]。

---

## 我卡在這裡

> 本表每週複查一次；首選工具的急性事件（資安、棄坑、下架）另見 [[entities/claude-code]] 與 [[topics/ai-agent-safety]]。

| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |
|---|---|---|---|
| 帳單爆了，看不到錢花在哪 | ⌨️ **tare** | 不想動終端、要桌面常駐 → 🖥️ Claude Usage Widget；想比較多個 coding agent 的花費 → Frugal Tokens | 🟡（08-27） |
| context 一直被工具輸出撐爆 | 🔌 **pxpipe** | 不能接受請求過代理層 → 🧩 Graft（數字有爭議，見細節）；還不確定是誰在撐爆 → 先跑 ⌨️ PrismoDev 診斷 | 🟡（08-05，附防刷佐證） |
| 接手沒碰過的大 repo，agent 讀不懂 | 🧩 [**graphify**](https://github.com/Graphify-Labs/graphify) | 要讓**人**看懂而非 agent → [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)；要把架構畫成圖交付 → [archify](https://github.com/tt-a1i/archify)；改 code 要索引自動同步 → [codegraph](https://github.com/colbymchenry/codegraph)（社群實測待累積） | 🟢（05-02 起多來源；08-31 訊號 11.3 萬星） |
| 每開新 session 都要重講一遍 | ⌨️ **brain.md** | 要團隊共享而非單機 → 🖥️ OzBrain；已在用 Obsidian → VIR | 🟡（08-25） |
| 多個 agent 在同一 repo 互相覆蓋 | ⌨️ [**Harness**](https://github.com/frenchie4111/harness) | 隔離後 commit 落地仍打架 → Claude Code Merge Queue；要跨 harness 統一協作邏輯 → omnigent | 🟢（04-29 起多來源） |
| 一堆 agent 在跑，看不到誰卡住 | ⌨️ **Omar** | 只跑 3–5 個、不想多花一毛 token → HUD（走官方 event stream）；要 GUI 主控台 → Cockpit | 🟢（05-02 起多來源） |
| 它說做完了，但根本沒做 | 🧩 [**Groundtruth**](https://github.com/vnmoorthy/groundtruth) | 要留可稽核證據給團隊審 → Proof Loop（建構者／驗證者分離） | 🟡（04-27） |
| CLAUDE.md 寫了它不聽 | —（答案是機制不是工具，見細節） | 規則多到耗 token → Writ；跨工具設定碎片化 → Caliber | 🟢（08-25 實測） |
| 不想被單一供應商綁死 | 🔌 **Workweave Router** | 只想改用本地模型、不動主配置 → claudely；想繞過計量計費 → clarp（⚠️ 政策風險，見細節） | 🟡（06-27） |

**圖例**——證據：🟢 多來源實測／🟡 單一實測（多為作者自測）／⚪ 僅星數。**證據等級為收錄或查證當時的判定，括號內即判定日，不隨時間自動回訪**。安裝：🧩 skill/plugin（一行安裝隨時可拔）／⌨️ CLI／🖥️ 桌面 app（注意平台鎖定）／🔌 proxy·MCP（**流量過第三方層，裝前先評估安全**）。首選只在出現新證據時更換，不為輪替而換。

**推薦細節**

- **pxpipe vs Graft 的數字強度不同**（08-30 彙整）：pxpipe 有作者實測（25,000 text token 壓至 2,700 image token、帳單降 59–70%，08-05；星數防刷已查證 forks 8.5%）；Graft 宣稱降 42%（08-15）但 HN 討論質疑 benchmark 段落疑似 AI 代寫、未經第三方覆核。接受走代理層就選 pxpipe（證據較強）；只想掛個 hook 隨時可拔、且不介意數字未覆核，才選 Graft。
- **「CLAUDE.md 不聽」沒有工具首選是結論不是留白**：dev.to 一手實作（08-25）顯示**以 hooks 強制執行取代 prompt 建議後，規則遵循率達 100%**——答案是機制不是工具，做法見 [[topics/community-tech-patterns]]。四個失效機理中只有後三者是工具能解的：規則被機率性忽略且無反饋、規則越多越貴（Writ 以語意檢索只注入相關規則）、規則腐化（Patina 偵測）、跨工具碎片化（Caliber 統一管理）。
- **接手大 repo 的分界**（09-03 補寫）：graphify 給 **agent** 用（本機 AST、免向量 DB，`/graphify` skill）；同組另三個解的是不同工種——Understand-Anything 給**人**探索、archify 給人**交付圖**、codegraph 是 graphify 的競品（自動同步索引，僅星數證據）。官方面的「接手大 repo 第一步」（先讀 CI、從子目錄啟動、LSP）在 [[topics/coding-workflow-guide]] 第 2a 段：官方設定先做，索引工具再裝。
- **Harness 同名提醒**：本表首選 [frenchie4111/harness](https://github.com/frenchie4111/harness)（多 worktree 並行管理）與 [[topics/skill-interest-watch]] multi-agent 榜上的 `revfactory/harness`（設計 agent team 的 meta-skill）**不是同一個專案**，裝前認清 owner。
- **多 agent 互踩**：Harness 為 ✅ 廣泛採用（04-29 收錄，多來源）；omnigent 星數 9,080（08-05 防刷查證時 8,150、forks 14.7%）但無第三方實測回報，列次選、證據 ⚪。
- **監看首選的分界**：HUD 經官方 JSON event stream 運作、不額外耗 token（08-07），適合小規模；Omar 管到 100 個 agent（05-02）。兩者解同一症狀的不同規模段。
- **clarp 的政策風險**（05-21 收錄）：以本地 PTY＋唯讀 API 代理規避 6/15 起的計量計費，屬計費規避而非最佳化；企業環境安裝前先確認與 Anthropic 合約條款的相容性。
- **記憶類的分界**：brain.md 零依賴、純檔案（08-25，504 星）；OzBrain 走團隊共享知識庫（08-21，HN 69）；VIR 直接萃取 session 檔進 Obsidian vault（05-23）。單機選檔案式，跨人選共享式。

### AI 輔助開發的長期副作用（早期信號，尚無成熟工具）

- **技能退化**（`recap`）— 開發者不再獨立解題，調試能力隨時間萎縮
- **命名漂移** — 每個 session 根據當下 context 取名，同概念可能出現四個不同名稱
- **架構邊界侵蝕**（`modularity plugin`、`Mneme`）— AI 為讓測試通過直接跨架構邊界，快速累積技術債
- **無法獨立 debug** — 程式在跑但開發者沒有心智模型，遇 bug 只能再問 AI，形成依賴閉環

官方公開敘事方向（加速使用、更長自主 agent）與上述擔憂反向，短期不會主動回應；官方 vs 社群缺口對照見 [[topics/official-community-gap]]。

---

## 🧩 Skills 速查（依 coding 用途分類）

社群 Agent Skills 的用途索引（**官方** skill 另有兩條軸：按工程流程階段與按產出物格式選用，見 [[topics/coding-workflow-guide]]）。安裝多為一行（`/plugin` 或 `npx skills add`），隨時可拔。

**Codebase 理解／索引**——知識傳承的三個工種：讓 **agent** 記住 repo、讓**人**看懂 repo、把架構**講給人聽**（建程式庫的一次性設定首選在「給 agent」列）

| Skill | 證據 | 一句話 |
|---|---|---|
| [**graphify**](https://github.com/Graphify-Labs/graphify) | 🟢（05-02 收錄 40k★＋71× 宣稱；08-31 訊號 11.3 萬星、`/graphify` skill、本機 AST 免向量 DB） | 【給 agent·索引】把 codebase（含文件、SQL schema）建成知識圖譜供跨 harness 查詢 |
| [**codegraph**](https://github.com/colbymchenry/codegraph) | ⚪（09-02 查證 user-query；69,253★、forks 4,420、活躍 push） | 【給 agent·索引】預索引 code 知識圖、**改 code 自動同步**、全本機——與 graphify 直接競品，auto-sync 主張更進一步，社群實測待累積 |
| [**Understand-Anything**](https://github.com/Egonex-AI/Understand-Anything) | ⚪（09-02 查證 user-query；81,325★、forks 6,841） | 【給人·探索式理解】把任意 code 變成可探索、可搜尋、可提問的互動知識圖——新人接手看懂 codebase 的那一格 |
| [**archify**](https://github.com/tt-a1i/archify) | ⚪（09-02 查證 user-query；43,378★、forks 2,777、214 commits） | 【給人·交付級圖表】架構／時序／資料流／生命週期圖，自包含 HTML 可匯出——把架構講給別人聽、寫進文件；🧩 `npx skills add tt-a1i/archify -g` |

**寫碼紀律／方法論**——改變 Claude 寫 code 的行為

| Skill | 證據 | 一句話 |
|---|---|---|
| [**obra/superpowers**](https://github.com/obra/superpowers) | ⚪（08-28，27.9 萬星，Reddit 有實際採用跡象） | Agentic skills 框架＋軟體開發方法論 |
| [**andrej-karpathy-skills**](https://github.com/multica-ai/andrej-karpathy-skills) | ⚪（08-29，星數增速異常存疑） | 單檔改善 LLM coding 常見缺陷，取材 Karpathy 觀察 |
| [**Groundtruth**](https://github.com/vnmoorthy/groundtruth) | 🟡（04-27） | Stop Hook 強制出示可驗證證明才准宣告完成 |
| **awesome-ux-skills** | 🟡（05-08） | Nielsen＋Shape of AI 等 UX 原則技能集 |

**產出與呈現**——生成特定產物或改變輸出形式

| Skill | 證據 | 一句話 |
|---|---|---|
| [**baoyu-design**](https://github.com/JimLiu/baoyu-design) | ⚪（08-29，3,637 星） | 本機執行 Claude Design 產自足式 HTML UI 原型 |
| [**/show-me**](https://www.humanlayer.com/blog/show-me-skill) | 🟡（08-13，雙來源） | 精簡視覺化取代大量文字輸出 |

**領域資料**——接特定資料域（coding 周邊，非核心寫碼流程）

| Skill | 證據 | 一句話 |
|---|---|---|
| [**Geosql**](https://github.com/dekart-xyz/geosql) | 🟢（07-08，機制已查證見懸置細節） | 地理空間資料（PostGIS／BigQuery／Snowflake）；4 倍提升僅在連 Dekart 時成立 |
| [**youtube-skills**](https://github.com/ZeroPointRepo/youtube-skills) | ⚪（08-12，防刷已查證） | YouTube 字幕擷取，跨 harness |
| [**Shortcuts Playground**](https://www.macstories.net/stories/introducing-shortcuts-playground/) | 🟡（05-23） | 自然語言生成 Apple Shortcuts |
| [**l3a0/claude-plugins**](https://github.com/l3a0/claude-plugins) | 🟡（08-24，HN 45） | OCR 復原 Kindle 被限制匯出的畫線筆記 |

> skill 分享基建（Sx 2.0）與彙整清單（awesome-llm-apps）不入本節——前者見工具目錄，後者這類「規模大但不對應症狀」的條目見 [[topics/skill-interest-watch]]。

---

## 指標說明

| 指標 | 說明 |
|------|------|
| **證據**（上方兩表） | 🟢 多來源實測 / 🟡 單一實測 / ⚪ 僅星數（未經行為佐證）；括號內為判定日，不隨時間自動回訪 |
| **採用**（下方目錄） | ✅ 廣泛採用 / ⚡ 小圈子使用 / ⏳ 觀望中 / ⚠️ 效果存疑 / ❌ 已放棄——與證據等級**不同軸**：採用量廣度 ≠ 宣稱可信度 |
| **類型** | 多 Agent / 記憶工具 / 費用監測 / 工作流 / 整合工具 / 搜尋/診斷 / 安全工具 / IDE/終端 / Skills / 其他 |
| **入選標準** | HN score ≥ 30 或評論 ≥ 5 / Show HN 投稿 / 同日 2 個獨立來源；無公開 repo 或純商業推廣者不收錄 |

---

## 工具目錄

| 工具 | 類型 | 採用 | 首次出現 | 簡介 |
| --- | --- | --- | --- | --- |
| [**thedotmack/claude-mem**](https://github.com/thedotmack/claude-mem) | 記憶工具 | ✅ | 2026-09-02 | 跨 harness（Claude Code、OpenClaw、Codex、Gemini 等 7 種以上）持久記憶，擷取 session 過程並用 AI 壓縮注入後續 session；9.3 萬星，2025-08-31 出生，本庫首次收錄 |
| [**addyosmani/agent-skills**](https://github.com/addyosmani/agent-skills) | Skills | ⏳ | 2026-09-02 | Addy Osmani（Google Chrome DevRel）具名生產級工程技能集合；9.2 萬星，2026-02 出生，僅星數佐證未另查證 |
| [**yetone/cumora**](https://github.com/yetone/cumora) | 工作流 | ⏳ | 2026-09-02 | 跨平台團隊聊天工具，讓 AI agent 成為聊天中的「一等公民」隊友，可接 Claude Code／Codex；3,416 星，作者具名知名開源開發者 |
| [**Abilityai/trinity**](https://github.com/Abilityai/trinity) | 多 Agent | ⏳ | 2026-09-02 | 自架 AI Agents 平台，支援 Claude Code、Codex、Gemini，Apache 2.0；503 星 |
| [**wanghuan9/skilldock**](https://github.com/wanghuan9/skilldock) | Skills | ⏳ | 2026-09-02 | AI skill 管理桌面應用，安裝/整理/編輯/同步/更新 Skills、MCP servers、plugins，跨 5 種 AI coding 工具；503 星 |
| [**Understand-Anything**](https://github.com/Egonex-AI/Understand-Anything) | 搜尋/診斷 | ⏳ | 2026-09-02 | 互動式 code 知識圖（可探索/搜尋/提問），跨 harness；81,325★、2026-03 出生，09-02 查證（防刷通過），社群實測待累積 |
| [**codegraph**](https://github.com/colbymchenry/codegraph) | 記憶工具 | ⏳ | 2026-09-02 | 預索引 code 知識圖、改 code 自動同步、全本機省 token；69,253★、2026-01 出生，09-02 查證（防刷通過），graphify 競品 |
| [**archify**](https://github.com/tt-a1i/archify) | Skills | ⏳ | 2026-09-02 | 架構/時序/資料流圖 agent skill，自包含 HTML；43,378★、2026-04 出生，09-02 查證（防刷通過） |
| [**x1xhlol/system-prompts-and-models-of-ai-tools**](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 其他 | ✅ | 2026-08-29 | 彙整 Claude Code、Cursor、Devin AI、Replit 等數十款 AI 編碼工具完整系統提示詞與模型設定；14.3 萬星，2025-03 出生，長期累積型參考資源 |
| [**Shubhamsaboo/awesome-llm-apps**](https://github.com/Shubhamsaboo/awesome-llm-apps) | Skills | ✅ | 2026-08-30 | 彙整百餘款 AI Agent、Agent Skills 與 RAG 開源應用清單；13.5 萬星，2024-04 出生，長期累積型參考資源 |
| [**multica-ai/andrej-karpathy-skills**](https://github.com/multica-ai/andrej-karpathy-skills) | Skills | ⏳ | 2026-08-29 | 單一 CLAUDE.md 檔案改善 Claude Code 行為，取材自 Karpathy 對 LLM coding 常見缺陷的觀察；20.9 萬星，星數存疑（見收錄註記） |
| [**garrytan/gstack**](https://github.com/garrytan/gstack) | 多 Agent | ⏳ | 2026-08-30 | Garry Tan（YC 總裁）公開自己的 Claude Code 設定，23 個角色化工具分飾 CEO、設計師、工程經理等職能；13.0 萬星，星數真實性未經驗證（見收錄註記） |
| [**JimLiu/baoyu-design**](https://github.com/JimLiu/baoyu-design) | Skills | ⏳ | 2026-08-29 | 本機以 Agent Skill 執行 [[entities/claude-design]]，供 Cursor／Claude Code 產出自足式 HTML UI 原型，官方建議搭配 Opus 4.8；3,637 星 |
| [**rsmdt/the-startup**](https://github.com/rsmdt/the-startup) | 工作流 | ⏳ | 2026-08-25 | 「The Agentic Startup」風格 Claude Code commands／skills／agents 集合；507 星 |
| [**mindmuxai/brain.md**](https://github.com/mindmuxai/brain.md) | 記憶工具 | ⏳ | 2026-08-25 | 零依賴、檔案式跨 session 持久記憶層，為 coding agent 保存決策／需求／限制的「專案大腦」；504 星 |
| [**l3a0/claude-plugins**](https://github.com/l3a0/claude-plugins) | 其他 | ⏳ | 2026-08-24 | Claude Code Skill 用 OCR 從 Kindle Cloud Reader 復原被限制匯出的畫線筆記；HN score 45 |
| [**obra/superpowers**](https://github.com/obra/superpowers) | Skills | ⏳ | 2026-08-28 | Agentic skills 框架與軟體開發方法論；累計 27.9 萬星，2025-10 出生，本庫今日首次收錄；僅星數佐證，forks／issues 未驗證，惟已見於 Reddit 使用者抱怨（間接證明有實際採用） |
| [**tare**](https://github.com/kelviq/tare) | 費用監測 | ⏳ | 2026-08-27 | CLI 底部即時顯示 usage/context/model 狀態並配合 hook 監測用量暴增；Show HN score 84 |
| [**opslane**](https://github.com/opslane/opslane) | 工作流 | ⏳ | 2026-08-27 | 監看 user session 找出真實影響使用者的 bug，僅在能驗證修復後才開 PR；Show HN score 34 |
| [**ambient-context**](https://github.com/dragthelake/ambient-context) | 記憶工具 | ⏳ | 2026-08-25 | macOS 選單列 app，透過 Accessibility API 讀取焦點視窗文字寫成逐日 Markdown，供 Claude Code 查詢近況；Show HN score 51，source_count 2 |
| [**OzBrain**](https://ozbrain.com) | 記憶工具 | ⏳ | 2026-08-21 | agent 與團隊共享的知識庫，取代傳統筆記/任務管理工具；Show HN score 69，source_count 2 |
| [**Proliferate**](https://github.com/proliferate-ai/proliferate) | 多 Agent | ⏳ | 2026-08-21 | YC S25，開源自架 AI IDE，統一操作 Claude Code／Codex／OpenCode／Cursor／Grok；Show HN score 39，source_count 2 |
| [**Frugal Tokens**](https://demo.frugaltokens.com/) | 費用監測 | ⏳ | 2026-08-19 | 探索跨 coding agent（含 Claude Code）的成本與用量，含 cache miss 對花費的影響；Show HN score 33，source_count 2 |
| [**machine0**](https://machine0.io) | 整合工具 | ⏳ | 2026-08-18 | YC S26，持久化 CPU/GPU 雲端 VM 供長時間自主 agent 運算，`machine0 new mybox` 即開機，$0.013/hr 起；Launch HN score 78 |
| [**internet-court-skill**](https://github.com/internet-court/internet-court-skill) | 安全工具 | ⏳ | 2026-08-18 | agent-to-agent 商務信任層 skill：自然語言 mandate、ERC-7710 委任權限、x402 支付、託管與爭議解決；5,317 星（09-02 更新），佐證不足（見收錄註記） |
| [**claw-orchestrator**](https://github.com/Enderfga/claw-orchestrator) | 多 Agent | ⏳ | 2026-08-17 | 跨 harness 統一 runtime（Claude Code／Codex／Antigravity／Cursor／OpenCode），持久 session＋multi-agent councils＋MCP server；547 星 |
| [**statuslin.es**](https://statuslin.es) | UI 工具 | ⏳ | 2026-08-17 | 社群策展的 Claude Code status line 樣式展示網站，每則附真實 sandbox 容器截圖；同時被 2 個獨立來源收錄 |
| [**Graft**](https://github.com/NanoNets/Graft) | 費用監測 | ⚠️ | 2026-08-15 | Claude Code hooks 削減 grep 輸出 token，宣稱降幅 42%（HN 39，跨 2 來源）；HN 討論串質疑 README 的 benchmark 段落疑似 AI 代寫，數字未經第三方覆核 |
| [**/show-me**](https://www.humanlayer.com/blog/show-me-skill) | Skills | ⏳ | 2026-08-13 | agent skill，讓 coding agent 以精簡視覺化呈現取代大量文字輸出；兩個獨立來源同日報導 |
| [**youtube-skills**](https://github.com/ZeroPointRepo/youtube-skills) | Skills | ⏳ | 2026-08-12 | 供 AI agent 使用的 YouTube 字幕擷取 skill，相容 OpenClaw、Hermes-Agent、Claude Code、Cursor、Windsurf；506 星，已查證非刷星（forks 10.7%） |
| [**devspace**](https://github.com/Waishnav/devspace) | 整合工具 | ⏳ | 2026-08-11 | 把 ChatGPT 網頁介面／Claude Web 轉換成類 Codex／Claude Code 的操作體驗；3,675 星，已查證非刷星（forks 10.9%） |
| [**smart-ralph**](https://github.com/tzachbon/smart-ralph) | 工作流 | ⏳ | 2026-08-11 | 結合 Ralph Wiggum loop 與結構化規格流程的 Claude Code plugin，主打規格驅動開發與智慧壓縮 compaction；510 星，已查證非刷星（forks 9.0%） |
| [**headroom-desktop**](https://github.com/gglucass/headroom-desktop) | 費用監測 | ⏳ | 2026-08-11 | macOS 桌面工具，本機壓縮 pipeline 攔截 prompt 移除 tool output／log／樣板文字；已查證整體 session 平均省約 15–25% token（非宣傳的 50%）；508 星，已查證非刷星 |
| [**ospec**](https://github.com/clawplays/ospec) | 工作流 | ⏳ | 2026-08-11 | 規格驅動 agentic 工作流框架，「規劃—執行—驗證」可驗證目標迴圈，相容 Claude Code、Codex、Gemini、OpenCode；502 星，forks 比例 6.0% 低於防刷佐證基準，刷星可能性未能完全排除 |
| [**loopx**](https://github.com/huangruiteng/loopx) | 多 Agent | ⏳ | 2026-08-09 | 輕量級 loop 工程狀態核心，持久目標、配額感知自動喚醒、可執行待辦、證據紀錄與可驗證交接，agent-loop agnostic；4,476 星，已查證非刷星（forks 8.6%） |
| [**HarnessFlow**](https://github.com/HangYu8123/HarnessFlow) | 多 Agent | ⏳ | 2026-08-09 | 鎖定 Codex、Claude、GitHub Copilot 的通用 coding workflow harness；482 星，forks 比例 6.8% 低於防刷佐證基準，僅近期 commit 一項佐證 |
| [**omnigent**](https://github.com/omnigent-ai/omnigent) | 多 Agent | ⏳ | 2026-08-05 | harness 無關 meta-harness，換底層 agent（Claude Code／Codex／Cursor／Pi）不必重寫協作邏輯；9,080 星（08-05 查證非刷星時為 8,150 星，forks 14.7%），持續成長 |
| [**pxpipe**](https://github.com/teamchong/pxpipe) | 費用監測 | ⏳ | 2026-08-05 | 把文字 context 渲染成圖片降低 token 用量，實測約 25,000 text token 壓至 2,700 image token；6,955 星，已查證非刷星（forks 8.5%） |
| [**Wallfacer**](https://github.com/pradipta/wallfacer) | 多 Agent | ⏳ | 2026-08-07 | Claude Code 專用終端機 session 管理工具；Show HN score 35，source_count 2（跨來源佐證） |
| [**HUD**](https://github.com/adrida/hud-mode) | IDE/終端 | ⏳ | 2026-08-07 | 開源極簡終端 UI，支援 Claude Code／Codex／OpenCode；經官方 JSON event stream 運作不額外耗 token；HN 25 |
| [**Cockpit**](https://episko.dev/) | 多 Agent | ⏳ | 2026-08-02 | Rust 打造的 Claude Code 多 Agent 監控主控台，彙整多個 agent／session／專案執行狀態於單一介面；HN score 11，source_count 2 |
| [**claude-workflow-v2**](https://github.com/CloudAI-X/claude-workflow-v2) | 工作流 | ✅ | 2026-08-04 | 通用 Claude Code 工作流插件（7 agents+26 commands+14 skills+14 hooks），1.4k 星／188 forks，達廣泛採用（非 pipeline 進料，人工查證收錄）|
| [**Claude Code Merge Queue**](https://github.com/funador/claude-code-merge-queue) | 多 Agent | ⏳ | 2026-07-30 | 讓多個平行 agent 的 commit 排隊依序落地、逐一建置測試後才合併，緩解低規格機器同時建置的資源競爭；HN 39 |
| [**Sx 2.0**](https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html) | Skills | ⚡ | 2026-07-13 | 透過 Dropbox / Google Drive / iCloud 免 git 分享 Claude/Codex skill；2.0 版新增原生 app 與 Skill Evals；Show HN score 39 |
| [**Geosql**](https://github.com/dekart-xyz/geosql) | Skills | ✅ | 2026-07-08 | Claude/Codex/Copilot 地理空間資料 skill（PostGIS／BigQuery／Snowflake）；「4 倍效能提升」機制已查證，見下方懸置細節 ⟨Q-01⟩（HN score 55） |
| [**Workweave Router**](https://github.com/workweave/router) | 模型路由 | ⚡ | 2026-06-27 | 成本感知模型路由器，作為 Anthropic/OpenAI 相容 endpoint 運作，依請求難度自動路由模型；起因 Opus 4.7 tokenizer 改版後成本大漲；實測成本降 40%+；Show HN score 181 |
| [**bulk-delete-claude-chat**](https://github.com/MatteoLeonesi/bulk-delete-claude-chat) | UI 工具 | ⚡ | 2026-06-13 | 解決 Claude 網頁版缺乏批量刪除對話功能的痛點；自動捲動、全選、刪除（對比 ChatGPT 已有內建批量刪除）；HN score 56 |
| [**AVP（Agent Vault Proxy）**](https://github.com/inflightsec/agent-vault-proxy) | 安全工具 | ⚡ | 2026-06-12 | 解決 coding agent 持有 API key 的安全風險；placeholder + 最後一刻注入，agent 環境只存 placeholder，真實金鑰在 wire 層即時替換；Show HN |
| [**Workplane**](https://workplane.co) | 整合工具 | ⚡ | 2026-06-12 | 解決 Claude/Codex 輸出的 .md/.html 檔案難以分享問題；支援版本回滾與 MCP 整合，Claude Desktop／Code／OpenClaw 均可存取共享資料夾；Show HN |
| [**Minicor**](https://www.minicor.com/) | 工作流 | ⚡ | 2026-05-27 | YC P26 新創，AI 公司整合無 API 桌面系統（Windows RPA）的可擴展基礎設施；HN score 98 |
| [**Superset**](https://github.com/superset-sh/superset) | 多 Agent | ⚡ | 2026-05-23 | YC P26 開源 agentic IDE，同時平行運行 Claude Code／Codex／OpenCode，底層以 git worktree 隔離各 agent 工作區；Show HN |
| [**VIR**](https://www.reddit.com/r/ClaudeAI/comments/1tlcai2/) | 記憶工具 | ⚡ | 2026-05-23 | 背景讀取 `~/.claude/projects` session 檔萃取知識（pattern/gotcha/decision/tool），寫入 Obsidian vault 供 MCP 存取，解決記憶歸零問題 |
| [**CoreMem**](https://coremem.app) | 記憶工具 | ⚡ | 2026-05-23 | 集中管理跨 agent、跨 session 的 context（專案細節、寫作風格、技術偏好），可透過 URL、Chrome extension、MCP、VS Code plugin 讓任何 AI 工具存取 |
| [**Shortcuts Playground**](https://www.macstories.net/stories/introducing-shortcuts-playground/) | Skills | ⚡ | 2026-05-23 | Claude Code / Codex 開源 plugin，用自然語言描述即可生成 Apple Shortcuts；MacStories 出品，完整文件化，直接指向 plugin repo 即可安裝；Show HN 發布 |
| [**agent-teamflow**](https://www.reddit.com/r/ClaudeAI/comments/1tkl3z6/) | 多 Agent | ⚡ | 2026-05-22 | 9 個 slash commands + 分支命名慣例，讓多位開發者的 Claude Code agent 平行運作且不互相踩踏，每人有獨立 staging 分支；實習生開源 |
| [**Proof Loop**](https://github.com/LeoStehlik/proof-loop) | 工作流 | ⚡ | 2026-05-22 | 針對 agent 謊報任務完成的問題：要求設定驗收標準、分離建構者與驗證者角色、每項標準記錄 PASS/FAIL/UNKNOWN 結果並附證據；Show HN 發布 |
| [**agent-estimate**](https://github.com/kiloloop/agent-estimate) | 費用監測 | ⚡ | 2026-05-22 | 解決「Claude Code 估算時間基於人類速度訓練資料」問題，以 PERT 方法論搭配 agent 速度乘數，提供 XS–XL 任務分類及可靠度警示；Show HN 發布 |
| [**engramx**](https://www.reddit.com/r/ClaudeAI/comments/1tka3no/) | 費用監測 | ⚡ | 2026-05-22 | context 過濾層，防止 session 重讀整個 repo 導致帳單暴增；引用 Karpathy 「最小必要 context」原則，已有 Skill Pack v4.0.0（89.1% token 減少）實測記錄 |
| [**DPlex**](https://www.reddit.com/r/ClaudeAI/comments/1tkhd3l/) | IDE/終端 | ⚡ | 2026-05-22 | 針對 AI 輔助開發設計的終端機多工器，解決多個 Claude Code / Copilot CLI session 跨視窗管理的狀態消失問題，重啟後可還原完整佈局 |
| [**ChunkHound v5.1**](https://www.reddit.com/r/ClaudeAI/comments/1tkkxmk/) | 搜尋/診斷 | ⚡ | 2026-05-22 | 更新：MCP 多客戶端共用單一 DuckDB 連線、搜尋結果改為 token 效率更高的 Markdown 格式，新增 Elixir/Dart/Lua/SQL/HTML/CSS 語言支援 |
| [**clarp**](https://www.reddit.com/r/ClaudeAI/comments/1tj2exk/claude_p_is_moving_to_metered_pricing_on_june_15/) | 費用監測 | ⚡ | 2026-05-21 | `claude -p` drop-in 替代品，本地 PTY + 唯讀 API 代理，規避 6/15 計量計費，多數專案只需更換 binary 名稱 |
| [**vibe-skill**](https://www.reddit.com/r/ClaudeAI/comments/1tjfyh0/i_used_claude_code_to_build_while_delegating/) | 費用監測 | ⚡ | 2026-05-21 | Claude 負責規劃 + diff 審查，實際撰碼委派 Mistral Vibe；10 天實測節省 57M tokens，成本降逾 90% |
| [**TokenShield**](https://www.npmjs.com/package/@curatedmcp/tokenshield) | 費用監測 | ⚡ | 2026-05-20 | 本地 Node.js proxy，攔截送往 api.anthropic.com 的請求並去除重複的 tool_result 內容（同一檔案多次被讀等情況），宣稱可減少 40–70% 的 Claude Code 費用；npmjs 發布 |
| [**Logbox**](https://github.com/struct-dot-ai/logbox) | 整合工具 | ⚡ | 2026-05-20 | 將 dev server log 導入本地 SQLite，再透過 MCP 讓 Claude Code 直接查詢，解決 Claude 無法即時追蹤 log 流的問題；Show HN 發布 |
| [**PrismoDev**](https://github.com/shanirsh/prismodev) | 搜尋/診斷 | ⚡ | 2026-05-20 | 掃描本地 session log，找出 context bloat 來源（過大 CLAUDE.md、重複 tool output、broad exploration），不需 API key、本地離線；Show HN |
| [**mdviewer**](https://github.com/rajatarya/mdviewer) | 其他 | ⚡ | 2026-05-20 | 100% 由 AI coding agent 完成的原生 macOS Markdown 閱覽器，支援 Obsidian 延伸語法／Mermaid／數學公式，以 Tauri 2 打造無 Electron 依賴；Show HN |
| [**cdesktop**](https://www.reddit.com/r/ClaudeAI/comments/1thlxrw/cdesktop_opensource_claude_code_desktop/) | 多 Agent | ⚡ | 2026-05-19 | 開源桌面應用，單一 UI 整合 Claude Code／Codex／Gemini CLI 等 5 個 coding agent，支援 20+ 第三方模型，`npx` 執行 |
| [**AnyFrame**](https://anyfrm.com) | 安全工具 | ⚡ | 2026-05-18 | 為 Claude Code/Codex 提供微 VM 沙盒環境，一次定義 Agent 並快取映像檔，支援 Python SDK／Web 介面，可整合 Linear/Sentry MCP；Show HN |
| [**agent-baton**](https://www.reddit.com/r/ClaudeAI/comments/1tgel55/) | 費用監測 | ⚡ | 2026-05-18 | 利用 Anthropic 使用量 API + Claude Code hook，在觸及速率上限前主動發出警告並轉移進行中的工作，解決 Claude Code 靜默中斷的長期痛點 |
| [**LockedIn**](https://www.reddit.com/r/ClaudeAI/comments/1tg8yg6/) | 記憶工具 | ⚡ | 2026-05-18 | Claude Code 插件（1 路由技能 + 6 子技能），在 session 中持續記錄開發者工作脈絡，下次對話的 Claude 可直接繼承上次進度，無需重新說明背景 |
| **Claude Usage Widget** | 費用監測 | ✅ | 2026-05-18 | 浮動桌面小工具，讀取 Anthropic 速率限制 API 標頭，即時顯示 5 小時 session 使用量（含色彩進度條）、每週配額、token 輸入輸出統計，每 5 秒更新，支援 Windows + macOS |
| [**CostHawk 排行榜**](https://costhawk.ai/leaderboard) | 費用監測 | ⚡ | 2026-05-16 | 公開 token 消耗排行榜，比較 Claude Code / Codex / Cursor 用戶用量，不儲存 prompt |
| [**Dragoman**](https://github.com/asakin/dragoman) | 多 Agent | ⚡ | 2026-05-13 | 多模型路由 CLI，依問題類型自動路由至 Perplexity/Gemini/Ollama，支援 4 模型並行 + Claude 彙整 |
| [**Cocall.ai**](https://www.reddit.com/r/ClaudeAI/comments/1tbz13b/) | 整合工具 | ⚡ | 2026-05-13 | AI 代理撥打外線電話，遇不確定問題自動暫停詢問使用者再繼續，全雙工語音，支援 IVR 導航 |
| [**Writ**](https://www.reddit.com/r/ClaudeAI/comments/1tb047p/) | 工作流 | ⚡ | 2026-05-12 | Neo4j 知識圖譜 5 階段 Pipeline 自動擷取相關規則集，解決 CLAUDE.md 被忽略 + 無關規則耗 token 雙重問題 |
| [**ltm**](https://www.reddit.com/r/ClaudeAI/comments/1tb0nwk/) | 記憶工具 | ⚡ | 2026-05-12 | Core Memory Packet JSON 協定，跨編輯器 / 跨機器 / 跨模型的供應商中立 Agent 記憶 |
| [**Usage4Claude 3.0.0**](https://www.reddit.com/r/ClaudeAI/comments/1tazqpg/) | 費用監測 | ✅ | 2026-05-12 | 開源 macOS 選單列用量追蹤，3.0.0 版新增 Codex 追蹤，憑證存 Keychain |
| **adamsreview** | 工作流 | ⚡ | 2026-05-11 | 多代理 PR review，平行子代理 + 多階段驗證，作者聲稱比官方 /review、/ultrareview、CodeRabbit 捕捉更多真實 bug |
| **vibe-log-cli** | 工作流 | ⚡ | 2026-05-11 | Claude Code 插件自動生成每日 / 每週開發工作摘要，適合 vibe coding 長期用戶 |
| **Tokenyst** | 費用監測 | ⚡ | 2026-05-10 | Claude Code pay-as-you-go 任務層級 token 預算設定，每次提示後即時顯示剩餘額度與使用比例 |
| **Remind** | 工作流 | ⚡ | 2026-05-10 | Mac 本機排程 Claude Code，用「提醒事項」App 指定時間觸發，支援 iPhone/Apple Watch，可續接既有 session |
| **draft CLI plugin** | 記憶工具 | ⚡ | 2026-05-10 | session-init hook 自動注入結構化產品上下文摘要，解決跨 session 記憶歸零，不呼叫額外 API |
| **re_gent** | 工作流 | ⚡ | 2026-05-09 | AI agent 版本控制工具（Git for AI Agents），解決 /compact 後歷史斷層與決策追溯，已支援 Claude Code |
| **obsidian-semantic** | 記憶工具 | ⚡ | 2026-05-09 | 讓 Claude Code 以語義搜尋使用 Obsidian vault，支援 Ollama/LMStudio/Gemini |
| **Claudy** | 多 Agent | ⚡ | 2026-05-08 | Rust 撰寫，多供應商設定檔一鍵切換（Anthropic/Gemini/Codex）、本地代理 MCP 橋接、token 用量分析 |
| **DataMoat** | 安全工具 | ⚡ | 2026-05-08 | AES-256-GCM 加密工作記錄為本機私有資產，支援搜尋/重用/移交，vault 金鑰完全留在本機 |
| **4-agent Code Review** | 工作流 | ⚡ | 2026-05-08 | 架構師代理（純協調）+ 三模型廠商專家代理，審查意見需具體證據，可包裝為 MCP 替代 CodeRabbit，MIT |
| **awesome-ux-skills** | Skills | ⚡ | 2026-05-08 | Nielsen + Shape of AI 等 UX 原則技能集，供設計導向工程師重複使用 |
| [**BrowserCode**](https://github.com/leaningtech/browsercode) | IDE/終端 | ⚡ | 2026-05-07 | WebAssembly 瀏覽器執行 Claude Code，支援行動裝置，讓 iPad、鎖定設備也能使用 CLI 功能 |
| **/qu /ans 跨 session 插件** | 多 Agent | ⚡ | 2026-05-07 | 兩個 Claude Code session 直接雙向問答，省去人工跨 session 複製貼上 |
| **recap** | 工作流 | ⚡ | 2026-05-07 | 掃描 Claude Code + Codex 對話，自動產出陌生概念說明摘要，主動對抗 AI 開發 skill atrophy |
| **Kstack** | 整合工具 | ⚡ | 2026-05-07 | K8s 監控/除錯/安全審計 skill pack（/investigate、/audit-security、/audit-outdated） |
| **Claude Code Routines** | 工作流 | ⚡ | 2026-05-07 | 排程 agent 任務（commit 摘要、依賴掃描、日誌彙整），核心優勢是 Agent 能對結果推理而非固定指令 |
| **Claudette** | 工作流 | ⚡ | 2026-05-06 | 每個 agent 獨立 git worktree + session + 終端機，speculative parallelism 工作流，HN 討論活躍 |
| **claude-smart** | 記憶工具 | ⚡ | 2026-05-06 | 將用戶糾正泛化為跨專案通用規則，解決同樣錯誤反覆出現的問題 |
| [**Claude Relay**](https://www.reddit.com/r/ClaudeAI/comments/1tb0nwk/) | 多 Agent | ⚡ | 2026-05-05 | 讓多個本地 Claude Code session 互相傳訊查詢，省去人工跨 session 複製貼上 |
| **Memex** | 記憶工具 | ⚡ | 2026-05-05 | 本地 RAG + 離線 embedding 持久記憶，MCP 接入，所有資料留存本機無需雲端 |
| **Claude-Find** | 搜尋/診斷 | ⚡ | 2026-05-05 | 語義搜尋跨 session 決策脈絡，解決 /resume 只能依名稱篩選的痛點 |
| **Askdiff** | 工作流 | ⚡ | 2026-05-05 | diff 介面直接問生成此程式碼的 Claude Code session，串流取得原始決策理由 |
| [**Semble**](https://github.com/MinishLab/semble) | 搜尋/診斷 | ⚡ | 2026-05-04 | 專為 Claude Code 等 Agent 優化的程式碼搜尋工具，結合 Model2Vec 靜態嵌入 + BM25 融合檢索，宣稱比 grep 節省 98% token；Show HN 發布 |
| **Kirikiri** | IDE/終端 | ⚡ | 2026-05-04 | iOS 開源 mobile IDE，Flutter+dartssh2，透過 SSH/Google Cloud Shell 執行 Claude Code |
| **Prism MCP** | 整合工具 | ⚡ | 2026-05-04 | VS Code LSP 橋接 Claude Code，讓 AI 以語義方式瀏覽程式碼（已上 Marketplace） |
| **claudely** | 多 Agent | ⚡ | 2026-05-04 | 保留 Claude Code 生態的前提下切換至 Ollama/LM Studio/llama.cpp，無需改主配置 |
| **Smithy** | 整合工具 | ⚡ | 2026-05-04 | 從 Jira/GitLab/Forgejo 觸發容器化 Claude Code session，自動開 PR、響應 CI |
| **Patina** | 工作流 | ⚡ | 2026-05-04 | CLAUDE.md retro loop 維護 CLI，防止 AI harness 配置「腐化」（MIT，已上 npm） |
| **Pilot Shell** | 工作流 | ⚡ | 2026-05-04 | /spec（TDD）、/fix（複雜度偵測自動中止）、/prd（需求文件）三指令工程紀律框架 |
| [**Omar**](https://omar.tech) | IDE/終端 | ✅ | 2026-05-02 | TUI 儀表板統一管理 100 個 Claude Code Agent，支援層級化 Agent 管理 |
| **graphify** | 記憶工具 | ✅ | 2026-05-02 | Leiden 偵測建程式碼知識圖譜，71 倍 token 減少，26 天 450k+ 下載 40k stars |
| [**NanoBrain**](https://nanobrain.app/) | 記憶工具 | ⚡ | 2026-05-02 | git-backed Markdown 知識庫，< 50ms append，整合 Gmail/Calendar/Slack |
| **Council** | 多 Agent | ⚡ | 2026-05-02 | 並行執行 claude+codex+gemini 同一 prompt，主持模型彙整並標記分歧 |
| **Chrome 用量監控擴充** | 費用監測 | ✅ | 2026-05-02 | 即時顯示 token 數、context 使用量、prompt cache 倒數、速率限制進度條 |
| **Caliber** | 工作流 | ⚡ | 2026-05-02 | 跨工具 AI config 統一管理（CLAUDE.md/.cursor/rules/AGENTS.md），本週 888 stars |
| [**Governor**](https://github.com/0xhimanshu/governor) | 費用監測 | ⚡ | 2026-05-02 | Token 浪費優化插件；已查證：V2 benchmark 同時量測 token 數與「決策正確度保留率」回應 HN 對基準粗糙的質疑，平均省 45.5% token（2026-08-13 查證） |
| **Throttle Meter** | 費用監測 | ⚡ | 2026-04-30 | macOS menubar 用量計，即時顯示 5h 滾動窗口與週配額 |
| **Brifly** | 記憶工具 | ⚡ | 2026-04-30 | Claude Code 跨 session 持久記憶層，支援多人協作 |
| **Mneme** | 工作流 | ⚡ | 2026-04-30 | repo-native ADR 注入，CI 攔截違反架構的 PR |
| **Nimbalyst** | 多 Agent | ⚡ | 2026-04-30 | 多 agent 視覺化工作台，WYSIWYG diff 逐一審核各 Agent 修改 |
| **Trent** | 安全工具 | ⚡ | 2026-04-30 | Claude Code 內嵌架構層安全評估，補足 CVE 掃描對業務邏輯的盲點 |
| [**Harness**](https://github.com/frenchie4111/harness) | 多 Agent | ✅ | 2026-04-29 | 多 Git worktree 並行管理多個 Claude Code agent，補 cmux/Conductor 不足 |
| **CodeThis** | 整合工具 | ⚡ | 2026-04-29 | MCP 原生 paste bin，AI 可直接建立語法高亮程式碼分享貼文 |
| **Claude Exporter** | 整合工具 | ⚡ | 2026-04-29 | Chrome 擴充功能，對話匯出 PDF/Word/Notion，填補持久化需求 |
| **Jupyter MCP server** | 整合工具 | ⚡ | 2026-04-28 | 取代內建 NotebookEdit，支援完整 kernel 互動與輸出讀取 |
| **PullMD** | 整合工具 | ⚡ | 2026-04-28 | 網頁抓取時先轉 Markdown，避免 token 浪費（有效內容僅佔 HTML 約 20%） |
| [**Groundtruth**](https://github.com/vnmoorthy/groundtruth) | 工作流 | ⚡ | 2026-04-27 | Stop Hook，強制 Claude 提供可驗證執行證明才能宣告完成 |
| **EvanFlow** | 工作流 | ⚡ | 2026-04-27 | TDD 驅動迴圈，16 技能 + 2 子代理人，每步人工確認，不自動 commit |
| **Relay plugin** | 工作流 | ⚡ | 2026-04-27 | 強制 Claude Code 先對齊問題本質再動手，Plan Mode 提問升級 |
| **SmolVM** | 安全工具 | ⚡ | 2026-04-27 | 本機沙盒執行 Claude Code / Codex，單指令啟動，保護宿主系統 |
| **Rapunzel** | IDE/終端 | ⚡ | 2026-04-27 | 樹狀標籤頁多代理瀏覽器，支援 Claude Code / Codex / Gemini |
| **OpenCode-power-pack** | 整合工具 | ⚡ | 2026-04-27 | 11 個 Claude Code 官方技能移植至 OpenCode，打破工具綁定 |
| [**Claude Squad**](https://www.reddit.com/r/ClaudeAI/comments/1svmpkv/) | 多 Agent | ✅ | 2026-04-26 | 多人多 agent 並行開發，orchestrator 分派任務並合併分支 |
| [**mux0**](https://mux0.com/) | IDE/終端 | ✅ | 2026-04-26 | 開源 macOS 終端，側邊欄即時顯示多 agent 狀態 |
| **CC-Canary** | 工作流 | ✅ | 2026-04-25 | 讀取 session log 自動偵測效能漂移，HERMES.md bug 後更受重視；詳見 [[topics/code-quality-decline]] |

**收錄註記**（表內「見收錄註記」的三筆）
- **andrej-karpathy-skills**（08-29）：僅 GitHub Search 星數，無 forks／issues 佐證可查，增速異常值得存疑，不作為獨立驗證訊號。
- **gstack**（08-30）：13.0 萬星僅用 5.5 個月達成，增速明顯快於同類存量盤點案例，星數真實性未經驗證；作者具名且內容具體故收錄。
- **internet-court-skill**（08-18 收錄，09-02 更新星數）：5,317 星，前次 08-18 為 3,793 星；無出生日期標記、無 forks／issues 佐證可查。

**懸置細節**
- ⟨Q-01⟩ 已查證（2026-08-13）：「4 倍」宣稱的機制已釐清數據不一致的來源——GeoSQL 讓 agent 把空間查詢結果透過 Dekart 渲染成地圖並回看修正幾何錯誤（map-in-the-loop），4 倍準確度提升**只在連接 Dekart 時成立**；未連接 Dekart 時 GeoSQL 表現與一般 SQL agent 相當，先前細部任務成功率數據加總不一致即源於部分任務未啟用 Dekart 視覺回饋（[dekart.xyz 部落格](https://dekart.xyz/blog/claude-code-vs-aino-geospatial-agent/)、[Show HN](https://news.ycombinator.com/item?id=48829242)）；詳見 [[topics/community-tech-discussions]]

---

## 參考來源

- [[topics/community-tech-patterns]] — 工作流模式與技術做法
- [[topics/community-tech-discussions]] — 概念辯論與設計哲學
- [[topics/official-community-gap]] — 官方 vs 社群缺口分析
- [[feature-radar]] — 官方功能熱度雷達
