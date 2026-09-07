<!-- /components/ar/layout/navbar.vue -->
<template>
  <div dir="rtl" class="relative" style="font-family: 'Tajawal', system-ui, -apple-system, sans-serif;">
    <!-- Mobile Top Navbar (hidden on desktop) -->
    <NavbarMobTop class="md:hidden" />

    <nav class="hidden md:block bg-[#808285] fixed top-0 inset-x-0 z-50 md:border-b" dir="rtl" style="font-family: 'Tajawal', system-ui, -apple-system, sans-serif;">
      <div class="navbar-inner navbar-container">
        <div class="flex items-center h-16 md:h-20">
          <!-- Logo & Brand -->
          <div class="flex items-center justify-start md:border-r md:border-l md:border-white pl-2 md:pl-8 pr-2 md:pr-8 h-full flex-shrink-0 w-auto md:w-[230px]">
              <NuxtLink to="/ar" aria-label="Go to home" class="block">
                <img src="/english logo W1.png" alt="POLYCHEM Logo" class="w-28 md:w-40 h-28 md:h-40 object-contain" />
              </NuxtLink>
          </div>

          <!-- USE CASES with border and hover effect -->
          <!-- show PRODUCTS button on desktop only (hidden on mobile) -->
          <div class="hidden md:flex items-center h-full md:border-r md:border-white">
            <button 
              @click="toggleFullscreenMenu"
              class="nav-link flex items-center gap-2 text-[13px] text-white font-medium px-8 h-full text-white relative overflow-hidden"
              :class="{ active: productActive || isOnProductsSection }"
            >
              <span class="relative z-10">المنتجات</span>
              <svg class="w-4 h-4 relative z-10" fill="currentColor" viewBox="0 0 20 20">
                <path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/>
              </svg>
            </button>
          </div>

          <!-- Main Menu with hover effects -->
          <div class="hidden md:flex items-center flex-1 justify-center h-full">
            <NuxtLink 
              to="/ar" 
              class="nav-link text-[13px] font-medium px-8 text-white relative overflow-hidden h-full flex items-center"
            >
              <span class="relative z-10">الرئيسية</span>
            </NuxtLink>

            <NuxtLink 
              to="/ar/aboutus" 
              class="nav-link flex items-center justify-center gap-2 text-[13px] font-medium px-8 text-white relative overflow-hidden h-full w-40 "
            >
              <span class="relative z-10">معلومات عنا</span>
            </NuxtLink>

            <NuxtLink 
              to="/ar/news" 
              class="nav-link text-[13px] font-medium px-8 text-white relative overflow-hidden h-full flex items-center"
            >
              <span class="relative z-10">الأخبار</span>
            </NuxtLink>

            <NuxtLink 
              to="/ar/careers" 
              class="nav-link text-[13px] font-medium px-8 text-white relative overflow-hidden h-full flex items-center"
            >
              <span class="relative z-10">الوظائف</span>
            </NuxtLink>

            <NuxtLink 
              to="/ar/contact" 
              class="nav-link text-[13px] font-medium px-8 text-white relative overflow-hidden h-full flex items-center w-40"
            >
              <span class="relative z-10">اتصل بنا</span>
            </NuxtLink>
          </div>

          <!-- Right Side -->
<div class="hidden md:flex items-center justify-end h-full w-auto flex-shrink-0">
  <div class="relative h-full flex items-center border-l border-r border-white px-2" ref="langDropdownEn">
    <button
      @click="langOpen = !langOpen"
      class="nav-link text-[13px] font-medium px-6 h-full text-white relative overflow-hidden"
    >
      <span class="relative z-10">AR</span>
    </button>
    <div
      v-show="langOpen"
      class="absolute top-full right-0 mt-1 w-36 bg-white rounded-lg shadow-lg z-[100] overflow-hidden border border-gray-100"
    >
      <button
        class="w-full px-4 py-3 text-sm text-yellow-600 bg-yellow-50 flex items-center justify-between cursor-default"
      >
        <span class="text-xs text-yellow-400">AR</span>
        <span style="font-family: 'Tajawal', system-ui, -apple-system, sans-serif;">العربية</span>
      </button>
      <button
        @click="() => { switchLang('fa'); langOpen = false }"
        class="w-full px-4 py-3 text-sm text-gray-700 hover:bg-yellow-50 hover:text-yellow-600 transition-colors flex items-center justify-between"
      >
        <span class="text-xs text-gray-400">FA</span>
        <span style="font-family: 'IRANYekan', system-ui, -apple-system, sans-serif;">فارسی</span>
      </button>
      <button
        @click="() => { switchLang('en'); langOpen = false }"
        class="w-full px-4 py-3 text-sm text-gray-700 hover:bg-yellow-50 hover:text-yellow-600 transition-colors flex items-center justify-between"
      >
        <span class="text-xs text-gray-400 ">EN</span>
        <span>English</span>
      </button>
      <button
        @click="() => { switchLang('tr'); langOpen = false }"
        class="w-full px-4 py-3 text-sm text-gray-700 hover:bg-yellow-50 hover:text-yellow-600 transition-colors flex items-center justify-between"
      >
        <span class="text-xs text-gray-400 ">TR</span>
        <span>Türkçe</span>
      </button>
    </div>
  </div>

  <NuxtLink to="/clientarea/login" class="nav-link text-[13px] font-medium px-6 h-full text-white relative overflow-hidden border-l border-r border-white flex items-center justify-center">
    <span class="relative z-10">دخول العملاء</span>
  </NuxtLink>
