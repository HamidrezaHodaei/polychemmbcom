<!-- AppLoading.vue -->
<template>
  <Teleport to="body">
    <Transition name="fade">
        <div v-if="isLoading && !isLanding" class="loading-overlay">
        <div class="loading-container">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 170.08 170.08"
            class="loader-svg"
          >
            <!-- دایره زرد -->
            <path
              ref="yellowCircle"
              fill="#ffcc05"
              d="M180.23,93.77a85,85,0,1,1-85-85,85,85,0,0,1,85,85"
              transform="translate(-10.16 -8.73)"
            />

            <!-- دایره سفید دور -->
            <circle
              ref="whiteCircle"
              fill="none"
              stroke="#fff"
              stroke-width="1.5"
              cx="85.04"
              cy="85.04"
              r="78.1"
            />

            <!-- path ها -->
            <path ref="path1" fill="none" stroke="#fff" stroke-width="1.5"
              d="M51.71,60.3l11.8,3.61a26.54,26.54,0,0,0,7.6,1.2A38.34,38.34,0,0,0,75,65c10.21-.54,11.3,8,11.88,13.89.15,1.55-.27,3,.81,4.08-3.17-3-10.22-.86-16,3.76C70.14,88,69.7,76.15,67.55,71.69,65.3,67,64.31,66.78,60,64.57Z"
              transform="translate(-10.16 -8.73)"
            />
            <path ref="path2" fill="none" stroke="#fff" stroke-width="1.5"
              d="M89.22,81.67C114.67,78,107,61.12,110.07,46.37c1.29-6.17,4.32-11.56,7.73-16.78C102,39.81,90.17,51.81,84.3,66.48,88.51,70.2,89.33,75.34,89.22,81.67Z"
              transform="translate(-10.16 -8.73)"
            />
            <path ref="path3" fill="none" stroke="#fff" stroke-width="1.5"
              d="M90.15,65.89a21.63,21.63,0,0,0-2.87,4.39c1.65,3.17,2,7,1.94,11.4a16,16,0,0,1,6.83,1.17c18.08,1.16,18-15,25.51-26.27,3.47-5.26,8.26-9.17,13.35-12.78C116.44,47.53,101,54.36,90.15,65.89Z"
              transform="translate(-10.16 -8.73)"
            />
            <path ref="path4" fill="none" stroke="#fff" stroke-width="1.5"
              d="M97.34,68.25C92.28,70.39,89.82,73,89,76a37.57,37.57,0,0,1,.26,5.72c6-.21,10.66,2.35,14.22,7.4,10,.72,16.67-9.34,26.05-14.55,5.51-3,11.57-4.3,17.75-5.14C129.14,64.15,112.3,63.06,97.34,68.25Z"
              transform="translate(-10.16 -8.73)"
            />
            <path ref="path5" fill="none" stroke="#fff" stroke-width="1.5"
              d="M102.67,75.17c-8-.72-11.6,2.12-13.28,6.5,8.88-.22,15,5.75,18.59,17,6.3-.27,13.16-2.72,20.1-2.84,6.3-.1,12.23,1.65,18.08,3.82C132.66,86.51,118.31,77.62,102.67,75.17Z"
              transform="translate(-10.16 -8.73)"
            />
            <path ref="path6" fill="none" stroke="#fff" stroke-width="1.5"
              d="M87.91,85c-4.48,1.72-5.76,7.5-4.81,13.65,2.65,17.21,21,20.67,29.42,44.16a117.24,117.24,0,0,0-6.32-43.12C103.79,93,96.35,81.72,87.91,85Z"
              transform="translate(-10.16 -8.73)"
            />
            <path ref="path7" fill="none" stroke="#fff" stroke-width="1.5"
              d="M89,85.17c-5.9-.25-9.48,7.37-10.18,16C77.2,120.57,92.91,129.31,92.93,158a142.83,142.83,0,0,0,9.39-49.46C102.29,100.32,98.81,85.6,89,85.17Z"
              transform="translate(-10.16 -8.73)"
            />
            <path ref="path8" fill="none" stroke="#fff" stroke-width="1.5"
              d="M89,85.48c-5.46-2.26-11.42,3.68-15,11.56-8.11,17.67,3.66,31.26-6.12,58.18A142.72,142.72,0,0,0,93.54,112C96.31,104.27,98.08,89.24,89,85.48Z"
              transform="translate(-10.16 -8.73)"
            />
            <path ref="path9" fill="none" stroke="#fff" stroke-width="1.5"
              d="M88.47,86.2c-3.54-3.86-10.4-1.63-16.37,3.11-14.21,11.28-10.57,29-28.95,47.42A133,133,0,0,0,81.9,110.35C87.26,105,94.67,93,88.47,86.2Z"
              transform="translate(-10.16 -8.73)"
            />
          </svg>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import gsap from 'gsap'

