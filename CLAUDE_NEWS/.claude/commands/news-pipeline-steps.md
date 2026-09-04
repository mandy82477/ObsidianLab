---
description: News Pipeline Agent 執行規範：Phase A（Step 0/1a/1b）與 Phase C（Step 3-6）步驟。由 news-pipeline.md spawn 的兩個背景 Agent 分別讀取本檔案執行對應段落；Step 2 不在本檔案，由呼叫 /news-pipeline 的 session 親自執行（見 `.claude/commands/news-pipeline.md` Phase B）。
---

# News Pipeline Steps（Agent 執行規範）

此檔案由 `.claude/commands/news-pipeline.md` spawn 的兩個背景 Agent 分別讀取：Phase A agent 只執行 Step 0/1a/1b；Phase C agent 只執行 Step 3-6。**兩個 agent 皆不 spawn 子 agent。**

**Step 2（wiki ingest 記者派工）不在本檔案，也不可包進任何背景 agent**——背景 agent 再派 agent 時，記者的完成通知會被系統送到最上層 session 而非派工的背景 agent，導致 pipeline 永久卡死（已實際發生過）。Step 2 改由呼叫 `/news-pipeline` 的 session 親自執行，依 `.claude/commands/wiki-ingest.md` 完整步驟，細節見 `.claude/commands/news-pipeline.md` Phase B。

## 設定

```
REPO_ROOT = C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
PYTHON    = C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe
模型      = Sonnet（由 spawn 時指定，全程使用，無需切換）
```

TARGET_DATE 由 Agent prompt 傳入。

---

# Phase A 步驟（Step 0 / 1a / 1b）

## 本機與雲端的行為必須一致 `[加入: 2026-07-25]`

**本檔是唯一的步驟語意來源。** 本機 `/news-pipeline` 與雲端 routine 跑出來的行為必須相同——同樣的閘門、同樣的失敗處理、同樣的重試、同樣的產物。

雲端 runbook（`docs/cloud-runbooks/daily.md`）**只允許承載環境差異**，共三類，其餘一律寫在本檔：

| 允許出現在 runbook 的 | 不允許（必須寫在本檔） |
|------|------|
| 環境值（路徑、`python3` vs `python.exe`、日期取得方式） | 任何閘門、檢查、重試、失敗處理邏輯 |
| 哪些步驟不適用該環境（雲端跳過 Step 1a，因抓料由 GitHub Actions 完成） | 步驟本身的做法與判準 |
| 無人值守政策（需使用者確認的動作改寫成待辦） | 需要確認的是哪些動作 |

> 判斷標準：這條規則換到另一個環境還成立嗎？成立 → 寫在本檔。只在特定環境成立 → 才進 runbook。（反例見沿革檔 2026-07-25 A）

---

## Step 0：昨日缺跑檢查

**僅當 TARGET_DATE 為今日時執行**（backfill 模式，即 TARGET_DATE 非今日時跳過本步驟——補跑歷史日期時「昨天」無意義）。

計算 TARGET_DATE 的前一天 YESTERDAY，檢查 `news/YESTERDAY.md` 是否存在：
- 存在 → 一行帶過，繼續 Step 1a
- 不存在 → 記錄缺失，於完成摘要表加一列「⚠️ 昨日（YESTERDAY）日報缺失」，並提示使用者可執行 `/news-pipeline` 帶日期參數手動補跑；Step 6 log 寫入 `WARN: yesterday digest missing (YESTERDAY)`。**不自動補跑**（避免排程場景下連鎖跑兩天造成時間不可控）

---

## Step 0b：冪等閘 `[加入: 2026-07-25]`

檢查 `news/TARGET_DATE.md` 是否已存在：

- **不存在** → 正常繼續
- **已存在，且 TARGET_DATE 是今日（排程／無參數模式）** → **中止**，理由 `digest already exists`，寫入 Step 6 log 後結束。重跑會覆寫日報並讓 wiki 記者對同一批新聞重複 prepend——日報覆寫還能重生，**wiki 重複條目要人工逐頁挑，代價高得多**
- **已存在，但 TARGET_DATE 由參數明確指定（backfill 模式）** → 使用者已明示覆寫意圖，**不中止**，但在完成摘要標一行 `⚠️ 覆寫既有日報 TARGET_DATE`，並提醒 wiki ingest 可能產生重複條目、需人工核對

會觸發此閘的情境：手動觸發撞上排程、當日已補跑過、或前次執行日報已產出但後段失敗。

---

## Step 1a：新聞抓取（Python，不呼叫 LLM）

用 Bash 執行：

```
cd REPO_ROOT\src
PYTHON -m news_aggregator.main --gather-only [--date TARGET_DATE]
```

- 若 TARGET_DATE 非今日，加上 `--date TARGET_DATE`
- 成功後寫出 `src/gathered_items.json`（含 items、date、source_status）
- 若失敗（exit code 非 0），停止並回報錯誤，不繼續後續步驟

**抓完立刻歸檔（強制）`[加入: 2026-07-25]`：**

```
PYTHON REPO_ROOT\scripts\archive_gathered.py
```

把原料存一份到 `src/gathered_archive/<date>.json`（保留 14 天）。`gathered_items.json` 沒有按日分檔、每次抓料直接覆寫，沒有這份副本的話，**日報沒產出的那天、已抓到手的原料會在隔天被蓋掉，而來源視窗早已滾過去——那天就永久漏了**。GitHub Actions 的 `daily-gather` 呼叫同一支腳本，兩邊行為一致。

---

### 補跑（backfill）注意事項 `[加入: 2026-07-25]`

雲端漏跑後在本機 `/news-pipeline <date>` 補，有四個已知摩擦點：

**1. 別把 `src/gathered_items.json` commit 上去。** 補跑會**覆寫**這個檔（它沒有按日期分檔），寫進去的是補跑那天的資料。這個檔同時是雲端 routine 的輸入——雲端啟動時讀到的若不是當日資料，新鮮度防線會中止當天執行。也就是**一次本機補跑可能連帶讓當天的雲端排程空跑**。
- 只有 GitHub Actions 的 `daily-gather` 該 commit 這個檔
- 還原動作與**時機**見本檔 `Step 5` 的「replay 路徑收尾」，此處不重複——時機是有講究的（太早會讓 Step 1c、Step 2 讀到錯的日期，太晚會讓 push 重試失效），兩處各寫一份就會失步，而失步的那一份會在無人值守時生效
- 絕不要在補跑流程裡用 `git add -A` / `git add .`

