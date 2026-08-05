# 社群工具目錄 · 可篩選視圖

> **資料來源：** `wiki/topics/community-tech-tools.md` 的 `## 工具目錄` 表格，開啟時即時解析。
> 這裡**不存任何資料**——原表仍是唯一的家，要改內容請改原頁。

輸入框打字即時篩選（比對整列文字），點欄位標題排序。

```dataviewjs
await dv.view("CLAUDE_NEWS/wiki/_views/table-explorer", {
  page: "CLAUDE_NEWS/wiki/topics/community-tech-tools.md",
  section: "## 工具目錄",
  truncate: { "簡介": 140 },
  tally: ["採用", "類型"],
  sortBy: "首次出現",
  sortAsc: false
});
```
