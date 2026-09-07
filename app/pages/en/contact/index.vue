<!-- /en/contact/index.vue -->
<template>
  <div>
    <navbar />
    <div class="min-h-screen bg-[#f1f2f2] py-16 px-4 relative">

      <!-- Globe + Contact us overlay (hidden on mobile, visible on tablet+) -->
      <div class="globe-wrapper relative hidden md:flex justify-center items-center w-full">
        <worldc
          class="absolute top-0 z-0 globe-component"
          :scroll-rotate="scrollRotate"
        />
        <div class="absolute left-1/2 top-1/2 z-10" style="transform: translate(-50%, -50%); pointer-events: none;">
          <h1 class="contact-title font-bold text-[#848484] text-center select-none"
            style="text-shadow: 0 2px 16px #fff, 0 1px 0 #fff;">
            Contact us
          </h1>
        </div>
      </div>

      <!-- Mobile-only Contact title (shown only on mobile) -->
      <div class="flex md:hidden justify-center items-center mb-8 pt-4">
        <h1 class="text-3xl font-bold text-[#848484] text-center">Contact us</h1>
      </div>

      <!-- Header & Tabs -->
      <div class="text-center mb-8 md:mb-16 mt-0 md:mt-[-120px] relative z-20">
        <!-- Navigation Tabs: desktop only -->
        <div class="hidden xl:block tabs-wrapper mx-auto bg-white overflow-hidden shadow-sm">
          <div class="grid grid-cols-6">
            <button
              v-for="(tab, idx) in tabs"
              :key="tab.key"
              :class="[
                'tab-btn text-[#848484] transition-colors px-8 py-6 relative overflow-hidden',
                idx !== tabs.length - 1 ? 'border-r border-gray-200' : '',
                activeTab === tab.key ? 'bg-gray-100 font-bold' : ''
              ]"
              @click="scrollToSection(tab.key)"
            >
              <span class="relative z-10">{{ tab.label }}</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Middle East Section -->
      <div id="middleEast-section" ref="middleEastSection" class="max-w-7xl mx-auto mb-12 relative z-20">
        <h2 class="section-title font-bold text-[#848484] mb-6 md:mb-8">Middle East</h2>
        <div class="cards-row flex overflow-x-auto gap-0 no-scrollbar md:flex-wrap xl:flex-nowrap">
          <div
            v-for="(country, idx) in middleEastCountries"
            :key="'me-'+idx"
            class="contact-card flex flex-col items-center justify-center text-center"
            @mousemove="handleContactMouseMove($event, countryRefsOffset + idx)"
            @mouseleave="handleContactMouseLeave(countryRefsOffset + idx)"
            @touchmove="handleContactTouchMove($event, countryRefsOffset + idx)"
            @touchend="handleContactMouseLeave(countryRefsOffset + idx)"
          >
            <h3 class="text-xl md:text-2xl font-semibold text-[#848484] mb-3 md:mb-4">{{ country.name }}</h3>
            <p class="text-[#848484] mb-4 md:mb-6">{{ country.city }}</p>
            <div class="space-y-2 w-full flex flex-col items-center">
              <p class="text-sm text-[#848484]">Email</p>
              <div class="flex items-center justify-center gap-2 flex-wrap">
                <a :href="`mailto:${country.email}`" class="text-[#848484] hover:underline text-sm md:text-base break-all">
                  {{ country.email }}
                </a>
                <button
                  type="button"
                  class="copy-btn ml-1 px-2 py-1 rounded text-xs text-[#848484] border border-gray-300 transition"
                  @click="copyEmail(country.email, countryRefsOffset + idx)"
                >
                  <span v-if="copiedIdx === countryRefsOffset + idx && copied">Copied!</span>
                  <span v-else>Copy</span>
                </button>
              </div>
            </div>
            <div
              class="contact-card-bg-characters pointer-events-none"
              :ref="el => { if (el) contactCharactersRefs[countryRefsOffset + idx] = el }"
            >
              {{ contactRandomTexts[countryRefsOffset + idx] }}
            </div>
          </div>
        </div>
      </div>

      <!-- CIS & Caucasus Section -->
      <div id="cis-section" ref="cisSection" class="max-w-7xl mx-auto mb-12">
        <h2 class="section-title font-bold text-[#848484] mb-6 md:mb-8">CIS & Caucasus</h2>
        <div class="cards-row flex overflow-x-auto gap-0 no-scrollbar md:flex-wrap xl:flex-nowrap">
          <div
            v-for="(country, idx) in cisCountries"
            :key="'cis-'+idx"
            class="contact-card flex flex-col items-center justify-center text-center"
            @mousemove="handleContactMouseMove($event, cisRefsOffset + idx)"
            @mouseleave="handleContactMouseLeave(cisRefsOffset + idx)"
            @touchmove="handleContactTouchMove($event, cisRefsOffset + idx)"
            @touchend="handleContactMouseLeave(cisRefsOffset + idx)"
          >
            <h3 class="text-xl md:text-2xl font-semibold text-[#848484] mb-3 md:mb-4">{{ country.name }}</h3>
            <p class="text-[#848484] mb-4 md:mb-6">{{ country.city }}</p>
            <div class="space-y-2 w-full flex flex-col items-center">
              <p class="text-sm text-[#848484]">Email</p>
              <a :href="`mailto:${country.email}`" class="text-[#848484] hover:underline text-sm md:text-base break-all">
                {{ country.email }}
              </a>
              <button
                type="button"
                class="copy-btn px-2 py-1 rounded text-xs text-[#848484] border border-gray-300 transition"
                @click="copyEmail(country.email, cisRefsOffset + idx)"
              >
                <span v-if="copiedIdx === cisRefsOffset + idx && copied">Copied!</span>
                <span v-else>Copy</span>
              </button>
            </div>
            <div
              class="contact-card-bg-characters pointer-events-none"
              :ref="el => { if (el) contactCharactersRefs[cisRefsOffset + idx] = el }"
            >
              {{ contactRandomTexts[cisRefsOffset + idx] }}
            </div>
          </div>
        </div>
      </div>

      <!-- Europe Section -->
      <div id="europe-section" ref="europeSection" class="max-w-7xl mx-auto mb-12">
        <h2 class="section-title font-bold text-[#848484] mb-6 md:mb-8">Europe</h2>
        <div class="cards-row flex overflow-x-auto gap-0 no-scrollbar md:flex-wrap xl:flex-nowrap">
          <div
            v-for="(country, idx) in europeCountries"
            :key="'eu-'+idx"
            class="contact-card flex flex-col items-center justify-center text-center"
            @mousemove="handleContactMouseMove($event, europeRefsOffset + idx)"
            @mouseleave="handleContactMouseLeave(europeRefsOffset + idx)"
            @touchmove="handleContactTouchMove($event, europeRefsOffset + idx)"
            @touchend="handleContactMouseLeave(europeRefsOffset + idx)"
          >
            <h3 class="text-xl md:text-2xl font-semibold text-[#848484] mb-3 md:mb-4">{{ country.name }}</h3>
            <p class="text-[#848484] mb-4 md:mb-6">{{ country.city }}</p>
            <div class="space-y-2 w-full flex flex-col items-center">
              <p class="text-sm text-[#848484]">Email</p>
              <div class="flex items-center justify-center gap-2 flex-wrap">
                <a :href="`mailto:${country.email}`" class="text-[#848484] hover:underline text-sm md:text-base break-all">
                  {{ country.email }}
                </a>
                <button
                  type="button"
                  class="copy-btn ml-1 px-2 py-1 rounded text-xs text-[#848484] border border-gray-300 transition"
                  @click="copyEmail(country.email, europeRefsOffset + idx)"
                >
                  <span v-if="copiedIdx === europeRefsOffset + idx && copied">Copied!</span>
                  <span v-else>Copy</span>
                </button>
              </div>
            </div>
            <div
              class="contact-card-bg-characters pointer-events-none"
              :ref="el => { if (el) contactCharactersRefs[europeRefsOffset + idx] = el }"
            >
              {{ contactRandomTexts[europeRefsOffset + idx] }}
            </div>
          </div>
        </div>
      </div>

      <!-- Asia Section -->
      <div id="asia-section" ref="asiaSection" class="max-w-7xl mx-auto mb-12">
        <h2 class="section-title font-bold text-[#848484] mb-6 md:mb-8">Asia Pacific</h2>
        <div class="cards-row flex overflow-x-auto gap-0 no-scrollbar md:flex-wrap xl:flex-nowrap">
          <div
            v-for="(country, idx) in asiaCountries"
            :key="'asia-'+idx"
            class="contact-card flex flex-col items-center justify-center text-center"
            @mousemove="handleContactMouseMove($event, asiaRefsOffset + idx)"
            @mouseleave="handleContactMouseLeave(asiaRefsOffset + idx)"
            @touchmove="handleContactTouchMove($event, asiaRefsOffset + idx)"
            @touchend="handleContactMouseLeave(asiaRefsOffset + idx)"
          >
            <h3 class="text-xl md:text-2xl font-semibold text-[#848484] mb-3 md:mb-4">{{ country.name }}</h3>
            <p class="text-[#848484] mb-4 md:mb-6">{{ country.city }}</p>
            <div class="space-y-2 w-full flex flex-col items-center">
              <p class="text-sm text-[#848484]">Email</p>
              <div class="flex items-center justify-center gap-2 flex-wrap">
                <a :href="`mailto:${country.email}`" class="text-[#848484] hover:underline text-sm md:text-base break-all">
                  {{ country.email }}
                </a>
                <button
                  type="button"
                  class="copy-btn ml-1 px-2 py-1 rounded text-xs text-[#848484] border border-gray-300 transition"
                  @click="copyEmail(country.email, asiaRefsOffset + idx)"
                >
                  <span v-if="copiedIdx === asiaRefsOffset + idx && copied">Copied!</span>
                  <span v-else>Copy</span>
                </button>
              </div>
            </div>
            <div
              class="contact-card-bg-characters pointer-events-none"
              :ref="el => { if (el) contactCharactersRefs[asiaRefsOffset + idx] = el }"
            >
              {{ contactRandomTexts[asiaRefsOffset + idx] }}
            </div>
          </div>
        </div>
      </div>

      <!-- Our Address Section -->
      <div id="address-section" ref="addressSection" class="max-w-7xl mx-auto mb-12 relative z-10">
        <h2 class="section-title font-bold text-[#848484] mb-6 md:mb-8">Our Address</h2>
        <div class="bg-white rounded-lg shadow-lg p-4 md:p-8">
          <div class="flex flex-col lg:flex-row gap-8 items-start">
            <!-- Address Information -->
            <div class="flex-1 space-y-6">
              <div>
                <h3 class="text-xl md:text-2xl font-semibold text-[#848484] mb-4">Aras Free Trade</h3>
                <p class="text-[#848484] leading-relaxed">
                  Plots 437 & 438, South C Street<br />
                  Industrial Town Phase 2<br />
                  Aras Free Trade-Industrial Zone
                </p>
              </div>
              <div>
                <h4 class="text-base md:text-lg font-semibold text-[#848484] mb-2">Contact Information</h4>
                <div class="space-y-2">
                  <p class="text-[#848484]">
                    <span class="font-medium">Email:</span>
                    <a href="mailto:info@polychemmb.com" class="text-[#848484] hover:text-[#FFD700] transition-colors break-all">
                      info@polychemmb.com
                    </a>
                  </p>
                  <p class="text-[#848484]">
                    <span class="font-medium">Phone:</span>
                    <a href="tel:+982122898979" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                      +98 21 2289 8979-80
                    </a>
                  </p>
                </div>
              </div>
              <div>
                <h4 class="text-base md:text-lg font-semibold text-[#848484] mb-2">Business Hours</h4>
                <p class="text-[#848484]">
                  <span class="font-medium">Saturday to Wednesday:</span><br>
                  8:00 AM – 5:00 PM (Tehran Time, UTC+3:30)<br><br>
                  <span class="font-medium">Thursday to Friday:</span><br>
                  8:00 AM – 4:00 PM (Tehran Time, UTC+3:30)
                </p>
              </div>
              <div>
                <h4 class="text-base md:text-lg font-semibold text-[#848484] mb-2">Sales Department</h4>
                <div class="space-y-2">
                  <p class="text-[#848484]">
                    <span class="font-medium inline-block w-16">Email:</span>
                    <a href="mailto:Sales@polychemmb.com" class="text-[#848484] hover:text-[#FFD700] transition-colors break-all">
                      Sales@polychemmb.com
                    </a>
                  </p>
                  <p class="text-[#848484]">
                    <span class="font-medium inline-block w-16">Phone:</span>
                    <a href="tel:+989144605066" class="text-[#848484] hover:text-[#FFD700] transition-colors">+98 914 460 50 66</a>
                  </p>
                  <p class="text-[#848484]">
                    <span class="font-medium inline-block w-16">Phone:</span>
                    <a href="tel:+989004605066" class="text-[#848484] hover:text-[#FFD700] transition-colors">+98 900 460 50 66</a>
                  </p>
                  <p class="text-[#848484]">
                    <span class="font-medium inline-block w-16">Phone:</span>
                    <a href="tel:+905312866666" class="text-[#848484] hover:text-[#FFD700] transition-colors">+90 531 286 66 66</a>
                  </p>
                </div>
              </div>
            </div>
            <!-- Map Component -->
            <div class="flex-1 w-full">
              <MapComponent />
            </div>
          </div>
        </div>
      </div>

      <!-- Send us a message (Form) Section -->
      <div id="form-section" ref="formSection" class="max-w-7xl mx-auto mb-12">
        <FormComponent :countries="allContactCountryNames" />
      </div>

    </div>
    <Chatbox />
    <footer2 />
  </div>
