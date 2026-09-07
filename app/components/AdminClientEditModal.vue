<!-- app/components/AdminClientEditModal.vue -->
<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4 font-iranyekan" dir="rtl">
    <div class="bg-white rounded-2xl w-full max-w-6xl max-h-[90vh] flex flex-col shadow-2xl">
      <!-- Modal Header -->
      <div class="flex items-center justify-between p-6 border-b border-gray-200 bg-gradient-to-r from-blue-50 to-indigo-50">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
            </svg>
          </div>
          <div>
            <h2 class="text-xl font-bold text-gray-900">ویرایش جامع کاربر</h2>
            <p class="text-sm text-gray-600">{{ clientData.username }}</p>
          </div>
        </div>
        <button 
          @click="closeModal"
          type="button"
          class="p-2 hover:bg-red-100 rounded-lg transition-colors group"
        >
          <svg class="w-6 h-6 text-gray-500 group-hover:text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="flex-1 overflow-y-auto p-6 custom-scrollbar">
        <!-- Error/Success Messages -->
        <div v-if="error" class="mb-4 p-4 bg-red-50 border-l-4 border-red-500 rounded-lg flex items-start gap-3">
          <svg class="w-5 h-5 text-red-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-sm text-red-700">{{ error }}</p>
        </div>

        <div v-if="success" class="mb-4 p-4 bg-green-50 border-l-4 border-green-500 rounded-lg flex items-start gap-3">
          <svg class="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-sm text-green-700">{{ success }}</p>
        </div>

        <div class="space-y-6">
          <!-- 📷 تصویر پروفایل -->
          <div class="bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl p-6 border border-gray-200">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              تصویر پروفایل
            </h3>
            
            <div class="flex items-center gap-6">
              <div class="relative">
                <img 
                  v-if="formData.profile_image" 
                  :src="getProfileImageUrl(formData.profile_image)" 
                  alt="Profile" 
                  class="w-24 h-24 rounded-xl object-cover shadow-lg border-4 border-white"
                >
                <div v-else class="w-24 h-24 bg-gradient-to-br from-blue-400 to-indigo-500 rounded-xl flex items-center justify-center shadow-lg">
                  <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </div>
                <button 
                  @click="$refs.fileInput.click()" 
                  type="button"
                  class="absolute bottom-0 right-0 bg-blue-600 hover:bg-blue-700 w-8 h-8 rounded-full flex items-center justify-center shadow-lg transition-all hover:scale-110"
                >
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                  </svg>
                </button>
                <input ref="fileInput" type="file" accept="image/*" @change="handleProfileImageChange" class="hidden">
              </div>
              
              <div class="flex-1">
                <p class="text-sm font-medium text-gray-700 mb-1">آپلود تصویر جدید</p>
                <p class="text-xs text-gray-500">فرمت‌های مجاز: JPG, PNG, GIF (حداکثر 5MB)</p>
              </div>
            </div>
          </div>

          <!-- 👤 اطلاعات پایه -->
          <div class="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
              اطلاعات پایه
            </h3>
            
            <div class="grid grid-cols-3 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">نام کاربری</label>
                <input 
                  v-model="formData.username"
                  type="text"
                  disabled
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg bg-gray-100 cursor-not-allowed text-gray-600 font-medium"
                />
                <p class="text-xs text-gray-500 mt-1">غیرقابل تغییر</p>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">نام *</label>
                <input 
                  v-model="formData.first_name"
                  type="text"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">نام خانوادگی *</label>
                <input 
                  v-model="formData.last_name"
                  type="text"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">نام شرکت *</label>
                <input 
                  v-model="formData.company_name"
                  type="text"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">شناسه اقتصادی</label>
                <input 
                  v-model="formData.economic_code"
                  type="text"
                  placeholder="مثال: 14006412345"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">وضعیت</label>
                <select 
                  v-model="formData.is_active"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option :value="true"> فعال</option>
                  <option :value="false"> غیرفعال</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">ایمیل *</label>
                <input 
                  v-model="formData.email"
                  type="email"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">شماره تماس *</label>
                <input 
                  v-model="formData.phone"
                  type="tel"
                  placeholder="09123456789"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">رمز عبور جدید (اختیاری)</label>
                <input 
                  v-model="formData.password"
                  type="password"
                  placeholder="برای تغییر رمز وارد کنید"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
            </div>

            <div class="mt-4">
              <label class="block text-sm font-medium text-gray-700 mb-2">آدرس</label>
              <textarea 
                v-model="formData.address"
                rows="2"
                class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
              ></textarea>
            </div>
          </div>

          <!-- 🏢 اطلاعات دفتر مرکزی -->
          <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-xl p-6 border border-green-200">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
              دفتر مرکزی
            </h3>
            
            <div class="grid grid-cols-2 gap-4">
              <div class="col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">آدرس دفتر</label>
                <textarea 
                  v-model="formData.office_address"
                  rows="2"
                  placeholder="آدرس کامل دفتر مرکزی را وارد کنید"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent resize-none"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">کد پستی دفتر</label>
                <input 
                  v-model="formData.office_postal_code"
                  type="text"
                  placeholder="1234567890"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">تلفن دفتر</label>
                <input 
                  v-model="formData.office_phone"
                  type="tel"
                  placeholder="021-12345678"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
                />
              </div>

              <div class="col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">ایمیل دفتر</label>
                <input 
                  v-model="formData.office_email"
                  type="email"
                  placeholder="office@company.com"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
                />
              </div>
            </div>
          </div>

          <!-- 🏭 اطلاعات کارخانه -->
          <div class="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-6 border border-purple-200">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
              </svg>
              آدرس کارخانه
            </h3>
            
            <div class="grid grid-cols-2 gap-4">
              <div class="col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">آدرس کارخانه</label>
                <textarea 
                  v-model="formData.factory_address"
                  rows="2"
                  placeholder="آدرس کامل کارخانه را وارد کنید"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent resize-none"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">کد پستی کارخانه</label>
                <input 
                  v-model="formData.factory_postal_code"
                  type="text"
                  placeholder="1234567890"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">تلفن کارخانه</label>
                <input 
                  v-model="formData.factory_phone"
                  type="tel"
                  placeholder="021-12345678"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                />
              </div>

              <div class="col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">ایمیل کارخانه</label>
                <input 
                  v-model="formData.factory_email"
                  type="email"
                  placeholder="factory@company.com"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="flex gap-3 p-6 border-t border-gray-200 bg-gray-50">
        <button 
          @click="closeModal"
          type="button"
          class="flex-1 px-6 py-3 border-2 border-gray-300 rounded-lg hover:bg-gray-100 transition-all font-medium text-gray-700 flex items-center justify-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
          انصراف
        </button>
        <button 
          @click="saveChanges"
          :disabled="saving"
          type="button"
          class="flex-1 px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-lg hover:from-blue-700 hover:to-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all font-bold shadow-lg hover:shadow-xl flex items-center justify-center gap-2"
        >
          <svg v-if="!saving" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
          </svg>
          <svg v-else class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
          </svg>
          {{ saving ? 'در حال ذخیره...' : 'ذخیره تغییرات' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminClientEditModal',
  props: {
    isOpen: {
      type: Boolean,
      required: true
    },
    clientData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      formData: {
        username: '',
        password: '',
        first_name: '',
        last_name: '',
        company_name: '',
        economic_code: '',
        email: '',
        phone: '',
        address: '',
        is_active: true,
        office_address: '',
        office_postal_code: '',
        office_phone: '',
        office_email: '',
        factory_address: '',
        factory_postal_code: '',
        factory_phone: '',
        factory_email: '',
        profile_image: null
      },
      error: '',
      success: '',
      saving: false
    }
  },
  computed: {
    apiBaseURL() {
      return process.env.VUE_APP_API_URL || 'https://polychemmb.com'
    }
  },
  watch: {
    clientData: {
      handler(newData) {
        if (newData && newData.id) {
          this.loadClientData()
        }
      },
      immediate: true,
      deep: true
    }
  },
  methods: {
    async loadClientData() {
      try {
        const token = localStorage.getItem('access_token')
        const response = await fetch(`${this.apiBaseURL}/api/admin/clients/${this.clientData.id}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        })

        if (response.ok) {
          const data = await response.json()
          if (data.success && data.client) {
            this.formData = {
              username: data.client.username || '',
              password: '',
              first_name: data.client.first_name || '',
              last_name: data.client.last_name || '',
              company_name: data.client.company_name || '',
              economic_code: data.client.economic_code || '',
              email: data.client.email || '',
              phone: data.client.phone || '',
              address: data.client.address || '',
              is_active: data.client.is_active !== undefined ? data.client.is_active : true,
              office_address: data.client.office_address || '',
              office_postal_code: data.client.office_postal_code || '',
              office_phone: data.client.office_phone || '',
              office_email: data.client.office_email || '',
              factory_address: data.client.factory_address || '',
              factory_postal_code: data.client.factory_postal_code || '',
              factory_phone: data.client.factory_phone || '',
              factory_email: data.client.factory_email || '',
              profile_image: data.client.profile_image || null
            }
          }
        }
      } catch (err) {
        console.error('Error loading client data:', err)
        this.error = 'خطا در بارگذاری اطلاعات کاربر'
      }
    },

    getProfileImageUrl(image) {
      if (!image) return ''
      if (image.startsWith('http')) return image
      return `${this.apiBaseURL}/public/uploads/profiles/${image}`
    },

    async handleProfileImageChange(event) {
      const file = event.target.files[0]
      if (!file) return

      // بررسی سایز فایل (5MB)
      if (file.size > 5 * 1024 * 1024) {
        this.error = 'حجم فایل نباید بیشتر از 5 مگابایت باشد'
        return
      }

      // بررسی نوع فایل
      const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp']
      if (!allowedTypes.includes(file.type)) {
        this.error = 'فرمت فایل مجاز نیست. فقط JPG, PNG, GIF قابل قبول است'
        return
      }

      try {
        const token = localStorage.getItem('access_token')
        const formDataUpload = new FormData()
        formDataUpload.append('profile_image', file)

        const response = await fetch(`${this.apiBaseURL}/api/admin/clients/${this.clientData.id}/upload-profile-image`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`
          },
          body: formDataUpload
        })

        const data = await response.json()
        if (data.success) {
          this.formData.profile_image = data.profile_image
          this.success = 'تصویر پروفایل با موفقیت آپلود شد'
          setTimeout(() => { this.success = '' }, 3000)
        } else {
          this.error = data.message || 'خطا در آپلود تصویر'
        }
      } catch (err) {
        console.error('Upload error:', err)
        this.error = 'خطا در آپلود تصویر'
      }
    },

    async saveChanges() {
      this.error = ''
      this.success = ''

      // اعتبارسنجی
      const required = ['first_name', 'last_name', 'company_name', 'email', 'phone']
      const missing = required.filter(f => !this.formData[f] || this.formData[f].trim() === '')
      
      if (missing.length > 0) {
        this.error = `لطفاً فیلدهای الزامی را پر کنید: ${missing.join(', ')}`
        return
      }

      if (this.formData.password && this.formData.password.length < 8) {
        this.error = 'رمز عبور باید حداقل 8 کاراکتر باشد'
        return
      }

      this.saving = true

      try {
        const token = localStorage.getItem('access_token')

        // بروزرسانی اطلاعات اصلی
        const updatePayload = {
          first_name: this.formData.first_name.trim(),
          last_name: this.formData.last_name.trim(),
          company_name: this.formData.company_name.trim(),
          economic_code: this.formData.economic_code.trim(),
          email: this.formData.email.trim(),
          phone: this.formData.phone.trim(),
          address: this.formData.address.trim(),
          is_active: this.formData.is_active,
          office_address: this.formData.office_address.trim(),
          office_postal_code: this.formData.office_postal_code.trim(),
          office_phone: this.formData.office_phone.trim(),
          office_email: this.formData.office_email.trim(),
          factory_address: this.formData.factory_address.trim(),
          factory_postal_code: this.formData.factory_postal_code.trim(),
          factory_phone: this.formData.factory_phone.trim(),
          factory_email: this.formData.factory_email.trim()
        }

        const response = await fetch(`${this.apiBaseURL}/api/admin/clients/${this.clientData.id}`, {
          method: 'PUT',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(updatePayload)
        })

        const data = await response.json()

        if (!data.success) {
          this.error = data.message || 'خطا در بروزرسانی اطلاعات'
          return
        }

        // تغییر رمز عبور در صورت نیاز
        if (this.formData.password && this.formData.password.trim() !== '') {
          const pwdResponse = await fetch(`${this.apiBaseURL}/api/admin/clients/${this.clientData.id}/change-password`, {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              new_password: this.formData.password
            })
          })

          const pwdData = await pwdResponse.json()
          if (!pwdData.success) {
            this.error = 'اطلاعات بروزرسانی شد اما خطا در تغییر رمز عبور: ' + (pwdData.message || '')
            return
          }
        }

        this.success = 'اطلاعات با موفقیت بروزرسانی شد'
        
        setTimeout(() => {
          this.$emit('saved')
          this.closeModal()
        }, 1500)

      } catch (err) {
        console.error('Save error:', err)
        this.error = 'خطا در ارتباط با سرور'
      } finally {
        this.saving = false
      }
    },

    closeModal() {
      this.error = ''
      this.success = ''
      this.$emit('close')
    }
  }
}
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #3b82f6 0%, #6366f1 100%);
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, #2563eb 0%, #4f46e5 100%);
}
</style>