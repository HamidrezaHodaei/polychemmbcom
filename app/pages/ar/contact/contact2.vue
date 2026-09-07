<template>
  <div
    class="w-full min-h-screen bg-[#f1f2f2]"
    style="height: 400vh; font-family: system-ui, -apple-system, sans-serif"
  >
    <h1
      class="relative text-center pt-24 text-2xl md:text-3xl px-4 text-[#A8A8A8]"
    >
      Scroll to see the timeline animation
    </h1>

    <svg
      id="svg-stage"
      ref="svgStage"
      class="w-full mx-auto mt-[60vh] overflow-visible px-4"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 1400 1200"
      preserveAspectRatio="xMidYMid meet"
    >
      <!-- خطوط افقی -->
      <path
        class="line01 line"
        d="M 0 200 1400 200"
        fill="none"
        stroke="#A8A8A8"
        stroke-width="2"
      ></path>
      <path
        class="line02 line"
        d="M 0 400 1400 400"
        fill="none"
        stroke="#A8A8A8"
        stroke-width="2"
      ></path>
      <path
        class="line03 line"
        d="M 0 600 1400 600"
        fill="none"
        stroke="#A8A8A8"
        stroke-width="2"
      ></path>
      <path
        class="line04 line"
        d="M 0 800 1400 800"
        fill="none"
        stroke="#A8A8A8"
        stroke-width="2"
      ></path>
      <path
        class="line05 line"
        d="M 0 1000 1400 1000"
        fill="none"
        stroke="#A8A8A8"
        stroke-width="2"
      ></path>

      <!-- متن‌های سال سمت چپ -->
      <text
        class="text01"
        x="30"
        y="190"
        fill="#A8A8A8"
        font-size="15"
        style="visibility: hidden"
      >
        2018
      </text>
      <text
        class="text02"
        x="30"
        y="390"
        fill="#A8A8A8"
        font-size="15"
        style="visibility: hidden"
      >
        2019
      </text>
      <text
        class="text03"
        x="30"
        y="590"
        fill="#A8A8A8"
        font-size="15"
        style="visibility: hidden"
      >
        2020
      </text>
      <text
        class="text04"
        x="30"
        y="790"
        fill="#A8A8A8"
        font-size="15"
        style="visibility: hidden"
      >
        2021
      </text>
      <text
        class="text05"
        x="30"
        y="990"
        fill="#A8A8A8"
        font-size="15"
        style="visibility: hidden"
      >
        2022
      </text>

      <!-- متن‌های توضیحات سمت راست -->
      <text
        class="desc01"
        x="1350"
        y="175"
        fill="#A8A8A8"
        font-size="15"
        text-anchor="end"
        style="visibility: hidden"
      >
        Project Launch
      </text>
      <text
        class="desc02"
        x="1350"
        y="375"
        fill="#A8A8A8"
        font-size="15"
        text-anchor="end"
        style="visibility: hidden"
      >
        Team Growth
      </text>
      <text
        class="desc03"
        x="1350"
        y="575"
        fill="#A8A8A8"
        font-size="15"
        text-anchor="end"
        style="visibility: hidden"
      >
        First Product
      </text>
      <text
        class="desc04"
        x="1350"
        y="775"
        fill="#A8A8A8"
        font-size="15"
        text-anchor="end"
        style="visibility: hidden"
      >
        Global Expansion
      </text>
      <text
        class="desc05"
        x="1350"
        y="975"
        fill="#A8A8A8"
        font-size="15"
        text-anchor="end"
        style="visibility: hidden"
      >
        Major Success
      </text>

      <!-- مسیر اصلی که از تمام خطوط عبور می‌کند -->
      <path
        class="theLine"
        d="M 100,0 Q 900 100 700 200 Q 500 300 700 400 Q 900 500 700 600 Q 500 700 700 800 Q 900 900 700 1000 Q 500 1100 700 1200"
        fill="none"
        stroke="#A8A8A8"
        stroke-width="5"
      />

      <!-- توپ‌های ثابت روی خطوط -->
      <circle
        class="ball ball01"
        r="6"
        cx="700"
        cy="200"
        fill="#ffd700"
        style="visibility: hidden"
      ></circle>
      <circle
        class="ball ball02"
        r="6"
        cx="700"
        cy="400"
        fill="#ffd700"
        style="visibility: hidden"
      ></circle>
      <circle
        class="ball ball03"
        r="6"
        cx="700"
        cy="600"
        fill="#ffd700"
        style="visibility: hidden"
      ></circle>
      <circle
        class="ball ball04"
        r="6"
        cx="700"
        cy="800"
        fill="#ffd700"
        style="visibility: hidden"
      ></circle>
      <circle
        class="ball ball05"
        r="6"
        cx="700"
        cy="1000"
        fill="#ffd700"
        style="visibility: hidden"
      ></circle>

      <!-- توپ متحرک -->
      <circle
        class="ball ballMoving"
        r="8"
        cx="100"
        cy="0"
        fill="#ffd700"
        style="visibility: hidden"
      ></circle>
    </svg>

    <!-- فضای اضافی برای اسکرول -->
    <div class="h-screen"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const svgStage = ref(null)
let mainTimeline = null
let pulsesTimeline = null

onMounted(async () => {
  // این صفحه فقط در مرورگر اجرا شود
  if (!process.client) return

  const gsap = (await import('gsap')).default
  const { ScrollTrigger } = await import('gsap/ScrollTrigger')
  const { DrawSVGPlugin } = await import('gsap/DrawSVGPlugin')
  const { MotionPathPlugin } = await import('gsap/MotionPathPlugin')

  gsap.registerPlugin(ScrollTrigger, DrawSVGPlugin, MotionPathPlugin)
  gsap.defaults({ ease: 'none' })

  // انیمیشن پالس برای توپ‌ها هنگام برخورد
  pulsesTimeline = gsap.timeline({
    defaults: {
      duration: 0.05,
      autoAlpha: 1,
      scale: 2,
      transformOrigin: 'center',
      ease: 'elastic(2.5, 1)',
    },
  })
    .to('.ball01, .text01, .desc01', {}, 0.3)
    .to('.ball02, .text02, .desc02', {}, 0.455)
    .to('.ball03, .text03, .desc03', {}, 0.599)
    .to('.ball04, .text04, .desc04', {}, 0.695)
    .to('.ball05, .text05, .desc05', {}, 0.865)

  mainTimeline = gsap.timeline({
    defaults: { duration: 1 },
    scrollTrigger: {
      trigger: '#svg-stage',
      scrub: true,
      start: 'top center',
      end: 'bottom center',
    },
  })
    .to('.ballMoving', { duration: 0.01, autoAlpha: 1 })
    .from('.theLine', { drawSVG: 0 }, 0)
    .to(
      '.ballMoving',
      {
        motionPath: {
          path: '.theLine',
          align: '.theLine',
          alignOrigin: [0.5, 0.5],
        },
      },
      0
    )
    .add(pulsesTimeline, 0)
})

onUnmounted(() => {
  if (mainTimeline) mainTimeline.kill()
  if (pulsesTimeline) pulsesTimeline.kill()
  if (process.client) {
    const { ScrollTrigger } = require('gsap/ScrollTrigger')
    ScrollTrigger.getAll().forEach((trigger) => trigger.kill())
  }
})
</script>

<style scoped>
/* استایل اضافی در صورت نیاز */
</style>
