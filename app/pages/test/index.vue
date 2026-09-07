<template>
  <div class="page-root">
    <Navbar />

    <!-- ============================================================
         SECTION 1: Hero
    ============================================================ -->
    <section class="hero-section">
      <div class="hero-container">
        <div class="hero-grid">

          <!-- Left: Text -->
          <div class="hero-left">
            <h1 class="hero-heading">
               Manufacturing &amp; Compounding Solutions<br />
             
            </h1>
            <p class="hero-description">
              Tailored polymer production, scalable to your exact technical
              specifications and engineered for premium end-use performance—
              from pilot-scale development to full full-scale manufacturing.
            </p>
            <button class="hero-cta" type="button">Request sample</button>
          </div>

          <!-- Right: Image -->
          <div class="hero-right">
            <div class="hero-image-wrapper">
              <img
                src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&q=80"
                alt="Polymer compounding manufacturing equipment"
                class="hero-image"
              />
            </div>
          </div>

        </div>
      </div>

      <!-- Stats Card -->
      <div class="stats-section">
        <div class="stats-container">
          <div class="stats-grid">

            <div class="stat-item">
              <div class="stat-icon-wrap">
                <svg class="stat-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                  <circle cx="12" cy="8" r="4" fill="white"/>
                  <path d="M4 20c0-4 3.6-7 8-7s8 3 8 7" stroke="white" stroke-width="2" stroke-linecap="round"/>
                </svg>
              </div>
              <div class="stat-text">
                <span class="stat-number">31+</span>
                <span class="stat-label">client</span>
              </div>
            </div>

            <div class="stat-divider" aria-hidden="true"></div>

            <div class="stat-item">
              <div class="stat-icon-wrap">
                <svg class="stat-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                  <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" fill="white"/>
                </svg>
              </div>
              <div class="stat-text">
                <span class="stat-number">200,000</span>
                <span class="stat-label">Annual Capacity (Tons)</span>
              </div>
            </div>

            <div class="stat-divider" aria-hidden="true"></div>

            <div class="stat-item">
              <div class="stat-icon-wrap">
                <svg class="stat-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                  <rect x="3" y="5" width="18" height="3" rx="1" fill="white"/>
                  <rect x="3" y="11" width="18" height="3" rx="1" fill="white"/>
                  <rect x="3" y="17" width="18" height="3" rx="1" fill="white"/>
                </svg>
              </div>
              <div class="stat-text">
                <span class="stat-number">20+</span>
                <span class="stat-label">Product Grades</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         SECTION 2: Feature — Custom Polymer Compounding
    ============================================================ -->
    <section class="feature-section">
      <div class="section-container">
        <div class="feature-grid">

          <!-- Left: Image -->
          <div class="feature-image-col">
            <div class="feature-image-wrapper">
              <img
                src="https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80"
                alt="Polymer compounding production line with blue pellets"
                class="feature-image"
              />
            </div>
          </div>

          <!-- Right: Text -->
          <div class="feature-text-col">
            <h2 class="feature-heading">
              Custom Polymer Compounding<br />
              That Starts with Your Specs
            </h2>
            <p class="feature-description">
              From pilot trials to high-volume production, we
              engineer around your precise performance needs.
            </p>
            <ul class="checklist">
              <li class="checklist-item">
                <span class="check-icon" aria-hidden="true">
                  <svg viewBox="0 0 20 20" fill="none">
                    <circle cx="10" cy="10" r="10" fill="#22C55E"/>
                    <path d="M5.5 10.5L8.5 13.5L14.5 7" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
                <span>Advanced additive, functional modifier, and color integration</span>
              </li>
              <li class="checklist-item">
                <span class="check-icon" aria-hidden="true">
                  <svg viewBox="0 0 20 20" fill="none">
                    <circle cx="10" cy="10" r="10" fill="#22C55E"/>
                    <path d="M5.5 10.5L8.5 13.5L14.5 7" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
                <span>Contract manufacturing and high-precision toll compounding</span>
              </li>
              <li class="checklist-item">
                <span class="check-icon" aria-hidden="true">
                  <svg viewBox="0 0 20 20" fill="none">
                    <circle cx="10" cy="10" r="10" fill="#22C55E"/>
                    <path d="M5.5 10.5L8.5 13.5L14.5 7" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
                <span>ISO 9001, FDA, and global quality compliance</span>
              </li>
              <li class="checklist-item">
                <span class="check-icon" aria-hidden="true">
                  <svg viewBox="0 0 20 20" fill="none">
                    <circle cx="10" cy="10" r="10" fill="#22C55E"/>
                    <path d="M5.5 10.5L8.5 13.5L14.5 7" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
                <span>Short-run, pilot scale, and full-scale flexibility</span>
              </li>
            </ul>
          </div>

        </div>
      </div>
    </section>

    <!-- ============================================================
         SECTION 3: Choose Your Plan header
    ============================================================ -->
    <section class="plan-section">
      <div class="plan-container">
        <h2 class="plan-heading">Flexible Customization Options for High-Performance Applications
