<template>
  <div class="home-wave">
    <canvas ref="canvasRef"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const canvasRef = ref(null);

let animationId = null;
let count = 0;

const SEPARATION = 200;
const AMOUNTX = 40;
const AMOUNTY = 60;

const particles = [];

// Camera settings matching original
const camera = {
  fov: 65,
  position: { x: 0, y: 355, z: 122 },
  aspect: 1,
  near: 1,
  far: 10000
};

// Initialize particles
const initParticles = () => {
  let i = 0;
  for (let ix = 0; ix < AMOUNTX; ix++) {
    for (let iy = 0; iy < AMOUNTY; iy++) {
      particles[i++] = {
        baseX: ix * SEPARATION - ((AMOUNTX * SEPARATION) / 2),
        baseZ: iy * SEPARATION - ((AMOUNTY * SEPARATION) / 2),
        x: 0,
        y: 0,
        z: 0,
        screenX: 0,
        screenY: 0,
        scale: 1
      };
    }
  }
};

// Project 3D point to 2D screen coordinates - matching CanvasRenderer behavior
const project3DTo2D = (worldX, worldY, worldZ, canvasWidth, canvasHeight) => {
  // Calculate view position
  const viewX = worldX - camera.position.x;
  const viewY = worldY - camera.position.y;
  const viewZ = worldZ - camera.position.z;
  
  // Perspective projection
  if (viewZ >= 0) return null; // Behind camera
  
  const fov = (camera.fov * Math.PI) / 180;
  const f = 1 / Math.tan(fov / 2);
  
  const aspect = canvasWidth / canvasHeight;
  
  // Projection matrix calculation
  const projectedX = (viewX * f / aspect) / -viewZ;
  const projectedY = (viewY * f) / -viewZ;
  
  // Convert to screen coordinates
  const halfWidth = canvasWidth / 2;
  const halfHeight = canvasHeight / 2;
  
  return {
    x: projectedX * halfWidth + halfWidth,
    y: -projectedY * halfHeight + halfHeight, // Flip Y axis
    z: viewZ
  };
};

// Render frame
const render = () => {
  const canvas = canvasRef.value;
  if (!canvas) return;
  
  const ctx = canvas.getContext('2d');
  const width = canvas.width;
  const height = canvas.height;
  
  // Clear canvas with white background
  ctx.fillStyle = 'white';
  ctx.fillRect(0, 0, width, height);
  
  // Update camera aspect
  camera.aspect = width / height;
  
  // Update and draw particles
  let i = 0;
  for (let ix = 0; ix < AMOUNTX; ix++) {
    for (let iy = 0; iy < AMOUNTY; iy++) {
      const particle = particles[i++];
      
      // Update position with wave calculation (same as original)
      particle.x = particle.baseX;
      particle.y = (Math.sin((ix + count) * 0.3) * 50) +
                   (Math.sin((iy + count) * 0.5) * 50);
      particle.z = particle.baseZ;
      
      // Update scale (same as original)
      particle.scale = (Math.sin((ix + count) * 0.3) + 1) * 4 +
                       (Math.sin((iy + count) * 0.5) + 1) * 4;
      
      // Project to 2D
      const projected = project3DTo2D(particle.x, particle.y, particle.z, width, height);
      
      if (projected && projected.z < 0) {
        const screenX = projected.x;
        const screenY = projected.y;
        
        // Only draw if on screen
        if (screenX >= -50 && screenX <= width + 50 &&
            screenY >= -50 && screenY <= height + 50) {
          
          // Draw particle - small circle
          ctx.save();
          ctx.translate(screenX, screenY);
          
          // Scale based on particle scale
          const drawScale = particle.scale;
          ctx.scale(drawScale, drawScale);
          
          ctx.beginPath();
          ctx.arc(0, 0, 0.5, 0, Math.PI * 2, true);
          ctx.fillStyle = '#848484'; // Yellow/Gold color
          ctx.fill();
          
          ctx.restore();
        }
      }
    }
  }
  
  count += 0.1;
};

// Animation loop
const animate = () => {
  animationId = requestAnimationFrame(animate);
  render();
};

// Handle window resize
const onWindowResize = () => {
  const canvas = canvasRef.value;
  if (!canvas) return;
  
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  camera.aspect = canvas.width / canvas.height;
};

// Initialize
const init = () => {
  if (!canvasRef.value) return;
  
  const canvas = canvasRef.value;
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  camera.aspect = canvas.width / canvas.height;
  
  initParticles();
  
  window.addEventListener('resize', onWindowResize);
  animate();
};

onMounted(() => {
  init();
});

onUnmounted(() => {
  if (animationId) {
    cancelAnimationFrame(animationId);
  }
  window.removeEventListener('resize', onWindowResize);
});
</script>

<style scoped>
.home-wave {
  position: fixed;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  background: white; /* White background like original */
}

canvas {
  display: block;
  width: 100%;
  height: 100%;
}
</style>