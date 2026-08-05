# 來源健康 · 零產出告警

> **資料來源：** `data/source_funnel.jsonl`（每日抓取漏斗）與 `data/source_registry.json`（來源註冊表），開啟時即時解析。這裡不存任何資料。

這頁存在的理由：**Claude API Release Notes 曾連續 26 天抓到 0 筆而沒有任何人發現**——
`ok: true`、沒有例外、沒有告警，只是靜靜地什麼都沒抓到。那份漏斗資料一直在累積，只是
從來沒有消費者。下一次同類失效應該在第 3 天就浮出來，不是第 26 天。

```dataviewjs
const FUNNEL   = "CLAUDE_NEWS/data/source_funnel.jsonl";
const REGISTRY = "CLAUDE_NEWS/data/source_registry.json";
const WARN_DAYS = { red: 14, amber: 7, watch: 3 };   // 連續零產出天數的告警階梯
const RATE_WINDOW = 30;                              // 收錄率統計窗（天）

try {
  const rawFunnel = await dv.io.load(FUNNEL);
  if (!rawFunnel) throw new Error(`讀不到 ${FUNNEL}`);

  let registry = { sources: [] };
  try { registry = JSON.parse(await dv.io.load(REGISTRY)); } catch (e) { /* 選填 */ }
  const regByName = {};
  for (const s of registry.sources || []) regByName[s.name] = s;

  // ── 解析漏斗：同一天可能有多筆（gather / render / backfill），
  //    取每個 (日期, 來源) 的最大值，避免同日重複計數。
  const byDate = {};              // date -> source -> {gathered, emitted, ok}
  for (const line of rawFunnel.split("\n")) {
    if (!line.trim()) continue;
    let rec;
    try { rec = JSON.parse(line); } catch (e) { continue; }
    const d = rec.date;
    if (!d) continue;
    byDate[d] = byDate[d] || {};
    for (const [name, v] of Object.entries(rec.sources || {})) {
      const cur = byDate[d][name] || { gathered: 0, emitted: 0, ok: true };
      byDate[d][name] = {
        gathered: Math.max(cur.gathered, v.gathered || 0),
        emitted:  Math.max(cur.emitted,  v.emitted  || 0),
        ok: cur.ok && v.ok !== false,
      };
    }
  }

  const dates = Object.keys(byDate).sort();              // 舊 → 新
  const recent = dates.slice(-RATE_WINDOW);
  const names = [...new Set(dates.flatMap(d => Object.keys(byDate[d])))].sort();

  const rows = [];
  for (const name of names) {
    // 連續零產出：從最新一天往回數
    let streak = 0, lastHit = "—";
    for (let i = dates.length - 1; i >= 0; i--) {
      const v = byDate[dates[i]][name];
      if (!v) continue;                                   // 該日無此來源紀錄，跳過
      if (v.gathered > 0) { lastHit = dates[i]; break; }
      streak++;
    }

    let g = 0, e = 0, fails = 0, days = 0;
    for (const d of recent) {
      const v = byDate[d][name];
      if (!v) continue;
      days++; g += v.gathered; e += v.emitted;
      if (!v.ok) fails++;
    }

    let flag = "✅";
    if (streak >= WARN_DAYS.red) flag = "🔴";
    else if (streak >= WARN_DAYS.amber) flag = "🟡";
    else if (streak >= WARN_DAYS.watch) flag = "⚪";
    if (fails > 0) flag += " ⛔抓取失敗";

    const reg = regByName[name];
    rows.push([
      flag,
      name,
      streak,
      lastHit,
      g,
      e,
      g > 0 ? Math.round((e / g) * 100) + "%" : "—",
      reg ? reg.category : "未註冊",
      days,
    ]);
  }

  // 告警優先：連續零產出天數大者在前
  rows.sort((a, b) => b[2] - a[2]);

  const alerts = rows.filter(r => r[0] !== "✅");
  dv.paragraph(
    `資料涵蓋 **${dates.length} 天**（${dates[0]} ~ ${dates[dates.length - 1]}）　｜　` +
    `來源 **${names.length}** 個　｜　` +
    (alerts.length
      ? `⚠️ **${alerts.length} 個來源需留意**：` + alerts.map(r => `${r[1]}（${r[2]} 天）`).join("、")
      : "✅ 全部來源近期都有產出")
  );

  dv.header(3, "來源狀態");
  dv.table(
    ["", "來源", "連續零產出(天)", "最後有產出", `抓取(${RATE_WINDOW}d)`, `進日報(${RATE_WINDOW}d)`, "收錄率", "類別", "有紀錄天數"],
    rows
  );

  dv.paragraph(
    "**判讀：** 連續零產出不必然是缺陷——官方 changelog 本來就可能整週沒發布。" +
    "但它是**唯一能在事前看見靜默失效的訊號**，配合「最後有產出」判斷：該來源平時多久出一次？" +
    "遠超過那個間隔就值得手動打開網址確認。收錄率則看下游門檻，長期偏低代表抓進來的東西不對題。"
  );

} catch (err) {
  const box = dv.container.createEl("pre", {
    text: `視圖失敗：\n${err && err.stack ? err.stack : err}`
  });
  box.style.cssText = "color:var(--text-error);white-space:pre-wrap;font-size:.85em";
}
```
