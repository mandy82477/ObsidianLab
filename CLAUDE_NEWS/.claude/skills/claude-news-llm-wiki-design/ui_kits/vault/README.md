# UI Kit — Obsidian Vault

A pixel-leaning recreation of how the **CLAUDE_NEWS LLM-WIKI** appears inside Obsidian: three-pane layout (file tree / editor / backlinks), Markdown rendered with native callouts, wikilinks, frontmatter-style metadata, and a Mermaid diagram inset.

## Files
- `index.html` — the live vault recreation (entity page open by default)
- `VaultShell.jsx` — three-pane shell with title bar
- `FileTree.jsx` — left sidebar
- `EditorPane.jsx` — center reading view
- `BacklinksPane.jsx` — right "Linked mentions"
- `Callout.jsx` / `Wikilink.jsx` / `Frontmatter.jsx` / `MermaidPanel.jsx` — primitives