</div>

          <!-- Mobile Menu Button: Hamburger Icon -->
          <button 
            @click="toggleFullscreenMenu"
            class="md:hidden ml-auto text-white hover:text-yellow-400 px-4 py-3 rounded-lg hover:bg-black/20 transition-all duration-200 flex items-center justify-center"
            aria-label="Open menu"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>

        <!-- Mobile Menu -->
        <transition name="mobile-menu">
          <!-- removed border on mobile: no border classes here -->
          <div v-if="mobileMenuOpen" class="md:hidden pb-4 bg-[#808285] max-h-[calc(100vh-64px)] overflow-y-auto">
            <div class="flex flex-col gap-2 pt-4 px-4">
              <button 
                @click="toggleFullscreenMenu"
                class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden text-left w-full"
                :class="{ active: productActive }"
              >
                <span class="relative z-10">المنتجات</span>
              </button>
              <NuxtLink to="/ar" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10">الرئيسية</span>
              </NuxtLink>
              <NuxtLink to="/ar/aboutus" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10">معلومات عنا</span>
              </NuxtLink>
              <NuxtLink to="/ar/news" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10">الأخبار</span>
              </NuxtLink>
              <NuxtLink to="/ar/careers" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10">الوظائف</span>
              </NuxtLink>
              <NuxtLink to="/ar/contact" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10">اتصل بنا</span>
              </NuxtLink>
              <div class="pt-3 mt-2">
                <button class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded block w-full text-left relative overflow-hidden mb-2">
                  <span class="relative z-10">AR</span>
                </button>
                <NuxtLink to="/ar/login" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded block w-full text-left relative overflow-hidden">
                  <span class="relative z-10">دخول</span>
                </NuxtLink>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </nav>
    <!-- Spacer to offset fixed navbar height -->
    <div class="hidden md:block h-16 md:h-20"></div>

    <!-- Mobile bottom navbar (active on small screens only) -->
    <NavbarMob class="md:hidden" />

    <!-- Render Chatbox on Home and About pages -->
    <Chatbox v-if="route.path === '/' || route.path === '/ar/aboutus'" />

    <!-- Fullscreen Menu - Mobile Optimized -->
    <div 
      v-show="isMenuOpen"
      ref="fullscreenMenu"
      class="fixed inset-0 z-40 overflow-hidden"
    >
      <div class="h-full flex flex-col md:flex-row">
        <!-- Left Side - Preview Box (hidden on mobile, 40% on desktop) -->
        <div class="hidden md:flex w-[40%] bg-gradient-to-br from-gray-50 to-white relative overflow-hidden">
          <div 
            ref="previewBox"
            class="absolute inset-0 flex items-center justify-center p-20 opacity-0"
          >
            <div class="text-center space-y-6">
               <!-- changed: show preview product image instead of static icon -->
              <img
                ref="previewImage"
                :src="hoveredItem?.image || '/Roto.webp'"
                alt="preview"
                class="w-1500 h-1500   object-cover transform scale-0"
                :style="previewImageStyle"
                
              />
            
              <!-- backdrop behind title & description (bigger, semi-transparent) -->
              <div class="inline-block bg-white/70 backdrop-blur-sm rounded-2xl px-8 py-6 max-w-[90%]">
                <div 
                  ref="previewTitle"
                  class="opacity-0 transform translate-y-4"
                  :style="previewTitleStyle"
                >
                  <h3 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3">{{ hoveredItem?.title || 'ROTOCHEM 0955W' }}</h3>
                  <p class="text-xl text-gray-600">{{ hoveredItem?.code || '' }}</p>
                </div>
                <p 
                  ref="previewDesc"
                  class="text-gray-700 text-lg max-w-md mx-auto opacity-0 transform translate-y-4 mt-3"
                  :style="previewDescStyle"
                >
                  {{ hoveredItem?.description || 'Specialized white color plastic compound for rotational molding applications. Linear medium density polyethylene copolymer with narrow molecular weight distribution and TiO2. Ideal for reliable and durable materials that withstand harsh environmental conditions.' }}
                </p>
              </div>
            </div>

            <!-- Decorative Grid -->
            <div class="absolute inset-0 opacity-5">
              <div class="grid grid-cols-8 grid-rows-8 h-full w-full">
                <div v-for="i in 64" :key="i" class="border border-gray-900"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Side - Menu Items (100% on mobile, 60% on desktop) -->
        <div class="w-full md:w-[60%] bg-white relative flex flex-col h-full">
          <div 
            ref="menuContainer"
            class="h-full flex flex-col justify-start md:justify-center px-6 md:px-16 py-6 md:py-0 opacity-0 transform translate-y-[-100%] overflow-y-auto md:overflow-y-visible"
          >
            <!-- Close Button (HIDDEN ON MOBILE) -->
            <button 
              @click="toggleFullscreenMenu"
              ref="closeButton"
              class="hidden md:flex absolute top-6 right-6 text-gray-700 hover:text-gray-900 transition-colors opacity-0 md:top-8 md:right-8 md:w-10 md:h-10 w-8 h-8 flex items-center justify-center"
              aria-label="Close menu"
            >
              <svg class="w-6 h-6 md:w-10 md:h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>

            <!-- Title -->
            <div 
              ref="menuTitle"
              class="mb-8 md:mb-12 mt-12 md:mt-16 opacity-0 transform translate-y-[-20px]"
            >
              <h2 class="text-3xl md:text-5xl font-bold text-gray-900 mb-2">منتجاتنا</h2>
              <div class="w-20 h-1 bg-yellow-500"></div>
            </div>

            <!-- Menu Items -->
            <div ref="itemsWrapper" class="space-y-1 max-h-[calc(100vh-200px)] md:max-h-[70vh] overflow-y-auto pr-4 custom-scrollbar pb-6 md:pb-0 menu-items-scroll text-[Tajawal]">
              <button
                v-for="(item, index) in useCases"
                :key="index"
                :ref="el => { if (el) menuItems[index] = el }"
                @mouseenter="handleHover(item, index)"
                @mouseleave="handleLeave"
                @click="() => handleMenuItemClick(item)"
                type="button"
                class="menu-item group flex items-center justify-between border-b border-gray-200 py-4 md:py-6 px-4 md:px-6 hover:bg-gray-50 transition-all duration-300 transform translate-y-[-30px] active:bg-gray-100 md:active:bg-transparent"
                style="opacity: 1 !important; min-height: 48px; width: 100%; text-align: left;"
              >
                <div class="flex items-center gap-3 md:gap-6 menu-item-content flex-1 min-w-0" style="opacity: 1 !important; color: #1f2937 !important;">
                  <span style="color: #6b7280 !important; opacity: 1 !important;" class="text-[11px] md:text-[13px] font-mono group-hover:text-yellow-500 transition-colors flex-shrink-0">{{ item.code }}</span>
                  <h3 style="color: #1f2937 !important; opacity: 1 !important;" class="text-lg md:text-xl font-semibold group-hover:translate-x-2 transition-transform truncate">{{ item.title }}</h3>
                </div>
                <svg class="w-5 h-5 md:w-6 md:h-6 text-gray-400 group-hover:text-yellow-500 group-hover:translate-x-2 transition-all flex-shrink-0 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick, computed, watch } from 'vue'
