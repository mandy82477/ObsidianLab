# 雲端 routine 共用規則

`[建立: 2026-07-25]`

所有雲端排程 routine（`daily.md` / `weekly-lint.md`）開頭都必須先讀本檔。
routine 的 trigger prompt 只是薄殼（「cd 到 CLAUDE_NEWS，讀某份 runbook 照做」），**真正的執行規範全部在 repo 內**，跟著 pipeline 一起版本控管。

---

## 為什麼 trigger prompt 要是薄殼 `[加入: 2026-07-25]`

2026-07-25 review 發現：舊的 trigger prompt 直接把步驟編號寫死（`Step 0 / 1a / 1b / 3 / 4 / 5 / 6`、`Step 6a / 6c / 6d / 6f`），而 prompt 存在雲端 API、不在 repo 內，`scripts/check_rules.py` 掃不到。後果已經實際發生：**舊 daily prompt 的列舉裡沒有 `Step 1c`**（`--confirm-digest`，2026-07-13 漏失 25 則新聞後才補的防線），雲端沒漏做純粹是因為 agent 讀檔時順著往下做了，不是 prompt 要求的。

因此定下三條規約：

1. **trigger prompt 不得包含任何步驟編號、步驟標題或執行細節**，只能指向 runbook
2. **runbook 引用步驟時用標題錨點（含中文標題全稱），不用純編號**，並登記進 `.claude/review-registry.json` 由測試套件保護
3. **runbook 只承載環境差異，不承載行為** `[加入: 2026-07-25]`——閘門、檢查、重試、失敗處理一律寫在 command 檔（`.claude/commands/news-pipeline-steps.md`、`.claude/commands/wiki-lint.md`），讓**本機 `/news-pipeline` 與雲端排程跑出完全相同的行為**。允許/不允許寫在 runbook 的分界，見 `news-pipeline-steps.md` 的「本機與雲端的行為必須一致」表

> 判斷標準一：這份 prompt 在 pipeline 改版後會不會靜默走偏？若會，把它搬進 repo。
> 判斷標準二：這條規則換到另一個環境還成立嗎？成立 → 寫進 command 檔，不寫在 runbook。

---

## 環境覆寫（三份 runbook 共用）

雲端是 Linux 沙盒，repo 內文件多處寫的是使用者本機的 Windows 路徑。**一律忽略檔案裡出現的 Windows 寫法**（`C:\...`、`...python.exe`），改用：

| 變數 | 雲端值 |
|------|--------|
| 工作目錄 | repo checkout 內的 `CLAUDE_NEWS/`（所有操作前先 `cd` 進去） |
| `REPO_ROOT` | 上述 `CLAUDE_NEWS/` 的絕對路徑 |
| `PYTHON` | `python3` |
| 今日日期 | `date -u +%F`（UTC）。**每日 pipeline 的目標日期不用此值**——見 daily.md 開頭 |

測試用 `python3 scripts/run_tests.py`，建置用 `python3 scripts/build_web.py`。

**環境自備補丁（第一件事，先於任何步驟）`[加入: 2026-07-25]`：**

```
python3 scripts/cloud_bootstrap.py
```

雲端沙盒預設缺 `python-dotenv`（`main.py` 匯入鏈第一步就撞）、`feedparser`、以及 `sgmllib3k`（其 `setup.py install` 在 Python 3.11 觸發 distutils 相容性錯誤，導致 `pip install -r src/requirements_news.txt` 整包失敗）。這三個缺口自 2026-07-14 起**每次雲端執行都復現**（至少 07-14、07-21、07-22、07-23、07-24 五次），過去都靠當場手動修，容器一回收就沒了。

上述腳本把那套手動修法固化：冪等（已存在就跳過）、不致命（失敗只印警告、退出碼恆為 0）。**它是 workaround 不是真解**——真解是雲端基礎映像預裝這些套件，見 `docs/workaround-register.md` 對應列。

