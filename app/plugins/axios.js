// plugins/axios.js
import axios from 'axios'

export default defineNuxtPlugin(() => {
  const axiosInstance = axios.create({
    baseURL: 'https://polychemmb.com/api', // مسیر API
    timeout: 10000,
    headers: {
      'Content-Type': 'application/json'
    }
  })

  // Request Interceptor - اضافه کردن خودکار توکن
  axiosInstance.interceptors.request.use(
    (config) => {
      if (process.client) {
        const isAdminRoute = config.url?.includes('/admin/')
        const isClientRoute = config.url?.includes('/client/')

        let token = null

        // تغییر کلید توکن مطابق با clientmanage.vue
        if (isAdminRoute) {
          token = localStorage.getItem('access_token') || localStorage.getItem('admin_token')
        } else if (isClientRoute) {
          token = localStorage.getItem('client_token')
        }

        if (token) {
          config.headers.Authorization = `Bearer ${token}`
        }
      }
      return config
    },
    (error) => Promise.reject(error)
  )

  // Response Interceptor - مدیریت خطاها
  axiosInstance.interceptors.response.use(
    (response) => response,
    async (error) => {
      if (error.response?.status === 401 && process.client) {
        const isAdminRoute = error.config.url?.includes('/admin/')
        if (isAdminRoute) {
          localStorage.removeItem('access_token')
          localStorage.removeItem('admin_token')
          localStorage.removeItem('admin_refresh_token')
          localStorage.removeItem('admin_user')

          if (window.location.pathname !== '/admin/login') {
            window.location.href = '/admin/login'
          }
        } else {
          localStorage.removeItem('client_token')
          localStorage.removeItem('client_refresh_token')
          localStorage.removeItem('client_user')

          if (window.location.pathname !== '/login') {
            window.location.href = '/login'
          }
        }
      }
      return Promise.reject(error)
    }
  )

  return {
    provide: {
      axios: axiosInstance
    }
  }
})
