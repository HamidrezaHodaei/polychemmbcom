<!-- components/fa/layout/navbar.vue -->
<template>
  <div>
    <nav class="hidden lg:block bg-[#808285] fixed top-0 inset-x-0 z-50 lg:border-b">
      <div class="navbar-inner navbar-container">
        <div class="flex items-center h-16 lg:h-20">

          <!-- Right Side (زبان + ورود) -->
          <div class="hidden lg:flex items-center justify-end h-full w-auto flex-shrink-0">
            <!-- دکمه زبان با dropdown -->
            <div class="relative h-full flex items-center border-l border-r border-white px-2" ref="langDropdownFa">
              <button
                @click="langOpen = !langOpen"
                class="nav-link text-[13px] font-medium px-6 h-full text-white relative overflow-hidden"
              >
                <span class="relative z-10 font-[Montserrat] text-[14.5px]">FA</span>
              </button>
              <!-- Dropdown -->
              <div
                v-show="langOpen"
                class="absolute top-full right-0 mt-1 w-36 bg-white rounded-lg shadow-lg z-[100] overflow-hidden border border-gray-100"
              >
                <!-- فارسی (فعال) -->
                <button
                  class="w-full px-4 py-3 text-sm text-yellow-600 bg-yellow-50 flex items-center justify-between cursor-default"
                >
                  <span class="text-xs text-yellow-400">FA</span>
                  <span style="font-family: IRANYekan, sans-serif;">فارسی</span>
                </button>
                <!-- عربی -->
                <button
                  @click="() => { switchLang('ar'); langOpen = false }"
                  class="w-full px-4 py-3 text-sm text-gray-700 hover:bg-yellow-50 hover:text-yellow-600 transition-colors flex items-center justify-between"
                >
                  <span class="text-xs text-gray-400">AR</span>
                  <span style="font-family: 'Tajawal', system-ui, -apple-system, sans-serif;">العربية</span>
                </button>
                <!-- انگلیسی -->
                <button
                  @click="() => { switchLang('en'); langOpen = false }"
                  class="w-full px-4 py-3 text-sm text-gray-700 hover:bg-yellow-50 hover:text-yellow-600 transition-colors flex items-center justify-between"
                >
                  <span class="text-xs text-gray-400">EN</span>
                  <span>English</span>
                </button>
                <!-- ترکی -->
                <button
                  @click="() => { switchLang('tr'); langOpen = false }"
                  class="w-full px-4 py-3 text-sm text-gray-700 hover:bg-yellow-50 hover:text-yellow-600 transition-colors flex items-center justify-between"
                >
                  <span class="text-xs text-gray-400">TR</span>
                  <span>Türkçe</span>
                </button>
              </div>
            </div>

            <NuxtLink to="/clientarea/login" class="nav-link text-[13px] font-medium px-6 h-full text-white relative overflow-hidden border-l border-r border-white flex items-center justify-center">
              <span class="relative z-10 font-[IRANYekan] font-bold text-[14.5px]">ورود مشتریان </span>
            </NuxtLink>
          </div>

          <!-- Main Menu -->
          <div class="hidden lg:flex items-center flex-1 justify-center h-full">
            <NuxtLink
              to="/fa/contact"
              class="nav-link text-[13px] font-medium px-8 text-white relative overflow-hidden h-full flex items-center w-40"
            >
              <span class="relative z-10 font-[IRANYekan] font-bold text-[14.5px]">ارتباط با ما</span>
            </NuxtLink>

            <NuxtLink
              to="/fa/careers"
              class="nav-link text-[13px] font-medium px-8 text-white relative overflow-hidden h-full flex items-center"
            >
              <span class="relative z-10 font-[IRANYekan] font-bold text-[14.5px]">فرصت‌های همکاری</span>
            </NuxtLink>

            <NuxtLink
              to="/fa/news"
              class="nav-link text-[13px] font-medium px-8 text-white relative overflow-hidden h-full flex items-center"
            >
              <span class="relative z-10 font-[IRANYekan] font-bold text-[14.5px]">اخبار</span>
            </NuxtLink>

            <NuxtLink
              to="/fa/aboutus"
              class="nav-link flex items-center justify-center gap-2 text-[13px] font-medium px-8 text-white relative overflow-hidden h-full w-40"
            >
              <span class="relative z-10 font-[IRANYekan] font-bold text-[14.5px]">درباره ما</span>
            </NuxtLink>

            <NuxtLink
              to="/fa"
              class="nav-link text-[13px] font-medium px-8 text-white relative overflow-hidden h-full flex items-center"
            >
              <span class="relative z-10 font-[IRANYekan] font-bold text-[14.5px]">صفحه نخست</span>
            </NuxtLink>
          </div>

          <!-- PRODUCTS button desktop -->
          <div class="hidden lg:flex items-center h-full lg:border-r lg:border-white">
            <button
              @click="toggleFullscreenMenu"
              class="nav-link flex items-center gap-2 text-[13px] text-white font-medium px-8 h-full relative overflow-hidden"
              :class="{ active: isProductsRoute }"
            >
              <svg class="w-4 h-4 relative z-10" fill="currentColor" viewBox="0 0 20 20">
                <path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/>
              </svg>
              <span class="relative z-10 font-[IRANYekan] font-bold text-[14.5px]">محصولات ما</span>
            </button>
          </div>

          <!-- Logo -->
          <div class="flex items-center justify-start lg:border-r lg:border-l lg:border-white pl-2 lg:pl-8 pr-2 lg:pr-8 h-full flex-shrink-0 w-auto lg:w-[230px]">
            <NuxtLink to="/fa" aria-label="Go to home" class="block">
              <img src="/layout/logo/english logo W1.png" alt="POLYCHEM Logo" class="w-28 lg:w-40 h-28 lg:h-40 object-contain" />
            </NuxtLink>
          </div>

          <!-- Mobile PRODUCTS Button -->
          <button
            @click="toggleMobileMenu"
            class="lg:hidden ml-auto text-white hover:text-yellow-400 px-4 py-3 rounded-lg hover:bg-black/20 transition-all duration-200 flex items-center gap-2"
            aria-label="Open mobile menu"
          >
            <!-- hamburger icon -->
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
          </button>
        </div>

        <!-- Mobile Menu -->
        <transition name="mobile-menu">
          <div v-if="mobileMenuOpen" class="lg:hidden pb-4 bg-[#808285] max-h-[calc(100vh-64px)] overflow-y-auto">
            <div class="flex flex-col gap-2 pt-4 px-4">
              <button
                @click="toggleFullscreenMenu"
                class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden text-right w-full"
                :class="{ active: isProductsRoute }"
              >
                <span class="relative z-10 font-[IRANYekan]">محصولات ما</span>
              </button>

              <NuxtLink to="/fa" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10 font-[IRANYekan]">صفحه نخست</span>
              </NuxtLink>

              <NuxtLink to="/fa/aboutus" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10 font-[IRANYekan]">درباره ما</span>
              </NuxtLink>

              <NuxtLink to="/fa/news" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10 font-[IRANYekan]">اخبار</span>
              </NuxtLink>

              <NuxtLink to="/fa/careers" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10 font-[IRANYekan]">فرصت‌های همکاری</span>
              </NuxtLink>

              <NuxtLink to="/fa/contact" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded relative overflow-hidden w-full block">
                <span class="relative z-10 font-[IRANYekan]">ارتباط با ما</span>
              </NuxtLink>

              <div class="pt-3 mt-2 border-t border-white/20">
                <!-- دکمه زبان موبایل -->
                <div class="relative mb-2">
                  <button
                    @click="mobileLangOpen = !mobileLangOpen"
                    class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded block w-full text-right relative overflow-hidden"
                  >
                    <span class="relative z-10 font-[Montserrat]">FA</span>
                  </button>
                  <!-- Mobile Lang Dropdown -->
                  <div v-show="mobileLangOpen" class="mt-1 bg-white rounded-lg shadow-lg overflow-hidden">
                    <button
                      class="w-full px-4 py-3 text-sm text-yellow-600 bg-yellow-50 flex items-center justify-end gap-2 cursor-default"
                    >
                      <span style="font-family: IRANYekan, sans-serif;">فارسی</span>
                      <span class="text-xs text-yellow-400">FA</span>
                    </button>
                    <button
                      @click="() => { switchLang('en'); mobileLangOpen = false; mobileMenuOpen = false }"
                      class="w-full px-4 py-3 text-sm text-gray-700 hover:bg-yellow-50 flex items-center justify-end gap-2"
                    >
                      <span>English</span>
                      <span class="text-xs text-gray-400">EN</span>
                    </button>
                  </div>
                </div>

                <NuxtLink to="/fa/login" class="nav-link-mobile text-[13px] font-medium text-white hover:text-gray-200 py-3 px-4 rounded block w-full text-right relative overflow-hidden">
                  <span class="relative z-10 font-[IRANYekan]">ورود مشتریان</span>
                </NuxtLink>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </nav>

    <!-- Mobile Top Navbar -->
    <NavbarMobTop class="block lg:hidden" />

    <!-- Spacer -->
    <div class="hidden lg:block h-16 lg:h-20"></div>

    <!-- Mobile bottom navbar -->
    <NavbarMob class="block lg:hidden" />

    <!-- Chatbox -->
    <Chatbox v-if="route.path === '/fa' || route.path === '/fa/aboutus'" />

    <!-- Fullscreen Product Menu -->
    <div
      v-show="isMenuOpen"
      ref="fullscreenMenu"
      class="fixed inset-0 z-40 overflow-hidden"
    >
      <div class="h-full flex flex-col md:flex-row">
        <!-- Left Side - Preview (hidden mobile) -->
        <div class="hidden md:flex w-[40%] bg-gradient-to-br from-gray-50 to-white relative overflow-hidden">
          <div
            ref="previewBox"
            class="absolute inset-0 flex items-center justify-center p-20 opacity-0"
          >
            <div class="text-center space-y-6">
              <img
                ref="previewImage"
                :src="hoveredItem?.image || '/Roto.webp'"
                alt="preview"
                class="w-1500 h-1500 object-cover transform scale-0"
                :style="previewImageStyle"
              />
              <div class="inline-block bg-white/70 backdrop-blur-sm rounded-2xl px-8 py-6 max-w-[90%]">
                <div
                  ref="previewTitle"
                  class="opacity-0 transform translate-y-4"
                  :style="previewTitleStyle"
                >
                  <h3 class="text-3xl md:text-4xl font-bold text-[#848484] mb-3">{{ hoveredItem?.title || 'ROTOCHEM 0955W' }}</h3>
                  <p class="text-xl text-gray-600">{{ hoveredItem?.code || '' }}</p>
                </div>
                <p
                  ref="previewDesc"
                  class="text-gray-700 text-lg max-w-md mx-auto opacity-0 transform translate-y-4 mt-3 font-[IRANYekan] text-right leading-[32px]"
                  dir="rtl"
                  :style="previewDescStyle"
                >
                  {{ hoveredItem?.description || 'یک آمیزه پلیمری تخصصی سفید رنگ است که برای کاربرد قالب‌گیری دورانی طراحی شده است.' }}
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

        <!-- Right Side - Menu Items -->
        <div class="w-full md:w-[60%] bg-white relative flex flex-col h-full">
          <div
            ref="menuContainer"
            class="h-full flex flex-col justify-start md:justify-center px-6 md:px-16 py-6 md:py-0 opacity-0 transform translate-y-[-100%] overflow-y-auto md:overflow-y-visible"
          >
            <!-- Close Button -->
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
              <h2 class="text-2xl md:text-4xl font-[IRANYekan] text-[#848484] mb-2 text-right">محصولات ما</h2>
              <div class="w-20 h-1 bg-[#ffd000] ml-auto"></div>
            </div>

            <!-- Menu Items -->
            <div ref="itemsWrapper" class="space-y-1 max-h-[calc(100vh-200px)] md:max-h-[70vh] overflow-y-auto pr-4 custom-scrollbar pb-6 md:pb-0">
              <button
                v-for="(item, index) in useCases"
                :key="index"
                :ref="el => { if (el) menuItems[index] = el }"
                @mouseenter="handleHover(item, index)"
                @mouseleave="handleLeave"
                @click="() => handleMenuItemClick(item)"
                type="button"
                class="menu-item group flex items-center justify-between border-b border-gray-200 py-4 md:py-6 px-4 md:px-6 hover:bg-gray-50 transition-all duration-300 transform translate-y-[-30px] active:bg-gray-100 md:active:bg-transparent"
                style="opacity: 1 !important; min-height: 48px; width: 100%; text-align: right;"
              >
                <!-- Arrow left side (RTL) -->
                <svg class="w-5 h-5 md:w-6 md:h-6 text-gray-400 group-hover:text-yellow-500 group-hover:translate-x-[-2] transition-all flex-shrink-0 mr-2 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                </svg>

                <div class="flex items-center gap-3 md:gap-6 menu-item-content flex-1 min-w-0 justify-end" style="opacity: 1 !important; color: #1f2937 !important;">
                  <h3 style="color: #1f2937 !important; opacity: 1 !important;" class="text-lg md:text-xl font-semibold group-hover:translate-x-[-2] transition-transform truncate text-[#848484] font-[IRANYekan]">{{ item.title }}</h3>
                  <span style="color: #6b7280 !important; opacity: 1 !important;" class="text-[11px] md:text-[13px] group-hover:text-yellow-500 transition-colors flex-shrink-0">{{ item.code }}</span>
                </div>
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
import Chatbox from '~/components/fa/chatbox/chatbox.vue'
import { useRoute, useRouter } from 'vue-router'
import { useLang } from '~/composables/useLang'

