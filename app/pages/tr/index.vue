<!-- /pages/tr/index.vue -->
<template>
  <div>
    <Landpage v-if="showLanding && isClient" />

    <div v-show="!showLanding || !isClient">
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
      <Chatbox />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import Landpage from "~/components/layout/landpage.vue"
import Navbar from "~/components/tr/layout/navbar.vue"
import Hero from "~/components/tr/home/Hero.vue"
import Slider from "~/components/tr/home/Slider.vue"
import Text from "~/components/tr/home/Text.vue"
import Cards from "~/components/tr/home/cards.vue"
import Global from "~/components/tr/home/world.vue"
import InfinitySlider from "~/components/tr/home/InfiniteSlider.vue"
import Footer from "~/components/tr/layout/footer.vue"
import Chatbox from '~/components/tr/chatbox/chatbox.vue'

// ✅ SEO ترکی کامل
useSeoMeta({
  title: 'POLYCHEM | Masterbatch ve Polimer Bileşik Üreticisi | Aras Serbest Bölgesi İran',
  ogTitle: 'POLYCHEM | Masterbatch ve Polimer Bileşik Üreticisi | Aras Serbest Bölgesi İran',
  description: "POLYCHEM (Polychemmb) — İran'ın önde gelen renkli masterbatch, dolgu masterbatch (CaCO3), katkı masterbatch ve PP bileşik üreticisi. Aras Serbest Bölgesi'nde üretim, Orta Doğu ve Kafkasya'ya ihracat.",
  ogDescription: "İran'ın önde gelen masterbatch ve polimer bileşik ihracatçısı ve üreticisi. ISO 9001:2015 sertifikalı. Aras Serbest Bölgesi.",
  ogUrl: 'https://polychemmb.com/tr',
  ogType: 'website',
  ogImage: 'https://polychemmb.com/logo.png',
  twitterCard: 'summary_large_image',
  twitterTitle: 'POLYCHEM | Masterbatch ve Polimer Bileşik | İran',
  twitterDescription: "İran'ın önde gelen masterbatch üreticisi — renkli, dolgu, katkı masterbatch ve PP bileşik. Aras Serbest Bölgesi.",
})

useHead({
  htmlAttrs: { lang: 'tr', dir: 'ltr' },
  link: [
    { rel: 'canonical', href: 'https://polychemmb.com/tr' },
    { rel: 'alternate', hreflang: 'tr', href: 'https://polychemmb.com/tr' },
    { rel: 'alternate', hreflang: 'en', href: 'https://polychemmb.com/en' },
    { rel: 'alternate', hreflang: 'fa', href: 'https://polychemmb.com/fa' },
    { rel: 'alternate', hreflang: 'ar', href: 'https://polychemmb.com/ar' },
    { rel: 'alternate', hreflang: 'x-default', href: 'https://polychemmb.com/en' },
  ],
  meta: [
    { name: 'robots', content: 'index, follow' },
    {
      name: 'keywords',
      content: "masterbatch, renkli masterbatch, dolgu masterbatch, katkı masterbatch, polimer bileşik, PP bileşik, PP-Talk bileşik, masterbatch üreticisi İran, Polychem, Polychemmb, Aras Serbest Bölgesi, CaCO3 masterbatch, UV masterbatch, alev geciktirici masterbatch, antistatik masterbatch, mühendislik polimeri, plastik katkı maddeleri, masterbatch ihracatçısı İran"
    },
    { name: 'author', content: 'Polychem Corporation (Polychemmb)' },
    { property: 'og:locale', content: 'tr_TR' },
    { property: 'og:locale:alternate', content: 'en_US' },
    { property: 'og:site_name', content: 'Polychem | Polychemmb' },
  ],
  script: [
    {
      type: 'application/ld+json',
      key: 'tr-webpage-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'WebPage',
        '@id': 'https://polychemmb.com/tr/#webpage',
        url: 'https://polychemmb.com/tr',
        name: "POLYCHEM | Masterbatch ve Polimer Bileşik Üreticisi | Aras Serbest Bölgesi İran",
        description: "POLYCHEM (Polychemmb) — İran'ın önde gelen masterbatch ve polimer bileşik üreticisi. Aras Serbest Bölgesi.",
        inLanguage: 'tr',
        isPartOf: { '@id': 'https://polychemmb.com/#website' },
        about: { '@id': 'https://polychemmb.com/#organization' },
        breadcrumb: {
          '@type': 'BreadcrumbList',
          itemListElement: [
            {
              '@type': 'ListItem',
              position: 1,
              name: 'Ana Sayfa',
              item: 'https://polychemmb.com/tr',
            },
          ],
        },
        keywords: 'masterbatch, renkli masterbatch, dolgu masterbatch, polimer bileşik, PP bileşik, masterbatch üreticisi İran, Polychem, Polychemmb',
      }),
    },
  ],
})

const showLanding = ref(false)
const isClient = ref(false)
const router = useRouter()

const onLandingComplete = () => {
  sessionStorage.setItem('polychem_landing_seen', 'true')
  showLanding.value = false
}

onMounted(() => {
  isClient.value = true
  localStorage.setItem('polychem_lang', 'tr')

  const hasSeenLanding = sessionStorage.getItem('polychem_landing_seen')
  if (!hasSeenLanding) {
    showLanding.value = true
  }

  window.addEventListener('landing-complete', onLandingComplete)

  router.beforeEach((to, from, next) => {
    if (from.path === '/tr' && to.path !== '/tr') {
      sessionStorage.removeItem('homeScrollPosition_tr')
    }
    next()
  })
})

onUnmounted(() => {
  window.removeEventListener('landing-complete', onLandingComplete)
})
</script>