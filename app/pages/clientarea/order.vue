<!-- pages/clientarea/order.vue - نسخه کامل با نمایش اطلاعات راننده -->
<template>
  <div class="flex-1 overflow-y-auto custom-scrollbar font-[IRANYekan]" dir="rtl">
    <!-- Status Filter Tabs -->
    <div class="bg-white/70 backdrop-blur-xl rounded-2xl border border-white/40 shadow-lg mb-6 overflow-hidden">
      <div class="flex items-center gap-2 p-4 overflow-x-auto">
        <button 
          v-for="tab in statusTabs"
          :key="tab.value"
          @click="selectedStatus = tab.value"
          :class="[
            'px-4 py-2 whitespace-nowrap rounded-lg transition-all font-medium text-sm',
            selectedStatus === tab.value
              ? 'bg-yellow-400 text-gray-900 shadow-md'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          ]"
        >
          {{ tab.label }}
        </button>
      </div>
    </div>

    <!-- Orders List -->
    <div class="space-y-4 pb-6" v-if="!loading">
      <div v-for="order in filteredOrders" :key="order.id" 
           class="bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl border border-white/40">
        
        <!-- Order Header -->
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center gap-4">
            <h3 class="text-sm font-semibold text-gray-700">
              سفارش <span class="text-yellow-600">{{ order.order_number }}</span>
            </h3>
            <span class="text-xs text-gray-500">{{ formatDate(order.created_at) }}</span>
          </div>
          <button 
            @click="viewOrderDetails(order)"
            class="bg-yellow-400 hover:bg-yellow-500 text-gray-900 px-6 py-2 rounded-full text-sm font-bold transition-all hover:scale-105 flex items-center gap-2"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
            مشاهده
          </button>
        </div>

        <!-- Order Items -->
        <div class="space-y-4 mb-6">
          <div class="flex items-center gap-4 p-4 bg-white/40 rounded-2xl transition-all hover:bg-white/50">
            <div class="w-20 h-20 bg-gradient-to-br from-yellow-100 to-yellow-200 rounded-xl flex items-center justify-center flex-shrink-0">
              <svg class="w-10 h-10 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
              </svg>
            </div>
            
            <div class="flex-1">
              <h4 class="text-base font-bold text-gray-900 mb-1">{{ order.product_name }}</h4>
              <div class="flex items-center gap-4 text-xs text-gray-700">
                <span>وزن: <span class="font-semibold">{{ order.weight_kg }} کیلو</span></span>
                <span>بسته‌بندی: <span class="font-semibold">{{ order.packaging_name }}</span></span>
              </div>
            </div>

            <div class="text-left">
              <p class="text-xs text-gray-600 mb-1">وضعیت</p>
              <span :class="getStatusColorBadge(order.status)" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium">
                {{ getStatusLabel(order.status) }}
              </span>
            </div>
          </div>
        </div>

        <!-- Order Footer -->
        <div class="flex items-center justify-between pt-4 border-t border-gray-200">
          <div class="flex items-center gap-3">
            <button 
              v-if="order.status === 'awaiting_proforma_approval'"
              @click="uploadSignedProforma(order)"
              class="text-sm text-blue-600 hover:text-blue-700 font-semibold flex items-center gap-2"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              آپلود پیش‌فاکتور
            </button>
            <button 
              v-if="order.status === 'awaiting_proforma'"
              class="text-sm text-gray-500 font-semibold flex items-center gap-2"
            >
              <svg class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              در انتظار صدور پیش‌فاکتور
            </button>
          </div>
          <div class="text-left">
            <p class="text-xl font-bold text-gray-900">{{ formatPrice(order.total_price) }} تومان</p>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="filteredOrders.length === 0" class="bg-white/60 backdrop-blur-xl rounded-3xl p-12 shadow-xl border border-white/40 text-center">
        <svg class="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
        </svg>
        <h3 class="text-lg font-bold text-gray-900 mb-2">سفارشی یافت نشد</h3>
      </div>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="flex items-center justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-yellow-400"></div>
    </div>

    <!-- Modal -->
    <div v-if="showOrderModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4" @click.self="closeModal">
      <div class="bg-white rounded-2xl w-full max-w-4xl max-h-[90vh] flex flex-col shadow-2xl">
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
          <!-- Info -->
          <div class="grid grid-cols-4 gap-4">
            <div class="bg-yellow-50 rounded-xl p-4 border border-yellow-200">
              <p class="text-xs text-yellow-700 mb-1 font-medium">محصول</p>
              <p class="font-bold text-sm">{{ selectedOrder?.product_name }}</p>
            </div>
            <div class="bg-blue-50 rounded-xl p-4 border border-blue-200">
              <p class="text-xs text-blue-700 mb-1 font-medium">وزن</p>
              <p class="font-bold">{{ selectedOrder?.weight_kg }} کیلو</p>
            </div>
            <div class="bg-purple-50 rounded-xl p-4 border border-purple-200">
              <p class="text-xs text-purple-700 mb-1 font-medium">بسته‌بندی</p>
              <p class="font-bold text-sm">{{ selectedOrder?.packaging_name }}</p>
            </div>
            <div class="bg-green-50 rounded-xl p-4 border border-green-200">
              <p class="text-xs text-green-700 mb-1 font-medium">قیمت</p>
              <p class="font-bold text-sm">{{ formatPrice(selectedOrder?.total_price) }}</p>
            </div>
          </div>

          <!-- Current Status Section -->
          <div class="bg-gradient-to-br from-yellow-50 to-orange-50 rounded-xl p-6 border border-yellow-200">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-yellow-400 rounded-full flex items-center justify-center">
                <svg class="w-5 h-5 text-gray-900" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <div>
                <p class="text-xs text-yellow-700 font-medium">وضعیت فعلی سفارش</p>
                <span :class="getStatusColorBadge(selectedOrder?.status)" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-bold mt-1">
                  {{ getStatusLabel(selectedOrder?.status) }}
                </span>
              </div>
            </div>
            <p class="text-sm text-gray-700 bg-white/50 rounded-lg p-3">
              {{ getStatusDescription(selectedOrder?.status) }}
            </p>
          </div>

          <!-- Stage 1: Awaiting Proforma -->
       <div v-if="selectedOrder?.status === 'awaiting_proforma'">
        
            </div>

          <!-- Stage 2: Upload -->
          <div v-if="selectedOrder?.status === 'awaiting_proforma_approval'" class="bg-purple-50 rounded-xl p-6 border-2 border-purple-200">
            <h3 class="text-sm font-bold mb-4">تایید پیش‌فاکتور</h3>
            
            <!-- Download -->
            <div class="mb-4" v-if="proformaFile">
              <h4 class="text-sm font-medium mb-3">پیش‌فاکتور صادر شده</h4>
              <div class="flex items-center justify-between p-4 bg-white border-2 border-purple-200 rounded-lg">
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 bg-red-100 rounded-lg flex items-center justify-center">
                    <svg class="w-6 h-6 text-red-600" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <div>
                    <p class="text-sm font-bold">{{ proformaFile.original_filename }}</p>
                    <p class="text-xs text-gray-600">{{ formatFileSize(proformaFile.file_size) }}</p>
                  </div>
                </div>
                <button @click="downloadFile(proformaFile.id)" class="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-lg font-medium text-sm flex items-center gap-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  دانلود
                </button>
              </div>
            </div>

            <!-- Upload -->
            <div>
              <h4 class="text-sm font-medium mb-3">آپلود امضا شده</h4>
              <div @click="triggerFileUpload" class="border-2 border-dashed border-purple-300 rounded-lg p-8 text-center bg-white hover:bg-purple-50 cursor-pointer">
                <svg class="w-12 h-12 text-purple-600 mx-auto mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
                <p class="text-sm text-purple-700 font-bold mb-1">{{ selectedFile ? selectedFile.name : 'آپلود PDF' }}</p>
                <p class="text-xs text-gray-500">حداکثر 10MB</p>
                <input ref="fileInput" type="file" class="hidden" accept=".pdf" @change="handleFileSelect" />
              </div>
              <button v-if="selectedFile" @click="submitSignedProforma" :disabled="uploading" class="w-full mt-4 px-4 py-3 bg-purple-600 text-white rounded-lg hover:bg-purple-700 font-bold disabled:opacity-50">
                {{ uploading ? 'در حال آپلود...' : 'ارسال' }}
              </button>
            </div>
          </div>
   <!-- Stage 3: Awaiting Bill Issue -->
            <div v-else-if="selectedOrder?.status === 'awaiting_bill_issue'" >
             
            </div>

          <!-- Stage 4: Awaiting Loading -->
          <div v-if="selectedOrder?.status === 'awaiting_loading'" class="bg-blue-50 rounded-xl p-6 border-2 border-blue-200">
            <div class="flex items-center gap-3 mb-4">
              <span class="flex items-center justify-center w-8 h-8 rounded-full bg-blue-400 text-white text-sm font-bold">4</span>
              <h3 class="text-sm font-bold text-gray-900">در انتظار بارگیری</h3>
            </div>
            <div class="bg-white rounded-lg p-4">
              <div class="flex items-start gap-3">
                <svg class="w-5 h-5 text-blue-600 mt-0.5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                <div>
                  <p class="text-sm text-gray-900 font-medium mb-1">آماده بارگیری</p>
                  <p class="text-xs text-gray-600">سفارش شما آماده بارگیری می‌باشد.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- 🆕 Driver Info Display -->
          <div v-if="selectedOrder?.driver_info && (selectedOrder?.status === 'loading_complete' || selectedOrder?.status === 'delivered')" 
               class="bg-indigo-50 rounded-xl p-6 border-2 border-indigo-200">
            <div class="flex items-center gap-3 mb-4">
              <span class="flex items-center justify-center w-8 h-8 rounded-full bg-indigo-400 text-white text-sm font-bold">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </span>
              <h3 class="text-sm font-bold text-gray-900">اطلاعات راننده</h3>
            </div>
            
            <div class="bg-white rounded-lg p-4">
              <div class="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <p class="text-xs text-gray-600 mb-1">نام راننده</p>
                  <p class="font-bold text-gray-900">{{ selectedOrder.driver_info.driver_name }}</p>
                </div>
                <div>
                  <p class="text-xs text-gray-600 mb-1">تلفن راننده</p>
                  <p class="font-bold text-gray-900 dir-ltr text-right">{{ selectedOrder.driver_info.driver_phone }}</p>
                </div>
                
                <div v-if="selectedOrder.driver_info.vehicle_type">
                  <p class="text-xs text-gray-600 mb-1">نوع خودرو</p>
                  <p class="font-medium text-gray-900">{{ selectedOrder.driver_info.vehicle_type }}</p>
                </div>
                <div v-if="selectedOrder.driver_info.vehicle_plate">
                  <p class="text-xs text-gray-600 mb-1">شماره پلاک</p>
                  <p class="font-medium text-gray-900">{{ selectedOrder.driver_info.vehicle_plate }}</p>
                </div>
                
                <div v-if="selectedOrder.driver_info.estimated_delivery_date" class="col-span-2">
                  <p class="text-xs text-gray-600 mb-1">زمان تحویل تخمینی</p>
                  <p class="font-medium text-gray-900">{{ formatDate(selectedOrder.driver_info.estimated_delivery_date) }}</p>
                </div>
              </div>
              
              <div v-if="selectedOrder.driver_info.notes" class="mt-4 p-3 bg-blue-50 rounded-lg border border-blue-200">
                <p class="text-xs text-blue-700 mb-1 font-medium">یادداشت</p>
                <p class="text-sm text-gray-700">{{ selectedOrder.driver_info.notes }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Footer -->
        <div class="p-6 border-t">
          <button @click="closeModal" class="w-full px-4 py-3 border-2 border-gray-300 rounded-lg hover:bg-gray-100 font-bold">
            بستن
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      selectedStatus: 'all',
      showOrderModal: false,
      selectedOrder: null,
      selectedFile: null,
      uploading: false,
      loading: true,
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
      orders: []
    }
  },
  computed: {
    filteredOrders() {
      if (this.selectedStatus === 'all') return this.orders
      return this.orders.filter(order => order.status === this.selectedStatus)
    },
    proformaFile() {
      if (!this.selectedOrder || !this.selectedOrder.files) return null
      return this.selectedOrder.files.find(f => f.file_type === 'proforma_admin')
    }
  },
  mounted() {
    this.fetchOrders()
  },
  methods: {
    async fetchOrders() {
      try {
        this.loading = true
        const token = localStorage.getItem('client_token') || localStorage.getItem('token')
        const response = await axios.get('https://polychemmb.com/api/client/orders/list', {
          headers: { 'Authorization': `Bearer ${token}` },
          params: { status: this.selectedStatus }
        })
        if (response.data.success) this.orders = response.data.data
      } catch (error) {
        console.error(error)
        alert('خطا در دریافت سفارشات')
      } finally {
        this.loading = false
      }
    },
    async viewOrderDetails(order) {
      try {
        const token = localStorage.getItem('client_token') || localStorage.getItem('token')
        const response = await axios.get(`https://polychemmb.com/api/client/orders/${order.id}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        })
        if (response.data.success) {
          console.log('=== CLIENT ORDER DATA ===')
          console.log('Full order:', response.data.data)
          console.log('Driver info:', response.data.data.driver_info)
          console.log('Files:', response.data.data.files)
          console.log('=========================')
          
          this.selectedOrder = response.data.data
          this.showOrderModal = true
        }
      } catch (error) {
        console.error(error)
        alert('خطا')
      }
    },
    closeModal() {
      this.showOrderModal = false
      this.selectedOrder = null
      this.selectedFile = null
    },
    uploadSignedProforma(order) {
      this.viewOrderDetails(order)
    },
    triggerFileUpload() {
      this.$refs.fileInput.click()
    },
    handleFileSelect(event) {
      const file = event.target.files[0]
      if (file) {
        if (file.size > 10 * 1024 * 1024) return alert('حداکثر 10MB')
        if (file.type !== 'application/pdf') return alert('فقط PDF')
        this.selectedFile = file
      }
    },
    async submitSignedProforma() {
      if (!this.selectedFile) return alert('فایل انتخاب کنید')
      try {
        this.uploading = true
        const token = localStorage.getItem('client_token') || localStorage.getItem('token')
        const formData = new FormData()
        formData.append('file', this.selectedFile)
        const response = await axios.post(
          `https://polychemmb.com/api/client/orders/${this.selectedOrder.id}/upload-signed-proforma`,
          formData,
          {
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'multipart/form-data'
            }
          }
        )
        if (response.data.success) {
          alert('آپلود شد')
          this.closeModal()
          this.fetchOrders()
        }
      } catch (error) {
        alert('خطا: ' + error.message)
      } finally {
        this.uploading = false
      }
    },
    async downloadFile(fileId) {
      try {
        const token = localStorage.getItem('client_token') || localStorage.getItem('token')
        const response = await axios.get(`https://polychemmb.com/api/client/orders/download/${fileId}`, {
          headers: { 'Authorization': `Bearer ${token}` },
          responseType: 'blob'
        })
        const url = window.URL.createObjectURL(new Blob([response.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', `proforma.pdf`)
        document.body.appendChild(link)
        link.click()
        link.remove()
      } catch (error) {
        alert('خطا در دانلود')
      }
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
    getStatusColorBadge(status) {
      const colors = {
        'awaiting_proforma': 'bg-yellow-100 text-yellow-800 border border-yellow-300',
        'awaiting_proforma_approval': 'bg-purple-100 text-purple-800 border border-purple-300',
        'awaiting_bill_issue': 'bg-orange-100 text-orange-800 border border-orange-300',
        'awaiting_loading': 'bg-blue-100 text-blue-800 border border-blue-300',
        'loading_complete': 'bg-indigo-100 text-indigo-800 border border-indigo-300',
        'delivered': 'bg-green-100 text-green-800 border border-green-300',
        'cancelled': 'bg-red-100 text-red-800 border border-red-300'
      }
      return colors[status] || 'bg-gray-100 text-gray-800'
    },
    getStatusDescription(status) {
      const descriptions = {
        'awaiting_proforma': 'در حال آماده‌سازی پیش‌فاکتور',
        'awaiting_proforma_approval': 'پیش‌فاکتور صادر شد. لطفاً نسخه مهر و امضا شده را برای تأیید بارگذاری کنید.',
        'awaiting_bill_issue': 'در حال صدور حواله',
        'awaiting_loading': 'آماده بارگیری',
        'loading_complete': 'بارگیری شده',
        'delivered': 'تحویل داده شد',
        'cancelled': 'لغو شده'
      }
      return descriptions[status] || ''
    },
    formatDate(date) {
      return date ? new Date(date).toLocaleDateString('fa-IR') : '-'
    },
    formatPrice(price) {
      return new Intl.NumberFormat('fa-IR').format(price || 0)
    },
    formatFileSize(bytes) {
      if (!bytes) return '0 بایت'
      return `${(bytes / (1024 * 1024)).toFixed(2)} MB`
    }
  },
  watch: {
    selectedStatus() { this.fetchOrders() }
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
}
</style>