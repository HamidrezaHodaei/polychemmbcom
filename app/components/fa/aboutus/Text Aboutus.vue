<!-- /components/fa/aboutus/Text Aboutus.vue -->
<template>
  <main class="text-main w-full bg-[#f1f2f2] " dir="rtl">
    <div class="inner">

      <!-- متن برند -->
      <p class="brand-text font-[IRANYekan] font-bold text-[#848484]">
        شرکت پلیمر‌شیمی‌ارس چشم‌اندازی از
      </p>
      <!-- باکس انیمیشنی -->
      <div class="slide-wrapper overflow-hidden flex-shrink-0">
        <div class="animate-slide font-[IRANYekan]">
          <div class="box font-[IRANYekan]">نوآوری</div>
          <div class="box font-[IRANYekan]">فناوری</div>
          <div class="box font-[IRANYekan]">وفاداری</div>
          <div class="box font-[IRANYekan]">شایستگی</div>
          <div class="box font-[IRANYekan]">خلاقیت</div>
          <div class="box font-[IRANYekan]">صداقت</div>
          <div class="box font-[IRANYekan]">کیفیت</div>
          <div class="box font-[IRANYekan]">اصالت</div>
        </div>
      </div>


    </div>
  </main>
</template>

<style scoped>
* { box-sizing: border-box; }

.text-main {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2.5rem 1.5rem;
  min-height: 20vh;
}

.inner {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  width: 100%;
  max-width: 1100px;
  flex-wrap: wrap;
}

/* ===== SLIDE BOX ===== */
.slide-wrapper { height: 64px; }

.box {
  height: 64px;
  background: #FFD700;
  color: white;
  font-weight: 800;
  font-size: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 2rem;
  white-space: nowrap;
}

/* ===== BRAND TEXT ===== */
.brand-text {
  font-size: clamp(18px, 4vw, 50px);
  font-weight: 700;
  text-align: center;
  line-height: 1.3;
}

/* ===== ANIMATION ===== */
.animate-slide { animation: slide-d 21s infinite linear; }

@keyframes slide-d {
  0%, 11%      { transform: translateY(0); }
  12.5%, 23.5% { transform: translateY(-64px); }
  25%, 36%     { transform: translateY(-128px); }
  37.5%, 48.5% { transform: translateY(-192px); }
  50%, 61%     { transform: translateY(-256px); }
  62.5%, 73.5% { transform: translateY(-320px); }
  75%, 86%     { transform: translateY(-384px); }
  87.5%, 98.5% { transform: translateY(-448px); }
  100%         { transform: translateY(0); }
}

/* ===== TABLET (≤ 768px) ===== */
@media (max-width: 768px) {
  .text-main { padding: 2rem 1rem; min-height: 15vh; }
  .slide-wrapper { height: 50px; }
  .box { height: 50px; font-size: 32px; padding: 0 1.25rem; }
  .animate-slide { animation-name: slide-t; }

  @keyframes slide-t {
    0%, 11%      { transform: translateY(0); }
    12.5%, 23.5% { transform: translateY(-50px); }
    25%, 36%     { transform: translateY(-100px); }
    37.5%, 48.5% { transform: translateY(-150px); }
    50%, 61%     { transform: translateY(-200px); }
    62.5%, 73.5% { transform: translateY(-250px); }
    75%, 86%     { transform: translateY(-300px); }
    87.5%, 98.5% { transform: translateY(-350px); }
    100%         { transform: translateY(0); }
  }
}

/* ===== MOBILE (≤ 480px) ===== */
@media (max-width: 480px) {
  .text-main { padding: 1.5rem 1rem 2rem; min-height: auto; }

  /* باکس روی، متن زیر */
  .inner {
    flex-direction: column;
    gap: 10px;
    align-items: center;
    text-align: center;
  }

  .slide-wrapper { height: 44px; }

  .box {
    height: 44px;
    font-size: 26px;
    padding: 0 1.25rem;
  }

  .brand-text {
    font-size: clamp(15px, 5vw, 21px);
    text-align: center;
  }

  .animate-slide { animation-name: slide-m; }

  @keyframes slide-m {
    0%, 11%      { transform: translateY(0); }
    12.5%, 23.5% { transform: translateY(-44px); }
    25%, 36%     { transform: translateY(-88px); }
    37.5%, 48.5% { transform: translateY(-132px); }
    50%, 61%     { transform: translateY(-176px); }
    62.5%, 73.5% { transform: translateY(-220px); }
    75%, 86%     { transform: translateY(-264px); }
    87.5%, 98.5% { transform: translateY(-308px); }
    100%         { transform: translateY(0); }
  }
}
</style>