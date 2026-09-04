# .claude/commands/news-pipeline-steps.md 沿革（教訓存檔）

本檔是 `.claude/commands/news-pipeline-steps.md` 的歷史敘事，不是待執行規則；條文處的「沿革檔 YYYY-MM-DD[ 字母]」皆指本檔對應段。考古鏈：`[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

本檔是**歷史敘事，不是待執行步驟**——步驟已在上方，執行 pipeline 時不必讀本檔。存放於此的原因：步驟本身已能獨立執行，敘事只在有人想問「為什麼有這條」時才需要。考古鏈為 `[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

**2026-07-25 A**（本機／雲端行為一致）：冪等閘、push 重試最初只寫進雲端 runbook，等於本機跑同一條 pipeline 卻少了兩道保護。

**2026-07-24**（Step 1c 漏做的後果）：2026-07-14～07-24 雲端自動化期間，每日確認率幾乎為 0（僅本機手動執行的 07-19、07-22 為 100%），兩階段確認機制形同空轉，跨日去重完全靠 `seen_urls.json` 獨撐。

**2026-07-31**（web build gate 的由來）：舊規則是「整包測試過才建 web」。當日雲端日更因 3 個抓料端的 `ModuleNotFoundError` 判定失敗而跳過 build，網站整天停在前一天——但日報與 wiki 都已正常產出並 commit，那 3 個案例跟 `build_web.py` 的輸入毫無關係。

**2026-08-15**（多來源條目的來源欄）：記者依日報來源欄做歸因、`data/source_attribution.jsonl` 再餵 `scripts/source_scorecard.py` 的 wiki 率，於是低流量官方來源（幾乎必定輸給 HN／Google News）長期看起來零貢獻——當日 Anthropic Blog 供了最大條的浮水印報導，掛名全歸 HN。

**2026-08-26**（gate 擋下時的修復迴圈）：wiki 懸置探針含千分位逗號 `$1,125` 被切成 `$1` 而 FAIL，日報與 wiki 全部正常，網站卻停更一天，瑕疵本身也沒人修。

**2026-09-02**（append-only 衝突自動解）：雲端 17:00 UTC 班完整跑完日報＋wiki＋web，push 撞上本機同時間的 commit，衝突檔只有 `wiki/log.md`（兩側各自 append 段落，無語意衝突），依舊規則放棄整輪，22:00 班重做一遍。