**2. 先找當日原料副本，找不到才重抓。** `src/gathered_archive/<date>.json` 是抓料當下存的原料副本（保留 14 天，由 GitHub Actions 與本機 Step 1a 各自寫入）：

- **副本存在** → **跳過 Step 1a**，直接 `cp src/gathered_archive/<date>.json src/gathered_items.json`，然後從 Step 1b 開始。這是 replay 當天的真實原料，補出來的日報與原本該產出的一致
- **副本不存在**（超過 14 天，或那天連抓料都失敗）→ 才走 Step 1a 重抓。此時要有心理準備：來源多是 RSS／API 的近期視窗，撈不到幾天前的內容。gather 的失敗補撈機制把回看窗口最多拉到 **50 小時**（約兩天），`--date` 補跑則以「目標日 00:00 UTC 到現在」為窗口再裁切回目標日——**離現在越遠，補出來的日報越空，超過兩三天基本上補不回來**。這是來源特性不是 bug；接受那幾天較稀疏，不要為了填滿而放寬收錄門檻

**3. 補跑不套用跨日去重快取**（`main.py` 明文：backfill 不碰 cache，否則會拿今日的快取去誤刪過去的項目）。因此補出來的日報**可能與前後日的日報有重複條目**，屬預期行為，wiki ingest 端由 `wiki-ingest.md` 的「確認最近是否已處理過同一份日報」把關。

**4. 補跑日報已存在時**：`Step 0b：冪等閘` 會因為你明確給了日期參數而放行覆寫，但 wiki 那邊會產生重複條目，需人工核對——見該步驟說明。

---

## Step 1b：生成日報

### 機械契約字串（勿改；新增時登記 `.claude/review-registry.json`）`[加入: 2026-09-04]`

**script 會 grep 的字串只住這張表**，下方規則引用時指回本表、不另抄。改任何一格必須同步右欄消費端。

| 契約字串／形狀 | 消費端 | 改壞的後果 |
|---|---|---|
| 區塊標題 emoji（📌⭐🔧💰📰💬🧭📡） | `build_web.py` SECTION_EMOJI → JSON key（`app.js` 消費的是 key，不是 emoji） | 該區塊整段不進網站，且被吞進前一區的 body |
| 標頭 `**日期：** … \| **來源：** X/10 \| **文章數：** N \| **更新時間：** …` | `build_web.py` header_re／gen_re／src_count_re | 日期／文章數／來源比全部落空（`test_digest_contract.py` 會擋） |
| 聚焦行 `- **[標籤]** 說明（[來源名](url)）` | `build_web.py` FOCUS_RE／FOCUS_INLINE_LINK_RE／FOCUS_INLINE_GROUP_RE、`app.js` focus 渲染 | 裸 markdown 上站、badge 全站消失 |
| 條目三行式：`**[標題](url)**`＋說明＋`` `來源` · MM/DD HH:MM UTC``（討論區末加 `情緒：`） | `build_web.py` STORY_RE／SOURCE_RE、3a 自檢 | 條目解析不到，整則消失 |
| 🧭 行 `- **[標題](url)** — 說明（→ 專頁名）` | `build_web.py` TOPIC_RADAR_RE | 雷達區不進網站 |
| 📡 表 `\| 來源 \| ✅/❌ \| 條數 \|` | `build_web.py` SOURCE_TABLE_RE、3b 自檢、lint 6e | 來源健康檢查斷炊 |
| 聚焦區塊錨點 `### 📌 今日聚焦`（含 `###` 層級）＋聚焦條列必以 `- **[` 起頭（連字號 6g 必要） | wiki-lint 6g 分子分母 awk／grep、`build_web.py` FOCUS_RE | 覆蓋率誤報暴跌或灌大分母 |

**0-1. 新鮮度防線（強制，生成前先做）`[加入: 2026-07-25]`**：讀取 `src/gathered_items.json`，確認 `date` 等於 TARGET_DATE 且 `items` 非空。

- 兩者皆滿足 → 繼續
- 任一不滿足 → **中止，不生成假日報**。Step 6 log 寫 `ABORTED: gathered_items.json date=<實際值> items=<數量>，非目標日期的新鮮資料`，結束

本機剛跑完 Step 1a 時這道檢查通常必然通過（資料才剛產生）；它真正保護的是**replay 路徑**——雲端每日班與補跑都是 `cp gathered_archive/<date>.json` 進來，而檔名只差一個字就會 replay 錯一天，這道檢查是唯一擋得住的地方。兩種環境都執行，不因「應該不會發生」而略過。

**0-2. 原料健康檢查（強制）`[加入: 2026-07-25]`**：新鮮度防線只擋「沒抓到」，擋不住「抓到但殘缺」——10 個來源掛 9 個仍會生出一份看起來正常、實則系統性偏食的日報，並被六記者沉澱進 wiki 變成長期污染。

```
PYTHON REPO_ROOT\scripts\check_gather_health.py
```

- **exit 0 且輸出無 ⚠️** → 正常生成
- **exit 0 但輸出有 ⚠️（失敗來源達警示數）** → 照常生成，但**必須**在日報的 `📡 來源狀態` 區塊上方加一行 `> ⚠️ 本日 N 個來源抓取失敗，涵蓋面較平日窄`，Step 6 log 一併記錄
- **exit 2 或 3** → **中止，不生成日報**。Step 6 log 寫 `ABORTED: gather health check failed`＋腳本輸出，結束

門檻與校準依據寫在腳本內（依 07-10~07-24 實績設定），要調整改腳本常數，不要在這裡另寫一套數字。

1. 讀取 `src/gathered_items.json`
2. 依照以下 prompt 格式，**直接**用繁體中文生成日報 Markdown（不呼叫任何外部 API）：

