<template>
  <div>
    <navbar />
    <div class="min-h-screen bg-[#f1f2f2] py-16 px-4 relative">
      <!-- Globe + Contact us overlay -->
      <div class="relative flex justify-center items-center w-full" style="height: 480px; min-height: 340px;">
        <worldc
          class="absolute top-0 z-0"
          style="left: calc(50% - 800px); width: 1400px; height: 700px; max-width: 100vw; filter: drop-shadow(none);"
          :scroll-rotate="scrollRotate"
        />
        <div
          class="absolute left-1/2 top-1/2 z-10"
          style="transform: translate(-50%, -50%); pointer-events: none;"
        >
          <h1 class="text-6xl font-bold text-[#848484] mb-0 text-center select-none" style="text-shadow: 0 2px 16px #fff, 0 1px 0 #fff;">
            İletişim
          </h1>
        </div>
      </div>
      <!-- Header & Tabs -->
      <div class="text-center mb-16 mt-[-120px] relative z-20">
        <!-- Navigation Tabs -->
        <div class="grid grid-cols-6 w-7xl mx-auto bg-white overflow-hidden shadow-sm">
          <button
            v-for="(tab, idx) in tabs"
            :key="tab.key"
            :class="[
              'text-[#848484] transition-colors px-8 py-6 relative overflow-hidden',
              idx !== tabs.length - 1 ? 'border-r border-gray-200' : '',
              activeTab === tab.key ? 'bg-gray-100 font-bold' : 'hover:text-white'
            ]"
            @click="scrollToSection(tab.key)"
          >
            <span class="relative z-10">{{ tab.label }}</span>
          </button>
        </div>
      </div>

      <!-- Middle East Section -->
      <div
        id="middleEast-section"
        ref="middleEastSection"
        class="max-w-7xl mx-auto mb-12 relative z-20"
      >
        <h2 class="text-4xl font-bold text-[#848484] mb-8 relative z-20">Middle East</h2>
        <div class="flex overflow-x-auto gap-0 no-scrollbar">
          <div
            v-for="(country, idx) in middleEastCountries"
            :key="'me-'+idx"
            class="contact-card flex flex-col items-center justify-center text-center"
            @mousemove="handleContactMouseMove($event, countryRefsOffset + idx)"
            @mouseleave="handleContactMouseLeave(countryRefsOffset + idx)"
            @touchmove="handleContactTouchMove($event, countryRefsOffset + idx)"
            @touchend="handleContactMouseLeave(countryRefsOffset + idx)"
          >
            <h3 class="text-2xl font-semibold text-[#848484] mb-4">{{ country.name }}</h3>
            <p class="text-[#848484] mb-6">{{ country.city }}</p>
            <div class="space-y-2 w-full flex flex-col items-center">
              <p class="text-sm text-[#848484]">Email</p>
              <div class="flex items-center justify-center gap-2">
                <a :href="`mailto:${country.email}`" class="text-[#848484] hover:underline">
                  {{ country.email }}
                </a>
                <button
                  type="button"
                  class="ml-1 px-2 py-1 rounded bg-gray-100 hover:bg-gray-200 text-xs text-[#848484] border border-gray-300 transition"
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
      <div
        id="cis-section"
        ref="cisSection"
        class="max-w-7xl mx-auto mb-12"
      >
        <h2 class="text-4xl font-bold text-[#848484] mb-8 ">CIS & Caucasus</h2>
        <div class="flex overflow-x-auto gap-0 no-scrollbar">
          <div
            v-for="(country, idx) in cisCountries"
            :key="'cis-'+idx"
            class="contact-card flex flex-col items-center justify-center text-center"
            @mousemove="handleContactMouseMove($event, cisRefsOffset + idx)"
            @mouseleave="handleContactMouseLeave(cisRefsOffset + idx)"
            @touchmove="handleContactTouchMove($event, cisRefsOffset + idx)"
            @touchend="handleContactMouseLeave(cisRefsOffset + idx)"
          >
            <h3 class="text-2xl font-semibold text-[#848484] mb-4">{{ country.name }}</h3>
            <p class="text-[#848484] mb-6">{{ country.city }}</p>
            <div class="space-y-2 w-full flex flex-col items-center">
              <p class="text-sm text-[#848484]">Email</p>
              <a :href="`mailto:${country.email}`" class="text-[#848484] hover:underline">
                {{ country.email }}
              </a>
              <button
                type="button"
                class="px-2 py-1 rounded bg-gray-100 hover:bg-gray-200 text-xs text-[#848484] border border-gray-300 transition"
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
      <div
        id="europe-section"
        ref="europeSection"
        class="max-w-7xl mx-auto mb-12"
      >
        <h2 class="text-4xl font-bold text-[#848484] mb-8 text">Europe</h2>
        <div class="flex overflow-x-auto gap-0 no-scrollbar">
          <div
            v-for="(country, idx) in europeCountries"
            :key="'eu-'+idx"
            class="contact-card flex flex-col items-center justify-center text-center"
            @mousemove="handleContactMouseMove($event, europeRefsOffset + idx)"
            @mouseleave="handleContactMouseLeave(europeRefsOffset + idx)"
            @touchmove="handleContactTouchMove($event, europeRefsOffset + idx)"
            @touchend="handleContactMouseLeave(europeRefsOffset + idx)"
          >
            <h3 class="text-2xl font-semibold text-[#848484] mb-4">{{ country.name }}</h3>
            <p class="text-[#848484] mb-6">{{ country.city }}</p>
            <div class="space-y-2 w-full flex flex-col items-center">
              <p class="text-sm text-[#848484]">Email</p>
              <div class="flex items-center justify-center gap-2">
                <a :href="`mailto:${country.email}`" class="text-[#848484] hover:underline">
                  {{ country.email }}
                </a>
                <button
                  type="button"
                  class="ml-1 px-2 py-1 rounded bg-gray-100 hover:bg-gray-200 text-xs text-[#848484] border border-gray-300 transition"
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
      <div
        id="asia-section"
        ref="asiaSection"
        class="max-w-7xl mx-auto mb-12"
      >
        <h2 class="text-4xl font-bold text-[#848484] mb-8 ">Asia Pacific</h2>
        <div class="flex overflow-x-auto gap-0 no-scrollbar">
          <div
            v-for="(country, idx) in asiaCountries"
            :key="'asia-'+idx"
            class="contact-card flex flex-col items-center justify-center text-center"
            @mousemove="handleContactMouseMove($event, asiaRefsOffset + idx)"
            @mouseleave="handleContactMouseLeave(asiaRefsOffset + idx)"
            @touchmove="handleContactTouchMove($event, asiaRefsOffset + idx)"
            @touchend="handleContactMouseLeave(asiaRefsOffset + idx)"
          >
            <h3 class="text-2xl font-semibold text-[#848484] mb-4">{{ country.name }}</h3>
            <p class="text-[#848484] mb-6">{{ country.city }}</p>
            <div class="space-y-2 w-full flex flex-col items-center">
              <p class="text-sm text-[#848484]">Email</p>
              <div class="flex items-center justify-center gap-2">
                <a :href="`mailto:${country.email}`" class="text-[#848484] hover:underline">
                  {{ country.email }}
                </a>
                <button
                  type="button"
                  class="ml-1 px-2 py-1 rounded bg-gray-100 hover:bg-gray-200 text-xs text-[#848484] border border-gray-300 transition"
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
<div
  id="address-section"
  ref="addressSection"
  class="max-w-7xl mx-auto mb-12 relative z-10"