import gsap from 'gsap'
import NavbarMobTop from './navbar-mob-top.vue'
import NavbarMob from './navbar-mob.vue'
import Chatbox from '/components/ar/chatbox/chatbox.vue'
import { useRoute, useRouter } from 'vue-router'
import { useLang } from '~/composables/useLang'


const mobileMenuOpen = ref(false)
const fullscreenMenu = ref(null)
const menuContainer = ref(null)
const menuTitle = ref(null)
const closeButton = ref(null)
const previewBox = ref(null)
const previewIcon = ref(null)
const previewImage = ref(null)
const previewTitle = ref(null)
const previewDesc = ref(null)
const itemsWrapper = ref(null)
const menuItems = ref([])
const isMenuOpen = ref(false)
const hoveredItem = ref(null)
const productActive = ref(false)
const route = useRoute()
const router = useRouter()
const { switchLang } = useLang()
const langOpen = ref(false)
const langDropdownEn = ref(null)

// Flag to prevent duplicate menu openings
const isOpeningMenu = ref(false)

// Track previous route for comparison
const previousRoute = ref(null)

// بسته شدن dropdown وقتی بیرونش کلیک میشه
const closeDropdownOutside = (e) => {
  if (process.client && langDropdownEn.value && !langDropdownEn.value.contains(e.target)) {
    langOpen.value = false
  }
}

// handlers for wheel/touch to prevent background scrolling
const wheelHandler = (e) => {
  e.stopPropagation()
}
const touchHandler = (e) => {
  e.stopPropagation()
}

