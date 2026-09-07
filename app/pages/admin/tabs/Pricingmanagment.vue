<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-4 md:p-8 persian-font" dir="rtl">
    <!-- Loading Overlay -->
    <div v-if="loading" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50">
      <div class="bg-white rounded-2xl p-8 shadow-2xl">
        <div class="animate-spin rounded-full h-16 w-16 border-b-2 border-gray-900 mx-auto mb-4"></div>
        <p class="text-gray-700 font-semibold">در حال بارگذاری تنظیمات...</p>
      </div>
    </div>

    <!-- Success/Error Messages -->
    <div v-if="message.text" 
         :class="[
           'fixed top-4 left-4 z-50 px-6 py-4 rounded-xl shadow-lg animate-slide-in',
           message.type === 'error' ? 'bg-red-500 text-white' : 'bg-green-500 text-white'
         ]">
      <div class="flex items-center gap-3">
        <svg v-if="message.type === 'success'" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
        </svg>
        <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
        <span class="font-semibold">{{ message.text }}</span>
      </div>
    </div>

    <!-- Customer & Product Selection -->
    <div class="max-w-6xl mx-auto mb-8 fade-in-up-0">
      <div class="bg-white/70 backdrop-blur-sm rounded-2xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-all">
        <div class="bg-gradient-to-r from-indigo-600 to-indigo-700 px-6 py-5">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 bg-white/10 rounded-xl flex items-center justify-center backdrop-blur-sm">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
            </div>
            <div>
              <h2 class="text-2xl font-bold text-white">انتخاب مشتری و محصول</h2>
              <p class="text-indigo-100 text-sm mt-0.5">مشتری و محصول مورد نظر را انتخاب کنید</p>
            </div>
          </div>
        </div>
        
        <div class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Customer Selection -->
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">مشتری (اختیاری - برای قیمت اختصاصی)</label>
              <select 
                v-model="selectedCustomerId"
                @change="onCustomerChange"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all bg-white font-medium hover:border-gray-400"
              >
                <option :value="null">قیمت‌های پایه (بدون مشتری)</option>
                <option v-for="customer in customers" :key="customer.id" :value="customer.id">
                  {{ customer.name }}
                </option>
              </select>
            </div>

            <!-- Product Selection -->
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">محصول انتخاب شده</label>
              
              <!-- Selected Product Display -->
              <div v-if="currentProduct" class="mb-3 px-4 py-3 bg-gradient-to-r from-indigo-50 to-blue-50 border-2 border-indigo-200 rounded-xl">
                <div class="flex items-center justify-between">
                  <div>
                    <div class="font-bold text-gray-900">{{ currentProduct.name }}</div>
                    <div class="text-sm text-gray-600 mt-1">
                      <span v-if="currentProduct.product_code" class="inline-flex items-center px-2 py-0.5 rounded bg-indigo-100 text-indigo-700 font-semibold text-xs">
                        کد: {{ currentProduct.product_code }}
                      </span>
                      <span v-if="currentProduct.category_name" class="mr-2 text-gray-500">
                        {{ currentProduct.category_name }}
                        <span v-if="currentProduct.subcategory_name" class="text-indigo-600"> / {{ currentProduct.subcategory_name }}</span>
                      </span>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs text-green-600 font-semibold bg-green-100 px-2 py-1 rounded-lg">✓ فعال</span>
                  </div>
                </div>
              </div>
              
              <!-- No Product Selected -->
              <div v-else class="mb-3 px-4 py-3 bg-gray-50 border-2 border-dashed border-gray-300 rounded-xl text-center">
                <p class="text-sm text-gray-500">هیچ محصولی انتخاب نشده است</p>
              </div>
              
              <!-- Action Button -->
              <button 
                @click="showProductSelectionModal = true"
                class="flex items-center gap-2 px-5 py-2.5 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-all hover:shadow-md"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                </svg>
                {{ currentProduct ? 'تغییر محصول' : 'انتخاب محصول' }}
              </button>
            </div>
          </div>

          <!-- Add New Product Button -->
          <div class="mt-4 flex gap-3">
            <button 
              @click="showAddProductModal = true"
              class="flex items-center gap-2 px-5 py-2.5 bg-gray-900 text-white rounded-xl font-semibold hover:bg-gray-800 transition-all hover:shadow-md"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
              </svg>
              افزودن محصول جدید
            </button>

            <button 
              v-if="selectedProductId"
              @click="deleteCurrentProduct"
              class="flex items-center gap-2 px-5 py-2.5 bg-white border border-gray-300 text-red-600 rounded-xl font-semibold hover:bg-red-50 hover:border-red-300 transition-all"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
              </svg>
              حذف این محصول
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Product Configuration (Only shown when product is selected) -->
    <div v-if="selectedProductId && currentProduct" class="max-w-6xl mx-auto space-y-6 fade-in-up-1">
      
      <!-- Basic Product Info -->
      <div class="bg-white/70 backdrop-blur-sm rounded-2xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-all">
        <div class="bg-gradient-to-r from-gray-900 to-gray-800 px-6 py-5">
          <h2 class="text-2xl font-bold text-white">اطلاعات پایه محصول</h2>
        </div>
        
        <div class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <!-- Product Name -->
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">نام محصول</label>
              <input 
                type="text" 
                v-model="currentProduct.name"
                @blur="saveCurrentProduct"
                class="w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-all bg-white font-medium hover:border-gray-400"
              />
            </div>

            <!-- Product Code -->
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">کد محصول</label>
              <input 
                type="text" 
                v-model="currentProduct.product_code"
                @blur="saveCurrentProduct"
                class="w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-all bg-white font-medium hover:border-gray-400"
              />
            </div>

            <!-- Free Shipping Threshold -->
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">ارسال رایگان ≥ (کیلوگرم)</label>
              <input 
                type="number" 
                v-model.number="currentProduct.free_shipping_threshold"
                @blur="saveCurrentProduct"
                class="w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-all bg-white hover:border-gray-400"
                placeholder="30000"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- Weight Brackets -->
      <div class="bg-white/70 backdrop-blur-sm rounded-2xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-all">
        <div class="bg-gradient-to-r from-blue-600 to-blue-700 px-6 py-5">
          <h2 class="text-2xl font-bold text-white">بازه‌های قیمتی</h2>
        </div>
        
        <div class="p-6 space-y-6">
          <!-- Base Price Brackets -->
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-3">قیمت‌های پایه (برای همه مشتریان)</label>
            
            <!-- Table Header -->
            <div class="bg-white/70 rounded-xl overflow-hidden border border-gray-200">
              <table class="w-full">
                <thead>
                  <tr class="border-b border-gray-200 bg-gray-50/50">
                    <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">حداقل وزن (کیلوگرم)</th>
                    <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">قیمت پایه (ریال/کیلوگرم)</th>
                    <th class="px-6 py-4 text-center text-sm font-semibold text-gray-700">عملیات</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(bracket, i) in currentProduct.weight_brackets" :key="i" class="border-b border-gray-200 hover:bg-blue-50/30 transition-colors">
                    <td class="px-6 py-4">
                      <input 
                        type="number" 
                        v-model.number="bracket.min_weight"
                        @blur="saveCurrentProduct"
                        placeholder="وزن"
                        class="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white hover:border-gray-400 transition-all"
                      />
                    </td>
                    <td class="px-6 py-4">
                      <input 
                        type="number" 
                        v-model.number="bracket.base_price_per_kg"
                        @blur="saveCurrentProduct"
                        placeholder="قیمت"
                        class="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white hover:border-gray-400 transition-all"
                      />
                    </td>
                    <td class="px-6 py-4 text-center">
                      <button 
                        @click="removeWeightBracket(i)"
                        class="p-2 text-red-500 hover:bg-red-50 rounded-lg transition-all"
                        :disabled="currentProduct.weight_brackets.length <= 1"
                      >
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                        </svg>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            
            <button 
              @click="addWeightBracket"
              class="mt-3 text-sm text-blue-700 hover:text-blue-900 font-semibold flex items-center gap-2 hover:gap-3 transition-all"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
              </svg>
              افزودن بازه جدید
            </button>
          </div>

          <!-- Client-Specific Price Brackets -->
          <div v-if="selectedCustomerId">
            <label class="block text-sm font-semibold text-gray-700 mb-3">
              قیمت‌های اختصاصی برای مشتری انتخاب شده
            </label>
            
            <!-- Table -->
            <div class="bg-white/70 rounded-xl overflow-hidden border border-gray-200">
              <table class="w-full">
                <thead>
                  <tr class="border-b border-gray-200 bg-indigo-50/50">
                    <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">حداقل وزن (کیلوگرم)</th>
                    <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">قیمت اختصاصی (ریال/کیلوگرم)</th>
                    <th class="px-6 py-4 text-center text-sm font-semibold text-gray-700">عملیات</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(bracket, i) in currentProduct.customer_weight_brackets" :key="i" class="border-b border-gray-200 hover:bg-indigo-50/30 transition-colors">
                    <td class="px-6 py-4">
                      <input 
                        type="number" 
                        v-model.number="bracket.min_weight"
                        @blur="saveCurrentProduct"
                        placeholder="وزن"
                        class="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white hover:border-gray-400 transition-all"
                      />
                    </td>
                    <td class="px-6 py-4">
                      <input 
                        type="number" 
                        v-model.number="bracket.client_price_per_kg"
                        @blur="saveCurrentProduct"
                        placeholder="قیمت"
                        class="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white hover:border-gray-400 transition-all"
                      />
                    </td>
                    <td class="px-6 py-4 text-center">
                      <button 
                        @click="removeCustomerWeightBracket(i)"
                        class="p-2 text-red-500 hover:bg-red-50 rounded-lg transition-all"
                        :disabled="currentProduct.customer_weight_brackets.length <= 1"
                      >
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                        </svg>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            
            <button 
              @click="addCustomerWeightBracket"
              class="mt-3 text-sm text-indigo-700 hover:text-indigo-900 font-semibold flex items-center gap-2 hover:gap-3 transition-all"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
              </svg>
              افزودن بازه جدید
            </button>
          </div>
        </div>
      </div>

      <!-- Payment Terms (Product-Specific) -->
      <div class="bg-white/70 backdrop-blur-sm rounded-2xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-all">
        <div class="bg-gradient-to-r from-yellow-500 to-yellow-600 px-6 py-5">
          <h2 class="text-2xl font-bold text-white">شرایط پرداخت این محصول</h2>
          <p class="text-yellow-100 text-sm mt-0.5">انتخاب شرایط پرداخت مجاز برای این محصول</p>
        </div>
        
        <div class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div v-for="term in allPaymentTerms" :key="term.id" 
                 @click="togglePaymentTerm(term.id)"
                 class="p-4 border-2 rounded-xl cursor-pointer transition-all"
                 :class="isPaymentTermSelected(term.id) 
                   ? 'border-yellow-500 bg-yellow-50 shadow-sm' 
                   : 'border-gray-200 hover:border-yellow-300 hover:bg-gray-50'">
              <div class="flex items-center justify-between">
                <div>
                  <div class="font-semibold text-gray-900">{{ term.name }}</div>
                  <div class="text-sm text-gray-600 mt-0.5">
                    {{ term.adjustment_type === 'percent' 
                      ? (term.adjustment > 0 ? '+' : '') + term.adjustment + '%' 
                      : (term.adjustment > 0 ? '+' : '') + term.adjustment + ' ریال' }}
                  </div>
                </div>
                <div v-if="isPaymentTermSelected(term.id)" 
                     class="w-6 h-6 bg-yellow-500 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>
          
          <button 
            @click="saveCurrentProduct"
            class="mt-4 px-6 py-3 bg-yellow-500 text-white rounded-xl font-semibold hover:bg-yellow-600 transition-all hover:shadow-md"
          >
            ذخیره شرایط پرداخت
          </button>
        </div>
      </div>

      <!-- Packaging Types (Product-Specific) -->
      <div class="bg-white/70 backdrop-blur-sm rounded-2xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-all">
        <div class="bg-gradient-to-r from-green-600 to-green-700 px-6 py-5">
          <h2 class="text-2xl font-bold text-white">انواع بسته‌بندی این محصول</h2>
          <p class="text-green-100 text-sm mt-0.5">انتخاب بسته‌بندی‌های مجاز برای این محصول</p>
        </div>
        
        <div class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div v-for="pkg in allPackaging" :key="pkg.id" 
                 @click="togglePackaging(pkg.id)"
                 class="p-4 border-2 rounded-xl cursor-pointer transition-all"
                 :class="isPackagingSelected(pkg.id) 
                   ? 'border-green-500 bg-green-50 shadow-sm' 
                   : 'border-gray-200 hover:border-green-300 hover:bg-gray-50'">
              <div class="flex items-center justify-between">
                <div>
                  <div class="font-semibold text-gray-900">{{ pkg.name }}</div>
                  <div class="text-sm text-gray-600 mt-0.5">
                    {{ pkg.cost_type === 'percent' 
                      ? pkg.extra_cost + '%' 
                      : pkg.extra_cost + ' ریال' }}
                  </div>
                </div>
                <div v-if="isPackagingSelected(pkg.id)" 
                     class="w-6 h-6 bg-green-500 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>
          
          <button 
            @click="saveCurrentProduct"
            class="mt-4 px-6 py-3 bg-green-600 text-white rounded-xl font-semibold hover:bg-green-700 transition-all hover:shadow-md"
          >
            ذخیره انواع بسته‌بندی
          </button>
        </div>
      </div>

    </div>

    <!-- Global Settings (Always visible) -->
    <div class="max-w-6xl mx-auto mt-8 space-y-6 fade-in-up-2">
      
      <!-- Manage Global Payment Terms -->
      <div class="bg-white/70 backdrop-blur-sm rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
        <div class="bg-gradient-to-r from-purple-600 to-purple-700 px-6 py-5 flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold text-white">مدیریت شرایط پرداخت کلی</h2>
            <p class="text-purple-100 text-sm mt-0.5">ایجاد و ویرایش شرایط پرداخت برای استفاده در محصولات</p>
          </div>
          <button 
            @click="addGlobalPayment"
            class="px-5 py-2.5 bg-white text-purple-600 rounded-xl font-semibold hover:bg-purple-50 transition-all hover:shadow-md"
          >
            + افزودن شرط جدید
          </button>
        </div>
        
        <div class="p-6">
          <!-- Table View -->
          <div class="bg-white/70 rounded-xl overflow-hidden border border-gray-200">
            <table class="w-full">
              <thead>
                <tr class="border-b border-gray-200 bg-purple-50/50">
                  <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">نام شرط پرداخت</th>
                  <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">مقدار تعدیل</th>
                  <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">نوع</th>
                  <th class="px-6 py-4 text-center text-sm font-semibold text-gray-700">عملیات</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(payment, i) in globalPaymentTerms" :key="payment.id" class="border-b border-gray-200 hover:bg-purple-50/30 transition-colors group">
                  <td class="px-6 py-4">
                    <input 
                      type="text" 
                      v-model="payment.name" 
                      @blur="savePaymentTerm(payment)"
                      placeholder="شرط پرداخت"
                      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all bg-white text-gray-800 font-medium hover:border-gray-400"
                    />
                  </td>
                  <td class="px-6 py-4">
                    <input 
                      type="number" 
                      v-model.number="payment.adjustment" 
                      @blur="savePaymentTerm(payment)"
                      placeholder="0"
                      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all bg-white hover:border-gray-400"
                    />
                  </td>
                  <td class="px-6 py-4">
                    <select 
                      v-model="payment.adjustment_type"
                      @change="savePaymentTerm(payment)"
                      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all bg-white hover:border-gray-400"
                    >
                      <option value="fixed">ریال</option>
                      <option value="percent">درصد</option>
                    </select>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <button 
                      @click="removeGlobalPayment(i)"
                      class="p-2 text-red-500 hover:bg-red-50 rounded-lg transition-all opacity-0 group-hover:opacity-100"
                      v-if="globalPaymentTerms.length > 1"
                    >
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                      </svg>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Manage Global Packaging -->
      <div class="bg-white/70 backdrop-blur-sm rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
        <div class="bg-gradient-to-r from-teal-600 to-teal-700 px-6 py-5 flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold text-white">مدیریت انواع بسته‌بندی کلی</h2>
            <p class="text-teal-100 text-sm mt-0.5">ایجاد و ویرایش انواع بسته‌بندی برای استفاده در محصولات</p>
          </div>
          <button 
            @click="addGlobalPackaging"
            class="px-5 py-2.5 bg-white text-teal-600 rounded-xl font-semibold hover:bg-teal-50 transition-all hover:shadow-md"
          >
            + افزودن نوع جدید
          </button>
        </div>
        
        <div class="p-6">
          <!-- Table View -->
          <div class="bg-white/70 rounded-xl overflow-hidden border border-gray-200">
            <table class="w-full">
              <thead>
                <tr class="border-b border-gray-200 bg-teal-50/50">
                  <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">نام بسته‌بندی</th>
                  <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">هزینه اضافی</th>
                  <th class="px-6 py-4 text-right text-sm font-semibold text-gray-700">نوع</th>
                  <th class="px-6 py-4 text-center text-sm font-semibold text-gray-700">عملیات</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(pkg, i) in globalPackaging" :key="pkg.id" class="border-b border-gray-200 hover:bg-teal-50/30 transition-colors group">
                  <td class="px-6 py-4">
                    <input 
                      type="text" 
                      v-model="pkg.name" 
                      @blur="savePackaging(pkg)"
                      placeholder="نام بسته‌بندی"
                      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-white text-gray-800 font-medium hover:border-gray-400"
                    />
                  </td>
                  <td class="px-6 py-4">
                    <input 
                      type="number" 
                      v-model.number="pkg.extra_cost" 
                      @blur="savePackaging(pkg)"
                      placeholder="0"
                      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-white hover:border-gray-400"
                    />
                  </td>
                  <td class="px-6 py-4">
                    <select 
                      v-model="pkg.cost_type"
                      @change="savePackaging(pkg)"
                      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-white hover:border-gray-400"
                    >
                      <option value="fixed">ریال</option>
                      <option value="percent">درصد</option>
                    </select>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <button 
                      @click="removeGlobalPackaging(i)"
                      class="p-2 text-red-500 hover:bg-red-50 rounded-lg transition-all opacity-0 group-hover:opacity-100"
                      v-if="globalPackaging.length > 1"
                    >
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                      </svg>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Delivery Settings -->
      <div class="bg-white/70 backdrop-blur-sm rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
        <div class="bg-gradient-to-r from-orange-600 to-orange-700 px-6 py-5">
          <h2 class="text-2xl font-bold text-white">تنظیمات تحویل</h2>
        </div>
        
        <div class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Factory Pickup -->
            <div class="p-6 bg-white rounded-xl border-2 border-gray-200 hover:border-orange-500 transition-all cursor-pointer"
                 :class="deliveryMethod === 'factory' ? 'ring-2 ring-orange-500 border-orange-500 bg-orange-50/50' : ''"
                 @click="deliveryMethod = 'factory'; saveDeliverySettings()">
              <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-orange-600 rounded-xl flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                  </svg>
                </div>
                <div class="flex-1">
                  <h3 class="text-lg font-bold text-gray-900 mb-1">تحویل در کارخانه</h3>
                  <p class="text-sm text-gray-600 mb-3">مشتری از کارخانه ما تحویل می‌گیرد</p>
                  <div class="flex items-center gap-2">
                    <span class="px-3 py-1.5 bg-white rounded-lg text-sm font-semibold text-orange-600 border border-orange-200">
                      بدون هزینه ارسال
                    </span>
                  </div>
                </div>
                <div v-if="deliveryMethod === 'factory'" class="w-6 h-6 bg-orange-600 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/>
                  </svg>
                </div>
              </div>
            </div>

            <!-- Customer Delivery -->
            <div class="p-6 bg-white rounded-xl border-2 border-gray-200 hover:border-purple-500 transition-all cursor-pointer"
                 :class="deliveryMethod === 'customer' ? 'ring-2 ring-purple-500 border-purple-500 bg-purple-50/50' : ''"
                 @click="deliveryMethod = 'customer'; saveDeliverySettings()">
              <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-purple-600 rounded-xl flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                  </svg>
                </div>
                <div class="flex-1">
                  <h3 class="text-lg font-bold text-gray-900 mb-1">تحویل به مشتری</h3>
                  <p class="text-sm text-gray-600 mb-3">ما به محل مشتری تحویل می‌دهیم</p>
                  <div class="flex items-center gap-2">
                    <input 
                      type="number" 
                      v-model.number="deliveryCost" 
                      @blur="saveDeliverySettings"
                      placeholder="هزینه"
                      class="w-32 px-3 py-1.5 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600 bg-white hover:border-gray-400 transition-all"
                    />
                    <span class="text-sm font-medium text-gray-600">ریال هزینه ارسال</span>
                  </div>
                </div>
                <div v-if="deliveryMethod === 'customer'" class="w-6 h-6 bg-purple-600 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- Product Selection Modal -->
    <div v-if="showProductSelectionModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4 animate-fade-in">
      <div class="bg-white rounded-2xl max-w-3xl w-full max-h-[85vh] overflow-hidden shadow-2xl animate-scale-in">
        <!-- Header -->
        <div class="bg-gradient-to-r from-indigo-600 to-indigo-700 px-6 py-5">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center backdrop-blur-sm">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                </svg>
              </div>
              <div>
                <h3 class="text-2xl font-bold text-white">جستجو و انتخاب محصول</h3>
                <p class="text-indigo-100 text-sm mt-0.5">ابتدا دسته‌بندی را انتخاب کنید</p>
              </div>
            </div>
            <button 
              @click="closeProductSelectionModal"
              class="w-9 h-9 bg-white/10 hover:bg-white/20 rounded-lg transition-all flex items-center justify-center"
            >
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>
        </div>
        
        <div class="p-6 overflow-y-auto max-h-[calc(85vh-88px)]">
          <!-- Step 1: Category Selection -->
          <div class="mb-5">
            <label class="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
              <span class="flex items-center justify-center w-6 h-6 bg-indigo-600 text-white rounded-full text-xs font-bold">1</span>
              دسته‌بندی اصلی
            </label>
            <select 
              v-model="productSelectionFilter.categoryId"
              @change="onProductFilterCategoryChange"
              class="w-full px-4 py-3.5 border-2 border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 hover:border-gray-400 transition-all bg-white font-medium text-gray-700"
            >
              <option :value="null">یک دسته‌بندی انتخاب کنید...</option>
              <option v-for="cat in mainCategories" :key="cat.id" :value="cat.id">
                {{ cat.name }}
              </option>
            </select>
          </div>

          <!-- Step 2: Subcategory Selection (if applicable) -->
          <div v-if="productFilterSubcategories.length > 0" class="mb-5">
            <label class="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
              <span class="flex items-center justify-center w-6 h-6 bg-indigo-600 text-white rounded-full text-xs font-bold">2</span>
              زیر دسته‌بندی (اختیاری)
            </label>
            <select 
              v-model="productSelectionFilter.subcategoryId"
              class="w-full px-4 py-3.5 border-2 border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 hover:border-gray-400 transition-all bg-white font-medium text-gray-700"
            >
              <option :value="null">همه زیر دسته‌ها</option>
              <option v-for="sub in productFilterSubcategories" :key="sub.id" :value="sub.id">
                {{ sub.name }}
              </option>
            </select>
          </div>

          <div class="h-px bg-gradient-to-r from-transparent via-gray-300 to-transparent my-6"></div>

          <!-- Step 3: Product List -->
          <div v-if="productSelectionFilter.categoryId">
            <label class="block text-sm font-bold text-gray-700 mb-3 flex items-center justify-between">
              <span class="flex items-center gap-2">
                <span class="flex items-center justify-center w-6 h-6 bg-indigo-600 text-white rounded-full text-xs font-bold">
                  {{ productFilterSubcategories.length > 0 ? '3' : '2' }}
                </span>
                انتخاب محصول
              </span>
              <span v-if="filteredProducts.length > 0" class="text-indigo-600 text-sm font-semibold bg-indigo-50 px-3 py-1 rounded-lg">
                {{ filteredProducts.length }} محصول یافت شد
              </span>
            </label>
            
            <!-- No products Found -->
            <div v-if="filteredProducts.length === 0" class="text-center py-16 bg-gradient-to-br from-gray-50 to-gray-100 rounded-2xl border-2 border-dashed border-gray-300">
              <svg class="w-20 h-20 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"/>
              </svg>
              <p class="font-bold text-gray-800 text-lg mb-1">محصولی در این دسته‌بندی یافت نشد</p>
              <p class="text-sm text-gray-600">لطفاً دسته‌بندی دیگری انتخاب کنید یا محصول جدیدی ایجاد کنید</p>
            </div>

            <!-- products Grid -->
            <div v-else class="grid grid-cols-1 gap-3 max-h-[400px] overflow-y-auto pr-2 custom-scrollbar">
              <div 
                v-for="product in filteredProducts" 
                :key="product.id"
                @click="selectProductFromModal(product.id)"
                class="p-4 bg-white border-2 border-gray-200 rounded-xl hover:border-indigo-500 hover:shadow-lg cursor-pointer transition-all group relative overflow-hidden"
              >
                <div class="absolute inset-0 bg-gradient-to-r from-indigo-500/0 to-indigo-500/0 group-hover:from-indigo-500/5 group-hover:to-blue-500/5 transition-all"></div>
                <div class="relative flex items-center justify-between">
                  <div class="flex-1">
                    <div class="font-bold text-gray-900 group-hover:text-indigo-900 text-lg mb-1">
                      {{ product.name }}
                    </div>
                    <div class="flex items-center gap-2 flex-wrap">
                      <span v-if="product.product_code" class="inline-flex items-center px-2.5 py-1 rounded-lg bg-indigo-100 text-indigo-700 font-semibold text-xs">
                        کد: {{ product.product_code }}
                      </span>
                      <span v-if="product.category_name" class="inline-flex items-center px-2.5 py-1 rounded-lg bg-gray-100 text-gray-700 text-xs">
                        {{ product.category_name }}
                      </span>
                      <span v-if="product.subcategory_name" class="inline-flex items-center px-2.5 py-1 rounded-lg bg-blue-100 text-blue-700 text-xs">
                        {{ product.subcategory_name }}
                      </span>
                    </div>
                  </div>
                  <div class="flex-shrink-0 mr-4 w-10 h-10 bg-gray-100 group-hover:bg-indigo-100 rounded-full flex items-center justify-center transition-all">
                    <svg class="w-5 h-5 text-gray-400 group-hover:text-indigo-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Message before category selection -->
          <div v-else class="text-center py-16 bg-gradient-to-br from-indigo-50 to-blue-50 rounded-2xl border-2 border-dashed border-indigo-300">
            <div class="w-20 h-20 mx-auto mb-4 bg-indigo-100 rounded-full flex items-center justify-center">
              <svg class="w-10 h-10 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"/>
              </svg>
            </div>
            <p class="font-bold text-gray-800 text-lg mb-1">ابتدا دسته‌بندی را انتخاب کنید</p>
            <p class="text-sm text-gray-600">برای مشاهده و انتخاب محصولات، لطفاً یک دسته‌بندی انتخاب کنید</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Add Product Modal -->
    <div v-if="showAddProductModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl">
        <h3 class="text-2xl font-bold text-gray-900 mb-4">افزودن محصول جدید</h3>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">نام محصول</label>
            <input 
              type="text" 
              v-model="newProduct.name"
              class="w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-600 hover:border-gray-400 transition-all"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">کد محصول (اختیاری)</label>
            <input 
              type="text" 
              v-model="newProduct.product_code"
              class="w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-600 hover:border-gray-400 transition-all"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">دسته‌بندی اصلی</label>
            <select 
              v-model="newProduct.category_id"
              @change="onNewProductCategoryChange"
              class="w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-600 hover:border-gray-400 transition-all"
            >
              <option :value="null">انتخاب دسته‌بندی</option>
              <option v-for="cat in mainCategories" :key="cat.id" :value="cat.id">
                {{ cat.name }}
              </option>
            </select>
          </div>

          <div v-if="selectedCategorySubcategories.length > 0">
            <label class="block text-sm font-semibold text-gray-700 mb-2">زیر دسته‌بندی (اختیاری)</label>
            <select 
              v-model="newProduct.subcategory_id"
              class="w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-600 hover:border-gray-400 transition-all"
            >
              <option :value="null">بدون زیر دسته</option>
              <option v-for="sub in selectedCategorySubcategories" :key="sub.id" :value="sub.id">
                {{ sub.name }}
              </option>
            </select>
          </div>
        </div>

        <div class="flex gap-3 mt-6">
          <button 
            @click="createNewProduct"
            class="flex-1 px-6 py-3 bg-gray-900 text-white rounded-xl font-semibold hover:bg-gray-800 transition-all hover:shadow-md"
          >
            ایجاد محصول
          </button>
          <button 
            @click="showAddProductModal = false"
            class="px-6 py-3 bg-gray-200 text-gray-700 rounded-xl font-semibold hover:bg-gray-300 transition-all"
          >
            انصراف
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { reactive, ref, onMounted, computed } from 'vue'