</template>

<script setup>
import { ref, nextTick, onMounted, onUnmounted } from 'vue'
import FormComponent from '~/components/en/contact/form.vue'
import MapComponent from '~/components/en/contact/map.vue'
import navbar from '~/components/en/layout/navbar.vue'
import footer2 from '~/components/en/layout/footer.vue'
import worldc from '~/components/en/contact/world.vue'
import Chatbox from '~/components/en/chatbox/chatbox.vue'

const tabs = [
  { key: 'middleEast', label: 'Middle East' },
  { key: 'cis', label: 'CIS & Caucasus' },
  { key: 'europe', label: 'Europe' },
  { key: 'asia', label: 'Asia' },
  { key: 'address', label: 'Our Address' },
  { key: 'form', label: 'Send us a message' }
]

useSeoMeta({
  title: 'Contact Us | POLYCHEM',
  description: 'Contact POLYCHEM for polymer compounds, masterbatches, export sales, and technical support.',
  ogTitle: 'Contact Us | POLYCHEM',
  ogDescription: 'Reach our global sales teams and technical experts.',
  ogUrl: 'https://polychemmb.com/en/contact',
})

const activeTab = ref('middleEast')

const scrollToSection = async (tabKey) => {
  activeTab.value = tabKey
  await nextTick()
  const idMap = {
    middleEast: 'middleEast-section',
    cis: 'cis-section',
    europe: 'europe-section',
    asia: 'asia-section',
    address: 'address-section',
    form: 'form-section'
  }
  const el = document.getElementById(idMap[tabKey])
  if (!el) return
  const navbarEl = document.querySelector('nav') || document.querySelector('.navbar') || document.querySelector('#navbar')
  let navHeight = navbarEl ? navbarEl.offsetHeight : 80
  if (!navHeight || navHeight < 40) navHeight = 80
  const top = el.getBoundingClientRect().top + window.scrollY - navHeight - 8
  window.scrollTo({ top, behavior: 'smooth' })
}

