<!-- /pages/ar/products/126FP.vue -->
<template>  <div dir="rtl" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;">  <!-- ===================================================================== -->
  <!-- MOBILE LAYOUT                                                          -->
  <!-- ===================================================================== -->
  <div v-if="isMobile" class="page-wrap">
    <!-- Top navbar: logo + PRODUCTS menu + language switcher -->
    <nav class="navbar">
      <div class="logo-container">
        <a @click.prevent="goHome" class="block cursor-pointer">
          <img src="/english logo W1.png" alt="شعار بوليكم" class="logo" />
        </a>
      </div>

      <div class="right-section">
        <button class="menu-btn" @click="goToProducts">
          المنتجات
        </button>

        <div class="divider"></div>

        <button class="lang-selector-btn" @click="toggleLangMenu">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
      </div>
    </nav>

    <!-- Language dropdown -->
    <transition name="slide">
      <div v-if="langMenuOpen" class="glass-menu-fullscreen">
        <div class="menu-scroll-wrapper">
          <ul class="menu-list">
            <li class="menu-item" :class="{ active: currentLang === 'en' }" @click="handleLangClick('en')">ENGLISH</li>
            <li class="menu-item font-iranyekan" :class="{ active: currentLang === 'ar' }" @click="handleLangClick('ar')">العربية</li>
            <li class="menu-item font-iranyekan" :class="{ active: currentLang === 'fa' }" @click="handleLangClick('fa')">فارسی</li>
            <li class="menu-item" :class="{ active: currentLang === 'tr' }" @click="handleLangClick('tr')">TÜRKÇE</li>
          </ul>
        </div>
      </div>
    </transition>

    <!-- Product detail content -->
    <div class="content-below-navbar">
      <div class="px-5 pt-6 pb-4">
        <p v-if="product.brand" class="text-[11px] tracking-widest text-gray-400 uppercase mb-1">{{ product.brand }}</p>
        <h1 class="text-2xl font-semibold text-gray-900 mb-4">{{ product.title }}</h1>

        <div class="mb-6">
          <h4 class="text-xs font-semibold tracking-[0.2em] text-[#898989] uppercase mb-2">{{ product.subtitleTitle }}</h4>
          <p class="text-gray-700 leading-relaxed text-sm whitespace-pre-line">{{ product.subtitle }}</p>
        </div>
      </div>

      <img :src="product.detailImage" :alt="product.title" class="w-full block" loading="lazy" />

      <div class="bg-[#A8A8A8] text-white px-5 py-8">
        <h3 class="font-semibold tracking-widest text-lg mb-6 text-[#FFCD05]">المواصفات الفنية</h3>
        <div class="space-y-3">
          <div
            v-for="(spec, idx) in product.specs"
            :key="idx"
            class="bg-white/10 rounded-lg px-4 py-3 grid grid-cols-2 gap-x-3 gap-y-1 text-xs"
          >
            <span class="col-span-2 font-semibold text-white text-sm mb-1">{{ spec.property }}</span>
            <span class="text-[#FFCD05] font-medium tracking-wide uppercase">Test Method</span>
            <span class="text-white/80">{{ spec.testMethod }}</span>
            <span class="text-[#FFCD05] font-medium tracking-wide uppercase">Unit</span>
            <span class="text-white/80">{{ spec.unit }}</span>
            <span class="text-[#FFCD05] font-medium tracking-wide uppercase">Typical Value</span>
            <span class="text-white font-semibold">{{ spec.typicalValue }}</span>
          </div>
        </div>
      </div>

      <div class="bg-[#f6f6f6] text-[#3d3d3d] px-5 py-8">
        <div v-for="(section, idx) in product.detailSections" :key="section.title || idx" class="mb-6 last:mb-0">
          <h4 class="text-xs font-semibold tracking-[0.2em] text-[#898989] uppercase mb-2">{{ section.title }}</h4>
          <p class="text-sm leading-relaxed whitespace-pre-line">{{ section.body }}</p>
        </div>
      </div>

      <!-- CTA buttons at the bottom -->
      <div class="px-5 py-6 bg-page-bg">
        <div class="cta-stack-mobile">
          <div class="cta-pair-mobile">
            <button class="cta-btn btn-slide-down" @click="goToRequestSample">
              <span>طلب عينة</span>
            </button>
            <a
              :href="product.dataSheet"
              target="_blank"
              rel="noopener noreferrer"
              class="cta-btn cta-btn-filled btn-slide-down-reverse"
            >
              <span>تحميل صحيفة البيانات</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- DESKTOP LAYOUT                                                         -->
  <!-- ===================================================================== -->
  <div v-else class="page">
    <div class="shell">
      <header class="header">
        <nav class="nav">
          <button class="nav-item" @click="goHome">
            <svg class="home-icon" width="17" height="17" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 11.5L12 4l9 7.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M5 10v9a1 1 0 001 1h4v-6h4v6h4a1 1 0 001-1v-9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>الرئيسية</span>
          </button>
          <a class="nav-item effect-1-yellow" href="#" title="المنتجات" @click.prevent="goToProducts">
            <span class="btn-text">المنتجات</span>
            <span class="btn-arrow">→</span>
          </a>
        </nav>

        <div class="logo">
          <img src="/Polychem-1.png" alt="شعار بوليكم" class="logo-image" />
        </div>

        <div class="header-actions">
          <button class="lang-btn" @click="toggleLangMenu">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
              <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8" />
              <path d="M3 12h18M12 3c2.5 2.7 3.8 6 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-6-3.8-9s1.3-6.3 3.8-9z" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
            </svg>
            <span>{{ currentLang === 'en' ? 'ENGLISH' : currentLang.toUpperCase() }}</span>
          </button>
        </div>
      </header>

      <!-- Language dropdown (desktop) -->
      <transition name="slide">
        <div v-if="langMenuOpen" class="desktop-menu-panel">
          <ul class="desktop-menu-list">
            <li class="desktop-menu-item" :class="{ active: currentLang === 'en' }" @click="handleLangClick('en')">ENGLISH</li>
            <li class="desktop-menu-item" :class="{ active: currentLang === 'ar' }" @click="handleLangClick('ar')">العربية</li>
            <li class="desktop-menu-item" :class="{ active: currentLang === 'fa' }" @click="handleLangClick('fa')">فارسی</li>
            <li class="desktop-menu-item" :class="{ active: currentLang === 'tr' }" @click="handleLangClick('tr')">TÜRKÇE</li>
          </ul>
        </div>
      </transition>

      <main class="main-grid">
        <div class="left-col">
          <div class="hero-image">
            <img :src="product.heroImage" :alt="product.title + ' - صورة المنتج'" class="hero-photo" loading="lazy" />
          </div>
        </div>

        <div class="right-col">
          <h1 class="title">{{ product.title }}</h1>
          <p class="desc">{{ product.subtitle }}</p>

          <ul v-if="product.featureList && product.featureList.length" class="feature-list">
            <li v-for="(feature, idx) in product.featureList" :key="idx">{{ feature }}</li>
          </ul>

          <div class="cta-row">
            <button class="add-to-cart btn-slide-down" @click="goToRequestSample">
              <span>طلب عينة</span>
            </button>
            <a
              :href="product.dataSheet"
              target="_blank"
              rel="noopener noreferrer"
              class="gpay btn-slide-down-reverse"
            >
              <span>تحميل صحيفة البيانات</span>
            </a>
          </div>
        </div>

        <div class="specs-box">
          <div class="specs-accordion">
            <div v-for="spec in specs" :key="spec.id" class="spec-item">
              <button class="spec-head" @click="toggleSpec(spec.id)">
                <span>{{ spec.title }}</span>
                <span class="spec-icon" :class="{ open: spec.open }">+</span>
              </button>
              <div v-if="spec.open" class="spec-body">
                <p v-if="spec.content" class="spec-text">{{ spec.content }}</p>

                <div v-if="spec.isTable" class="tech-specs">
                  <div class="tech-specs-header">
                    <span>Property</span>
                    <span>Test Method</span>
                    <span>Unit</span>
                    <span>Typical Value</span>
                  </div>
                  <div v-for="(row, idx) in techSpecs" :key="idx" class="tech-specs-row">
                    <div class="tech-specs-property">{{ row.property }}</div>
                    <div>{{ row.testMethod }}</div>
                    <div>{{ row.unit }}</div>
                    <div class="tech-specs-value">{{ row.typicalValue }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useLang } from '~/composables/useLang'

