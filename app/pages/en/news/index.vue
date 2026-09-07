<template>
  <div>
    <Navbar />
    <main class="bg-gray-100">
      <section class="previews xl:flex">
        <!-- Hero Section -->
        <div class="relative h-[30em] xl:fixed xl:top-0 xl:left-0 xl:h-screen xl:w-[45%] bg-black">
          <figure
            v-for="(image, index) in backgroundImages"
            :key="index"
            class="absolute inset-0 bg-cover bg-center bg-no-repeat transition-opacity duration-1000 grayscale-img"
            :class="{
              'opacity-0': currentImageIndex !== index,
              'opacity-100': currentImageIndex === index
            }"
            :style="{ backgroundImage: `url(${image})` }"
          />
          <div class="absolute inset-0 bg-black/20" />
        </div>

        <!-- Content Section -->
        <div class="min-h-screen xl:ml-[45%]">

          <!-- Posts -->
          <ul>
            <li
              v-for="(post, index) in posts"
              :key="index"
              class="preview transition-colors duration-200"
              :class="{ 'bg-white': index % 2 === 1 }"
              @mouseenter="changeImage(index)"
            >
              <NuxtLink :to="post.link || '#'" class="block p-8 xl:px-32 xl:py-16 2xl:px-40">
                <div class="flex items-center gap-2 mb-1">
                  <span class="text-black text-sm">{{ post.date }}</span>
                  <span
                    v-if="post.tag"
                    class="px-2 py-1 text-xs font-semibold uppercase tracking-wider bg-[#FFCD05] text-white rounded"
                  >
                    {{ post.tag }}
                  </span>
                </div>

                <h2 class="font-bold mb-2 mt-1 text-2xl xl:text-3xl" style="color: #848484;">
                  {{ post.title }}
                </h2>

                <p class="mb-3 leading-relaxed" style="color: #acacad;">
                  {{ post.excerpt }}
                </p>

                <span
                  class="btn-slide-down inline-block px-2 py-2 uppercase tracking-wider text-sm border-3 rounded-lg relative overflow-hidden"
                  style="color: #FFCD05; border-color: #FFCD05;"
                >
                  <span class="relative z-10">Read More</span>
                </span>
              </NuxtLink>
            </li>
          </ul>

        </div>
      </section>
    </main>

    <Chatbox />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '/components/en/layout/navbar.vue'
import Chatbox from '/components/en/chatbox/chatbox.vue'

const currentImageIndex = ref(0)

const backgroundImages = [
  '/News/Polychem_Aras_Top_Industrial_Unit_Achievement_2026.webp',
  '/Visit-tabriz-3.webp',
  '/Tabriz-Plast-2025-1.webp',
  '/plast-2.jpg',
  '/Visit-of-the-CEO-of-Bank-of-Industry.webp',
  '/HDCHEM-4760.webp',
  '/Report.webp',
  '/dynamic-data-visualization-3d.webp',
  '/high-angle-plastic-bottles-arrangement2.webp'
]

