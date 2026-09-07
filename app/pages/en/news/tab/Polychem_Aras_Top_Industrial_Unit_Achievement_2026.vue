<template>
  <div class="relative">
    <HomeWave />
    <div>
      <Navbar />
      <div class="page-wrapper min-h-screen bg-gray-100 font-montserrat py-32 px-4">
        <!-- Background Text -->
        <div class="fond">
          <span class="s1 absolute top-0 left-0 text-[8rem] sm:text-[10rem] md:text-[12rem] lg:text-[15rem] font-extrabold uppercase text-gray-300 leading-none opacity-50">
            News
          </span>
          <span class="s2 absolute bottom-0 right-0 text-[8rem] sm:text-[10rem] md:text-[12rem] lg:text-[15rem] font-extrabold uppercase text-gray-300 leading-none opacity-50">
            Awards
          </span>
        </div>

        <!-- Card Container -->
        <div class="card relative h-[490px] w-full max-w-[900px] mx-auto bg-white shadow-[10px_10px_93px_0px_rgba(0,0,0,0.75)]">
          <!-- Thumbnail Image SLIDER -->
          <div class="thumbnail absolute left-[30px] top-[-30px] h-[340px] w-[530px] overflow-hidden shadow-[10px_10px_60px_0px_rgba(0,0,0,0.75)] flex items-center justify-center">
            <img
              class="left absolute left-1/2 top-1/2 h-auto w-full -translate-x-1/2 -translate-y-1/2 transform transition-all duration-300"
              :src="images[activeIndex]"
              alt="Blog thumbnail"
            />
            <!-- Buttons & Dots (Keep existing) -->
            <button @click="prevSlide" class="absolute left-2 top-1/2 -translate-y-1/2 bg-white/70 hover:bg-[#FFCD05] text-black rounded-full w-8 h-8 flex items-center justify-center shadow" aria-label="Previous">‹</button>
            <button @click="nextSlide" class="absolute right-2 top-1/2 -translate-y-1/2 bg-white/70 hover:bg-[#FFCD05] text-black rounded-full w-8 h-8 flex items-center justify-center shadow" aria-label="Next">›</button>
            <div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-2">
              <button v-for="(img, idx) in images" :key="idx" @click="goToSlide(idx)" :class="['w-3 h-3 rounded-full', activeIndex === idx ? 'bg-[#FFCD05]' : 'bg-gray-300']" aria-label="Go to slide"></button>
            </div>
          </div>

          <!-- Right Content -->
          <div class="right ml-[590px] mr-5">
            <h1 class="pt-[15px] text-[1.05rem] sm:text-[1.1rem] md:text-[1.2rem] text-[#FFCD05] font-bold">
            POLYCHEM Recognized as Top Industrial Unit in Aras Free Zone
            </h1>

            <!-- Separator -->
            <div class="separator mt-2.5 border-t border-[#C3C3C3]"></div>

            <!-- Description -->
            <p class="pt-2.5 text-[0.85rem] sm:text-[0.9rem] md:text-[0.95rem] leading-[150%] text-black">
              On the occasion of Industry and Mine Day, POLYCHEM was honored as one of the top Manufacturing units in the Aras Free Zone. This recognition was awarded in appreciation of our continuous efforts and outstanding performance in production and entrepreneurship. We view this achievement as a powerful motivation to continue driving industrial excellence and contributing to the economic growth of the region.
            </p>
            
            <!-- Read More Button -->
            <NuxtLink to="/en/news" class="btn-slide-down inline-block px-5 py-3 mt-4 uppercase tracking-wider text-sm text-[#FFCD05] border-3 border-[#FFCD05] rounded-lg relative overflow-hidden cursor-pointer">
              <span class="relative z-10">View All News</span>
            </NuxtLink>
          </div>

          <!-- Date -->
          <h5 class="absolute left-[30px] bottom-[30px] text-[6rem] text-[#C3C3C3] leading-none">01</h5>
          <h6 class="absolute left-[30px] bottom-[10px] text-[2rem] text-[#C3C3C3] leading-none">July 2026</h6>

          <!-- Social Icons & FAB (Keep existing) -->
          <!-- ... -->
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import Navbar from '~/components/en/layout/navbar.vue';
import HomeWave from '~/components/en/layout/HomeWave.vue';

// Slider images (add or adjust paths as needed)

const images = [
  '/News/Polychem_Aras_Top_Industrial_Unit_Achievement_2026.webp',
  '/News/Polychem_Aras_Top_Industrial_Unit_Achievement_2026_2.webp'
]
const activeIndex = ref(0)
let interval = null

function nextSlide() {
  activeIndex.value = (activeIndex.value + 1) % images.length
}
function prevSlide() {
  activeIndex.value = (activeIndex.value - 1 + images.length) % images.length
}
function goToSlide(idx) {
  activeIndex.value = idx
}

onMounted(() => {
  interval = setInterval(() => {
    nextSlide()
  }, 4000)
})
onBeforeUnmount(() => {
  clearInterval(interval)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

.font-montserrat {
  font-family: 'Montserrat', sans-serif;
}

h1, h2 {
  font-family: 'Montserrat', sans-serif;
}

.border-3 {
  border-width: 3px;
}

.grayscale-img {
  filter: grayscale(100%);
}

/* Hover filled slide down button effect */
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

/* Social Media Icon Hover Effects */
.youtube-icon:hover .youtube-svg {
  fill: #fff !important;
}

.instagram-icon:hover .instagram-svg {
  fill: #fff !important;
}

.linkedin-icon:hover .linkedin-svg {
  fill: #fff !important;
}

.email-icon:hover .email-svg {
  stroke: #fff !important;
}

/* FAB Animation - Similar to Hero.vue yellow circle */
.fab {
  animation: fab-morph 5s linear infinite;
}

/* Keep icon stable while button rotates */
.fab svg {
  animation: fab-icon-counter-rotate 5s linear infinite;
}

@keyframes fab-morph {
  from {
    transform: rotateZ(0deg);
    border-radius: 50%;
  }
  50% {
    border-radius: 0%;
  }
  to {
    transform: rotateZ(360deg);
    border-radius: 50%;
  }
}

@keyframes fab-icon-counter-rotate {
  from {
    transform: rotateZ(0deg);
  }
  to {
    transform: rotateZ(-360deg);
  }
}

/* Responsive adjustments */
@media (max-width: 968px) {
  .page-wrapper {
    padding-top: 90px !important;
  }
  .card {
    height: auto;
    width: 90%;
    padding-bottom: 30px;
  }
  
  .thumbnail {
    position: relative;
    left: 0;
    top: 0;
    width: 100%;
    height: 320px;
    margin-bottom: 20px;
  }
  
  .right {
    margin-left: 20px;
    margin-right: 20px;
    padding-bottom: 100px;
  }
  
  h5, h6 {
    left: 20px;
  }
  
  ul {
    margin-left: 20px;
    bottom: 50px;
  }
  
  .fab {
    right: 20px;
  }
  
  .s1, .s2 {
    font-size: 8rem;
  }
}

@media (max-width: 640px) {
  .page-wrapper {
    padding-top: 110px !important;
  }
  .card {
    width: 95%;
  }
  .thumbnail {
    height: 220px;
  }
  .right {
    margin-left: 15px;
    margin-right: 15px;
  }
  h5 {
    font-size: 4rem;
  }
  h6 {
    font-size: 1.4rem;
  }
}

@media (max-width: 400px) {
  .page-wrapper {
    padding-top: 120px !important;
  }
  .thumbnail {
    height: 190px;
  }
  .s1, .s2 {
    opacity: 0.25 !important;
  }
}
</style>