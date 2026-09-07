<template>
  <section class="chemistry-cards-section" ref="sectionRef">
    <div class="container">
      <div class="cards-container">
        <div class="row" v-for="(rowCards, rIdx) in rows" :key="rIdx">
          <div class="col" v-for="(card, cIdx) in rowCards" :key="rIdx * 2 + cIdx">
            <div class="single-card-wrapper">
              <a :href="card.link">
                <div class="card-hover-container">
                  <div class="card-image">
                    <img :src="card.image" :alt="card.title" />
                  </div>
                  <div class="card-content text-left">
                    <span class="card-badge">{{ card.badge }}</span>
                    <h3 class="card-title">{{ card.title }}</h3>
                    <p class="card-date">{{ card.date }}</p>
                    <button class="card-button text-[15px]"><span>Devamını oku</span></button>
                  </div>
                  <div class="card-gradient"></div>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'

const backgroundImages = [
  '/Eurasia-Istanbul-2025.webp',
  '/Visit-of-the-CEO-of-Bank-of-Industry.webp',
  '/HDCHEM-4760.webp',
  '/Report.webp',
  '/Tabriz-plast-1.jpg',
  '/Visit-tabriz-3.webp'
]

const cards = ref([
  {
    badge: 'Haberler',
    title: 'POLYCHEM, Aras Serbest Bölgesi’nin En İyi Sanayi Kuruluşu Seçildi',
    date: '1 Temmuz 2026',
    link: '/en/news/tab/Polychem_Aras_Top_Industrial_Unit_Achievement_2026',
    image: '/News/Polychem_Aras_Top_Industrial_Unit_Achievement_2026.webp'
  },
  {
    badge: 'Haberler',
    title: 'Maden ve Ticaret Teşkilatı Başkanı Tabriz Plast 2025\'te POLYCHEM\'i Ziyaret Etti',
    date: '17 Aralık 2025',
    link: '/tr/news/tab/Official-Visit-Engineer-Parnian-Tabriz-Plast-2025',
    image: backgroundImages[5]
  },
  {
    badge: 'Etkinlik',
    title: 'POLYCHEM, 22. Uluslararası Tabriz Plast 2025 Özel Fuarına Katıldı',
    date: '16-19 Aralık 2025',
    link: '/tr/news/tab/tabriz-plast-2025',
    image: backgroundImages[4]
  },
  {
    badge: 'Etkinlik',
    title: 'POLYCHEM, Plast Eurasia İstanbul 2025\'e katılımını duyurmaktan heyecan duyuyor.',
    date: '3-6 Aralık 2025',
    link: '/tr/news/tab/plast-eurasia-2025',
    image: backgroundImages[0]
  },
  {
    badge: 'Haberler',
    title: 'Sanayi ve Maden Bankası Merkez Şubesi Müdürü\'nün Ziyareti',
    date: '24 Kasım 2025',
    link: '/tr/news/tab/Visit-of-the-CEO-of-Bank-of-Industry',
    image: backgroundImages[1]
  },
  {
    badge: 'Haberler',
    title: 'Yeni Ürün Lansmanı: HDCHEM 4760 – Üstün Şişirme Kalıplama Bileşiği',
    date: '14 Kasım 2025',
    link: '/tr/news/tab/New-Product-Launch-HDCHEM-4760',
    image: backgroundImages[2]
  }
])

const sectionRef = ref(null)
const navbarHeight = ref(60)
const isMobile = ref(false)
const mobileBreakpoint = 576

const updateIsMobile = () => {
  isMobile.value = window.innerWidth <= mobileBreakpoint
}

const rows = computed(() => {
  const cardsToDisplay = isMobile.value ? cards.value.slice(0, 2) : cards.value
  const out = []
  for (let i = 0; i < cardsToDisplay.length; i += 2) {
    out.push(cardsToDisplay.slice(i, i + 2))
  }
  return out
})

const measureAndApplyHeight = () => {
  if (!sectionRef.value) return
  if (window.innerWidth <= 1023) {
    sectionRef.value.style.removeProperty('--card-height')
    return
  }
  const firstCard = sectionRef.value.querySelector('.card-hover-container')
  const height = firstCard ? firstCard.getBoundingClientRect().height : 320
  sectionRef.value.style.setProperty('--card-height', `${Math.round(height)}px`)
}

const handleScroll = () => {
  if (window.innerWidth > mobileBreakpoint) {
    if (!sectionRef.value) return
    const images = sectionRef.value.querySelectorAll('.card-image img.scrolling')
    images.forEach(img => img.classList.remove('scrolling'))
    return
  }
  if (!sectionRef.value) return
  const images = sectionRef.value.querySelectorAll('.card-image img')
  images.forEach(img => {
    const rect = img.getBoundingClientRect()
    if (rect.top > navbarHeight.value) {
      img.classList.add('scrolling')
    } else {
      img.classList.remove('scrolling')
    }
  })
}

let resizeObserver = null
onMounted(() => {
  updateIsMobile()
  requestAnimationFrame(measureAndApplyHeight)
  window.addEventListener('resize', measureAndApplyHeight)
  window.addEventListener('resize', updateIsMobile)
  window.addEventListener('scroll', handleScroll)
  if (window.ResizeObserver && sectionRef.value) {
    resizeObserver = new ResizeObserver(() => measureAndApplyHeight())
    sectionRef.value.querySelectorAll('.card-hover-container').forEach(el => resizeObserver.observe(el))
  }
})

