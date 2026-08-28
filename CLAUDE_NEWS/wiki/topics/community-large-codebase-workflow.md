---
page: "topics/community-large-codebase-workflow"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-08-22"
last_news_update: "2026-08-22"
update_freq: "🗓️ 週更（每週從模式庫沉澱一次；更新日期停留數天屬正常節奏）"
status_main: "ongoing"
days_since_news: 7
inbound_links: 26
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
**更新頻率：** 🗓️ 週更（每週從模式庫沉澱一次；更新日期停留數天屬正常節奏）
**開始日期：** 2026-05-02
**最後更新：** 2026-08-22
**最後新聞更新：** 2026-08-22

> **本週答案變動**（2026-08-22）
> 「Context / Token」線：grep 搜尋輸出成為第四種被盯上的裁剪對象（Graft，宣稱降 42% token），補入「工具輸出裁剪」子問題；惟宣稱本身遭社群質疑為未驗證數字。其餘三條線本週無新節點，答案不變。

---

## 摘要

小專案上好用的做法——單一 CLAUDE.md、單一 session、讀完整檔案——搬進大型 codebase 就開始失靈：並行 agent 互踩、context 被工具輸出撐爆、agent 記不住昨天的架構決策、多 agent 產出沒人把關。本頁把 [[topics/community-tech-patterns]] 裡屬於這四個痛點的節點，每週沉澱成「現在該怎麼做、還缺什麼」；節點證據與出處一律在模式庫，本頁不重複。官方機制以 [[entities/claude-code]]、[[entities/managed-agents]] 為準。

| 主線 | 一句話問題 | 現在的答案 |
|------|-----------|-----------|
| 1. 並行規模 | 幾個 agent 同時跑會互踩？ | 每 agent 一個 git worktree；先從 10–20 個驗證協調機制 |
| 2. Context / Token | context 怎麼不被大 repo 撐爆？ | 不預先加載、按需取回；變笨先測量再歸因 |
| 3. 索引與記憶 | agent 怎麼記得住跨 session 的決策？ | repo 才是記憶體——決策外化成 CLAUDE.md／spec／ADR，本地索引按需查 |
| 4. 除錯與分工 | 多 agent 產出誰把關？ | 審查者唯讀＋工具範圍限制；跨模型交叉審查有量化效益 |

---

## 技術彙整

### 1. 並行規模：幾個 agent 同時跑會互踩？

**現在的答案**
- 每個 agent 一個 git worktree（或等價的檔案系統隔離）——沒有獨立工作空間，並行必崩
- 先從 10–20 個 agent 驗證協調機制；每次倍增規模重新驗證，不要線性外推
- 平行 agent 的 commit 用本地合併佇列依序建置、測試、合併，不要各分支各自觸發 CI

**還沒解決**：官方 20 路並行、創始人「每晚數千子代理」與社群實測「4→20 就崩」之間的落差沒人系統驗證（推論）。監控多 agent 進度的儀表板很多，但沒有定論做法。

| 子問題 | 社群走到哪 | 代表實作 | 證據強度 |
|---|---|---|---|
| 隔離 | OS 帳號隔離 → git worktree 成共識，並工具化、動態化 | Claudette、Superset、cc-fleet 等 | 多來源 |
| 規模上限 | 4→20 崩潰主因：git lock／DB 連線競爭、context 洩漏、無協調層 | 《Why 20 Instances Break Down》、1000 fan-out 教學 | 單一深度分析 |
| 可觀測性 | 32 天內 6 個獨立儀表板；分「讀官方 event stream」與「自解析 transcript」兩路 | HUD、Cockpit 等，見 [[topics/community-pattern-trends]] 趨勢六 | 已成趨勢 |
| 落地整合 | 本地合併佇列（4–5 agent／日 90 commit／8GB 筆電） | 單一作者實測 | 單一實測 |

**為什麼會這樣**：規模一大，共享資源（git、DB）與 context 邊界最先破，所以隔離原語最早收斂；協調層與整合序列化是隔離做好之後才暴露的下一層瓶頸；人工盯進度撐不住，才催生一批儀表板。

---

### 2. Context / Token：context 怎麼不被大 repo 撐爆？

