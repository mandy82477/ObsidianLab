// table-explorer — 原地解析 wiki 頁面裡的 markdown 表格，變成可篩選、可點欄排序的視圖。
//
// 為什麼是「解析原表」而不是「一列一筆記」：Bases 只讀 frontmatter properties，
// 要讓它查得到就得把 123 個工具拆成 123 個檔案，直接違反 wiki 的「一頁一故事」。
// DataviewJS 可以 dv.io.load() 讀原始檔自行解析，於是原表仍是唯一的家，這裡只是視圖。
//
// 用法（在 .md 的 dataviewjs 區塊內）：
//   await dv.view("CLAUDE_NEWS/wiki/_views/table-explorer", {
//     page: "CLAUDE_NEWS/wiki/topics/community-tech-tools.md",
//     section: "## 工具目錄",
//     truncate: { "簡介": 140 },     // 選填，過長欄位在視圖裡截斷
//     tally: ["採用", "類型"],        // 選填，要出統計的欄位
//     sortBy: "首次出現",             // 選填，預設排序欄
//     sortAsc: false                  // 選填
//   });

const { page, section, truncate = {}, tally = [], sortBy = null, sortAsc: initAsc = false } = input;

let raw = null;
try {
  raw = await dv.io.load(page);
} catch (e) {
  raw = null;
}

if (!raw) {
  dv.paragraph(`⚠️ 讀不到 \`${page}\`。路徑以 vault 根目錄為基準，若 vault 根不是 ObsidianLab 請調整。`);
} else {
  const lines = raw.split("\n");
  const start = lines.findIndex((l) => l.trim() === section);
  let header = null;
  const rows = [];

  if (start >= 0) {
    for (let i = start + 1; i < lines.length; i++) {
      const l = lines[i].trim();
      if (l.startsWith("## ")) break; // 下一個大節即停
      if (!l.startsWith("|")) continue;
      const cells = l.replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim());
      if (cells.every((c) => /^:?-{2,}:?$/.test(c))) continue; // 分隔列
      if (!header) {
        header = cells;
        continue;
      }
      rows.push(cells);
    }
  }

  if (!header) {
    dv.paragraph(`⚠️ 在 \`${page}\` 找不到 \`${section}\` 區塊的表格（章節標題須完全相符）。`);
  } else {
    // ── 統計行 ──────────────────────────────────────────────────────
    const bits = [`**共 ${rows.length} 列**`];
    for (const col of tally) {
      const i = header.indexOf(col);
      if (i < 0) continue;
      const counts = {};
      for (const r of rows) counts[r[i]] = (counts[r[i]] || 0) + 1;
      const parts = Object.entries(counts)
        .sort((a, b) => b[1] - a[1])
        .map(([k, n]) => `${k || "—"} ${n}`);
      bits.push(`${col}：${parts.join("、")}`);
    }
    dv.paragraph(bits.join("　｜　"));

    // ── 控制列 ──────────────────────────────────────────────────────
    const controls = dv.container.createDiv();
    controls.style.margin = "0.6em 0";
    const box = controls.createEl("input", {
      attr: { type: "text", placeholder: "篩選：打字比對整列文字" },
    });
    box.style.cssText = "width:100%;padding:4px 8px";
    const results = dv.container.createDiv();

    let sortCol = sortBy && header.indexOf(sortBy) >= 0 ? header.indexOf(sortBy) : 0;
    let asc = initAsc;

    const cut = (val, col) => {
      const lim = truncate[col];
      return lim && val.length > lim ? val.slice(0, lim) + "…" : val;
    };

    function render() {
      // 整段包 try/catch：這函式由 input 事件呼叫，丟出的例外會變成無人處理的
      // rejection、畫面只剩空白（2026-08-05 首版用 MarkdownRenderer 就是這樣靜默失敗）。
      try {
        const q = box.value.trim().toLowerCase();
        const view = (q ? rows.filter((r) => r.join(" ").toLowerCase().includes(q)) : rows.slice()).sort(
          (a, b) => {
            const x = a[sortCol] || "";
            const y = b[sortCol] || "";
            return (x < y ? -1 : x > y ? 1 : 0) * (asc ? 1 : -1);
          }
        );

        results.empty();
        const head = header.map((h, i) => (i === sortCol ? `${h} ${asc ? "▲" : "▼"}` : h));
        const body = view.map((r) => r.map((c, i) => cut(c, header[i])));

        // 用 Dataview 自己的 renderer（會算繪儲存格裡的 markdown 連結）。
        // dv.table 一律寫進 dv.container，故暫時把 container 換成 results 再換回，
        // 這樣重繪只清掉表格、不會連上方統計行與輸入框一起清掉。
        const prev = dv.container;
        dv.container = results;
        try {
          dv.table(head, body);
        } finally {
          dv.container = prev;
        }

        const note = results.createEl("div", { text: `顯示 ${view.length} / ${rows.length} 列` });
        note.style.cssText = "opacity:.6;font-size:.85em;margin-top:.4em";

        // dv.table 內部有非同步算繪，等一拍再抓表頭掛排序
        setTimeout(() => {
          results.querySelectorAll("thead th").forEach((th, i) => {
            th.style.cursor = "pointer";
            th.onclick = () => {
              if (sortCol === i) asc = !asc;
              else {
                sortCol = i;
                asc = true;
              }
              render();
            };
          });
        }, 0);
      } catch (err) {
        results.empty();
        const e = results.createEl("pre", { text: `視圖算繪失敗：\n${err && err.stack ? err.stack : err}` });
        e.style.cssText = "color:var(--text-error);white-space:pre-wrap;font-size:.85em";
      }
    }

    box.addEventListener("input", () => render());
    render();
  }
}
