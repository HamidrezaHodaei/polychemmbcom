<!-- /pages/fa/index.vue -->
<template>
  <div>
    <Navbar />
    <Hero />
    <div class="mt-8">
      <SliderDesktop />
      <Text />
      <Cards />
      <Global />
      <InfinitySlider />
    </div>
    <Footer />
    <Chatbox />
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import Navbar from "~/components/fa/layout/navbar.vue"
import Hero from "~/components/fa/home/Hero.vue"
import SliderDesktop from "~/components/fa/home/Slider.vue"
import Text from "~/components/fa/home/Text.vue"
import Cards from "~/components/fa/home/cards.vue"
import Global from "~/components/fa/home/world.vue"
import InfinitySlider from "~/components/fa/home/InfiniteSlider.vue"
import Footer from "~/components/fa/layout/footer.vue"
import Chatbox from '~/components/fa/chatbox/chatbox.vue'

// ✅ SEO فارسی کامل
useSeoMeta({
  title: 'پلیکم | تولیدکننده مستربچ و کامپاند پلیمری | پلیمرشیمی ارس',
  ogTitle: 'پلیکم | تولیدکننده مستربچ و کامپاند پلیمری | پلیمرشیمی ارس',
  description: 'پلیکم (پلیمرشیمی ارس) تولیدکننده تخصصی مستربچ پرکننده (کربنات کلسیم)، مستربچ افزودنی، کامپاند مهندسی و مستربچ رنگی در منطقه آزاد ارس ایران. صادرات به خاورمیانه.',
  ogDescription: 'پلیکم (پلیمرشیمی ارس) — تولیدکننده و صادرکننده پیشرو مستربچ و کامپاند پلیمری در ایران. منطقه آزاد ارس، جلفا.',
  ogUrl: 'https://polychemmb.com/fa',
  ogType: 'website',
  ogImage: 'https://polychemmb.com/logo.png',
  twitterCard: 'summary_large_image',
  twitterTitle: 'پلیکم | مستربچ و کامپاند پلیمر | پلیمرشیمی ارس',
  twitterDescription: 'تولیدکننده مستربچ رنگی، پرکننده و افزودنی در منطقه آزاد ارس ایران.',
})

useHead({
  // ✅ فارسی — dir باید rtl باشه
  htmlAttrs: { lang: 'fa', dir: '' },
  link: [
    { rel: 'canonical', href: 'https://polychemmb.com/fa' },
    { rel: 'alternate', hreflang: 'fa', href: 'https://polychemmb.com/fa' },
    { rel: 'alternate', hreflang: 'en', href: 'https://polychemmb.com/en' },
    { rel: 'alternate', hreflang: 'ar', href: 'https://polychemmb.com/ar' },
    { rel: 'alternate', hreflang: 'tr', href: 'https://polychemmb.com/tr' },
    { rel: 'alternate', hreflang: 'x-default', href: 'https://polychemmb.com/en' },
  ],
  meta: [
    { name: 'robots', content: 'index, follow' },
    {
      name: 'keywords',
      content: 'پلیکم, پلی کم, پلی‌کم, پلیمرشیمی ارس, پلیمر شیمی ارس, مستربچ, مستربچ رنگی, مستربچ پرکننده, مستربچ افزودنی, کامپاند پلیمر, کامپاند PP, کامپاند پلی پروپیلن, تولیدکننده مستربچ, تولیدکننده مستربچ ایران, مستربچ ایران, مستربچ ارس, منطقه آزاد ارس, کربنات کلسیم مستربچ, CaCO3 مستربچ, رنگ‌دهنده پلاستیک, افزودنی پلاستیک, Polychem, Polychemmb, masterbatch Iran'
    },
    { name: 'author', content: 'پلی‌کم — Polychem Corporation' },
    { property: 'og:locale', content: 'fa_IR' },
    { property: 'og:locale:alternate', content: 'en_US' },
    { property: 'og:site_name', content: 'پلیکم | پلیمرشیمی ارس' },
  ],
  script: [
    // ✅ Schema فارسی اختصاصی
    {
      type: 'application/ld+json',
      key: 'fa-webpage-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'WebPage',
        '@id': 'https://polychemmb.com/fa/#webpage',
        url: 'https://polychemmb.com/fa',
        name: 'پلیکم | تولیدکننده مستربچ و کامپاند پلیمر | پلیمرشیمی ارس',
        description: 'پلیکم (پلیمرشیمی ارس) تولیدکننده تخصصی مستربچ رنگی، مستربچ پرکننده، مستربچ افزودنی و کامپاند PP در منطقه آزاد ارس ایران.',
        inLanguage: 'fa',
        isPartOf: { '@id': 'https://polychemmb.com/#website' },
        about: { '@id': 'https://polychemmb.com/#organization' },
        breadcrumb: {
          '@type': 'BreadcrumbList',
          itemListElement: [
            {
              '@type': 'ListItem',
              position: 1,
              name: 'صفحه اصلی',
              item: 'https://polychemmb.com/fa',
            },
          ],
        },
        keywords: 'پلیکم, پلیمرشیمی ارس, مستربچ, مستربچ رنگی, مستربچ پرکننده, کامپاند PP, تولیدکننده مستربچ ایران',
        speakable: {
          '@type': 'SpeakableSpecification',
          cssSelector: ['h1', 'h2', '.hero-description'],
        },
      }),
    },
  ],
})

const isMobile = ref(false)

const checkMobile = () => {
  if (process.client) {
    isMobile.value = window.innerWidth < 768
  }
}

onMounted(() => {
  sessionStorage.removeItem('homeScrollPosition_fa')
  localStorage.setItem('polychem_lang', 'fa')
  checkMobile()
  window.addEventListener('resize', checkMobile)
})

onBeforeUnmount(() => {
  if (process.client) {
    window.removeEventListener('resize', checkMobile)
  }
})
</script>