<template>
  <!-- ریشهٔ صفحه – flex column برای sticky footer -->
  <div class="flex flex-col min-h-screen bg-[#f1f2f2]">

    <!-- Navbar -->
    <navbar />

    <!-- محتوای اصلی -->
    <main class="flex-1 px-4 py-16">
      <div class="max-w-7xl mx-auto">

        <!-- Header -->
        <div class="mb-12">
          <p class="text-sm text-[#848484] mb-3">FORMU DOLDURUN</p>
          <h1 class="text-5xl font-bold text-[#848484]">Numune Talep Edin</h1>
        </div>

        <!-- Form -->
        <form class="space-y-8" @submit.prevent="submitForm">
          <!-- First Name & Last Name -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">1. AD *</label>
              <input v-model="form.name" type="text" placeholder="Ahmet"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">2. SOYAD *</label>
              <input v-model="form.lastname" type="text" placeholder="Yılmaz"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
          </div>

          <!-- Company & Country -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">3. ŞİRKET *</label>
              <input v-model="form.company" type="text" placeholder="Şirket adınız"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">4. ÜLKE *</label>
              <input v-model="form.country" type="text" placeholder="örn. Türkiye"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
          </div>

          <!-- Email & Phone -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">5. E-POSTA *</label>
              <input v-model="form.email" type="email" placeholder="ahmetyilmaz@Polychemmb.com"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">6. TELEFON *</label>
              <input v-model="form.phone" type="tel" placeholder="+90 212 000 00 00..."
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
          </div>

          <!-- Industry & Requested Product -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Industry (simple custom dropdown) -->
            <div class="relative" v-click-outside="() => (industryOpen = false)">
              <label class="block text-sm text-[#848484] mb-3">7. SEKTÖR *</label>
              <button type="button" @click="industryOpen = !industryOpen"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-left py-3 focus:outline-none flex items-center justify-between"
                :class="form.industry ? 'text-[#848484]' : 'text-gray-400'">
                <span>{{ form.industry || 'Bir sektör seçin' }}</span>
                <span class="dropdown-arrow" :class="{ 'rotate-180': industryOpen }">⌄</span>
              </button>
              <span class="focus-border" :class="{ 'w-full': industryOpen }"></span>

              <ul v-if="industryOpen" class="simple-dropdown">
                <li v-for="ind in industries" :key="ind"
                  @click="form.industry = ind; industryOpen = false"
                  class="simple-dropdown-item">
                  {{ ind }}
                </li>
              </ul>
            </div>

            <!-- Requested Product (simple custom dropdown) -->
            <div class="relative" v-click-outside="() => (productOpen = false)">
              <label class="block text-sm text-[#848484] mb-3">8. TALEP EDİLEN ÜRÜN *</label>
              <button type="button" @click="productOpen = !productOpen"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-left py-3 focus:outline-none flex items-center justify-between"
                :class="form.product ? 'text-[#848484]' : 'text-gray-400'">
                <span>{{ form.product || 'Bir ürün seçin' }}</span>
                <span class="dropdown-arrow" :class="{ 'rotate-180': productOpen }">⌄</span>
              </button>
              <span class="focus-border" :class="{ 'w-full': productOpen }"></span>

              <ul v-if="productOpen" class="simple-dropdown">
                <li v-for="p in products" :key="p.index"
                  @click="form.product = p.title; productOpen = false"
                  class="simple-dropdown-item">
                  {{ p.title }}
                </li>
              </ul>
            </div>
          </div>

          <!-- Quantity -->
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">9. GEREKLİ MİKTAR</label>
            <input v-model="form.quantity" type="text" placeholder="örn. 25 kg numune"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
            <span class="focus-border"></span>
          </div>

          <!-- Message -->
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">10. MESAJ</label>
            <textarea v-model="form.message" rows="4" placeholder="Uygulamanız, kullanım amacınız ve teknik gereksinimleriniz hakkında bize bilgi verin..."
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none resize-none"></textarea>
            <span class="focus-border"></span>
          </div>

          <!-- Checkboxes -->
          <div class="space-y-4 mt-8">
            <div class="flex items-start gap-3">
              <input type="checkbox" id="privacy" required
                class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]" />
              <label for="privacy" class="text-[#848484]">
                <span class="underline cursor-pointer">Gizlilik politikasını</span> kabul ediyorum *
              </label>
            </div>
            <div class="flex items-start gap-3">
              <input type="checkbox" id="consent" required
                class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]" />
              <label for="consent" class="text-[#848484]">
                Verilerimin POLYCHEM tarafından numune talebimin işlenmesi amacıyla kullanılmasına izin veriyorum. *
              </label>
            </div>
          </div>

          <!-- Submit Button -->
          <div class="mt-10">
            <button type="submit"
              class="btn-slide-down relative w-full h-14 rounded-lg overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] font-medium text-lg transition-all hover:text-white">
              <span class="relative z-10">Talebi Gönder</span>
            </button>
          </div>
        </form>
      </div>
    </main>

    <!-- فوتر کاملاً full-width -->
    <footer class="w-full">
      <footer2 />
    </footer>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useLang } from '~/composables/useLang'
