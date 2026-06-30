---
description: News Pipeline Agent 執行規範：Step 1a 至 Step 6 完整步驟。由 news-pipeline.md spawn 的 background Agent 讀取此檔案後執行。
---

# News Pipeline Steps（Agent 執行規範）

此檔案由 `.claude/commands/news-pipeline.md` spawn 的 background Agent 讀取並執行。
**Agent 直接在本 session 執行所有步驟，不再 spawn 子 agent。**

## 設定

```
REPO_ROOT = C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
PYTHON    = C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe
模型      = Sonnet（由 spawn 時指定，全程使用，無需切換）
```

TARGET_DATE 由 Agent prompt 傳入。

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
> 你是一位專注於 AI 技術的中文科技記者，擅長用繁體中文撰寫清晰、客觀的技術新聞摘要。

**輸出結構（五個區塊，無內容則省略）：**

```
# Claude Code & Anthropic 每日新聞摘要

**日期：** TARGET_DATE | **來源：** X/6 | **文章數：** N | **更新時間：** YYYY-MM-DD HH:MM UTC

---

### 📌 今日聚焦
3–5 點導讀，格式：**[標籤]** 說明（標籤：重大事件/持續追蹤/新工具/社群趨勢/風險警示）

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

### 💬 技術熱度討論
僅 category=community 的條目，每條末加 情緒：😊/😤/😐/🤔

### 💰 付費方案動態
定價、配額、Token 費用相關
```

**每條排版格式：**
```
**[原文標題](url)**
一到兩句繁體中文說明核心重點與為何值得關注。
`來源名稱` · MM/DD HH:MM UTC
```

3. 生成完成後，寫入 `news/TARGET_DATE.md`（完整 Markdown）
4. 用 Bash git 暫存並 commit（**先不 push**，本次所有變更於 Step 5 統一推送，避免多次 push 觸發 Pages 部署並發競爭）：
```
git -C REPO_ROOT add news/TARGET_DATE.md
git -C REPO_ROOT commit -m "news: daily digest TARGET_DATE"
```
- 若 commit 失敗，停止並回報錯誤，不繼續後續步驟

---

## Step 2：Wiki Ingest

執行完整 wiki ingest 流程（本步驟為 `.claude/commands/wiki-ingest.md` 的精簡複本，修改任一方時必須同步另一方）：

1. 讀取 `news/TARGET_DATE.md`；同時讀取 `wiki/CLAUDE.md`、`.claude/rules/wiki-ingest.md`（主編指南）、`wiki/index.md`、`wiki/log.md`
2. **分類（主編）**：依 `.claude/rules/wiki-ingest.md` 分類表為每則條目標記類別（模型 / 功能 / 商業 / 安全政策 / 社群 / 人物）
3. **派工（Agent tool）**：對每個有條目的類別呼叫 Agent tool（有多類別時同一訊息並行發出）；**記者 agent 必須 foreground 啟動（不可設 `run_in_background: true`）**，否則完成通知無法回到本 agent；各記者讀取 `.claude/rules/wiki-ingest-[category].md`，更新負責頁面；需建新頁面時讀 `.claude/rules/wiki-ingest-format.md`；完成後回傳標準回報格式（詳見 `.claude/commands/wiki-ingest.md` Step 3）
4. **彙整共用檔案（主編）**：依所有記者回報，更新 `wiki/feature-radar.md`（含依 `.claude/rules/wiki-ingest-features.md`「本週推薦自動更新規則」覆寫 `## ⭐ 本週推薦`）、`wiki/index.md`（狀態變更 + 新頁面）、`wiki/log.md`（append）；若有重大事件，更新 `wiki/overview.md`

- Step 2 失敗時記錄但繼續 Step 4（web build 不依賴 wiki）

---

## Step 3：Commit Wiki 變更（不 push）

用 Bash 執行（**先不 push**，於 Step 5 統一推送）：

```
git -C REPO_ROOT add wiki/
git -C REPO_ROOT commit -m "wiki: auto-ingest TARGET_DATE"
```

- 若 wiki 無任何變更，跳過 commit，繼續 Step 4

---

## Step 4：建置 Web Reader

用 Bash 執行：

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

格式（依各步驟結果填入 OK / FAILED / SKIPPED）：

```
[DATE TIME] === Agent pipeline start (TARGET_DATE) ===
[DATE TIME] Aggregator OK
[DATE TIME] Wiki ingest OK
[DATE TIME] Building web reader...
[DATE TIME] Single push done (news + wiki + web)
[DATE TIME] === Pipeline complete (agent) ===
```

- Step 1 失敗時，寫 `Aggregator FAILED - stopping`，之後不繼續
- Step 2 失敗時，寫 `Wiki ingest FAILED`
- Step 4 失敗時，寫 `build_web FAILED - pushing news/wiki only`
- Step 5 push 失敗時，寫 `Push FAILED`
- 時間戳使用系統當前時間（`Get-Date` 或 `date` 指令取得），格式 `[週X YYYY/MM/DD HH:MM:SS.SS]`

---

## 完成摘要

完成後輸出：

| 步驟 | 結果 |
|------|------|
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
- Step 1 失敗時停止整個 pipeline
- Step 2（wiki ingest）失敗時記錄並繼續 Step 4
- Step 4（web build）失敗時跳過 web commit，但仍須執行 Step 5 的統一 push（推送已完成的 news / wiki commit）
- **所有 git push 集中在 Step 5 一次完成**；中途步驟（1b、3）一律只 commit 不 push，避免 Pages 部署並發競爭
- **Step 6 log 寫入必須執行**，即使前面步驟失敗也不能跳過
- 繁體中文輸出
