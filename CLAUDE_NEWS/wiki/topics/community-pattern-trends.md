# 社群趨勢觀察（週更）

**狀態：** ongoing
**領域：** 🌐 社群
**開始日期：** 2026-06-29
**最後更新：** 2026-06-30
**最後新聞更新：** 2026-06-30

> **本週趨勢觀察**（2026-06-30）
> 「強制層取代建議層」新增環境感知 hooks 節點（Adrafinil HN 113）；「Context 主權」新增 56KB 上限主動截斷模式；「模型路由自動化」Workweave Router（HN 181）持續延燒，趨勢成熟信號穩固。「對抗性設計」Verity 自癒式 review gate 加入，醞釀趨勢升溫。

---

## 摘要

本頁從 [[topics/community-tech-patterns]] 的具體模式中，**萃取出宏觀趨勢**——社群正在往哪些方向收斂，每條趨勢的熱度曲線（加溫 / 穩定 / 醞釀），以及**對現有設計的啟示**：工程師看到這條趨勢，該回頭重新思考自己現有設計的什麼。

- **週更**：本頁只在 `/wiki-lint` 時更新，不進每日 ingest。
- **與其他頁分工**：具體模式條目見 [[topics/community-tech-patterns]]；何時首次出現的歷史流水帳見 [[topics/community-tech-timeline]]；思想辯論見 [[topics/community-tech-discussions]]。
- **熱度錨點（注意力，非技術力）**：🔥🔥🔥🔥 = HN ≥ 100 或跨平台廣泛熱議；🔥🔥🔥 = HN 30–99 或單平台高互動；🔥🔥 = HN 10–29 或多來源；🔥 = 單一來源或早期信號。無 HN 數據的節點為熱度估計。

---

## 成形趨勢

### 趨勢一：強制層取代建議層　`成形`　熱度趨勢：▬ 穩定延燒

**演進：**
- 🔥🔥 **Hooks 強制執行機制**（5/06）：用 Hooks 在工具呼叫前後攔截行為，而非只在 CLAUDE.md 寫「請不要…」
- 🔥🔥 **每新規則必刪一條**（6/20）：發現 CLAUDE.md 規則一多反而降低遵守率，提出規則總量硬上限
- 🔥🔥🔥 **Hooks 取代 CLAUDE.md 規則**（6/23）：正式定調——「必須 100% 執行」的規則搬進 Hooks，CLAUDE.md 只留偏好與風格
- 🔥🔥 **Pre-completion Hook**（6/25）：用 Hook 偵測模型「讓我知道如果…」式的模糊收尾，攔下來強制它真正做完
- 🔥🔥 **環境感知條件觸發（Adrafinil）**（6/28，HN 113）：hooks 不再只是業務邏輯觸發器，而是升格為「感知 agent 活躍狀態 → 決定環境副作用是否觸發」的條件控制器；可延伸至 Slack DND、資源分配等場景

**代表模式：**
- **Hooks 強制執行取代 CLAUDE.md 規則**：把 deploy 保護、formatter、migration 防寫等「必做」遷到 PreToolUse / PostToolUse hook，用 exit code 控制放行或攔截
- **ANMA 架構邊界合約**：用 YAML 合約定義架構邊界 + Hook 強制驗證，讓便宜模型也守得住規則（實測 0/20 vs 無約束時 13/19 違規）
- **Pre-completion Hook**：Stop Hook 掃描最後一輪輸出，偵測到模糊結束語句就回傳非零 exit，逼模型繼續

**對現有設計的啟示：** 你 CLAUDE.md 裡任何「必須 100% 遵守」的規則都放錯位置了——LLM 是機率性遵守，規則越多遵守率越低。把它們分成兩類：偏好留 CLAUDE.md，邊界搬 Hooks。

判斷標準只有一個：**「這條規則被遺漏一次，我會生氣嗎？」** 生氣 → Hook，無所謂 → CLAUDE.md。

