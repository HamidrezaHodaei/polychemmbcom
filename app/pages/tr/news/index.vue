<template>
  <div>
    <Navbar />
    <main class="bg-gray-100">
      <section class="previews md:flex">
        <!-- Hero Section -->
        <div class="relative h-[30em] md:fixed md:top-0 md:left-0 md:h-screen md:w-[45%] bg-black">
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
        <div class="min-h-screen md:ml-[45%]">
          

          <!-- Posts -->
          <ul>
            <li
              v-for="(post, index) in posts"
              :key="index"
              class="preview transition-colors duration-200"
              :class="{ 'bg-white': index % 2 === 1 }"
              @mouseenter="changeImage(index)"
            >
              <NuxtLink :to="post.link || '#'" class="block p-8 md:px-32 md:py-16 xl:px-40">
                <div class="flex items-center gap-2 mb-1">
                  <span class="text-black text-sm">{{ post.date }}</span>
                  <span
                    v-if="post.tag"
                    class="px-2 py-1 text-xs font-semibold uppercase tracking-wider bg-[#FFCD05] text-white rounded"
                  >
                    {{ post.tag }}
                  </span>
                </div>

                <h2 class="text-[#848484] text-2xl md:text-3xl font-bold mb-2 mt-1">
                  {{ post.title }}
                </h2>

                <p class="text-[#acacad] mb-3 leading-relaxed">
                  {{ post.excerpt }}
                </p>

                <span
                  class="btn-slide-down inline-block px-2 py-2 uppercase tracking-wider text-sm text-[#FFCD05] border-3 border-[#FFCD05] rounded-lg relative overflow-hidden"
                >
<span class="relative z-10">Daha Fazla Oku</span>                </span>
              </NuxtLink>
            </li>
          </ul>

          <!-- Footer -->
          
        </div>
      </section>
    </main>

    <Chatbox />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '/components/tr/layout/navbar.vue'
import Chatbox from '/components/tr/chatbox/chatbox.vue'

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
    date: '01 Temmuz 2026',
    title: 'Polychem Aras, Aras Serbest Bölgesi’nin En İyi Sanayi Kuruluşu Seçildi',
    excerpt: 'Sanayi ve Maden Günü kapsamında Polychem Aras, Aras Serbest Bölgesi’ndeki en iyi sanayi kuruluşlarından biri olarak onurlandırıldı.',
    tag: 'Haber',
    link: '/tr/news/tab/Polychem_Aras_Top_Industrial_Unit_Achievement_2026'
  },
  {
    date: '17 Aralık 2025',
    title: 'Doğu Azerbaycan IMT Başkanı POLYCHEM’i Tabriz Plast 2025’te Ziyaret Etti',
    excerpt: 'Doğu Azerbaycan Eyaleti Sanayi, Maden ve Ticaret Örgütü (SAMT) Başkanı Mühendis Parnian, Tabriz Plast 2025 Fuarı sırasında POLYCHEM standını ziyaret etti.',
    tag: 'Haber',
    link: '/tr/news/tab/Official-Visit-Engineer-Parnian-Tabriz-Plast-2025'
  },
  {
    date: '16-19 Aralık 2025',
    title: 'POLYCHEM Tabriz Plast 2025’te',
    excerpt: 'POLYCHEM, 22. Uluslararası Özel Lastik, Plastik ve Makine Fuarı (Tabriz Plast 2025) etkinliğine katıldı.',
    tag: 'Etkinlik',
    link: '/tr/news/tab/tabriz-plast-2025'
  },
  {
    date: '3-6 Aralık 2025',
    title: 'Plast Eurasia İstanbul 2025',
    excerpt: 'POLYCHEM, bölgedeki önde gelen plastik sektörü fuarı Plast Eurasia İstanbul 2025’e katılacağını duyurmaktan heyecan duyuyor. Etkinlik 3–6 Aralık 2025 tarihlerinde TÜYAP Fuar ve Kongre Merkezi’nde gerçekleştirilecek.',
    tag: 'Etkinlik',
    link: '/tr/news/tab/plast-eurasia-2025'
  },
  {
    date: '24 Kasım 2025',
    title: 'Sanayi ve Madencilik Bankası Merkez Şube Başkanı POLYCHEM’i Ziyaret Etti',
    excerpt: 'Ziyarete bankanın çeşitli başkan yardımcıları ve üst düzey yöneticileri ile POLYCHEM şirket yöneticileri katıldı. Dr. Rezavi, mühendislik polimerleri, özel kompozitler, masterbatch’ler, polimer katkıları ve yeni nesil ürünlerin üretim hatlarını yakından inceledi, en son araştırma ve üretim başarılarını gözden geçirdi.',
    tag: 'Haber',
    link: '/tr/news/tab/Visit-of-the-CEO-of-Bank-of-Industry'
  },
  {
    date: '14 Kasım 2025',
    title: 'Yeni Ürün Lansmanı: HDCHEM 4760 – En Güçlü Blow Molding Kompoziti',
    excerpt: 'HDCHEM serisindeki en güçlü blow molding kalitesini tanıtmaktan gurur duyuyoruz: HDCHEM 4760',
    tag: 'Haber',
    link: '/tr/news/tab/New-Product-Launch-HDCHEM-4760'
  },
  {
    date: '1 Kasım 2025',
    title: 'Küresel Polipropilen ve Polipropilen Kompozit Pazar Analizi – 2032 Tahmini',
    excerpt: 'Küresel Polipropilen ve Polipropilen Kompozit Pazar Analizi, Ürün Tipi (Polipropilen (PP), Polipropilen Kompozitler), Fiber Tipi (Cam Elyafı, Karbon Elyafı, Diğerleri), Uygulama (Ambalaj, İnşaat, Otomotiv, Elektrik-Elektronik, Havacılık ve Savunma, Diğerleri) - Sektör Trendleri ve 2032 Tahmini',
    tag: 'Rapor',
    link: '/tr/news/tab/Global-Polypropylene-and-Composites-Market-Report-2032'
  },
  {
    date: '6 Aralık 2024',
    title: 'Küresel Düşük Yoğunluklu Polietilen Tek Kullanımlık Eldiven Pazarı – 2032 Tahmini',
    excerpt: 'Küresel Düşük Yoğunluklu Polietilen Tek Kullanımlık Eldiven Pazarı, Boyut Bazlı Segmentasyon (Küçük, Orta, Büyük, X-Large), Kullanıcı Tipi (Gıda ve İçecek, Medikal, Endüstriyel, Diğer), Dağıtım Kanalı (Doğrudan ve Distribütörler aracılığıyla) – 2032 Tahmini',
    tag: 'Rapor',
    link: '/tr/news/tab/Cast_LowDensity_PE_Gloves_Market_Report_2032'
  },
  {
    date: '27 Ekim 2025',
    title: 'Artan Polipropilen Fiyatları Üretim Maliyetlerini %40’a Kadar Yükseltti',
    excerpt: 'Polietilen ve polipropilen fiyatlarındaki hızlı artış, gıda sektörü ve tüketiciler için yeni bir alarm sinyali verdi. Bu artış, paketleme üreticilerinden gıda fabrikalarına kadar üretim birimlerini maliyet kriziyle karşı karşıya bıraktı ve etkisi temel ürün fiyatlarına doğrudan yansıdı.',
    tag: 'Haber',
    link: '/tr/news/tab/Rising-Polypropylene-Prices'
  },
]

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
  color: #fff;
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
