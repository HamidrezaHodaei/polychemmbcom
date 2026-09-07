<!-- /components/ar/home/slider.vue -->

<template>
  <div class="container mx-auto px-4 font-[Tajawal] text-red-100" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;">
    <div class="w-full">
      <div
        ref="cardsContainer"
        class="relative flex justify-center items-center h-[80vh] mb-8 mt-8 pt-20 sm:pt-28 sm:h-[85vh] md:pt-44 md:h-[80vh]"
      >

        <!-- Kart 1 -->
        <div
          ref="card1"
          class="card-stack absolute w-[90%] h-auto sm:w-[88%] sm:h-[68vh] md:w-[85.5%] md:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col sm:flex-row md:flex-row items-stretch overflow-hidden bg-white"
          style="top: 10%; z-index: 2;"
        >
          <div class="card-image w-full h-[250px] sm:w-3/5 sm:h-auto md:w-3/5 md:h-auto overflow-hidden rounded-t-[20px] sm:rounded-t-none sm:rounded-tr-[20px] sm:rounded-br-[20px] md:rounded-tr-[20px] md:rounded-br-[20px] md:rounded-tl-[0px] md:rounded-bl-[0px]">
            <img src="/ROTOCHEM-955W.webp" alt="Ürün 1" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full sm:w-2/5 md:w-2/5 p-5 sm:p-6 md:p-8 flex flex-col justify-start sm:justify-center md:justify-center gap-3 sm:gap-3 md:gap-4 card-content bg-white min-h-[280px] sm:min-h-0 md:min-h-0">
            <h2 class="text-xl sm:text-2xl md:text-[30px] uppercase font-[Montserrat] text-[#848484] mb-0 sm:mb-2 md:mb-[20px]" style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;">ROTOCHEM 0955W</h2>
            <p class="text-sm sm:text-sm md:text-base lg:text-lg text-[#848484] font-[Tajawal] text-justify" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;" dir="rtl"><span style="font-family: 'Montserrat';">ROTOCHEM 0955W</span> – مركب تشكيل دوراني أبيض قائم على كوبوليمر MDPE يحتوي على MWD منخفض وثاني أكسيد التيتانيوم. يوفر متانة استثنائية ومقاومة عالية للأشعة فوق البنفسجية، مما يجعله اختيارًا مثاليًا للتطبيقات الصناعية والاستهلاكية الصعبة.</p>
            <a href="/ar/products/0955W" class="btn-slide-down mt-4 sm:mt-5 md:mt-[30px] ml-0 sm:ml-0 md:ml-[80px] w-full sm:w-auto md:w-auto h-11 sm:h-11 md:h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-full sm:max-w-[260px] md:max-w-[300px] flex items-center justify-center">
              <span class="relative z-10 font-medium" style="font-family: 'Tajawal', sans-serif; font-size: 15px;">ورقة البيانات التقنية</span>
            </a>
          </div>
        </div>

        <!-- Kart 2 -->
        <div
          ref="card2"
          class="card-stack absolute w-[90%] h-auto sm:w-[88%] sm:h-[68vh] md:w-[85.5%] md:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col sm:flex-row md:flex-row items-stretch overflow-hidden bg-white"
          style="top: 80px; z-index: 3;"
        >
          <div class="card-image w-full h-[250px] sm:w-3/5 sm:h-auto md:w-3/5 md:h-auto overflow-hidden rounded-t-[20px] sm:rounded-t-none sm:rounded-tr-[20px] sm:rounded-br-[20px] md:rounded-tr-[20px] md:rounded-br-[20px] md:rounded-tl-[0px] md:rounded-bl-[0px]">
            <img src="/POLYFILF700.webp" alt="Ürün 2" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full sm:w-2/5 md:w-2/5 p-5 sm:p-6 md:p-8 flex flex-col justify-start sm:justify-center md:justify-center gap-3 sm:gap-3 md:gap-4 card-content bg-white min-h-[280px] sm:min-h-0 md:min-h-0">
            <h2 class="text-xl sm:text-2xl md:text-[30px] font-[Montserrat] text-[#848484] mb-0 sm:mb-2 md:mb-[20px]" style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;">POLYFIL F700</h2>
            <p class="text-sm sm:text-sm md:text-base lg:text-lg text-[#848484] font-[Tajawal] text-justify" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;" dir="rtl"><span style="font-family: 'Montserrat';">POLYFIL F700</span> – مركب فيلم نفخ HDPE عالي الأداء يوفر قوة فائقة وتجانس فيلم مثالي وقابلية معالجة استثنائية.</p>
            <a href="/ar/products/POLYFIL-F700" class="btn-slide-down mt-4 sm:mt-5 md:mt-[30px] ml-0 sm:ml-0 md:ml-[80px] w-full sm:w-auto md:w-auto h-11 sm:h-11 md:h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-full sm:max-w-[260px] md:max-w-[300px] flex items-center justify-center">
              <span class="relative z-10 font-medium" style="font-family: 'Tajawal', sans-serif; font-size: 15px;">ورقة البيانات التقنية</span>
            </a>
          </div>
        </div>

        <!-- Kart 3 -->
        <div
          ref="card3"
          class="card-stack absolute w-[90%] h-auto sm:w-[88%] sm:h-[68vh] md:w-[85.5%] md:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col sm:flex-row md:flex-row items-stretch overflow-hidden bg-white"
          style="top: 60px; z-index: 4;"
        >
          <div class="card-image w-full h-[250px] sm:w-3/5 sm:h-auto md:w-3/5 md:h-auto overflow-hidden rounded-t-[20px] sm:rounded-t-none sm:rounded-tr-[20px] sm:rounded-br-[20px] md:rounded-tr-[20px] md:rounded-br-[20px] md:rounded-tl-[0px] md:rounded-bl-[0px]">
            <img src="/HDCHEM-4760.webp" alt="Ürün 3" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full sm:w-2/5 md:w-2/5 p-5 sm:p-6 md:p-8 flex flex-col justify-start sm:justify-center md:justify-center gap-3 sm:gap-3 md:gap-4 card-content bg-white min-h-[280px] sm:min-h-0 md:min-h-0">
            <h2 class="text-xl sm:text-2xl md:text-[30px] font-[Montserrat] text-[#848484] uppercase mb-0 sm:mb-2 md:mb-[20px]" style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;">HDCHEM 4760</h2>
            <p class="text-sm sm:text-sm md:text-base lg:text-lg text-[#848484] font-[Tajawal] text-justify" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;" dir="rtl"><span style="font-family: 'Montserrat';">HDCHEM 4760</span> – مركب كوبوليمر PE طُوّر خصيصًا لتطبيقات النفخ والتشكيل. يوفر هذا المادة البوليمرية قوة انصهار جيدة وخصائص ميكانيكية متوازنة وقابلية معالجة فائقة لأجزاء الصناعة والمستهلك.</p>
            <a href="/ar/products/HDCHEM-4760" class="btn-slide-down mt-4 sm:mt-5 md:mt-[30px] ml-0 sm:ml-0 md:ml-[80px] w-full sm:w-auto md:w-auto h-11 sm:h-11 md:h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-full sm:max-w-[260px] md:max-w-[300px] flex items-center justify-center">
              <span class="relative z-10 font-medium" style="font-family: 'Tajawal', sans-serif; font-size: 15px;">ورقة البيانات التقنية</span>
            </a>
          </div>
        </div>

        <!-- Kart 4 -->
        <div
          ref="card4"
          class="card-stack absolute w-[90%] h-auto sm:w-[88%] sm:h-[68vh] md:w-[85.5%] md:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col sm:flex-row md:flex-row items-stretch overflow-hidden bg-white"
          style="top: 90px; z-index: 5;"
        >
          <div class="card-image w-full h-[250px] sm:w-3/5 sm:h-auto md:w-3/5 md:h-auto overflow-hidden rounded-t-[20px] sm:rounded-t-none sm:rounded-tr-[20px] sm:rounded-br-[20px] md:rounded-tr-[20px] md:rounded-br-[20px] md:rounded-tl-[0px] md:rounded-bl-[0px]">
            <img src="/SLIPCHEM-E178.webp" alt="Ürün 4" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full sm:w-2/5 md:w-2/5 p-5 sm:p-6 md:p-8 flex flex-col justify-start sm:justify-center md:justify-center gap-3 sm:gap-3 md:gap-4 card-content bg-white min-h-[280px] sm:min-h-0 md:min-h-0">
            <h2 class="text-xl sm:text-2xl md:text-[30px] font-[Montserrat] text-[#848484] mb-0 sm:mb-2 md:mb-[20px]" style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;">SLIPCHEM-E 178</h2>
            <p class="text-sm sm:text-sm md:text-base lg:text-lg text-[#848484] font-[Tajawal] text-justify" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;" dir="rtl"><span style="font-family: 'Montserrat';">SLIPCHEM-E 178</span> – ماستربتش انزلاق فاخر يعتمد على PE. يقلل قيمة COF بشكل كبير لتطبيقات لف الأفلام والتعبئة والتغليف؛ يوفر تشتتًا ممتازًا واستقرارًا حراريًا عاليًا وهجرة متسقة.</p>
            <a href="/ar/products/SlIPCHEM-E-178" class="btn-slide-down mt-4 sm:mt-5 md:mt-[30px] ml-0 sm:ml-0 md:ml-[80px] w-full sm:w-auto md:w-auto h-11 sm:h-11 md:h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-full sm:max-w-[260px] md:max-w-[300px] flex items-center justify-center">
              <span class="relative z-10 font-medium" style="font-family: 'Tajawal', sans-serif; font-size: 15px;">ورقة البيانات التقنية</span>
            </a>
          </div>
        </div>

        <!-- Kart 5 -->
        <div
          ref="card5"
          class="card-stack absolute w-[90%] h-auto sm:w-[88%] sm:h-[68vh] md:w-[85.5%] md:h-[76.5vh] rounded-[20px] shadow-2xl flex flex-col sm:flex-row md:flex-row items-stretch overflow-hidden bg-white"
          style="top: 120px; z-index: 6;"
        >
          <div class="card-image w-full h-[250px] sm:w-3/5 sm:h-auto md:w-3/5 md:h-auto overflow-hidden rounded-t-[20px] sm:rounded-t-none sm:rounded-tr-[20px] sm:rounded-br-[20px] md:rounded-tr-[20px] md:rounded-br-[20px] md:rounded-tl-[0px] md:rounded-bl-[0px]">
            <img src="/RAFCOLOR-1560.webp" alt="Ürün 5" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full sm:w-2/5 md:w-2/5 p-5 sm:p-6 md:p-8 flex flex-col justify-start sm:justify-center md:justify-center gap-3 sm:gap-3 md:gap-4 card-content bg-white min-h-[280px] sm:min-h-0 md:min-h-0">
            <h2 class="text-xl sm:text-2xl md:text-3xl font-[Montserrat] text-[#848484] mb-0 sm:mb-2 md:mb-[20px]" style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;">RAFCOLOR 1560</h2>
            <p class="text-sm sm:text-sm md:text-base lg:text-lg text-[#848484] font-[Tajawal] text-justify" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;" dir="rtl"><span style="font-family: 'Montserrat';">RAFCOLOR 1560</span> – ماستربتش أبيض عالي الجودة يحتوي على نسبة عالية من ثاني أكسيد التيتانيوم روتيل (TiO₂) وراتينج بولي بروبيلين حراري. يوفر ثاني أكسيد التيتانيوم المختار خصائص تعتيم وتشتت ممتازة.</p>
            <a href="/ar/products/RAFCOLOR-1560" class="btn-slide-down mt-4 sm:mt-5 md:mt-[30px] ml-0 sm:ml-0 md:ml-[80px] w-full sm:w-auto md:w-auto h-11 sm:h-11 md:h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors max-w-full sm:max-w-[260px] md:max-w-[300px] flex items-center justify-center">
              <span class="relative z-10 font-medium" style="font-family: 'Tajawal', sans-serif; font-size: 15px;">ورقة البيانات التقنية</span>
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