const useCases = [
  { 
    code: '', 
    title: 'ROTOCHEM 0955W', 
    slug: '0955W',
    description: 'مركب بلاستيكي أبيض اللون مخصص لتطبيقات القولبة الدورانية. يحتوي على كوبوليمر بولي إيثيلين خطي متوسط الكثافة بتوزيع ضيق للوزن الجزيئي وثاني أكسيد التيتانيوم TiO2. مثالي للمواد الموثوقة والمتينة التي تتحمل الظروف البيئية القاسية.',
    image: '/Product/Navbar/ROTOCHEM-0955W.webp',
    index: 0,
    offsetY: '15px',
    offsetTextY: '60px',
    offsetDescY: '130px'
  },
  { 
    code: '', 
    title: 'ROTOCHEM 0955B', 
    slug: '0955B',
    description: 'مركب بلاستيكي أزرق اللون مخصص لتطبيقات القولبة الدورانية. يحتوي على كوبوليمر بولي إيثيلين خطي متوسط الكثافة بتوزيع ضيق للوزن الجزيئي وثاني أكسيد التيتانيوم TiO2. ممتاز للتطبيقات الصناعية والاستهلاكية اللي تحتاج مواد ثابتة ومستقرة.',
    image: '/Product/Navbar/ROTOCHEM-0955B.webp',
    index: 1,
    offsetY: '12px',
    offsetTextY: '4px',
    offsetDescY: '12px'
  },
  { 
    code: '', 
    title: 'POLYFIL F700', 
    slug: 'POLYFIL-F700',
    description: 'مركب بولي إيثيلين عالي الأداء لتطبيقات أفلام نفخ HDPE. مصمم ليوفر خصائص ميكانيكية متفوقة وتجانس ممتاز للأفلام وقابلية معالجة موثوقة في تطبيقات الأفلام الرفيعة جداً (10-25 ميكرون). مناسب لأكياس التسوق والأكياس على شكل تيشيرت وأكياس القمامة والأفلام الملامسة للغذاء.',
    image: '/Product/Navbar/POLYFIL-F700.webp',
    index: 2,
    offsetY: '18px',
    offsetTextY: '6px',
    offsetDescY: '60px'
  },
  { 
    code: '', 
    title: 'POLYFILL 1300 EWA', 
    slug: 'POLYFIL-1300-EWA',
    description: 'ماستر باتش حشو على أساس بولي إيثيلين يحتوي على 82% كربونات كالسيوم (CaCO₃). يوفر تشتتاً ممتازاً في المنتج النهائي بفضل محتواه من CaCO₃ الدقيق جداً والمعالج. مصمم خصيصاً للإضافة المباشرة أثناء معالجة البولي أوليفين بما فيها البثق والحقن.',
    image: '/Product/index/1300.webp',
    index: 3,
    offsetY: '18px',
    offsetTextY: '6px',
    offsetDescY: '60px'
  },
  { 
    code: '', 
    title: 'HDCHEM 4760', 
    slug: 'HDCHEM-4760',
    description: 'مركب بلاستيكي مخصص لتطبيقات القولبة بالنفخ. مركب كوبوليمر بولي إيثيلين بخصائص متميزة تشمل انسيابية جيدة ومقاومة للصدمات وصلابة عالية ومقاومة ESCR. خيار موثوق للمواد الثابتة والمستقرة.',
    image: '/Product/Navbar/HDCHEM-4760.webp',
    index: 4,
    offsetY: '18px',
    offsetTextY: '6px',
    offsetDescY: '50px'    
  },
  { 
    code: '', 
    title: 'SlIPCHEM E 178', 
    slug: 'SlIPCHEM-E-178',
    description: 'ماستر باتش سليب عالي الأداء يحتوي على عامل سليب عالي الجودة في راتنج حامل من البولي إيثيلين. يقلل معامل الاحتكاك (COF) بين طبقات الأفلام البوليمرية أثناء لف الأفلام وإنتاج الأكياس والتعبئة. يوفر تشتتاً ممتازاً واستقراراً حرارياً عالياً وأداء هجرة ثابتاً.',
    image: '/Product/Navbar/SlIPCHEM-E178.webp',
    index: 5,
    offsetY: '18px',
    offsetTextY: '6px',
    offsetDescY: '50px' 
  },
  { 
    code: '', 
    title: 'RAFCOLOR 1560', 
    slug: 'RAFCOLOR-1560',
    description: 'ماستر باتش أبيض يحتوي على نسبة عالية من ثاني أكسيد التيتانيوم روتيل وراتنج بولي بروبيلين ثيرموبلاستيك. ماستر باتش أبيض عالي التركيز بتشتت ممتاز واستقرار حراري عالٍ. موصى به لتطبيقات الرافيا والأشرطة وخيوط CF/BCF وغيرها.',
    image: '/Product/Navbar/RAFCOLOR-1560.webp',
    index: 6,
    offsetDescY: '90px',
    offsetTextY: '50px',
    offsetY: '20px'
  },
  { 
    code: '', 
    title: 'CALCICHEM 126 FP', 
    slug: 'CALCICHEM-126-FP',
    description: 'ماستر باتش حشو على أساس بولي بروبيلين يحتوي على 80% كربونات كالسيوم (CaCO₃). يوفر تشتتاً ممتازاً بفضل محتواه من CaCO₃ الدقيق جداً والمعالج. مصمم للإضافة المباشرة أثناء معالجة البولي أوليفين بما فيها البثق والحقن.',
    image: '/Product/Navbar/CALCICHEM-126FP.webp',
    index: 7,
    offsetDescY: '50px',
    offsetTextY: '50px',
    offsetY: '20px'
  },
  { 
    code: '', 
    title: 'CALCICHEM 110 FRF', 
    slug: 'CALCICHEM-110-FRF',
    description: 'معدّل معدني يحتوي على نسبة عالية من CaCO₃ الدقيق جداً والمعالج. مصمم للأفلام والرافيا والحبال. مناسب للمنتجات العامة مع حاملات PE وPP. يرفع الكفاءة ويخفض تكاليف المواد الخام.',
    image: '/Product/Navbar/CALCICHEM-110FRF.webp',
    index: 8,
    offsetDescY: '50px',
    offsetTextY: '50px',
    offsetY: '20px'
  },
  { 
    code: '', 
    title: 'CALCICHEM 275 PM', 
    slug: 'CALCICHEM-275-PM',
    description: 'ماستر باتش معدني على أساس بولي بروبيلين يحتوي على 75% حشو معدني دقيق جداً. يعزز الأداء بتشتت ممتاز وتحميل معدني عالٍ. مُركَّب للإضافة المباشرة أثناء بثق أفلام BOPP وCPP وOPP.',
    image: '/Product/Navbar/CALCICHEM-275PM.webp',
    index: 9,
    offsetDescY: '70px',
    offsetTextY: '50px',
    offsetY: '20px'
  },
  { 
    code: '', 
    title: 'UVCHEM MB-R18', 
    slug: 'UVCHEM-MB-R18',
    description: 'ماستر باتش مثبت UV عالي الأداء للرافيا والأقمشة المنسوجة. يحتوي على مثبطات HALS وماصات UV؛ يوفر مقاومة طويلة الأمد ضد الأكسدة الضوئية وبهت اللون وفقدان الخصائص الميكانيكية. يوفر تشتتاً ممتازاً واستقراراً حرارياً وتوافقاً مع مصفوفة PP.',
    image: '/Product/Navbar/UVCHEM-MBR18.webp',
    index: 10,
    offsetY: '24px',
    offsetTextY: '8px',
    offsetDescY: '22px'
  },
]
const handleHover = (item, index) => {
  hoveredItem.value = item
  
  const tl = gsap.timeline()
  
  tl.to([previewTitle.value, previewDesc.value], {
    opacity: 0,
    y: -10,
    duration: 0.2
  })
  .set([previewTitle.value, previewDesc.value], {
    opacity: 0
  })
  .to([previewTitle.value, previewDesc.value], {
    opacity: 1,
    y: 0,
    duration: 0.4,
    stagger: 0.1
  })

  if (previewImage.value) {
    gsap.fromTo(previewImage.value, 
      { opacity: 0, scale: 0.85 }, 
      { opacity: 1, scale: 1, duration: 0.45, ease: 'back.out(1.2)' }
    )
  }
}

