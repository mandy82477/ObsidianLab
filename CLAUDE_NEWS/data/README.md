# data/ — 結構化資料檔（JSONL）

本目錄存放 pipeline 產出的結構化統計資料，**append only**，供後續分析「哪個來源對哪個類別最有幫助」。資料檔（`*.jsonl`）由自動化流程維護：`source_attribution.jsonl` 由 wiki ingest 主編 append；`source_funnel.jsonl` 由每日 GitHub Actions gather / render 時 append 並 commit。

另含兩個非 JSONL 檔（皆為 `scripts/source_scorecard.py` 的輸入，設計說明見 `docs/source-scoring-optimization.md`）：

- **`source_registry.json`**：來源註冊表（單一真相源）——pipeline 註冊名 ↔ attribution slug ↔ 來源層品質標籤（`score_reliability` / `curation_mode`）。手動維護，新增或調整來源時同步更新。
- **`external/domain_pc1.csv`**：Lin et al. (2023, PNAS Nexus) 的 domain 信譽聚合分數（11,520 domains，pc1 0–1），來自 [hauselin/domain-quality-ratings](https://github.com/hauselin/domain-quality-ratings)。靜態外部資料，每季複查時效（見 `docs/workaround-register.md`）。

## source_attribution.jsonl

wiki ingest 時的來源歸因 ledger。主編收齊記者回報後，把各記者「來源歸因」欄逐筆轉為一行 JSON append（記者回報「無」則不寫）。

Schema（每行一筆）：

```json
{"date": "2026-07-11", "source": "hacker-news", "category": "社群", "page": "topics/community-tech-patterns", "item_url": "https://...", "item_title": "...", "publisher": "Financial Times"}
```

| 欄位 | 說明 |
|------|------|
| `date` | 日報日期（YYYY-MM-DD） |
| `source` | 來源 slug（`hacker-news` / `reddit` / `github-issues` / `github` / `google-news` / `devto` / `anthropic-blog` / `anthropic-status` / `claude-api-release-notes` / `blog` / `official-docs` / `official-skills` / `topic-watch`；`lobsters` 僅存歷史資料，來源已於 2026-07-10 移出），對照表見 `.claude/rules/wiki-reporter-shared.md`，註冊表 `data/source_registry.json` |
| `category` | 六類別之一：模型 / 功能 / 商業 / 安全政策 / 社群 / 人物 |
| `page` | 寫入的 wiki 相對路徑，不含 `.md`（如 `topics/ai-agent-safety`） |
| `item_url` | 日報條目原始連結 |
| `item_title` | 日報條目標題 |
| `publisher` | **選填**，來源標記斜線後半段（出版者／子版／站名）。記者回報的 `source` 只有斜線前半段，而 `google-news` 底下實際有 250+ 個出版者、品質從 Reuters 到內容農場都有，單一 slug 的品質標籤對它沒有意義。由 `scripts/enrich_attribution_publisher.py` 從日報回推補上（不改記者契約）；日報查無對應 URL、或來源本身無斜線（如 `Hacker News`）時不帶此欄。`topic-watch` 的斜線後半段是 topic slug（如 `ai-talent-flow`），回填後可按專頁統計定向抓取的實際貢獻 |

### publisher 回填

`scripts/enrich_attribution_publisher.py` 掃 `news/*.md` 建 URL → 來源標記對照，為缺 `publisher` 的行補值。**冪等**，可隨時重跑；新歸因 append 後執行一次即可補齊。

```bash
python scripts/enrich_attribution_publisher.py --dry-run   # 只報告
python scripts/enrich_attribution_publisher.py             # 實際寫入
```

首次回填（2026-08-05）：466 筆補上、涵蓋 141 家；`google-news` 涵蓋率 93%（229/247，127 家出版者）。未匹配多為語意差異（HN 條目記原文網址、日報連討論串），非解析錯誤。

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

## pending-handoffs.jsonl

記者間「轉知」帳本（append only，最後一筆勝出），`[加入: 2026-08-15]`。跨記者交辦（如社群記者發現新工作模式要功能記者評估產品化矩陣）過去靠主編口頭轉達、無接手驗收；現在照 `pending-signals.jsonl` 的同構做法走閉迴路：主編 `open` 登帳 → 派工時 `list` 附清單 → 記者回報「轉知處置」→ 主編 `close`／`void`。

一律用 `python scripts/pending_handoffs.py {open|list|close|void}` 操作，不手改。行格式：
- 開立：`{"id":"H-xxxxxx","opened":"YYYY-MM-DD","from":"社群","to":"功能","page":"topics/...","note":"...","status":"open"}`
- 結案：`{"id":"H-xxxxxx","closed":"YYYY-MM-DD","status":"done|void","by":"功能","result":"..."}`

id 由（開立日、來源、目標、note）雜湊而來，同一交辦重複開立冪等；`list` 對逾 14 天未結案者標 ⚠️。

