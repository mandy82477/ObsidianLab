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

## Step 0：昨日缺跑檢查

**僅當 TARGET_DATE 為今日時執行**（backfill 模式，即 TARGET_DATE 非今日時跳過本步驟——補跑歷史日期時「昨天」無意義）。

計算 TARGET_DATE 的前一天 YESTERDAY，檢查 `news/YESTERDAY.md` 是否存在：
- 存在 → 一行帶過，繼續 Step 1a
- 不存在 → 記錄缺失，於完成摘要表加一列「⚠️ 昨日（YESTERDAY）日報缺失」，並提示使用者可執行 `/news-pipeline` 帶日期參數手動補跑；Step 6 log 寫入 `WARN: yesterday digest missing (YESTERDAY)`。**不自動補跑**（避免排程場景下連鎖跑兩天造成時間不可控）

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

---

## Step 1b：生成日報

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

**選材門檻 `[加入: 2026-07-16，依首次聚焦校準修正]`：**
- **[新工具]**：單一 Show HN 工具未達互動門檻對照表（`.claude/rules/wiki-reporter-shared.md`）**中**門檻、且無跨來源佐證（source_count = 1）時，不單獨列入今日聚焦（校準顯示此類條目 30 天存活率 0/9）；多款工具同批亮相時歸入「⭐ 重點話題」，不逐一在聚焦具名。
- **[風險警示]**：具名資安研究機構/研究者揭露、附具體攻擊鏈或 CVE 細節的條目優先；無具名背書的單一社群抱怨即使當日互動較高，也不優先於前者。

**每一條聚焦項目，凡有對應的參考新聞，必須在說明文字末尾加上 `（ref: URL）`，URL 為 gathered_items.json 中該新聞的原始 url 欄位值。每條新聞各加一個 ref，可在同一行加多個。**
- 若該聚焦項目對應單一新聞 → 加一個 `（ref: URL）`
- 若該聚焦項目彙整多則新聞 → 每條新聞各加一個 `（ref: URL）`，全部列在同一行末尾
- 若確實找不到對應新聞（例如是推論或背景說明）→ 可省略 ref

範例：
- **[重大事件]** Claude 發布 Sonnet 4，context window 翻倍。（ref: https://www.anthropic.com/news/claude-sonnet-4）
- **[新工具]** Superset、OpenRig、VIR 三款工具同步亮相。（ref: https://github.com/superset-sh/superset）（ref: https://github.com/openrig/openrig）

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
```

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
- 若 push 失敗，回報錯誤並在 Step 6 log 記錄 `Push FAILED`

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