>
  <h2 class="text-4xl font-bold text-[#848484] mb-8">Adresimiz</h2>
  <div class="bg-white rounded-lg shadow-lg p-8">
    <div class="flex flex-col lg:flex-row gap-8 items-start">
      <!-- Address Information -->
      <div class="flex-1 space-y-6">
        <div>
          <h3 class="text-2xl font-semibold text-[#848484] mb-4">Aras Serbest Ticaret</h3>
          <p class="text-[#848484] leading-relaxed">
            Parsel 437 & 438, Güney C Caddesi<br />
            Sanayi Şehri Faz 2<br />
            Aras Serbest Ticaret-Sanayi Bölgesi
          </p>
        </div>

        <div>
          <h4 class="text-lg font-semibold text-[#848484] mb-2">İletişim Bilgileri</h4>
          <div class="space-y-2">
            <p class="text-[#848484]">
              <span class="font-medium">E-posta:</span> 
              <a href="mailto:info@polychemmb.com" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                info@polychemmb.com
              </a>
            </p>
            <p class="text-[#848484]">
              <span class="font-medium">Telefon:</span> 
              <a href="tel:+982122898979" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                +98 21 2289 8979-80
              </a>
            </p>
          </div>
        </div>

        <div>
          <h4 class="text-lg font-semibold text-[#848484] mb-2">Çalışma Saatleri</h4>
          <p class="text-[#848484]">
            <span class="font-medium w-16">Cumartesi – Çarşamba:</span><br>
            08:00 – 17:00 (Tahran Saati, UTC+3:30)<br><br>
            <span class="font-medium w-16">Perşembe – Cuma:</span><br>
            08:00 – 16:00 (Tahran Saati, UTC+3:30)
          </p>
        </div>

        <div>
          <h4 class="text-lg font-semibold text-[#848484] mb-2">Satış Departmanı İletişim Bilgileri</h4>
          <div class="space-y-2">
            <p class="text-[#848484]">
              <span class="font-medium inline-block w-16">Eposta:</span> 
              <a href="mailto:Sales@polychemmb.com" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                Sales@polychemmb.com
              </a>
            </p>
            <p class="text-[#848484]">
              <span class="font-medium inline-block w-16">Telefon:</span> 
              <a href="tel:+989144605066" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                +98 914 460 50 66
              </a>
            </p>
            <p class="text-[#848484]">
              <span class="font-medium inline-block w-16">Telefon:</span> 
              <a href="tel:+989004605066" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                +98 900 460 50 66
              </a>
            </p>
            <p class="text-[#848484]">
              <span class="font-medium inline-block w-16">Telefon:</span> 
              <a href="tel:+905312866666" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                +90 531 286 66 66
              </a>
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
      <div
        id="form-section"
        ref="formSection"
        class="max-w-7xl mx-auto mb-12"
      >
        <FormComponent :countries="allContactCountryNames" />
      </div>
    </div>
    <!-- Chat widget (always present on page) -->
    <Chatbox />
    <footer2 />
  </div>
