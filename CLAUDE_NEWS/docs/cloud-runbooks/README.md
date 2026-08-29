# 雲端排程 trigger 定義（source of truth）

`[建立: 2026-07-25]`

雲端 routine 的定義只存在 claude.ai 的 trigger API，**repo 內沒有備份就等於沒有 source of truth**——2026-07-12 曾發生「文件記載的 trigger ID 根本不存在，routine 連續兩天沒跑而無人察覺」。本目錄 `docs/cloud-runbooks/triggers/` 下的 JSON 是各 trigger 的鏡像備份，用於比對與還原。

## 現行 trigger

| 名稱 | ID | cron（UTC） | 台北時間 | 定義檔 | runbook |
|------|----|------|------|--------|---------|
| `daily-news-pipeline-cloud` | `trig_01AWf2wwmVeL3ykPCSyxyvzw` | `0 22 * * *` | 隔日 06:00 | `docs/cloud-runbooks/triggers/daily-news-pipeline-cloud.json` | `docs/cloud-runbooks/daily.md` |
| `weekly-wiki-lint-cloud` | `trig_01E41amaGSNuL8jeUhCR8iUw` | `0 3 * * 6` | 每週六 11:00 | `docs/cloud-runbooks/triggers/weekly-wiki-lint-cloud.json` | `docs/cloud-runbooks/weekly-lint.md` |
| `daily-watchdog-push` | `trig_01FqjE53JVAKTnPxnt8iJCb6` | `30 1 * * *` | 09:30 | `docs/cloud-runbooks/triggers/daily-watchdog-push.json` | `docs/cloud-runbooks/watchdog-push.md` |

另有 `cloud-writeback-probe`（`trig_01KYk75uTSqLsXcmTNaawmLL`）為 2026-07-10 的寫回測試殘留，已 disabled，未納入備份。

上游第一段 GitHub Actions `daily-gather`（`.github/workflows/daily-gather.yml`，`0 10 * * *` UTC）與告警層 `daily-watchdog`（`0 15 * * *` UTC）都在 repo 內，不需鏡像。

`daily-watchdog`（寄信）與 `daily-watchdog-push`（推手機）是**同一套判準的兩個送達管道**，共用 `scripts/daily_health_check.py`；判準不可分別改寫在 workflow 或 runbook 裡（理由見 `docs/cloud-runbooks/watchdog-push.md`）。

## 維護規約

1. **改 trigger 前先改 runbook**——trigger prompt 是薄殼，只指向 runbook，不含任何步驟細節（理由見 `docs/cloud-runbooks/_shared.md`）
2. **改完 trigger 後同步更新對應的鏡像 JSON**，讓鏡像與雲端一致
3. **定期核對**：`RemoteTrigger list` 的結果要與本目錄一致；文件寫了 trigger ID 不代表它真的存在
4. runbook 引用的步驟標題受 `scripts/check_rules.py` 保護（登記在 `.claude/review-registry.json`），改 command 檔的步驟標題會讓測試套件變紅

## 還原方式

trigger 遺失時，用對應 JSON 的 `job_config` / `cron_expression` / `name` 重新 `RemoteTrigger create`，新的 ID 要回填本檔表格。
