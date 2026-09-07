<!-- app/components/ClientLogsModal.vue -->
<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4" @click.self="close">
    <div class="bg-white rounded-lg w-full max-w-6xl max-h-[90vh] flex flex-col shadow-xl">
      <!-- Modal Header -->
      <div class="flex items-center justify-between p-6 border-b border-gray-200">
        <div>
          <h2 class="text-xl font-bold text-gray-900">لاگ‌های کاربر</h2>
          <p v-if="clientInfo" class="text-sm text-gray-600 mt-1">
            {{ clientInfo.first_name }} {{ clientInfo.last_name }} ({{ clientInfo.username }})
          </p>
        </div>
        <button 
          @click="close"
          type="button"
          class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
        >
          <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Tabs -->
      <div class="flex border-b border-gray-200 px-6">
        <button 
          @click="activeTab = 'logins'"
          :class="[
            'px-4 py-3 font-medium transition-colors',
            activeTab === 'logins' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-gray-900'
          ]"
        >
          ورود/خروج ({{ totalLogins }})
        </button>
        <button 
          @click="activeTab = 'activities'"
          :class="[
            'px-4 py-3 font-medium transition-colors',
            activeTab === 'activities' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-gray-900'
          ]"
        >
          فعالیت‌ها ({{ totalActivities }})
        </button>
      </div>

      <!-- Modal Body -->
      <div class="flex-1 overflow-y-auto p-6">
        <!-- Loading State -->
        <div v-if="loading" class="text-center py-12">
          <div class="inline-block">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
          </div>
          <p class="text-gray-600 mt-4">در حال بارگذاری...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg">
          <p class="text-sm text-red-700">{{ error }}</p>
        </div>

        <!-- Login Logs -->
        <div v-else-if="activeTab === 'logins'">
          <div v-if="loginLogs.length === 0" class="text-center py-12">
            <svg class="w-12 h-12 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <p class="text-gray-600">لاگ ورودی یافت نشد</p>
          </div>

          <div v-else class="space-y-3">
            <div 
              v-for="log in loginLogs" 
              :key="log.id"
              class="border border-gray-200 rounded-lg p-4 hover:bg-gray-50 transition-colors"
            >
              <div class="flex items-start justify-between">
                <div class="flex-1">
                  <div class="flex items-center gap-2 mb-2">
                    <span 
                      :class="[
                        'inline-flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium',
                        log.success ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
                      ]"
                    >
                      <span class="w-2 h-2 rounded-full" :class="log.success ? 'bg-green-500' : 'bg-red-500'"></span>
                      {{ log.success ? 'ورود موفق' : 'ورود ناموفق' }}
                    </span>
                    <span class="text-xs text-gray-500">#{{ log.id }}</span>
                  </div>
                  
                  <div class="grid grid-cols-2 gap-3 text-sm">
                    <div>
                      <span class="text-gray-600">زمان ورود:</span>
                      <span class="font-medium text-gray-900 mr-2">{{ formatDateTime(log.login_time) }}</span>
                    </div>
                    <div>
                      <span class="text-gray-600">زمان خروج:</span>
                      <span class="font-medium text-gray-900 mr-2">{{ log.logout_time ? formatDateTime(log.logout_time) : 'هنوز خارج نشده' }}</span>
                    </div>
                    <div>
                      <span class="text-gray-600">IP:</span>
                      <span class="font-mono text-gray-900 mr-2">{{ log.ip_address || '-' }}</span>
                    </div>
                    <div>
                      <span class="text-gray-600">مدت جلسه:</span>
                      <span class="font-medium text-gray-900 mr-2">{{ formatDuration(log.session_duration) }}</span>
                    </div>
                  </div>

                  <div v-if="log.user_agent" class="mt-2 pt-2 border-t border-gray-200">
                    <span class="text-xs text-gray-600">مرورگر: </span>
                    <span class="text-xs text-gray-700">{{ log.user_agent }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Activity Logs -->
        <div v-else-if="activeTab === 'activities'">
          <div v-if="activityLogs.length === 0" class="text-center py-12">
            <svg class="w-12 h-12 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            <p class="text-gray-600">فعالیتی یافت نشد</p>
          </div>

          <div v-else class="space-y-3">
            <div 
              v-for="log in activityLogs" 
              :key="log.id"
              class="border border-gray-200 rounded-lg p-4 hover:bg-gray-50 transition-colors"
            >
              <div class="flex items-start justify-between">
                <div class="flex-1">
                  <div class="flex items-center gap-2 mb-2">
                    <span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-700">
                      {{ translateActionType(log.action_type) }}
                    </span>
                    <span 
                      :class="[
                        'inline-flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium',
                        getStatusClass(log.status)
                      ]"
                    >
                      <span class="w-2 h-2 rounded-full" :class="getStatusDotClass(log.status)"></span>
                      {{ translateStatus(log.status) }}
                    </span>
                    <span class="text-xs text-gray-500">#{{ log.id }}</span>
                  </div>
                  
                  <p class="text-sm text-gray-700 mb-2">{{ log.action_description || 'بدون توضیحات' }}</p>
                  
                  <div class="grid grid-cols-2 gap-3 text-sm">
                    <div>
                      <span class="text-gray-600">زمان:</span>
                      <span class="font-medium text-gray-900 mr-2">{{ formatDateTime(log.created_at) }}</span>
                    </div>
                    <div>
                      <span class="text-gray-600">IP:</span>
                      <span class="font-mono text-gray-900 mr-2">{{ log.ip_address || '-' }}</span>
                    </div>
                  </div>

                  <div v-if="log.resource_type" class="mt-2 text-xs text-gray-600">
                    منبع: {{ log.resource_type }}
                    <span v-if="log.resource_id">#{{ log.resource_id }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="flex justify-end gap-3 p-6 border-t border-gray-200 bg-gray-50">
        <button 
          @click="close"
          type="button"
          class="px-6 py-2 border border-gray-300 rounded-lg hover:bg-gray-100 transition-colors font-medium"
        >
          بستن
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ClientLogsModal',
  props: {
    isOpen: {
      type: Boolean,
      default: false
    },
    clientId: {
      type: Number,
      default: null
    },
    clientInfo: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      activeTab: 'logins',
      loading: false,
      error: '',
      loginLogs: [],
      activityLogs: [],
      totalLogins: 0,
      totalActivities: 0
    }
  },
  computed: {
    apiBaseURL() {
      return process.env.VUE_APP_API_URL || 'https://polychemmb.com'
    }
  },
  watch: {
    isOpen(newVal) {
      if (newVal && this.clientId) {
        this.loadLogs();
      }
    }
  },
  methods: {
    async loadLogs() {
      if (!this.clientId) return;

      this.loading = true;
      this.error = '';

      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          this.error = 'توکن احراز هویت یافت نشد';
          return;
        }

        const response = await fetch(`${this.apiBaseURL}/api/admin/logs/client/${this.clientId}/all?limit=100`, {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });

        if (!response.ok) {
          throw new Error(`خطای سرور: ${response.status}`);
        }

        const data = await response.json();

        if (data.success) {
          this.loginLogs = data.login_logs || [];
          this.activityLogs = data.activity_logs || [];
          this.totalLogins = data.total_logins || 0;
          this.totalActivities = data.total_activities || 0;
        } else {
          this.error = data.message || 'خطا در بارگذاری لاگ‌ها';
        }
      } catch (err) {
        this.error = `خطا در ارتباط با سرور: ${err.message}`;
        console.error('Load logs error:', err);
      } finally {
        this.loading = false;
      }
    },

    close() {
      this.$emit('close');
    },

    formatDateTime(dateString) {
      if (!dateString) return '-';
      try {
        const date = new Date(dateString);
        return date.toLocaleDateString('fa-IR', {
          year: 'numeric',
          month: '2-digit',
          day: '2-digit',
          hour: '2-digit',
          minute: '2-digit'
        });
      } catch {
        return dateString;
      }
    },

    formatDuration(seconds) {
      if (!seconds || seconds === 0) return '-';
      const hours = Math.floor(seconds / 3600);
      const minutes = Math.floor((seconds % 3600) / 60);
      if (hours > 0) {
        return `${hours}س ${minutes}د`;
      }
      return `${minutes}د`;
    },

    translateActionType(type) {
      const translations = {
        'view_pricing': 'مشاهده قیمت',
        'create_order': 'ایجاد سفارش',
        'update_profile': 'بروزرسانی پروفایل',
        'change_password': 'تغییر رمز',
        'create_ticket': 'ایجاد تیکت',
        'view_order': 'مشاهده سفارش',
        'cancel_order': 'لغو سفارش'
      };
      return translations[type] || type;
    },

    translateStatus(status) {
      const translations = {
        'success': 'موفق',
        'failed': 'ناموفق',
        'warning': 'هشدار'
      };
      return translations[status] || status;
    },

    getStatusClass(status) {
      const classes = {
        'success': 'bg-green-100 text-green-700',
        'failed': 'bg-red-100 text-red-700',
        'warning': 'bg-yellow-100 text-yellow-700'
      };
      return classes[status] || 'bg-gray-100 text-gray-700';
    },

    getStatusDotClass(status) {
      const classes = {
        'success': 'bg-green-500',
        'failed': 'bg-red-500',
        'warning': 'bg-yellow-500'
      };
      return classes[status] || 'bg-gray-500';
    }
  }
}
</script>