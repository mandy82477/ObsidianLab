# 評審派工模板（Opus，一位；實作後續用做複核）

貼 `../dispatch-prefix.md` 共用前綴，接本段，再逐字貼 dispatch-prefix 的「評審輸出契約」。

```
## 本次任務：第 {N} 波評審——`wiki/{slug}.md`

工作目錄 {REPO}；scratchpad {SCRATCH}（設計者逐字稿在 `docs/page-audits/{slug}-{date}-draft.md`）。

**受評**：`{slug}-{date}-proposal.md`＋`-proposal-map.md`＋`-draft.md`。
**上游**：`{slug}-{date}.md`（健檢卡含預測對照）、`wave{N}-cold-reader-{date}.md`、`{slug}-{date}-verified.md`（主編查證；行號口徑見該檔）。
**對象頁**：{頁、archive、鄰居；跨頁改動須走 `pending_handoffs.py`}。
**規則檔與腳本**：`.claude/rules/{rules}.md`、`wiki-ingest-format.md`、`wiki-reporter-shared.md`、`scripts/check_reader_language.py`、`check_cell_limits.py`、`check_pending_markers.py`、`check_hierarchy.py`、`table_census.py`、`build_web.py`、`.claude/review-registry.json`；上一波 `{prev}-review.md` 當格式樣板（含實作單與實作複核）。

**主 session 已定**：使命句「{…}」。**裁決點處置**：{每點：待使用者（兩案並評、預設是什麼）／代判（值）}。主 session 代判的數字你要自己重算。

**四視角逐一站**：明天的維護者（記者照改後規則檔下週會不會寫回舊形狀；狀態欄誰填、依據什麼）／機器（錨點入邊、registry、兩閘每格、蒸餾月份與上限、懸置語法、腳本宣稱逐條讀原始碼）／冷讀者（原四題逐題預測改版後幾跳、卡不卡；新表「誰會遇到」能不能對號；動作句是否不下指令）／治理（有沒有偷偷立法到全站；去向表一行不少——**抽驗 ≥5 段**；節點三問本頁與每個鄰居都答了沒；整頁去向有無偷渡成「順手併掉」；跨維護者有沒有走帳本）。

**前幾波實作複核抓到的病提前防**（skill 評審清單逐條過）：退場條文三句三答案、狀態值定義與示範列不符、callout 數字與表不一致、「未列入」無條文依據、標頭「最後更新」沒跟、砍前保命條款、「搬家」與「免動作」對實作者要寫動詞、一手優先、退場條文連活產品行為一起跑、併頁殼配套。

{接：評審輸出契約逐字}

**產物**：`docs/page-audits/{slug}-{date}-review.md`。回報：🔴 幾條各一句、🟡 幾條、實作單步數、設計者第二輪必須親改的項目（若無寫「無」）。繁體中文。
```

提案若在評審開工後更新，主 session 立刻 SendMessage：「以磁碟現行檔為準，若已讀舊版重讀」。

## 續用：實作複核（實作落地後，SendMessage 同一 agent）

```
實作已完成（Sonnet 實作者照你 {k} 步＋設計者第二輪逐字），請做**實作複核**，append 到 review 末尾 `## 實作複核（{date}）`，上限 50 行。逐步核「照做／偏離（哪裡）／漏做」。重點親自核（不信回報）：
1. 保命條款：{被砍處的懸置有沒有先搬家}。
2. 結論表與 draft 逐字對；判準與列序一致；{代判項}落地。
3. 懸置：實作者報 {n}／逾期 {m}——你重跑 `iter_pending()` 裁定。
4. 規則檔與 lint 步驟：退場、補位、入口三句齊；`table_census.py` 機制欄「有」；驗紅一次。
5. 蒸餾與 archive；`build_web.py` 錨點 WARN 不增。
6. 實作者自報偏離逐條判可接受與否。
7. 跨頁與帳本：只做定稿範圍、類別中文、對象頁正確。
8. 冷讀者原四題逐題預測改版後結果（給複驗對照）。
結尾：放行／不放行＋剩餘 🔴 附修法。
```
