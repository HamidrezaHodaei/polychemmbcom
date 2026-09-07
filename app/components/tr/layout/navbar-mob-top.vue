<!-- /components/tr/layout/navbar-mob-top.vue -->
<template>
  <div class="app-container">
    <nav class="navbar">
      <div class="logo-container">
        <a @click.prevent="goHome" class="block cursor-pointer">
          <img src="/english logo W1.png" alt="POLYCHEM Logo" class="logo" />
        </a>
      </div>
      
      <div class="right-section">
        <button class="menu-btn" @click="toggleMenu">
          {{ menuOpen ? 'Kapat' : 'Ürünler' }}
        </button>
        
        <div class="divider"></div>
        
        <button class="lang-selector-btn" @click="toggleLangMenu">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
      </div>
    </nav>

    <transition name="slide">
      <div v-if="langMenuOpen" class="glass-menu-fullscreen">
        <div class="menu-scroll-wrapper">
          <ul class="menu-list">
            <li class="menu-item" :class="{ active: currentLang === 'en' }" @click="handleLangClick('en')">
              ENGLISH
            </li>
            <li class="menu-item font-iranyekan" :class="{ active: currentLang === 'ar' }" @click="handleLangClick('ar')">
              العربية
            </li>
            <li class="menu-item font-iranyekan" :class="{ active: currentLang === 'fa' }" @click="handleLangClick('fa')">
              فارسی
            </li>
            <li class="menu-item" :class="{ active: currentLang === 'tr' }" @click="handleLangClick('tr')">
              TÜRKÇE
            </li>
          </ul>
        </div>
      </div>
    </transition>

    <transition name="slide">
      <div v-if="menuOpen" class="glass-menu-fullscreen">
        <div class="menu-scroll-wrapper">
          <ul class="menu-list">
            <li 
              v-for="product in useCases" 
              :key="product.index"
              class="menu-item" 
              @click="navigateToProduct(product)"
            >
              {{ product.title }}
            </li>
          </ul>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, watch, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useLang } from '~/composables/useLang'

const router = useRouter()
const route = useRoute()
const { switchLang, currentLang } = useLang()

const menuOpen = ref(false)
const langMenuOpen = ref(false)

// ✅ فقط overflow — بدون position: fixed
watch([menuOpen, langMenuOpen], ([newMenuOpen, newLangMenuOpen]) => {
  if (process.client) {
    if (newMenuOpen || newLangMenuOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
  }
})

onUnmounted(() => {
  if (process.client) {
    document.body.style.overflow = ''
    showMobileNavbar()
    showChatbox()
  }
})

const useCases = [
  { title: 'ROTOCHEM 0955W', index: 0, path: '/tr/products/0955W' },
  { title: 'ROTOCHEM 0955B', index: 1, path: '/tr/products/0955B' },
  { title: 'POLYFIL F700', index: 2, path: '/tr/products/POLYFIL-F700' },
  { title: 'POLYFIL 1300 EWA', index: 3, path: '/tr/products/POLYFIL-1300-EWA' },
  { title: 'HDCHEM 4760', index: 4, path: '/tr/products/HDCHEM-4760' },
  { title: 'SlIPCHEM E 178', index: 5, path: '/tr/products/SlIPCHEM-E-178' },
  { title: 'RAFCOLOR 1560', index: 6, path: '/tr/products/RAFCOLOR-1560' },
  { title: 'CALCICHEM 126 FP', index: 7, path: '/tr/products/CALCICHEM-126-FP' },
  { title: 'CALCICHEM 110 FRF', index: 8, path: '/tr/products/CALCICHEM-110-FRF' },
  { title: 'CALCICHEM 275 PM', index: 9, path: '/tr/products/CALCICHEM-275-PM' },
  { title: 'UVCHEM MB-R18', index: 10, path: '/tr/products/UVCHEM-MB-R18' },
]

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
  if (menuOpen.value) {
    langMenuOpen.value = false
    hideMobileNavbar()
    hideChatbox()
  } else {
    showMobileNavbar()
    showChatbox()
  }
}

const toggleLangMenu = () => {
  langMenuOpen.value = !langMenuOpen.value
  if (langMenuOpen.value) {
    menuOpen.value = false
    hideMobileNavbar()
    hideChatbox()
  } else {
    showMobileNavbar()
    showChatbox()
  }
}

const hideMobileNavbar = () => {
  if (process.client) {
    const navbar = document.querySelector('[data-nav-teleported]')
    if (navbar) navbar.style.display = 'none'
  }
}

const showMobileNavbar = () => {
  if (process.client) {
    const navbar = document.querySelector('[data-nav-teleported]')
    if (navbar) navbar.style.display = ''
  }
}

