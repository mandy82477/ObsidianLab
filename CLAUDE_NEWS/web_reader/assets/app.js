// CLAUDE NEWS · LLM-WIKI — app.js

(function () {
  'use strict';

  const $ = s => document.querySelector(s);
  const $$ = s => document.querySelectorAll(s);
  let rendered = { today: false, wiki: false, archive: false };
  let detailReturnView = 'wiki';

  // ── On-demand fetch caches ───────────────────────────────────────────────────
  const _wikiCache   = {};   // id   → full wiki object
  const _digestCache = {};   // date → full digest object

  async function fetchWiki(id) {
    if (_wikiCache[id]) return _wikiCache[id];
    const res = await fetch(`data/wiki/${encodeURIComponent(id)}.json`);
    if (!res.ok) throw new Error(`wiki/${id}: HTTP ${res.status}`);
    const data = await res.json();
    _wikiCache[id] = data;
    return data;
  }

  async function fetchDigest(date) {
    if (_digestCache[date]) return _digestCache[date];
    const res = await fetch(`data/digest/${encodeURIComponent(date)}.json`);
    if (!res.ok) throw new Error(`digest/${date}: HTTP ${res.status}`);
    const data = await res.json();
    _digestCache[date] = data;
    return data;
  }

  function setDetailLoading(msg) {
    const el = $('#detail-content');
    if (el) el.innerHTML =
      `<div style="padding:60px;text-align:center;color:var(--fg-3);font-family:var(--font-mono);font-size:12px">${msg}</div>`;
  }

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
    localStorage.setItem('claude-news-theme', next);
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

  const MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const DOW    = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
  function dateParts(dateStr) {
    const p = dateStr.split('-');
    const dt = new Date(dateStr + 'T00:00:00Z');
    return {
      y:   p[0],
      m:   MONTHS[parseInt(p[1],10)-1] || '',
      d:   parseInt(p[2]||'0',10),
      dow: isNaN(dt) ? '' : DOW[dt.getUTCDay()],
    };
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
  function focusTagCls(tag) { return FOCUS_TAG_MAP[tag.replace(/^\[|\]$/g, '')] || 'track'; }

  function shortStatus(s) {
    return (s || '').replace(/[（(][^）)]*[）)]/g, '').trim();
  }

  // ── Story HTML ───────────────────────────────────────────────────────────────
  function storyHtml(s, star = false, focusTag = '') {
    // JS-side URL match (focusTag) takes priority; fall back to Python-computed focusTags
    const effectiveTag = focusTag || (s.focusTags && s.focusTags[0]) || '';
    const cls = star ? 'story story--star' : 'story';
    const focusBadge = effectiveTag
      ? `<span class="focus-tag focus-tag--${focusTagCls(effectiveTag)} story__focus-badge">${esc(effectiveTag)}</span>`
      : '';
    return `<div class="${cls}">
  <div class="story__title"><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a>${focusBadge}</div>
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

    const _idx = (window.WIKI_DATA || {}).digestIndex || [];
    const _latestDate = _idx.length ? _idx.slice().sort((a,b) => b.date.localeCompare(a.date))[0].date : null;
    const isLatest = _latestDate === d.date;
    parts.push(`<div class="feed__header">
  <div class="day-badge">
    <div class="day-badge__y">${esc(dp.y)}</div>
    <span class="day-badge__d">${dp.d}</span>
    <div class="day-badge__m">${esc(dp.m)} · ${esc(dp.dow)}</div>
  </div>
  <div class="feed__meta">
    <h1>每日新聞摘要 · Claude Code &amp; Anthropic</h1>
    <div class="feed__metarow">
      <span><b>${d.articleCount}</b> articles</span>
      <span class="sep">·</span>
      ${isLatest ? '<span class="pulse-dot">fresh</span>' : ''}
    </div>
    <div class="feed__metarow" style="margin-top:4px;font-size:11px">
      <span>${esc(d.date)} · ${esc(d.sourceCount || '')} sources · generated ${esc(d.generatedAt)}</span>
    </div>
  </div>
</div>`);

    // focus — first
    if (d.focus?.length) {
      parts.push(`<div class="section section--focus">
<div class="section__h"><span class="section__h-label">今 日 聚 焦</span><span class="section__h-en">today's focus</span><span class="section__h-count">${d.focus.length} items</span></div>
<ul class="focus-list">`);
      d.focus.forEach(f => {
        const cls = focusTagCls(f.tag);
        parts.push(`<li class="focus-item"><span class="focus-tag focus-tag--${cls}">${esc(f.tag)}</span><span>${esc(f.text)}</span></li>`);
      });
      parts.push('</ul></div>');
    }

    // build focus URL → tag map (for badge injection on matching stories)
    const focusUrlMap = {};
    (d.focus || []).forEach(f => {
      (f.ref_urls || (f.ref_url ? [f.ref_url] : [])).forEach(u => { focusUrlMap[u] = f.tag; });
    });

    // sections
    const sections = [
      { key: 'topStories',  emoji: '⭐', label: '重點話題',   en: 'headlines',         star: true  },
      { key: 'techUpdates', emoji: '🔧', label: '技術更新',   en: 'technical updates', star: false },
      { key: 'discussions', emoji: '💬', label: '技術熱度討論', en: 'discussion',        star: false },
      { key: 'billing',     emoji: '💰', label: '付費方案動態', en: 'pricing & access',  star: false },
    ];

    sections.forEach(({ key, emoji, label, en, star }) => {
      if (!d[key]?.length) return;
      const spaced = label.split('').join(' ');
      parts.push(`<div class="section">
<div class="section__h"><span class="section__h-label">${spaced}</span><span class="section__h-en">${en}</span><span class="section__h-count">${d[key].length} items</span></div>`);
      d[key].forEach(s => parts.push(storyHtml(s, star, focusUrlMap[s.url] || '')));
      parts.push('</div>');
    });

    // source status — one-line ribbon
    if (d.sourceStatus?.length) {
      parts.push(`<aside class="source-ribbon">
<span class="source-ribbon__label">SOURCES</span>`);
      d.sourceStatus.forEach((s, i) => {
        const zero = s.count === 0 ? ' src-n--zero' : '';
        if (i > 0) parts.push(`<span class="source-ribbon__sep">·</span>`);
        parts.push(`<span class="source-ribbon__item"><span class="src-name">${esc(s.name.toLowerCase())}</span><span class="src-n${zero}">${s.count}</span></span>`);
      });
      parts.push('</aside>');
    }

    container.innerHTML = parts.join('\n');
  }

  // ── Latest digest ────────────────────────────────────────────────────────────
  async function renderLatestDigest() {
    const container = $('#digest-content');
    if (!container) return;
    const index = (window.WIKI_DATA || {}).digestIndex || [];
    if (!index.length) { container.innerHTML = ''; return; }
    const latestDate = index.slice().sort((a,b) => b.date.localeCompare(a.date))[0].date;
    container.innerHTML =
      `<div style="padding:60px;text-align:center;color:var(--fg-3);font-family:var(--font-mono);font-size:12px">載入中…</div>`;
    try {
      const d = await fetchDigest(latestDate);
      renderDigest(d, container);
    } catch(e) {
      container.innerHTML =
        `<div style="padding:40px;text-align:center;color:var(--fg-3);font-family:var(--font-mono);font-size:12px">載入失敗：${latestDate}.json</div>`;
      console.error(e);
    }
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

    const lastUpdated = data.radar?.lastUpdated
      || (data.digestIndex || []).slice().sort((a, b) => b.date.localeCompare(a.date))[0]?.date
      || today;
    const subEl = $('#wiki-sub');
    if (subEl) subEl.textContent = `最後更新：${lastUpdated} · 共 ${totalPages} 個頁面`;

    // Populate radar card last-updated label
    const radarMeta = $('#radar-card-updated');
    if (radarMeta && data.radar?.lastUpdated) {
      radarMeta.textContent = `最後更新 ${data.radar.lastUpdated}`;
    }

    // Populate gap card last-updated label
    const gapMeta = $('#gap-card-updated');
    if (gapMeta) {
      const gapTopic = (data.topics || []).find(t => t.id === 'official-community-gap');
      if (gapTopic?.lastUpdated) gapMeta.textContent = `最後更新 ${gapTopic.lastUpdated}`;
    }

    buildSortBar('sort-bar-entity', ENTITY_SORT_OPTIONS, entitySort, 'setSortEntity');
    buildSortBar('sort-bar-topic',  TOPIC_SORT_OPTIONS,  topicSort,  'setSortTopic');
    renderEntityRows();
    renderTopicRows();
  }

  // ── Archive ──────────────────────────────────────────────────────────────────
  const MONTH_NAMES_FULL = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const DOW_NAMES = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
  function renderArchive() {
    const container = $('#archive-grid');
    if (!container) return;
    const index = (window.WIKI_DATA || {}).digestIndex || [];
    if (!index.length) { container.innerHTML = ''; return; }

    // sort newest first
    const sorted = [...index].sort((a,b) => b.date.localeCompare(a.date));
    const dates = sorted.map(d => d.date);
    const totalArticles = sorted.reduce((sum, d) => sum + (d.articleCount || 0), 0);
    const subEl = $('#archive-sub');
    if (subEl && dates.length) {
      subEl.innerHTML = `<b>${dates[dates.length-1]}</b> → <b>${dates[0]}</b> <span class="sep">·</span> <b>${dates.length}</b> 份日報 <span class="sep">·</span> <b>${totalArticles}</b> 文章`;
    }

    // group by YYYY-MM, newest month first
    const months = {};
    sorted.forEach(d => {
      const ym = d.date.slice(0, 7);
      (months[ym] = months[ym] || []).push(d);
    });
    const monthKeys = Object.keys(months).sort().reverse();

    const parts = [];
    monthKeys.forEach((ym, mi) => {
      const days = months[ym];
      const [y, m] = ym.split('-');
      const monthName = MONTH_NAMES_FULL[parseInt(m, 10) - 1] || '';
      const monthArticles = days.reduce((s, d) => s + (d.articleCount || 0), 0);
      const range = `${days[days.length-1].date} → ${days[0].date.slice(5)}`;
      parts.push(`<section class="arch__month">
  <div class="arch__monthMark">
    <div class="arch__monthMark__num">${esc(m)} · ${esc(y)}</div>
    <span class="arch__monthMark__name">${esc(monthName)}</span>
    <div class="arch__monthMark__meta">
      <div>${esc(range)}</div>
      <div><b>${days.length}</b> digests<span class="sep">·</span><b>${monthArticles}</b> articles</div>
    </div>
  </div>
  <div class="arch__days">`);
      days.forEach((d, di) => {
        const isLatest = mi === 0 && di === 0;
        const dateObj = new Date(d.date + 'T00:00:00Z');
        const dow = isNaN(dateObj) ? '' : DOW_NAMES[dateObj.getUTCDay()];
        const dateCls = 'arch__row__date' + (isLatest ? ' arch__row__date--latest' : '');
        parts.push(`<a href="#${esc(d.date)}" class="arch__row" onclick="event.preventDefault();openDigestPage('${esc(d.date)}')">
  <div class="${dateCls}">${esc(d.date.slice(5))}<span class="dow">${esc(dow)}</span></div>
  <div class="arch__row__focus">${esc(d.preview)}</div>
  <div class="arch__row__count">${d.articleCount}<span class="unit">items</span></div>
</a>`);
      });
      parts.push(`</div>
</section>`);
    });

    // sparkline — oldest → newest left to right
    const chrono = [...sorted].reverse();
    const counts = chrono.map(d => d.articleCount || 0);
    const max = Math.max(...counts, 1);
    const W = 1100, H = 80;
    const stepX = counts.length > 1 ? W / (counts.length - 1) : 0;
    const pts = counts.map((v, i) => `${(i * stepX).toFixed(1)},${(H - (v / max) * (H - 12) - 4).toFixed(1)}`).join(' ');
    const ranked = counts.map((v, i) => ({ v, i })).sort((a, b) => b.v - a.v).slice(0, 3);
    const peakDates = ranked.map(r => chrono[r.i].date.slice(5)).join(', ');
    const dotsSvg = ranked.map(r => {
      const cx = r.i * stepX, cy = H - (r.v / max) * (H - 12) - 4;
      return `<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="3" fill="var(--ochre-9)"/>`;
    }).join('');

    parts.push(`<aside class="arch__spark">
  <div class="arch__spark__head">
    <span>daily volume</span>
    <em>signal across ${counts.length} days</em>
    <span class="ct">${counts.length} pts · ochre marks top 3</span>
  </div>
  <svg class="arch__spark__svg" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none">
    <line x1="0" y1="${H-4}" x2="${W}" y2="${H-4}" stroke="var(--border-1)" stroke-width="1"/>
    <polyline points="${pts}" fill="none" stroke="var(--ink-2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.8"/>
    ${dotsSvg}
  </svg>
  <div class="arch__spark__legend">
    <span>${esc(chrono[0]?.date || '')}</span>
    <span>peaks · ${esc(peakDates)}</span>
    <span>${esc(chrono[chrono.length-1]?.date || '')}</span>
  </div>
</aside>`);

    container.innerHTML = parts.join('\n');
  }

  // ── Enterprise tracker matrix renderer ───────────────────────────────────────
  const ET_STATUS = {
    active:    { bg: 'et-active',    icon: '✅', label: '使用中' },
    warning:   { bg: 'et-warning',   icon: '⚠️', label: '縮減中' },
    switching: { bg: 'et-switching', icon: '🔄', label: '切換中' },
    exited:    { bg: 'et-exited',    icon: '❌', label: '已退出' },
    unknown:   { bg: 'et-unknown',   icon: '❓', label: '未確認' },
  };

  function renderEnterpriseMatrix(tracker) {
    const { enterprises, tools, matrix } = tracker;
    if (!enterprises?.length || !tools?.length) return '';

    // shorten tool names for column headers
    const shortTool = t => t.replace('（API）','').replace('（API）','').replace(' CLI','').replace('Anthropic ','');

    const thead = `<tr>
      <th class="et-th-ent">企業</th>
      <th class="et-th-size">規模</th>
      ${tools.map(t => `<th class="et-th-tool" title="${esc(t)}">${esc(shortTool(t))}</th>`).join('')}
    </tr>`;

    const tbody = enterprises.map(({ name, size }) => {
      const cells = tools.map(tool => {
        const cell = (matrix[name] || {})[tool];
        if (!cell) return `<td class="et-cell et-empty">—</td>`;
        const s = ET_STATUS[cell.statusKey] || ET_STATUS.unknown;
        const dateStr = cell.eventDate
          ? `<span class="et-date">${cell.eventDate.slice(5)}</span>`  // MM-DD
          : '';
        const tooltip = [cell.note, cell.confirmedDate ? `確認: ${cell.confirmedDate}` : ''].filter(Boolean).join(' · ');
        return `<td class="et-cell ${s.bg}" title="${esc(tooltip)}">
          <span class="et-icon">${s.icon}</span>${dateStr}
        </td>`;
      }).join('');
      const sizeClass = size === '頂尖' ? 'et-size--top' : '';
      return `<tr>
        <td class="et-ent">${esc(name)}</td>
        <td class="et-size ${sizeClass}">${esc(size)}</td>
        ${cells}
      </tr>`;
    }).join('');

    const legend = Object.values(ET_STATUS).map(s =>
      `<span class="et-legend-item"><span class="${s.bg} et-legend-dot"></span>${s.label}</span>`
    ).join('');

    return `<div class="et-wrap">
  <div class="et-legend">${legend}</div>
  <div class="et-scroll">
    <table class="et-matrix">
      <thead>${thead}</thead>
      <tbody>${tbody}</tbody>
    </table>
  </div>
  <p class="et-hint">hover 格子查看備註 · 日期欄為狀態生效時間點</p>
</div>`;
  }

  // ── Open wiki entity/topic as full page ──────────────────────────────────────
  window.openWikiPage = async function (id, type) {
    detailReturnView = 'wiki';
    const backLabel = $('#detail-back-label');
    if (backLabel) backLabel.textContent = 'Wiki 知識庫';
    const crumb = $('#detail-breadcrumb');
    if (crumb) crumb.textContent = id;

    switchView('detail', null);
    setDetailLoading('載入中…');

    let item;
    // feature-radar is embedded in data.js — no fetch needed
    const inlineRadar = (window.WIKI_DATA || {}).radar;
    if (id === 'feature-radar' && inlineRadar?.markdown) {
      item = inlineRadar;
    } else {
      try {
        item = await fetchWiki(id);
      } catch(e) {
        setDetailLoading(`載入失敗：${esc(id)}.json`);
        console.error(e);
        return;
      }
    }

    // strip H1 + front-matter metadata
    let md = (item.markdown || '');
    md = md.replace(/^#[^#][^\n]*\n/, '');
    md = md.replace(/^(\s*\*\*[^*]+[：:]\*\*[^\n]*\n|\s*\n)*/m, '');

    let bodyHtml;
    if (typeof marked !== 'undefined') {
      md = md.replace(/\[\[([^\]]+)\]\]/g, (_, p) => `<WIKILINK>${p}</WIKILINK>`);
      bodyHtml = marked.parse(md);
      bodyHtml = bodyHtml.replace(/<WIKILINK>([^<]+)<\/WIKILINK>/g, (_, p) => {
        // news/ links have no detail page — render as plain span
        if (p.startsWith('news/')) return `<span class="detail__wikilink">${esc(p)}</span>`;
        // resolve id + type from path prefix
        let wiId, wiType;
        if (p.startsWith('entities/')) { wiId = p.slice(9); wiType = 'entity'; }
        else if (p.startsWith('topics/')) { wiId = p.slice(7); wiType = 'topic'; }
        else if (p === 'feature-radar')  { wiId = 'feature-radar'; wiType = 'radar'; }
        else {
          const wdata = window.WIKI_DATA || {};
          wiId = p;
          wiType = (wdata.topics || []).some(t => t.id === p) ? 'topic' : 'entity';
        }
        const safeId = wiId.replace(/\\/g, '\\\\').replace(/'/g, "\\'");
        return `<button class="detail__wikilink detail__wikilink--link" onclick="openWikiPage('${safeId}','${wiType}')">${esc(p)}</button>`;
      });
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

    const _pt = item.pageType || type;
    const typeLabel = _pt === 'entity' ? '實體' : _pt === 'radar' ? '熱度雷達' : '議題';

    // ── Enterprise tracker: inject matrix above markdown body ─────────────
    let trackerHtml = '';
    if (id === 'enterprise-tool-tracker' && item.enterpriseTracker) {
      trackerHtml = renderEnterpriseMatrix(item.enterpriseTracker);
    }

    $('#detail-content').innerHTML = `
<div class="detail__type-row">
  ${item.status ? `<span class="pill pill--${item.pill}">${esc(item.status)}</span>` : ''}
  <span class="pill pill--gray">${esc(item.entityType || typeLabel)}</span>
</div>
<h1 class="detail__h1">${esc(item.name)}</h1>
${metaRows.length ? `<div class="detail__meta">${metaHtml}</div>` : ''}
${trackerHtml}
<div class="detail__body">${bodyHtml}</div>`;
    makeTablesSortable($('#detail-content'));
    if (id === 'community-tech-tools') injectToolsInsights($('#detail-content'));
  };

  // ── Open archive digest as full page ─────────────────────────────────────────
  window.openDigestPage = async function (date) {
    detailReturnView = 'archive';
    const backLabel = $('#detail-back-label');
    if (backLabel) backLabel.textContent = '典藏';
    const crumb = $('#detail-breadcrumb');
    if (crumb) { crumb.textContent = date; crumb.style.cssText = 'font-family:var(--font-mono);font-size:12px;color:var(--tan-7)'; }

    switchView('detail', null);
    setDetailLoading('載入中…');

    let d;
    try {
      d = await fetchDigest(date);
    } catch(e) {
      setDetailLoading(`載入失敗：${esc(date)}.json`);
      console.error(e);
      return;
    }

    const wrapper = document.createElement('div');
    wrapper.className = 'feed';
    wrapper.style.cssText = 'max-width:100%;padding:0';
    renderDigest(d, wrapper);
    $('#detail-content').innerHTML = '';
    $('#detail-content').appendChild(wrapper);
    makeTablesSortable($('#detail-content'));
  };

  // ── Close detail — return to previous view ───────────────────────────────────
  window.closeDetail = function () {
    const returnBtn = document.querySelector(`.nav__link[data-view="${detailReturnView}"]`);
    switchView(detailReturnView, returnBtn);
  };

  // ── Search ───────────────────────────────────────────────────────────────────
  let _searchIdx  = -1;      // keyboard-selected result index
  let _searchCorpus = null;  // null = not yet loaded

  // Load search-index.json once; fallback to metadata-only corpus on error
  async function loadSearchCorpus() {
    if (_searchCorpus) return;
    try {
      const r = await fetch('data/search-index.json');
      _searchCorpus = await r.json();
    } catch (e) {
      console.warn('[search] index load failed, falling back to metadata', e);
      const data = window.WIKI_DATA || {};
      _searchCorpus = [
        ...(data.entities || []).map(e => ({ ...e, type: 'entity', text: e.summary || '' })),
        ...(data.topics   || []).map(t => ({ ...t, type: 'topic',  text: t.summary || '' })),
      ];
    }
  }

  // Extract a snippet of text around the first keyword match
  function getSnippet(text, q, context = 90) {
    const lower = text.toLowerCase();
    const qi    = lower.indexOf(q.toLowerCase());
    if (qi < 0) return '';
    const start   = Math.max(0, qi - 25);
    const end     = Math.min(text.length, qi + q.length + context);
    let snippet   = text.slice(start, end).replace(/\n/g, ' ').trim();
    if (start > 0)              snippet = '…' + snippet;
    if (end < text.length)      snippet += '…';
    return snippet;
  }

  function highlight(text, q) {
    if (!q || !text) return esc(text);
    const re = new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
    return esc(text).replace(re, '<mark>$1</mark>');
  }

  function runSearch(q) {
    const results = $('#search-results');
    if (!results) return;
    _searchIdx = -1;
    if (!q.trim()) { results.innerHTML = ''; return; }

    if (!_searchCorpus) {
      results.innerHTML = '<div class="search-empty">索引載入中，請稍候再試…</div>';
      return;
    }

    const lq = q.toLowerCase();
    const scored = _searchCorpus.map(item => {
      const name    = (item.name    || '').toLowerCase();
      const id      = (item.id      || '').toLowerCase();
      const summary = (item.summary || '').toLowerCase();
      const text    = (item.text    || '').toLowerCase();
      let score = 0;
      if (name === lq || id === lq)   score = 100;
      else if (name.startsWith(lq))   score = 80;
      else if (id.startsWith(lq))     score = 70;
      else if (name.includes(lq))     score = 50;
      else if (id.includes(lq))       score = 40;
      else if (summary.includes(lq))  score = 20;
      else if (text.includes(lq))     score = 10;
      return { item, score };
    }).filter(r => r.score > 0).sort((a, b) => b.score - a.score).slice(0, 10);

    if (!scored.length) {
      results.innerHTML = `<div class="search-empty">找不到「${esc(q)}」相關結果</div>`;
      return;
    }

    results.innerHTML = scored.map(({ item, score }, i) => {
      const pageType  = item.type || item.pageType || 'entity';
      const isRadar   = pageType === 'radar';
      const typeCls   = (pageType === 'topic') ? 'topic' : 'entity';
      const typeLabel = isRadar ? '雷達' : (pageType === 'topic' ? '議題' : '實體');

      // For name/summary hits show summary; for content hits show match context
      let snippetHtml = '';
      if (score <= 20 && item.text) {
        const raw = getSnippet(item.text, q);
        if (raw) snippetHtml = `<div class="search-result__snippet">${highlight(raw, q)}</div>`;
      } else if (item.summary) {
        snippetHtml = `<div class="search-result__summary">${esc(item.summary.slice(0, 90))}…</div>`;
      }

      const pill   = item.pill   || 'gray';
      const status = item.status || '';
      return `<div class="search-result" data-idx="${i}" data-id="${esc(item.id)}" data-pagetype="${esc(pageType)}"
                   onclick="pickSearch('${esc(item.id)}','${esc(pageType)}')">
  <span class="search-result__type search-result__type--${typeCls}">${typeLabel}</span>
  <div class="search-result__body">
    <div class="search-result__name">${highlight(item.name || item.id, q)}</div>
    ${snippetHtml}
  </div>
  <span class="search-result__pill"><span class="pill pill--${pill}">${esc(shortStatus(status))}</span></span>
</div>`;
    }).join('');
  }

  function navigateSearch(dir) {
    const items = $$('#search-results .search-result');
    if (!items.length) return;
    items.forEach(el => el.classList.remove('is-selected'));
    _searchIdx = (_searchIdx + dir + items.length) % items.length;
    items[_searchIdx].classList.add('is-selected');
    items[_searchIdx].scrollIntoView({ block: 'nearest' });
  }

  function confirmSearch() {
    const sel = $('#search-results .search-result.is-selected') || $('#search-results .search-result');
    if (sel) sel.click();
  }

  window.pickSearch = function (id, pageType) {
    closeSearch();
    openWikiPage(id, pageType);
  };

  window.openSearch = function () {
    const overlay = $('#search-overlay');
    if (!overlay) return;
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    const input = $('#search-input');
    if (input) { input.value = ''; input.focus(); }
    const results = $('#search-results');
    if (results) results.innerHTML = '';
    _searchIdx = -1;
    // Pre-load search corpus in background (no-op if already loaded)
    loadSearchCorpus();
  };

  window.closeSearch = function () {
    const overlay = $('#search-overlay');
    if (!overlay) return;
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
  };

  // wire up search input on DOMContentLoaded (below)

  // ── Tools insights panel ─────────────────────────────────────────────────────
  let _toolsFilterActive = 'all';

  window._setToolsFilter = function (key) {
    _toolsFilterActive = key;
    // Update filter button styles
    $$('.tools-insights__filter-btn').forEach(btn => {
      btn.classList.toggle('is-active', btn.dataset.filter === key);
    });
    // Show/hide table rows
    const detail = $('#detail-content');
    if (!detail) return;
    const table = detail.querySelector('.detail__body table');
    if (!table) return;
    const rows = Array.from(table.querySelectorAll('tbody tr'));
    rows.forEach(row => {
      if (key === 'all') { row.style.display = ''; return; }
      const cells = row.cells;
      const adoptCell = cells[2] ? cells[2].textContent.trim() : '';
      const typeCell  = cells[1] ? cells[1].textContent.trim() : '';
      let show = false;
      if (key === 'adopted')        show = adoptCell.includes('✅');
      else if (key === 'niche')     show = adoptCell.includes('⚡');
      else if (key === 'watching')  show = adoptCell.includes('⏳');
      else if (key === 'skeptical') show = adoptCell.includes('⚠️');
      else show = typeCell === key;
      row.style.display = show ? '' : 'none';
    });
  };

  function injectToolsInsights(container) {
    const body = container.querySelector('.detail__body');
    if (!body) return;
    // Find the tools table specifically (first-column header = '工具')
    let table = null;
    body.querySelectorAll('table').forEach(t => {
      if (!table) {
        const firstTh = t.querySelector('thead th');
        if (firstTh && firstTh.textContent.trim() === '工具') table = t;
      }
    });
    if (!table) return;
    const rows = Array.from(table.querySelectorAll('tbody tr'));
    if (!rows.length) return;

    let active = 0, cooling = 0, inactive = 0;
    let adopted = 0, niche = 0, watching = 0;
    const typeCount = {};

    // Schema: 工具 | 類型 | 採用(✅⚡⏳⚠️❌) | 首次出現 | 簡介
    rows.forEach(row => {
      const cells = row.cells;
      if (cells.length < 3) return;
      const adopt = cells[2].textContent.trim();
      const type  = cells[1].textContent.trim();
      if (adopt.includes('✅')) adopted++;
      else if (adopt.includes('⚡')) niche++;
      else if (adopt.includes('⏳')) watching++;
      else if (adopt.includes('⚠️')) inactive++;
      if (type) typeCount[type] = (typeCount[type] || 0) + 1;
    });

    const total = rows.length;
    const topTypes = Object.entries(typeCount).sort((a, b) => b[1] - a[1]).slice(0, 6);
    const filterBtns = [
      { key: 'all',      label: `全部 ${total}` },
      { key: 'adopted',  label: `✅ 廣泛採用 ${adopted}` },
      { key: 'niche',    label: `⚡ 小圈子 ${niche}` },
      { key: 'watching', label: `⏳ 觀望 ${watching}` },
      { key: 'skeptical',label: `⚠️ 存疑 ${inactive}` },
    ];
    topTypes.forEach(([t]) => filterBtns.push({ key: t, label: t }));

    const panel = document.createElement('div');
    panel.className = 'tools-insights';
    panel.innerHTML = `
<div class="tools-insights__title">工具概覽</div>
<div class="tools-insights__stats">
  <div class="tools-insights__stat">
    <span class="tools-insights__num">${total}</span>
    <span class="tools-insights__label">收錄工具</span>
  </div>
  <div class="tools-insights__divider"></div>
  <div class="tools-insights__stat">
    <span class="tools-insights__adopt">✅ 廣泛採用 <b>${adopted}</b></span>
    <span class="tools-insights__adopt">⚡ 小圈子 <b>${niche}</b></span>
    <span class="tools-insights__adopt">⏳ 觀望 <b>${watching}</b></span>
    <span class="tools-insights__adopt">⚠️ 存疑 <b>${inactive}</b></span>
  </div>
</div>
<div class="tools-insights__filter-bar">
  ${filterBtns.map(f => `<button class="tools-insights__filter-btn${f.key === 'all' ? ' is-active' : ''}" data-filter="${esc(f.key)}" onclick="_setToolsFilter('${f.key.replace(/'/g, "\\'")}')">${esc(f.label)}</button>`).join('')}
</div>`;
    body.insertAdjacentElement('beforebegin', panel);
    _toolsFilterActive = 'all';

    // Auto-sort by adoption (col 2) descending on load: ✅ → ⚡ → ⏳ → ⚠️
    const ths = Array.from(table.querySelectorAll('thead th'));
    if (ths.length > 2) {
      ths[2].classList.add('sort-asc'); // prime for descending on first call
      sortTable(table, 2, ths[2], ths);
    }
  }

  // ── Sortable tables ──────────────────────────────────────────────────────────
  function cellSortValue(text) {
    const t = text.trim();
    const fires = (t.match(/🔥/g) || []).length;
    if (fires > 0) return fires;
    // Activity circles
    if (t.includes('🟢')) return 3;
    if (t.includes('🟡')) return 2;
    if (t.includes('🔴')) return 1;
    if (t.includes('⚫')) return 0;
    // Trial value
    if (t.includes('✅')) return 3;
    if (t.includes('⚡')) return 2;
    if (t.includes('⏳')) return 1;
    if (t.includes('⚠️')) return 0;
    if (t.includes('❌')) return -1;
    // Date strings sort lexicographically (YYYY-MM-DD or MM-DD)
    if (/^\d{2,4}-\d{2}(-\d{2})?$/.test(t)) return t;
    return t.toLowerCase();
  }

  function sortTable(table, col, activeTh, ths) {
    const tbody = table.querySelector('tbody');
    if (!tbody) return;
    const wasAsc = activeTh.classList.contains('sort-asc');
    const dir = wasAsc ? -1 : 1;
    ths.forEach(th => th.classList.remove('sort-asc', 'sort-desc'));
    activeTh.classList.add(dir === 1 ? 'sort-asc' : 'sort-desc');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    rows.sort((a, b) => {
      const av = cellSortValue(a.cells[col]?.textContent || '');
      const bv = cellSortValue(b.cells[col]?.textContent || '');
      if (typeof av === 'number' && typeof bv === 'number') return (av - bv) * dir;
      return String(av).localeCompare(String(bv), 'zh-TW') * dir;
    });
    rows.forEach(r => tbody.appendChild(r));
  }

  function makeTablesSortable(container) {
    container.querySelectorAll('.detail__body table').forEach(table => {
      const ths = Array.from(table.querySelectorAll('thead th'));
      if (!ths.length) return;
      ths.forEach((th, col) => {
        th.classList.add('sortable');
        th.addEventListener('click', () => sortTable(table, col, th, ths));
      });
    });
  }

  // ── Init ─────────────────────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', () => {
    // keyboard shortcuts
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        const overlay = $('#search-overlay');
        if (overlay && overlay.classList.contains('is-open')) { closeSearch(); return; }
        const detail = $('#view-detail');
        if (detail && detail.classList.contains('is-active')) closeDetail();
      }
      if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openSearch();
      }
      // Arrow keys in search
      if ($('#search-overlay')?.classList.contains('is-open')) {
        if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
          e.preventDefault();
          navigateSearch(e.key === 'ArrowDown' ? 1 : -1);
        }
        if (e.key === 'Enter') {
          e.preventDefault();
          confirmSearch();
        }
      }
    });

    // search input live handler
    const searchInput = $('#search-input');
    if (searchInput) {
      searchInput.addEventListener('input', () => runSearch(searchInput.value));
    }

    // marked.js config
    if (typeof marked !== 'undefined') {
      marked.setOptions({ breaks: true, gfm: true });
    }

    // render today on load
    renderLatestDigest();
    rendered.today = true;

    // dynamically update ABOUT "last ingest" from digestIndex
    const digestIdx = window.WIKI_DATA && window.WIKI_DATA.digestIndex;
    if (digestIdx && digestIdx.length > 0) {
      const latest = digestIdx[0];
      const dateFmt = latest.date.replace(/-/g, '·'); // "2026·05·22"
      const lastEl  = $('.about__prov-last');
      const subEl   = $('.about__prov-lastsub');
      if (lastEl) lastEl.innerHTML = `<em>${dateFmt}</em>`;
      if (subEl)  subEl.textContent = `${latest.articleCount} articles · 6/6 sources · score ≥ 3`;
    }
  });

})();