**現在的答案**
- 不預先 @ 一堆檔案，按需取回、並限制單次讀取量；長 session 退化的解法是裁剪輸入，不是加 context
- 「變笨」先量 context 組成再怪工具——MCP 工具清單、CLAUDE.md、headless 冷啟動都是可量的固定成本
- CLAUDE.md 每行都是對每個請求課的「context 稅」：依觸發頻率決定放 CLAUDE.md／skill／hook／docs 哪一層

**還沒解決**：「該裁多少」沒有跨案例統一標準，多為個別作者自訂閾值；圖片化 context（pxpipe）與 grep 輸出裁剪（Graft）都只有單一案例，且 Graft 的降幅宣稱本身遭社群質疑。

| 子問題 | 社群走到哪 | 代表實作 | 證據強度 |
|---|---|---|---|
| 按需取回 | 預先 @-mention 定為反模式；讀取上限＋索引層；不裁剪會 O(N²)（62.8–85.9% 額外 token） | Just-in-Time Retrieval、Compact Memory、Git Lazy Mount 等 | 多來源 |
| MCP 成本 | 9 個 server ≈ 每輪 38k token 冷啟動；設計（描述長度、回傳格式）實測有差 | MCP 信任邊界審查、隱藏成本實測 | 多來源 |
| 極簡輸出 | 單次回覆 70→20 token；65% 降耗；企業已當降本策略 | Caveman Skill、404 Media 報導 | 多來源 |
| CLAUDE.md 取捨 | 四層寄放地依觸發頻率；載入順序（CLAUDE.local.md 後載、受管理原則檔各 OS 路徑不同） | 「該裝什麼」「載入順序」兩篇 | 單一深度分析 |
| 固定成本量測 | `claude -p` 未加 `--bare` 冷啟動約 15 萬 token，多 agent pipeline 反覆呼叫會放大 | headless 冷啟動實測 | 單一實測 |
| 工具輸出裁剪 | 高頻高輸出來源逐一被盯上：grep 搜尋輸出宣稱可削減 42% token，但 benchmark 段落遭質疑 AI 代寫，數字未經第三方驗證 | Graft | 單一實測（存疑）|
| 非主流方向 | 清程式碼內 AI 殘留註解（CCN，2,700 次迭代自陳）；文字 context 渲染成圖片（pxpipe） | CCN、pxpipe | 推論 |

**為什麼會這樣**：大 repo 的檔案量與工具輸出量本身就超過 context，任何「多讀一點保險」的直覺都會撐爆；於是社群的每一步都是在把「哪裡吃了 token」變成可量測的數字，再針對數字最大的那塊裁——但量測本身的可信度也需要驗證，不是每個宣稱的百分比都經得起檢視。

---

### 3. 索引與記憶：agent 怎麼記得住跨 session 的決策？

**現在的答案**
- repo 才是記憶體、模型只是工作者：已確定的架構決策外化到 CLAUDE.md、spec、ADR，不靠模型跨 session 記住
- 本地優先的索引（向量 DB／圖資料庫／SQLite／純 Markdown）按需語義查詢，不把全部記憶塞進 context
- 「什麼不該再做」也要記——已否決方案沒進 agent 可讀的知識源，agent 會重做一次

**還沒解決**：跨工具可攜（ltm／OKF）仍是少數派；「codebase 文件自動維護」只有 CodeAlmanac 一例；「已否決方案索引」停在問題點名、無工具。

| 子問題 | 社群走到哪 | 代表實作 | 證據強度 |
|---|---|---|---|
| 統一框架 | Repo-as-Memory：決策外化；跨 repo 依賴圖需另注入（`nx graph` 等） | Repo-as-Memory、Cross-repo Blast Radius | 單一深度分析＋推論 |
| 本地索引 | 向量 DB（39ms 檢索）／圖資料庫／SQLite session 索引／Markdown+git，各走一路 | Memex、session-indexer、Iantha 等 | 多來源 |
| 可攜性 | Markdown 規則檔不跨工具 → JSON 協定或格式規約 | ltm、OKF | 單一實測 |
| 文件自動維護 | codebase wiki 隨對話自動更新，取代手維護 MANUAL.md | CodeAlmanac | 單一實測 |
| 否決方案索引 | 「已被否決」只在人腦或討論串 → 隱形重工 | 概念性觀察 | 推論 |

