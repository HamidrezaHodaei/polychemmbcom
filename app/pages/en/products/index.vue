<template>
  <Navbar />
  <div class="page">
    <div class="wrap">
      <div class="brand-header">
        <img src="/Polychem-1.png" alt="POLYCHEM Logo" class="brand-logo brand-logo--mobile" />
      </div>
      <div class="header-row">
        <h1 class="sr-only">PolyChem Masterbatch & Compound products</h1>
      </div>
      <div class="toolbar">
        <div class="tabs">
          <button
            v-for="tab in tabs"
            :key="tab"
            class="tab"
            :class="{ 'tab--active': activeTab === tab }"
            @click="activeTab = tab"
          >
            {{ tab }}
          </button>
        </div>

        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" width="20" height="20" fill="none">
            <circle cx="10.5" cy="10.5" r="6.5" stroke="currentColor" stroke-width="2.2" />
            <line x1="15.5" y1="15.5" x2="21" y2="21" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" />
          </svg>
          <input
            v-model="searchQuery"
            type="text"
            class="search-input"
            placeholder="Search products..."
          />
          <button class="search-go" @click="searchQuery = searchQuery">SEARCH</button>
        </div>
      </div>

      <div class="grid">
        <div v-for="item in filteredItems" :key="item.id" class="card">
          <div class="card-top">
            <div class="thumb" :style="{ background: item.gradient }">
              <img v-if="item.image" class="thumb-image" :src="item.image" :alt="item.name" />
              <span v-else class="thumb-letter">{{ item.name.charAt(0) }}</span>
            </div>
            <div class="info">
              <div class="tag">{{ item.category }}</div>
              <h3 class="name">{{ item.name }}</h3>
              <p class="desc">{{ item.description }}</p>
            </div>
          </div>

          <div class="bottom">
            <a :href="`/en/products/${productFileMap[item.name] || item.name}`" class="view-btn">
              <svg class="view-btn-border" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="100%" height="100%" fill="none" />
              </svg>
              <span class="view-btn-label">
                View Product
                <svg class="view-btn-icon" viewBox="0 0 24 24" width="11" height="11" fill="none">
                  <path d="M9 6l6 6-6 6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
              </span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer />
</template>

<script setup>
import { computed, ref } from 'vue'
import Navbar from '~/components/en/layout/navbar.vue'
import Footer from '~/components/en/layout/footer.vue'

const tabs = ['All', 'Filler Masterbatch', 'Color Masterbatch', 'Additive Masterbatch', 'Compound']
const activeTab = ref('All')
const searchQuery = ref('')

