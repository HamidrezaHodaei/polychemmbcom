<!-- /tr/aboutus/aboutus.vue -->
<template>
  <div class="page-wrapper bg-[#f1f2f2]">
    <navbar />
    <navbar-mob />

    <main class="page-main">
      <aboutus />
    </main>

    <footer class="w-full">
      <Chatbox />
    </footer>
  </div>
</template>

<script setup>
import navbar from '~/components/ar/layout/navbar.vue'
import navbarMob from '~/components/ar/layout/navbar-mob.vue'
import aboutus from '~/components/ar/aboutus/Aboutus.vue'
import Chatbox from '~/components/ar/chatbox/chatbox.vue'
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&display=swap');

.page-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100svh;
  font-family: 'Montserrat', sans-serif;
  color: #848484;
  /* Prevent fixed children from being clipped */
  transform: none !important;
  -webkit-transform: none !important;
}

.page-main {
  flex: 1;
  /* On desktop: standard padding */
  padding: 2rem 1.5rem 4rem;
}

/* ========== MOBILE ========== */
@media (max-width: 768px) {
  .page-main {
    /* Top padding accounts for fixed mobile navbar height */
    padding-top: calc(var(--navbar-height, 72px) + 1rem);
    padding-left: 0;
    padding-right: 0;
    /* Bottom padding accounts for bottom mobile navbar */
    padding-bottom: calc(80px + env(safe-area-inset-bottom, 0px));
  }
}

@media (max-width: 480px) {
  .page-main {
    padding-top: calc(var(--navbar-height, 64px) + 0.5rem);
    padding-bottom: calc(70px + env(safe-area-inset-bottom, 0px));
  }
}
</style>