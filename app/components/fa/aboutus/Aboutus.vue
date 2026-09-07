<!-- /components/fa/aboutus/Aboutus.vue -->
<script setup>
import { ref } from 'vue'
const hoveredId = ref(null)
const cards = [
  { id: 1, src: '/Aboutus/about-5.webp',  alt: 'Polychem Gallery 1' },
  { id: 2, src: '/Aboutus/POLYCHEM-03.webp',  alt: 'Polychem Gallery 2' },
  { id: 3, src: '/Aboutus/POLYCHEM-01.webp', alt: 'Polychem Gallery 3' },
  { id: 4, src: '/Aboutus/POLYCHEM-02.webp',  alt: 'Polychem Gallery 4' },
]
</script>

<template>
  <div class="about-root">

    <!-- متن - یک بار در DOM، همیشه نمایش داده می‌شود -->
    <div class="text-section font-[IRANYekan]" dir="rtl">
      <h2>درباره ما</h2>
      <p class="text-justify">
        پلی‌کم، پیشگام در تولید کامپاندهای پلیمری پیشرفته و مستربچ‌های مهندسی، در قلب منطقه آزاد ارس مستقر است. بر این باوریم که کیفیت یک محصول نهایی، ریشه در انتخاب درست مواد اولیه دارد. پلی‌کم حاصل همراهی تجربه چندین‌ساله صنعت با دانش محققان جوان است.
      </p>
      <h4>تمرکز ما بر چیست؟</h4>
      <ul dir="rtl">
        <li>تولید تخصصی: عرضه کامپاندهای پلیمری مهندسی و مستربچ‌های باکیفیت.</li>
        <li>تحقیق و توسعه: بومی‌سازی دانش فنی و انتقال تکنولوژی‌های نوین.</li>
        <li>همراهی فنی: ارائه مشاوره‌های مهندسی و طراحی دقیق فرآیندهای تولید.</li>
      </ul>
      <p dir="rtl">در پلی‌کم، نوآوری و تخصص را به راهکارهای قابل اعتماد و با کیفیت بالا برای صنایع پرتقاضا تبدیل می‌کنیم.</p>
      <NuxtLink to="/fa/careers" class="btn-slide-down read-more">
        <span class="btn-text">به ما بپیوندید...</span>
      </NuxtLink>
    </div>

    <!-- گالری دسکتاپ: آکاردئون افقی -->
    <div class="gallery-desktop" @mouseleave="hoveredId = null">
      <div
        v-for="card in cards" :key="card.id"
        class="card" :class="{ 'card--hovered': hoveredId === card.id }"
        @mouseenter="hoveredId = card.id"
      >
        <img :src="card.src" :alt="card.alt" loading="lazy" class="card__img" />
        <span class="card__overlay" aria-hidden="true" />
      </div>
    </div>

    <!-- گالری موبایل: ماسونری -->
    <div class="gallery-mobile">
      <div class="mg-col mg-col-a">
        <div class="mg-card tall">
          <img :src="cards[0].src" :alt="cards[0].alt" loading="lazy" />
        </div>
        <div class="mg-card short">
          <img :src="cards[1].src" :alt="cards[1].alt" loading="lazy" />
        </div>
      </div>
      <div class="mg-col mg-col-b">
        <div class="mg-card short">
          <img :src="cards[2].src" :alt="cards[2].alt" loading="lazy" />
        </div>
        <div class="mg-card tall">
          <img :src="cards[3].src" :alt="cards[3].alt" loading="lazy" />
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&display=swap');
* { box-sizing: border-box; }

/* =============================================
   DESKTOP (> 480px): grid دو ستونه
   ترتیب: گالری چپ | متن راست
   ============================================= */
.about-root {
  width: 85%;
  max-width: 1170px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;
  align-items: center;
  gap: 60px;
  padding: 35px 0;
  margin: 0 auto;
}

/* متن: ستون راست */
.text-section {
  grid-column: 2;
  grid-row: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 14px;
}

/* گالری دسکتاپ: ستون چپ */
.gallery-desktop {
  grid-column: 1;
  grid-row: 1;
  display: flex;
  overflow: hidden;
  border-radius: 16px;
  box-shadow: 0 26px 70px rgba(0,0,0,0.35);
  height: 420px;
  width: 100%;
}

/* گالری موبایل: پنهان در دسکتاپ */
.gallery-mobile { display: none; }

