<template>
  <div class="map-wrapper">
    <div ref="mapContainer" class="map-container">
      <iframe
        width="100%"
        height="100%"
        style="border:0;"
        loading="lazy"
        allowfullscreen
        referrerpolicy="no-referrer-when-downgrade"
        :src="`https://maps.google.com/maps?q=${destLat},${destLng}&t=&z=13&ie=UTF8&iwloc=&output=embed`">
      </iframe>
    </div>
    
    <!-- Navigation Button -->
    <div class="routing-button">
      <button @click="getDirections" class="btn-directions">
        <span class="font-[IRANYekan]">مسیریابی</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const mapContainer = ref(null);

const destLat = 38.92111436229225;
const destLng = 45.6492204411566;

const getDirections = () => {
  const ua = navigator.userAgent || '';
  const isIOS = /iPhone|iPad|iPod/i.test(ua);
  const isAndroid = /Android/i.test(ua);
  const isMobile = isIOS || isAndroid;

  // برای موبایل: لینک مستقیم به Google Maps با fallback
  if (isMobile) {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const userLat = position.coords.latitude;
          const userLng = position.coords.longitude;
          
          // لینک مستقیم Google Maps که روی همه موبایل‌ها کار می‌کنه
          const mapsUrl = `https://www.google.com/maps/dir/?api=1&origin=${userLat},${userLng}&destination=${destLat},${destLng}&travelmode=driving`;
          
          if (isIOS) {
            // اول سعی می‌کنیم اپلیکیشن Apple Maps رو باز کنیم
            const appleMapsUrl = `maps://maps.apple.com/?saddr=${userLat},${userLng}&daddr=${destLat},${destLng}&dirflg=d`;
            window.location.href = appleMapsUrl;
            
            // اگر اپلیکیشن نصب نبود، بعد از 500ms به Google Maps می‌ریم
            setTimeout(() => {
              window.location.href = mapsUrl;
            }, 500);
          } else {
            // برای اندروید، مستقیم به Google Maps می‌ریم
            window.location.href = mapsUrl;
          }
        },
        (error) => {
          console.error('خطا در دریافت موقعیت:', error);
          // اگر دسترسی به موقعیت نداشتیم، فقط مقصد رو نشون می‌دیم
          const mapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${destLat},${destLng}&travelmode=driving`;
          window.location.href = mapsUrl;
        },
        {
          enableHighAccuracy: false,
          timeout: 5000,
          maximumAge: 0
        }
      );
    } else {
      // اگر geolocation پشتیبانی نمی‌شه
      const mapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${destLat},${destLng}&travelmode=driving`;
      window.location.href = mapsUrl;
    }
  } else {
    // برای دسکتاپ: باز کردن در تب جدید
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const userLat = position.coords.latitude;
          const userLng = position.coords.longitude;
          const mapsUrl = `https://www.google.com/maps/dir/?api=1&origin=${userLat},${userLng}&destination=${destLat},${destLng}&travelmode=driving`;
          window.open(mapsUrl, '_blank');
        },
        (error) => {
          console.error('خطا در دریافت موقعیت:', error);
          const mapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${destLat},${destLng}&travelmode=driving`;
          window.open(mapsUrl, '_blank');
        }
      );
    } else {
      const mapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${destLat},${destLng}&travelmode=driving`;
      window.open(mapsUrl, '_blank');
    }
  }
};
</script>

<style scoped>
.map-wrapper {
  width: 100%;
  height: 610px;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  z-index: 1;
}

.map-container {
  width: 100%;
  height: 100%;
}

.routing-button {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
}

.btn-directions {
  position: relative;
  overflow: hidden;
  background: #f3f4f6;
  color: #848484;
  border: 1px solid #d1d5db;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: color 300ms, border-color 300ms, background-color 300ms;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  white-space: nowrap;
  z-index: 1;
  -webkit-tap-highlight-color: transparent;
}

.btn-directions::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}

.btn-directions:hover::before,
.btn-directions:focus-visible::before,
.btn-directions:active::before {
  transform: translateY(0);
}

.btn-directions:hover,
.btn-directions:focus-visible,
.btn-directions:active {
  color: #fff;
  border-color: #FFCD05;
  outline: none;
}

.btn-directions span {
  position: relative;
  z-index: 1;
}

/* بهینه‌سازی برای موبایل */
@media (max-width: 768px) {
  .map-wrapper {
    height: 400px;
    border-radius: 4px;
  }
  
  .btn-directions {
    padding: 12px 24px;
    font-size: 14px;
    touch-action: manipulation;
  }
  
  .routing-button {
    bottom: 10px;
  }
}
</style>