| 規則 | 放哪裡 | 原因 |
|------|--------|------|
| 「用繁體中文回答」 | CLAUDE.md | 偶爾漏了只是語言問題，不影響系統正確性 |
| 「不加多餘注釋」 | CLAUDE.md | 風格偏好，判斷空間大，偶爾多一行無傷大雅 |
| 「不可 `git push --force` 到 main」 | PreToolUse Hook | 一次失誤就是事故，不能靠機率 |
| 「commit 前跑測試」 | PreToolUse Hook | 緊急狀態下 LLM 最容易「忘記」這條 |
| 「不可讀 `.env` 檔」 | PreToolUse Hook | 安全邊界，一次洩漏就是問題 |
| 「.ts 檔寫完後跑 prettier」 | PostToolUse Hook | 格式一致性是死規定不是建議 |

Hook 的原理：exit 1 = 硬攔截，不是「提醒模型注意」，而是工具呼叫根本不會發生。

---

### 趨勢二：Multi-agent 隔離工程化　`成形`　熱度趨勢：▬ 成熟穩定

**演進：**
- 🔥 **零星嘗試**（4/26）：多 agent 概念出現，但還沒解決「互相踩到彼此檔案」的問題
- 🔥🔥🔥 **Git Worktrees 作為隔離原語**（5/23）：找到關鍵解法——每個 agent 配一個 git worktree，檔案系統完全隔離
- 🔥🔥 **並行工作流轉型指南**（6/24）：從「單一 prompt 反覆調整」的線性做法，轉為「任務分解 → 並行派發 → 彙整驗證」
- 🔥🔥 **20-instance 崩潰分析**（6/26）：實測從 4 個擴到 20 個並行時的崩潰原因（git lock 競爭、context 洩漏到鄰近 agent）與對策

**代表模式：**
- **Git Worktrees 隔離原語**：多 agent 各持獨立 worktree，根除共享目錄的覆蓋衝突
- **20-instance 崩潰分析**：超過 10 個並行就需要 orchestrator 協調層，且要從小規模漸進擴展
- **Personas vs Tool-scoping**：用「每個 agent 只掛載其職責所需的工具」當邊界，比「你是 QA」這種角色描述可靠——模型能無視身份，但無法呼叫沒掛載的工具

**對現有設計的啟示：** 如果你的 multi-agent 共用工作目錄，遲早互相覆蓋。並行的前提是隔離（worktree / 容器），不是 prompt 技巧；超過 10 個 agent 必須有 orchestrator 協調層。

**具體失敗場景：**
- 10 個 agent 同時修改同一個 `utils.py` → 後寫的把前寫的蓋掉 → 錯誤不可復現，debug 成本極高
- 告訴 agent 「你是 QA，只能看不能改」→ 模型可能無視角色描述，還是呼叫了 Edit 工具

**怎麼修：**
- 每個 agent → `git worktree add ../task-1-branch` → 完全獨立的檔案系統，根除覆蓋可能
- 「QA agent 只掛載 Read 工具，不掛 Edit/Write」→ 物理上無法修改，不靠 prompt 約束
- 超過 10 個並行時：主 agent 派發任務、收集完成訊號、統一 merge → orchestrator 才有能力在 conflict 時介入仲裁（單靠 agent 自己 merge 會打架）

---

### 趨勢三：Context 主權爭奪　`成形`　熱度趨勢：▬ 高檔穩定

**演進：**
- 🔥🔥🔥 **Context 是核心瓶頸**（5/12）：確認大型專案的真正天花板是 context 管理，而非程式碼生成品質
- 🔥🔥🔥 **Context Rot 修復五法**（6/20）：「Claude 越用越笨」幾乎都是 context 腐蝕；五種具體修復策略成社群共識
- 🔥🔥🔥 **三連發：Just-in-Time / Repo-as-Memory / 避免預加載**（6/26）：同期三篇互補，把「context 精準性優於完整性」推成新原則
- 🔥🔥 **Context 上限主動截斷**（6/29）：agent 讀取上限設計——56KB 問題揭示 agent 為「確保完整性」反而讀入噪音；明確設定讀取上限（行數/字元數）是 context 管理的防禦性基礎設施

