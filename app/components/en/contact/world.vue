<template>
  <div class="globe-wrapper">
    <canvas ref="globeCanvas"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const globeCanvas = ref(null)

onMounted(() => {
  if (!globeCanvas.value) return

  const canvas = globeCanvas.value
  const ctx = canvas.getContext('2d')

  let width, height, radius, centerX, centerY
  let animFrameId = null

  // ─── مهم‌ترین بخش: DPI-aware canvas sizing ───────────────────────────────
  function updateDimensions() {
    const dpr = window.devicePixelRatio || 1
    const rect = canvas.parentElement.getBoundingClientRect()

    // اندازه CSS (برای layout)
    width  = rect.width
    height = rect.height
    canvas.style.width  = width  + 'px'
    canvas.style.height = height + 'px'

    // اندازه واقعی pixel buffer (با DPR)
    canvas.width  = Math.round(width  * dpr)
    canvas.height = Math.round(height * dpr)

    // scale کردن context تا همه چیز sharp بمونه
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)

    // حالا radius و center رو با CSS size حساب می‌کنیم
    const minDim = Math.min(width, height)
    // برای موبایل عمودی کوچیک‌تر، برای دسکتاپ بزرگ‌تر
    const factor = width < 480 ? 0.38
                 : width < 900 ? 0.42
                 : 0.45
    radius  = minDim * factor
    centerX = width  / 2
    centerY = height / 2
  }

  // ─── Mouse / Touch tracking ───────────────────────────────────────────────
  let isDragging = false
  let lastX = 0, lastY = 0

  // ─── Globe rotation state ─────────────────────────────────────────────────
  let rotationX = 0, rotationY = 0
  let targetRotationX = 0, targetRotationY = 0
  let velocityX = 0, velocityY = 0
  const autoRotationSpeed = 0.001

  // ─── Globe dots ───────────────────────────────────────────────────────────
  const dots = []
  const numLat = 40
  const numLon = 80
  for (let lat = 0; lat < numLat; lat++) {
    for (let lon = 0; lon < numLon; lon++) {
      dots.push({
        theta: (lat / numLat) * Math.PI,
        phi:   (lon / numLon) * Math.PI * 2,
        baseBrightness: Math.random() * 0.3 + 0.7
      })
    }
  }

  const locationMarkers = [
    { theta: Math.PI * 0.42, phi: Math.PI * 1.15, name: 'Iran' },
    { theta: Math.PI * 0.52, phi: Math.PI * 1.08, name: 'Saudi Arabia' },
    { theta: Math.PI * 0.48, phi: Math.PI * 1.18, name: 'UAE' },
    { theta: Math.PI * 0.38, phi: Math.PI * 1.05, name: 'Turkey' },
    { theta: Math.PI * 0.50, phi: Math.PI * 1.14, name: 'Qatar' },
    { theta: Math.PI * 0.44, phi: Math.PI * 1.08, name: 'Iraq' },
    { theta: Math.PI * 0.46, phi: Math.PI * 1.12, name: 'Kuwait' },
    { theta: Math.PI * 0.54, phi: Math.PI * 1.02, name: 'Yemen' }
  ]

  // ─── Projection ───────────────────────────────────────────────────────────
  function project3DTo2D(theta, phi, rotX, rotY) {
    let x = Math.sin(theta) * Math.cos(phi)
    let y = Math.cos(theta)
    let z = Math.sin(theta) * Math.sin(phi)

    // rotate Y
    const cosY = Math.cos(rotY), sinY = Math.sin(rotY)
    const tx = x * cosY - z * sinY
    z = x * sinY + z * cosY
    x = tx

    // rotate X
    const cosX = Math.cos(rotX), sinX = Math.sin(rotX)
    const ty = y * cosX - z * sinX
    z = y * sinX + z * cosX
    y = ty

    const scale = radius / (radius + z * 0.5)
    return {
      x: centerX + x * radius * scale,
      y: centerY + y * radius * scale,
      z,
      scale,
      visible: z > -radius * 0.3
    }
  }

  // ─── Draw ─────────────────────────────────────────────────────────────────
  function drawGlobe() {
    ctx.clearRect(0, 0, width, height)
    ctx.fillStyle = '#f1f2f2'
    ctx.fillRect(0, 0, width, height)

    const markerSize = Math.max(6, radius * 0.06)   // proportional to globe

    const allPoints = []

    dots.forEach(dot => {
      const pos = project3DTo2D(dot.theta, dot.phi, rotationX, rotationY)
      if (pos.visible) {
        allPoints.push({
          x: pos.x, y: pos.y, z: pos.z,
          brightness: dot.baseBrightness * pos.scale,
          size: Math.max(0.8, 1.5 * pos.scale),
          type: 'dot'
        })
      }
    })

    locationMarkers.forEach(marker => {
      const pos = project3DTo2D(marker.theta, marker.phi, rotationX, rotationY)
      if (pos.visible) {
        allPoints.push({
          x: pos.x, y: pos.y, z: pos.z,
          scale: pos.scale,
          type: 'marker',
          name: marker.name,
          ms: markerSize * pos.scale
        })
      }
    })

    allPoints.sort((a, b) => a.z - b.z)

    allPoints.forEach(p => {
      if (p.type === 'dot') {
        const alpha = Math.max(0, Math.min(1, p.brightness))
        const g = Math.floor(132 * alpha)
        ctx.fillStyle = `rgba(${g},${g},${g},${alpha})`
        ctx.beginPath()
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2)
        ctx.fill()

      } else {
        const ms = p.ms

        // glow
        const grd = ctx.createRadialGradient(p.x, p.y - ms * 0.5, 0, p.x, p.y - ms * 0.5, ms * 2)
        grd.addColorStop(0, 'rgba(255,215,0,0.4)')
        grd.addColorStop(1, 'rgba(255,215,0,0)')
        ctx.fillStyle = grd
        ctx.beginPath()
        ctx.arc(p.x, p.y - ms * 0.5, ms * 2, 0, Math.PI * 2)
        ctx.fill()

        // pin head
        ctx.fillStyle   = '#FFD700'
        ctx.strokeStyle = '#FFFFFF'
        ctx.lineWidth   = Math.max(1, 2 * p.scale)
        ctx.beginPath()
        ctx.arc(p.x, p.y - ms * 0.5, ms * 0.6, 0, Math.PI * 2)
        ctx.fill()
        ctx.stroke()

        // pin body
        ctx.beginPath()
        ctx.moveTo(p.x, p.y)
        ctx.lineTo(p.x - ms * 0.3, p.y - ms * 0.8)
        ctx.lineTo(p.x + ms * 0.3, p.y - ms * 0.8)
        ctx.closePath()
        ctx.fill()
        ctx.stroke()
      }
    })

    // edge vignette
    const vignette = ctx.createRadialGradient(centerX, centerY, radius * 0.8, centerX, centerY, radius * 1.1)
    vignette.addColorStop(0, 'rgba(132,132,132,0)')
    vignette.addColorStop(0.8, 'rgba(132,132,132,0.1)')
    vignette.addColorStop(1, 'rgba(132,132,132,0)')
    ctx.fillStyle = vignette
    ctx.beginPath()
    ctx.arc(centerX, centerY, radius * 1.1, 0, Math.PI * 2)
    ctx.fill()
  }

  // ─── Animation loop ───────────────────────────────────────────────────────
  function animate() {
    if (!isDragging) targetRotationY += autoRotationSpeed

    rotationX += (targetRotationX - rotationX) * 0.1
    rotationY += (targetRotationY - rotationY) * 0.1

    if (!isDragging) {
      targetRotationY += velocityX
      targetRotationX += velocityY
      velocityX *= 0.95
      velocityY *= 0.95
    }

    drawGlobe()
    animFrameId = requestAnimationFrame(animate)
  }

  // ─── Unified pointer handlers ─────────────────────────────────────────────
  function onPointerDown(x, y) {
    isDragging = true
    lastX = x; lastY = y
    velocityX = 0; velocityY = 0
  }
  function onPointerMove(x, y) {
    if (!isDragging) return
    const dx = x - lastX, dy = y - lastY
    velocityX = dx * 0.005
    velocityY = dy * 0.005
    targetRotationY += dx * 0.005
    targetRotationX += dy * 0.005
    lastX = x; lastY = y
  }
  function onPointerUp() { isDragging = false }

  // Mouse
  const onMouseDown  = e => onPointerDown(e.clientX, e.clientY)
  const onMouseMove  = e => onPointerMove(e.clientX, e.clientY)
  const onMouseUp    = ()  => onPointerUp()

  // Touch — از changedTouches برای touchend استفاده می‌کنیم
  const onTouchStart = e => { e.preventDefault(); const t = e.touches[0];        onPointerDown(t.clientX, t.clientY) }
  const onTouchMove  = e => { e.preventDefault(); const t = e.touches[0];        onPointerMove(t.clientX, t.clientY) }
  const onTouchEnd   = e => { e.preventDefault(); onPointerUp() }

  // Resize — از ResizeObserver به جای window resize استفاده می‌کنیم (دقیق‌تر)
  const ro = new ResizeObserver(() => { updateDimensions() })
  ro.observe(canvas.parentElement)

  canvas.addEventListener('mousedown',  onMouseDown)
  canvas.addEventListener('mousemove',  onMouseMove)
  canvas.addEventListener('mouseup',    onMouseUp)
  canvas.addEventListener('mouseleave', onMouseUp)
  canvas.addEventListener('touchstart', onTouchStart, { passive: false })
  canvas.addEventListener('touchmove',  onTouchMove,  { passive: false })
  canvas.addEventListener('touchend',   onTouchEnd,   { passive: false })

  updateDimensions()
  animate()

  onUnmounted(() => {
    cancelAnimationFrame(animFrameId)
    ro.disconnect()
    canvas.removeEventListener('mousedown',  onMouseDown)
    canvas.removeEventListener('mousemove',  onMouseMove)
    canvas.removeEventListener('mouseup',    onMouseUp)
    canvas.removeEventListener('mouseleave', onMouseUp)
    canvas.removeEventListener('touchstart', onTouchStart)
    canvas.removeEventListener('touchmove',  onTouchMove)
    canvas.removeEventListener('touchend',   onTouchEnd)
  })
})
</script>

<style scoped>
.globe-wrapper {
  width: 100%;
  height: 100vh;           /* یا هر ارتفاعی که می‌خوای */
  overflow: hidden;
  background-color: #f1f2f2;
  position: relative;
}

canvas {
  display: block;          /* حذف فضای زیر inline element */
  cursor: grab;
  touch-action: none;      /* جلوگیری از scroll هنگام drag روی کره */
  /* width/height از طریق JS ست می‌شه */
}

canvas:active {
  cursor: grabbing;
}
</style>