const middleEastCountries = [
  { name: 'Iraq', city: 'Baghdad', email: 'mea-sales@polychemmb.com' },
  { name: 'Iran', city: 'Tehran', email: 'mea-sales@polychemmb.com' },
  { name: 'Kuwait', city: 'Kuwait City', email: 'mea-sales@polychemmb.com' }
]
const cisCountries = [
  { name: 'Armenia', city: 'Yerevan', email: 'cis-sales@polychemmb.com' },
  { name: 'Azerbaijan', city: 'Baku', email: 'cis-sales@polychemmb.com' },
  { name: 'Belarus', city: 'Minsk', email: 'cis-sales@polychemmb.com' },
  { name: 'Kazakhstan', city: 'Astana', email: 'cis-sales@polychemmb.com' },
  { name: 'Kyrgyzstan', city: 'Bishkek', email: 'cis-sales@polychemmb.com' },
  { name: 'Russia', city: 'Moscow', email: 'cis-sales@polychemmb.com' },
  { name: 'Tajikistan', city: 'Dushanbe', email: 'cis-sales@polychemmb.com' },
  { name: 'Uzbekistan', city: 'Tashkent', email: 'cis-sales@polychemmb.com' }
]
const europeCountries = [
  { name: 'Turkey', city: 'Ankara', email: 'europe-sales@polychemmb.com' },
  { name: 'Greece', city: 'Athens', email: 'europe-sales@polychemmb.com' }
]
const asiaCountries = [
  { name: 'China', city: 'Beijing', email: 'apac-sales@polychemmb.com' },
  { name: 'India', city: 'New Delhi', email: 'apac-sales@polychemmb.com' },
  { name: 'Pakistan', city: 'Islamabad', email: 'apac-sales@polychemmb.com' }
]

