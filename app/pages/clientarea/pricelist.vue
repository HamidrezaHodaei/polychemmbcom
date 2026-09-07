<!-- pages/clientarea/pricelist.vue - FIXED VERSION -->
<template>
  <div class="h-full overflow-hidden font-[IRANYekan]">
    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center h-full">
      <div class="text-center">
        <div class="animate-spin rounded-full h-16 w-16 border-b-2 border-yellow-400 mx-auto mb-4"></div>
        <p class="text-gray-600">در حال بارگذاری اطلاعات قیمت‌گذاری...</p>
      </div>
    </div>

    <div v-else class="grid grid-cols-12 gap-4 h-full overflow-hidden">
      <!-- Left Side - Form -->
      <div class="col-span-8 overflow-y-auto custom-scrollbar pr-2">
        <div class="grid grid-cols-2 gap-4 pb-4">
          <!-- Select Grade -->
          <div class="col-span-2 bg-white/60 backdrop-blur-xl rounded-3xl p-5 shadow-xl border border-white/40 relative z-30">
              <h3 class="text-base font-bold text-gray-900 mb-3">انتخاب گرید</h3>
              <div class="grid grid-cols-3 gap-2 mb-3">
                <button
                  v-for="cat in mainCategories"
                  :key="cat.id"
                  @click="selectCategory(cat)"
                  :class="[
                    'py-2.5 px-3 rounded-xl font-semibold text-sm transition-all border-2',
                    selectedCategoryId === cat.id
                      ? 'bg-yellow-400 text-gray-900 border-yellow-400 shadow-lg'
                      : 'bg-white/60 text-gray-700 border-gray-200 hover:border-yellow-400'
                  ]">
                  {{ cat.name }}
                </button>
              </div>
              <div v-if="subCategories.length > 0" class="grid grid-cols-3 gap-2 mb-3">
                <button
                  v-for="sub in subCategories"
                  :key="sub.id"
                  @click="selectSubCategory(sub)"
                  :class="[
                    'py-2 px-3 rounded-lg font-medium text-xs transition-all border-2',
                    selectedSubCategoryId === sub.id
                      ? 'bg-yellow-400 text-black border-yellow-400 shadow-md'
                      : 'bg-white/60 text-gray-600 border-gray-200 hover:border-yellow-400'
                  ]">
                  {{ sub.name }}
                </button>
              </div>
              <div class="relative" ref="selectRef">
                <div
                  @click="toggleDropdown"
                  class="w-full px-4 py-3 pr-10 rounded-xl border border-white/30 focus:border-white/50 text-base font-medium bg-white/10 backdrop-blur-md text-black hover:bg-white/20 cursor-pointer transition-all shadow-xl"
                  :class="{ 'border-white/50': isOpen, 'text-gray-400': !selectedProduct }">
                  {{ selectedProduct ? selectedProduct.name : 'لطفا انتخاب کنید' }}
                  <svg class="w-5 h-5 absolute left-4 top-1/2 -translate-y-1/2 text-black/70 transition-transform duration-200" :class="{ 'rotate-180': isOpen }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </div>
                <Transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
                  <div v-show="isOpen" class="absolute z-[100] w-full mt-2 bg-gray-700/95 backdrop-blur-md rounded-xl shadow-2xl border border-white/20 overflow-hidden max-h-60 overflow-y-auto">
                    <div v-for="product in filteredProducts" :key="product.id" @click="selectProduct(product)" class="px-4 py-3 text-white cursor-pointer transition-all duration-200 hover:bg-yellow-500 hover:text-black" :class="{ 'bg-yellow-500/20': selectedProduct?.id === product.id }">
                      {{ product.name }}
                    </div>
                    <div v-if="filteredProducts.length === 0" class="px-4 py-3 text-gray-400 text-center">محصولی موجود نیست</div>
                  </div>
                </Transition>
              </div>
            </div>

          <!-- Pick Your Amount -->
          <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-5 shadow-xl border border-white/40 max-h-[220px] relative z-20">
            <h3 class="font-bold text-gray-900 mb-3 text-[20px]">انتخاب مقدار (کیلوگرم)</h3>
            <div class="relative" ref="amountSelectRef">
              <div @click="toggleAmountDropdown" class="w-full px-6 py-3 pr-12 rounded-xl border border-white/30 focus:border-white/50 text-lg font-medium text-center bg-white/10 backdrop-blur-md hover:bg-white/20 cursor-pointer transition-all shadow-xl translate-y-[27px]" :class="{ 'border-white/50': isAmountOpen, 'text-gray-400': !selectedWeight, 'text-black': selectedWeight }">
                {{ selectedWeight ? `${selectedWeight} کیلوگرم` : 'لطفا انتخاب کنید...' }}
                <svg class="w-5 h-5 absolute left-4 top-1/2 -translate-y-1/2 text-black/70 transition-transform duration-200" :class="{ 'rotate-180': isAmountOpen }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </div>
              <Transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
                <div v-show="isAmountOpen" class="absolute z-[200] w-full mt-2 bg-gray-700/95 backdrop-blur-md rounded-xl shadow-2xl border border-white/20 overflow-hidden max-h-60 overflow-y-auto">
                  <div v-for="weight in availableWeights" :key="weight" @click="selectWeight(weight)" class="px-4 py-3 text-white text-center cursor-pointer transition-all duration-200 hover:bg-yellow-500 hover:text-black" :class="{ 'bg-yellow-500/20': selectedWeight === weight }">
                    {{ weight }} کیلوگرم
                  </div>
                  <div v-if="availableWeights.length === 0" class="px-4 py-3 text-gray-400 text-center">ابتدا یک محصول انتخاب کنید</div>
                </div>
              </Transition>
            </div>
          </div>

          <!-- Pick Your Package -->
          <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-5 md:p-6 shadow-xl border border-white/40" :class="{ 'ring-2 ring-red-500': showValidationError && !selectedPackageId }">
            <h3 class="text-base md:text-lg font-bold text-gray-900 mb-3">
              انتخاب بسته‌بندی
              <span v-if="showValidationError && !selectedPackageId" class="text-red-500 text-sm mr-2">*</span>
            </h3>
            <div v-if="packagingOptions.length === 0" class="text-center py-4 text-gray-500">هیچ بسته‌بندی برای این محصول تعریف نشده است</div>
            <div v-else class="grid grid-cols-2 gap-3">
              <button v-for="pkg in packagingOptions" :key="pkg.id" @click="selectedPackageId = pkg.id" :class="['py-4 px-4 rounded-xl font-bold text-sm transition-all border-2', selectedPackageId === pkg.id ? 'bg-yellow-400 text-gray-900 border-yellow-400 shadow-lg' : 'bg-white/60 text-gray-700 border-gray-200 hover:border-yellow-400']">
                <div class="flex flex-col items-center gap-1.5">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" /></svg>
                  <span class="text-center">{{ pkg.name }}</span>
                  <span class="text-xs text-gray-600">{{ pkg.cost_type === 'percent' ? `+${pkg.extra_cost}%` : `+${formatRial(pkg.extra_cost)}` }}</span>
                </div>
              </button>
            </div>
          </div>

          <!-- Payment Method -->
          <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-5 shadow-xl border border-white/40 col-span-2" :class="{ 'ring-2 ring-red-500': showValidationError && !selectedPaymentId }">
            <h3 class="text-base font-bold text-gray-900 mb-3">
              روش پرداخت
              <span v-if="showValidationError && !selectedPaymentId" class="text-red-500 text-sm mr-2">*</span>
            </h3>
            <div v-if="paymentOptions.length === 0" class="text-center py-4 text-gray-500">هیچ روش پرداختی برای این محصول تعریف نشده است</div>
            <div v-else class="grid grid-cols-5 gap-2">
              <button v-for="method in paymentOptions" :key="method.id" @click="selectedPaymentId = method.id" :class="['py-3.5 px-4 rounded-xl font-semibold text-sm transition-all border-2 relative', selectedPaymentId === method.id ? 'bg-yellow-400 text-gray-900 border-yellow-400 shadow-lg' : 'bg-white/60 text-gray-700 border-gray-200 hover:border-yellow-400']">
                <div class="flex flex-col items-center gap-1">
                  <span class="text-center leading-tight">{{ method.name }}</span>
                  <span v-if="method.adjustment !== 0" class="text-[10px] px-1.5 py-0.5 rounded" :class="method.adjustment < 0 ? 'bg-green-500 text-white' : 'bg-orange-500 text-white'">
                    {{ method.adjustment_type === 'percent' ? (method.adjustment > 0 ? '+' : '') + method.adjustment + '%' : (method.adjustment > 0 ? '+' : '') + formatRial(method.adjustment) }}
                  </span>
                </div>
              </button>
            </div>
          </div>

          <!-- Transit Way -->
