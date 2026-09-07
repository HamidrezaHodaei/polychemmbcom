<!-- /fa/news/index.vue -->
<template>
  <div>
    <!-- Navbar (LTR باقی می‌ماند) -->
    <Navbar />

    <!-- محتوای صفحه RTL -->
    <main class="bg-gray-100 font-[IRANYekan]" dir="rtl" :key="$route.fullPath">
      <section class="previews xl:flex">
        <!-- Hero Section -->
        <div class="relative h-[30em] xl:fixed xl:top-0 xl:left-0 xl:h-screen xl:w-[45%] bg-black">

          <!-- ✅ هر پست یک figure جداگانه — فقط opacity تغییر می‌کند -->
          <figure
            v-for="(post, index) in posts"
            :key="index"
            class="absolute inset-0 bg-cover bg-center bg-no-repeat transition-opacity duration-1000 grayscale-img"
            :class="{
              'opacity-0': currentImageIndex !== index,
              'opacity-100': currentImageIndex === index
            }"
            :style="{ backgroundImage: `url(${post.image})` }"
          />
          <div class="absolute inset-0 bg-black/20" />
        </div>

        <!-- Content -->
        <div class="min-h-screen xl:ml-[45%] text-right">

          <ul>
            <li
              v-for="(post, index) in posts"
              :key="index"
              class="preview transition-colors duration-200"
              :class="{ 'bg-white': index % 2 === 1 }"
              @mouseenter="changeImage(index)"
            >
              <NuxtLink
                :to="post.link || '#'"
                class="block p-8 md:px-32 md:py-16 xl:px-40"
              >
                <!-- تاریخ و تگ -->
                <div class="flex items-center gap-2 mb-1">
                  <div class="flex items-center gap-2 ml-auto">
                    <span
                      v-if="post.tag"
                      class="px-2 py-1 text-xs font-semibold bg-[#FFCD05] text-white rounded"
                    >
                      {{ post.tag }}
                    </span>
                    <span class="text-black text-sm">
                      {{ post.date }}
                    </span>
                  </div>
                </div>

                <h2 class="text-[#848484] text-2xl md:text-3xl font-bold mb-2 mt-1">
                  {{ post.title }}
                </h2>

                <p class="text-[#acacad] mb-3 leading-relaxed">
                  {{ post.excerpt }}
                </p>

                <span
                  class="btn-slide-down inline-block px-2 py-2 text-sm text-[#FFCD05] border-3 border-[#FFCD05] rounded-lg relative overflow-hidden"
                >
                  <span class="relative z-10">ادامه مطلب</span>
                </span>
              </NuxtLink>
            </li>
          </ul>

        </div>
      </section>
    </main>

    <Chatbox />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '~/components/fa/layout/navbar.vue'
import Chatbox from '~/components/fa/chatbox/chatbox.vue'

const currentImageIndex = ref(0)

useSeoMeta({
  title: 'اخبار - پلیکم',
  description: 'شرکت پلی‌کم تولیدکننده و صادرکننده انواع مستربچ رنگی، پرکننده (فیلر)، مستربچ افزودنی و کامپاندهای مهندسی در منطقه آزاد ارس.',
  ogTitle: 'اخبار',
  ogDescription: 'تولیدکننده پیشرو و صادرکننده مستربچ و کامپاندهای پلیمری در ایران.',
  ogUrl: 'https://polychemmb.com/fa/news',
  ogType: 'website',
})

