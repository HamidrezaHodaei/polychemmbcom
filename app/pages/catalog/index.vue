<template>
  <div class="screen">
    <!-- Full-screen background photo -->
    <img
      class="bg-image"
      src="https://picsum.photos/id/292/900/1200"
      alt="Fresh crispy chips"
      loading="eager"
    />
    <div class="overlay"></div>

    <!-- Everything below sits on top of the photo -->
    <div class="content">
      <!-- Status bar -->
      <div class="status-bar">
     
        <div class="status-icons">
          <!-- signal bars kept, wifi + battery icons removed -->
         
        </div>
      </div>

      <!-- Title/subtitle moved up, above the button -->
      <div class="text-block">
        <h1 class="title">
          Crunch The
          <span class="title-accent">Moment</span>
        </h1>
        <p class="subtitle">
          Satisfy your craving with bold flavors and irresistible crispiness. Fresh chips, fast delivery.
        </p>
      </div>

      <div class="spacer"></div>

      <!-- Slide-to-start button: draggable, functional, sits at the bottom -->
      <div class="cta-track" ref="trackRef">
        <div class="cta-fill" :style="{ width: fillWidth + 'px' }"></div>

        <span class="cta-label" :style="{ opacity: labelOpacity }">
          {{ completed ? "LET'S GO!" : 'SLIDE TO GET STARTED' }}
        </span>

        <div
          class="cta-thumb"
          :class="{ dragging, completed }"
          :style="{ transform: `translateX(${thumbX}px)` }"
          @pointerdown="onPointerDown"
        >
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M2 8H14M14 8L9 3M14 8L9 13" stroke="#E9772E" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const emit = defineEmits(['get-started'])

const trackRef = ref(null)
const thumbX = ref(0)
const dragging = ref(false)
const completed = ref(false)

const THUMB_SIZE = 46
const TRACK_PADDING = 6
let maxX = 0

function updateMaxX() {
  if (trackRef.value) {
    maxX = trackRef.value.offsetWidth - THUMB_SIZE - TRACK_PADDING * 2
    if (completed.value) thumbX.value = maxX
  }
}

const fillWidth = computed(() => thumbX.value + THUMB_SIZE + TRACK_PADDING)
const labelOpacity = computed(() => {
  if (!maxX) return 1
  return Math.max(0, 1 - (thumbX.value / maxX) * 1.6)
})

let startClientX = 0
let startThumbX = 0

function getClientX(e) {
  return e.touches ? e.touches[0].clientX : e.clientX
}

function onPointerDown(e) {
  if (completed.value) return
  dragging.value = true
  startClientX = getClientX(e)
  startThumbX = thumbX.value
  window.addEventListener('pointermove', onPointerMove)
  window.addEventListener('pointerup', onPointerUp)
  window.addEventListener('touchmove', onPointerMove, { passive: false })
  window.addEventListener('touchend', onPointerUp)
}

function onPointerMove(e) {
  if (!dragging.value) return
  if (e.cancelable) e.preventDefault()
  const delta = getClientX(e) - startClientX
  thumbX.value = Math.max(0, Math.min(maxX, startThumbX + delta))
}

function onPointerUp() {
  dragging.value = false
  window.removeEventListener('pointermove', onPointerMove)
  window.removeEventListener('pointerup', onPointerUp)
  window.removeEventListener('touchmove', onPointerMove)
  window.removeEventListener('touchend', onPointerUp)

  if (maxX > 0 && thumbX.value >= maxX * 0.85) {
    thumbX.value = maxX
    completed.value = true
    handleGetStarted()
  } else {
    thumbX.value = 0
  }
}

function handleGetStarted() {
  // Wire this up to routing, an API call, etc.
  emit('get-started')
}

onMounted(() => {
  updateMaxX()
  window.addEventListener('resize', updateMaxX)
})
onBeforeUnmount(() => {
  window.removeEventListener('resize', updateMaxX)
  window.removeEventListener('pointermove', onPointerMove)
  window.removeEventListener('pointerup', onPointerUp)
  window.removeEventListener('touchmove', onPointerMove)
  window.removeEventListener('touchend', onPointerUp)
})
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.screen {
  width: 100%;
  max-width: 480px;
  min-height: 100dvh;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
  background: #14140f;
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
  display: flex;
  flex-direction: column;
}

/* ---------- Background photo (fills the whole screen) ---------- */
.bg-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  z-index: 0;
}

.overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(10,10,8,0.55) 0%,
    rgba(10,10,8,0.25) 30%,
    rgba(10,10,8,0.45) 60%,
    rgba(8,8,6,0.92) 100%
  );
  z-index: 1;
}

/* ---------- Content (overlaid on top of the photo) ---------- */
.content {
  position: relative;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100dvh;
  padding: 0 clamp(18px, 6vw, 28px) max(16px, env(safe-area-inset-bottom));
  z-index: 5;
}

/* ---------- Status bar ---------- */
.status-bar {
  flex-shrink: 0;
  height: max(44px, env(safe-area-inset-top));
  margin: 0 clamp(-18px, -6vw, -28px);
  padding: 0 clamp(16px, 5vw, 22px);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.time {
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: 0.2px;
}
.status-icons {
  display: flex;
  align-items: center;
  gap: 6px;
}

/* ---------- Text block (moved up, sits above the button) ---------- */
.text-block {
  margin-top: clamp(28px, 8vh, 56px);
}

.title {
  margin: 0 0 12px 0;
  font-size: clamp(26px, 8vw, 34px);
  line-height: 1.15;
  font-weight: 800;
  color: #ffffff;
}
.title-accent {
  display: block;
  color: #f0862c;
}

.subtitle {
  margin: 0;
  font-size: clamp(13px, 3.6vw, 14.5px);
  line-height: 1.5;
  color: rgba(255,255,255,0.75);
  max-width: 320px;
}

.spacer {
  flex: 1;
  min-height: 24px;
}

/* ---------- Slide-to-start button ---------- */
.cta-track {
  position: relative;
  width: 100%;
  height: 58px;
  border-radius: 29px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
  display: flex;
  align-items: center;
  overflow: hidden;
  touch-action: none;
}

.cta-fill {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  border-radius: 29px;
  background: linear-gradient(180deg, #f6923a, #ea7a1f);
  transition: width 0.05s linear;
}

.cta-label {
  position: relative;
  width: 100%;
  text-align: center;
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1px;
  pointer-events: none;
  transition: opacity 0.1s linear;
}

.cta-thumb {
  position: absolute;
  top: 6px;
  left: 6px;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: grab;
  touch-action: none;
  box-shadow: 0 6px 14px rgba(0,0,0,0.35);
}
.cta-thumb.dragging {
  cursor: grabbing;
  transition: none;
}
.cta-thumb:not(.dragging) {
  transition: transform 0.25s ease;
}
.cta-thumb.completed {
  background: #fff;
}

/* ---------- Home indicator ---------- */
.home-indicator {
  width: 134px;
  height: 5px;
  border-radius: 3px;
  background: rgba(255,255,255,0.4);
  margin: 14px auto 0;
}

/* ---------- Small phone tweak ---------- */
@media (max-width: 360px) {
  .text-block {
    margin-top: clamp(20px, 6vh, 40px);
  }
}
</style>