</h2>
        <p class="plan-description">
        </p>
      </div>
    </section>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Navbar from '~/components/en/layout/navbar.vue'
import Footer from '~/components/en/layout/footer.vue'

// Full page — Hero + Feature + Plan header
</script>

<style scoped>
/* ---- Reset ---- */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* ---- Root ---- */
.page-root {
  background-color: #f1f2f2;
  font-family: 'Montserrat', sans-serif;
  color: #848484;
  width: 100%;
}

/* ============================================================
   HERO SECTION
============================================================ */
.hero-section {
  background-color: transparent;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.hero-container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 72px 64px 56px;
  flex: 1;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 56px;
  align-items: center;
  min-height: 480px;
}

/* Left */
.hero-left {
  display: flex;
  flex-direction: column;
  position: relative;
}

.hero-heading {
  font-size: clamp(2.2rem, 3.8vw, 3.4rem);
  font-weight: 800;
  line-height: 1.12;
  color: #848484;
  letter-spacing: -0.025em;
  margin-bottom: 28px;
}

.hero-description {
  font-size: 16px;
  line-height: 1.75;
  color: #848484;
  max-width: 460px;
  margin-bottom: 40px;
}

.hero-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: fit-content;
  min-height: 3rem;
  padding: 0 1.5rem;
  font-size: 0.95rem;
  font-weight: 700;
  color: #FFCD05;
  background-color: transparent;
  border: 2px solid #FFCD05;
  border-radius: 0.75rem;
  position: relative;
  overflow: hidden;
  transition: color 300ms ease, border-color 300ms ease;
  z-index: 1;
}

.hero-cta::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: -1;
}

.hero-cta:hover,
.hero-cta:focus-visible {
  color: #ffffff;
  outline: none;
}

.hero-cta:hover::before,
.hero-cta:focus-visible::before {
  transform: translateY(0);
}


