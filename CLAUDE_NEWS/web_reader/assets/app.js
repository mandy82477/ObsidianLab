// CLAUDE NEWS · LLM-WIKI — app.js

(function () {
  'use strict';

  const $ = s => document.querySelector(s);
  const $$ = s => document.querySelectorAll(s);
  let rendered = { today: false, wiki: false, archive: false, about: false, weekly: false };
  let detailReturnView = 'wiki';

  // ── On-demand fetch caches ───────────────────────────────────────────────────
  const _wikiCache   = {};   // id   → full wiki object
  const _digestCache = {};   // date → full digest object
  const _weeklyCache = {};   // week id → full weekly object

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

  async function fetchWeekly(id) {
    if (_weeklyCache[id]) return _weeklyCache[id];
    const res = await fetch(`data/weekly/${encodeURIComponent(id)}.json`);
    if (!res.ok) throw new Error(`weekly/${id}: HTTP ${res.status}`);
    const data = await res.json();
    _weeklyCache[id] = data;
    return data;
  }

  function setDetailLoading(msg) {
    const el = $('#detail-content');
    if (el) el.innerHTML =
      `<div style="padding:60px;text-align:center;color:var(--fg-3);font-family:var(--font-mono);font-size:12px">${msg}</div>`;
  }

  // ── Sort state ───────────────────────────────────────────────────────────────
  // Knowledge-base list defaults to 最新新聞 desc (falls back to lastUpdated /
  // startDate / firstSeen when a page has no news-driven update yet). Users can
  // also switch to 名稱 asc via the sort bar.
  let kbSort = { key: 'lastNewsUpdated', dir: 'desc' };

  const KB_SORT_OPTIONS = [
    { key: 'lastNewsUpdated', label: '最新新聞' },
    { key: 'name',            label: '名稱' },
    { key: 'kbType',          label: '型別' },
  ];

  function buildSortBar(containerId, options, state, onSort) {
    const bar = $('#' + containerId);
    if (!bar) return;
    bar.innerHTML = `<span class="sort-bar__label">排序</span>` +
      options.map(({ key, label }) => {
        const active = state.key === key;
        const arrow  = active ? (state.dir === 'desc' ? ' ↓' : ' ↑') : '';
        return `<button class="sort-btn${active ? ' is-active' : ''}" onclick="${onSort}('${key}')">${esc(label)}${active ? `<span class="sort-btn__arrow">${arrow}</span>` : ''}</button>`;
      }).join('');
  }

  window.setSortKb = function (key) {
    if (kbSort.key === key) {
      kbSort.dir = kbSort.dir === 'desc' ? 'asc' : 'desc';
    } else {
      kbSort.key = key;
      kbSort.dir = (key === 'name' || key === 'kbType') ? 'asc' : 'desc';
    }
    buildSortBar('sort-bar-kb', KB_SORT_OPTIONS, kbSort, 'setSortKb');
    renderKbRows();
  };

  // slugs that are presented as "對照" (comparison/tracker) pages rather than
  // a plain entity/topic — purely a presentation-layer label, data layer untouched
  const KB_COMPARISON_SLUGS = ['model-comparison', 'anthropic-commitments', 'feature-radar', 'official-community-gap'];

  const KB_TYPE_LABEL = { entity: '檔案', topic: '議題', comparison: '對照' };
  function kbTypeOf(item) {
    return KB_COMPARISON_SLUGS.includes(item.id) ? 'comparison' : item._kbBaseType;
  }

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
      } else if (key === 'kbType') {
        av = kbTypeOf(a);
        bv = kbTypeOf(b);
      } else if (key === 'lastUpdated') {
        av = a.lastUpdated || a.startDate || a.firstSeen || '';
        bv = b.lastUpdated || b.startDate || b.firstSeen || '';
      } else if (key === 'lastNewsUpdated') {
        av = a.lastNewsUpdate || a.lastUpdated || a.startDate || a.firstSeen || '';
        bv = b.lastNewsUpdate || b.lastUpdated || b.startDate || b.firstSeen || '';
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

  // ── Domain filter ────────────────────────────────────────────────────────────
  let activeDomain = 'all';

  window.setDomainFilter = function (domain) {
    activeDomain = domain;
    // Update chip active state
    document.querySelectorAll('.domain-chip').forEach(btn => {
      btn.classList.toggle('domain-chip--active', btn.dataset.domain === domain);
    });
    renderKbRows();
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
    if (id === 'about'   && !rendered.about)    { renderTransparency(); rendered.about   = true; }
    if (id === 'weekly'  && !rendered.weekly)   { renderWeekly();       rendered.weekly  = true; }
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

  // 情緒徽章：單色 mono 符號取代平台 emoji（沿用既有 hairline chip 慣例）。
  // 同時比對 emoji 與中文詞──日報原始資料兩種格式皆可能出現（見 build_web.py 註解）。
  const SENTIMENT_MAP = [
    { match: /😊|正面/,     cls: 'positive', symbol: '+', text: '正面' },
    { match: /😤|負面/,     cls: 'negative', symbol: '−', text: '負面' },
    { match: /😐|中性/,     cls: 'neutral',  symbol: '~', text: '中性' },
    { match: /🤔|褒貶不一/, cls: 'mixed',    symbol: '?', text: '褒貶不一' },
  ];
  function sentimentHtml(raw) {
    if (!raw) return '';
    for (const { match, cls, symbol, text } of SENTIMENT_MAP) {
      if (match.test(raw)) {
        return `<span class="sentiment sentiment--${cls}" title="社群情緒：${text}">${symbol} ${text}</span>`;
      }
    }
    return `<span class="sentiment sentiment--neutral">${esc(raw)}</span>`;
  }

  const FOCUS_TAG_MAP = { '重大事件':'major','持續追蹤':'track','新工具':'tool','社群趨勢':'trend','風險警示':'risk' };
  function focusTagCls(tag) { return FOCUS_TAG_MAP[tag.replace(/^\[|\]$/g, '')] || 'track'; }

  // ── 技術更新區摺疊 ────────────────────────────────────────────────────────────
  // 只有 breaking change／安全修補屬於「actionable」，預設展開；其餘收合，
  // 使用者點「顯示其餘 N 則」才展開。純渲染層判斷，不影響 build_web.py 資料結構。
  const TECH_ACTIONABLE_RE = /breaking change|breaking|安全性?修補|漏洞|CVE-|棄用|弃用|deprecat|vulnerab|hotfix|緊急修復|重大缺陷/i;
  function isActionableTechUpdate(s) {
    return TECH_ACTIONABLE_RE.test(`${s.title || ''} ${s.body || ''}`);
  }

  window.toggleSection = function (id, btn) {
    const el = document.getElementById(id);
    if (!el) return;
    const isHidden = el.hasAttribute('hidden');
    if (isHidden) {
      el.removeAttribute('hidden');
      btn.textContent = '收合';
    } else {
      el.setAttribute('hidden', '');
      btn.textContent = `顯示其餘 ${btn.dataset.count} 則`;
    }
  };

  function shortStatus(s) {
    return (s || '').replace(/[（(][^）)]*[）)]/g, '').trim();
  }

  // ── Status label 中文化 ──────────────────────────────────────────────────────
  // 純顯示層對映：資料層（data.js / wiki 檔案）維持英文原值不動。
  // 取「（」之前的主值查表；查不到表的值原樣顯示。
  const STATUS_LABEL = {
    active: '活躍', beta: '測試中', deprecated: '已棄用', acquired: '已收購',
    resolved: '已結案', ongoing: '進行中', monitoring: '觀察中',
  };

  // main value only (English, before "（"), lowercased+trimmed for lookup
  function statusMainKey(s) {
    return shortStatus(s).toLowerCase();
  }

  // parenthetical annotation, e.g. "monitoring（官方已說明，待驗證恢復）" → "官方已說明，待驗證恢復"
  function statusAnnotation(s) {
    const m = (s || '').match(/[（(]([^）)]*)[）)]/);
    return m ? m[1].trim() : '';
  }

  // 列表用：只顯示中文主值（不含補充說明）
  function statusLabelShort(s) {
    const key = statusMainKey(s);
    return STATUS_LABEL[key] || shortStatus(s);
  }

  // 詳頁用：中文主值（原補充說明），查不到表則原樣顯示完整字串
  function statusLabelFull(s) {
    const key = statusMainKey(s);
    const label = STATUS_LABEL[key];
    if (!label) return s || '';
    const anno = statusAnnotation(s);
    return anno ? `${label}（${anno}）` : label;
  }

  // ── Story HTML ───────────────────────────────────────────────────────────────
  function storyHtml(s, star = false, focusTag = '') {
    // JS-side URL match (focusTag) takes priority; fall back to Python-computed focusTags
    const effectiveTag = focusTag || (s.focusTags && s.focusTags[0]) || '';
    const cls = star ? 'story story--star' : 'story';
    const focusBadge = effectiveTag
      ? `<span class="focus-tag focus-tag--${focusTagCls(effectiveTag)} story__focus-badge">${esc(effectiveTag)}</span>`
      : '';
    // 「已沉澱」徽章 — build_web.py 依 lastNewsUpdate 比對出的今日已沉澱 wiki 頁
    const sedimentBadges = (s.sedimented || []).map(w =>
      `<button type="button" class="sediment-chip" title="今日已沉澱至 wiki：${esc(w.id)}" onclick="event.stopPropagation();openWikiPage('${esc(w.id)}','${esc(w.pageType)}')">已沉澱</button>`
    ).join('');
    return `<div class="${cls}">
  <div class="story__title"><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a>${focusBadge}${sedimentBadges}</div>
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
    const metaTopItems = [
      `<span><b>${d.articleCount}</b> articles</span>`,
      isLatest ? '<span class="pulse-dot">fresh</span>' : '',
    ].filter(Boolean);
    const metaBottomItems = [
      esc(d.date),
      d.sourceCount ? `${esc(d.sourceCount)} sources` : '',
      d.generatedAt ? `generated ${esc(d.generatedAt)}` : '',
    ].filter(Boolean);
    parts.push(`<div class="feed__header">
  <div class="day-badge">
    <div class="day-badge__y">${esc(dp.y)}</div>
    <span class="day-badge__d">${dp.d}</span>
    <div class="day-badge__m">${esc(dp.m)} · ${esc(dp.dow)}</div>
  </div>
  <div class="feed__meta">
    <h1>每日新聞摘要 · Claude Code &amp; Anthropic</h1>
    <div class="feed__metarow">
      ${metaTopItems.join('<span class="sep">·</span>')}
    </div>
    <div class="feed__metarow" style="margin-top:4px;font-size:11px">
      <span>${metaBottomItems.join(' · ')}</span>
    </div>
  </div>
</div>`);

    // bulletin — one-line skip signal above focus
    if (d.bulletin) {
      parts.push(`<div class="digest-bulletin"><span class="digest-bulletin__label">今日快訊</span><span class="digest-bulletin__text">${esc(d.bulletin)}</span></div>`);
    }

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
      { key: 'topStories',    emoji: '⭐', label: '重點話題',     en: 'headlines',         star: true  },
      { key: 'techUpdates',   emoji: '🔧', label: '官方公告',     en: 'official releases', star: false },
      { key: 'mediaReports',  emoji: '📰', label: '媒體報導',   en: 'media reports',     star: false },
      { key: 'discussions',   emoji: '💬', label: '社群討論',   en: 'community',        star: false },
      { key: 'billing',       emoji: '💰', label: '付費方案動態', en: 'pricing & access',  star: false },
    ];

    sections.forEach(({ key, emoji, label, en, star }) => {
      if (!d[key]?.length) return;
      const spaced = label.split('').join(' ');
      parts.push(`<div class="section">
<div class="section__h"><span class="section__h-label">${spaced}</span><span class="section__h-en">${en}</span><span class="section__h-count">${d[key].length} items</span></div>`);
      if (key === 'techUpdates') {
        const items = d[key];
        let actionable = items.filter(isActionableTechUpdate);
        let rest = items.filter(s => !isActionableTechUpdate(s));
        // 退化案例：整區沒有任何 actionable 條目時全部展開，不摺疊。
        // 否則讀者看到的是「官方公告 5 ITEMS」底下只有一顆按鈕的空區塊，
        // 而「今天官方有沒有動靜」正是本站目標讀者的核心問題，不該預設藏起來。
        if (!actionable.length) { actionable = rest; rest = []; }
        actionable.forEach(s => parts.push(storyHtml(s, star, focusUrlMap[s.url] || '')));
        if (rest.length) {
          parts.push(`<div class="section__toggle-wrap">
  <button class="section__toggle-btn" type="button" data-count="${rest.length}" onclick="toggleSection('tech-updates-collapsed', this)">顯示其餘 ${rest.length} 則</button>
</div>
<div class="section__collapsed" id="tech-updates-collapsed" hidden>`);
          rest.forEach(s => parts.push(storyHtml(s, star, focusUrlMap[s.url] || '')));
          parts.push('</div>');
        }
      } else {
        d[key].forEach(s => parts.push(storyHtml(s, star, focusUrlMap[s.url] || '')));
      }
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

    // 今日 wiki 動態 — 頁尾小節，列出今天有新內容沉澱的 wiki 頁（lastNewsUpdate === 日報日期）
    if (d.sedimentedToday?.length) {
      parts.push(`<div class="section section--wiki-today">
<div class="section__h"><span class="section__h-label">今 日 W I K I 動 態</span><span class="section__h-en">wiki updates today</span><span class="section__h-count">${d.sedimentedToday.length} pages</span></div>
<div class="wiki-today-list">`);
      d.sedimentedToday.forEach(p => {
        parts.push(`<button type="button" class="wiki-today-chip" onclick="openWikiPage('${esc(p.id)}','${esc(p.pageType)}')">${esc(p.name)}</button>`);
      });
      parts.push('</div></div>');
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
  // Merge entities + topics into a single "knowledge base" list. Each item keeps
  // its original type (_kbBaseType) so openWikiPage routing (entity/topic) is
  // unaffected — this is purely a presentation-layer merge.
  function buildKbList() {
    const data = window.WIKI_DATA || {};
    const entities = (data.entities || []).map(e => ({ ...e, _kbBaseType: 'entity' }));
    const topics   = (data.topics   || []).map(t => ({ ...t, _kbBaseType: 'topic'  }));
    return entities.concat(topics);
  }

  function renderKbRows() {
    const container = $('#wiki-kb');
    if (!container) return;
    const all = buildKbList();
    if (!all.length) return;
    const _d = new Date(); const today = `${_d.getFullYear()}-${String(_d.getMonth()+1).padStart(2,'0')}-${String(_d.getDate()).padStart(2,'0')}`;
    const sorted = sortItems(all, kbSort.key, kbSort.dir);
    const filtered = activeDomain === 'all' ? sorted : sorted.filter(i => i.domain === activeDomain);
    container.innerHTML = filtered.map(item => {
      const kbType = kbTypeOf(item);
      const typeLabel = KB_TYPE_LABEL[kbType] || '檔案';
      const rowCls = kbType === 'topic' ? 'entity-row entity-row--topic' : 'entity-row';
      return `
<div class="${rowCls}" onclick="openWikiPage('${esc(item.id)}','${item._kbBaseType}')">
  <div class="entity-row__name"><span class="entity-row__slug">${esc(item.id)}</span></div>
  <div><span class="kb-type-pill kb-type-pill--${kbType}">${esc(typeLabel)}</span>${item.updateFreq ? ' <span class="kb-type-pill kb-type-pill--weekly">🗓️ 週更</span>' : ''}</div>
  <div><span class="pill pill--${item.pill}">${esc(statusLabelShort(item.status))}</span></div>
  <div class="entity-row__summary">${esc(item.latestHeadline || '')}</div>
  <div class="entity-row__updated">${item.lastNewsUpdate === today ? '<span class="badge-new">今日</span>' : ''}${esc(item.lastNewsUpdate || item.lastUpdated || item.startDate || item.firstSeen || '')}</div>
</div>`;
    }).join('');
  }

  function renderWiki() {
    const data = window.WIKI_DATA || { entities: [], topics: [] };
    const totalPages = (data.entities?.length || 0) + (data.topics?.length || 0);
    const _d = new Date(); const today = `${_d.getFullYear()}-${String(_d.getMonth()+1).padStart(2,'0')}-${String(_d.getDate()).padStart(2,'0')}`;

    // Prefer the latest daily digest date — that reflects actual pipeline freshness.
    // feature-radar's own lastUpdated is a fallback only (radar page may go untouched
    // on days with no new feature, which would otherwise show a stale date here).
    const lastUpdated = (data.digestIndex || []).slice().sort((a, b) => b.date.localeCompare(a.date))[0]?.date
      || data.radar?.lastUpdated
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

    buildSortBar('sort-bar-kb', KB_SORT_OPTIONS, kbSort, 'setSortKb');
    renderKbRows();
  }

  // ── Archive ──────────────────────────────────────────────────────────────────
  const MONTH_NAMES_FULL = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const DOW_NAMES = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
  // ── Transparency（關於頁「資料透明度」，資料來自 build 時的來源記分卡）────────────
  function renderTransparency() {
    const host = $('#transparency');
    if (!host) return;
    const T = window.TRANSPARENCY;
    if (!T || !T.sources || !T.sources.length) { host.innerHTML = ''; return; }

    const pct = v => Math.round(v * 100) + '%';
    const active = T.sources.filter(s => s.active);
    const ranked = active.filter(s => s.curation_mode !== 'whitelist')
                         .sort((a, b) => b.presence - a.presence);
    const wl = active.filter(s => s.curation_mode === 'whitelist')
                     .sort((a, b) => a.name.localeCompare(b.name));

    let hasDagger = false;
    const rankedRows = ranked.map(s => {
      const warn = s.low_sample ? ' <span class="trans__warn" title="樣本不足（<14 天或 <30 條），僅供趨勢觀察">⚠︎</span>' : '';
      let emit = '—', wiki = '—';
      if (s.gathered > 0) {
        emit = pct(s.emit_rate) + (s.rate_comparable ? '' : '†');
        if (!s.rate_comparable) hasDagger = true;
      }
      if (s.emitted > 0) wiki = pct(s.wiki_rate);
      return `<tr><td class="trans__src">${esc(s.name)}${warn}</td>` +
             `<td class="num">${s.gathered}</td><td class="num">${s.emitted}</td>` +
             `<td class="num">${s.wiki_hits}</td><td class="num">${emit}</td>` +
             `<td class="num">${wiki}</td><td class="num">${pct(s.presence)}</td></tr>`;
    }).join('');

    const wlRows = wl.map(s =>
      `<tr><td class="trans__src">${esc(s.name)}</td>` +
      `<td class="num">${s.gathered}</td><td class="num">${s.emitted}</td>` +
      `<td class="num">${s.wiki_hits}</td></tr>`
    ).join('');

    const gn = T.sources.find(s => s.slug === 'google-news');
    const b = (gn && gn.pc1_buckets) || {};
    const domainLine = (b.high || b.mid || b.low || b.unknown)
      ? `<div class="trans__note">Google News 媒體信譽組成（wiki 歸因條目，Lin et al. 2023）：` +
        `高 ${b.high || 0} · 中 ${b.mid || 0} · 低 ${b.low || 0} · 未知 ${b.unknown || 0}</div>`
      : '';

    host.innerHTML = `
      <div class="about__scope-eyebrow">04 · transparency</div>
      <h2 class="about__scope-h">資料 <em>透明度</em></h2>
      <p class="trans__lead">觀測窗 ${esc(T.window.from)} — ${esc(T.window.to)}（${T.window.days} 天）：
        抓取 ${T.totals.gathered} → 收錄 ${T.totals.emitted} → 沉澱 wiki ${T.totals.wiki_hits} 筆 ·
        來源集中度 HHI ${T.hhi.toFixed(3)}</p>
      <div class="trans__wrap"><table class="trans__table">
        <thead><tr><th>社群 / 媒體來源</th><th class="num">抓取</th><th class="num">收錄</th>
        <th class="num">wiki</th><th class="num">收錄率</th><th class="num">wiki 率</th><th class="num">占比</th></tr></thead>
        <tbody>${rankedRows}</tbody>
      </table></div>
      ${hasDagger ? '<div class="trans__note">† 跨日重覆視窗抓法（dev.to top=30），收錄率結構性偏低，不與其他來源比較。</div>' : ''}
      <div class="trans__wrap"><table class="trans__table trans__table--wl">
        <thead><tr><th>官方 / 白名單來源（保險性，不排名）</th><th class="num">抓取</th><th class="num">收錄</th><th class="num">wiki</th></tr></thead>
        <tbody>${wlRows}</tbody>
      </table></div>
      ${domainLine}
      <div class="trans__note">收錄率與 wiki 率為 Bayesian 平滑值；指標定義與公道性規則見
        <a href="https://github.com/mandy82477/ObsidianLab/blob/master/CLAUDE_NEWS/docs/source-scoring-optimization.md"
           target="_blank" rel="noreferrer">source-scoring-optimization.md ↗</a></div>`;
  }

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

  // ── Markdown → HTML (+ wikilink resolution) — shared by wiki 詳頁與週報 ───────
  // opts.short：只顯示末段名稱（如 topics/model-comparison → model-comparison）並加
  // detail__wikilink--short class（收斂裝飾、縮小字級），供週報卡片判準欄使用
  // （見 web-reader-design.md 修復記錄，只影響該情境，不動其他頁 wikilink 樣式）。
  function wikilinkButtonHtml(p, opts = {}) {
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
    const label = opts.short ? p.split('/').pop() : p;
    const cls = 'detail__wikilink detail__wikilink--link' + (opts.short ? ' detail__wikilink--short' : '');
    return `<button class="${cls}" onclick="openWikiPage('${safeId}','${wiType}')">${esc(label)}</button>`;
  }

  function linkifyWikilinks(html) {
    return html.replace(/<WIKILINK>([^<]+)<\/WIKILINK>/g, (_, p) => wikilinkButtonHtml(p));
  }

  // 純內文片段（無 H1／無 meta 前綴）→ HTML，供週報期刊版面各段落使用
  function mdToHtml(md) {
    if (!md) return '';
    if (typeof marked === 'undefined') {
      return `<pre style="white-space:pre-wrap;font-size:13px">${esc(md)}</pre>`;
    }
    const src = md.replace(/\[\[([^\]]+)\]\]/g, (_, p) => `<WIKILINK>${p}</WIKILINK>`);
    return linkifyWikilinks(marked.parse(src));
  }

  // 表格儲存格等單行文字（不包 <p>）：跳脫＋解析 wikilink，不跑完整 marked
  function weeklyInlineText(text) {
    return esc(text || '').replace(/\[\[([^\]]+)\]\]/g, (_, p) => wikilinkButtonHtml(p));
  }

  // 判準欄專用：wikilink 收斂為末段名稱＋收斂裝飾（P2-2，見 web-reader-design.md）
  function weeklyCriterionText(text) {
    return esc(text || '').replace(/\[\[([^\]]+)\]\]/g, (_, p) => wikilinkButtonHtml(p, { short: true }));
  }

  // 頭條敘事 deck：取 §H2 title 冒號後半（如「一、頭條敘事：X」→「X」）；
  // 無冒號則去掉「頭條敘事」前綴後渲染；再取不到就不渲染（淡週容忍，見 P1-2）。
  function weeklyHeadlineDeck(title) {
    if (!title) return '';
    const idx = title.search(/[：:]/);
    if (idx !== -1 && idx < title.length - 1) return title.slice(idx + 1).trim();
    const stripped = title.replace(/^[一二三四五六七八九十百]+[、.]?\s*頭條敘事\s*/, '').trim();
    return (stripped && stripped !== title) ? stripped : '';
  }

  function renderMarkdownBody(raw, opts = {}) {
    let md = raw || '';
    md = md.replace(/^#[^#][^\n]*\n/, '');
    if (opts.stripMeta !== false) {
      md = md.replace(/^(\s*\*\*[^*]+[：:]\*\*[^\n]*\n|\s*\n)*/m, '');
    }
    if (typeof marked === 'undefined') {
      return `<pre style="white-space:pre-wrap;font-size:13px">${esc(md)}</pre>`;
    }
    md = md.replace(/\[\[([^\]]+)\]\]/g, (_, p) => `<WIKILINK>${p}</WIKILINK>`);
    return linkifyWikilinks(marked.parse(md));
  }

  // ── Weekly reports — journal layout（期刊版面，見 web-reader-design.md）──────
  function weeklySectionHeader(labelChars, en) {
    const spaced = esc(labelChars.split('').join(' '));
    const enHtml = en ? `<span class="section__h-en">${esc(en)}</span>` : '';
    return `<div class="section__h weekly-section__h"><span class="section__h-label">${spaced}</span>${enHtml}</div>`;
  }

  // 從 H1（如「本週深挖 · 2026-W30（07-20 ～ 07-26）」）萃取括號內日期區間；
  // 找不到就回傳空字串，masthead 優雅省略那一段（不強求所有週報標題都帶日期）。
  function weeklyDateRangeFromName(name) {
    const m = /[（(]([^）)]+)[）)]/.exec(name || '');
    return m ? m[1] : '';
  }

  // 由本期 id 推算下一週 id，供「回收槽」顯示——純前端字串運算，非真正的曆法
  // 換算（ISO 週偶有 53 週，這裡不處理，UI 標籤用途足夠）。
  function weeklyNextWeekId(id) {
    const m = /^(\d{4})-W(\d{2})$/.exec(id || '');
    if (!m) return '';
    let year = parseInt(m[1], 10);
    let week = parseInt(m[2], 10) + 1;
    if (week > 52) { week = 1; year += 1; }
    return `${year}-W${String(week).padStart(2, '0')}`;
  }

  // 「本週數字」說明文字取第一個句號之前；無句號的長文字才硬截斷。
  function weeklyTruncateStat(desc) {
    const d = desc || '';
    const periodIdx = d.indexOf('。');
    if (periodIdx !== -1) {
      const head = d.slice(0, periodIdx + 1);
      return { text: head, truncated: head.length < d.length };
    }
    if (d.length > 48) return { text: d.slice(0, 48) + '…', truncated: true };
    return { text: d, truncated: false };
  }

  // w：fetchWeekly() 回傳的單期週報物件。有結構化欄位（§A）時走期刊版面；
  // 舊 build（無 sections／無 lede）時 fallback 回整段 markdown 渲染，不可白屏。
  function renderWeeklyJournal(w) {
    const s = w.sections || {};
    const hasStructured = !!(w.lede || s.headline || s.discussion || s.nextweek || s.numbers);
    if (!hasStructured) {
      return `<div class="weekly-journal weekly-journal--legacy">
  <div class="weekly-card weekly-card--latest">
    <div class="weekly-card__id">${esc(w.id)}</div>
    <h2 class="weekly-card__title">${esc(w.name)}</h2>
    <div class="detail__body">${renderMarkdownBody(w.markdown)}</div>
  </div>
</div>`;
    }

    const dateRange = weeklyDateRangeFromName(w.name);
    const parts = [];

    parts.push(`<div class="weekly-journal">
  <div class="weekly-masthead">
    <div class="weekly-masthead__kicker">WEEKLY · ${esc(w.id)}${dateRange ? ' · ' + esc(dateRange) : ''}</div>
    <h1 class="weekly-masthead__title">本週<em>深挖</em></h1>
  </div>`);

    if (w.lede) {
      parts.push(`
  <div class="weekly-lede">
    <div class="weekly-lede__kicker">本週一句話</div>
    <blockquote class="weekly-lede__text">${esc(w.lede)}</blockquote>
  </div>`);
    }

    if (s.headline) {
      const deck = weeklyHeadlineDeck(s.headline.title);
      parts.push(`
  <div class="weekly-section">
    ${weeklySectionHeader('頭條敘事', 'headline')}${deck ? `
    <div class="weekly-headline__deck">${esc(deck)}</div>` : ''}
    <div class="weekly-headline">${mdToHtml(s.headline.body)}</div>
  </div>`);
    }

    if (s.discussion) {
      const d = s.discussion;
      parts.push(`
  <div class="weekly-section">
    ${weeklySectionHeader('技術討論', 'discussion & deep dive')}`);
      if (d.versionNote) {
        parts.push(`
    <div class="weekly-version">
      <span class="weekly-version__pill">本週版本</span>
      <div class="weekly-version__text">${mdToHtml(d.versionNote)}</div>
    </div>`);
      }
      if (d.roundup) {
        parts.push(`
    <div class="weekly-roundup">${mdToHtml(d.roundup)}</div>`);
      }
      if (d.deepDive) {
        parts.push(`
    <div class="weekly-deepdive">
      <div class="weekly-deepdive__kicker">深挖專欄 · DEEP DIVE</div>
      <h3 class="weekly-deepdive__title">${esc(d.deepDive.title)}</h3>
      <div class="weekly-deepdive__body">${mdToHtml(d.deepDive.body)}</div>
    </div>`);
      }
      parts.push(`
  </div>`);
    }

    if (s.nextweek) {
      const nextId = weeklyNextWeekId(w.id);
      parts.push(`
  <div class="weekly-section">
    ${weeklySectionHeader('下週看什麼', 'next week')}${s.nextweek.intro ? `
    <div class="weekly-nextweek__intro">${esc(s.nextweek.intro)}</div>` : ''}
    <div class="weekly-bets">`);
      (s.nextweek.forecasts || []).forEach(fc => {
        parts.push(`
      <div class="weekly-bet">
        <span class="weekly-bet__type">${weeklyInlineText(fc.type)}</span>
        <div class="weekly-bet__forecast">${weeklyInlineText(fc.forecast)}</div>
        <div class="weekly-bet__rule"></div>
        <div class="weekly-bet__criterion"><span class="weekly-bet__criterion-label">判準</span>${weeklyCriterionText(fc.criterion)}</div>
        <div class="weekly-bet__ledger"><span class="weekly-bet__ledger-mark"></span>待回收 · ${esc(nextId)}</div>
      </div>`);
      });
      parts.push(`
    </div>
  </div>`);
    }

    if (s.numbers) {
      parts.push(`
  <div class="weekly-section weekly-colophon">
    ${weeklySectionHeader('本週數字', 'numbers')}
    <div class="weekly-stats">`);
      (s.numbers.stats || []).forEach(st => {
        const { text, truncated } = weeklyTruncateStat(st.desc);
        parts.push(`
      <div class="weekly-stat"${truncated ? ` title="${esc(st.desc)}"` : ''}>
        <div class="weekly-stat__value">${esc(st.value)}</div>
        <div class="weekly-stat__desc">${weeklyInlineText(text)}</div>
      </div>`);
      });
      parts.push(`
    </div>
  </div>`);
    }

    (w.extraSections || []).forEach(ex => {
      parts.push(`
  <div class="weekly-section weekly-section--extra">
    ${weeklySectionHeader(ex.title, '')}
    <div class="weekly-extra">${mdToHtml(ex.body)}</div>
  </div>`);
    });

    if (w.footer) {
      parts.push(`
  <div class="weekly-footer">${esc(w.footer)}</div>`);
    }

    parts.push(`
</div>`);
    return parts.join('');
  }

  async function renderWeekly() {
    const container = $('#weekly-content');
    if (!container) return;
    const shellHead = document.getElementById('weekly-shell-head');
    const index = (window.WIKI_DATA || {}).weeklyIndex || [];
    const subEl = $('#weekly-sub');
    if (!index.length) {
      // 空狀態：沒有期刊 masthead 可顯示，殼層大標留著才不會整頁空白
      if (shellHead) shellHead.style.display = '';
      if (subEl) subEl.textContent = '';
      container.innerHTML = `<div class="weekly-empty">尚無週報 — 週報機制已建置，第一份將於本週產出後顯示於此。</div>`;
      return;
    }
    // 最新一期已自帶期刊 masthead（「本週深挖」），與殼層大標重複——整組隱藏（P1-1）
    if (shellHead) shellHead.style.display = 'none';
    if (subEl) subEl.textContent = '';
    const [latest, ...older] = index;
    container.innerHTML = `
<div class="weekly-latest" id="weekly-latest-slot"></div>
${older.length ? `<div class="weekly-list-count">共 ${index.length} 份週報 · 最新一份預設展開</div><div class="weekly-list-h">歷週</div><div class="weekly-list">${older.map(w => `
  <a href="#${esc(w.id)}" class="weekly-row" onclick="event.preventDefault();openWeeklyPage('${esc(w.id)}')">
    <div class="weekly-row__id">${esc(w.id)}</div>
    <div class="weekly-row__preview">${esc(w.preview || '')}</div>
  </a>`).join('')}</div>` : ''}`;

    const slot = $('#weekly-latest-slot');
    if (!slot) return;
    slot.innerHTML = `<div style="padding:40px;text-align:center;color:var(--ink-3);font-family:var(--font-mono);font-size:12px">載入中…</div>`;
    try {
      const w = await fetchWeekly(latest.id);
      slot.innerHTML = renderWeeklyJournal(w);
      makeTablesSortable(slot);
    } catch (e) {
      slot.innerHTML = `<div style="padding:40px;text-align:center;color:var(--ink-3);font-family:var(--font-mono);font-size:12px">載入失敗：${esc(latest.id)}.json</div>`;
      console.error(e);
    }
  }

  window.openWeeklyPage = async function (id) {
    detailReturnView = 'weekly';
    const backLabel = $('#detail-back-label');
    if (backLabel) backLabel.textContent = '週報';
    const crumb = $('#detail-breadcrumb');
    if (crumb) { crumb.textContent = id; crumb.style.cssText = 'font-family:var(--font-mono);font-size:12px;color:var(--tan-7)'; }

    switchView('detail', null);
    setDetailLoading('載入中…');

    let w;
    try {
      w = await fetchWeekly(id);
    } catch (e) {
      setDetailLoading(`載入失敗：${esc(id)}.json`);
      console.error(e);
      return;
    }

    $('#detail-content').innerHTML = renderWeeklyJournal(w);
    makeTablesSortable($('#detail-content'));
  };

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

    // strip H1 + front-matter metadata, render markdown + wikilinks
    const bodyHtml = renderMarkdownBody(item.markdown || '');

    const metaRows = [];
    if (item.entityType) metaRows.push({ label: '類型',     val: item.entityType });
    if (item.status)     metaRows.push({ label: '狀態',     val: statusLabelFull(item.status) });
    if (item.firstSeen)  metaRows.push({ label: '首次出現', val: item.firstSeen });
    if (item.startDate)  metaRows.push({ label: '開始日期', val: item.startDate });
    if (item.lastUpdated)metaRows.push({ label: '最後更新', val: item.lastUpdated });
    if (item.updateFreq) metaRows.push({ label: '更新頻率', val: item.updateFreq });

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
  ${item.status ? `<span class="pill pill--${item.pill}">${esc(statusLabelFull(item.status))}</span>` : ''}
  <span class="pill pill--gray">${esc(item.entityType || typeLabel)}</span>
  ${item.updateFreq ? `<span class="pill pill--weekly">🗓️ 週更</span>` : ''}
</div>
<h1 class="detail__h1">${esc(item.name)}</h1>
${metaRows.length ? `<div class="detail__meta">${metaHtml}</div>` : ''}
${trackerHtml}
<div class="detail__body">${bodyHtml}</div>`;
    makeTablesSortable($('#detail-content'));
    enhanceCallout($('#detail-content'));
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

  // ── Search log (local-only query footprint) ───────────────────────────────────
  const SEARCH_LOG_KEY   = 'claude-news-search-log';
  const SEARCH_LOG_LIMIT = 200;
  const SEARCH_LOG_DEBOUNCE_MS = 800;
  let _searchLogTimer = null;

  function todayStr() {
    const d = new Date();
    const pad = n => String(n).padStart(2, '0');
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  }

  function readSearchLog() {
    try {
      const raw = localStorage.getItem(SEARCH_LOG_KEY);
      const arr = raw ? JSON.parse(raw) : [];
      return Array.isArray(arr) ? arr : [];
    } catch (e) {
      return [];
    }
  }

  function writeSearchLog(arr) {
    try {
      localStorage.setItem(SEARCH_LOG_KEY, JSON.stringify(arr));
    } catch (e) {
      // localStorage unavailable (private mode etc.) — silently skip
    }
  }

  // Record a finalized query (debounced caller). Dedupes same query+day, updates hits.
  function logSearchQuery(q, hits) {
    const query = q.trim();
    if (!query) return;
    let log;
    try {
      log = readSearchLog();
    } catch (e) {
      return;
    }
    const d = todayStr();
    const existingIdx = log.findIndex(entry => entry.q === query && entry.d === d);
    if (existingIdx >= 0) {
      log[existingIdx].hits = hits;
      // move updated entry to front (most recent activity first)
      const [entry] = log.splice(existingIdx, 1);
      log.unshift(entry);
    } else {
      log.unshift({ q: query, hits, d });
    }
    if (log.length > SEARCH_LOG_LIMIT) log = log.slice(0, SEARCH_LOG_LIMIT);
    writeSearchLog(log);
  }

  function scheduleSearchLog(q, hits) {
    if (_searchLogTimer) clearTimeout(_searchLogTimer);
    _searchLogTimer = setTimeout(() => {
      logSearchQuery(q, hits);
      renderZeroHitPanel();
    }, SEARCH_LOG_DEBOUNCE_MS);
  }

  function getZeroHitLog() {
    return readSearchLog().filter(e => e.hits === 0).slice(0, 10);
  }

  function renderZeroHitPanel() {
    const wrap = $('#search-zerohit');
    if (!wrap) return;
    const items = getZeroHitLog();
    if (!items.length) { wrap.innerHTML = ''; wrap.classList.remove('is-visible'); return; }
    wrap.classList.add('is-visible');
    const rows = items.map(e => {
      const [, m, day] = (e.d || '').split('-');
      const md = (m && day) ? `${m}/${day}` : e.d;
      return `<div class="search-zerohit__row"><span class="search-zerohit__q">${esc(e.q)}</span><span class="search-zerohit__d">${esc(md || '')}</span></div>`;
    }).join('');
    wrap.innerHTML = `
      <button class="search-zerohit__toggle" type="button" onclick="toggleZeroHitPanel()" aria-expanded="false">
        <svg class="search-zerohit__chev" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>
        查無結果的搜尋（${items.length}）
      </button>
      <div class="search-zerohit__body">
        <div class="search-zerohit__list">${rows}</div>
        <div class="search-zerohit__actions">
          <button class="search-zerohit__btn" type="button" onclick="copyZeroHitLog()">複製清單</button>
          <button class="search-zerohit__btn" type="button" onclick="clearZeroHitLog()">清除</button>
        </div>
      </div>`;
  }

  window.toggleZeroHitPanel = function () {
    const wrap = $('#search-zerohit');
    if (!wrap) return;
    const open = wrap.classList.toggle('is-open');
    const btn = wrap.querySelector('.search-zerohit__toggle');
    if (btn) btn.setAttribute('aria-expanded', String(open));
  };

  window.copyZeroHitLog = function () {
    const items = getZeroHitLog();
    const text = items.map(e => `${e.q} · ${e.d}`).join('\n');
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).catch(() => {});
    }
  };

  window.clearZeroHitLog = function () {
    try {
      const log = readSearchLog().filter(e => e.hits !== 0);
      writeSearchLog(log);
    } catch (e) { /* ignore */ }
    renderZeroHitPanel();
  };

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
    if (!q.trim()) {
      results.innerHTML = '';
      if (_searchLogTimer) { clearTimeout(_searchLogTimer); _searchLogTimer = null; }
      return;
    }

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

    scheduleSearchLog(q, scored.length);

    if (!scored.length) {
      results.innerHTML = `<div class="search-empty">找不到「${esc(q)}」相關結果</div>`;
      return;
    }

    results.innerHTML = scored.map(({ item, score }, i) => {
      const pageType  = item.type || item.pageType || 'entity';
      const isRadar   = pageType === 'radar';
      const isDigest  = pageType === 'digest';
      const isWeekly  = pageType === 'weekly';
      const typeCls   = (pageType === 'topic' || isDigest || isWeekly) ? 'topic' : 'entity';
      const typeLabel = isDigest ? '日報' : (isWeekly ? '週報' : (isRadar ? '雷達' : (pageType === 'topic' ? '議題' : '實體')));

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
      const pillHtml = status
        ? `<span class="search-result__pill"><span class="pill pill--${pill}">${esc(statusLabelShort(status))}</span></span>`
        : '';
      return `<div class="search-result" data-idx="${i}" data-id="${esc(item.id)}" data-pagetype="${esc(pageType)}"
                   onclick="pickSearch('${esc(item.id)}','${esc(pageType)}')">
  <span class="search-result__type search-result__type--${typeCls}">${typeLabel}</span>
  <div class="search-result__body">
    <div class="search-result__name">${highlight(item.name || item.id, q)}</div>
    ${snippetHtml}
  </div>
  ${pillHtml}
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
    if (pageType === 'digest') { openDigestPage(id); return; }
    if (pageType === 'weekly') { openWeeklyPage(id); return; }
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
    renderZeroHitPanel();
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

  // ── Callout 顯示修正 ─────────────────────────────────────────────────────────
  // 頁首 delta-first callout（"> **標題**（YYYY-MM-DD）\n> 說明…"）經 marked 轉出
  // 後是單一 <p>，描述文字過長時讀起來是一堵文字牆。這裡把標題行之後的描述
  // 依「；」拆成條列；沒有「；」可拆但仍過長時，改成可摺疊（預設收合前 3 行）。
  const CALLOUT_DESC_THRESHOLD = 120;

  function enhanceCallout(container) {
    const bq = container.querySelector('.detail__body > blockquote:first-of-type');
    if (!bq) return;
    const p = bq.querySelector('p');
    if (!p) return;
    const br = p.querySelector('br');
    if (!br) return;

    // 收集 <br> 之後的節點（=標題／日期之後的描述文字）——可能混雜文字節點與
    // 內嵌元素（如 wikilink 按鈕），拆條列／摺疊時必須保留這些元素節點本身，
    // 不能只取 textContent 重建（那樣會把 wikilink 按鈕壓扁成純文字）。
    const descNodes = [];
    for (let node = br.nextSibling; node; node = node.nextSibling) descNodes.push(node);
    if (!descNodes.length) return;
    const totalLen = descNodes.map(n => n.textContent || '').join('').trim().length;
    if (totalLen <= CALLOUT_DESC_THRESHOLD) return;

    // 攤平成 token 序列：文字節點依「；」切開（保留分隔符本身），元素節點整個複製保留
    const tokens = [];
    descNodes.forEach(node => {
      if (node.nodeType === Node.TEXT_NODE) {
        const segs = (node.textContent || '').split('；');
        segs.forEach((seg, i) => {
          if (seg) tokens.push({ text: seg });
          if (i < segs.length - 1) tokens.push({ text: '；', isBreak: true });
        });
      } else {
        tokens.push({ node: node.cloneNode(true) });
      }
    });

    // 依「；」分組——每個 isBreak token 之後另起一組
    const groups = [[]];
    tokens.forEach(tok => {
      groups[groups.length - 1].push(tok);
      if (tok.isBreak) groups.push([]);
    });
    while (groups.length && groups[groups.length - 1].length === 0) groups.pop();

    descNodes.forEach(n => n.remove());
    br.remove();

    const appendTokens = (host, group) => {
      group.forEach(tok => host.appendChild(tok.node ? tok.node : document.createTextNode(tok.text)));
    };

    if (groups.length > 1) {
      const ul = document.createElement('ul');
      ul.className = 'callout-list';
      groups.forEach(group => {
        const li = document.createElement('li');
        appendTokens(li, group);
        ul.appendChild(li);
      });
      bq.appendChild(ul);
    } else {
      const span = document.createElement('span');
      span.className = 'callout__desc';
      appendTokens(span, groups[0] || []);
      p.appendChild(document.createElement('br'));
      p.appendChild(span);
      bq.classList.add('is-foldable');
      const toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'callout__toggle';
      toggle.textContent = '展開全文 ▾';
      toggle.onclick = () => {
        const expanded = bq.classList.toggle('is-expanded');
        toggle.textContent = expanded ? '收合 ▴' : '展開全文 ▾';
      };
      bq.appendChild(toggle);
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
      if (subEl)  subEl.textContent = `${latest.articleCount} articles · 10 sources · curated daily`;
    }
  });

})();
