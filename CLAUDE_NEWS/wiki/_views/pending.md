# 懸置標記 · 逾期佇列

> **資料來源：** `wiki/entities/*.md` 與 `wiki/topics/*.md` 正文內的懸置標記（`❓ **待查證**` / `🔎 **查無官方**`），開啟時即時解析。這裡不存任何資料。
>
> 語法規格見 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節，本頁 regex 是 `scripts/pending_markers.py` 的 `PENDING_RE` 翻譯版——改一邊要改另一邊。frontmatter 的 `pending_count` 等四欄只是本頁的彙總數字（`scripts/gen_wiki_frontmatter.py` 產出），要看**每一筆**懸置標記還是得來這頁。

```dataviewjs
const ROOT = "CLAUDE_NEWS/wiki";
const REVIEW_DEFAULT_DAYS = 14;   // 與 scripts/check_pending_markers.py 的 REVIEW_DEFAULT_DAYS 對齊

try {
  // PENDING_RE 翻自 scripts/pending_markers.py（Python 具名群組 (?P<x>) → JS (?<x>)）
  const PENDING_RE = /(?<sym>[❓🔎])[ 　]*\*{2}(?<kind>待查證|查無官方)\*{2}[ 　]*（標[ ]?(?<marked>\d{4}-\d{2}-\d{2})｜查[ ]?(?<probes>[^）｜]+)(?:｜複[ ]?(?<review>\d{4}-\d{2}-\d{2}))?(?:｜訊[ ]?(?<signal>\d{4}-\d{2}-\d{2}))?）/g;
  // 標準式第四段：｜**題目**：內文（緊接在 metadata 括號後）
  const TITLE_RE = /^｜\*\*([^*]+)\*\*/;
  const FRONTMATTER_RE = /^---\r?\n[\s\S]*?\r?\n---\r?\n/;

  function parseDate(s) {
    const [y, m, d] = s.split("-").map(Number);
    return new Date(y, m - 1, d);
  }
  function addDays(dt, n) {
    const r = new Date(dt);
    r.setDate(r.getDate() + n);
    return r;
  }
  function fmt(dt) {
    const y = dt.getFullYear();
    const m = String(dt.getMonth() + 1).padStart(2, "0");
    const d = String(dt.getDate()).padStart(2, "0");
    return `${y}-${m}-${d}`;
  }

  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const pages = dv.pages(`"${ROOT}/entities" or "${ROOT}/topics"`);

  const rows = [];
  let totalCount = 0, overdueCount = 0, signalledCount = 0;

  for (const p of pages) {
    const path = p.file.path;
    const text = await dv.io.load(path);
    if (!text) continue;
    const body = text.replace(FRONTMATTER_RE, "");

    const slug = path.replace(new RegExp("^" + ROOT + "/"), "").replace(/\.md$/, "");
    const link = `[[${ROOT}/${slug}|${slug}]]`;

    PENDING_RE.lastIndex = 0;
    let m;
    while ((m = PENDING_RE.exec(body)) !== null) {
      const g = m.groups;
      totalCount++;

      const markedDate = parseDate(g.marked);
      const reviewDate = g.review ? parseDate(g.review) : addDays(markedDate, REVIEW_DEFAULT_DAYS);
      const overdueDays = Math.round((today - reviewDate) / 86400000);
      const isOverdue = overdueDays >= 0;
      const hasSignal = !!g.signal;
      if (isOverdue) overdueCount++;
      if (hasSignal) signalledCount++;

      const after = body.slice(m.index + m[0].length, m.index + m[0].length + 200);
      const tm = TITLE_RE.exec(after);
      const title = tm ? tm[1] : "（無題目／短標記，見頁面內文）";

      const prefix = (isOverdue ? "🔴" : "") + (hasSignal ? "📡" : "");

      rows.push({
        prefix, link, title, marked: g.marked, review: fmt(reviewDate),
        overdueDays, hasSignal, signal: g.signal || "—",
      });
    }
  }

  // 排序：訊欄優先 → 逾期天數降序
  rows.sort((a, b) => (b.hasSignal - a.hasSignal) || (b.overdueDays - a.overdueDays));

  dv.paragraph(
    `總筆數 **${totalCount}**　｜　逾期 **${overdueCount}**　｜　有訊號 **${signalledCount}**`
  );

  dv.header(3, "逾期佇列（訊欄優先→逾期天數降序）");
  dv.table(
    ["頁面", "題目", "標記日", "複查日（含預設+14）", "逾期天數", "訊"],
    rows.map(r => [
      (r.prefix ? r.prefix + " " : "") + r.link,
      r.title,
      r.marked,
      r.review,
      r.overdueDays,
      r.signal,
    ])
  );

  dv.paragraph(
    "**判讀：** 逾期天數為負代表尚未到複查日；🔴 已逾期、📡 有訊號（日報已出現後續、待主編處理）。" +
    "此頁只列每一筆的細節；跨頁彙總數字（`pending_count` 等）已寫進各頁 frontmatter，供 Bases 排序篩選。"
  );

} catch (err) {
  const box = dv.container.createEl("pre", {
    text: `視圖失敗：\n${err && err.stack ? err.stack : err}`
  });
  box.style.cssText = "color:var(--text-error);white-space:pre-wrap;font-size:.85em";
}
```
