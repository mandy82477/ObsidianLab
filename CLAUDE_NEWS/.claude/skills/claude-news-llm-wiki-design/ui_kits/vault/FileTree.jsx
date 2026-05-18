// FileTree.jsx — left sidebar — synced to CLAUDE_NEWS @ 2026-05-17
const { useState: useStateFT } = React;

const NEWS_DAYS = [
  "2026-05-17", "2026-05-16", "2026-05-15", "2026-05-14", "2026-05-13",
  "2026-05-12", "2026-05-11", "2026-05-10", "2026-05-09", "2026-05-08",
  "2026-05-07", "2026-05-06", "2026-05-05", "2026-05-04", "2026-05-03",
  "2026-05-02",
  "2026-04-30", "2026-04-29", "2026-04-28", "2026-04-27", "2026-04-26", "2026-04-25",
];

const ENTITIES = [
  "claude-code", "opus-4-7", "pricing", "mythos",
  "managed-agents", "claude-security", "openclaw",
  "google-investment", "bugcrawl", "claude-design",
  "project-deal", "boris-cherny", "cat-wu",
];

const TOPICS = [
  "official-community-gap",
  "code-quality-decline",
  "ai-agent-safety",
  "anthropic-government-policy",
  "competitor-landscape",
  "community-tech-tools",
  "community-tech-patterns",
  "community-tech-discussions",
  "google-investment",
];

function FileTree({ activeFile, onSelect }) {
  const [open, setOpen] = useStateFT({
    news: true, wiki: true, entities: true, topics: false, src: false,
  });
  const toggle = (k) => setOpen({ ...open, [k]: !open[k] });

  const Row = ({ depth, kind, name, file, count }) => {
    const active = file === activeFile;
    return (
      <div className={"ft__row" + (active ? " ft__row--active" : "")}
           style={{ paddingLeft: 8 + depth * 14 }}
           onClick={() => file && onSelect(file)}>
        {kind === "folder" ? (
          <span className="ft__caret" onClick={(e) => { e.stopPropagation(); toggle(file || name); }}>
            {open[file || name] ? "▾" : "▸"}
          </span>
        ) : <span className="ft__caret" />}
        <span className="ft__icon">
          {kind === "folder"
            ? <img src="https://unpkg.com/lucide-static@latest/icons/folder.svg" />
            : <img src="https://unpkg.com/lucide-static@latest/icons/file-text.svg" />}
        </span>
        <span className="ft__name">{name}</span>
        {count != null && <span className="ft__count">{count}</span>}
      </div>
    );
  };

  return (
    <div className="filetree">
      <div className="filetree__head">
        <span className="ft__sectiontitle">CLAUDE_NEWS</span>
        <button className="iconbtn iconbtn--sm" title="new file">
          <img src="https://unpkg.com/lucide-static@latest/icons/file-plus.svg" />
        </button>
      </div>
      <div className="filetree__tree">

        {/* news/ */}
        <Row depth={0} kind="folder" name="news" file="news" count={NEWS_DAYS.length} />
        {open.news && NEWS_DAYS.map(d => (
          <Row key={d} depth={1} kind="file" name={d + ".md"} file={"news/" + d + ".md"} />
        ))}

        {/* wiki/ */}
        <Row depth={0} kind="folder" name="wiki" file="wiki" />
        {open.wiki && <>
          <Row depth={1} kind="file" name="index.md"         file="wiki/index.md" />
          <Row depth={1} kind="file" name="overview.md"      file="wiki/overview.md" />
          <Row depth={1} kind="file" name="feature-radar.md" file="wiki/feature-radar.md" />
          <Row depth={1} kind="file" name="log.md"           file="wiki/log.md" />

          <Row depth={1} kind="folder" name="entities" file="entities" count={ENTITIES.length} />
          {open.entities && ENTITIES.map(name => (
            <Row key={name} depth={2} kind="file" name={name + ".md"} file={"wiki/entities/" + name + ".md"} />
          ))}

          <Row depth={1} kind="folder" name="topics" file="topics" count={TOPICS.length} />
          {open.topics && TOPICS.map(name => (
            <Row key={name} depth={2} kind="file" name={name + ".md"} file={"wiki/topics/" + name + ".md"} />
          ))}
        </>}

        <Row depth={0} kind="folder" name="src" file="src" />
        <Row depth={0} kind="file" name="CLAUDE.md" file="CLAUDE.md" />
        <Row depth={0} kind="file" name="README.md" file="README.md" />
      </div>
    </div>
  );
}

window.FileTree = FileTree;
