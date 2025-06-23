  "service-worker.js": """
    const CACHE_NAME = 'fasar-cache-v1';
    const urlsToCache = [
      '/',
      '/static/css/style.css',
      '/static/js/main.js',
      '/static/icons/icon-192.png',
      '/static/icons/icon-512.png'
    ];

    self.addEventListener('install', event => {
      event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
          return cache.addAll(urlsToCache);
        })
      );
    });
