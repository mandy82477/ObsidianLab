# Claude News Wiki — Design System

A design system for **CLAUDE_NEWS LLM-WIKI**, an Obsidian-vault–based AI news aggregator that scrapes Claude/Anthropic coverage every 24 hours, runs an LLM filter + summarizer pipeline, and rolls findings into a hand-curated wiki of entities and topics.

This system codifies the visual + content language of that vault: a dark, dense, monospace-flavored "researcher's notebook" aesthetic crossed with Anthropic-adjacent warm accents, designed for long-form Markdown reading at desk-density.

---

## Source Material

| Source | Where | Notes |
|---|---|---|
| `mandy82477/ObsidianLab` (GitHub) | `https://github.com/mandy82477/ObsidianLab` | The vault itself. Branch `master`. CLAUDE_NEWS lives under `CLAUDE_NEWS/`. |
| News digests | `CLAUDE_NEWS/news/YYYY-MM-DD.md` | Daily auto-generated digests (Traditional Chinese). |
| Wiki entities | `CLAUDE_NEWS/wiki/entities/*.md` | Persistent pages for models, products, features, people. |
| Wiki topics | `CLAUDE_NEWS/wiki/topics/*.md` | Cross-day ongoing issues. |
| Pipeline architecture | `CLAUDE_NEWS/src/DesignDocument/Design Diagram.md` | Mermaid flowcharts of the aggregator + ingest pipeline. |
| Operator docs | `CLAUDE_NEWS/CLAUDE.md` | Internal LLM-facing guide; has the canonical schema. |

A trimmed mirror of the most relevant files lives under `source/CLAUDE_NEWS/` in this project for reference; we don't assume the reader has access to the original repo.

---

## What this system covers

The product has **two surfaces**, both Markdown-driven:

1. **Obsidian Vault** — how a daily reader experiences the wiki: notes, callouts, wikilinks, Mermaid diagrams, the daily news digest.
2. **Web Reader** — a public, browser-friendly rendering of the same Markdown corpus (digest archive + wiki entities/topics, with search and a "today" feed).

Decks are not a primary surface; the design system covers Type, Color, Spacing, Components, and a small set of Brand assets.

---

## Index

```
README.md                  ← you are here
SKILL.md                   ← agent skill manifest (Claude Code compatible)
colors_and_type.css        ← all CSS variables + base type rules
fonts/                     ← webfonts (or substitution notes)
assets/                    ← logos, icons, callout glyphs, sample imagery
preview/                   ← design system preview cards (Design System tab)
ui_kits/
  vault/                   ← Obsidian vault recreation (entity page, daily digest, graph)
  web_reader/              ← Public web reader recreation (today feed, entity, search)
source/CLAUDE_NEWS/        ← imported source files for reference
```

---

## CONTENT FUNDAMENTALS

The wiki is written in **Traditional Chinese** with English technical terms left untranslated. Tone is that of an internal research analyst writing for other engineers — informative, terse, occasionally dry, never marketing-y.

### Voice

- **Third-person observational.** Almost never "you" or "we." The wiki narrates: *"Anthropic 正處於快速擴張與品質爭議並存的關鍵節點"* ("Anthropic is at a critical juncture of rapid expansion alongside quality controversy"). The reader is a peer researcher, not a customer.
- **Source-cited.** Every claim attaches a source line (`Hacker News · 04/30 14:36 UTC`, `Reddit / r/ClaudeAI`). Confidence is signaled — `> ⚠️ 待確認` ("pending confirmation") sits next to unverified items.
- **Non-promotional.** When Anthropic announces a product, the wiki summarizes capability and immediately notes community reaction, including negative. *"Opus 4.7 可以用一個改變來拯救"* ("Opus 4.7 could be saved by one change") is a real pull-quote.

### Casing & punctuation

- **English brand names keep their casing.** Anthropic, Claude Code, Opus, Mythos, Bugcrawl, MCP, Hooks, Skills. Never "claude code," never "Claude-Code."
- **CJK + Latin spacing:** a half-space implied between scripts (the vault relies on the renderer; in CSS we honor it via `text-spacing-trim: trim-start`).
- **No Oxford comma in English fragments;** lists in CJK use `、` not `,`.
- **Sentence-case headings** in English; CJK headings are unstyled (no all-caps equivalent exists).

### Emoji — used as semantic anchors, not decoration

The corpus uses a small, fixed emoji set with **specific meanings.** Do not invent new ones.

