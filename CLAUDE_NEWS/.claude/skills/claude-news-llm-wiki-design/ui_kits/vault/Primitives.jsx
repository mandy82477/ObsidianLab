// Primitives — Wikilink, Callout, Frontmatter, MermaidPanel

function Wikilink({ to, children }) {
  return <a className="wikilink" href={"#" + to}>{children || to}</a>;
}

function Callout({ kind = "note", title, children }) {
  const icons = {
    note: "📝", info: "ℹ", warning: "⚠️", danger: "⛔", quote: "💬", success: "✅"
  };
  return (
    <div className={"callout callout--" + kind}>
      <div className="callout__title">
        <span>{icons[kind] || "📝"}</span>
        <span>{title}</span>
      </div>
      <div>{children}</div>
    </div>
  );
}

function Frontmatter({ rows }) {
  return (
    <div className="frontmatter">
      {rows.map(([k, v], i) => (
        <div key={i} className="frontmatter__row">
          <span className="frontmatter__k">{k}</span>
          <span className="frontmatter__v">{v}</span>
        </div>
      ))}
    </div>
  );
}

function MermaidPanel({ caption, children }) {
  return (
    <figure className="mermaid">
      <div className="mermaid__panel">{children}</div>
      {caption && <figcaption className="mermaid__caption">{caption}</figcaption>}
    </figure>
  );
}

function SourceLine({ source, time, sentiment }) {
  return (
    <div className="sourceline">
      <code>{source}</code>
      <span>·</span>
      <span>{time}</span>
      {sentiment && <><span>·</span><span style={{color:"var(--sentiment-" + sentiment.tone + ")"}}>情緒：{sentiment.label}</span></>}
    </div>
  );
}

Object.assign(window, { Wikilink, Callout, Frontmatter, MermaidPanel, SourceLine });
