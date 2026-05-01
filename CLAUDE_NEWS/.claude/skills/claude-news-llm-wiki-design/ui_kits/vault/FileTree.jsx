// FileTree.jsx — left sidebar
const { useState: useStateFT } = React;

function FileTree({ activeFile, onSelect }) {
  const [open, setOpen] = useStateFT({ news: true, wiki: true, entities: true, topics: true, src: false });
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
        <button className="iconbtn iconbtn--sm">
          <img src="https://unpkg.com/lucide-static@latest/icons/file-plus.svg" />
        </button>
      </div>
      <div className="filetree__tree">
        <Row depth={0} kind="folder" name="news" file="news" count={6} />
        {open.news && <>
          <Row depth={1} kind="file" name="2026-04-30.md" file="news/2026-04-30.md" />
          <Row depth={1} kind="file" name="2026-04-29.md" file="news/2026-04-29.md" />
          <Row depth={1} kind="file" name="2026-04-28.md" file="news/2026-04-28.md" />
          <Row depth={1} kind="file" name="2026-04-27.md" file="news/2026-04-27.md" />
          <Row depth={1} kind="file" name="2026-04-26.md" file="news/2026-04-26.md" />
          <Row depth={1} kind="file" name="2026-04-25.md" file="news/2026-04-25.md" />
        </>}
        <Row depth={0} kind="folder" name="wiki" file="wiki" />
        {open.wiki && <>
          <Row depth={1} kind="file" name="index.md" file="wiki/index.md" />
          <Row depth={1} kind="file" name="overview.md" file="wiki/overview.md" />
          <Row depth={1} kind="file" name="log.md" file="wiki/log.md" />
          <Row depth={1} kind="folder" name="entities" file="entities" count={7} />
          {open.entities && <>
            <Row depth={2} kind="file" name="claude-code.md" file="wiki/entities/claude-code.md" />
            <Row depth={2} kind="file" name="opus-4-7.md" file="wiki/entities/opus-4-7.md" />
            <Row depth={2} kind="file" name="mythos.md" file="wiki/entities/mythos.md" />
            <Row depth={2} kind="file" name="pricing.md" file="wiki/entities/pricing.md" />
            <Row depth={2} kind="file" name="bugcrawl.md" file="wiki/entities/bugcrawl.md" />
            <Row depth={2} kind="file" name="claude-design.md" file="wiki/entities/claude-design.md" />
            <Row depth={2} kind="file" name="project-deal.md" file="wiki/entities/project-deal.md" />
          </>}
          <Row depth={1} kind="folder" name="topics" file="topics" count={4} />
          {open.topics && <>
            <Row depth={2} kind="file" name="code-quality-decline.md" />
            <Row depth={2} kind="file" name="competitor-landscape.md" />
            <Row depth={2} kind="file" name="community-tech-patterns.md" />
            <Row depth={2} kind="file" name="google-investment.md" />
          </>}
        </>}
        <Row depth={0} kind="folder" name="src" file="src" />
        <Row depth={0} kind="file" name="CLAUDE.md" file="CLAUDE.md" />
        <Row depth={0} kind="file" name="README.md" file="README.md" />
      </div>
    </div>
  );
}

window.FileTree = FileTree;
