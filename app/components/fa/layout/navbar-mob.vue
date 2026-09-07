<!-- /fa/layout/navbar-mob.vue -->
<template>
  <teleport to="body">
    <div class="navigation" :style="navStyle" ref="navRef" data-nav-teleported>
      <ul>
        <li
          v-for="(item, index) in menuItems"
          :key="index"
          :class="['list', { active: activeIndex === index }]"
          @click="setActive(index)"
        >
          <a :href="item.link">
            <span class="icon" v-html="item.icon"></span>
            <span class="title font-[IRANYekan]">{{ item.title }}</span>
          </a>
        </li>
        <!-- indicator now positioned by JS for pixel-accuracy -->
        <div class="indicator" ref="indicatorRef"></div>
      </ul>
    </div>
  </teleport>
</template>

<script setup>
import { ref, computed, onMounted, watch, nextTick, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const activeIndex = ref(0)

const menuItems = [
  { 
    title: 'خانه', 
    icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>',
    link: '/fa' 
  },
  { 
    title: 'درباره ما', 
    icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
    link: '/fa/aboutus' 
  },
  { 
    title: 'اخبار', 
    icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/></svg>',
    link: '/fa/news' 
  },
  
  { 
    title: 'تماس با  ما', 
    icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>',
    link: '/fa/contact' 
  },
  { 
    title: 'ورود مشتریان', 
    icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>',
    link: '/clientarea/login' 
  }
]

// navStyle now includes --count and --idx (active index) + colors
const navStyle = computed(() => ({
  '--nav-bg': colors.value.bg,
  '--indicator': colors.value.indicator,
  '--count': menuItems.length,
  '--idx': activeIndex.value
}))

// رنگ‌ها بر اساس مسیر (می‌توانید تنظیمات را تغییر دهید)
const routeToColors = (path) => {
  if (path === '/' || path === '/home') {
    return { bg: '#ffffff', indicator: '#f7cc40' }
  }
  return { bg: '#f3f4f6', indicator: '#f7cc40' }
}
const colors = computed(() => routeToColors(route.path))

// پیدا کردن ایندکس براساس مسیر فعلی
const findIndexForRoute = (path) => {
  // 1. تطابق دقیق (Exact match)
  const exactIdx = menuItems.findIndex(item => item.link === path)
  if (exactIdx !== -1) return exactIdx

  // 2. تطابق با شروع مسیر (Starts with) - طولانی‌ترین مسیر را انتخاب می‌کنیم
  let bestIdx = -1
  let maxLen = 0
  
  for (let i = 0; i < menuItems.length; i++) {
    const link = menuItems[i].link
    if (!link) continue
    
    // از مچ شدن روت اصلی '/' با همه چیز جلوگیری می‌کنیم مگر اینکه دقیقاً '/' باشد
    if (link !== '/' && path.startsWith(link)) {
       if (link.length > maxLen) {
         maxLen = link.length
         bestIdx = i
       }
    }
  }
  
  if (bestIdx !== -1) return bestIdx
  
  // 3. اگر هیچکدام مچ نشدند و مسیر روت است
  if (path === '/' || path === '/home') {
     const homeIdx = menuItems.findIndex(i => i.link === '/' || i.link === '/home')
     return homeIdx >= 0 ? homeIdx : 0
  }
  
  if (path.startsWith('/fa/products')) return -1

  return 0
}

const setActive = (index) => {
  activeIndex.value = index
}

// --- NEW / CHANGED: refs and indicator logic ---
const navRef = ref(null)
const indicatorRef = ref(null)
const liNodes = ref([])

// update indicator position/width based on actual DOM measurements
const updateIndicator = async () => {
  await nextTick()
  const nav = navRef.value
  const indicator = indicatorRef.value
  if (!nav || !indicator) return

  const items = nav.querySelectorAll('ul > li')
  liNodes.value = Array.from(items)
  const idx = activeIndex.value
  const target = liNodes.value[idx]
  if (!target) {
    indicator.style.width = ''
    indicator.style.transform = ''
    return
  }

  const ulRect = nav.querySelector('ul').getBoundingClientRect()
  const tRect = target.getBoundingClientRect()
  const offsetLeft = tRect.left - ulRect.left
  const width = tRect.width

  indicator.style.width = `${width}px`
  indicator.style.transform = `translateX(${offsetLeft}px)`
}

const cleanup = []
const onResize = () => updateIndicator()

onMounted(() => {
  activeIndex.value = findIndexForRoute(route.path)
  updateIndicator()
  window.addEventListener('resize', onResize)
  cleanup.push(() => window.removeEventListener('resize', onResize))
})

onBeforeUnmount(() => {
  cleanup.forEach(fn => fn())
})

watch(() => activeIndex.value, () => updateIndicator())
watch(() => route.path, (newPath) => {
  activeIndex.value = findIndexForRoute(newPath)
  updateIndicator()
})

</script>

<style scoped>

* {
  margin: 0;
  padding: 0;
  font-family: "IRANYekan", sans-serif;
  box-sizing: border-box;
}

.navigation {
  position: fixed !important;
  bottom: calc(env(safe-area-inset-bottom, 0px) + 12px) !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: min(450px, calc(100% - 40px));
  max-width: 100%;
  height: 95px;
  border-radius: 50px;
  background-color: var(--nav-bg, #fff);
  z-index: 9999 !important;
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.1);
  padding: 0 8px;
}

.navigation ul {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
}

.navigation ul li {
  position: relative;
  list-style: none;
  flex: 1;
  min-width: 0; /* ← مهم: اجازه می‌دهد flex item از محدوده خارج نشود */
  height: 100%;
  z-index: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.navigation ul li a {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: 100%;
  text-align: center;
  color: #666;
  gap: 8px;
  padding: 0 2px; /* ← فاصله کوچک از لبه‌ها */
  overflow: hidden; /* ← جلوگیری از سرریز محتوا */
}

.navigation ul li a .icon {
  width: 45px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: 0.5s;
  flex-shrink: 0; /* ← آیکون هرگز کوچک نمی‌شود */
}

.navigation ul li a .icon :deep(svg) {
  width: 28px;
  height: 28px;
  transition: 0.3s;
}

/* 🚀 آیکون هنگام فعال‌شدن بالا می‌آید */
.navigation ul li.active a .icon {
  transform: translateY(10px);
  color: #fff;
}

/* svg کمی بزرگ‌تر می‌شود */
.navigation ul li.active a .icon :deep(svg) {
  transform: scale(1.15);
}

/* متن پایین‌تر می‌آید */
.navigation ul li.active a .title {
  transform: translateY(10px);
  color: #fff;
  opacity: 0;
}

.navigation ul li a .title {
  font-size: 11px;
  transition: 0.3s;
  color: #666;

  /* ← اضافه شده: جلوگیری از خروج متن از کادر */
  display: block;
  width: 100%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: center;
  line-height: 1.2;
}

/* ← صفحه‌های متوسط موبایل: فونت کمی کوچک‌تر */
@media (max-width: 420px) {
  .navigation ul li a .title {
    font-size: 9.5px;
  }
}

/* ← صفحه‌های کوچک موبایل: فونت حداقلی + فشرده‌سازی */
@media (max-width: 360px) {
  .navigation ul li a .title {
    font-size: 8px;
    letter-spacing: -0.3px;
  }

  .navigation ul li a .icon {
    width: 36px;
    height: 36px;
  }

  .navigation ul li a .icon :deep(svg) {
    width: 22px;
    height: 22px;
  }
}

/* Indicator circle */
.navigation ul .indicator {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  transition: transform 0.36s cubic-bezier(.2,.9,.2,1), width 0.36s;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
  z-index: 0;
}

.navigation ul .indicator::before {
  content: "";
  position: absolute;
  width: 55px;
  height: 55px;
  background-color: var(--indicator, #f7cc40);
  border-radius: 50%;
  top: 18px;
  left: 50%;
  transform: translateX(-50%);
  transition: 0.36s;
  z-index: 0;
}

.navigation ul li {
  z-index: 1;
}

.navigation {
  bottom: calc(env(safe-area-inset-bottom, 0px) + 20px);
}

@media (min-width: 1025px) {
  .navigation[data-nav-teleported] {
    display: none !important;
    visibility: hidden !important;
    pointer-events: none !important;
  }
}

@media (max-width: 1024px) {
  .navigation[data-nav-teleported] {
    position: fixed !important;
    bottom: calc(env(safe-area-inset-bottom, 0px) + 12px) !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: min(500px, calc(100% - 40px)) !important;
    height: 90px !important;
    z-index: 9999 !important;
    pointer-events: auto !important;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    backface-visibility: hidden;
  }

  .navigation[data-nav-teleported] ul,
  .navigation[data-nav-teleported] ul li,
  .navigation[data-nav-teleported] ul li a {
    pointer-events: auto !important;
  }

  .navigation[data-nav-teleported] ul .indicator::before {
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
  }
}
</style>