---
page: "topics/community-large-codebase-workflow"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-08-15"
last_news_update: "2026-08-15"
status_main: "ongoing"
days_since_news: 0
inbound_links: 11
attribution_count: 2
attribution_last: "2026-08-05"
top_source: "reddit"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 大型 Codebase 規模化開發：社群工作流主線

**狀態：** ongoing
**領域：** 🌐 社群
**開始日期：** 2026-05-02
**最後更新：** 2026-08-15
**最後新聞更新：** 2026-08-15

> **最新進展**（2026-08-15）
> 「除錯與分工架構」線出現第一個直接針對「subagent 回報是否屬實」缺口設計的工具：loopx（4,476 星，已確認非刷星）以「證據紀錄＋可驗證交接」要求每個任務單元交接時附上可查核的證據——把驗證從事後人工複核往前挪了一步，但尚無使用回饋證明它真能降低虛報。其餘三條線結論不變。

---

## 摘要

Claude Code 熟手在小型專案上已經摸熟的做法——單一 CLAUDE.md、單一 session、讀完整檔案——一旦搬進大型 codebase 就開始失靈：並行 agent 數量一多就互踩、context window 被 40k+ token 的工具輸出擠爆、agent 記不住昨天已經做過的架構決策、多 agent 產出的程式碼誰來把關也沒有定論。本頁把 [[topics/community-tech-patterns]] 中散落各日、原本各自獨立記錄的節點，依「規模」「記憶」「品質」三個 codebase 特有的痛點軸，縫成四條可讀的主線，回答「社群在大型 codebase 上實際卡在哪、試過什麼、目前收斂到哪」——讀者不必逐條翻找日期。

每條主線的節點證據與出處仍以 [[topics/community-tech-patterns]] 為準（本頁不複製條目全文，只做敘事與索引）；官方對應機制（plan mode、subagent、`/context`、LSP 等）見 [[entities/claude-code]] 與 [[entities/managed-agents]]，此處僅加註對照、不重寫官方文件。

| 主線 | 核心問題 | 目前收斂點 |
|------|---------|-----------|
| 並行規模的極限與對策 | 幾個 agent 同時跑，什麼時候會互相踩到？ | worktree 隔離是共識，「協調層」「可觀測性」與「落地整合序列化」仍在補洞 |
| Context / Token 管理 | 大 codebase 的檔案/工具輸出量遠超小專案，context 怎麼不被撐爆？ | 「先測量再歸因」+「即時取回優於預先加載」已成常識性共識，CLAUDE.md 取捨也收斂為觸發頻率判準 |
| Codebase 索引與記憶 | codebase 太大、太久，agent（和文件）怎麼記得住？ | 記憶方案從「跨 session 記決策」擴散到「codebase 文件自動維護」 |
| 除錯與分工架構 | 多 agent／多人協作在大 repo 上，誰負責審、誰負責錯誤歸因？ | 「唯讀審查者」與「工具範圍限制」比「角色描述」更可靠；「回報是否屬實」的驗證缺口剛出現第一個工具化嘗試 |

---

## 技術彙整

### 1. 並行規模的極限與對策

**這條線在解什麼問題：** 小型專案上開 2、3 個 Claude Code session 靠人工就能管理；大型 codebase 一旦想榨出真正的規模效益（同時改多個模組、同時測多份 PR），並行數量很快超過人工可監督的上限，此時「共享資源競爭」「context 洩漏至鄰近 agent」「缺乏協調層」開始集中爆發。

**隔離原語：從 OS 帳號走到 git worktree。** 最早的隔離手法是作業系統帳號隔離——讓兩個 Claude Code 代理在同一台 VPS 上以獨立 OS 用戶運作，各自開 PR、發通知，「爆炸半徑」被限制在帳號權限範圍內。很快就被更輕量的原語取代：Claudette 讓每個 agent 擁有獨立 git worktree + session + 終端機（speculative parallelism，多分支同時跑、互不干擾）；「Git Worktrees 作為多 Agent 隔離原語」把做法正式定名，指出它比 OS 帳號更輕、更適合 CI/CD；Superset 把分配 worktree 自動化；cc-fleet 與「串行 vs 並行工作流」把「識別可平行的任務 DAG」總結為可複用步驟；「Multi-agent 工作流轉型指南」則點明**獨立工作空間是並行的前提**——沒有它，代理互相覆蓋會直接讓工作流崩潰。後續「動態工作流與 1000 Subagents Fan-out」再把靜態預先分配推向「執行時動態決定分支數量」。