import navbar from '~/components/tr/layout/navbar.vue'
import footer2 from '~/components/tr/layout/footer.vue'

const router = useRouter()
const { switchLang, currentLang } = useLang()

// Ensure page is mounted properly
onMounted(() => {
  console.log('Numune talep sayfası yüklendi')
})

const goToProducts = () => {
  const lang = currentLang.value || 'tr'
  router.push(`/${lang}/products`)
}

const products = [
  { title: 'ROTOCHEM 0955W', index: 0 },
  { title: 'ROTOCHEM 0955B', index: 1 },
  { title: 'POLYFIL F700', index: 2 },
  { title: 'POLYFIL 1300 EWA', index: 3 },
  { title: 'HDCHEM 4760', index: 4 },
  { title: 'SLIPCHEM E 178', index: 5 },
  { title: 'RAFCOLOR 1560', index: 6 },
  { title: 'CALCICHEM 126 FP', index: 7 },
  { title: 'CALCICHEM 110 FRF', index: 8 },
  { title: 'CALCICHEM 275 PM', index: 9 },
  { title: 'UVCHEM MB-R18', index: 10 },
]

// TODO: gerçek sektör kategorilerinizle değiştirin
const industries = [
  'Ambalaj',
  'Otomotiv',
  'Kablo & Tel',
  'Boru & Bağlantı Elemanları',
  'Tarım',
  'İnşaat',
  'Ev Aletleri',
  'Tekstil',
  'Diğer',
]

const form = ref({
  name: '',
  lastname: '',
  company: '',
  country: '',
  email: '',
  phone: '',
  industry: '',
  product: '',
  quantity: '',
  message: ''
})

const industryOpen = ref(false)
const productOpen = ref(false)

// minimal click-outside directive so dropdowns close on outside click
const vClickOutside = {
  mounted(el, binding) {
    el.__clickOutsideHandler = (e) => {
      if (!(el === e.target || el.contains(e.target))) binding.value(e)
    }
    document.addEventListener('click', el.__clickOutsideHandler, true)
  },
  unmounted(el) {
    document.removeEventListener('click', el.__clickOutsideHandler, true)
  }
}

const submitForm = () => {
  console.log('Numune talebi gönderildi:', form.value)
  alert('Numune talebiniz başarıyla gönderildi! (Demo)')
  // اینجا می‌تونی API کال کنی
}

useSeoMeta({
  title: 'Numune Talep Edin | POLYCHEM',
  description: 'POLYCHEM\'den ürün numunesi talep edin. Masterbatch, katkı maddesi ve polimer bileşik çözümlerimizi keşfedin.',
  ogTitle: 'Numune Talep Edin | POLYCHEM',
  ogDescription: 'Ücretsiz ürün numunesi talep edin ve POLYCHEM\'in gelişmiş polimer bileşik çözümlerini keşfedin.',
  ogUrl: 'https://polychemmb.com/tr/request-sample',
  ogType: 'website',
})
</script>

<style scoped>
/* انیمیشن خط زیر اینپوت‌ها */
.focus-border {
  @apply absolute bottom-0 left-0 w-0 h-0.5 bg-[#FFCD05] transition-all duration-700;
}
.effect-input:focus ~ .focus-border {
  @apply w-full;
}

/* دکمه slide-down زرد */
.btn-slide-down::before {
  content: '';
  @apply absolute inset-0 bg-[#FFCD05] -translate-y-full transition-transform duration-300;
}
.btn-slide-down:hover::before,
.btn-slide-down:focus-visible::before {
  @apply translate-y-0;
}

/* small tweak: underline height */
.focus-border {
  height: 2px;
}

/* simple dropdown arrow */
.dropdown-arrow {
  @apply text-[#848484] transition-transform duration-300 text-lg leading-none;
}

/* simple dropdown panel */
.simple-dropdown {
  @apply absolute left-0 right-0 mt-1 bg-white border border-[#e5e5e5] rounded-md max-h-60 overflow-y-auto z-20;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
}
.simple-dropdown-item {
  @apply px-4 py-2 text-sm text-[#848484] cursor-pointer transition-colors;
}
.simple-dropdown-item:hover {
  @apply bg-[#FFCD05]/10 text-[#1a1a1a];
}

/* ensure the animated underline sits on the input's bottom edge for textarea */
.relative textarea.effect-input ~ .focus-border {
  bottom: 6px;
}
</style>