**System：**
> 你是一位專注於 Claude 與 Anthropic 生態的中文科技記者，擅長用繁體中文撰寫清晰、客觀的技術新聞摘要。
> 語氣分寸必須繼承來源，不得加碼：程度與嚴重度形容詞只能在來源原文有對應強度時使用；來源用中性或低強度字眼，摘要就對應保留該強度，寧可保守，不可放大。自我檢查法：你寫的每一個程度形容詞，都要能在 `gathered_items.json` 該則原文的標題或摘要裡找到同等強度的依據；找不到就降回中性描述。

**輸出結構（六個正文區塊 ＋ 選配的專頁雷達區塊，無內容則省略）：**

```
⚠️ 本區塊是混合體：以 #／###／表格開頭的行是要照抄的骨架，其餘散文與條列全是給你判斷用的規則。
規則一律判斷完即丟——日報成品內不得出現「選材門檻」「准入」「讀者契約」「冷讀者」「本區」「機械契約」
字樣的句子，也不得出現 [加入:]／[改版:] 標記（2026-07-25 與 2026-09-03 都發生過規則被原樣印進日報）。

# Claude Code & Anthropic 每日新聞摘要

**日期：** TARGET_DATE | **來源：** X/10 | **文章數：** N | **更新時間：** YYYY-MM-DD HH:MM UTC

---

### 📌 今日聚焦
3–5 點導讀，格式：**[標籤]** 說明（標籤：重大事件/持續追蹤/新工具/社群趨勢/風險警示）
標籤只描述類別，不授權升高語氣——即使掛 [風險警示]，說明文字的嚴重度仍以來源原文為準。

選材門檻（下列三條是**給你判斷用的**；`[改版: 2026-09-04]` **判斷完即丟，任何門檻文字都不寫進日報**——冷讀者實測：檔尾「選材門檻」附錄裸露規則檔路徑與「存活率 0/9」這類內規，是全篇唯一寫給內部人看的段落，已廢除）：
- **[新工具]**：單一 Show HN 工具未達互動門檻對照表（`.claude/rules/wiki-reporter-shared.md`）**中**門檻、且無跨來源佐證（source_count = 1）時，不單獨列入今日聚焦（校準顯示此類條目 30 天存活率 0/9）；多款工具同批亮相時歸入「⭐ 重點話題」，不逐一在聚焦具名——此時說明句以「同日 N 款同類工具亮相」作為今日訊號。
- **[風險警示]**：具名資安研究機構/研究者揭露、附具體攻擊鏈或 CVE 細節的條目優先；無具名背書的單一社群抱怨即使當日互動較高，也不優先於前者。
- **[持續追蹤]**：此標籤語意上向讀者承諾「這是有跡象會延燒的故事線」，須有多方訊號佐證。僅有單一低分來源（HN < 10 分且 source_count = 1）的指控/爭議類條目、或當日已修復的服務監控事件，**不得**標為 [持續追蹤]，也不獨立佔一條聚焦名額——改標 [風險警示]，或併入其他既有故事線內文一句帶過（2026-08-01 校準顯示此類條目 30 天後續產出 0/2）。

**每一條聚焦項目，凡有對應的參考新聞，在句末用行內連結引用** `[改版: 2026-09-04]`：格式 `（[來源名](url)）`，多則用頓號並列 `（[HN](url1)、[官方](url2)）`。來源名寫讀者認得的短名（媒體名／HN／官方／issue 編號），**不寫裸 URL、不用 `[N]` 腳注**——腳注要讀者跳到檔尾再跳回來，5 分鐘讀者不會做這個動作，等於聚焦沒有連結（2026-09-04 冷讀者實測；舊期的 `[N]` 檔尾清單格式已退場，不回溯改舊檔）。
- 若確實找不到對應新聞（例如是推論或背景說明）→ 可省略連結
- **此格式為機械契約**：形狀與消費端見本 Step 上方「機械契約字串」表；回歸測試 `src/tests/test_focus_inline_links.py` 會紅

範例：
- **[重大事件]** Claude 發布 Sonnet 4，context window 翻倍。（[官方](https://example.com/announcement)）
- **[社群趨勢]** Superset、OpenRig、VIR 三款工具同步亮相。（[HN](https://example.com/a)、[HN](https://example.com/b)）

### ⭐ 重點話題
跨多來源出現或引起大量討論的項目。三條准入 `[加入: 2026-09-04，冷讀者 review]`：
- **每則說明句必須讀得出「為什麼今天它是重點」**。合格的今日訊號限三種，且**必須在說明句寫出具體值**：(a) source_count ≥ 2（寫「N 個來源同日報導」）；(b) 當日互動達互動門檻對照表**中**門檻（寫出實際分數／讚數／留言數）；(c) 可指名的狀態變化（版本號、價格數字、狀態頁事件、issue 開／關）。三者皆答不出具體值 → 不進本區，改投對應區塊
- **`GitHub Search` 存量／發現條目不進本區**——星數是 repo 一生累積的規模、不是今日熱度，「本庫今日首次收錄」是內部事件不是讀者的新聞；一律歸 💬 技術熱度討論（見「存量盤點條目的寫法」）
- **排序依今日訊號強度**（跨來源數、當日互動），不依累積規模

### 🔧 技術更新
僅 category=official 的條目（GitHub release、Anthropic Blog）。**若今日無任何 official 條目，完全省略此區塊，不可用 community 條目填充。**

### 💰 付費方案動態 `[順序改版: 2026-09-04]`
定價、配額、Token 費用相關——**固定排在媒體報導之前**：這一區直接影響讀者的帳單與配額，冷讀者實測它被排在倒數第三時是「全篇最被低估的一條」。

### 📰 媒體報導
僅收錄 category=media 的條目（Reuters/WSJ/科技媒體等），不加情緒標籤。

### 💬 技術熱度討論
僅 category=community 的條目，每條末加 情緒：😊/😤/😐/🤔

**聚焦防重複 `[加入: 2026-09-04]`（適用所有正文區塊）**：已被「📌 今日聚焦」點名的條目，所屬區塊的說明句**必須至少含一個聚焦句沒有的具體元素**（數字、版本號、具名主體、機制細節、後續影響其一）；自檢法：兩句並排，答不出「這句哪個名詞或數字是聚焦句沒有的」就重寫，兩句連續 12 個字元相同亦視為複製。中文說明也不得只是標題直譯，答不出「比標題多說了什麼」就重寫。

### 🧭 專頁雷達（定向抓取）`[加入: 2026-08-13]`
**只放 `topic` 欄非空的條目**（來源標籤為 `Topic Watch / <slug>`），其餘區塊一律不得放這類條目。

這批是**為特定 wiki 專頁定向抓來的**，收錄判準是「對該專頁有無價值」，**不套用 Claude/Anthropic 關聯門檻**——它們的標題本來就不會提到 Claude（2026-08-05 Jeff Dean 等人離開 Google 創辦 Discovery Loop，就是因此漏了 8 天）。

- 每條一行：`- **[標題](url)** — 一句話說明（→ 專頁名）`，**上限 5 行**，超出者只列標題連結
- 讀者契約：正文六區塊維持 Claude/Anthropic 純度，本區自成一格，讀者一眼能分辨
- **升格例外**：僅當該條目本身重大（具名高管流動、競品重大定價變動、具體漏洞揭露）才可改列入「📌 今日聚焦」，此時**必須**在說明句標明它與 Claude/Anthropic 的關聯為何值得讀者知道；判斷不出關聯就留在本區
- 今日無此類條目時**整個區塊省略**

### 存量盤點條目的寫法 `[加入: 2026-08-28]`

`summary` 以 `[存量盤點｜YYYY-MM-DD 出生、本庫今日首次收錄]` 開頭的條目（來源 `GitHub Search`，每日至多 2 則），**不是今天發生的事**——它是既有的知名 repo，本庫今天才第一次看見。

- **不得寫進「📌 今日聚焦」，也不得寫進「⭐ 重點話題」**（`[改版: 2026-09-04]`——重點話題的讀者契約是「今天發生了什麼」，存量條目沒有今日訊號；冷讀者實測：抓取時刻的來源行時間戳讓最沒新聞性的條目看起來最新鮮），也不得用「今日發布」「新推出」這類措辭。一律歸「💬 技術熱度討論」尾端
- **說明句必須帶出生年月**，例：`（2026-02 出生、93,000 星，本庫今日首次收錄）`。讀者要能一眼分辨「這是我可能早就聽過、但本站漏掉的東西」；**星數一律千分位阿拉伯數字**（`3,002 星`），不用「萬」（兩種計數法混用讓讀者無法橫向比，2026-09-04 冷讀者實測）
- **情緒與位置**：存量條目一律標 `情緒：😐`（它不是當日討論，無社群情緒可判），且**排在 💬 區塊所有當日條目之後**，不與當日討論交錯
- **前綴要「翻譯」成括號說明，不是原樣照抄，也不是刪掉** `[改版: 2026-08-29]`
  - ✅ `**[obra/superpowers](url)**（2025-10 出生、279,000 星，本庫今日首次收錄）agentic skills 框架與軟體開發方法論…`
  - ❌ 原樣照抄：`**[obra/superpowers](url)** [存量盤點｜2025-10-09 出生、本庫今日首次收錄] 累計…`（方括號標記是給你看的機器訊號，讀者看到會以為是系統雜訊）
  - ❌ 整段刪掉：讀者會把 279,000 星的東西誤讀成今天剛發布
  - ❌ 用「萬」：`27.9 萬星`——與其他條目的千分位寫法混用，讀者無法橫向比

### 📡 來源狀態
從 `gathered_items.json` 的 `source_status` 欄位生成表格，格式嚴格如下（web reader 解析器依賴此格式）：

| 來源 | 狀態 | 條數 |
|------|------|------|
| Anthropic Blog | ✅ | 0 |
| Hacker News | ✅ | 13 |

（每個來源一列，依 `source_status` 全部列出；`ok=true` → ✅，`false` → ❌）

---

```

