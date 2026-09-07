<template>
  <div dir="rtl" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;">
    <Navbar />
    <main class="bg-gray-100" style="font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;">
      <section class="previews md:flex">
        <!-- Hero Section -->
        <div class="relative h-[30em] md:fixed md:top-0 md:left-0 md:h-screen md:w-[45%] bg-black">
          <figure
            v-for="(image, index) in backgroundImages"
            :key="index"
            class="absolute inset-0 bg-cover bg-center bg-no-repeat transition-opacity duration-1000 grayscale-img"
            :class="{
              'opacity-0': currentImageIndex !== index,
              'opacity-100': currentImageIndex === index
            }"
            :style="{ backgroundImage: `url(${image})` }"
          />
          <div class="absolute inset-0 bg-black/20" />
        </div>

        <!-- Content Section -->
        <div class="min-h-screen md:ml-[45%]">
          

          <!-- Posts -->
          <ul>
            <li
              v-for="(post, index) in posts"
              :key="index"
              class="preview transition-colors duration-200"
              :class="{ 'bg-white': index % 2 === 1 }"
              @mouseenter="changeImage(index)"
            >
              <NuxtLink :to="post.link || '#'" class="block p-8 md:px-32 md:py-16 xl:px-40">
                <div class="flex items-center gap-2 mb-1">
                  <span class="text-black text-sm">{{ post.date }}</span>
                  <span
                    v-if="post.tag"
                    class="px-2 py-1 text-xs font-semibold uppercase tracking-wider bg-[#FFCD05] text-white rounded"
                  >
                    {{ post.tag }}
                  </span>
                </div>

                <h2 class="text-[#848484] text-2xl md:text-3xl font-bold mb-2 mt-1">
                  {{ post.title }}
                </h2>

                <p class="text-[#acacad] mb-3 leading-relaxed">
                  {{ post.excerpt }}
                </p>

                <span
                  class="btn-slide-down inline-block px-2 py-2 uppercase tracking-wider text-sm text-[#FFCD05] border-3 border-[#FFCD05] rounded-lg relative overflow-hidden"
                >
<span class="relative z-10">اقرأ أكثر</span>                </span>
              </NuxtLink>
            </li>
          </ul>

          <!-- Footer -->
          
        </div>
      </section>
    </main>

    <Chatbox />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '/components/ar/layout/navbar.vue'
import Chatbox from '/components/ar/chatbox/chatbox.vue'

const currentImageIndex = ref(0)

const backgroundImages = [
'/News/Polychem_Aras_Top_Industrial_Unit_Achievement_2026.webp',
'/Visit-tabriz-3.webp',
'/Tabriz-Plast-2025-1.webp',  
'/plast-2.jpg',
  '/Visit-of-the-CEO-of-Bank-of-Industry.webp',
  '/HDCHEM-4760.webp',
  '/Report.webp',
  '/dynamic-data-visualization-3d.webp',
  '/high-angle-plastic-bottles-arrangement2.webp'

]

