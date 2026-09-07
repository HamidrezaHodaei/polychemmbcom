<!-- /tr/aboutus/index.vue -->
<template>
  <div>
    <ClientOnly>
      <navbar />
      <navbar-mob />
    </ClientOnly>
    
    <ClientOnly>
      <!-- Aboutus Hero Section -->
      <div class="flex items-center justify-center bg-[#f1f2f2] about-hero">
        <div class="w-full">
          <Aboutus />
        </div>
      </div>

      <!-- قسم الإحصائيات -->
<div class="bg-[#f1f2f2] stats-section" dir="rtl">
  <div class="max-w-7xl mx-auto px-4 py-8 md:py-16">
    <!-- 2x2 Grid -->
    <div class="grid grid-cols-2 md:grid-cols-2 gap-3 md:gap-6 mb-3 md:mb-6 max-w-5xl mx-auto">
      <!-- Kart 1 -->
      <div 
        class="bg-white rounded-xl p-4 md:p-12 shadow-sm relative overflow-hidden group hover:shadow-md transition-shadow duration-300 card-interactive min-h-[120px] md:min-h-auto"
        @mousemove="handleCardMouseMove"
        @mouseleave="handleCardMouseLeave"
        :ref="el => { if (el) cardRefs[0] = el }"
      >
        <div class="absolute inset-0 opacity-5 card-bg-characters" :ref="el => { if (el) bgRefs[0] = el }">
          {{ bgTexts[0] }}
        </div>
        <div class="absolute top-3 right-3 md:top-4 md:right-4 text-[#848484] opacity-20">
          <svg class="w-6 h-6 md:w-12 md:h-12" fill="currentColor" viewBox="0 0 24 24">
            <path d="M13 7h-2v4H7v2h4v4h2v-4h4v-2h-4V7zm-1-5C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/>
          </svg>
        </div>
        <div class="text-3xl md:text-6xl font-light text-[#848484] mb-2 md:mb-4 relative z-10 font-[Tajawal]">
          10<span class="text-xl md:text-4xl align-super">+</span>
        </div>
        <p class="text-[#848484] text-xs md:text-lg relative z-10 font-[Tajawal] leading-snug">سنوات الخبرة الإجمالية</p>
      </div>

      <!-- Kart 2 - Sarı -->
      <div 
        class="yellow-card rounded-xl p-4 md:p-12 shadow-sm relative overflow-hidden group hover:shadow-md transition-shadow duration-300 card-interactive min-h-[120px] md:min-h-auto"
        @mousemove="handleCardMouseMove"
        @mouseleave="handleCardMouseLeave"
        :ref="el => { if (el) cardRefs[1] = el }"
      >
        <div class="absolute inset-0 opacity-5 card-bg-characters" :ref="el => { if (el) bgRefs[1] = el }">
          {{ bgTexts[1] }}
        </div>
      </div>

      <!-- Kart 3 -->
      <div 
        class="bg-[#E8E6E6] rounded-xl p-4 md:p-12 shadow-sm relative overflow-hidden group hover:shadow-md transition-shadow duration-300 card-interactive min-h-[120px] md:min-h-auto"
        @mousemove="handleCardMouseMove"
        @mouseleave="handleCardMouseLeave"
        :ref="el => { if (el) cardRefs[2] = el }"
      >
        <div class="absolute inset-0 opacity-5 card-bg-characters" :ref="el => { if (el) bgRefs[2] = el }">
          {{ bgTexts[2] }}
        </div>
      </div>

      <!-- Kart 4 -->
      <div 
        class="bg-white rounded-xl p-4 md:p-12 shadow-sm relative overflow-hidden group hover:shadow-md transition-shadow duration-300 card-interactive min-h-[120px] md:min-h-auto"
        @mousemove="handleCardMouseMove"
        @mouseleave="handleCardMouseLeave"
        :ref="el => { if (el) cardRefs[3] = el }"
      >
        <div class="absolute inset-0 opacity-5 card-bg-characters" :ref="el => { if (el) bgRefs[3] = el }">
          {{ bgTexts[3] }}
        </div>
        <div class="absolute top-3 right-3 md:top-4 md:right-4 text-[#848484] opacity-20">
          <svg class="w-6 h-6 md:w-12 md:h-12" fill="currentColor" viewBox="0 0 24 24">
            <path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/>
          </svg>
        </div>
        <div class="text-3xl md:text-6xl font-light text-[#848484] mb-2 md:mb-4 relative z-10 font-[Tajawal]">
          4.3<span class="text-xl md:text-4xl align-super">%</span>
        </div>
        <p class="text-[#848484] text-xs md:text-lg relative z-10 font-[Tajawal] leading-snug">النمو العضوي</p>
      </div>
    </div>

    <!-- Alt Grid - 2 sütun mobilde, 3 sütun desktop -->
    <div class="grid grid-cols-2 md:grid-cols-3 gap-3 md:gap-6 max-w-5xl mx-auto">
      <div 
        v-for="(card, idx) in bottomCards"
        :key="idx + 4"
        :class="[
          'rounded-xl p-4 md:p-12 shadow-sm relative overflow-hidden group hover:shadow-md transition-shadow duration-300 card-interactive min-h-[120px] md:min-h-auto',

