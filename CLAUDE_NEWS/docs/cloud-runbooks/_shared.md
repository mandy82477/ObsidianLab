# 雲端 routine 共用規則

`[建立: 2026-07-25]`

所有雲端排程 routine（`daily.md` / `weekly-lint.md`）開頭都必須先讀本檔。
routine 的 trigger prompt 只是薄殼（「cd 到 CLAUDE_NEWS，讀某份 runbook 照做」），**真正的執行規範全部在 repo 內**，跟著 pipeline 一起版本控管。

---

## 為什麼 trigger prompt 要是薄殼 `[加入: 2026-07-25]`

2026-07-25 review 發現：舊的 trigger prompt 直接把步驟編號寫死（`Step 0 / 1a / 1b / 3 / 4 / 5 / 6`、`Step 6a / 6c / 6d / 6f`），而 prompt 存在雲端 API、不在 repo 內，`scripts/check_rules.py` 掃不到。後果已經實際發生：**舊 daily prompt 的列舉裡沒有 `Step 1c`**（`--confirm-digest`，2026-07-13 漏失 25 則新聞後才補的防線），雲端沒漏做純粹是因為 agent 讀檔時順著往下做了，不是 prompt 要求的。

因此定下兩條規約：

1. **trigger prompt 不得包含任何步驟編號、步驟標題或執行細節**，只能指向 runbook
2. **runbook 引用步驟時用標題錨點（含中文標題全稱），不用純編號**，並登記進 `.claude/review-registry.json` 由測試套件保護

> 判斷標準：這份 prompt 在 pipeline 改版後會不會靜默走偏？若會，把它搬進 repo。

---

## 環境覆寫（三份 runbook 共用）

雲端是 Linux 沙盒，repo 內文件多處寫的是使用者本機的 Windows 路徑。**一律忽略檔案裡出現的 Windows 寫法**（`C:\...`、`...python.exe`），改用：

| 變數 | 雲端值 |
|------|--------|
| 工作目錄 | repo checkout 內的 `CLAUDE_NEWS/`（所有操作前先 `cd` 進去） |
| `REPO_ROOT` | 上述 `CLAUDE_NEWS/` 的絕對路徑 |
| `PYTHON` | `python3` |
| 今日日期 | `date -u +%F`（UTC） |

測試用 `python3 scripts/run_tests.py`，建置用 `python3 scripts/build_web.py`。

**已知環境缺口：** 雲端沙盒預設缺 `feedparser` / `sgmllib3k`，且 `pip install -r src/requirements_news.txt` 會因 `sgmllib3k` 的 `setup.py install` 觸發 Python 3.11 distutils 相容性錯誤而失敗。遇到時的繞路見 `docs/workaround-register.md` 對應列（`pip download --no-deps sgmllib3k` 取原始碼、手動把 `sgmllib.py` 複製進 site-packages）。此繞路是 session-local，每個新容器都要重做。

**egress 限制：** 雲端沙盒封鎖一般外部網域（Reddit / HN / Google News 全回 403），因此**任何需要抓取外部新聞的步驟都不在雲端執行**，由 GitHub Actions 負責（見 `docs/daily-automation.md`）。

---

## 收尾閉迴路（共用）

1. `git add` 對應目錄 → `git commit`（無變更則跳過，不視為失敗）
2. `python3 scripts/run_tests.py` — 失敗則跳過 web build，但**仍要推送已完成的 commit**，並在 log 記 `Tests FAILED - web build skipped`
3. `python3 scripts/build_web.py` → `git add web_reader/` → commit
4. **單一 `git push`** 推送本次全部 commit

**為何只能 push 一次：** 每次 push 觸發一個 GitHub Pages 部署，多次 push 會讓部署互相搶佔（concurrency race），最後那個關鍵的 web 部署可能被取消，線上停在舊版而 pipeline 無從得知。一次推送 = 一個部署 = 無 race。

---

## 無人值守原則

雲端 routine 沒有互動使用者可以即時確認，因此：

- **凡 command 檔標示「需使用者確認」的動作，一律不得自行執行**，改寫成待辦留在 `wiki/log.md` 本次紀錄的「📋 待使用者確認」清單
- **不可為了讓流程跑完而降低品質門檻**（例如資料不新鮮就硬生日報）
- 中止時必須留下可追查的證據：append 一行到 `src/logs/task_scheduler.log` 並 commit push，不可靜默結束
- 全程繁體中文輸出