const router = useRouter()
const { switchLang, currentLang } = useLang()

const SITE_URL = 'https://www.polychemmb.com'
const PAGE_PATH = '/ar/products/126FP'

// ─── Mobile detection ──────────────────────────────────────────────
const isMobile = ref(false)
const checkMobile = () => {
  if (typeof window === 'undefined') return false
  return window.innerWidth < 768
}

const cartCount = ref(0)
const langMenuOpen = ref(false)

const toggleLangMenu = () => {
  langMenuOpen.value = !langMenuOpen.value
  if (process.client) document.body.style.overflow = langMenuOpen.value ? 'hidden' : ''
}

const handleLangClick = (lang) => {
  langMenuOpen.value = false
  if (process.client) document.body.style.overflow = ''
  switchLang(lang)
}

const goHome = () => {
  const lang = currentLang.value || 'ar'
  if (process.client && typeof window !== 'undefined') {
    window.location.assign(`/${lang}`)
    return
  }
  router.push(`/${lang}`)
}

const goToProducts = () => {
  const lang = currentLang.value || 'ar'
  const target = `/${lang}/products`

  if (process.client && typeof window !== 'undefined') {
    window.location.assign(target)
    return
  }

  router.push(target)
}

const goToRequestSample = () => {
  const lang = currentLang.value || 'ar'
  if (process.client && typeof window !== 'undefined') {
    window.location.href = `/${lang}/request-sample`
    return
  }
  router.push(`/${lang}/request-sample`)
}