onMounted(async () => {
  await nextTick()
  
  gsap.config({
    force3D: true,
    nullTargetWarn: false
  })

  const cards = [card1.value, card2.value, card3.value, card4.value, card5.value]
  
  gsap.set(cards, {
    willChange: 'transform, opacity',
    force3D: true
  })

  mainTimeline = gsap.timeline({
    defaults: {
      ease: 'none',
      duration: 1
    }
  })

  mainTimeline.fromTo(card1.value, 
    { opacity: 0.6, y: 20 },
    { opacity: 1, y: 0, duration: 0.3 }
  )

  mainTimeline.fromTo(card2.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.1'
  )
  
  mainTimeline.to(card1.value,
    { scale: 0.95, yPercent: -2, opacity: 0.7, duration: 1 },
    '<'
  )

  mainTimeline.fromTo(card3.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.3'
  )
  
  mainTimeline.to([card1.value, card2.value],
    { 
      scale: (i) => 0.93 - (i * 0.02),
      yPercent: (i) => -4 + (i * 2),
      opacity: (i) => 0.6 + (i * 0.1),
      duration: 1 
    },
    '<'
  )

  mainTimeline.fromTo(card4.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.3'
  )
  
  mainTimeline.to([card1.value, card2.value, card3.value],
    { 
      scale: (i) => 0.91 - (i * 0.02),
      yPercent: (i) => -6 + (i * 2),
      opacity: (i) => 0.5 + (i * 0.1),
      duration: 1 
    },
    '<'
  )

  mainTimeline.fromTo(card5.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.3'
  )
  
  mainTimeline.to([card1.value, card2.value, card3.value, card4.value],
    { 
      scale: (i) => 0.89 - (i * 0.02),
      yPercent: (i) => -8 + (i * 2),
      opacity: (i) => 0.4 + (i * 0.1),
      duration: 1 
    },
    '<'
  )

  scrollTriggerInstance = ScrollTrigger.create({
    trigger: cardsContainer.value,
    start: 'top top',
    end: '+=4000',
    pin: true,
    scrub: 1.2,
    anticipatePin: 1,
    invalidateOnRefresh: true,
    animation: mainTimeline
  })

})

