# 每日 pipeline 自動化架構（分裂式）

`[建立: 2026-07-10]`

每日日報改為**全自動、關機也跑**,採「GitHub Actions 抓料 + 雲端 routine 做 LLM」分裂架構。
手動 `/news-pipeline` 完整保留為**補救路徑**,不受本架構影響。

---

## 為什麼要拆兩段

單一雲端 routine 跑不動每日 pipeline:雲端沙盒的 **egress 政策封鎖一般外部網域**（Reddit / HN / Google News … 全回 403），抓新聞（Step 1a）抓到 0 條。實測 2026-07-10 雲端 0 條、GitHub Actions 43 條。

拆解關鍵:**抓新聞不需 LLM/API（純 Python 下載）**,可移到有完整網路的 GitHub Actions;**生日報/wiki 需訂閱 LLM**,留在雲端 routine（不需上網,egress 擋不到）。

```
① GitHub Actions（.github/workflows/daily-gather.yml）
   10:00 UTC / 18:00 台北 · 網路無限制 · 免 API
   跑 python -m news_aggregator.main --gather-only
   → commit gathered_items.json + seen_urls.json + emitted_items.json 回 master
        ↓（資料進 repo）
② 雲端 routine（daily-news-pipeline-cloud，trig_01JNrBGyrsZk1HjBQeJ7UKLG）
   13:00 UTC / 21:00 台北 · 訂閱 LLM · 不需上網
   讀 ① 的 gathered_items.json（新鮮度防線：非今日/0 條則中止不生假日報）
   → 生日報 → 六記者 ingest → build → 單一 push → 上站
```

兩段用 **3 小時時間差**鬆耦合（`[改版: 2026-07-11]` 原設計 30 分鐘，首跑當日 GitHub Actions 排程延遲 1.5–2.7 小時導致 ② 新鮮度防線中止、未生假日報，已拉大緩衝覆蓋觀測到的最大延遲）；② 的新鮮度防線確保 ① 若失敗,② 不會拿舊料生假日報。

## 為什麼快取檔要 commit（與 CLAUDE.md 資料檔例外的關係）

`seen_urls.json` / `emitted_items.json` 是**跨日去重快取**。本機跑時它們留在磁碟自然持久;但 GitHub Actions **每次全新 checkout**,不 commit 回去的話隔天去重就失效、重複出舊聞。故 ① **必須** commit 這兩個檔 + `gathered_items.json`。
CLAUDE.md 說資料檔「不需 commit」是指手動流程無此義務,非禁止;自動流程基於持久化需要而 commit,不違反。單一寫者=① Actions（手動 `--date` 補救不碰快取,見 `main.py` line 178）。

## 出問題時如何補救

自動線任一段失敗（Actions 紅叉 / 雲端 routine ABORTED / 某天沒上站），**用手動路徑補**:

```
本機執行：/news-pipeline 2026-07-XX
```

手動路徑本機網路無限制、一條龍跑完,`--date` 補救**不碰去重快取**,不會污染自動線狀態。

## 監控與驗證

- **Actions**：https://github.com/mandy82477/ObsidianLab/actions → `daily-gather`
- **雲端 routine**：https://claude.ai/code/routines/trig_01JNrBGyrsZk1HjBQeJ7UKLG
- **是否上站**：master 每天應出現 `data: daily gather`（①）+ `news/wiki/web`（②）共約 4 筆 commit;網站 Pages 自動重建。
- **首跑結果（2026-07-11）**：❌ 失敗。① 實際延遲至 14:02 UTC 才 push（設計 12:30 UTC），② 於 13:00 UTC 開跑時讀不到當日資料，新鮮度防線正確中止、未生假日報。已本機補跑並將 ① 排程提早至 10:00 UTC（3 小時緩衝），見 `docs/workaround-register.md` 對應列。下次自動線觀察日：2026-07-12 起。
