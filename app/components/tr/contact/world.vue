<template>
  <div class="w-full h-screen overflow-hidden relative" style="background-color: #f1f2f2;">
    <canvas ref="globeCanvas" class="w-full h-full"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const globeCanvas = ref(null)

onMounted(() => {
  if (!globeCanvas.value) return

  const canvas = globeCanvas.value
  const ctx = canvas.getContext('2d')
  
  let width = canvas.width = window.innerWidth
  let height = canvas.height = window.innerHeight
  
  // Mouse tracking
  let mouseX = 0
  let mouseY = 0
  let isDragging = false
  let lastMouseX = 0
  let lastMouseY = 0
  
  // Globe rotation
  let rotationX = 0
  let rotationY = 0
  let targetRotationX = 0
  let targetRotationY = 0
  let velocityX = 0
  let velocityY = 0
  
  // Globe settings
  const radius = Math.min(width, height) * 0.45
  const centerX = width / 2
  const centerY = height / 2
  
  // Auto-rotation speed
  const autoRotationSpeed = 0.001
  
  // Create dots for globe surface
  const dots = []
  const numLat = 40
  const numLon = 80
  
  // Generate dots in a sphere pattern
  for (let lat = 0; lat < numLat; lat++) {
    for (let lon = 0; lon < numLon; lon++) {
      const theta = (lat / numLat) * Math.PI
      const phi = (lon / numLon) * Math.PI * 2
      
      dots.push({
        theta,
        phi,
        baseBrightness: Math.random() * 0.3 + 0.7
      })
    }
  }
  
  // Location markers for Middle East countries (approximate positions)
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
    // Convert spherical to Cartesian
    let x = Math.sin(theta) * Math.cos(phi)
    let y = Math.cos(theta)
    let z = Math.sin(theta) * Math.sin(phi)
    
    // Rotate around Y axis
    const cosY = Math.cos(rotY)
    const sinY = Math.sin(rotY)
    const tempX = x * cosY - z * sinY
    const tempZ = x * sinY + z * cosY
    x = tempX
    z = tempZ
    
    // Rotate around X axis
    const cosX = Math.cos(rotX)
    const sinX = Math.sin(rotX)
    const tempY = y * cosX - z * sinX
    z = y * sinX + z * cosX
    y = tempY
    
    // Project to 2D
    const scale = radius / (radius + z * 0.5)
    const x2d = centerX + x * radius * scale
    const y2d = centerY + y * radius * scale
    
    return { x: x2d, y: y2d, z, scale, visible: z > -radius * 0.3 }
  }
  
  function drawGlobe() {
    ctx.fillStyle = '#f1f2f2'
    ctx.fillRect(0, 0, width, height)
    
    // Draw all dots
    const allPoints = []
    
    // Regular grid dots
    dots.forEach(dot => {
      const pos = project3DTo2D(dot.theta, dot.phi, rotationX, rotationY)
      if (pos.visible) {
        allPoints.push({
          x: pos.x,
          y: pos.y,
          z: pos.z,
          brightness: dot.baseBrightness * pos.scale,
          size: 1.5 * pos.scale,
          type: 'dot'
        })
      }
    })
    
    // Location markers
    locationMarkers.forEach(marker => {
      const pos = project3DTo2D(marker.theta, marker.phi, rotationX, rotationY)
      if (pos.visible) {
        allPoints.push({
          x: pos.x,
          y: pos.y,
          z: pos.z,
          scale: pos.scale,
          type: 'marker',
          name: marker.name
        })
      }
    })
    
    // Sort by z-depth
    allPoints.sort((a, b) => a.z - b.z)
    
    // Draw dots and markers
    allPoints.forEach(point => {
      if (point.type === 'dot') {
        const alpha = Math.max(0, Math.min(1, point.brightness))
        const grayValue = Math.floor(132 * alpha) // #848484 = rgb(132, 132, 132)
        
        ctx.fillStyle = `rgba(${grayValue}, ${grayValue}, ${grayValue}, ${alpha})`
        ctx.beginPath()
        ctx.arc(point.x, point.y, point.size, 0, Math.PI * 2)
        ctx.fill()
      } else if (point.type === 'marker') {
        const markerSize = 8 * point.scale
        
        // Draw pin shape
        ctx.fillStyle = '#FFD700'
        ctx.strokeStyle = '#FFFFFF'
        ctx.lineWidth = 2 * point.scale
        
        // Pin circle
        ctx.beginPath()
        ctx.arc(point.x, point.y - markerSize * 0.5, markerSize * 0.6, 0, Math.PI * 2)
        ctx.fill()
        ctx.stroke()
        
        // Pin point
        ctx.beginPath()
        ctx.moveTo(point.x, point.y)
        ctx.lineTo(point.x - markerSize * 0.3, point.y - markerSize * 0.8)
        ctx.lineTo(point.x + markerSize * 0.3, point.y - markerSize * 0.8)
        ctx.closePath()
        ctx.fill()
        ctx.stroke()
        
        // Glow effect
        const gradient = ctx.createRadialGradient(
          point.x, 
          point.y - markerSize * 0.5, 
          0, 
          point.x, 
          point.y - markerSize * 0.5, 
          markerSize * 2
        )
        gradient.addColorStop(0, 'rgba(255, 215, 0, 0.4)')
        gradient.addColorStop(1, 'rgba(255, 215, 0, 0)')
        ctx.fillStyle = gradient
        ctx.beginPath()
        ctx.arc(point.x, point.y - markerSize * 0.5, markerSize * 2, 0, Math.PI * 2)
        ctx.fill()
      }
    })
    
    // Draw globe outline/edge glow
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
    // Auto-rotation (always active)
    if (!isDragging) {
      targetRotationY += autoRotationSpeed
    }
    
    // Smooth rotation interpolation
    rotationX += (targetRotationX - rotationX) * 0.1
    rotationY += (targetRotationY - rotationY) * 0.1
    
    // Add momentum/inertia
    if (!isDragging) {
      targetRotationY += velocityX
      targetRotationX += velocityY
      velocityX *= 0.95
      velocityY *= 0.95
    }
    
    drawGlobe()
    requestAnimationFrame(animate)
  }
  
  // Mouse event handlers
  function handleMouseDown(e) {
    isDragging = true
    lastMouseX = e.clientX
    lastMouseY = e.clientY
    velocityX = 0
    velocityY = 0
  }
  
  function handleMouseMove(e) {
    mouseX = e.clientX
    mouseY = e.clientY
    
    if (isDragging) {
      const deltaX = e.clientX - lastMouseX
      const deltaY = e.clientY - lastMouseY
      
      velocityX = deltaX * 0.005
      velocityY = deltaY * 0.005
      
      targetRotationY += deltaX * 0.005
      targetRotationX += deltaY * 0.005
      
      lastMouseX = e.clientX
      lastMouseY = e.clientY
    }
  }
  
  function handleMouseUp() {
    isDragging = false
  }
  
  function handleResize() {
    width = canvas.width = window.innerWidth
    height = canvas.height = window.innerHeight
  }
  
  // Touch events for mobile
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
  
  // Add event listeners
  canvas.addEventListener('mousedown', handleMouseDown)
  canvas.addEventListener('mousemove', handleMouseMove)
  canvas.addEventListener('mouseup', handleMouseUp)
  canvas.addEventListener('mouseleave', handleMouseUp)
  canvas.addEventListener('touchstart', handleTouchStart, { passive: false })
  canvas.addEventListener('touchmove', handleTouchMove, { passive: false })
  canvas.addEventListener('touchend', handleTouchEnd, { passive: false })
  window.addEventListener('resize', handleResize)
  
  // Start animation
  animate()
  
  // Cleanup
  onUnmounted(() => {
    canvas.removeEventListener('mousedown', handleMouseDown)
    canvas.removeEventListener('mousemove', handleMouseMove)
    canvas.removeEventListener('mouseup', handleMouseUp)
    canvas.removeEventListener('mouseleave', handleMouseUp)
    canvas.removeEventListener('touchstart', handleTouchStart)
    canvas.removeEventListener('touchmove', handleTouchMove)
    canvas.removeEventListener('touchend', handleTouchEnd)
    window.removeEventListener('resize', handleResize)
  })
})
</script>

<style scoped>
canvas {
  cursor: grab;
}

canvas:active {
  cursor: grabbing;
}
</style>