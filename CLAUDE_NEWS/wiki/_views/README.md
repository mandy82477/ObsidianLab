# _views — Obsidian 內部視圖（不上網站）

這裡放**只在 Obsidian 裡用**的維運視圖。`scripts/build_web.py` 只掃 `wiki/*.md`（不遞迴）
與 `wiki/entities`、`wiki/topics` 兩個資料夾，因此本目錄的內容不會出現在網站上。

## wiki-health.base

用 Obsidian Bases（核心外掛，已啟用）查詢 entities/topics 頁面的 frontmatter。
frontmatter 由 `scripts/gen_wiki_frontmatter.py` 生成——**頁面標頭的粗體欄位才是唯一
的家**，frontmatter 只是它的機器投影，跟 `web_reader/data/` 一樣屬建置產物。改內容
請改粗體標頭再重跑腳本；手改 frontmatter 會被覆寫。

```bash
python scripts/gen_wiki_frontmatter.py
```

六個視圖：

| 視圖 | 回答什麼 |
|------|---------|
| ⚠️ 高引用但停滯 | **最該先看**：入鏈 ≥ 15 但超過 21 天沒有新聞更新的頁。很多頁指向它、讀者被導過去卻看到舊東西；頁面沒壞、鏈結沒斷，屬靜默失效 |
| 陳舊排行 | 依「幾天沒有新聞更新」倒序，一眼看出誰停最久 |
| 孤島（沒人指向） | 入鏈 ≤ 3 但近期有更新——一直在維護卻沒人指向，讀者到不了。新建頁常在此，補 wikilink 即可脫離 |
| 供料來源分布 | 每頁的主要供料來源與歸因筆數，看單一來源集中度 |
| 週更頁節奏監控 | 有「更新頻率」欄的頁面上次策展多久前 |
| 全頁總表 | 所有欄位的總覽，可自行排序篩選 |

## 為什麼是 Bases 而不是 Dataview

此 vault 未安裝 Dataview，Bases 則是已啟用的核心外掛，能力足夠（屬性篩選＋表格視圖）。

差別在於：Bases 只讀 frontmatter properties，**讀不到散文與 markdown 表格**。若日後想把
`community-tech-tools` 的工具目錄、`enterprise-tool-tracker` 的企業表變成可排序視圖，
需要安裝 Dataview 並改用 DataviewJS（`dv.io.load()` 讀原始檔自行解析），Bases 做不到。
