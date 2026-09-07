<template>
  <div class="h-full overflow-y-auto custom-scrollbar pb-6 font-iranyekan" dir="rtl">
    <div class="grid grid-cols-12 gap-4">
      <!-- Left Column - Profile & Account -->
      <div class="col-span-8 space-y-4">
        <!-- Profile Card -->
        <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl border border-white/40">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-lg font-bold text-gray-900">اطلاعات پروفایل</h3>
            <button v-if="!editingProfile" @click="editingProfile = true" class="text-sm text-yellow-600 hover:text-yellow-700 font-semibold transition-colors">
              ویرایش
            </button>
            <button v-else @click="cancelEditProfile" class="text-sm text-red-600 hover:text-red-700 font-semibold transition-colors">
              انصراف
            </button>
          </div>

          <div class="flex items-center gap-6 mb-6">
            <!-- Profile Picture -->
            <div class="relative">
              <img v-if="profileImageUrl" :src="profileImageUrl" alt="Profile" class="w-24 h-24 rounded-2xl object-cover shadow-lg">
              <div v-else class="w-24 h-24 bg-gradient-to-br from-yellow-300 to-yellow-500 rounded-2xl flex items-center justify-center shadow-lg">
                <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
              </div>
              <button v-if="editingProfile" @click="$refs.fileInput.click()" class="absolute bottom-0 right-0 bg-yellow-400 hover:bg-yellow-500 w-7 h-7 rounded-full flex items-center justify-center shadow-lg transition-all hover:scale-110">
                <svg class="w-4 h-4 text-gray-900" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                </svg>
              </button>
              <input ref="fileInput" type="file" accept="image/*" @change="handleProfileImageChange" class="hidden">
            </div>
            
            <div class="flex-1">
              <p class="text-lg font-bold text-gray-900">{{ formData.first_name }} {{ formData.last_name }}</p>
              <p class="text-sm text-gray-600">{{ formData.email }}</p>
              <p class="text-xs text-gray-500 mt-2">شرکت: {{ formData.company_name || 'وارد نشده' }}</p>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">نام</label>
              <input v-model="formData.first_name" type="text" :disabled="!editingProfile" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 disabled:opacity-60">
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">نام خانوادگی</label>
              <input v-model="formData.last_name" type="text" :disabled="!editingProfile" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 disabled:opacity-60">
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">نام شرکت</label>
              <input v-model="formData.company_name" type="text" :disabled="!editingProfile" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 disabled:opacity-60">
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">شناسه اقتصادی</label>
              <input v-model="formData.economic_code" type="text" :disabled="!editingProfile" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 disabled:opacity-60" placeholder="مثال: 14006412345">
            </div>
            <div class="bg-white/40 rounded-2xl p-4 col-span-2">
              <label class="text-xs text-gray-600 block mb-2">آدرس ایمیل</label>
              <input v-model="formData.email" type="email" :disabled="!editingProfile" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 disabled:opacity-60">
            </div>
            <div class="bg-white/40 rounded-2xl p-4 col-span-2">
              <label class="text-xs text-gray-600 block mb-2">شماره تماس</label>
              <input v-model="formData.phone" type="tel" :disabled="!editingProfile" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 disabled:opacity-60">
            </div>
          </div>

          <button v-if="editingProfile" @click="saveProfile" :disabled="savingProfile" class="w-full mt-4 bg-yellow-400 hover:bg-yellow-500 disabled:opacity-50 text-gray-900 py-3 rounded-2xl font-bold transition-all hover:scale-105 shadow-lg">
            {{ savingProfile ? 'در حال ذخیره...' : 'ذخیره پروفایل' }}
          </button>
        </div>

        <!-- Security Card -->
        <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl border border-white/40">
          <h3 class="text-lg font-bold text-gray-900 mb-6">تنظیمات امنیتی</h3>

          <!-- Change Username -->
          <div class="mb-6 pb-6 border-b border-gray-200">
            <h4 class="text-base font-semibold text-gray-900 mb-4">نام کاربری</h4>
            <div class="bg-white/40 rounded-2xl p-4 mb-4">
              <label class="text-xs text-gray-600 block mb-2">نام کاربری فعلی</label>
              <input v-model="formData.username" type="text" :disabled="!editingUsername" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 disabled:opacity-60">
            </div>
            <button v-if="!editingUsername" @click="editingUsername = true" class="bg-gray-900 hover:bg-gray-800 text-white px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105">
              تغییر نام کاربری
            </button>
            <div v-else class="flex gap-2">
              <button @click="saveUsername" :disabled="savingUsername" class="bg-yellow-400 hover:bg-yellow-500 disabled:opacity-50 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105">
                {{ savingUsername ? 'در حال ذخیره...' : 'ذخیره' }}
              </button>
              <button @click="editingUsername = false" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105">
                انصراف
              </button>
            </div>
          </div>

          <!-- Change Password -->
          <div class="mb-6 pb-6 border-b border-gray-200">
            <h4 class="text-base font-semibold text-gray-900 mb-4">رمز عبور</h4>
            <div class="space-y-4 mb-4" v-if="editingPassword">
              <div class="bg-white/40 rounded-2xl p-4">
                <label class="text-xs text-gray-600 block mb-2">رمز عبور فعلی</label>
                <input v-model="passwordForm.current" type="password" placeholder="••••••••" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 bg-white/80">
              </div>
              <div class="bg-white/40 rounded-2xl p-4">
                <label class="text-xs text-gray-600 block mb-2">رمز عبور جدید</label>
                <input v-model="passwordForm.new" type="password" placeholder="••••••••" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 bg-white/80">
              </div>
              <div class="bg-white/40 rounded-2xl p-4">
                <label class="text-xs text-gray-600 block mb-2">تکرار رمز عبور جدید</label>
                <input v-model="passwordForm.confirm" type="password" placeholder="••••••••" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 bg-white/80">
              </div>
            </div>
            <div v-if="!editingPassword" class="flex gap-2">
              <button @click="editingPassword = true" class="bg-yellow-400 hover:bg-yellow-500 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105 shadow-lg">
                تغییر رمز عبور
              </button>
            </div>
            <div v-else class="flex gap-2">
              <button @click="savePassword" :disabled="savingPassword" class="bg-yellow-400 hover:bg-yellow-500 disabled:opacity-50 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105 shadow-lg">
                {{ savingPassword ? 'در حال به‌روزرسانی...' : 'بروزرسانی رمز عبور' }}
              </button>
              <button @click="cancelPassword" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105">
                انصراف
              </button>
            </div>
          </div>

          <!-- Two-Factor Authentication -->
          <div>
            <div class="flex items-center justify-between mb-4">
              <div>
                <h4 class="text-base font-semibold text-gray-900">احراز هویت دو مرحله‌ای</h4>
                <p class="text-xs text-gray-600 mt-1">یک لایه امنیتی اضافی به حساب خود اضافه کنید</p>
              </div>
              <button class="bg-green-500 hover:bg-green-600 text-white px-5 py-2 rounded-full text-sm font-semibold transition-all hover:scale-105">
                فعال‌سازی
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column - Addresses -->
      <div class="col-span-4 space-y-4">
        <!-- Main Office Address -->
        <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl border border-white/40">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-base font-bold text-gray-900">دفتر مرکزی</h3>
            <button v-if="!editingOffice" @click="editingOffice = true" class="text-sm text-yellow-600 hover:text-yellow-700 font-semibold">ویرایش</button>
            <button v-else @click="cancelEditOffice" class="text-sm text-red-600 hover:text-red-700 font-semibold">انصراف</button>
          </div>

          <div v-if="editingOffice" class="space-y-4 mb-4">
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">آدرس</label>
              <textarea v-model="formData.office_address" rows="2" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 resize-none"></textarea>
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">کد پستی</label>
              <input v-model="formData.office_postal_code" type="text" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80">
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">ایمیل</label>
              <input v-model="formData.office_email" type="email" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80">
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">تلفن</label>
              <input v-model="formData.office_phone" type="tel" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80">
            </div>
            <div class="flex gap-2">
              <button @click="saveOffice" :disabled="savingAddress" class="bg-yellow-400 hover:bg-yellow-500 disabled:opacity-50 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105">
                {{ savingAddress ? 'در حال ذخیره...' : 'ذخیره' }}
              </button>
              <button @click="cancelEditOffice" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105">
                انصراف
              </button>
            </div>
          </div>

          <div v-else class="space-y-3 mb-4">
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              <div>
                <p class="text-xs text-gray-600 mb-1">آدرس</p>
                <p class="text-sm font-semibold text-gray-900">{{ formData.office_address || 'وارد نشده' }}</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <div>
                <p class="text-xs text-gray-600 mb-1">کد پستی</p>
                <p class="text-sm font-semibold text-gray-900">{{ formData.office_postal_code || 'وارد نشده' }}</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <div>
                <p class="text-xs text-gray-600 mb-1">ایمیل</p>
                <p class="text-sm font-semibold text-gray-900">{{ formData.office_email || 'وارد نشده' }}</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              <div>
                <p class="text-xs text-gray-600 mb-1">تلفن</p>
                <p class="text-sm font-semibold text-gray-900">{{ formData.office_phone || 'وارد نشده' }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Factory Address -->
        <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl border border-white/40">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-base font-bold text-gray-900">آدرس کارخانه</h3>
            <button v-if="!editingFactory" @click="editingFactory = true" class="text-sm text-yellow-600 hover:text-yellow-700 font-semibold">ویرایش</button>
            <button v-else @click="cancelEditFactory" class="text-sm text-red-600 hover:text-red-700 font-semibold">انصراف</button>
          </div>

          <div v-if="editingFactory" class="space-y-4 mb-4">
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">آدرس</label>
              <textarea v-model="formData.factory_address" rows="2" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80 resize-none"></textarea>
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">کد پستی</label>
              <input v-model="formData.factory_postal_code" type="text" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80">
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">ایمیل</label>
              <input v-model="formData.factory_email" type="email" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80">
            </div>
            <div class="bg-white/40 rounded-2xl p-4">
              <label class="text-xs text-gray-600 block mb-2">تلفن</label>
              <input v-model="formData.factory_phone" type="tel" class="w-full px-3 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:outline-none text-gray-900 font-semibold bg-white/80">
            </div>
            <div class="flex gap-2">
              <button @click="saveFactory" :disabled="savingFactory" class="bg-yellow-400 hover:bg-yellow-500 disabled:opacity-50 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105">
                {{ savingFactory ? 'در حال ذخیره...' : 'ذخیره' }}
              </button>
              <button @click="cancelEditFactory" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-6 py-2.5 rounded-full font-semibold text-sm transition-all hover:scale-105">
                انصراف
              </button>
            </div>
          </div>

          <div v-else class="space-y-3 mb-4">
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              <div>
                <p class="text-xs text-gray-600 mb-1">آدرس</p>
                <p class="text-sm font-semibold text-gray-900">{{ formData.factory_address || 'وارد نشده' }}</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <div>
                <p class="text-xs text-gray-600 mb-1">کد پستی</p>
                <p class="text-sm font-semibold text-gray-900">{{ formData.factory_postal_code || 'وارد نشده' }}</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <div>
                <p class="text-xs text-gray-600 mb-1">ایمیل</p>
                <p class="text-sm font-semibold text-gray-900">{{ formData.factory_email || 'وارد نشده' }}</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              <div>
                <p class="text-xs text-gray-600 mb-1">تلفن</p>
                <p class="text-sm font-semibold text-gray-900">{{ formData.factory_phone || 'وارد نشده' }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Toast -->
    <transition name="toast">
      <div v-if="toast.show" class="toast" :class="`toast-${toast.type}`">
        {{ toast.message }}
      </div>
    </transition>
  </div>
</template>

<script>
const API_BASE_URL = 'https://polychemmb.com/api'

export default {
  name: 'SettingsPage',
  data() {
    return {
      editingProfile: false,
      editingUsername: false,
      editingPassword: false,
      editingOffice: false,
      editingFactory: false,
      
      savingProfile: false,
      savingPassword: false,
      savingUsername: false,
      savingAddress: false,
      savingFactory: false,
      
      formData: {
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        username: '',
        company_name: '',
        address: '',
        economic_code: '',
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
      formDataBackup: {},
      
      passwordForm: {
        current: '',
        new: '',
        confirm: ''
      },
      
      toast: {
        show: false,
        message: '',
        type: 'success'
      }
    }
  },

  computed: {
    profileImageUrl() {
      if (!this.formData.profile_image) return null
      const img = this.formData.profile_image
      if (img.startsWith('http') || img.startsWith('data:')) return img
      return `${API_BASE_URL}/public/uploads/profiles/${img}`
    }
  },

  mounted() {
    this.loadProfileData()
  },

  methods: {
    getAuthToken() {
      return localStorage.getItem('client_token') || localStorage.getItem('token')
    },

    showToast(message, type = 'success') {
      this.toast = { show: true, message, type }
      setTimeout(() => {
        this.toast.show = false
      }, 3000)
    },

    async apiCall(endpoint, options = {}) {
      const token = this.getAuthToken()
      if (!token) {
        this.$router.push('/client/login')
        return null
      }

      try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
          method: options.method || 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: options.body ? JSON.stringify(options.body) : undefined
        })

        if (response.status === 401) {
          localStorage.clear()
          this.$router.push('/client/login')
          return null
        }

        if (!response.ok) {
          const errorData = await response.json()
          throw new Error(errorData.message || `HTTP ${response.status}`)
        }

        return await response.json()
      } catch (error) {
        console.error('API Error:', error)
        this.showToast(error.message, 'error')
        return null
      }
    },

    async loadProfileData() {
      try {
        const data = await this.apiCall('/client/profile')
        if (data && data.success && data.user) {
          this.formData = {
            first_name: data.user.first_name || '',
            last_name: data.user.last_name || '',
            email: data.user.email || '',
            phone: data.user.phone || '',
            username: data.user.username || '',
            company_name: data.user.company_name || '',
            address: data.user.address || '',
            economic_code: data.user.economic_code || '',
            office_address: data.user.office_address || '',
            office_postal_code: data.user.office_postal_code || '',
            office_phone: data.user.office_phone || '',
            office_email: data.user.office_email || '',
            factory_address: data.user.factory_address || '',
            factory_postal_code: data.user.factory_postal_code || '',
            factory_phone: data.user.factory_phone || '',
            factory_email: data.user.factory_email || '',
            profile_image: data.user.profile_image || null
          }
          this.formDataBackup = JSON.parse(JSON.stringify(this.formData))
        }
      } catch (error) {
        console.error('Error loading profile:', error)
      }
    },

    async saveProfile() {
      this.savingProfile = true
      try {
        const data = await this.apiCall('/client/profile', {
          method: 'PUT',
          body: {
            first_name: this.formData.first_name,
            last_name: this.formData.last_name,
            email: this.formData.email,
            phone: this.formData.phone,
            company_name: this.formData.company_name,
            address: this.formData.address,
            economic_code: this.formData.economic_code
          }
        })

        if (data && data.success) {
          this.showToast('پروفایل با موفقیت ذخیره شد', 'success')
          this.editingProfile = false
          this.formDataBackup = JSON.parse(JSON.stringify(this.formData))
        }
      } finally {
        this.savingProfile = false
      }
    },

    cancelEditProfile() {
      this.formData = JSON.parse(JSON.stringify(this.formDataBackup))
      this.editingProfile = false
    },

    async savePassword() {
      if (this.passwordForm.new !== this.passwordForm.confirm) {
        this.showToast('رمز عبور جدید و تکرار آن برابر نیستند', 'error')
        return
      }

      this.savingPassword = true
      try {
        const data = await this.apiCall('/client/change-password', {
          method: 'POST',
          body: {
            current_password: this.passwordForm.current,
            new_password: this.passwordForm.new
          }
        })

        if (data && data.success) {
          this.showToast('رمز عبور با موفقیت تغییر کرد', 'success')
          this.passwordForm = { current: '', new: '', confirm: '' }
          this.editingPassword = false
        }
      } finally {
        this.savingPassword = false
      }
    },

    cancelPassword() {
      this.passwordForm = { current: '', new: '', confirm: '' }
      this.editingPassword = false
    },

    async saveUsername() {
      this.savingUsername = true
      try {
        const data = await this.apiCall('/client/change-username', {
          method: 'POST',
          body: { new_username: this.formData.username }
        })

        if (data && data.success) {
          this.showToast('نام کاربری با موفقیت تغییر کرد', 'success')
          this.editingUsername = false
          this.formDataBackup.username = this.formData.username
        }
      } finally {
        this.savingUsername = false
      }
    },

    async saveOffice() {
      this.savingAddress = true
      try {
        const data = await this.apiCall('/client/profile', {
          method: 'PUT',
          body: {
            office_address: this.formData.office_address,
            office_postal_code: this.formData.office_postal_code,
            office_phone: this.formData.office_phone,
            office_email: this.formData.office_email
          }
        })

        if (data && data.success) {
          this.showToast('آدرس دفتر مرکزی با موفقیت ذخیره شد', 'success')
          this.editingOffice = false
          this.formDataBackup = JSON.parse(JSON.stringify(this.formData))
        }
      } finally {
        this.savingAddress = false
      }
    },

    cancelEditOffice() {
      this.formData.office_address = this.formDataBackup.office_address
      this.formData.office_postal_code = this.formDataBackup.office_postal_code
      this.formData.office_phone = this.formDataBackup.office_phone
      this.formData.office_email = this.formDataBackup.office_email
      this.editingOffice = false
    },

    async saveFactory() {
      this.savingFactory = true
      try {
        const data = await this.apiCall('/client/profile', {
          method: 'PUT',
          body: {
            factory_address: this.formData.factory_address,
            factory_postal_code: this.formData.factory_postal_code,
            factory_phone: this.formData.factory_phone,
            factory_email: this.formData.factory_email
          }
        })

        if (data && data.success) {
          this.showToast('آدرس کارخانه با موفقیت ذخیره شد', 'success')
          this.editingFactory = false
          this.formDataBackup = JSON.parse(JSON.stringify(this.formData))
        }
      } finally {
        this.savingFactory = false
      }
    },

    cancelEditFactory() {
      this.formData.factory_address = this.formDataBackup.factory_address
      this.formData.factory_postal_code = this.formDataBackup.factory_postal_code
      this.formData.factory_phone = this.formDataBackup.factory_phone
      this.formData.factory_email = this.formDataBackup.factory_email
      this.editingFactory = false
    },

    async handleProfileImageChange(event) {
      const file = event.target.files[0]
      if (!file) return

      const reader = new FileReader()
      reader.onload = (e) => {
        this.formData.profile_image = e.target.result
      }
      reader.readAsDataURL(file)

      await this.uploadProfileImage(file)
    },

    async uploadProfileImage(file) {
      try {
        const token = this.getAuthToken()
        const formData = new FormData()
        formData.append('profile_image', file)

        const response = await fetch(`${API_BASE_URL}/client/upload-profile-image`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`
          },
          body: formData
        })

        if (!response.ok) throw new Error('خطا در آپلود تصویر')

        const data = await response.json()
        if (data.success) {
          this.formData.profile_image = data.profile_image
          this.showToast('تصویر با موفقیت آپلود شد', 'success')
        }
      } catch (error) {
        this.showToast(error.message, 'error')
      }
    }
  }
}
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(243, 244, 246, 0.5);
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #f8cf48 0%, #f8cf48 100%);
  border-radius: 10px;
  transition: background 0.3s ease;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, #f8cf48 0%, #f8cf48 100%);
}

.toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  color: white;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  z-index: 10000;
  animation: slideUp 0.3s ease-out;
}

.toast-success {
  background: #10b981;
}

.toast-error {
  background: #ef4444;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}
</style>