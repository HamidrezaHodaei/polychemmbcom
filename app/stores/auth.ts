import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as any,
    token: null as string | null,
    isAuthenticated: false
  }),
  
  actions: {
    async register(userData: any) {
      const { apiCall } = useApi()
      try {
        const user = await apiCall('/api/auth/register', {
          method: 'POST',
          body: userData
        })
        console.log('✅ Register success:', user)
        return user
      } catch (error: any) {
        console.error('❌ Register error:', error)
        throw error
      }
    },
    
    async login(credentials: any) {
      const { apiCall } = useApi()
      try {
        console.log('📤 Login attempt:', credentials.username)
        
        // Login request
        const data = await apiCall('/api/auth/login', {
          method: 'POST',
          body: credentials
        })
        
        console.log('✅ Login success, token received')
        
        // ⭐ ذخیره token
        this.token = data.access_token
        localStorage.setItem('token', data.access_token)
        
        // ⭐ کمی صبر کنیم تا localStorage آپدیت شود
        await new Promise(resolve => setTimeout(resolve, 100))
        
        // ⭐ دریافت اطلاعات کاربر
        await this.fetchUser()
        
        return data
      } catch (error: any) {
        console.error('❌ Login error:', error)
        this.logout()
        throw error
      }
    },
    
    async fetchUser() {
      const { apiCall } = useApi()
      try {
        const token = localStorage.getItem('token')
        console.log('📤 Fetching user with token:', token ? 'exists' : 'MISSING!')
        
        if (!token) {
          throw new Error('No token available')
        }
        
        const user = await apiCall('/api/auth/me', {
          method: 'GET'
        })
        
        console.log('✅ User fetched:', user.username)
        
        this.user = user
        this.isAuthenticated = true
        
        return user
      } catch (error: any) {
        console.error('❌ Fetch user error:', error)
        this.logout()
        throw error
      }
    },
    
    logout() {
      this.user = null
      this.token = null
      this.isAuthenticated = false
      localStorage.removeItem('token')
      console.log('👋 Logged out')
      navigateTo('/login')
    },
    
    initAuth() {
      const token = localStorage.getItem('token')
      console.log('🔄 Init auth, token:', token ? 'exists' : 'missing')
      
      if (token) {
        this.token = token
        this.fetchUser().catch(() => {
          console.log('❌ Token invalid, logging out')
          this.logout()
        })
      }
    }
  }
})