// ─── زبان ───
const { switchLang } = useLang()
const langOpen = ref(false)
const mobileLangOpen = ref(false)
const langDropdownFa = ref(null)

// ─── رفرنس‌های DOM ───
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
const route = useRoute()
const router = useRouter()
const previousRoute = ref(null)
const isOpeningMenu = ref(false)

const isProductsRoute = computed(() => {
  const path = (route.path || '').toLowerCase()
  return path.includes('/fa/products') || path.includes('/fa/product') || path === '/fa/product'
})

// ─── موبایل مدیریت ───
const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

// ─── scroll block ───
const wheelHandler = (e) => { e.stopPropagation() }
const touchHandler = (e) => { e.stopPropagation() }

// ─── محصولات داده ───
const useCases = [
  {
    code: '',
    title: 'ROTOCHEM 0955W',
    description: 'یک آمیزه پلیمری تخصصی سفید رنگ است که برای کاربرد قالب‌گیری دورانی طراحی شده است. این محصول ترکیبی از گرید کوپلیمر پلی‌اتیلن با چگالی متوسط با توزیع وزن مولکولی باریک و دی‌اکسید تیتانیوم می‌باشد.',
    image: '/Product/Navbar/ROTOCHEM-0955W.webp',
    index: 0,
    offsetY: '14.5px',
    offsetTextY: '60px',
    offsetDescY: '130px'
  },
  {
    code: '',
    title: 'ROTOCHEM 0955B',
    description: 'یک آمیزه پلیمری تخصصی آبی رنگ است که برای کاربرد قالب‌گیری دورانی طراحی شده است. این محصول ترکیبی از گرید کوپلیمر پلی‌اتیلن با چگالی متوسط خطی با توزیع وزن مولکولی باریک و رنگدانه آبی می‌باشد.',
    image: '/Product/Navbar/ROTOCHEM-0955B.webp',
    index: 1,
    offsetY: '12px',
    offsetTextY: '4px',
    offsetDescY: '12px'
  },
  {
    code: '',
    title: 'POLYFIL F700',
    description: 'یک کامپاند پلی‌اتیلن است که به‌طور ویژه برای کاربردهای فیلم دمشی پلی‌اتیلن سنگین فرموله شده است. این گرید به‌گونه‌ای طراحی شده که خواص مکانیکی مطلوب، یکنواختی عالی فیلم و فرآیندپذیری مناسب را حتی در تولید فیلم‌های بسیار نازک فراهم می‌کند.',
    image: '/Product/Navbar/POLYFIL-F700.webp',
    index: 2,
    offsetY: '18px',
    offsetTextY: '6px',
    offsetDescY: '40px'
  },
    {
    code: '',
    title: 'POLYFIL 1300 EWA',
    description: 'POLYFILL 1300 EWA برای فرمولاسیون‌های پایه پلی‌اتیلن طراحی شده و در تولید انواع فیلم و بسته‌بندی قابل استفاده است.',
    image: '/Product/index/1300.webp',
    index: 3,
    offsetY: '18px',
    offsetTextY: '6px',
    offsetDescY: '40px'
  },
  {
    code: '',
    title: 'HDCHEM 4760',
    description: 'کامپاند پلاستیکی تخصصی است که برای کاربردهای قالب‌گیری بادی طراحی شده است. این محصول ترکیبی از کوپلیمرهای پلی‌اتیلنی بوده و دارای مجموعه‌ای از ویژگی‌های مطلوب و کاربردی است.',
    image: '/Product/Navbar/HDCHEM-4760.webp',
    index: 4,
    offsetY: '18px',
    offsetTextY: '6px',
    offsetDescY: '50px'
  },
  {
    code: '',
    title: 'SlIPCHEM E 178',
    description: 'مستربچ لیزکننده با عملکرد بالا است که حاوی عامل لغزنده با کیفیت بالا است که در رزین حامل پلی‌اتیلن پراکنده شده است. این محصول به طور خاص برای کاهش ضریب اصطکاک بین لایه‌های فیلم پلیمری در حین فرآیندهای رول پیچی، ساخت کیسه و بسته‌بندی توسعه یافته است.',
    image: '/Product/Navbar/SlIPCHEM-E178.webp',
    index: 5,
    offsetY: '18px',
    offsetTextY: '6px',
    offsetDescY: '50px'
  },
  {
    code: '',
    title: 'RAFCOLOR 1560',
    description: 'یک مستربچ سفید بر پایه پلی پروپلین و درصد بالائی از تیتانیوم دی اکساید می‌باشد. در تولید این محصول از دی اکسید تیتانیوم مرغوب و مخصوص تولید محصولات پلاستیکی استفاده شده است.',
    image: '/Product/Navbar/RAFCOLOR-1560.webp',
    index: 6,
    offsetDescY: '90px',
    offsetTextY: '50px',
    offsetY: '20px'
  },
  {
    code: '',
    title: 'CALCICHEM 126 FP',
    description: 'مستربچ پرکننده بر پایه پلی‌پروپیلن حاوی 80% کربنات کلسیم (CaCO₃) است. دارای محتوای بالا، بسیار ریز و تیمار شده CaCO₃ بوده که پراکنش عالی را تضمین می‌کند.',
    image: '/Product/Navbar/CALCICHEM-126FP.webp',
    index: 7,
    offsetDescY: '50px',
    offsetTextY: '50px',
    offsetY: '20px'
  },
  {
    code: '',
    title: 'CALCICHEM 110 FRF',
    description: 'یک مستربچ پرکننده است که حاوی کربنات کلسیم با اندازه ذرات بسیار ریز و پوشش دار شده می‌باشد. این مستربچ از پراکنش عالی در محصول نهایی برخوردار است.',
    image: '/Product/Navbar/CALCICHEM-110FRF.webp',
    index: 8,
    offsetDescY: '50px',
    offsetTextY: '50px',
    offsetY: '20px'
  },
  {
    code: '',
    title: 'CALCICHEM 275 PM',
    description: 'یک مستربچ پرکننده بر پایه پلی‌پروپیلن است که پراکنش و پراکندگی عالی را در محصول نهایی تضمین می‌کند. این مستربچ به‌طور ویژه برای استفاده مستقیم در فرایند اکستروژن فیلم‌های BOPP، CPP و OPP طراحی شده.',
    image: '/Product/Navbar/CALCICHEM-275PM.webp',
    index: 9,
    offsetDescY: '70px',
    offsetTextY: '50px',
    offsetY: '20px'
  },
  {
    code: '',
    title: 'UVCHEM MB-R18',
    description: 'یک مستربچ پایدارکننده اشعه فرابنفش (UV) با عملکرد بالا است که برای استفاده در رافیا و پارچه‌های بافته شده طراحی شده است. شامل ترکیبی هم‌افزا از پایدارکننده‌های نوری آمینی (HALS) و جاذب‌های اشعه فرابنفش (UV) است.',
    image: '/Product/Navbar/UVCHEM-MBR18.webp',
    index: 10,
    offsetY: '24px',
    offsetTextY: '8px',
    offsetDescY: '22px'
  }
]