<div class="bg-white/60 backdrop-blur-xl rounded-3xl p-3 shadow-xl border border-white/40 col-span-2" :class="{ 'ring-2 ring-red-500': showValidationError && !selectedDeliveryMethod }">
  <h3 class="text-base font-bold text-gray-900 mb-3">
    روش حمل و نقل
    <span v-if="showValidationError && !selectedDeliveryMethod" class="text-red-500 text-sm mr-2">*</span>
  </h3>
  <div class="grid grid-cols-2 gap-3">
    <button v-for="transit in deliveryOptions" :key="transit.id" @click="selectedDeliveryMethod = transit.id" :class="['py-2 px-4 rounded-xl font-bold text-base transition-all border-2 flex flex-col items-center gap-2 w-full', selectedDeliveryMethod === transit.id ? 'bg-yellow-400 text-gray-900 border-yellow-400 shadow-lg' : 'bg-white/60 text-gray-700 border-gray-200 hover:border-yellow-400']">
      <svg class="w-8 h-8 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 013.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" /></svg>
      <span class="text-center">{{ translateDeliveryMethod(transit.name) }}</span>
      <span v-if="transit.id === 'customer' && selectedWeight && selectedWeight >= freeShippingThreshold" class="text-xs text-green-600 font-semibold">ارسال رایگان</span>
      <span v-else-if="transit.cost > 0" class="text-xs text-gray-600">{{ formatRial(transit.cost) }}</span>
    </button>
  </div>
  <div v-if="selectedWeight && selectedWeight >= freeShippingThreshold" class="flex items-center justify-center gap-2 px-3 py-2 mt-3 bg-green-500/20 rounded-lg border border-green-500/30">
    <svg class="w-4 h-4 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
    <span class="text-xs font-semibold text-green-400">ارسال رایگان به دلیل سفارش {{ selectedWeight }} کیلوگرم</span>
  </div>
