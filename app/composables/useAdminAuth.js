// composables/useAdminAuth.js
export const useAdminAuth = () => {
  // توکن کو صحیح نام سے save کریں
  const setAdminToken = (token, refresh_token, user) => {
    if (process.client) {
      // ✅ یہ نام استعمال کریں
      localStorage.setItem('access_token', token)      // صحیح!
      localStorage.setItem('refresh_token', refresh_token)
      localStorage.setItem('admin_user', JSON.stringify(user))
      
      // ڈیبگ
      console.log('✅ توکن save شد:', {
        token: token.substring(0, 20) + '...',
        saved: localStorage.getItem('access_token') ? 'ہاں' : 'نہیں'
      })
    }
  }

  const getAdminToken = () => {
    if (process.client) {
      return localStorage.getItem('access_token')  // صحیح!
    }
    return null
  }

  const getAdminUser = () => {
    if (process.client) {
      const user = localStorage.getItem('admin_user')
      return user ? JSON.parse(user) : null
    }
    return null
  }

  const clearAdminToken = () => {
    if (process.client) {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('admin_user')
    }
  }

  const isAdminAuthenticated = () => {
    return !!getAdminToken()
  }

  return {
    setAdminToken,
    getAdminToken,
    getAdminUser,
    clearAdminToken,
    isAdminAuthenticated
  }
}