<template>
  <div class="visitor-dashboard" dir="rtl">
    <!-- Statistics Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-label">بازدید امروز</span>
        <span class="stat-value">{{ stats.today }}</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">بازدید این هفته</span>
        <span class="stat-value">{{ stats.week }}</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">آی‌پی‌های منحصربه‌فرد</span>
        <span class="stat-value">{{ stats.uniqueIps }}</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">کل بازدیدها</span>
        <span class="stat-value">{{ stats.total }}</span>
      </div>
    </div>

    <!-- Filters Section -->
    <div class="filters-section">
      <button @click="resetFilters" class="reset-btn">بازنشانی فیلترها</button>

      <div class="filter-group">
        <select v-model="filters.country" @change="loadVisitors" class="filter-select">
          <option value="">تمام کشورها</option>
          <option v-for="c in countryList" :key="c" :value="c">{{ c }}</option>
        </select>
      </div>

      <div class="filter-group">
        <select v-model="filters.days" @change="loadVisitors" class="filter-select">
          <option value="1">۲۴ ساعت اخیر</option>
          <option value="7">۷ روز اخیر</option>
          <option value="30">۳۰ روز اخیر</option>
          <option value="">همه</option>
        </select>
      </div>

      <div class="filter-group search-group">
        <input
          v-model="filters.search"
          @input="debounceSearch"
          type="text"
          placeholder="جستجو بر اساس آی‌پی یا مسیر..."
          class="filter-select"
        />
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>در حال بارگذاری...</p>
    </div>

    <!-- Empty State -->
    <div v-else-if="visitors.length === 0" class="empty-state">
      <p class="empty-text">هیچ بازدیدی یافت نشد</p>
    </div>

    <!-- Visitors Table -->
    <div v-else class="visitors-table">
      <div class="table-header">
        <div class="header-cell" style="width: 8%"></div>
        <div class="header-cell" style="width: 24%">موقعیت و آی‌پی</div>
        <div class="header-cell" style="width: 20%">سیستم‌عامل و مرورگر</div>
        <div class="header-cell" style="width: 24%">مسیر بازدید شده</div>
        <div class="header-cell" style="width: 24%">آخرین بازدید</div>
      </div>

      <div
        v-for="visitor in visitors"
        :key="visitor.id"
        class="visitor-row"
      >
        <div class="visitor-icon-cell" style="width: 8%">
          <component :is="deviceIcon(visitor.user_agent)" />
        </div>

        <div class="visitor-location-cell" style="width: 24%">
          <div class="location-info">
            <div class="location-text">{{ visitor.country || 'نامشخص' }}</div>
            <div class="ip-text">{{ visitor.ip_address }}</div>
          </div>
        </div>

        <div class="visitor-os-cell" style="width: 20%">
          <div class="os-info">
            <div class="os-text">{{ parseOS(visitor.user_agent) }}</div>
            <div class="browser-text">{{ parseBrowser(visitor.user_agent) }}</div>
          </div>
        </div>

        <div class="visitor-path-cell" style="width: 24%">
          <span class="path-badge">{{ visitor.path }}</span>
        </div>

        <div class="visitor-time-cell" style="width: 24%">
          <div class="time-info">
            <div class="time-relative">{{ formatRelative(visitor.visited_at) }}</div>
            <div class="time-absolute">{{ formatDate(visitor.visited_at) }}</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="pagination.total > 0" class="pagination">
      <button
        @click="previousPage"
        :disabled="pagination.offset === 0"
        class="pagination-btn"
      >
        قبلی
      </button>
      <span class="pagination-info">
        صفحه {{ currentPage }} از {{ totalPages }} (کل: {{ pagination.total }})
      </span>
      <button
        @click="nextPage"
        :disabled="!pagination.has_more"
        class="pagination-btn"
      >
        بعدی
      </button>
    </div>

    <!-- Toast Notification -->
    <transition name="toast">
      <div v-if="toast.show" class="toast" :class="`toast-${toast.type}`">
        {{ toast.message }}
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      API_BASE_URL: 'https://polychemmb.com/api',
      loading: false,

      stats: {
        today: 0,
        week: 0,
        uniqueIps: 0,
        total: 0
      },

      filters: {
        search: '',
        country: '',
        days: '7'
      },

      countryList: [],
      visitors: [],
      pagination: {
        total: 0,
        limit: 20,
        offset: 0,
        has_more: false
      },

      toast: {
        show: false,
        message: '',
        type: 'success'
      },

      searchTimeout: null
    };
  },

  computed: {
    currentPage() {
      return Math.floor(this.pagination.offset / this.pagination.limit) + 1;
    },
    totalPages() {
      return Math.ceil(this.pagination.total / this.pagination.limit) || 1;
    }
  },

  mounted() {
    this.loadStats();
    this.loadVisitors();
  },

  methods: {
    getAuthToken() {
      const token =
        localStorage.getItem('admin_token') ||
        localStorage.getItem('access_token') ||
        localStorage.getItem('token') ||
        localStorage.getItem('auth_token');

      if (!token) {
        console.error('❌ No token found');
        this.showToast('لطفاً وارد شوید', 'error');
        this.$router.push('/admin/login');
        return null;
      }

      return token;
    },

    async apiCall(endpoint, options = {}) {
      const token = this.getAuthToken();
      if (!token) return null;

      const url = `${this.API_BASE_URL}${endpoint}`;

      try {
        const response = await fetch(url, {
          method: options.method || 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
            ...(options.headers || {})
          },
          body: options.body ? JSON.stringify(options.body) : undefined
        });

        if (response.status === 401) {
          localStorage.clear();
          this.showToast('سشن منقضی شده است. لطفاً دوباره وارد شوید', 'error');
          this.$router.push('/admin/login');
          return null;
        }

        if (!response.ok) {
          return null;
        }

        return await response.json();
      } catch (error) {
        console.error('❌ Error:', error);
        this.showToast('خطا در ارتباط با سرور', 'error');
        return null;
      }
    },

    showToast(message, type = 'success') {
      this.toast = { show: true, message, type };
      setTimeout(() => {
        this.toast.show = false;
      }, 3000);
    },

    async loadStats() {
      const data = await this.apiCall('/admin/logs/visitors/stats');
      if (data && data.stats) {
        this.stats = data.stats;
      }
    },

    async loadVisitors() {
      this.loading = true;
      try {
        const params = new URLSearchParams({
          limit: this.pagination.limit,
          offset: this.pagination.offset
        });

        if (this.filters.country) params.append('country', this.filters.country);
        if (this.filters.days) params.append('days', this.filters.days);
        if (this.filters.search) params.append('search', this.filters.search);

        const data = await this.apiCall(`/admin/logs/visitors?${params}`);

        if (data) {
          this.visitors = data.logs || [];
          this.pagination = data.pagination || this.pagination;
          this.countryList = data.countries || this.countryList;
        }
      } finally {
        this.loading = false;
      }
    },

    debounceSearch() {
      clearTimeout(this.searchTimeout);
      this.searchTimeout = setTimeout(() => {
        this.pagination.offset = 0;
        this.loadVisitors();
      }, 500);
    },

    resetFilters() {
      this.filters = { search: '', country: '', days: '7' };
      this.pagination.offset = 0;
      this.loadVisitors();
    },

    nextPage() {
      this.pagination.offset += this.pagination.limit;
      this.loadVisitors();
    },

    previousPage() {
      this.pagination.offset = Math.max(0, this.pagination.offset - this.pagination.limit);
      this.loadVisitors();
    },

    parseOS(ua) {
      if (!ua) return 'نامشخص';
      if (/windows/i.test(ua)) return 'Windows';
      if (/macintosh|mac os/i.test(ua)) return 'macOS';
      if (/android/i.test(ua)) return 'Android';
      if (/iphone|ipad|ios/i.test(ua)) return 'iOS';
      if (/linux/i.test(ua)) return 'Linux';
      return 'نامشخص';
    },

    parseBrowser(ua) {
      if (!ua) return 'نامشخص';
      if (/edg/i.test(ua)) return 'Edge';
      if (/chrome/i.test(ua)) return 'Chrome';
      if (/safari/i.test(ua) && !/chrome/i.test(ua)) return 'Safari';
      if (/firefox/i.test(ua)) return 'Firefox';
      return 'نامشخص';
    },

    deviceIcon(ua) {
      const isMobile = ua && /android|iphone|ipad/i.test(ua);
      return {
        template: isMobile
          ? `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="7" y="2" width="10" height="20" rx="2"/><line x1="11" y1="18" x2="13" y2="18"/></svg>`
          : `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>`
      };
    },

    formatRelative(dateString) {
      if (!dateString) return '-';
      const diffMs = Date.now() - new Date(dateString).getTime();
      const diffMin = Math.floor(diffMs / 60000);
      if (diffMin < 1) return 'همین الان';
      if (diffMin < 60) return `${diffMin} دقیقه پیش`;
      const diffHour = Math.floor(diffMin / 60);
      if (diffHour < 24) return `${diffHour} ساعت پیش`;
      const diffDay = Math.floor(diffHour / 24);
      return `${diffDay} روز پیش`;
    },

    formatDate(dateString) {
      if (!dateString) return '-';
      try {
        return new Date(dateString).toLocaleString('fa-IR');
      } catch {
        return dateString;
      }
    }
  }
};
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/gh/rastikerdar/iran-yekan-font@v3.0.0/dist/font-face.css');