const { $axios } = useNuxtApp()

const API_BASE = 'https://polychemmb.com/api/admin/pricing-management'

// State
const loading = ref(false)
const message = ref({ text: '', type: 'success' })

const customers = ref([])
const selectedCustomerId = ref(null)

const productsList = ref([])
const selectedProductId = ref(null)
const currentProduct = ref(null)

const categoriesTree = ref([])
const globalPackaging = reactive([])
const globalPaymentTerms = reactive([])
const deliveryMethod = ref('factory')
const deliveryCost = ref(150)

const allPaymentTerms = ref([])
const allPackaging = ref([])

const showAddProductModal = ref(false)
const showProductSelectionModal = ref(false)

const newProduct = ref({
  name: '',
  product_code: '',
  category_id: null,
  subcategory_id: null
})

const productSelectionFilter = ref({
  categoryId: null,
  subcategoryId: null
})

// Computed
const mainCategories = computed(() => {
  return categoriesTree.value.filter(cat => !cat.parent_id)
})

const selectedCategorySubcategories = computed(() => {
  if (!newProduct.value.category_id) return []
  const category = categoriesTree.value.find(cat => cat.id === newProduct.value.category_id)
  return category?.subcategories || []
})

const productFilterSubcategories = computed(() => {
  if (!productSelectionFilter.value.categoryId) return []
  const category = categoriesTree.value.find(cat => cat.id === productSelectionFilter.value.categoryId)
  return category?.subcategories || []
})