const handleLeave = () => {
}

// Helper function to check if path is a product page
const isProductPage = (path) => {
  if (!path) return false
  const normalizedPath = path.toLowerCase()
  return normalizedPath.includes('/ar/product') || 
         normalizedPath.includes('/ar/product_polychem') ||
         normalizedPath === '/ar/product'
}

// Check if currently on products index or product detail page
const isOnProductsSection = computed(() => {
  const currentPath = route.path.toLowerCase()
  return currentPath === '/ar/products' || isProductPage(currentPath)
})

const toggleFullscreenMenu = async () => {
  if (!fullscreenMenu.value) return
  
  if (isMenuOpen.value) {
    closeMenu()
    setTimeout(() => {
      isMenuOpen.value = false
      productActive.value = false
      mobileMenuOpen.value = false
    }, 800)
  } else {
    isMenuOpen.value = true
    mobileMenuOpen.value = false
    await nextTick()
    try { hoveredItem.value = useCases[0] } catch (e) {}
    productActive.value = true
    openMenu()
  }
}

const openMenu = () => {
  if (isOpeningMenu.value) return
  isOpeningMenu.value = true
  
  const menu = fullscreenMenu.value
  
  menu.style.pointerEvents = 'auto'
  
  // فقط در مرورگر body.style را تغییر بده
  if (process.client) {
    try { document.body.style.overflow = 'hidden' } catch (err) {}
  }
  
  const tl = gsap.timeline({
    onComplete: () => {
      isOpeningMenu.value = false
    }
  })
  
  tl.to(menuContainer.value, {
    y: 0,
    opacity: 1,
    duration: 0.8,
    ease: 'power3.out'
  })
  
  tl.to(menuTitle.value, {
    opacity: 1,
    y: 0,
    duration: 0.5,
    ease: 'power2.out'
  }, '-=0.5')
  
  tl.to(closeButton.value, {
    opacity: 1,
    duration: 0.3
  }, '-=0.3')
  
  tl.to(menuItems.value, {
    opacity: 1,
    y: 0,
    duration: 0.5,
    ease: 'power2.out',
    stagger: 0.04
  }, '-=0.5')
  
  tl.to(previewBox.value, {
    opacity: 1,
    duration: 0.6
  }, '-=0.8')
  
  if (previewImage.value) {
    tl.to(previewImage.value, {
      scale: 1,
      opacity: 1,
      duration: 0.6,
      ease: 'back.out(1.7)'
    }, '-=0.4')
  } else {
    tl.to(previewIcon.value, {
      scale: 1,
      duration: 0.6,
      ease: 'back.out(1.7)'
    }, '-=0.4')
  }
  
  tl.to([previewTitle.value, previewDesc.value], {
    opacity: 1,
    y: 0,
    duration: 0.5,
    stagger: 0.1
  }, '-=0.3')
}

