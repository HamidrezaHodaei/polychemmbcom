<template>
<div class="flex h-full font-[IRANYekan]" dir="rtl">
    <!-- Main Content -->
    <div class="flex-1 flex flex-col p-8 overflow-y-auto custom-scrollbar">
      <!-- Main Form Container -->
      <div class="flex gap-8 flex-1">
        <!-- Left Section - Form -->
        <div class="flex-1 space-y-6">
          <!-- Category Section -->
          <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border border-white/40">
            <label class="text-sm font-bold text-gray-900 mb-4 block">
              دسته‌بندی / بخش <span class="text-red-500">*</span>
            </label>
            <div class="grid grid-cols-3 gap-4">
              <button 
                v-for="category in categories"
                :key="category.value"
                @click="ticketData.category = category.value"
                :class="[
                  'py-4 px-4 rounded-2xl font-bold text-sm transition-all duration-300 border-2',
                  ticketData.category === category.value
                    ? 'bg-yellow-400 text-gray-900 border-yellow-500 shadow-lg scale-105'
                    : 'bg-white/40 text-gray-700 border-transparent hover:bg-white/60'
                ]"
              >
                {{ category.label }}
              </button>
            </div>
          </div>

          <!-- Ticket Details Section -->
          <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border border-white/40 relative z-10">
            <h3 class="text-lg font-bold text-gray-900 mb-6">جزئیات درخواست</h3>
            <div class="space-y-5">
              <!-- Ticket Title -->
              <div>
                <label class="text-sm font-semibold text-gray-700 block mb-2">
                  عنوان درخواست <span class="text-red-500">*</span>
                </label>
                <input 
                  v-model="ticketData.title"
                  type="text" 
                  placeholder="مثال: مشکل در اتصال سیستم"
                  class="w-full px-4 py-3 rounded-xl bg-white/50 border border-white/40 text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all"
                />
              </div>

              <!-- Priority -->
              <div>
                <label class="text-sm font-semibold text-gray-700 block mb-2">
                  اولویت <span class="text-red-500">*</span>
                </label>
                <div class="relative z-[100]" ref="prioritySelectRef">
                  <div
                    @click="togglePriorityDropdown"
                    class="w-full px-4 py-3 rounded-xl border border-white/30 focus:border-white/50 text-base font-medium bg-white/10 backdrop-blur-md text-gray-900 hover:bg-white/20 cursor-pointer transition-all shadow-xl flex items-center justify-between"
                    :class="{ 'border-white/50': isPriorityOpen }">
                    <span>{{ priorityOptions.find(p => p.value === ticketData.priority)?.label || 'انتخاب کنید' }}</span>
                    <svg 
                      class="w-5 h-5 text-gray-600 transition-transform duration-200"
                      :class="{ 'rotate-180': isPriorityOpen }"
                      fill="none" 
                      stroke="currentColor" 
                      viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  </div>

                  <Transition
                    enter-active-class="transition ease-out duration-200"
                    enter-from-class="opacity-0 translate-y-1"
                    enter-to-class="opacity-100 translate-y-0"
                    leave-active-class="transition ease-in duration-150"
                    leave-from-class="opacity-100 translate-y-0"
                    leave-to-class="opacity-0 translate-y-1">
                    <div
                      v-show="isPriorityOpen"
                      class="absolute z-[100] w-full mt-2 bg-gray-700/95 backdrop-blur-md rounded-xl shadow-2xl border border-white/20 overflow-hidden">
                      <div
                        v-for="option in priorityOptions"
                        :key="option.value"
                        @click="selectPriority(option.value)"
                        class="px-4 py-3 text-white cursor-pointer transition-all duration-200 hover:bg-yellow-500 hover:text-black flex items-center gap-2"
                        :class="{ 'bg-yellow-500/20': ticketData.priority === option.value }">
                        <span :class="`priority-indicator priority-${option.value}`"></span>
                        {{ option.label }}
                      </div>
                    </div>
                  </Transition>
                </div>
              </div>
            </div>
          </div>

          <!-- Message Section -->
          <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border border-white/40 relative z-0">
            <label class="text-sm font-bold text-gray-900 mb-4 block">
              پیام <span class="text-red-500">*</span>
            </label>
            <div class="bg-white/40 rounded-2xl border border-white/40 overflow-hidden flex flex-col">
              <textarea 
                v-model="ticketData.message"
                placeholder="در اینجا توضیحات درخواست خود را بنویسید..."
                rows="8"
                class="w-full px-4 py-4 bg-transparent text-gray-900 placeholder-gray-500 focus:outline-none resize-none"
              ></textarea>
              <div class="border-t border-white/40 p-3 bg-white/10 flex justify-end">
                <button 
                  @click="submitTicket" 
                  :disabled="isSubmitting"
                  class="px-6 py-2 bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-bold rounded-lg transition-all flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <svg v-if="!isSubmitting" class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                  </svg>
                  <div v-else class="spinner-small"></div>
                  <span v-if="isSubmitting">در حال ارسال...</span>
                  <span v-else">ارسال تیکت</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Section - Upload & Info -->
        <div class="flex-1 space-y-6 flex flex-col">
          <!-- Upload Area -->
          <div 
            @dragover.prevent="isDragging = true"
            @dragleave.prevent="isDragging = false"
            @drop.prevent="handleDrop"
            :class="[
              'bg-white/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border-2 border-dashed transition-all duration-300 relative z-0',
              isDragging 
                ? 'border-yellow-400 bg-yellow-50/40' 
                : 'border-white/40 hover:border-yellow-300'
            ]"
          >
            <div class="text-center">
              <div class="w-16 h-16 bg-yellow-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10" />
                </svg>
              </div>
              <p class="text-sm font-bold text-gray-900 mb-1">فایل‌ها را اینجا بکشید</p>
              <p class="text-xs text-gray-600 mb-3">یا برای انتخاب فایل کلیک کنید</p>
              <p class="text-xs text-gray-500">فرمت‌های مجاز: PDF, JPG, PNG, DOC - حداکثر 10 مگابایت</p>
              <input 
                type="file" 
                @change="handleFileSelect" 
                class="hidden" 
                ref="fileInput"
                multiple 
                accept=".pdf,.jpg,.jpeg,.png,.doc,.docx" 
              />
              <button @click="$refs.fileInput.click()" class="mt-3 px-4 py-2 bg-yellow-400 text-gray-900 rounded-lg font-semibold hover:bg-yellow-500 transition-all">
                انتخاب فایل
              </button>
            </div>
          </div>

          <!-- Uploaded Files -->
          <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl border border-white/40 relative z-0 flex-1">
            <h3 class="text-sm font-bold text-gray-900 mb-4">فایل‌های انتخاب شده</h3>
            <div class="space-y-3">
              <div v-for="(file, idx) in uploadedFiles" :key="idx" class="flex items-center justify-between p-3 bg-white/40 rounded-xl hover:bg-white/60 transition-colors">
                <div class="flex items-center gap-3 flex-1 min-w-0">
                  <div class="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <svg class="w-5 h-5 text-red-600" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <div class="min-w-0 flex-1">
                    <p class="text-xs font-semibold text-gray-900 truncate">{{ file.name }}</p>
                    <p class="text-xs text-gray-600">{{ formatFileSize(file.size) }}</p>
                  </div>
                </div>
                <button @click="removeFile(idx)" class="text-red-500 hover:text-red-700 transition-colors ml-2">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                  </svg>
                </button>
              </div>
              <div v-if="uploadedFiles.length === 0" class="text-center py-8">
                <p class="text-xs text-gray-500">هیچ فایلی انتخاب نشده است</p>
              </div>
            </div>
          </div>

          <!-- Quick Support Card -->
          <div class="bg-gradient-to-br from-yellow-400 to-yellow-300 rounded-3xl p-6 shadow-2xl text-gray-900 border border-yellow-300 relative z-0">
            <div class="flex items-start gap-3 mb-1">
              <div class="w-12 h-12 bg-white/60 backdrop-blur-xl rounded-full flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
              </div>
              <div>
                <h4 class="text-base font-bold mb-1">پشتیبانی فوری</h4>
                <p class="text-xs opacity-90">تیم ما ۲۴/۷ آماده کمک است</p>
              </div>
            </div>
            <button 
              @click="callSupport"
              class="w-full bg-white text-yellow-600 font-bold py-2 rounded-2xl hover:bg-white/90 transition-colors text-sm mt-4 flex items-center justify-center gap-2"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              تماس با تیم پشتیبانی
            </button>
          </div>
        </div>
      </div>

      <!-- Divider -->
      <div class="my-8 border-t-2 border-white/40"></div>

      <!-- My Tickets Section -  FIX: Proper scrolling container -->
      <div class="mt-8 mb-8 flex flex-col max-h-[700px]">
        <h2 class="text-2xl font-bold text-gray-900 mb-6 flex-shrink-0">درخواست‌های شما</h2>

        <!-- Loading State -->
        <div v-if="loadingTickets" class="flex items-center justify-center py-12">
          <div class="spinner"></div>
        </div>

        <!-- Empty State -->
        <div v-else-if="myTickets.length === 0" class="bg-white/60 backdrop-blur-xl rounded-3xl p-12 shadow-lg border border-white/40 text-center">
          <svg class="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <p class="text-gray-600 text-lg font-semibold">درخواستی موجود نیست</p>
          <p class="text-gray-500 mt-2">فعلاً درخواستی ثبت نکرده‌اید</p>
        </div>

        <!--  FIX: Tickets Grid - separate scrolling from ticket details -->
        <div v-else class="flex-1 overflow-y-auto custom-scrollbar pr-2">
          <div class="space-y-4 pb-4">
            <div 
              v-for="ticket in myTickets"
              :key="ticket.id"
              class="bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-lg border border-white/40 hover:border-yellow-300 hover:shadow-xl transition-all"
            >
            <!-- Ticket Header -->
            <div class="flex items-start justify-between mb-4">
              <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                  <h3 class="text-lg font-bold text-gray-900">{{ ticket.title }}</h3>
                  <span class="text-sm text-gray-500">#{{ ticket.ticket_number }}</span>
                </div>
                <p class="text-sm text-gray-600">{{ getCategoryLabel(ticket.category) }}</p>
              </div>
              <div class="flex items-center gap-3">
                <span :class="getStatusBadgeClass(ticket.status)" class="px-3 py-1 rounded-full text-xs font-semibold">
                  {{ getStatusLabel(ticket.status) }}
                </span>
                <span :class="getPriorityBadgeClass(ticket.priority)" class="px-3 py-1 rounded-full text-xs font-semibold">
                  {{ getPriorityLabel(ticket.priority) }}
                </span>
              </div>
            </div>

            <!-- Ticket Meta -->
            <div class="flex items-center justify-between text-sm text-gray-600 mb-4">
              <span>{{ formatDate(ticket.created_at) }}</span>
              <span>{{ ticket.message_count || 0 }} پیام</span>
            </div>

            <!-- Expandable Detail -->
            <transition
              enter-active-class="transition duration-200 ease-out"
              enter-from-class="opacity-0 -translate-y-2"
              enter-to-class="opacity-100 translate-y-0"
              leave-active-class="transition duration-150 ease-in"
              leave-from-class="opacity-100 translate-y-0"
              leave-to-class="opacity-0 -translate-y-2">
              <div v-if="expandedTicketId === ticket.id" class="mt-6 pt-6 border-t border-white/40 space-y-4" @click.stop>
                <!-- Original Message -->
                <div class="bg-gray-50 rounded-xl p-4">
                  <p class="text-xs font-semibold text-gray-700 mb-2">پیام اصلی:</p>
                  <p class="text-gray-900 text-sm leading-relaxed">{{ ticket.message }}</p>
                </div>

                <!--  FIX: Messages with proper display of admin messages -->
                <div class="space-y-3">
                  <p class="text-xs font-semibold text-gray-700">تبادل پیام‌ها ({{ (ticket.messages || []).length }}):</p>
                  <div v-if="ticket.messages && ticket.messages.length > 0" class="space-y-3 max-h-96 overflow-y-auto rounded-lg bg-white/30 p-3 custom-scrollbar">
                    <div 
                      v-for="msg in ticket.messages"
                      :key="msg.id"
                      :class="msg.sender_type === 'admin' ? 'bg-blue-50 border-r-4 border-blue-400' : 'bg-gray-50'"
                      class="p-3 rounded-lg transition-all hover:shadow-md"
                    >
                      <div class="flex items-center gap-2 mb-2">
                        <div v-if="msg.sender_type === 'admin'" class="w-8 h-8 rounded-full bg-[#848484] flex items-center justify-center flex-shrink-0">
                          <img src="/english logo W1.png" alt="Support" class="w-7 h-7 object-contain" />
                        </div>
                        <div v-else class="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center flex-shrink-0">
                          <svg class="w-4 h-4 text-gray-600" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
                          </svg>
                        </div>
                        <div class="flex-1 flex items-center justify-between">
                          <p class="text-xs font-bold" :class="msg.sender_type === 'admin' ? 'text-blue-700' : 'text-gray-700'">
                            {{ msg.sender_type === 'admin' ? 'پشتیبانی' : 'شما' }}
                          </p>
                          <p class="text-xs text-gray-500">{{ formatDate(msg.created_at) }}</p>
                        </div>
                      </div>
                      <p class="text-sm text-gray-900 mr-10">{{ msg.message }}</p>
                    </div>
                  </div>
                  <div v-else class="text-center py-4 text-gray-500 text-sm">
                    هیچ پیامی وجود ندارد
                  </div>
                </div>

                <!-- Reply Section -->
                <div v-if="ticket.status !== 'resolved' && ticket.status !== 'closed'" class="bg-yellow-50 rounded-xl p-4">
                  <p class="text-xs font-semibold text-gray-700 mb-2">ارسال پیام:</p>
                  <textarea 
                    v-model="replyMessages[ticket.id]"
                    placeholder="پاسخ خود را بنویسید..."
                    rows="3"
                    class="w-full px-3 py-2 rounded-lg bg-white border border-yellow-200 text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-yellow-400 resize-none"
                  ></textarea>
                  <button 
                    @click="sendReply(ticket.id)"
                    :disabled="!replyMessages[ticket.id]?.trim() || sendingReplyId === ticket.id"
                    class="mt-2 w-full px-4 py-2 bg-yellow-400 hover:bg-yellow-500 disabled:opacity-50 text-gray-900 rounded-lg font-semibold text-sm transition-all"
                  >
                    {{ sendingReplyId === ticket.id ? 'در حال ارسال...' : 'ارسال پیام' }}
                  </button>
                </div>

                <!-- Status Message -->
                <div v-if="ticket.status === 'resolved'" class="bg-green-50 rounded-xl p-4 text-center">
                  <p class="text-green-800 font-semibold text-sm"> این درخواست حل شده است</p>
                </div>
              </div>
            </transition>

            <!-- Expand Icon -->
            <div @click="toggleTicketDetail(ticket)" class="flex justify-center mt-4 cursor-pointer hover:bg-gray-100/50 py-2 rounded-xl transition-colors">
              <svg 
                :class="expandedTicketId === ticket.id ? 'rotate-180' : ''"
                class="w-5 h-5 text-gray-400 transition-transform duration-200" 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
              </svg>
            </div>
            </div>
          </div>
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
  name: 'CreateTicketPage',
  data() {
    return {
      isDragging: false,
      isPriorityOpen: false,
      isSubmitting: false,
      loadingTickets: false,
      expandedTicketId: null,
      sendingReplyId: null,
      
      ticketData: {
        title: '',
        category: '',
        priority: 'medium',
        message: ''
      },
      
      categories: [
        { label: 'مالی', value: 'financial' },
        { label: 'فنی', value: 'technical' },
        { label: 'صورتحساب', value: 'billing' },
        { label: 'سفارش', value: 'order' },
        { label: 'محصول', value: 'product' },
        { label: 'سایر', value: 'other' }
      ],
      
      priorityOptions: [
        { label: 'پایین', value: 'low' },
        { label: 'متوسط', value: 'medium' },
        { label: 'بالا', value: 'high' },
        { label: 'بحرانی', value: 'critical' }
      ],
      
      uploadedFiles: [],
      myTickets: [],
      replyMessages: {},
      
      toast: {
        show: false,
        message: '',
        type: 'success'
      },
      
      API_BASE_URL: 'https://polychemmb.com/api'
    }
  },
  
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
    this.loadMyTickets();
  },
  
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside);
  },
  
  methods: {
    getAuthToken() {
      return localStorage.getItem('client_token') || localStorage.getItem('token');
    },
    
    showToast(message, type = 'success') {
      this.toast = { show: true, message, type };
      setTimeout(() => {
        this.toast.show = false;
      }, 3000);
    },

    async apiCall(endpoint, options = {}) {
      const token = this.getAuthToken();
      if (!token) {
        this.$router.push('/client/login');
        return null;
      }

      try {
        const response = await fetch(`${this.API_BASE_URL}${endpoint}`, {
          method: options.method || 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: options.body ? JSON.stringify(options.body) : undefined
        });

        if (response.status === 401) {
          localStorage.clear();
          this.$router.push('/client/login');
          return null;
        }

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        return await response.json();
      } catch (error) {
        console.error('API Error:', error);
        return null;
      }
    },

    //  تابع بارگذاری تفصیلات تیکت شامل پیام‌ها
    async loadTicketDetails(ticketId) {
      try {
        const data = await this.apiCall(`/client/tickets/${ticketId}`);
        if (data && data.ticket) {
          const ticketIndex = this.myTickets.findIndex(t => t.id === ticketId);
          if (ticketIndex !== -1) {
            // به‌روزرسانی تیکت با تمام جزئیات شامل پیام‌ها
            this.myTickets[ticketIndex] = {
              ...this.myTickets[ticketIndex],
              ...data.ticket
            };
            console.log('Ticket details loaded:', data.ticket);
          }
        }
      } catch (error) {
        console.error('Error loading ticket details:', error);
        this.showToast('خطا در بارگذاری تفصیلات تیکت', 'error');
      }
    },

    async loadMyTickets() {
      this.loadingTickets = true;
      try {
        const data = await this.apiCall('/client/tickets?limit=100');
        if (data) {
          this.myTickets = data.tickets || [];
          console.log('Tickets loaded:', this.myTickets.length);
        }
      } finally {
        this.loadingTickets = false;
      }
    },
    
    async submitTicket() {
      // Validation
      if (!this.ticketData.category) {
        this.showToast('لطفاً دسته‌بندی را انتخاب کنید', 'error');
        return;
      }
      
      if (!this.ticketData.title.trim()) {
        this.showToast('لطفاً عنوان تیکت را وارد کنید', 'error');
        return;
      }
      
      if (!this.ticketData.message.trim()) {
        this.showToast('لطفاً متن پیام را وارد کنید', 'error');
        return;
      }
      
      this.isSubmitting = true;
      
      try {
        const token = this.getAuthToken();
        
        // Step 1: Create ticket
        const response = await fetch(`${this.API_BASE_URL}/client/tickets`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.ticketData)
        });
        
        if (!response.ok) {
          const error = await response.json();
          throw new Error(error.message || 'خطا در ایجاد تیکت');
        }
        
        const data = await response.json();
        const ticketId = data.ticket.id;
        
        // Step 2: Upload files if any
        if (this.uploadedFiles.length > 0) {
          await this.uploadFiles(ticketId);
        }
        
        this.showToast('تیکت با موفقیت ایجاد شد', 'success');
        
        // Reset form
        this.ticketData = {
          title: '',
          category: '',
          priority: 'medium',
          message: ''
        };
        this.uploadedFiles = [];
        
        // Reload tickets
        await this.loadMyTickets();
        
      } catch (error) {
        console.error('Error creating ticket:', error);
        this.showToast(error.message || 'خطا در ایجاد تیکت', 'error');
      } finally {
        this.isSubmitting = false;
      }
    },
    
    async uploadFiles(ticketId) {
      const token = this.getAuthToken();
      
      for (const file of this.uploadedFiles) {
        try {
          const formData = new FormData();
          formData.append('file', file);
          
          const response = await fetch(`${this.API_BASE_URL}/client/tickets/${ticketId}/files`, {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${token}`
            },
            body: formData
          });
          
          if (!response.ok) {
            console.error(`Failed to upload file: ${file.name}`);
          }
        } catch (error) {
          console.error(`Error uploading file ${file.name}:`, error);
        }
      }
    },

    async sendReply(ticketId) {
      const message = this.replyMessages[ticketId];
      if (!message?.trim()) {
        this.showToast('پیام خالی است', 'error');
        return;
      }

      this.sendingReplyId = ticketId;
      try {
        const data = await this.apiCall(`/client/tickets/${ticketId}/messages`, {
          method: 'POST',
          body: { message }
        });

        if (data && data.success) {
          this.showToast('پیام ارسال شد', 'success');
          this.replyMessages[ticketId] = '';
          
          // Reload ticket details
          await this.loadTicketDetails(ticketId);
        }
      } finally {
        this.sendingReplyId = null;
      }
    },

    //  با اضافه کردن loadTicketDetails
    toggleTicketDetail(ticket) {
      if (this.expandedTicketId === ticket.id) {
        this.expandedTicketId = null;
      } else {
        this.expandedTicketId = ticket.id;
        //  بارگذاری تفصیلات تیکت شامل پیام‌ها
        this.loadTicketDetails(ticket.id);
      }
    },
    
    handleFileSelect(event) {
      const files = Array.from(event.target.files);
      this.addFiles(files);
    },
    
    handleDrop(event) {
      this.isDragging = false;
      const files = Array.from(event.dataTransfer.files);
      this.addFiles(files);
    },
    
    addFiles(files) {
      const validFiles = files.filter(file => {
        if (file.size > 10 * 1024 * 1024) {
          this.showToast(`فایل ${file.name} بیش از 10 مگابایت است`, 'error');
          return false;
        }
        
        const allowedTypes = ['.pdf', '.jpg', '.jpeg', '.png', '.doc', '.docx'];
        const fileExt = '.' + file.name.split('.').pop().toLowerCase();
        
        if (!allowedTypes.includes(fileExt)) {
          this.showToast(`فرمت فایل ${file.name} مجاز نیست`, 'error');
          return false;
        }
        
        return true;
      });
      
      this.uploadedFiles.push(...validFiles);
    },
    
    removeFile(index) {
      this.uploadedFiles.splice(index, 1);
    },
    
    formatFileSize(bytes) {
      if (bytes < 1024) return bytes + ' B';
      if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
      return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
    },
    
    togglePriorityDropdown() {
      this.isPriorityOpen = !this.isPriorityOpen;
    },
    
    selectPriority(value) {
      this.ticketData.priority = value;
      this.isPriorityOpen = false;
    },
    
    handleClickOutside(event) {
      if (this.$refs.prioritySelectRef && !this.$refs.prioritySelectRef.contains(event.target)) {
        this.isPriorityOpen = false;
      }
    },

    callSupport() {
      // Create phone call link
      window.location.href = 'tel:+989144605066';
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

    getStatusLabel(status) {
      const labels = {
        open: 'باز',
        inprogress: 'در حال بررسی',
        closed: 'بسته',
        resolved: 'حل شده',
        awaiting: 'در انتظار'
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

    getStatusBadgeClass(status) {
      const classes = {
        open: 'bg-blue-100 text-blue-800',
        inprogress: 'bg-orange-100 text-orange-800',
        closed: 'bg-gray-100 text-gray-800',
        resolved: 'bg-green-100 text-green-800',
        awaiting: 'bg-yellow-100 text-yellow-800'
      };
      return classes[status] || 'bg-gray-100 text-gray-800';
    },

    getPriorityBadgeClass(priority) {
      const classes = {
        low: 'bg-green-100 text-green-800',
        medium: 'bg-yellow-100 text-yellow-800',
        high: 'bg-orange-100 text-orange-800',
        critical: 'bg-red-100 text-red-800'
      };
      return classes[priority] || 'bg-gray-100 text-gray-800';
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
}
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(250, 204, 21, 0.4);
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(250, 204, 21, 0.6);
}

input:focus,
select:focus,
textarea:focus {
  box-shadow: 0 0 0 3px rgba(250, 204, 21, 0.1);
}

.priority-indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
}

.priority-low {
  background: #10b981;
}

.priority-medium {
  background: #eab308;
}

.priority-high {
  background: #f59e0b;
}

.priority-critical {
  background: #dc2626;
}

.spinner-small {
  width: 20px;
  height: 20px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(250, 204, 21, 0.3);
  border-top-color: #FACC15;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  z-index: 10000;
  min-width: 250px;
  color: white;
}

.toast-success {
  background: #10b981;
}

.toast-error {
  background: #ef4444;
}

.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  transform: translateX(100%);
  opacity: 0;
}

.toast-leave-to {
  transform: translateY(100%);
  opacity: 0;
}

/*  بهبود نمایش پیام‌های ادمین */
.bg-blue-50 {
  background-color: #eff6ff;
  border-right: 4px solid #3b82f6;
  padding-right: 12px;
}
</style>