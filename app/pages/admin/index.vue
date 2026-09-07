<!-- app/pages/admin/index.vue - با دریافت اطلاعات از بک‌اند -->
<template>
<div class="flex min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 font-[IRANYekan]" dir="rtl">
    <!-- Sidebar -->
    <aside class="fixed right-0 top-0 h-screen w-64 bg-white flex flex-col z-40 pointer-events-auto shadow-2xl">
      <!-- Logo Section -->
      <div class="px-6 pt-8 pb-6 border-b border-slate-100 bg-gradient-to-b from-slate-50 to-white">
        <div class="flex items-center gap-3 justify-end translate-x-[40px]">
          <img src="/polychem wall B.png" alt="PolyChem Logo" class="w-32 h-auto drop-shadow-md" />
        </div>
      </div>

      <!-- Navigation -->
      <nav class="flex-1 px-3 py-4 overflow-auto space-y-1">
        <button
          v-for="item in navItems"
          :key="item.name"
          type="button"
          @click.stop="setActiveTab(item.component, item.name)"
          :class="[
            'w-full flex items-center gap-3 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200 relative',
            activeComponent === item.component
              ? 'bg-slate-900 text-white shadow-lg'
              : 'text-slate-600 hover:bg-slate-50'
          ]"
        >
          <img :src="item.icon" :alt="item.name" class="w-5 h-5 flex-shrink-0" />
          <span class="flex-1 text-right">{{ item.name }}</span>
        </button>
      </nav>

      <!-- Divider -->
      <div class="px-4 py-2 border-t border-slate-100"></div>

      <!-- Settings Link -->
      <div class="px-3 py-2">
        <button
          type="button"
          @click.stop="setActiveTab('Settings', 'تنظیمات')"
          :class="[
            'w-full flex items-center gap-3 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200',
            activeComponent === 'Settings'
              ? 'bg-slate-900 text-white shadow-lg'
              : 'text-slate-600 hover:bg-slate-50'
          ]"
        >
          <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          <span class="flex-1 text-right">تنظیمات</span>
        </button>
      </div>

      <!-- User Profile -->
      <div class="px-3 py-4 border-t border-slate-100">
        <button type="button" class="w-full flex items-center gap-3 px-3 py-3 rounded-lg hover:bg-slate-50 transition-all group" @click.stop>
          <div class="w-10 h-10 bg-slate-200 rounded-lg flex items-center justify-center flex-shrink-0 text-slate-600">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
            </svg>
          </div>
          <div class="flex-1 text-right min-w-0">
            <p class="text-sm font-bold text-slate-900">{{ adminProfile.full_name || 'در حال بارگذاری...' }}</p>
            <p class="text-xs text-slate-500 truncate">{{ adminProfile.email || '' }}</p>
          </div>
        </button>
      </div>
    </aside>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col mr-64 relative z-0">
      <!-- Main Content Area -->
      <main class="flex-1 p-8 overflow-auto">
        <div class="mb-10">
          <h1 class="text-5xl font-bold text-slate-900">{{ activeLabel }}</h1>
          <div class="h-1.5 w-24 bg-slate-900 rounded-full mt-4"></div>
        </div>
        <component :is="activeComponent" />
      </main>
    </div>
  </div>
</template>

<script>
import Dashboard from './tabs/Dashboard.vue'
import Task from './tabs/Task.vue'
import UserManagment from './tabs/UserManagment.vue'
import Pricing from './tabs/Pricingmanagment.vue'
import orders from './tabs/orders.vue' 
import inbox from './tabs/inbox.vue'
import visitlog from './tabs/visitlog.vue'
import Client from './tabs/client.vue'
import Settings from './tabs/Settings.vue'

