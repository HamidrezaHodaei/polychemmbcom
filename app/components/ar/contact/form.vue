<template>
  <div class="min-h-screen bg-[#f1f2f2] py-16 px-4" dir="rtl">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="mb-12">
        <p class="text-sm text-[#848484] mb-3">ملء النموذج</p>
        <h1 class="text-5xl font-bold text-[#848484]">أرسل لنا رسالة</h1>
      </div>

      <!-- Form -->
      <div class="space-y-8">
        <!-- First Name & Last Name Row -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">1. الاسم الأول *</label>
            <input 
              type="text" 
              placeholder="أحمد"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none"
            />
            <span class="focus-border"></span>
          </div>
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">2. اسم العائلة *</label>
            <input 
              type="text" 
              placeholder="محمد"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none"
            />
            <span class="focus-border"></span>
          </div>
        </div>

        <!-- Email & Phone Row -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">3. البريد الإلكتروني *</label>
            <input 
              type="email" 
              placeholder="ahmed@polychemmb.com"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none"
            />
            <span class="focus-border"></span>
          </div>
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3">4. الهاتف *</label>
            <input 
              type="tel" 
              placeholder="+21 2289 8979"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none"
            />
            <span class="focus-border"></span>
          </div>
        </div>

        <!-- Company -->
        <div class="relative">
          <label class="block text-sm text-[#848484] mb-3">5. الشركة *</label>
          <input 
            type="text" 
            placeholder="بولي كيم..."
            class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none"
          />
          <span class="focus-border"></span>
        </div>

        <!-- Country Selection -->
        <div>
          <label class="block text-sm text-[#848484] mb-4">6. اختر الدولة المتأثرة</label>
          <div class="flex flex-wrap gap-3">
            <button
              v-for="(c, idx) in props.countries"
              :key="c + '-' + idx"
              type="button"
              class="btn-slide-down bg-transparent border-2 border-[#FFCD05] text-[#FFCD05] px-6 py-3 rounded-full relative overflow-hidden transition-colors"
            >
              <span class="relative z-10">{{ c }}</span>
            </button>
          </div>
        </div>

        <!-- Object -->
        <div class="relative">
          <label class="block text-sm text-[#848484] mb-3">7. الموضوع *</label>
          <input 
            type="text" 
            placeholder="موضوع رسالتك..."
            class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none"
          />
          <span class="focus-border"></span>
        </div>

        <!-- Message -->
        <div class="relative">
          <label class="block text-sm text-[#848484] mb-3">8. الرسالة *</label>
          <textarea 
            placeholder="قدم جميع المعلومات المفيدة..."
            rows="4"
            class="effect-input w-full bg-transparent border-b border-[#848484] text-[#848484] placeholder-gray-400 py-3 focus:outline-none resize-none"
          ></textarea>
          <span class="focus-border"></span>
        </div>

        <!-- Checkboxes -->
        <div class="space-y-4 mt-8">
          <div class="flex items-start gap-3">
            <input 
              type="checkbox" 
              id="privacy" 
              class="mt-1 w-5 h-5 border-2 border-[#848484] rounded"
            />
            <label for="privacy" class="text-[#848484]">
              أوافق على <span class="underline cursor-pointer">سياسة الخصوصية</span> *
            </label>
          </div>
          
          <div class="flex items-start gap-3">
            <input 
              type="checkbox" 
              id="consent" 
              class="mt-1 w-5 h-5 border-2 border-[#848484] rounded"
            />
            <label for="consent" class="text-[#848484]">
              أوافق على استخدام بياناتي من قبل بولي كيم لمعالجة طلبي. *
            </label>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="mt-8">
          <button 
            type="button"
            class="btn-slide-down w-full h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors font-medium"
          >
            <span class="relative z-10">أرسل الرسالة</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Component logic here if needed
/* receive countries from parent; keep a reasonable fallback */
const props = defineProps({
  countries: {
    type: Array,
    default: () => [
      'France','Estonia','Italy','Spain','Belgium','Canada',
      'United States of America','Mexico','Singapore','United Arab Emirates'
    ]
  }
})
</script>

<style scoped>
.focus-border {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #ffd700;
  transition: 1s;
}

.effect-input:focus ~ .focus-border {
  width: 100%;
  transition: 1s;
}

textarea.effect-input {
  display: block;
}

/* Button slide-down effect (copied from login page for consistency) */
.btn-slide-down {
  background-color: transparent;
  color: #FFCD05;
  border: 2px solid #FFCD05;
  position: relative;
  overflow: hidden;
  transition: color 300ms;
}
.btn-slide-down::before {
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
.btn-slide-down:hover::before,
.btn-slide-down:focus-visible::before {
  transform: translateY(0);
}
.btn-slide-down:hover,
.btn-slide-down:focus-visible {
  color: #ffffff;
  outline: none;
}
.btn-slide-down > .relative.z-10 {
  position: relative;
  z-index: 10;
}
</style>