onUnmounted(() => {
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
/* Font Faces - Tajawal */
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-ExtraLight.ttf") format("truetype");
  font-weight: 200;
  font-style: normal;
  font-display: swap;
}

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

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-ExtraBold.ttf") format("truetype");
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Black.ttf") format("truetype");
  font-weight: 900;
  font-style: normal;
  font-display: swap;
}

/* Font Faces - Montserrat */
@font-face {
  font-family: "Montserrat";
  src: url("/Fonts/Montserrat-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Montserrat";
  src: url("/Fonts/Montserrat-Bold.ttf") format("truetype");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

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
  perspective: 1000px;
  background-color: #ffffff !important;
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

/* بوردر زرد سمت چپ — دقیقاً مثل نسخه فارسی */
.card-content::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 6px;
  height: 100%;
  background: #FFCD05;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
  z-index: 1;
}

/* تبلت و موبایل — بوردر بالا */
@media (max-width: 1023px) {
  .card-content::before {
    left: 0;
    top: 0;
    width: 100%;
    height: 6px;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }

  .card-stack {
    min-height: auto !important;
  }

  .card-image {
    border-radius: 20px 20px 0 0 !important;
  }

  .card-content {
    border-radius: 0 0 20px 20px !important;
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .card-stack {
    width: 92% !important;
    height: auto !important;
    min-height: auto !important;
    flex-direction: column !important;
  }

  .card-image {
    width: 100% !important;
    height: 280px !important;
  }

  .card-content {
    width: 100% !important;
    min-height: 280px !important;
    padding: 1.25rem 1.5rem !important;
    justify-content: flex-start !important;
  }

  .btn-slide-down {
    width: 100% !important;
    max-width: 100% !important;
    margin-left: 0 !important;
  }
}

@media (max-width: 767px) {
  .card-stack {
    min-height: auto !important;
    width: 90% !important;
    height: auto !important;
    flex-direction: column !important;
  }

  .card-image {
    width: 100% !important;
    height: 250px !important;
    border-radius: 20px 20px 0 0 !important;
  }

  .btn-slide-down {
    width: 100% !important;
    max-width: 100% !important;
    margin-left: 0 !important;
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
  transform: translate3d(0, 0, 0);
  transition: filter 300ms ease;
}

.card-stack:hover .card-image img {
  filter: grayscale(0) !important;
}
</style>