export default {
  components: { Dashboard, Task, UserManagment, Pricing, orders, inbox, visitlog, Client, Settings },
  data() {
    return {
      activeComponent: 'Task',
      activeLabel: 'کارها',
      adminProfile: {
        full_name: '',
        email: '',
        username: ''
      },
      navItems: [
        { name: 'داشبورد', component: 'Dashboard', icon: 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"%3E%3Crect x="3" y="3" width="7" height="7"%3E%3C/rect%3E%3Crect x="14" y="3" width="7" height="7"%3E%3C/rect%3E%3Crect x="14" y="14" width="7" height="7"%3E%3C/rect%3E%3Crect x="3" y="14" width="7" height="7"%3E%3C/rect%3E%3C/svg%3E' },
        { name: 'کارها', component: 'Task', icon: 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"%3E%3Cpath d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"%3E%3C/path%3E%3Ccircle cx="9" cy="7" r="4"%3E%3C/circle%3E%3Cpath d="M22 21v-2a4 4 0 0 0-3-3.87"%3E%3C/path%3E%3Cpath d="M16 3.13a4 4 0 0 1 0 7.75"%3E%3C/path%3E%3C/svg%3E' },
        { name: 'مدیریت کاربران', component: 'UserManagment', icon: 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"%3E%3Cpath d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"%3E%3C/path%3E%3Ccircle cx="9" cy="7" r="4"%3E%3C/circle%3E%3Cline x1="19" y1="8" x2="19" y2="14"%3E%3C/line%3E%3Cline x1="22" y1="11" x2="16" y2="11"%3E%3C/line%3E%3C/svg%3E' },
        { name: 'مدیریت مشتریان', component: 'Client', icon: 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"%3E%3Cpolygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"%3E%3C/polygon%3E%3C/svg%3E' },
        { name: 'مدیریت قیمت', component: 'Pricing', icon: 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"%3E%3Crect x="2" y="3" width="20" height="14" rx="2" ry="2"%3E%3C/rect%3E%3Cline x1="8" y1="21" x2="16" y2="21"%3E%3C/line%3E%3Cline x1="12" y1="17" x2="12" y2="21"%3E%3C/line%3E%3C/svg%3E' },
        { name: 'سفارشات', component: 'orders', icon: 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"%3E%3Crect x="3" y="3" width="7" height="7"%3E%3C/rect%3E%3Crect x="14" y="3" width="7" height="7"%3E%3C/rect%3E%3Crect x="14" y="14" width="7" height="7"%3E%3C/rect%3E%3Crect x="3" y="14" width="7" height="7"%3E%3C/rect%3E%3C/svg%3E' },
        { name: 'تیکت‌ها', component: 'inbox', icon: 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"%3E%3Crect x="2" y="7" width="20" height="14" rx="2" ry="2"/%3E%3Cpath d="M16 5V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v2"/%3E%3Cpath d="M6 12h12"/%3E%3C/svg%3E' },
        { name: 'آمار بازدید', component: 'visitlog', icon: 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"%3E%3Crect x="3" y="4" width="18" height="18" rx="2" ry="2"%3E%3C/rect%3E%3Cline x1="16" y1="2" x2="16" y2="6"%3E%3C/line%3E%3Cline x1="8" y1="2" x2="8" y2="6"%3E%3C/line%3E%3Cline x1="3" y1="10" x2="21" y2="10"%3E%3C/line%3E%3C/svg%3E' }
      ]
    }
  },
  mounted() {
    this.fetchAdminProfile()
  },
  methods: {
    setActiveTab(componentKey, label) {
      this.activeComponent = componentKey
      this.activeLabel = label
    },
    async fetchAdminProfile() {
      try {
        const token = localStorage.getItem('admin_token') || 
                      localStorage.getItem('access_token') || 
                      localStorage.getItem('token')
        
        if (!token) {
          console.error('No token found')
          return
        }

        const response = await fetch('https://polychemmb.com/api/admin/profile', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          }
        })

        if (response.ok) {
          const data = await response.json()
          // ✅ ترکیب first_name و last_name برای ایجاد full_name
          this.adminProfile = {
            full_name: `${data.first_name} ${data.last_name}`.trim(),
            email: data.email,
            username: data.username
          }
        }
      } catch (error) {
        console.error('Error fetching admin profile:', error)
      }
    }
  }
}
</script>

<style scoped>
@font-face {
  font-family: 'IRANYekan';
  src: url('/fonts/IRANYekanWebRegular.ttf') format('truetype');
}

* {
  font-family: 'IRANYekan', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

nav::-webkit-scrollbar,
main::-webkit-scrollbar {
  width: 6px;
}

nav::-webkit-scrollbar-track,
main::-webkit-scrollbar-track {
  background: transparent;
}

nav::-webkit-scrollbar-thumb,
main::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
  transition: background 0.3s;
}

nav::-webkit-scrollbar-thumb:hover,
main::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

button {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

button:active {
  transform: scale(0.98);
}

aside {
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}
</style>