</template>

<script setup>
import { ref, nextTick, onMounted, onUnmounted } from 'vue'
import FormComponent from '~/components/tr/contact/form.vue'
import MapComponent from '~/components/tr/contact/map.vue'
import navbar from '~/components/tr/layout/navbar.vue'
import footer2 from '~/components/tr/layout/footer.vue'
import worldc from '~/components/tr/contact/world.vue'
import Chatbox from '~/components/tr/chatbox/chatbox.vue'

// Tabs
const tabs = [
  { key: 'middleEast', label: 'Middle East' },
  { key: 'cis', label: 'CIS & Caucasus' },
  { key: 'europe', label: 'Europe' },
  { key: 'asia', label: 'Asia' },
  { key: 'address', label: 'Our Address' },
  { key: 'form', label: 'Send us a message' }
]

// Active tab
const activeTab = ref('middleEast')
const sectionRefs = {
  middleEast: ref(null),
  cis: ref(null),
  europe: ref(null),
  asia: ref(null),
  form: ref(null)
}

// Scroll to section
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
  const sectionId = idMap[tabKey]
  const el = document.getElementById(sectionId)
  if (!el) return

  // try to detect the navbar height; fallback to 80px
  const navbarEl = document.querySelector('nav') || document.querySelector('.navbar') || document.querySelector('#navbar')
  let navHeight = navbarEl ? navbarEl.offsetHeight : 0
  if (!navHeight || navHeight < 40) {
    // sensible default if nav not found or reports tiny height
    navHeight = 80
  }

  // compute final scroll position and scroll smoothly
  const top = el.getBoundingClientRect().top + window.scrollY - navHeight - 8 // small gap
  window.scrollTo({ top, behavior: 'smooth' })
}

// Countries data
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

// Add combined country names for form
const allContactCountryNames = [
  ...middleEastCountries.map(c => c.name),
  ...cisCountries.map(c => c.name),
  ...europeCountries.map(c => c.name),
  ...asiaCountries.map(c => c.name)
]

// Offsets for refs/texts
const countryRefsOffset = 0
const cisRefsOffset = countryRefsOffset + middleEastCountries.length
const europeRefsOffset = cisRefsOffset + cisCountries.length
const asiaRefsOffset = europeRefsOffset + europeCountries.length
const totalCards = middleEastCountries.length + cisCountries.length + europeCountries.length + asiaCountries.length

