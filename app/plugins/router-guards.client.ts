// plugins/router-guards.client.ts
export default defineNuxtPlugin(() => {
  const router = useRouter()

  router.beforeEach((to, from, next) => {
    if (
      from.path === '/fa' && to.path !== '/fa' ||
      from.path === '/en' && to.path !== '/en' ||
      from.path === '/tr' && to.path !== '/tr'
    ) {
      const lang = from.path.replace('/', '')
      sessionStorage.removeItem(`homeScrollPosition_${lang}`)
    }
    next()
  })
})