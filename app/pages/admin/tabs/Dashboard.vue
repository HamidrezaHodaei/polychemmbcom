<template>
  <div class="space-y-6">
    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <!-- Total Users -->
      <div class="bg-white rounded-xl border border-gray-200 p-6 hover:shadow-lg transition-shadow">
        <div class="flex items-center justify-between mb-4">
          <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
          </div>
          <span class="text-sm font-medium text-green-600 bg-green-50 px-2 py-1 rounded">+12%</span>
        </div>
        <h3 class="text-gray-500 text-sm font-medium mb-1">Total Users</h3>
        <p class="text-3xl font-bold text-gray-900">{{ totalUsers.toLocaleString() }}</p>
      </div>

      <!-- Total Orders -->
      <div class="bg-white rounded-xl border border-gray-200 p-6 hover:shadow-lg transition-shadow">
        <div class="flex items-center justify-between mb-4">
          <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
            </svg>
          </div>
          <span class="text-sm font-medium text-green-600 bg-green-50 px-2 py-1 rounded">+8%</span>
        </div>
        <h3 class="text-gray-500 text-sm font-medium mb-1">Total Orders</h3>
        <p class="text-3xl font-bold text-gray-900">{{ totalOrders.toLocaleString() }}</p>
      </div>

      <!-- Unread Messages -->
      <div class="bg-white rounded-xl border border-gray-200 p-6 hover:shadow-lg transition-shadow">
        <div class="flex items-center justify-between mb-4">
          <div class="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
          </div>
          <span class="text-sm font-medium text-red-600 bg-red-50 px-2 py-1 rounded">New</span>
        </div>
        <h3 class="text-gray-500 text-sm font-medium mb-1">Unread Messages</h3>
        <p class="text-3xl font-bold text-gray-900">{{ unreadMessages }}</p>
      </div>

      <!-- Website Visits -->
      <div class="bg-white rounded-xl border border-gray-200 p-6 hover:shadow-lg transition-shadow">
        <div class="flex items-center justify-between mb-4">
          <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
          </div>
          <span class="text-sm font-medium text-green-600 bg-green-50 px-2 py-1 rounded">+24%</span>
        </div>
        <h3 class="text-gray-500 text-sm font-medium mb-1">Website Visits</h3>
        <p class="text-3xl font-bold text-gray-900">{{ websiteVisits.toLocaleString() }}</p>
      </div>
    </div>

    <!-- Charts Section -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- Website Analytics Chart -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-semibold text-gray-900">Website Analytics</h3>
          <select class="text-sm border border-gray-200 rounded-lg px-3 py-1 focus:outline-none focus:ring-2 focus:ring-gray-900">
            <option>Last 7 days</option>
            <option>Last 30 days</option>
            <option>Last 3 months</option>
          </select>
        </div>
        <div class="space-y-4">
          <div v-for="day in websiteAnalytics" :key="day.day" class="flex items-center gap-4">
            <span class="text-sm font-medium text-gray-600 w-16">{{ day.day }}</span>
            <div class="flex-1 bg-gray-100 rounded-full h-8 relative overflow-hidden">
              <div 
                class="bg-gradient-to-r from-blue-500 to-blue-600 h-full rounded-full flex items-center justify-end pr-3 transition-all duration-500"
                :style="{ width: day.percentage + '%' }"
              >
                <span class="text-xs font-semibold text-white">{{ day.visits.toLocaleString() }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Sales Analytics Chart -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-semibold text-gray-900">Sales Analytics</h3>
          <select class="text-sm border border-gray-200 rounded-lg px-3 py-1 focus:outline-none focus:ring-2 focus:ring-gray-900">
            <option>This month</option>
            <option>Last month</option>
            <option>This year</option>
          </select>
        </div>
        <div class="space-y-4">
          <div class="flex items-center justify-between p-4 bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg border border-green-100">
            <div>
              <p class="text-sm text-gray-600 mb-1">Total Revenue</p>
              <p class="text-2xl font-bold text-gray-900">${{ totalRevenue.toLocaleString() }}</p>
            </div>
            <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center">
              <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
          
          <div class="space-y-3">
            <div v-for="product in topProducts" :key="product.name" class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center">
                  <span class="text-sm font-semibold text-gray-700">{{ product.name.charAt(0) }}</span>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-900">{{ product.name }}</p>
                  <p class="text-xs text-gray-500">{{ product.sales }} sales</p>
                </div>
              </div>
              <span class="text-sm font-semibold text-gray-900">${{ product.revenue.toLocaleString() }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Recent Activity -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <h3 class="text-lg font-semibold text-gray-900 mb-4">Recent Activity</h3>
      <div class="space-y-4">
        <div v-for="activity in recentActivities" :key="activity.id" class="flex items-start gap-4 pb-4 border-b border-gray-100 last:border-0">
          <div :class="['w-10 h-10 rounded-full flex items-center justify-center', activity.color]">
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="activity.icon" />
            </svg>
          </div>
          <div class="flex-1">
            <p class="text-sm font-medium text-gray-900">{{ activity.title }}</p>
            <p class="text-xs text-gray-500 mt-1">{{ activity.description }}</p>
          </div>
          <span class="text-xs text-gray-400">{{ activity.time }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      totalUsers: 45678,
      totalOrders: 8942,
      unreadMessages: 127,
      websiteVisits: 234567,
      totalRevenue: 892450,
      websiteAnalytics: [
        { day: 'Mon', visits: 4250, percentage: 85 },
        { day: 'Tue', visits: 3890, percentage: 78 },
        { day: 'Wed', visits: 4580, percentage: 92 },
        { day: 'Thu', visits: 3200, percentage: 64 },
        { day: 'Fri', visits: 4890, percentage: 98 },
        { day: 'Sat', visits: 3650, percentage: 73 },
        { day: 'Sun', visits: 2980, percentage: 60 }
      ],
      topProducts: [
        { name: 'Product Alpha', sales: 234, revenue: 45600 },
        { name: 'Product Beta', sales: 189, revenue: 38900 },
        { name: 'Product Gamma', sales: 156, revenue: 29800 },
        { name: 'Product Delta', sales: 142, revenue: 25400 }
      ],
      recentActivities: [
        {
          id: 1,
          title: 'New order received',
          description: 'Order #12345 from John Doe - $450.00',
          time: '2 min ago',
          color: 'bg-green-500',
          icon: 'M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z'
        },
        {
          id: 2,
          title: 'New user registered',
          description: 'Sarah Wilson joined the platform',
          time: '15 min ago',
          color: 'bg-blue-500',
          icon: 'M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z'
        },
        {
          id: 3,
          title: 'Payment processed',
          description: 'Invoice #5678 paid - $890.00',
          time: '1 hour ago',
          color: 'bg-purple-500',
          icon: 'M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z'
        },
        {
          id: 4,
          title: 'Support ticket resolved',
          description: 'Ticket #8901 marked as resolved',
          time: '3 hours ago',
          color: 'bg-yellow-500',
          icon: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z'
        }
      ]
    }
  }
}
</script>

<style scoped>
/* Custom animations and transitions */
</style>