| Emoji | Meaning | Where it appears |
|---|---|---|
| ⭐ | Top story / pinned | Daily digest "重點話題" header |
| 🔧 | Technical update | Daily digest section header |
| 💬 | Community discussion | Daily digest section header |
| 💰 | Pricing / billing news | Daily digest section header |
| 📌 | Today's focus / takeaways | End-of-digest summary |
| ✅ | Source succeeded / verified | Source status table |
| ⚠️ | Caution / unverified | Inline next to claims awaiting confirmation |
| ⛔ | Stopped / failed | Pipeline diagrams |
| 🔥 | High discussion heat | Sentiment indicators in overview |
| 📈 | Trending up | Activity indicators |
| 🔒 | Restricted access | Mythos and similar |
| 😊 😐 😤 🤔 | Sentiment tags on posts | Reddit/HN items in 💬 section |

Outside this set, **no decorative emoji.** No 🚀 launches, no 🎉 celebrations, no 💡 tips.

### Specific examples

- A digest item: *"⭐ **[Claude Code refuses requests if your commits mention 'OpenClaw'](url)** — Claude Code 被發現存在異常行為：若 Git 提交訊息中含有特定 JSON 格式的 'OpenClaw' 字串，工具會直接拒絕請求…"* — observation, mechanism, evidence, source line.
- A wiki entity: *"**類型：** product / **狀態：** active / **首次出現：** 2025（正式推出） / **最後更新：** 2026-04-27"* — frontmatter-style metadata block at the top of every entity page.
- Wikilinks: `[[entities/claude-code]]`, `[[news/2026-04-25]]`. We render these as inline tags with a leading `[[` glyph.

---

## VISUAL FOUNDATIONS

The vault is a researcher's terminal with markdown rendering on top. The web reader inherits that personality. **Dark by default**, paper light theme available, but every preview in this system is dark-first.

### Color

- **Backgrounds:** deep neutral with a slight blue undertone (`#1e1e2e` base). Two surface tints above it for cards and elevated panels. No pure black.
- **Foreground:** off-white at 92% lightness; secondary text drops to ~62%. Tertiary (timestamps, source captions) sits at ~42%.
- **Brand accent:** an Obsidian-purple (`#7C6CDC`) used for wikilinks, focused state, and the dot in the logo. Used **sparingly** — in long-form reading it appears once or twice per screen.
- **Warm accent:** Claude/Anthropic-flavored tan (`#D4A574`), reserved for the ⭐ "重點話題" rail and the day's headline number in the digest.
- **Semantic:** four states — info (cyan-blue), success (green), warn (amber), danger (red). Each appears as a callout left-border + icon, never as a full background fill on body content.
- **Light theme** mirrors the same hue relationships on a paper background (`#FAF7F0`, slightly warm).

### Type

- **Display / headings:** `Inter Tight` (variable, weights 500–700). Tight tracking, the "engineering doc" feel rather than editorial.
- **Body:** `Inter` regular for English; **`Noto Sans TC`** for Traditional Chinese — both metric-compatible at the same x-height, so mixed-script paragraphs don't bobble.
- **Mono:** `JetBrains Mono` — used for code, file paths, wikilinks, key/value frontmatter, and the `[[ ]]` link glyphs.
- **Scale:** modular, base 16, 1.2 step. H1 28 / H2 22 / H3 18 / body 16 / small 14 / micro 12. Line-height generous (1.6 on body, 1.3 on headings).

### Spacing

- 4px grid. Tokens: `--space-0.5` (2) through `--space-12` (96). Most common values: 8, 12, 16, 24.
- Section padding inside cards: 16/20. Between list items in a digest: 12. Between digest sections: 32.

### Backgrounds, imagery, surfaces

- **No hero imagery.** The product is text. Surface is flat dark, sometimes a 1px hairline border (`#2A2B3D`).
- **Cards** use a 1px hairline border with a 2-tone subtle gradient surface (top edge marginally lighter), `border-radius: 8px`. A faint inner highlight on the top edge (1px, `rgba(255,255,255,0.04)`).
- **Callouts** (info / note / warning / quote) — the Obsidian native style: 4px left border in the semantic color, soft tinted background (~6% alpha of the same color), title row with an icon and label. We replicate this exactly.
- **Mermaid diagrams** render on a 1-shade-darker panel inset in the page body, padded 24px, captioned beneath in mono.

### Animation

- Almost none. This is a research wiki, not a marketing site.
- Hover: 100ms `cubic-bezier(0.2, 0, 0.2, 1)` opacity + background tint. No transforms, no shadows.
- Page transitions: instant. Wiki nav is internal anchors, not animated views.
- The one exception: the daily digest "freshness pulse" — a 1px ring on the day badge breathing at 2s intervals when the page was generated within the last 6 hours. Subtle.

### Hover & press states