const closeMenu = () => {
  const menu = fullscreenMenu.value
  
  const tl = gsap.timeline()
  
  tl.to(menuItems.value, {
    opacity: 0,
    y: -20,
    duration: 0.3,
    ease: 'power2.in',
    stagger: 0.02
  })
  
  tl.to(menuTitle.value, {
    opacity: 0,
    y: -20,
    duration: 0.3
  }, '-=0.2')
  
  tl.to([previewTitle.value, previewDesc.value, previewIcon.value, previewImage.value], {
    opacity: 0,
    scale: 0.9,
    duration: 0.3
  }, '-=0.3')
  
  tl.to(closeButton.value, {
    opacity: 0,
    duration: 0.2
  }, '-=0.2')
  
  tl.to(menuContainer.value, {
    y: '-100%',
    opacity: 0,
    duration: 0.6,
    ease: 'power3.in'
  }, '-=0.2')
  
  tl.to(previewBox.value, {
    opacity: 0,
    duration: 0.3,
    onComplete: () => {
      menu.style.pointerEvents = 'none'
      hoveredItem.value = null
      productActive.value = false
      
      // فقط در مرورگر body.style را تغییر بده
      if (process.client) {
        try { document.body.style.overflow = '' } catch (err) {}
      }
      
      // پاک کردن event listeners با بررسی
      if (process.client && itemsWrapper.value) {
        try {
          itemsWrapper.value.removeEventListener('wheel', wheelHandler)
          itemsWrapper.value.removeEventListener('touchmove', touchHandler)
        } catch (err) {
          console.error('Error removing event listeners:', err)
        }
      }
    }
  }, '-=0.4')
}

// Function to handle return from product page and open menu
const handleReturnFromProduct = async () => {
  // Activate button
  productActive.value = true
  
  // Check if we're on a main page
  const currentPath = route.path
  const isMainPage = ['/', '/ar', '/ar/aboutus', '/ar/news', '/ar/careers', '/ar/contact'].includes(currentPath)
  
  if (isMainPage && !isMenuOpen.value && !isOpeningMenu.value) {
    await nextTick()
    isMenuOpen.value = true
    await nextTick()
    try { hoveredItem.value = useCases[0] } catch (e) {}
    openMenu()
  }
}

onMounted(async () => {
  // فقط کدهای مربوط به DOM در onMounted اجرا شود
  if (!process.client) return
  
  await nextTick()
  
  // Initialize previous route
  previousRoute.value = { path: route.path, query: route.query }
  
  // اضافه کردن event listener برای dropdown
  window.addEventListener('click', closeDropdownOutside)
  
  if (menuItems.value && menuItems.value.length > 0) {
    gsap.set(menuItems.value, { y: -30, opacity: 0 })
  }
  if (menuTitle.value) {
    gsap.set(menuTitle.value, { y: -20, opacity: 0 })
  }
  if (previewTitle.value && previewDesc.value) {
    gsap.set([previewTitle.value, previewDesc.value], { y: 4, opacity: 0 })
  }
  if (previewIcon.value) {
    gsap.set(previewIcon.value, { scale: 0 })
  }
  if (previewImage.value) {
    gsap.set(previewImage.value, { scale: 0.85, opacity: 0 })
  }

  if (itemsWrapper.value) {
    itemsWrapper.value.style.overscrollBehavior = 'contain'
    itemsWrapper.value.style.touchAction = 'auto'
    itemsWrapper.value.addEventListener('wheel', wheelHandler, { passive: false })
    itemsWrapper.value.addEventListener('touchmove', touchHandler, { passive: false })
  }

  // Escape key handler
  const handleEscape = (e) => {
    if (e.key === 'Escape' && isMenuOpen.value) {
      toggleFullscreenMenu()
    }
  }
  
  window.addEventListener('keydown', handleEscape)
  
  // Store cleanup function
  onUnmounted(() => {
    window.removeEventListener('keydown', handleEscape)
  })
})

