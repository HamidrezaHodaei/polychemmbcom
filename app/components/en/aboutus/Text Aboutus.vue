<template>
  <section class="w-full bg-[#f1f2f2] flex items-center justify-center px-4 py-8">
    <div class="flex flex-col sm:flex-row items-center justify-center text-center sm:text-left gap-6 sm:gap-8 w-full max-w-[1200px]">

      <!-- متن ثابت - همه در یک خط (responsive مثل Text.vue) -->
      <p class="font-bold text-[#848484] uppercase flex flex-wrap sm:flex-nowrap items-center justify-center sm:justify-start">
      
        <span class="brand-rest">Where every grain of polymer becomes</span>
      </p>

      <!-- باکس انیمیشنی -->
      <div class="h-12 sm:h-[60px] overflow-hidden flex-shrink-0">
        <div class="animate-slide">
          <div class="box">Polymer Art</div>
          <div class="box">Originality</div>
          <div class="box">Loyalty</div>
          <div class="box">Creativity</div>
          <div class="box">Honesty</div>
          <div class="box">Elegance</div>
          <div class="box">Meaningful</div>
          <div class="box">Polymer Art</div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&display=swap');

* {
  font-family: 'Montserrat', sans-serif;
}

/* Polychem برند اصلی */
.brand {
  font-weight: 800;
  font-size: clamp(32px, 7vw, 45px);
  letter-spacing: 0.05em;
  white-space: nowrap;
  display: inline-block;
  vertical-align: middle;
}

/* خط تیره جدا‌کننده */
.brand-separator {
  font-weight: 700;
  font-size: clamp(24px, 5vw, 36px);
  margin: 0 clamp(0.3rem, 2vw, 0.6rem);
  opacity: 0.9;
  vertical-align: middle;
  display: inline-block;
}

/* متن ادامه‌دهنده */
.brand-rest {
  font-weight: 700;
  font-size: clamp(15px, 4vw, 35px);
  white-space: nowrap;
  display: inline-block;
  vertical-align: middle;
  max-width: 100%;
}

/* باکس‌های زرد با انیمیشن */
.box {
  height: 64px;
  background: #FFD700;
  color: white;
  font-weight: 700;
  font-size: clamp(15px, 5vw, 35px);
  text-transform: uppercase;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 clamp(1rem, 3vw, 2rem);
  white-space: nowrap;
}

/* انیمیشن روان */
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

/* موبایل: تنظیمات برای قرارگیری داخل کادر و خوانایی */
@media (max-width: 640px) {
  section {
    padding: 1.5rem 1rem;
  }

  .brand {
    font-size: clamp(28px, 8vw, 36px);
  }

  .brand-separator {
    display: none;
  }

  .box {
    height: 48px;
    font-size: clamp(18px, 4.5vw, 32px);
    padding: 0 1rem;
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

/* تبلت و بالاتر */
@media (min-width: 641px) {
  section {
    min-height: auto;
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

/* اکسترا لارج */
@media (min-width: 1024px) {
  section {
    padding: 2rem 2rem;
  }
}
</style>