const posts = [
  {
    date: '۱۰ تیر ۱۴۰۵',
    title: 'تجلیل از شرکت پلیمر شیمی ارس (پلیکم) به عنوان واحد صنعتی برتر منطقه',
    excerpt: 'به مناسبت روز صنعت و معدن، شرکت POLYCHEM در مراسم رسمی با حضور مسئولین سازمان منطقه آزاد ارس به عنوان یکی از واحدهای تولیدی برتر این منطقه تجلیل شد.',
    tag: 'اخبار',
    link: '/fa/news/tab/Polychem_Aras_Top_Industrial_Unit_Achievement_2026',
    image: '/News/Polychem_Aras_Top_Industrial_Unit_Achievement_2026.webp'
  },
  {
    date: '۱۷ آذر ۱۴۰۴',
    title: 'بازدید رئیس سازمان صنعت، معدن و تجارت آذربایجان شرقی از پلی‌کم در نمایشگاه تبریز پلاست ۲۰۲۵',
    excerpt: 'مهندس پرنیان، رئیس محترم سازمان صنعت، معدن و تجارت استان آذربایجان شرقی، در جریان برگزاری نمایشگاه تبریز پلاست ۲۰۲۵ از غرفه شرکت POLYCHEM بازدید کرد.',
    tag: 'اخبار',
    link: '/fa/news/tab/Official-Visit-Engineer-Parnian-Tabriz-Plast-2025',
    image: '/Visit-tabriz-3.webp'
  },
  {
    date: '۱۶–۱۹ آذر ۱۴۰۴',
    title: 'حضور POLYCHEM در نمایشگاه تبریز پلاست ۲۰۲۵',
    excerpt: 'شرکت POLYCHEM در بیست‌ودومین نمایشگاه بین‌المللی تخصصی لاستیک، پلاستیک و ماشین‌آلات (Tabriz Plast 2025) حضور فعال داشت.',
    tag: 'رویداد',
    link: '/fa/news/tab/tabriz-plast-2025',
    image: '/Tabriz-Plast-2025-1.webp'
  },
  {
    date: '۳–۶ آذر ۱۴۰۴',
    title: 'نمایشگاه Plast Eurasia استانبول ۲۰۲۵',
    excerpt: 'POLYCHEM با افتخار مشارکت خود را در نمایشگاه Plast Eurasia Istanbul 2025، بزرگ‌ترین رویداد صنعت پلاستیک منطقه، اعلام می‌کند.',
    tag: 'رویداد',
    link: '/fa/news/tab/plast-eurasia-2025',
    image: '/plast-2.jpg'
  },
  {
    date: '۲۴ آبان ۱۴۰۴',
    title: 'بازدید رئیس شعبه مرکزی بانک صنعت و معدن از شرکت POLYCHEM',
    excerpt: 'در این بازدید، مدیران ارشد بانک و مدیران شرکت POLYCHEM از خطوط پیشرفته تولید پلیمرهای مهندسی، کامپوزیت‌ها و مستربچ‌ها بازدید کردند.',
    tag: 'اخبار',
    link: '/fa/news/tab/Visit-of-the-CEO-of-Bank-of-Industry',
    image: '/Visit-of-the-CEO-of-Bank-of-Industry.webp'
  },
  {
    date: '۱۴ آبان ۱۴۰۴',
    title: 'رونمایی از محصول جدید HDCHEM 4760',
    excerpt: 'HDCHEM 4760 به‌عنوان قدرتمندترین گرید قالب‌گیری بادی در خانواده HDCHEM معرفی شد.',
    tag: 'اخبار',
    link: '/fa/news/tab/New-Product-Launch-HDCHEM-4760',
    image: '/HDCHEM-4760.webp'
  },
  {
    date: '۱ آبان ۱۴۰۴',
    title: 'گزارش تحلیل بازار جهانی پلی‌پروپیلن و کامپوزیت‌ها تا ۲۰۳۲',
    excerpt: 'این گزارش شامل تحلیل اندازه بازار، سهم، روندها و پیش‌بینی صنعت پلی‌پروپیلن و کامپوزیت‌های آن تا سال ۲۰۳۲ است.',
    tag: 'گزارش',
    link: '/fa/news/tab/Global-Polypropylene-and-Composites-Market-Report-2032',
    image: '/Report.webp'
  },
  {
    date: '۶ آذر ۱۴۰۳',
    title: 'گزارش بازار جهانی دستکش‌های پلی‌اتیلن کم‌چگال یکبارمصرف',
    excerpt: 'تحلیل جامع بازار جهانی دستکش‌های پلی‌اتیلن کم‌چگال بر اساس اندازه، مصرف‌کننده نهایی و کانال توزیع.',
    tag: 'گزارش',
    link: '/fa/news/tab/Cast_LowDensity_PE_Gloves_Market_Report_2032',
    image: '/dynamic-data-visualization-3d.webp'
  },
  {
    date: '۲۷ مهر ۱۴۰۴',
    title: 'افزایش قیمت پلی‌پروپیلن و رشد هزینه‌های تولید تا ۴۰٪',
    excerpt: 'افزایش شدید قیمت پلی‌اتیلن و پلی‌پروپیلن فشار سنگینی بر واحدهای تولیدی و صنایع غذایی وارد کرده است.',
    tag: 'اخبار',
    link: '/fa/news/tab/Rising-Polypropylene-Prices',
    image: '/high-angle-plastic-bottles-arrangement2.webp'
  }
]

const changeImage = (index) => {
  currentImageIndex.value = index
}
</script>

<style>
body {
  font-family: 'IRANYekan', 'Montserrat', sans-serif;
}

.border-3 {
  border-width: 3px;
}

.grayscale-img {
  filter: grayscale(100%);
}

.btn-slide-down::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: #ffcd05;
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
</style>