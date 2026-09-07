<template>
  <div class="hero">
    <h1 class="hero__title">
      <span class="hero__label js-hero-label">
        {{ displayedLabel }}
      </span>
      <br />
      <div class="hero__job-line">
        <div class="hero__job">
          <span>{{ currentJob }}</span>
        </div>
      </div>
      <!-- صندوق مخفي لقياس عرض نص الدول -->
      <span ref="jobMeasure" class="job-measure">
        <span>{{ currentJob }}</span>
      </span>
    </h1>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'

const labelText = 'التجارة الدولية'
const jobs = [
'تركيا',  
'العراق',
  'أذربيجان',
  'أرمينيا',
  'اليونان',
  'جورجيا'
]

const displayedLabel = ref('')
const currentJob = ref(jobs[0])
const currentJobIndex = ref(0)

let labelTick = 0
const LABEL_TICK_INTERVAL = 80 // سرعة ظهور النص
const JOB_SWITCH_INTERVAL = 4000 // فترة التبديل بين الدول

const jobMeasure = ref(null)

// الحصول على العرض الدقيق لنص الدول
const getJobWidth = async (text) => {
  await nextTick()
  if (jobMeasure.value) {
    // تحديث النص في span الداخلي
    jobMeasure.value.querySelector('span').textContent = text
    return jobMeasure.value.offsetWidth + 'px'
  }
  return 'auto'
}

// كتابة النص الرئيسي
const typeLabel = () => {
  const interval = setInterval(() => {
    if (labelTick < labelText.length) {
      labelTick++
      displayedLabel.value = labelText.substring(0, labelTick)
    } else {
      clearInterval(interval)
      // بعد انتهاء الكتابة، اعرض أول دولة بحركة
      setTimeout(showFirstJob, 300)
      // ابدأ تبديل الدول
      setInterval(rotateJob, JOB_SWITCH_INTERVAL)
    }
  }, LABEL_TICK_INTERVAL)
}

// عرض أول دولة بحركة
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

// تبديل الدول بحركة انزلاقية
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
  }, 1000) // مدة حركة الإغلاق
}

onMounted(() => {
  typeLabel()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-200.ttf') format('truetype');
  font-weight: 200;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-300.ttf') format('truetype');
  font-weight: 300;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-400.ttf') format('truetype');
  font-weight: 400;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-500.ttf') format('truetype');
  font-weight: 500;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-700.ttf') format('truetype');
  font-weight: 700;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-800.ttf') format('truetype');
  font-weight: 800;
}

@font-face {
  font-family: 'Tajawal';
  src: url('/Font/Tajawal-900.ttf') format('truetype');
  font-weight: 900;
}

body {
  background-color: #848484;
  margin: 0;
  padding: 0;
}

.hero {
  padding: 60px 40px;
  background:#f1f2f2;
  font-family: 'Tajawal', sans-serif;
  direction: rtl;
  text-align: right;
  min-height: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.hero__title {
  font-size: 4rem;
  font-weight: 700;
  line-height: 1.2;
  margin: 0;
  color: #848484;
  font-family: 'Tajawal', sans-serif;
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
  font-family: 'Tajawal', sans-serif;
  letter-spacing: 0.08em;
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
  transition: width 1s cubic-bezier(0.77, 0, 0.175, 1), opacity 0.75s ease-in;
  display: inline-block;
  font-family: 'Tajawal', sans-serif;
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
  font-weight: 700;
  font-family: 'Tajawal', sans-serif;
  padding: 0.5rem 0;
  margin: 0 0.75rem;
}
.job-measure span {
  display: block;
  margin: 0 0.75rem;
}

/* Responsive: make fonts and spacings smaller on narrow screens so text fits and both sections visible */
@media (max-width: 768px) {
  .hero {
    padding: 20px;
    align-items: flex-start;
    justify-content: center;
  }
  .hero__title {
    font-size: 1.8rem; /* smaller for mobile */
    line-height: 1.1;
    text-align: center;
  }
  .job-measure {
    font-size: 2rem; /* match hero__title */
    padding: 0.25rem 0;
    margin: 0 0.4rem;
  }
  .job-measure span {
    margin: 0 0.4rem; /* changed: reduce margin to match */
  }
  .hero__label,
  .hero__job span {
    padding: 0.25rem 0;
  }

  /* changed: make the label 1% smaller on mobile */
  .hero__label {
    font-size: 1em;
  }

  .hero__job-line {
    transition: width 0.8s cubic-bezier(0.77, 0, 0.175, 1);
  }
  .hero__job {
    font-size: 1.8rem;
    padding: 0;
    margin: 0;
  }
}
@media (max-width: 768px) {
  .hero__label {
    font-size: 0.9em;
  }
}
</style>