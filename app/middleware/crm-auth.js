// middleware/crm-auth.js
// ----------------------------------------------------------------------
// این میدل‌ور فقط سمت کلاینت بررسی می‌کند (چون توکن در localStorage است
// و در SSR در دسترس نیست). اگر توکن نبود، کاربر به صفحه لاگین هدایت می‌شود.
// ----------------------------------------------------------------------
import { useCrmAuth } from '~/composables/useCrmAuth'

export default defineNuxtRouteMiddleware((to) => {
  // در SSR کاری نکن؛ فقط سمت کلاینت چک کن
  if (process.server) return

  const { isCrmAuthenticated } = useCrmAuth()

  if (!isCrmAuthenticated() && to.path !== '/Crm/login') {
    return navigateTo('/Crm/login')
  }
})