// ─── Product data (CALCICHEM 126 FP only) ─────────────────────────────────
const product = {
  "title": "CALCICHEM 126 FP",
  "brand": "",
  "subtitleTitle": "الوصف",
  "subtitle": "CALCICHEM 126 FP هو ماستر باتش حشو على قاعدة بولي بروبيلين يحتوي على 80% كربونات الكالسيوم (CaCO₃) بجسيمات ناعمة جداً ومُغلَّفة.",
  "detailImage": "/Product/index/calcum-126.webp",
  "heroImage": "/Product/index/calcum-126.webp",
  "featureList": [],
  "detailSections": [
    {
      "title": "المميزات",
      "body": "▪ زيادة سرعة الإنتاج\n▪ تقليل امتصاص الرطوبة\n▪ تحسين التوصيل الحراري\n▪ تعزيز خاصية مانع الالتصاق (Anti-blocking)\n▪ تحسين قابلية الطباعة على المنتج النهائي\n▪ استقرار الأداء طوال عملية الإنتاج"
    },
    {
      "title": "التغليف",
      "body": "يُعرض CALCICHEM 126 FP على شكل حبيبات قياسية في أكياس سعة 25 كيلوغرام."
    },
    {
      "title": "التخزين والمناولة",
      "body": "يجب تخزين CALCICHEM 126 FP بعيداً عن أشعة الشمس المباشرة والحرارة. يُستخدم خلال 18 شهراً من تاريخ الإنتاج."
    }
  ],
  "specs": [
    {
      "property": "نسبة كربونات الكالسيوم",
      "testMethod": "ASTM D4218",
      "unit": "%",
      "typicalValue": "80 ± 2"
    },
    {
      "property": "نسبة الرطوبة",
      "testMethod": "ASTM D644",
      "unit": "ppm",
      "typicalValue": "≤ 1500"
    },
    {
      "property": "مؤشر تدفق المصهور (230°C / 2.16 kg)",
      "testMethod": "ASTM D1238",
      "unit": "g/10min",
      "typicalValue": "6 ± 2"
    },
    {
      "property": "الكثافة عند 23°C",
      "testMethod": "ASTM D1505",
      "unit": "g/cm³",
      "typicalValue": "1.85 ± 0.05"
    }
  ],
  "dataSheet": "/Product/Datasheet-AR/CALCICHEM 126 FP Ar.pdf"
}