// ─── hover ───
const handleHover = (item, index) => {
  hoveredItem.value = item

  const tl = gsap.timeline()
  tl.to([previewTitle.value, previewDesc.value], {
    opacity: 0, y: -10, duration: 0.2
  })
  .set([previewTitle.value, previewDesc.value], { opacity: 0 })
  .to([previewTitle.value, previewDesc.value], {
    opacity: 1, y: 0, duration: 0.4, stagger: 0.1
  })

  if (previewImage.value) {
    gsap.fromTo(previewImage.value,
      { opacity: 0, scale: 0.85 },
      { opacity: 1, scale: 1, duration: 0.45, ease: 'back.out(1.2)' }
    )
  }
}

const handleLeave = () => {}

// ─── product page check ───
const isProductPage = (path) => {
  if (!path) return false
  const n = path.toLowerCase()
  return n.includes('/fa/products') || n.includes('/fa/product') || n === '/fa/product'
}

// ─── fullscreen menu ───
const toggleFullscreenMenu = async () => {
  if (!fullscreenMenu.value) return

  if (isMenuOpen.value) {
    closeMenu()
    setTimeout(() => {
      isMenuOpen.value = false
    }, 800)
  } else {
    isMenuOpen.value = true
    await nextTick()
    try { hoveredItem.value = useCases[0] } catch (e) {}
    openMenu()
  }
}

