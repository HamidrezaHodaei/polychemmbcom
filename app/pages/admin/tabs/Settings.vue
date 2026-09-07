<!-- admin/profile.vue - FINAL FIXED VERSION -->
<template>
  <div class="max-w-6xl mx-auto">
    <!-- Profile Section -->
    <div class="bg-white rounded-2xl shadow-lg overflow-hidden mb-6">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 p-8">
        
        <!-- Left: Personal Information -->
        <div class="lg:col-span-2">
          <h2 class="text-2xl font-bold text-slate-900 mb-8">مشخصات ادمین</h2>
          
          <!-- Username Section -->
          <div class="mb-8 pb-8 border-b border-slate-200">
            <label class="block text-sm font-bold text-slate-700 mb-3">نام کاربری</label>
            <div class="flex gap-3">
              <input
                type="text"
                v-model="form.username"
                placeholder="نام کاربری جدید را وارد کنید"
                class="flex-1 px-4 py-3 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900 transition-all"
              />
              <button
                @click="updateUsername"
                :disabled="!form.username || form.username === originalForm.username || loadingUsername"
                class="px-6 py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all font-medium whitespace-nowrap"
              >
                {{ loadingUsername ? 'درحال...' : 'بروزرسانی' }}
              </button>
            </div>
            <p v-if="messages.username" :class="messages.usernameSuccess ? 'text-green-600' : 'text-red-600'" class="text-sm mt-2">
              {{ messages.username }}
            </p>
          </div>

          <!-- First Name Section - ✅ FIXED LAYOUT -->
          <div class="grid grid-cols-2 gap-4 mb-8 pb-8 border-b border-slate-200">
            <!-- First Name -->
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-3">نام</label>
              <input
                type="text"
                v-model="form.first_name"
                placeholder="مثلاً: علی"
                class="w-full px-4 py-3 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900 transition-all"
              />
            </div>

            <!-- Last Name -->
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-3">نام خانوادگی</label>
              <input
                type="text"
                v-model="form.last_name"
                placeholder="مثلاً: محمد"
                class="w-full px-4 py-3 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900 transition-all"
              />
            </div>

            <!-- Update Button -->
            <div class="col-span-2">
              <button
                @click="updateName"
                :disabled="(!form.first_name && !form.last_name) || (form.first_name === originalForm.first_name && form.last_name === originalForm.last_name) || loadingName"
                class="w-full px-6 py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all font-medium"
              >
                {{ loadingName ? 'درحال...' : 'بروزرسانی نام' }}
              </button>
            </div>
          </div>

          <p v-if="messages.name" :class="messages.nameSuccess ? 'text-green-600' : 'text-red-600'" class="text-sm mb-4">
            {{ messages.name }}
          </p>
          
          <!-- Email Section -->
          <div class="mb-8 pb-8 border-b border-slate-200">
            <label class="block text-sm font-bold text-slate-700 mb-3">ایمیل</label>
            <div class="flex gap-3">
              <input
                type="email"
                v-model="form.email"
                placeholder="ایمیل جدید را وارد کنید"
                class="flex-1 px-4 py-3 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900 transition-all"
              />
              <button
                @click="updateEmail"
                :disabled="!form.email || form.email === originalForm.email || loadingEmail"
                class="px-6 py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all font-medium whitespace-nowrap"
              >
                {{ loadingEmail ? 'درحال...' : 'بروزرسانی' }}
              </button>
            </div>
            <p v-if="messages.email" :class="messages.emailSuccess ? 'text-green-600' : 'text-red-600'" class="text-sm mt-2">
              {{ messages.email }}
            </p>
          </div>

          <!-- Password Section -->
          <div>
            <h3 class="text-lg font-bold text-slate-900 mb-4">تغییر رمز عبور</h3>
            <div class="space-y-3">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">رمز عبور فعلی</label>
                <input
                  type="password"
                  v-model="password.current"
                  placeholder="رمز عبور فعلی را وارد کنید"
                  class="w-full px-4 py-3 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900 transition-all"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">رمز عبور جدید</label>
                <input
                  type="password"
                  v-model="password.new"
                  placeholder="رمز عبور جدید را وارد کنید"
                  class="w-full px-4 py-3 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900 transition-all"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">تأیید رمز عبور</label>
                <input
                  type="password"
                  v-model="password.confirm"
                  placeholder="رمز عبور جدید را دوباره وارد کنید"
                  class="w-full px-4 py-3 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900 transition-all"
                />
              </div>
              <button
                @click="updatePassword"
                :disabled="!password.current || !password.new || !password.confirm || loadingPassword"
                class="w-full px-6 py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all font-medium mt-2"
              >
                {{ loadingPassword ? 'درحال...' : 'تغییر رمز عبور' }}
              </button>
            </div>
            <p v-if="messages.password" :class="messages.passwordSuccess ? 'text-green-600' : 'text-red-600'" class="text-sm mt-2">
              {{ messages.password }}
            </p>
          </div>
        </div>

        <!-- Right: Profile Image -->
        <div class="lg:col-span-1">
          <div class="sticky top-8">
            <!-- Image Preview Container -->
            <div class="mb-6 text-center">
              <div class="w-48 h-48 mx-auto bg-gradient-to-br from-slate-100 to-slate-200 rounded-2xl flex items-center justify-center overflow-hidden shadow-xl border-4 border-white mb-4 relative group">
                <img
                  v-if="profileImage"
                  :src="profileImage"
                  alt="Profile"
                  class="w-full h-full object-cover"
                />
                <svg
                  v-else
                  class="w-20 h-20 text-slate-400"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>
              </div>
              <p class="text-slate-600 text-sm">{{ profileImage ? '✓ عکس آپلود شد' : 'عکس پروفایل خود را آپلود کنید' }}</p>
            </div>

            <!-- Upload Options -->
            <div class="space-y-2">
              <input
                ref="fileInput"
                type="file"
                accept="image/*"
                @change="handleImageUpload"
                class="hidden"
              />
              
              <button
                @click="$refs.fileInput.click()"
                class="w-full px-4 py-3 bg-slate-900 text-white rounded-lg hover:bg-slate-800 transition-all font-medium flex items-center justify-center gap-2 shadow-md hover:shadow-lg"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                </svg>
                آپلود عکس
              </button>

              <button
                v-if="profileImage"
                @click="removeImage"
                class="w-full px-4 py-3 bg-gradient-to-r from-red-500 to-red-600 text-white rounded-lg hover:from-red-600 hover:to-red-700 transition-all font-medium shadow-md hover:shadow-lg"
              >
                حذف عکس
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: '',
        email: '',
        first_name: '',
        last_name: ''
      },
      originalForm: {
        username: '',
        email: '',
        first_name: '',
        last_name: ''
      },
      password: {
        current: '',
        new: '',
        confirm: ''
      },
      profileImage: null,
      
      // Loading states
      loadingUsername: false,
      loadingEmail: false,
      loadingName: false,
      loadingPassword: false,
      
      // Messages
      messages: {
        username: '',
        usernameSuccess: false,
        email: '',
        emailSuccess: false,
        name: '',
        nameSuccess: false,
        password: '',
        passwordSuccess: false
      }
    }
  },
  mounted() {
    this.loadProfile()
  },
  methods: {
    // ✅ API Call Helper
    async apiCall(endpoint, options = {}) {
      const token = localStorage.getItem('admin_token') || 
                    localStorage.getItem('access_token') ||
                    localStorage.getItem('token')
      
      if (!token) {
        console.error('❌ No token found')
        this.$router.push('/admin/login')
        return null
      }

      const url = `https://polychemmb.com/api${endpoint}`
      
      const response = await fetch(url, {
        method: options.method || 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: options.body ? JSON.stringify(options.body) : undefined
      })

      if (response.status === 401) {
        localStorage.clear()
        this.$router.push('/admin/login')
        return null
      }

      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status}`)
      }

      return await response.json()
    },

    // ✅ Load Profile
    async loadProfile() {
      try {
        const data = await this.apiCall('/admin/profile')
        
        if (data?.success && data?.data) {
          this.form = {
            username: data.data.username || '',
            email: data.data.email || '',
            first_name: data.data.first_name || '',
            last_name: data.data.last_name || ''
          }
          this.originalForm = JSON.parse(JSON.stringify(this.form))
          console.log('✅ Profile loaded:', this.form)
        }
      } catch (error) {
        console.error('❌ Error loading profile:', error)
      }
    },

    // ✅ Update Username
    async updateUsername() {
      try {
        this.loadingUsername = true
        const data = await this.apiCall('/admin/update-username', {
          method: 'PUT',
          body: { username: this.form.username }
        })

        if (data?.success) {
          this.originalForm.username = this.form.username
          this.messages.username = '✓ نام کاربری با موفقیت تغییر کرد'
          this.messages.usernameSuccess = true
          setTimeout(() => { this.messages.username = '' }, 3000)
        } else {
          this.messages.username = data?.message || 'خطا'
          this.messages.usernameSuccess = false
        }
      } catch (error) {
        this.messages.username = error.message
        this.messages.usernameSuccess = false
      } finally {
        this.loadingUsername = false
      }
    },

    // ✅ Update Email
    async updateEmail() {
      try {
        this.loadingEmail = true
        const data = await this.apiCall('/admin/update-email', {
          method: 'PUT',
          body: { email: this.form.email }
        })

        if (data?.success) {
          this.originalForm.email = this.form.email
          this.messages.email = '✓ ایمیل با موفقیت تغییر کرد'
          this.messages.emailSuccess = true
          setTimeout(() => { this.messages.email = '' }, 3000)
        } else {
          this.messages.email = data?.message || 'خطا'
          this.messages.emailSuccess = false
        }
      } catch (error) {
        this.messages.email = error.message
        this.messages.emailSuccess = false
      } finally {
        this.loadingEmail = false
      }
    },

    // ✅ Update Name - FIXED (الگ الگ fields)
    async updateName() {
      try {
        this.loadingName = true
        
        console.log('📤 Sending:', {
          first_name: this.form.first_name,
          last_name: this.form.last_name
        })

        const data = await this.apiCall('/admin/update-name', {
          method: 'PUT',
          body: { 
            first_name: this.form.first_name,
            last_name: this.form.last_name
          }
        })

        console.log('📥 Response:', data)

        if (data?.success) {
          this.originalForm.first_name = this.form.first_name
          this.originalForm.last_name = this.form.last_name
          this.messages.name = '✓ نام با موفقیت تغییر کرد'
          this.messages.nameSuccess = true
          
          // ✅ Navbar کو update کریں
          setTimeout(() => {
            this.$root.$emit('profile-updated', {
              first_name: this.form.first_name,
              last_name: this.form.last_name,
              email: this.form.email
            })
          }, 500)
          
          setTimeout(() => { this.messages.name = '' }, 3000)
        } else {
          this.messages.name = data?.message || 'خطا'
          this.messages.nameSuccess = false
        }
      } catch (error) {
        console.error('❌ Error:', error)
        this.messages.name = error.message
        this.messages.nameSuccess = false
      } finally {
        this.loadingName = false
      }
    },

    // ✅ Update Password
    async updatePassword() {
      try {
        this.loadingPassword = true
        const data = await this.apiCall('/admin/change-password', {
          method: 'PUT',
          body: {
            current_password: this.password.current,
            new_password: this.password.new,
            confirm_password: this.password.confirm
          }
        })

        if (data?.success) {
          this.password = { current: '', new: '', confirm: '' }
          this.messages.password = '✓ رمز عبور با موفقیت تغییر کرد'
          this.messages.passwordSuccess = true
          setTimeout(() => { this.messages.password = '' }, 3000)
        } else {
          this.messages.password = data?.message || 'خطا'
          this.messages.passwordSuccess = false
        }
      } catch (error) {
        this.messages.password = error.message
        this.messages.passwordSuccess = false
      } finally {
        this.loadingPassword = false
      }
    },

    // Image Upload
    handleImageUpload(event) {
      const file = event.target.files[0]
      if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
          this.profileImage = e.target.result
        }
        reader.readAsDataURL(file)
      }
    },

    removeImage() {
      this.profileImage = null
    }
  }
}
</script>

<style scoped>
input[type="text"],
input[type="email"],
input[type="password"] {
  transition: all 0.3s ease;
}

input[type="text"]:hover,
input[type="email"]:hover,
input[type="password"]:hover {
  border-color: #cbd5e1;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus {
  outline: none;
  border-color: #1f2937;
  box-shadow: 0 0 0 3px rgba(31, 41, 55, 0.1);
}

button {
  transition: all 0.3s ease;
}

button:active:not(:disabled) {
  transform: scale(0.98);
}
</style>