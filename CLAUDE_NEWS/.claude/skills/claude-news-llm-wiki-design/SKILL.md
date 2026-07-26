---
name: claude-news-llm-wiki-design
description: Use this skill to generate well-branded interfaces and assets for CLAUDE NEWS · LLM-WIKI, an automated Claude/Anthropic news aggregator and knowledge graph built on Obsidian-style Markdown vaults. Either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.
If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.
If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## Quick reference

- **Brand:** CLAUDE NEWS · LLM-WIKI — informative, technical, automated daily digest of Claude/Anthropic news, plus a wiki-style entity graph.
- **Voice:** documentary, terse, source-cited. CJK + English mixed prose. Mono for metadata, serif for prose.
- **Colors:** paper/sumi editorial, light-first (`--bg-0: #F7F4ED` warm bone paper; sumi ink ladder `#1A1814` → `#B8B2A4`); **single ochre accent** (`--ochre-9: #8E5F3D`), hairline ink-tinted borders. Dark theme via `data-theme` token swap. No second accent hue. *(Updated 2026-07-26 — the previous quick-ref described the pre-redesign dark/purple system and contradicted both `colors_and_type.css` and the deployed site; the token file is authoritative.)*
- **Type:** Cormorant Garamond + Noto Serif (display/long prose), Inter + Noto Sans TC (UI), JetBrains Mono (metadata, code, sourcelines). Scale in `colors_and_type.css` (`--fs-micro` 12 → `--fs-monumental` 96).
- **Iconography:** Lucide via CDN (`https://unpkg.com/lucide-static@latest/icons/<name>.svg`). Sparingly. Repo's own brand glyph in `assets/logo.svg`.
- **Surfaces:**
  - `ui_kits/vault/` — Obsidian-style three-pane editor for the curator
  - `ui_kits/web_reader/` — public daily digest + wiki for readers
- **Tokens:** `colors_and_type.css` at root.
- **Don'ts:** no emoji as icons (the digest *content* uses ⭐💬💰🔧📌 as section markers — that's fine, leave them in copy). No bluish-purple gradients. No rounded-corner-with-left-color-stripe cards. No invented illustrations — use placeholders if missing.