const items = ref([
  {
    id: 1,
    name: 'ROTOCHEM 0955W',
    description: 'Specialized white compound for rotational molding with strong UV stability and consistent surface finish.',
    category: 'Compound',
    gradient: 'linear-gradient(135deg,#f8d39f,#e28a2a)',
    image: '/Product/index/955w-p.jpg',
  },
  {
    id: 2,
    name: 'ROTOCHEM 0955B',
    description: 'Blue rotational molding compound designed for durable, bright, and impact-resistant molded parts.',
    category: 'Compound',
    gradient: 'linear-gradient(135deg,#8ec5ff,#3f6fe6)',
    image: '/Product/index/955B.webp',
  },
  {
    id: 3,
    name: 'POLYFIL F700',
    description: 'High-performance polyethylene compound for HDPE blown film applications with excellent uniformity.',
    category: 'Compound',
    gradient: 'linear-gradient(135deg,#e6d9b8,#b08b46)',
    image: '/Product/index/polyfilf700-2.webp',
  },
  {
    id: 4,
    name: 'SLIPCHEM E 178',
    description: 'Slip masterbatch that reduces friction in film winding, bag making, and packaging processes.',
    category: 'Additive Masterbatch',
    gradient: 'linear-gradient(135deg,#d7f1d3,#5fae72)',
    image: '/Product/index/slipchem.webp',
  },
  {
    id: 5,
    name: 'POLYFILL 1300 EWA',
    description: 'Calcium carbonate filler masterbatch for improved stiffness, output, and density in PE applications.',
    category: 'Filler Masterbatch',
    gradient: 'linear-gradient(135deg,#f5cfc6,#c77764)',
    image: '/Product/index/1300.webp',
  },
  {
    id: 6,
    name: 'HDCHEM 4760',
    description: 'Blow molding compound with good flow, impact strength, rigidity, and ESCR performance.',
    category: 'Compound',
    gradient: 'linear-gradient(135deg,#e7cda5,#a97043)',
    image: '/Product/index/Hdchem-2.webp',
  },
  {
    id: 7,
    name: 'RAFCOLOR 1560',
    description: 'High-concentration white masterbatch for raffia, tapes, and woven products with excellent dispersion.',
    category: 'Color Masterbatch',
    gradient: 'linear-gradient(135deg,#f4f4f4,#b7b7b7)',
    image: '/Product/index/Rafcolor-1.webp',
  },
  {
    id: 8,
    name: 'CALCICHEM 126 FP',
    description: 'Polypropylene-based filler masterbatch with high calcium carbonate loading for productivity and quality.',
    category: 'Filler Masterbatch',
    gradient: 'linear-gradient(135deg,#d8d8e8,#8b8ea9)',
    image: '/Product/index/calcum-126.webp',
  },
  {
    id: 9,
    name: 'CALCICHEM 110 FRF',
    description: 'Mineral modifier designed for films, raffia, and ropes with excellent cost-performance balance.',
    category: 'Filler Masterbatch',
    gradient: 'linear-gradient(135deg,#e0c7a3,#8d6a3f)',
    image: '/Product/index/110-1.webp',
  },
  {
    id: 10,
    name: 'CALCICHEM 275 PM',
    description: 'High-performance mineral masterbatch tailored for BOPP, CPP, and OPP film extrusion.',
    category: 'Filler Masterbatch',
    gradient: 'linear-gradient(135deg,#ddd2c0,#8e6d4f)',
    image: '/Product/index/275-1.webp',
  },
  {
    id: 11,
    name: 'UVCHEM MB R18',
    description: 'UV stabilizer masterbatch that improves outdoor durability and color stability in polypropylene products.',
    category: 'Additive Masterbatch',
    gradient: 'linear-gradient(135deg,#cfe6ff,#5c88c9)',
    image: '/Product/index/Uv-chem.webp',
  },
])

const filteredItems = computed(() => {
  let list = items.value

  if (activeTab.value !== 'All') {
    list = list.filter((item) => item.category === activeTab.value)
  }

  const q = searchQuery.value.trim().toLowerCase()
  if (q) {
    list = list.filter(
      (item) =>
        item.name.toLowerCase().includes(q) ||
        item.description.toLowerCase().includes(q) ||
        item.category.toLowerCase().includes(q)
    )
  }

  return list
})

const productFileMap = {
  'ROTOCHEM 0955W': '0955W',
  'ROTOCHEM 0955B': '0955B',
  'POLYFIL F700': 'POLYFIL-F700',
  'SLIPCHEM E 178': 'SlIPCHEM-E-178',
  'POLYFILL 1300 EWA': 'POLYFIL-1300-EWA',
  'HDCHEM 4760': 'HDCHEM-4760',
  'RAFCOLOR 1560': 'RAFCOLOR-1560',
  'CALCICHEM 126 FP': 'CALCICHEM-126-FP',
  'CALCICHEM 110 FRF': 'CALCICHEM-110-FRF',
  'CALCICHEM 275 PM': 'CALCICHEM-275-PM',
  'UVCHEM MB R18': 'UVCHEM-MB-R18',
}

// SEO: meta tags, Open Graph/Twitter, canonical + hreflang, JSON-LD product list
useSeoMeta({
  title: 'Products | POLYCHEM',
  description:
    "Browse PolyChem's filler, color, and additive masterbatches and polymer compounds — including ROTOCHEM, POLYFIL, CALCICHEM, and UVCHEM product lines.",
  ogTitle: 'Masterbatch & Compound products | POLYCHEM',
  ogDescription:
    "Browse PolyChem's filler, color, and additive masterbatches and polymer compounds.",
  ogType: 'website',
  ogUrl: 'https://polychemmb.com/en/products',
  ogImage: 'https://polychemmb.com/Polychem-1.png',
  twitterCard: 'summary_large_image',
  twitterTitle: 'Masterbatch & Compound products | PolyChem',
  twitterDescription:
    "Browse PolyChem's filler, color, and additive masterbatches and polymer compounds.",
  twitterImage: 'https://polychemmb.com/Polychem-1.png',
})

