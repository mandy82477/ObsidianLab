# Design Diagram — 現況架構（維運用）

**最後更新：** 2026-07-11
**文件定位：** 這份是「**系統現在怎麼運作**」的操作/維運架構圖，給要執行或維護 pipeline 的人看。
「**系統怎麼演變成現在這樣**」的演進敘事，另見 `docs/architecture-evolution.html`（互動時間軸），兩者分工不重疊。

> ⚠️ **環境鐵則（讀圖前必知）：**
> - 本專案**沒有 `ANTHROPIC_API_KEY`**，全流程不呼叫任何外部 LLM API。
> - **`claude -p` 全面禁用**。所有 LLM 工作只在 Claude Code session 內完成（日報生成、wiki ingest 派工）。
> - 觸發方式是 `/news-pipeline` skill（在 Claude Code 內執行），**不是** `.bat` + Windows 排程呼叫 `claude -p`。

---

## 全流程總覽（`/news-pipeline`，三段式）

三段拆分的原因：Step 2 要用 Agent tool 派記者，而「背景 agent 再派 agent」會導致完成通知迷路（巢狀背景的系統性限制），所以 Step 2 必須由呼叫 skill 的 session 親自跑。

```mermaid
flowchart TD
    TRIG["/news-pipeline [YYYY-MM-DD]\n在 Claude Code session 觸發"] --> PA

    subgraph PA["Phase A —— 背景 agent（model: sonnet）"]
        S0["Step 0：昨日缺跑檢查\n（今日模式才跑，backfill 跳過）"]
        S1A["Step 1a：Python 聚合器\n--gather-only（無 LLM）"]
        S1B["Step 1b：Claude session 生成日報\n六區塊 + 格式自檢 3a/3b"]
        S0 --> S1A --> S1B
    end

    PA -->|Step 1a FAILED| STOP["寫 log：Aggregator FAILED\n跳過 B/C，結束"]
    PA -->|成功，通知本 session| PB

    subgraph PB["Phase B —— 呼叫 session 親自執行（不可委派）"]
        S2["Step 2：Wiki Ingest\n主編分類 → 六記者 foreground 派工 → 主編彙整"]
    end

    PB --> PC

    subgraph PC["Phase C —— 第二個背景 agent（model: sonnet）"]
        S3["Step 3：commit wiki（不 push）"]
        S4["Step 4：跑測試套件 → 建置 web reader\n（測試不過則跳過 build，仍推送 news/wiki）"]
        S5["Step 5：單一 git push\n（一次推送 news+wiki+web，避免 Pages 並發競爭）"]
        S6["Step 6：append task_scheduler.log\n（無論成敗都寫）"]
        S3 --> S4 --> S5 --> S6
    end

    PC --> DONE(["本 session 彙整 A+B+C，輸出完成摘要"])
```

---

## 聚合器內部（Step 1a：`main.py --gather-only`，全程無 LLM）

```mermaid
flowchart TD
    subgraph SRC["10 個來源（ThreadPoolExecutor 並行抓取）"]
        direction LR
        S1["Anthropic Blog\n(/news + /engineering)"]
        S2["Anthropic Status\n(status RSS)"]
        S3["GitHub Releases"]
        S4["GitHub Issues"]
        S5["Hacker News"]
        S6["Reddit\n(含 r/ClaudeCode)"]
        S7["Google News\n(category=media)"]
        S8["dev.to\n(API + reactions)"]
        S9["Claude API\nRelease Notes"]
        S10["Blogroll\n(權威部落客 RSS\n4 位 probation)"]
    end

    SRC --> DEDUP["dedup.py\nURL 正規化 + 模糊標題去重\n官方來源優先"]
    DEDUP --> CACHE{"emitted_cache\n14 天 TTL 跨執行去重\n（backfill 模式跳過）"}
    CACHE -->|新項目 / 達重燃門檻| ENRICH
    CACHE -->|近期已發過| DROP["略過"]

    ENRICH["enricher.py\ntrafilatura 抓原文補 summary\n（paywall 網域跳過）"] --> FILTER

    subgraph FILTER["filter.py —— 規則式過濾（無 LLM）"]
        F1["GNews 標題關鍵字比對"]
        F2["PR wire 網域黑名單\n(prnewswire / businesswire ...)"]
    end

    FILTER --> OUT["gathered_items.json\n（items + date + source_status\n+ score_unit + source_count）"]
    FILTER --> FUNNEL["data/source_funnel.jsonl\n（append：每次執行各來源\ngathered/filtered/emitted 漏斗數）"]
```

