// ArchiveList.jsx — archive timeline (presentation only)
// Data lives in data-sample.js — edit that file, not this one.

function ArchiveRow({ date, dow, tag, title, sub, count }) {
  return (
    <a href={"#news/" + date} className="arch__row">
      <div className="arch__row__date">
        {date.slice(5)}
        <span className="dow">{dow}</span>
      </div>
      <div className="arch__row__focus">
        {tag && <span className="tag">{tag}</span>}
        {title}
        {sub && <span className="sub">{sub}</span>}
      </div>
      <div className="arch__row__count">
        {count}
        <span className="unit">items</span>
      </div>
    </a>
  );
}

function ArchiveMonth({ num, name, range, count, articles, children }) {
  return (
    <section className="arch__month">
      <div className="arch__monthMark">
        <div className="arch__monthMark__num">{num}</div>
        <span className="arch__monthMark__name">{name}</span>
        <div className="arch__monthMark__meta">
          <div>{range}</div>
          <div><b>{count}</b> digests<span className="sep">·</span><b>{articles}</b> articles</div>
        </div>
      </div>
      <div className="arch__days">{children}</div>
    </section>
  );
}

function Sparkline({ data }) {
  const max = Math.max(...data, 1);
  const W = 1100;
  const H = 80;
  const stepX = data.length > 1 ? W / (data.length - 1) : W;
  const pts = data.map((v, i) => `${(i * stepX).toFixed(1)},${(H - (v / max) * (H - 12) - 4).toFixed(1)}`).join(" ");
  const ranked = data.map((v, i) => ({ v, i })).sort((a, b) => b.v - a.v).slice(0, 3);
  return (
    <svg className="arch__spark__svg" viewBox={`0 0 ${W} ${H}`} preserveAspectRatio="none">
      <defs>
        <linearGradient id="spark-fade" x1="0" x2="1">
          <stop offset="0"    stopColor="var(--ink-1)" stopOpacity="0.15"/>
          <stop offset="0.1"  stopColor="var(--ink-1)" stopOpacity="0.7"/>
          <stop offset="0.92" stopColor="var(--ink-1)" stopOpacity="0.85"/>
          <stop offset="1"    stopColor="var(--ink-1)" stopOpacity="0.2"/>
        </linearGradient>
      </defs>
      <line x1="0" y1={H - 4} x2={W} y2={H - 4} stroke="var(--border-1)" strokeWidth="1"/>
      <polyline points={pts} fill="none" stroke="url(#spark-fade)" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
      {ranked.map((r) => {
        const x = r.i * stepX;
        const y = H - (r.v / max) * (H - 12) - 4;
        return <circle key={r.i} cx={x} cy={y} r="3" fill="var(--ochre-9)"/>;
      })}
    </svg>
  );
}

function ArchiveList() {
  const meta   = window.SAMPLE_META          || {};
  const may    = window.SAMPLE_ARCHIVE_MAY   || [];
  const apr    = window.SAMPLE_ARCHIVE_APR   || [];
  const mar    = window.SAMPLE_ARCHIVE_MAR   || [];
  const counts = window.SAMPLE_SPARKLINE     || [];

  const totalDays     = meta.archiveDays     || (may.length + apr.length + mar.length);
  const totalArticles = meta.archiveArticles || "—";
  const totalSources  = meta.archiveSources  || "—";
  const archiveStart  = meta.archiveStart    || "—";
  const archiveEnd    = meta.archiveEnd      || "—";

  const aprCount = apr.reduce((s, r) => s + r.count, 0);
  const marCount = mar.reduce((s, r) => s + r.count, 0);

  return (
    <article className="archive">
      <header className="hero">
        <div className="hero__kicker">archive · 時序檔案室</div>
        <h1 className="hero__title"><em>{totalDays}</em> days, <em>filed</em>.</h1>
        <div className="hero__meta">
          <span><b>{archiveStart}</b> <span className="sep">→</span> <b>{archiveEnd}</b></span>
          <span className="sep">·</span>
          <span><b>{totalArticles}</b> articles</span>
          <span className="sep">·</span>
          <span><b>{totalSources}</b> sources</span>
          <span className="sep">·</span>
          <span>md vault</span>
        </div>
      </header>

      {may.length > 0 && (
        <ArchiveMonth num="05 · 2026" name="May" range={`${may[may.length-1].date} → ${may[0].date}`}
          count={may.length} articles={may.reduce((s,r)=>s+r.count,0)}>
          {may.map((r) => <ArchiveRow key={r.date} {...r} />)}
        </ArchiveMonth>
      )}

      <ArchiveMonth num="04 · 2026" name="April" range="2026-04-01 → 04-30" count={apr.length} articles={aprCount}>
        {apr.map((r) => <ArchiveRow key={r.date} {...r} />)}
      </ArchiveMonth>

      <ArchiveMonth num="03 · 2026" name="March" range="2026-03-09 → 03-31" count={mar.length} articles={marCount}>
        {mar.map((r) => <ArchiveRow key={r.date} {...r} />)}
      </ArchiveMonth>

      {counts.length > 0 && (
        <aside className="arch__spark">
          <div className="arch__spark__head">
            <span>daily volume</span>
            <em>signal across {totalDays} days</em>
            <span className="ct">{counts.length} pts · ochre marks top 3</span>
          </div>
          <Sparkline data={counts}/>
          <div className="arch__spark__legend">
            <span>{archiveStart}</span>
            <span>peaks · 04-30, 03-20, 03-31</span>
            <span>{archiveEnd}</span>
          </div>
        </aside>
      )}
    </article>
  );
}

window.ArchiveList = ArchiveList;
