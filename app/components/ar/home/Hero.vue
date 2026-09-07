<template>
  <div class="hero-container">
    <div class="bg-wrapper" :style="posterStyle">
      <video
        ref="videoA"
        class="bg-video"
        :class="{ 'video-active': activeSlot === 'A' }"
        loop
        muted
        playsinline
        preload="none"
      ></video>
      <video
        ref="videoB"
        class="bg-video"
        :class="{ 'video-active': activeSlot === 'B' }"
        loop
        muted
        playsinline
        preload="none"
      ></video>
      <div class="overlay overlay-1"></div>
      <div class="overlay overlay-2"></div>
    </div>

    <figure class="content-box">
      <h1 class="main-title text-bold">
        <img src="/logo-AR.png" alt="POLYCHEM" class="logo-image translate-x-[20px]" />
        <span class="subtitle">هندسة البوليمر</span>
      </h1>
      <figcaption>
        <p class="intro-text">
          بوليكيم، مصنع متخصص لإنتاج تركيبات البوليمر والماستربتش في منطقة أراس للتخصيص. نوعيات خفيفة الوزن تم تطويرها لاستخدام المواد ذات الأداء العالي في الإنتاج الحديث.
        </p>
      </figcaption>
    </figure>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const VIDEOS  = ['/Hero1.mp4', '/Hero2.mp4', '/Hero3.mp4', '/Hero1.mp4']
const POSTERS = ['/video-poster-1.webp', '/video-poster-2.webp', '/video-poster-3.webp', '/video-poster-1.webp']
const INTERVAL_MS = 5000

const videoA     = ref(null)
const videoB     = ref(null)
const activeSlot = ref('A')
const posterStyle = ref({})

let currentIndex  = 0
let rotationTimer = null

function getVideoEl(slot) {
  return slot === 'A' ? videoA.value : videoB.value
}

function getInactiveSlot() {
  return activeSlot.value === 'A' ? 'B' : 'A'
}

function switchToVideo(index) {
  const inactive = getInactiveSlot()
  const el       = getVideoEl(inactive)
  if (!el) return

  el.oncanplay = null
  el.src = VIDEOS[index]

  el.oncanplay = () => {
    el.oncanplay = null
    el.play().catch(() => {})
    currentIndex     = index
    activeSlot.value = inactive

    // وقتی چهارمین ویدیو (Hero1 نهایی) شروع به پخش کرد، تایمر را بکش
    if (index === VIDEOS.length - 1) {
      clearInterval(rotationTimer)
      rotationTimer = null
    }
  }

  el.load()
}

function advance() {
  const nextIndex = currentIndex + 1
  if (nextIndex >= VIDEOS.length) return
  switchToVideo(nextIndex)
}

onMounted(() => {
  currentIndex = 0

  posterStyle.value = {
    backgroundImage:    `url(${POSTERS[0]})`,
    backgroundSize:     'cover',
    backgroundPosition: 'center',
  }

  const startFirstVideo = () => {
    const el = videoA.value
    if (!el) return

    el.src = VIDEOS[0]

    el.oncanplay = () => {
      el.oncanplay = null
      el.play().catch(() => {})
      posterStyle.value = {}
      rotationTimer = setInterval(advance, INTERVAL_MS)
    }

    el.load()
  }

  const posterImg   = new Image()
  posterImg.src     = POSTERS[0]
  posterImg.onload  = () => setTimeout(startFirstVideo, 100)
  posterImg.onerror = () => setTimeout(startFirstVideo, 100)
})

onBeforeUnmount(() => {
  if (rotationTimer) clearInterval(rotationTimer)
})
</script>

<style scoped>
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-ExtraLight.ttf") format("truetype");
  font-weight: 200; font-style: normal; font-display: swap;
}
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Light.ttf") format("truetype");
  font-weight: 300; font-style: normal; font-display: swap;
}
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Regular.ttf") format("truetype");
  font-weight: 400; font-style: normal; font-display: swap;
}
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Medium.ttf") format("truetype");
  font-weight: 500; font-style: normal; font-display: swap;
}
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Bold.ttf") format("truetype");
  font-weight: 700; font-style: normal; font-display: swap;
}
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-ExtraBold.ttf") format("truetype");
  font-weight: 800; font-style: normal; font-display: swap;
}
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Black.ttf") format("truetype");
  font-weight: 900; font-style: normal; font-display: swap;
}

*, *::before, *::after { box-sizing: border-box; }

.hero-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  height: 100svh;
  height: 100dvh;
  margin: 0;
  background: #000;
  color: #fff;
  overflow: hidden;
}

.bg-wrapper {
  position: absolute;
  inset: 0;
  overflow: hidden;
  background-color: #000;
}