**規模上限：官方展示與社群實測之間的落差。** 官方層面 Managed Agents 原生支援 **20 路並行子代理**（見 [[entities/managed-agents]]），Boris Cherny 隨後公開「每晚讓數千個子代理執行深度工作」的工作流（見 [[entities/boris-cherny]]），被主流媒體報導、帶動「大規模並行能撐多大」的討論。社群實測給出另一端的答案：《Why 20 Claude Code Instances Break Down》具體拆解從 4 個擴到 20 個 agent 時的崩潰主因——共享資源競爭（git lock、資料庫連線）、context 洩漏、缺乏協調層——主張每次倍增規模都要重新驗證協調機制，而非線性外推；1000 fan-out 教學自己也提醒「千級為理論上限，建議先從 10–20 個驗證協調架構」，等於呼應了崩潰分析。**官方展示的規模上限與社群實測會崩潰的規模下限之間，有一段落差尚未被填平**（推論）。Mac Mini M4 無人監督自主部署則把討論延伸到「消費級硬體上長期背景運行」。

**可觀測性：已確立為固定需求。** 規模一大，人工盯進度本身就變成瓶頸。從讀取本機 JSONL transcript 做多 agent 即時「對話地圖」（live-log-viewer-next）開始，Topsoil、Fleet Deck、Cockpit（Rust 主控台）、Wallfacer、HUD 陸續出現——跨 32 天累積 **6 個獨立實作**，單日甚至同時有 2 款同題工具亮相，已達獨立成形趨勢的門檻。技術路徑初步分化為「讀官方 event stream」（HUD，較穩健）與「自行解析 transcript／獨立主控台」（其餘 5 者）兩條；完整清單見 [[topics/community-pattern-trends]]「趨勢六：多 Agent 可觀測性儀表板化」。

**落地整合序列化：新浮現的下游瓶頸。** 多個平行 agent 同時產出的 commit 落地時，若各分支同時觸發建置與測試，資源與 CI 帳單都撐不住。「本地合併佇列」記錄作者以 4–5 個平行 agent 在 8GB MacBook Air 上每天推送近 90 次 commit 的實測，改用佇列讓提交依序落地、逐一完整建置測試後才合併下一筆——這是「協調層」之外首次出現的整合序列化對策。

**目前收斂點：** worktree（或等價的檔案系統隔離）作為並行原語已是共識；官方 20 路與社群千級宣稱之間的落差仍未系統性驗證；可觀測性已從「補洞中」升級為確立需求，且補位速度正在加快；落地整合序列化是新的下游子問題——尚未出現能同時滿足「規模夠大」與「崩潰率可控」的定論做法。

---

### 2. Context / Token 管理

**這條線在解什麼問題：** 大型 codebase 的檔案數量、歷史 commit、工具輸出量遠超小型專案，若延用小專案「把可能相關的檔案都讀進來」的直覺做法，context window 很快被撐爆、模型「越用越笨」；這是大 codebase 特有的規模問題。

**路由與極簡輸出：最早的降耗嘗試。** 「Token 路由與成本優化」用 CLAUDE.md 規則把批量文件讀取、樣板生成等機械性任務導向低成本模型，對話性推理才留給旗艦模型。「Token 大量降耗策略」把重點轉向「從 context 管理入手，而非壓縮 prompt 本身」，Caveman Skill 給出 65% 降耗的實測數字；404 Media 報導的「企業穴居人模式」證實 OpenAI、Nvidia、GitHub 開發者已把極簡輸出當成企業級降本策略，後續 CaveMan Skill 新實作再把單次回覆從約 70 token 壓到約 20——這是一個持續被重新實作的活躍模式，不是單一案例。

**MCP 成本：從直覺到數字。** 「MCP Code Execution Token 效率」點出大量 MCP 伺服器的靜態工具清單會讓 context 在第一條訊息前就半滿；「MCP Server 信任邊界審查」補上具體數字（9 個 server = 每輪 38k tokens 冷啟動）；「MCP Server 設計對每輪對話隱藏 token 成本的實測比較」則是第一手量化實測，比較工具清單、描述長度、回傳格式對 token 的實際影響。三者合起來把「MCP 越多、context 越貴」升級成有數字支撐的共識。

