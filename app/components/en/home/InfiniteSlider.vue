<template>
    <div class="slider" ref="sliderRef">
      <div class="slide-track">
        <div v-for="(img, index) in images" :key="index" class="slide">
          <img :src="img" alt="logo" class="logo" :class="{ active: activeIndex === index }" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue';

  const baseImages = [
     "/Home/InfiniteSlider/Mahanplast.webp",     
  "/Saaf-film.webp",    
  "/Olsanbaft.webp",
  "/Paraplastic.webp",    
  "/Reyhaneh.webp",
  "/logoMegabiz.webp",
  "/Logo-Final.webp",
    ];
  
  const images = [...baseImages, ...baseImages, ...baseImages, ...baseImages, ...baseImages, ...baseImages, ...baseImages, ...baseImages, ...baseImages, ...baseImages];

  const sliderRef = ref(null);
  const activeIndex = ref(-1);
  let rafId = null;
  const CENTER_THRESHOLD = 40;

  function updateActive() {
    const slider = sliderRef.value;
    if (!slider) {
      rafId = requestAnimationFrame(updateActive);
      return;
    }
    const slides = Array.from(slider.querySelectorAll('.slide'));
    const sliderRect = slider.getBoundingClientRect();
    const sliderCenterX = sliderRect.left + sliderRect.width / 2;

    let bestIndex = -1;
    let bestDistance = Infinity;
    slides.forEach((slideEl, i) => {
      const rect = slideEl.getBoundingClientRect();
      const slideCenterX = rect.left + rect.width / 2;
      const dist = Math.abs(slideCenterX - sliderCenterX);
      if (dist < bestDistance) {
        bestDistance = dist;
        bestIndex = i;
      }
    });

    activeIndex.value = bestDistance <= CENTER_THRESHOLD ? bestIndex : -1;
    rafId = requestAnimationFrame(updateActive);
  }

  onMounted(() => {
    rafId = requestAnimationFrame(updateActive);
  });

  onUnmounted(() => {
    if (rafId) cancelAnimationFrame(rafId);
  });
  </script>
  
  <style scoped lang="scss">
  body {
    align-items: center;
    background: #e3e3e3;
    display: flex;
    height: 100vh;
    justify-content: center;
  }
  
  @mixin white-gradient {
    background: linear-gradient(to right, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0) 100%);
  }
  
  $animationSpeed: 40s;
  
  @keyframes scroll {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(calc(-250px * 10));
    }
  }

  @keyframes scrollMobile {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(calc(-125px * 10));
    }
  }
  
  .slider {
    background: white;
    box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.125);
    height: 100px;
    margin: 0;
    padding: 0;
    overflow: hidden;
    position: relative;
    width: 100vw;

    .slide-track {
      animation: scroll $animationSpeed linear infinite;
      display: flex;
      width: calc(250px * 20);
    }
  
    .slide {
      height: 100px;
      width: auto;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0 28px;
    }
    
    .logo {
      max-height: 72px;
      max-width: 220px;
      width: auto;
      height: auto;
      object-fit: contain;
      display: block;
      filter: grayscale(100%);
      transition: filter 0.25s ease, transform 0.25s ease;
    }

    .logo.active {
      filter: grayscale(0%);
      transform: scale(1.03);
    }

    .slide:hover .logo {
      filter: grayscale(0%);
    }

    // Media query for mobile
    @media (max-width: 800px) {
      height: 70px;

      .slide-track {
        animation: scrollMobile $animationSpeed linear infinite;
        width: calc(125px * 20);
      }

      .slide {
        height: 70px;
        padding: 0 14px;
      }

      .logo {
        max-height: 52px;
        max-width: 140px;
      }
    }
  }
  </style>