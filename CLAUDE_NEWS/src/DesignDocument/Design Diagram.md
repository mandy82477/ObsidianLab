# Design Diagram — 現況架構（維運用）

**最後更新：** 2026-07-29
**文件定位：** 這份是「**系統現在怎麼運作**」的操作/維運架構圖，給要執行或維護 pipeline 的人看。
「**系統怎麼演變成現在這樣**」的演進敘事，另見 `docs/architecture-evolution.html`（互動時間軸），兩者分工不重疊。

> ⚠️ **環境鐵則（讀圖前必知）：**
> - 本專案**沒有 `ANTHROPIC_API_KEY`**，全流程不呼叫任何外部 LLM API。
> - **`claude -p` 全面禁用**。所有 LLM 工作只在 Claude Code session 內完成（日報生成、wiki ingest 派工）。
> - 觸發方式是 `/news-pipeline` skill（在 Claude Code 內執行），**不是** `.bat` + Windows 排程呼叫 `claude -p`。

---

## 全流程總覽（`/news-pipeline`，三段式）

三段拆分的原因：Step 2 要用 Agent tool 派記者，而「背景 agent 再派 agent」會導致完成通知迷路（巢狀背景的系統性限制），所以 Step 2 必須由呼叫 skill 的 session 親自跑。

> 每日自動線（GitHub Actions 抓料 + 雲端 routine 產日報/wiki/web 的分裂架構）另見 `docs/daily-automation.md` 與 `docs/cloud-runbooks/`；本圖描述的手動 `/news-pipeline` 為補救路徑，兩者步驟一致。

```mermaid
flowchart TD
    TRIG["/news-pipeline [YYYY-MM-DD]\n在 Claude Code session 觸發"] --> PA

    subgraph PA["Phase A —— 背景 agent（model: sonnet）"]
        S0["Step 0：昨日缺跑檢查\n（今日模式才跑，backfill 跳過）"]
        S1A["Step 1a：Python 聚合器\n--gather-only（無 LLM）"]
        S1B["Step 1b：Claude session 生成日報\n六區塊 + 自檢 3a 格式/3b 來源表\n/3c 摘要忠實度（抽樣對照原文）"]
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

**emitted_cache 的兩道機制**（詳細註解見 `src/news_aggregator/emitted_cache.py`）：
- **兩階段確認（digest_confirmed）**：`--gather-only`（GH Actions）只把條目標為「暫定收錄」，日報實際生成後由 `--confirm-digest`（雲端 Step 1c）翻正；未確認條目視同不在快取、持續重新供片——防止「抓料成功但日報沒生成」時條目被永久黑洞（2026-07-13 教訓；確認結果由雲端寫回 repo 的寫者分工見 `docs/daily-automation.md`）。
- **重燃（reignite）**：已確認條目若分數翻倍且增量 ≥ 10，重新收錄——讓後來才起飛的條目（如 GitHub Search「上升中」repo 帶回的最新星數）能再次浮上日報。

**關鍵欄位：**
- `score_unit`：分（HN）/ 讚（Reddit、dev.to）/ 星（GitHub Search）/ 留言 —— 跨來源比熱度時單位不同，不可直接比大小
- `source_count`：同一事件被幾個獨立來源報導，> 1 視為重要度加權
- `source_status`：每個來源本次抓到幾筆（餵給日報「📡 來源狀態」表 + wiki-lint 6f 來源健康檢查）
- `source_funnel.jsonl`：跨日累積的來源漏斗統計（gathered→filtered→emitted），與 `source_attribution.jsonl` 一起餵給**來源記分卡**（見下方「來源評分」節；GH Actions 每日 commit）

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

**注入防護 `[加入: 2026-07-17]`：** 日報條目的標題/摘要來自外部網路，記者一律視為引用資料而非指令；條目內出現指令式文字不執行，回報「⚠️ 疑似注入」轉知主編（`.claude/rules/wiki-reporter-shared.md` 邊界限制）。

**來源歸因走 ledger、不進 wiki 正文：** 記者在回報訊息填「來源歸因」欄（非 wiki 正文），主編彙整時 append 至 `data/source_attribution.jsonl`。此設計取代了舊的 `[[sources/xxx]]` wikilink 機制（2026-07-11 撤除——wikilink 會污染 web reader 且 Graph 二元邊答不了來源比重問題）。

---

## Wiki Lint（`/wiki-lint`，每週，10 步）

排程：雲端 routine `weekly-wiki-lint-cloud`（每週六 09:00 台北，runbook 見 `docs/cloud-runbooks/weekly-lint.md`）；本機手動執行為補救路徑。

```mermaid
flowchart TD
    L1["1. 載入 wiki 全貌"] --> L2
    L2["2. 六記者並行（model: sonnet）\n3a 矛盾 / 3b 孤立 / 3c 過期(用最後新聞更新判)\n3d resolved 收尾 / 3e 呈現品質 / 3f 入口層健檢\n3g 待查證回訪"] --> L3
    L3["3. 語意分岔／死案候選（需使用者確認）"] --> L4
    L4["4. 建議新實體頁"] --> L5
    L5["5. 更新 overview.md"] --> L6
    L6["6. 規則健檢 6a–6g\n(矛盾/引用/遵守率/年齡/來源健康+記分卡\n/跨檔語意矛盾/品質指標+成長迴路蒸餾)"] --> L7
    L7["7. 讀者模擬驗收（3 讀者 3 跳測試）"] --> L8
    L8["8. append log（含 metrics 趨勢）"] --> L9
    L9["9. 更新 index.md"] --> L10
    L10["10. 收尾閉迴路\ncommit wiki → 測試 → build web → 單一 push"]
