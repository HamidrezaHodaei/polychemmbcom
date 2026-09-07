<!-- /components/fa/home/slider-mob.vue -->
<template>
  <ClientOnly>
    <div class="container mx-auto px-4">
      <div class="w-full">
        <div
          ref="cardsContainer"
          class="relative flex justify-center items-center h-[80vh] mb-24 mt-24 pt-20"
        >
        <div
          ref="card1"
          class="card-stack absolute w-[90%] h-auto rounded-[20px] shadow-2xl flex flex-col items-stretch overflow-hidden bg-white"
          style="top: 10%; z-index: 2;"
        >
          <div class="card-image w-full h-[300px] overflow-hidden rounded-t-[20px]">
            <img src="/ROTOCHEM-955W.webp" alt="Rotochem 0955W" class="w-full h-full object-cover filter grayscale" />
          </div>
          
          <div class="w-full p-6 flex flex-col justify-start gap-3 card-content bg-white min-h-[300px]">
            <h2 class="text-lg font-[Montserrat] text-[#848484] uppercase">Rotochem 0955W</h2>
            <p class="text-xs text-[#848484] font-[IRANYekan] text-right leading-relaxed" dir="rtl">
              یک آمیزه پلیمری تخصصی سفید رنگ است که برای کاربرد قالب‌گیری دورانی طراحی شده است. این محصول ترکیبی از گرید کوپلیمر پلی‌اتیلن با چگالی متوسط با توزیع وزن مولکولی باریک و دی‌اکسید تیتانیوم می‌باشد.
            </p>
            <NuxtLink to="/fa/products/0955W" class="btn-slide-down mt-2 w-full h-10 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors flex items-center justify-center">
              <span class="relative z-10 font-medium font-[IRANYekan] text-[14px]">مشاهده اطلاعات فنی</span>
            </NuxtLink>
          </div>
        </div>

        <div
          ref="card2"
          class="card-stack absolute w-[90%] h-auto rounded-[20px] shadow-2xl flex flex-col items-stretch overflow-hidden bg-white"
          style="top: 80px; z-index: 3;"
        >
          <div class="card-image w-full h-[300px] overflow-hidden rounded-t-[20px]">
            <img src="/POLYFILF700.webp" alt="POLYFIL F700" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full p-6 flex flex-col justify-start gap-3 card-content bg-white min-h-[300px]">
            <h2 class="text-lg font-[Montserrat] text-[#848484] uppercase">POLYFIL F700</h2>
            <p class="text-xs text-[#848484] font-[IRANYekan] text-right leading-relaxed" dir="rtl">
              یک کامپاند پلی‌اتیلن است که به‌طور ویژه برای کاربردهای فیلم دمشی پلی‌اتیلن سنگین فرموله شده است. این گرید به‌گونه‌ای طراحی شده که خواص مکانیکی مطلوب، یکنواختی عالی فیلم و فرآیندپذیری مناسب را حتی در تولید فیلم‌های بسیار نازک فراهم می‌کند.
            </p>
            <NuxtLink to="/fa/products/POLYFIL-F700" class="btn-slide-down mt-2 w-full h-10 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors flex items-center justify-center">
              <span class="relative z-10 font-medium font-[IRANYekan] text-[14px]">مشاهده اطلاعات فنی</span>
            </NuxtLink>
          </div>
        </div>

        <div
          ref="card3"
          class="card-stack absolute w-[90%] h-auto rounded-[20px] shadow-2xl flex flex-col items-stretch overflow-hidden bg-white"
          style="top: 60px; z-index: 4;"
        >
          <div class="card-image w-full h-[300px] overflow-hidden rounded-t-[20px]">
            <img src="/HDCHEM-4760.webp" alt="HDCHEM 4760" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full p-6 flex flex-col justify-start gap-3 card-content bg-white min-h-[300px]">
            <h2 class="text-lg font-[Montserrat] text-[#848484] uppercase">HDCHEM 4760</h2>
            <p class="text-xs text-[#848484] font-[IRANYekan] text-right leading-relaxed" dir="rtl">
              یک کامپاند پلاستیکی تخصصی است که برای کاربردهای قالب‌گیری بادی طراحی شده است. این محصول ترکیبی از کوپلیمرهای پلی‌اتیلنی بوده و دارای مجموعه‌ای از ویژگی‌های مطلوب و کاربردی برای قطعات صنعتی و بطری‌ها است.
            </p>
            <NuxtLink to="/fa/products/HDCHEM-4760" class="btn-slide-down mt-2 w-full h-10 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors flex items-center justify-center">
              <span class="relative z-10 font-medium font-[IRANYekan] text-[14px]">مشاهده اطلاعات فنی</span>
            </NuxtLink>
          </div>
        </div>

        <div
          ref="card4"
          class="card-stack absolute w-[90%] h-auto rounded-[20px] shadow-2xl flex flex-col items-stretch overflow-hidden bg-white"
          style="top: 90px; z-index: 5;"
        >
          <div class="card-image w-full h-[300px] overflow-hidden rounded-t-[20px]">
            <img src="/SLIPCHEM-E178.webp" alt="SLIPCHEM E178" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full p-6 flex flex-col justify-start gap-3 card-content bg-white min-h-[300px]">
            <h2 class="text-lg font-[Montserrat] text-[#848484] uppercase">SLIPCHEM E178</h2>
            <p class="text-xs text-[#848484] font-[IRANYekan] text-right leading-relaxed" dir="rtl">
              یک مستربچ‌ لیزکننده با عملکرد بالا است که حاوی عامل لغزنده با کیفیت بالا می‌باشد. این محصول به طور خاص برای کاهش ضریب اصطکاک بین لایه‌های فیلم در حین فرآیندهای رول پیچی، ساخت کیسه و بسته‌بندی توسعه یافته است.
            </p>
            <NuxtLink to="/fa/products/SlIPCHEM-E-178" class="btn-slide-down mt-2 w-full h-10 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors flex items-center justify-center">
              <span class="relative z-10 font-medium font-[IRANYekan] text-[14px]">مشاهده اطلاعات فنی</span>
            </NuxtLink>
          </div>
        </div>

        <div
          ref="card5"
          class="card-stack absolute w-[90%] h-auto rounded-[20px] shadow-2xl flex flex-col items-stretch overflow-hidden bg-white"
          style="top: 120px; z-index: 6;"
        >
          <div class="card-image w-full h-[300px] overflow-hidden rounded-t-[20px]">
            <img src="/RAFCOLOR-1560.webp" alt="RAFCOLOR 1560" class="w-full h-full object-cover filter grayscale" />
          </div>

          <div class="w-full p-6 flex flex-col justify-start gap-3 card-content bg-white min-h-[300px]">
            <h2 class="text-lg font-[Montserrat] text-[#848484] uppercase">RAFCOLOR 1560</h2>
            <p class="text-xs text-[#848484] font-[IRANYekan] text-right leading-relaxed" dir="rtl">
              یک مستربچ سفید بر پایه پلی پروپلین و درصد بالائی از تیتانیوم دی‌اکسید می باشد. در تولید این محصول از دی‌اکسید تیتانیوم مرغوب استفاده شده است. این مستربچ با پراکندگی عالی، برای تولید محصولات متنوع با پوشش‌دهی بالا قابل استفاده است.
            </p> 
            <NuxtLink to="/fa/products/RAFCOLOR-1560" class="btn-slide-down mt-2 w-full h-10 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors flex items-center justify-center">
              <span class="relative z-10 font-medium font-[IRANYekan] text-[14px]">مشاهده اطلاعات فنی</span>
            </NuxtLink>
          </div>
        </div>
        </div>
      </div>
    </div>
  </ClientOnly>
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
  // صبر برای مقدارگذاری DOM
  await nextTick()
  
  // پاک کردن تمام ScrollTrigger های قبلی
  ScrollTrigger.getAll().forEach(trigger => trigger.kill())
  
  // تنظیمات بهینه برای عملکرد روان
  gsap.config({
    force3D: true,
    nullTargetWarn: false
  })

  const cards = [card1.value, card2.value, card3.value, card4.value, card5.value]
  
  // تنظیم اولیه کارت‌ها
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

  // انیمیشن کارت اول (فقط fade in)
  mainTimeline.fromTo(card1.value, 
    { opacity: 0, y: 50 },
    { opacity: 1, y: 0, duration: 0.5 }
  )

  // کارت دوم ظاهر می‌شود
  mainTimeline.fromTo(card2.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.3'
  )
  
  // کارت اول عقب می‌رود
  mainTimeline.to(card1.value,
    { scale: 0.95, yPercent: -2, opacity: 0.7, duration: 1 },
    '<'
  )

  // کارت سوم ظاهر می‌شود
  mainTimeline.fromTo(card3.value,
    { yPercent: 100, opacity: 0 },
    { yPercent: 0, opacity: 1, duration: 1 },
    '+=0.3'
  )
  
  // کارت‌های قبلی عقب می‌روند
  mainTimeline.to([card1.value, card2.value],
    { 
      scale: (i) => 0.93 - (i * 0.02),
      yPercent: (i) => -4 + (i * 2),
      opacity: (i) => 0.6 + (i * 0.1),
      duration: 1 
    },
    '<'
  )

  // کارت چهارم ظاهر می‌شود
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

  // کارت پنجم ظاهر می‌شود
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

  // ایجاد ScrollTrigger با تنظیمات بهینه
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

  // Smooth scrolling برای مرورگرها
  ScrollTrigger.normalizeScroll(true)
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
  ScrollTrigger.getAll().forEach(trigger => trigger.kill())
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

.card-content::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 6px;
  background: #FFCD05;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  z-index: 1;
}

.card-image {
  background-color: #ffffff !important;
  position: relative;
  border-radius: 20px 20px 0 0 !important;
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

.card-content {
  border-radius: 0 0 20px 20px !important;
}
</style>