const allContactCountryNames = [
  ...middleEastCountries.map(c => c.name),
  ...cisCountries.map(c => c.name),
  ...europeCountries.map(c => c.name),
  ...asiaCountries.map(c => c.name)
]

const countryRefsOffset = 0
const cisRefsOffset = countryRefsOffset + middleEastCountries.length
const europeRefsOffset = cisRefsOffset + cisCountries.length
const asiaRefsOffset = europeRefsOffset + europeCountries.length
const totalCards = middleEastCountries.length + cisCountries.length + europeCountries.length + asiaCountries.length

const contactCharactersRefs = ref([])
const CONTACT_PARTICLE_LENGTH = 95000
const contactRandomChemicalString = (length = CONTACT_PARTICLE_LENGTH) => {
  const pair = '· '
  return pair.repeat(Math.ceil(length / pair.length)).substring(0, length)
}
const contactRandomTexts = ref(Array(totalCards).fill(null).map(() => contactRandomChemicalString()))

const handleContactMouseMove = (e, index) => {
  const card = e.currentTarget
  const rect = card.getBoundingClientRect()
  const x = e.clientX - rect.left
  const y = e.clientY - rect.top
  const el = contactCharactersRefs.value[index]
  if (!el) return
  el.style.setProperty('--x', `${x}px`)
  el.style.setProperty('--y', `${y}px`)
  const tx = ((x - rect.width / 2) / (rect.width / 2)) * 18
  const ty = ((y - rect.height / 2) / (rect.height / 2)) * 18
  el.style.setProperty('--tx', `${tx}px`)
  el.style.setProperty('--ty', `${ty}px`)
  el.style.setProperty('--scale', '1.06')
  contactRandomTexts.value[index] = contactRandomChemicalString()
}
const handleContactTouchMove = (e, index) => {
  const touch = e.touches[0]
  const card = e.currentTarget
  const rect = card.getBoundingClientRect()
  const x = touch.clientX - rect.left
  const y = touch.clientY - rect.top
  const el = contactCharactersRefs.value[index]
  if (!el) return
  el.style.setProperty('--x', `${x}px`)
  el.style.setProperty('--y', `${y}px`)
  const tx = ((x - rect.width / 2) / (rect.width / 2)) * 18
  const ty = ((y - rect.height / 2) / (rect.height / 2)) * 18
  el.style.setProperty('--tx', `${tx}px`)
  el.style.setProperty('--ty', `${ty}px`)
  el.style.setProperty('--scale', '1.06')
  contactRandomTexts.value[index] = contactRandomChemicalString()
}
const handleContactMouseLeave = (index) => {
  const el = contactCharactersRefs.value[index]
  if (!el) return
  el.style.setProperty('--tx', '0px')
  el.style.setProperty('--ty', '0px')
  el.style.setProperty('--scale', '1')
}

