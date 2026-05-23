---
description: 完整每日 pipeline：抓新聞 → wiki ingest → 推送 wiki → 建置 web reader → 推送。
argument-hint: [YYYY-MM-DD]
---

# News Pipeline

執行完整每日自動化流程。若提供日期參數（`$ARGUMENTS`），以補跑模式執行該日期；否則以今天為目標。

## 設定

```
REPO_ROOT    = C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
PYTHON       = C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe
DIGEST_MODEL = claude-haiku-4-5-20251001   ← Step 1b 日報生成（結構化任務，Haiku 足夠）
INGEST_MODEL = claude-sonnet-4-6           ← Step 2 Wiki Ingest（複雜判斷，需要 Sonnet）
```

若有提供 `$ARGUMENTS`，目標日期為 `$ARGUMENTS`；否則取系統今天日期（YYYY-MM-DD）。

---

## Step 1a：新聞抓取（Python，不呼叫 LLM）

用 Bash 執行：

```
cd REPO_ROOT\src
PYTHON -m news_aggregator.main --gather-only [--date TARGET_DATE]
```

- 若有 `$ARGUMENTS`，加上 `--date $ARGUMENTS`
- 成功後寫出 `src/gathered_items.json`（含 items、date、source_status）
- 若失敗（exit code 非 0），停止並回報錯誤，不繼續後續步驟

---

## Step 1b：生成日報（Claude 直接在 session 執行）

**執行前先切換模型：** `/model claude-haiku-4-5-20251001`

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

### ⭐ 重點話題
跨多來源出現或引起大量討論的項目

### 🔧 技術更新
僅 category=official 的條目

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
4. 用 Bash git push：
```
git -C REPO_ROOT add news/TARGET_DATE.md
git -C REPO_ROOT commit -m "news: daily digest TARGET_DATE"
git -C REPO_ROOT push
```
- 若失敗，停止並回報錯誤，不繼續後續步驟

---

## Step 2：Wiki Ingest

**執行前先切換模型：** `/model claude-sonnet-4-6`

執行完整 wiki ingest 流程（直接在本 session 執行，不呼叫 `claude -p`）：

1. 讀取 `news/TARGET_DATE.md`
2. 讀取 `wiki/index.md` + `wiki/log.md`，確認未重複 ingest
3. 比對日報內容，找受影響的既有頁面
4. 更新相關 entities/ 和 topics/ 頁面
5. 判斷是否需建立新頁面（entities/ 或 topics/）
6. 更新 `wiki/feature-radar.md`
7. Append 至 `wiki/log.md`
8. 更新 `wiki/index.md`
9. 執行呈現品質審查（見 CLAUDE.md）
10. 輸出 Step 9 核對清單

- Step 2 失敗時記錄但繼續 Step 4（web build 不依賴 wiki）

---

## Step 3：推送 Wiki 變更

用 Bash 執行：

```
git -C REPO_ROOT add wiki/
git -C REPO_ROOT commit -m "wiki: auto-ingest TARGET_DATE"
git -C REPO_ROOT push
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

## Step 5：推送 Web 變更

用 Bash 執行：

```
git -C REPO_ROOT add web_reader/
git -C REPO_ROOT commit -m "web: rebuild TARGET_DATE"
git -C REPO_ROOT push
```

---

## Step 6：寫入 task_scheduler.log

整個 pipeline 結束後，**無論成功或失敗**，都必須 append 執行記錄至：

```
REPO_ROOT\src\logs\task_scheduler.log
```

格式（依各步驟結果填入 OK / FAILED / SKIPPED）：

```
[DATE TIME] === Manual pipeline start (via /news-pipeline in Claude session) ===
[DATE TIME] Aggregator OK
[DATE TIME] Wiki ingest OK
[DATE TIME] Wiki push done
[DATE TIME] Building web reader...
[DATE TIME] Web push done
[DATE TIME] === Pipeline complete (manual) ===
```

- Step 1 失敗時，寫 `Aggregator FAILED - stopping`，之後不繼續
- Step 2 失敗時，寫 `Wiki ingest FAILED`
- Step 4 失敗時，寫 `build_web FAILED - skipping web push`
- 時間戳使用系統當前時間（`Get-Date` 或 `date` 指令取得），格式 `[週X YYYY/MM/DD HH:MM:SS.SS]`

---

## 完成摘要

完成後輸出：

| 步驟 | 結果 |
|------|------|
| Step 1 新聞聚合 | ✅ / ❌ |
| Step 2 Wiki Ingest | ✅ / ❌ |
| Step 3 Wiki 推送 | ✅ / ⏭️ 無變更 / ❌ |
| Step 4 Web 建置 | ✅ / ❌ |
| Step 5 Web 推送 | ✅ / ❌ |
| Step 6 Log 寫入 | ✅ / ❌ |
| 目標日期 | TARGET_DATE |

## 模型還原

Step 2 完成後，用 `/model claude-sonnet-4-6` 確認模型維持在 Sonnet（後續步驟無 LLM 需求，但保持一致）。

---

## 注意事項

- 所有 Bash 指令使用絕對路徑，不依賴 PATH 環境變數
- Step 1 失敗時停止整個 pipeline
- Step 2（wiki ingest）失敗時記錄並繼續 Step 4
- Step 4 失敗時跳過 Step 5
- **Step 6 log 寫入必須執行**，即使前面步驟失敗也不能跳過
- 繁體中文輸出
