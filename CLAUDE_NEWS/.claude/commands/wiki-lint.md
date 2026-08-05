---
description: 每週執行 wiki 品質檢查，修正矛盾/孤立/過期頁面，更新 overview。
---

# Wiki Lint

每週執行，檢查 wiki 品質並修正問題。建議在週末或週一執行。

## 步驟

### 1. 載入 wiki 全貌

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/rules/wiki-ingest.md` — 分類標準與派工流程（主編指南）
- `.claude/rules/wiki-ingest-format.md` — 頁面格式模板、欄位規則、品質標準
- `wiki/index.md` — 取得所有頁面清單
- `wiki/log.md` — 了解最近的 ingest 紀錄與活動

### 2. 並行派工（六位記者同時執行）

對每個類別呼叫 Agent tool，在**同一訊息中並行發出全部六個呼叫**。每個 Agent 呼叫必須帶 `model: "sonnet"`（lint 與策展為有界判斷任務，不需旗艦模型；未指定會繼承主 session 模型，六記者並行足以打穿訂閱配額）。

| 類別 | subagent_type | 領域 |
|------|--------------|------|
| 模型 | `wiki-reporter-models` | 🤖 模型 |
| 功能 | `wiki-reporter-features` | 🛠️ 工具/功能 |
| 商業 | `wiki-reporter-commercial` | 💼 商業 |
| 安全政策 | `wiki-reporter-safety-policy` | 🏛️ 政策/安全 |
| 社群 | `wiki-reporter-community` | 🌐 社群 |
| 人物 | `wiki-reporter-people` | 👤 人物 |

> **頁面範圍為動態認領，不是寫死清單：** 每位記者的負責頁面＝`wiki/index.md` 中「領域」欄等於自己那一組的所有 entities/ 與 topics/ 頁面（含近期新增），開工前先讀 index.md 認領清單，再加上自己規則檔（`.claude/rules/wiki-ingest-[category].md`）觸發條件表中列出的頁面。這樣新增頁面不需要回頭改這份派工表。

> **社群記者額外任務：** `community-tech-tools.md` 已脫離每日 ingest，是 **lint 專用策展頁**。除 3a–3g 品質檢查外，須額外依 `.claude/rules/wiki-ingest-community-lint.md` 的「策展規則」與「精選層提拔規則」執行：讀取近 7–14 天 `news/*.md` 萃取達標新工具、汰除過氣條目、提拔精選層、同步痛點洞察。派工 prompt 須附上「今日日期」供記者計算 news/ 範圍。

每個 Agent 呼叫的 prompt：

```
今日日期：[YYYY-MM-DD]
任務：對你負責的頁面執行 wiki lint 檢查並修正問題。

你的負責頁面＝`wiki/index.md` 中領域為 [對應領域] 的所有頁面（含近期新增），開工前先讀 index.md 認領清單，再加上你規則檔（`.claude/rules/wiki-ingest-[category].md`）觸發條件表中列出的頁面。

讀取 `.claude/rules/wiki-ingest-format.md`，然後對每個頁面依序執行：

**3a 矛盾偵測**
同一事件的描述若與其他已知頁面矛盾（日期不同、結論相反）→ 以日報原文為準修正，兩頁互加 wikilink。

**3b 孤立頁面**
用 Grep 搜尋此頁面 slug 是否在 wiki/ 目錄其他檔案中有 wikilink 引用。
若完全孤立（無任何頁面以 `[[...]]` 連結到它）→ 在語意相關的頁面補上 wikilink。

**3c 過期議題**
topics/ 頁面狀態為 `ongoing`，且「**最後新聞更新**」距今超過 14 天，且 log.md 近期無相關更新。（不可用「最後更新」判斷——lint 與格式修正會 bump 該欄位，導致過期偵測永不觸發。）
→ 議題確已結束：狀態改 `resolved`，填寫「目前結論」
→ 仍在進行但無新消息：狀態改 `monitoring`

**3d 已解決議題收尾**
topics/ 狀態為 `resolved` → 確認「目前結論」已填寫、頂部 callout 註明已結案。**留在原路徑不遷移**（一頁一故事，遷移會斷 wikilink 與讀者動線）。

**3e 呈現品質審查**
依 `.claude/rules/wiki-ingest-format.md`「Wiki 頁面呈現品質標準」掃描：
必須修復：摘要可獨立閱讀、關鍵資訊前置、無 LLM 專屬指令
警示觸發：頁面 > 200 行、連續 8+ 個無分組日期條目、方案比較未用表格

**3f 超長頁面入口層健檢（> 500 行）**
檢查是否具備入口層（delta-first callout ＋ 概覽表或月份/主題分組）；缺少者補結構。**不提拆分方案**。
僅當發現語意分岔（一頁實際含兩個獨立故事）或死案段落（resolved 且無引用）時，才回報主 session 供使用者決定。

**3g 待查證回訪**
對你負責的頁面 grep「待查證」「單方指控」「無官方證實」「待核實」等懸置標記。
逐一檢查標記所在條目的事件日期：
- 距今 ≤ 14 天 → 不動（還在合理查證期）
- 距今 > 14 天 → 比對近 14 天 `news/*.md` 有無後續報導：
  - 有後續（證實/否認/新進展）→ 更新條目內容，並移除或改寫原懸置標記
  - 無後續 → 標記改為「（YYYY-MM-DD 指控，至今無後續）」，讓讀者分辨「還在查」vs「早就沒下文」

完成後依標準格式回報。
```

記者回報格式（標準化）：

```
## [類別] Lint 回報
修正矛盾：[list or 無]
補孤立連結：[list or 無]
狀態更新：[page: ongoing→monitoring/resolved or 無]
resolved 收尾：[list or 無]
呈現品質：[每頁 ✅/⚠️已修復/📋待辦]
入口層健檢：[頁面名稱 + 行數 + 補結構結果，或語意分岔/死案候選 or 無]
待查證回訪：[已更新: list / 已改註無後續: list / 無懸置標記]
index.md 狀態變更：[page: 舊狀態→新狀態 or 無]
```

**收報核對（自我遵守率）`[加入: 2026-07-05]`：** 主編收到每份回報後，逐項核對 3a–3g **七項是否各有明確結果**（具體頁名＋結論，而非籠統一句「全部通過」；「無」也算明確結果，但須看得出該項有被執行）。缺項或含糊者以 SendMessage 退回該記者補做，不得代填。核對結果（N/6 位一次過、**退回原因**）記入 Step 8 log。

**月度蒸餾（記者成長迴路）`[加入: 2026-07-05]`：** 僅每月第一次 lint 執行（判斷方式同 6g 指標二：`wiki/log.md` 本月尚無 `Lint` 記錄），其餘週次輸出「非本月首次 lint，跳過月度蒸餾」。

步驟：
1. grep 過去 30 天 `wiki/log.md` 的**「退回」**記錄（收報核對段落）與**「品質備註」**行（ingest 紀錄，見 `.claude/rules/wiki-ingest.md` 第三步）
2. 按「記者類別 × 錯誤型態」統計出現次數
3. **同一型態 ≥ 2 次**者產出立法提案；僅 1 次者只列入「觀察中」清單，不立法

提案格式：
```
| 記者 | 錯誤型態 | 次數 | 建議條文 | 目標檔案與節 | 新增/改寫 |
```
- 若該錯誤**已有對應規則仍重複違反**，提案一律為**改寫既有條文使其更明確**，不新增
- 提案**向使用者確認後才寫入**；寫入依 `.claude/rules/claude-md-edit.md` 流程，完成後執行 `/review-commands` 直到零錯誤

輸出：
```
🌱 月度蒸餾（記者成長迴路）：
  立法提案（N 條）：
  | 記者 | 錯誤型態 | 次數 | 建議條文 | 目標檔案與節 | 新增/改寫 |
  觀察中（僅 1 次，K 條）：[列出或「無」]
❓ 是否採納以上提案？（全部 / 部分 / 皆否）
```

### 3. 處理語意分岔／死案歸檔候選（需使用者確認）

收齊所有記者回報後，彙整 3f 中回報的語意分岔或死案候選（若無候選，此步驟直接跳過）。以下列格式呈現並**等待使用者確認**：

```
📄 [頁面名稱]（XXX 行）發現[語意分岔 / 死案段落]

記者分析：
- [說明分岔成兩個獨立故事的具體內容，或死案段落內容與無引用佐證]

建議方案：
- [語意分岔]：拆為 [新頁面 A] / [新頁面 B]
- [死案歸檔]：歸檔至 [目標頁面]

❓ 請確認：是否同意處理？分類是否正確？命名是否OK？
```

根據使用者回應執行處理或記錄為待辦。

### 4. 建議並建立新實體頁

掃描所有頁面（可用 Grep），找出被提及 3 次以上但尚無專頁的名稱（模型、功能、人物、產品）。
→ 建立對應的 entities/ 頁面，填入目前已知資訊。
→ 在來源頁面補上 wikilink。

### 5. 更新 wiki/overview.md

重寫 `wiki/overview.md` 的內容，反映當前局勢：
- 目前最活躍的議題（ongoing topics）
- 近兩週的重大事件摘要
- 值得持續關注的趨勢

### 5b. 跨家任務榜單週更（主編派工）`[加入: 2026-08-05]`

`wiki/topics/model-task-leaderboard.md`（任務 × 跨家模型領先者週快照）由本步驟維護——它吃外部榜單網站而非新聞條目，類別路由接不到，此處為其唯一觸發邊；記者無 web 工具，由主編派工執行。

1. 派一個 `general-purpose` agent 帶 `model: "haiku"`（低成本抓取任務），prompt 要求：逐一查該頁「涵蓋榜單」清單中的所有榜（頁面表格內含 URL），回報各榜前 3–5 名、分數/Elo/占比、資料日期、來源方式（直接抓取 or 二手搜尋＋日期）；JS 渲染抓不到時退用 WebSearch 近期報導並標注二手；查不到明說，不可編造模型名或分數
2. 主編收報後更新該頁快照表：每列覆寫為最新結果（覆寫式快照，歷史不留存於此頁）。**表格形狀固定 4 欄**（任務｜本週前三名｜資料日期｜榜單）——前三名用「A > B > C」短語呈現，**具體分數與取得方式（直接抓取／二手報導）一律寫在「快照細節與注意事項」區，不進表格**；更新每列「資料日期」與頁面「最後更新」；連續 2 週抓不到的榜在該列標「（連續 N 週無法取得，考慮汰換）」並回報使用者
3. 此為非新聞性更新，不動「最後新聞更新」；快照數字**不回寫** `model-comparison.md` 或各模型頁（快照只住這一頁，避免過期數字擴散）

### 6. CLAUDE.md 健檢

讀取 `wiki/CLAUDE.md`、`.claude/rules/wiki-ingest.md`、`.claude/rules/wiki-ingest-format.md`（已在 Step 1 載入，可直接檢查），依序執行下列各項檢查：

#### 6a. 規則矛盾偵測

逐段掃描，找出同一行為在不同章節有相反指示、同一情境觸發條件衝突、新舊規則語意重疊或互相否定。

→ 輸出：
```
⚠️ 矛盾：[規則 A 位置] vs [規則 B 位置]
  A 說：「…」
  B 說：「…」
  建議：保留 [A/B]，理由：…
```
→ **向使用者確認後再修改**，不自行決定保留哪條規則。

#### 6b. 規則引用驗證

逐一 grep 以下錨點，確認仍存在於對應檔案中：

| 規則描述中的引用 | 應存在於 | 驗證方式 |
|---------------|---------|---------|
| `首次出現` 欄 | `wiki/topics/community-tech-tools.md` | grep `\| 首次出現 \|` |
| `## 痛點洞察` 區塊 | `wiki/topics/community-tech-tools.md` | grep `## 痛點洞察` |
| `近期工具` 欄 | `wiki/topics/community-tech-tools.md` | grep `近期工具` |
| `## 技術彙整` 區塊 | `wiki/topics/community-tech-discussions.md` | grep `## 技術彙整` |
| `熱門討論` 表格 | `wiki/topics/community-tech-discussions.md` | grep `熱門討論` |
| `衍生` 欄 | `wiki/topics/community-tech-discussions.md` | grep `衍生` |
| `全覽表` 區塊 | `wiki/feature-radar.md` | grep `全覽表` |

輸出：
```
📎 引用驗證：
  ✅ `首次出現` 欄確認存在
  ⚠️ `XXX` 未找到 → 規則可能過時
```
→ 發現 ⚠️ 時向使用者說明，**不自行刪除規則**。

#### 6c. 規則遵守率抽樣

讀取 `wiki/log.md` 最近 3 筆 Ingest 條目，對照：

| 規則 | 合格標準 |
|------|---------|
| 每次 ingest 執行呈現品質審查 | log 含 ✅/⚠️/📋 標記，3/3 |
| 每次 ingest 更新 feature-radar.md | log 提及 feature-radar，3/3 |
| 新工具加入時更新痛點洞察近期工具欄 | 出現工具的 ingest 須提及 |
| log.md 格式正確（來源日報、更新頁面、摘要欄位） | 3/3 |

輸出：
```
🔍 遵守率抽樣（近 3 次 ingest）：
  ✅ 呈現品質審查 — 3/3
  ⚠️ 近期工具更新 — 1/3
```
→ 遵守率 < 2/3 的規則：說明原因，**向使用者確認是否調整規則**。

#### 6d. 規則年齡審查

`.claude/rules/wiki-ingest-format.md`、`.claude/rules/wiki-reporter-shared.md` 及各記者規則檔（`wiki-ingest-*.md`）中帶有 `[加入: YYYY-MM-DD]` 標記的 `##` 區塊，計算距今天數。

- **距今 > 60 天**：逐一確認規則描述的行為是否仍與現狀吻合
- **距今 ≤ 60 天**：記錄「在閾值內，無需審查」

輸出：
```
📅 規則年齡審查（今日 YYYY-MM-DD，閾值 60 天）：
  ⚠️ [規則名稱] [加入: YYYY-MM-DD]（距今 XX 天）→ 確認格式仍正確
  ✅ [規則名稱]（距今 XX 天）→ 在閾值內
```
→ ⚠️ 規則列出後**向使用者確認是否需要修訂**，不自行修改。

#### 6e. 來源健康檢查 `[加入: 2026-07-04，改版: 2026-07-16]`

讀取近 7 天 `web_reader/data/digest/*.json` 的 `sourceStatus` 陣列，統計每個來源的每日抓取數：
- 同一來源**連續 3 天 count=0** → ⚠️ 告警（可能是來源壞掉而非真的沒新聞，如時區 bug、RSS 改版、rate limit）
- 輸出各來源 7 天貢獻統計表，供判斷來源價值
發現 ⚠️ 時回報使用者，不自行修改管線程式。

**來源記分卡 `[加入: 2026-07-16]`：** 執行 `python scripts/source_scorecard.py`，將輸出表格附入本節回報。判讀規則（指標定義見 `docs/source-scoring-optimization.md`）：
- 標 ⚠️ 樣本不足的來源只讀趨勢，**不得**據以建議汰換
- 樣本充足（✅）且 Wilson 下界與 Presence 雙低的來源 → 列入「觀察名單」回報使用者，不自行動 pipeline 或 registry
- 出現「⚠️ 未註冊 slug」→ 檢查 `data/source_registry.json` 與記者回報的 slug 用字，回報使用者
- Google News 低信譽桶（pc1 < 0.4）> 0 筆 → 列出條目供人工覆核

#### 6f. 跨檔案語意矛盾掃描 `[加入: 2026-07-05]`

讀取 `.claude/commands/review-commands.md`「同步配對註冊表」列出的所有配對，逐組**語意比對**（非僅字面 grep）：兩側對同一行為的指示是否實質衝突（例如一方說「必須 foreground」另一方說「可背景執行」；一方列六類 subagent_type 但名稱與另一方不同）。

→ 輸出 dry-run 回報：
```
⚠️ 語意矛盾：[配對名稱]
  A 位置：[檔案:行號] 說：「…」
  B 位置：[檔案:行號] 說：「…」
  建議：保留 [A/B]，理由：…
```
若無矛盾則寫「✅ 全部配對語意一致」。

**向使用者確認後才修改**，不自行決定保留哪條規則。

#### 6g. 品質指標 `[加入: 2026-07-05，改版: 2026-07-27]`

**指標一：ref 覆蓋率（每週必跑）**——回歸偵測器：格式改動弄斷歸因時會連續每天壞，成本僅兩個 grep，不可等月報。

⚠️ **日報有兩種歸因格式，必須同時計**：`（ref: url）` 行內式為 2026-07-24 以前；`[N]` 註腳 ＋ 檔尾「今日聚焦參考連結」清單為 2026-07-25 起（格式定義見 `.claude/commands/news-pipeline-steps.md`「Step 1b：生成日報」）。**只計其中一種，會把新格式的日子讀成 0 而誤報覆蓋率暴跌**——2026-07-26 lint 實例：舊式單一 grep 誤報 71%，雙格式重算實際 97%。此為「回歸偵測器自己壞掉」的前例，改日報格式時必須回頭同步本節。

⚠️ **必須先限縮到「今日聚焦」區塊再數**：檔尾「選材門檻」附錄使用相同的 `- **[...]**` 條列形狀，不限縮會灌大分母（2026-07-26 實例：未限縮 7 條，實際 5 條）。

```
# 分母：今日聚焦條列數
awk '/^### 📌 今日聚焦/{f=1;next} /^### /{f=0} f' news/YYYY-MM-DD.md | grep -cE '^- \*\*\['
# 分子：帶歸因的條列數（兩種格式擇一即算）
awk '/^### 📌 今日聚焦/{f=1;next} /^### /{f=0} f' news/YYYY-MM-DD.md | grep -E '^- \*\*\[' | grep -cE '（ref:|\[[0-9]+\]'
```

對近 7 天每一天分別執行。覆蓋率 = 7 天分子總和 / 7 天分母總和。
- **< 80%** → ⚠️ 警示，列出哪幾天缺歸因
- **≥ 80%** → ✅ 通過
- 某天分母為 0（當日無「今日聚焦」區塊）→ 該天不計入分子分母，並在回報中註明是哪一天

**指標二：採用驗證率（僅每月第一次 lint 執行）**——慢變量（14 天升級窗口），週報只有雜訊。判斷方式：`wiki/log.md` 中本月尚無 `Lint` 記錄才執行；其餘週次輸出「非本月首次 lint，跳過採用驗證率」。
統計 `wiki/feature-radar.md` 全覽表與 `wiki/topics/community-tech-tools.md` 工具目錄中，14 天前標記 ⏳ 的條目，有多少比例在 14 天內升級為 ⚡ 或 ✅。
- 僅回報趨勢供判讀，**不觸發強制修改**

**指標三：外部死鏈（僅每月第一次 lint 執行，與採用驗證率同節奏）**——判斷方式同指標二：`wiki/log.md` 本月尚無 `Lint` 記錄才執行。
```
python scripts/check_links.py
```
掃描 `wiki/**/*.md`（不含 `news/`）中的外部連結，逐一 HEAD 請求驗證。輸出「疑似死鏈」清單（4xx/5xx/逾時）；429/403 標「可能反爬，人工確認」不算死鏈。
- 死鏈由對應類別記者在頁面上標註「（原文已失效）」（**保留原 URL 不刪**，供讀者仍可嘗試存取或查 web archive）
- 非本月首次 lint 時輸出「非本月首次 lint，跳過外部死鏈檢查」

輸出：
```
📊 品質指標（近 7 天 / 14 天窗口）：
  ref 覆蓋率：XX%（閾值 80%）→ ✅ / ⚠️（缺 ref 日期：…）
  採用驗證率：⏳→⚡/✅ 共 N 條中 M 條達成（XX%，僅供判讀）／非本月首次 lint，跳過
  外部死鏈：共 N 條疑似死鏈，已標註 M 條 / 非本月首次 lint，跳過