const posts = [
  {
    date: 'July 1, 2026',
    title: 'POLYCHEM Recognized as Top Industrial Unit in Aras Free Zone',
    excerpt: 'On the occasion of Industry and Mine Day, POLYCHEM was honored as one of the top Manufacturing units in the Aras Free Zone, celebrating its outstanding performance in production and entrepreneurship.',
    tag: 'News',
    link: '/en/news/tab/Polychem_Aras_Top_Industrial_Unit_Achievement_2026'
  },
  {
    date: 'Dec 17, 2025',
    title: 'President of East Azerbaijan IMT Organization Visits POLYCHEM at Tabriz Plast 2025',
    excerpt: 'Engineer Parnian, the esteemed President of the East Azerbaijan Province\'s Industry, Mine, and Trade Organization (SAMT), paid a visit to the POLYCHEM booth during the Tabriz Plast 2025 Exhibition.',
    tag: 'News',
    link: '/en/news/tab/Official-Visit-Engineer-Parnian-Tabriz-Plast-2025'
  },
  {
    date: 'Dec 16-19, 2025',
    title: 'POLYCHEM at Tabriz Plast 2025',
    excerpt: 'POLYCHEM participated in the 22nd International Specialized Exhibition of Rubber, Plastics and Machinery (Tabriz Plast 2025).',
    tag: 'event',
    link: '/en/news/tab/tabriz-plast-2025'
  },
  {
    date: 'Dec 3-6, 2025',
    title: 'Plast Eurasia İstanbul 2025',
    excerpt: 'POLYCHEM is excited to announce its participation in Plast Eurasia Istanbul 2025, the leading plastics industry trade fair in the region, taking place from 3–6 December 2025 at TÜYAP Fair & Congress Center.',
    tag: 'event',
    link: '/en/news/tab/plast-eurasia-2025'
  },
  {
    date: 'Nov 24, 2025',
    title: 'Visit of the Head of the Central Branch of Bank of Industry and Mine to Company POLYCHEM',
    excerpt: 'The visit was attended by several vice presidents and senior managers of the bank, as well as the managers of POLYCHEM Company (the operator of the Polychem brand). Dr. Rezavi closely inspected the company\'s advanced production lines for engineering polymers, specialized composites, masterbatches, polymeric additives, and the new generation of products, while reviewing the latest research and production achievements.',
    tag: 'News',
    link: '/en/news/tab/Visit-of-the-CEO-of-Bank-of-Industry',
  },
  {
    date: 'Nov 14, 2025',
    title: 'New Product Launch: HDCHEM 4760 – The Ultimate Blow Molding Compound',
    excerpt: 'We are proud to unveil the most powerful blow molding grade in the entire HDCHEM range: HDCHEM 4760',
    tag: 'News',
    link: '/en/news/tab/New-Product-Launch-HDCHEM-4760',
  },
  {
    date: 'Nov 1, 2025',
    title: 'Global Polypropylene and Polypropylene Composites Market Size, Share, and Trends Analysis Report – Industry Overview and Forecast to 2032',
    excerpt: 'Global Polypropylene and Polypropylene Composites Market, By Product Type (Polypropylene (PP), Polypropylene Composites), Fiber Type (Glass Fiber, Carbon Fiber, Others), Application (Packaging, Building and Construction, Automotive, Electrical and Electronics, Aerospace and Defence, Others) - Industry Trends and Forecast to 2032',
    tag: 'Report',
    link: '/en/news/tab/Global-Polypropylene-and-Composites-Market-Report-2032'
  },
  {
    date: 'Dec 6, 2024',
    title: 'Global Cast Low-Density Polyethylene Disposable Gloves Market Size, Share, and Trends Analysis Report – Industry Overview and Forecast to 2032',
    excerpt: 'Global Cast Low-Density Polyethylene Disposable Gloves Market Segmentation, By Size (Small, Medium, Large, and X-Large), End Users (Food and Beverages, Medical, Industrial, and Others), Distribution Channel (Direct Distribution and Via Distributors) – Industry Trends and Forecast to 2032',
    tag: 'Report',
    link: '/en/news/tab/Cast_LowDensity_PE_Gloves_Market_Report_2032',
  },
  {
    date: 'Oct 27, 2025',
    title: 'Rising Polypropylene Prices Increase Production Costs by Up to 40%',
    excerpt: 'The runaway increase in the prices of polyethylene and polypropylene has sounded a new alarm for the food industry and consumers. This surge has put production units—from packaging manufacturers to food factories—under a cost crisis, and its effects are now directly reflected in the prices of essential goods.',
    tag: 'News',
    link: '/en/news/tab/Rising-Polypropylene-Prices'
  },
]
useSeoMeta({
  title: 'News | POLYCHEM',
  description: 'Stay updated with the latest news, market reports, product launches, and updates from POLYCHEM in the polymer and masterbatch industry.',
  ogTitle: 'Polymer & Masterbatch Industry News | POLYCHEM',
  ogDescription: 'Stay updated with the latest news, market reports, product launches, and updates from POLYCHEM in the polymer and masterbatch industry.',
  ogUrl: 'https://polychemmb.com/en/news',
  ogType: 'website',
})
const changeImage = (index) => {
  currentImageIndex.value = index
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

body {
  font-family: 'Montserrat', sans-serif;
}

.border-3 {
  border-width: 3px;
}

.grayscale-img {
  filter: grayscale(100%);
}

.btn-slide-down::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: #ffcd05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}

.btn-slide-down:hover::before {
  transform: translateY(0);
}

.btn-slide-down:hover {
  color: #fff !important;
}

.archive-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 3px;
  background-color: #ffcd05;
  transition: width 0.4s ease;
}

.archive-link:hover::after {
  width: 100%;
}
</style>