```

**6e 來源健康 + 記分卡 `[改版: 2026-07-16]`：** 除既有「連續 3 天 count=0」抓取告警外，每週執行 `python scripts/source_scorecard.py` 附記分卡表；樣本充足且 Wilson 下界與 Presence 雙低者列觀察名單回報使用者，不自行動 pipeline。

**心跳紀錄 `[加入: 2026-07-27]`：** 成功／no-op／中止一律 append `src/logs/task_scheduler.log` 並 commit——讓「跑了但無事可改」與「靜默死亡」在 GitHub 上可分辨（2026-07-25 雲端 lint 無聲失敗、死因不可考的教訓）。

---

## 週報（`/weekly`，每週對外交付）

`[加入: 2026-07-26]` 當週技術新聞的教學式深挖專欄，輸出 `weekly/YYYY-Wnn.md`，全文 5 分鐘讀完；與 `/wiki-weekly-review`（對內策展）分工。

```mermaid
flowchart TD
    W1["1. 蒐集素材\n近 7 日 news/*.md（唯讀）\n+ wiki/log.md 同期 ingest\n+ index.md 近期異動 + feature-radar.md"] --> W2
    W2["2. 防重複檢查\n掃描既有 weekly/*.md 的深挖題目\n撞題須有新角度才准再上"] --> W3
    W3["3. 四段式撰寫\n(1) 頭條敘事（300–500 字，不列清單）\n(2) 技術討論 + 深挖專欄（400–600 字，教學式）\n(3) 下週看什麼（可證偽預告，下週回收對錯）\n(4) 檔尾數字"] --> W4
    W4["4. 收尾閉迴路\ncommit → 測試 → build web → 單一 push"] --> W5
    W5["build_web.py 結構化解析 weekly/\n→ web_reader/data/weekly/\n→ web reader 週報頁籤"]
```

---

## 來源評分（監控層，2026-07-16 上線）

**Phase 1＝純監控**：分數不回饋 pipeline 任何行為；enforcement（汰換、門檻調整、黑名單下放）屬 Phase 2，門檻＝累積 ≥ 60 天資料且逐項走 `/pipeline-change-check`。設計依據與逐來源機制：`docs/source-scoring-optimization.md`。

```mermaid
flowchart TD
    REG["data/source_registry.json\n（單一真相源：註冊名↔slug\n↔score_reliability↔curation_mode）"]
    FUN["data/source_funnel.jsonl\n（每日漏斗，GH Actions append）"]
    ATT["data/source_attribution.jsonl\n（wiki 歸因，主編 append）"]
    PC1["data/external/domain_pc1.csv\n（Lin et al. 2023，11,520 domains\n每季複查時效）"]

    REG & FUN & ATT & PC1 --> SC["scripts/source_scorecard.py\n（純 stdlib、零 LLM）\n收錄率/Wilson 下界/wiki 率\n/Presence/HHI/domain 信譽分佈\nBayesian 假票平滑"]

    SC -->|每週| LINT6E["/wiki-lint 6e\n附表＋觀察名單建議\n（人工確認才動 registry/blogroll）"]
    SC -->|每日 build| WEB["build_web.py 嵌 window.TRANSPARENCY\n→ web reader 關於頁「資料透明度」"]