**檔尾 `[改版: 2026-09-04]`**：📡 來源狀態表即是檔案結尾——「選材門檻」附錄與「今日聚焦參考連結」清單皆已廢除（門檻是內規不上讀者版；聚焦連結已改行內）。來源狀態表**上方最多兩行 `>` 說明，順序固定**：
1. Step 1b 0-2 原料健康檢查的 `> ⚠️ 本日 N 個來源抓取失敗，涵蓋面較平日窄`（有觸發才寫）
2. 缺席區塊說明：五個常設正文區塊（⭐／🔧／💰／📰／💬）本日省略者合併一行讀者語言說明（如 `> 本日 Google News 0 則故無媒體報導區；無官方發布故無技術更新區`）；🧭 專頁雷達為選配，省略不寫說明

**每條排版格式（⚠️ 嚴格遵守，web reader 解析器依賴此格式）：**
```
**[原文標題](url)**
一到兩句繁體中文說明核心重點與為何值得關注。
`來源名稱` · MM/DD HH:MM UTC
```
- 標題行必須是 `**[標題](url)**`（方括號連結），**不可**寫成 `- **標題**：內文` 的 bullet 形式
- 來源行必須是 `` `來源` · 時間 `` 獨立一行
- 違反此格式時 web reader 會解析出空區塊，讀者只看得到今日聚焦
- **多來源條目要把來源全部列出 `[加入: 2026-08-16]`**：`gathered_items.json` 的 `contributors` 非空時（dedup 併掉的其他來源），來源欄寫成 `` `勝出來源 ＋其他來源、其他來源` ``，例如 `` `Hacker News ＋Anthropic Blog、Google News / PCMag` ``。只寫勝出來源會讓低流量官方來源在下游的來源記分卡上長期顯示零貢獻（教訓見沿革檔 2026-08-15）。解析器不受影響——`SOURCE_RE` 對反引號內是自由文字
- `gathered_items.json` 每條含 `score_unit` 欄位（分＝HN points、留言＝評論數），選材比較熱度時注意單位不同不可直接互比
- 跨來源比較熱度時的粗略等價量級：HN 30 分 ≈ Reddit 50 讚 ≈ 10 則留言 ≈ dev.to 20 讚；source_count ≥ 2（跨來源報導）視為高於任何單來源分數的訊號
- `source_count > 1` 表示多個獨立來源報導同一事件，選材時視為重要度加權訊號