- **Links (wikilinks + external):** purple at rest, brighter purple on hover, plus a 1px underline that fades in. `text-decoration-thickness: 1px; text-underline-offset: 3px`.
- **Buttons:** primary hovers slightly lighter (+4% L); presses slightly darker (-4% L), no scale.
- **List rows:** hover applies a 4% white background; active row has the purple left-rail.
- **Tags / chips:** hover increases border opacity, no background change.

### Borders, radii, shadows

- **Borders:** 1px hairlines, `rgba(255,255,255,0.06)` on dark, `rgba(0,0,0,0.08)` on light. Two-tone borders only on the day badge.
- **Radii:** 4 (chips, tags), 6 (inputs, buttons), 8 (cards), 12 (modals), full (avatars only).
- **Shadows:** essentially none on dark surfaces. Light theme uses one soft elevation: `0 1px 2px rgba(20, 14, 4, 0.06), 0 4px 12px rgba(20, 14, 4, 0.04)`. We **never** stack multiple shadows.

### Transparency / blur

- The top nav uses `backdrop-filter: blur(12px)` over an 80%-alpha background.
- Modals: 60% alpha scrim, no blur on the body — keeps focus on the modal without softening reading state.
- Otherwise opaque. No frosted cards, no translucent backgrounds inside content.

### Layout

- Desktop reader: max-width **720px** for body prose, **920px** when a sidebar TOC is shown, **1200px** for the index/today views. The vault feel is single-column reading.
- Three-pane vault recreation: left file tree (240) / main editor (flex) / right backlinks (260).
- Sticky top nav (56px), no sticky footer.
- Daily digest uses a **single column** with section anchors listed in the TOC, never a card grid.

### Imagery vibe

- The corpus has no photography. Pasted screenshots, when they appear, are kept at native resolution on a 1-shade-darker panel with a 1px border. No filter. No grain.
- Logos for sources (HN, Reddit, GitHub) appear as 14px monochrome glyphs at 70% opacity in source captions.

### Cards

- 1px hairline border (no shadow).
- 8px radius.
- 16–20px internal padding.
- Optional 1px inner top highlight at 4% white.
- Title row: 14–16px, weight 600. Body: 14–15px secondary.
- Hover: border brightens to 12% white. No translate, no scale.

---

## ICONOGRAPHY

The vault itself has no custom icon font. Icons appear in three forms:

1. **Emoji** — used semantically (see CONTENT FUNDAMENTALS above). Treated as iconography, not decoration.
2. **Lucide icons** — chosen as the substitution for UI affordances (chevrons, search, settings, file, link, external-link). Stroke-based, 1.5px weight, 16/20/24 sizes. Linked from CDN: `https://unpkg.com/lucide-static@latest/icons/{name}.svg`.
3. **Source glyphs** — small monochrome marks for HN, Reddit, GitHub, Anthropic Blog, Google News. We render these as inline SVGs in `assets/source-glyphs/`.

### Rules

- **No multi-color icons.** Stroke-only, currentColor.
- **No filled icons** except the day-badge ring and the ⭐ pin glyph (which is the emoji at 1.1em).
- **Emoji are not substituted with icons** in body content — `⚠️` next to a wiki claim is part of the voice. In UI chrome (buttons, nav), use Lucide.
- **Substitution flagged:** Lucide is our pragmatic choice; the original vault renders Obsidian's built-in stroke icons via its theme. Visually they're nearly identical (Lucide is the open ancestor of Obsidian's set), but the user should know.

See `preview/iconography.html` for the full registry.

---

## SUBSTITUTIONS & FLAGS FOR THE USER

> ⚠️ **Read this section.** Several pieces of this system are best-effort substitutions because the source vault doesn't ship its own brand assets.

| What | Substitution | Why |
|---|---|---|
| **Logo** | Hand-set wordmark "CLAUDE NEWS / WIKI" in Inter Tight 700 + JetBrains Mono, with a small purple bracket dot. | The repo has no logo. Provide one, or approve this. |
| **Body fonts** | Inter (Latin), Noto Sans TC (CJK), JetBrains Mono — all from Google Fonts. | The vault uses the reader's local Obsidian theme; no font files are shipped. These are the closest open metrics-matched stand-ins. |
| **Icons** | Lucide via CDN. | Obsidian's icons are bundled with the app, not the vault. Lucide is the open precursor — visually equivalent for our needs. |
| **Imagery** | None included. | Source has no photography or illustration. We deliberately don't generate any. |
| **Source glyphs** | Hand-drawn SVG approximations of HN/Reddit/GitHub/etc. | Each platform's logo is trademarked; these are recognizable but unofficial outlines used at 14px. |

**Iterate with me on:** logo direction, whether to commit the Inter / Noto / JetBrains font files into `fonts/` or stay on Google Fonts CDN, and whether the warm Claude tan should appear more or less in the system.
