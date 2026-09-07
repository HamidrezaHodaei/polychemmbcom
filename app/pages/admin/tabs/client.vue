<!-- app/pages/admin/tabs/clientmanage.vue - UPDATED TO USE COMPREHENSIVE EDIT MODAL -->
<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-4 md:p-8 space-y-6 font-[IRANYekan]" dir="rtl">
    <!-- Header with Statistics -->
    <div class="flex items-center justify-between slide-in">
      <div></div>
      <button 
        type="button"
        @click="showAddClientModal = true"
        class="flex items-center gap-2 px-6 py-3 bg-[#1f2937] text-white rounded-lg hover:from-blue-700 hover:to-blue-800 transition-all shadow-lg hover:shadow-xl"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        افزودن کاربر جدید
      </button>
    </div>

    <!-- Statistics Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 fade-in-up-1">
      <div class="bg-white rounded-lg p-6 border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">تعداد کل کاربران</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ statistics.total_clients || 0 }}</p>
          </div>
          <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg p-6 border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">کاربران فعال</p>
            <p class="text-3xl font-bold text-green-600 mt-2">{{ statistics.active_clients || 0 }}</p>
          </div>
          <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg p-6 border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">کاربران غیرفعال</p>
            <p class="text-3xl font-bold text-red-600 mt-2">{{ statistics.inactive_clients || 0 }}</p>
          </div>
          <div class="w-12 h-12 bg-red-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg p-6 border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">درصد فعالیت</p>
            <p class="text-3xl font-bold text-purple-600 mt-2">{{ statistics.active_percentage || 0 }}%</p>
          </div>
          <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="bg-white rounded-lg border border-gray-200 p-6 fade-in-up-2 shadow-sm">
      <div class="flex flex-col md:flex-row items-center gap-4">
        <div class="flex-1 relative">
          <svg class="w-5 h-5 text-gray-400 absolute right-3 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input
            v-model="searchQuery"
            @keyup.enter="resetPaginationAndLoad()"
            type="text"
            placeholder="جستجوی نام کاربر، ایمیل یا شرکت..."
            class="w-full pr-10 pl-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <select 
          v-model="filterStatus"
          @change="resetPaginationAndLoad()"
          class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="">همه وضعیت‌ها</option>
          <option value="true">فعال</option>
          <option value="false">غیرفعال</option>
        </select>
        <button 
          @click="resetPaginationAndLoad()"
          type="button"
          class="px-6 py-2 bg-[#1f2937] text-white rounded-lg hover:bg-gray-800 transition-colors"
        >
          جستجو
        </button>
      </div>
    </div>

    <!-- Clients Table -->
    <div class="bg-white rounded-lg border border-gray-200 overflow-hidden fade-in-up shadow-sm">
      <!-- Loading State -->
      <div v-if="loading" class="p-8 text-center">
        <div class="inline-block">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        </div>
        <p class="text-gray-600 mt-4">در حال بارگذاری...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="p-6 bg-red-50 border-t border-red-200">
        <div class="flex items-center gap-3">
          <svg class="w-5 h-5 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4v.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <div>
            <p class="font-semibold text-red-800">خطا</p>
            <p class="text-sm text-red-700">{{ error }}</p>
          </div>
        </div>
      </div>

      <!-- Table -->
      <div v-else class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-50 border-b border-gray-200">
            <tr>
              <th class="text-right py-3 px-6 text-xs font-semibold text-gray-700 uppercase">شناسه</th>
              <th class="text-right py-3 px-6 text-xs font-semibold text-gray-700 uppercase">نام کاربری</th>
              <th class="text-right py-3 px-6 text-xs font-semibold text-gray-700 uppercase">نام و نام خانوادگی</th>
              <th class="text-right py-3 px-6 text-xs font-semibold text-gray-700 uppercase">ایمیل</th>
              <th class="text-right py-3 px-6 text-xs font-semibold text-gray-700 uppercase">شرکت</th>
              <th class="text-right py-3 px-6 text-xs font-semibold text-gray-700 uppercase">وضعیت</th>
              <th class="text-right py-3 px-6 text-xs font-semibold text-gray-700 uppercase">تاریخ عضویت</th>
              <th class="text-right py-3 px-6 text-xs font-semibold text-gray-700 uppercase">اقدام</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="client in clients" :key="client.id" class="hover:bg-gray-50 transition-colors">
              <td class="py-4 px-6">
                <span class="text-sm text-gray-500">#{{ client.id }}</span>
              </td>
              <td class="py-4 px-6">
                <span class="font-medium text-gray-900">{{ client.username }}</span>
              </td>
              <td class="py-4 px-6">
                <span class="text-gray-700">{{ client.first_name }} {{ client.last_name }}</span>
              </td>
              <td class="py-4 px-6">
                <span class="text-gray-600 text-sm">{{ client.email }}</span>
              </td>
              <td class="py-4 px-6">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-700">
                  {{ client.company_name }}
                </span>
              </td>
              <td class="py-4 px-6">
                <span 
                  :class="[
                    'inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium',
                    client.is_active ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
                  ]"
                >
                  <span class="w-2 h-2 rounded-full" :class="client.is_active ? 'bg-green-500' : 'bg-red-500'"></span>
                  {{ client.is_active ? 'فعال' : 'غیرفعال' }}
                </span>
              </td>
              <td class="py-4 px-6 text-sm text-gray-600">
                {{ formatDate(client.created_at) }}
              </td>
              <td class="py-4 px-6">
                <div class="flex items-center gap-2">
                  <!-- دکمه مشاهده لاگ‌ها -->
                  <button 
                    @click="viewClientLogs(client)"
                    type="button"
                    class="p-2 hover:bg-purple-100 rounded-lg transition-colors group relative"
                    title="مشاهده لاگ‌ها"
                  >
                    <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                    <span class="absolute bottom-full right-1/2 translate-x-1/2 mb-2 px-2 py-1 text-xs text-white bg-gray-900 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none">
                      مشاهده لاگ‌ها
                    </span>
                  </button>

                  <!-- دکمه ویرایش جامع -->
                  <button 
                    @click="editClientComprehensive(client)"
                    type="button"
                    class="p-2 hover:bg-blue-100 rounded-lg transition-colors group relative"
                    title="ویرایش جامع"
                  >
                    <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                    <span class="absolute bottom-full right-1/2 translate-x-1/2 mb-2 px-2 py-1 text-xs text-white bg-gray-900 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none">
                      ویرایش جامع
                    </span>
                  </button>

                  <!-- دکمه حذف -->
                  <button 
                    @click="deleteClient(client)"
                    type="button"
                    class="p-2 hover:bg-red-100 rounded-lg transition-colors group relative"
                    title="حذف"
                  >
                    <svg class="w-5 h-5 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                    <span class="absolute bottom-full right-1/2 translate-x-1/2 mb-2 px-2 py-1 text-xs text-white bg-gray-900 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none">
                      حذف
                    </span>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Empty State -->
        <div v-if="clients.length === 0" class="p-12 text-center">
          <svg class="w-12 h-12 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <p class="text-gray-600">کاربری یافت نشد</p>
        </div>
      </div>

      <!-- Pagination -->
      <div v-if="!loading && clients.length > 0" class="flex items-center justify-between px-6 py-4 border-t border-gray-200 bg-gray-50">
        <p class="text-sm text-gray-600">
          صفحه {{ pagination.page }} از {{ pagination.total_pages }} (کل: {{ pagination.total }})
        </p>
        <div class="flex items-center gap-2">
          <button 
            @click="previousPage()"
            :disabled="!pagination.has_prev"
            type="button"
            class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            قبلی
          </button>
          <span class="text-sm text-gray-600">{{ pagination.page }}</span>
          <button 
            @click="nextPage()"
            :disabled="!pagination.has_next"
            type="button"
            class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            بعدی
          </button>
        </div>
      </div>
    </div>

    <!-- Simple Add Modal (Same as before) -->
    <div v-if="showAddClientModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-lg w-full max-w-2xl max-h-[90vh] flex flex-col shadow-xl">
        <div class="flex items-center justify-between p-6 border-b border-gray-200">
          <h2 class="text-xl font-bold text-gray-900">افزودن کاربر جدید</h2>
          <button 
            @click="closeModal()"
            type="button"
            class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div class="flex-1 overflow-y-auto p-6">
          <div v-if="modalError" class="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg">
            <p class="text-sm text-red-700">{{ modalError }}</p>
          </div>

          <div class="space-y-4">
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">نام کاربری *</label>
                <input 
                  v-model="formData.username"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">رمز عبور *</label>
                <input 
                  v-model="formData.password"
                  type="password"
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">نام *</label>
                <input 
                  v-model="formData.first_name"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">نام خانوادگی *</label>
                <input 
                  v-model="formData.last_name"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">نام شرکت *</label>
              <input 
                v-model="formData.company_name"
                type="text"
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">ایمیل *</label>
                <input 
                  v-model="formData.email"
                  type="email"
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">شماره تماس *</label>
                <input 
                  v-model="formData.phone"
                  type="tel"
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">آدرس</label>
              <textarea 
                v-model="formData.address"
                rows="2"
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              ></textarea>
            </div>
          </div>
        </div>

        <div class="flex gap-3 p-6 border-t border-gray-200 bg-gray-50">
          <button 
            @click="closeModal()"
            type="button"
            class="flex-1 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-100 transition-colors font-medium"
          >
            لغو
          </button>
          <button 
            @click="saveClient()"
            :disabled="submitting"
            type="button"
            class="flex-1 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 transition-colors font-medium"
          >
            {{ submitting ? 'در حال ارسال...' : 'افزودن کاربر' }}
          </button>
        </div>
      </div>
    </div>

    <!-- ✅ Comprehensive Edit Modal -->
    <AdminClientEditModal
      :isOpen="showComprehensiveEditModal"
      :clientData="selectedClientForEdit || {}"
      @close="closeComprehensiveEditModal()"
      @saved="handleClientSaved()"
    />

    <!-- Client Logs Modal -->
    <ClientLogsModal
      :isOpen="showLogsModal"
      :clientId="selectedClientForLogs?.id"
      :clientInfo="selectedClientForLogs"
      @close="closeLogsModal()"
    />
  </div>