**egress 限制：** 雲端沙盒封鎖一般外部網域（Reddit / HN / Google News 全回 403），因此**任何需要抓取外部新聞的步驟都不在雲端執行**，由 GitHub Actions 負責（見 `docs/daily-automation.md`）。

---

## 收尾閉迴路

**實際步驟不在本檔**：每日走 `.claude/commands/news-pipeline-steps.md` 的 `Step 3` / `Step 4` / `Step 5`，每週走 `.claude/commands/wiki-lint.md` 的 `10. 收尾閉迴路`。本檔只記共用理由。

形狀相同：commit（無變更則跳過，不算失敗）→ 跑測試套件（失敗則跳過 web build 但**仍推送已完成的 commit**）→ build → **單一 `git push`**。

**為何只能 push 一次：** 每次 push 觸發一個 GitHub Pages 部署，多次 push 會讓部署互相搶佔（concurrency race），最後那個關鍵的 web 部署可能被取消，線上停在舊版而 pipeline 無從得知。一次推送 = 一個部署 = 無 race。

### push 失敗重試：見 `.claude/commands/news-pipeline-steps.md` 的 `Step 5`

重試程序（重試上限、detached HEAD 檢查、唯一可自動解的衝突）是**本機與雲端共用的行為**，因此完整定義在該步驟內，本檔不重複也不摘要具體指令——摘要一久就會與正本失步。

**為何在雲端特別致命：** 你的 commit 只存在這個容器裡，push 不成功就跟著容器一起消失，而且下次是全新 checkout，救不回來。本機至少 commit 還在，隔天還能補推。**但兩邊照同一套程序處理**——差別只在後果嚴重度，不在做法。

---

## 無人值守原則

雲端 routine 沒有互動使用者可以即時確認，因此：

- **STARTED 開跑標記（環境補丁之後、任何步驟之前）`[加入: 2026-07-27]`**：append 一行 `[cloud <routine 名> STARTED <UTC 時間戳>]` 到 `src/logs/task_scheduler.log`，立即 `git add` → commit（訊息 `chore: cloud <routine 名> started <date>`）→ **push**。**為什麼開跑就要 push 一次：** 收尾心跳只涵蓋「活著走到收尾」的情境；2026-07-25 weekly lint 的無聲失敗最可能死在中途（session 被殺不會留任何東西），單靠收尾心跳無法與「根本沒跑起來」分辨。有了開跑標記，GitHub 上變成四態可判：`STARTED + OK 心跳`＝成功；`STARTED + FAILED 心跳`＝失敗但可追查；**`STARTED 無後續`＝中途死（可據此查 session 層）**；`完全無 STARTED`＝trigger 沒觸發或環境起不來。**與「單一 push」原則不衝突**：該原則防的是收尾階段多次連續 push 造成 Pages 部署互相搶佔；開跑 push 與收尾 push 相隔整個 routine 時長（數十分鐘以上），無並發競爭，且其部署內容與線上無異、無害


- **凡 command 檔標示「需使用者確認」的動作，一律不得自行執行**，改寫成待辦留在 `wiki/log.md` 本次紀錄的「📋 待使用者確認」清單
- **不可為了讓流程跑完而降低品質門檻**（例如資料不新鮮就硬生日報）
- **每次執行都必須留下可追查的證據——無論成功／no-op／中止** `[改版: 2026-07-27]`：append 一行結果到 `src/logs/task_scheduler.log` 並隨收尾一起 commit push（每日走 `news-pipeline-steps.md`「Step 6」、每週走 `wiki-lint.md`「10. 收尾閉迴路」的心跳紀錄步驟，本檔不重複步驟細節）。中止時同樣先寫 FAILED/ABORTED 心跳再結束，不可靜默。**為什麼 no-op 也要寫：** 2026-07-25 weekly lint 無聲失敗、死因不可考——若只規定中止留證據，「順利跑完但無事可改」與「靜默死亡」在 GitHub 上都是零 artifact，無從分辨，驗證等於白等
- 全程繁體中文輸出
