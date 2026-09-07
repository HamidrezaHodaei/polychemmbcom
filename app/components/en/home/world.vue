<!-- /components/en/home/world.vue -->
<template>
  <div class="globe-text-wrapper">
    <div class="globe-side">
      <canvas ref="globeCanvas" class="w-full h-full"></canvas>
    </div>
    <div class="text-side">
      <Textworld />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Textworld from './textworld.vue'

const globeCanvas = ref(null)

onMounted(() => {
  if (!globeCanvas.value) return

  const canvas = globeCanvas.value
  const ctx = canvas.getContext('2d')
  const dpr = window.devicePixelRatio || 1

  let width = 0, height = 0
  let isDragging = false
  let lastMouseX = 0, lastMouseY = 0
  let rotationX = 0, rotationY = 0
  let targetRotationX = -0.35, targetRotationY = 0
  let velocityX = 0, velocityY = 0
  let radius = 0, centerX = 0, centerY = 0

  const autoRotationSpeed = 0.003
  const dots = []

  for (let lat = 0; lat < 40; lat++) {
    for (let lon = 0; lon < 80; lon++) {
      dots.push({
        theta: (lat / 40) * Math.PI,
        phi: (lon / 80) * Math.PI * 2,
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

  function project3DTo2D(theta, phi, rotX, rotY) {
    let x = Math.sin(theta) * Math.cos(phi)
    let y = Math.cos(theta)
    let z = Math.sin(theta) * Math.sin(phi)

    const cosY = Math.cos(rotY), sinY = Math.sin(rotY)
    const tempX = x * cosY - z * sinY
    const tempZ = x * sinY + z * cosY
    x = tempX; z = tempZ

    const cosX = Math.cos(rotX), sinX = Math.sin(rotX)
    const tempY = y * cosX - z * sinX
    z = y * sinX + z * cosX
    y = tempY

    const scale = radius / (radius + z * 0.5)
    return {
      x: centerX + x * radius * scale,
      y: centerY + y * radius * scale,
      z, scale,
      visible: z > -radius * 0.3
    }
  }

  function drawGlobe() {
    ctx.fillStyle = '#f1f2f2'
    ctx.fillRect(0, 0, width, height)

    const allPoints = []

    dots.forEach(dot => {
      const pos = project3DTo2D(dot.theta, dot.phi, rotationX, rotationY)
      if (pos.visible) {
        allPoints.push({
          x: pos.x, y: pos.y, z: pos.z,
          brightness: dot.baseBrightness * pos.scale,
          size: 1.5 * pos.scale,
          type: 'dot'
        })
      }
    })

    locationMarkers.forEach(marker => {
      const pos = project3DTo2D(marker.theta, marker.phi, rotationX, rotationY)
      if (pos.visible) {
        allPoints.push({ x: pos.x, y: pos.y, z: pos.z, scale: pos.scale, type: 'marker', name: marker.name })
      }
    })

    allPoints.sort((a, b) => a.z - b.z)

    allPoints.forEach(point => {
      if (point.type === 'dot') {
        const alpha = Math.max(0, Math.min(1, point.brightness))
        const grayValue = Math.floor(132 * alpha)
        ctx.fillStyle = `rgba(${grayValue}, ${grayValue}, ${grayValue}, ${alpha})`
        ctx.beginPath()
        ctx.arc(point.x, point.y, point.size, 0, Math.PI * 2)
        ctx.fill()
      } else if (point.type === 'marker') {
        const markerSize = 12 * point.scale
        ctx.fillStyle = '#FFCC00'
        ctx.strokeStyle = 'rgba(255,255,255,0.9)'
        ctx.lineWidth = 3 * point.scale

        ctx.beginPath()
        ctx.arc(point.x, point.y - markerSize * 0.5, markerSize * 0.8, 0, Math.PI * 2)
        ctx.fill()
        ctx.stroke()

        ctx.beginPath()
        ctx.moveTo(point.x, point.y)
        ctx.lineTo(point.x - markerSize * 0.35, point.y - markerSize * 0.95)
        ctx.lineTo(point.x + markerSize * 0.35, point.y - markerSize * 0.95)
        ctx.closePath()
        ctx.fill()
        ctx.stroke()

        const gradient = ctx.createRadialGradient(
          point.x, point.y - markerSize * 0.5, 0,
          point.x, point.y - markerSize * 0.5, markerSize * 2.5
        )
        gradient.addColorStop(0, 'rgba(255, 215, 0, 0.6)')
        gradient.addColorStop(1, 'rgba(255, 215, 0, 0)')
        ctx.fillStyle = gradient
        ctx.beginPath()
        ctx.arc(point.x, point.y - markerSize * 0.5, markerSize * 2.5, 0, Math.PI * 2)
        ctx.fill()

        ctx.fillStyle = 'rgba(255,255,255,0.9)'
        ctx.beginPath()
        ctx.arc(point.x - markerSize * 0.18, point.y - markerSize * 0.7, markerSize * 0.18, 0, Math.PI * 2)
        ctx.fill()
      }
    })

    const gradient = ctx.createRadialGradient(centerX, centerY, radius * 0.8, centerX, centerY, radius * 1.1)
    gradient.addColorStop(0, 'rgba(132, 132, 132, 0)')
    gradient.addColorStop(0.8, 'rgba(132, 132, 132, 0.1)')
    gradient.addColorStop(1, 'rgba(132, 132, 132, 0)')
    ctx.fillStyle = gradient
    ctx.beginPath()
    ctx.arc(centerX, centerY, radius * 1.1, 0, Math.PI * 2)
    ctx.fill()
  }

  function animate() {
    rotationX += (targetRotationX - rotationX) * 0.1
    rotationY += (targetRotationY - rotationY) * 0.1
    if (!isDragging) {
      targetRotationY += velocityX
      targetRotationX += velocityY
      targetRotationY += autoRotationSpeed
      velocityX *= 0.95
      velocityY *= 0.95
    }
    drawGlobe()
    requestAnimationFrame(animate)
  }

  function handleMouseDown(e) {
    isDragging = true
    lastMouseX = e.clientX
    lastMouseY = e.clientY
    velocityX = 0
    velocityY = 0
  }

  function handleMouseMove(e) {
    if (isDragging) {
      const deltaX = e.clientX - lastMouseX
      const deltaY = e.clientY - lastMouseY
      velocityX = deltaX * 0.007
      velocityY = deltaY * 0.007
      targetRotationY += deltaX * 0.007
      targetRotationX += deltaY * 0.007
      lastMouseX = e.clientX
      lastMouseY = e.clientY
    }
  }

  function handleMouseUp() { isDragging = false }

  function resizeCanvasToDisplaySize() {
    const rect = canvas.getBoundingClientRect()
    width = rect.width
    height = rect.height

    canvas.width = Math.round(rect.width * dpr)
    canvas.height = Math.round(rect.height * dpr)
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)

    if (width < 600) {
      radius = Math.min(width, height) * 0.48
      centerX = width / 2
    } else if (width < 1024) {
      radius = Math.min(width, height) * 0.44
      centerX = width / 2
    } else {
      radius = Math.min(width, height) * 0.40
      centerX = width * 0.38
    }
    centerY = height / 2
  }

  function handleTouchStart(e) {
    e.preventDefault()
    const touch = e.touches[0]
    handleMouseDown({ clientX: touch.clientX, clientY: touch.clientY })
  }
  function handleTouchMove(e) {
    e.preventDefault()
    const touch = e.touches[0]
    handleMouseMove({ clientX: touch.clientX, clientY: touch.clientY })
  }
  function handleTouchEnd(e) {
    e.preventDefault()
    handleMouseUp()
  }

  canvas.addEventListener('mousedown', handleMouseDown)
  canvas.addEventListener('mousemove', handleMouseMove)
  canvas.addEventListener('mouseup', handleMouseUp)
  canvas.addEventListener('mouseleave', handleMouseUp)
  canvas.addEventListener('touchstart', handleTouchStart, { passive: false })
  canvas.addEventListener('touchmove', handleTouchMove, { passive: false })
  canvas.addEventListener('touchend', handleTouchEnd, { passive: false })
  window.addEventListener('resize', resizeCanvasToDisplaySize)

  resizeCanvasToDisplaySize()
  animate()

  onUnmounted(() => {
    canvas.removeEventListener('mousedown', handleMouseDown)
    canvas.removeEventListener('mousemove', handleMouseMove)
    canvas.removeEventListener('mouseup', handleMouseUp)
    canvas.removeEventListener('mouseleave', handleMouseUp)
    canvas.removeEventListener('touchstart', handleTouchStart)
    canvas.removeEventListener('touchmove', handleTouchMove)
    canvas.removeEventListener('touchend', handleTouchEnd)
    window.removeEventListener('resize', resizeCanvasToDisplaySize)
  })
})
</script>

<style scoped>
.globe-text-wrapper {
  display: flex;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  background-color: #f1f2f2;
  align-items: stretch;
}

/* ===== DESKTOP (1024px+) ===== */
.globe-side {
  width: 50%;
  height: 100%;
  min-height: 100%;
  box-sizing: border-box;
}
.text-side {
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

/* ===== TABLET (600px – 1023px) ===== */
@media (min-width: 600px) and (max-width: 1023px) {
  .globe-text-wrapper {
    flex-direction: column;
    height: auto;
    min-height: unset; /* ← سفیدی اضافه حذف شد */
  }
  .globe-side {
    width: 100%;
    height: 40vh;
    min-height: 260px;
  }
  .text-side {
    width: 100%;
    height: auto;
    padding: 12px 24px;
  }
}

/* ===== LAPTOP (1024px – 1365px) ===== */
@media (min-width: 1024px) and (max-width: 1365px) {
  .globe-side {
    width: 48%;
    height: 100%;
  }
  .text-side {
    width: 52%;
    height: 100%;
    padding: 0 20px;
  }
}

/* ===== MOBILE (max 599px) ===== */
@media (max-width: 599px) {
  .globe-text-wrapper {
    flex-direction: column;
    height: auto;
  }
  .globe-side {
    width: 100%;
    height: 50vh;
    min-height: 40vh;
  }
  .text-side {
    width: 100%;
    padding: 12px 16px;
    height: auto;
  }
}
/* ===== 125% ZOOM (Desktop) ===== */
@media (min-width: 1024px) and (max-width: 1365px) and (min-resolution: 120dpi) {
  .globe-side {
    width: 47%;
    height: 100%;
  }
  .text-side {
    width: 53%;
    height: 100%;
    padding: 0 16px;
  }
}

@media (min-width: 1366px) and (min-resolution: 120dpi) {
  .globe-side {
    width: 48%;
    height: 100%;
  }
  .text-side {
    width: 52%;
    height: 100%;
    padding: 0 16px;
  }
}

/* ===== 150% ZOOM (Desktop) ===== */
@media (min-width: 1024px) and (max-width: 1365px) and (min-resolution: 144dpi) {
  .globe-side {
    width: 46%;
    height: 100%;
  }
  .text-side {
    width: 54%;
    height: 100%;
    padding: 0 12px;
  }
}

@media (min-width: 1366px) and (min-resolution: 144dpi) {
  .globe-side {
    width: 46%;
    height: 100%;
  }
  .text-side {
    width: 54%;
    height: 100%;
    padding: 0 12px;
  }
}
canvas {
  width: 100% !important;
  height: 100% !important;
  display: block;
}
</style>