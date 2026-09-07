<!-- /fa/login/index.vue -->
<template>
  <div class="min-h-screen flex items-center justify-center bg-[#f1f2f2] p-6 font-[IRANYekan] relative text-[#808285] rtl" dir="rtl">
    <!-- Desktop logo -->
    <NuxtLink to="/" class="absolute top-4 right-4 z-20 hidden md:block" aria-label="خانه">
      <img src="/polychem wall B.png" alt="لوگو" class="w-40 h-auto" />
    </NuxtLink>

    <!-- Mobile background -->
    <div class="mobile-bg md:hidden" aria-hidden="true">
      <div class="mobile-bg-frame">
        <img src="/login.webp" alt="پس‌زمینه موبایل" class="mobile-bg-img" />
      </div>
    </div>

    <div class="bg-white rounded-xl shadow-lg h-[640px] max-w-5xl w-full flex flex-col md:flex-row-reverse overflow-hidden md:h-[580px] relative form-card">
      
      <!-- Left Image (Desktop only) -->
      <div class="hidden md:block md:flex-1 h-full w-[600px]">
        <img src="/login.webp" alt="تصویر فرم" class="w-full h-full object-cover" />
      </div>

      <!-- Form -->
      <form @submit.prevent="handleLogin" class="w-full md:w-[420px] p-8 flex flex-col items-center justify-center h-full pt-0 relative">
        <!-- Mobile logo -->
        <NuxtLink to="/" class="mobile-logo md:hidden absolute top-4 right-4 z-20" aria-label="خانه">
          <img src="/polychem wall B.png" alt="لوگو" class="w-28 h-auto" />
        </NuxtLink>

        <!-- Back to Home -->
        <NuxtLink to="/" aria-label="بازگشت به خانه" class="absolute top-4 left-4 text-gray-500 hover:text-gray-700 text-2xl leading-none translate-x-[370px]">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 " viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/>
          </svg>
        </NuxtLink>

        <!-- Logo & Heading -->
        <div class="text-center mb-8">
          <h1 class="text-2xl font-semibold mb-2">ورود مشتریان</h1>
          <p>برای دسترسی به داشبورد خود وارد شوید.</p>
        </div>

        <!-- Error/Success Messages -->
        <div v-if="errorMessage" class="w-full max-w-[420px] mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded-lg text-sm">
          {{ errorMessage }}
        </div>

        <div v-if="successMessage" class="w-full max-w-[420px] mb-4 p-3 bg-green-100 border border-green-400 text-green-700 rounded-lg text-sm">
          {{ successMessage }}
        </div>

        <!-- Input Fields -->
        <div class="w-full max-w-[420px] flex flex-col gap-6">
          <div class="relative">
            <input 
              required 
              type="text" 
              id="username" 
              v-model="form.username"
              placeholder=" " 
              class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white text-right" 
              :disabled="loading"
              autocomplete="username"
            />
            <label for="username" class="absolute right-0 top-2 text-gray-400 text-sm transition-all
              peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
              peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
              peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">نام کاربری</label>
          </div>

          <div class="relative">
            <input 
              required 
              :type="showPassword ? 'text' : 'password'" 
              id="password" 
              v-model="form.password"
              placeholder=" " 
              class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white pr-10 text-right" 
              :disabled="loading"
              autocomplete="current-password"
            />
            <label for="password" class="absolute right-0 top-2 text-gray-400 text-sm transition-all
              peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
              peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
              peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">رمز عبور</label>
            
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute left-0 top-1/2 -translate-y-1/2 p-2 text-gray-500 hover:text-gray-700 focus-visible:outline-none"
              aria-label="نمایش/مخفی کردن رمز عبور"
            >
              <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/>
                <circle cx="12" cy="12" r="3"/>
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 3l18 18"/>
                <path d="M10.6 10.6a3 3 0 004.2 4.2"/>
                <path d="M9.88 4.26A10.94 10.94 0 0112 4c6.5 0 10 8 10 8a17.44 17.44 0 01-3.36 4.58M6.61 6.61A17.53 17.53 0 002 12s3.5 7 10 7a10.82 10.82 0 004.39-.93"/>
              </svg>
            </button>
          </div>

          <button 
            type="submit" 
            :disabled="loading"
            class="btn-slide-down w-full h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors disabled:opacity-50"
          >
            <span class="relative z-10">{{ loading ? 'در حال ورود...' : 'ورود' }}</span>
          </button>
        </div>

        <!-- Footer links -->
        <div class="w-full max-w-[480px] mt-6 text-center text-sm text-gray-600 relative pb-10">
          <p>نیاز به حساب کاربری دارید؟ <NuxtLink to="/fa/contact" class="text-[#FFCD05] hover:text-[#808285]">تماس با ما</NuxtLink></p>
        </div>
      </form>
    </div>

    <!-- Mobile navbar at bottom -->
    <div class="md:hidden">
      <NavbarMob />
    </div>

    <!-- Chat widget -->
    <Chatbox />
  </div>
</template>

<script setup>
// import { useAuth } from '~/composables/useAuth'

const { setToken } = useAuth()
const router = useRouter()

const API_URL = 'http://localhost:8080/api/client'

const showPassword = ref(false)
const loading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const form = ref({
  username: '',
  password: ''
})

const handleLogin = async () => {
  if (!form.value.username || !form.value.password) {
    errorMessage.value = 'لطفاً تمام فیلدها را پر کنید'
    return
  }

  loading.value = true
  errorMessage.value = ''
  successMessage.value = ''

  try {
    const data = await $fetch(`${API_URL}/login`, {
      method: 'POST',
      body: {
        username: form.value.username,
        password: form.value.password
      }
    })

    // ذخیره توکن با استفاده از composable
    setToken(data.token, data.refresh_token, data.client)

    successMessage.value = 'ورود موفقیت‌آمیز! در حال انتقال...'
    
    setTimeout(() => {
      router.push('/clientarea')
    }, 1000)

  } catch (error) {
    console.error('Login error:', error)
    errorMessage.value = error.data?.message || error.message || 'خطایی رخ داده است'
  } finally {
    loading.value = false
  }
}

// پاک کردن پیام‌های خطا هنگام تایپ
watch(() => form.value.username, () => {
  if (errorMessage.value) errorMessage.value = ''
})

watch(() => form.value.password, () => {
  if (errorMessage.value) errorMessage.value = ''
})
</script>

<style scoped>
input {
  background-color: #ffffff !important;
}

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
  -webkit-box-shadow: 0 0 0 1000px #ffffff inset !important;
  box-shadow: 0 0 0 1000px #ffffff inset !important;
  -webkit-text-fill-color: #111111 !important;
  caret-color: #111111;
  transition: background-color 5000s ease-in-out 0s;
}

.btn-slide-down {
  background-color: transparent;
}
.btn-slide-down::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}
.btn-slide-down:hover::before,
.btn-slide-down:focus-visible::before {
  transform: translateY(0);
}
.btn-slide-down:hover,
.btn-slide-down:focus-visible {
  color: #ffffff;
  outline: none;
}

.mobile-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50vh;
  z-index: 0;
  pointer-events: none;
}

.mobile-bg-frame {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: relative;
}

.mobile-bg-img {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, -80px);
  width: 120%;
  height: 100%;
  object-fit: cover;
  opacity: 0.95;
  object-position: center bottom;
}

.form-card {
  z-index: 5;
  position: relative;
}

.mobile-logo {
  z-index: 10;
}
</style>