useHead({
  link: [
    { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap',
    },
    { rel: 'canonical', href: 'https://polychemmb.com/en/products' },
    { rel: 'alternate', hreflang: 'en', href: 'https://polychemmb.com/en/products' },
    { rel: 'alternate', hreflang: 'fa', href: 'https://polychemmb.com/fa/products' },
    { rel: 'alternate', hreflang: 'ar', href: 'https://polychemmb.com/ar/products' },
    { rel: 'alternate', hreflang: 'tr', href: 'https://polychemmb.com/tr/products' },
    { rel: 'alternate', hreflang: 'x-default', href: 'https://polychemmb.com/en/products' },
  ],
  script: [
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        itemListElement: items.value.map((item, index) => ({
          '@type': 'ListItem',
          position: index + 1,
          item: {
            '@type': 'Product',
            name: item.name,
            description: item.description,
            category: item.category,
            image: `https://polychemmb.com${item.image}`,
            url: `https://polychemmb.com/en/products/${productFileMap[item.name] || item.name}`,
          },
        })),
      }),
    },
  ],
})
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.page {
  min-height: 100vh;
  background: #f2f2f2;
  font-family: 'Montserrat', 'Segoe UI', sans-serif;
  padding: 24px 16px 60px;
}

.wrap {
  max-width: 1320px;
  margin: 0 auto;
}

.brand-header {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-bottom: 24px;
}

.brand-logo {
  width: auto;
  object-fit: contain;
}

.brand-logo--mobile {
  display: none;
  height: 40px;
}

.brand-logo--desktop {
  display: block;
  height: 42px;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Toolbar row (search + tabs side by side, aligned with the grid) */
.toolbar {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 32px;
}

/* Search box */
.search-box {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  border: 1.5px solid #d8d8dc;
  border-radius: 999px;
  padding: 4px 4px 4px 18px;
  flex: 0 1 340px;
  transition: border-color 0.2s ease;
}

.search-box:hover,
.search-box:focus-within {
  border-color: #ffd000;
}

.search-icon {
  flex-shrink: 0;
  color: #9b9ba3;
  transition: color 0.2s ease;
}

.search-box:hover .search-icon,
.search-box:focus-within .search-icon {
  color: #ffd000;
}

.search-input {
  flex: 1 1 auto;
  min-width: 0;
  border: none;
  outline: none;
  background: transparent;
  font-family: inherit;
  font-size: 13px;
  color: #1c1c22;
  padding: 8px 0;
}

.search-input::placeholder {
  color: #c2c2c8;
}

.search-go {
  flex-shrink: 0;
  border: none;
  background: transparent;
  color: #1c1c22;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.04em;
  padding: 9px 16px;
  border-radius: 999px;
  cursor: pointer;
  transition: background 0.25s ease, color 0.25s ease, box-shadow 0.25s ease, transform 0.15s ease;
}

.search-go:hover {
  background: #ffd000;
  color: #1c1c22;
  box-shadow: 0 6px 14px rgba(255, 208, 0, 0.4);
}

.search-go:active {
  transform: scale(0.94);
}

/* Tabs — wrap onto multiple rows instead of scrolling or squeezing, so every tab stays fully visible */
.tabs {
  display: flex;
  flex-wrap: wrap;
  background: #ebebeb;
  border-radius: 18px;
  padding: 6px;
  gap: 6px;
  flex: 1 1 320px;
  min-width: 0;
}

.tab {
  flex: 0 0 auto;
  border: none;
  background: transparent;
  color: #131212;
  font-family: inherit;
  font-size: 14px;
  font-weight: 500;
  padding: 10px 16px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.tab:hover {
  color: #ffd61e;
}

.tab--active {
  background: #ffffff;
  color: #1c1c22;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.06);
}

/* Header */
.header-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 20px;
  padding: 0 4px;
  gap: 12px;
}

.title {
  font-size: 26px;
  font-weight: 700;
  color: #1c1c22;
  margin: 0 0 6px;
}

.subtitle {
  font-size: 13px;
  color: #7f7f87;
  margin: 0;
}

.count {
  font-size: 13px;
  color: #a3a3ab;
  white-space: nowrap;
}

/* Grid */
.grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 26px;
}

/* Tablet: stack search below tabs, let tabs use full width with scroll */
@media (max-width: 1024px) {
  .toolbar {
    flex-direction: column;
    align-items: stretch;
    gap: 12px;
  }

  .tabs {
    width: 100%;
    flex: 1 1 auto;
  }

  .search-box {
    flex-basis: auto;
    width: 100%;
  }
}