**按需取回，而非預先加載。** 這是本線最核心的原則。「Just-in-Time @-file Retrieval」把「預先 @-mention 所有可能用到的檔案」明確定性為反模式；「Agent Context 上限主動管理」補上另一半——不只「何時取回」，還要「取回多少」，用讀取上限搭配索引/摘要層避免為回答單一問題讀 56KB 文件。同一原則的工具化包括：Git Lazy Mount 讓 1GB+ monorepo 的 AI session 按需 fetch、附 sgrep 繞過全量 grep；「本機圖資料庫」指出快取不跨 session 是 pay-as-you-go 用戶單次 session 費用達 $6–10 的主因，改讓模型只讀結構化摘要；Tokenyst 補上任務層級的即時 token 預算顯示；「本地小模型分流」（Fast Context Task Router）把程式碼探索委派給本地小 LLM，聲稱省 50–60% context token、代價是延遲（該專案原由 Microsoft 發布後已下架，機制僅存二手驗證）。「Compact Memory」用可執行 benchmark 量化了不裁剪的代價：多數 agent 每輪重送完整 transcript，會在多輪任務造成 62.8%–85.9% 額外 context token、屬 O(N²) 增長；只保留當前任務所需的語意摘要可壓回接近 O(N)。一系列 CLAUDE.md／loop 模式（Loop Engineering、規則總量上限、Context 裁剪 Tool Output）共同指向同一結論：**解決長 session 退化的關鍵是主動裁剪輸入，不是加更多 context**。

**CLAUDE.md 該裝什麼、有沒有被載入。** 「精簡 CLAUDE.md」的直覺被推進成可操作判準：CLAUDE.md 每次請求都自動載入，每一行都是對每個請求課的「context 稅」；一條 guidance 該放 CLAUDE.md／skill／hook／docs 哪一層，取決於它該多常觸發——四層寄放地依觸發頻率判斷。另一半問題是規則寫了卻沒被載入：依官方文件整理的四種記憶範圍載入順序指出 CLAUDE.local.md 在同層級共用 CLAUDE.md 之後載入（適合放個人化覆寫），受管理原則檔在 Linux／Windows 也存在但路徑不同於 macOS——大型 codebase 常見多層目錄，規則寫錯層級是「規則被忽略」的常見根因。兩者互補：一談內容歸屬、一談載入機制（[[topics/community-tech-patterns]] CLAUDE.md 管理類別）。

**先測量、再歸因。** 「Context Window 診斷法」是本線最實用的方法論收斂：作者原本直覺懷疑「變笨」是某個 MCP 佔用 context，實測後發現並非如此——先測量、再歸咎工具，呼應 [[topics/community-tech-discussions]] 的「越用越笨多為 context 腐蝕、非模型退步」共識。這個方法論的量測對象正在擴大：「headless Claude Code 冷啟動實測」指出 `claude -p` 未加 `--bare` 時，冷啟動固定載入約 15 萬 token 的系統提示、工具定義與預設 context——互動式單一 session 不明顯，但大型 codebase 常見的多 agent pipeline（CI、批次任務、fan-out）會大量重複發起 headless 呼叫，每次都吃一筆固定成本，是規模化後才被放大的隱性開銷（單一作者實測，數字待複現）。

**主流之外的兩個方向。** CCN 把精簡對象從工具輸出/文件延伸到**程式碼本體**——只清除 AI 模型留下的殘留註解，聲稱經 2,700 次迭代測試（未經第三方驗證）；pxpipe 則把「更精簡的文字」翻轉為「改變表徵形式」，將文字 context 渲染成圖片再傳遞，具體降耗比例與適用類型尚無公開數據，是本線唯一的圖片化取向探索。

**目前收斂點：** 「不預先加載、按需取回」與「先測量、再歸因」已是常識性共識；MCP 設計對 token 成本的影響已有量化數字；CLAUDE.md 取捨收斂為「觸發頻率決定寄放地」的四層判準；但「該裁多少」仍缺乏跨案例統一標準，多為個別作者的自訂閾值；「先測量」的適用範圍正從單次呼叫內部擴大到多 agent pipeline 反覆呼叫的**累積成本**；圖片化 context 尚屬單一案例。

---

### 3. Codebase 索引與記憶

