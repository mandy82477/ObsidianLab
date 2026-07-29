# 雲端排程 trigger 定義（source of truth）

`[建立: 2026-07-25]`

雲端 routine 的定義只存在 claude.ai 的 trigger API，**repo 內沒有備份就等於沒有 source of truth**——2026-07-12 曾發生「文件記載的 trigger ID 根本不存在，routine 連續兩天沒跑而無人察覺」。本目錄 `docs/cloud-runbooks/triggers/` 下的 JSON 是各 trigger 的鏡像備份，用於比對與還原。

## 現行 trigger

| 名稱 | ID | cron（UTC） | 台北時間 | 定義檔 | runbook |
|------|----|------|------|--------|---------|
| `daily-news-pipeline-cloud` | `trig_01AWf2wwmVeL3ykPCSyxyvzw` | `0 13 * * *` | 每日 21:00 | `docs/cloud-runbooks/triggers/daily-news-pipeline-cloud.json` | `docs/cloud-runbooks/daily.md` |
| `weekly-wiki-lint-cloud` | `trig_01E41amaGSNuL8jeUhCR8iUw` | `0 1 * * 6` | 每週六 09:00 | `docs/cloud-runbooks/triggers/weekly-wiki-lint-cloud.json` | `docs/cloud-runbooks/weekly-lint.md` |
| `claude-code-daily-tip` | `trig_01RKBaFd9zKAGjHxHhcDdJxn` | `0 0 * * *` | 每日 08:00 | `docs/cloud-runbooks/triggers/claude-code-daily-tip.json` | —（自包含 prompt，非新聞 pipeline；例外理由見鏡像 JSON `note` 欄）|

另有 `cloud-writeback-probe`（`trig_01KYk75uTSqLsXcmTNaawmLL`）為 2026-07-10 的寫回測試殘留，已 disabled，未納入備份。

上游第一段 GitHub Actions `daily-gather`（`.github/workflows/daily-gather.yml`，`0 10 * * *` UTC）在 repo 內，不需鏡像。

## 維護規約

1. **改 trigger 前先改 runbook**——trigger prompt 是薄殼，只指向 runbook，不含任何步驟細節（理由見 `docs/cloud-runbooks/_shared.md`）
2. **改完 trigger 後同步更新對應的鏡像 JSON**，讓鏡像與雲端一致
3. **定期核對**：`RemoteTrigger list` 的結果要與本目錄一致；文件寫了 trigger ID 不代表它真的存在
4. runbook 引用的步驟標題受 `scripts/check_rules.py` 保護（登記在 `.claude/review-registry.json`），改 command 檔的步驟標題會讓測試套件變紅

## 還原方式

trigger 遺失時，用對應 JSON 的 `job_config` / `cron_expression` / `name` 重新 `RemoteTrigger create`，新的 ID 要回填本檔表格。
