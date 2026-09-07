<template>
        <Navbar />

  <div class="relative" dir="rtl">
    <HomeWave />
    <div class="font-[IRANYekan]">
      <div class="min-h-screen bg-gray-100 py-32 px-4">
        <div class="fond">
          <span class="s1 absolute top-0 right-0 text-[15rem] font-extrabold uppercase text-gray-300 leading-none opacity-50"></span>
          <span class="s2 absolute bottom-0 left-0 text-[15rem] font-extrabold uppercase text-gray-300 leading-none opacity-50"></span>
        </div>

        <div class="card relative h-[480px] w-full max-w-[900px] mx-auto bg-white shadow-[10px_10px_93px_0px_rgba(0,0,0,0.75)]">
          <div class="thumbnail absolute right-[30px] top-[-30px] h-[350px] w-[530px] overflow-hidden shadow-[10px_10px_60px_0px_rgba(0,0,0,0.75)]">
            <img
              class="absolute right-1/2 top-1/2 h-auto w-full translate-x-1/2 -translate-y-1/2 transform"
              src="/high-angle-plastic-bottles-arrangement.webp"
              alt="نوسانات قیمت پلی‌پروپیلن"
            />
          </div>

          <div class="right mr-[590px] ml-5 text-right">
            <h1 class="pt-[15px] text-[1.3rem] text-[#FFCD05] font-bold leading-relaxed">
              تأثیر مستقیم نوسانات بازار پلیمر بر بهای تمام‌شده محصولات؛ افزایش فشار بر صنایع پایین‌دستی
            </h1>

            <div class="separator mt-2.5 border-t border-[#C3C3C3]"></div>

            <p class="pt-2.5 text-right text-[0.95rem] leading-[180%] text-black">
              گزارش‌های اخیر بازار حاکی از آن است که روند صعودی قیمت پلی‌اتیلن و پلی‌پروپیلن، فراتر از صنعت پلاستیک، زنجیره تأمین سایر بخش‌های حیاتی از جمله صنایع غذایی و دارویی را تحت تأثیر قرار داده است. این مواد به عنوان ارکان اصلی تولید انواع بسته‌بندی، ظروف و فیلم‌های محافظ، نقش تعیین‌کننده‌ای در قیمت نهایی کالاها دارند. 
              <br><br>
              
            </p>
            
            <NuxtLink to="/fa/news" class="btn-slide-down inline-block px-5 py-2.5 mt-4 text-sm text-[#FFCD05] border-2 border-[#FFCD05] rounded-lg relative overflow-hidden cursor-pointer font-bold">
              <span class="relative z-10">مشاهده همه اخبار</span>
            </NuxtLink>
          </div>

          <h5 class="absolute right-[30px] bottom-[30px] text-[6rem] text-[#C3C3C3] leading-none font-bold">
            24
          </h5>
          <h6 class="absolute right-[35px] bottom-[10px] text-[2rem] text-[#C3C3C3] leading-none">
            آبان ماه
          </h6>

          <div class="absolute bottom-[50px] right-[250px] flex gap-6 flex-row-reverse">
             </div>

          <button class="fab absolute left-[50px] bottom-[-40px] flex h-20 w-20 items-center justify-center bg-[#FFCD05] text-white shadow-[10px_10px_50px_0px_rgba(0,0,0,0.75)] cursor-pointer hover:bg-[#E6B800] transition-colors"></button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.font-\[IRANYekan\] {
  font-family: 'IRANYekan', Tahoma, sans-serif;
}

/* افکت دکمه */
.btn-slide-down::before {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}
.btn-slide-down:hover::before {
  transform: translateY(0);
}
.btn-slide-down:hover {
  color: #fff;
}

/* انیمیشن دکمه شناور */
.fab {
  animation: fab-morph 5s linear infinite;
}
@keyframes fab-morph {
  from { transform: rotateZ(0deg); border-radius: 50%; }
  50% { border-radius: 0%; }
  to { transform: rotateZ(360deg); border-radius: 50%; }
}

@media (max-width: 968px) {
  .card { height: auto; width: 95%; padding-bottom: 20px; }
  .thumbnail { position: relative; right: 0; top: 0; width: 100%; height: 250px; margin-bottom: 20px; }
  .right { margin-right: 20px; margin-left: 20px; padding-bottom: 80px; }
  h5, h6 { right: 20px; }
  .fab { left: 20px; }
}
</style>
<script setup>
import Navbar from '~/components/fa/layout/navbar.vue';
import HomeWave from '~/components/en/layout/HomeWave.vue';
</script>
