// ReaderShell.jsx — nav shell + footer (presentation only)
// Footer metadata comes from window.SAMPLE_META in data-sample.js.
function ReaderShell({ active, onNav, children }) {
  const meta = window.SAMPLE_META || {};
  return (
    <div className="reader">
      <header className="reader__nav">
        <div className="reader__nav-inner">
          <a className="reader__brand" href="#today" onClick={(e)=>{e.preventDefault();onNav("today");}}>
            <svg width="28" height="28" viewBox="0 0 44 44" fill="none">
              <rect x="2" y="2" width="40" height="40" rx="2" fill="var(--bg-1)" stroke="var(--ochre-7)"/>
              <path d="M14 18 L14 26 L18 26" stroke="var(--ochre-9)" strokeWidth="1.5" strokeLinecap="round" fill="none"/>
              <circle cx="22" cy="22" r="2.5" fill="var(--ochre-9)"/>
              <path d="M30 18 L30 26 L26 26" stroke="var(--ochre-9)" strokeWidth="1.5" strokeLinecap="round" fill="none"/>
            </svg>
            <div>
              <div className="reader__brand-name">CLAUDE NEWS</div>
              <div className="reader__brand-sub">L L M · W I K I</div>
            </div>
          </a>
          <nav className="reader__navlinks">
            <a href="#today"   className={active==="today"  ?"is-active":""} onClick={(e)=>{e.preventDefault();onNav("today");}}>Today</a>
            <a href="#archive" className={active==="archive"?"is-active":""} onClick={(e)=>{e.preventDefault();onNav("archive");}}>Archive</a>
            <a href="#wiki"    className={active==="wiki"   ?"is-active":""} onClick={(e)=>{e.preventDefault();onNav("wiki");}}>Wiki</a>
            <a href="about.html">About</a>
          </nav>
          <button className="reader__search">
            <img src="https://unpkg.com/lucide-static@latest/icons/search.svg" />
            <span>Search…</span>
            <span className="kbd">⌘K</span>
          </button>
        </div>
      </header>
      <main className="reader__main">{children}</main>
      <footer className="prov" aria-label="provenance">
        <div className="prov__inner">
          <div>
            <div className="prov__h">last ingest</div>
            <div className="prov__last"><em>{meta.lastIngest || "—"}</em>&nbsp;&nbsp;08:00 TST</div>
            <div className="prov__lastsub">{meta.archiveArticles || "—"} articles · {meta.archiveSources || "—"} sources · score ≥ 3</div>
          </div>
          <div>
            <div className="prov__h">sources</div>
            <div className="prov__sources">
              anthropic.com<br/>
              github.com/<span>releases</span><br/>
              news.ycombinator.com<br/>
              reddit.com/<span>r/ClaudeAI</span><br/>
              news.google.com<br/>
              dev.to
            </div>
          </div>
          <div className="prov__repo">
            <div className="prov__h">source</div>
            <a href="https://github.com/mandy82477/ObsidianLab" target="_blank" rel="noreferrer">github.com/mandy82477/ObsidianLab ↗</a>
            <div className="meta">
              obsidian vault · markdown<br/>
              wiki/ · entities / topics<br/>
              news/ · daily reports<br/>
              CC-BY · personal project
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
window.ReaderShell = ReaderShell;
