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

> 判斷標準：這條規則換到另一個環境還成立嗎？成立 → 寫在本檔。只在特定環境成立 → 才進 runbook。
> 反例（2026-07-25 曾犯）：冪等閘、push 重試最初只寫進雲端 runbook，等於本機跑同一條 pipeline 卻少了兩道保護。

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

把原料存一份到 `src/gathered_archive/<date>.json`（保留 14 天）。`gathered_items.json` 沒有按日分檔、每次抓料直接覆寫，沒有這份副本的話，**日報沒產出的那天、已經抓到手的原料會在隔天被蓋掉，之後補跑只能回頭重抓，而來源視窗早已滾過去——那天就永久漏了**。GitHub Actions 的 `daily-gather` 呼叫的是同一支腳本，兩邊行為一致。

---

### 補跑（backfill）注意事項 `[加入: 2026-07-25]`

雲端漏跑後在本機 `/news-pipeline <date>` 補，有四個已知摩擦點：

**1. 別把 `src/gathered_items.json` commit 上去。** 補跑會**覆寫**這個檔（它沒有按日期分檔），寫進去的是補跑那天的資料。這個檔同時是雲端 routine 的輸入——雲端啟動時讀到的若不是當日資料，新鮮度防線會中止當天執行。也就是**一次本機補跑可能連帶讓當天的雲端排程空跑**。
- 只有 GitHub Actions 的 `daily-gather` 該 commit 這個檔
- 補跑收尾時執行 `git -C REPO_ROOT checkout -- src/gathered_items.json` 還原，避免不小心被 `git add` 帶上車
- 絕不要在補跑流程裡用 `git add -A` / `git add .`

**2. 先找當日原料副本，找不到才重抓。** `src/gathered_archive/<date>.json` 是抓料當下存的原料副本（保留 14 天，由 GitHub Actions 與本機 Step 1a 各自寫入）：

- **副本存在** → **跳過 Step 1a**，直接 `cp src/gathered_archive/<date>.json src/gathered_items.json`，然後從 Step 1b 開始。這是 replay 當天的真實原料，補出來的日報與原本該產出的一致
- **副本不存在**（超過 14 天，或那天連抓料都失敗）→ 才走 Step 1a 重抓。此時要有心理準備：來源多是 RSS／API 的近期視窗，撈不到幾天前的內容。gather 的失敗補撈機制把回看窗口最多拉到 **50 小時**（約兩天），`--date` 補跑則以「目標日 00:00 UTC 到現在」為窗口再裁切回目標日——**離現在越遠，補出來的日報越空，超過兩三天基本上補不回來**。這是來源特性不是 bug；接受那幾天較稀疏，不要為了填滿而放寬收錄門檻

**3. 補跑不套用跨日去重快取**（`main.py` 明文：backfill 不碰 cache，否則會拿今日的快取去誤刪過去的項目）。因此補出來的日報**可能與前後日的日報有重複條目**，屬預期行為，wiki ingest 端由 `wiki-ingest.md` 的「確認最近是否已處理過同一份日報」把關。

**4. 補跑日報已存在時**：`Step 0b：冪等閘` 會因為你明確給了日期參數而放行覆寫，但 wiki 那邊會產生重複條目，需人工核對——見該步驟說明。

---

## Step 1b：生成日報

**0-1. 新鮮度防線（強制，生成前先做）`[加入: 2026-07-25]`**：讀取 `src/gathered_items.json`，確認 `date` 等於 TARGET_DATE 且 `items` 非空。

- 兩者皆滿足 → 繼續
- 任一不滿足 → **中止，不生成假日報**。Step 6 log 寫 `ABORTED: gathered_items.json date=<實際值> items=<數量>，非目標日期的新鮮資料`，結束

本機剛跑完 Step 1a 時這道檢查通常必然通過（資料才剛產生）；它真正保護的是**跳過 Step 1a 的情境**（雲端由 GitHub Actions 供料，可能延遲、失敗或還沒跑），以及本機重跑時誤讀到舊資料。兩種環境都執行，不因「本機應該不會發生」而略過。

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

**輸出結構（六個區塊，無內容則省略）：**

