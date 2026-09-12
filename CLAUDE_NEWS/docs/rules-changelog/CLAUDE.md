# 根目錄 `./CLAUDE.md` 沿革（教訓存檔）

本檔是根目錄 `./CLAUDE.md` 的歷史敘事，不是待執行規則；條文處的「沿革檔 YYYY-MM-DD」皆指本檔對應段。考古鏈：`[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

**2026-08-29 A**（commit 範圍：只 add 指名路徑）：本條原本只寫在 `.claude/commands/news-pipeline-steps.md`「絕不要在補跑流程裡用 `git add -A`」，射程只到補跑流程；臨時修復工作不在射程內，於是當天出事：一個訊息為「fix: 目標日期取自耐久的 gathered_archive」的 commit，掃走了同時間另一份工作中的 `wiki/entities/pricing.md`（+43）、`wiki/topics/model-comparison.md`（+30）、`code-quality-decline.md`、`log.md`（+39）。兩層傷害：(a) commit 了半成品——那批 wiki 改動尚未修完錨點、規則也還沒移到 lint 檔；(b) 殺掉可追溯性——本專案的品質系統建立在「為什麼加這條」查得到（`log.md` Query 條目、`[加入: YYYY-MM-DD]` 標記、條文裡的「教訓來自 X 月 Y 日」），而這些考古全靠 `git log` / `git blame`。訊息錯置的 commit 讓那條路斷掉，且事後補不回來。

**2026-08-29 B**（開放迴路掃描為何印三個數字、失敗為何不得當 0）：`scripts/open_loops.py` 初版只印一個總數 229，其中 195 由舊語法盲區＋逾期懸置主導——其餘四類全部歸零，總數也只掉到 34，那不是彙整，是「盲區筆數＋雜訊」。同時 feature-radar 那一類初版用全文 `count("⏳")`，把跨層重複與圖例都算進去，實測 23 對真實 13（高報 77%），且未逾 90 天的觀望根本不算積壓。因此輸出拆成「需收尾／已跳票／存量遷移」三個數字，各答不同問題。另外懸置類掃描壞掉會拋 `PendingScanUnavailable`，此時標題印「數量未知」、總計標下界 `≥`、exit code 非 0——一支專門防低報的腳本，自己靜默回 0 就是得了它要治的病。