(idx === 1) ? 'yellow-card' :
          (card.value && ['24','50','84','32'].includes(card.value)) ? 'bg-white' : 'bg-[#E8E6E6]'
        ]"
        @mousemove="handleCardMouseMove"
        @mouseleave="handleCardMouseLeave"
        :ref="el => { if (el) cardRefs[idx + 4] = el }"
      >
        <div class="absolute inset-0 opacity-5 card-bg-characters" :ref="el => { if (el) bgRefs[idx + 4] = el }">
          {{ bgTexts[idx + 4] }}
        </div>
        <div v-if="card.icon" class="absolute top-3 right-3 md:top-4 md:right-4 text-[#848484] opacity-20">
          <svg class="w-6 h-6 md:w-12 md:h-12" fill="currentColor" viewBox="0 0 24 24">
            <path :d="card.icon"/>
          </svg>
        </div>
        <div class="text-3xl md:text-6xl font-light text-[#848484] mb-2 md:mb-4 relative z-10 font-[Tajawal]">
          {{ card.value }}<span class="text-xl md:text-4xl align-super">{{ card.unit }}</span>
        </div>
        <p class="text-[#848484] text-xs md:text-lg relative z-10 font-[Tajawal] leading-snug">{{ card.label }}</p>
      </div>
    </div>
  </div>
</div>

   <div class="py-10 md:py-20 px-4 bg-[#f1f2f2]" dir="rtl">
  <div class="max-w-7xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 md:gap-16 items-center">
      <!-- الصورة -->
      <div class="relative h-[220px] sm:h-[320px] md:h-[600px] rounded-2xl overflow-hidden order-2 lg:order-1">
        <div class="absolute inset-0 bg-gradient-to-t from-yellow-500/30 to-transparent z-10"></div>
        <img 
          src="/Aboutus/vision.webp" 
          alt="المصنع" 
          class="w-full h-full object-cover grayscale"
        />
      </div>
      <!-- النص -->
      <div class="font-[Tajawal] order-1 lg:order-2">
        <h2 class="text-2xl sm:text-3xl md:text-5xl lg:text-6xl text-[#848484] mb-4 md:mb-12 text-right font-[Tajawal]">الرؤية</h2>
        <p class="text-[#848484] text-sm md:text-lg mb-4 md:mb-8 leading-relaxed text-justify font-[Tajawal]">
          نحن في بولي كيم نتخيل مستقبلاً حيث تكون المواد البوليمرية المتقدمة مصدر إلهام لمنتجات أفضل وعمليات إنتاج أذكى وصناعة بلاستيكية أكثر استدامة.
        </p>
        <p class="text-[#848484] text-sm md:text-lg mb-4 md:mb-8 leading-relaxed text-justify font-[Tajawal]">
          هدفنا أن نكون الشريك الأكثر موثوقية في حلول المركبات عالية الأداء والماستر باتش. نطمح إلى أن نكون شركة معروفة بالابتكار والنزاهة والالتزام بالتميز.
        </p>
      </div>
    </div>
  </div>
</div>

      <!-- Scroll / Timeline Section -->
      <Scroll />
    </ClientOnly>

    <footer2 />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Aboutus from '~/components/ar/aboutus/Aboutus.vue'
import Scroll from '~/components/ar/aboutus/scroll.vue'
import footer2 from '~/components/ar/layout/footer.vue'
import navbar from '~/components/ar/layout/navbar.vue'
import navbarMob from '~/components/ar/layout/navbar-mob.vue'

const cardRefs = ref([])
const bgRefs = ref([])
const bgTexts = ref(Array(10).fill(''))

const bottomCards = [
  {
    value: '32',
    unit: '+',
    label: 'عدد العملاء',
    icon: 'M13 7h-2v4H7v2h4v4h2v-4h4v-2h-4V7zm-1-5C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z'
  },
  {
    value: '',
    unit: '',
    label: '',
    icon: null
  },
  {
    value: '84',
    unit: '%',
    label: 'رضا العملاء',
    icon: 'M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z'
  },
  {
    value: '',
    unit: '',
    label: '',
    icon: null
  },
  {
    value: '24',
    unit: '/7',
    label: 'الدعم على مدار الساعة',
    icon: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'
  },
  {
    value: '50',
    unit: '+',
    label: 'عدد الموظفين',
    icon: 'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z'
  }
]