3. 生成完成後，寫入 `news/TARGET_DATE.md`（完整 Markdown）

3a. **格式自檢（強制）**：寫入後執行下列指令，若輸出為 0 表示條目格式錯誤，必須依「每條排版格式」重寫再檢：
```
grep -cE '^\*\*\[.+\]\(https?://' news/TARGET_DATE.md
```
（今日聚焦以外的每個區塊各條目都應貢獻一個匹配；正常日報此數值 ≥ 5）

3a-2. **內規外洩自檢（強制）`[加入: 2026-09-04]`**：
```
grep -nE '選材門檻|准入|冷讀者|讀者契約|機械契約|本區|\[改版:|\[加入:|存活率|source_count' news/TARGET_DATE.md
```
（**應為零命中**——任何命中都代表規格文字被印進讀者版；2026-07-25 與 09-03 都發生過。刪除該段再檢）

3b. **來源狀態表存在性檢查（強制）**：
```
grep -c "^| .* | [✅❌] | [0-9]" news/TARGET_DATE.md
```
（應 ≥ 8，代表來源狀態表已寫入；若不足，補寫 📡 來源狀態區塊再檢）

3c. **分層原則（不是檢查，是判斷依據）`[加入: 2026-07-26]`**：

**日報是給讀者看的，只留讀者要讀的重點，篩掉一部分是預期行為，不必也不該塞進全部抓到的東西。** 你依「每條排版格式」寫進日報的，是你判斷讀者需要讀的那些。

被你篩掉的條目**不會消失**：`scripts/list_digest_omissions.py` 會把差集列出來餵進 wiki ingest 的分類與派工，由各類別記者依自己的門檻判斷收不收（見 `.claude/commands/wiki-ingest.md`）。**沉澱層要考慮全部，呈現層只留重點**——兩層各司其職，所以你可以放心篩。

⚠️ 但選材門檻那三條只用於挑選「📌 今日聚焦」那 3–5 條導讀，**不是**日報其他區塊的收錄門檻；其他區塊要不要收，用你對讀者價值的判斷，不要套聚焦專用的數字門檻。

3d. **摘要忠實度自檢（強制）`[加入: 2026-07-17，措辭更正: 2026-07-26]`**：抽樣核對說明句是否忠於原文——**凡進了日報的條目，記者就是讀你寫的摘要來沉澱**（未進日報者另走 `scripts/list_digest_omissions.py` 直接餵原始抓取資料），摘要失真會被沉澱成長期污染：
- 抽樣：今日聚焦**全抽**＋其餘區塊各抽 1 條（合計約 8–10 條）
- 逐條對照 `gathered_items.json` 中同 URL 條目的 `title` / `summary`：說明句中的**事實成分**（數字、版本號、主詞、因果、結論）必須能從原文支撐；原文沒有的具體數字或結論不可出現
- 不符 → 以原文為準改寫該條說明句，改寫後重檢
- 結果記入本 Step 回報（「忠實度自檢：抽 N 條，改寫 M 條」）；**M ≥ 3 視為摘要品質異常**，除改寫外須在回報中標 ⚠️ 供使用者判斷是否深查
- 判斷原則：這是「忠實」檢查不是「精彩」檢查——語氣、取捨、詳略不管，只管事實有沒有依據

3e. **週報未結案預告偵測（機械，非 LLM）`[加入: 2026-08-02]`**：用 Bash 執行

```
PYTHON REPO_ROOT\scripts\scan_open_forecasts.py TARGET_DATE
```

- 讀 `weekly/` 最新一期的未結案預告，取其判準結尾的「｜查證：關鍵字」對今日日報做字串比對，命中則 append 至 `weekly/open-signals.jsonl`，供下期 `/weekly-report` 回收時取用（免去憑記憶重讀七天日報）
- **純字串比對，不做判斷、不改日報**；命中與否都不影響本日產出，失敗只記錄不阻斷 pipeline
- ⚠️ **此步驟必須留在選材與寫入之後**：若讓選材階段知道週報正在賭什麼，會產生確認偏誤——選材傾向撿能證實預告的條目，命中率虛高，並連帶破壞每月聚焦校準的獨立性（校準量測的正是選材品質，兩者不得互相知情）。規格見 `.claude/commands/weekly-report.md` 第 (3) 段

3f. **懸置標記命中偵測（機械，非 LLM）`[加入: 2026-08-10]`**：用 Bash 執行

```
PYTHON REPO_ROOT\scripts\scan_pending_verifications.py TARGET_DATE
```

- 拿 wiki 全庫「懸置標記」（見 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節）的探針比對今日日報，命中則 append 至 `data/pending-signals.jsonl`，並在 stdout 印出依記者分組、可直接貼進派工的附件
- 輸出由執行 Step 2（wiki ingest）的主 session 取用：把對應記者類別的派工附件段落原樣附在該記者的派工訊息裡，讓記者知道「今天日報可能回答了哪個懸置」
- **B 級（僅單一弱探針命中且僅在內文）不進派工附件**，只記入 jsonl 供之後查核，不得轉貼給記者
- **純字串比對，不做判斷、不改 wiki**；失敗只記錄不阻斷 pipeline，不影響本日其餘產出

3g. **截止日到期前強制官方複查（機械，非 LLM）`[加入: 2026-08-28]`**：用 Bash 執行

```
PYTHON REPO_ROOT\scripts\scan_expiring_deadlines.py
```

- 掃全 wiki 的「⏰ 倒數中」表列與散文 `⏰ YYYY-MM-DD` 標記，列出**已過期**與**7 天內到期**者
- **記者不處理這批**（無 web 工具，不可自行推斷）。輸出接進 Step 6 的完成摘要「📋 待使用者裁示」，由主編層 WebFetch 查官方原文後三選一：日期仍有效 → 不動／已延長 → 更新截止日並記事件／已作廢 → 移除倒數並**回掃全庫引用方**（同一截止日常散在 3 處以上，只改一處等於沒改）
- 無命中時印「無需複查的截止日」，不佔用摘要版面；失敗只記錄不阻斷 pipeline