import { useRoute } from 'vue-router'
import { computed } from 'vue'

const isLoading = useLoadingState()
const route = useRoute()

// هنگام رفتن به صفحه landing، بلافاصله loading را غیرفعال کن
const isLanding = computed(() => route.path === '/landing')

// اگر کاربر به صفحه landing برود، loading را غیرفعال کن
watch(isLanding, (newVal) => {
  if (newVal) {
    isLoading.value = false
  }
}, { immediate: true })
const yellowCircle = ref(null)
const whiteCircle = ref(null)
const path1 = ref(null)
const path2 = ref(null)
const path3 = ref(null)
const path4 = ref(null)
const path5 = ref(null)
const path6 = ref(null)
const path7 = ref(null)
const path8 = ref(null)
const path9 = ref(null)

onMounted(() => {
  let loadComplete = false
  let minTimeComplete = false

  // آماده‌سازی انیمیشن SVG
  const paths = [
    whiteCircle.value,
    path1.value,
    path2.value,
    path3.value,
    path4.value,
    path5.value,
    path6.value,
    path7.value,
    path8.value,
    path9.value
  ]

  // آماده‌سازی line-draw
  paths.forEach(p => {
    if (p) {
      const length = p.getTotalLength()
      p.style.strokeDasharray = length
      p.style.strokeDashoffset = length
    }
  })

  const tl = gsap.timeline({ repeat: -1 })

  // انیمیشن دایره زرد
  tl.fromTo(
    yellowCircle.value,
    { scale: 0, opacity: 0, transformOrigin: '50% 50%' },
    { scale: 1, opacity: 1, duration: 0.6, ease: 'power2.out' }
  )

  // رسم مسیرها
  paths.forEach(p => {
    if (p) {
      tl.to(p, {
        strokeDashoffset: 0,
        duration: 0.18,
        ease: 'none'
      })
    }
  })

  // مکث
  tl.to({}, { duration: 1 })

  // ریست
  tl.set(paths, {
    strokeDashoffset: (i, t) => t?.getTotalLength?.() || 0
  })
  tl.set(yellowCircle.value, { scale: 0, opacity: 0 })

  // Check when page is fully loaded
  const handleLoad = () => {
    loadComplete = true
    checkBothComplete()
  }

  // Minimum 3 seconds delay
  setTimeout(() => {
    minTimeComplete = true
    checkBothComplete()
  }, 3000)

  // Hide loader only when both conditions are met
  const checkBothComplete = () => {
    if (loadComplete && minTimeComplete) {
      isLoading.value = false
    }
  }

  window.addEventListener('load', handleLoad)

  // Fallback: if already loaded before component mounts
  if (document.readyState === 'complete') {
    loadComplete = true
    checkBothComplete()
  }
})
</script>

<style scoped>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #ffffff;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background-color: transparent;
}

.loader-svg {
  max-width: 160px;
  max-height: 160px;
  width: 100%;
  height: auto;
  display: block;
  border: none;
  outline: none;
}

/* hide all strokes initially until animation runs */
.loader-svg path,
.loader-svg circle {
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>