```

**公道性規則**（防指標冤枉特定來源）：whitelist 來源（官方源/Blogroll）不排 Presence 名次、另列保險組；跨日重覆視窗抓法（dev.to top=30）收錄率帶 † 不跨來源比較（registry `rate_comparable` 欄）；零樣本顯示「—」不回吐平滑先驗。

---

## 規則一致性治理（兩層防線）

`.claude/commands/`、`.claude/rules/`、`CLAUDE.md` 之間有大量交叉引用與同步配對，靠人肉維持一致會漂移。機械檢查已腳本化（`scripts/check_rules.py` 讀 `.claude/review-registry.json`，跑裸露引用/路徑存在/錨點/同步配對四類檢查 + coupling 提示），兩層防線確保「改了規則就會被驗」：

```mermaid
flowchart TD
    EDIT["改動 .claude/commands|rules 或 CLAUDE.md"] --> H2

    H2["第一層：Stop hook（收工檢查）\ncheck_rules_on_stop.py\n偵測規則檔 mtime > 上次綠檢\n→ block 收工，逼先驗"]
    H2 --> H3["第二層：DoD 兜底\nrun_tests.py 內建 check_rules.py\n測試不綠不算完工"]

    H3 --> CHECK{"python scripts/check_rules.py"}
    CHECK -->|零錯誤| MARK["寫 .claude/.last-rules-check\n（兩層共用記號檔，重置提醒）"]
    CHECK -->|有 ❌| FIX["/review-commands 薄殼\n判讀失敗 → 修檔案或改 registry\n→ 重跑到零錯誤"]
    FIX --> CHECK
```

**通用化：** 此機制已抽成全域 skill `/build-review-command`（通用引擎 + 專案 registry 分離），可在其他專案快速建立同套兩層防線。

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
        W["weekly/YYYY-Wnn.md（/weekly 產出）"]
    end
    B & C & D --> BUILD["scripts/build_web.py\n（wikilink 斷鏈檢查 + 領域欄位防呆\n+ 剝除 [[sources/*]] 分析標記不外洩 web\n+ 嵌來源記分卡 window.TRANSPARENCY\n+ 週報結構化解析）"]
    A --> BUILD
    W --> BUILD
    BUILD --> E
```

**唯讀/限制：** `news/` 唯讀；`log.md` 只能 append；wiki 檔案只能在 `CLAUDE_NEWS/wiki/`；記者不可碰 `feature-radar.md`/`index.md`/`log.md`（主編統一序列化）。

---

## 模組對照（想改哪裡看這裡）

| 想做的事 | 動哪個檔 |
|---------|---------|
| 新增新聞來源 | `src/news_aggregator/sources/` 繼承 `BaseSource`，在 `main.py` sources 列表註冊 |
| 增減權威部落客 | `src/news_aggregator/sources/blogroll.json`（status: probation/active/retired，汰換依來源記分卡建議、使用者確認） |
| 調來源品質標籤 / 看來源效益 | `data/source_registry.json`（標籤）＋ `python scripts/source_scorecard.py`（記分卡，隨 `/wiki-lint` 6e 週跑） |
| 改過濾規則 | `src/news_aggregator/filter.py`（純規則，無 LLM） |
| 改日報格式 | `.claude/commands/news-pipeline-steps.md` Step 1b |
| 改週報格式 | `.claude/commands/weekly.md` |
| 改記者職責/規則 | `.claude/rules/wiki-ingest-[category].md` |
| 改 web 呈現 | `web_reader/`（設計規範見 `.claude/rules/web-reader-design.md`）+ `scripts/build_web.py` |
| 改任何規則/指令後驗證 | `/review-commands`（判讀 `scripts/check_rules.py` 失敗並修復；機械檢查已掛進 `run_tests.py`） |
| 改規則一致性檢查項 | `.claude/review-registry.json`（同步配對/錨點/allowlist，登記於此即生效） |

執行日誌：`src/logs/` | 測試：`scripts/run_tests.py`
