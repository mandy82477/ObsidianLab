---
description: 手動觸發新聞聚合器，抓取並寫出 news/YYYY-MM-DD.md。
argument-hint: [YYYY-MM-DD]
---

# Wiki Digest

手動執行新聞聚合器，補抓今日（或指定日期）的 Claude / Anthropic 相關新聞。

## 使用時機

- 排程器當天未執行（例如電腦關機或網路中斷）
- 日報條目過少或來源全部失敗，需要重跑
- 想在正式排程外即時取得最新新聞

## 步驟

### 1. 確認目標日期

從 `$ARGUMENTS` 取得日期（若無則使用今天 YYYY-MM-DD）。

### 2. 確認環境

執行前確認：
- `CLAUDE_NEWS/src/` 目錄存在
- `.env` 存在且 `ANTHROPIC_API_KEY` 已設定（或確認 claude CLI 已登入）
- 若不確定依賴是否安裝：`pip list | findstr -i "anthropic trafilatura feedparser"`

### 3. 執行聚合器

```bash
cd src
python -m news_aggregator.main
```

執行日誌即時寫入 `src/logs/news_aggregator.log`，若有錯誤可直接查看。

### 4. 確認輸出

確認 `news/YYYY-MM-DD.md` 已寫出，並檢查：
- 條目數是否 > 3 則（若過少，查看日誌確認哪個來源失敗）
- 日報末尾「來源狀態表」是否至少一個來源顯示成功
- 若全部來源失敗，告知使用者並建議：
  1. 確認網路連線
  2. 確認 `ANTHROPIC_API_KEY` 是否有效
  3. 查看 `src/logs/news_aggregator.log` 尋找錯誤訊息

### 5. 後續動作

日報寫出後，詢問使用者是否立即執行 `/wiki-ingest` 更新 wiki。

## 注意事項

- Windows 環境：確保在正確的 Python 環境執行（若有多個 venv）
- 重跑不會覆蓋 `seen_urls.json` 中已記錄的 URL——重跑同一天可能只抓到新增條目
- 執行完成後若要 git push，聚合器本身已整合 `git_push.py`（自動 commit）