// Watch for route changes
watch(() => route.fullPath, async (newFullPath, oldFullPath) => {
  // Get current and previous paths (without query)
  const newPath = route.path
  const oldPath = previousRoute.value?.path
  
  // Update previous route
  previousRoute.value = { path: route.path, query: route.query }
  
  // Only proceed if we have both paths
  if (!oldPath || !newPath) return
  
  // Close menu when navigating between pages
  if (isMenuOpen.value && oldPath !== newPath) {
    closeMenu()
    setTimeout(() => {
      isMenuOpen.value = false
      productActive.value = false
    }, 400)
  }
  
  // Check if we're coming FROM a product page TO a main page
  const comingFromProduct = isProductPage(oldPath)
  const goingToMainPage = ['/', '/ar', '/ar/aboutus', '/ar/news', '/ar/careers', '/ar/contact'].includes(newPath)
  
  // Only open menu in this specific case
  if (comingFromProduct && goingToMainPage) {
    // Wait a bit to ensure DOM is ready
    await nextTick()
    setTimeout(() => {
      handleReturnFromProduct()
    }, 150)
  }
}, { immediate: false })

// Navigate programmatically to product page with query then close menu
const handleMenuItemClick = async (item) => {
  if (!item) return

  if (isMenuOpen.value) closeMenu()
  isMenuOpen.value = false
  productActive.value = false
  mobileMenuOpen.value = false
  if (fullscreenMenu.value) fullscreenMenu.value.style.pointerEvents = 'none'
  if (process.client) document.body.style.overflow = ''
  
  try {
    const productPath = item.slug ? `/ar/products/${item.slug}` : `/ar/products`
    if (process.client) {
      window.location.assign(productPath)
      return
    }
    await router.push(productPath)
  } catch (err) {
    console.error('Navigation error:', err)
  }
}

onUnmounted(() => {
  // فقط در مرورگر cleanup انجام بده
  if (!process.client) return
  
  try { 
    document.body.style.overflow = '' 
  } catch (err) {}
  
  // بستن menu‌ها
  isMenuOpen.value = false
  mobileMenuOpen.value = false
  
  // پاک کردن event listeners با بررسی امن
  if (itemsWrapper.value) {
    try {
      itemsWrapper.value.removeEventListener('wheel', wheelHandler)
      itemsWrapper.value.removeEventListener('touchmove', touchHandler)
    } catch (err) {
      console.error('Error removing event listeners:', err)
    }
  }
  
  // پاک کردن dropdown listener
  try {
    window.removeEventListener('click', closeDropdownOutside)
  } catch (err) {
    console.error('Error removing dropdown listener:', err)
  }
})

const previewImageStyle = computed(() => {
  const y = hoveredItem.value?.offsetY ?? '0px'
  return {
    position: 'relative',
    top: y,
    transition: 'top 220ms ease'
  }
})

const previewTitleStyle = computed(() => {
  const y = hoveredItem.value?.offsetTextY ?? '0px'
  return {
    position: 'relative',
    top: y,
    transition: 'top 220ms ease'
  }
})

const previewDescStyle = computed(() => {
  const y = hoveredItem.value?.offsetDescY ?? '0px'
  return {
    position: 'relative',
    top: y,
    transition: 'top 220ms ease'
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

/* RTL Direction for Arabic */
nav {
  direction: rtl;
}

.nav-link,
.nav-link-mobile {
  font-family: "Tajawal", system-ui, -apple-system, sans-serif;
}

/* Button 2 Hover Effect - Desktop */
.nav-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  height: 100%;
  z-index: 0;
  background-color: #000;
  transform: scaleY(0.3);
  opacity: 0;
  transition: all 0.3s ease;
}

.nav-link:hover::before {
  opacity: 1;
  background-color: rgb(187, 187, 187);
  transform: scaleY(1);
  transition: transform 0.6s cubic-bezier(0.08, 0.35, 0.13, 1.02), opacity 0.4s;
}

.nav-link:hover {
  color: #ffffff !important;
}

.nav-link:hover span {
  color: #ffffff !important;
}

/* Mobile Menu Links Hover Effect */
.nav-link-mobile::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  height: 100%;
  z-index: 0;
  background-color: #000;
  transform: scaleY(0.3);
  opacity: 0;
  transition: all 0.3s ease;
}

.nav-link-mobile:hover::before {
  opacity: 1;
  background-color: #ffcd05;
  transform: scaleY(1);
  transition: transform 0.6s cubic-bezier(0.08, 0.35, 0.13, 1.02), opacity 0.4s;
}

.nav-link-mobile:hover {
  color: #030303 !important;
}

.nav-link-mobile:hover span {
  color: #000000 !important;
}

/* Active state matches hover appearance */
.nav-link.active::before {
  opacity: 1;
  background-color: #ffffff;
  transform: scaleY(1);
}
.nav-link.active,
.nav-link.active span {
  color: #000000 !important;
}

.nav-link-mobile.active::before {
  opacity: 1;
  background-color: #ffffff;
  transform: scaleY(1);
}
.nav-link-mobile.active,
.nav-link-mobile.active span {
  color: #030303 !important;
}

/* Nuxt router active states (desktop) */
.router-link-active.nav-link::before,
.router-link-exact-active.nav-link::before {
  opacity: 1;
  background-color: #ffffff;
  transform: scaleY(1);
}
.router-link-active.nav-link,
.router-link-active.nav-link span,
.router-link-exact-active.nav-link,
.router-link-exact-active.nav-link span {
  color: #000000 !important;
}

/* Nuxt router active states (mobile) */
.router-link-active.nav-link-mobile::before,
.router-link-exact-active.nav-link-mobile::before {
  opacity: 1;
  background-color: #ffcd05;
  transform: scaleY(1);
}
.router-link-active.nav-link-mobile,
.router-link-active.nav-link-mobile span,
.router-link-exact-active.nav-link-mobile,
.router-link-exact-active.nav-link-mobile span {
  color: #030303 !important;
}

/* Mobile Menu Animation */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: all 0.3s ease;
}