**關鍵欄位：**
- `score_unit`：分（HN）/ 讚（Reddit、dev.to）/ 留言 —— 跨來源比熱度時單位不同，不可直接比大小
- `source_count`：同一事件被幾個獨立來源報導，> 1 視為重要度加權
- `source_status`：每個來源本次抓到幾筆（餵給日報「📡 來源狀態」表 + wiki-lint 6f 來源健康檢查）
- `source_funnel.jsonl`：跨日累積的來源漏斗統計（gathered→filtered→emitted），供未來 `/source-review` 判斷各來源效益與部落客汰換（GH Actions 每日 commit）

---

## Wiki Ingest（Step 2：主編 + 六記者，星型派工）

```mermaid
flowchart TD
    NEWS["讀 news/YYYY-MM-DD.md"] --> CLASSIFY

    CLASSIFY["主編分類\n每則標記類別（可多類）"] --> DISPATCH

    DISPATCH["foreground 派工（model: sonnet）\n六類記者同一訊息並行\n⚠️ 不可 run_in_background\n⚠️ 記者不可再委派子 agent"]

    DISPATCH --> R1 & R2 & R3 & R4 & R5 & R6

    R1["模型記者"]
    R2["功能記者"]
    R3["商業記者"]
    R4["安全政策記者"]
    R5["社群記者"]
    R6["人物記者"]

    R1 & R2 & R3 & R4 & R5 & R6 -->|標準回報格式| CONSOLIDATE

    CONSOLIDATE["主編彙整（序列化寫入共用檔）\n收報核對：逐項驗 3a–3g 有明確結果，缺項退回"]
    CONSOLIDATE --> SHARED["feature-radar.md（本週推薦/升版風險/倒數中）\nindex.md（狀態變更 + 新頁）\nlog.md（append，含品質備註）\noverview.md（重大事件才更新）"]
    CONSOLIDATE --> LEDGER["data/source_attribution.jsonl\n（append：記者回報的『來源歸因』欄\n轉 日期×來源×類別×頁面）"]
```

**頁面歸屬＝動態認領：** 記者的負責頁面由 `index.md` 的「領域」欄位決定，不寫死清單；新頁面自動被對應記者涵蓋。

**來源歸因走 ledger、不進 wiki 正文：** 記者在回報訊息填「來源歸因」欄（非 wiki 正文），主編彙整時 append 至 `data/source_attribution.jsonl`。此設計取代了舊的 `[[sources/xxx]]` wikilink 機制（2026-07-11 撤除——wikilink 會污染 web reader 且 Graph 二元邊答不了來源比重問題）。

---

## Wiki Lint（`/wiki-lint`，每週手動，9 步）

```mermaid
flowchart TD
    L1["1. 載入 wiki 全貌"] --> L2
    L2["2. 六記者並行（model: sonnet）\n3a 矛盾 / 3b 孤立 / 3c 過期(用最後新聞更新判)\n3d resolved 收尾 / 3e 呈現品質 / 3f 入口層健檢\n3g 待查證回訪"] --> L3
    L3["3. 語意分岔／死案候選（需使用者確認）"] --> L4
    L4["4. 建議新實體頁"] --> L5
    L5["5. 更新 overview.md"] --> L6
    L6["6. 規則健檢 6a–6h\n(矛盾/引用/遵守率/年齡/長度/來源健康\n/跨檔語意矛盾/品質指標+成長迴路蒸餾)"] --> L7
    L7["7. 讀者模擬驗收（3 讀者 3 跳測試）"] --> L8
    L8["8. append log（含 metrics 趨勢）"] --> L9
    L9["9. 更新 index.md"]
```