const filteredProducts = computed(() => {
  // اگر هیچ دسته‌بندی انتخاب نشده، لیست خالی برگردان
  if (!productSelectionFilter.value.categoryId) {
    return []
  }

  let filtered = productsList.value

  // Filter by category
  const selectedCategory = categoriesTree.value.find(cat => cat.id === productSelectionFilter.value.categoryId)
  if (selectedCategory) {
    filtered = filtered.filter(p => p.category_name === selectedCategory.name)
  }

  // Filter by subcategory (if selected)
  if (productSelectionFilter.value.subcategoryId) {
    const selectedSubcategory = productFilterSubcategories.value.find(sub => sub.id === productSelectionFilter.value.subcategoryId)
    if (selectedSubcategory) {
      filtered = filtered.filter(p => p.subcategory_name === selectedSubcategory.name)
    }
  }

  return filtered
})

// Helper Functions
const showMessage = (text, type = 'success') => {
  message.value = { text, type }
  setTimeout(() => {
    message.value = { text: '', type: 'success' }
  }, 3000)
}

const onNewProductCategoryChange = () => {
  newProduct.value.subcategory_id = null
}

const onProductFilterCategoryChange = () => {
  productSelectionFilter.value.subcategoryId = null
}

const closeProductSelectionModal = () => {
  showProductSelectionModal.value = false
  productSelectionFilter.value = {
    categoryId: null,
    subcategoryId: null
  }
}