```

**趨勢表 append：** 算完以上指標後，在 `wiki/metrics.md` 表格 append 一列（只 append 不改舊列；月度指標非首次 lint 時該欄填「跳過」）；並讀最近 3 列，輸出一句趨勢判讀（持平／惡化中／已回升），**惡化中即使未破警戒線也要標 ⚠️**。

### 7. 讀者模擬驗收 `[加入: 2026-07-02]`

站在三種目標讀者（根目錄 `CLAUDE.md`「目標讀者」）的角度各出一題**本週真實會問的問題**（從近 7 天日報事件取材），模擬讀者從 `wiki/index.md` 出發：

| 讀者 | 問題類型範例 |
|------|------------|
| Claude Code 重度使用者 | 「現在該不該升版？」「X 功能壞了嗎？」 |
| AI 系統開發者 | 「Y 模式社群驗證結果如何？」「Z 的替代方案是什麼？」 |
| Anthropic 生態追蹤者 | 「W 政策事件現在進展到哪？」 |

**驗收標準：** 從 index.md 出發，**3 跳內**（index → 頁面 → 區塊）能否得到答案。

- ✅ 3 跳內找到 → 通過
- ⚠️ 找得到但超過 3 跳或散在多頁 → 修復：在最相關頁面補 callout / wikilink，或補 index.md 摘要欄
- ❌ 找不到 → 記錄至 log.md 待辦，回報使用者是否為結構性缺口

### 8. 記錄本次 lint

在 `wiki/log.md` 末尾 append：

```
## YYYY-MM-DD Lint

