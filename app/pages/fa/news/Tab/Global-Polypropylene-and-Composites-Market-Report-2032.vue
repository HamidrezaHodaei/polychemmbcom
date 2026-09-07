<template>
          <div class="relative" >

        <Navbar />
<div dir="rtl">
    <HomeWave />
    <div class="font-[IRANYekan]">
      <div class="min-h-screen bg-gray-100 py-32 px-4">
        <div class="fond">
          <span class="s1 absolute top-0 right-0 text-[15rem] font-extrabold uppercase text-gray-300 leading-none opacity-50"></span>
          <span class="s2 absolute bottom-0 left-0 text-[15rem] font-extrabold uppercase text-gray-300 leading-none opacity-50"></span>
        </div>

        <div class="card relative h-[500px] w-full max-w-[900px] mx-auto bg-white shadow-[10px_10px_93px_0px_rgba(0,0,0,0.75)]">
          <div class="thumbnail absolute right-[30px] top-[-30px] h-[270px] w-[530px] overflow-hidden shadow-[10px_10px_60px_0px_rgba(0,0,0,0.75)] bg-white">
            <img
              class="absolute right-1/2 top-1/2 h-auto w-full translate-x-1/2 -translate-y-1/2 transform"
              src="/Report.webp"
              alt="گزارش بازار جهانی پلی‌پروپیلن"
            />
          </div>

          <div class="right mr-[590px] ml-5 text-right">
            <h1 class="pt-[25px] text-[1.2rem] text-[#FFCD05] font-bold leading-relaxed">
              گزارش جامع بازار جهانی پلی‌پروپیلن و کامپوزیت‌ها؛ تحلیل روندها و پیش‌بینی بازه ۲۰۲۴ تا ۲۰۳۲
            </h1>

            <div class="separator mt-2.5 border-t border-[#C3C3C3]"></div>

            <p class="pt-3 text-justify text-[0.92rem] leading-[180%] text-black">
              این گزارش تحلیلی به بررسی ابعاد بازار، سهم بازیگران کلیدی و محرک‌های رشد در صنعت پلی‌پروپیلن (PP) و کامپوزیت‌های تقویت‌شده (الیاف شیشه و کربن) می‌پردازد. تحلیل پیش رو، تحولات استراتژیک در حوزه‌های کلیدی از جمله **صنایع بسته‌بندی، خودرو، ساختمان و صنایع دفاعی** را پوشش داده و نقش نوآوری‌های پلیمری را در شکل‌دهی به آینده این بازار بررسی می‌کند.
            </p>
            
            <NuxtLink to="/fa/news" class="btn-slide-down inline-block px-5 py-2 mt-4 text-sm text-[#FFCD05] border-2 border-[#FFCD05] rounded-lg relative overflow-hidden cursor-pointer font-bold">
              <span class="relative z-10">مشاهده همه اخبار</span>
            </NuxtLink>
          </div>

          <div class="absolute right-[30px] top-[260px] w-[530px] pl-4 text-right">
            <p class="text-[1.4rem] leading-relaxed text-gray-700 font-bold pt-4">
              دسترسی به متن کامل گزارش:
            </p>
            <a 
              href="https://www.databridgemarketresearch.com/reports/global-polypropylene-and-polypropylene-composites-market" 
              target="_blank"
              rel="noopener noreferrer"
              class="btn-slide-down inline-block mt-3 px-6 py-3 text-sm text-[#FFCD05] border-2 border-[#FFCD05] rounded-lg relative overflow-hidden cursor-pointer font-bold"
            >
              <span class="relative z-10">مشاهده منبع گزارش (Data Bridge)</span>
            </a>
          </div>

          <h5 class="absolute right-[30px] bottom-[30px] text-[6rem] text-[#C3C3C3] leading-none font-bold">
            09
          </h5>
          <h6 class="absolute right-[35px] bottom-[10px] text-[2rem] text-[#C3C3C3] leading-none">
            آذر ماه
          </h6>

          <div class="absolute bottom-[50px] right-[250px] flex gap-6 flex-row-reverse">
            </div>

          <button class="fab absolute left-[50px] bottom-[-40px] flex h-20 w-20 items-center justify-center bg-[#FFCD05] text-white shadow-[10px_10px_50px_0px_rgba(0,0,0,0.75)] cursor-pointer"></button>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<style scoped>
.font-\[IRANYekan\] {
  font-family: 'IRANYekan', 'Tahoma', sans-serif;
}

/* Hover effect */
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
.btn-slide-down:hover::before { transform: translateY(0); }
.btn-slide-down:hover { color: #ffffff; }

/* FAB Animation */
.fab { animation: fab-morph 5s linear infinite; }
@keyframes fab-morph {
  from { transform: rotateZ(0deg); border-radius: 50%; }
  50% { border-radius: 0%; }
  to { transform: rotateZ(360deg); border-radius: 50%; }
}

@media (max-width: 968px) {
  .card { height: auto; width: 95%; }
  .thumbnail { position: relative; right: 0; top: 0; width: 100%; height: 250px; margin-bottom: 20px; }
  .right { margin-right: 20px; margin-left: 20px; padding-bottom: 100px; }
  h5, h6 { right: 20px; }
  .fab { left: 20px; right: auto; }
}
</style>
<script setup>
import Navbar from '~/components/fa/layout/navbar.vue';
import HomeWave from '~/components/en/layout/HomeWave.vue';
</script>