const selectProductFromModal = async (productId) => {
  selectedProductId.value = productId
  await loadProductDetail(productId)
  closeProductSelectionModal()
}

// Load Data
const loadData = async () => {
  loading.value = true
  
  try {
    // Load categories
    const categoriesRes = await $axios.get(`${API_BASE}/categories`)
    categoriesTree.value = categoriesRes.data.categories
    
    // Load customers
    const customersRes = await $axios.get(`${API_BASE}/clients`)
    customers.value = customersRes.data.clients || []
    
    // Load products list
    const productsRes = await $axios.get(`${API_BASE}/products-list`)
    productsList.value = productsRes.data.products || []
    
    // Load global packaging
    const packagingRes = await $axios.get(`${API_BASE}/packaging`)
    globalPackaging.splice(0, globalPackaging.length, ...packagingRes.data.packaging)
    allPackaging.value = packagingRes.data.packaging
    
    // Load global payment terms
    const paymentRes = await $axios.get(`${API_BASE}/payment-terms`)
    globalPaymentTerms.splice(0, globalPaymentTerms.length, ...paymentRes.data.payment_terms)
    allPaymentTerms.value = paymentRes.data.payment_terms
    
    // Load delivery settings
    const deliveryRes = await $axios.get(`${API_BASE}/delivery-settings`)
    const settings = deliveryRes.data.settings
    deliveryMethod.value = settings.delivery_method || 'factory'
    deliveryCost.value = parseFloat(settings.delivery_cost_customer || 150)
    
  } catch (error) {
    console.error('Error loading data:', error)
    showMessage('خطا در بارگذاری اطلاعات', 'error')
  } finally {
    loading.value = false
  }
}