const copied = ref(false)
const copiedIdx = ref(null)
const copyEmail = async (email, idx) => {
  try {
    await navigator.clipboard.writeText(email)
    copied.value = true
    copiedIdx.value = idx
    setTimeout(() => { copied.value = false; copiedIdx.value = null }, 1200)
  } catch (e) {}
}

const scrollRotate = ref(0)
const handleScroll = () => { scrollRotate.value = window.scrollY * 0.003 }
onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))
</script>

<style scoped>

/* ─── Globe ──────────────────────────────────────── */
.globe-wrapper {
  height: 480px;
  min-height: 340px;
}
.globe-component {
  left: calc(50% - 800px);
  width: 1400px;
  height: 700px;
  max-width: 100vw;
}
.contact-title { font-size: 3.75rem; }

@media (max-width: 768px) {
  .globe-wrapper  { height: 280px; min-height: 200px; }
  .globe-component { left: calc(50% - 400px); width: 800px; height: 400px; }
  .contact-title  { font-size: 2rem; }
}

/* ─── Tabs wrapper ───────────────────────────────── */
.tabs-wrapper { max-width: 80rem; }

/* ─── Tab button hover effect ────────────────────── */
.tab-btn {
  position: relative;
  overflow: hidden;
  transition: color 300ms ease;
}
.tab-btn::before {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 100%; height: 100%;
  background-color: #979797;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}
.tab-btn:hover::before,
.tab-btn:focus-visible::before { transform: translateY(0); }
.tab-btn:hover,
.tab-btn:focus-visible { color: #ffffff; outline: none; }
.tab-btn span { position: relative; z-index: 1; }

/* ─── Section titles ─────────────────────────────── */
.section-title { font-size: 2.25rem; }
@media (max-width: 768px) {
  .section-title { font-size: 1.5rem; }
}

/* ─── Cards row ──────────────────────────────────── */

/* Mobile: vertical stack */
@media (max-width: 767px) {
  .cards-row {
    flex-direction: column !important;
    overflow-x: visible !important;
  }
}

/* Tablet (768–1279px): 2-column wrap grid */
@media (min-width: 768px) and (max-width: 1279px) {
  .cards-row {
    flex-wrap: wrap !important;
    overflow-x: visible !important;
  }
  .cards-row .contact-card {
    width: 50% !important;
    min-width: 0 !important;
    flex: 0 0 50% !important;
  }
}

/* Desktop (1280px+): horizontal scroll row */
@media (min-width: 1280px) {
  .cards-row {
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
  }
}

/* ─── Contact card ───────────────────────────────── */
.contact-card {
  background: #fff;
  border-radius: 0;
  padding: 2rem;
  box-shadow: 0 1px 4px 0 #e5e7eb;
  position: relative;
  overflow: hidden;
  border-right: 1px solid #e5e7eb;
  border-bottom: 1px solid #e5e7eb;
  min-width: 280px;
  min-height: 360px;
  flex: 1 1 0%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  transition: box-shadow 0.3s;
}
.contact-card:hover { box-shadow: 0 4px 16px 0 #e5e7eb; }

@media (max-width: 767px) {
  .contact-card {
    min-width: auto;
    width: 100%;
    min-height: 300px;
    border-right: none;
  }
}

/* ─── Copy button ────────────────────────────────── */
.copy-btn {
  position: relative;
  overflow: hidden;
  background: transparent;
  color: #848484;
  border: 1px solid #e5e7eb;
  transition: color 300ms, border-color 300ms;
  z-index: 1;
}
.copy-btn::before {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 100%; height: 100%;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}
.copy-btn:hover::before,
.copy-btn:focus-visible::before { transform: translateY(0); }
.copy-btn:hover,
.copy-btn:focus-visible { color: #fff; border-color: #FFCD05; outline: none; }
.copy-btn > span { position: relative; z-index: 1; }

/* ─── Background particle effect ────────────────── */
.contact-card-bg-characters {
  --x: 0px; --y: 0px; --tx: 0px; --ty: 0px; --scale: 1;
  position: absolute;
  top: 0; left: 0;
  height: 100%; width: 100%;
  word-wrap: break-word;
  font-size: 15px;
  line-height: 0.5;
  overflow: hidden;
  font-family: monospace;
  color: #a8a8a8;
  opacity: 0;
  transition: opacity 0.45s cubic-bezier(.2,.9,.3,1);
  will-change: transform, opacity;
  -webkit-mask-image: radial-gradient(300px circle at var(--x) var(--y), #000 20%, rgba(0,0,0,0.25), transparent);
  mask-image: radial-gradient(300px circle at var(--x) var(--y), #000 20%, rgba(0,0,0,0.25), transparent);
  transform: translate(var(--tx, 0px), var(--ty, 0px)) scale(var(--scale, 1));
  padding: 20px;
  z-index: 2;
  pointer-events: none;
}
.contact-card:hover .contact-card-bg-characters,
.contact-card:active .contact-card-bg-characters { opacity: 1; }

/* ─── Scrollbar hide ─────────────────────────────── */
.no-scrollbar::-webkit-scrollbar { display: none; }
.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
.scrollbar-hide::-webkit-scrollbar { display: none; }
.scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
</style>