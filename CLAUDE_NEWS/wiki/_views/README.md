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

## DataviewJS 表格視圖

Bases 只讀 frontmatter properties，**讀不到散文與 markdown 表格**。頁面內那些真正像資料庫
的大表（工具目錄、企業追蹤）要變成可排序可篩選的視圖，只能靠 DataviewJS——它能
`dv.io.load()` 讀原始檔自行解析。

關鍵是**不必把 121 個工具拆成 121 個檔案**：原表仍是唯一的家，視圖只是即時解析它。
拆檔才是違反「一頁一故事」的做法。

| 檔案 | 內容 |
|------|------|
| `table-explorer.js` | 共用實作：解析指定頁面指定區塊的 markdown 表格 → 篩選框＋點欄排序＋統計行。兩個視圖共用，不留兩份副本 |
| `tools-explorer.md` | `community-tech-tools.md` 的 `## 工具目錄`（121 列 × 5 欄），統計採用與類型 |
| `enterprise-explorer.md` | `enterprise-tool-tracker.md` 的 `## 企業工具使用現況`（39 列 × 7 欄），統計狀態與工具；備註欄截斷至 120 字以便橫向比較 |

要為其他表格加視圖，複製一個 .md 改 `page` / `section` / `truncate` / `tally` 即可，
不需要動 JS。

**路徑以 vault 根目錄為基準**（即 `ObsidianLab/`），所以帶 `CLAUDE_NEWS/` 前綴；
若 vault 根不同，改各 .md 裡的 `page` 與 `dv.view()` 路徑。

### 兩者分工

- **Bases**（`wiki-health.base`）：查頁面層級的 metadata——哪頁停滯、哪頁沒人指向
- **DataviewJS**（`*-explorer.md`）：查頁面**內**的表格資料——哪個工具、哪家企業
