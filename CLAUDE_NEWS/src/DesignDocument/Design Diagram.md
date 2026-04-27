# Design Diagram

---

## 全流程總覽（run_news.bat）

每日 08:00 由 Windows 工作排程器觸發，依序執行三個步驟。

``` mermaid
flowchart TD
    BAT["🗓 run_news.bat\n每日 08:00 排程"] --> AGG

    AGG["Step 1\nPython 聚合器\nmain.py"] -->|成功| NEWS_OUT
    AGG -->|失敗 exit 1| STOP(["⛔ 停止"])

    NEWS_OUT["news/YYYY-MM-DD.md\nsrc/news_aggregator/seen_urls.json"] --> PUSH1["git commit & push\ngit_push.py"]

    PUSH1 --> WIKI

    WIKI["Step 2\nclaude -p '/wiki-ingest'\n--dangerously-skip-permissions"] -->|成功| WIKI_FILES
    WIKI -->|失敗 exit 非 0| WARN(["⚠ 記錄警告\n跳過 wiki push\nexit 0 繼續"])

    WIKI_FILES["wiki/entities/*.md\nwiki/topics/*.md\nwiki/log.md\nwiki/index.md"] --> PUSH2

    PUSH2["Step 3\ngit add wiki/\ngit commit 'wiki: auto-ingest YYYY-MM-DD'\ngit push"] --> DONE(["✅ 完成"])
```

---

## 聚合器 Pipeline（main.py）

``` mermaid
flowchart TD
    subgraph sources["sources/"]
        S1[anthropic_blog.py]

        subgraph S2box["github_releases.py"]
            S2A["官方 Releases\nanthropics/claude-code\nanthropics/anthropic-sdk-*"]
            S2B["GitHub Repo Search\nclaude-code / claude anthropic\nmcp-server claude\n新建 repo，過去 26h"]
        end

        subgraph S3box["hackernews.py"]
            S3A["Story 搜尋\n'Claude Code' / 'Anthropic'\nscore ≥ 3"]
            S3B["Show HN 搜尋\n'claude' / 'anthropic'\ntags=show_hn, score ≥ 1"]
        end

        subgraph S4box["reddit.py"]
            S4A["r/ClaudeAI\nr/artificial\nr/MachineLearning"]
            S4B["r/LocalLLaMA\n（技術比較 & 真實應用）"]
        end

        S5[google_news.py\n'Claude Code' / 'Anthropic AI']
    end

    CFG["config.py\nSEARCH_TERMS / LOOKBACK_HOURS=26\nAPI tokens / paths"]
    CACHE[("seen_urls.json\n跨執行去重快取")]

    S1 & S2box & S3box & S4box & S5 --> DEDUP

    DEDUP["dedup.py\nURL 正規化去重\n模糊標題去重 threshold=0.85\n官方來源優先"]
    DEDUP --> ENRICH

    ENRICH["enricher.py\ntrafilatura 抓原文\n補充 summary 欄位（最多 600 字）"]
    ENRICH --> FILTER

    subgraph FILTER["filter.py — 相關性評分"]
        F1{ANTHROPIC_API_KEY?}
        F2["Claude Haiku API\n批次評分 1–5"]
        F3{claude CLI 可用?}
        F4["claude -p\n批次評分 1–5"]
        F5["略過過濾\n保留全部"]
        F1 -->|有| F2
        F1 -->|無| F3
        F3 -->|有| F4
        F3 -->|無| F5
    end

    FILTER -->|"score ≥ 3"| ANALYZE

    subgraph ANALYZE["analyzer.py — 中文摘要（5 區塊）"]
        A1{ANTHROPIC_API_KEY?}
        A2["Claude Haiku API\n寫繁中摘要"]
        A3{claude CLI 可用?}
        A4["claude -p\n寫繁中摘要"]
        A5["fallback\n純文字列表"]
        A1 -->|有| A2
        A1 -->|無| A3
        A3 -->|有| A4
        A3 -->|無| A5
    end

    ANALYZE --> DIGEST

    subgraph DIGEST["digest.py — 輸出結構"]
        D1["⭐ 重點話題"]
        D2["🔧 技術更新"]
        D3["💬 技術熱度討論（含情緒標籤）"]
        D4["💰 付費方案動態"]
        D5["📌 今日聚焦（3–5 點總結）"]
    end

    DIGEST --> MD["news/YYYY-MM-DD.md"]
    MD --> GIT["git_push.py\ngit add news/YYYY-MM-DD.md\ngit add seen_urls.json\ngit commit & push"]

    CFG -.-> sources
    CFG -.-> DEDUP
    CACHE -.-> DEDUP

    MAIN["main.py\norchestrator"] -.-> sources & DEDUP & ENRICH & FILTER & ANALYZE & DIGEST & GIT
```