@media (max-width: 900px) {
  .grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 600px) {
  .brand-header {
    justify-content: center;
    margin-bottom: 20px;
  }

  .brand-logo--mobile {
    display: block;
    height: 38px;
  }

  .brand-logo--desktop {
    display: none;
  }

  .grid {
    grid-template-columns: 1fr;
  }

  .header-row {
    flex-direction: column;
  }

  .tab {
    font-size: 13px;
    padding: 9px 14px;
  }

  .search-input {
    font-size: 14px; /* avoid iOS auto-zoom on focus */
  }
}

/* Card */
.card {
  background: #ffffff;
  border-radius: 24px;
  padding: 24px;
  box-shadow: 0 2px 10px rgba(20, 20, 30, 0.04);
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}

.card:hover {
  box-shadow: 0 8px 20px rgba(20, 20, 30, 0.08);
  transform: translateY(-2px);
}

.card-top {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
}

.thumb {
  flex-shrink: 0;
  width: 96px;
  height: 96px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 30px;
  font-weight: 700;
  overflow: hidden;
}

.thumb-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.thumb-letter {
  line-height: 1;
}

.info {
  min-width: 0;
}

.tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #6b6b76;
  margin-bottom: 8px;
}

.name {
  font-size: 18px;
  font-weight: 600;
  color: #1c1c22;
  margin: 0 0 6px;
  line-height: 1.3;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  line-clamp: 2;
}

.desc {
  font-size: 13.5px;
  color: #a8a8b0;
  line-height: 1.6;
  margin: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  line-clamp: 3;
}

.meta {
  font-size: 11.5px;
  color: #b3b3ba;
  margin-bottom: 14px;
}

.bottom {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 12px;
}

.view-btn {
  align-items: center;
  background: #ffffff;
  border: none;
  color: #1c1c22;
  cursor: pointer;
  display: inline-flex;
  font-family: inherit;
  font-size: 11px;
  font-weight: 400;
  height: 32px;
  justify-content: center;
  letter-spacing: 0.03em;
  overflow: visible;
  padding: 0 14px;
  position: relative;
  text-decoration: none;
  text-transform: uppercase;
  transition: background 0.3s ease, color 0.3s ease, font-weight 0.3s ease, letter-spacing 0.3s ease;
  width: 170px;
}

.view-btn-border {
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  width: 100%;
}

.view-btn-border rect {
  fill: none;
  stroke: #ffd000;
  stroke-width: 1.2;
  stroke-dasharray: 404, 0;
  transition: all 0.35s linear;
}

.view-btn:hover {
  background: rgba(255, 255, 255, 0);
  font-weight: 600;
  letter-spacing: 0.08em;
}

.view-btn:hover .view-btn-border rect {
  stroke-dasharray: 15, 298;
  stroke-dashoffset: 47;
  stroke-width: 1.6;
  transition: all 1.35s cubic-bezier(0.19, 1, 0.22, 1);
}

.view-btn:active {
  transform: scale(0.97);
}

.view-btn-label {
  align-items: center;
  display: inline-flex;
  gap: 6px;
  position: relative;
  z-index: 2;
}

.view-btn-icon {
  flex-shrink: 0;
}

.stepper {
  display: flex;
  align-items: center;
  gap: 10px;
}

.qty {
  font-size: 14px;
  font-weight: 600;
  color: #55555c;
  width: 14px;
  text-align: center;
}

.qty--muted {
  color: #c7c7cd;
}

.step-btn {
  width: 30px;
  height: 30px;
  border-radius: 999px;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.15s ease, transform 0.1s ease;
}

.step-btn:active:not(:disabled) {
  transform: scale(0.92);
}

.step-btn--minus {
  background: #f0f0f2;
  color: #a3a3ab;
}

.step-btn--minus:hover:not(:disabled) {
  background: #e4e4e7;
}

.step-btn--minus:disabled {
  color: #d4d4d8;
  cursor: not-allowed;
}

.step-btn--plus {
  background: #3d7dfb;
  color: #ffffff;
  box-shadow: 0 4px 10px rgba(61, 125, 251, 0.35);
}

.step-btn--plus:hover:not(:disabled) {
  background: #2c6cf0;
}

.step-btn--plus-disabled {
  background: #f0f0f2 !important;
  color: #d4d4d8 !important;
  box-shadow: none !important;
  cursor: not-allowed;
}
</style>