```
# Claude Code & Anthropic 每日新聞摘要

**日期：** TARGET_DATE | **來源：** X/10 | **文章數：** N | **更新時間：** YYYY-MM-DD HH:MM UTC

---

### 📌 今日聚焦
3–5 點導讀，格式：**[標籤]** 說明（標籤：重大事件/持續追蹤/新工具/社群趨勢/風險警示）
標籤只描述類別，不授權升高語氣——即使掛 [風險警示]，說明文字的嚴重度仍以來源原文為準。

選材門檻（下列兩條是**給你判斷用的**，判斷完把門檻文字寫到檔尾，見「檔尾附錄」；**這段括號說明本身是指示，不可出現在日報裡**）：
- **[新工具]**：單一 Show HN 工具未達互動門檻對照表（`.claude/rules/wiki-reporter-shared.md`）**中**門檻、且無跨來源佐證（source_count = 1）時，不單獨列入今日聚焦（校準顯示此類條目 30 天存活率 0/9）；多款工具同批亮相時歸入「⭐ 重點話題」，不逐一在聚焦具名。
- **[風險警示]**：具名資安研究機構/研究者揭露、附具體攻擊鏈或 CVE 細節的條目優先；無具名背書的單一社群抱怨即使當日互動較高，也不優先於前者。

**每一條聚焦項目，凡有對應的參考新聞，用 `[N]` 編號引用**（N 為「今日聚焦」區塊內遞增的全域序號，依首次出現順序編號；同一 URL 重複出現時共用同一個編號，不重新編號）。**正文只寫編號，不寫 URL**——URL 依編號順序彙整到檔尾的「今日聚焦參考連結」清單（見下方「檔尾附錄」）。
- 若該聚焦項目對應單一新聞 → 加一個 `[N]`
- 若該聚焦項目彙整多則新聞 → 每條新聞各給一個編號，全部列在說明文字末尾（如 `[1][2]`）
- 若確實找不到對應新聞（例如是推論或背景說明）→ 可省略編號

範例：
- **[重大事件]** Claude 發布 Sonnet 4，context window 翻倍。[1]
- **[新工具]** Superset、OpenRig、VIR 三款工具同步亮相。[2][3]

### ⭐ 重點話題
跨多來源出現或引起大量討論的項目

### 🔧 技術更新
僅 category=official 的條目（GitHub release、Anthropic Blog）。**若今日無任何 official 條目，完全省略此區塊，不可用 community 條目填充。**

### 📰 媒體報導
僅收錄 category=media 的條目（Reuters/WSJ/科技媒體等），不加情緒標籤。

### 💬 技術熱度討論
僅 category=community 的條目，每條末加 情緒：😊/😤/😐/🤔

### 💰 付費方案動態
定價、配額、Token 費用相關

### 📡 來源狀態
從 `gathered_items.json` 的 `source_status` 欄位生成表格，格式嚴格如下（web reader 解析器依賴此格式）：

| 來源 | 狀態 | 條數 |
|------|------|------|
| Anthropic Blog | ✅ | 0 |
| Hacker News | ✅ | 13 |

（每個來源一列，依 `source_status` 全部列出；`ok=true` → ✅，`false` → ❌）

---

**選材門檻 `[加入: 2026-07-16，依首次聚焦校準修正]`：**
- **[新工具]**：單一 Show HN 工具未達互動門檻對照表（`.claude/rules/wiki-reporter-shared.md`）**中**門檻、且無跨來源佐證（source_count = 1）時，不單獨列入今日聚焦（校準顯示此類條目 30 天存活率 0/9）；多款工具同批亮相時歸入「⭐ 重點話題」，不逐一在聚焦具名。
- **[風險警示]**：具名資安研究機構/研究者揭露、附具體攻擊鏈或 CVE 細節的條目優先；無具名背書的單一社群抱怨即使當日互動較高，也不優先於前者。

**今日聚焦參考連結：**
1. https://example.com/first-cited-url
2. https://example.com/second-cited-url
```

**檔尾附錄（⚠️ 呈現優化 2026-07-24，緊接在 📡 來源狀態表格之後、檔案最末）：**
- 先接一個 `---` 分隔線
- 再接「選材門檻」說明區塊：把上方兩條門檻（`[新工具]`、`[風險警示]`）搬到這裡，**不要**同時留一份在今日聚焦區塊裡。標題固定寫 `**選材門檻：**`（`[加入: …]` 標記與括號內的操作指示都是給你看的，**一律不要寫進日報**——2026-07-25 首次套用新格式時，這段指示文字被原樣印給讀者看了）
- 最後接「**今日聚焦參考連結：**」清單：依「📌 今日聚焦」區塊裡出現的 `[N]` 編號順序，逐行列出對應 URL（`N. URL`）；只列今日聚焦實際引用到的 URL，其餘來源新聞的 URL 已經在各自區塊的標題連結中，不重複列於此處
- 若今日聚焦完全沒有任何 `[N]` 引用（例如全是推論、無對應新聞），則「今日聚焦參考連結」整段省略；若當日日報連「📌 今日聚焦」段落都沒有寫（極端情況），則整個檔尾附錄也省略

