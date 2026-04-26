``` mermaid
flowchart TD
    subgraph sources["sources/"]
        S1[anthropic_blog.py]
        S2[github_releases.py]
        S3[hackernews.py]
        S4[reddit.py]
        S5[google_news.py]
    end

    CFG[config.py\nSEARCH_TERMS / LOOKBACK_HOURS\nAPI tokens / paths]
    CACHE[(seen_urls.json\n跨執行去重快取)]

    S1 & S2 & S3 & S4 & S5 --> DEDUP

    DEDUP[dedup.py\nURL 正規化去重\n模糊標題去重 0.85\n官方來源優先]
    DEDUP --> ENRICH

    ENRICH[enricher.py\ntrafilatura 抓原文\n補充 summary 欄位]
    ENRICH --> FILTER

    subgraph FILTER["filter.py — 相關性評分"]
        F1{ANTHROPIC_API_KEY?}
        F2[Claude Haiku API\n批次評分 1–5]
        F3{claude CLI 可用?}
        F4[claude -p\n批次評分 1–5]
        F5[略過過濾\n保留全部]
        F1 -->|有| F2
        F1 -->|無| F3
        F3 -->|有| F4
        F3 -->|無| F5
    end

    FILTER -->|score 大於等於 3| ANALYZE

    subgraph ANALYZE["analyzer.py — 中文摘要"]
        A1{ANTHROPIC_API_KEY?}
        A2[Claude API\n寫繁中摘要]
        A3{claude CLI 可用?}
        A4[claude -p\n寫繁中摘要]
        A5[fallback\n純文字列表]
        A1 -->|有| A2
        A1 -->|無| A3
        A3 -->|有| A4
        A3 -->|無| A5
    end

    ANALYZE --> DIGEST
    DIGEST[digest.py\n組合 header + body\n來源狀態表]
    DIGEST --> MD["news/YYYY-MM-DD.md"]
    MD --> GIT[git_push.py\ngit commit & push]

    CFG -.-> sources
    CFG -.-> DEDUP
    CACHE -.-> DEDUP

    MAIN[main.py\norchestrator] -.-> sources & DEDUP & ENRICH & FILTER & ANALYZE & DIGEST & GIT
```
Wiki Lint
``` mermaid
flowchart TD

USER([使用者下指令<br/>執行 wiki lint]) --> IDX
IDX[讀 wiki/index.md<br/>取得所有頁面清單]
IDX --> LOG

LOG[讀 wiki/log.md<br/>確認最近更新紀錄]
LOG --> READ

READ[逐一讀取<br/>entities/ 和 topics/ 頁面]
READ --> LINT

subgraph LINT["Lint 檢查"]
    L1[找矛盾頁面<br/>兩頁描述同一事件但說法不同]
    L2[找孤立頁面<br/>沒有任何其他頁面連結到它]
    L3[標記過期議題<br/>ongoing 但長時間無更新]
    L4[建議新實體頁<br/>被多次提及但尚無專頁]
end

LINT --> FIX

subgraph FIX["修正與更新"]
    F1[修正矛盾內容]
    F2[為孤立頁面補連結]
    F3[將已解決議題<br/>從 topics/ 移至 entities/]
    F4[建立新 entities/ 頁面]
end

FIX --> OVERVIEW
OVERVIEW[更新 wiki/overview.md<br/>當前局勢綜覽]
OVERVIEW --> APPENDLOG

APPENDLOG[Append wiki/log.md<br/>記錄本次 lint 執行]
APPENDLOG --> UPDATEIDX
UPDATEIDX[更新 wiki/index.md]
```