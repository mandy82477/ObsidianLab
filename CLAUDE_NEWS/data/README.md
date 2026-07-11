# data/ — 結構化資料檔（JSONL）

本目錄存放 pipeline 產出的結構化統計資料，**append only**，供後續分析「哪個來源對哪個類別最有幫助」。資料檔（`*.jsonl`）由自動化流程維護：`source_attribution.jsonl` 由 wiki ingest 主編 append；`source_funnel.jsonl` 由每日 GitHub Actions gather / render 時 append 並 commit。

## source_attribution.jsonl

wiki ingest 時的來源歸因 ledger。主編收齊記者回報後，把各記者「來源歸因」欄逐筆轉為一行 JSON append（記者回報「無」則不寫）。

Schema（每行一筆）：

```json
{"date": "2026-07-11", "source": "hacker-news", "category": "社群", "page": "topics/community-tech-patterns", "item_url": "https://...", "item_title": "..."}
```

| 欄位 | 說明 |
|------|------|
| `date` | 日報日期（YYYY-MM-DD） |
| `source` | 來源 slug（`hacker-news` / `reddit` / `github-issues` / `github` / `google-news` / `devto` / `lobsters` / `anthropic-blog` / `anthropic-status` / `claude-api-release-notes` / `blog`），對照表見 `.claude/rules/wiki-reporter-shared.md` |
| `category` | 六類別之一：模型 / 功能 / 商業 / 安全政策 / 社群 / 人物 |
| `page` | 寫入的 wiki 相對路徑，不含 `.md`（如 `topics/ai-agent-safety`） |
| `item_url` | 日報條目原始連結 |
| `item_title` | 日報條目標題 |

## source_funnel.jsonl

每日抓取漏斗統計，由 `src/news_aggregator/main.py` 的 `write_funnel_record()` 寫入。

Schema（每行一筆，每次 gather / render 各一筆）：

```json
{"date": "2026-07-11", "run_ts": "2026-07-11T02:00:00+00:00", "mode": "gather", "lookback_hours": 26, "sources": {"Hacker News": {"ok": true, "gathered": 12, "filtered": 5, "emitted": 3}}, "totals": {"gathered": 80, "filtered": 20, "emitted": 12}}
```

| 欄位 | 說明 |
|------|------|
| `date` | 日報日期 |
| `run_ts` | 執行時間（UTC ISO） |
| `mode` | `gather` / `render` / `backfill` |
| `lookback_hours` | 回看時數 |
| `sources` | 以來源註冊名為 key；`ok`（抓取是否成功）、`gathered` / `filtered` / `emitted` 各階段條目數；對不回註冊名的計數歸入 `"_unmapped"` 桶 |
| `totals` | 三階段總數 |