const contactCharactersRefs = ref([])
const CONTACT_PARTICLE_LENGTH_INITIAL = 95000
const CONTACT_PARTICLE_LENGTH_ON_MOVE = 95000
const contactRandomChemicalString = (length = CONTACT_PARTICLE_LENGTH_ON_MOVE) => {
  const pair = '· '
  const repeats = Math.ceil(length / pair.length)
  return pair.repeat(repeats).substring(0, length)
}
const contactRandomTexts = ref(
  Array(totalCards).fill().map(() => contactRandomChemicalString(CONTACT_PARTICLE_LENGTH_INITIAL))
)

const handleContactMouseMove = (e, index) => {
  const card = e.currentTarget
  const rect = card.getBoundingClientRect()
  const x = e.clientX - rect.left
  const y = e.clientY - rect.top
  if (contactCharactersRefs.value[index]) {
    contactCharactersRefs.value[index].style.setProperty('--x', `${x}px`)
    contactCharactersRefs.value[index].style.setProperty('--y', `${y}px`)
    const cx = rect.width / 2
    const cy = rect.height / 2
    const maxOffset = 18
    const tx = ((x - cx) / cx) * maxOffset
    const ty = ((y - cy) / cy) * maxOffset
    contactCharactersRefs.value[index].style.setProperty('--tx', `${tx}px`)
    contactCharactersRefs.value[index].style.setProperty('--ty', `${ty}px`)
    contactCharactersRefs.value[index].style.setProperty('--scale', '1.06')
    contactRandomTexts.value[index] = contactRandomChemicalString(CONTACT_PARTICLE_LENGTH_ON_MOVE)
  }
}
const handleContactTouchMove = (e, index) => {
  const touch = e.touches[0]
  const card = e.currentTarget
  const rect = card.getBoundingClientRect()
  const x = touch.clientX - rect.left
  const y = touch.clientY - rect.top
  if (contactCharactersRefs.value[index]) {
    contactCharactersRefs.value[index].style.setProperty('--x', `${x}px`)
    contactCharactersRefs.value[index].style.setProperty('--y', `${y}px`)
    const cx = rect.width / 2
    const cy = rect.height / 2
    const maxOffset = 18
    const tx = ((x - cx) / cx) * maxOffset
    const ty = ((y - cy) / cy) * maxOffset
    contactCharactersRefs.value[index].style.setProperty('--tx', `${tx}px`)
    contactCharactersRefs.value[index].style.setProperty('--ty', `${ty}px`)
    contactCharactersRefs.value[index].style.setProperty('--scale', '1.06')
    contactRandomTexts.value[index] = contactRandomChemicalString(CONTACT_PARTICLE_LENGTH_ON_MOVE)
  }
}
const handleContactMouseLeave = (index) => {
  if (contactCharactersRefs.value[index]) {
    contactCharactersRefs.value[index].style.setProperty('--tx', `0px`)
    contactCharactersRefs.value[index].style.setProperty('--ty', `0px`)
    contactCharactersRefs.value[index].style.setProperty('--scale', '1')
  }
}

// Copy email logic
const copied = ref(false)
const copiedIdx = ref(null)
const copyEmail = async (email, idx) => {
  try {
    await navigator.clipboard.writeText(email)
    copied.value = true
    copiedIdx.value = idx
    setTimeout(() => {
      copied.value = false
      copiedIdx.value = null
    }, 1200)
  } catch (e) {
    // fallback: do nothing
  }
}

// Globe scroll-rotate state
const scrollRotate = ref(0)
const handleScroll = () => {
  scrollRotate.value = window.scrollY * 0.003
}
onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.contact-card-bg-characters {
  --x: 0px;
  --y: 0px;
  --tx: 0px;
  --ty: 0px;
  --scale: 1;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  word-wrap: break-word;
  font-size: 15px;
  line-height: 0.5;
  overflow: hidden;
  font-family: monospace;
  color: #a8a8a8;
  opacity: 0;
  transition: opacity 0.45s cubic-bezier(.2,.9,.3,1);
  will-change: transform, opacity;
  -webkit-mask-image: radial-gradient(
    300px circle at var(--x) var(--y),
    #000 20%,
    rgba(0, 0, 0, 0.25),
    transparent
  );
  mask-image: radial-gradient(
    300px circle at var(--x) var(--y),
    #000 20%,
    rgba(0, 0, 0, 0.25),
    transparent
  );
  transform: translate(var(--tx, 0px), var(--ty, 0px)) scale(var(--scale, 1.025));
  padding: 20px;
  z-index: 2;
  pointer-events: none;
}
.contact-card:hover .contact-card-bg-characters,
.contact-card:active .contact-card-bg-characters {
  opacity: 1;
}