// Customer Change
const onCustomerChange = async () => {
  if (selectedProductId.value) {
    await loadProductDetail(selectedProductId.value)
  }
}

// Load Product Detail
const loadProductDetail = async (productId) => {
  loading.value = true
  try {
    let url = `${API_BASE}/products/${productId}`
    if (selectedCustomerId.value) {
      url += `?client_id=${selectedCustomerId.value}`
    }
    
    const res = await $axios.get(url)
    currentProduct.value = res.data.product
    
    // Initialize selected payment terms and packaging
    if (!currentProduct.value.payment_term_ids) {
      currentProduct.value.payment_term_ids = currentProduct.value.payment_terms?.map(t => t.id) || []
    }
    if (!currentProduct.value.packaging_ids) {
      currentProduct.value.packaging_ids = currentProduct.value.packaging_types?.map(p => p.id) || []
    }
    
  } catch (error) {
    console.error('Error loading product:', error)
    showMessage('خطا در بارگذاری محصول', 'error')
  } finally {
    loading.value = false
  }
}

// Save Current Product
const saveCurrentProduct = async () => {
  if (!currentProduct.value) return
  
  try {
    const productData = {
      ...currentProduct.value,
      selected_client_id: selectedCustomerId.value
    }
    
    await $axios.put(`${API_BASE}/products/${currentProduct.value.id}`, productData)
    showMessage('محصول با موفقیت ذخیره شد', 'success')
  } catch (error) {
    console.error('Error saving product:', error)
    showMessage('خطا در ذخیره محصول', 'error')
  }
}