**代表模式：**
- **Context 裁剪 Tool Output**：主動截斷或摘要化工具回應，而非全量塞入 context
- **Just-in-Time @-file Retrieval**：不預先 @ 一堆檔案，只在需要時才即時取回
- **Repo-as-Memory**：模型是工作者、repo 才是記憶體；已決定的事外化成檔案，不寄望模型跨 session 記住
- **Compact Memory**：以語意摘要取代每輪重送完整 transcript，把 O(N²) context 開銷壓回接近 O(N)（附可跑 benchmark）

**對現有設計的啟示：** 「塞越多越安全」是反模式。如果你預先 @ 一堆檔案、或把所有決策寄望模型記住，正在製造 context rot。改成：repo 是記憶體、即時取回、已決定的事外化成檔案。同時，「完整讀取」也是反模式——明確設定 agent 讀取上限，讓 agent 先查索引再決定是否全讀。

| 反模式（你可能正在這樣做） | 改成這樣 |
|--------------------------|---------|
| CLAUDE.md 開頭 `@README @architecture @api-spec @schema` 全部預載 | 只有真的需要時才 @ 那個檔案，其他讓模型 grep 後按需取回 |
| 「上次討論決定用 PostgreSQL，模型應該記得」 | 把決策寫進 `decisions/db-choice.md`，明確讓 agent 讀那個檔案 |
| Agent 被指示「讀完整個 README」| 先 grep 找相關章節行號，再 Read 那 20 行；56KB README 裡有 50KB 跟當前任務無關 |
| 每輪都把完整 transcript 重送 | 以語意摘要取代，把 O(N²) context 開銷壓回接近 O(N) |

直覺：如果對話後期模型開始「忘記」前面說的事，不是因為它變笨——是 context 被早期塞入的大量文件稀釋了。

---

### 趨勢四：模型路由自動化　`成形`　熱度趨勢：📈 加溫中（最新）

**演進：**
- 🔥 **Dragoman 多模型路由**（5/13）：早期單一分享，用顯式規則手動指定哪個任務走哪個模型
- 🔥🔥 **三角色分工 Pipeline**（6/25）：Claude 規劃 / Codex 建功能 / ChatGPT 查詢，各司其職並定義交接協定
- 🔥🔥🔥🔥 **Workweave Router**（6/27，HN 181）：**本週引爆點**，嵌入式自動路由依請求難度選模型，無需手動規則

**代表模式：**
- **Workweave Router**：嵌入 Claude Code / Codex / Cursor 的成本感知路由，依難度自動降階
- **Multi-model Pipeline**：三模型明確分工 + 結構化交接，控制跨平台 token 成本
- **Dragoman**：~800 行 CLI，顯式規則路由至 Perplexity / Gemini / Ollama 並由 Claude 統整
- **分層模型策略**：Sonnet 主力 + Opus 諮詢，依任務複雜度節省約 60% 用量

**對現有設計的啟示：** 「永遠用最強模型」在燒錢。如果你所有任務都走 Opus，該按難度路由——簡單任務降階可省 60%+。但留意黑盒路由的「最佳」由路由器自己定義，缺乏可解釋性。

**哪些任務可以降階：**

| 任務 | 適合模型 | 理由 |
|------|---------|------|
| 格式轉換、JSON 整理、標籤提取 | Haiku | 規則明確，不需要 reasoning |
| 一般 feature 開發、重構、已知類型 bug | Sonnet | 大部分日常工作的最佳 CP 值點 |
| 跨系統架構決策、複雜 bug 調查、不確定性高的問題 | Opus | 真正需要深度 reasoning 的任務 |
| 「幫我 review 這段 migration SQL 的安全性」| **Opus，不可降階** | 看起來簡單但降階後後果嚴重 |

**成本感：** 假設一天 100 次呼叫，全走 Opus ≈ $100；Haiku 50% / Sonnet 40% / Opus 10% ≈ $18。

