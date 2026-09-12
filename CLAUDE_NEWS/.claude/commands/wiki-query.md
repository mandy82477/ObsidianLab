---
description: 查 wiki 內容並照契約回答：問「wiki 裡 X 怎麼說」「最近 X 怎樣」「X 和 Y 差在哪」、要出處、或要把查證結果寫回 wiki 時使用。
---

# Wiki 查詢

Query 是本庫三個動作之一（寫入／查詢／整理，見 `./CLAUDE.md`「這是一個 LLM wiki：三個動作」）。本指令規定查詢怎麼走、答案怎麼交、什麼時候要把答案寫回去。

---

## 1. 分流：先選路，不要一律先讀 index

六路的完整定義住 `wiki/CLAUDE.md`「搜尋策略」，**照那裡執行，本節只做速查**：

| 問題長這樣 | 走第幾路 |
|---|---|
| 出現專有名詞、issue 編號、版本號、錯誤碼 | 1（直接 Grep `wiki/`） |
| 概念、選型、「哪頁在講 X」 | 2（`wiki/index.md` 挑頁 → 讀該頁頂部 callout） |
| 「哪些頁是某狀態／某領域／多久沒更新」 | 3（Grep 頁面標頭欄位） |
| 「最近 X 怎樣」「上週發生什麼」 | 4（`wiki/log.md` 先 Grep 日期，或 `news/`） |
| 「誰負責這頁／這頁多久更新一次」 | 5（`.claude/reporter-rules/` 負責頁面表） |
| 「誰引用 X」「A 和 B 怎麼連」「這議題散在哪幾節」 | 6（`python scripts/wiki_graph.py`） |

一路查完沒有答案就換下一路，不要在同一路上加關鍵字硬撈。

## 2. 回答契約

- **每個事實帶三樣**：`[[wikilink]]`（指到事實的家那一頁，長頁加錨點）＋日期（該頁標的查證日或事件日）＋證據等級（沿用該頁既有用語：官方一手／官方文件／跨媒體與社群多來源／具名表態／單次高互動討論／社群估算）。
- **「現在」和「當時」不混**：頁頂 callout 與結論表是現在；`## 時序`、`## 歷史記錄`、`wiki/log.md` 是當時。引用歷史條目時要明說那是當時的說法。
- **懸置標記照抄不升級**：頁面標 ❓ 待查證／🔎 查無官方的事實，回答時一併說它還沒定案，不得改寫成肯定句。
- **找不到就說找不到**：回「wiki 沒有」並列出查過哪幾路、用了哪些關鍵字。**不得用通用知識補**——那會讓使用者以為那句話經過本庫查證。
- 數字有兩個版本時並陳，不擇一。

## 3. 答案回流（使用者提問通道）

wiki 裡沒有、或使用者點名要查證的事實，走這條通道——**查證是入場券**：

1. 以 WebFetch／WebSearch 查**一手來源**（官方文件、官方公告、原始 repo、原始貼文）。查不到一手來源 → 只能標懸置，不得寫成事實。
2. 寫進事實該在的那一頁（判斷落點看 `.claude/reporter-rules/` 各領域的負責頁面表），**必標查證日＋來源連結**；寫頁前先讀 `.claude/reporter-rules/wiki-ingest-format.md`（頁面格式、懸置標記語法、表格上限）與 `.claude/reporter-rules/wiki-reporter-shared.md`（書寫風格硬上限、讀者語言禁詞）。紀律見 `./CLAUDE.md`「使用者提問通道」與 `.claude/rules/collection-scope.md`。
3. `wiki/log.md` append 一筆 Query 條目（append only，格式照既有條目）：

   ```
   ## YYYY-MM-DD Query：一句話標題

   **點出什麼：** 使用者問了什麼、庫內現況是什麼。
   **根因：** 為什麼庫內會是這樣。
   **處置：** (a) … (b) … 歸因 slug `user-query`。
   ```

4. `data/source_attribution.jsonl` append 一行，`source` 為 `user-query`，schema 見 `data/README.md`。

**不寫頁的情況**：純查詢（使用者只是要答案）、事實已經在頁上且未過期。這兩種只回答，不動檔案。

## 4. 質疑回流

使用者的問題若**揭露缺陷**（該頁答不出它該答的問題、數字沒有來源、規則有漏洞、機制從沒被執行過），除了上一節的 Query 條目，回報末尾多一行：

```
是否屬新型質疑模式：是（模式名一句）／否（已屬既有模式：…）
```

判「是」者交 `/wiki-lint` 步驟 7b 評估要不要加進抽問題庫（判準見 `.claude/reporter-rules/wiki-lint-inquiry.md`「題庫維護」，加題須經使用者確認）。

## 5. 收尾

動過任何 wiki 頁時：

```
python scripts/check_cell_limits.py --page <頁面 slug>
python scripts/check_reader_language.py --page <頁面 slug>
```

**把實際輸出的最後一行抄進回報**，不是寫「✅ 通過」；順序固定：改完 → 跑 → 抄輸出 → 不再動那一頁。

改動照 `./CLAUDE.md`「完工定義」閉迴路（測試綠／已 commit／依賴缺口已登記）；**commit 與否屬使用者裁決**，本指令不自行 commit。
