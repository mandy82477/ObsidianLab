---
description: 完整每日 pipeline：抓新聞 → wiki ingest → 推送 wiki → 建置 web reader → 推送。
argument-hint: [YYYY-MM-DD]
---

# News Pipeline

執行完整每日自動化流程，**以 background Agent 執行，節省主 session context**。

若提供日期參數（`$ARGUMENTS`），以補跑模式執行；否則以今天為目標。

---

## 呼叫此 Skill 時：Spawn Background Agent

使用 **Agent tool** 帶以下參數，然後主 session 無需等待，可繼續其他工作：

| 參數 | 值 |
|------|---|
| description | `News pipeline {TARGET_DATE}` |
| run_in_background | `true` |
| model | `sonnet` |

**prompt**（`{TARGET_DATE}` 替換為今日日期或 `$ARGUMENTS`，格式 YYYY-MM-DD）：

```
你是 Claude News Pipeline Agent。

設定：
- REPO_ROOT   = C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
- PYTHON      = C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe
- TARGET_DATE = {TARGET_DATE}

步驟：
1. 讀取 `C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS\.claude\commands\news-pipeline-steps.md`，取得完整執行規範
2. 從 Step 1a 開始依序執行所有步驟直到 Step 6

規範：pipeline 各步驟直接在本 agent session 執行；**唯一例外是 Step 2 wiki ingest 的記者派工**——依 steps 規範以 Agent tool 並行派出各類記者，且**必須 foreground（不可設 run_in_background: true）**，否則記者完成通知會送到主 session 而非本 agent，pipeline 會卡死在等待。使用繁體中文輸出。
```

Agent 完成後自動通知主 session。

---

完整步驟規範：`.claude/commands/news-pipeline-steps.md`
