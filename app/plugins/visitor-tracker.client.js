// plugins/visitor-tracker.client.js
export default defineNuxtPlugin(() => {
  const router = useRouter()
  const config = useRuntimeConfig()

  // در dev از لوکال، در production از دامنه‌ی واقعی
  const API_BASE = config.public.apiBase ||'https://polychemmb.com/api'

  const trackVisit = (path) => {
    fetch(`${API_BASE}/track-visit`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        path,
        referrer: document.referrer || ''
      })
    })
      .then(res => {
        if (!res.ok) {
          console.warn('[track-visit] failed:', res.status)
        }
      })
      .catch((err) => {
        console.warn('[track-visit] network error:', err)
      })
  }

  trackVisit(window.location.pathname)

  router.afterEach((to) => {
    trackVisit(to.fullPath)
  })
})