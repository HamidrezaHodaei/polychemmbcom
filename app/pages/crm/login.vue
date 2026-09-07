<!-- pages/Crm/login.vue -->
<template>
  <div class="min-h-screen flex items-center justify-center p-4 bg-wrapper">
    <div class="w-full max-w-6xl bg-gradient-to-br from-orange-50 via-amber-50 to-yellow-100 rounded-3xl shadow-2xl overflow-hidden flex">

      <!-- Left Panel - Form -->
      <div class="w-full lg:w-5/12 p-8 lg:p-12 flex flex-col">
        <!-- Logo -->
        <div class="mb-12">
          <img src="/polychem.png" alt="Logo" class="h-20" />
        </div>

        <!-- Form Content -->
        <div class="flex-1 flex flex-col justify-center max-w-md">
          <h1 class="text-3xl lg:text-4xl font-bold text-[#848484] tracking-tight mb-2" style="font-family: 'Montserrat', sans-serif;">
            Welcome Back
          </h1>
          <p class="text-[#848484] mb-8" style="font-family: 'Montserrat', sans-serif;">
            Please enter your details to access the control center.
          </p>

          <!-- پیام خطا -->
          <div v-if="errorMessage" class="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded-lg text-sm">
            {{ errorMessage }}
          </div>

          <!-- پیام موفقیت -->
          <div v-if="successMessage" class="mb-4 p-3 bg-green-100 border border-green-400 text-green-700 rounded-lg text-sm">
            {{ successMessage }}
          </div>

          <!-- فرم ورود -->
          <div class="space-y-5">
            <!-- Username -->
            <div>
              <label class="block text-sm text-gray-600 mb-2">Username</label>
              <input
                v-model="form.username"
                type="text"
                placeholder="admin"
                autocomplete="username"
                class="w-full px-4 py-3 bg-white/70 border border-transparent rounded-xl focus:outline-none focus:ring-2 focus:ring-yellow-400 transition"
                @keyup.enter="handleLogin"
                :disabled="loading"
              />
            </div>

            <!-- Password -->
            <div>
              <label class="block text-sm text-gray-600 mb-2">Password</label>
              <div class="relative">
                <input
                  v-model="form.password"
                  :type="showPassword ? 'text' : 'password'"
                  placeholder="••••••••••••••••••"
                  autocomplete="current-password"
                  class="w-full px-4 py-3 bg-white/70 border border-transparent rounded-xl focus:outline-none focus:ring-2 focus:ring-yellow-400 transition"
                  @keyup.enter="handleLogin"
                  :disabled="loading"
                />
                <button
                  type="button"
                  @click="showPassword = !showPassword"
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
                  :disabled="loading"
                >
                  <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                  <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                  </svg>
                </button>
              </div>
            </div>

            <!-- Submit Button -->
            <button
              @click="handleLogin"
              :disabled="loading"
              class="btn-slide-down w-full h-12 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span class="relative z-10">{{ loading ? 'در حال ورود...' : 'ورود به پنل' }}</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Right Panel - Image/Content -->
      <div class="hidden lg:block lg:w-7/12 relative rounded-l-[3rem] overflow-hidden">
        <img
          src="/right-a.webp"
          alt="CRM PolyChem"
          class="w-full h-full object-cover"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCrmAuth } from '~/composables/useCrmAuth'

// این صفحه هیچ میدل‌وری ندارد چون خودش صفحه لاگین است
definePageMeta({
  layout: false,
})

const router = useRouter()
const { setCrmToken, isCrmAuthenticated } = useCrmAuth()

// آدرس بک‌اند CRM — کاملاً مستقل از بک‌اند اصلی PolyChem
// از همون متغیر محیطی که در index.vue استفاده می‌شود می‌خواند
const API_BASE = import.meta.env.VITE_API_BASE ||'https://crmapi.polychemmb.com'

const loading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')
const showPassword = ref(false)

const form = ref({
  username: '',
  password: '',
})

// اگر کاربر از قبل لاگین است مستقیم به داشبورد برود
onMounted(() => {
  if (isCrmAuthenticated()) {
    router.push('/Crm')
  }
})

async function handleLogin() {
  if (!form.value.username || !form.value.password) {
    errorMessage.value = 'لطفاً نام کاربری و رمز عبور را وارد کنید'
    return
  }

  loading.value = true
  errorMessage.value = ''
  successMessage.value = ''

  try {
    const response = await fetch(`${API_BASE}/api/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: form.value.username,
        password: form.value.password,
      }),
    })

    const result = await response.json()

    if (!response.ok || !result.success) {
      throw new Error(result.message || 'ورود ناموفق بود')
    }

    // ذخیره توکن‌ها با composable
    setCrmToken(result.data.token, result.data.refresh_token, result.data.user)

    successMessage.value = 'ورود موفقیت‌آمیز بود! در حال انتقال...'

    setTimeout(() => {
      router.push('/Crm')
    }, 600)

  } catch (error) {
    errorMessage.value = error.message || 'خطایی رخ داد. دوباره تلاش کنید.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.bg-wrapper {
  background-image: url('/tehran.jpg');
  background-size: 90%;
  background-position: 190% center;
  background-attachment: fixed;
  position: relative;
}

.bg-wrapper::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: inherit;
  background-attachment: fixed;
  filter: grayscale(100%);
  pointer-events: none;
  z-index: 0;
}

.bg-wrapper > div {
  position: relative;
  z-index: 1;
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
</style>
