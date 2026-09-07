<template>
  <!-- ریشهٔ صفحه – flex column برای sticky footer -->
  <div class="flex flex-col min-h-screen bg-[#f1f2f2]">

    <!-- Navbar -->
    <navbar />

    <!-- محتوای اصلی (فقط این بخش محدودیت عرض داره) -->
    <main class="flex-1 px-4 py-16">
      <div class="max-w-7xl mx-auto">

   <!-- Header -->
<div class="mb-12">
  <p class="text-sm text-[#848484] mb-3">FORMU DOLDURUN</p>
  <h1 class="text-5xl font-bold text-[#848484]">Pozisyon için başvur</h1>
</div>

<!-- Form -->
<form class="space-y-8" @submit.prevent="submitForm">
  <!-- First Name & Last Name -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="relative">
      <label class="block text-sm text-[#848484] mb-3">1. AD </label>
      <input v-model="form.name" type="text" placeholder="John"
        class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
      <span class="focus-border"></span>
    </div>
    <div class="relative">
      <label class="block text-sm text-[#848484] mb-3">2. SOYAD </label>
      <input v-model="form.lastname" type="text" placeholder="Doe"
        class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
      <span class="focus-border"></span>
    </div>
  </div>

  <!-- Email & Phone -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="relative">
      <label class="block text-sm text-[#848484] mb-3">3. E-POSTA </label>
      <input v-model="form.email" type="email" placeholder="johndoe@polychemmb.com"
        class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
      <span class="focus-border"></span>
    </div>
    <div class="relative">
      <label class="block text-sm text-[#848484] mb-3">4. TELEFON </label>
      <input v-model="form.phone" type="tel" placeholder="+90 21 2289 8979..."
        class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
      <span class="focus-border"></span>
    </div>
  </div>

  <!-- Position -->
  <div class="relative">
    <label class="block text-sm text-[#848484] mb-3">5. POZİSYON </label>
    <input v-model="form.position" type="text" placeholder="örn. Kimya Mühendisi"
      class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none" />
    <span class="focus-border"></span>
  </div>

  <!-- CV Upload -->
  <div class="relative">
    <label class="block text-sm text-[#848484] mb-3">6. ÖZGEÇMİŞ YÜKLE </label>
    <div class="flex items-center gap-4">
      <input ref="cvInput" @change="handleFileUpload" id="cv" type="file" accept=".pdf,.doc,.docx" class="hidden-file-input" />
      <button type="button" @click="triggerCv"
        class="btn-slide-down file-btn h-12 px-4 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors font-medium">
        <span class="relative z-10">DOSYA SEÇ</span>
      </button>
      <span class="text-sm text-[#848484] truncate max-w-md" v-if="form.cvName">{{ form.cvName }}</span>
    </div>
    <span class="focus-border"></span>
  </div>

  <!-- Message -->
  <div class="relative">
    <label class="block text-sm text-[#848484] mb-3">7. MESAJ </label>
    <textarea v-model="form.message" rows="4" placeholder="Kendinizden, deneyimlerinizden ve motivasyonunuzdan bahsedin..."
      class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none resize-none"></textarea>
    <span class="focus-border"></span>
  </div>

     
  <!-- Checkboxes -->
  <div class="space-y-4 mt-8">
    <div class="flex items-start gap-3">
      <input type="checkbox" id="privacy" required
        class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]" />
      <label for="privacy" class="text-[#848484]">
        Gizlilik politikasını kabul ediyorum <span class="underline cursor-pointer"></span>
      </label>
    </div>
    <div class="flex items-start gap-3">
      <input type="checkbox" id="consent" required
        class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]" />
      <label for="consent" class="text-[#848484]">
        Başvurumun işlenmesi için verilerimin POLYCHEM tarafından kullanılmasına izin veriyorum. *
      </label>
    </div>
  </div>

  <!-- Submit Button -->
  <div class="mt-10">
    <button type="submit"
      class="btn-slide-down relative w-full h-14 rounded-lg overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] font-medium text-lg transition-all hover:text-white">
      <span class="relative z-10">Başvuruyu Gönder</span>
    </button>
  </div>
</form>
      </div>
    </main>

    <!-- فوتر کاملاً full-width و بدون هیچ padding یا محدودیت -->
    <footer class="w-full">
      <Chatbox />
      <footer2 />
    </footer>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import navbar from '~/components/tr/layout/navbar.vue'
import footer2 from '~/components/tr/layout/footer.vue'
import Chatbox from '~/components/tr/chatbox/chatbox.vue'

const form = ref({
  name: '',
  lastname: '',
  email: '',
  phone: '',
  position: '',
  cv: null,
  cvName: '',       // <-- added to store displayed filename
  message: ''
})

const cvInput = ref(null) // ref to trigger hidden input

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
  alert('Application submitted successfully! (Demo)')
  // اینجا می‌تونی API کال کنی
}
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

/* keep native file input hidden but accessible */
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

/* keep file button visually consistent with submit button without changing layout size */
.file-btn {
  /* ensure same vertical size as other inputs/buttons */
  min-height: 3rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding-left: 1rem;
  padding-right: 1rem;
}

/* ensure the visible file button text becomes white on hover/focus */
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

/* ensure the animated underline sits on the input's bottom edge for textarea */
.relative textarea.effect-input ~ .focus-border {
  bottom: 6px; /* nudges the underline to align with textarea border */
}

/* small tweak: underline height */
.focus-border {
  height: 2px; /* slightly thicker for better visibility and alignment */
}
</style>