<template>
  <div class="hero font-[IRANYekan]">
    <h1 class="hero__title font-[IRANYekan]">
      <span class="hero__label js-hero-label font-[IRANYekan]">
        {{ displayedLabel }}
      </span>
      <br />
      <div class="hero__job-line">
        <div class="hero__job font-[IRANYekan]">
          <span>{{ currentJob }}</span>
        </div>
      </div>
      <!-- باکس مخفی برای اندازه‌گیری عرض متن شغل -->
      <span ref="jobMeasure" class="job-measure">
        <span>{{ currentJob }}</span>
      </span>
    </h1>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'

// تنظیمات
const labelText = 'بازار تجارت بین‌المللی با کشورهای'
const jobs = [
  'عراق',
  'آذربایجان',
  'ترکیه',
  'ارمنستان',
  'یونان',
  'گرجستان'
]


const displayedLabel = ref('')
const currentJob = ref(jobs[0])
const currentJobIndex = ref(0)

let labelTick = 0
const LABEL_TICK_INTERVAL = 80 // سرعت تایپ شدن متن
const JOB_SWITCH_INTERVAL = 4000 // هر چند ثانیه شغل عوض بشه

const jobMeasure = ref(null)

// تابع گرفتن عرض دقیق متن شغل
const getJobWidth = async (text) => {
  await nextTick()
  if (jobMeasure.value) {
    // مقدار span داخلی را آپدیت کن
    jobMeasure.value.querySelector('span').textContent = text
    return jobMeasure.value.offsetWidth + 'px'
  }
  return 'auto'
}

// تابع تایپ کردن متن اصلی
const typeLabel = () => {
  const interval = setInterval(() => {
    if (labelTick < labelText.length) {
      labelTick++
      displayedLabel.value = labelText.substring(0, labelTick)
    } else {
      clearInterval(interval)
      // بعد از اتمام تایپ، اولین شغل رو با انیمیشن نشون بده
      setTimeout(showFirstJob, 300)
      // شروع چرخش شغل‌ها
      setInterval(rotateJob, JOB_SWITCH_INTERVAL)
    }
  }, LABEL_TICK_INTERVAL)
}

// نمایش اولین شغل با انیمیشن
const showFirstJob = async () => {
  currentJob.value = jobs[0]
  await nextTick()
  const jobEl = document.querySelector('.hero__job')
  const lineEl = document.querySelector('.hero__job-line')
  if (jobEl && lineEl) {
    const width = await getJobWidth(currentJob.value)
    jobEl.style.width = '0px'
    setTimeout(() => {
      lineEl.style.width = width
      jobEl.style.width = width
      jobEl.style.opacity = '1'
    }, 50)
  }
}

// چرخش شغل‌ها با انیمیشن کشویی
const rotateJob = async () => {
  const jobEl = document.querySelector('.hero__job')
  const lineEl = document.querySelector('.hero__job-line')

  if (!jobEl || !lineEl) return

  jobEl.style.width = '0px'
  jobEl.style.opacity = '0'

  setTimeout(async () => {
    currentJobIndex.value = (currentJobIndex.value + 1) % jobs.length
    currentJob.value = jobs[currentJobIndex.value]

    await nextTick()
    const newWidth = await getJobWidth(currentJob.value)
    jobEl.style.width = '0px'

    setTimeout(() => {
      lineEl.style.width = newWidth
      jobEl.style.width = newWidth
      jobEl.style.opacity = '1'
    }, 100)
  }, 1000) // مدت زمان انیمیشن جمع شدن
}

onMounted(() => {
  typeLabel()
})
</script>

<style scoped>

body {
  background-color: #848484;
  margin: 0;
  padding: 0;
}

.hero {
  padding: 60px 40px;
  background:#f1f2f2;
  text-transform: uppercase;
  min-height: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.hero__title {
  font-size: 4rem;
  font-weight: bold;
  line-height: 1.2;
  margin: 0;
  color: #848484;
}

.hero__label,
.hero__job span {
  display: inline-block;
  padding: 0.5rem 0;
  white-space: nowrap;
  overflow: hidden;
}

.hero__label {
  color: #848484;
}

.hero__job-line {
  text-align: right;
  overflow: hidden;
  display: inline-block;
  width: 0;
  transition: width 1s cubic-bezier(0.77, 0, 0.175, 1);
}

.hero__job {
  background: #FFD700;
  color: #fff;
  direction: rtl;
  width: 0;
  opacity: 0;
  overflow: hidden;
  white-space: nowrap;
  text-align: right;
  transition: width 1s cubic-bezier(0.77, 0, 0.175, 1), opacity 0.75s ease-in;
  display: inline-block;

}

.hero__job span {
  display: block;
  margin: 0 0.75rem;
}

.job-measure {
  position: absolute;
  visibility: hidden;
  white-space: nowrap;
  pointer-events: none;
  font-size: 4rem;
  font-weight: bold;
  text-transform: uppercase;
  padding: 0.5rem 0;
  margin: 0 0.75rem;
}
.job-measure span {
  display: block;
  margin: 0 0.75rem;
}

/* ===== TABLET (600px – 1023px) ===== */
@media (min-width: 600px) and (max-width: 1023px) {
  .hero {
    padding: 16px 24px;
    align-items: center;
    justify-content: center;
  }
  .hero__title {
    font-size: 2.6rem;
    line-height: 1.15;
    text-align: center;
  }
  .hero__label { font-size: 0.95em; }
  .hero__label,
  .hero__job span { padding: 0.35rem 0; }
  .hero__job { font-size: 2.5rem; }
  .hero__job-line { transition: width 0.9s cubic-bezier(0.79, 0, 0.18, 1); }
  .job-measure {
    font-size: 2.6rem;
    padding: 0.35rem 0;
    margin: 0 0.55rem;
  }
  .job-measure span { margin: 0 0.55rem; }
}

/* ===== MOBILE (max 599px) ===== */
@media (max-width: 599px) {
  .hero {
    padding: 20px;
    align-items: flex-start;
    justify-content: center;
    margin-bottom: 40px;
  }
  .hero__title {
    font-size: 1.8rem;
    line-height: 1.1;
    text-align: center;
  }
  .job-measure {
    font-size: 2rem;
    padding: 0.25rem 0;
    margin: 0 0.4rem;
  }
  .job-measure span { margin: 0 0.4rem; }
  .hero__label,
  .hero__job span { padding: 0.25rem 0; }
  .hero__label { font-size: 1em; }
  .hero__job-line { transition: width 0.8s cubic-bezier(0.77, 0, 0.175, 1); }
  .hero__job {
    font-size: 1.8rem;
    padding: 0;
    margin: 0;
  }
}
</style>