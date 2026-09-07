<!-- admin/tabs/orders.vue - نسخه کامل با preview فایل + قفل اسکرول -->
<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-4 md:p-8 space-y-6 font-[IRANYekan]" dir="rtl">
    <!-- Header -->
    <div class="flex items-center justify-between slide-in">
      <div>
        <h1 class="text-2xl font-bold text-gray-900">مدیریت سفارشات</h1>
        <p class="text-sm text-gray-600 mt-1">مشاهده و مدیریت تمام سفارشات</p>
      </div>
    </div>

    <!-- Status Tabs -->
    <div class="bg-white/70 rounded-2xl border border-gray-200 overflow-hidden fade-in-up-1">
      <div class="flex items-center justify-between px-6 py-4 border-b border-gray-200">
        <div class="flex items-center gap-2 overflow-x-auto">
          <button 
            v-for="tab in statusTabs"
            :key="tab.value"
            @click="selectedStatus = tab.value"
            :class="[
              'px-4 py-2 whitespace-nowrap rounded-lg transition-colors font-medium text-sm',
              selectedStatus === tab.value
                ? 'bg-gray-900 text-white'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            ]"
          >
            {{ tab.label }}
          </button>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900"></div>
    </div>

    <!-- Orders Table -->
    <div v-else class="bg-white rounded-lg border border-gray-200 overflow-hidden fade-in-up-2">
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-100">
            <tr>
              <th class="text-right py-3 px-6 text-xs font-bold uppercase">شماره</th>
              <th class="text-right py-3 px-6 text-xs font-bold uppercase">مشتری</th>
              <th class="text-right py-3 px-6 text-xs font-bold uppercase">محصول</th>
              <th class="text-right py-3 px-6 text-xs font-bold uppercase">قیمت</th>
              <th class="text-right py-3 px-6 text-xs font-bold uppercase">وضعیت</th>
              <th class="text-right py-3 px-6 text-xs font-bold uppercase">تاریخ</th>
              <th class="text-center py-3 px-6 text-xs font-bold uppercase">عملیات</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="order in filteredOrders" :key="order.id" class="hover:bg-gray-50">
              <td class="py-4 px-6 text-sm font-medium">{{ order.order_number }}</td>
              <td class="py-4 px-6 text-sm">
                <div>
                  <p class="font-medium">{{ order.company_name || `${order.first_name} ${order.last_name}` }}</p>
                  <p class="text-xs text-gray-500">{{ order.email }}</p>
                </div>
              </td>
              <td class="py-4 px-6 text-sm">
                <div>
                  <p class="font-medium">{{ order.product_name }}</p>
                  <p class="text-xs text-gray-500">{{ order.weight_kg }} کیلو</p>
                </div>
              </td>
              <td class="py-4 px-6 text-sm font-medium">{{ formatPrice(order.total_price) }}</td>
              <td class="py-4 px-6">
                <span :class="getStatusColor(order.status)" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium">
                  {{ getStatusLabel(order.status) }}
                </span>
              </td>
              <td class="py-4 px-6 text-sm">{{ formatDate(order.created_at) }}</td>
              <td class="py-4 px-6 text-center">
                <button @click="viewOrder(order)" class="text-gray-900 hover:text-gray-700 font-medium text-sm">
                  مشاهده
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Empty State -->
      <div v-if="filteredOrders.length === 0" class="text-center py-12">
        <svg class="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
        </svg>
        <h3 class="text-lg font-bold text-gray-900 mb-2">سفارشی یافت نشد</h3>
      </div>
    </div>

    <!-- ==================== FILE PREVIEW MODAL ==================== -->
    <div v-if="showPreviewModal" class="fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center z-[60] p-4" @click.self="closePreview">
      <div class="bg-white rounded-2xl w-full max-w-4xl max-h-[92vh] flex flex-col shadow-2xl">
        <!-- Preview Header -->
        <div class="flex items-center justify-between px-6 py-4 border-b bg-gray-50 rounded-t-2xl">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-indigo-600" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
              </svg>
            </div>
            <div>
              <p class="font-bold text-gray-900 text-sm">{{ previewFile?.name || previewFile?.original_filename }}</p>
              <p class="text-xs text-gray-500">{{ previewFile?.size ? formatFileSize(previewFile.size) : formatFileSize(previewFile?.file_size) }}</p>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <!-- Download button for existing files -->
            <button v-if="previewFile?.id && !previewFile?.isLocal" @click="downloadAdminFile(previewFile.id)" class="px-3 py-1.5 bg-gray-900 text-white rounded-lg text-sm flex items-center gap-1.5 hover:bg-gray-800">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              دانلود
            </button>

            <!-- ===== دکمه‌های فایل لوکال ===== -->
            <button
              v-if="previewFile?.isLocal"
              @click="confirmUploadFromPreview"
              :disabled="uploading"
              class="px-4 py-1.5 bg-green-600 text-white rounded-lg text-sm flex items-center gap-1.5 hover:bg-green-700 disabled:opacity-50 font-bold"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              {{ uploading ? 'در حال آپلود...' : 'تایید و آپلود' }}
            </button>
            <button
              v-if="previewFile?.isLocal"
              @click="changeFile"
              class="px-3 py-1.5 bg-yellow-500 text-white rounded-lg text-sm flex items-center gap-1.5 hover:bg-yellow-600"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              تغییر فایل
            </button>
            <!-- ================================ -->

            <button @click="closePreview" class="p-2 hover:bg-gray-200 rounded-lg transition-colors">
              <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        <!-- Preview Loading -->
        <div v-if="previewLoading" class="flex-1 flex items-center justify-center min-h-[400px]">
          <div class="text-center">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto mb-3"></div>
            <p class="text-sm text-gray-500">در حال بارگذاری فایل...</p>
          </div>
        </div>

        <!-- Preview Body -->
        <div v-else class="flex-1 overflow-hidden rounded-b-2xl bg-gray-100 flex items-center justify-center min-h-[400px]">
          <!-- PDF Preview -->
          <iframe
            v-if="previewUrl && previewType === 'pdf'"
            :src="previewUrl"
            class="w-full h-full min-h-[500px] rounded-b-2xl border-0"
            style="height: 70vh;"
          ></iframe>

          <!-- Image Preview -->
          <img
            v-else-if="previewUrl && previewType === 'image'"
            :src="previewUrl"
            class="max-w-full max-h-full object-contain rounded-lg shadow"
            style="max-height: 70vh;"
            alt="preview"
          />

          <!-- Unsupported -->
          <div v-else class="text-center p-12">
            <svg class="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <p class="text-gray-600 font-medium">پیش‌نمایش برای این نوع فایل پشتیبانی نمی‌شود</p>
            <p class="text-sm text-gray-500 mt-1">لطفاً فایل را دانلود کنید</p>
          </div>
        </div>
      </div>
    </div>
    <!-- ============================================================ -->

    <!-- Order Modal -->
    <div v-if="showOrderModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4" @click.self="closeModal">
      <div class="bg-white rounded-lg w-full max-w-4xl max-h-[90vh] flex flex-col">
        <!-- Header -->
        <div class="flex items-center justify-between p-6 border-b">
          <div>
            <h2 class="text-xl font-bold">جزئیات سفارش</h2>
            <p class="text-sm text-gray-600">{{ selectedOrder?.order_number }}</p>
          </div>
          <button @click="closeModal" class="p-2 hover:bg-gray-100 rounded-lg">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Body -->
        <div class="flex-1 overflow-y-auto p-6 space-y-6">
          <!-- Info Cards -->
          <div class="grid grid-cols-4 gap-4">
            <div class="bg-gray-50 rounded-lg p-4 border">
              <p class="text-xs text-gray-600 mb-1">مشتری</p>
              <p class="font-medium text-sm">{{ selectedOrder?.company_name || `${selectedOrder?.first_name} ${selectedOrder?.last_name}` }}</p>
            </div>
            <div class="bg-gray-50 rounded-lg p-4 border">
              <p class="text-xs text-gray-600 mb-1">تاریخ</p>
              <p class="font-medium text-sm">{{ formatDate(selectedOrder?.created_at) }}</p>
            </div>
            <div class="bg-gray-50 rounded-lg p-4 border">
              <p class="text-xs text-gray-600 mb-1">وزن</p>
              <p class="font-medium">{{ selectedOrder?.weight_kg }} کیلو</p>
            </div>
            <div class="bg-gray-50 rounded-lg p-4 border">
              <p class="text-xs text-gray-600 mb-1">قیمت</p>
              <p class="font-medium text-sm">{{ formatPrice(selectedOrder?.total_price) }}</p>
            </div>
          </div>

          <!-- Status -->
          <div class="bg-blue-50 rounded-lg p-4 border border-blue-200">
            <p class="text-xs text-blue-600 mb-2 font-medium">وضعیت</p>
            <span :class="getStatusColor(selectedOrder?.status)" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium">
              {{ getStatusLabel(selectedOrder?.status) }}
            </span>
          </div>

          <!-- Details -->
          <div>
            <h3 class="text-sm font-semibold mb-3">جزئیات</h3>
            <div class="bg-gray-50 rounded-lg p-4 space-y-2 text-sm">
              <div class="flex justify-between">
                <span class="text-gray-600">محصول:</span>
                <span class="font-medium">{{ selectedOrder?.product_name }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-600">بسته‌بندی:</span>
                <span class="font-medium">{{ selectedOrder?.packaging_name }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-600">پرداخت:</span>
                <span class="font-medium">{{ selectedOrder?.payment_term_name }}</span>
              </div>
            </div>
          </div>

          <!-- Files Section -->
          <div>
            <h3 class="text-sm font-semibold mb-3 flex items-center gap-2">
              <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              فایل‌های پیوست
              <span v-if="selectedOrder?.files && selectedOrder.files.length > 0" class="text-xs bg-gray-900 text-white px-2 py-0.5 rounded-full">
                {{ selectedOrder.files.length }}
              </span>
            </h3>
            
            <div v-if="selectedOrder?.files && selectedOrder.files.length > 0" class="space-y-3">
              <div v-for="file in selectedOrder.files" :key="file.id" 
                   class="flex items-center justify-between p-4 rounded-lg border transition-all"
                   :class="file.uploaded_by_type === 'admin' ? 'bg-blue-50 border-blue-200 hover:bg-blue-100' : 'bg-green-50 border-green-200 hover:bg-green-100'">
                
                <div class="flex items-center gap-3 flex-1">
                  <div 
                    @click="openExistingFilePreview(file)"
                    :class="[
                      'w-14 h-14 rounded-lg flex items-center justify-center flex-shrink-0 cursor-pointer relative overflow-hidden border-2 transition-all hover:scale-105',
                      file.uploaded_by_type === 'admin' ? 'bg-blue-100 border-blue-300 hover:border-blue-500' : 'bg-green-100 border-green-300 hover:border-green-500'
                    ]"
                    title="کلیک برای پیش‌نمایش"
                  >
                    <img v-if="file.thumbnail_url" :src="file.thumbnail_url" class="w-full h-full object-cover rounded-lg" />
                    <template v-else>
                      <svg class="w-7 h-7" :class="file.uploaded_by_type === 'admin' ? 'text-blue-500' : 'text-green-500'" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                      </svg>
                    </template>
                    <div class="absolute inset-0 bg-black bg-opacity-0 hover:bg-opacity-20 flex items-center justify-center rounded-lg transition-all">
                      <svg class="w-5 h-5 text-white opacity-0 hover:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                      </svg>
                    </div>
                  </div>
                  
                  <div class="flex-1 min-w-0">
                    <p class="text-sm font-bold text-gray-900 truncate">{{ file.original_filename }}</p>
                    <div class="flex items-center gap-3 text-xs text-gray-600 mt-1 flex-wrap">
                      <span class="flex items-center gap-1">
                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                        </svg>
                        {{ formatFileSize(file.file_size) }}
                      </span>
                      <span>•</span>
                      <span class="font-medium" :class="file.uploaded_by_type === 'admin' ? 'text-blue-600' : 'text-green-600'">
                        {{ file.uploaded_by_type === 'admin' ? 'ادمین' : 'مشتری' }}
                      </span>
                      <span>•</span>
                      <span>{{ getFileTypeLabel(file.file_type) }}</span>
                    </div>
                  </div>
                </div>
                
                <div class="flex items-center gap-2 ml-3 flex-shrink-0">
                  <button @click="openExistingFilePreview(file)" class="px-3 py-2 bg-white border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-100 text-sm font-medium flex items-center gap-1.5 transition-colors">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                    پیش‌نمایش
                  </button>
                  <button @click="downloadAdminFile(file.id)" class="px-3 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 text-sm font-medium flex items-center gap-1.5">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                    </svg>
                    دانلود
                  </button>
                </div>
              </div>
            </div>
            
            <div v-else class="bg-gray-50 rounded-lg p-8 text-center border border-gray-200">
              <svg class="w-12 h-12 text-gray-400 mx-auto mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
              <p class="text-sm text-gray-600 font-medium">هیچ فایلی آپلود نشده است</p>
            </div>
          </div>

          <!-- Upload Proforma -->
          <div v-if="selectedOrder?.status === 'awaiting_proforma'" class="bg-yellow-50 rounded-lg p-6 border border-yellow-200">
            <h3 class="text-sm font-semibold mb-4">صدور پیش‌فاکتور</h3>
            
            <!-- Drop Zone -->
            <div 
              @click="$refs.proformaInput.click()" 
              @dragover.prevent="isDragging = true"
              @dragleave.prevent="isDragging = false"
              @drop.prevent="handleDrop"
              :class="[
                'border-2 border-dashed rounded-xl p-6 text-center cursor-pointer transition-all',
                isDragging ? 'border-yellow-500 bg-yellow-200' : 'border-yellow-300 hover:bg-yellow-100',
                selectedProformaFile ? 'border-green-400 bg-green-50' : ''
              ]"
            >
              <svg class="w-8 h-8 mx-auto mb-2" :class="selectedProformaFile ? 'text-green-500' : 'text-yellow-500'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <p class="text-sm font-medium" :class="selectedProformaFile ? 'text-green-700' : 'text-yellow-700'">
                {{ selectedProformaFile ? selectedProformaFile.name : 'فایل PDF یا تصویر را اینجا بکشید یا کلیک کنید' }}
              </p>
              <p v-if="!selectedProformaFile" class="text-xs text-yellow-500 mt-1">فایل PDF یا تصویر قابل قبول است</p>
              <p v-if="selectedProformaFile" class="text-xs text-green-500 mt-1">{{ formatFileSize(selectedProformaFile.size) }}</p>
              <input ref="proformaInput" type="file" class="hidden" accept=".pdf,image/*" @change="handleProformaSelect" />
            </div>

            <!-- ===== وضعیت فایل + دکمه‌های پیش‌نمایش و آپلود ===== -->
            <div v-if="selectedProformaFile" class="mt-4 flex items-center gap-3">
              <div class="flex-1 bg-white border border-green-300 rounded-lg px-4 py-3 flex items-center gap-3">
                <svg class="w-8 h-8 text-green-500 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                </svg>
                <div class="flex-1 min-w-0">
                  <p class="text-sm font-bold text-gray-900 truncate">{{ selectedProformaFile.name }}</p>
                  <p class="text-xs text-gray-500">{{ formatFileSize(selectedProformaFile.size) }}</p>
                </div>
                <svg class="w-5 h-5 text-green-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <button 
                @click="openLocalPreview"
                class="px-4 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 text-sm font-bold flex items-center gap-2 flex-shrink-0"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
                پیش‌نمایش
              </button>
              <button 
                @click="uploadProforma" 
                :disabled="uploading" 
                class="px-4 py-3 bg-gray-900 text-white rounded-lg hover:bg-gray-800 disabled:opacity-50 text-sm font-bold flex items-center gap-2 flex-shrink-0"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
                {{ uploading ? 'آپلود...' : 'ارسال' }}
              </button>
            </div>
            <!-- ====================================================== -->
          </div>

          <!-- Driver Info Input -->
          <div v-if="selectedOrder?.status === 'awaiting_loading'" class="bg-blue-50 rounded-lg p-6 border border-blue-200">
            <h3 class="text-sm font-semibold mb-4">اطلاعات راننده</h3>
            <div class="grid grid-cols-2 gap-3 mb-3">
              <input v-model="driverInfo.driver_name" type="text" placeholder="نام راننده" class="px-3 py-2 border rounded-lg text-sm" />
              <input v-model="driverInfo.driver_phone" type="text" placeholder="تلفن" class="px-3 py-2 border rounded-lg text-sm" />
              <input v-model="driverInfo.vehicle_plate" type="text" placeholder="پلاک" class="px-3 py-2 border rounded-lg text-sm" />
              <input v-model="driverInfo.vehicle_type" type="text" placeholder="نوع خودرو" class="px-3 py-2 border rounded-lg text-sm" />
            </div>
            <button @click="saveDriverInfo" class="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm">
              ثبت اطلاعات راننده
            </button>
          </div>

          <!-- Driver Info Display -->
          <div v-if="selectedOrder?.driver_info" class="bg-indigo-50 rounded-xl p-6 border-2 border-indigo-200">
            <div class="flex items-center gap-3 mb-4">
              <svg class="w-6 h-6 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
              </svg>
              <h3 class="text-sm font-bold text-gray-900">اطلاعات راننده</h3>
            </div>
            <div class="bg-white rounded-lg p-4">
              <div class="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <p class="text-xs text-gray-600 mb-1">نام راننده</p>
                  <p class="font-bold text-gray-900">{{ selectedOrder.driver_info.driver_name || '-' }}</p>
                </div>
                <div>
                  <p class="text-xs text-gray-600 mb-1">تلفن</p>
                  <p class="font-bold text-gray-900 dir-ltr text-right">{{ selectedOrder.driver_info.driver_phone || '-' }}</p>
                </div>
                <div v-if="selectedOrder.driver_info.vehicle_type">
                  <p class="text-xs text-gray-600 mb-1">نوع خودرو</p>
                  <p class="font-medium text-gray-900">{{ selectedOrder.driver_info.vehicle_type }}</p>
                </div>
                <div v-if="selectedOrder.driver_info.vehicle_plate">
                  <p class="text-xs text-gray-600 mb-1">پلاک</p>
                  <p class="font-medium text-gray-900">{{ selectedOrder.driver_info.vehicle_plate }}</p>
                </div>
                <div v-if="selectedOrder.driver_info.loading_date">
                  <p class="text-xs text-gray-600 mb-1">تاریخ بارگیری</p>
                  <p class="font-medium text-gray-900">{{ formatDate(selectedOrder.driver_info.loading_date) }}</p>
                </div>
                <div v-if="selectedOrder.driver_info.estimated_delivery_date">
                  <p class="text-xs text-gray-600 mb-1">تحویل تخمینی</p>
                  <p class="font-medium text-gray-900">{{ formatDate(selectedOrder.driver_info.estimated_delivery_date) }}</p>
                </div>
                <div v-if="selectedOrder.driver_info.notes" class="col-span-2">
                  <p class="text-xs text-gray-600 mb-1">یادداشت</p>
                  <p class="font-medium text-gray-700 text-sm">{{ selectedOrder.driver_info.notes }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Change Status -->
          <div class="bg-green-50 rounded-lg p-6 border border-green-200">
            <h3 class="text-sm font-semibold mb-4">تغییر وضعیت</h3>
            <select v-model="newStatus" class="w-full px-4 py-2 border rounded-lg mb-3 text-sm">
              <option value="">انتخاب وضعیت جدید</option>
              <option value="awaiting_proforma_approval">در انتظار تایید</option>
              <option value="awaiting_bill_issue">در انتظار حواله</option>
              <option value="awaiting_loading">در انتظار بارگیری</option>
              <option value="loading_complete">بارگیری شده</option>
              <option value="delivered">تحویل داده شد</option>
              <option value="cancelled">لغو سفارش</option>
            </select>
            <textarea v-if="newStatus === 'cancelled'" v-model="cancellationReason" rows="2" class="w-full px-3 py-2 border rounded-lg text-sm mb-3" placeholder="دلیل لغو..."></textarea>
            <button @click="updateOrderStatus" :disabled="!newStatus || (newStatus === 'cancelled' && !cancellationReason)" class="w-full px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 disabled:opacity-50 text-sm">
              به‌روزرسانی وضعیت
            </button>
          </div>
        </div>

        <!-- Footer -->
        <div class="flex gap-3 p-6 border-t bg-gray-50">
          <button 
            @click="deleteOrder(selectedOrder.id)"
            class="px-4 py-3 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors font-bold flex items-center gap-2"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
            حذف سفارش
          </button>
          <button 
            @click="closeModal"
            class="flex-1 px-4 py-3 border-2 border-gray-300 rounded-lg hover:bg-gray-100 transition-colors font-bold text-gray-700"
          >
            بستن
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedStatus: 'all',
      searchQuery: '',
      showOrderModal: false,
      selectedOrder: null,
      newStatus: '',
      cancellationReason: '',
      selectedProformaFile: null,
      uploading: false,
      loading: true,
      isDragging: false,
      driverInfo: {
        driver_name: '',
        driver_phone: '',
        vehicle_plate: '',
        vehicle_type: ''
      },
      statusTabs: [
        { label: 'همه', value: 'all' },
        { label: 'پیش‌فاکتور', value: 'awaiting_proforma' },
        { label: 'تایید', value: 'awaiting_proforma_approval' },
        { label: 'حواله', value: 'awaiting_bill_issue' },
        { label: 'بارگیری', value: 'awaiting_loading' },
        { label: 'بارگیری شده', value: 'loading_complete' },
        { label: 'تحویل', value: 'delivered' },
        { label: 'لغو', value: 'cancelled' }
      ],
      orders: [],

      // ===== Preview State =====
      showPreviewModal: false,
      previewFile: null,
      previewUrl: null,
      previewType: null,
      previewLoading: false,
      localPreviewUrl: null,
      localPreviewType: null,
      // =========================
    }
  },

  computed: {
    filteredOrders() {
      if (this.selectedStatus === 'all') return this.orders
      return this.orders.filter(o => o.status === this.selectedStatus)
    }
  },

  mounted() {
    this.fetchOrders()
  },

  beforeUnmount() {
    this.revokeLocalPreview()
    this.revokePreview()
    document.body.style.overflow = ''
  },

  methods: {

    // ==================== Scroll Lock ====================

    lockScroll() {
      document.body.style.overflow = 'hidden'
    },

    unlockScroll() {
      if (!this.showOrderModal && !this.showPreviewModal) {
        document.body.style.overflow = ''
      }
    },

    // ==================== Preview Methods ====================

    /**
     * انتخاب فایل → پیش‌نمایش خودکار در مدال
     */
    handleProformaSelect(event) {
      this.revokeLocalPreview()
      const file = event.target.files[0]
      if (!file) return
      this.selectedProformaFile = file
      const url = URL.createObjectURL(file)
      this.localPreviewUrl = url
      this.localPreviewType = this.getFileType(file.type, file.name)
      // ← باز کردن خودکار مدال پیش‌نمایش
      this.openLocalPreview()
    },

    handleDrop(event) {
      this.isDragging = false
      const file = event.dataTransfer.files[0]
      if (!file) return
      const isAccepted = file.type === 'application/pdf' || file.type.startsWith('image/')
      if (!isAccepted) {
        alert('فقط فایل PDF یا تصویر قابل قبول است')
        return
      }
      this.revokeLocalPreview()
      this.selectedProformaFile = file
      const url = URL.createObjectURL(file)
      this.localPreviewUrl = url
      this.localPreviewType = this.getFileType(file.type, file.name)
      // ← باز کردن خودکار مدال پیش‌نمایش
      this.openLocalPreview()
    },

    /** پیش‌نمایش فایل لوکال در مدال بزرگ */
    openLocalPreview() {
      this.previewFile = {
        name: this.selectedProformaFile.name,
        size: this.selectedProformaFile.size,
        isLocal: true
      }
      this.previewUrl = this.localPreviewUrl
      this.previewType = this.localPreviewType
      this.previewLoading = false
      this.showPreviewModal = true
      this.lockScroll()
    },

    /** تایید و آپلود از داخل مدال پیش‌نمایش */
    async confirmUploadFromPreview() {
      this.closePreview()
      await this.uploadProforma()
    },

    /** انتخاب فایل دیگر از داخل مدال پیش‌نمایش */
    changeFile() {
      this.closePreview()
      this.$nextTick(() => {
        if (this.$refs.proformaInput) this.$refs.proformaInput.click()
      })
    },

    /** پیش‌نمایش فایل موجود روی سرور */
    async openExistingFilePreview(file) {
      try {
        const token = localStorage.getItem('admin_token') || localStorage.getItem('access_token') || localStorage.getItem('token')
        if (!token) return

        this.previewFile = file
        this.previewUrl = null
        this.previewType = null
        this.previewLoading = true
        this.showPreviewModal = true
        this.lockScroll()

        const response = await fetch(`https://polychemmb.com/api/admin/orders/download/${file.id}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        })
        if (!response.ok) throw new Error('خطا در بارگذاری فایل')

        const blob = await response.blob()
        this.revokePreview()
        const url = URL.createObjectURL(blob)
        this.previewUrl = url
        this.previewType = this.getFileType(blob.type, file.original_filename)
        this.previewLoading = false

      } catch (error) {
        alert('خطا در نمایش فایل: ' + error.message)
        this.showPreviewModal = false
        this.previewLoading = false
        this.unlockScroll()
      }
    },

    closePreview() {
      this.showPreviewModal = false
      this.previewLoading = false
      this.revokePreview()
      this.previewFile = null
      this.previewUrl = null
      this.previewType = null
      this.unlockScroll()
    },

    revokePreview() {
      if (this.previewUrl && !this.previewFile?.isLocal) {
        URL.revokeObjectURL(this.previewUrl)
      }
    },

    revokeLocalPreview() {
      if (this.localPreviewUrl) {
        URL.revokeObjectURL(this.localPreviewUrl)
        this.localPreviewUrl = null
        this.localPreviewType = null
      }
    },

    getFileType(mimeType, filename) {
      if (!mimeType && filename) {
        const ext = filename.split('.').pop().toLowerCase()
        if (ext === 'pdf') return 'pdf'
        if (['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp'].includes(ext)) return 'image'
        return null
      }
      if (mimeType === 'application/pdf' || (filename || '').endsWith('.pdf')) return 'pdf'
      if (mimeType && mimeType.startsWith('image/')) return 'image'
      return null
    },

    // =========================================================

    async apiCall(endpoint, options = {}) {
      const token = localStorage.getItem('admin_token') || localStorage.getItem('access_token') || localStorage.getItem('token')
      if (!token) {
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
        this.$router.push('/admin/login')
        return null
      }
      if (!response.ok) throw new Error(`HTTP Error: ${response.status}`)
      return await response.json()
    },

    async apiUpload(endpoint, formData) {
      const token = localStorage.getItem('admin_token') || localStorage.getItem('access_token') || localStorage.getItem('token')
      if (!token) return null
      const url = `https://polychemmb.com/api${endpoint}`
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` },
        body: formData
      })
      if (!response.ok) throw new Error(`HTTP Error: ${response.status}`)
      return await response.json()
    },

    async fetchOrders() {
      try {
        this.loading = true
        const data = await this.apiCall('/admin/orders/list')
        if (data?.success) this.orders = data.data || []
      } catch (error) {
        alert('خطا: ' + error.message)
      } finally {
        this.loading = false
      }
    },

    async viewOrder(order) {
      try {
        const data = await this.apiCall(`/admin/orders/${order.id}`)
        if (data?.success) {
          this.selectedOrder = data.data
          this.showOrderModal = true
          this.lockScroll()
        }
      } catch (error) {
        alert('خطا: ' + error.message)
      }
    },

    async uploadProforma() {
      try {
        this.uploading = true
        const formData = new FormData()
        formData.append('file', this.selectedProformaFile)
        const data = await this.apiUpload(`/admin/orders/${this.selectedOrder.id}/upload-proforma`, formData)
        if (data?.success) {
          alert('پیش‌فاکتور آپلود شد')
          this.closeModal()
          this.fetchOrders()
        }
      } catch (error) {
        alert('خطا: ' + error.message)
      } finally {
        this.uploading = false
      }
    },

    async saveDriverInfo() {
      if (!this.driverInfo.driver_name || !this.driverInfo.driver_phone) {
        alert('نام و تلفن راننده الزامی است')
        return
      }
      try {
        const data = await this.apiCall(`/admin/orders/${this.selectedOrder.id}/driver-info`, {
          method: 'POST',
          body: this.driverInfo
        })
        if (data?.success) {
          alert('اطلاعات راننده ثبت شد')
          await this.viewOrder({ id: this.selectedOrder.id })
        }
      } catch (error) {
        alert('خطا: ' + error.message)
      }
    },

    async updateOrderStatus() {
      try {
        const data = await this.apiCall(`/admin/orders/${this.selectedOrder.id}/update-status`, {
          method: 'PUT',
          body: {
            status: this.newStatus,
            change_reason: this.cancellationReason || null
          }
        })
        if (data?.success) {
          alert('وضعیت به‌روز شد')
          this.closeModal()
          this.fetchOrders()
        }
      } catch (error) {
        alert('خطا: ' + error.message)
      }
    },

    async downloadAdminFile(fileId) {
      try {
        const token = localStorage.getItem('admin_token') || localStorage.getItem('access_token') || localStorage.getItem('token')
        if (!token) {
          this.$router.push('/admin/login')
          return
        }
        const response = await fetch(`https://polychemmb.com/api/admin/orders/download/${fileId}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        })
        if (!response.ok) throw new Error('خطا در دانلود فایل')
        const blob = await response.blob()
        const downloadUrl = URL.createObjectURL(blob)
        const link = document.createElement('a')
        link.href = downloadUrl
        link.setAttribute('download', `file_${fileId}.pdf`)
        document.body.appendChild(link)
        link.click()
        link.remove()
        URL.revokeObjectURL(downloadUrl)
      } catch (error) {
        alert('خطا در دانلود فایل: ' + error.message)
      }
    },

    async deleteOrder(orderId) {
      if (!confirm('آیا از حذف این سفارش اطمینان دارید؟\n\nتوجه: تمام فایل‌های مرتبط نیز حذف خواهند شد و این عمل قابل بازگشت نیست!')) {
        return
      }
      try {
        const data = await this.apiCall(`/admin/orders/${orderId}/delete`, {
          method: 'DELETE'
        })
        if (data?.success) {
          alert('سفارش با موفقیت حذف شد')
          this.closeModal()
          this.fetchOrders()
        }
      } catch (error) {
        alert('خطا در حذف سفارش: ' + error.message)
      }
    },

    closeModal() {
      this.showOrderModal = false
      this.selectedOrder = null
      this.newStatus = ''
      this.cancellationReason = ''
      this.revokeLocalPreview()
      this.selectedProformaFile = null
      this.driverInfo = { driver_name: '', driver_phone: '', vehicle_plate: '', vehicle_type: '' }
      this.unlockScroll()
    },

    getFileTypeLabel(fileType) {
      const labels = {
        'proforma_admin': 'پیش‌فاکتور (ادمین)',
        'proforma_client_signed': 'پیش‌فاکتور امضا شده (مشتری)',
        'bill': 'حواله',
        'delivery_receipt': 'رسید تحویل',
        'other': 'سایر'
      }
      return labels[fileType] || fileType
    },

    formatFileSize(bytes) {
      if (!bytes) return '0 بایت'
      const mb = bytes / (1024 * 1024)
      if (mb < 1) {
        const kb = bytes / 1024
        return `${kb.toFixed(1)} کیلوبایت`
      }
      return `${mb.toFixed(2)} مگابایت`
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
      return labels[status] || ''
    },

    getStatusColor(status) {
      const colors = {
        'awaiting_proforma': 'bg-yellow-100 text-yellow-800',
        'awaiting_proforma_approval': 'bg-purple-100 text-purple-800',
        'awaiting_bill_issue': 'bg-orange-100 text-orange-800',
        'awaiting_loading': 'bg-blue-100 text-blue-800',
        'loading_complete': 'bg-indigo-100 text-indigo-800',
        'delivered': 'bg-green-100 text-green-800',
        'cancelled': 'bg-red-100 text-red-800'
      }
      return colors[status] || 'bg-gray-100 text-gray-800'
    },

    formatDate(date) {
      return date ? new Date(date).toLocaleDateString('fa-IR') : '-'
    },

    formatPrice(price) {
      return new Intl.NumberFormat('fa-IR').format(price || 0) + ' ریال'
    }
  },

  watch: {
    selectedStatus() { this.fetchOrders() },
    searchQuery() { this.fetchOrders() }
  }
}
</script>

<style scoped>
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.fade-in-up-1 { animation: fadeInUp 0.6s ease-out 0.1s forwards; opacity: 0; }
.fade-in-up-2 { animation: fadeInUp 0.6s ease-out 0.2s forwards; opacity: 0; }
.slide-in { animation: fadeInUp 0.6s ease-out; }
</style>