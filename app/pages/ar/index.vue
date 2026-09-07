<!-- /pages/ar/index.vue  ← مهم: فایل باید در /pages/ar/ باشه نه /pages/ -->
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
import Navbar from "~/components/ar/layout/navbar.vue"
import Hero from "~/components/ar/home/Hero.vue"
import Slider from "~/components/ar/home/Slider.vue"
import Text from "~/components/ar/home/Text.vue"
import Cards from "~/components/ar/home/cards.vue"
import Global from "~/components/ar/home/world.vue"
import InfinitySlider from "~/components/ar/home/InfiniteSlider.vue"
import Footer from "~/components/ar/layout/footer.vue"
import Chatbox from '~/components/ar/chatbox/chatbox.vue'

// ✅ SEO عربی کامل
useSeoMeta({
  title: 'پلیکم | الشركة الرائدة في صناعة الماسترباتش ومركبات البوليمر | منطقة آراس الحرة',
  ogTitle: 'پلیکم | الشركة الرائدة في صناعة الماسترباتش ومركبات البوليمر | منطقة آراس الحرة',
  description: 'شركة POLYCHEM (پلیکم)، الشركة الرائدة في منطقة آراس الحرة بإيران في إنتاج ماسترباتش ملون عالي الجودة، وماسترباتش الحشو (كربونات الكالسيوم)، وماسترباتش الإضافات، ومركبات البولي بروبيلين الهندسية. التصدير إلى الشرق الأوسط والقوقاز.',
  ogDescription: 'الشركة الرائدة والمصدرة لمنتجات الماسترباتش ومركبات البوليمر في إيران. حاصلة على شهادة ISO 9001:2015.',
  ogUrl: 'https://polychemmb.com/ar',
  ogType: 'website',
  ogImage: 'https://polychemmb.com/logo.png',
  twitterCard: 'summary_large_image',
  twitterTitle: 'پلیکم | ماسترباتش ومركبات البوليمر | إيران',
  twitterDescription: 'الشركة الرائدة في تصنيع الماسترباتش الملون والحشو والإضافات في منطقة آراس الحرة بإيران.',
})

useHead({
  // ✅ عربی — dir باید rtl باشه (نه 'lar')
  htmlAttrs: { lang: 'ar', dir: '' },
  link: [
    { rel: 'canonical', href: 'https://polychemmb.com/ar' },
    { rel: 'alternate', hreflang: 'ar', href: 'https://polychemmb.com/ar' },
    { rel: 'alternate', hreflang: 'en', href: 'https://polychemmb.com/en' },
    { rel: 'alternate', hreflang: 'fa', href: 'https://polychemmb.com/fa' },
    { rel: 'alternate', hreflang: 'tr', href: 'https://polychemmb.com/tr' },
    { rel: 'alternate', hreflang: 'x-default', href: 'https://polychemmb.com/en' },
  ],
  meta: [
    { name: 'robots', content: 'index, follow' },
    {
      name: 'keywords',
      content: 'ماسترباتش, ماسترباتش ملون, ماسترباتش الحشو, ماسترباتش الإضافات, مركبات البوليمر, مركب PP, مصنع ماسترباتش إيران, بولي كيم, Polychem, Polychemmb, منطقة آراس الحرة, كربونات الكالسيوم ماسترباتش, ماسترباتش مقاوم للأشعة فوق البنفسجية, ماسترباتش مقاوم للحرائق, بولي بروبيلين مركب, بوليمر هندسي, ماسترباتش مضاد للكهرباء الساكنة'
    },
    { name: 'author', content: 'Polychem Corporation (Polychemmb) | پلیکم' },
    { property: 'og:locale', content: 'ar_IQ' },
    { property: 'og:locale:alternate', content: 'en_US' },
    { property: 'og:site_name', content: 'پلیکم| Polychem' },
  ],
  script: [
    {
      type: 'application/ld+json',
      key: 'ar-webpage-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'WebPage',
        '@id': 'https://polychemmb.com/ar/#webpage',
        url: 'https://polychemmb.com/ar',
        name: 'پلیكم | الشركة الرائدة في صناعة الماسترباتش ومركبات البوليمر | منطقة آراس الحرة',
        description: 'شركة POLYCHEM (بولي كيم) — الشركة الرائدة في إيران في تصنيع الماسترباتش ومركبات البوليمر.',
        inLanguage: 'ar',
        isPartOf: { '@id': 'https://polychemmb.com/#website' },
        about: { '@id': 'https://polychemmb.com/#organization' },
        breadcrumb: {
          '@type': 'BreadcrumbList',
          itemListElement: [
            {
              '@type': 'ListItem',
              position: 1,
              name: 'الصفحة الرئيسية',
              item: 'https://polychemmb.com/ar',
            },
          ],
        },
        keywords: 'ماسترباتش, ماسترباتش ملون, مركبات البوليمر, مصنع ماسترباتش إيران, بولي كيم, Polychem, Polychemmb',
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
  localStorage.setItem('polychem_lang', 'ar')

  const hasSeenLanding = sessionStorage.getItem('polychem_landing_seen')
  if (!hasSeenLanding) {
    showLanding.value = true
  }

  if (!hasSeenLanding) {
    sessionStorage.removeItem('homeScrollPosition_ar')
  }

  window.addEventListener('landing-complete', onLandingComplete)

  router.beforeEach((to, from, next) => {
    if (from.path === '/ar' && to.path !== '/ar') {
      sessionStorage.removeItem('homeScrollPosition_ar')
    }
    next()
  })
})

onUnmounted(() => {
  // ✅ cleanup صحیح — process.client چک نیاز نیست چون onUnmounted فقط client-side اجرا میشه
  window.removeEventListener('landing-complete', onLandingComplete)
})
</script>