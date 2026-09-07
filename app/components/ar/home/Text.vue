<template>
  <main class="w-full bg-[#f1f2f2] flex items-center justify-center px-4 font-[Tajawal]" style="min-height: 100vh; direction: rtl;" dir="rtl">
    <div class="flex flex-col sm:flex-row items-center justify-center text-center sm:text-right gap-6 sm:gap-8 w-full py-8 sm:py-0">

<!-- النص الثابت - جميعه في سطر واحد -->
<p class="font-bold text-[#848484] flex flex-wrap sm:flex-nowrap items-center justify-center sm:justify-end" style="font-family: 'Tajawal', sans-serif;">
  <span class="brand"> پلیمرشیمی‌ارس</span>

  <span class="brand-rest" style="font-family: 'Tajawal', sans-serif;">المكان الذي يتحول فيه كل بوليمر</span>
</p>

<!-- صندوق الكلمات المتحركة -->
<div class="h-12 sm:h-[60px] overflow-hidden flex-shrink-0">
  <div class="animate-slide">
    <div class="box" style="font-family: 'Tajawal', sans-serif;">فن البوليمر</div>
    <div class="box" style="font-family: 'Tajawal', sans-serif;">الأصالة</div>
    <div class="box" style="font-family: 'Tajawal', sans-serif;">الولاء</div>
    <div class="box" style="font-family: 'Tajawal', sans-serif;">الإبداع</div>
    <div class="box" style="font-family: 'Tajawal', sans-serif;">الصدق</div>
    <div class="box" style="font-family: 'Tajawal', sans-serif;">الأناقة</div>
    <div class="box" style="font-family: 'Tajawal', sans-serif;">المعنى</div>
    <div class="box" style="font-family: 'Tajawal', sans-serif;">فن البوليمر</div>
  </div>
</div>
</div>
</main>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&display=swap');

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-200.ttf') format('truetype');
  font-weight: 200;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-300.ttf') format('truetype');
  font-weight: 300;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-400.ttf') format('truetype');
  font-weight: 400;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-500.ttf') format('truetype');
  font-weight: 500;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-700.ttf') format('truetype');
  font-weight: 700;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-800.ttf') format('truetype');
  font-weight: 800;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-900.ttf') format('truetype');
  font-weight: 900;
}

* {
  font-family: 'Tajawal', sans-serif;
}

/* Polychem العلامة التجارية */
.brand {
  font-weight: 700;
  font-size: clamp(24px, 5vw, 35px);
  white-space: nowrap;
  display: inline-block;
  vertical-align: middle;
  font-family: 'Tajawal', sans-serif;
}

/* الخط الفاصل الغامق */
.brand-separator {
  font-weight: 700;
  font-size: clamp(24px, 5vw, 36px);
  margin: 0 clamp(0.3rem, 2vw, 0.6rem);
  opacity: 0.9;
  vertical-align: middle;
  display: inline-block;
  font-family: 'Montserrat', sans-serif;
}

/* النص الوصفي */
.brand-rest {
  font-weight: 700;
  font-size: clamp(24px, 5vw, 35px);
  white-space: normal;
  display: inline-block;
  vertical-align: middle;
  max-width: 100%;
  font-family: 'Tajawal', sans-serif;
}

/* الصناديق الصفراء مع الحركة */
.box {
  height: 64px;
  background: #FFD700;
  color: white;
  font-weight: 800;
  font-size: clamp(20px, 4vw, 45px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 clamp(1rem, 3vw, 2rem);
  white-space: nowrap;
  font-family: 'Tajawal', sans-serif;
}

/* الحركة السلسة */
.animate-slide {
  animation: slide 21s infinite linear;
}

@keyframes slide {
  0%, 11%    { transform: translateY(0); }
  12.5%, 23.5% { transform: translateY(-64px); }
  25%, 36%   { transform: translateY(-128px); }
  37.5%, 48.5% { transform: translateY(-192px); }
  50%, 61%   { transform: translateY(-256px); }
  62.5%, 73.5% { transform: translateY(-320px); }
  75%, 86%   { transform: translateY(-384px); }
  87.5%, 98.5% { transform: translateY(-448px); }
  100%       { transform: translateY(0); }
}

/* الهاتف المحمول */
@media (max-width: 640px) {
  main {
    min-height: auto;
    padding: 2rem 1rem;
  }

  .brand {
    font-size: clamp(28px, 7vw, 36px);
  }

  .brand-rest {
    font-size: clamp(28px, 7vw, 36px);
  }

  .brand-separator {
    display: none;
  }

  .box {
    height: 48px;
    font-size: clamp(28px, 7vw, 36px);
  }

  @keyframes slide {
    0%, 11%    { transform: translateY(0); }
    12.5%, 23.5% { transform: translateY(-48px); }
    25%, 36%   { transform: translateY(-96px); }
    37.5%, 48.5% { transform: translateY(-144px); }
    50%, 61%   { transform: translateY(-192px); }
    62.5%, 73.5% { transform: translateY(-240px); }
    75%, 86%   { transform: translateY(-288px); }
    87.5%, 98.5% { transform: translateY(-336px); }
    100%       { transform: translateY(0); }
  }
}

/* الأجهزة اللوحية والشاشات الأكبر */
@media (min-width: 641px) {
  main {
    min-height: screen;
  }

  .box {
    height: 60px;
  }

  @keyframes slide {
    0%, 11%    { transform: translateY(0); }
    12.5%, 23.5% { transform: translateY(-60px); }
    25%, 36%   { transform: translateY(-120px); }
    37.5%, 48.5% { transform: translateY(-180px); }
    50%, 61%   { transform: translateY(-240px); }
    62.5%, 73.5% { transform: translateY(-300px); }
    75%, 86%   { transform: translateY(-360px); }
    87.5%, 98.5% { transform: translateY(-420px); }
    100%       { transform: translateY(0); }
  }
}

/* الشاشات الكبيرة جداً */
@media (min-width: 1024px) {
  main {
    min-height: screen;
    padding: 4rem 2rem;
  }
}
</style>