// composables/useCrmAuth.js
// ----------------------------------------------------------------------
// این composable کاملاً مستقل از useAdminAuth.js (سیستم لاگین سایت اصلی
// PolyChem) است — اسم تابع و کلیدهای localStorage عمداً متفاوت‌اند تا هیچ
// تداخلی بین توکن پنل CRM و توکن ادمین سایت اصلی پیش نیاید.
// ----------------------------------------------------------------------

const CRM_TOKEN_KEY = 'crm_access_token'
const CRM_REFRESH_KEY = 'crm_refresh_token'
const CRM_USER_KEY = 'crm_admin_user'

export const useCrmAuth = () => {
  const setCrmToken = (token, refresh_token, user) => {
    if (process.client) {
      localStorage.setItem(CRM_TOKEN_KEY, token)
      if (refresh_token) localStorage.setItem(CRM_REFRESH_KEY, refresh_token)
      if (user) localStorage.setItem(CRM_USER_KEY, JSON.stringify(user))
    }
  }

  const getCrmToken = () => {
    if (process.client) {
      return localStorage.getItem(CRM_TOKEN_KEY)
    }
    return null
  }

  const getCrmRefreshToken = () => {
    if (process.client) {
      return localStorage.getItem(CRM_REFRESH_KEY)
    }
    return null
  }

  const getCrmUser = () => {
    if (process.client) {
      const user = localStorage.getItem(CRM_USER_KEY)
      return user ? JSON.parse(user) : null
    }
    return null
  }

  const clearCrmToken = () => {
    if (process.client) {
      localStorage.removeItem(CRM_TOKEN_KEY)
      localStorage.removeItem(CRM_REFRESH_KEY)
      localStorage.removeItem(CRM_USER_KEY)
    }
  }

  const isCrmAuthenticated = () => {
    return !!getCrmToken()
  }

  return {
    setCrmToken,
    getCrmToken,
    getCrmRefreshToken,
    getCrmUser,
    clearCrmToken,
    isCrmAuthenticated,
  }
}