4. 用 Bash git 暫存並 commit（**先不 push**，本次所有變更於 Step 5 統一推送，避免多次 push 觸發 Pages 部署並發競爭）：
```
git -C REPO_ROOT add news/TARGET_DATE.md
git -C REPO_ROOT add data/pending-signals.jsonl
git -C REPO_ROOT commit -m "news: daily digest TARGET_DATE"
```
- `data/pending-signals.jsonl` 為 3f 產出（懸置標記命中紀錄），無變更時 `git add` 為 no-op，不影響 commit
- 若 commit 失敗，停止並回報錯誤，不繼續後續步驟

---

## Step 1c：確認 emitted-cache（強制，commit 成功後才執行）

```
cd REPO_ROOT\src
PYTHON -m news_aggregator.main --confirm-digest --date TARGET_DATE
```

- 把 Step 1a 篩出的項目標記 `digest_confirmed: true`；未確認的項目視同未出現過，下次重跑會重新提供、不會被永久靜默丟棄（2026-07-13 曾因日報未產出導致 25 則新聞永久漏失，詳見當日 log）
- 失敗只記警告，不影響已完成的 news commit，繼續後續步驟
- **確認結果必須進 git（強制）`[加入: 2026-07-25]`**：`--confirm-digest` 改的是 `src/news_aggregator/emitted_items.json`，這個檔不 commit 就等於沒改過——GitHub Actions 與雲端 routine 都是全新 checkout，讀的是 repo 版本。執行完 append 下列指令，讓它跟著 Step 5 的統一 push 一起上去：
  ```
  git -C REPO_ROOT add src/news_aggregator/emitted_items.json
  git -C REPO_ROOT commit -m "data: confirm emitted-cache TARGET_DATE"
  ```
  （無變更則跳過。**不要單獨 push**，一律留給 Step 5。這樣「日報上站」與「快取確認」同批推送，要嘛一起成功、要嘛一起回到未確認狀態，不會出現「確認了但日報沒上站」的不一致）
- 漏做的實際後果見沿革檔 2026-07-24

---

## Step 2：Wiki Ingest（不在本檔案）

Step 2 由呼叫 `/news-pipeline` 的 session 親自執行，完整步驟見 `.claude/commands/wiki-ingest.md`（不在此重複，避免兩份副本失步）。執行方式與失敗處理原則見 `.claude/commands/news-pipeline.md` Phase B：Step 2 失敗時記錄但仍進入 Phase C（web build 不依賴 wiki）。

---

# Phase C 步驟（Step 3 / 4 / 5 / 6）

## Step 3：Commit Wiki 變更（不 push）

用 Bash 執行（**先不 push**，於 Step 5 統一推送）：

```
git -C REPO_ROOT add wiki/ data/source_attribution.jsonl data/pending-handoffs.jsonl
git -C REPO_ROOT commit -m "wiki: auto-ingest TARGET_DATE"
```

- `data/source_attribution.jsonl`（來源歸因）與 `data/pending-handoffs.jsonl`（轉知帳本）是 Step 2 主編彙整的產出，與 wiki 同批 commit；無變更時 `git add` 為 no-op
- 若 wiki 無任何變更，跳過 commit，繼續 Step 4

---

## Step 4：建置 Web Reader

**建置前先跑 web build gate（強制，內含完整測試套件）：**

```
PYTHON REPO_ROOT\scripts\gate_web_build.py
```

此腳本會代跑 `scripts/run_tests.py`，再依 `docs/known-test-gaps.json` 判定該不該擋。**不要另外自己跑 `run_tests.py` 再自行判斷**——判準集中在腳本裡，才不會兩處失步。

- **exit 0** → 放行，繼續執行 build（可能是「全綠」，也可能是「失敗但全屬已登記缺口」；後者腳本會印出放行理由）
- **exit 非 0** → **先走下方「gate 擋下時的修復迴圈」，不可直接跳過 build**；迴圈仍失敗才視同 Step 4 失敗：跳過 web build 與 web commit，但仍繼續 Step 5（推送已完成的 news / wiki commit）與 Step 6（記錄 log）

### gate 擋下時的修復迴圈 `[加入: 2026-08-26]`

你是 LLM agent，gate 印出的失敗訊息你讀得懂也多半修得好——擋下就放棄等於把「讀者今天看不到網站」當成對一個格式瑕疵的懲罰。（教訓見沿革檔 2026-08-26）

**流程（至多修 2 輪，每輪：讀失敗 → 修 → 重跑 gate）：**

1. 讀 gate 輸出，定位失敗的檢查與檔案行號（輸出通常直接給到 `頁面:行號` 或測試案例名）
2. 判斷失敗屬於哪一類，只修**允許清單**內的：

| 失敗類型 | 可否自行修復 | 修法 |
|---|---|---|
| wiki 內容格式（懸置標記語法、探針不合格、欄位缺漏、日期格式、表格對帳差一列） | ✅ | 依對應規則檔修 `wiki/` 內容本身（如探針改寫成合規字串），修完併入本次 wiki commit（`git commit --amend` 或補一個 `wiki: fix gate failure` commit） |
| 規則檔同步配對／錨點（`check_rules.py`），且是**本次 pipeline 改動造成** | ✅ | 修回一致 |
| 單元測試失敗、腳本層 bug、環境依賴缺失 | ❌ | 不修——腳本改動需要人工 review，照舊擋下並回報 |

3. 重跑 `gate_web_build.py`：exit 0 → 繼續 build，Step 6 log 在摘要行後**多記一行** `REPAIRED: <一句話：修了什麼>`；仍非 0 → 進第 2 輪；2 輪後仍失敗 → 放棄，照舊跳過 build 並在 log 記 `repair attempted, still blocked`

