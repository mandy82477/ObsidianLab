// CLAUDE NEWS · LLM-WIKI — app.js

(function () {
  'use strict';

  const $ = s => document.querySelector(s);
  const $$ = s => document.querySelectorAll(s);
  let rendered = { today: false, wiki: false, archive: false };

  // ── Theme toggle ────────────────────────────────────────────────────────────
  window.toggleTheme = function () {
    const root = document.documentElement;
    const next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    const btn = $('.nav__theme');
    if (btn) btn.textContent = next === 'dark' ? '☽' : '☀';
  };

  // ── Tab switch ──────────────────────────────────────────────────────────────
  window.switchView = function (id, btn) {
    $$('.view').forEach(v => v.classList.remove('is-active'));
    $$('.nav__link').forEach(l => l.classList.remove('is-active'));
    const view = $('#view-' + id);
    if (view) view.classList.add('is-active');
    if (btn && btn.classList) btn.classList.add('is-active');

    if (id === 'today'   && !rendered.today)   { renderLatestDigest(); rendered.today   = true; }
    if (id === 'wiki'    && !rendered.wiki)     { renderWiki();         rendered.wiki    = true; }
    if (id === 'archive' && !rendered.archive)  { renderArchive();      rendered.archive = true; }
  };

  // ── Helpers ─────────────────────────────────────────────────────────────────
  function esc(s) {
    if (s == null) return '';
    return String(s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  const MONTHS = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
  function dateParts(dateStr) {
    // "YYYY-MM-DD"
    const p = dateStr.split('-');
    return { y: p[0], m: MONTHS[parseInt(p[1],10)-1] || '', d: parseInt(p[2]||'0',10) };
  }

  const SENTIMENT_MAP = {
    '正面': ['positive', '😊 正面'],
    '負面': ['negative', '😤 負面'],
    '中性': ['neutral',  '😐 中性'],
    '褒貶不一': ['mixed', '🤔 褒貶不一'],
  };
  function sentimentHtml(raw) {
    if (!raw) return '';
    for (const [k, [cls, label]] of Object.entries(SENTIMENT_MAP)) {
      if (raw.includes(k)) return `<span class="sentiment sentiment--${cls}">${label}</span>`;
    }
    return `<span class="sentiment sentiment--neutral">${esc(raw)}</span>`;
  }

  const FOCUS_TAG_MAP = { '重大事件':'major','持續追蹤':'track','新工具':'tool','社群趨勢':'trend','風險警示':'risk' };
  function focusTagCls(tag) { return FOCUS_TAG_MAP[tag] || 'track'; }

  // strip （...） and (...) from status label for compact display
  function shortStatus(s) {
    return (s || '').replace(/[（(][^）)]*[）)]/g, '').trim();
  }

  // ── Story HTML ───────────────────────────────────────────────────────────────
  function storyHtml(s, star = false) {
    const cls = star ? 'story story--star' : 'story';
    return `<div class="${cls}">
  <div class="story__title"><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a></div>
  ${s.body ? `<div class="story__body">${esc(s.body)}</div>` : ''}
  <div class="sourceline">
    ${s.source ? `<code>${esc(s.source)}</code>` : ''}
    ${s.time   ? `<span>· ${esc(s.time)}</span>` : ''}
    ${sentimentHtml(s.sentiment)}
  </div>
</div>`;
  }

  // ── Render digest ────────────────────────────────────────────────────────────
  function renderDigest(d, container) {
    if (!d) { container.innerHTML = '<div style="padding:40px;text-align:center;color:var(--fg-3);font-family:var(--font-mono);font-size:12px">No digest data.</div>'; return; }

    const dp = dateParts(d.date);
    const parts = [];

    // header with day-badge
    const isLatest = Object.keys(window.DIGEST_ALL || {}).sort().reverse()[0] === d.date;
    parts.push(`<div class="feed__header">
  <div class="day-badge">
    <div class="day-badge__y">${esc(dp.y)}</div>
    <div class="day-badge__d">${dp.d}</div>
    <div class="day-badge__m">${dp.m}</div>
  </div>
  <div class="feed__meta">
    <h1>Claude Code &amp; Anthropic 每日新聞摘要</h1>
    <div class="feed__metarow">
      <span><b>${esc(d.date)}</b></span>
      <span class="sep">·</span>
      <span>來源 <b>${esc(d.sourceCount || '')}</b></span>
      <span class="sep">·</span>
      <span>文章 <b>${d.articleCount}</b> 則</span>
      <span class="sep">·</span>
      ${isLatest ? '<span class="pulse-dot">最新</span>' : ''}
    </div>
    <div class="feed__metarow" style="margin-top:4px">
      <span>更新時間 ${esc(d.generatedAt)}</span>
    </div>
  </div>
</div>`);

    // focus — rendered first (導讀)
    if (d.focus?.length) {
      parts.push(`<div class="section section--focus">
<div class="section__h" style="margin:0 0 0"><span class="emoji">📌</span> 今日聚焦</div>
<ul class="focus-list">`);
      d.focus.forEach(f => {
        const cls = focusTagCls(f.tag);
        parts.push(`<li class="focus-item"><span class="focus-tag focus-tag--${cls}">${esc(f.tag)}</span><span>${esc(f.text)}</span></li>`);
      });
      parts.push('</ul></div>');
    }

    // sections
    const sections = [
      { key: 'topStories',  emoji: '⭐', label: '重點話題',   star: true  },
      { key: 'techUpdates', emoji: '🔧', label: '技術更新',   star: false },
      { key: 'discussions', emoji: '💬', label: '技術熱度討論', star: false },
      { key: 'billing',     emoji: '💰', label: '付費方案動態', star: false },
    ];

    sections.forEach(({ key, emoji, label, star }) => {
      if (!d[key]?.length) return;
      parts.push(`<div class="section">
<div class="section__h"><span class="emoji">${emoji}</span> ${label}</div>`);
      d[key].forEach(s => parts.push(storyHtml(s, star)));
      parts.push('</div>');
    });

    // source status grid
    if (d.sourceStatus?.length) {
      parts.push(`<div class="sourcetable">
<div class="sourcetable__title">來源狀態</div>
<div class="sourcetable__grid">`);
      d.sourceStatus.forEach(s => {
        parts.push(`<div class="source-cell">
  <span class="source-cell__name">${esc(s.name)}</span>
  <span class="source-cell__status">${s.ok ? '✅' : '❌'}</span>
  <span class="source-cell__count">${s.count} 篇</span>
</div>`);
      });
      parts.push('</div><div class="sourcetable__note">Twitter/X 資料不包含在本摘要中（官方 API 需付費）</div></div>');
    }

    container.innerHTML = parts.join('\n');
  }

  // ── Latest digest ────────────────────────────────────────────────────────────
  function renderLatestDigest() {
    const container = $('#digest-content');
    if (!container) return;
    const all = window.DIGEST_ALL || {};
    const dates = Object.keys(all).sort().reverse();
    if (!dates.length) { container.innerHTML = ''; return; }
    renderDigest(all[dates[0]], container);
  }

  // ── Open digest in modal (archive) ──────────────────────────────────────────
  window.openDigestModal = function (date) {
    const d = (window.DIGEST_ALL || {})[date];
    if (!d) return;

    const inner = $('#wiki-modal-inner');
    inner.innerHTML = `
<button class="modal__close" onclick="closeModal()">✕</button>
<div id="digest-modal-feed"></div>`;

    renderDigest(d, $('#digest-modal-feed'));

    const scrim = $('#modal-scrim');
    scrim.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  };

  // ── Wiki ─────────────────────────────────────────────────────────────────────
  function renderWiki() {
    const data = window.WIKI_DATA || { entities: [], topics: [] };
    const eContainer = $('#wiki-entities');
    const tContainer = $('#wiki-topics');
    const totalPages = (data.entities?.length || 0) + (data.topics?.length || 0);
    const today = new Date().toISOString().slice(0, 10);

    // sub-header
    const subEl = $('#wiki-sub');
    if (subEl) subEl.textContent = `最後更新：${today} · 頁面數：${totalPages} · 點擊實體查看詳細頁面`;

    if (eContainer && data.entities?.length) {
      eContainer.innerHTML = data.entities.map(e => `
<div class="entity-row" onclick="openWikiModal('${esc(e.id)}','entity')">
  <div class="entity-row__name"><span class="bracket">[[</span>${esc(e.id)}<span class="bracket">]]</span></div>
  <div class="entity-row__type">${esc(e.entityType)}</div>
  <div><span class="pill pill--${e.pill}">${esc(shortStatus(e.status))}</span></div>
  <div class="entity-row__summary" title="${esc(e.summary)}">${esc(e.summary)}</div>
  <div class="entity-row__updated">${esc(e.lastUpdated || e.firstSeen || '')}</div>
</div>`).join('');
    }

    if (tContainer && data.topics?.length) {
      tContainer.innerHTML = data.topics.map(t => `
<div class="entity-row entity-row--topic" onclick="openWikiModal('${esc(t.id)}','topic')">
  <div class="entity-row__name"><span class="bracket">[[</span>${esc(t.id)}<span class="bracket">]]</span></div>
  <div><span class="pill pill--${t.pill}">${esc(shortStatus(t.status))}</span></div>
  <div class="entity-row__summary" title="${esc(t.summary)}">${esc(t.summary)}</div>
  <div class="entity-row__updated">${esc(t.lastUpdated || t.startDate || '')}</div>
</div>`).join('');
    }
  }

  // ── Archive ──────────────────────────────────────────────────────────────────
  function renderArchive() {
    const container = $('#archive-grid');
    if (!container) return;
    const index = (window.WIKI_DATA || {}).digestIndex || [];
    if (!index.length) { container.innerHTML = ''; return; }

    const dates = index.map(d => d.date).sort().reverse();
    const subEl = $('#archive-sub');
    if (subEl && dates.length) subEl.textContent = `${dates.length} 份日報 · ${dates[dates.length-1]} → ${dates[0]}`;

    container.innerHTML = index.map((d, i) => {
      const isLatest = i === 0;
      const cls = 'archive-card' + (isLatest ? ' archive-card--latest' : '');
      const dateLabel = isLatest ? `${esc(d.date)} · 最新` : esc(d.date);
      return `<div class="${cls}" onclick="openDigestModal('${esc(d.date)}')">
  <div class="archive-card__date">${dateLabel}</div>
  <div class="archive-card__title">${esc(d.preview)}</div>
  <div class="archive-card__meta"><span>${d.articleCount} 篇</span><span>⭐ ${d.topCount}</span></div>
</div>`;
    }).join('');
  }

  // ── Wiki modal ────────────────────────────────────────────────────────────────
  window.openWikiModal = function (id, type) {
    const data = window.WIKI_DATA || {};
    const list = type === 'entity' ? data.entities : data.topics;
    const item = (list || []).find(x => x.id === id);
    if (!item) return;

    // strip H1 title + front-matter metadata block (up to first --- or first ##)
    let md = (item.markdown || '');
    // remove H1
    md = md.replace(/^#[^#][^\n]*\n/, '');
    // remove leading metadata lines (**key：** value) and blank lines before first section
    md = md.replace(/^(\s*\*\*[^*]+[：:]\*\*[^\n]*\n|\s*\n)*/m, '');

    // render markdown to HTML
    let bodyHtml;
    if (typeof marked !== 'undefined') {
      // convert [[wikilink]] → wikilink span
      md = md.replace(/\[\[([^\]]+)\]\]/g, (_, p) =>
        `<WIKILINK>${p}</WIKILINK>`
      );
      bodyHtml = marked.parse(md);
      // post-process wikilinks
      bodyHtml = bodyHtml.replace(/<WIKILINK>([^<]+)<\/WIKILINK>/g, (_, p) =>
        `<span class="modal__wikilink">${esc(p)}</span>`
      );
    } else {
      bodyHtml = `<pre style="white-space:pre-wrap;font-size:12px">${esc(md)}</pre>`;
    }

    // split into sections (## headings) for the modal layout
    // We render the whole body inside modal__body, let CSS style it via .modal__body h2/h3
    const metaRows = [];
    if (item.entityType) metaRows.push({ label: '類型', val: item.entityType });
    if (item.status)     metaRows.push({ label: '狀態', val: item.status });
    if (item.firstSeen)  metaRows.push({ label: '首次出現', val: item.firstSeen });
    if (item.startDate)  metaRows.push({ label: '開始日期', val: item.startDate });
    if (item.lastUpdated)metaRows.push({ label: '最後更新', val: item.lastUpdated });

    const metaHtml = metaRows.map(r =>
      `<div class="modal__meta-row"><span class="modal__meta-label">${esc(r.label)}</span><span>${esc(r.val)}</span></div>`
    ).join('');

    const typeLabel = type === 'entity' ? '實體' : '議題';

    $('#wiki-modal-inner').innerHTML = `
<button class="modal__close" onclick="closeModal()">✕</button>
<div class="modal__type-row">
  <span class="pill pill--${item.pill}">${esc(item.status)}</span>
  <span class="pill pill--gray">${esc(item.entityType || typeLabel)}</span>
</div>
<div class="modal__h1">${esc(item.name)}</div>
${metaRows.length ? `<div class="modal__meta">${metaHtml}</div>` : ''}
<div class="modal__body">${bodyHtml}</div>`;

    const scrim = $('#modal-scrim');
    scrim.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  };

  window.closeModal = function () {
    $('#modal-scrim').classList.remove('is-open');
    document.body.style.overflow = '';
  };

  // ── Init ─────────────────────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', () => {
    // close modal on scrim click
    const scrim = $('#modal-scrim');
    if (scrim) scrim.addEventListener('click', e => { if (e.target === scrim) closeModal(); });

    // keyboard shortcuts
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeModal();
      if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {
        e.preventDefault();
        // future: focus search
      }
    });

    // marked.js config
    if (typeof marked !== 'undefined') {
      marked.setOptions({ breaks: true, gfm: true });
    }

    // render today on load
    renderLatestDigest();
    rendered.today = true;
  });

})();