**每條排版格式（⚠️ 嚴格遵守，web reader 解析器依賴此格式）：**
```
**[原文標題](url)**
一到兩句繁體中文說明核心重點與為何值得關注。
`來源名稱` · MM/DD HH:MM UTC
```
- 標題行必須是 `**[標題](url)**`（方括號連結），**不可**寫成 `- **標題**：內文` 的 bullet 形式
- 來源行必須是 `` `來源` · 時間 `` 獨立一行
- 違反此格式時 web reader 會解析出空區塊，讀者只看得到今日聚焦
- `gathered_items.json` 每條含 `score_unit` 欄位（分＝HN points、留言＝評論數），選材比較熱度時注意單位不同不可直接互比
- 跨來源比較熱度時的粗略等價量級：HN 30 分 ≈ Reddit 50 讚 ≈ 10 則留言 ≈ dev.to 20 讚；source_count ≥ 2（跨來源報導）視為高於任何單來源分數的訊號
- `source_count > 1` 表示多個獨立來源報導同一事件，選材時視為重要度加權訊號

3. 生成完成後，寫入 `news/TARGET_DATE.md`（完整 Markdown）

3a. **格式自檢（強制）**：寫入後執行下列指令，若輸出為 0 表示條目格式錯誤，必須依「每條排版格式」重寫再檢：
```
grep -cE '^\*\*\[.+\]\(https?://' news/TARGET_DATE.md
```
（今日聚焦以外的每個區塊各條目都應貢獻一個匹配；正常日報此數值 ≥ 5）

3b. **來源狀態表存在性檢查（強制）**：
```
grep -c "^| .* | [✅❌] | [0-9]" news/TARGET_DATE.md
```
（應 ≥ 8，代表來源狀態表已寫入；若不足，補寫 📡 來源狀態區塊再檢）

3d. **收錄完整性自檢（強制）`[加入: 2026-07-26]`**：

```
PYTHON REPO_ROOT\scripts\check_digest_coverage.py --date TARGET_DATE
```

- exit 0 → 通過
- exit 2 → **把腳本列出的遺漏條目補進對應區塊後重檢**，不可跳過

**日報要收錄 `gathered_items.json` 的全部條目**，只有重複或明顯無關的可以略過。日報的定位是「留原始資料給人看」，過濾與精煉是 wiki 記者的職責（見根目錄 `CLAUDE.md`）。

⚠️ **「選材門檻」只用於挑選「📌 今日聚焦」那 3–5 條導讀，不是整份日報的收錄門檻。** 一則新聞沒被選進今日聚焦，仍然要出現在它所屬的分類區塊裡。2026-07-26 加入此檢查，是因為 07-25 抓料 73 則卻只收 38 則（含 61 留言、47 留言的 GitHub Issue 被丟掉），推測正是把聚焦用的門檻誤套到整份日報。

3c. **摘要忠實度自檢（強制）`[加入: 2026-07-17]`**：抽樣核對說明句是否忠於原文——日報是 wiki 的唯一原始資料，摘要失真會被記者沉澱成長期污染：
- 抽樣：今日聚焦**全抽**＋其餘區塊各抽 1 條（合計約 8–10 條）
- 逐條對照 `gathered_items.json` 中同 URL 條目的 `title` / `summary`：說明句中的**事實成分**（數字、版本號、主詞、因果、結論）必須能從原文支撐；原文沒有的具體數字或結論不可出現
- 不符 → 以原文為準改寫該條說明句，改寫後重檢
- 結果記入本 Step 回報（「忠實度自檢：抽 N 條，改寫 M 條」）；**M ≥ 3 視為摘要品質異常**，除改寫外須在回報中標 ⚠️ 供使用者判斷是否深查
- 判斷原則：這是「忠實」檢查不是「精彩」檢查——語氣、取捨、詳略不管，只管事實有沒有依據

4. 用 Bash git 暫存並 commit（**先不 push**，本次所有變更於 Step 5 統一推送，避免多次 push 觸發 Pages 部署並發競爭）：
```
git -C REPO_ROOT add news/TARGET_DATE.md
git -C REPO_ROOT commit -m "news: daily digest TARGET_DATE"
```
- 若 commit 失敗，停止並回報錯誤，不繼續後續步驟

---

## Step 1c：確認 emitted-cache（強制，commit 成功後才執行）

```
cd REPO_ROOT\src
PYTHON -m news_aggregator.main --confirm-digest [--date TARGET_DATE]
```

