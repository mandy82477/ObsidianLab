/* CLAUDE NEWS · LLM-WIKI — Service Worker
 *
 * Strategy: network-first, cache fallback. This is a daily-updated news reader,
 * so an online visitor must always get the freshest digest/wiki; the cache is
 * purely offline insurance (last-seen content works on a plane / no signal).
 *
 * SW_VERSION is rewritten by scripts/build_web.py on every build, so each deploy
 * ships a new cache name → clients auto-drop the stale cache in activate().
 */
const SW_VERSION = '1783752409';
const CACHE = 'claude-news-' + SW_VERSION;

// App shell precached on install (relative to the SW scope = web_reader/).
// Versioned assets (?v=) and on-demand data/*.json are runtime-cached instead.
const SHELL = [
  '.',
  'index.html',
  'assets/marked.min.js',
  'manifest.webmanifest',
  'icons/icon-192.png',
  'icons/icon-512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      // addAll is atomic — one 404 fails the whole install — so tolerate
      // individual misses by caching best-effort.
      .then((cache) => Promise.allSettled(SHELL.map((u) => cache.add(u))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((k) => k.startsWith('claude-news-') && k !== CACHE)
            .map((k) => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;

  // Only handle same-origin GETs; let everything else (POST, cross-origin) pass.
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    fetch(req)
      .then((res) => {
        // Cache a copy of every successful same-origin response for offline use.
        if (res && res.status === 200) {
          const copy = res.clone();
          caches.open(CACHE).then((cache) => cache.put(req, copy));
        }
        return res;
      })
      .catch(() =>
        caches.match(req).then((hit) => {
          if (hit) return hit;
          // Offline navigation to an un-cached URL → fall back to the app shell.
          if (req.mode === 'navigate') return caches.match('index.html');
          return Response.error();
        })
      )
  );
});
