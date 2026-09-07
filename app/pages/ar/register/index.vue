<template>
  <div class="min-h-screen flex items-center justify-center bg-[#f1f2f2] p-6 font-sans relative text-[#808285]">
    <!-- Desktop logo (keep for md+) -->
    <NuxtLink to="/" class="absolute top-4 left-4 z-20 hidden md:block" aria-label="Home">
      <img src="/polychem wall B.png" alt="Logo" class="w-40 h-auto" />
    </NuxtLink>

    <!-- Mobile background (behind the white card) - mobile only -->
    <div class="mobile-bg md:hidden" aria-hidden="true">
      <div class="mobile-bg-frame">
        <img
          src="/login.webp"
          alt="Mobile background"
          class="mobile-bg-img"
          :style="{'--img-translate': imgTranslate + 'px', '--img-y': imgY + 'px'}"
          ref="mobileImgRef"
        />
      </div>
    </div>

    <div class="bg-white rounded-xl shadow-lg h-[640px] max-w-5xl w-full flex flex-col md:flex-row overflow-hidden md:h-[580px] relative form-card">
      <!-- Left Image (Desktop only, matching login) -->
      <div class="hidden md:block md:flex-1 h-full w-[600px]">
        <img src="/login.webp" alt="Form Image" class="w-full h-full object-cover" />
      </div>

      <!-- Form -->
      <form @submit.prevent="onSubmit" class="w-full md:w-[420px] p-8 flex flex-col items-center justify-center h-full pt-0 relative">
        <!-- Mobile logo on top-left of form -->
        <NuxtLink to="/" class="mobile-logo md:hidden absolute top-4 left-4 z-20" aria-label="Home">
          <img src="/polychem wall B.png" alt="Logo" class="w-28 h-auto" />
        </NuxtLink>

        <!-- Back to Home -->
        <a href="/" aria-label="Back to home" class="absolute top-4 right-4 text-gray-500 hover:text-gray-700 text-2xl leading-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/>
          </svg>
        </a>

        <!-- Logo & Heading -->
        <div class="text-center mb-8">
          <h1 class="text-2xl font-semibold mb-2">Create Account</h1>
          <p>Please fill out all the required fields to create your account!</p>
        </div>

        <!-- Step Indicators -->
        <div class="w-full max-w-[480px] mb-6 flex items-center justify-center gap-2">
          <span :class="['h-2 w-2 rounded-full', currentStep === 1 ? 'bg-[#FFCD05]' : 'bg-gray-300']"></span>
          <span :class="['h-2 w-2 rounded-full', currentStep === 2 ? 'bg-[#FFCD05]' : 'bg-gray-300']"></span>
          <span :class="['h-2 w-2 rounded-full', currentStep === 3 ? 'bg-[#FFCD05]' : 'bg-gray-300']"></span>
          <span :class="['h-2 w-2 rounded-full', currentStep === 4 ? 'bg-[#FFCD05]' : 'bg-gray-300']"></span>
          <span :class="['h-2 w-2 rounded-full', currentStep === 5 ? 'bg-[#FFCD05]' : 'bg-gray-300']"></span>
        </div>

        <!-- Slides -->
        <div class="w-full max-w-[480px] flex flex-col gap-6">
          <!-- Step 1: Account (Username/Email) -->
          <div v-if="currentStep === 1" class="flex flex-col gap-6">
            <div class="relative">
              <input required type="text" id="username" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white" v-model="form.username" />
              <label for="username" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Username</label>
            </div>
            <div class="relative">
              <input required type="email" id="email" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white" v-model="form.email" />
              <label for="email" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Email</label>
            </div>
          </div>

          <!-- Step 2: Passwords -->
          <div v-if="currentStep === 2" class="flex flex-col gap-6">
            <div class="relative">
              <input required :type="showPassword ? 'text' : 'password'" id="password" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white pr-10" v-model="form.password" />
              <label for="password" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Password</label>
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute right-0 top-1/2 -translate-y-1/2 p-2 text-gray-500 hover:text-gray-700 focus-visible:outline-none"
                aria-label="Toggle password visibility"
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
            <div class="relative">
              <input required :type="showConfirmPassword ? 'text' : 'password'" id="confirmPassword" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white pr-10" v-model="form.confirmPassword" />
              <label for="confirmPassword" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Confirm Password</label>
              <button
                type="button"
                @click="showConfirmPassword = !showConfirmPassword"
                class="absolute right-0 top-1/2 -translate-y-1/2 p-2 text-gray-500 hover:text-gray-700 focus-visible:outline-none"
                aria-label="Toggle confirm password visibility"
              >
                <svg v-if="!showConfirmPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
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
          </div>

          <!-- Step 3: Personal -->
          <div v-if="currentStep === 3" class="flex flex-col gap-6">
            <div class="relative">
              <input required type="text" id="firstName" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white" v-model="form.firstName" />
              <label for="firstName" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">First Name</label>
            </div>
            <div class="relative">
              <input required type="text" id="lastName" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white" v-model="form.lastName" />
              <label for="lastName" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Last Name</label>
            </div>
          </div>

          <!-- Step 4: Company -->
          <div v-if="currentStep === 4" class="flex flex-col gap-6">
            <div class="relative">
              <input required type="text" id="company" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white" v-model="form.companyName" />
              <label for="company" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Company Name</label>
            </div>
            <div class="relative">
              <input required type="text" id="jobTitle" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white" v-model="form.jobTitle" />
              <label for="jobTitle" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Job Title</label>
            </div>
          </div>

          <!-- Step 5: Phone -->
          <div v-if="currentStep === 5" class="flex flex-col gap-6">
            <div class="relative">
              <input required type="tel" id="phone" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white pr-28" v-model="form.phoneNumber" />
              <label for="phone" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Phone Number</label>
              <button
                type="button"
                @click="onSendCode"
                class="absolute right-0 top-1/2 -translate-y-1/2 px-3 py-1.5 text-sm border border-[#FFCD05] text-[#FFCD05] rounded-md hover:bg-[#FFCD05] hover:text-white"
              >
                Send code
              </button>
            </div>
            <div class="relative">
              <input required type="text" id="verificationCode" placeholder=" " class="peer w-full border-b-2 border-gray-300 focus:border-[#FFCD05] outline-none py-2 bg-white" v-model="form.verificationCode" />
              <label for="verificationCode" class="absolute left-0 top-2 text-gray-400 text-sm transition-all
                peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-sm
                peer-focus:-top-4 peer-focus:text-[#FFCD05] peer-focus:text-sm
                peer-[:not(:placeholder-shown)]:-top-4 peer-[:not(:placeholder-shown)]:text-gray-700 peer-[:not(:placeholder-shown)]:text-sm">Verification Code</label>
            </div>
          </div>
        </div>

        <!-- Navigation -->
        <div class="w-full max-w-[480px] mt-6 flex items-center justify-between">
          <button
            type="button"
            class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50"
            :disabled="currentStep === 1"
            @click="onBack"
          >
            Back
          </button>
          <button
            v-if="currentStep < totalSteps"
            type="button"
            class="btn-slide-down h-11 px-6 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors"
            @click="onNext"
          >
            <span class="relative z-10">Next</span>
          </button>
          <button
            v-else
            type="submit"
            class="btn-slide-down h-11 px-6 rounded-lg relative overflow-hidden border-2 border-[#FFCD05] text-[#FFCD05] transition-colors"
          >
            <span class="relative z-10">Create Account</span>
          </button>
        </div>

        <!-- Footer links -->
        <div class="w-full max-w-[480px] mt-6 text-center text-sm text-gray-600 relative pb-10">
          <p>Already have an account? <NuxtLink to="/login" class="text-[#FFCD05] hover:text-[#808285]">Login</NuxtLink></p>
          <div class="absolute right-0 -bottom-12 text-right">
            <div class="inline-flex items-center gap-2 cursor-pointer select-none">
              <span class="">English</span>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 9l6 6 6-6"/>
              </svg>
            </div>
          </div>
        </div>
      </form>
    </div>

    <!-- Mobile navbar at bottom -->
    <div class="md:hidden">
      <NavbarMob />
    </div>

    <!-- Chat widget (always present on page) -->
    <Chatbox />
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import NavbarMob from "~/components/ar/layout/navbar-mob.vue"
import Chatbox from '~/components/en/chatbox/chatbox.vue'

const form = reactive({
  username: '',
  firstName: '',
  lastName: '',
  companyName: '',
  jobTitle: '',
  email: '',
  phoneNumber: '',
  verificationCode: '',
  password: '',
  confirmPassword: ''
})

const showPassword = ref(false)
const showConfirmPassword = ref(false)
const currentStep = ref(1)
const totalSteps = 5

// control image translation on mobile (px)
const imgTranslate = ref(0)
const imgY = ref(-80) // مقدار پیش‌فرض: تصویر را بالا می‌بریم تا پایینش دیده شود (px)
const mobileImgRef = ref(null)

const onSubmit = () => {
  if (form.password !== form.confirmPassword) {
    alert('Passwords do not match!')
    return
  }
  console.log('Register:', form)
}

const onSendCode = () => {
  if (!form.phoneNumber) {
    alert('Please enter your phone number first.')
    return
  }
  console.log('Send verification code to:', form.phoneNumber)
}

const validateStep = (step: number) => {
  if (step === 1) {
    if (!form.username || !form.email) {
      alert('Please complete all required fields.')
      return false
    }
  } else if (step === 2) {
    if (!form.password || !form.confirmPassword) {
      alert('Please enter and confirm your password.')
      return false
    }
    if (form.password !== form.confirmPassword) {
      alert('Passwords do not match!')
      return false
    }
  } else if (step === 3) {
    if (!form.firstName || !form.lastName) {
      alert('Please enter your first and last name.')
      return false
    }
  } else if (step === 4) {
    if (!form.companyName || !form.jobTitle) {
      alert('Please complete company information.')
      return false
    }
  } else if (step === 5) {
    if (!form.phoneNumber || !form.verificationCode) {
      alert('Please enter phone number and verification code.')
      return false
    }
  }
  return true
}

const onNext = () => {
  if (validateStep(currentStep.value)) {
    currentStep.value += 1
  }
}

const onBack = () => {
  if (currentStep.value > 1) currentStep.value -= 1
}
</script>

<style scoped>
/* match login autofill + background behavior */
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

/* Hover filled slide down button effect (same as login) */
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

/* Mobile background positioned behind the white card (mobile only) */
.mobile-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50vh; /* نصف ارتفاع صفحه */
  z-index: 0;
  pointer-events: none;
}
.mobile-bg-frame {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: relative;
  /* بدون برش تا تصویر کامل پشت کارت نشان داده شود */
}
.mobile-bg-img {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, var(--img-y, 0px)) translateX(var(--img-translate, 0px));
  width: 120%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
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

/* Mobile navbar (same as login) */
.navbar-mob {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 64px;
  background-color: #ffffff;
  border-top: 1px solid #eaeaea;
  display: flex;
  align-items: center;
  justify-content: space-around;
  z-index: 20;
}
.navbar-mob a {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: #808285;
  font-size: 12px;
  position: relative;
}
.navbar-mob a.active {
  color: #FFCD05;
}
.navbar-mob svg {
  margin-bottom: 2px;
}
</style>