<template>
  <div class="h-screen w-screen overflow-hidden relative" dir="rtl">
    <div class="absolute inset-0 z-0">
      <img src="/Product/index/Rafcolor-1.webp" alt="Background" class="w-full h-full object-cover grayscale" />
      <div class="absolute inset-0 bg-gradient-to-t from-yellow-400/20 to-transparent"></div>
    </div>

    <div class="relative z-10 h-full flex flex-col p-6">
      <header class="bg-gray-200/50 backdrop-blur-lg rounded-3xl px-6 py-3 mb-4 flex flex-row-reverse items-center justify-between shadow-lg border border-white/30">
        <div class="flex items-center gap-2">
          <img src="/english logo W1.png" alt="" class="h-8">
        </div>
        
        <nav class="flex items-center gap-6">
          <button v-for="tab in tabs" :key="tab" 
            :class="['px-4 py-2 font-medium transition-all text-sm relative group']"
            @click="activeTab = tab">
            <span :class="activeTab === tab ? 'text-white' : 'text-white'">{{ tab }}</span>
            <span v-if="activeTab === tab" class="absolute bottom-0 start-0 end-0 h-0.5 bg-yellow-400 rounded-full"></span>
            <span v-else class="absolute bottom-0 start-1/2 end-1/2 h-0.5 bg-yellow-400/50 rounded-full group-hover:start-0 group-hover:end-0 transition-all duration-300"></span>
          </button>
        </nav>

        <div class="flex items-center gap-3">
          <div class="text-right">
            <p class="text-sm font-bold text-white">{{ displayName }}</p>
          </div>
          <button class="w-9 h-9 bg-white/40 hover:bg-white/70 rounded-full flex items-center justify-center transition-all hover:scale-105">
            <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
          </button>
          <button @click="handleLogout" class="w-9 h-9 bg-white/40 hover:bg-white/70 rounded-full flex items-center justify-center transition-all hover:scale-105">
            <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
          </button>
          
          <div class="relative group">
            <img 
              :src="profileImageUrl" 
              :alt="displayName"
              class="w-9 h-9 rounded-full border-2 border-white shadow-sm object-cover cursor-pointer"
              @click="triggerFileUpload"
            />
            <div class="absolute -bottom-1 -right-1 w-4 h-4 bg-yellow-400 rounded-full border-2 border-white flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
              <svg class="w-2.5 h-2.5 text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </div>
            <div v-if="uploadingImage" class="absolute inset-0 bg-white bg-opacity-80 rounded-full flex items-center justify-center">
              <div class="animate-spin rounded-full h-5 w-5 border-b-2 border-yellow-400"></div>
            </div>
          </div>
          
          <input 
            ref="profileImageInput"
            type="file" 
            accept="image/png,image/jpeg,image/jpg,image/gif,image/webp"
            class="hidden"
            @change="handleProfileImageUpload"
          />
        </div>
      </header>

      <div class="flex-1 overflow-hidden h-full flex flex-col">
        <OrdersPage v-if="activeTab === 'سفارشات'" />
        <PriceList v-else-if="activeTab === 'ثبت سفارش'" />

        <div v-else-if="activeTab === 'داشبورد'" class="grid grid-cols-12 gap-4 h-full overflow-y-auto custom-scrollbar pb-6">
          <div class="col-span-12 bg-gradient-to-br from-yellow-400 to-yellow-500 rounded-3xl p-6 shadow-xl border border-white/40 text-white">
            <h2 class="text-2xl font-bold mb-2">{{ welcomeMessage }}</h2>
          </div>

          <div class="col-span-6 bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl border border-white/40">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-bold text-gray-900">سفارشات اخیر</h3>
              <button @click="activeTab = 'سفارشات'" class="text-sm text-yellow-600 hover:text-yellow-700 font-semibold">مشاهده همه</button>
            </div>
            <div class="space-y-3">
              <div v-if="recentOrders.length === 0" class="text-center py-8 text-gray-500">
                <p class="text-sm">هنوز سفارشی ثبت نشده</p>
              </div>
              <div v-for="order in recentOrders" :key="order.id" class="flex items-center justify-between p-4 bg-white/40 rounded-2xl hover:bg-white/50 transition-all">
                <div class="flex-1">
                  <p class="font-semibold text-gray-900">{{ order.order_number }}</p>
                  <p class="text-xs text-gray-600">{{ formatDate(order.created_at) }}</p>
                </div>
                <div class="text-left">
                  <p class="font-bold text-gray-900">{{ formatPrice(order.total_price) }}</p>
                  <span :class="getStatusColor(order.status)" class="text-xs font-semibold px-2.5 py-1 rounded-lg">
                    {{ getStatusLabel(order.status) }}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <div class="col-span-6 bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl border border-white/40">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-bold text-gray-900">اطلاعات حساب</h3>
              <button @click="activeTab = 'تنظیمات'" class="text-sm text-yellow-600 hover:text-yellow-700 font-semibold">ویرایش</button>
            </div>
           <div class="space-y-3">
                 <div v-if="userProfile.company_name" class="flex items-center gap-3">
                <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs text-gray-600">شرکت</p>
                  <p class="text-sm font-semibold text-gray-900">{{ userProfile.company_name }}</p>
                </div>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs text-gray-600">ایمیل</p>
                  <p class="text-sm font-semibold text-gray-900">{{ userProfile.email || 'تعیین نشده' }}</p>
                </div>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs text-gray-600">تلفن</p>
                  <p class="text-sm font-semibold text-gray-900">{{ userProfile.phone || 'تعیین نشده' }}</p>
                </div>
              </div>
           
            </div>
          </div>

          <div class="col-span-12 bg-white/60 backdrop-blur-xl rounded-3xl p-5 shadow-xl border border-white/40">
            <h3 class="text-base font-bold text-gray-900 mb-1">گزارش فعالیت</h3>
            <p class="text-xs text-gray-600 mb-4">تلاش‌های ورود و فعالیت‌های اخیر</p>
            <div class="max-h-[230px] overflow-y-auto pr-2 custom-scrollbar space-y-2">
              <div v-if="activityLogs.length === 0" class="text-center py-8 text-gray-500">
                <p class="text-sm">فعالیتی ثبت نشده</p>
              </div>
              <div v-for="(log, idx) in activityLogs" :key="idx" 
                   class="flex items-start justify-between p-2.5 rounded-xl transition-all hover:bg-white/70"
                   :class="log.success ? 'bg-green-50/60' : 'bg-red-50/60'">
                <div class="flex items-start gap-2 flex-1">
                  <div class="w-7 h-7 rounded-lg flex items-center justify-center flex-shrink-0"
                       :class="log.success ? 'bg-green-100 text-green-600' : 'bg-red-100 text-red-600'">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path v-if="log.success" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div class="flex-1">
                    <p class="text-xs font-semibold text-gray-900">{{ log.action }}</p>
                    <p class="text-[10px] text-gray-500">{{ log.time }}</p>
                  </div>
                </div>
                <span class="text-[9px] font-semibold px-2 py-0.5 rounded-lg"
                      :class="log.success ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'">
                  {{ log.status }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <div v-else-if="activeTab === 'تیکت'" class="flex-1 overflow-hidden">
          <LoyaltyPage />
        </div>

        <div v-else-if="activeTab === 'تنظیمات'" class="flex-1 overflow-hidden">
          <SettingsPage @profile-updated="loadUserProfile" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import OrdersPage from './order.vue'
import PriceList from './pricelist.vue'
import LoyaltyPage from './Ticket.vue'
import SettingsPage from './Settings.vue'

const API_BASE_URL = 'https://polychemmb.com/api'

export default {
  name: 'ClientArea',
  components: { OrdersPage, PriceList, LoyaltyPage, SettingsPage },
  data() {
    return {
      activeTab: 'داشبورد',
      tabs: ['داشبورد', 'ثبت سفارش', 'سفارشات', 'تیکت', 'تنظیمات'],
      userProfile: {},
      recentOrders: [],
      activityLogs: [],
      isLoading: true,
      uploadingImage: false
    }
  },
  computed: {
    displayName() {
      if (this.userProfile.company_name) return this.userProfile.company_name
      const firstName = this.userProfile.first_name || ''
      const lastName = this.userProfile.last_name || ''
      const fullName = `${firstName} ${lastName}`.trim()
      if (fullName) return fullName
      return this.userProfile.username || 'کاربر'
    },

    welcomeMessage() {
      const name = this.userProfile.company_name || 'عزیز'
      return `خوش آمدید، ${name}!`
    },

    profileImageUrl() {
      if (this.userProfile.profile_image) {
        const imagePath = this.userProfile.profile_image
        if (imagePath.startsWith('http://') || imagePath.startsWith('https://')) {
          return imagePath
        }
        return `${API_BASE_URL}/public/uploads/profiles/${imagePath}`
      }
      const name = this.userProfile.company_name || this.displayName
      return `https://ui-avatars.com/api/?name=${encodeURIComponent(name)}&background=848484&color=fff&size=128&bold=true&font-size=0.4`
    }
  },
  mounted() {
    this.loadUserProfile()
    window.addEventListener('profile-image-updated', this.handleProfileImageUpdate)
  },
  beforeUnmount() {
    window.removeEventListener('profile-image-updated', this.handleProfileImageUpdate)
  },
  methods: {
    async loadUserProfile() {
      const token = localStorage.getItem('client_token') || localStorage.getItem('token')
      if (!token) {
        this.$router.push('/clientarea/login')
        return
      }

      try {
        const response = await fetch(`${API_BASE_URL}/client/profile`, {
          headers: { 'Authorization': `Bearer ${token}` }
        })

        if (response.ok) {
          const data = await response.json()
          this.userProfile = data.user || data
          await this.loadRecentOrders()
          await this.loadActivityLogs()
        } else if (response.status === 401) {
          this.clearAuthAndRedirect()
        }
      } catch (error) {
        console.error('Error loading profile:', error)
      } finally {
        this.isLoading = false
      }
    },

    async loadRecentOrders() {
      const token = localStorage.getItem('client_token') || localStorage.getItem('token')
      if (!token) return
      try {
        const response = await fetch(`${API_BASE_URL}/client/orders/recent?limit=3`, {
          headers: { 'Authorization': `Bearer ${token}` }
        })
        if (response.ok) {
          const data = await response.json()
          this.recentOrders = data.data || []
        }
      } catch (error) {
        this.recentOrders = []
      }
    },

    async loadActivityLogs() {
      const token = localStorage.getItem('client_token') || localStorage.getItem('token')
      if (!token) return
      try {
        const response = await fetch(`${API_BASE_URL}/client/activity-logs?limit=10`, {
          headers: { 'Authorization': `Bearer ${token}` }
        })
        if (response.ok) {
          const data = await response.json()
          this.activityLogs = data.logs || []
        }
      } catch (error) {
        this.activityLogs = []
      }
    },

    clearAuthAndRedirect() {
      localStorage.removeItem('client_token')
      localStorage.removeItem('token')
      this.$router.push('/clientarea/login')
    },

    async handleLogout() {
      const token = localStorage.getItem('client_token') || localStorage.getItem('token')
      if (token) {
        try {
          await fetch(`${API_BASE_URL}/client/logout`, {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${token}` }
          })
        } catch (error) {
          console.warn(error)
        }
      }
      this.clearAuthAndRedirect()
    },

    formatDate(date) {
      return date ? new Date(date).toLocaleDateString('fa-IR') : '-'
    },

    formatPrice(price) {
      return new Intl.NumberFormat('fa-IR').format(price || 0) + ' ریال'
    },

    getStatusLabel(status) {
      const labels = {
        'awaiting_proforma': 'پیش‌فاکتور',
        'awaiting_proforma_approval': 'تایید',
        'awaiting_bill_issue': 'حواله',
        'awaiting_loading': 'بارگیری',
        'loading_complete': 'بارگیری شده',
        'delivered': 'تحویل',
        'cancelled': 'لغو'
      }
      return labels[status] || status
    },

    getStatusColor(status) {
      const colors = {
        'awaiting_proforma': 'bg-yellow-100 text-yellow-700',
        'awaiting_proforma_approval': 'bg-purple-100 text-purple-700',
        'awaiting_bill_issue': 'bg-orange-100 text-orange-700',
        'awaiting_loading': 'bg-blue-100 text-blue-700',
        'loading_complete': 'bg-indigo-100 text-indigo-700',
        'delivered': 'bg-green-100 text-green-700',
        'cancelled': 'bg-red-100 text-red-700'
      }
      return colors[status] || 'bg-gray-100 text-gray-700'
    },

    triggerFileUpload() {
      this.$refs.profileImageInput.click()
    },

    async handleProfileImageUpload(event) {
      const file = event.target.files[0]
      if (!file) return

      const allowedTypes = ['image/png', 'image/jpeg', 'image/jpg', 'image/gif', 'image/webp']
      if (!allowedTypes.includes(file.type)) {
        alert('فقط فایل‌های PNG, JPG, JPEG, GIF و WEBP مجاز هستند')
        return
      }

      if (file.size > 5 * 1024 * 1024) {
        alert('حجم فایل نباید بیشتر از 5 مگابایت باشد')
        return
      }

      this.uploadingImage = true

      try {
        const token = localStorage.getItem('client_token') || localStorage.getItem('token')
        const formData = new FormData()
        formData.append('profile_image', file)

        const response = await fetch(`${API_BASE_URL}/client/upload-profile-image`, {
          method: 'POST',
          headers: { 'Authorization': `Bearer ${token}` },
          body: formData
        })

        const data = await response.json()

        if (response.ok && data.success) {
          this.userProfile.profile_image = data.filepath || data.profile_image
          alert('عکس پروفایل با موفقیت آپلود شد')
          window.dispatchEvent(new CustomEvent('profile-image-updated', {
            detail: { profile_image: this.userProfile.profile_image }
          }))
        } else {
          alert(data.message || 'خطا در آپلود عکس')
        }
      } catch (error) {
        console.error('Upload error:', error)
        alert('خطا در آپلود عکس پروفایل')
      } finally {
        this.uploadingImage = false
        this.$refs.profileImageInput.value = ''
      }
    },

    handleProfileImageUpdate(event) {
      if (event.detail && event.detail.profile_image) {
        this.userProfile.profile_image = event.detail.profile_image
      }
    }
  }
}

</script>

<style scoped>
:deep(*) {
  font-family: 'IRANYekan', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: rgba(243, 244, 246, 0.5); border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #f8cf48 0%, #f8cf48 100%); border-radius: 10px; }
</style>