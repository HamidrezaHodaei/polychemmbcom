<!-- /app.vue -->
<template>
  <NuxtPage :key="$route.path" />
  <component :is="productMobileNavbar" v-if="productMobileNavbar" />
  <AppLoading />
</template>

<script setup>
import { computed } from 'vue'
import AppLoading from '~/components/en/loading/AppLoading.vue'
import EnNavbarMob from '~/components/en/layout/navbar-mob.vue'
import FaNavbarMob from '~/components/fa/layout/navbar-mob.vue'
import ArNavbarMob from '~/components/ar/layout/navbar-mob.vue'
import TrNavbarMob from '~/components/tr/layout/navbar-mob.vue'

const route = useRoute()
const productMobileNavbar = computed(() => {
  const match = route.path.match(/^\/(en|fa|ar|tr)\/products\/[^/]+/)
  if (!match) return null

  return {
    en: EnNavbarMob,
    fa: FaNavbarMob,
    ar: ArNavbarMob,
    tr: TrNavbarMob,
  }[match[1]]
})

const config = useRuntimeConfig()
const siteUrl = config.public.siteUrl || 'https://polychemmb.com'
const siteLogo = `${siteUrl}/logo.png`

// ✅ فقط تنظیمات پایه اینجاست — هر صفحه lang و dir خودش رو override میکنه
useHead({
  // lang پیشفرض — صفحات زبانی این رو override میکنن
  htmlAttrs: { lang: 'en', dir: 'ltr' },

  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1, viewport-fit=cover' },
    { name: 'theme-color', content: '#1a202c' },
    { name: 'color-scheme', content: 'light' },
    { name: 'mobile-web-app-capable', content: 'yes' },
    { name: 'apple-mobile-web-app-capable', content: 'yes' },
    { name: 'apple-mobile-web-app-status-bar-style', content: 'default' },
    { name: 'author', content: 'Polychem Corporation (Polychemmb)' },
    { name: 'robots', content: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' },
  ],

  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico?v=6' },
    { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png?v=6' },
    { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png?v=6' },
    { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png?v=6' },
    { rel: 'manifest', href: '/site.webmanifest' },
    { rel: 'sitemap', type: 'application/xml', href: '/sitemap.xml' },
    { rel: 'dns-prefetch', href: 'https://fonts.googleapis.com' },
    { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
    { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: 'anonymous' },
  ],

  script: [
    // ✅ Organization Schema — یک بار در app.vue کافیه
    {
      type: 'application/ld+json',
      key: 'organization-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Organization',
        '@id': `${siteUrl}/#organization`,
        name: 'Polychem',
        legalName: 'Polychem Corporation',
        alternateName: [
          'Polychemmb', 'Polychem MB', 'Polychem Iran',
          'پلی‌کم', 'پلیکم', 'پلی کم', 'پلیمرشیمی ارس',
          'شرکت پلكيم', 'Polychem Aras','پلیمرشیمی منقطه آزاد ارس',
        ],
        url: siteUrl,
        logo: {
          '@type': 'ImageObject',
          '@id': `${siteUrl}/#logo`,
          url: siteLogo,
          width: 250,
          height: 250,
          caption: 'Polychem — Masterbatch & Polymer Compound Manufacturer Iran',
        },
        description: "Polychem (Polychemmb) is Iran's leading manufacturer of masterbatch and polymer compounds. Located in Aras Free Zone. | پلی‌کم پیشروترین تولیدکننده مستربچ و کامپاند پلیمر در ایران.",
        foundingDate: '2015',
        telephone: ['+98-921-22898980'],
        email: 'info@polychemmb.com',
        address: {
          '@type': 'PostalAddress',
          streetAddress: 'Aras Free Trade-Industrial Zone',
          addressLocality: 'Jolfa',
          addressRegion: 'East Azerbaijan Province',
          postalCode: '5481',
          addressCountry: { '@type': 'Country', name: 'Iran' },
        },
        sameAs: [
          'https://www.linkedin.com/company/polychemmb',
          'https://www.instagram.com/polychemmb',
        ],
      }),
    },

    // ✅ WebSite Schema
    {
      type: 'application/ld+json',
      key: 'website-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'WebSite',
        '@id': `${siteUrl}/#website`,
        url: siteUrl,
        name: 'Polychem | Masterbatch & Polymer Compound | پلیکم',
        alternateName: ['Polychemmb', 'پلی‌کم', 'پلیمرشیمی ارس'],
        publisher: { '@id': `${siteUrl}/#organization` },
        inLanguage: ['en', 'fa', 'ar', 'tr'],
        potentialAction: {
          '@type': 'SearchAction',
          target: {
            '@type': 'EntryPoint',
            urlTemplate: `${siteUrl}/search?q={search_term_string}`,
          },
          'query-input': 'required name=search_term_string',
        },
      }),
    },
  ],
})
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');

html, body, #__nuxt {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background-color: #f1f2f2;
}

* { font-family: inherit; }

img { content-visibility: auto; }

@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan thin.ttf') format('truetype');
  font-weight: 100;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan light.ttf') format('truetype');
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan medium.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan extrabold.ttf') format('truetype');
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan black.ttf') format('truetype');
  font-weight: 900;
  font-style: normal;
  font-display: swap;
}
</style>