</div>
        </div>
      </div>

      <!-- Right Side - Price Summary -->
      <div class="col-span-4 h-full overflow-hidden">
        <div class="bg-gray-900/70 backdrop-blur-xl rounded-3xl p-6 shadow-2xl border border-gray-700/50 h-full flex flex-col">
          
          <!-- Header - fixed -->
          <div class="flex items-center gap-2 mb-4 flex-shrink-0">
            <svg class="w-5 h-5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
            </svg>
            <h3 class="text-lg font-bold text-white">پیش‌فاکتور شما</h3>
          </div>

          <!-- ✅ SCROLLABLE section: info cards + breakdown -->
          <div class="flex-1 min-h-0 overflow-y-auto custom-scrollbar mb-3">
            <div class="space-y-2 mb-3">

              <!-- Grade & weight card -->
              <div class="bg-gray-800/50 backdrop-blur-sm rounded-xl p-3 flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <div class="w-8 h-8 bg-yellow-400 rounded-lg flex items-center justify-center flex-shrink-0">
                    <svg class="w-4 h-4 text-gray-900" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" /></svg>
                  </div>
                  <div class="min-w-0">
                    <p class="text-[10px] text-gray-400">گرید</p>
                    <p class="text-sm font-bold text-white truncate">{{ selectedProduct?.name || 'انتخاب نشده' }}</p>
                  </div>
                </div>
                <div class="text-right flex-shrink-0">
                  <p class="text-[10px] text-gray-400">مقدار</p>
                  <p class="text-sm font-bold text-white">{{ selectedWeight || 0 }} کیلوگرم</p>
                </div>
              </div>

              <!-- Packaging card -->
              <div class="bg-gray-800/50 backdrop-blur-sm rounded-xl p-3">
                <div class="flex items-center gap-2 mb-1">
                  <svg class="w-3.5 h-3.5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" /></svg>
                  <p class="text-[10px] text-gray-400">بسته‌بندی</p>
                </div>
                <p class="text-sm font-bold text-white">{{ getPackageName() }}</p>
              </div>

              <!-- Payment card -->
              <div class="bg-gray-800/50 backdrop-blur-sm rounded-xl p-3">
                <div class="flex items-center gap-2 mb-1">
                  <svg class="w-3.5 h-3.5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" /></svg>
                  <p class="text-[10px] text-gray-400">پرداخت</p>
                </div>
                <p class="text-sm font-bold text-white">{{ getPaymentName() }}</p>
              </div>

              <!-- Price per kg card -->
              <div v-if="localPrice" class="bg-gray-800/50 backdrop-blur-sm rounded-xl p-3">
                <div class="flex items-center gap-2 mb-2">
                  <svg class="w-3.5 h-3.5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                  <p class="text-[10px] text-gray-400">قیمت هر کیلوگرم</p>
                </div>
                <div class="grid grid-cols-2 gap-2">
                  <div class="text-center bg-gray-700/40 rounded-lg py-2 px-2">
                    <p class="text-[9px] text-gray-400 mb-1">قیمت فروش پایه</p>
                    <p class="text-xs font-bold text-blue-300">{{ formatRial(localPrice.breakdown.base_price_per_kg) }}</p>
                  </div>
                  <div class="text-center bg-gray-700/40 rounded-lg py-2 px-2">
                    <p class="text-[9px] text-gray-400 mb-1">قیمت اختصاصی</p>
                    <p class="text-xs font-bold text-green-300">{{ formatRial(localPrice.breakdown.effective_price_per_kg) }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Breakdown detail rows -->
            <div v-if="localPrice" class="bg-gray-800/50 backdrop-blur-sm rounded-2xl p-4">
              <div class="space-y-2">
                <div v-if="selectedWeight && localPrice.base_price" class="flex justify-between items-center px-3 py-2 bg-gray-700/40 rounded-lg">
                  <span class="text-xs text-gray-400">قیمت هر کیلوگرم</span>
                  <div class="flex items-center gap-2">
                    <span v-if="localPrice.breakdown.has_special_price && localPrice.breakdown.base_price_per_kg !== localPrice.breakdown.effective_price_per_kg" class="text-xs font-medium text-gray-500 line-through">{{ formatRial(localPrice.breakdown.base_price_per_kg) }}</span>
<span class="text-sm font-semibold text-yellow-400 transition-all duration-300">
{{ formatRial(localPrice.total_price / selectedWeight) }}
</span>                  </div>
                </div>

                <div class="flex justify-between items-center">
                  <div>
                    <span class="text-xs text-gray-400 block">قیمت محصول</span>
                    <span v-if="selectedWeight" class="text-[10px] text-gray-500">برای {{ selectedWeight }} کیلو</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <span v-if="localPrice.breakdown.has_special_price && localPrice.breakdown.base_price_per_kg !== localPrice.breakdown.effective_price_per_kg" class="text-sm font-semibold text-gray-500 line-through">{{ formatRial(localPrice.breakdown.base_price_per_kg * selectedWeight) }}</span>
                    <span class="text-sm font-semibold" :class="localPrice.breakdown.has_special_price && localPrice.breakdown.base_price_per_kg !== localPrice.breakdown.effective_price_per_kg ? 'text-green-400' : 'text-white'">{{ formatRial(localPrice.base_price) }}</span>
                  </div>
                </div>
<div v-if="localPrice.breakdown.has_special_price && localPrice.breakdown.base_price_per_kg !== localPrice.breakdown.effective_price_per_kg" class="flex items-center justify-center gap-2 px-3 py-2 bg-green-500/20 rounded-lg border border-green-500/30">
  <svg class="w-4 h-4 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
  <span class="text-sm font-semibold text-green-400">قیمت ویژه شما!</span>
  <span class="text-xs text-green-300">
    {{
      (localPrice.breakdown.base_price_per_kg * selectedWeight - localPrice.total_price) > 0
        ? formatRial(localPrice.breakdown.base_price_per_kg * selectedWeight - localPrice.total_price)
        : formatRial(localPrice.breakdown.base_price_per_kg * selectedWeight - localPrice.base_price)
    }} تخفیف
  </span>
</div>
                <div class="flex justify-between items-center">
                  <span class="text-xs text-gray-400">بسته‌بندی</span>
                  <span class="text-sm font-semibold text-white">{{ formatRial(localPrice.packaging_cost) }}</span>
                </div>

                <div class="flex justify-between items-center">
                  <span class="text-xs text-gray-400">حمل و نقل</span>
                  <span class="text-sm font-semibold" :class="localPrice.breakdown.free_shipping ? 'text-green-400' : 'text-white'">
                    <span v-if="localPrice.breakdown.free_shipping">رایگان</span>
                    <span v-else>{{ formatRial(localPrice.delivery_cost) }}</span>
                  </span>
                </div>

                <div v-if="localPrice.breakdown.free_shipping" class="flex items-center justify-center gap-2 px-3 py-2 bg-green-500/20 rounded-lg border border-green-500/30">
                  <svg class="w-4 h-4 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                  <span class="text-xs font-semibold text-green-400">ارسال رایگان به دلیل سفارش {{ selectedWeight }} کیلوگرم</span>
                </div>

                <div v-if="localPrice.payment_adjustment !== 0" class="flex justify-between items-center" :class="localPrice.payment_adjustment < 0 ? 'text-green-400' : 'text-orange-400'">
                  <span class="text-xs">{{ localPrice.payment_adjustment < 0 ? 'تخفیف پرداخت نقدی' : 'تسهیلات فروش بلندمدت' }}</span>
                  <span class="text-sm font-semibold">{{ localPrice.payment_adjustment > 0 ? '+' : '' }}{{ formatRial(localPrice.payment_adjustment) }}</span>
                </div>
              </div>
            </div>
          </div>
          <!-- END scrollable section -->

          <!-- ✅ FIXED BOTTOM: total price + button — never scrolls away -->
          <div class="flex-shrink-0">
            <div v-if="localPrice" class="bg-gray-800/50 backdrop-blur-sm rounded-2xl p-4 mb-3 border border-yellow-400/20">
              <div class="text-center">
                <p class="text-sm text-gray-400 mb-1">قیمت کل</p>
                <p class="text-3xl font-bold text-yellow-400 transition-all duration-300">
                  {{ formatRial(localPrice.total_price) }}
                </p>
              </div>
            </div>

            <button
              @click="startOrder"
              class="w-full py-3.5 rounded-2xl font-bold text-base transition-all shadow-lg flex items-center justify-center gap-2"
              :class="canStartOrder
                ? 'bg-yellow-400 hover:bg-yellow-500 text-gray-900 hover:scale-105 cursor-pointer'
                : 'bg-gray-600 text-gray-400 cursor-not-allowed'">
              <span>درخواست پیش فاکتور</span>
              <svg class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </button>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import axios from 'axios'

const API_BASE = 'https://polychemmb.com/api/client/pricing'
const token = ref(localStorage.getItem('client_token') || '')

const deliveryMethodNames = {
  'factory': 'تحویل درب کارخانه',
  'customer': 'تحویل به مشتری',
  'Ex-Factory Delivery': 'تحویل درب کارخانه',
  'Delivery to Customer': 'تحویل به مشتری'
}

const translateDeliveryMethod = (name) => deliveryMethodNames[name] || name

const loading = ref(true)
const categoriesTree = ref([])
const packagingOptions = ref([])
const paymentOptions = ref([])
const deliveryOptions = ref([])

const selectedCategoryId = ref(null)
const selectedSubCategoryId = ref(null)
const selectedProduct = ref(null)
const selectedWeight = ref(null)
const selectedPackageId = ref(null)
const selectedPaymentId = ref(null)
const selectedDeliveryMethod = ref(null)

const isOpen = ref(false)
const selectRef = ref(null)
const isAmountOpen = ref(false)
const amountSelectRef = ref(null)

const showValidationError = ref(false)
const availableWeights = ref([])
const clientBrackets = ref([])
const freeShippingThreshold = ref(30000)

const formatRial = (amount) => {
  return new Intl.NumberFormat('fa-IR', { style: 'decimal', minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(amount) + ' ریال'
}

const mainCategories = computed(() => categoriesTree.value.filter(cat => !cat.parent_id))

const subCategories = computed(() => {
  if (!selectedCategoryId.value) return []
  const selectedCat = categoriesTree.value.find(cat => cat.id === selectedCategoryId.value)
  return selectedCat?.subcategories || []
})

const filteredProducts = computed(() => {
  if (!selectedCategoryId.value) return []
  const category = categoriesTree.value.find(cat => cat.id === selectedCategoryId.value)
  if (!category) return []
  if (selectedSubCategoryId.value && subCategories.value.length > 0) {
    const subcategory = subCategories.value.find(sub => sub.id === selectedSubCategoryId.value)
    return subcategory?.products || []
  }
  return category.products || []
})

const localPrice = computed(() => {
  if (!selectedWeight.value || !clientBrackets.value.length) return null
  const sortedBrackets = [...clientBrackets.value].sort((a, b) => b.min_weight - a.min_weight)
  const bracket = sortedBrackets.find(b => selectedWeight.value >= b.min_weight) || clientBrackets.value.reduce((min, b) => b.min_weight < min.min_weight ? b : min)
  const basePricePerKg = parseFloat(bracket.base_price_per_kg || 0)
  const clientPricePerKg = bracket.client_price_per_kg !== null && bracket.client_price_per_kg !== undefined ? parseFloat(bracket.client_price_per_kg) : null
  const effectivePricePerKg = clientPricePerKg !== null ? clientPricePerKg : basePricePerKg
  const basePrice = effectivePricePerKg * selectedWeight.value
  const pkg = packagingOptions.value.find(p => p.id === selectedPackageId.value)
  let packagingCost = 0
  if (pkg) packagingCost = pkg.cost_type === 'percent' ? basePrice * (parseFloat(pkg.extra_cost) / 100) : parseFloat(pkg.extra_cost)
  const isFreeShipping = selectedDeliveryMethod.value === 'customer' && selectedWeight.value >= freeShippingThreshold.value
  let deliveryCost = 0
  if (selectedDeliveryMethod.value === 'customer' && !isFreeShipping) {
    const deliveryOption = deliveryOptions.value.find(d => d.id === 'customer')
    deliveryCost = deliveryOption ? parseFloat(deliveryOption.cost) : 150
  }
  const payment = paymentOptions.value.find(p => p.id === selectedPaymentId.value)
  let paymentAdjustment = 0
  if (payment && payment.adjustment !== 0) {
    const subtotal = basePrice + packagingCost + deliveryCost
    paymentAdjustment = payment.adjustment_type === 'percent' ? subtotal * (parseFloat(payment.adjustment) / 100) : parseFloat(payment.adjustment)
  }
  const totalPrice = basePrice + packagingCost + deliveryCost + paymentAdjustment
  return {
    base_price: Math.round(basePrice),
    packaging_cost: Math.round(packagingCost),
    delivery_cost: Math.round(deliveryCost),
    payment_adjustment: Math.round(paymentAdjustment),
    total_price: Math.round(totalPrice),
    breakdown: { base_price_per_kg: basePricePerKg, client_price_per_kg: clientPricePerKg, effective_price_per_kg: effectivePricePerKg, has_special_price: clientPricePerKg !== null, free_shipping: isFreeShipping }
  }
})

const canStartOrder = computed(() => {
  return selectedProduct.value && selectedWeight.value && selectedPackageId.value && selectedPaymentId.value && selectedDeliveryMethod.value && localPrice.value !== null
})

const loadData = async () => {
  loading.value = true
  try {
    const headers = { Authorization: `Bearer ${token.value}` }
    const categoriesRes = await axios.get(`${API_BASE}/categories-tree`, { headers })
    categoriesTree.value = categoriesRes.data.categories
    const deliveryRes = await axios.get(`${API_BASE}/delivery-options`, { headers })
    deliveryOptions.value = deliveryRes.data.options.methods
    if (deliveryOptions.value.length > 0) selectedDeliveryMethod.value = deliveryOptions.value[0].id
    if (mainCategories.value.length > 0) selectCategory(mainCategories.value[0])
  } catch (error) {
    console.error('Error loading pricing data:', error)
    alert('بارگذاری اطلاعات قیمت‌گذاری با خطا مواجه شد. لطفا صفحه را رفرش کنید.')
  } finally {
    loading.value = false
  }
}

const selectCategory = (cat) => {
  selectedCategoryId.value = cat.id
  selectedSubCategoryId.value = null
  selectedProduct.value = null
  selectedWeight.value = null
  availableWeights.value = []
  clientBrackets.value = []
  packagingOptions.value = []
  paymentOptions.value = []
  selectedPackageId.value = null
  selectedPaymentId.value = null
  if (subCategories.value.length > 0) selectSubCategory(subCategories.value[0])
  else if (filteredProducts.value.length > 0) selectProduct(filteredProducts.value[0])
}

const selectSubCategory = (sub) => {
  selectedSubCategoryId.value = sub.id
  selectedProduct.value = null
  selectedWeight.value = null
  availableWeights.value = []
  clientBrackets.value = []
  packagingOptions.value = []
  paymentOptions.value = []
  selectedPackageId.value = null
  selectedPaymentId.value = null
  if (filteredProducts.value.length > 0) selectProduct(filteredProducts.value[0])
}

const toggleDropdown = () => { isOpen.value = !isOpen.value }

const selectProduct = async (product) => {
  selectedProduct.value = product
  isOpen.value = false
  selectedWeight.value = null
  clientBrackets.value = []
  try {
    const headers = { Authorization: `Bearer ${token.value}` }
    const weightResponse = await axios.get(`${API_BASE}/products/${product.id}/weight-options`, { headers })
    availableWeights.value = weightResponse.data.weight_options
    clientBrackets.value = weightResponse.data.brackets || []
    freeShippingThreshold.value = weightResponse.data.free_shipping_threshold ?? 30000
    const paymentResponse = await axios.get(`${API_BASE}/payment-options`, { headers, params: { product_id: product.id } })
    paymentOptions.value = paymentResponse.data.payment_terms
    const packagingResponse = await axios.get(`${API_BASE}/packaging-options`, { headers, params: { product_id: product.id } })
    packagingOptions.value = packagingResponse.data.packaging
    selectedPackageId.value = packagingOptions.value.length > 0 ? packagingOptions.value[0].id : null
    selectedPaymentId.value = paymentOptions.value.length > 0 ? paymentOptions.value[0].id : null
    if (availableWeights.value.length > 0) selectWeight(availableWeights.value[0])
  } catch (error) {
    console.error('Error loading product data:', error)
    alert('خطا در بارگذاری اطلاعات محصول')
  }
}

const toggleAmountDropdown = () => { if (availableWeights.value.length > 0) isAmountOpen.value = !isAmountOpen.value }
const selectWeight = (weight) => { selectedWeight.value = weight; isAmountOpen.value = false }
const getPackageName = () => { const pkg = packagingOptions.value.find(p => p.id === selectedPackageId.value); return pkg ? pkg.name : 'انتخاب نشده' }
const getPaymentName = () => { const payment = paymentOptions.value.find(p => p.id === selectedPaymentId.value); return payment ? payment.name : 'انتخاب نشده' }

const startOrder = async () => {
  if (!selectedPackageId.value || !selectedPaymentId.value || !selectedDeliveryMethod.value) {
    showValidationError.value = true
    let missingItems = []
    if (!selectedPackageId.value) missingItems.push('بسته‌بندی')
    if (!selectedPaymentId.value) missingItems.push('روش پرداخت')
    if (!selectedDeliveryMethod.value) missingItems.push('روش حمل و نقل')
    alert(`لطفا موارد زیر را انتخاب کنید:\n- ${missingItems.join('\n- ')}`)
    return
  }
  if (!canStartOrder.value) return
  showValidationError.value = false
  try {
    const headers = { Authorization: `Bearer ${token.value}` }
    const price = localPrice.value
    const orderResponse = await axios.post('https://polychemmb.com/api/client/orders/create', {
      product_id: selectedProduct.value.id, product_name: selectedProduct.value.name,
      weight_kg: selectedWeight.value, packaging_id: selectedPackageId.value,
      packaging_name: getPackageName(), payment_term_id: selectedPaymentId.value,
      payment_term_name: getPaymentName(), delivery_method: selectedDeliveryMethod.value,
      base_price: price.base_price, packaging_cost: price.packaging_cost,
      delivery_cost: price.delivery_cost, payment_adjustment: price.payment_adjustment,
      total_price: price.total_price
    }, { headers })
    if (orderResponse.data.success) {
      alert(`سفارش با موفقیت ثبت شد! شماره سفارش: ${orderResponse.data.data.order_number}`)
      selectedProduct.value = null; selectedWeight.value = null; selectedPackageId.value = null
      selectedPaymentId.value = null; selectedDeliveryMethod.value = null
      availableWeights.value = []; clientBrackets.value = []; packagingOptions.value = []; paymentOptions.value = []
      showValidationError.value = false
      console.log('Order created:', orderResponse.data.data)
    }
  } catch (error) {
    console.error('Error creating order:', error)
    alert('ثبت سفارش با خطا مواجه شد. لطفا دوباره تلاش کنید.')
  }
}

const handleClickOutside = (event) => {
  if (selectRef.value && !selectRef.value.contains(event.target)) isOpen.value = false
  if (amountSelectRef.value && !amountSelectRef.value.contains(event.target)) isAmountOpen.value = false
}

onMounted(() => { loadData(); document.addEventListener('click', handleClickOutside) })
onUnmounted(() => { document.removeEventListener('click', handleClickOutside) })
</script>

<style scoped>
.overflow-y-auto::-webkit-scrollbar { width: 6px; }
.overflow-y-auto::-webkit-scrollbar-track { background: rgba(255,255,255,0.1); border-radius: 10px; }
.overflow-y-auto::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.3); border-radius: 10px; }
.overflow-y-auto::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.5); }
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(250,204,21,0.4); border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(250,204,21,0.6); }
* { direction: rtl; }
</style>