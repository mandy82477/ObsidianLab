# Claude News

每日自動抓取 Claude / Anthropic 相關新聞，生成 Markdown 日報並維護 LLM 知識庫。

## 架構

```
news/           ← 每日日報（YYYY-MM-DD.md）
wiki/           ← LLM 維護的知識庫（entities/ topics/）
src/            ← Python 新聞聚合器
web_reader/     ← 靜態網頁閱讀器
scripts/        ← 建置工具（build_web.py）
```

完整流程設計：`src/DesignDocument/Design Diagram.md`

---

## 快速上手

1. `pip install -r src/requirements_news.txt`
2. 在 repo 根目錄建立 `.env`，填入 `GITHUB_TOKEN`（建議）、Reddit 金鑰（可選）
3. 執行 `/news-pipeline` 確認完整 pipeline 可正常運作（日誌：`src/logs/task_scheduler.log`）

---

## 日常操作

| 操作 | 指令 |
|------|------|
| 手動執行完整 pipeline | `/news-pipeline` |
| 補跑指定日期 | `/news-pipeline 2026-05-01` |
| 單獨更新 wiki | `/wiki-ingest` |
| 每週 wiki 品質檢查 | `/wiki-lint` |

---

## 環境需求

- Python 3.13+
- Claude Code（互動式 pipeline）
- GitHub Token（避免 API rate limit）