// Weight Brackets
const addWeightBracket = () => {
  if (!currentProduct.value.weight_brackets) {
    currentProduct.value.weight_brackets = []
  }
  currentProduct.value.weight_brackets.push({ min_weight: 0, base_price_per_kg: 0 })
}

const removeWeightBracket = (index) => {
  if (currentProduct.value.weight_brackets.length > 1) {
    currentProduct.value.weight_brackets.splice(index, 1)
  }
}

const addCustomerWeightBracket = () => {
  if (!currentProduct.value.customer_weight_brackets) {
    currentProduct.value.customer_weight_brackets = []
  }
  currentProduct.value.customer_weight_brackets.push({ min_weight: 0, client_price_per_kg: 0 })
}

const removeCustomerWeightBracket = (index) => {
  if (currentProduct.value.customer_weight_brackets.length > 1) {
    currentProduct.value.customer_weight_brackets.splice(index, 1)
  }
}

// Payment Terms Selection
const isPaymentTermSelected = (termId) => {
  return currentProduct.value?.payment_term_ids?.includes(termId) || false
}

const togglePaymentTerm = (termId) => {
  if (!currentProduct.value.payment_term_ids) {
    currentProduct.value.payment_term_ids = []
  }
  
  const index = currentProduct.value.payment_term_ids.indexOf(termId)
  if (index > -1) {
    currentProduct.value.payment_term_ids.splice(index, 1)
  } else {
    currentProduct.value.payment_term_ids.push(termId)
  }
}