---

## Wiki Ingest Pipeline（/wiki-ingest）

由 run_news.bat Step 2 以 `claude -p "/wiki-ingest" --dangerously-skip-permissions` 觸發，也可手動執行。

``` mermaid
flowchart TD
    TRIGGER["claude -p '/wiki-ingest'\n由 run_news.bat 觸發\n或手動下指令"] --> READ_NEWS

    READ_NEWS["讀 news/YYYY-MM-DD.md\n（今日日報）"] --> READ_WIKI

    READ_WIKI["同時讀取\nwiki/index.md — 現有頁面目錄\nwiki/log.md — 確認是否已 ingest"]

    READ_WIKI --> CHECK{"今日已 ingest?"}
    CHECK -->|是| SKIP(["跳過，記錄並結束"])
    CHECK -->|否| MATCH

    MATCH["比對日報內容 vs index.md\n識別受影響的既有頁面\n識別新實體 / 新議題"]

    MATCH --> UPDATE

    subgraph UPDATE["更新既有頁面（視影響範圍）"]
        U1["entities/*.md\n插入歷史記錄（最新在上）\n更新現況 / 最後更新欄位"]
        U2["topics/*.md\n插入時序條目\n累積技術彙整（不重複）"]
        U3["community-tech-patterns.md\n更新時序 + 熱門應用表格排名"]
    end

    UPDATE --> NEW_PAGES{"需要建立新頁面？"}

    NEW_PAGES -->|"新 entity\n被明確描述有具體資訊"| CREATE_E["建立 entities/xxx.md\n（依 CLAUDE.md 模板）"]
    NEW_PAGES -->|"新 topic\n連續 2 天以上出現"| CREATE_T["建立 topics/xxx.md\n（依 CLAUDE.md 模板）"]
    NEW_PAGES -->|無| APPEND

    CREATE_E & CREATE_T --> APPEND

    APPEND["Append wiki/log.md\n記錄來源日報、更新頁面、新增頁面、摘要"]
    APPEND --> IDX["更新 wiki/index.md\n加入新頁面連結、更新頁面數"]
    IDX --> DONE(["wiki 檔案更新完成\n→ run_news.bat Step 3 git push"])
```

---

## Wiki Lint（/wiki-lint）

每週手動執行，維護 wiki 品質。

``` mermaid
flowchart TD

USER(["使用者下指令\n執行 wiki lint"]) --> IDX
IDX["讀 wiki/index.md\n取得所有頁面清單"]
IDX --> LOG

LOG["讀 wiki/log.md\n確認最近更新紀錄"]
LOG --> READ

READ["逐一讀取\nentities/ 和 topics/ 頁面"]
READ --> LINT

subgraph LINT["Lint 檢查"]
    L1["找矛盾頁面\n兩頁描述同一事件但說法不同"]
    L2["找孤立頁面\n沒有任何其他頁面連結到它"]
    L3["標記過期議題\nongoing 但長時間無更新"]
    L4["建議新實體頁\n被多次提及但尚無專頁"]
end

LINT --> FIX

subgraph FIX["修正與更新"]
    F1["修正矛盾內容"]
    F2["為孤立頁面補連結"]
    F3["將已解決議題\n從 topics/ 移至 entities/"]
    F4["建立新 entities/ 頁面"]
end

FIX --> OVERVIEW
OVERVIEW["更新 wiki/overview.md\n當前局勢綜覽"]
OVERVIEW --> APPENDLOG

APPENDLOG["Append wiki/log.md\n記錄本次 lint 執行"]
APPENDLOG --> UPDATEIDX
UPDATEIDX["更新 wiki/index.md"]
```