const openMenu = () => {
  if (isOpeningMenu.value) return
  isOpeningMenu.value = true

  const menu = fullscreenMenu.value
  menu.style.pointerEvents = 'auto'
  try { document.body.style.overflow = 'hidden' } catch (err) {}

  const tl = gsap.timeline({
    onComplete: () => { isOpeningMenu.value = false }
  })

  tl.to(menuContainer.value, { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' })
  tl.to(menuTitle.value, { opacity: 1, y: 0, duration: 0.5, ease: 'power2.out' }, '-=0.5')
  tl.to(closeButton.value, { opacity: 1, duration: 0.3 }, '-=0.3')
  tl.to(menuItems.value, { opacity: 1, y: 0, duration: 0.5, ease: 'power2.out', stagger: 0.04 }, '-=0.5')
  tl.to(previewBox.value, { opacity: 1, duration: 0.6 }, '-=0.8')

  if (previewImage.value) {
    tl.to(previewImage.value, { scale: 1, opacity: 1, duration: 0.6, ease: 'back.out(1.7)' }, '-=0.4')
  }

  tl.to([previewTitle.value, previewDesc.value], { opacity: 1, y: 0, duration: 0.5, stagger: 0.1 }, '-=0.3')
}

const closeMenu = () => {
  const menu = fullscreenMenu.value

  const tl = gsap.timeline()
  tl.to(menuItems.value, { opacity: 0, y: -20, duration: 0.3, ease: 'power2.in', stagger: 0.02 })
  tl.to(menuTitle.value, { opacity: 0, y: -20, duration: 0.3 }, '-=0.2')
  tl.to([previewTitle.value, previewDesc.value, previewIcon.value, previewImage.value], { opacity: 0, scale: 0.9, duration: 0.3 }, '-=0.3')
  tl.to(closeButton.value, { opacity: 0, duration: 0.2 }, '-=0.2')
  tl.to(menuContainer.value, { y: '-100%', opacity: 0, duration: 0.6, ease: 'power3.in' }, '-=0.2')
  tl.to(previewBox.value, {
    opacity: 0, duration: 0.3,
    onComplete: () => {
      menu.style.pointerEvents = 'none'
      hoveredItem.value = null
      try { document.body.style.overflow = '' } catch (err) {}
    }
  }, '-=0.4')
}

// ─── return from product ───
const handleReturnFromProduct = async () => {
  const currentPath = route.path
  const isMainPage = ['/fa', '/fa/about', '/fa/news', '/fa/careers', '/fa/contact'].includes(currentPath)

  if (isMainPage && !isMenuOpen.value && !isOpeningMenu.value) {
    await nextTick()
    isMenuOpen.value = true
    await nextTick()
    try { hoveredItem.value = useCases[0] } catch (e) {}
    openMenu()
  }
}

// ─── click menu item ───
const productPathMap = {
  0: '/fa/products/0955W',
  1: '/fa/products/0955B',
  2: '/fa/products/POLYFIL-F700',
  3: '/fa/products/POLYFIL-1300-EWA',
  4: '/fa/products/HDCHEM-4760',
  5: '/fa/products/SlIPCHEM-E-178',
  6: '/fa/products/RAFCOLOR-1560',
  7: '/fa/products/CALCICHEM-126-FP',
  8: '/fa/products/CALCICHEM-110-FRF',
  9: '/fa/products/CALCICHEM-275-PM',
  10: '/fa/products/UVCHEM-MB-R18',
}

const handleMenuItemClick = async (item) => {
  if (!item) return

  if (isMenuOpen.value) closeMenu()
  isMenuOpen.value = false
  if (fullscreenMenu.value) fullscreenMenu.value.style.pointerEvents = 'none'
  if (process.client) document.body.style.overflow = ''

  try {
    const path = productPathMap[item.index] || '/fa/products'
    if (process.client) {
      window.location.assign(path)
      return
    }
    await router.push(path)
  } catch (err) {
    console.error('Navigation error:', err)
  }
}

// ─── dropdown بیرون کلیک ───
const closeDropdownOutside = (e) => {
  if (langDropdownFa.value && !langDropdownFa.value.contains(e.target)) {
    langOpen.value = false
  }
}

// ─── lifecycle ───
onMounted(async () => {
  await nextTick()

  // dropdown بیرون کلیک لیسنر
  window.addEventListener('click', closeDropdownOutside)

  previousRoute.value = { path: route.path, query: route.query }

  if (menuItems.value && menuItems.value.length > 0) {
    gsap.set(menuItems.value, { y: -30, opacity: 0 })
  }
  if (menuTitle.value) {
    gsap.set(menuTitle.value, { y: -20, opacity: 0 })
  }
  if (previewTitle.value && previewDesc.value) {
    gsap.set([previewTitle.value, previewDesc.value], { y: 4, opacity: 0 })
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

})

// ─── route watch ───
watch(() => route.fullPath, async (newFullPath, oldFullPath) => {
  const newPath = route.path
  const oldPath = previousRoute.value?.path

  previousRoute.value = { path: route.path, query: route.query }

  if (!oldPath || !newPath) return

  const comingFromProduct = isProductPage(oldPath)
  const goingToMainPage = ['/fa', '/fa/about', '/fa/news', '/fa/careers', '/fa/contact'].includes(newPath)

  if (comingFromProduct && goingToMainPage) {
    await nextTick()
    setTimeout(() => {
      handleReturnFromProduct()
    }, 150)
  }
}, { immediate: false })

// ─── Escape key ───
onMounted(() => {
  const handleEscape = (e) => {
    if (e.key === 'Escape' && isMenuOpen.value) {
      toggleFullscreenMenu()
    }
  }
  window.addEventListener('keydown', handleEscape)
  onUnmounted(() => window.removeEventListener('keydown', handleEscape))
})

// ─── cleanup ───
onUnmounted(() => {
  try { document.body.style.overflow = '' } catch (err) {}
  window.removeEventListener('click', closeDropdownOutside)
  if (itemsWrapper.value) {
    itemsWrapper.value.removeEventListener('wheel', wheelHandler)
    itemsWrapper.value.removeEventListener('touchmove', touchHandler)
  }
})

// ─── computed styles ───
const previewImageStyle = computed(() => {
  const y = hoveredItem.value?.offsetY ?? '0px'
  return { position: 'relative', top: y, transition: 'top 220ms ease' }
})

const previewTitleStyle = computed(() => {
  const y = hoveredItem.value?.offsetTextY ?? '0px'
  return { position: 'relative', top: y, transition: 'top 220ms ease' }
})

const previewDescStyle = computed(() => {
  const y = hoveredItem.value?.offsetDescY ?? '0px'
  return { position: 'relative', top: y, transition: 'top 220ms ease' }
})
</script>

<style scoped>
/* ─── Desktop nav-link hover ─── */
.nav-link::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  display: block;
  width: 100%; height: 100%;
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

.nav-link:hover,
.nav-link:hover span {
  color: #ffffff !important;
}

/* ─── Mobile nav-link hover ─── */
.nav-link-mobile::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  display: block;
  width: 100%; height: 100%;
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

.nav-link-mobile:hover,
.nav-link-mobile:hover span {
  color: #030303 !important;
}

/* ─── Active states ─── */
.nav-link.active::before {
  opacity: 1;
  background-color: #ffffff;
  transform: scaleY(1);
}
.nav-link.active,
.nav-link.active span {
  color: #848484 !important;
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

/* ─── Router active ─── */
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
  color: #848484 !important;
}

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

/* ─── Mobile menu animation ─── */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: all 0.3s ease;
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  max-height: 0;
}

/* ─── Menu items ─── */
.menu-item {
  transform: translateZ(0);
  backface-visibility: hidden;
  color: #1f2937 !important;
  isolation: isolate;
  will-change: opacity, transform;
}

.menu-item-content {
  opacity: 1 !important;
  position: relative;
  z-index: 10;
  isolation: isolate;
}

.menu-item h3 {
  color: #848484 !important;
  position: relative;
  z-index: 10;
  opacity: 1 !important;
  font-family: 'IRANYekan', sans-serif;
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

/* ─── Scrollbar ─── */
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: rgba(0,0,0,0.05); border-radius: 3px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.2); border-radius: 3px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(234,179,8,0.5); }

/* ─── nav alignment ─── */
.nav-link,
.nav-link-mobile {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  white-space: nowrap;
}

.nav-link > span,
.nav-link-mobile > span {
  display: inline-flex;
  align-items: center;
  height: 100%;
}

.nav-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 80px;
  box-sizing: border-box;
}

