<template>
    <div class="relative">
 <HomeWave 
    
    />
  <div >
  <div>
    <Navbar />
  <div class="min-h-screen bg-gray-100 font-montserrat py-32 px-4">
    <!-- Background Text -->
    <div class="fond">
      <span class="s1 absolute top-0 left-0 text-[15rem] font-extrabold uppercase text-gray-300 leading-none opacity-50">
        
      </span>
      <span class="s2 absolute bottom-0 right-0 text-[15rem] font-extrabold uppercase text-gray-300 leading-none opacity-50">
        
      </span>
    </div>

    <!-- Card Container -->
    <div class="card relative h-[490px] w-full max-w-[900px] mx-auto bg-white shadow-[10px_10px_93px_0px_rgba(0,0,0,0.75)]">
      <!-- Thumbnail Image SLIDER (replaced static image) -->
      <div class="thumbnail absolute left-[30px] top-[-30px] h-[340px] w-[530px] overflow-hidden shadow-[10px_10px_60px_0px_rgba(0,0,0,0.75)] flex items-center justify-center">
        <img
          class="left absolute left-1/2 top-1/2 h-auto w-full -translate-x-1/2 -translate-y-1/2 transform transition-all duration-300"
          :src="images[activeIndex]"
          alt="Blog thumbnail"
        />
        <!-- Prev Button -->
        <button @click="prevSlide" class="absolute left-2 top-1/2 -translate-y-1/2 bg-white/70 hover:bg-[#FFCD05] text-black rounded-full w-8 h-8 flex items-center justify-center shadow" aria-label="Previous">
          ‹
        </button>
        <!-- Next Button -->
        <button @click="nextSlide" class="absolute right-2 top-1/2 -translate-y-1/2 bg-white/70 hover:bg-[#FFCD05] text-black rounded-full w-8 h-8 flex items-center justify-center shadow" aria-label="Next">
          ›
        </button>
        <!-- Dots -->
        <div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-2">
          <button
            v-for="(img, idx) in images"
            :key="idx"
            @click="goToSlide(idx)"
            :class="['w-3 h-3 rounded-full', activeIndex === idx ? 'bg-[#FFCD05]' : 'bg-gray-300']"
            aria-label="Go to slide"
          ></button>
        </div>
      </div>

      <!-- Right Content -->
      <div class="right ml-[590px] mr-5">
        <h1 class="pt-[15px] text-[1.2rem] text-[#FFCD05] font-bold">
          POLYCHEM at Tabriz Plast 2025
        </h1>

    

        <!-- Separator -->
        <div class="separator mt-2.5 border-t border-[#C3C3C3]"></div>

        <!-- Description -->
        <p class="pt-2.5  text-[0.95rem] leading-[150%] text-black">POLYCHEM participated in the 22nd International Specialized Exhibition of Rubber, Plastics and Machinery (Tabriz Plast 2025) 
         <br> Booth Information:
<br> Venue: Tabriz International Exhibition Center
<br> Hall: Shahriar
<br> Booth No.: 21
<br>
        </p>
        
        <!-- Read More Button -->
        <NuxtLink to="/en/news" class="btn-slide-down inline-block px-5 py-3 mt-4 uppercase tracking-wider text-sm text-[#FFCD05] border-3 border-[#FFCD05] rounded-lg relative overflow-hidden cursor-pointer">
          <span class="relative z-10">View All News</span>
        </NuxtLink>
      </div>

      <!-- Date (Inside Card) -->
      <h5 class="absolute left-[30px] bottom-[30px] text-[6rem] text-[#C3C3C3] leading-none">
        16
      </h5>
      <h6 class="absolute left-[30px] bottom-[10px] text-[2rem] text-[#C3C3C3] leading-none">
        December
      </h6>

      <!-- Social Icons -->
      <div class="absolute bottom-[50px] left-[250px] flex gap-6">
        <!-- Instagram Icon -->
        <a 
          href="http://instagram.com/polychemmb" 
          class="instagram-icon w-10 h-10 rounded-full border-2 border-[#7B7B7B] flex items-center justify-center hover:border-[#FFCD05] hover:bg-[#FFCD05] transition-all duration-300 active:scale-95"
          aria-label="Instagram"
        >
          <svg class="w-5 h-5 instagram-svg" fill="#7B7B7B" viewBox="0 0 24 24">
            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
          </svg>
        </a>
        
        <!-- YouTube Icon -->
        <a 
          href="#" 
          class="youtube-icon w-10 h-10 rounded-full border-2 border-[#7B7B7B] flex items-center justify-center hover:border-[#FFCD05] hover:bg-[#FFCD05] transition-all duration-300 active:scale-95"
          aria-label="YouTube"
        >
          <svg class="w-5 h-5 youtube-svg" fill="#7B7B7B" viewBox="0 0 24 24">
            <path d="M23.498 6.186a2.994 2.994 0 0 0-2.108-2.117C19.633 3.5 12 3.5 12 3.5s-7.633 0-9.39.569A2.994 2.994 0 0 0 .502 6.186C0 7.943 0 12 0 12s0 4.057.502 5.814a2.994 2.994 0 0 0 2.108 2.117C4.367 20.5 12 20.5 12 20.5s7.633 0 9.39-.569a2.994 2.994 0 0 0 2.108-2.117C24 16.057 24 12 24 12s0-4.057-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
          </svg>
        </a>
        
        <!-- LinkedIn Icon -->
        <a 
          href="https://www.linkedin.com/company/polychem-turkey/" 
          class="linkedin-icon w-10 h-10 rounded-full border-2 border-[#7B7B7B] flex items-center justify-center hover:border-[#FFCD05] hover:bg-[#FFCD05] transition-all duration-300 active:scale-95"
          aria-label="LinkedIn"
        >
          <svg class="w-5 h-5 linkedin-svg" fill="#7B7B7B" viewBox="0 0 24 24">
            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
          </svg>
        </a>
        
        <!-- Email Icon -->
        <a 
          href="mailto:info@polychemmb.com" 
          class="email-icon w-10 h-10 rounded-full border-2 border-[#7B7B7B] flex items-center justify-center hover:border-[#FFCD05] hover:bg-[#FFCD05] transition-all duration-300 active:scale-95"
          aria-label="Email"
        >
          <svg class="w-5 h-5 email-svg" fill="none" stroke="#7B7B7B" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
          </svg>
        </a>
      </div>

      <!-- Floating Action Button -->
      <button class="fab absolute right-[50px] bottom-[-40px] flex h-20 w-20 items-center justify-center bg-[#FFCD05] text-white shadow-[10px_10px_50px_0px_rgba(0,0,0,0.75)] cursor-pointer hover:bg-[#E6B800] transition-colors">
      </button>
    </div>
  </div>
  </div>
  </div>
    </div>

</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import Navbar from '~/components/tr/layout/navbar.vue'
import HomeWave from '~/components/en/layout/HomeWave.vue'


// Slider images (add or adjust paths as needed)
const images = [
'/Tabriz-Plast-2025-2.webp',
'/Tabriz-Plast-2025-3.webp',
'/Tabriz-Plast-2025-4.webp',
'/Tabriz-Plast-2025-5.webp',
'/Tabriz-Plast-2025-6.webp',
'/Tabriz-Plast-2025-7.webp',
'/Tabriz-Plast-2025-8.webp'

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
  .card {
    height: auto;
    width: 90%;
  }
  
  .thumbnail {
    position: relative;
    left: 0;
    top: 0;
    width: 100%;
    height: 250px;
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
</style>
