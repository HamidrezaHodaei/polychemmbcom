<!-- /components/en/aboutus/scroll.vue -->
<template>
  <div class="w-full bg-[#f1f2f2] scroll-wrapper font-[Montserrat]">

    <!-- Heading: Desktop only -->
    <h1
      class="desktop-heading text-center text-xl md:text-2xl lg:text-3xl px-4 pt-10 md:pt-20 text-[#A8A8A8] font-[Montserrat]"
      dir="ltr"
    >
      Scroll to watch POLYCHEM's story unfold
    </h1>

    <!-- ========== DESKTOP SVG Timeline ========== -->
    <div class="desktop-svg">
      <svg
        id="svg-stage"
        ref="svgStage"
        class="w-full mx-auto mt-[8vh] overflow-visible px-4"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 1400 1400"
        preserveAspectRatio="xMidYMid meet"
      >
        <defs>
          <pattern id="img01" x="0" y="0" width="1" height="1">
            <image href="/2015.webp" x="-12" y="-12" width="250" height="130" preserveAspectRatio="xMidYMid slice"/>
          </pattern>
          <pattern id="img02" x="0" y="0" width="1" height="1">
            <image href="/2019.webp" x="5" y="2" width="150" height="170" preserveAspectRatio="xMidYMid slice"/>
          </pattern>
          <pattern id="img03" x="0" y="0" width="1" height="1">
            <image href="/2022.jfif" x="-25" y="-30" width="150" height="170" preserveAspectRatio="xMidYMid slice"/>
          </pattern>
          <pattern id="img04" x="0" y="0" width="1" height="1">
            <image href="/2023.jfif" x="-20" y="-5" width="150" height="170" preserveAspectRatio="xMidYMid slice"/>
          </pattern>
          <pattern id="img05" x="0" y="0" width="1" height="1">
            <image href="/2025.webp" x="-10" y="2" width="150" height="170" preserveAspectRatio="xMidYMid slice"/>
          </pattern>
        </defs>

        <path class="line01 line" d="M 0 200 1400 200" fill="none" stroke="#A8A8A8" stroke-width="2"/>
        <path class="line02 line" d="M 0 450 1400 450" fill="none" stroke="#A8A8A8" stroke-width="2"/>
        <path class="line03 line" d="M 0 700 1400 700" fill="none" stroke="#A8A8A8" stroke-width="2"/>
        <path class="line04 line" d="M 0 950 1400 950" fill="none" stroke="#A8A8A8" stroke-width="2"/>
        <path class="line05 line" d="M 0 1200 1400 1200" fill="none" stroke="#A8A8A8" stroke-width="2"/>

        <!-- Years - English -->
        <text class="text01" x="30" y="190" fill="#A8A8A8" font-size="15" font-family="Montserrat" style="visibility:hidden">2015</text>
        <text class="text02" x="30" y="440" fill="#A8A8A8" font-size="15" font-family="Montserrat" style="visibility:hidden">2019</text>
        <text class="text03" x="30" y="690" fill="#A8A8A8" font-size="15" font-family="Montserrat" style="visibility:hidden">2022</text>
        <text class="text04" x="30" y="940" fill="#A8A8A8" font-size="15" font-family="Montserrat" style="visibility:hidden">2023</text>
        <text class="text05" x="30" y="1190" fill="#A8A8A8" font-size="15" font-family="Montserrat" style="visibility:hidden">2025</text>

        <!-- Descriptions - English -->
        <text class="desc01" x="1350" y="175" fill="#A8A8A8" font-size="15" text-anchor="end" font-family="Montserrat" style="visibility:hidden">Start of factory construction</text>
        <text class="desc02" x="1350" y="425" fill="#A8A8A8" font-size="15" text-anchor="end" font-family="Montserrat" style="visibility:hidden">Completion of the project and official commissioning</text>
        <text class="desc03" x="1350" y="675" fill="#A8A8A8" font-size="15" text-anchor="end" font-family="Montserrat" style="visibility:hidden">Start of production</text>
        <text class="desc04" x="1350" y="925" fill="#A8A8A8" font-size="15" text-anchor="end" font-family="Montserrat" style="visibility:hidden">Global market entry</text>
        <text class="desc05" x="1350" y="1175" fill="#A8A8A8" font-size="15" text-anchor="end" font-family="Montserrat" style="visibility:hidden">Current status and ongoing development</text>

        <path
          class="theLine"
          d="M 100,0 Q 900 100 700 200 Q 500 325 700 450 Q 900 575 700 700 Q 500 825 700 950 Q 900 1075 700 1200 Q 500 1300 700 1400"
          fill="none" stroke="#A8A8A8" stroke-width="5"
        />

        <circle class="ball ballMoving" r="8" cx="100" cy="0" fill="#ffd700" style="visibility:hidden"/>
        <circle class="ball ball01" r="60" cx="700" cy="200" fill="url(#img01)" stroke="#ffd700" stroke-width="3" style="visibility:hidden"/>
        <circle class="ball ball02" r="60" cx="700" cy="450" fill="url(#img02)" stroke="#ffd700" stroke-width="3" style="visibility:hidden"/>
        <circle class="ball ball03" r="60" cx="700" cy="700" fill="url(#img03)" stroke="#ffd700" stroke-width="3" style="visibility:hidden"/>
        <circle class="ball ball04" r="60" cx="700" cy="950" fill="url(#img04)" stroke="#ffd700" stroke-width="3" style="visibility:hidden"/>
        <circle class="ball ball05" r="60" cx="700" cy="1200" fill="url(#img05)" stroke="#ffd700" stroke-width="3" style="visibility:hidden"/>
      </svg>
    </div>

    <!-- ========== MOBILE Timeline: Vertical Cards ========== -->
    <div class="mobile-tl">
      <div class="tl-track">
        <div class="tl-line"></div>
        <div v-for="(item, i) in timelineItems" :key="i" class="tl-item">
          <div class="tl-dot">
            <img :src="item.img" :alt="item.year" />
          </div>
          <div class="tl-card font-[Montserrat]">
            <span class="tl-year">{{ item.year }}</span>
            <p class="tl-desc" dir="ltr">{{ item.desc }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Logo: Desktop only -->
    <div class="logo-wrap">
      <img src="/layout/logo/english logo W1.png" alt="Polychem Logo" class="w-32 sm:w-44 md:w-56 lg:w-72 h-auto" />
    </div>

    <div class="pb-8 md:pb-10"></div>
    <TextAboutus />
    <div class="pb-16 md:pb-20"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { DrawSVGPlugin } from 'gsap/DrawSVGPlugin'
import { MotionPathPlugin } from 'gsap/MotionPathPlugin'
import TextAboutus from './Text Aboutus.vue'

gsap.registerPlugin(ScrollTrigger, DrawSVGPlugin, MotionPathPlugin)

const svgStage = ref(null)
let mainTimeline = null
let pulsesTimeline = null

const timelineItems = [
  { year: '2015', desc: 'Start of factory construction', img: '/2015.webp' },
  { year: '2019', desc: 'Completion of the project and official commissioning', img: '/2019.webp' },
  { year: '2022', desc: 'Start of production', img: '/2022.jfif' },
  { year: '2023', desc: 'Global market entry', img: '/2023.jfif' },
  { year: '2025', desc: 'Current status and ongoing development', img: '/2025.webp' },
]

onMounted(() => {
  if (!process.client) return

  gsap.defaults({ ease: "none" })

  pulsesTimeline = gsap.timeline({
    defaults: {
      duration: 0.05, autoAlpha: 1, scale: 1.5,
      transformOrigin: "center", ease: "elastic(2.5, 1)"
    }
  })
    .to(".ball01, .text01, .desc01", {}, 0.300)
    .to(".ball02, .text02, .desc02", {}, 0.455)
    .to(".ball03, .text03, .desc03", {}, 0.599)
    .to(".ball04, .text04, .desc04", {}, 0.695)
    .to(".ball05, .text05, .desc05", {}, 0.865)

  mainTimeline = gsap.timeline({
    defaults: { duration: 1 },
    scrollTrigger: {
      trigger: "#svg-stage",
      scrub: true,
      start: "top center",
      end: "bottom center"
    }
  })
    .to(".ballMoving", { duration: 0.01, autoAlpha: 1 })
    .from(".theLine", { drawSVG: 0 }, 0)
    .to(".ballMoving", {
      motionPath: { path: ".theLine", align: ".theLine", alignOrigin: [0.5, 0.5] }
    }, 0)
    .add(pulsesTimeline, 0)
})

onUnmounted(() => {
  if (mainTimeline) mainTimeline.kill()
  if (pulsesTimeline) pulsesTimeline.kill()
  ScrollTrigger.getAll().forEach(t => t.kill())
})
</script>

<style scoped>
* { box-sizing: border-box; }

/* ========== DESKTOP: SVG shown, mobile-tl hidden ========== */
.desktop-heading { display: block; }
.desktop-svg     { display: block; }
.mobile-tl       { display: none; }
.logo-wrap       { display: flex; justify-content: center; margin-top: 2.5rem; padding: 0 1rem; }

/* ========== MOBILE (≤ 639px): SVG hidden, timeline shown ========== */
@media (max-width: 639px) {
  .desktop-heading { display: none; }
  .desktop-svg     { display: none; }
  .logo-wrap       { display: none; }

  .mobile-tl {
    display: block;
    padding: 28px 16px 8px;
  }
}

/* ========== MOBILE TIMELINE STYLES ========== */
.tl-track {
  position: relative;
  padding-right: 38px;
}

.tl-line {
  position: absolute;
  right: 27px;
  top: 4px; bottom: 4px;
  width: 2px;
  background: linear-gradient(to bottom, #ffd700 0%, #C8C8C8 80%, transparent 100%);
  border-radius: 2px;
}

.tl-item {
  display: flex;
  flex-direction: row-reverse;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 24px;
  position: relative;
}
.tl-item:last-child { margin-bottom: 0; }

.tl-dot {
  flex-shrink: 0;
  width: 54px; height: 54px;
  border-radius: 50%;
  overflow: hidden;
  border: 2.5px solid #ffd700;
  box-shadow: 0 2px 12px rgba(255,215,0,0.25);
  background: #e0e0e0;
  position: relative; z-index: 2;
}
.tl-dot img {
  width: 100%; height: 100%;
  object-fit: cover;
  filter: grayscale(20%);
}

.tl-card {
  flex: 1;
  background: white;
  border-radius: 12px;
  padding: 10px 13px;
  box-shadow: 0 2px 14px rgba(0,0,0,0.08);
  text-align: left;
  border-left: 3px solid #ffd700;
}

.tl-year {
  display: block;
  font-size: 14px; font-weight: 700;
  color: #ffd700; margin-bottom: 3px;
}

.tl-desc {
  font-size: 13px; color: #848484;
  line-height: 1.65; margin: 0;
}
</style>