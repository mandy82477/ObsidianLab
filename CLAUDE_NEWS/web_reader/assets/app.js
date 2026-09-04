// CLAUDE NEWS · LLM-WIKI — app.js

(function () {
  'use strict';

  const $ = s => document.querySelector(s);
  const $$ = s => document.querySelectorAll(s);
  let rendered = { today: false, wiki: false, archive: false, about: false, weekly: false, map: false };
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

  const KB_TYPE_LABEL = { entity: '檔案', topic: '議題', comparison: '對照', weekly: '週更' };
  function kbTypeOf(item) {
    return KB_COMPARISON_SLUGS.includes(item.id) ? 'comparison' : item._kbBaseType;
  }
  // Sort-only grouping: weekly-cadence pages (updateFreq set) cluster into their
  // own group regardless of underlying entity/topic/comparison type. Display-layer
  // kbTypeOf() above is untouched — this only feeds the kbType sort comparator.
  function kbSortGroupOf(item) {
    return item.updateFreq ? 'weekly' : kbTypeOf(item);
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
        av = kbSortGroupOf(a);
        bv = kbSortGroupOf(b);
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
      // kbType groups (含週更自成一組) sort by name within a tied group
      if (key === 'kbType' && cmp === 0) {
        const an = (a.name || a.id || '').toLowerCase();
        const bn = (b.name || b.id || '').toLowerCase();
        const nameCmp = an < bn ? -1 : an > bn ? 1 : 0;
        return dir === 'asc' ? nameCmp : -nameCmp;
      }
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
    if (id === 'map'     && !rendered.map)      { renderMap();          rendered.map     = true; }
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
      `<button type="button" class="sediment-chip" title="這則新聞的內容已整理進 wiki 頁「${esc(w.name || w.id)}」，點擊開啟" onclick="event.stopPropagation();openWikiPage('${esc(w.id)}','${esc(w.pageType)}')">已沉澱</button>`
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
    // fresh 只在「日報日期＝今天」才成立；最新一份但已隔天以上時改標相對天數，
    // 避免讀者把 2 天前的資料誤信為當日（2026-07-28 讀者 review）
    const _t = new Date(); const _todayStr = `${_t.getFullYear()}-${String(_t.getMonth()+1).padStart(2,'0')}-${String(_t.getDate()).padStart(2,'0')}`;
    const _ageDays = Math.max(0, Math.round((new Date(_todayStr + 'T00:00:00Z') - new Date(d.date + 'T00:00:00Z')) / 86400000));
    const freshHtml = !isLatest ? '' :
      _ageDays === 0 ? '<span class="pulse-dot">fresh</span>' :
      `<span class="digest-age">${_ageDays === 1 ? '1 day ago' : _ageDays + ' days ago'}</span>`;
    const metaTopItems = [
      `<span><b>${d.articleCount}</b> articles</span>`,
      freshHtml,
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
        // 2026-09-04 使用者裁決：今日聚焦句尾不顯示來源連結（先改「來源 1、來源 2」為圖示，再裁決整個移除）。
        // markdown 的行內連結照留——6g 歸因覆蓋率靠它算；細節在下方各區條目自有原文連結。
        const refs = '';
        parts.push(`<li class="focus-item"><span class="focus-tag focus-tag--${cls}">${esc(f.tag)}</span><span>${esc(f.text)}</span>${refs}</li>`);
      });
      parts.push('</ul>');
      // 常駐導流：重度使用者的核心問題「該不該升版」答案在熱度雷達頁，
      // 但從日報頁原本沒有任何入口（2026-07-28 讀者 review 高影響項）
      parts.push(`<div class="focus-radar-cta">該不該升版？<button type="button" class="focus-radar-cta__link" onclick="openWikiPage('feature-radar','radar')">看功能熱度雷達的升版風險與建議 →</button></div>`);
      parts.push('</div>');
    }

    // build focus URL → tag map (for badge injection on matching stories)
    const focusUrlMap = {};
    (d.focus || []).forEach(f => {
      (f.ref_urls || []).forEach(u => { focusUrlMap[u] = f.tag; });
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

    // 🧭 專頁雷達 — 為特定 wiki 專頁定向抓取的條目（2026-08-13 起）。
    // 自成一格、放在正文六區之後：讀者契約是正文維持 Claude/Anthropic 純度，
    // 這區的條目標題本來就不會提到 Claude，必須讓讀者一眼分辨「這是為哪頁抓的」。
    if (d.topicRadar?.length) {
      parts.push(`<div class="section section--radar">
<div class="section__h"><span class="section__h-label">專 頁 雷 達</span><span class="section__h-en">topic watch · 定向抓取</span><span class="section__h-count">${d.topicRadar.length} items</span></div>`);
      d.topicRadar.forEach(s => {
        const p = s.topicPage;
        const chip = p
          ? `<button type="button" class="radar-topic-chip" onclick="openWikiPage('${esc(p.id)}','${esc(p.pageType)}')">→ ${esc(p.name)}</button>`
          : (s.topic ? `<span class="radar-topic-chip radar-topic-chip--plain">→ ${esc(s.topic)}</span>` : '');
        parts.push(`<div class="story story--radar">
  <div class="story__title"><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a></div>
  ${s.body ? `<div class="story__body">${esc(s.body)}</div>` : ''}
  <div class="sourceline">${chip}</div>
</div>`);
      });
      parts.push('</div>');
    }

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
<div class="section__h"><span class="section__h-label">今 日 W I K I 動 態</span><span class="section__h-en">wiki updates today</span><span class="section__h-count">${d.sedimentedToday.length} pages</span><button type="button" class="map__link-btn section__h-map" onclick='openMapSet(${esc(JSON.stringify(d.sedimentedToday.map(p => p.id)))}, "${esc(d.date || "")} 有新聞落地的頁")'>在星圖上看 →</button></div>
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
    const codingIds = new Set((window.WIKI_DATA || {}).codingPages || []);
    // 子故事階層（2026-09-03）：子頁不平鋪，只從母頁詳頁下鑽；列表只顯示根頁
    const roots = sorted.filter(i => !i.parent);
    // 讀者分類（2026-09-03）：篩選看 readerDomains 多標籤（build 端算好：領域值照放，index 💻 入口表
    // 的頁再加一枚 💻 開發實務，不獨佔）；舊資料無此欄時退回 domain＋codingPages，避免快取舊 data.js 時整頁空白
    const readerDomains = i => i.readerDomains || [i.domain].concat(codingIds.has(i.id) ? ['💻 開發實務'] : []);
    const filtered = activeDomain === 'all' ? roots
      : activeDomain === 'weekly' ? roots.filter(i => !!i.updateFreq)
      : roots.filter(i => readerDomains(i).includes(activeDomain));
    // 週更篩選時置頂一行說明：日期停留數天是策展節奏，不是漏更新
    const weeklyNote = activeDomain === 'weekly'
      ? '<div class="kb-filter-note">這些頁面採每週策展維護，更新日期停留數天屬正常節奏，並非漏更新。</div>'
      : activeDomain === '💻 開發實務'
      ? '<div class="kb-filter-note">程式開發實務——做某件事該下哪個 skill、卡住了找社群首選、寫 code 選哪個模型。</div>'
      : '';
    container.innerHTML = weeklyNote + filtered.map(item => {
      const kbType = kbTypeOf(item);
      const isWeeklyCadence = !!item.updateFreq;
      const typeLabel = isWeeklyCadence ? KB_TYPE_LABEL.weekly : (KB_TYPE_LABEL[kbType] || '檔案');
      const typePillCls = isWeeklyCadence ? 'weekly' : kbType;
      const rowCls = kbType === 'topic' ? 'entity-row entity-row--topic' : 'entity-row';
      return `
<div class="${rowCls}" onclick="openWikiPage('${esc(item.id)}','${item._kbBaseType}')">
  <div class="entity-row__name"><span class="entity-row__zh">${esc(item.name || item.id)}</span><span class="entity-row__slug">${esc(item.id)}</span></div>
  <div><span class="kb-type-pill kb-type-pill--${typePillCls}">${isWeeklyCadence ? '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-1px;margin-right:3px"><rect x="3" y="5" width="18" height="16" rx="1"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="8" y1="3" x2="8" y2="7"></line><line x1="16" y1="3" x2="16" y2="7"></line></svg>' : ''}${esc(typeLabel)}</span></div>
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
      <div class="trans__note">收錄率與 wiki 率為 Bayesian 平滑值（小樣本向整體先驗收縮，避免極端值誤導）。</div>`;
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
  // detail__wikilink--short class。**目前無呼叫端** `[2026-08-30]`——原本唯一的使用者是
  // 週報判準欄，該欄已依使用者裁決不再渲染；對應 CSS 已一併移除，故此路徑現無樣式。
  // 保留參數本身（一個三元式）以免日後需要時重寫；要再用須同時補回 CSS。
  // slug → 中文頁名（查無則回傳 null）；wikilink 按鈕優先顯示中文名，
  // 冷讀者不需自己完成 slug ↔ 中文名的對映（2026-07-28 讀者 review）
  function wikiPageName(id) {
    const wdata = window.WIKI_DATA || {};
    if (id === 'feature-radar') return '功能熱度雷達';
    const hit = (wdata.entities || []).find(e => e.id === id) || (wdata.topics || []).find(t => t.id === id);
    return (hit && hit.name) ? hit.name : null;
  }

  // 內嵌到 onclick 屬性裡的 JS 字面值：反斜線／引號／< 都得中和，
  // 否則錨點含引號的頁面會把整段 handler 打斷。
  function jsStr(s) {
    return String(s)
      .replace(/\\/g, '\\\\')
      .replace(/'/g, "\\'")
      .replace(/"/g, '\\x22')
      .replace(/</g, '\\x3C');
  }

  // [[頁面#錨點|別名]] 三段拆解。marked 在表格內會把 \| 還原成 |，表格外則原樣
  // 留著反斜線，兩種都要吃掉（語法契約見 CLAUDE.md「連結與嵌入語法」）。
  function parseWikilink(raw) {
    const s = String(raw).replace(/\\([|#])/g, '$1');
    const bar    = s.indexOf('|');
    const alias  = bar >= 0 ? s.slice(bar + 1).trim() : '';
    const target = (bar >= 0 ? s.slice(0, bar) : s).trim();
    const hash   = target.indexOf('#');
    return {
      page:   (hash >= 0 ? target.slice(0, hash) : target).trim(),
      anchor: hash >= 0 ? target.slice(hash + 1).trim() : '',
      alias,
    };
  }

  function wikilinkButtonHtml(raw, opts = {}) {
    const { page: p, anchor, alias } = parseWikilink(raw);
    const cls = 'detail__wikilink detail__wikilink--link' + (opts.short ? ' detail__wikilink--short' : '');
    // [[#標題]] — 同頁段落跳轉，不離開目前頁面
    if (!p) {
      if (!anchor) return '';
      return `<button class="${cls}" onclick="scrollToAnchor('${jsStr(anchor)}')">${esc(alias || anchor)}</button>`;
    }
    // news/ links have no detail page — render as plain span
    if (p.startsWith('news/')) return `<span class="detail__wikilink">${esc(alias || p)}</span>`;
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
    const label = alias || wikiPageName(wiId) || (opts.short ? p.split('/').pop() : p);
    const anchorArg = anchor ? `,'${jsStr(anchor)}'` : '';
    return `<button class="${cls}" onclick="openWikiPage('${jsStr(wiId)}','${wiType}'${anchorArg})">${esc(label)}</button>`;
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

  // 頭條敘事 deck：取 §H2 title 冒號後半（如「一、頭條敘事：X」→「X」）；
  // 無冒號則去掉「頭條敘事」前綴後渲染；再取不到就不渲染（淡週容忍，見 P1-2）。
  function weeklyHeadlineDeck(title) {
    if (!title) return '';
    const idx = title.search(/[：:]/);
    if (idx !== -1 && idx < title.length - 1) return title.slice(idx + 1).trim();
    const stripped = title.replace(/^[一二三四五六七八九十百]+[、.]?\s*頭條敘事\s*/, '').trim();
    return (stripped && stripped !== title) ? stripped : '';
  }

  // 段首粗體導語（如「**產品定位：**…」）升級為 run-in 錨點樣式——純渲染層處理，
  // 不動 wiki markdown 來源。判準：段落開頭 <strong> 且內容以全形冒號結尾。
  function markRunInLeads(html) {
    return html.replace(/<p><strong>([^<]*：)<\/strong>/g, '<p><strong class="run-in-lead">$1</strong>');
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
    return addHeadingIds(markRunInLeads(linkifyWikilinks(marked.parse(md))));
  }

  // 這版 marked 不產生標題 id（headerIds 已移除），所以 md 內的 `[文字](#錨點)` 在站上
  // 全部是死連結。長頁面若要有可點的目錄就得自己補 id——slug 規則對齊 GitHub：
  // 轉小寫、去標點、空白換連字號，中日韓字元原樣保留。
  function headingSlug(text) {
    return text
      .replace(/<[^>]*>/g, '')
      .trim()
      .toLowerCase()
      .replace(/[^\w一-鿿\- ]/g, '')
      .trim()
      .replace(/\s+/g, '-');
  }

  function addHeadingIds(html) {
    const seen = new Set();
    return html.replace(/<h([2-4])>([\s\S]*?)<\/h\1>/g, (m, level, inner) => {
      let id = headingSlug(inner);
      if (!id) return m;
      let n = 1;
      while (seen.has(id)) id = `${headingSlug(inner)}-${n++}`;
      seen.add(id);
      return `<h${level} id="${id}">${inner}</h${level}>`;
    });
  }

  // [[頁面#錨點]] 的落地點：錨點文字走 headingSlug 對上 addHeadingIds 產的 id。
  // 對不上就不捲（頁面標題改名是常態，讀者停在頁首仍讀得到內容）。
  window.scrollToAnchor = function (anchorText) {
    const id = headingSlug(String(anchorText || ''));
    if (!id) return false;
    const el = document.getElementById(id);
    if (!el) return false;
    // 刻意用瞬移不用 smooth：跨頁跳段常是數千 px，平滑動畫既慢又暈。
    // 扣掉 sticky topbar 高度，否則標題會被壓在工具列底下。
    const bar = document.querySelector('.detail__topbar');
    const pad = (bar ? bar.getBoundingClientRect().height : 0) + 12;
    const top = el.getBoundingClientRect().top + window.scrollY - pad;
    window.scrollTo(0, Math.max(0, Math.round(top)));
    return true;
  };

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

  function weeklyPrevWeekId(id) {
    const m = /^(\d{4})-W(\d{2})$/.exec(id || '');
    if (!m) return '';
    let year = parseInt(m[1], 10);
    let week = parseInt(m[2], 10) - 1;
    if (week < 1) { week = 52; year -= 1; }
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

    // 判準不渲染 `[2026-08-30 使用者裁決]`：它是給 check_weekly_ledger 的凍結契約
    // （尾端還掛著 ｜查證：探針關鍵字），不是給讀者的內容。markdown 與 JSON 照舊保留，
    // 凍結與逐條結算機制零改動；螢幕上只留「待回收 · Wnn」那一句——那是本節對讀者的承諾。
    if (s.nextweek) {
      const nextId = weeklyNextWeekId(w.id);
      const prevId = weeklyPrevWeekId(w.id);
      const recap = s.nextweek.recap || [];
      parts.push(`
  <div class="weekly-section">
    ${weeklySectionHeader('下週看什麼', 'next week')}${s.nextweek.intro ? `
    <div class="weekly-nextweek__intro">${esc(s.nextweek.intro)}</div>` : ''}`);

      parts.push(`
    <div class="weekly-bets__head">
      <span class="weekly-bets__dir">→ 下週盯這些</span>
      <span class="weekly-bets__title">本期新立的預告 · 待 ${esc(nextId)} 回收</span>
    </div>
    <div class="weekly-bets">`);
      (s.nextweek.forecasts || []).forEach(fc => {
        parts.push(`
      <div class="weekly-bet">
        <span class="weekly-bet__type">${weeklyInlineText(fc.type)}</span>
        <div class="weekly-bet__forecast">${weeklyInlineText(fc.forecast)}</div>
        <div class="weekly-bet__rule"></div>
        <div class="weekly-bet__ledger"><span class="weekly-bet__ledger-mark"></span>待回收 · ${esc(nextId)}</div>
      </div>`);
      });
      parts.push(`
    </div>`);

      // 本節目的是「提醒下週有哪些消息值得關注」（2026-08-30 使用者裁定），故新預告在上、
      // 回收在下——回收段是服務前瞻的篩選器（哪些舊線死了可以放下），不是帳本本身。
      // 兩者仍需一眼分得開：缺少方向標示會讓讀者無從判斷哪張是回頭看（2026-W31 回報的問題）。
      if (recap.length) {
        parts.push(`
    <div class="weekly-ledger">
      <div class="weekly-ledger__head">
        <span class="weekly-ledger__dir">↩ 上週的線</span>
        <span class="weekly-ledger__title">上一期（${esc(prevId)}）預告的下場</span>
      </div>${s.nextweek.recapIntro ? `
      <div class="weekly-ledger__intro">${weeklyInlineText(s.nextweek.recapIntro)}</div>` : ''}`);
        recap.forEach(rc => {
          parts.push(`
      <div class="weekly-ledger__row">
        <div class="weekly-ledger__forecast">${weeklyInlineText(rc.forecast)}</div>
        <div class="weekly-ledger__result">${weeklyInlineText(rc.result)}</div>
      </div>`);
        });
        parts.push(`
    </div>`);
      }

      parts.push(`
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
  window.openWikiPage = async function (id, type, anchor) {
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

    // ── 子故事階層：麵包屑（往上）＋子頁卡（往下）——子頁不在列表，只從這裡到 ──
    const kbAll = buildKbList();
    const byId = Object.fromEntries(kbAll.map(i => [i.id, i]));
    const crumbs = [];
    let cur = item.parent ? byId[item.parent.split('/').pop()] : null;
    while (cur && crumbs.length < 8) { crumbs.unshift(cur); cur = cur.parent ? byId[cur.parent.split('/').pop()] : null; }
    if (crumb && crumbs.length) crumb.textContent = crumbs.map(c => c.name || c.id).join(' › ') + ' › ' + (item.name || id);
    const kids = kbAll.filter(i => i.parent && i.parent.split('/').pop() === id);
    const crumbHtml = crumbs.length
      ? `<div class="detail__crumbs">${crumbs.map(c => `<button class="wikilink" onclick="openWikiPage('${esc(c.id)}','${c._kbBaseType}')">${esc(c.name || c.id)}</button>`).join(' › ')} › <span>${esc(item.name || id)}</span></div>`
      : '';
    const kidsHtml = kids.length
      ? `<div class="detail__children"><div class="wiki__section-h">子故事（${kids.length}）</div>${kids.map(k =>
          `<div class="entity-row entity-row--${k._kbBaseType}" onclick="openWikiPage('${esc(k.id)}','${k._kbBaseType}')" role="button" tabindex="0">
  <div class="entity-row__name"><span class="entity-row__zh">${esc(k.name || k.id)}</span><span class="entity-row__slug">${esc(k.id)}</span></div>
  <div class="entity-row__summary">${esc(k.latestHeadline || k.summary || '')}</div>
  <div class="entity-row__updated">${esc(k.lastNewsUpdate || k.lastUpdated || '')}</div>
</div>`).join('')}</div>`
      : '';

    $('#detail-content').innerHTML = `
<div class="detail__type-row">
  ${item.status ? `<span class="pill pill--${item.pill}">${esc(statusLabelFull(item.status))}</span>` : ''}
  <span class="pill pill--gray">${esc(item.entityType || typeLabel)}</span>
  ${item.updateFreq ? `<span class="pill pill--weekly">🗓️ 週更</span>` : ''}
</div>
${crumbHtml}
<h1 class="detail__h1">${esc(item.name)}</h1>
${metaRows.length ? `<div class="detail__meta">${metaHtml}</div>` : ''}
${trackerHtml}
${kidsHtml}
<div class="detail__body">${bodyHtml}</div>
<div class="detail__minimap" id="detail-minimap"></div>`;
    renderMiniMap(id, $('#detail-minimap'));
    makeTablesSortable($('#detail-content'));
    enhanceCallout($('#detail-content'));
    if (id === 'community-tech-tools') injectToolsInsights($('#detail-content'));
    // innerHTML 是同步的，直接捲即可；表格增強改動高度時第一次可能落空，補一次重試。
    // 不用 requestAnimationFrame——分頁在背景時 rAF 會被節流到不觸發。
    if (anchor && !scrollToAnchor(anchor)) setTimeout(() => scrollToAnchor(anchor), 80);
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
      results.innerHTML = '<div class="search-empty">索引載入中…</div>';
      // 補一次載入並在完成後重跑當前查詢，避免訊息永遠停在「載入中」
      loadSearchCorpus().then(() => {
        const cur = $('#search-input');
        if (_searchCorpus && cur && cur.value.trim() === q.trim()) runSearch(q);
      });
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

  // ── Map：wiki 連結地圖（data/graph.json，d3 首次開啟才載入）────────────────────
  // 讀者視角：頁名、領域、被引用數、距上次新聞。維運診斷（孤兒、盲區）不在此頁。
  // 領域色取既有語意 token（ochre/info/success/warn/danger/ink），單一強調色原則的
  // 例外比照「emoji 只允許在資料值」：顏色在這裡是資料值，不是 UI 強調。
  // 玩法（2026-09-04 使用者點名）：疊層（今天動過／來源餵養）、兩點連連看、隨機漫步、
  // 詳頁小星圖。不做足跡（不留任何瀏覽紀錄）、不做時光機。
  const MAP_DOMAIN_TOKEN = {
    '🤖 模型': '--ochre-9', '🛠️ 工具/功能': '--info', '💼 商業': '--success',
    '🏛️ 政策/安全': '--danger', '🌐 社群': '--warn', '👤 人物': '--ink-3', '': '--ink-2',
  };
  const MAP_CHIPS = ['全部', '🤖 模型', '🛠️ 工具/功能', '💼 商業', '🏛️ 政策/安全', '🌐 社群', '👤 人物', '💻 開發實務'];
  let mapState = null;
  let graphPromise = null;

  function loadD3() {
    if (window.d3) return Promise.resolve(window.d3);
    return new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js';
      s.onload = () => resolve(window.d3);
      s.onerror = () => reject(new Error('d3 載入失敗'));
      document.head.appendChild(s);
    });
  }
  function loadGraph() {
    if (!graphPromise) {
      graphPromise = fetch('data/graph.json').then(r => { if (!r.ok) throw new Error('graph.json ' + r.status); return r.json(); })
        .catch(e => { graphPromise = null; throw e; });
    }
    return graphPromise;
  }

  function mapCss(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || '#888';
  }
  function mapAgeOpacity(days) {
    if (days == null) return 0.85;
    if (days <= 7) return 1; if (days <= 30) return 0.78; if (days <= 90) return 0.55; return 0.35;
  }
  function mapRadius(n, mode) {
    if (mode === 'lines') return 3.5 + Math.sqrt((n.lines || 0) / 30);
    if (mode === 'age')   return 3.5 + Math.min(n.daysSinceNews == null ? 60 : n.daysSinceNews, 180) / 16;
    return 3.5 + Math.sqrt(n.inBody || 0) * 2.1;
  }
  function mapOpenable(n) {
    return n.pageType === 'entity' || n.pageType === 'topic' || n.id === 'feature-radar';
  }
  function mapColor(n) { return mapCss(MAP_DOMAIN_TOKEN[n.domain] || '--ink-2'); }

  // 疊層：{type:'none'|'today'|'source'|'set', slug?, ids?, label?}
  function mapOverlayHit(n) {
    const o = mapState.overlay;
    if (!o || o.type === 'none') return true;
    if (o.type === 'today') return !!n.lastNewsUpdate && n.lastNewsUpdate === mapState.latestNews;
    if (o.type === 'source') return !!(n.sources && n.sources[o.slug]);
    if (o.type === 'set') return o.ids.has(n.id);
    return true;
  }


  // 關聯領域：鄰居（正文邊）按領域計數，畫成一列小條——回答「這個人／這頁跟哪些領域有關」
  function mapDomainMix(nodeId, edges, byId, excludeSelfDomain) {
    const cnt = new Map();
    edges.forEach(e => {
      const a = e.source?.id ?? e.source ?? e.s, b = e.target?.id ?? e.target ?? e.d;
      if (a !== nodeId && b !== nodeId) return;
      const other = byId.get(a === nodeId ? b : a);
      if (!other || !other.domain) return;
      cnt.set(other.domain, (cnt.get(other.domain) || 0) + 1);
    });
    const rows = [...cnt.entries()].sort((x, y) => y[1] - x[1]);
    const total = rows.reduce((s, r) => s + r[1], 0);
    if (!total) return '';
    return `<div class="map__mix" title="鄰居頁按領域計數">${rows.map(([d, c]) =>
      `<span class="map__mix-item"><i class="map__mix-dot" style="background:${mapCss(MAP_DOMAIN_TOKEN[d] || '--ink-2')}"></i>${esc(d.replace(/^[^\s]+\s/, ''))} <b>${Math.round(c / total * 100)}%</b></span>`).join('')}</div>`;
  }
  function mapLegendHtml() {
    return Object.entries(MAP_DOMAIN_TOKEN).filter(([d]) => d).map(([d, tok]) =>
      `<span class="map__legend-item"><i class="map__mix-dot" style="background:${mapCss(tok)}"></i>${esc(d.replace(/^[^\s]+\s/, ''))}</span>`).join('');
  }

  async function renderMap() {
    const canvas = $('#map-canvas');
    if (!canvas) return;
    canvas.innerHTML = '<div class="map__loading">載入星圖…</div>';
    let d3, data;
    try {
      [d3, data] = await Promise.all([loadD3(), loadGraph()]);
    } catch (e) {
      canvas.innerHTML = `<div class="map__loading">星圖暫時無法載入（${esc(e.message)}）。</div>`;
      return;
    }
    const nodes = data.nodes.map(n => Object.assign({}, n));
    const byId = new Map(nodes.map(n => [n.id, n]));
    const edgesAll = data.edges.filter(e => byId.has(e.s) && byId.has(e.d))
      .map(e => ({ source: e.s, target: e.d, body: e.body, tpl: e.tpl, part: e.part, n: e.body + e.tpl + e.part }));

    mapState = { d3, nodes, byId, edgesAll, domain: '全部', size: 'in', bodyOnly: true, selected: null, query: '',
                 overlay: { type: 'none' }, latestNews: data.latestNews || '', sourcesMeta: data.sources || [],
                 generated: data.generated || '', pathFrom: null, path: null, pendingSelect: mapState?.pendingSelect || null };
    mapUpdateSub();

    // chips
    const chipWrap = $('#map-domains');
    chipWrap.innerHTML = MAP_CHIPS.map(c => `<button class="domain-chip${c === '全部' ? ' domain-chip--active' : ''}" data-map-domain="${esc(c)}">${esc(c.replace(/^[^\s]+\s/, ''))}</button>`).join('');
    chipWrap.querySelectorAll('[data-map-domain]').forEach(b => b.addEventListener('click', () => {
      mapState.domain = b.dataset.mapDomain;
      chipWrap.querySelectorAll('.domain-chip').forEach(x => x.classList.toggle('domain-chip--active', x === b));
      mapRestyle();
    }));
    // 疊層下拉：無／今天動過／各來源
    const ov = $('#map-overlay');
    ov.innerHTML = `<option value="none">無</option><option value="today">最新一天動過的頁（${esc(mapState.latestNews)}）</option>` +
      mapState.sourcesMeta.filter(s => s.count > 0).map(s => `<option value="src:${esc(s.slug)}">來源：${esc(s.name)}（${s.count}）</option>`).join('');
    ov.onchange = () => {
      const v = ov.value;
      mapState.overlay = v === 'none' ? { type: 'none' } : v === 'today' ? { type: 'today' } : { type: 'source', slug: v.slice(4), label: ov.options[ov.selectedIndex].textContent };
      mapUpdateSub(); mapRestyle();
    };
    $('#map-size').onchange = e => { mapState.size = e.target.value; mapRestyle(true); };
    $('#map-body-only').onchange = e => { mapState.bodyOnly = e.target.checked; mapRebuildLinks(); };
    $('#map-random').onclick = () => mapRandomStep();
    const find = $('#map-find');
    find.oninput = () => { mapState.query = find.value.trim().toLowerCase(); mapRestyle(); };
    find.onkeydown = ev => {
      if (ev.key !== 'Enter' || !mapState.query) return;
      const hit = nodes.find(n => n.name.toLowerCase().includes(mapState.query) || n.id.includes(mapState.query));
      if (hit) mapSelect(hit, true);
    };

    // svg
    const isMobile = window.innerWidth < 720;
    const W = canvas.clientWidth || 900;
    const H = isMobile ? Math.max(420, Math.round(window.innerHeight * 0.62)) : Math.min(720, Math.max(480, window.innerHeight - 300));
    canvas.innerHTML = '';
    const svg = d3.select(canvas).append('svg').attr('width', W).attr('height', H).attr('viewBox', `0 0 ${W} ${H}`).attr('class', 'map__svg');
    const root = svg.append('g');
    const linkG = root.append('g').attr('class', 'map__links');
    const pulseG = root.append('g').attr('class', 'map__pulses');
    const nodeG = root.append('g').attr('class', 'map__nodes');
    const labelG = root.append('g').attr('class', 'map__labels');
    const zoom = d3.zoom().scaleExtent([0.35, 4]).on('zoom', ev => {
      root.attr('transform', ev.transform);
      mapState.k = ev.transform.k;
      mapLabelVisibility();
    });
    svg.call(zoom).on('dblclick.zoom', null);
    svg.on('click', ev => { if (ev.target === svg.node()) mapSelect(null); });
    Object.assign(mapState, { svg, root, linkG, pulseG, nodeG, labelG, zoom, W, H, k: 1, isMobile });

    const sim = d3.forceSimulation(nodes)
      .force('charge', d3.forceManyBody().strength(isMobile ? -140 : -230))
      .force('center', d3.forceCenter(W / 2, H / 2))
      .force('collide', d3.forceCollide().radius(n => mapRadius(n, mapState.size) + 4))
      .force('x', d3.forceX(W / 2).strength(0.05))
      .force('y', d3.forceY(H / 2).strength(0.09));
    mapState.sim = sim;

    const node = nodeG.selectAll('circle').data(nodes, n => n.id).join('circle')
      .attr('class', 'map__node')
      .attr('r', n => mapRadius(n, 'in'))
      .call(d3.drag()
        .on('start', (ev, n) => { if (!ev.active) sim.alphaTarget(0.25).restart(); n.fx = n.x; n.fy = n.y; })
        .on('drag', (ev, n) => { n.fx = ev.x; n.fy = ev.y; })
        .on('end', (ev, n) => { if (!ev.active) sim.alphaTarget(0); n.fx = null; n.fy = null; }))
      .on('click', (ev, n) => { ev.stopPropagation(); mapState.pathFrom ? mapFinishPath(n) : mapSelect(n); })
      .on('mouseenter', (ev, n) => { if (!mapState.selected) mapHover(n); })
      .on('mouseleave', () => { if (!mapState.selected) mapHover(null); });
    node.append('title').text(n => `${n.name}\n${n.domain || '根層頁'} · 被引用 ${n.inBody} · ${n.daysSinceNews == null ? '無新聞日期' : n.daysSinceNews + ' 天前有新聞'}`);

    labelG.selectAll('text').data(nodes, n => n.id).join('text')
      .attr('class', 'map__label').attr('dy', n => mapRadius(n, 'in') + 11).attr('text-anchor', 'middle')
      .text(n => n.name.length > 14 ? n.name.slice(0, 13) + '…' : n.name);

    mapRebuildLinks();
    sim.on('tick', () => {
      mapState.linkSel.attr('x1', e => e.source.x).attr('y1', e => e.source.y).attr('x2', e => e.target.x).attr('y2', e => e.target.y);
      nodeG.selectAll('circle').attr('cx', n => n.x).attr('cy', n => n.y);
      pulseG.selectAll('circle').attr('cx', n => n.x).attr('cy', n => n.y);
      labelG.selectAll('text').attr('x', n => n.x).attr('y', n => n.y);
    });
    mapRestyle();
    const legend = $('#map-legend'); if (legend) legend.innerHTML = mapLegendHtml();

    // 從日報／詳頁帶進來的請求（在圖建好之前就被叫到）
    if (mapState.pendingSelect) { const req = mapState.pendingSelect; mapState.pendingSelect = null; setTimeout(() => mapApplyRequest(req), 900); }

    // 主題切換時重取 token 色
    new MutationObserver(() => { mapRestyle(); const lg = $('#map-legend'); if (lg) lg.innerHTML = mapLegendHtml(); }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
  }

  function mapUpdateSub() {
    const s = mapState, sub = $('#map-sub'); if (!sub) return;
    const o = s.overlay || { type: 'none' };
    const total = `<b>${s.nodes.length}</b> 頁 · <b>${s.edgesAll.length}</b> 條連結 · 資料 ${esc(s.generated)}`;
    if (o.type === 'today') sub.innerHTML = `亮著的是 <b>${esc(s.latestNews)}</b> 有新聞落地的頁。${total}`;
    else if (o.type === 'source') sub.innerHTML = `亮著的是被「<b>${esc(o.label.replace(/^來源：/, '').replace(/（\d+）$/, ''))}</b>」餵過的頁——看這個來源養出哪片星區。${total}`;
    else if (o.type === 'set') sub.innerHTML = `亮著的是 <b>${esc(o.label || '')}</b>。${total} <button class="map__link-btn" onclick="mapClearOverlay()">清除</button>`;
    else sub.innerHTML = `每頁一顆點，頁與頁之間的 wikilink 是線。點越大，被引用越多；顏色越淡，離上次新聞越久。${total}`;
  }
  window.mapClearOverlay = function () { if (!mapState) return; mapState.overlay = { type: 'none' }; const ov = $('#map-overlay'); if (ov) ov.value = 'none'; mapUpdateSub(); mapRestyle(); };

  function mapVisibleEdges() {
    const s = mapState;
    return s.bodyOnly ? s.edgesAll.filter(e => e.body > 0) : s.edgesAll;
  }
  function mapRebuildLinks() {
    const s = mapState, d3 = s.d3;
    const edges = mapVisibleEdges().map(e => Object.assign({}, e));
    s.linkSel = s.linkG.selectAll('line').data(edges, e => (e.source.id || e.source) + '>' + (e.target.id || e.target)).join('line')
      .attr('class', 'map__link').attr('stroke-width', e => 0.6 + Math.sqrt(s.bodyOnly ? e.body : e.n) * 0.5);
    s.sim.force('link', d3.forceLink(edges).id(n => n.id).distance(e => 60 + 26 / Math.sqrt(e.n)).strength(e => Math.min(0.9, 0.25 + e.n * 0.08)));
    s.edges = edges;
    s.neighbors = new Map();
    edges.forEach(e => {
      const a = e.source.id || e.source, b = e.target.id || e.target;
      if (!s.neighbors.has(a)) s.neighbors.set(a, new Set());
      if (!s.neighbors.has(b)) s.neighbors.set(b, new Set());
      s.neighbors.get(a).add(b); s.neighbors.get(b).add(a);
    });
    s.path = null; s.pathFrom = null;
    s.sim.alpha(0.6).restart();
    mapRestyle();
  }

  function mapNodeVisible(n) {
    const s = mapState;
    if (s.domain !== '全部' && !(n.tags || []).includes(s.domain)) return false;
    if (s.query && !(n.name.toLowerCase().includes(s.query) || n.id.includes(s.query))) return false;
    if (!mapOverlayHit(n)) return false;
    return true;
  }

  function mapRestyle(resize) {
    const s = mapState; if (!s || !s.nodeG) return;
    const focus = s.selected || s.hovered;
    const nb = focus ? (s.neighbors.get(focus.id) || new Set()) : null;
    const pathSet = s.path ? new Set(s.path) : null;
    const pathEdge = e => pathSet && pathSet.has(e.source.id) && pathSet.has(e.target.id) && Math.abs(s.path.indexOf(e.source.id) - s.path.indexOf(e.target.id)) === 1;
    const ochre = mapCss('--ochre-9');
    s.nodeG.selectAll('circle')
      .attr('fill', mapColor)
      .attr('r', n => mapRadius(n, s.size))
      .attr('fill-opacity', n => {
        if (!mapNodeVisible(n)) return 0.06;
        const base = mapAgeOpacity(n.daysSinceNews);
        if (pathSet) return pathSet.has(n.id) ? 1 : 0.08;
        if (!focus) return base;
        return (n.id === focus.id || nb.has(n.id)) ? Math.max(base, 0.9) : 0.08;
      })
      .attr('stroke', n => (focus && n.id === focus.id) || (pathSet && pathSet.has(n.id)) ? ochre : 'none')
      .attr('stroke-width', 2);
    if (resize) { s.sim.force('collide').radius(n => mapRadius(n, s.size) + 4); s.sim.alpha(0.3).restart(); s.labelG.selectAll('text').attr('dy', n => mapRadius(n, s.size) + 11); }
    s.linkSel
      .attr('stroke', e => (pathEdge(e) || (focus && (e.source.id === focus.id || e.target.id === focus.id))) ? mapCss('--ochre-7') : mapCss('--ink-4'))
      .attr('stroke-opacity', e => {
        if (pathSet) return pathEdge(e) ? 0.95 : 0.03;
        const vis = mapNodeVisible(e.source) && mapNodeVisible(e.target);
        if (!vis) return 0.03;
        if (!focus) return 0.35;
        return (e.source.id === focus.id || e.target.id === focus.id) ? 0.85 : 0.04;
      })
      .attr('stroke-width', e => pathEdge(e) ? 2.2 : 0.6 + Math.sqrt(s.bodyOnly ? e.body : e.n) * 0.5);
    // 脈動環：疊層命中的頁
    const pulsing = s.overlay && s.overlay.type !== 'none' ? s.nodes.filter(n => mapNodeVisible(n)) : [];
    const pulses = s.pulseG.selectAll('circle').data(pulsing, n => n.id);
    pulses.exit().remove();
    pulses.enter().append('circle').attr('class', 'map__pulse').attr('fill', 'none').attr('stroke', ochre).attr('stroke-width', 1.2)
      .each(function (n) {
        const r = mapRadius(n, s.size);
        s.d3.select(this).append('animate').attr('attributeName', 'r').attr('values', `${r + 2};${r + 14}`).attr('dur', '1.8s').attr('repeatCount', 'indefinite');
        s.d3.select(this).append('animate').attr('attributeName', 'stroke-opacity').attr('values', '0.8;0').attr('dur', '1.8s').attr('repeatCount', 'indefinite');
      })
      .merge(pulses).attr('cx', n => n.x).attr('cy', n => n.y).attr('stroke', ochre);
    mapLabelVisibility();
    const hint = $('#map-hint');
    if (hint) hint.textContent = s.pathFrom ? `連連看：已選「${s.pathFrom.name}」，再點另一顆星` : '拖曳平移、滾輪或雙指縮放；點一顆星看它連到哪';
  }

  function mapLabelVisibility() {
    const s = mapState; if (!s || !s.labelG) return;
    const focus = s.selected || s.hovered;
    const nb = focus ? (s.neighbors.get(focus.id) || new Set()) : null;
    const pathSet = s.path ? new Set(s.path) : null;
    const k = s.k || 1;
    const threshold = s.isMobile ? 13 : 8.5;   // 未放大時只標樞紐，避免手機字疊成一團
    const overlayOn = s.overlay && s.overlay.type !== 'none';
    s.labelG.selectAll('text')
      .attr('font-size', Math.max(9, 11 / Math.sqrt(k)))
      .attr('opacity', n => {
        if (!mapNodeVisible(n)) return 0;
        if (pathSet) return pathSet.has(n.id) ? 1 : 0;
        if (focus) return (n.id === focus.id || nb.has(n.id)) ? 1 : 0;
        if (s.query || overlayOn) return 1;
        return (mapRadius(n, s.size) >= threshold || k >= 1.6) ? 0.85 : 0;
      });
  }

  function mapHover(n) { mapState.hovered = n; mapRestyle(); }

  function mapCenterOn(n, minK) {
    const s = mapState; if (n.x == null) return;
    const k = Math.max(s.k, minK || 1.2);
    const t = s.d3.zoomIdentity.translate(s.W / 2 - n.x * k, s.H / 2 - n.y * k).scale(k);
    s.svg.transition().duration(450).call(s.zoom.transform, t);
  }

  function mapSelect(n, center) {
    const s = mapState; s.selected = n; s.hovered = null; s.path = null; s.pathFrom = null;
    const panel = $('#map-panel');
    if (!n) { panel.hidden = true; mapRestyle(); return; }
    const inbound = s.edges.filter(e => e.target.id === n.id).map(e => ({ n: e.source, c: s.bodyOnly ? e.body : e.n })).sort((a, b) => b.c - a.c);
    const outbound = s.edges.filter(e => e.source.id === n.id).map(e => ({ n: e.target, c: s.bodyOnly ? e.body : e.n })).sort((a, b) => b.c - a.c);
    const li = arr => arr.length ? arr.slice(0, 12).map(x => `<li><button class="map__panel-link" data-map-go="${esc(x.n.id)}">${esc(x.n.name)}</button><span class="map__panel-count">${x.c}</span></li>`).join('') + (arr.length > 12 ? `<li class="map__panel-more">…還有 ${arr.length - 12} 頁</li>` : '') : '<li class="map__panel-more">—</li>';
    const age = n.daysSinceNews == null ? '無新聞日期' : n.daysSinceNews === 0 ? '今天有新聞' : `${n.daysSinceNews} 天前有新聞`;
    const mixHtml = mapDomainMix(n.id, s.edges, s.byId);
    const topSrc = Object.entries(n.sources || {}).sort((a, b) => b[1] - a[1]).slice(0, 3)
      .map(([k, v]) => `${esc((s.sourcesMeta.find(m => m.slug === k) || {}).name || k)} ${v}`).join(' · ');
    panel.innerHTML = `
      <button class="map__panel-close" aria-label="關閉">×</button>
      <div class="map__panel-kicker">${esc(n.domain || '根層頁')}${n.pageType === 'entity' ? ' · 實體' : n.pageType === 'topic' ? ' · 議題' : ''}</div>
      <div class="map__panel-title">${esc(n.name)}</div>
      <div class="map__panel-meta">${age} · 被引用 ${n.inBody} 頁 · ${n.lines} 行</div>
      ${topSrc ? `<div class="map__panel-meta">餵養來源：${topSrc}</div>` : ''}
      ${mixHtml ? `<div class="map__panel-h">關聯領域</div>${mixHtml}` : ''}
      <div class="map__panel-actions">
        ${mapOpenable(n) ? `<button class="map__panel-open" data-map-open="${esc(n.id)}" data-map-type="${esc(n.pageType)}">開啟頁面 →</button>` : ''}
        <button class="map__panel-ghost" data-map-path="1">連到另一頁…</button>
        <button class="map__panel-ghost" data-map-walk="1">隨機走一步</button>
      </div>
      <div class="map__panel-h">誰引用它（${inbound.length}）</div><ul class="map__panel-list">${li(inbound)}</ul>
      <div class="map__panel-h">它引用誰（${outbound.length}）</div><ul class="map__panel-list">${li(outbound)}</ul>`;
    panel.hidden = false;
    panel.querySelector('.map__panel-close').addEventListener('click', () => mapSelect(null));
    panel.querySelectorAll('[data-map-go]').forEach(b => b.addEventListener('click', () => mapSelect(s.byId.get(b.dataset.mapGo), true)));
    const openBtn = panel.querySelector('[data-map-open]');
    if (openBtn) openBtn.addEventListener('click', () => openWikiPage(openBtn.dataset.mapOpen, openBtn.dataset.mapType));
    panel.querySelector('[data-map-path]').addEventListener('click', () => { s.pathFrom = n; mapRestyle(); });
    panel.querySelector('[data-map-walk]').addEventListener('click', () => mapRandomStep());
    if (center) mapCenterOn(n);
    mapRestyle();
  }

  // 兩點連連看：BFS 最短引用鏈（依目前可見邊，無向）
  function mapShortestPath(a, b) {
    const s = mapState; if (a === b) return [a];
    const prev = new Map([[a, null]]); const q = [a];
    while (q.length) {
      const cur = q.shift();
      for (const nx of (s.neighbors.get(cur) || [])) {
        if (prev.has(nx)) continue;
        prev.set(nx, cur);
        if (nx === b) { const out = [b]; let c = b; while ((c = prev.get(c)) != null) out.unshift(c); return out; }
        q.push(nx);
      }
    }
    return null;
  }
  function mapFinishPath(target) {
    const s = mapState; const from = s.pathFrom; s.pathFrom = null;
    const path = mapShortestPath(from.id, target.id);
    const panel = $('#map-panel');
    s.selected = null; s.path = path;
    const names = path ? path.map(id => s.byId.get(id)) : [];
    panel.innerHTML = `
      <button class="map__panel-close" aria-label="關閉">×</button>
      <div class="map__panel-kicker">連連看</div>
      <div class="map__panel-title">${esc(from.name)} → ${esc(target.name)}</div>
      ${path ? `<div class="map__panel-meta">${path.length - 1} 步引用鏈</div><ol class="map__panel-chain">${names.map(n => `<li><button class="map__panel-link" data-map-go="${esc(n.id)}">${esc(n.name)}</button></li>`).join('')}</ol>`
             : `<div class="map__panel-meta">在目前的連結範圍內找不到路徑。試著關掉「只看正文引用」。</div>`}`;
    panel.hidden = false;
    panel.querySelector('.map__panel-close').addEventListener('click', () => mapSelect(null));
    panel.querySelectorAll('[data-map-go]').forEach(b => b.addEventListener('click', () => mapSelect(s.byId.get(b.dataset.mapGo), true)));
    mapRestyle();
  }

  // 隨機漫步：從目前選中的頁沿一條邊走；沒選中就隨機挑一顆可見的星
  function mapRandomStep() {
    const s = mapState; if (!s) return;
    let next;
    if (s.selected) {
      const nb = [...(s.neighbors.get(s.selected.id) || [])].map(id => s.byId.get(id)).filter(mapNodeVisible);
      next = nb.length ? nb[Math.floor(Math.random() * nb.length)] : null;
    }
    if (!next) { const pool = s.nodes.filter(mapNodeVisible); next = pool[Math.floor(Math.random() * pool.length)]; }
    if (next) mapSelect(next, true);
  }

  // 從日報／詳頁進地圖：{select:id} 或 {ids:[...], label}
  function mapApplyRequest(req) {
    const s = mapState; if (!s || !s.nodeG) { mapState = mapState || {}; mapState.pendingSelect = req; return; }
    if (req.ids) {
      s.overlay = { type: 'set', ids: new Set(req.ids), label: req.label };
      const ov = $('#map-overlay'); if (ov) ov.value = 'none';
      s.selected = null; $('#map-panel').hidden = true;
      mapUpdateSub(); mapRestyle();
      const first = s.byId.get(req.ids[0]); if (first) mapCenterOn(first, 1);
    } else if (req.select) {
      const n = s.byId.get(req.select); if (n) mapSelect(n, true);
    }
  }
  window.openMapAt = function (id) {
    switchView('map', document.querySelector('[data-view=map]'));
    if (mapState && mapState.nodeG) setTimeout(() => mapApplyRequest({ select: id }), 50);
    else { mapState = mapState || {}; mapState.pendingSelect = { select: id }; }
  };
  window.openMapSet = function (ids, label) {
    switchView('map', document.querySelector('[data-view=map]'));
    if (mapState && mapState.nodeG) setTimeout(() => mapApplyRequest({ ids, label }), 50);
    else { mapState = mapState || {}; mapState.pendingSelect = { ids, label }; }
  };

  // ── 詳頁小星圖：這頁＋一跳鄰居，點鄰居直接跳頁 ─────────────────────────────
  async function renderMiniMap(id, host) {
    if (!host) return;
    let d3, data;
    try { [d3, data] = await Promise.all([loadD3(), loadGraph()]); } catch (e) { host.remove(); return; }
    const me = data.nodes.find(n => n.id === id);
    if (!me) { host.remove(); return; }
    const byId = new Map(data.nodes.map(n => [n.id, n]));
    let edges = data.edges.filter(e => (e.s === id || e.d === id) && e.body > 0);
    if (!edges.length) edges = data.edges.filter(e => e.s === id || e.d === id);
    if (!edges.length) { host.remove(); return; }
    const nbIds = [...new Set(edges.map(e => e.s === id ? e.d : e.s))];
    const nodes = [Object.assign({}, me, { _me: true })].concat(nbIds.map(x => Object.assign({}, byId.get(x))));
    const links = edges.map(e => ({ source: e.s, target: e.d, n: e.body || e.n || 1 }));
    const W = Math.min(host.clientWidth || 640, 760), H = nbIds.length > 14 ? 320 : 240;
    host.innerHTML = `<div class="wiki__section-h">連結鄰居（${nbIds.length}）<button class="map__link-btn" onclick="openMapAt('${esc(id)}')">在星圖上看 →</button></div>`;
    host.insertAdjacentHTML('beforeend', mapDomainMix(id, edges, byId));
    const svg = d3.select(host).append('svg').attr('width', W).attr('height', H).attr('viewBox', `0 0 ${W} ${H}`).attr('class', 'minimap__svg');
    const link = svg.append('g').selectAll('line').data(links).join('line').attr('stroke', mapCss('--ink-4')).attr('stroke-opacity', 0.5).attr('stroke-width', l => 0.6 + Math.sqrt(l.n) * 0.5);
    const node = svg.append('g').selectAll('circle').data(nodes).join('circle')
      .attr('r', n => n._me ? 9 : 4 + Math.sqrt(n.inBody || 0) * 1.3)
      .attr('fill', mapColor).attr('fill-opacity', n => n._me ? 1 : mapAgeOpacity(n.daysSinceNews))
      .attr('stroke', n => n._me ? mapCss('--ochre-9') : 'none').attr('stroke-width', 2)
      .attr('class', n => n._me ? 'minimap__node minimap__node--me' : 'minimap__node')
      .on('click', (ev, n) => { if (!n._me && mapOpenable(n)) openWikiPage(n.id, n.pageType); });
    node.append('title').text(n => n.name);
    const label = svg.append('g').selectAll('text').data(nodes).join('text').attr('class', 'map__label').attr('text-anchor', 'middle')
      .attr('font-size', 10.5).attr('dy', n => (n._me ? 9 : 4 + Math.sqrt(n.inBody || 0) * 1.3) + 11)
      .text(n => n.name.length > 12 ? n.name.slice(0, 11) + '…' : n.name);
    d3.forceSimulation(nodes)
      .force('link', d3.forceLink(links).id(n => n.id).distance(nbIds.length > 14 ? 70 : 85))
      .force('charge', d3.forceManyBody().strength(-160))
      .force('center', d3.forceCenter(W / 2, H / 2))
      .force('collide', d3.forceCollide().radius(18))
      .force('x', d3.forceX(W / 2).strength(0.08)).force('y', d3.forceY(H / 2).strength(0.15))
      .on('tick', () => {
        nodes.forEach(n => { n.x = Math.max(14, Math.min(W - 14, n.x)); n.y = Math.max(14, Math.min(H - 18, n.y)); });
        link.attr('x1', l => l.source.x).attr('y1', l => l.source.y).attr('x2', l => l.target.x).attr('y2', l => l.target.y);
        node.attr('cx', n => n.x).attr('cy', n => n.y);
        label.attr('x', n => n.x).attr('y', n => n.y);
      });
    // 你可能也想看：不直接相連但共享鄰居多的頁（build 端算好；達不到門檻就不顯示，不湊數）
    const recs = (me.alsoSee || []).map(r => Object.assign({ shared: r.shared }, byId.get(r.id))).filter(r => r && r.name);
    if (recs.length) {
      host.insertAdjacentHTML('beforeend', `<div class="wiki__section-h" style="margin-top:18px">你可能也想看</div>
<div class="alsosee">${recs.map(r => `<button type="button" class="alsosee__card" onclick="openWikiPage('${esc(r.id)}','${esc(r.pageType)}')">
  <span class="alsosee__name">${esc(r.name)}</span>
  <span class="alsosee__why">和本頁一起被 ${esc((r.shared || []).map(x => (byId.get(x) || {}).name || x).join('、'))} 引用，但兩頁互不相連</span>
</button>`).join('')}</div>`);
    }
  }

})();