// ─── Desktop accordion specs (same content as product.specs / sections) ──
const specs = ref([
  { id: 'advantage', title: product.detailSections[0].title, content: product.detailSections[0].body, open: true },
  { id: 'packaging', title: product.detailSections[1].title, content: product.detailSections[1].body, open: true },
  { id: 'storage_and_handling', title: product.detailSections[2] ? product.detailSections[2].title : '', content: product.detailSections[2] ? product.detailSections[2].body : '', open: true },
  { id: 'techspecs', title: 'المواصفات الفنية', isTable: true, open: true },
])

function toggleSpec(id) {
  const item = specs.value.find((s) => s.id === id)
  if (item) item.open = !item.open
}

const techSpecs = ref(product.specs)

onMounted(() => {
  isMobile.value = checkMobile()
  window.addEventListener('resize', () => { isMobile.value = checkMobile() })
})

onUnmounted(() => {
  if (process.client) document.body.style.overflow = ''
})

// ───────────────────────────────────────────────────────────────────
// SEO — meta tags, Open Graph, Twitter Card, canonical, hreflang, JSON-LD
// ───────────────────────────────────────────────────────────────────
const pageTitle = 'CALCICHEM 126 FP | پلیکم (پلیمر شیمی ارس)'
const pageDescription = 'CALCICHEM 126 FP هو ماستر باتش حشو على قاعدة بولي بروبيلين يحتوي على 80% كربونات الكالسيوم (CaCO₃) بجسيمات ناعمة جداً ومُغلَّفة.'
const ogImage = `${SITE_URL}${product.heroImage}`
const canonicalUrl = `${SITE_URL}${PAGE_PATH}`

useSeoMeta({
  title: pageTitle,
  description: pageDescription,
  ogTitle: pageTitle,
  ogDescription: pageDescription,
  ogImage,
  ogType: 'website',
  ogUrl: canonicalUrl,
  ogLocale: 'ar_AR',
  ogSiteName: 'Polychem',
  twitterCard: 'summary_large_image',
  twitterTitle: pageTitle,
  twitterDescription: pageDescription,
  twitterImage: ogImage,
  robots: 'index, follow',
})

const productJsonLd = computed(() => ({
  '@context': 'https://schema.org',
  '@type': 'Product',
  name: product.title,
  description: product.subtitle,
  image: ogImage,
  brand: {
    '@type': 'Organization',
    name: 'Polychem',
  },
  manufacturer: {
    '@type': 'Organization',
    name: 'Polychem',
    url: SITE_URL,
  },
  additionalProperty: product.specs.map((spec) => ({
    '@type': 'PropertyValue',
    name: spec.property,
    value: spec.typicalValue,
    unitText: spec.unit,
  })),
}))

const breadcrumbJsonLd = computed(() => ({
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'الرئيسية', item: `${SITE_URL}/ar` },
    { '@type': 'ListItem', position: 2, name: 'المنتجات', item: `${SITE_URL}/ar/products` },
    { '@type': 'ListItem', position: 3, name: product.title, item: canonicalUrl },
  ],
}))

