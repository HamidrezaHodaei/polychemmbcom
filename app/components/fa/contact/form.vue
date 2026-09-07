<template>
  <div class="min-h-screen bg-[#f1f2f2] py-16 px-4 font-[IRANYekan]" dir="rtl">
    <div class="max-w-7xl mx-auto">
      <div class="mb-12 text-right">
        <p class="text-sm text-[#848484] mb-3 uppercase tracking-widest"></p>
        <h1 class="text-5xl font-bold text-[#848484] pb-[50px]">فرم تماس</h1>
      </div>

      <div class="space-y-10">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3 font-bold">۱. نام *</label>
            <input 
              type="text" 
              placeholder="کیارش"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#444] placeholder-gray-400 py-3 focus:outline-none"
            />
            <span class="focus-border"></span>
          </div>
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3 font-bold">۲. نام خانوادگی *</label>
            <input 
              type="text" 
              placeholder="منتظری"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#444] placeholder-gray-400 py-3 focus:outline-none"
            />
            <span class="focus-border"></span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3 font-bold">۳. ایمیل *</label>
            <input 
              type="email" 
              dir="ltr"
              placeholder="info@polychemmb.com"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#444] placeholder-gray-400 py-3 focus:outline-none text-right"
            />
            <span class="focus-border"></span>
          </div>
          <div class="relative">
            <label class="block text-sm text-[#848484] mb-3 font-bold">۴. شماره تماس *</label>
            <input 
              type="tel" 
              dir="ltr"
              placeholder="۰۹۱۲۳۴۵۶۷۸۹"
              class="effect-input w-full bg-transparent border-b border-[#848484] text-[#444] placeholder-gray-400 py-3 focus:outline-none text-right"
            />
            <span class="focus-border"></span>
          </div>
        </div>

        <div class="relative">
          <label class="block text-sm text-[#848484] mb-3 font-bold">۵. نام شرکت / مجموعه *</label>
          <input 
            type="text" 
            placeholder="نام تجاری شما..."
            class="effect-input w-full bg-transparent border-b border-[#848484] text-[#444] placeholder-gray-400 py-3 focus:outline-none"
          />
          <span class="focus-border"></span>
        </div>

        <div class="relative">
          <label class="block text-sm text-[#848484] mb-3 font-bold">۶. موضوع پیام *</label>
          <input 
            type="text" 
            placeholder="موضوع درخواست شما..."
            class="effect-input w-full bg-transparent border-b border-[#848484] text-[#444] placeholder-gray-400 py-3 focus:outline-none"
          />
          <span class="focus-border"></span>
        </div>

        <div class="relative">
          <label class="block text-sm text-[#848484] mb-3 font-bold">۷. متن پیام *</label>
          <textarea 
            placeholder="توضیحات خود را اینجا بنویسید..."
            rows="4"
            class="effect-input w-full bg-transparent border-b border-[#848484] text-[#444] placeholder-gray-400 py-3 focus:outline-none resize-none"
          ></textarea>
          <span class="focus-border"></span>
        </div>

        <div class="space-y-4 mt-8">
          <div class="flex items-start gap-3">
            <input 
              type="checkbox" 
              id="privacy" 
              class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]"
            />
            <label for="privacy" class="text-[#848484] text-sm">
              من <span class="underline cursor-pointer font-bold">قوانین و حریم خصوصی</span> را می‌پذیرم *
            </label>
          </div>
          
          <div class="flex items-start gap-3">
            <input 
              type="checkbox" 
              id="consent" 
              class="mt-1 w-5 h-5 border-2 border-[#848484] rounded accent-[#FFCD05]"
            />
            <label for="consent" class="text-[#848484] text-sm">
              با استفاده از داده‌های من جهت پردازش درخواستم توسط پلی‌کم موافقت می‌کنم. *
            </label>
          </div>
        </div>

        <div class="mt-8">
          <button 
            type="button"
            class="btn-slide-down w-full h-14 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors font-bold text-lg"
          >
            <span class="relative z-10">ارسال پیام</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// بخش کشورها حذف شد
</script>

<style scoped>
.font-\[IRANYekan\] {
  font-family: 'IRANYekan', Tahoma, sans-serif;
}

.focus-border {
  position: absolute;
  bottom: 0;
  right: 0; /* تغییر از چپ به راست برای RTL */
  width: 0;
  height: 2px;
  background-color: #FFCD05;
  transition: 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.effect-input:focus ~ .focus-border {
  width: 100%;
}

.btn-slide-down {
  background-color: transparent;
  z-index: 1;
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
  z-index: -1;
}

.btn-slide-down:hover::before {
  transform: translateY(0);
}

.btn-slide-down:hover {
  color: #ffffff;
}
</style>