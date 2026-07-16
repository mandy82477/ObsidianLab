# data/ — 結構化資料檔（JSONL）

本目錄存放 pipeline 產出的結構化統計資料，**append only**，供後續分析「哪個來源對哪個類別最有幫助」。資料檔（`*.jsonl`）由自動化流程維護：`source_attribution.jsonl` 由 wiki ingest 主編 append；`source_funnel.jsonl` 由每日 GitHub Actions gather / render 時 append 並 commit。

另含兩個非 JSONL 檔（皆為 `scripts/source_scorecard.py` 的輸入，設計說明見 `docs/source-scoring-optimization.md`）：

- **`source_registry.json`**：來源註冊表（單一真相源）——pipeline 註冊名 ↔ attribution slug ↔ 來源層品質標籤（`score_reliability` / `curation_mode`）。手動維護，新增或調整來源時同步更新。
- **`external/domain_pc1.csv`**：Lin et al. (2023, PNAS Nexus) 的 domain 信譽聚合分數（11,520 domains，pc1 0–1），來自 [hauselin/domain-quality-ratings](https://github.com/hauselin/domain-quality-ratings)。靜態外部資料，每季複查時效（見 `docs/workaround-register.md`）。

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
