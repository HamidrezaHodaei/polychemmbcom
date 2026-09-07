// /composables/useLang.ts
export const useLang = () => {
  const route = useRoute()

  const currentLang = computed(() => {
    const path = route.path.toLowerCase()
    if (path.startsWith('/ar')) return 'ar'
    if (path.startsWith('/fa')) return 'fa'
    if (path.startsWith('/tr')) return 'tr'
    return 'en'
  })

  const switchLang = (targetLang: string) => {
    if (typeof window === 'undefined') return

    let currentPath = route.path
      .replace(/^\/ar\/?/i, '')
      .replace(/^\/fa\/?/i, '')
      .replace(/^\/en\/?/i, '')
      .replace(/^\/tr\/?/i, '')

    if (!currentPath || currentPath === '/') {
      currentPath = ''
    } else if (!currentPath.startsWith('/')) {
      currentPath = '/' + currentPath
    }

    const newPath = `/${targetLang.toLowerCase()}${currentPath}`
    
    // ✅ full navigation — همه کامپوننت‌ها از صفر mount میشن
    window.location.href = newPath
  }

  return { currentLang, switchLang }
}