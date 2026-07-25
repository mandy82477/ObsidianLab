# 每日 pipeline 自動化架構（分裂式）

`[建立: 2026-07-10]`

每日日報改為**全自動、關機也跑**,採「GitHub Actions 抓料 + 雲端 routine 做 LLM」分裂架構。
手動 `/news-pipeline` 完整保留為**補救路徑**,不受本架構影響。

> **雲端 routine 的執行規範不在本檔** `[加入: 2026-07-25]`
> 本檔講「為什麼這樣拆」；雲端 routine 實際照什麼步驟跑，見 `docs/cloud-runbooks/daily.md`（每日）與 `docs/cloud-runbooks/weekly-lint.md`（每週），共用規則見 `docs/cloud-runbooks/_shared.md`。trigger 本身的定義鏡像與維護規約見 `docs/cloud-runbooks/README.md`。

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
② 雲端 routine（daily-news-pipeline-cloud，trig_01AWf2wwmVeL3ykPCSyxyvzw）
   13:00 UTC / 21:00 台北 · 訂閱 LLM · 不需上網
   讀 ① 的 gathered_items.json（新鮮度防線：非今日/0 條則中止不生假日報）
   → 生日報 → 六記者 ingest → build → 單一 push → 上站
```

兩段用 **3 小時時間差**鬆耦合（`[改版: 2026-07-11]` 原設計 30 分鐘，首跑當日 GitHub Actions 排程延遲 1.5–2.7 小時導致 ② 新鮮度防線中止、未生假日報，已拉大緩衝覆蓋觀測到的最大延遲）；② 的新鮮度防線確保 ① 若失敗,② 不會拿舊料生假日報。

## 為什麼快取檔要 commit（與 CLAUDE.md 資料檔例外的關係）

`seen_urls.json` / `emitted_items.json` 是**跨日去重快取**。本機跑時它們留在磁碟自然持久;但 GitHub Actions **每次全新 checkout**,不 commit 回去的話隔天去重就失效、重複出舊聞。故 ① **必須** commit 這兩個檔 + `gathered_items.json`。
CLAUDE.md 說資料檔「不需 commit」是指手動流程無此義務,非禁止;自動流程基於持久化需要而 commit,不違反。

**寫者分工 `[改版: 2026-07-25]`：** 原本記載「單一寫者=① Actions」,但那導致 ② 的 `--confirm-digest` 結果從未進 repo——② 在容器內把 `emitted_items.json` 標記為已確認,容器一銷毀就沒了,下次全新 checkout 讀到的仍是未確認。實測 2026-07-14～07-24 雲端期間每日確認率幾乎為 0（僅本機手動執行的 07-19、07-22 為 100%）,兩階段確認機制形同空轉,跨日去重全靠 `seen_urls.json` 獨撐。現改為:
- ① Actions 寫 `gathered_items.json` / `seen_urls.json` / `emitted_items.json`（新增未確認條目）
- ② 雲端 routine **只寫 `emitted_items.json` 的確認欄位**,並與日報同批 push（見 `.claude/commands/news-pipeline-steps.md` 的 `Step 1c：確認 emitted-cache`）
- 兩者時間錯開 3 小時且都走 push 重試,不構成競態;手動 `--date` 補救不碰快取,見 `main.py`

## 出問題時如何補救

自動線任一段失敗（Actions 紅叉 / 雲端 routine ABORTED / 某天沒上站），**用手動路徑補**:

```
本機執行：/news-pipeline 2026-07-XX
```

手動路徑本機網路無限制、一條龍跑完,`--date` 補救**不碰去重快取**,不會污染自動線狀態。

## 監控與驗證

- **看門狗（告警層）`[加入: 2026-07-25]`**：`.github/workflows/daily-watchdog.yml`,每日 15:00 UTC / 23:00 台北檢查當日 `gathered_items.json` 與 `news/<date>.md` 是否齊全,缺件則 job 失敗——GitHub 對失敗的排程 workflow 會寄信,這是本系統唯一的主動告警管道。紅燈時看 job summary 判斷是哪一段缺件,依下方補救路徑處理。
- **Actions**：https://github.com/mandy82477/ObsidianLab/actions → `daily-gather` / `daily-watchdog`
- **雲端 routine**：https://claude.ai/code/routines/trig_01AWf2wwmVeL3ykPCSyxyvzw
- **是否上站**：master 每天應出現 `data: daily gather`（①）+ `news/wiki/web`（②）共約 4 筆 commit;網站 Pages 自動重建。
- **首跑結果（2026-07-11）**：❌ 失敗。① 實際延遲至 14:02 UTC 才 push（設計 12:30 UTC），② 於 13:00 UTC 開跑時讀不到當日資料，新鮮度防線正確中止、未生假日報。已本機補跑並將 ① 排程提早至 10:00 UTC（3 小時緩衝），見 `docs/workaround-register.md` 對應列。
- **07-12 追查發現真正根因（2026-07-13 確認）**：② 這個雲端 routine **從未被實際建立過**——文件記載的 trigger ID `trig_01JNrBGyrsZk1HjBQeJ7UKLG` 用 `RemoteTrigger list` 查詢完全不存在。也就是說 07-11、07-12 連兩天①都有成功抓料 commit（07-12 那次已用完整 CI log 核對確認：58→34 則、`e18b02d` 正常 push），但②從頭到尾沒有任何排程在跑，並非延遲或中止。已於 2026-07-13 15:15 UTC 用 `RemoteTrigger create` 重新建立正確的 daily-news-pipeline-cloud（trig_01AWf2wwmVeL3ykPCSyxyvzw，cron `0 13 * * *`）。
- **首次真正排程執行結果（2026-07-14）**：✅ 成功。13:00 UTC 觸發，新鮮度防線通過（`gathered_items.json` date=2026-07-14、60 則），依序完成 Step 0/1b/2/3/4/5/6，統一 push 4 筆 commit（`1b90dfb..8b6793e`）。過程中兩個非架構性插曲：(1) 雲端 sandbox 環境預設缺 `feedparser`/`sgmllib3k`（Python 3.11 distutils 相容性問題），導致 Step 1c 與測試套件一度失敗，已用手動安裝 `sgmllib.py` 繞過（session-local，未持久化，登記於 `docs/workaround-register.md` 待補環境層級真解）；(2) 本地 git 初始為 detached HEAD（因 session 啟動時 fetch 前 `origin/master` 快取落後），已重新 `checkout -B master` 修復，未遺失任何 commit。分裂架構（① GH Actions 抓料 + ② 雲端 routine 產 news/wiki/web）確認穩定跑通。