/* Right */
.hero-right {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.hero-image-wrapper {
  width: 100%;
  max-width: 640px;
  border-radius: 16px;
  overflow: hidden;
  background: #e0ddd8;
  aspect-ratio: 4 / 3;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Stats */
.stats-section {
  width: 100%;
  background-color: #f1f2f2;
  padding: 0 64px 64px;
}

.stats-container {
  max-width: 1280px;
  margin: 0 auto;
}

.stats-grid {
  display: flex;
  align-items: stretch;
  border: 1px solid #e2e0da;
  border-radius: 12px;
  background-color: #ffffff;
  overflow: hidden;
}

.stat-item {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 36px 32px;
}

.stat-divider {
  width: 1px;
  background-color: #e2e0da;
  flex-shrink: 0;
  align-self: stretch;
}

.stat-icon-wrap {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background-color: #FFCD05;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-icon { width: 22px; height: 22px; }

.stat-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.stat-number {
  font-size: 26px;
  font-weight: 800;
  color: #848484;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.stat-label {
  font-size: 13.5px;
  color: #848484;
  line-height: 1.3;
}

/* ============================================================
   FEATURE SECTION
============================================================ */
.feature-section {
  width: 100%;
  background-color: #f1f2f2;
  padding: 88px 0 96px;
}

.section-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 64px;
}

.feature-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.feature-image-col {
  display: flex;
  align-items: center;
}

.feature-image-wrapper {
  width: 100%;
  border-radius: 16px;
  overflow: hidden;
  background: #d8d5d0;
  aspect-ratio: 4 / 3;
  box-shadow: 0 2px 24px rgba(0, 0, 0, 0.08);
}

.feature-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.feature-text-col {
  display: flex;
  flex-direction: column;
}

.feature-heading {
  font-size: clamp(1.75rem, 2.8vw, 2.75rem);
  font-weight: 700;
  line-height: 1.2;
  color: #848484;
  letter-spacing: -0.02em;
  margin-bottom: 24px;
}

.feature-description {
  font-size: 16px;
  line-height: 1.7;
  color: #848484;
  margin-bottom: 36px;
}

.checklist {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.checklist-item {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  font-size: 15.5px;
  line-height: 1.55;
  color: #848484;
}

.check-icon {
  width: 22px;
  height: 22px;
  flex-shrink: 0;
  margin-top: 1px;
}

.check-icon svg {
  width: 22px;
  height: 22px;
  display: block;
}

/* ============================================================
   PLAN SECTION
============================================================ */
.plan-section {
  width: 100%;
  background-color: #f1f2f2;
  padding: 16px 0 80px;
}

.plan-container {
  max-width: 680px;
  margin: 0 auto;
  padding: 0 24px;
  text-align: center;
}

.plan-heading {
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  font-weight: 800;
  color: #848484;
  letter-spacing: -0.02em;
  line-height: 1.15;
  margin-bottom: 20px;
}

.plan-description {
  font-size: 16px;
  line-height: 1.7;
  color: #848484;
}

/* ============================================================
   RESPONSIVE
============================================================ */
@media (max-width: 1024px) {
  .hero-container { padding: 60px 40px 44px; }
  .stats-section { padding: 0 40px 48px; }
  .hero-grid { gap: 36px; }
  .section-container { padding: 0 40px; }
  .feature-grid { gap: 48px; }
  .feature-section { padding: 72px 0 80px; }
}

@media (max-width: 768px) {
  /* Hero */
  .hero-container { padding: 48px 24px 40px; }
  .hero-grid { grid-template-columns: 1fr; gap: 32px; }
  .hero-right { justify-content: center; order: -1; }
  .hero-image-wrapper { max-width: 100%; aspect-ratio: 16 / 9; }
  .hero-description { max-width: 100%; }
  .cta-glow { width: 200px; }

  /* Stats */
  .stats-section { padding: 0 24px 40px; }
  .stats-grid { flex-direction: column; border-radius: 10px; }
  .stat-divider { width: 100%; height: 1px; align-self: auto; }
  .stat-item { width: 100%; padding: 22px 24px; }

  /* Feature */
  .feature-section { padding: 56px 0 64px; }
  .section-container { padding: 0 24px; }
  .feature-grid { grid-template-columns: 1fr; gap: 36px; }
  .feature-image-wrapper { aspect-ratio: 16 / 9; }

  /* Plan */
  .plan-section { padding: 8px 0 64px; }
}

@media (max-width: 480px) {
  .hero-container { padding: 36px 20px 32px; }
  .hero-heading { font-size: 1.6rem; }
  .stats-section { padding: 0 16px 32px; }
  .stat-number { font-size: 22px; }
  .stat-icon-wrap { width: 44px; height: 44px; }
  .stat-icon { width: 18px; height: 18px; }
  .section-container { padding: 0 20px; }
  .feature-heading { font-size: 1.5rem; }
  .checklist-item { font-size: 14.5px; }
  .plan-heading { font-size: 1.6rem; }
}
</style>