.nav-link svg {
  display: inline-block;
  vertical-align: middle;
  margin-right: 6px;
}

.nav-link-mobile { min-height: 44px; }

/* ─── Container ─── */
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

/* ─── Mobile ─── */
@media (max-width: 767px) {
  .navbar-container {
    max-width: 100%;
    padding: 0;
  }
  .navbar-inner {
    transform: none !important;
  }
  .nav-link-mobile {
    min-height: 48px !important;
    padding: 12px 6px !important;
  }
  .menu-item {
    min-height: 48px !important;
    padding: 16px !important;
  }
  .menu-item h3 { font-size: 16px !important; }
  .menu-item span { font-size: 12px !important; }
  .navbar-inner img {
    width: 160px !important;
    height: 96px !important;
  }
}

/* ─── Desktop ─── */
@media (min-width: 768px) {
  .navbar-container {
    max-width: 1280px;
    min-width: 1280px;
  }
  .navbar-inner {
    --navbar-shift: -32px;
    transform: translateX(var(--navbar-shift));
  }
  .hide-desktop { display: none !important; }
}

/* ─── Fonts ─── */
@font-face {
  font-family: 'IRANYekan';
  src: url('/fonts/Qs_Iranyekan.ttf') format('truetype');
  font-weight: 300;
  font-style: normal;
}

@font-face {
  font-family: 'IRANYekan-b';
  src: url('/font/Qs_Iranyekan_bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}
</style>