useHead({
  link: [
    { rel: 'canonical', href: canonicalUrl },
    { rel: 'alternate', hreflang: 'en', href: `${SITE_URL}/en/products/126FP` },
    { rel: 'alternate', hreflang: 'fa', href: `${SITE_URL}/fa/products/126FP` },
    { rel: 'alternate', hreflang: 'ar', href: `${SITE_URL}/ar/products/126FP` },
    { rel: 'alternate', hreflang: 'tr', href: `${SITE_URL}/tr/products/126FP` },
    { rel: 'alternate', hreflang: 'x-default', href: `${SITE_URL}/en/products/126FP` },
  ],
  script: [
    { type: 'application/ld+json', innerHTML: JSON.stringify(productJsonLd.value) },
    { type: 'application/ld+json', innerHTML: JSON.stringify(breadcrumbJsonLd.value) },
  ],
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');

@font-face {
  font-family: 'IRANYekan';
  src: url('/Fonts/IRANYekan.ttf') format('truetype');
}

* { box-sizing: border-box; }

/* ===================================================================== */
/* SHARED — Data sheet button animation (used both mobile & desktop)      */
/* ===================================================================== */
.btn-slide-down { background-color: transparent; }
.btn-slide-down::before {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 100%; height: 100%;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}
.btn-slide-down:hover::before,
.btn-slide-down:focus-visible::before { transform: translateY(0); }
.btn-slide-down:hover,
.btn-slide-down:focus-visible { color: #ffffff; outline: none; }
.btn-slide-down > span { position: relative; z-index: 1; }

/* Same slide animation, colors reversed: yellow background -> white on hover */
.btn-slide-down-reverse {
  position: relative;
  overflow: hidden;
  background-color: #FFCD05;
  color: #ffffff;
  border: 2px solid #FFCD05;
  box-sizing: border-box;
}
.btn-slide-down-reverse:hover,
.btn-slide-down-reverse:focus-visible { border-color: #FFCD05; }
.btn-slide-down-reverse::before {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 100%; height: 100%;
  background-color: #ffffff;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}
.btn-slide-down-reverse:hover::before,
.btn-slide-down-reverse:focus-visible::before { transform: translateY(0); }
.btn-slide-down-reverse:hover,
.btn-slide-down-reverse:focus-visible { color: #FFCD05; outline: none; }
.btn-slide-down-reverse > span { position: relative; z-index: 1; }

/* ===================================================================== */
/* MOBILE                                                                 */
/* ===================================================================== */
.page-wrap {
  min-height: 100vh;
  padding-bottom: calc(120px + env(safe-area-inset-bottom, 0px));
  background: #f1f2f2;
  font-family: 'IRANYekan', 'Montserrat', 'Tahoma', sans-serif;
  direction: rtl;
  text-align: right;
}

.navbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  width: 100%;
  height: 64px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 16px;
  background: #808285;
  border: none;
  z-index: 1000;
}

.logo-container { display: flex; align-items: center; }
.logo { width: 150px; height: auto; object-fit: contain; filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.1)); }

.right-section { display: flex; align-items: center; gap: 0; }

.menu-btn {
  background: transparent;
  border: none;
  color: #ffffff;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.5px;
  padding: 8px 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 4px;
  min-width: 90px;
  text-align: center;
}
.menu-btn:hover { background: rgba(255, 255, 255, 0.15); }

.divider { width: 1px; height: 20px; background-color: #ffffff; margin: 0 6px; }

.lang-selector-btn {
  background: transparent;
  border: none;
  color: #ffffff;
  padding: 8px;
  cursor: pointer;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.lang-selector-btn:hover { background: rgba(255, 255, 255, 0.15); }
.lang-selector-btn svg { width: 18px; height: 18px; }

.content-below-navbar { padding-top: 64px; }

.bg-page-bg { background-color: #f1f2f2; }

.cta-stack-mobile {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 24px;
}

.cta-pair-mobile {
  display: flex;
  gap: 10px;
}

.cta-btn {
  width: 100%;
  height: 46px;
  background-color: transparent;
  color: #FFCD05;
  border: 2px solid #FFCD05;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: color 300ms ease;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
  min-width: 0;
}

.cta-btn-filled {
  background-color: #FFCD05;
  color: #ffffff;
  border: 2px solid #FFCD05;
}

.glass-menu-fullscreen {
  position: fixed;
  top: 64px; left: 0; right: 0; bottom: 0;
  width: 100%;
  height: calc(100vh - 64px);
  background-color: hsla(0, 0%, 81%, 0.4);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: none;
  box-shadow: 0 -4px 32px 0 rgba(0, 0, 0, 0.1);
  z-index: 9999999;
  overflow-y: auto;
  overflow-x: hidden;
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
}

.menu-scroll-wrapper { width: 100%; min-height: 100%; padding: 16px 20px 80px 20px; display: block; }
.menu-list { list-style: none; padding: 0; margin: 0 auto; width: 100%; max-width: 600px; }

.menu-item {
  color: #1a1a1a;
  font-size: 18px;
  font-weight: 400;
  letter-spacing: 1px;
  padding: 18px 15px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
  border-radius: 12px;
  margin: 8px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  -webkit-tap-highlight-color: transparent;
  min-height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.menu-item:last-child { border-bottom: none; }
.menu-item:hover, .menu-item:active { background: rgba(255, 255, 255, 0.3); transform: scale(1.02); }
.menu-item.active { background: rgba(255, 255, 255, 0.4); font-weight: 600; }

.font-iranyekan { font-family: 'IRANYekan', 'Montserrat', sans-serif; font-size: 20px; }

.slide-enter-active, .slide-leave-active { transition: all 0.4s ease; }
.slide-enter-from { opacity: 0; transform: translateY(-20px); }
.slide-leave-to { opacity: 0; transform: translateY(-20px); }

h1, h2, h3, h4, h5, h6, .tracking-widest { word-spacing: -0.10em; }
h2 { word-spacing: -0.08em; }

/* ===================================================================== */
/* DESKTOP                                                                */
/* ===================================================================== */
.page {
  min-height: 100vh;
  background: #f1f2f2;
  padding: 24px;
  font-family: 'IRANYekan', 'Montserrat', 'Tahoma', sans-serif;
  direction: rtl;
  text-align: right;
  display: flex;
  justify-content: center;
}

.shell {
  width: 100%;
  max-width: 1400px;
  background: #f6f6f6;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.06);
  position: relative;
}

.header {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 18px 40px;
  background: #fbfbfa;
  border-bottom: 1px solid #e5e5e5;
}

.logo { display: flex; align-items: center; justify-content: center; }
.header-actions { justify-self: end; }
.logo-image { height: 36px; width: auto; display: block; }

.nav { display: flex; align-items: center; gap: 32px; }

.nav-item {
  display: flex;
  align-items: center;
  gap: 6px;
  background: none;
  border: none;
  font-size: 15px;
  color: #3d3d3d;
  cursor: pointer;
  font-weight: 500;
  text-decoration: none;
}

.home-icon { flex-shrink: 0; }

.effect-1-yellow {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 132px;
  height: 44px;
  border-radius: 999px;
  background-color: #FFCD05;
  color: #ffffff;
  font-weight: 700;
  font-size: 14px;
  text-decoration: none;
  overflow: hidden;
  box-shadow: 0 4px 14px rgba(255, 205, 5, 0.35);
  transition: background-color 0.25s ease;
}

.effect-1-yellow .btn-text { transition: transform 0.25s ease; }
.effect-1-yellow .btn-arrow {
  position: absolute;
  right: 16px;
  font-size: 15px;
  opacity: 0;
  transform: translateX(10px);
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.header-actions { display: flex; align-items: center; gap: 14px; }

.desktop-menu-panel {
  position: absolute;
  top: 78px;
  left: 0;
  right: 0;
  z-index: 500;
  background: hsla(0, 0%, 100%, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid #e5e5e5;
  max-height: 60vh;
  overflow-y: auto;
  padding: 20px 40px;
}

.desktop-menu-list {
  list-style: none;
  margin: 0 auto;
  padding: 0;
  max-width: 900px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.desktop-menu-item {
  color: #1a1a1a;
  font-size: 15px;
  font-weight: 500;
  letter-spacing: 0.3px;
  padding: 14px 16px;
  cursor: pointer;
  text-align: center;
  border-radius: 10px;
  background: #ffffff;
  border: 1px solid #ececec;
  transition: all 0.2s ease;
}
.desktop-menu-item:hover { border-color: #FFCD05; color: #b58a00; }
.desktop-menu-item.active { background: #FFCD05; color: #ffffff; border-color: #FFCD05; }

.main-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 24px;
  padding: 24px 40px 48px;
}

.left-col { display: flex; flex-direction: column; gap: 24px; height: 100%; }

.hero-image {
  background: transparent;
  border-radius: 20px;
  min-height: 420px;
  height: 100%;
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  overflow: hidden;
}

.hero-photo {
  width: 100%;
  height: 100%;
  min-height: 420px;
  border-radius: 20px;
  object-fit: cover;
  object-position: center;
  display: block;
  background: #fff;
}

.specs-box { grid-column: 1 / -1; background: #ffffff; border-radius: 20px; padding: 28px 32px; }

.specs-accordion { width: 100%; }
.spec-item { border-bottom: 1px solid #ececec; }
.spec-item:last-child { border-bottom: none; }

.spec-head {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: none;
  border: none;
  padding: 16px 0;
  font-size: 15px;
  font-weight: 700;
  color: #1a1a1a;
  cursor: pointer;
  text-align: left;
}

.spec-icon { font-size: 18px; font-weight: 400; color: #FFCD05; transition: transform 0.2s ease; flex-shrink: 0; }
.spec-icon.open { transform: rotate(45deg); }

.spec-body { padding: 0 0 18px; }
.spec-text { font-size: 14px; line-height: 1.7; color: #444; margin: 0; white-space: pre-line; }

.tech-specs { background: #A8A8A8; color: #fff; border-radius: 14px; padding: 20px 24px; margin-top: 12px; }

.tech-specs-header {
  display: grid;
  grid-template-columns: 1.4fr 1fr 0.6fr 1fr;
  gap: 12px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #FFCD05;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
}

.tech-specs-row {
  display: grid;
  grid-template-columns: 1.4fr 1fr 0.6fr 1fr;
  gap: 12px;
  padding: 14px 0;
  font-size: 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.85);
}
.tech-specs-row:last-child { border-bottom: none; }
.tech-specs-property { font-weight: 600; color: rgba(255, 255, 255, 0.95); }
.tech-specs-value { font-weight: 700; color: #fff; }

.right-col { background: #ffffff; border-radius: 20px; padding: 40px; display: flex; flex-direction: column; }

.title { font-size: 40px; font-weight: 500; letter-spacing: 0.01em; margin: 0 0 18px; color: #1a1a1a; }
.desc { font-size: 16px; line-height: 1.6; color: #4b5563; margin: 0 0 16px; max-width: 560px; white-space: pre-line; }

.feature-list { background: #f1f2f2; border-radius: 16px; padding: 24px 28px; margin: 0 0 24px; list-style: disc; }
.feature-list li { font-size: 16px; color: #1f1f1f; margin-bottom: 14px; padding-left: 4px; }
.feature-list li:last-child { margin-bottom: 0; }

.cta-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 30px;
}

.add-to-cart {
  flex: 1;
  background-color: transparent;
  color: #FFCD05;
  border: 2px solid #FFCD05;
  border-radius: 999px;
  padding: 18px 20px;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: 0.02em;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: color 300ms ease;
}

.gpay {
  flex: 1;
  background: #FFCD05;
  color: #fff;
  border: 2px solid #FFCD05;
  border-radius: 999px;
  padding: 18px 20px;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  text-decoration: none;
}

.lang-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 44px;
  padding: 0 14px;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 999px;
  background: #fff;
  color: #1a1a1a;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.03em;
  cursor: pointer;
  transition: background 0.2s ease, border-color 0.2s ease, transform 0.15s ease;
}
.lang-btn svg { flex-shrink: 0; opacity: 0.75; transition: opacity 0.2s ease; }
.lang-btn:active { transform: scale(0.96); }

@media (hover: hover) and (pointer: fine) {
  .effect-1-yellow:hover { background-color: #e6b800; }
  .effect-1-yellow:hover .btn-text { transform: translateX(-9px); }
  .effect-1-yellow:hover .btn-arrow { opacity: 1; transform: translateX(0); }

  .lang-btn:hover { background: #f5f5f5; border-color: rgba(0, 0, 0, 0.18); }
  .lang-btn:hover svg { opacity: 1; }
}

@media (max-width: 1024px) {
  .main-grid { grid-template-columns: 1fr; padding: 20px; }
  .left-col { height: auto; }
  .hero-image { flex: none; min-height: 320px; }
  .right-col { padding: 28px; }
  .desktop-menu-list { grid-template-columns: repeat(2, 1fr); }
}
</style>