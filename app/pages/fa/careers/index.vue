<template>
  <!-- ریشهٔ صفحه – flex column برای sticky footer -->  <navbar />
  <div class="flex flex-col min-h-screen bg-[#f1f2f2] font-[IRANYekan]" dir="rtl">

    <!-- Navbar (LTR) -->
  

    <!-- محتوای اصلی -->
    <main class="flex-1 px-4 py-16">
      <div class="max-w-7xl mx-auto">

        <!-- Header -->
        <div class="mb-12 text-right">
          <p class="text-sm text-[#848484] mb-3">فرم درخواست شغل را تکمیل کنید</p>
          <h1 class="text-5xl font-bold text-[#848484] mb-5">درخواست موقعیت شغلی</h1>
        </div>

        <!-- Form -->
        <form class="space-y-8" @submit.prevent="submitForm">
          <!-- First Name & Last Name -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">۱. نام *</label>
              <input v-model="form.name" type="text" placeholder="محمد"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">۲. نام خانوادگی *</label>
              <input v-model="form.lastname" type="text" placeholder="احمدی"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
          </div>

          <!-- Email & Phone -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">۳. ایمیل *</label>
              <input v-model="form.email" type="email" placeholder="example@polychemmb.com"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
            <div class="relative">
              <label class="block text-sm text-[#848484] mb-3">۴. شماره تماس *</label>
              <input v-model="form.phone" type="tel" placeholder="+۹۸ ۲۱ ۲۲۸۹ ۸۹۷۹"
                class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
              <span class="focus-border"></span>
            </div>
          </div>

          <!-- Position -->
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">۵. موقعیت شغلی *</label>
            <input v-model="form.position" type="text" placeholder="مثلاً مهندس شیمی"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
            <span class="focus-border"></span>
          </div>

          <!-- CV Upload -->
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">۶. ارسال رزومه *</label>
            <div class="flex items-center gap-4">
              <input ref="cvInput" @change="handleFileUpload" id="cv" type="file" accept=".pdf,.doc,.docx" class="hidden-file-input" />
              <button type="button" @click="triggerCv"
                class="btn-slide-down file-btn h-12 px-4 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors font-medium">
                <span class="relative z-10">انتخاب فایل</span>
              </button>
              <span class="text-sm text-[#848484] truncate max-w-md" v-if="form.cvName">{{ form.cvName }}</span>
            </div>
            <span class="focus-border"></span>
          </div>

          <!-- Message -->
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">۷. پیام *</label>
            <textarea v-model="form.message" rows="4" placeholder="درباره خود، تجربه و انگیزه خود بنویسید..."
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none resize-none"></textarea>
            <span class="focus-border"></span>
          </div>

          <!-- Checkboxes -->
          <div class="space-y-4 mt-8">
            <div class="flex items-start gap-3">
              <input type="checkbox" id="privacy" required
                class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]" />
              <label for="privacy" class="text-[#848484]">
                من با <span class="underline cursor-pointer">سیاست حفظ حریم خصوصی</span> موافقم *
              </label>
            </div>
            <div class="flex items-start gap-3">
              <input type="checkbox" id="consent" required
                class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]" />
              <label for="consent" class="text-[#848484]">
                اجازه می‌دهم داده‌هایم برای پردازش درخواست توسط POLYCHEM استفاده شود *
              </label>
            </div>
          </div>

          <!-- Submit Button -->
          <div class="mt-10">
            <button type="submit"
              class="btn-slide-down relative w-full h-14 rounded-lg overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] font-medium text-lg transition-all hover:text-white">
              <span class="relative z-10">ارسال درخواست</span>
            </button>
          </div>
        </form>
      </div>
    </main>

    <!-- فوتر full-width -->
    <footer class="w-full">
    </footer>

  </div>
        <footer2 />
      <Chatbox />

</template>

<script setup>
import { ref } from 'vue'
import navbar from '~/components/fa/layout/navbar.vue'
import footer2 from '~/components/fa/layout/footer.vue'
import Chatbox from '~/components/fa/chatbox/chatbox.vue'

const form = ref({
  name: '',
  lastname: '',
  email: '',
  phone: '',
  position: '',
  cv: null,
  cvName: '',
  message: ''
})
useSeoMeta({
  title: 'فرصت‌های همکاری',
  description: 'شرکت پلی‌کم  تولیدکننده و صادرکننده انواع مستربچ رنگی، پرکننده (فیلر)، مستربچ افزودنی و کامپاندهای مهندسی در منطقه آزاد ارس.',
  ogTitle: 'فرصت‌های همکاری',
  ogDescription: 'تولیدکننده پیشرو و صادرکننده مستربچ و کامپاندهای پلیمری در ایران.',
  ogUrl: 'https://polychemmb.com/fa/careers',
  ogType: 'website',
})
const cvInput = ref(null)

const handleFileUpload = (e) => {
  const file = e.target.files && e.target.files[0]
  if (file) {
    form.value.cv = file
    form.value.cvName = file.name
  } else {
    form.value.cv = null
    form.value.cvName = ''
  }
}

const triggerCv = () => {
  if (cvInput.value) cvInput.value.click()
}

const submitForm = () => {
  console.log('Form submitted:', form.value)
  alert('درخواست با موفقیت ارسال شد! (نسخه دمو)')
}
</script>

<style scoped>
/* خطوط زیر input */
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

/* فایل آپلود مخفی */
.hidden-file-input {
  position: absolute !important;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  border: 0;
}

.file-btn {
  min-height: 3rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0 1rem;
}

.file-btn,
.file-btn .relative.z-10 {
  transition: color 200ms;
}
.file-btn:hover,
.file-btn:focus-visible,
.file-btn:hover .relative.z-10,
.file-btn:focus-visible .relative.z-10 {
  color: #ffffff !important;
}

.relative textarea.effect-input ~ .focus-border {
  bottom: 6px;
}
</style>