**硬性禁止（違反任一條就等於把 gate 拆掉）：**
- 不可修改任何 `scripts/check_*.py`、`run_tests.py`、`gate_web_build.py`
- 不可為了放行而新增 `docs/known-test-gaps.json` 條目（該檔只在人工登記 workaround 時動）
- 不可用「刪掉觸發失敗的內容」了事——探針寫錯要改對，不是把整條懸置標記刪掉；刪除等於湮滅待查證事項
- 修復只准動失敗訊息**指名**的位置，不可順手擴大改動範圍

Step 6 的 log 一律抄腳本輸出的**最後一行摘要**（例如 `測試失敗 3 案，全屬已登記缺口（feedparser-sgmllib）- web build 放行`），不要自己改寫措辭——log 是日後判斷「哪天為什麼沒上站」的唯一證據。

> **為何是 gate 而不是直接看測試結果 `[加入: 2026-08-01]`：** 過緊的 gate 用「正確性」的名義製造「可用性」的損失。放寬的邊界很嚴格：**只有登記在 `docs/known-test-gaps.json`、且錯誤訊息也對得上的失敗才放行，出現任何一個沒登記的失敗就照舊全擋**；允許清單空的時候，行為等同舊規則。（教訓見沿革檔 2026-07-31）

- 放行後依序執行（frontmatter 必須先於 build_web，兩者都吃當日已寫完的 wiki）：

```
PYTHON REPO_ROOT\scripts\enrich_attribution_publisher.py
PYTHON REPO_ROOT\scripts\gen_wiki_frontmatter.py
PYTHON REPO_ROOT\scripts\build_web.py
```

- 前兩支皆為冪等的衍生資料重算，失敗不擋 build：
  - `enrich_attribution_publisher.py` 補當日新歸因的 `publisher` 欄位（記者回報的 slug 只有斜線前半段，`google-news` 底下實際有 250+ 家出版者）
  - `gen_wiki_frontmatter.py` 重算頁面 frontmatter（入鏈數、供料數、停滯天數、signal），供 Obsidian Bases 查詢；不跑則 `wiki/_views/wiki-health.base` 的數字會停在上次生成日
- `build_web.py` 成功後繼續；若失敗，回報錯誤並跳過推送

---

## Step 5：Commit Web 並統一推送（單一 push）

先 commit web 變更，再用**單一 git push** 一次推送本次所有 commit（news + wiki + web）。

**為何單一 push：** 每次 `git push` 都會觸發一個 GitHub Pages 部署。分多次 push 時，多個部署會互相搶佔（concurrency race），最後關鍵的 web 部署可能被取消或失敗，導致線上停留舊版而 pipeline 無從得知。一次推送 = 一個部署 = 無 race。

```
git -C REPO_ROOT add web_reader/
git -C REPO_ROOT commit -m "web: rebuild TARGET_DATE"
# 統一推送本次所有 commit（一次 push 只觸發一個 Pages 部署）
git -C REPO_ROOT push
```

- 若 web build 無變更，仍須執行 `git -C REPO_ROOT push` 推送先前的 news / wiki commit
- **replay 路徑收尾（強制）`[改版: 2026-08-29]`**：本次若曾 `cp src/gathered_archive/<date>.json src/gathered_items.json`（backfill 模式，以及雲端每日班——它現在也走這條路徑），**必須在 Step 1c 之後、任何 push 之前（含中止落地的那次）**執行 `git -C REPO_ROOT checkout -- src/gathered_items.json` 還原成 repo 版本。
  - **不可等到 push 之後**：本 repo 的 `rebase.autoStash` 為 false，工作樹髒的話下方 push 重試的 `git pull --rebase` 會被 git 直接拒絕（不是衝突，是前置檢查），兩次重試必然失敗，而雲端未推送的 commit 隨容器銷毀救不回來——日報、wiki、web 全部白做
  - **不可提早到 Step 1c 之前**：`--confirm-digest` 讀的就是這個檔；Step 2 的專頁定向路由也吃它的 `topic` 欄（那是該欄唯一的來源）
  - **中止路徑也算**：cp 之後才觸發的中止（新鮮度防線、原料健康檢查 exit 2/3）同樣要先還原再 commit abort log，否則 abort log 推不上去、雲端看起來像中途死亡，把一次正確的閘門攔截誤報成靜默失敗

**push 失敗重試（強制）`[加入: 2026-07-25]`**

push 被拒最常見的原因是 non-fast-forward——GitHub Actions 的 `daily-gather` 或另一個環境在你執行期間也 push 了（Actions 排程實測延遲過 2 小時 42 分，時間緩衝不保證不撞）。**在雲端，未推送的 commit 會隨容器銷毀且下次是全新 checkout，救不回來**；本機雖然 commit 還在，仍應照同樣程序處理，兩邊行為一致。

```
git -C REPO_ROOT rev-parse --abbrev-ref HEAD   # 不是 master 就先 git checkout -B master
git -C REPO_ROOT push || {
  git -C REPO_ROOT pull --rebase origin master && git -C REPO_ROOT push
}
```

- 最多重試 **2 次**，每次都先 `pull --rebase` 再 push
- 先確認在 master 上：2026-07-14 曾因 session 啟動時 `origin/master` 快取落後而處於 detached HEAD，該狀態下 push 不會更新遠端分支
- **允許自動解的衝突只有兩類**：
  1. `src/news_aggregator/emitted_items.json`——此檔有兩個寫者（GitHub Actions 加入未確認條目、pipeline 翻確認欄位）。解法固定：**放棄我方的 confirm commit、保留遠端版本**，因為日報上站遠比確認欄位重要，未確認的條目只會被重新提供一次，是良性退化。處理後標「emitted-cache 確認本次放棄，項目將於次日重新提供」
  2. **append-only 檔的 append-append 衝突 `[加入: 2026-09-03]`**——`wiki/log.md`、`data/source_attribution.jsonl` 等只會在檔尾各自新增的檔（白名單住 `scripts/resolve_append_only.py` 的 `APPEND_ONLY`，不在此重抄）。解法固定：**跑 `python scripts/resolve_append_only.py`**，它以 `git merge-file --union` 三方合併保留兩側新增（順序 base→ours→theirs），只動白名單內的檔；有任何白名單外的衝突它會 exit 1 且不動任何檔——此時走下一條 abort。成功後 `git -c core.editor=true rebase --continue` 再 push。
     > 沒有判斷成分的衝突不該逼整班重跑。（起因見沿革檔 2026-09-02）
