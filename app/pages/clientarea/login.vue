<!-- /clientarea/login.vue -->
<template>
  <div
    class="min-h-screen flex items-center justify-center bg-[#f1f2f2] p-6 relative text-[#808285]"
    :class="[isRtl ? 'font-[IRANYekan] rtl' : 'font-sans ltr']"
    :dir="isRtl ? 'rtl' : 'ltr'"
  >
    <!-- Desktop logo -->
    <NuxtLink
      :to="isRtl ? '/fa' : '/en'"
      class="absolute top-4 z-20 hidden md:block"
      :class="isRtl ? 'right-4' : 'left-4'"
      :aria-label="t('home')"
    >
      <img src="/polychem wall B.png" alt="Logo" class="w-40 h-auto" />
    </NuxtLink>

    <!-- Mobile background -->
    <div class="mobile-bg md:hidden" aria-hidden="true">
      <div class="mobile-bg-frame">
        <img src="/login.webp" :alt="t('mobileBg')" class="mobile-bg-img" />
      </div>
    </div>

    <div class="bg-white rounded-xl shadow-lg h-[640px] max-w-5xl w-full flex flex-col overflow-hidden md:h-[580px] relative form-card"
      :class="isRtl ? 'md:flex-row-reverse' : 'md:flex-row'"
    >

      <!-- Side Image (Desktop only) -->
      <div class="hidden md:block md:flex-1 h-full w-[600px]">
        <img src="/login.webp" :alt="t('formImage')" class="w-full h-full object-cover" />
      </div>

      <!-- Form -->
      <form
        @submit.prevent="handleLogin"
        class="w-full md:w-[420px] p-8 flex flex-col items-center justify-center h-full pt-0 relative"
      >
        <!-- Mobile logo -->
        <NuxtLink
          :to="isRtl ? '/fa' : '/en'"
          class="mobile-logo md:hidden absolute top-4 z-20"
          :class="isRtl ? 'right-4' : 'left-4'"
          :aria-label="t('home')"
        >
          <img src="/polychem wall B.png" alt="Logo" class="w-28 h-auto" />
        </NuxtLink>

        <!-- Back to Home arrow -->
        <NuxtLink
          :to="isRtl ? '/fa' : '/en'"
          :aria-label="t('backHome')"
          class="absolute top-4 right-4 text-gray-500 hover:text-gray-700 text-2xl leading-none"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/>
          </svg>
        </NuxtLink>

        <!-- Language Toggle -->
        <button
          type="button"
          @click="toggleLanguage"
          class="absolute top-14 left-4 z-20 text-xs border border-gray-300 rounded-full px-3 py-1 hover:border-[#FFCD05] hover:text-[#FFCD05] transition-colors"
        >
          {{ isRtl ? 'EN' : 'FA' }}
        </button>

        <!-- Heading -->
        <div class="text-center mb-8">
          <h1 class="text-2xl font-semibold mb-2">{{ t('title') }}</h1>
          <p>{{ t('subtitle') }}</p>
        </div>

        <!-- Error Message -->
        <div
          v-if="errorMessage"
          class="w-full max-w-[420px] mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded-lg text-sm"
        >
          {{ errorMessage }}
        </div>

        <!-- Success Message -->
        <div
          v-if="successMessage"
          class="w-full max-w-[420px] mb-4 p-3 bg-green-100 border border-green-400 text-green-700 rounded-lg text-sm"
        >
          {{ successMessage }}
        </div>

        <!-- Input Fields -->
        <div class="w-full max-w-[420px] flex flex-col gap-6">

          <!-- Username -->
          <div class="relative">
            <input
              required
              type="text"
              id="username"
              v-model="form.username"
              placeholder=" "
              class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white"
              :class="isRtl ? 'text-right' : 'text-left'"
              :disabled="loading"
              autocomplete="username"
            />
            <label
              for="username"
              class="absolute top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm"
              :class="isRtl ? 'right-0' : 'left-0'"
            >
              {{ t('username') }}
            </label>
          </div>

          <!-- Password -->
          <div class="relative">
            <input
              required
              :type="showPassword ? 'text' : 'password'"
              id="password"
              v-model="form.password"
              placeholder=" "
              class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white"
              :class="isRtl ? 'text-right pl-10 pr-0' : 'text-left pr-10 pl-0'"
              :disabled="loading"
              autocomplete="current-password"
            />
            <label
              for="password"
              class="absolute top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm"
              :class="isRtl ? 'right-0' : 'left-0'"
            >
              {{ t('password') }}
            </label>

            <!-- Show/Hide password toggle -->
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute top-1/2 -translate-y-1/2 p-2 text-gray-500 hover:text-gray-700 focus-visible:outline-none"
              :class="isRtl ? 'left-0' : 'right-0'"
              :aria-label="t('togglePassword')"
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

          <!-- Forgot Password -->
          <NuxtLink
            :to="isRtl ? '/fa/forgot-password' : '/en/forgot-password'"
            class="hover:text-[#FFCD05] text-sm"
            :class="isRtl ? 'text-right' : 'text-left'"
          >
            {{ t('forgotPassword') }}
          </NuxtLink>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading"
            class="btn-slide-down w-full h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors disabled:opacity-50"
          >
            <span class="relative z-10">
              {{ loading ? t('signingIn') : t('signIn') }}
            </span>
          </button>
        </div>

        <!-- Footer -->
        <div class="w-full max-w-[480px] mt-6 text-center text-sm text-gray-600 relative pb-3">
          <p>
            {{ t('noAccount') }}
            <NuxtLink
              :to="isRtl ? '/fa/contact' : '/en/contact'"
              class="text-[#FFCD05] hover:text-[#808285]"
            >
              {{ t('contactUs') }}
            </NuxtLink>
          </p>
        </div>

        <!-- Admin Login -->
        <div class="pb-5">
          <NuxtLink
            to="/admin/login"
            class="flex items-center gap-1.5 text-gray-300 hover:text-gray-400 transition-colors group"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            <span class="text-xs">{{ t('adminLogin') }}</span>
          </NuxtLink>
        </div>
      </form>
    </div>

    <!-- Mobile navbar -->
    <div class="md:hidden">
      <NavbarMob />
    </div>

    <!-- Chat widget -->
    <Chatbox />
  </div>
