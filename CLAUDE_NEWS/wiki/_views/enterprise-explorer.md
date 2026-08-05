# 企業工具追蹤 · 可篩選視圖

> **資料來源：** `wiki/topics/enterprise-tool-tracker.md` 的 `## 企業工具使用現況` 表格，開啟時即時解析。
> 這裡**不存任何資料**——原表仍是唯一的家，要改內容請改原頁。

備註欄在原表常有數百字，此視圖截斷至 120 字以便橫向比較；完整內容見原頁。
輸入框打字即時篩選（例如打 `❌` 看退出的企業、打 `Claude Code` 看用該工具的），點欄位標題排序。

```dataviewjs
await dv.view("CLAUDE_NEWS/wiki/_views/table-explorer", {
  page: "CLAUDE_NEWS/wiki/topics/enterprise-tool-tracker.md",
  section: "## 企業工具使用現況",
  truncate: { "備註": 120, "規模": 40 },
  tally: ["狀態", "AI 編碼工具"],
  sortBy: "事件日期",
  sortAsc: false
});
```