.contact-card {
  background: #fff;
  border-radius: 0;
  padding: 2rem;
  box-shadow: 0 1px 4px 0 #e5e7eb;
  position: relative;
  overflow: hidden;
  border-right: 1px solid #e5e7eb;
  min-width: 320px;
  min-height: 400px;
  flex: 1 1 0%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  transition: box-shadow 0.3s;
}
.contact-card:hover {
  box-shadow: 0 4px 16px 0 #e5e7eb;
}

button[type="button"].ml-1 {
  position: relative;
  overflow: hidden;
  background: transparent;
  color: #848484;
  border: 1px solid #e5e7eb;
  transition: color 300ms, border-color 300ms;
  z-index: 1;
}
button[type="button"].ml-1::before {
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
button[type="button"].ml-1:hover::before,
button[type="button"].ml-1:focus-visible::before {
  transform: translateY(0);
}
button[type="button"].ml-1:hover,
button[type="button"].ml-1:focus-visible {
  color: #fff;
  border-color: #FFCD05;
  outline: none;
}
button[type="button"].ml-1 > span {
  position: relative;
  z-index: 1;
}

/* Mobile improvements for contact cards */
@media (max-width: 767px) {
  /* Stack horizontally-scrolling rows into vertical lists */
  .flex.overflow-x-auto.no-scrollbar {
    flex-direction: column;
    overflow-x: visible;
    overflow-y: visible;
    gap: 0;
    align-items: stretch;
  }

  /* Make each contact card full-width */
  .contact-card {
    min-width: auto;
    width: 100%;
    max-width: 100%;
    margin: 0;
    padding: 2rem;
    min-height: 300px;
    border-right: none;
    border-bottom: 1px solid #e5e7eb;
    border-radius: 0;
    box-shadow: 0 1px 4px 0 #e5e7eb;
  }

  .contact-card h3 {
    font-size: 1.5rem;
    margin-bottom: 0.75rem;
  }

  .contact-card p {
    font-size: 1rem;
    margin-bottom: 0.75rem;
  }

  .contact-card .space-y-2 {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
  }

  .contact-card .flex.items-center.justify-center.gap-2 {
    flex-direction: row;
    gap: 0.5rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  button[type="button"].ml-1 {
    padding: 0.5rem 0.75rem;
    font-size: 13px;
    border-radius: 4px;
  }

  .contact-card-bg-characters {
    font-size: 15px;
    line-height: 0.5;
    padding: 20px;
    -webkit-mask-image: radial-gradient(250px circle at var(--x) var(--y), #000 20%, rgba(0,0,0,0.25), transparent);
    mask-image: radial-gradient(250px circle at var(--x) var(--y), #000 20%, rgba(0,0,0,0.25), transparent);
  }

  .relative.flex.justify-center.items-center.w-full {
    height: 320px !important;
    min-height: 200px !important;
  }

  .absolute.left-1\/2.top-1\/2.z-10 h1 {
    font-size: 2rem !important;
  }
}

/* Tablet (768–1279px): 2-column wrap grid */
@media (min-width: 768px) and (max-width: 1279px) {
  .flex.overflow-x-auto.no-scrollbar .contact-card {
    flex-wrap: wrap !important;
    overflow-x: visible !important;
    width: 50% !important;
    min-width: 0 !important;
    flex: 0 0 50% !important;
  }
}

/* Desktop (1280px+): horizontal scroll row */
@media (min-width: 1280px) {
  .flex.overflow-x-auto.no-scrollbar {
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
  }
}

/* Section title responsive */
@media (max-width: 768px) {
  .grid.grid-cols-6 {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .grid.grid-cols-6 button {
    font-size: 14px;
    padding: 1rem;
  }
}
</style>