</template>

<script setup>
const router = useRouter()

// ─── Language ────────────────────────────────────────────────────────────────

// خوندن زبان قبل از رندر — قبل از onMounted
const currentLang = useState('login_lang', () => {
  if (process.client) {
    const saved = localStorage.getItem('preferred_language')
    return saved === 'fa' ? 'fa' : 'en'
  }
  return 'en'
})

const isRtl = computed(() => currentLang.value === 'fa')

const translations = {
  en: {
    home:           'Home',
    backHome:       'Back to home',
    mobileBg:       'Mobile background',
    formImage:      'Form Image',
    title:          'Client Login',
    subtitle:       'Sign in to access your dashboard.',
    username:       'Username',
    password:       'Password',
    togglePassword: 'Toggle password visibility',
    forgotPassword: 'Forgot your password?',
    signingIn:      'Signing in...',
    signIn:         'Sign in',
    noAccount:      'Need an account?',
    contactUs:      'Contact Us',
    fillFields:     'Please fill in all fields',
    loginSuccess:   'Login successful! Redirecting...',
    noToken:        'No access token received from server',
    loginError:     'An error occurred',
    adminLogin:     'Admin Panel',
  },
  fa: {
    home:           'خانه',
    backHome:       'بازگشت به خانه',
    mobileBg:       'پس‌زمینه موبایل',
    formImage:      'تصویر فرم',
    title:          'ورود مشتریان',
    subtitle:       'برای دسترسی به داشبورد خود وارد شوید.',
    username:       'نام کاربری',
    password:       'رمز عبور',
    togglePassword: 'نمایش/مخفی کردن رمز عبور',
    forgotPassword: 'رمز عبور خود را فراموش کرده‌اید؟',
    signingIn:      'در حال ورود...',
    signIn:         'ورود',
    noAccount:      'نیاز به حساب کاربری دارید؟',
    contactUs:      'تماس با ما',
    fillFields:     'لطفاً تمام فیلدها را پر کنید',
    loginSuccess:   'ورود موفقیت‌آمیز! در حال انتقال...',
    noToken:        'توکن دسترسی از سرور دریافت نشد',
    loginError:     'خطایی رخ داده است',
    adminLogin:     'پنل ادمین',
  }
}

