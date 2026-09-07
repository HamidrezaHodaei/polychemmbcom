<template>
  <main class="w-full bg-[#f1f2f2] flex items-center justify-center px-4" style="min-height: 100vh;">
    <div class="wrapper">

      <p class="brand-line">
        <span class="brand">Polychem</span>
        <span class="brand-separator"> — </span>
        <span class="brand-rest">Polimerin her tanesinin dönüştüğü yer</span>
      </p>

      <div class="box-container">
        <div class="animate-slide">
          <div class="box">Polimer Sanatı</div>
          <div class="box">Özgünlük</div>
          <div class="box">Sadakat</div>
          <div class="box">Yaratıcılık</div>
          <div class="box">Dürüstlük</div>
          <div class="box">Zarafet</div>
          <div class="box">Anlam</div>
          <div class="box">Polimer Sanatı</div>
        </div>
      </div>

    </div>
  </main>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&display=swap');

* {
  font-family: 'Montserrat', sans-serif;
}

/* ===== BASE (موبایل — زیر 1024px) ===== */
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 1.5rem;
  width: 100%;
  padding: 2rem 1rem;
}

.brand-line {
  font-weight: 700;
  color: #848484;
  text-transform: uppercase;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.brand {
  font-weight: 800;
  font-size: clamp(28px, 7vw, 45px);
  letter-spacing: 0.05em;
  white-space: nowrap;
}

.brand-separator {
  display: none;
}

.brand-rest {
  font-weight: 700;
  font-size: clamp(22px, 6vw, 35px);
  white-space: normal;
  max-width: 100%;
}

.box-container {
  overflow: hidden;
  flex-shrink: 0;
  height: 48px;
}

.animate-slide {
  animation: slide 21s infinite linear;
}

.box {
  height: 48px;
  background: #FFD700;
  color: white;
  font-weight: 800;
  font-size: clamp(22px, 6vw, 30px);
  text-transform: uppercase;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 1.2rem;
  white-space: nowrap;
}

@keyframes slide {
  0%,   11%    { transform: translateY(0); }
  12.5%,23.5%  { transform: translateY(-48px); }
  25%,  36%    { transform: translateY(-96px); }
  37.5%,48.5%  { transform: translateY(-144px); }
  50%,  61%    { transform: translateY(-192px); }
  62.5%,73.5%  { transform: translateY(-240px); }
  75%,  86%    { transform: translateY(-288px); }
  87.5%,98.5%  { transform: translateY(-336px); }
  100%         { transform: translateY(0); }
}

/* ===== 1024px – 1144px (نرو لپ‌تاپ) ===== */
@media (min-width: 1024px) and (max-width: 1144px) {
  .wrapper {
    flex-direction: row;
    text-align: left;
    gap: 1rem;
    padding: 2rem 1rem;
  }

  .brand-line {
    justify-content: flex-start;
    flex-wrap: wrap;
  }

  .brand-separator {
    display: inline;
    font-weight: 700;
    font-size: clamp(14px, 1.8vw, 20px);
    margin: 0 0.25rem;
    opacity: 0.9;
  }

  .brand      { font-size: clamp(26px, 2.4vw, 26px); }
  .brand-rest { font-size: clamp(24px, 1.9vw, 20px); }

  .box-container { height: 40px; }

  .box {
    height: 40px;
    font-size: clamp(26px, 1.8vw, 22px);
    padding: 0 0.9rem;
  }

  @keyframes slide {
    0%,   11%    { transform: translateY(0); }
    12.5%,23.5%  { transform: translateY(-40px); }
    25%,  36%    { transform: translateY(-80px); }
    37.5%,48.5%  { transform: translateY(-120px); }
    50%,  61%    { transform: translateY(-160px); }
    62.5%,73.5%  { transform: translateY(-200px); }
    75%,  86%    { transform: translateY(-240px); }
    87.5%,98.5%  { transform: translateY(-280px); }
    100%         { transform: translateY(0); }
  }

  @media (min-resolution: 120dpi) {
    .wrapper {
      gap: 0.8rem;
      padding: 1.5rem 0.8rem;
    }

    .brand      { font-size: clamp(15px, 2vw, 22px); }
    .brand-separator { font-size: clamp(12px, 1.6vw, 18px); }
    .brand-rest { font-size: clamp(12px, 1.6vw, 18px); }

    .box-container { height: 34px; }

    .box {
      height: 34px;
      font-size: clamp(13px, 1.5vw, 18px);
      padding: 0 0.7rem;
    }

    @keyframes slide {
      0%,   11%    { transform: translateY(0); }
      12.5%,23.5%  { transform: translateY(-34px); }
      25%,  36%    { transform: translateY(-68px); }
      37.5%,48.5%  { transform: translateY(-102px); }
      50%,  61%    { transform: translateY(-136px); }
      62.5%,73.5%  { transform: translateY(-170px); }
      75%,  86%    { transform: translateY(-204px); }
      87.5%,98.5%  { transform: translateY(-238px); }
      100%         { transform: translateY(0); }
    }
  }
}

/* ===== LAPTOP (1145px – 1365px) ===== */
@media (min-width: 1145px) and (max-width: 1365px) {
  .wrapper {
    flex-direction: row;
    text-align: left;
    gap: 2rem;
    padding: 3rem 1.5rem;
  }

  .brand-line {
    justify-content: flex-start;
  }

  .brand-separator {
    display: inline;
    font-weight: 700;
    font-size: clamp(22px, 3.5vw, 32px);
    margin: 0 0.4rem;
    opacity: 0.9;
  }

  .brand      { font-size: clamp(28px, 4vw, 40px); }
  .brand-rest { font-size: clamp(22px, 3vw, 32px); }

  .box-container { height: 54px; }

  .box {
    height: 54px;
    font-size: clamp(24px, 2.8vw, 38px);
    padding: 0 1.6rem;
  }

  @keyframes slide {
    0%,   11%    { transform: translateY(0); }
    12.5%,23.5%  { transform: translateY(-54px); }
    25%,  36%    { transform: translateY(-108px); }
    37.5%,48.5%  { transform: translateY(-162px); }
    50%,  61%    { transform: translateY(-216px); }
    62.5%,73.5%  { transform: translateY(-270px); }
    75%,  86%    { transform: translateY(-324px); }
    87.5%,98.5%  { transform: translateY(-378px); }
    100%         { transform: translateY(0); }
  }

  @media (min-resolution: 120dpi) {
    .wrapper {
      gap: 1.8rem;
      padding: 2.5rem 1.2rem;
    }

    .brand      { font-size: clamp(24px, 3.5vw, 35px); }
    .brand-separator { font-size: clamp(18px, 3vw, 28px); }
    .brand-rest { font-size: clamp(20px, 2.8vw, 30px); }

    .box-container { height: 48px; }

    .box {
      height: 48px;
      font-size: clamp(22px, 2.6vw, 34px);
      padding: 0 1.4rem;
    }

    @keyframes slide {
      0%,   11%    { transform: translateY(0); }
      12.5%,23.5%  { transform: translateY(-48px); }
      25%,  36%    { transform: translateY(-96px); }
      37.5%,48.5%  { transform: translateY(-144px); }
      50%,  61%    { transform: translateY(-192px); }
      62.5%,73.5%  { transform: translateY(-240px); }
      75%,  86%    { transform: translateY(-288px); }
      87.5%,98.5%  { transform: translateY(-336px); }
      100%         { transform: translateY(0); }
    }
  }

  @media (min-resolution: 144dpi) {
    .wrapper {
      gap: 1.5rem;
      padding: 2rem 1rem;
    }

    .brand      { font-size: clamp(22px, 3vw, 32px); }
    .brand-separator { font-size: clamp(16px, 2.6vw, 24px); }
    .brand-rest { font-size: clamp(18px, 2.4vw, 28px); }

    .box-container { height: 42px; }

    .box {
      height: 42px;
      font-size: clamp(20px, 2.2vw, 30px);
      padding: 0 1.2rem;
    }

    @keyframes slide {
      0%,   11%    { transform: translateY(0); }
      12.5%,23.5%  { transform: translateY(-42px); }
      25%,  36%    { transform: translateY(-84px); }
      37.5%,48.5%  { transform: translateY(-126px); }
      50%,  61%    { transform: translateY(-168px); }
      62.5%,73.5%  { transform: translateY(-210px); }
      75%,  86%    { transform: translateY(-252px); }
      87.5%,98.5%  { transform: translateY(-294px); }
      100%         { transform: translateY(0); }
    }
  }
}

/* ===== DESKTOP (1366px+) ===== */
@media (min-width: 1366px) {
  .wrapper {
    flex-direction: row;
    text-align: left;
    gap: 2.5rem;
    padding: 4rem 2rem;
  }

  .brand-line {
    justify-content: flex-start;
  }

  .brand-separator {
    display: inline;
    font-weight: 700;
    font-size: clamp(24px, 4vw, 36px);
    margin: 0 0.5rem;
    opacity: 0.9;
  }

  .brand      { font-size: clamp(32px, 4.5vw, 45px); }
  .brand-rest { font-size: clamp(24px, 3.5vw, 35px); }

  .box-container { height: 60px; }

  .box {
    height: 60px;
    font-size: clamp(28px, 3vw, 45px);
    padding: 0 2rem;
  }

  @keyframes slide {
    0%,   11%    { transform: translateY(0); }
    12.5%,23.5%  { transform: translateY(-60px); }
    25%,  36%    { transform: translateY(-120px); }
    37.5%,48.5%  { transform: translateY(-180px); }
    50%,  61%    { transform: translateY(-240px); }
    62.5%,73.5%  { transform: translateY(-300px); }
    75%,  86%    { transform: translateY(-360px); }
    87.5%,98.5%  { transform: translateY(-420px); }
    100%         { transform: translateY(0); }
  }

  @media (min-resolution: 120dpi) {
    .wrapper {
      gap: 2rem;
      padding: 3rem 1.5rem;
    }

    .brand      { font-size: clamp(28px, 4vw, 40px); }
    .brand-separator { font-size: clamp(20px, 3.5vw, 30px); }
    .brand-rest { font-size: clamp(20px, 3vw, 30px); }

    .box-container { height: 52px; }

    .box {
      height: 52px;
      font-size: clamp(24px, 2.8vw, 38px);
      padding: 0 1.6rem;
    }

    @keyframes slide {
      0%,   11%    { transform: translateY(0); }
      12.5%,23.5%  { transform: translateY(-52px); }
      25%,  36%    { transform: translateY(-104px); }
      37.5%,48.5%  { transform: translateY(-156px); }
      50%,  61%    { transform: translateY(-208px); }
      62.5%,73.5%  { transform: translateY(-260px); }
      75%,  86%    { transform: translateY(-312px); }
      87.5%,98.5%  { transform: translateY(-364px); }
      100%         { transform: translateY(0); }
    }
  }

  @media (min-resolution: 144dpi) {
    .wrapper {
      gap: 1.5rem;
      padding: 2.5rem 1rem;
    }

    .brand      { font-size: clamp(24px, 3.5vw, 35px); }
    .brand-separator { font-size: clamp(18px, 3vw, 26px); }
    .brand-rest { font-size: clamp(18px, 2.6vw, 26px); }

    .box-container { height: 44px; }

    .box {
      height: 44px;
      font-size: clamp(20px, 2.4vw, 32px);
      padding: 0 1.2rem;
    }

    @keyframes slide {
      0%,   11%    { transform: translateY(0); }
      12.5%,23.5%  { transform: translateY(-44px); }
      25%,  36%    { transform: translateY(-88px); }
      37.5%,48.5%  { transform: translateY(-132px); }
      50%,  61%    { transform: translateY(-176px); }
      62.5%,73.5%  { transform: translateY(-220px); }
      75%,  86%    { transform: translateY(-264px); }
      87.5%,98.5%  { transform: translateY(-308px); }
      100%         { transform: translateY(0); }
    }
  }
}
</style>