**為什麼會這樣**：跑了數月、數百 session 的 repo，agent 每次重「猜」已知答案既費 token 又重蹈覆轍；社群的共同答案是把記憶從模型搬到 repo 與本地索引，差別只在用什麼形式存、跨不跨工具。

---

### 4. 除錯與分工：多 agent 產出誰把關？

**現在的答案**
- 審查者 agent 不掛編輯工具、只能輸出意見——工具範圍限制比「你是 QA」的角色描述可靠
- 對抗式審查分兩階段：計畫前由另一 agent 讀 codebase 挑戰計畫、程式碼後由第二個 Claude 挑毛病，可串接；跨模型交叉審查（Claude 審 Codex）通過率 71.6%→89.7%，反向反而下降
- 審查負荷撐不住時往上游移：把把關前移到任務拆解與驗收條件，而非降低審查標準

**還沒解決**：工具範圍只擋「能不能做壞事」，擋不了「有沒有誠實回報」——subagent 靜默失敗（317 項清理、4 種失敗模式回報卻乾淨）仍是缺口；loopx 是第一個針對它的工具，尚無使用回饋。

| 子問題 | 社群走到哪 | 代表實作 | 證據強度 |
|---|---|---|---|
| 邊界規則 | 11 條多 agent CLAUDE.md 規則（工作區邊界、禁改共享狀態、merge 責任）；PostToolUse 稽核日誌 | Multi-agent 衝突防範、稽核日誌模式 | 多來源 |
| 對抗式審查 | 計畫前／程式碼後兩做法；唯讀審查者；跨模型交叉審查（arXiv 2607.21656 重現） | Read-Only Reviewer、Agent-plan-review-loop、adamsreview | 多來源＋學術重現 |
| 規劃分層 | 規劃層「做什麼」／執行層「怎麼做」；把關前移 | beads 兩層架構、品質把關前移 | 單一實測 |
| 長 session 穩健化 | 心跳／超時重試／狀態快照，從 MCP 層擴到 session（工具失敗、API 500、用量限制各有自動接續） | auto-undo、nightshift、resume-on-ratelimit | 多來源 |
| 回報驗證 | 靜默失敗案例 → 證據紀錄＋可驗證交接 | 「Subagent 在騙你」、loopx（4,476 星） | 單一實測 |
| 相鄰案例 | 六秒 CI 測語意漂移；同形狀 bug 跨 repo 批修 28 PR；PR 協作健康度視覺化 | 語意漂移 CI、批量 OSS 修復、Devthropology | 推論 |

**為什麼會這樣**：單一 Claude 自審自批會照單全收（affirmative bias），多 agent 又需要一致邊界，所以社群先用「權限」而非「人設」約束；Boris Cherny 的心法「給它略難的任務、確保它能沿途驗證自己」（[[entities/boris-cherny]]）是這些做法的上位原則——而「回報是否屬實」是沿途驗證裡最後一塊還沒補上的（推論）。

---

## 目前結論

- 四條線的共同做法是把小專案已驗證的原則（隔離、精簡、對抗式審查、決策外化）**加碼到更大的規模**，而非發明新機制。
- 收斂最高的是「除錯與分工」（唯讀＋工具範圍），但它剛暴露「回報是否屬實」的新缺口；「並行規模」的規模上限無定論，可觀測性與整合序列化正在補位；「索引與記憶」正從「agent 記得住」轉向「文件不腐化」，待第二個案例。
- 官方機制的最新狀態與版本號以 [[entities/claude-code]]、[[entities/managed-agents]] 為準。

---

## 相關實體

- [[topics/community-tech-patterns]]（四條線的完整節點與原始出處；節點以 `主線` 欄位標記所屬線）
- [[topics/community-tech-discussions]]（context 腐蝕 vs 模型退步等設計哲學層討論）
- [[topics/community-pattern-trends]]（跨模式的宏觀趨勢，週更）
- [[entities/claude-code]]、[[entities/managed-agents]]（官方 subagent、20 路並行等機制）
- [[entities/boris-cherny]]（千級子代理工作流、「沿途驗證」心法）

## 參考來源

節點來源連結見 [[topics/community-tech-patterns]] 對應條目；本頁不重複列出。