.bg-video {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 1.2s ease;
  z-index: 2;
}

.bg-video.video-active { opacity: 1; }

.overlay {
  position: absolute;
  background-image: linear-gradient(135deg, rgba(119,118,115,0.18), rgba(138,138,138,0.18));
  z-index: 3;
  pointer-events: none;
}

.overlay-1 { top:0; left:0; width:25%; height:25%; animation: overlay-anim-1 20s ease infinite; }
.overlay-2 { top:0; left:0; width:25%; height:25%; animation: overlay-anim-2 10s ease infinite; }

@keyframes overlay-anim-1 {
  0%    { width:25%; height:25%; left:0;    top:0;    backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
  12.5% { width:100%;             left:0;              backdrop-filter:blur(0);    -webkit-backdrop-filter:blur(0); }
  25%   { width:25%; height:25%; right:0;  left:auto; backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
  37.5% { height:100%;            top:0;               backdrop-filter:blur(0);    -webkit-backdrop-filter:blur(0); }
  50%   { width:25%; height:25%; bottom:0; top:auto;  backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
  62.5% { width:100%;             left:0;  right:auto; backdrop-filter:blur(0);   -webkit-backdrop-filter:blur(0); }
  75%   { width:25%; height:25%; left:0;              backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
  87.5% { height:100%;            top:0;   bottom:auto; backdrop-filter:blur(0);  -webkit-backdrop-filter:blur(0); }
  100%  { width:25%; height:25%; top:0;               backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
}

@keyframes overlay-anim-2 {
  0%    { width:25%; height:25%; left:0;   top:0;     backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
  12.5% { height:100%;           bottom:0; top:auto;  backdrop-filter:blur(0);    -webkit-backdrop-filter:blur(0); }
  25%   { width:25%; height:25%; bottom:0;            backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
  37.5% { width:100%;            right:0;  left:auto; backdrop-filter:blur(0);    -webkit-backdrop-filter:blur(0); }
  50%   { width:25%; height:25%; right:0;             backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
  62.5% { height:100%;           top:0;    bottom:auto; backdrop-filter:blur(0);  -webkit-backdrop-filter:blur(0); }
  75%   { width:25%; height:25%; right:0;  top:0;     backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
  87.5% { width:100%;            left:0;   right:auto; backdrop-filter:blur(0);   -webkit-backdrop-filter:blur(0); }
  100%  { width:25%; height:25%; left:0;   top:0;     backdrop-filter:blur(2vmin); -webkit-backdrop-filter:blur(2vmin); }
}

.content-box {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  max-width: 600px;
  border: 1px solid rgba(255,255,255,0.2);
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  background-color: rgba(0,0,0,0.2);
  backdrop-filter: blur(2vmin);
  -webkit-backdrop-filter: blur(2vmin);
  z-index: 10;
  margin: 0;
  direction: rtl;
  text-align: right;
}

.content-box::after {
  position: absolute;
  bottom: -10px;
  left: -10px;
  width: 60px;
  height: 60px;
  background-color: #ffd000;
  box-shadow: 0 6px 18px rgba(0,0,0,0.45);
  content: "";
  z-index: -1;
  animation: shape-rotate 5s linear infinite;
}

@keyframes shape-rotate {
  0%   { transform:rotate(0deg);   border-radius:0; }
  50%  { border-radius:49%; }
  100% { transform:rotate(360deg); border-radius:0; }
}

.main-title {
  font-family: "Tajawal", -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 40px;
  font-weight: 700;
  line-height: 1.2;
  color: #fff;
  margin: 0 0 20px 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
  text-align: right;
  width: 100%;
}

.logo-image {
  max-width: 40%;
  height: auto;
  max-height: 50px;
  width: auto;
  display: block;
}

.subtitle {
  font-size: 22px;
  font-weight: 400;
  color: #fff;
  letter-spacing: 0.5px;
}

figcaption {
  font-family: "Tajawal", -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 18px;
  font-weight: 400;
  line-height: 1.6;
  padding-right: 30px;
  border-right: 1px solid #fff;
  color: #fff;
  margin: 0;
  text-align: right;
}

.intro-text { margin: 0; }

@media (max-width: 1023px) {
  .content-box { max-width: 80%; padding: 22px; }
}

@media (max-width: 767px) {
  .content-box { max-width: 90%; padding: 16px; top: 45%; }
  .main-title  { font-size: 28px; }
  .subtitle    { font-size: 16px; }
  figcaption   { font-size: 14px; padding-right: 16px; }
}

@media (max-width: 380px) {
  .main-title { font-size: 22px; }
  .subtitle   { font-size: 14px; }
  figcaption  { font-size: 13px; }
}
</style>