<template>
  <div class="container mx-auto px-4 font-[Montserrat] text-red-100">
    <div class="w-full">
      <div
        ref="cardsContainer"
        class="cards-wrapper relative flex justify-center items-center h-[80vh] mb-8 mt-8 pt-44 md:pt-44 pt-20"
      >
        <!-- Card 1 -->
        <div
          ref="card1"
          class="card-stack absolute w-[98%] h-[95%] lg:w-[85.5%] lg:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col lg:flex-row items-stretch overflow-hidden bg-white"
          style="top: 10%; z-index: 2;"
        >
          <div class="card-image w-full lg:w-3/5 h-[300px] lg:h-auto overflow-hidden rounded-t-[20px] lg:rounded-tl-[20px] lg:rounded-bl-[20px] lg:rounded-tr-[0px] lg:rounded-br-[0px]">
            <img src="/ROTOCHEM-955W.webp" alt="Product 1" class="w-full h-full object-cover filter grayscale" />
          </div>
          <div class="w-full lg:w-2/5 p-8 flex flex-col justify-start lg:justify-center gap-4 card-content bg-white min-h-[330px] lg:min-h-0">
            <h2 class="text-2xl md:text-3xl lg:text-4xl uppercase font-[Montserrat] text-[#848484]">ROTOCHEM 0955W</h2>
            <p class="text-sm md:text-base lg:text-lg text-[#848484] font-[Montserrat]">ROTOCHEM 0955W – White rotational molding compound based on MDPE copolymer with narrow MWD and TiO₂. Offering exceptional durability and superior UV resistance, it is the perfect choice for demanding industrial and consumer applications.</p>
            <a href="/en/products/0955W" class="btn-slide-down w-full lg:w-auto h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-[220px] flex items-center justify-center">
              <span class="relative z-10 font-medium">Technical Data Sheet</span>
            </a>
          </div>
        </div>

        <!-- Card 2 -->
        <div
          ref="card2"
          class="card-stack absolute w-[98%] h-[92%] lg:w-[85.5%] lg:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col lg:flex-row items-stretch overflow-hidden bg-white"
          style="top: 80px; z-index: 3;"
        >
          <div class="card-image w-full lg:w-3/5 h-[300px] lg:h-auto overflow-hidden rounded-t-[20px] lg:rounded-tl-[20px] lg:rounded-bl-[20px] lg:rounded-tr-[0px] lg:rounded-br-[0px]">
            <img src="/POLYFILF700.webp" alt="Product 2" class="w-full h-full object-cover filter grayscale" />
          </div>
          <div class="w-full lg:w-2/5 p-8 flex flex-col justify-start lg:justify-center gap-4 card-content bg-white min-h-[330px] lg:min-h-0">
            <h2 class="text-2xl md:text-3xl lg:text-4xl font-[Montserrat] text-[#848484]">POLYFIL F700</h2>
            <p class="text-sm md:text-base lg:text-lg text-[#848484] font-[Montserrat]">POLYFIL F700 – High-performance HDPE blown film compound offering superior strength, excellent film uniformity, and outstanding processability.</p>
            <a href="/en/products/POLYFIL-F700" class="btn-slide-down w-full lg:w-auto h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-[220px] flex items-center justify-center">
              <span class="relative z-10 font-medium">Technical Data Sheet</span>
            </a>
          </div>
        </div>

        <!-- Card 3 -->
        <div
          ref="card3"
          class="card-stack absolute w-[98%] h-[95%] lg:w-[85.5%] lg:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col lg:flex-row items-stretch overflow-hidden bg-white"
          style="top: 60px; z-index: 4;"
        >
          <div class="card-image w-full lg:w-3/5 h-[300px] lg:h-auto overflow-hidden rounded-t-[20px] lg:rounded-tl-[20px] lg:rounded-bl-[20px] lg:rounded-tr-[0px] lg:rounded-br-[0px]">
            <img src="/HDCHEM-4760.webp" alt="Product 3" class="w-full h-full object-cover filter grayscale" />
          </div>
          <div class="w-full lg:w-2/5 p-8 flex flex-col justify-start lg:justify-center gap-4 card-content bg-white min-h-[330px] lg:min-h-0">
            <h2 class="text-2xl md:text-3xl lg:text-4xl font-[Montserrat] text-[#848484] uppercase">HDCHEM 4760</h2>
            <p class="text-sm md:text-base lg:text-lg text-[#848484] font-[Montserrat]">HDCHEM 4760 – Specialized PE copolymer compound for blow molding applications. This polymer materials belong and good melt strength, balanced mechanical properties, and superior processability for industrial and consumer parts.</p>
            <a href="/en/products/HDCHEM-4760" class="btn-slide-down w-full lg:w-auto h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-[220px] flex items-center justify-center">
              <span class="relative z-10 font-medium">Technical Data Sheet</span>
            </a>
          </div>
        </div>

        <!-- Card 4 -->
        <div
          ref="card4"
          class="card-stack absolute w-[98%] h-[92%] lg:w-[85.5%] lg:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col lg:flex-row items-stretch overflow-hidden bg-white"
          style="top: 90px; z-index: 5;"
        >
          <div class="card-image w-full lg:w-3/5 h-[300px] lg:h-auto overflow-hidden rounded-t-[20px] lg:rounded-tl-[20px] lg:rounded-bl-[20px] lg:rounded-tr-[0px] lg:rounded-br-[0px]">
            <img src="/SLIPCHEM-E178.webp" alt="Product 4" class="w-full h-full object-cover filter grayscale" />
          </div>
          <div class="w-full lg:w-2/5 p-8 flex flex-col justify-start lg:justify-center gap-4 card-content bg-white min-h-[330px] lg:min-h-0">
            <h2 class="text-2xl md:text-3xl lg:text-4xl font-[Montserrat] text-[#848484]">SLIPCHEM-E 178</h2>
            <p class="text-sm md:text-base lg:text-lg text-[#848484] font-[Montserrat]">SlIPCHEM-E 178 – Premium slip masterbatch in PE carrier. Significantly lowers COF with excellent dispersion, high thermal stability, and consistent migration for film winding and packaging.</p>
            <a href="/en/products/SlIPCHEM-E-178" class="btn-slide-down w-full lg:w-auto h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-[220px] flex items-center justify-center">
              <span class="relative z-10 font-medium">Technical Data Sheet</span>
            </a>
          </div>
        </div>

        <!-- Card 5 -->
        <div
          ref="card5"
          class="card-stack absolute w-[98%] h-[95%] lg:w-[85.5%] lg:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col lg:flex-row items-stretch overflow-hidden bg-white"
          style="top: 120px; z-index: 6;"
        >
          <div class="card-image w-full lg:w-3/5 h-[300px] lg:h-auto overflow-hidden rounded-t-[20px] lg:rounded-tl-[20px] lg:rounded-bl-[20px] lg:rounded-tr-[0px] lg:rounded-br-[0px]">
            <img src="/RAFCOLOR-1560.webp" alt="Product 5" class="w-full h-full object-cover filter grayscale" />
          </div>
          <div class="w-full lg:w-2/5 p-8 flex flex-col justify-start lg:justify-center gap-4 card-content bg-white min-h-[330px] lg:min-h-0">
            <h2 class="text-2xl md:text-3xl lg:text-4xl font-[Montserrat] text-[#848484]">RAFCOLOR 1560</h2>
            <p class="text-sm md:text-base lg:text-lg text-[#848484] font-[Montserrat]">RAFCOLOR is a high-quality white masterbatch containing a high loading of rutile titanium dioxide (TiO₂) and thermoplastic polypropylene resin. The selected TiO₂ offers excellent opacity and dispersion properties.</p>
            <a href="/en/products/RAFCOLOR-1560" class="btn-slide-down w-full lg:w-auto h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-[220px] flex items-center justify-center">
              <span class="relative z-10 font-medium">Technical Data Sheet</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const cardsContainer = ref(null)
