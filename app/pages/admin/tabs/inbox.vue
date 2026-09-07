<template>
  <div class="ticket-dashboard" dir="rtl">
    <!-- Statistics Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-label">تیکت‌های باز</span>
        <span class="stat-value">{{ stats.open }}</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">در انتظار پاسخ</span>
        <span class="stat-value">{{ stats.waiting }}</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">تیکت‌های فعال</span>
        <span class="stat-value">{{ stats.active }}</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">تیکت‌های حل شده</span>
        <span class="stat-value">{{ stats.resolved }}</span>
      </div>
    </div>

    <!-- Filters Section -->
    <div class="filters-section">
      <button @click="showResetConfirm = !showResetConfirm" class="reset-btn">بازنشانی فیلترها</button>
      
      <div class="filter-group">
        <select v-model="filters.status" @change="loadTickets" class="filter-select">
          <option value="">تمام وضعیت‌ها</option>
          <option value="open">باز</option>
          <option value="awaiting">در انتظار</option>
          <option value="inprogress">در حال انجام</option>
          <option value="closed">بسته</option>
          <option value="resolved">حل شده</option>
        </select>
      </div>
      
      <div class="filter-group">
        <select v-model="filters.priority" @change="loadTickets" class="filter-select">
          <option value="">تمام اولویت‌ها</option>
          <option value="critical">بحرانی</option>
          <option value="high">بالا</option>
          <option value="medium">متوسط</option>
          <option value="low">پایین</option>
        </select>
      </div>
      
      <div class="filter-group">
        <select v-model="filters.category" @change="loadTickets" class="filter-select">
          <option value="">تمام دسته‌بندی‌ها</option>
          <option value="financial">مالی</option>
          <option value="technical">فنی</option>
          <option value="billing">صورتحساب</option>
          <option value="order">سفارش</option>
          <option value="product">محصول</option>
          <option value="other">سایر</option>
        </select>
      </div>
      
      <div class="filter-group search-group">
        <input 
          v-model="filters.search" 
          @input="debounceSearch"
          type="text" 
          placeholder="جستجو در تیکت‌ها..."
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
    <div v-else-if="tickets.length === 0" class="empty-state">
      <p class="empty-text">هیچ تیکتی یافت نشد</p>
    </div>

    <!-- Tickets Table -->
    <div v-else class="tickets-table">
      <div class="table-header">
        <div class="header-cell" style="width: 35%">عنوان</div>
        <div class="header-cell" style="width: 15%">دسته‌بندی</div>
        <div class="header-cell" style="width: 12%">وضعیت</div>
        <div class="header-cell" style="width: 12%">اولویت</div>
        <div class="header-cell" style="width: 16%">بروزرسانی</div>
        <div class="header-cell" style="width: 10%; text-align: center">عملیات</div>
      </div>

      <div 
        v-for="ticket in tickets" 
        :key="ticket.id"
        class="ticket-row"
      >
        <div class="ticket-title-cell" style="width: 35%">
          <div class="ticket-info">
            <div class="ticket-title">{{ ticket.title }}</div>
            <div class="ticket-number">#{{ ticket.ticket_number }}</div>
            <div class="ticket-client">{{ ticket.client_first_name }} {{ ticket.client_last_name }}</div>
          </div>
        </div>

        <div class="ticket-category" style="width: 15%">
          <span class="category-text">{{ getCategoryLabel(ticket.category) }}</span>
        </div>

        <div class="ticket-status" style="width: 12%">
          <span :class="`status-${ticket.status}`" class="status-badge">
            {{ getStatusLabel(ticket.status) }}
          </span>
        </div>

        <div class="ticket-priority" style="width: 12%">
          <span :class="`priority-${ticket.priority}`" class="priority-badge">
            {{ getPriorityLabel(ticket.priority) }}
          </span>
        </div>

        <div class="ticket-updated" style="width: 16%">
          {{ formatDate(ticket.updated_at) }}
        </div>

        <div class="ticket-actions" style="width: 10%; text-align: center">
          <button @click="openTicketModal(ticket.id)" class="action-link">مشاهده</button>
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

    <!-- Ticket Detail Modal -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <!-- Modal Header -->
        <div class="modal-header">
          <div>
            <h2>جزئیات تیکت #{{ selectedTicket?.ticket_number }}</h2>
            <p class="modal-subtitle">{{ selectedTicket?.title }}</p>
          </div>
          <button @click="closeModal" class="close-btn">X</button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">
          <!-- Ticket Info -->
          <div class="info-grid">
            <div class="info-item">
              <span class="label">مشتری:</span>
              <span class="value">{{ selectedTicket?.client_first_name }} {{ selectedTicket?.client_last_name }}</span>
            </div>
            <div class="info-item">
              <span class="label">دسته‌بندی:</span>
              <span class="value">{{ getCategoryLabel(selectedTicket?.category) }}</span>
            </div>
            <div class="info-item">
              <span class="label">وضعیت:</span>
              <span :class="`status-${selectedTicket?.status}`" class="status-badge">
                {{ getStatusLabel(selectedTicket?.status) }}
              </span>
            </div>
            <div class="info-item">
              <span class="label">اولویت:</span>
              <span :class="`priority-${selectedTicket?.priority}`" class="priority-badge">
                {{ getPriorityLabel(selectedTicket?.priority) }}
              </span>
            </div>
            <div class="info-item">
              <span class="label">ایجاد شده:</span>
              <span class="value">{{ formatDate(selectedTicket?.created_at) }}</span>
            </div>
            <div class="info-item">
              <span class="label">آخرین بروزرسانی:</span>
              <span class="value">{{ formatDate(selectedTicket?.updated_at) }}</span>
            </div>
          </div>

          <!-- Messages -->
          <div class="messages-section">
            <h3>پیام‌های تیکت ({{ selectedTicket?.messages?.length || 0 }})</h3>
            <div class="messages-list">
              <div 
                v-for="msg in selectedTicket?.messages" 
                :key="msg.id"
                class="message-item"
                :class="msg.sender_type === 'admin' ? 'message-admin' : 'message-client'"
              >
                <div class="message-header">
                  <span class="sender-badge">{{ msg.sender_type === 'admin' ? 'پشتیبان' : 'مشتری' }}</span>
                  <span class="time">{{ formatDate(msg.created_at) }}</span>
                </div>
                <div class="message-text">{{ msg.message }}</div>
              </div>
            </div>
          </div>

          <!-- Reply Section -->
          <div class="reply-section">
            <h3>ارسال پاسخ</h3>
            <textarea 
              v-model="replyMessage"
              class="reply-textarea"
              placeholder="پاسخ خود را بنویسید..."
              rows="4"
            ></textarea>
            <button @click="sendReply" :disabled="!replyMessage.trim() || sendingReply" class="send-btn">
              {{ sendingReply ? 'در حال ارسال...' : 'ارسال پاسخ' }}
            </button>
          </div>

          <!-- Status Change Section -->
          <div class="status-section">
            <h3>تغییر وضعیت</h3>
            <div class="status-controls">
              <select v-model="newStatus" class="status-select">
                <option value="">انتخاب وضعیت جدید</option>
                <option value="open">باز</option>
                <option value="awaiting">در انتظار</option>
                <option value="inprogress">در حال انجام</option>
                <option value="closed">بسته</option>
                <option value="resolved">حل شده</option>
              </select>
              <button @click="updateStatus" :disabled="!newStatus || updatingStatus" class="update-btn">
                {{ updatingStatus ? 'در حال آپدیت...' : 'تغییر وضعیت' }}
              </button>
            </div>
          </div>
        </div>

        <!-- Modal Footer -->
        <div class="modal-footer">
          <button @click="closeModal" class="close-modal-btn">بستن</button>
        </div>
      </div>
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
      sendingReply: false,
      updatingStatus: false,
      showModal: false,
      showResetConfirm: false,
      selectedTicket: null,
      replyMessage: '',
      newStatus: '',
      
      stats: {
        open: 0,
        waiting: 0,
        active: 0,
        resolved: 0
      },
      
      filters: {
        search: '',
        status: '',
        priority: '',
        category: ''
      },
      
      tickets: [],
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
      return Math.ceil(this.pagination.total / this.pagination.limit);
    }
  },

  mounted() {
    console.log('🚀 TicketDashboard Mounted');
    this.loadStats();
    this.loadTickets();
  },

  methods: {
    /**
     * ✅ Token دریافت کریں
     */
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

    /**
     * ✅ API Call کریں
     */
    async apiCall(endpoint, options = {}) {
      const token = this.getAuthToken();
      if (!token) return null;

      const url = `${this.API_BASE_URL}${endpoint}`;
      
      try {
        console.log(`📡 ${options.method || 'GET'} ${url}`);

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
          console.error('❌ 401 Unauthorized');
          localStorage.clear();
          this.showToast('سشن منقضی شده است. لطفاً دوباره وارد شوید', 'error');
          this.$router.push('/admin/login');
          return null;
        }

        if (!response.ok) {
          console.error(`❌ ${response.status}`);
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
      console.log('📊 Loading stats...');
      const data = await this.apiCall('/admin/tickets/stats');
      
      if (data) {
        console.log('📦 Stats response:', data);
        
        if (data.stats) {
          this.stats = data.stats;
          console.log('✅ Stats loaded:', this.stats);
        } else if (data.success === false) {
          console.error('❌ Stats error:', data.message);
          this.showToast('خطا در بارگذاری آمار: ' + data.message, 'error');
        }
      } else {
        console.error('❌ No response from stats endpoint');
      }
    },

    async loadTickets() {
      this.loading = true;
      try {
        const params = new URLSearchParams({
          limit: this.pagination.limit,
          offset: this.pagination.offset
        });

        if (this.filters.status) params.append('status', this.filters.status);
        if (this.filters.priority) params.append('priority', this.filters.priority);
        if (this.filters.category) params.append('category', this.filters.category);
        if (this.filters.search) params.append('search', this.filters.search);

        const data = await this.apiCall(`/admin/tickets?${params}`);
        
        if (data) {
          this.tickets = data.tickets || [];
          this.pagination = data.pagination || {};
          console.log(`✅ Loaded ${this.tickets.length} tickets`);
        }
      } finally {
        this.loading = false;
      }
    },

    async openTicketModal(ticketId) {
      this.loading = true;
      try {
        const data = await this.apiCall(`/admin/tickets/${ticketId}`);
        if (data && data.ticket) {
          this.selectedTicket = data.ticket;
          this.showModal = true;
          this.replyMessage = '';
          this.newStatus = '';
          console.log('✅ Ticket loaded:', this.selectedTicket);
        }
      } finally {
        this.loading = false;
      }
    },

    async sendReply() {
      if (!this.replyMessage.trim()) {
        this.showToast('پیام خالی است', 'error');
        return;
      }

      this.sendingReply = true;
      try {
        const data = await this.apiCall(`/admin/tickets/${this.selectedTicket.id}/messages`, {
          method: 'POST',
          body: { message: this.replyMessage }
        });

        if (data && data.success) {
          this.showToast('پیام ارسال شد', 'success');
          this.replyMessage = '';
          await this.openTicketModal(this.selectedTicket.id);
          await this.loadStats();
        }
      } finally {
        this.sendingReply = false;
      }
    },

    async updateStatus() {
      if (!this.newStatus) {
        this.showToast('وضعیت را انتخاب کنید', 'error');
        return;
      }

      this.updatingStatus = true;
      try {
        const data = await this.apiCall(`/admin/tickets/${this.selectedTicket.id}/status`, {
          method: 'PUT',
          body: { status: this.newStatus }
        });

        if (data && data.success) {
          this.showToast('وضعیت تغییر کرد', 'success');
          this.newStatus = '';
          await this.openTicketModal(this.selectedTicket.id);
          await this.loadStats();
          await this.loadTickets();
        }
      } finally {
        this.updatingStatus = false;
      }
    },

    closeModal() {
      this.showModal = false;
      this.selectedTicket = null;
      this.replyMessage = '';
      this.newStatus = '';
    },

    debounceSearch() {
      clearTimeout(this.searchTimeout);
      this.searchTimeout = setTimeout(() => {
        this.pagination.offset = 0;
        this.loadTickets();
      }, 500);
    },

    resetFilters() {
      this.filters = { search: '', status: '', priority: '', category: '' };
      this.pagination.offset = 0;
      this.loadTickets();
    },

    nextPage() {
      this.pagination.offset += this.pagination.limit;
      this.loadTickets();
    },

    previousPage() {
      this.pagination.offset = Math.max(0, this.pagination.offset - this.pagination.limit);
      this.loadTickets();
    },

    getStatusLabel(status) {
      const labels = {
        open: 'باز',
        awaiting: 'در انتظار',
        inprogress: 'در حال انجام',
        closed: 'بسته',
        resolved: 'حل شده'
      };
      return labels[status] || status;
    },

    getPriorityLabel(priority) {
      const labels = {
        low: 'پایین',
        medium: 'متوسط',
        high: 'بالا',
        critical: 'بحرانی'
      };
      return labels[priority] || priority;
    },

    getCategoryLabel(category) {
      const labels = {
        financial: 'مالی',
        technical: 'فنی',
        billing: 'صورتحساب',
        order: 'سفارش',
        product: 'محصول',
        other: 'سایر'
      };
      return labels[category] || category;
    },

    formatDate(dateString) {
      if (!dateString) return '-';
      try {
        return new Date(dateString).toLocaleDateString('fa-IR');
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
}

.ticket-dashboard {
  background: #f5f7fa;
  min-height: 100vh;
  padding: 2rem;
  dir: rtl;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  transition: all 0.3s ease;
  text-align: center;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
}

.stat-label {
  color: #6b7280;
  font-size: 0.9rem;
  font-weight: 500;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1f2937;
}

/* Filters */
.filters-section {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  flex-wrap: wrap;
  align-items: center;
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
  padding: 0.75rem 1rem;
  border: 1.5px solid #e5e7eb;
  border-radius: 8px;
  font-size: 0.9rem;
  color: #374151;
  font-family: 'IRANYekan', sans-serif;
}

.filter-select:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.reset-btn {
  background: #1f2937;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  white-space: nowrap;
  transition: all 0.3s ease;
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
  background: white;
  border-radius: 12px;
  min-height: 300px;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e5e7eb;
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
.tickets-table {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.table-header {
  display: grid;
  grid-template-columns: 35% 15% 12% 12% 16% 10%;
  gap: 0;
  padding: 0;
  background: #f9fafb;
  border-bottom: 2px solid #e5e7eb;
  font-weight: 600;
  font-size: 0.85rem;
  color: #6b7280;
}

.header-cell {
  padding: 1.25rem 1.5rem;
  border-right: 1px solid #e5e7eb;
}

.header-cell:last-child {
  border-right: none;
}

.ticket-row {
  display: grid;
  grid-template-columns: 35% 15% 12% 12% 16% 10%;
  gap: 0;
  padding: 0;
  border-bottom: 1px solid #f3f4f6;
  transition: all 0.3s ease;
}

.ticket-row:hover {
  background: #f9fafb;
}

.ticket-title-cell {
  padding: 1.25rem 1.5rem;
  border-right: 1px solid #f3f4f6;
  display: flex;
  align-items: center;
}

.ticket-info {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.ticket-title {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.95rem;
}

.ticket-number {
  color: #9ca3af;
  font-size: 0.8rem;
  font-weight: 500;
}

.ticket-client {
  color: #6b7280;
  font-size: 0.85rem;
}

.ticket-category {
  padding: 1.25rem 1.5rem;
  border-right: 1px solid #f3f4f6;
  display: flex;
  align-items: center;
  text-align: right;
}

.category-text {
  color: #374151;
  font-size: 0.9rem;
  font-weight: 500;
}

.ticket-status {
  padding: 1.25rem 1.5rem;
  border-right: 1px solid #f3f4f6;
  display: flex;
  align-items: center;
}

.ticket-priority {
  padding: 1.25rem 1.5rem;
  border-right: 1px solid #f3f4f6;
  display: flex;
  align-items: center;
}

.status-badge {
  display: inline-block;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  white-space: nowrap;
}

.status-open {
  background: #fee2e2;
  color: #991b1b;
}

.status-awaiting {
  background: #fef3c7;
  color: #92400e;
}

.status-inprogress {
  background: #dbeafe;
  color: #1e40af;
}

.status-resolved,
.status-closed {
  background: #d1fae5;
  color: #065f46;
}

.priority-badge {
  display: inline-block;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  white-space: nowrap;
}

.priority-critical {
  background: #fee2e2;
  color: #991b1b;
}

.priority-high {
  background: #fef3c7;
  color: #92400e;
}

.priority-medium {
  background: #fef3c7;
  color: #92400e;
}

.priority-low {
  background: #d1fae5;
  color: #065f46;
}

.ticket-updated {
  padding: 1.25rem 1.5rem;
  border-right: 1px solid #f3f4f6;
  display: flex;
  align-items: center;
  color: #6b7280;
  font-size: 0.9rem;
  text-align: right;
}

.ticket-actions {
  padding: 1.25rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.action-link {
  background: none;
  border: none;
  color: #3b82f6;
  cursor: pointer;
  font-weight: 600;
  text-decoration: underline;
  transition: color 0.3s ease;
}

.action-link:hover {
  color: #1e40af;
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.5rem;
  margin-top: 2rem;
  padding: 1.5rem;
  background: white;
  border-radius: 12px;
}

.pagination-btn {
  padding: 0.6rem 1.2rem;
  background: white;
  border: 1.5px solid #e5e7eb;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  font-family: 'IRANYekan', sans-serif;
}

.pagination-btn:hover:not(:disabled) {
  border-color: #3b82f6;
  color: #3b82f6;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-info {
  color: #6b7280;
  font-weight: 500;
  min-width: 250px;
  text-align: center;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 16px;
  width: 100%;
  max-width: 700px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction: column;
}

.modal-header {
  padding: 2rem;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.modal-header h2 {
  margin: 0 0 0.5rem 0;
  font-size: 1.5rem;
  color: #1f2937;
}

.modal-subtitle {
  color: #6b7280;
  margin: 0;
  font-size: 0.95rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #6b7280;
  padding: 0;
  font-family: 'IRANYekan', sans-serif;
}

.modal-body {
  padding: 2rem;
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  padding: 1.5rem;
  background: #f9fafb;
  border-radius: 10px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.info-item .label {
  font-size: 0.85rem;
  color: #6b7280;
  font-weight: 600;
}

.info-item .value {
  font-size: 0.95rem;
  color: #1f2937;
  font-weight: 500;
}

/* Messages */
.messages-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.messages-section h3 {
  margin: 0;
  color: #1f2937;
  font-size: 1rem;
}

.messages-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 300px;
  overflow-y: auto;
}

.message-item {
  padding: 1rem;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.message-admin {
  background: #dbeafe;
  border-right: 4px solid #3b82f6;
}

.message-client {
  background: #f3f4f6;
  border-right: 4px solid #6b7280;
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
}

.sender-badge {
  font-weight: 600;
  color: #1f2937;
}

.time {
  color: #6b7280;
}

.message-text {
  color: #1f2937;
  font-size: 0.95rem;
  line-height: 1.6;
}

/* Reply Section */
.reply-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.reply-section h3 {
  margin: 0;
  color: #1f2937;
  font-size: 1rem;
}

.reply-textarea {
  padding: 1rem;
  border: 1.5px solid #e5e7eb;
  border-radius: 10px;
  font-family: 'IRANYekan', sans-serif;
  font-size: 0.95rem;
  color: #1f2937;
  resize: vertical;
}

.reply-textarea:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.send-btn {
  padding: 0.75rem 1.5rem;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  font-family: 'IRANYekan', sans-serif;
}

.send-btn:hover:not(:disabled) {
  background: #2563eb;
}

.send-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Status Section */
.status-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1.5rem;
  background: #f0fdf4;
  border-radius: 10px;
  border-right: 4px solid #10b981;
}

.status-section h3 {
  margin: 0;
  color: #1f2937;
  font-size: 1rem;
}

.status-controls {
  display: flex;
  gap: 1rem;
}

.status-select {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1.5px solid #d1d5db;
  border-radius: 8px;
  font-family: 'IRANYekan', sans-serif;
  font-size: 0.95rem;
}

.status-select:focus {
  outline: none;
  border-color: #10b981;
}

.update-btn {
  padding: 0.75rem 1.5rem;
  background: #10b981;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  white-space: nowrap;
  transition: all 0.3s ease;
  font-family: 'IRANYekan', sans-serif;
}

.update-btn:hover:not(:disabled) {
  background: #059669;
}

.update-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.modal-footer {
  padding: 1.5rem 2rem;
  border-top: 1px solid #e5e7eb;
}

.close-modal-btn {
  width: 100%;
  padding: 0.75rem 1.5rem;
  background: #f3f4f6;
  border: 1.5px solid #e5e7eb;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  font-family: 'IRANYekan', sans-serif;
}

.close-modal-btn:hover {
  background: #e5e7eb;
}

/* Toast */
.toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  color: white;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
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
  transform: translateX(100%);
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

  .table-header,
  .ticket-row {
    grid-template-columns: 1fr;
    gap: 0;
  }

  .header-cell,
  .ticket-title-cell,
  .ticket-category,
  .ticket-status,
  .ticket-priority,
  .ticket-updated,
  .ticket-actions {
    border-right: none;
    padding: 1rem;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }

  .status-controls {
    flex-direction: column;
  }
}
</style>