</template>

<script>
import ClientLogsModal from '@/components/ClientLogsModal.vue'
import AdminClientEditModal from '@/components/AdminClientEditModal.vue'

export default {
  name: 'AdminClientManagement',
  components: {
    ClientLogsModal,
    AdminClientEditModal
  },
  data() {
    return {
      clients: [],
      statistics: {
        total_clients: 0,
        active_clients: 0,
        inactive_clients: 0,
        active_percentage: 0
      },
      loading: false,
      error: '',
      modalError: '',
      showAddClientModal: false,
      showComprehensiveEditModal: false,
      selectedClientForEdit: null,
      submitting: false,
      searchQuery: '',
      filterStatus: '',
      pagination: {
        page: 1,
        limit: 10,
        total: 0,
        total_pages: 0,
        has_next: false,
        has_prev: false
      },
      formData: {
        username: '',
        password: '',
        email: '',
        first_name: '',
        last_name: '',
        company_name: '',
        phone: '',
        address: '',
        is_active: true,
        id: null
      },
      showLogsModal: false,
      selectedClientForLogs: null
    }
  },
  computed: {
    apiBaseURL() {
      return process.env.VUE_APP_API_URL || 'https://polychemmb.com'
    }
  },
  methods: {
    viewClientLogs(client) {
      this.selectedClientForLogs = client
      this.showLogsModal = true
    },

    closeLogsModal() {
      this.showLogsModal = false
      this.selectedClientForLogs = null
    },

    // ✅ NEW: Open comprehensive edit modal
    editClientComprehensive(client) {
      this.selectedClientForEdit = client
      this.showComprehensiveEditModal = true
    },

    // ✅ NEW: Close comprehensive edit modal
    closeComprehensiveEditModal() {
      this.showComprehensiveEditModal = false
      this.selectedClientForEdit = null
    },

    // ✅ NEW: Handle save from comprehensive modal
    async handleClientSaved() {
      await this.loadClients()
      await this.loadStatistics()
    },

    async loadClients() {
      this.loading = true;
      this.error = '';
      
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          this.error = 'توکن احراز هویت یافت نشد';
          this.$router.push('/admin/login');
          return;
        }

        let url = `${this.apiBaseURL}/api/admin/clients?page=${this.pagination.page}&limit=${this.pagination.limit}`;
        
        if (this.searchQuery) {
          url += `&search=${encodeURIComponent(this.searchQuery)}`;
        }
        
        if (this.filterStatus !== '') {
          url += `&is_active=${this.filterStatus}`;
        }

        const response = await fetch(url, {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });

        if (response.status === 401) {
          this.error = 'احراز هویت نامعتبر است';
          this.$router.push('/admin/login');
          return;
        }

        if (!response.ok) {
          throw new Error(`خطای سرور: ${response.status}`);
        }

        const data = await response.json();
        
        if (data.success) {
          let clientsList = [];
          
          if (data.clients && data.clients.clients && Array.isArray(data.clients.clients)) {
            clientsList = data.clients.clients;
          } else if (data.clients && Array.isArray(data.clients)) {
            clientsList = data.clients;
          }
          
          this.clients = clientsList;
          this.pagination = data.pagination || this.pagination;
          
          if (data.clients && data.clients.total) {
            this.pagination.total = data.clients.total;
            this.pagination.total_pages = Math.ceil(data.clients.total / this.pagination.limit);
          }
        } else {
          this.error = data.message || 'خطا در بارگذاری کاربران';
        }
      } catch (err) {
        this.error = `خطا در ارتباط با سرور: ${err.message}`;
        console.error('Load clients error:', err);
      } finally {
        this.loading = false;
      }
    },

    async loadStatistics() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) return;

        const response = await fetch(`${this.apiBaseURL}/api/admin/clients/statistics`, {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });

        if (response.ok) {
          const data = await response.json();
          if (data.success) {
            this.statistics = data.statistics;
          }
        }
      } catch (err) {
        console.error('Load statistics error:', err);
      }
    },

    closeModal() {
      this.showAddClientModal = false;
      this.modalError = '';
      this.resetForm();
    },

    resetForm() {
      this.formData = {
        id: null,
        username: '',
        password: '',
        email: '',
        first_name: '',
        last_name: '',
        company_name: '',
        phone: '',
        address: '',
        is_active: true
      };
    },

    async saveClient() {
      this.modalError = '';

      const required = ['username', 'password', 'email', 'first_name', 'last_name', 'company_name', 'phone'];
      const missing = required.filter(f => !this.formData[f] || this.formData[f].trim() === '');
      
      if (missing.length > 0) {
        this.modalError = `فیلدهای الزامی را پر کنید: ${missing.join(', ')}`;
        return;
      }

      if (this.formData.username.length < 3) {
        this.modalError = 'نام کاربری باید حداقل 3 کاراکتر باشد';
        return;
      }

      if (this.formData.password.length < 8) {
        this.modalError = 'رمز عبور باید حداقل 8 کاراکتر باشد';
        return;
      }

      this.submitting = true;

      try {
        const token = localStorage.getItem('access_token');
        const createPayload = {
          username: this.formData.username.trim(),
          password: this.formData.password,
          email: this.formData.email.trim(),
          first_name: this.formData.first_name.trim(),
          last_name: this.formData.last_name.trim(),
          company_name: this.formData.company_name.trim(),
          phone: this.formData.phone.trim(),
          address: this.formData.address.trim(),
          is_active: true
        };

        const response = await fetch(`${this.apiBaseURL}/api/admin/clients/`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(createPayload)
        });

        const data = await response.json();

        if (data.success) {
          this.closeModal();
          await this.loadClients();
          await this.loadStatistics();
        } else {
          this.modalError = data.message || 'خطا در ایجاد کاربر';
        }
      } catch (err) {
        this.modalError = `خطا در ارتباط با سرور: ${err.message}`;
        console.error('Save client error:', err);
      } finally {
        this.submitting = false;
      }
    },

    async deleteClient(client) {
      if (!client || !client.id) {
        this.error = 'خطا: شناسه کاربر یافت نشد';
        return;
      }

      if (!confirm(`آیا از حذف کاربر "${client.username}" اطمینان دارید؟ این عملیات قابل بازگشت نیست.`)) {
        return;
      }

      try {
        const token = localStorage.getItem('access_token');
        const response = await fetch(`${this.apiBaseURL}/api/admin/clients/${client.id}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });

        const data = await response.json();

        if (data.success) {
          await this.loadClients();
          await this.loadStatistics();
        } else {
          this.error = data.message || 'خطا در حذف کاربر';
        }
      } catch (err) {
        this.error = `خطا در ارتباط با سرور: ${err.message}`;
        console.error('Delete client error:', err);
      }
    },

    resetPaginationAndLoad() {
      this.pagination.page = 1;
      this.loadClients();
    },

    nextPage() {
      if (this.pagination.has_next) {
        this.pagination.page++;
        this.loadClients();
      }
    },

    previousPage() {
      if (this.pagination.has_prev) {
        this.pagination.page--;
        this.loadClients();
      }
    },

    formatDate(dateString) {
      if (!dateString) return '-';
      try {
        const date = new Date(dateString);
        return date.toLocaleDateString('fa-IR', {
          year: 'numeric',
          month: '2-digit',
          day: '2-digit'
        });
      } catch {
        return dateString;
      }
    }
  },
  mounted() {
    this.loadClients();
    this.loadStatistics();
  }
}
</script>

<style scoped>
@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
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

.slide-in {
  animation: slideDown 0.6s ease-out;
}

.fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
}

.fade-in-up-1 {
  animation: fadeInUp 0.6s ease-out 0.1s forwards;
  opacity: 0;
}

.fade-in-up-2 {
  animation: fadeInUp 0.6s ease-out 0.2s forwards;
  opacity: 0;
}
</style>