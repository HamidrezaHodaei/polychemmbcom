<template>
  <section class="chemistry-cards-section" ref="sectionRef" dir="rtl">
    <div class="container">
      <div class="cards-container">
        <!-- render rows of 2 cards each -->
        <div class="row" v-for="(rowCards, rIdx) in rows" :key="rIdx">
          <div class="col" v-for="(card, cIdx) in rowCards" :key="rIdx * 2 + cIdx">
            <div class="single-card-wrapper">
              <a :href="card.link">
                <div class="card-hover-container">
                  <!-- Image (left on desktop) -->
                  <div class="card-image">
                    <img :src="card.image" :alt="card.title" />
                  </div>

                  <!-- Content (right on desktop) -->
                  <div class="card-content">
                    <span class="card-badge">{{ card.badge }}</span>
                    <h3 class="card-title">{{ card.title }}</h3>
                    <p class="card-date">{{ card.date }}</p>
                    <button class="card-button"><span>اقرأ المزيد</span></button>
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
  '/Tabriz-Plast-2025-1.webp',
  '/Visit-tabriz-3.webp'
]

const cards = ref([
  {
    badge: 'أخبار',
    title: 'شركة "POLYCHEM" تُتوّج كأفضل منشأة صناعية في منطقة آراس الحرة',
    date: '1 يوليو 2026',
    link: '/ar/news/tab/Polychem_Aras_Top_Industrial_Unit_Achievement_2026',
    image: '/News/Polychem_Aras_Top_Industrial_Unit_Achievement_2026.webp'
  },
  {
    badge: 'حدث',
    title: 'بوليكيم تشارك في معرض طبرز بلاست 2025 الدولي الثاني والعشرين الخاص',
    date: '16-19 ديسمبر 2025',
    link: '/ar/news/tab/tabriz-plast-2025',
    image: backgroundImages[5]
  }, 
  {
    badge: 'أخبار',
    title: 'رئيس منظمة الصناعة والمعادن والتجارة في شرق أذربيجان يزور POLYCHEM في معرض تبريز بلاست 2025',
    date: '17 ديسمبر 2025',
    link: '/ar/news/tab/Official-Visit-Engineer-Parnian-Tabriz-Plast-2025',
    image: backgroundImages[4]
  },
  {
    badge: 'حدث',
    title: 'بوليكيم تتطلع للمشاركة في معرض بلاست يوراسيا اسطنبول 2025',
    date: '3-6 ديسمبر 2025',
    link: '/ar/news/tab/plast-eurasia-2025',
    image: backgroundImages[0]
  },
  {
    badge: 'أخبار',
    title: 'زيارة مدير الفرع الرئيسي لبنك الصناعة والمعادن',
    date: '24 نوفمبر 2025',
    link: '/ar/news/tab/Visit-of-the-CEO-of-Bank-of-Industry',
    image: backgroundImages[1]
  },
  {
    badge: 'أخبار',
    title: 'إطلاق منتج جديد: HDCHEM 4760 – مركب صب انتفاخي فائق',
    date: '14 نوفمبر 2025',
    link: '/ar/news/tab/New-Product-Launch-HDCHEM-4760',
    image: backgroundImages[3]
  }
])

// chunk into rows of 2
const rows = computed(() => {
  const cardsToDisplay = isMobile.value ? cards.value.slice(0, 2) : cards.value
  const out = []
  for (let i = 0; i < cardsToDisplay.length; i += 2) {
    out.push(cardsToDisplay.slice(i, i + 2))
  }
  return out
})

const sectionRef = ref(null)
const navbarHeight = ref(60) // تنظیم بر اساس ارتفاع navbar واقعی شما
const isMobile = ref(false)
const mobileBreakpoint = 991

const updateIsMobile = () => {
  isMobile.value = window.innerWidth <= mobileBreakpoint
}

const measureAndApplyHeight = () => {
  // do not force a fixed height on small screens — let content size naturally
  const mobileBreakpoint = 991
  if (!sectionRef.value) return
  if (window.innerWidth <= mobileBreakpoint) {
    // remove previously set fixed card height so cards expand to fit content on mobile
    sectionRef.value.style.removeProperty('--card-height')
    return
  }

  // target card link for "Global Cast Low-Density"
  const targetHref = '/news/Cast_LowDensity_PE_Gloves_Market_Report_2032'
  const anchor = sectionRef.value.querySelector(`a[href="${targetHref}"]`)
  let height = null
  if (anchor) {
    const cardContainer = anchor.querySelector('.card-hover-container') || anchor.closest('.card-hover-container')
    if (cardContainer) {
      height = cardContainer.getBoundingClientRect().height
    }
  }
  // fallback default height if target not rendered yet
  if (!height) {
    // try to pick first card height or use default
    const firstCard = sectionRef.value.querySelector('.card-hover-container')
    height = firstCard ? firstCard.getBoundingClientRect().height : 320
  }
  sectionRef.value.style.setProperty('--card-height', `${Math.round(height)}px`)
}