- **其他任何檔案的衝突 → 不自行解**：`git rebase --abort`，Step 6 log 記 `Push FAILED - rebase conflict`，並列出衝突檔案清單
- 兩次都失敗 → Step 6 log 記 `Push FAILED`，完成摘要明確標示**本次產出全部未上站**，不可寫成完成

---

## Step 6：寫入 task_scheduler.log

整個 pipeline 結束後，**無論成功或失敗**，都必須 append 執行記錄至：

```
REPO_ROOT\src\logs\task_scheduler.log
```

**本步驟由 Phase C agent 執行**，Step 0/1a/1b（Phase A）與 Step 2（Phase B）的結果由呼叫 session 透過 Phase C 的 spawn prompt「已知結果」欄位傳入（見 `.claude/commands/news-pipeline.md` Phase C），Phase C agent 不需重新查證，直接引用即可；Step 3/4/5 的結果則是 Phase C agent 自己執行後得知。

**例外：若 Phase A 的 Step 1a 失敗**，pipeline 不會進入 Phase C（見 Phase B 的失敗處理），此時 Step 6 log 改由呼叫 session 直接 append，格式相同。

格式（依各步驟結果填入 OK / FAILED / SKIPPED）：

```
[DATE TIME] === Agent pipeline start (TARGET_DATE) ===
[DATE TIME] Aggregator OK
[DATE TIME] Wiki ingest OK
[DATE TIME] Building web reader...
[DATE TIME] Single push done (news + wiki + web)
[DATE TIME] === Pipeline complete (agent) ===
```

- Step 0 昨日缺跑時，額外寫一行 `WARN: yesterday digest missing (YESTERDAY)`
- Step 1 失敗時，寫 `Aggregator FAILED - stopping`，之後不繼續（此情況下由呼叫 session 直接寫入，見上方例外）
- Step 2 失敗時，寫 `Wiki ingest FAILED`
- Step 4 gate 判定時，抄 `scripts/gate_web_build.py` 輸出的最後一行摘要（放行與擋下都要寫，例如 `測試全綠 - web build 放行`／`測試失敗含未登記案例（...）- web build 擋下`）
- Step 4 build_web 失敗時，寫 `build_web FAILED - pushing news/wiki only`
- Step 5 push 失敗時，寫 `Push FAILED`
- 時間戳使用系統當前時間（`Get-Date` 或 `date` 指令取得），格式 `[週X YYYY/MM/DD HH:MM:SS.SS]`

---

## 完成摘要

完成後輸出：

| 步驟 | 結果 |
|------|------|
| Step 0 昨日缺跑檢查 | ✅ 無缺失 / ⚠️ 昨日（YESTERDAY）日報缺失 / ⏭️ backfill 模式跳過 |
| Step 1 新聞聚合 | ✅ / ❌ |
| Step 2 Wiki Ingest | ✅ / ❌ |
| Step 3 Wiki Commit | ✅ / ⏭️ 無變更 / ❌ |
| Step 4 Web 建置 | ✅ / ❌ |
| Step 5 統一推送（news+wiki+web） | ✅ / ❌ |
| Step 6 Log 寫入 | ✅ / ❌ |
| 目標日期 | TARGET_DATE |

### 📋 待使用者裁示 `[加入: 2026-08-08]`

摘要表之後**必接**此區塊——待確認事項只寫進 `wiki/log.md` 等於沒有出口，使用者不會讀那個檔（2026-08-02 提出的 feature-radar 防霸榜裁示因此擱置 6 天）。

作法：Grep `wiki/log.md` 中 TARGET_DATE 該次 ingest 紀錄的「📋 待使用者確認」段落，逐條轉貼成一行摘要（`- [頁面/主題]：一句話問題`）。同時 Grep 前 14 天的 ingest 紀錄，**同一議題重複出現者標「⏳ 已擱置 N 天」**置頂。

**另必接 Step 1b-3g 的截止日複查清單 `[加入: 2026-08-28]`：** 若 3g 有命中（已過期或 7 天內到期），逐個截止日轉成一行 `- ⏰ [YYYY-MM-DD]（剩 N 天，M 處引用）：[事件]——需查官方原文確認日期是否仍有效`。這批與 log.md 的裁示不同源，**不可因為 log.md 沒有對應段落就省略**；3g 印「無需複查的截止日」時整段省略。

無任何未決項時寫 `- 無`，不可省略此區塊。

---

## 注意事項

- 所有 Bash 指令使用絕對路徑，不依賴 PATH 環境變數
- Step 0 僅在 TARGET_DATE 為今日時執行；backfill 模式（TARGET_DATE 非今日）跳過
- Step 1 失敗時停止整個 pipeline（Phase A agent 立即停止，不進入 Phase B / Phase C，Step 6 log 改由呼叫 session 直接寫入）
- Step 2（wiki ingest，由呼叫 session 親自執行，不在背景 agent 內）失敗時記錄並仍進入 Phase C（Step 4 不依賴 wiki）
- Step 4 web build gate（`scripts/gate_web_build.py`）擋下時跳過 web build 與 web commit，仍須執行 Step 5 的統一 push；gate 放行（含「失敗全屬已登記缺口」）時照常 build
- Step 4（web build）失敗時跳過 web commit，但仍須執行 Step 5 的統一 push（推送已完成的 news / wiki commit）
- **所有 git push 集中在 Step 5 一次完成**；中途步驟（1b、3）一律只 commit 不 push，避免 Pages 部署並發競爭
- **Step 6 log 寫入必須執行**，即使前面步驟失敗也不能跳過
- **Phase A、Phase C 兩個背景 agent 皆不可 spawn 子 agent**；唯一會呼叫 Agent tool 派工的 Step 2，已移出本檔案、改由呼叫 session 親自執行
- 繁體中文輸出

---

> **沿革檔：** `docs/rules-changelog/news-pipeline-steps.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，`[加入: 2026-09-04]`）