- 修正矛盾：（列出，若無則寫「無」）
- 補連結：（列出孤立頁面，若無則寫「無」）
- 狀態更新：（列出議題狀態變更）
- resolved 收尾：（列出，若無則寫「無」）
- 新增 entities：（列出，若無則寫「無」）
- 呈現品質：（列出修復或待辦的頁面，若全數通過則寫「全部通過」）
- 入口層健檢：（列出補結構的頁面，及語意分岔/死案候選處理結果：已處理 / 使用者稍後處理 / 無）
- 待查證回訪：（列出已更新條目、已改註「至今無後續」的條目，若無懸置標記則寫「無」）
- 規則檔健檢：
  - 矛盾：（列出，若無則寫「無」）
  - 引用驗證：（列出失效引用，若無則寫「全部通過」）
  - 遵守率：（列出 < 2/3 的規則，若全部通過則寫「全部通過」）
  - 過期規則（> 60 天）：（列出，若無則寫「無」）
  - 來源健康：（各來源 7 天統計，異常者列出 or 全部正常）
  - 跨檔案語意矛盾（6f）：（列出配對與建議，若無則寫「✅ 全部配對語意一致」）
  - 成長迴路（月度）：（立法提案 N 條／採納 M 條／觀察中 K 條，或「非本月首次 lint，跳過」）