const handleScroll = () => {
  // فقط در موبایل فعال شود
  const mobileBreakpoint = 576
  if (window.innerWidth > mobileBreakpoint) {
    // در دسکتاپ، scrolling class را حذف کن تا hover دوباره کار کند
    if (!sectionRef.value) return
    const images = sectionRef.value.querySelectorAll('.card-image img.scrolling')
    images.forEach(img => img.classList.remove('scrolling'))
    return
  }

  if (!sectionRef.value) return

  const images = sectionRef.value.querySelectorAll('.card-image img')
  images.forEach(img => {
    const rect = img.getBoundingClientRect()
    // اگر تصویر از navbar پایین‌تر است، scrolling class را اضافه کن
    if (rect.top > navbarHeight.value) {
      img.classList.add('scrolling')
    } else {
      img.classList.remove('scrolling')
    }
  })
}

let resizeObserver = null
onMounted(() => {
  // check mobile on mount
  updateIsMobile()
  // measure initially after layout
  requestAnimationFrame(measureAndApplyHeight)
  // recompute on window resize
  window.addEventListener('resize', measureAndApplyHeight)
  window.addEventListener('resize', updateIsMobile)
  // اضافه کردن scroll listener برای موبایل
  window.addEventListener('scroll', handleScroll)
  // also use ResizeObserver to catch image/content load changes
  if (window.ResizeObserver && sectionRef.value) {
    resizeObserver = new ResizeObserver(() => {
      measureAndApplyHeight()
    })
    // observe each card container
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
/* Font Faces - Tajawal */
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-ExtraLight.ttf") format("truetype");
  font-weight: 200;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Light.ttf") format("truetype");
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Medium.ttf") format("truetype");
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Bold.ttf") format("truetype");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-ExtraBold.ttf") format("truetype");
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Black.ttf") format("truetype");
  font-weight: 900;
  font-style: normal;
  font-display: swap;
}

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');

*,
*::after,
*::before {
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
  font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;
  padding: 20px;
  direction: rtl;
}

/* layout containers */
.container {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
}

.cards-container {
  position: relative;
  width: 100%;
}

.row {
  display: flex;
  gap: 20px;
  flex-wrap: nowrap;
  justify-content: center;
}

.row-top {
  margin-bottom: 0;
}

.row-bottom {
  margin-top: 0;
}

.col {
  flex: 1;
  min-width: 0;
}

.single-card-wrapper {
  height: 100%;
}

.single-card-wrapper > a {
  display: block;
  height: 100%;
  width: 100%;
  text-decoration: none;
  color: inherit;
}

/* make card look like slider: left image, right content */
.card-hover-container {
  border: 1px solid #e6e6e6;
  width: 100%;
  border-radius: 12px;
  display: flex;
  align-items: stretch;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  /* use measured height from the Global Cast Low-Density card */
  height: var(--card-height, 320px);
  background: #ffffff;
  transition: transform 0.3s ease;
}
.card-hover-container:hover { transform: translateY(-4px); }

/* image column */
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

/* remove grayscale on hover (desktop) */
.card-hover-container:hover .card-image img {
  filter: none;
}

/* mobile: scrolling class removes grayscale */
.card-image img.scrolling {
  filter: none;
}

/* content column */
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
  font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;
}
.card-title {
  color: #848484;
  font-size: 20px;
  font-weight: 600;
  line-height: 1.25;
  margin: 12px 0;
  font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;
  text-align: right;
}
.card-date {
  color: #FFCD05;
  font-size: 14px;
  margin-bottom: 10px;
  font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;
}
.card-button {
  background: transparent;
  color: #FFCD05;
  border: 2px solid #FFCD05;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  align-self: flex-end;
  position: relative;
  overflow: hidden;
  font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;
}
.card-button::before {
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
.card-button:hover::before,
.card-button:focus-visible::before {
  transform: translateY(0);
}
.card-button:hover,
.card-button:focus-visible {
  color: #ffffff;
  outline: none;
}
.card-button span {
  position: relative;
  z-index: 2;
}

/* subtle gradient overlay */
.card-gradient {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  opacity: 0.05;
  background: radial-gradient(circle at center, rgba(158,158,158,0.2) 15%, rgba(66,66,66,0.1) 50%, transparent 80%);
}

/* vertical yellow accent like Slider */
.card-content::before {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  width: 6px;
  height: 100%;
  background: #FFCD05;
  z-index: 3;
}

/* Responsive: stack image above content on small screens */
@media (max-width: 991px) {
  .row { flex-wrap: wrap; }
  .col { min-width: 50%; flex: 0 0 50%; }
  .card-hover-container {
    /* allow cards to grow with their content on small screens so text is fully visible */
    height: auto;
    min-height: 260px;
    flex-direction: column;
    overflow: visible;
  }
  .card-image { flex: 0 0 auto; max-width: 100%; height: 140px; }
  .card-content { padding: 16px; }
  .card-content::before { height: 6px; width: 100%; top: 0; left: 0; }
}

/* Mobile: full width rows and scroll-to-color behavior */
@media (max-width: 576px) {
  .col { min-width: 100%; flex: 0 0 100%; }
  .card-image { height: 200px; }
  .card-title { font-size: 18px; }
  .card-image img { filter: grayscale(100%); } /* keep images grayscale on mobile by default */
  .card-image img.scrolling { filter: none; } /* remove grayscale when scrolling */
  /* ensure mobile cards expand to fit content */
  .card-hover-container { height: auto; overflow: visible; }
}

/* ensure clickable area looks consistent */
.single-card-wrapper a { display:block; color:inherit; text-decoration:none; }
</style>