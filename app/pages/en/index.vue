<!-- /pages/en/index.vue -->
<template>
  <div>
    <!--
      ✅ Landpage به عنوان overlay روی همه چیز
      - Teleport بیرون از ClientOnly (این دو با هم conflict دارن)
      - v-if="showLanding" شروع false است پس در SSR چیزی رندر نمی‌شه
      - position: fixed + z-index: 9999 در landpage.vue لازمه
    -->
    <Teleport to="body">
      <Landpage v-if="showLanding" />
    </Teleport>

    <!-- ✅ محتوای اصلی همیشه SSR رندر می‌شه -->
    <Navbar />
    <Hero />
    <div class="mt-8 slider">
      <Slider />
      <Text />
      <Cards />
      <Global />
      <InfinitySlider />
    </div>
    <Footer />

    <ClientOnly>
      <Chatbox />
    </ClientOnly>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Landpage       from '~/components/layout/landpage.vue'
import Navbar         from '~/components/en/layout/navbar.vue'
import Hero           from '~/components/en/home/Hero.vue'
import Slider         from '~/components/en/home/Slider.vue'
import Text           from '~/components/en/home/Text.vue'
import Cards          from '~/components/en/home/cards.vue'
import Global         from '~/components/en/home/world.vue'
import InfinitySlider from '~/components/en/home/InfiniteSlider.vue'
import Footer         from '~/components/en/layout/footer.vue'
import Chatbox        from '~/components/en/chatbox/chatbox.vue'

// ─── SEO ──────────────────────────────────────────────────────────────────────
useSeoMeta({
  title:             'POLYCHEM | Masterbatch & Polymer Compound Manufacturer | Aras Free Zone Iran',
  ogTitle:           'POLYCHEM | Masterbatch & Polymer Compound Manufacturer | Aras Free Zone Iran',
  description:       'POLYCHEM (Polychemmb) — Iran\'s leading manufacturer of color masterbatch, filler masterbatch (CaCO3), additive masterbatch, PP compound and engineering polymer blends. Located in Aras Free Zone, exporting to Middle East & Caucasus.',
  ogDescription:     'Leading manufacturer and exporter of masterbatch and polymer compounds in Iran. ISO 9001:2015 certified. Aras Free Zone, Jolfa.',
  ogUrl:             'https://polychemmb.com/en',
  ogType:            'website',
  ogImage:           'https://polychemmb.com/og-image-en.jpg',
  twitterCard:       'summary_large_image',
  twitterTitle:      'POLYCHEM | Masterbatch & Polymer Compound | Iran',
  twitterDescription:'Iran\'s leading masterbatch manufacturer — color, filler, additive masterbatch & PP compound. Aras Free Zone.',
})

useHead({
  htmlAttrs: { lang: 'en', dir: 'ltr' },
  link: [
    { rel: 'canonical',  href: 'https://polychemmb.com/en' },
    { rel: 'alternate',  hreflang: 'en',        href: 'https://polychemmb.com/en' },
    { rel: 'alternate',  hreflang: 'fa',        href: 'https://polychemmb.com/fa' },
    { rel: 'alternate',  hreflang: 'ar',        href: 'https://polychemmb.com/ar' },
    { rel: 'alternate',  hreflang: 'tr',        href: 'https://polychemmb.com/tr' },
    { rel: 'alternate',  hreflang: 'x-default', href: 'https://polychemmb.com/en' },
  ],
  meta: [
    { name: 'robots',              content: 'index, follow' },
    { name: 'author',              content: 'Polychem Corporation (Polychemmb)' },
    { property: 'og:locale',           content: 'en_US' },
    { property: 'og:locale:alternate', content: 'fa_IR' },
    { property: 'og:site_name',        content: 'Polychem | Polychemmb' },
  ],
  script: [
    {
      type: 'application/ld+json',
      key:  'website-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type':    'WebSite',
        '@id':      'https://polychemmb.com/#website',
        url:        'https://polychemmb.com',
        name:       'Polychem | Polychemmb',
        inLanguage: 'en',
        publisher:  { '@id': 'https://polychemmb.com/#organization' },
      }),
    },
    {
      type: 'application/ld+json',
      key:  'organization-schema',
      children: JSON.stringify({
        '@context':    'https://schema.org',
        '@type':       'Organization',
        '@id':         'https://polychemmb.com/#organization',
        name:          'Polychem Corporation',
        alternateName: 'Polychemmb',
        url:           'https://polychemmb.com',
        logo: {
          '@type':    'ImageObject',
          url:        'https://polychemmb.com/logo.png',
          contentUrl: 'https://polychemmb.com/logo.png',
        },
        address: {
          '@type':         'PostalAddress',
          addressLocality: 'Jolfa',
          addressRegion:   'East Azerbaijan',
          addressCountry:  'IR',
          description:     'Aras Free Zone',
        },
      }),
    },
    {
      type: 'application/ld+json',
      key:  'en-webpage-schema',
      children: JSON.stringify({
        '@context':  'https://schema.org',
        '@type':     'WebPage',
        '@id':       'https://polychemmb.com/en/#webpage',
        url:         'https://polychemmb.com/en',
        name:        'POLYCHEM | Masterbatch & Polymer Compound Manufacturer | Aras Free Zone Iran',
        description: 'POLYCHEM (Polychemmb) is Iran\'s leading manufacturer of masterbatch and polymer compounds located in Aras Free Zone.',
        inLanguage:  'en',
        isPartOf:    { '@id': 'https://polychemmb.com/#website' },
        about:       { '@id': 'https://polychemmb.com/#organization' },
        breadcrumb: {
          '@type': 'BreadcrumbList',
          itemListElement: [
            { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://polychemmb.com/en' },
          ],
        },
      }),
    },
  ],
})

// ─── Landing page ──────────────────────────────────────────────────────────────
// showLanding با false شروع می‌کنه → در SSR چیزی رندر نمی‌شه
// onMounted → sessionStorage چک می‌کنه → اگه ندیده true می‌شه
const showLanding = ref(false)
const router = useRouter()

const onLandingComplete = () => {
  sessionStorage.setItem('polychem_landing_seen', 'true')
  showLanding.value = false
}

onMounted(() => {
  localStorage.setItem('polychem_lang', 'en')

  const hasSeenLanding = sessionStorage.getItem('polychem_landing_seen')
  showLanding.value = !hasSeenLanding

  window.addEventListener('landing-complete', onLandingComplete)

  router.beforeEach((to, from, next) => {
    if (from.path === '/en' && to.path !== '/en') {
      sessionStorage.removeItem('homeScrollPosition_en')
    }
    next()
  })
})

onUnmounted(() => {
  window.removeEventListener('landing-complete', onLandingComplete)
})
</script>