- 品質指標（6g）：
  - ref 覆蓋率（每週）：XX%（閾值 80%），缺 ref 日期：（列出或「無」）
  - 採用驗證率（月度）：N 條中 M 條達成（XX%，僅供判讀）／非本月首次 lint，跳過
  - 外部死鏈（月度）：共 N 條疑似死鏈，已標註 M 條／非本月首次 lint，跳過
  - 趨勢判讀：（持平／惡化中／已回升，一句話）
- 跨家榜單週更（5b）：（已更新 N 榜／M 榜無法取得（列出）／失敗原因）
- 讀者模擬：（3 題結果：✅/⚠️ 已修復/❌ 待辦，各附一句說明）
- lint 自我遵守率：（N/6 位記者回報一次過；退回者列出類別與缺項）
- overview.md：已更新
```

### 9. 更新 wiki/index.md

同步所有因本次 lint 造成的頁面新增、移動、狀態變更。

### 10. 收尾閉迴路：commit wiki + build web + 單一 push `[加入: 2026-07-10]`

**為何必要：** lint 只改 `wiki/*.md`，web build 僅發生於本步驟與 `/news-pipeline`。若跳過本步，本次修正不會出現在 web reader，得等下一次日更 pipeline 才上站——這正是「週更網站沒更新」的根因。lint 結束前必須自行閉迴路（對齊根目錄 `CLAUDE.md`「完工定義」：測試綠 + 已 commit）。

依序執行（`REPO_ROOT` = `C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS`，`PYTHON` = `C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe`）：

1. **Commit wiki 變更**（先不 push）：`git -C REPO_ROOT add wiki/` → `git -C REPO_ROOT commit -m "wiki: weekly lint YYYY-MM-DD"`（wiki 無變更則跳過 commit，續下一步）
2. **強制 web build gate**：`PYTHON REPO_ROOT\scripts\gate_web_build.py`（此腳本代跑完整測試套件，不要另外自己跑 `run_tests.py` 再自行判斷——判準集中在腳本裡，才不會與 `.claude/commands/news-pipeline-steps.md` Step 4 失步）
   - 擋下（exit≠0）→ 跳過 build 與 web commit，仍執行步驟 4 推送已完成的 wiki commit
   - 放行（exit 0，含「測試失敗但全屬 `docs/known-test-gaps.json` 已登記缺口」）→ 續步驟 3
   - 兩種結果都在步驟 4 的心跳紀錄抄上腳本輸出的**最後一行摘要**，不要自己改寫措辭
   - 放寬理由與邊界見 `.claude/commands/news-pipeline-steps.md` Step 4 的說明區塊（2026-07-31 教訓：抓料端依賴缺口不該讓整站停更）
3. **建置 web 並 commit**：`PYTHON REPO_ROOT\scripts\build_web.py` → `git -C REPO_ROOT add web_reader/` → `git -C REPO_ROOT commit -m "web: rebuild YYYY-MM-DD（週更 lint 上站）"`
4. **心跳紀錄（無論成功／no-op／中止都必須寫）`[加入: 2026-07-27]`**：append 一行結果到 `src/logs/task_scheduler.log`（格式沿用該檔既有慣例，如 `[週六 YYYY/MM/DD hh:mm:ss.00] Weekly lint OK - 修 N 頁，M 項待確認，測試/build/push 結果`；no-op 寫 `Weekly lint OK (no-op) - 無頁面需修正`；中途失敗寫 `Weekly lint FAILED - <卡在哪一步>`）→ `git -C REPO_ROOT add src/logs/task_scheduler.log` → `git -C REPO_ROOT commit -m "chore: weekly lint heartbeat YYYY-MM-DD"`。**這一步是本步驟序列中唯一保證產生 commit 的步驟**——目的是讓「跑了但無事可改」與「靜默死亡」在 GitHub 上可分辨（2026-07-25 雲端 lint 無聲失敗、死因不可考的教訓：當時成功與死亡的 artifact 都是零）。對應每日 pipeline 的 `.claude/commands/news-pipeline-steps.md`「Step 6」（無論前面成敗都必須寫），本機與雲端行為一致。
5. **單一 push**：`git -C REPO_ROOT push`（本次所有 commit 一次推送，一次 push = 一個 Pages 部署，避免並發競爭；理由同 `.claude/commands/news-pipeline-steps.md` Step 5）

> 本步 commit 為實質改動閉迴路的一部分，**不可只留在對話裡**（同 SessionStart hook 的未 commit 提醒對象）。心跳紀錄在中止情境下照樣執行——lint 中途放棄時，先寫 FAILED 心跳並 commit push 再結束，不可靜默離開。

## 注意事項

- 繁體中文為主，英文術語保留英文
- 每次修改頁面都必須更新「最後更新」欄位
- `log.md` 只能 append，不可修改既有條目
- `news/` 目錄唯讀，不可修改
- 一頁一故事：resolved 議題留在原路徑，不遷移、不搬家，避免斷 wikilink
- 步驟 3f 語意分岔／死案歸檔：**必須等待使用者確認才能執行**，記者只負責回報分析