useSeoMeta({
  title: 'عن بولي كيم | POLYCHEM',
  description: 'تعرف على المزيد عن بولي كيم، الشركة الرائدة في تصنيع المركبات البوليمرية والماستر باتش. اكتشف رؤيتنا وخبرتنا وقدراتنا الإنتاجية والتزامنا بالابتكار والاستدامة.',
  keywords: 'عن بولي كيم، مصنع المركبات البوليمرية، منتج الماستر باتش، صناعة البلاستيك، حلول البوليمر، شركة الماستر باتش',
  robots: 'index, follow',
  ogTitle: 'عن بولي كيم | المركبات البوليمرية المتقدمة والماستر باتش',
  ogDescription: 'استكشف رحلة بولي كيم ورؤيتنا وخبرتنا والتزامنا بتقديم مركبات بوليمرية عالية الأداء وحلول الماستر باتش في جميع أنحاء العالم.',
  ogType: 'website',
  ogUrl: 'https://polychemmb.com/ar/aboutus',
  ogSiteName: 'POLYCHEM',
  ogImage: 'https://polychemmb.com/Aboutus/vision.webp',
})

const randomDotsString = (length = 95000) => {
  const pair = '· '
  const repeats = Math.ceil(length / pair.length)
  return pair.repeat(repeats).substring(0, length)
}

const handleCardMouseMove = (e) => {
  if (!process.client) return
  const card = e.currentTarget
  const cardIndex = cardRefs.value.indexOf(card)
  if (cardIndex === -1 || !bgRefs.value[cardIndex]) return
  const rect = card.getBoundingClientRect()
  const x = e.clientX - rect.left
  const y = e.clientY - rect.top
  const bgEl = bgRefs.value[cardIndex]
  bgEl.style.setProperty('--x', `${x}px`)
  bgEl.style.setProperty('--y', `${y}px`)
  const cx = rect.width / 2
  const cy = rect.height / 2
  const maxOffset = 15
  const tx = ((x - cx) / cx) * maxOffset
  const ty = ((y - cy) / cy) * maxOffset
  bgEl.style.setProperty('--tx', `${tx}px`)
  bgEl.style.setProperty('--ty', `${ty}px`)
  bgEl.style.setProperty('--scale', '1.05')
  bgTexts.value[cardIndex] = randomDotsString(95000)
}

const handleCardMouseLeave = (e) => {
  if (!process.client) return
  const card = e.currentTarget
  const cardIndex = cardRefs.value.indexOf(card)
  if (cardIndex === -1 || !bgRefs.value[cardIndex]) return
  const bgEl = bgRefs.value[cardIndex]
  bgEl.style.setProperty('--tx', '0px')
  bgEl.style.setProperty('--ty', '0px')
  bgEl.style.setProperty('--scale', '1')
}

const updateNavbarHeightVar = () => {
  if (!process.client) return
  const navbarEl = document.querySelector('nav') || document.querySelector('.navbar') || document.querySelector('#navbar')
  let navHeight = navbarEl ? navbarEl.offsetHeight : 0
  if (!navHeight || navHeight < 40) navHeight = 80
  document.documentElement.style.setProperty('--navbar-height', `${navHeight}px`)
}

onMounted(() => {
  bgTexts.value = Array(10).fill(randomDotsString(95000))
  updateNavbarHeightVar()
  if (process.client) {
    window.addEventListener('resize', updateNavbarHeightVar)
  }
})

onUnmounted(() => {
  if (process.client) {
    window.removeEventListener('resize', updateNavbarHeightVar)
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

/* Font Faces - Tajawal */
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Light.ttf") format("truetype");
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Medium.ttf") format("truetype");
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Bold.ttf") format("truetype");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

.about-hero {
  font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;
  min-height: 100svh;
  padding-top: var(--navbar-height, 80px);
  box-sizing: border-box;
}

@media (min-width: 769px) {
  .about-hero {
    min-height: 100vh;
    padding-top: 0;
  }
}

.stats-section {
  /* No extra top margin needed on desktop */
}

@media (max-width: 768px) {
  .stats-section {
    padding-top: 0;
  }
}

.yellow-card {
  background-color: #faf0b7 !important;
}

.card-interactive {
  cursor: pointer;
}

.card-bg-characters {
  --x: 0px;
  --y: 0px;
  --tx: 0px;
  --ty: 0px;
  --scale: 1;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  word-wrap: break-word;
  font-size: 14px;
  line-height: 0.5;
  overflow: hidden;
  font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #a8a8a8;
  opacity: 0;
  transition: opacity 0.45s ease, transform 0.45s cubic-bezier(.2,.9,.3,1);
  will-change: transform, opacity;
  -webkit-mask-image: radial-gradient(
    250px circle at var(--x) var(--y),
    #000 15%,
    rgba(0, 0, 0, 0.3),
    transparent
  );
  mask-image: radial-gradient(
    250px circle at var(--x) var(--y),
    #000 15%,
    rgba(0, 0, 0, 0.3),
    transparent
  );
  transform: translate(var(--tx, 0px), var(--ty, 0px)) scale(var(--scale, 1.025));
  padding: 20px;
  z-index: 5;
}

.card-interactive:hover .card-bg-characters {
  opacity: 1;
}
</style>