const posts = [
  {
    date: '1 يوليو 2026',
    title: 'شركة "POLYCHEM" تُتوّج كأفضل منشأة صناعية في منطقة آراس الحرة',
    excerpt: 'تم تكريم شركة "POLYCHEM" كواحدة من أفضل المنشآت الصناعية في منطقة آراس الحرة بمناسبة يوم الصناعة والتعدين؛ وذلك تقديراً لأدائها المتميز في مجالي الإنتاج وريادة الأعمال.',
    tag: 'خبر',
    link: '/ar/news/tab/Polychem_Aras_Top_Industrial_Unit_Achievement_2026'
  },
  {
    date: '17 ديسمبر 2025',
    title: 'رئيس منظمة الصناعة والمعادن والتجارة في شرق أذربيجان يزور POLYCHEM في معرض تبريز البلاستيك 2025',
    excerpt: 'قام رئيس منظمة الصناعة والمعادن والتجارة بولاية شرق أذربيجان، المهندس بارنيان، بزيارة معرض تبريز البلاستيك الدولي 2025 حيث زار جناح POLYCHEM.',
    tag: 'خبر',
    link: '/ar/news/tab/Official-Visit-Engineer-Parnian-Tabriz-Plast-2025'
  },
  {
    date: '16-19 ديسمبر 2025',
    title: 'POLYCHEM في معرض تبريز البلاستيك 2025',
    excerpt: 'شاركت POLYCHEM في المعرض الدولي المتخصص الثاني والعشرين للمطاط والبلاستيك والآلات (معرض تبريز البلاستيك 2025).',
    tag: 'حدث',
    link: '/ar/news/tab/tabriz-plast-2025'
  },
  {
    date: '3-6 ديسمبر 2025',
    title: 'معرض بلاست يوراسيا إسطنبول 2025',
    excerpt: 'تفتخر POLYCHEM بالإعلان عن مشاركتها في معرض بلاست يوراسيا إسطنبول 2025، المعرض الرائد في قطاع البلاستيك بالمنطقة. سيقام الحدث في الفترة من 3-6 ديسمبر 2025 في مركز TÜYAP للمعارض والمؤتمرات.',
    tag: 'حدث',
    link: '/ar/news/tab/plast-eurasia-2025'
  },
  {
    date: '24 نوفمبر 2025',
    title: 'رئيس الفرع الرئيسي لبنك الصناعة يزور POLYCHEM',
    excerpt: 'حضرت الزيارة عدة نواب رئيس البنك والمديرين التنفيذيين بالإضافة إلى مسؤولي شركة POLYCHEM. استعرض د. رضوي خطوط إنتاج البوليمرات الهندسية والمركبات الخاصة والمادات الملدنة وإضافات البوليمر والمنتجات الجديدة من الجيل الجديد، وراجع أحدث الإنجازات البحثية والإنتاجية.',
    tag: 'خبر',
    link: '/ar/news/tab/Visit-of-the-CEO-of-Bank-of-Industry'
  },
  {
    date: '14 نوفمبر 2025',
    title: 'إطلاق منتج جديد: HDCHEM 4760 – أقوى مركب صب بالنفخ',
    excerpt: 'يسعدنا أن نقدم إليكم أقوى جودة صب بالنفخ في سلسلة HDCHEM: HDCHEM 4760',
    tag: 'خبر',
    link: '/ar/news/tab/New-Product-Launch-HDCHEM-4760'
  },
  {
    date: '1 نوفمبر 2025',
    title: 'تحليل سوق البولي بروبيلين والمركبات - توقعات 2032',
    excerpt: 'تحليل السوق العالمي للبولي بروبيلين والمركبات حسب نوع المنتج (البولي بروبيلين، مركبات البولي بروبيلين)، ونوع الألياف (الألياف الزجاجية، ألياف الكربون، وغيرها)، والتطبيقات (التغليف، البناء، السيارات، الكهربائية والإلكترونية، الطيران والدفاع، وغيرها) - اتجاهات القطاع وتوقعات 2032',
    tag: 'تقرير',
    link: '/ar/news/tab/Global-Polypropylene-and-Composites-Market-Report-2032'
  },
  {
    date: '6 ديسمبر 2024',
    title: 'سوق قفازات البولي إيثيلين منخفضة الكثافة العالمية - توقعات 2032',
    excerpt: 'سوق قفازات البولي إيثيلين منخفضة الكثافة الموسعة العالمي حسب التقسيم بالحجم (صغير، متوسط، كبير، كبير جداً)، ونوع المستخدم (الغذاء والمشروبات، الطبي، الصناعي، وغيره)، قناة التوزيع (المباشر وعبر الموزعين) - توقعات 2032',
    tag: 'تقرير',
    link: '/ar/news/tab/Cast_LowDensity_PE_Gloves_Market_Report_2032'
  },
  {
    date: '27 أكتوبر 2025',
    title: 'ارتفاع أسعار البولي بروبيلين يرفع تكاليف الإنتاج بنسبة 40٪',
    excerpt: 'قدم الارتفاع السريع في أسعار البولي إيثيلين والبولي بروبيلين إشارة إنذار جديدة لقطاع الغذاء والمستهلكين. أدى هذا الارتفاع إلى مواجهة وحدات الإنتاج من مصنعي التغليف إلى مصانع الغذاء بأزمة تكلفة، وانعكس تأثيره مباشرة على أسعار المنتجات الأساسية.',
    tag: 'خبر',
    link: '/ar/news/tab/Rising-Polypropylene-Prices'
  },
]

const changeImage = (index) => {
  currentImageIndex.value = index
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

/* Font Faces - Tajawal */
@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-ExtraLight.ttf") format("truetype");
  font-weight: 200;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Light.ttf") format("truetype");
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Medium.ttf") format("truetype");
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Bold.ttf") format("truetype");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-ExtraBold.ttf") format("truetype");
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Tajawal";
  src: url("/Font/Tajawal-Black.ttf") format("truetype");
  font-weight: 900;
  font-style: normal;
  font-display: swap;
}

/* Font Faces - Montserrat */
@font-face {
  font-family: "Montserrat";
  src: url("/Fonts/Montserrat-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Montserrat";
  src: url("/Fonts/Montserrat-Bold.ttf") format("truetype");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

body {
  font-family: 'Tajawal', 'Montserrat', sans-serif;
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

.archive-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 3px;
  background-color: #ffcd05;
  transition: width 0.4s ease;
}

.archive-link:hover::after {
  width: 100%;
}
</style>