- 把 Step 1a 篩出的項目標記 `digest_confirmed: true`；未確認的項目視同未出現過，下次重跑會重新提供、不會被永久靜默丟棄（2026-07-13 曾因日報未產出導致 25 則新聞永久漏失，詳見當日 log）
- 失敗只記警告，不影響已完成的 news commit，繼續後續步驟
- **確認結果必須進 git（強制）`[加入: 2026-07-25]`**：`--confirm-digest` 改的是 `src/news_aggregator/emitted_items.json`，這個檔不 commit 就等於沒改過——GitHub Actions 與雲端 routine 都是全新 checkout，讀的是 repo 版本。執行完 append 下列指令，讓它跟著 Step 5 的統一 push 一起上去：
  ```
  git -C REPO_ROOT add src/news_aggregator/emitted_items.json
  git -C REPO_ROOT commit -m "data: confirm emitted-cache TARGET_DATE"
  ```
  （無變更則跳過。**不要單獨 push**，一律留給 Step 5。這樣「日報上站」與「快取確認」同批推送，要嘛一起成功、要嘛一起回到未確認狀態，不會出現「確認了但日報沒上站」的不一致）
- 漏做的實際後果：2026-07-14～07-24 雲端自動化期間，每日確認率幾乎為 0（僅本機手動執行的 07-19、07-22 為 100%），兩階段確認機制形同空轉，跨日去重完全靠 `seen_urls.json` 獨撐

---

## Step 2：Wiki Ingest（不在本檔案）

Step 2 由呼叫 `/news-pipeline` 的 session 親自執行，完整步驟見 `.claude/commands/wiki-ingest.md`（不在此重複，避免兩份副本失步）。執行方式與失敗處理原則見 `.claude/commands/news-pipeline.md` Phase B：Step 2 失敗時記錄但仍進入 Phase C（web build 不依賴 wiki）。

---

# Phase C 步驟（Step 3 / 4 / 5 / 6）

## Step 3：Commit Wiki 變更（不 push）

用 Bash 執行（**先不 push**，於 Step 5 統一推送）：

```
git -C REPO_ROOT add wiki/
git -C REPO_ROOT commit -m "wiki: auto-ingest TARGET_DATE"
```

- 若 wiki 無任何變更，跳過 commit，繼續 Step 4

---

## Step 4：建置 Web Reader

**建置前先跑確定性測試套件（強制）：**

```
PYTHON REPO_ROOT\scripts\run_tests.py
```

- 測試失敗（exit code 非 0）→ 視同 Step 4 失敗：跳過 web build 與 web commit，但仍繼續 Step 5（推送已完成的 news / wiki commit）與 Step 6（記錄 log）；Step 6 log 寫 `Tests FAILED - web build skipped`
- 測試全過（exit code 0）→ 繼續執行：

```
PYTHON REPO_ROOT\scripts\build_web.py
```

- 成功後繼續；若失敗，回報錯誤並跳過推送

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
- **backfill 模式收尾（強制）**：push 完成後執行 `git -C REPO_ROOT checkout -- src/gathered_items.json`，把該檔還原成 repo 版本。理由見「補跑注意事項」第 1 點——補跑會覆寫這個雲端 routine 賴以判斷新鮮度的輸入檔

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
- **唯一允許自動解的衝突：`src/news_aggregator/emitted_items.json`**——此檔有兩個寫者（GitHub Actions 加入未確認條目、pipeline 翻確認欄位）。解法固定：**放棄我方的 confirm commit、保留遠端版本**，因為日報上站遠比確認欄位重要，未確認的條目只會被重新提供一次，是良性退化。處理後標「emitted-cache 確認本次放棄，項目將於次日重新提供」
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
- Step 4 測試套件失敗時，寫 `Tests FAILED - web build skipped`
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

---

## 注意事項

- 所有 Bash 指令使用絕對路徑，不依賴 PATH 環境變數
- Step 0 僅在 TARGET_DATE 為今日時執行；backfill 模式（TARGET_DATE 非今日）跳過
- Step 1 失敗時停止整個 pipeline（Phase A agent 立即停止，不進入 Phase B / Phase C，Step 6 log 改由呼叫 session 直接寫入）
- Step 2（wiki ingest，由呼叫 session 親自執行，不在背景 agent 內）失敗時記錄並仍進入 Phase C（Step 4 不依賴 wiki）
- Step 4 測試套件（`scripts/run_tests.py`）失敗時跳過 web build 與 web commit，仍須執行 Step 5 的統一 push
- Step 4（web build）失敗時跳過 web commit，但仍須執行 Step 5 的統一 push（推送已完成的 news / wiki commit）
- **所有 git push 集中在 Step 5 一次完成**；中途步驟（1b、3）一律只 commit 不 push，避免 Pages 部署並發競爭
- **Step 6 log 寫入必須執行**，即使前面步驟失敗也不能跳過
- **Phase A、Phase C 兩個背景 agent 皆不可 spawn 子 agent**；唯一會呼叫 Agent tool 派工的 Step 2，已移出本檔案、改由呼叫 session 親自執行
- 繁體中文輸出