/* --- آکاردئون --- */
.card {
  flex: 1 1 0;
  min-width: 0;
  height: 100%;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  transition: flex 0.5s ease;
}
.card--hovered { flex: 3; }
.card__img {
  width: 100%; height: 100%;
  object-fit: cover; display: block;
  filter: grayscale(100%);
  transition: transform 0.5s ease, filter 0.5s ease;
}
.card--hovered .card__img { transform: scale(1.12); filter: grayscale(0%); }
.card__overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.4), transparent 55%);
  opacity: 0; transition: opacity 0.3s ease;
  pointer-events: none; z-index: 1;
}
.card--hovered .card__overlay { opacity: 1; }

/* --- متن دسکتاپ --- */
.text-section h2 { font-size: 50px; font-weight: 600; color: #848484; }
.text-section h4 { font-size: 26px; font-weight: 400; color: #848484; }
.text-section p  { font-size: 15px; color: #848484; line-height: 28px; }
.text-section ul {
  list-style: disc; padding-right: 1.25rem;
  color: #848484; line-height: 1.9; font-size: 14px;
}
.text-section ul li { margin: 4px 0; }

/* --- دکمه --- */
.read-more {
  display: inline-block; text-decoration: none;
  font-size: 15px; letter-spacing: 1px;
  padding: 13px 30px; color: #FFCD05;
  border: 2px solid #FFCD05; border-radius: 8px;
  position: relative; overflow: hidden;
  background: transparent; transition: color 200ms;
  margin-top: 4px;
}
.btn-slide-down::before {
  content: ''; position: absolute; left: 0; top: 0;
  width: 100%; height: 100%; background: #FFCD05;
  transform: translateY(-100%); transition: transform 300ms ease; z-index: 0;
}
.btn-slide-down:hover::before { transform: translateY(0); }
.btn-slide-down:hover { color: #fff; outline: none; }
.btn-text { position: relative; z-index: 1; }

/* =============================================
   TABLET (≤ 768px): تک ستون، متن بالا گالری پایین
   ============================================= */
@media (max-width: 768px) {
  .about-root {
    width: 92%;
    grid-template-columns: 1fr;
    grid-template-rows: auto auto;
    gap: 22px;
    padding: 16px 0 36px;
  }

  /* متن اول */
  .text-section {
    grid-column: 1; grid-row: 1;
  }

  /* گالری آکاردئون دوم */
  .gallery-desktop {
    grid-column: 1; grid-row: 2;
    height: 260px; border-radius: 12px;
  }

  .text-section h2 { font-size: 30px; }
  .text-section h4 { font-size: 19px; }
  .text-section p  { font-size: 14px; line-height: 25px; }
}

/* =============================================
   MOBILE (≤ 480px): ماسونری جایگزین آکاردئون
   ============================================= */
@media (max-width: 480px) {
  .about-root {
    width: 100%;
    grid-template-columns: 1fr;
    grid-template-rows: auto auto;
    gap: 0;
    padding: 0 0 28px;
  }

  .text-section {
    grid-column: 1; grid-row: 1;
    padding: 6px 18px 18px;
    gap: 10px;
  }

  /* گالری دسکتاپ مخفی */
  .gallery-desktop { display: none !important; }

  /* گالری موبایل نمایش */
  .gallery-mobile {
    display: flex;
    grid-column: 1; grid-row: 2;
    flex-direction: row;
    gap: 7px;
    padding: 0 12px 8px;
    direction: ltr;
  }

  .mg-col {
    display: flex; flex-direction: column;
    gap: 7px; flex: 1;
  }
  /* ستون راست پایین‌تر = ماسونری */
  .mg-col-b { margin-top: 36px; }

  .mg-card {
    border-radius: 12px; overflow: hidden;
    position: relative;
    box-shadow: 0 6px 20px rgba(0,0,0,0.18);
  }
  .mg-card img {
    width: 100%; height: 100%;
    object-fit: cover; display: block;
    filter: grayscale(10%);
  }
  .mg-card::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.22), transparent 55%);
    pointer-events: none;
  }

  .mg-col-a .tall  { height: 195px; }
  .mg-col-a .short { height: 125px; }
  .mg-col-b .short { height: 125px; }
  .mg-col-b .tall  { height: 195px; }

  /* متن موبایل */
  .text-section h2 { font-size: 24px; }
  .text-section h4 { font-size: 15px; }
  .text-section p  { font-size: 13px; line-height: 23px; }
  .text-section ul { font-size: 13px; }
  .read-more { font-size: 13px; padding: 10px 20px; }
}

@media (prefers-reduced-motion: reduce) {
  .card, .card__img, .card__overlay { transition: none; }
}
</style>