
import legacy from '@vitejs/plugin-legacy'

export default defineNuxtConfig({
  compatibilityDate: '2024-01-01',

  devtools: {
    enabled: false,
  },

  ssr: true,

  // ─────────────────────────────────────────────
  // Nitro / Static Generation
  // ─────────────────────────────────────────────
  nitro: {
    preset: 'static',

    compressPublicAssets: true,

    prerender: {
      routes: [
        // صفحات اصلی هر زبان
        '/en',
        '/fa',
        '/tr',
        '/ar',

        // صفحات محصول
        '/en/products',
        '/fa/products',
        '/ar/products',
        '/tr/products',

        // صفحات درباره ما
        '/en/aboutus',
        '/fa/aboutus',
        '/ar/aboutus',
        '/tr/aboutus',

        // صفحات تماس
        '/en/contact',
        '/fa/contact',
        '/ar/contact',
        '/tr/contact',

        // صفحات خبر
        '/en/news',
        '/fa/news',
        '/ar/news',
        '/tr/news',

        // صفحات careers
        '/en/careers',
        '/fa/careers',
        '/ar/careers',
        '/tr/careers',

        // فایل‌های ضروری SEO
        '/sitemap.xml',
        '/robots.txt',
        '/llms.txt',
      ],

      crawlLinks: true,

      // تعداد صفحات همزمان برای prerender
      concurrency: 10,
    },

    routeRules: {
      '/sitemap.xml': {
        headers: {
          'Content-Type': 'application/xml; charset=utf-8',
        },
      },

      '/robots.txt': {
        headers: {
          'Content-Type': 'text/plain; charset=utf-8',
        },
      },

      '/llms.txt': {
        headers: {
          'Content-Type': 'text/plain; charset=utf-8',
        },
      },
    },
  },

  // ─────────────────────────────────────────────
  // Route Rules
  // ─────────────────────────────────────────────
  routeRules: {
    // صفحات خصوصی
    '/clientarea/**': {
      ssr: false,
      robots: false,
    },

    '/admin/**': {
      ssr: false,
      robots: false,
    },

    '/login/**': {
      robots: false,
    },

    '/*/login/**': {
      robots: false,
    },

    '/*/register/**': {
      robots: false,
    },

    // Redirect از ریشه به انگلیسی
    '/': {
      redirect: '/en',
    },
  },

  // ─────────────────────────────────────────────
  // App
  // ─────────────────────────────────────────────
  app: {
    head: {
      htmlAttrs: {
        lang: 'en',
      },

      meta: [
        {
          charset: 'utf-8',
        },

        {
          name: 'viewport',
          content:
            'width=device-width, initial-scale=1, viewport-fit=cover',
        },

        {
          name: 'theme-color',
          content: '#1a202c',
        },

        {
          name: 'apple-mobile-web-app-capable',
          content: 'yes',
        },

        {
          name: 'apple-mobile-web-app-status-bar-style',
          content: 'default',
        },

        {
          name: 'robots',
          content:
            'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1',
        },
      ],

      link: [
        {
          rel: 'icon',
          type: 'image/x-icon',
          href: '/favicon.ico',
        },

        {
          rel: 'preconnect',
          href: 'https://fonts.googleapis.com',
        },

        {
          rel: 'preconnect',
          href: 'https://fonts.gstatic.com',
          crossorigin: '',
        },

        {
          rel: 'sitemap',
          type: 'application/xml',
          href: '/sitemap.xml',
        },
      ],
    },

    pageTransition: {
      name: 'page',
      mode: 'out-in',
    },

    layoutTransition: {
      name: 'layout',
      mode: 'out-in',
    },
  },

  // ─────────────────────────────────────────────
  // Router
  // ─────────────────────────────────────────────
  router: {
    options: {
      strict: false,
    },
  },

  // ─────────────────────────────────────────────
  // Runtime Config
  // ─────────────────────────────────────────────
  runtimeConfig: {
    public: {
      apiBase:
        process.env.NUXT_PUBLIC_API_BASE ||
        'http://127.0.0.1:5000',

      wsBase:
        process.env.NUXT_PUBLIC_WS_BASE ||
        'wss://localhost:8000',

      siteUrl:
        process.env.NUXT_PUBLIC_SITE_URL ||
        'https://polychemmb.com',
    },
  },

  // ─────────────────────────────────────────────
  // Modules
  // ─────────────────────────────────────────────
  modules: [
    '@nuxtjs/tailwindcss',
    'v-gsap-nuxt',
    '@pinia/nuxt',
    '@nuxtjs/sitemap',
  ],

  // ─────────────────────────────────────────────
  // Site / SEO
  // ─────────────────────────────────────────────
  site: {
    url: 'https://polychemmb.com',
    name: 'Polychem | Masterbatch & Polymer Compound',
  },

  sitemap: {
    // صفحاتی که نباید در sitemap باشند
    exclude: [
      '/admin',
      '/admin/**',

      '/clientarea',
      '/clientarea/**',

      '/login',
      '/login/**',

      '/*/login',
      '/*/login/**',

      '/*/register',
      '/*/register/**',

      '/index',
    ],

    // ───────────────────────────────────────────
    // hreflang
    // ───────────────────────────────────────────
    urls: [
      // ══════════════════════════════════════════
      // Home
      // ══════════════════════════════════════════
      {
        loc: '/en',
        priority: 1.0,
        changefreq: 'weekly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en',
          },
        ],
      },

      {
        loc: '/fa',
        priority: 1.0,
        changefreq: 'weekly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en',
          },
        ],
      },

      {
        loc: '/ar',
        priority: 1.0,
        changefreq: 'weekly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en',
          },
        ],
      },

      {
        loc: '/tr',
        priority: 1.0,
        changefreq: 'weekly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en',
          },
        ],
      },

      // ══════════════════════════════════════════
      // Product
      // ══════════════════════════════════════════
      {
        loc: '/en/products',
        priority: 0.9,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/products',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/products',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/products',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/products',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/products',
          },
        ],
      },

      {
        loc: '/fa/products',
        priority: 0.9,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/products',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/products',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/products',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/products',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/products',
          },
        ],
      },

      {
        loc: '/ar/products',
        priority: 0.9,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/products',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/products',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/products',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/products',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/products',
          },
        ],
      },

      {
        loc: '/tr/products',
        priority: 0.9,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/products',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/products',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/products',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/products',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/products',
          },
        ],
      },

      // ══════════════════════════════════════════
      // About Us
      // ══════════════════════════════════════════
      {
        loc: '/en/aboutus',
        priority: 0.8,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/aboutus',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/aboutus',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/aboutus',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/aboutus',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/aboutus',
          },
        ],
      },

      {
        loc: '/fa/aboutus',
        priority: 0.8,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/aboutus',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/aboutus',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/aboutus',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/aboutus',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/aboutus',
          },
        ],
      },

      {
        loc: '/ar/aboutus',
        priority: 0.8,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/aboutus',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/aboutus',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/aboutus',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/aboutus',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/aboutus',
          },
        ],
      },

      {
        loc: '/tr/aboutus',
        priority: 0.8,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/aboutus',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/aboutus',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/aboutus',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/aboutus',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/aboutus',
          },
        ],
      },

      // ══════════════════════════════════════════
      // Contact
      // ══════════════════════════════════════════
      {
        loc: '/en/contact',
        priority: 0.7,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/contact',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/contact',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/contact',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/contact',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/contact',
          },
        ],
      },

      {
        loc: '/fa/contact',
        priority: 0.7,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/contact',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/contact',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/contact',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/contact',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/contact',
          },
        ],
      },

      {
        loc: '/ar/contact',
        priority: 0.7,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/contact',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/contact',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/contact',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/contact',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/contact',
          },
        ],
      },

      {
        loc: '/tr/contact',
        priority: 0.7,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/contact',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/contact',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/contact',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/contact',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/contact',
          },
        ],
      },

      // ══════════════════════════════════════════
      // News
      // ══════════════════════════════════════════
      {
        loc: '/en/news',
        priority: 0.7,
        changefreq: 'weekly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/news',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/news',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/news',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/news',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/news',
          },
        ],
      },

      {
        loc: '/fa/news',
        priority: 0.7,
        changefreq: 'weekly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/news',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/news',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/news',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/news',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/news',
          },
        ],
      },

      {
        loc: '/ar/news',
        priority: 0.7,
        changefreq: 'weekly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/news',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/news',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/news',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/news',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/news',
          },
        ],
      },

      {
        loc: '/tr/news',
        priority: 0.7,
        changefreq: 'weekly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/news',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/news',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/news',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/news',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/news',
          },
        ],
      },

      // ══════════════════════════════════════════
      // Careers
      // ══════════════════════════════════════════
      {
        loc: '/en/careers',
        priority: 0.5,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/careers',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/careers',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/careers',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/careers',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/careers',
          },
        ],
      },

      {
        loc: '/fa/careers',
        priority: 0.5,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/careers',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/careers',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/careers',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/careers',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/careers',
          },
        ],
      },

      {
        loc: '/ar/careers',
        priority: 0.5,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/careers',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/careers',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/careers',
          },
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/careers',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/careers',
          },
        ],
      },

      {
        loc: '/tr/careers',
        priority: 0.5,
        changefreq: 'monthly',
        lastmod: new Date().toISOString().split('T')[0],
        alternatives: [
          {
            hreflang: 'tr',
            href: 'https://polychemmb.com/tr/careers',
          },
          {
            hreflang: 'en',
            href: 'https://polychemmb.com/en/careers',
          },
          {
            hreflang: 'fa',
            href: 'https://polychemmb.com/fa/careers',
          },
          {
            hreflang: 'ar',
            href: 'https://polychemmb.com/ar/careers',
          },
          {
            hreflang: 'x-default',
            href: 'https://polychemmb.com/en/careers',
          },
        ],
      },
    ],
  },

  // ─────────────────────────────────────────────
  // GSAP
  // ─────────────────────────────────────────────
  gsap: {
    composables: true,
    clubPlugins: false,

    extraPlugins: {
      scrollTrigger: true,
    },
  },

  // ─────────────────────────────────────────────
  // Tailwind CSS
  // ─────────────────────────────────────────────
  tailwindcss: {
    config: {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Montserrat', 'system-ui', 'sans-serif'],
            serif: ['Montserrat', 'Georgia', 'serif'],
            mono: ['Consolas', 'Monaco', 'monospace'],
          },

          colors: {
            primary: {
              50: '#f0f9ff',
              500: '#0ea5e9',
              900: '#0c4a6e',
            },
          },
        },
      },

      corePlugins: {
        preflight: true,
      },
    },
  },

  // ─────────────────────────────────────────────
  // Experimental
  // ─────────────────────────────────────────────
  experimental: {
    // برای خروجی full-static بهتر است فعال باشد
    payloadExtraction: true,

    renderJsonPayloads: true,

    typedPages: true,
  },

  // ─────────────────────────────────────────────
  // Vite
  // ─────────────────────────────────────────────
  vite: {
    plugins: [
      legacy({
        targets: [
          'defaults',
          'not IE 11',
          'iOS >= 13',
          'Android >= 8',
        ],

        additionalLegacyPolyfills: [
          'regenerator-runtime/runtime',
        ],
      }),
    ],

    build: {
      minify: 'esbuild',
    },

    css: {
      postcss: {
        plugins: [
          require('autoprefixer'),
        ],
      },
    },
  },
})

