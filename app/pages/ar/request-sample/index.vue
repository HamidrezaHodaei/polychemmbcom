<template>
   <!-- Navbar -->
    <navbar />
  <!-- ریشهٔ صفحه – flex column برای sticky footer -->
  <div class="flex flex-col min-h-screen bg-[#f1f2f2] font-[IRANYekan]" dir="rtl">



    <!-- محتوای اصلی -->
    <main class="flex-1 px-4 py-16">
      <div class="max-w-7xl mx-auto font-[IRANYekan]">

        <!-- Header -->
        <div class="mb-12">
          <p class="text-sm text-[#848484] mb-3">تعبئة الاستمارة</p>
          <h1 class="text-5xl font-bold text-[#848484]">طلب عينة</h1>
        </div>

        <!-- Form -->
        <form class="space-y-8 font-[IRANYekan]" @submit.prevent="submitForm">
          <!-- First Name & Last Name -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">١. الاسم *</label>
              <input v-model="form.name" type="text" placeholder="مثلاً: أحمد"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none text-right" />
              <span class="focus-border"></span>
            </div>
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">٢. اللقب *</label>
              <input v-model="form.lastname" type="text" placeholder="مثلاً: العبيدي"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none text-right" />
              <span class="focus-border"></span>
            </div>
          </div>

          <!-- Company & Country -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">٣. اسم الشركة *</label>
              <input v-model="form.company" type="text" placeholder="اسم شركتك"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none text-right" />
              <span class="focus-border"></span>
            </div>
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">٤. البلد *</label>
              <input v-model="form.country" type="text" placeholder="مثلاً: العراق"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none text-right" />
              <span class="focus-border"></span>
            </div>
          </div>

          <!-- Email & Phone -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">٥. الإيميل *</label>
              <input v-model="form.email" type="email" placeholder="AhmedAli@Polychemmb.com"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none text-left" dir="ltr" />
              <span class="focus-border"></span>
            </div>
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">٦. رقم الهاتف *</label>
              <input v-model="form.phone" type="tel" placeholder="+964 770 123 4567..."
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none text-left" dir="ltr" />
              <span class="focus-border"></span>
            </div>
          </div>

          <!-- Industry & Requested Product -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Industry (simple custom dropdown) -->
            <div class="relative" v-click-outside="() => (industryOpen = false)">
              <label class="block text-sm text-[#848484] mb-3">٧. الصناعة *</label>
              <button type="button" @click="industryOpen = !industryOpen"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-right py-3 focus:outline-none flex items-center justify-between"
                :class="form.industry ? 'text-[#848484]' : 'text-gray-400'">
                <span>{{ form.industry || 'اختر الصناعة' }}</span>
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
              <label class="block text-sm text-[#848484] mb-3">٨. المنتج المطلوب *</label>
              <button type="button" @click="productOpen = !productOpen"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-right py-3 focus:outline-none flex items-center justify-between"
                :class="form.product ? 'text-[#848484]' : 'text-gray-400'">
                <span>{{ form.product || 'اختر المنتج' }}</span>
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
            <label class="block text-sm text-[#848484] mb-3">٩. الكمية المطلوبة</label>
            <input v-model="form.quantity" type="text" placeholder="مثلاً: عينة ٢٥ كيلوغرام"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none text-right" />
            <span class="focus-border"></span>
          </div>

          <!-- Message -->
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">١٠. الرسالة</label>
            <textarea v-model="form.message" rows="4" placeholder="نرجو وصف طريقة الاستخدام، الهدف من الطلب، والمتطلبات الفنية اللي تريدها..."
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none resize-none text-right"></textarea>
            <span class="focus-border"></span>
          </div>

          <!-- Checkboxes -->
          <div class="space-y-4 mt-8">
            <div class="flex items-start gap-3">
              <input type="checkbox" id="privacy" required
                class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]" />
              <label for="privacy" class="text-[#848484]">
                أوافق على <span class="underline cursor-pointer">سياسة الخصوصية</span> *
              </label>
            </div>
            <div class="flex items-start gap-3">
              <input type="checkbox" id="consent" required
                class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]" />
              <label for="consent" class="text-[#848484]">
                أوافق على استخدام بياناتي من قبل بولي كيم لمعالجة طلب العينة. *
              </label>
            </div>
          </div>

          <!-- Submit Button -->
          <div class="mt-10">
            <button type="submit"
              class="btn-slide-down relative w-full h-14 rounded-lg overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] font-medium text-lg transition-all hover:text-white">
              <span class="relative z-10">إرسال الطلب</span>
            </button>
          </div>
        </form>
      </div>
    </main>

    <!-- فوتر کاملاً full-width -->
    <footer class="w-full">

    </footer>

  </div>
   <footer2 />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useLang } from '~/composables/useLang'
import navbar from '~/components/ar/layout/navbar.vue'
import footer2 from '~/components/ar/layout/footer.vue'

const router = useRouter()
const { switchLang, currentLang } = useLang()

// Ensure page is mounted properly
onMounted(() => {
  console.log('Request sample page mounted')
})

const goToProducts = () => {
  const lang = currentLang.value || 'ar'
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

// TODO: replace with your actual industry categories
const industries = [
  'التعبئة والتغليف',
  'السيارات',
  'الأسلاك والكابلات',
  'الأنابيب والوصلات',
  'الزراعة',
  'البناء',
  'الأجهزة المنزلية',
  'النسيج',
  'أخرى',
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
  console.log('Sample request submitted:', form.value)
  alert('تم إرسال طلب العينة بنجاح! (نسخة تجريبية)')
  // اینجا می‌تونی API کال کنی
}

useSeoMeta({
  title: 'طلب عينة | بولي كيم',
  description: 'اطلب عينة من منتجات بولي كيم. تصفح مجموعتنا من الماستر باتش والإضافات والمركبات البوليمرية.',
  ogTitle: 'طلب عينة | بولي كيم',
  ogDescription: 'اطلب عينة مجانية من منتجاتنا وتعرّف على حلول بولي كيم المتقدمة في مجال المركبات البوليمرية.',
  ogUrl: 'https://polychemmb.com/ar/request-sample',
  ogType: 'website',
})
</script>

<style scoped>
/* انیمیشن خط زیر اینپوت‌ها */
.focus-border {
  @apply absolute bottom-0 right-0 w-0 h-0.5 bg-[#FFCD05] transition-all duration-700;
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
  @apply absolute right-0 left-0 mt-1 bg-white border border-[#e5e5e5] rounded-md max-h-60 overflow-y-auto z-20;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
}
.simple-dropdown-item {
  @apply px-4 py-2 text-sm text-[#848484] cursor-pointer transition-colors text-right;
}
.simple-dropdown-item:hover {
  @apply bg-[#FFCD05]/10 text-[#1a1a1a];
}

/* ensure the animated underline sits on the input's bottom edge for textarea */
.relative textarea.effect-input ~ .focus-border {
  bottom: 6px;
}
</style>