**這條線在解什麼問題：** 大型 codebase 累積的架構決策、命名慣例、已修過的 bug 遠超單一 session 或單一開發者能記住的量；agent 每個 session 重新「猜」一次已知答案，既浪費 token 又容易重蹈覆轍——在跑了數月、數百次 session 的大 repo 上是持續性成本。

**問題本質：stateless agent 的新鮮度缺陷。** 「Agent Context 新鮮度問題」最早點名：長 session 中 agent 不斷重讀相同檔案、不記得程式碼修改歷史；Memtrace 提出「時間感知代碼庫表示層」的解法方向。

**本地優先的記憶方案是主流。** 同一目標下社群走出多條並行路徑：本地向量資料庫 + MCP 整合、39ms 檢索的自建方案，核心原則是「按需語義查詢，不把全部記憶塞進 context」；Iantha 用純 Markdown + git 存儲、不需向量 DB；「本機圖資料庫」改用 LLM 生成關係圖取代 AST 或 embedding；Memex 走本地 RAG + 離線 embedding（解決雲端記憶隱私疑慮）；session 搜尋從 Claude-Find（語義搜尋 session，解決 `/resume` 只能靠第一條訊息篩選的痛點）演進到 session-indexer（本地 SQLite 索引 transcript，跨 session 搜尋過去對話與決策）；Claude Relay 則處理多 session 互通。「本地小模型分流」（見上節）某種意義上也是記憶議題的變體——把「探索 codebase 找答案」分流出去，避免主 agent 每次從頭理解結構。

**跨工具可攜性：少數派探索。** CLAUDE.md、`.cursor/rules`、AGENTS.md 都是 Markdown，無法在工具間攜帶；ltm 改用 JSON 協定的 Core Memory Packet 解決跨編輯器、跨機器、跨模型的可攜問題；OKF 則走「格式規約」而非「工具驅動」——純 Markdown 可讀的格式標準，不綁定工具，定位介於 ltm 與 Memex 之間，適合多人共用同一工作流的團隊。

**統一框架：repo 才是記憶體。** 「Repo-as-Memory / Stop Using the Model as Your Memory」提出框架性主張——**repo 才是記憶體，模型只是工作者**，已確定的架構決策應外化到 CLAUDE.md、spec 檔、ADR，不該依賴模型跨 session 記住；它被視為統一解釋 CLAUDE.md、`/specs`、ADR 等既有做法的共同底層哲學（推論）。「Cross-repo Blast Radius 分析」把範圍從單一 repo 擴到 repo 之間：Claude Code 讀完整 clone、Cursor 讀相似度索引，兩者都看不到跨 repo 依賴圖，需另外串接 `nx graph`、Gradle dependency tree 在 session 開始前注入「改這個函式會影響 N 個下游服務」的知識。

**方向轉變的兩個訊號。** CodeAlmanac（YC S26）把「codebase wiki 隨對話自動更新」做成產品，取代手動維護的 MANUAL.md、DESIGN.md，本地執行、免費——它記憶的對象不是「agent 的個人記憶」，而是**「codebase 本身的說明文件」**，代表這條線正從「讓 agent 記得住」擴散到「讓文件不再腐化」，與 CLAUDE.md 管理類別的「防腐爛」精神相通（推論）。另一則「已否決方案的隱形重工成本」指出 agent 會重新實作團隊已明確否決的方案，根因是「已被否決」這件事只存在於人類記憶或散落討論串，未被結構化記錄進 agent 可讀的知識來源——既有做法多談「記住怎麼做」，這則補上「記住什麼不該再做一次」也是記憶缺口，代價是直接可見的重工（概念性觀察，尚無工具或量化案例）。

**目前收斂點：** 本地優先（向量 DB / 圖資料庫 / SQLite / 純 Markdown）是主流，跨工具可攜性仍是少數派；「codebase 文件自動維護」是新方向但只有 CodeAlmanac 一個案例，未見第二個獨立佐證；「已否決方案索引」停留在問題點名階段，尚無對應工具。

---

### 4. 除錯與分工架構

**這條線在解什麼問題：** 大型 codebase 上，多 agent（或人 + agent 混合）協作寫程式後，誰來把關品質、誰負責追蹤某個 bug 的形狀與根因，比小型單人專案複雜得多——單一 Claude 自審自批容易對自己的計畫照單全收（affirmative bias），多 agent 產出的變更也需要跨 agent 一致的邊界規則才不會互相踩線。