* {
  font-family: 'IRANYekan', sans-serif;
  box-sizing: border-box;
}

.visitor-dashboard {
  background: #f5f7fa;
  min-height: 100vh;
  padding: 2rem;
  color: #1f2430;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
  margin-bottom: 1.75rem;
}

.stat-card {
  background: #ffffff;
  border: 1px solid #e6e8ec;
  padding: 1.5rem;
  border-radius: 14px;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  transition: all 0.25s ease;
  text-align: center;
  box-shadow: 0 1px 3px rgba(16, 24, 40, 0.04);
}

.stat-card:hover {
  border-color: #d3d7de;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(16, 24, 40, 0.08);
}

.stat-label {
  color: #6b7280;
  font-size: 0.85rem;
  font-weight: 500;
}

.stat-value {
  font-size: 2.25rem;
  font-weight: 800;
  color: #111827;
}

/* Filters */
.filters-section {
  background: #ffffff;
  border: 1px solid #e6e8ec;
  padding: 1.25rem 1.5rem;
  border-radius: 14px;
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  align-items: center;
  box-shadow: 0 1px 3px rgba(16, 24, 40, 0.04);
}

.filter-group {
  flex: 0 1 auto;
  min-width: 150px;
}

.search-group {
  flex: 1;
  min-width: 250px;
}

