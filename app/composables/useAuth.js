// composables/useAuth.js
export const useAuth = () => {
  const setToken = (token, refresh_token, user) => {
    if (process.client) {
      localStorage.setItem('client_token', token)
      localStorage.setItem('client_refresh_token', refresh_token)
      localStorage.setItem('client_user', JSON.stringify(user))
    }
  }

  const getToken = () => {
    if (process.client) {
      return localStorage.getItem('client_token')
    }
    return null
  }

  const clearToken = () => {
    if (process.client) {
      localStorage.removeItem('client_token')
      localStorage.removeItem('client_refresh_token')
      localStorage.removeItem('client_user')
    }
  }

  return {
    setToken,
    getToken,
    clearToken
  }
}