const hideChatbox = () => {
  if (process.client) {
    const chatbox = document.querySelector('.chat-widget')
    if (chatbox) chatbox.style.display = 'none'
  }
}

const showChatbox = () => {
  if (process.client) {
    const chatbox = document.querySelector('.chat-widget')
    if (chatbox) chatbox.style.display = ''
  }
}

const handleLangClick = (lang) => {
  langMenuOpen.value = false
  switchLang(lang)
}

const goHome = () => {
  const lang = currentLang.value || 'tr'
  router.push(`/${lang}`)
}

const navigateToProduct = (product) => {
  menuOpen.value = false
  showMobileNavbar()
  showChatbox()
  if (process.client) {
    document.body.style.overflow = ''
    window.location.assign(product.path)
    return
  }
  router.push(product.path)
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

@font-face {
  font-family: 'IRANYekan';
  src: url('/Fonts/IRANYekan.ttf') format('truetype');
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Montserrat', sans-serif;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 16px;
  background: #808285;
  border: none;
  z-index: 1000;
}

.logo-container {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.logo {
  width: 60px;
  height: 60px;
  object-fit: contain;
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.1));
}

.right-section {
  display: flex;
  align-items: center;
  gap: 0;
}

.menu-btn {
  background: transparent;
  border: none;
  color: #ffffff;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.5px;
  padding: 5px 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 4px;
  min-width: 140px;
  text-align: center;
}

.menu-btn:hover {
  background: rgba(255, 255, 255, 0.15);
}

.divider {
  width: 1px;
  height: 24px;
  background-color: #ffffff;
  margin: 0 8px;
}

.lang-selector-btn {
  background: transparent;
  border: none;
  color: #ffffff;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.5px;
  padding: 8px 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: auto;
}

.lang-selector-btn svg {
  width: 20px;
  height: 20px;
}

.lang-selector-btn:hover {
  background: rgba(255, 255, 255, 0.15);
}

/* ✅ overflow روی glass-menu — اسکرول درست کار می‌کنه */
.glass-menu-fullscreen {
  position: fixed;
  top: 70px;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: calc(100vh - 70px);
  background-color: hsla(0, 0%, 81%, 0.4);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 0 -4px 32px 0 rgba(0, 0, 0, 0.1);
  z-index: 99999999;
  overflow-y: auto;
  overflow-x: hidden;
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
}

.menu-scroll-wrapper {
  width: 100%;
  min-height: 100%;
  padding: 20px 30px 80px 30px;
  display: block;
}

.menu-list {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  width: 100%;
  max-width: 600px;
}

.menu-item {
  color: #1a1a1a;
  font-size: 20px;
  font-weight: 400;
  letter-spacing: 1.5px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
  border-radius: 12px;
  margin: 8px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  -webkit-tap-highlight-color: transparent;
  min-height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.menu-item:last-child {
  border-bottom: none;
}

.menu-item:hover,
.menu-item:active {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.02);
}

.menu-item.active {
  background: rgba(255, 255, 255, 0.4);
  font-weight: 600;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.4s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateY(-20px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

@media (min-width: 601px) and (max-width: 1023px) {
  .navbar {
    height: 74px;
    padding: 0 20px;
  }

  .logo {
    width: 150px;
    height: auto;
  }

  .menu-btn {
    font-size: 14px;
    padding: 6px 10px;
    min-width: 120px;
  }

  .divider {
    height: 22px;
    margin: 0 8px;
  }

  .lang-selector-btn {
    padding: 8px 10px;
  }

  .lang-selector-btn svg {
    width: 22px;
    height: 22px;
  }

  .glass-menu-fullscreen {
    top: 74px;
    height: calc(100vh - 74px);
  }

  .menu-item {
    font-size: 22px;
    padding: 22px 20px;
    min-height: 64px;
  }
}

@media (max-width: 600px) {
  .navbar {
    height: 64px;
    padding: 0 12px;
  }

  .logo {
    width: 150px;
    height: auto;
  }

  .menu-btn {
    font-size: 14px;
    padding: 6px 8px;
    min-width: 110px;
  }

  .divider {
    height: 20px;
    margin: 0 6px;
  }

  .lang-selector-btn {
    padding: 8px;
    min-width: auto;
  }

  .lang-selector-btn svg {
    width: 18px;
    height: 18px;
  }

  .glass-menu-fullscreen {
    top: 64px;
    height: calc(100vh - 64px);
  }

  .menu-scroll-wrapper {
    padding: 16px 20px 80px 20px;
  }

  .menu-item {
    font-size: 18px;
    padding: 18px 15px;
    letter-spacing: 1px;
    min-height: 56px;
  }
}

.font-iranyekan {
  font-family: 'IRANYekan', 'Montserrat', sans-serif;
  font-size: 20px;
}
</style>