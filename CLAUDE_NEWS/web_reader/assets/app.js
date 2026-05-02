// CLAUDE NEWS · LLM-WIKI — app.js

(function () {
  'use strict';

  const $ = s => document.querySelector(s);
  const $$ = s => document.querySelectorAll(s);
  let rendered = { today: false, wiki: false, archive: false };
  let detailReturnView = 'wiki';

  // ── Sort state ───────────────────────────────────────────────────────────────
  let entitySort = { key: 'lastUpdated', dir: 'desc' };
  let topicSort  = { key: 'lastUpdated', dir: 'desc' };

  const ENTITY_SORT_OPTIONS = [
    { key: 'lastUpdated', label: '最新更新' },
    { key: 'name',        label: '名稱' },
    { key: 'entityType',  label: '類型' },
    { key: 'status',      label: '狀態' },
  ];
  const TOPIC_SORT_OPTIONS = [
    { key: 'lastUpdated', label: '最新更新' },
    { key: 'name',        label: '名稱' },
    { key: 'startDate',   label: '開始日期' },
    { key: 'status',      label: '狀態' },
  ];

  // Status sort priority (lower = higher priority / shown first in desc)
  const STATUS_PRIORITY = { active:0, ongoing:0, '公開測試版':1, monitoring:1, warn:2, '秘密開發中':2, '測試中（未公開）':2, rumoured:3, resolved:4, deprecated:5 };
  function statusPriority(s) {
    const k = (s || '').toLowerCase().trim();
    for (const [pat, v] of Object.entries(STATUS_PRIORITY)) {
      if (k.includes(pat.toLowerCase())) return v;
    }
    return 3;
  }

  function sortItems(items, key, dir) {
    return [...items].sort((a, b) => {
      let av, bv;
      if (key === 'status') {
        av = statusPriority(a.status);
        bv = statusPriority(b.status);
      } else {
        av = (a[key] || '').toLowerCase();
        bv = (b[key] || '').toLowerCase();
      }
      const cmp = av < bv ? -1 : av > bv ? 1 : 0;
      // date fields default desc; missing dates sort to end
      const emptyLast = (!a[key] ? 1 : 0) - (!b[key] ? 1 : 0);
      if (emptyLast !== 0) return emptyLast;
      return dir === 'asc' ? cmp : -cmp;
    });
  }

  function buildSortBar(containerId, options, state, onSort) {
    const bar = $('#' + containerId);
    if (!bar) return;
    bar.innerHTML = `<span class="sort-bar__label">排序</span>` +
      options.map(({ key, label }) => {
        const active = state.key === key;
        const arrow  = active ? (state.dir === 'desc' ? ' ↓' : ' ↑') : '';
        return `<button class="sort-btn${active ? ' is-active' : ''}" onclick="${onSort}('${key}')">${label}${active ? `<span class="sort-btn__arrow">${arrow}</span>` : ''}</button>`;
      }).join('');
  }

  window.setSortEntity = function (key) {
    if (entitySort.key === key) {
      entitySort.dir = entitySort.dir === 'desc' ? 'asc' : 'desc';
    } else {
      entitySort.key = key;
      entitySort.dir = (key === 'lastUpdated') ? 'desc' : 'asc';
    }
    buildSortBar('sort-bar-entity', ENTITY_SORT_OPTIONS, entitySort, 'setSortEntity');
    renderEntityRows();
  };

  window.setSortTopic = function (key) {
    if (topicSort.key === key) {
      topicSort.dir = topicSort.dir === 'desc' ? 'asc' : 'desc';
    } else {
      topicSort.key = key;
      topicSort.dir = (key === 'lastUpdated' || key === 'startDate') ? 'desc' : 'asc';
    }
    buildSortBar('sort-bar-topic', TOPIC_SORT_OPTIONS, topicSort, 'setSortTopic');
    renderTopicRows();
  };

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
    window.scrollTo(0, 0);

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

    // focus — first
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

  // ── Wiki ─────────────────────────────────────────────────────────────────────
  function renderEntityRows() {
    const data = window.WIKI_DATA || {};
    const container = $('#wiki-entities');
    if (!container || !data.entities?.length) return;
    const sorted = sortItems(data.entities, entitySort.key, entitySort.dir);
    container.innerHTML = sorted.map(e => `
<div class="entity-row" onclick="openWikiPage('${esc(e.id)}','entity')">
  <div class="entity-row__name"><span class="bracket">[[</span>${esc(e.id)}<span class="bracket">]]</span></div>
  <div class="entity-row__type">${esc(e.entityType)}</div>
  <div><span class="pill pill--${e.pill}">${esc(shortStatus(e.status))}</span></div>
  <div class="entity-row__summary" title="${esc(e.summary)}">${esc(e.summary)}</div>
  <div class="entity-row__updated">${esc(e.lastUpdated || e.firstSeen || '')}</div>
</div>`).join('');
  }

  function renderTopicRows() {
    const data = window.WIKI_DATA || {};
    const container = $('#wiki-topics');
    if (!container || !data.topics?.length) return;
    const sorted = sortItems(data.topics, topicSort.key, topicSort.dir);
    container.innerHTML = sorted.map(t => `
<div class="entity-row entity-row--topic" onclick="openWikiPage('${esc(t.id)}','topic')">
  <div class="entity-row__name"><span class="bracket">[[</span>${esc(t.id)}<span class="bracket">]]</span></div>
  <div><span class="pill pill--${t.pill}">${esc(shortStatus(t.status))}</span></div>
  <div class="entity-row__summary" title="${esc(t.summary)}">${esc(t.summary)}</div>
  <div class="entity-row__updated">${esc(t.lastUpdated || t.startDate || '')}</div>
</div>`).join('');
  }

  function renderWiki() {
    const data = window.WIKI_DATA || { entities: [], topics: [] };
    const totalPages = (data.entities?.length || 0) + (data.topics?.length || 0);
    const today = new Date().toISOString().slice(0, 10);

    const subEl = $('#wiki-sub');
    if (subEl) subEl.textContent = `最後更新：${today} · 頁面數：${totalPages} · 點擊實體查看詳細頁面`;

    buildSortBar('sort-bar-entity', ENTITY_SORT_OPTIONS, entitySort, 'setSortEntity');
    buildSortBar('sort-bar-topic',  TOPIC_SORT_OPTIONS,  topicSort,  'setSortTopic');
    renderEntityRows();
    renderTopicRows();
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
      return `<div class="${cls}" onclick="openDigestPage('${esc(d.date)}')">
  <div class="archive-card__date">${dateLabel}</div>
  <div class="archive-card__title">${esc(d.preview)}</div>
  <div class="archive-card__meta"><span>${d.articleCount} 篇</span><span>⭐ ${d.topCount}</span></div>
</div>`;
    }).join('');
  }

  // ── Open wiki entity/topic as full page ──────────────────────────────────────
  window.openWikiPage = function (id, type) {
    const data = window.WIKI_DATA || {};
    const list = type === 'entity' ? data.entities : data.topics;
    const item = (list || []).find(x => x.id === id);
    if (!item) return;

    detailReturnView = 'wiki';
    const backLabel = $('#detail-back-label');
    if (backLabel) backLabel.textContent = 'Wiki 知識庫';
    const crumb = $('#detail-breadcrumb');
    if (crumb) crumb.textContent = id;

    // strip H1 + front-matter metadata
    let md = (item.markdown || '');
    md = md.replace(/^#[^#][^\n]*\n/, '');
    md = md.replace(/^(\s*\*\*[^*]+[：:]\*\*[^\n]*\n|\s*\n)*/m, '');

    let bodyHtml;
    if (typeof marked !== 'undefined') {
      md = md.replace(/\[\[([^\]]+)\]\]/g, (_, p) => `<WIKILINK>${p}</WIKILINK>`);
      bodyHtml = marked.parse(md);
      bodyHtml = bodyHtml.replace(/<WIKILINK>([^<]+)<\/WIKILINK>/g, (_, p) =>
        `<span class="detail__wikilink">${esc(p)}</span>`
      );
    } else {
      bodyHtml = `<pre style="white-space:pre-wrap;font-size:13px">${esc(md)}</pre>`;
    }

    const metaRows = [];
    if (item.entityType) metaRows.push({ label: '類型',     val: item.entityType });
    if (item.status)     metaRows.push({ label: '狀態',     val: item.status });
    if (item.firstSeen)  metaRows.push({ label: '首次出現', val: item.firstSeen });
    if (item.startDate)  metaRows.push({ label: '開始日期', val: item.startDate });
    if (item.lastUpdated)metaRows.push({ label: '最後更新', val: item.lastUpdated });

    const metaHtml = metaRows.map(r =>
      `<div class="detail__meta-row"><span class="detail__meta-label">${esc(r.label)}</span><span>${esc(r.val)}</span></div>`
    ).join('');

    const typeLabel = type === 'entity' ? '實體' : '議題';

    $('#detail-content').innerHTML = `
<div class="detail__type-row">
  <span class="pill pill--${item.pill}">${esc(item.status)}</span>
  <span class="pill pill--gray">${esc(item.entityType || typeLabel)}</span>
</div>
<h1 class="detail__h1">${esc(item.name)}</h1>
${metaRows.length ? `<div class="detail__meta">${metaHtml}</div>` : ''}
<div class="detail__body">${bodyHtml}</div>`;

    switchView('detail', null);
  };

  // ── Open archive digest as full page ─────────────────────────────────────────
  window.openDigestPage = function (date) {
    const d = (window.DIGEST_ALL || {})[date];
    if (!d) return;

    detailReturnView = 'archive';
    const backLabel = $('#detail-back-label');
    if (backLabel) backLabel.textContent = '典藏';
    const crumb = $('#detail-breadcrumb');
    if (crumb) { crumb.textContent = date; crumb.style.cssText = 'font-family:var(--font-mono);font-size:12px;color:var(--tan-7)'; }

    // wrap in a feed container for proper feed styles
    const wrapper = document.createElement('div');
    wrapper.className = 'feed';
    wrapper.style.cssText = 'max-width:100%;padding:0';
    renderDigest(d, wrapper);
    $('#detail-content').innerHTML = '';
    $('#detail-content').appendChild(wrapper);

    switchView('detail', null);
  };

  // ── Close detail — return to previous view ───────────────────────────────────
  window.closeDetail = function () {
    const returnBtn = document.querySelector(`.nav__link[data-view="${detailReturnView}"]`);
    switchView(detailReturnView, returnBtn);
  };

  // ── Init ─────────────────────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', () => {
    // keyboard shortcuts
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        const detail = $('#view-detail');
        if (detail && detail.classList.contains('is-active')) closeDetail();
      }
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
