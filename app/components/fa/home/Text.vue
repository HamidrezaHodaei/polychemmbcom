<template>
  <main class="w-full bg-[#f1f2f2] flex items-center justify-center px-4" style="min-height: 100vh;">
    <div class="flex flex-col items-center justify-center text-center gap-4 sm:gap-6 md:gap-6 lg:flex-row lg:text-left w-full py-8 max-w-7xl">

      <p class="font-bold text-[#848484] uppercase flex flex-wrap items-center justify-center lg:justify-start order-1 lg:order-2">
        <span class="brand-rest font-[IRANYekan]">شرکت پلیمر‌شیمی‌ارس چشم‌اندازی از </span>
      </p>

      <div class="h-[50px] sm:h-[55px] md:h-[52px] lg:h-[60px] overflow-hidden flex-shrink-0 order-2 lg:order-1">
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
.brand-rest {
  font-weight: 700;
  font-size: clamp(28px, 5vw, 50px);
  white-space: normal;
  display: inline-block;
  vertical-align: middle;
  max-width: 100%;
  line-height: 1.3;
}

.box {
  background: #FFD700;
  color: white;
  font-weight: 800;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
  height: 50px;
  font-size: 32px;
  padding: 0 1.5rem;
}

.animate-slide {
  animation: slide-mobile 21s infinite linear;
}

@keyframes slide-mobile {
  0%, 11%    { transform: translateY(0); }
  12.5%, 23.5% { transform: translateY(-50px); }
  25%, 36%   { transform: translateY(-100px); }
  37.5%, 48.5% { transform: translateY(-150px); }
  50%, 61%   { transform: translateY(-200px); }
  62.5%, 73.5% { transform: translateY(-250px); }
  75%, 86%   { transform: translateY(-300px); }
  87.5%, 98.5% { transform: translateY(-350px); }
  100%       { transform: translateY(0); }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .brand-rest {
    font-size: clamp(24px, 3.2vw, 32px);
    line-height: 1.35;
  }

  .box {
    height: 52px;
    font-size: 28px;
    padding: 0 1.4rem;
  }

  .animate-slide {
    animation: slide-tablet 21s infinite linear;
  }

  @keyframes slide-tablet {
    0%, 11%    { transform: translateY(0); }
    12.5%, 23.5% { transform: translateY(-52px); }
    25%, 36%   { transform: translateY(-104px); }
    37.5%, 48.5% { transform: translateY(-156px); }
    50%, 61%   { transform: translateY(-208px); }
    62.5%, 73.5% { transform: translateY(-260px); }
    75%, 86%   { transform: translateY(-312px); }
    87.5%, 98.5% { transform: translateY(-364px); }
    100%       { transform: translateY(0); }
  }
}

@media (min-width: 1024px) {
  .brand-rest {
    font-size: clamp(30px, 3vw, 42px);
  }

  .box {
    height: 60px;
    font-size: 38px;
    padding: 0 2.2rem;
  }

  .animate-slide {
    animation: slide-desktop 21s infinite linear;
  }

  @keyframes slide-desktop {
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
</style>