const t = (key) => translations[currentLang.value][key] ?? key

const toggleLanguage = () => {
  currentLang.value = isRtl.value ? 'en' : 'fa'
  if (process.client) {
    localStorage.setItem('preferred_language', currentLang.value)
  }
}

// ─── API — زبان روی بک‌اند تأثیر نمی‌گذارد ──────────────────────────────────
const API_URL = 'https://polychemmb.com/api/client'

// ─── Form state ──────────────────────────────────────────────────────────────
const showPassword  = ref(false)
const loading       = ref(false)
const errorMessage  = ref('')
const successMessage = ref('')

const form = ref({
  username: '',
  password: ''
})

// ─── Login handler ────────────────────────────────────────────────────────────
const handleLogin = async () => {
  if (!form.value.username || !form.value.password) {
    errorMessage.value = t('fillFields')
    return
  }

  loading.value      = true
  errorMessage.value  = ''
  successMessage.value = ''

  try {
    const response = await fetch(`${API_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: form.value.username,
        password: form.value.password
      })
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.message || t('loginError'))
    }

    if (process.client) {
      const accessToken  = data.access_token || data.token
      const refreshToken = data.refresh_token

      if (!accessToken) throw new Error(t('noToken'))

      localStorage.setItem('client_token',         accessToken)
      localStorage.setItem('client_refresh_token', refreshToken)
      localStorage.setItem('client_user',          JSON.stringify(data.user || data.client))
    }

    successMessage.value = t('loginSuccess')
    setTimeout(() => router.push('/clientarea'), 1000)

  } catch (error) {
    errorMessage.value = error.message || t('loginError')
  } finally {
    loading.value = false
  }
}

// ─── Clear errors on typing ───────────────────────────────────────────────────
watch(() => form.value.username, () => { if (errorMessage.value) errorMessage.value = '' })
watch(() => form.value.password, () => { if (errorMessage.value) errorMessage.value = '' })


</script>

<style scoped>
input {
  background-color: #ffffff !important;
}

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
  -webkit-box-shadow: 0 0 0 1000px #ffffff inset !important;
  box-shadow:         0 0 0 1000px #ffffff inset !important;
  -webkit-text-fill-color: #111111 !important;
  caret-color: #111111;
  transition: background-color 5000s ease-in-out 0s;
}

/* ── Slide-down button ── */
.btn-slide-down { background-color: transparent; }
.btn-slide-down::before {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 100%; height: 100%;
  background-color: #FFCD05;
  transform: translateY(-100%);
  transition: transform 300ms ease;
  z-index: 0;
}
.btn-slide-down:hover::before,
.btn-slide-down:focus-visible::before { transform: translateY(0); }
.btn-slide-down:hover,
.btn-slide-down:focus-visible { color: #ffffff; outline: none; }

/* ── Mobile background ── */
.mobile-bg {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 50vh;
  z-index: 0;
  pointer-events: none;
}
.mobile-bg-frame { width: 100%; height: 100%; overflow: hidden; position: relative; }
.mobile-bg-img {
  position: absolute;
  top: 0; left: 50%;
  transform: translate(-50%, -80px);
  width: 120%; height: 100%;
  object-fit: cover;
  opacity: 0.95;
  object-position: center bottom;
}

.form-card   { z-index: 5; position: relative; }
.mobile-logo { z-index: 10; }
</style>