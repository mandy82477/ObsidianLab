// EntityList.jsx — wiki index page (presentation only)
// Data lives in data-sample.js — edit that file, not this one.

function WikilinkRow({ path, summary, state, stateColor, updated }) {
  return (
    <a href="#" className="entityrow">
      <div className="entityrow__main">
        <div className="entityrow__link">
          <span className="br">[[</span>
          <span className="path">{path}</span>
          <span className="br">]]</span>
        </div>
        <div className="entityrow__summary">{summary}</div>
      </div>
      <div className="entityrow__state"><span className={"pill pill--"+stateColor}>● {state}</span></div>
      <div className="entityrow__updated">{updated || ""}</div>
    </a>
  );
}

function EntityList() {
  const scrolls = [
    { num: "i.",  name: "wiki/overview",      sub: "當前局勢·每週更新", href: "#wiki/overview" },
    { num: "ii.", name: "wiki/feature-radar", sub: "熱度雷達·每日更新", href: "#wiki/feature-radar" },
  ];

  const entities = window.SAMPLE_ENTITIES || [];
  const topics   = window.SAMPLE_TOPICS   || [];
  const meta     = window.SAMPLE_META     || {};

  const totalPages = entities.length + topics.length + scrolls.length;

  return (
    <div className="wikipage">
      <header className="hero" style={{padding: "0 0 36px"}}>
        <div className="hero__kicker">wiki · 知識圖譜</div>
        <h1 className="hero__title"><em>{totalPages}</em> pages<span className="br">·</span>a graph.</h1>
        <div className="hero__meta">
          <span><b>{entities.length}</b> entities</span>
          <span className="sep">·</span>
          <span><b>{topics.length}</b> topics</span>
          <span className="sep">·</span>
          <span>last ingest <b>{meta.lastIngestFull || "—"}</b></span>
          <span className="sep">·</span>
          <span>obsidian-style markdown</span>
        </div>
      </header>

      {/* top-level scrolls — overview + feature-radar */}
      <nav className="scrolls" aria-label="top-level wiki pages">
        {scrolls.map((s) => (
          <a key={s.name} href={s.href} className="scrolls__col">
            <div className="scrolls__num">{s.num}</div>
            <div className="scrolls__name">{s.name}</div>
            <div className="scrolls__sub">{s.sub}</div>
          </a>
        ))}
      </nav>

      <h2>entities — 實體頁</h2>
      <div className="entitytable">
        {entities.map((r) => <WikilinkRow key={r.path} {...r} />)}
      </div>
      <h2>topics — 進行中議題</h2>
      <div className="entitytable entitytable--topics">
        {topics.map((r) => <WikilinkRow key={r.path} {...r} />)}
      </div>
    </div>
  );
}
window.EntityList = EntityList;