onUnmounted(() => {
  window.removeEventListener('resize', measureAndApplyHeight)
  window.removeEventListener('resize', updateIsMobile)
  window.removeEventListener('scroll', handleScroll)
  if (resizeObserver) {
    resizeObserver.disconnect()
    resizeObserver = null
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');

*, *::after, *::before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.chemistry-cards-section {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f1f2f2;
  font-family: 'Montserrat', sans-serif;
  padding: 20px;
}

.container {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
}

.cards-container {
  position: relative;
  width: 100%;
  direction: rtl; /* match Persian layout direction */
}

.row {
  display: flex;
  gap: 20px;
  flex-wrap: nowrap;
  justify-content: center;
}

.col {
  flex: 1;
  min-width: 0;
}

.single-card-wrapper {
  height: 100%;
}

.card-hover-container {
  border: 1px solid #e6e6e6;
  width: 100%;
  border-radius: 12px;
  display: flex;
  align-items: stretch;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  height: var(--card-height, 320px);
  background: #ffffff;
  transition: transform 0.3s ease;
  direction: ltr; /* preserve image/content order inside cards */
}

.single-card-wrapper > a {
  display: block;
  height: 100%;
  width: 100%;
  text-decoration: none;
  color: inherit;
}
.card-hover-container:hover { transform: translateY(-4px); }

.card-image {
  position: relative;
  flex: 0 0 60%;
  max-width: 60%;
  background-color: #ffffff;
  overflow: hidden;
}
.card-image img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  filter: grayscale(100%);
  transition: filter 0.45s ease, transform 0.45s ease;
}
.card-hover-container:hover .card-image img { filter: none; }
.card-image img.scrolling { filter: none; }

.card-content {
  position: relative;
  z-index: 2;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #ffffff;
}
.card-badge {
  display: inline-block;
  background: #555555;
  color: #ffffff;
  padding: 6px 14px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  margin-bottom: 20px;
  text-transform: capitalize;
}
.card-title {
  color: #848484;
  font-size: 20px;
  font-weight: 600;
  line-height: 1.25;
  margin: 12px 0;
}
.card-date {
  color: #FFCD05;
  font-size: 14px;
  margin-bottom: 10px;
}
.card-button {
  background: transparent;
  color: #FFCD05;
  border: 2px solid #FFCD05;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  align-self: flex-start;
  position: relative;
  overflow: hidden;
}
.card-button::before {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 100%; height: 100%;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}
.card-button:hover::before,
.card-button:focus-visible::before { transform: translateY(0); }
.card-button:hover,
.card-button:focus-visible { color: #ffffff; outline: none; }
.card-button span { position: relative; z-index: 2; }

.card-gradient {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  opacity: 0.05;
  background: radial-gradient(circle at center, rgba(158,158,158,0.2) 15%, rgba(66,66,66,0.1) 50%, transparent 80%);
}

.card-content::before {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 6px; height: 100%;
  background: #FFCD05;
  z-index: 3;
}

/* ===== TABLET (600px – 1023px) ===== */
@media (min-width: 600px) and (max-width: 1023px) {
  .chemistry-cards-section { padding: 24px 16px; }
  .row { flex-wrap: wrap; gap: 16px; }
  .col { min-width: calc(50% - 8px); flex: 0 0 calc(50% - 8px); }

  .card-hover-container {
    height: auto;
    min-height: 280px;
    flex-direction: column;
    overflow: visible;
  }
  .card-image {
    flex: 0 0 auto;
    max-width: 100%;
    height: 180px;
  }
  .card-content {
    padding: 16px 20px;
  }
  .card-content::before {
    height: 6px;
    width: 100%;
    top: 0; left: 0;
  }
  .card-title { font-size: 16px; }
  .card-badge { font-size: 11px; margin-bottom: 12px; }
  .card-button { padding: 8px 16px; font-size: 13px; }
}

/* ===== MOBILE (max 599px) ===== */
@media (max-width: 599px) {
  .row { flex-wrap: wrap; gap: 16px; }
  .col { min-width: 100%; flex: 0 0 100%; }

  .card-hover-container {
    height: auto;
    min-height: 260px;
    flex-direction: column;
    overflow: visible;
  }
  .card-image {
    flex: 0 0 auto;
    max-width: 100%;
    height: 200px;
  }
  .card-content { padding: 16px; }
  .card-content::before {
    height: 6px;
    width: 100%;
    top: 0; left: 0;
  }
  .card-title { font-size: 18px; }
  .card-image img { filter: grayscale(100%); }
  .card-image img.scrolling { filter: none; }
}

/* ===== LAPTOP (1024px – 1365px) ===== */
@media (min-width: 1024px) and (max-width: 1365px) {
  .chemistry-cards-section { padding: 32px 24px; }
  .row { gap: 16px; flex-wrap: nowrap; }
  .col { flex: 1; min-width: 0; }

  .card-hover-container {
    height: var(--card-height, 280px);
  }
  .card-image {
    flex: 0 0 55%;
    max-width: 55%;
  }
  .card-content { padding: 20px; }
  .card-title { font-size: 18px; }
  .card-badge { font-size: 11px; padding: 5px 12px; }
  .card-date { font-size: 13px; }
  .card-button { padding: 8px 16px; font-size: 13px; }
}

/* ===== DESKTOP (1366px+) ===== */
@media (min-width: 1366px) {
  .row { gap: 20px; flex-wrap: nowrap; }
  .col { flex: 1; min-width: 0; }
}
</style>