// Packaging Selection
const isPackagingSelected = (pkgId) => {
  return currentProduct.value?.packaging_ids?.includes(pkgId) || false
}

const togglePackaging = (pkgId) => {
  if (!currentProduct.value.packaging_ids) {
    currentProduct.value.packaging_ids = []
  }
  
  const index = currentProduct.value.packaging_ids.indexOf(pkgId)
  if (index > -1) {
    currentProduct.value.packaging_ids.splice(index, 1)
  } else {
    currentProduct.value.packaging_ids.push(pkgId)
  }
}

// Create New Product
const createNewProduct = async () => {
  if (!newProduct.value.name || !newProduct.value.category_id) {
    showMessage('نام محصول و دسته‌بندی الزامی است', 'error')
    return
  }
  
  try {
    const res = await $axios.post(`${API_BASE}/products`, {
      name: newProduct.value.name,
      product_code: newProduct.value.product_code,
      category_id: newProduct.value.category_id,
      subcategory_id: newProduct.value.subcategory_id,
      weight_brackets: [{ min_weight: 100, base_price_per_kg: 0 }]
    })
    
    showMessage('محصول با موفقیت ایجاد شد', 'success')
    showAddProductModal.value = false
    
    // Reload products list
    const productsRes = await $axios.get(`${API_BASE}/products-list`)
    productsList.value = productsRes.data.products || []
    
    // Select the new product
    selectedProductId.value = res.data.product_id
    await loadProductDetail(res.data.product_id)
    
    // Reset form
    newProduct.value = { name: '', product_code: '', category_id: null, subcategory_id: null }
    
  } catch (error) {
    console.error('Error creating product:', error)
    showMessage('خطا در ایجاد محصول', 'error')
  }
}