const card1 = ref(null)
const card2 = ref(null)
const card3 = ref(null)
const card4 = ref(null)
const card5 = ref(null)

let mainTimeline = null
let scrollTriggerInstance = null

const isMobile = () => window.innerWidth < 1024

const buildAnimation = () => {
  // پاک‌سازی فقط instance مربوط به همین کامپوننت
  if (scrollTriggerInstance) {
    scrollTriggerInstance.kill()
    scrollTriggerInstance = null
  }
  if (mainTimeline) {
    mainTimeline.kill()
    mainTimeline = null
  }

  const cards = [card1.value, card2.value, card3.value, card4.value, card5.value]

  // اگر هر کارتی null بود، ادامه نده
  if (cards.some(c => !c)) return

  gsap.set(cards, {
    clearProps: 'all'
  })

  gsap.set(cards, {
    willChange: 'transform, opacity',
    force3D: true
  })

  const mobile = isMobile()

  mainTimeline = gsap.timeline({ defaults: { ease: 'none', duration: 1 } })

  // کارت اول – fade in اولیه
  mainTimeline.fromTo(
    card1.value,
    { opacity: 0.6, y: 20 },
    { opacity: 1, y: 0, duration: 0.3 }
  )

  // کارت دوم
  mainTimeline.fromTo(
    card2.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.1'
  )
  mainTimeline.to(
    card1.value,
    { scale: 0.95, yPercent: -2, opacity: 0.7, duration: 1 },
    '<'
  )

  // کارت سوم
  mainTimeline.fromTo(
    card3.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.3'
  )
  mainTimeline.to(
    [card1.value, card2.value],
    {
      scale: i => 0.93 - i * 0.02,
      yPercent: i => -4 + i * 2,
      opacity: i => 0.6 + i * 0.1,
      duration: 1
    },
    '<'
  )

  // کارت چهارم
  mainTimeline.fromTo(
    card4.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.3'
  )
  mainTimeline.to(
    [card1.value, card2.value, card3.value],
    {
      scale: i => 0.91 - i * 0.02,
      yPercent: i => -6 + i * 2,
      opacity: i => 0.5 + i * 0.1,
      duration: 1
    },
    '<'
  )

  // کارت پنجم
  mainTimeline.fromTo(
    card5.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.3'
  )
  mainTimeline.to(
    [card1.value, card2.value, card3.value, card4.value],
    {
      scale: i => 0.89 - i * 0.02,
      yPercent: i => -8 + i * 2,
      opacity: i => 0.4 + i * 0.1,
      duration: 1
    },
    '<'
  )

  // ────────────────────────────────────────────────
  // مشکل اصلی ۱: onRefresh حذف شد (باعث loop بی‌نهایت میشد)
  // مشکل اصلی ۲: normalizeScroll حذف شد (اسکرول طبیعی را میدزدید)
  // مشکل اصلی ۳: ScrollTrigger.getAll().kill() حذف شد (همه trigger‌های صفحه را میکشت)
  // ────────────────────────────────────────────────
  scrollTriggerInstance = ScrollTrigger.create({
    trigger: cardsContainer.value,
    start: 'top top',
    end: mobile ? '+=2500' : '+=4000',
    pin: true,
    scrub: mobile ? 0.5 : 1.2,
    anticipatePin: mobile ? 0 : 1,
    invalidateOnRefresh: true,
    fastScrollEnd: mobile,
    preventOverlaps: true,
    animation: mainTimeline
  })
}