.filter-select {
  width: 100%;
  padding: 0.7rem 1rem;
  border: 1.5px solid #e0e3e8;
  border-radius: 10px;
  font-size: 0.9rem;
  color: #1f2430;
  background: #ffffff;
  font-family: 'IRANYekan', sans-serif;
}

.filter-select:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.12);
}

.filter-select option {
  background: #ffffff;
  color: #1f2430;
}

.reset-btn {
  background: #1f2937;
  color: #ffffff;
  border: 1px solid #1f2937;
  padding: 0.7rem 1.4rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  white-space: nowrap;
  transition: all 0.25s ease;
  font-family: 'IRANYekan', sans-serif;
}

.reset-btn:hover {
  background: #111827;
}

/* Loading & Empty */
.loading-state, .empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  background: #ffffff;
  border: 1px solid #e6e8ec;
  border-radius: 14px;
  min-height: 260px;
}

.spinner {
  width: 36px;
  height: 36px;
  border: 3px solid #e6e8ec;
  border-top-color: #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.empty-text {
  color: #6b7280;
  font-size: 1rem;
}

/* Table */
.visitors-table {
  background: #ffffff;
  border: 1px solid #e6e8ec;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(16, 24, 40, 0.04);
}

.table-header {
  display: flex;
  background: #f9fafb;
  border-bottom: 1px solid #e6e8ec;
  font-weight: 600;
  font-size: 0.82rem;
  color: #6b7280;
}

.header-cell {
  padding: 1.1rem 1.25rem;
}

.visitor-row {
  display: flex;
  border-bottom: 1px solid #f0f1f3;
  transition: background 0.2s ease;
  align-items: center;
}

.visitor-row:last-child {
  border-bottom: none;
}

.visitor-row:hover {
  background: #f9fafb;
}

.visitor-icon-cell {
  padding: 1.1rem 1.25rem;
  display: flex;
  align-items: center;
  color: #9ca3af;
}

.visitor-location-cell,
.visitor-os-cell,
.visitor-path-cell,
.visitor-time-cell {
  padding: 1.1rem 1.25rem;
}

.location-info, .os-info, .time-info {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.location-text {
  font-weight: 600;
  color: #111827;
  font-size: 0.92rem;
}

.ip-text {
  color: #6b7280;
  font-size: 0.82rem;
  direction: ltr;
  text-align: right;
}

.os-text {
  font-weight: 600;
  color: #111827;
  font-size: 0.92rem;
}

.browser-text {
  color: #6b7280;
  font-size: 0.82rem;
}

.path-badge {
  display: inline-block;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  background: #dbeafe;
  color: #1e40af;
  direction: ltr;
}

.time-relative {
  font-weight: 600;
  color: #111827;
  font-size: 0.92rem;
}

.time-absolute {
  color: #6b7280;
  font-size: 0.82rem;
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.5rem;
  margin-top: 1.5rem;
  padding: 1.25rem;
  background: #ffffff;
  border: 1px solid #e6e8ec;
  border-radius: 14px;
}

.pagination-btn {
  padding: 0.55rem 1.2rem;
  background: #ffffff;
  border: 1.5px solid #e0e3e8;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  color: #1f2430;
  transition: all 0.25s ease;
  font-family: 'IRANYekan', sans-serif;
}

.pagination-btn:hover:not(:disabled) {
  border-color: #3b82f6;
  color: #3b82f6;
}

.pagination-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.pagination-info {
  color: #6b7280;
  font-weight: 500;
  min-width: 220px;
  text-align: center;
}

/* Toast */
.toast {
  position: fixed;
  bottom: 2rem;
  left: 2rem;
  padding: 1rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  color: white;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
  animation: slideUp 0.3s ease-out;
  z-index: 2000;
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

.toast-success {
  background: #10b981;
}

.toast-error {
  background: #ef4444;
}

.toast-enter-active, .toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  transform: translateX(-100%);
  opacity: 0;
}

@media (max-width: 1024px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }

  .filters-section {
    flex-direction: column;
  }

  .filter-group, .search-group {
    width: 100%;
  }

  .table-header {
    display: none;
  }

  .visitor-row {
    flex-direction: column;
    align-items: flex-start;
    padding: 1rem 0;
  }

  .visitor-icon-cell,
  .visitor-location-cell,
  .visitor-os-cell,
  .visitor-path-cell,
  .visitor-time-cell {
    width: 100% !important;
    padding: 0.4rem 1.25rem;
  }
}
</style>