// Delete Current Product
const deleteCurrentProduct = async () => {
  if (!currentProduct.value) return
  
  if (!confirm(`آیا از حذف محصول "${currentProduct.value.name}" اطمینان دارید؟`)) return
  
  try {
    await $axios.delete(`${API_BASE}/products/${currentProduct.value.id}`)
    showMessage('محصول با موفقیت حذف شد', 'success')
    
    // Reload products list
    const productsRes = await $axios.get(`${API_BASE}/products-list`)
    productsList.value = productsRes.data.products || []
    
    // Clear selection
    selectedProductId.value = null
    currentProduct.value = null
    
  } catch (error) {
    console.error('Error deleting product:', error)
    showMessage('خطا در حذف محصول', 'error')
  }
}

// Global Payment Terms
const addGlobalPayment = async () => {
  try {
    await $axios.post(`${API_BASE}/payment-terms`, {
      name: 'شرط پرداخت جدید',
      adjustment: 0,
      adjustment_type: 'percent'
    })
    await loadData()
    showMessage('شرط پرداخت با موفقیت ایجاد شد', 'success')
  } catch (error) {
    showMessage('خطا در ایجاد شرط پرداخت', 'error')
  }
}

const removeGlobalPayment = async (index) => {
  const term = globalPaymentTerms[index]
  if (!confirm(`آیا از حذف شرط پرداخت "${term.name}" اطمینان دارید؟`)) return
  
  try {
    await $axios.delete(`${API_BASE}/payment-terms/${term.id}`)
    globalPaymentTerms.splice(index, 1)
    allPaymentTerms.value = allPaymentTerms.value.filter(t => t.id !== term.id)
    showMessage('شرط پرداخت با موفقیت حذف شد', 'success')
  } catch (error) {
    showMessage('خطا در حذف شرط پرداخت', 'error')
  }
}

const savePaymentTerm = async (term) => {
  try {
    await $axios.put(`${API_BASE}/payment-terms/${term.id}`, term)
    showMessage('شرط پرداخت با موفقیت ذخیره شد', 'success')
  } catch (error) {
    showMessage('خطا در ذخیره شرط پرداخت', 'error')
  }
}

// Global Packaging
const addGlobalPackaging = async () => {
  try {
    await $axios.post(`${API_BASE}/packaging`, {
      name: 'بسته‌بندی جدید',
      extra_cost: 0,
      cost_type: 'fixed'
    })
    await loadData()
    showMessage('بسته‌بندی با موفقیت ایجاد شد', 'success')
  } catch (error) {
    showMessage('خطا در ایجاد بسته‌بندی', 'error')
  }
}

const removeGlobalPackaging = async (index) => {
  const pkg = globalPackaging[index]
  if (!confirm(`آیا از حذف بسته‌بندی "${pkg.name}" اطمینان دارید؟`)) return
  
  try {
    await $axios.delete(`${API_BASE}/packaging/${pkg.id}`)
    globalPackaging.splice(index, 1)
    allPackaging.value = allPackaging.value.filter(p => p.id !== pkg.id)
    showMessage('بسته‌بندی با موفقیت حذف شد', 'success')
  } catch (error) {
    showMessage('خطا در حذف بسته‌بندی', 'error')
  }
}

const savePackaging = async (pkg) => {
  try {
    await $axios.put(`${API_BASE}/packaging/${pkg.id}`, pkg)
    showMessage('بسته‌بندی با موفقیت ذخیره شد', 'success')
  } catch (error) {
    showMessage('خطا در ذخیره بسته‌بندی', 'error')
  }
}

// Delivery Settings
const saveDeliverySettings = async () => {
  try {
    await $axios.post(`${API_BASE}/delivery-settings`, {
      delivery_method: deliveryMethod.value,
      delivery_cost_customer: deliveryCost.value.toString()
    })
    showMessage('تنظیمات تحویل با موفقیت ذخیره شد', 'success')
  } catch (error) {
    showMessage('خطا در ذخیره تنظیمات تحویل', 'error')
  }
}

// Lifecycle
onMounted(() => {
  loadData()
})
</script>

<style>
@import url('https://cdn.jsdelivr.net/gh/rastikerdar/iranyekan-font@v4.0.0/WebFonts/css/iranyekan.css');

.persian-font,
.persian-font * {
  font-family: IRANYekan, sans-serif !important;
}

@keyframes slide-in {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.animate-slide-in {
  animation: slide-in 0.3s ease-out;
}

.fade-in-up-0 {
  animation: fadeInUp 0.6s ease-out 0s forwards;
  opacity: 0;
}

.fade-in-up-1 {
  animation: fadeInUp 0.6s ease-out 0.1s forwards;
  opacity: 0;
}

.fade-in-up-2 {
  animation: fadeInUp 0.6s ease-out 0.2s forwards;
  opacity: 0;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-fade-in {
  animation: fadeIn 0.2s ease-out;
}

.animate-scale-in {
  animation: scaleIn 0.3s ease-out;
}

button:not(:disabled):hover {
  transform: translateY(-1px);
}

table {
  border-collapse: separate;
  border-spacing: 0;
}

input:hover,
select:hover {
  border-color: #9ca3af;
}

.group:hover .group-hover\:opacity-100 {
  opacity: 1;
}

/* Custom Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
</style>