// resize handler با debounce برای جلوگیری از rebuild بیش از حد
let resizeTimer = null
const onResize = () => {
  clearTimeout(resizeTimer)
  resizeTimer = setTimeout(() => {
    buildAnimation()
  }, 300)
}

onMounted(async () => {
  await nextTick()

  gsap.config({
    force3D: true,
    nullTargetWarn: false
  })

  buildAnimation()

  window.addEventListener('resize', onResize, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('resize', onResize)
  clearTimeout(resizeTimer)

  if (scrollTriggerInstance) {
    scrollTriggerInstance.kill()
    scrollTriggerInstance = null
  }
  if (mainTimeline) {
    mainTimeline.kill()
    mainTimeline = null
  }
})
</script>

<style scoped>
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

input {
  background-color: #ffffff !important;
}

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
  -webkit-box-shadow: 0 0 0 1000px #ffffff inset !important;
  box-shadow: 0 0 0 1000px #ffffff inset !important;
  -webkit-text-fill-color: #111111 !important;
  caret-color: #111111;
  transition: background-color 5000s ease-in-out 0s;
}

.card-stack {
  will-change: transform, opacity;
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  perspective: 1000px;
  background-color: #ffffff !important;
  -webkit-transform: translate3d(0, 0, 0);
}

.btn-slide-down {
  background-color: transparent;
}

.btn-slide-down::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}

.btn-slide-down:hover::before,
.btn-slide-down:focus-visible::before {
  transform: translateY(0);
}

.btn-slide-down:hover,
.btn-slide-down:focus-visible {
  color: #ffffff;
  outline: none;
}

.card-content {
  background: #ffffff !important;
  position: relative;
  z-index: 1;
  color: #111827;
}

.card-content > * {
  position: relative;
  z-index: 2;
}

.card-content::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 6px;
  height: 100%;
  background: #FFCD05;
  z-index: 1;
}

@media (max-width: 1023px) {
  .card-content::before {
    left: 0;
    top: 0;
    width: 100%;
    height: 6px;
    border-radius: 0;
  }

  .card-stack {
    min-height: auto !important;
  }
}

.card-image {
  background-color: #ffffff !important;
  position: relative;
}

.card-image > img {
  display: block;
  background-color: #ffffff !important;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  transform: translate3d(0, 0, 0);
  transition: filter 300ms ease;
}

.card-stack:hover .card-image img {
  filter: grayscale(0) !important;
}

@media (max-width: 1023px) {
  .card-image {
    border-radius: 20px 20px 0 0 !important;
  }

  .card-content {
    border-radius: 0 0 20px 20px !important;
  }
}

/* Tablet */
@media (min-width: 768px) and (max-width: 1023px) {
  .cards-wrapper {
    height: auto !important;
    min-height: 700px;
    padding-top: 24px !important;
    margin-top: 16px !important;
    margin-bottom: 16px !important;
  }
}

/* موبایل */
@media (max-width: 767px) {
  .cards-wrapper {
    height: 75vh !important;
    padding-top: 16px !important;
    margin-top: 8px !important;
    margin-bottom: 8px !important;
    overscroll-behavior: none;
  }

  .card-stack {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
  }
}
</style>