---

## 規則一致性治理（三層防線）

`.claude/commands/`、`.claude/rules/`、`CLAUDE.md` 之間有大量交叉引用與同步配對，靠人肉維持一致會漂移。機械檢查已腳本化（`scripts/check_rules.py` 讀 `.claude/review-registry.json`，跑裸露引用/路徑存在/錨點/同步配對四類檢查 + coupling 提示），三層防線確保「改了規則就會被驗」：

```mermaid
flowchart TD
    EDIT["改動 .claude/commands|rules 或 CLAUDE.md"] --> H1

    H1["第一層：PostToolUse hook（dirty-period 預告）\ncheck_rule_modified.py\n一批改動只提醒一次，綠檢後重置"]
    H1 --> H2["第二層：Stop hook（收工檢查）\ncheck_rules_on_stop.py\n偵測規則檔 mtime > 上次綠檢\n→ block 收工，逼先驗"]
    H2 --> H3["第三層：DoD 兜底\nrun_tests.py 內建 check_rules.py\n測試不綠不算完工"]

    H3 --> CHECK{"python scripts/check_rules.py"}
    CHECK -->|零錯誤| MARK["寫 .claude/.last-rules-check\n（三層共用記號檔，重置提醒）"]
    CHECK -->|有 ❌| FIX["/review-commands 薄殼\n判讀失敗 → 修檔案或改 registry\n→ 重跑到零錯誤"]
    FIX --> CHECK
```

**通用化：** 此機制已抽成全域 skill `/build-review-command`（通用引擎 + 專案 registry 分離），可在其他專案快速建立同套三層防線。

---

## 產物與唯讀邊界

```mermaid
flowchart LR
    subgraph WRITE["可寫"]
        A["news/YYYY-MM-DD.md\n（唯讀原始資料，僅 pipeline 生成當下寫入）"]
        B["wiki/entities/*.md, topics/*.md"]
        C["wiki/feature-radar.md, index.md, overview.md, metrics.md"]
        D["wiki/log.md（append only）"]
        E["web_reader/data/（build 產物）"]
    end
    B & C & D --> BUILD["scripts/build_web.py\n（wikilink 斷鏈檢查 + 領域欄位防呆\n+ 剝除 [[sources/*]] 分析標記不外洩 web）"]
    A --> BUILD
    BUILD --> E
```

**唯讀/限制：** `news/` 唯讀；`log.md` 只能 append；wiki 檔案只能在 `CLAUDE_NEWS/wiki/`；記者不可碰 `feature-radar.md`/`index.md`/`log.md`（主編統一序列化）。

---

## 模組對照（想改哪裡看這裡）

| 想做的事 | 動哪個檔 |
|---------|---------|
| 新增新聞來源 | `src/news_aggregator/sources/` 繼承 `BaseSource`，在 `main.py` sources 列表註冊 |
| 增減權威部落客 | `src/news_aggregator/sources/blogroll.json`（status: probation/active/retired，汰換由 `/source-review` 建議） |
| 改過濾規則 | `src/news_aggregator/filter.py`（純規則，無 LLM） |
| 改日報格式 | `.claude/commands/news-pipeline-steps.md` Step 1b |
| 改記者職責/規則 | `.claude/rules/wiki-ingest-[category].md` |
| 改 web 呈現 | `web_reader/`（設計規範見 `.claude/rules/web-reader-design.md`）+ `scripts/build_web.py` |
| 改任何規則/指令後驗證 | `/review-commands`（判讀 `scripts/check_rules.py` 失敗並修復；機械檢查已掛進 `run_tests.py`） |
| 改規則一致性檢查項 | `.claude/review-registry.json`（同步配對/錨點/allowlist，登記於此即生效） |

執行日誌：`src/logs/` | 測試：`scripts/run_tests.py`