**黑盒路由的隱患：** Workweave Router 自己決定「這個請求夠難嗎」——如果判斷邏輯不透明，某些關鍵任務可能被靜默降階，你不知道為什麼結果不可靠。顯式規則路由（自己定義哪類任務走哪個模型）更容易 debug，代價是維護成本。

---

### 趨勢五：對抗性設計　`醞釀 → 成形`　熱度趨勢：↗ 醞釀中

**演進：**
- 🔥 **零星出現**（4/26）：對抗性審查概念初現，尚未系統化
- 🔥🔥 **6 月系統化**（6/25）：對抗性審查（計畫前 + 程式碼後對照）、Read-Only Reviewer 同期出現，形成設計分層
- 🔥🔥 **Verity 自癒式 review gate**（6/27）：每次 agent 執行後自動修復不安全代碼並記憶學習；「reviewer 記憶讓下次起點更優」是對抗性設計的持久化延伸（HN Show HN）

**代表模式：**
- **對抗性審查設計**：引入對立角色打破 LLM 樂觀偏差；計畫前審查讓審查者讀真實 codebase，程式碼後審查在草稿階段挑模糊假設
- **Read-Only Reviewer Agent**：reviewer 不持有編輯工具，用權限約束強制其只批評不動手，維持對立性可持續
- **多代理 PR Review**：平行子代理 + 多階段驗證，跨廠商模型交叉審查

**對現有設計的啟示：** 讓同一個模型自我審查抓不到問題（樂觀偏差）。如果你的 review agent 也能編輯，它會傾向直接改而非批評——用 read-only 權限 + 多廠商交叉，強制對立性可持續。

**為什麼自我審查失效：**
讓 Claude 寫完一個函式後問它「這段 code 有什麼問題？」→ 它傾向確認自己剛做的決定（「邏輯正確，看起來沒問題」）。這不是模型差，是認知偏差——任何人審查自己剛寫的東西都會如此。

**對抗性設計三個層次：**

| 層次 | 做法 | 效果 |
|------|------|------|
| 最低限度 | 同一個 Claude，先寫再開新 session 審查 | 消除「剛剛做了這個決定」的即時偏差 |
| 中等 | 兩個 agent：writer 掛 Edit/Write，reviewer 只掛 Read | 物理上無法修改 → reviewer 被迫只能批評，不會「幫你改好它」 |
| 最強 | Claude 寫 → GPT 或 Gemini 審 | 不共享訓練偏差，reviewer 不會「順著」原始模型的思路走 |

**Verity 的延伸邏輯：** reviewer 發現「你用了 `eval()`，這是安全漏洞」→ 自動修復 + 把「禁止 eval()」存進 memory → 下次 writer 一開始就帶著這條限制。累積越多輪，reviewer 的起點越高，不是每次從零開始審。

---

## 醞釀中（未列成形）

- **spec-driven 規格先行**：以規格 / 合約先於實作定義 AI 的行動邊界。ANMA 架構邊界合約、ISO/IEC/IEEE 29148 引入工作流等零星出現，概念紮實（ANMA 自帶 0/20 vs 13/19 數據）但社群驗證度仍低，待累積到判定門檻再升為成形趨勢。

---

## 趨勢判定門檻

一條模式要升格為「成形趨勢」，須同時滿足：

1. **≥ 3 個獨立來源** 提及此方向（不同作者 / 平台）
2. **跨 ≥ 14 天** 反覆出現（非單日爆紅後沉寂）
3. **至少 1 條代表模式達 A/B 層證據**（自帶量化數據，或機制自洽可操作）

未達門檻者列「醞釀中」觀察，不虛抬為趨勢。

---

## 相關實體

- [[topics/community-tech-patterns]]（具體模式型錄，本頁的素材來源）
- [[topics/community-tech-timeline]]（4–5 月歷史流水帳，演進起點考據）
- [[topics/community-tech-discussions]]（思想辯論，趨勢背後的社群共識）
- [[entities/claude-code]]（多數趨勢圍繞的官方產品）
- [[entities/boris-cherny]]（Loops 哲學影響多條趨勢的設計取向）