**邊界規則與可追溯性。** 「Multi-agent CLAUDE.md 衝突防範」是最早的系統性嘗試：11 條規則涵蓋獨立工作區邊界、禁止跨 agent 直接修改共享狀態、明確指定 merge 責任的 orchestrator、每個 agent 的讀/寫範圍白名單。「PostToolUse 生產稽核日誌」把除錯延伸到事後可追溯：用 hook 逐筆記錄工具呼叫的 Bash 指令與目標 repo，回答「代理上週三下午 3 點到底執行了什麼」，適用合規稽核。「Git Log 作為除錯首要步驟」則點出被忽略的捷徑：Claude Code 除錯時會自動讀 git log，描述性 commit message 能讓 agent 幾秒內縮小問題範圍——大 codebase 問題範圍大得多，這點尤其關鍵。

**對抗式審查：兩階段、可串接，且工具範圍比角色描述可靠。** 「對抗性審查設計」把「打破 LLM 樂觀偏差」整理成兩種互補做法：**做法 A（計畫前審查）**由 Agent B 讀真實 codebase 挑戰待審計畫，通過才放行（Agent-plan-review-loop 是開源實作）；**做法 B（程式碼後審查）**由第二個 Claude 扮演批評者，事先挑毛病並與起草者達成共識。兩者可串接：先用 B 收斂規格、再用 A 驗證計畫。adamsreview 用平行子代理從安全性、邏輯、效能、可維護性各自獨立審查再交叉彙整，作者自測聲稱比官方 `/review`、`/ultrareview` 抓到更多真實 bug（待獨立驗證）。權限層面，「Read-Only Reviewer Agent」讓 reviewer 不持有任何編輯工具、只能輸出審查意見，避免降格為第二個 implementer；「Personas vs Tool-Scoping」在設計框架層做出結論——**工具範圍限制比角色描述更可靠**：模型可以忽略「你是 QA」的身份設定，但無法呼叫未掛載的工具。跨模型交叉審查也拿到了第一筆量化證據：讓 Claude 審查 Codex 產出的程式碼，通過率從 71.6% 升至 89.7%；學術論文 [Cross-Model LLM Code Review（arXiv 2607.21656）](https://arxiv.org/abs/2607.21656) 以 116 則 LiveCodeBench 中／難題、六種條件重現此數字，並指出反向（Codex 審 Claude）使通過率從 91.4% 降至 82.8%——效益具方向不對稱性。

**規劃分層與把關前移。** 「beads + Claude Code 兩層工作規劃架構」把分工軸線從「誰審查」延伸到「誰規劃」：規劃層處理「做什麼」、執行層處理「怎麼做」，與 session 內的 Interview 模式互補。「品質把關前移」記錄審查負荷過載時的另一條路線：同時跑多個 coding agent 後 diff 量已超過逐行審閱負荷，作者不是放棄審查，而是把把關往更早的任務拆解與驗收條件設計階段前移——**負荷撐不住時往上游移動，而非降低標準**。Boris Cherny 在 YC Startup School 訪談中的心法可視為這些做法的共同上位原則：驅動 Claude 的關鍵已從 prompt engineering 轉為「交給它一個略嫌太難的任務，並確保它有辦法沿途驗證自己的工作」，「驗證」是多數人做得最不到位的一環（人物脈絡見 [[entities/boris-cherny]]）——唯讀審查者、對抗性審查、失敗自動復原本質上都是在替任務裝上「沿途驗證」的機制（推論）。

**長 session 穩健化：從 MCP 層擴到整個 session。** 「MCP Server 長 Session 失效模式」指出連線中斷、工具超時、上下文失憶三大失效模式，各對應心跳檢查、超時重試、狀態快照。之後一組節點把同一框架擴大到 Claude Code session 層級——同一問題（長任務中途被打斷）在三種觸發源上的獨立解法：auto-undo 處理多工具連續呼叫中途失敗留下的混亂狀態、偵測並回滾；nightshift 處理夜間跨模型 API 500 錯誤時自動等待並 resume 回同一對話；resume-on-ratelimit.sh 處理撞上用量限制時搭配 PROGRESS.md 自動重試接續。

**尚未解決的驗證缺口，與第一個工具化嘗試。** 「你的 AI Subagent 在騙你」記錄一次具體踩坑：把 317 個硬編碼色碼的清理拆給多個 subagent 平行處理，各自回報「完成」，實際檢查卻發現至少 4 種靜默失敗模式——回報乾淨但結果不然。這給「工具範圍限制」共識補上重要提醒：**工具範圍解決的是「agent 能不能做壞事」，不是「agent 有沒有誠實回報做了什麼」**（推論）。loopx（4,476 星／forks 8.6%／27 個 open issues／近期仍有 commit，已確認非刷星）是第一個直接針對此缺口設計的工具：其「證據紀錄（evidence recording）＋可驗證交接（verifiable handoff）」要求每個任務單元交接時附帶可查核的證據，把「回報是否屬實」從事後人工複核往前挪一步——尚無第一手使用心得佐證它實際降低虛報比例的效果（[[topics/community-tech-patterns]] Multi-agent 架構類別）。

**相鄰案例。** 「AI Agent 語意層漂移 CI 測試」用僅需六秒的 CI 測試偵測 agent 多日執行中悄悄偏離預期行為的語意漂移，是傳統 CI 測不到的 QA 盲點（早期、待更多驗證）；「批量 OSS Bug 修復」先識別一類 bug 的觸發條件與修復模式，再跨 repo 套用，一天內對多個知名開源專案提交約 28 個 PR；Devthropology（PR 貢獻者互動與程式碼健康度視覺化）雖非 Claude Code 專屬，但補足「agent 大量產出 PR 後，團隊層面如何觀察協作健康度」的相鄰缺口（推論）。

**目前收斂點：** 「唯讀審查者 + 工具範圍限制」仍是多 agent 分工的主流共識，但它只解決「能不能做壞事」，未解決「有沒有誠實回報」；loopx 代表社群已從「指出問題」進展到「嘗試工具化」，效果待使用回饋；對抗式審查在計畫前／程式碼後兩階段各有做法且可串接，跨模型交叉審查已有獨立學術論文重現量化效益；長 session 穩健化已從 MCP 層擴大到整個 session 層級；語意漂移偵測仍屬早期。

---

## 目前結論

- 大型 codebase 讓「規模」「記憶」「品質」三個小專案不明顯的痛點被放大，社群做法多半是把小專案已驗證的原則（隔離、精簡、對抗式審查）**加碼到更大的規模**，而非發明全新機制。
- 四條主線中，「除錯與分工架構」收斂程度最高（唯讀審查者 + 工具範圍限制是共識），但 subagent 靜默失敗案例顯示這個共識未涵蓋「agent 是否誠實回報」，該線正從「事前約束」擴向「事後偵測、復原與可驗證交接」（跨源頭自動接續機制 + loopx）；「並行規模的極限與對策」中，官方 20 路並行與社群千級 fan-out 宣稱之間的落差仍未被系統性驗證（推論），但可觀測性已確立為 6 個獨立實作反覆出現的固定需求（見 [[topics/community-pattern-trends]] 趨勢六），加上落地整合序列化這個新下游子問題，補洞速度正在加快。
- 「Codebase 索引與記憶」出現方向轉變的訊號（CodeAlmanac 從「agent 記憶」轉向「codebase 文件自動維護」），待第二個獨立案例佐證。
- 官方機制（Managed Agents 20 路並行、subagent、context 管理相關指令）的最新狀態與版本號，一律以 [[entities/claude-code]] 與 [[entities/managed-agents]] 為準，本頁不重複記錄版本細節。

---

## 相關實體

- [[topics/community-tech-patterns]]（本頁四條主線的完整節點目錄與原始出處，含尚未達到主線敘事門檻的其他社群模式）
- [[topics/community-tech-discussions]]（context 腐蝕 vs 模型退步的概念辯論、Context Rot 修復五法等設計哲學層討論）
- [[topics/community-pattern-trends]]（跨模式的宏觀趨勢彙整，週更）
- [[entities/claude-code]]（官方 subagent、Managed Agents 20 路並行等機制的最新狀態）
- [[entities/managed-agents]]（Dreaming 記憶整合、Outcomes 規格驅動執行等官方框架能力）
- [[entities/boris-cherny]]（千級子代理工作流公開聲明）

## 參考來源

節點來源連結見 [[topics/community-tech-patterns]] 對應日期段落；本頁不重複列出。
