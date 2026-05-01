// VaultShell.jsx — three-pane Obsidian-style window
const { useState } = React;

function VaultShell({ children, activeFile = "wiki/entities/claude-code.md" }) {
  return (
    <div className="vault">
      <div className="vault__titlebar">
        <div className="vault__traffic">
          <span style={{background:"#FF5F57"}}/>
          <span style={{background:"#FEBC2E"}}/>
          <span style={{background:"#28C840"}}/>
        </div>
        <div className="vault__title">
          <span className="vault__crumbs">
            <span style={{color:"var(--fg-3)"}}>CLAUDE_NEWS</span>
            <span style={{color:"var(--fg-4)"}}> / </span>
            <span>{activeFile}</span>
          </span>
        </div>
        <div className="vault__chrome">
          <button className="iconbtn" title="Graph">
            <img src="https://unpkg.com/lucide-static@latest/icons/git-branch.svg" />
          </button>
          <button className="iconbtn" title="Search">
            <img src="https://unpkg.com/lucide-static@latest/icons/search.svg" />
          </button>
          <button className="iconbtn" title="Settings">
            <img src="https://unpkg.com/lucide-static@latest/icons/settings.svg" />
          </button>
        </div>
      </div>
      <div className="vault__body">{children}</div>
      <div className="vault__statusbar">
        <span><b>Vault:</b> CLAUDE_NEWS</span>
        <span style={{marginLeft:"auto"}}><b>Auto-push:</b> ✅ on</span>
        <span><b>Last ingest:</b> 2026-04-30 08:00</span>
        <span><b>13</b> entities · <b>4</b> topics · <b>52</b> news</span>
      </div>
    </div>
  );
}

window.VaultShell = VaultShell;