.mobile-menu-enter-from {
  opacity: 0;
  max-height: 0;
}

.mobile-menu-leave-to {
  opacity: 0;
  max-height: 0;
}

/* Menu Item Hover Effect */
.menu-item {
  transform: translateZ(0);
  backface-visibility: hidden;
}

/* Ensure menu item text is always visible - override any opacity issues */
.menu-item {
  color: #1f2937 !important;
}

.menu-item-content {
  opacity: 1 !important;
  position: relative;
  z-index: 10;
  isolation: isolate;
}

.menu-item {
  isolation: isolate;
  will-change: opacity, transform;
}

.menu-item h3 {
  color: #1f2937 !important;
  position: relative;
  z-index: 10;
  opacity: 1 !important;
}

.menu-item span {
  color: #6b7280 !important;
  position: relative;
  z-index: 10;
  opacity: 1 !important;
}

.menu-item svg {
  color: #9ca3af !important;
  position: relative;
  z-index: 10;
  opacity: 1 !important;
}

/* Custom Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(234, 179, 8, 0.5);
}

.nav-link,
.nav-link-mobile {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  white-space: nowrap;
  padding-top: 0;
  padding-bottom: 0;
}

.nav-link > span,
.nav-link-mobile > span {
  display: inline-flex;
  align-items: center;
  height: 100%;
}

nav .flex.items-center.h-20 > * {
  min-height: 80px;
  display: flex;
  align-items: center;
}

.nav-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 80px;
  box-sizing: border-box;
  padding-top: 0;
  padding-bottom: 0;
  white-space: nowrap;
}

.nav-link > span {
  display: inline-flex;
  align-items: center;
  height: 100%;
}

.nav-link svg {
  display: inline-block;
  vertical-align: middle;
  margin-right: 6px;
  margin-left: 0;
}

.hidden.md\:flex.items-center.h-full > .nav-link,
.hidden.md\:flex.items-center.h-full .nav-link {
  height: 100%;
}

.flex.items-center.h-20 > * {
  height: 100%;
  display: flex;
  align-items: center;
}

.nav-link-mobile {
  min-height: 44px;
}

@media (min-width: 768px) {
  .hide-desktop {
    display: none !important;
  }
}

.navbar-container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
}

.navbar-inner {
  --navbar-shift: 0;
  transform: translateX(var(--navbar-shift));
  transition: transform 0.18s ease;
}

@media (max-width: 767px) {
  .navbar-container {
    max-width: 100%;
    padding: 0 16px;
  }
  .navbar-inner {
    transform: none !important;
  }
}

@media (max-width: 767px) {
  .nav-link-mobile {
    min-height: 48px !important;
    padding: 12px 6px !important;
  }

  .menu-item {
    min-height: 48px !important;
    padding: 16px !important;
  }

  .menu-item h3 {
    font-size: 16px !important;
  }

  .menu-item span {
    font-size: 12px !important;
  }

  .navbar-container {
    max-width: 100% !important;
    min-width: auto !important;
    padding: 0 !important;
  }

  .navbar-inner {
    transform: none !important;
  }

  .navbar-inner img {
    width: 160px !important;
    height: 96px !important;
  }
}

@media (min-width: 768px) {
  .navbar-container {
    max-width: 1280px;
    min-width: 1280px;
  }

  .navbar-inner {
    --navbar-shift: -32px;
    transform: translateX(var(--navbar-shift));
  }
}

@font-face {
  font-family: 'IRANYekan';
  src: url('/fonts/Qs_Iranyekan.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'IRANYekan';
  src: url('/fonts/Qs_Iranyekan_bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}

/* RTL Text Alignment */
.menu-item h3,
.menu-item span,
.nav-link span,
.nav-link-mobile span {
  text-align: right;
}

/* RTL Menu Items */
.menu-item {
  text-align: right;
}

/* RTL Dropdown */
.absolute.top-full {
  right: 0 !important;
  left: auto !important;
}
</style>