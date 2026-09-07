<template>
  <div class="space-y-6">
    <!-- Header Section -->
    <div class="flex items-center justify-between">
      <div>
        <p class="text-sm text-gray-600">Manage your team members and their account permissions here.</p>
      </div>
      <button 
        type="button"
        @click="showAddUserModal = true"
        class="flex items-center gap-2 px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Add user
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
      <div class="stat-card bg-white rounded-lg p-6 border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">Total Users</p>
            <p class="text-3xl font-bold text-gray-900 mt-1">{{ users.length }}</p>
          </div>
          <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="stat-card bg-white rounded-lg p-6 border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">Departments</p>
            <p class="text-3xl font-bold text-gray-900 mt-1">{{ departments.length }}</p>
          </div>
          <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
            </svg>
          </div>
        </div>
      </div>

      <div class="stat-card bg-white rounded-lg p-6 border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">Active Users</p>
            <p class="text-3xl font-bold text-gray-900 mt-1">{{ activeUsers }}</p>
          </div>
          <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="stat-card bg-white rounded-lg p-6 border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600">Admins</p>
            <p class="text-3xl font-bold text-gray-900 mt-1">{{ adminCount }}</p>
          </div>
          <div class="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="bg-white rounded-lg border border-gray-200 p-4">
      <div class="flex items-center gap-4">
        <div class="flex-1 relative">
          <svg class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search users..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
          />
        </div>
        <select 
          v-model="filterDepartment"
          class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
        >
          <option value="">All Departments</option>
          <option v-for="dept in departments" :key="dept" :value="dept">{{ dept }}</option>
        </select>
        <select 
          v-model="filterRole"
          class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
        >
          <option value="">All Roles</option>
          <option value="Admin">Admin</option>
          <option value="Manager">Manager</option>
          <option value="Employee">Employee</option>
        </select>
      </div>
    </div>

    <!-- Users Table -->
    <div class="bg-white rounded-lg border border-gray-200 overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-50 border-b border-gray-200">
            <tr>
              <th class="text-left py-3 px-6 text-xs font-medium text-gray-500 uppercase">
                <input type="checkbox" class="rounded border-gray-300" />
              </th>
              <th class="text-left py-3 px-6 text-xs font-medium text-gray-500 uppercase">User</th>
              <th class="text-left py-3 px-6 text-xs font-medium text-gray-500 uppercase">Department</th>
              <th class="text-left py-3 px-6 text-xs font-medium text-gray-500 uppercase">Role</th>
              <th class="text-left py-3 px-6 text-xs font-medium text-gray-500 uppercase">Status</th>
              <th class="text-left py-3 px-6 text-xs font-medium text-gray-500 uppercase">Last Active</th>
              <th class="text-left py-3 px-6 text-xs font-medium text-gray-500 uppercase">Date Added</th>
              <th class="text-left py-3 px-6 text-xs font-medium text-gray-500 uppercase"></th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr 
              v-for="user in filteredUsers" 
              :key="user.id"
              class="hover:bg-gray-50 transition-colors"
            >
              <td class="py-4 px-6">
                <input type="checkbox" class="rounded border-gray-300" />
              </td>
              <td class="py-4 px-6">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-white font-semibold">
                    {{ user.name.split(' ').map(n => n[0]).join('') }}
                  </div>
                  <div>
                    <p class="font-medium text-gray-900">{{ user.name }}</p>
                    <p class="text-sm text-gray-500">{{ user.email }}</p>
                  </div>
                </div>
              </td>
              <td class="py-4 px-6">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-700">
                  {{ user.department }}
                </span>
              </td>
              <td class="py-4 px-6">
                <span 
                  :class="[
                    'inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium',
                    user.role === 'Admin' ? 'bg-purple-100 text-purple-700' :
                    user.role === 'Manager' ? 'bg-yellow-100 text-yellow-700' :
                    'bg-gray-100 text-gray-700'
                  ]"
                >
                  {{ user.role }}
                </span>
              </td>
              <td class="py-4 px-6">
                <span 
                  :class="[
                    'inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium',
                    user.status === 'Active' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
                  ]"
                >
                  <span class="w-1.5 h-1.5 rounded-full" :class="user.status === 'Active' ? 'bg-green-500' : 'bg-red-500'"></span>
                  {{ user.status }}
                </span>
              </td>
              <td class="py-4 px-6 text-sm text-gray-600">{{ user.lastActive }}</td>
              <td class="py-4 px-6 text-sm text-gray-600">{{ user.dateAdded }}</td>
              <td class="py-4 px-6">
                <button 
                  type="button"
                  @click="editUser(user)"
                  class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
                >
                  <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <div class="flex items-center justify-between px-6 py-4 border-t border-gray-200">
        <p class="text-sm text-gray-600">
          Showing {{ filteredUsers.length }} of {{ users.length }} users
        </p>
        <div class="flex items-center gap-2">
          <button type="button" class="px-3 py-1 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
            Previous
          </button>
          <button type="button" class="px-3 py-1 bg-gray-900 text-white rounded-lg">1</button>
          <button type="button" class="px-3 py-1 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">2</button>
          <button type="button" class="px-3 py-1 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">3</button>
          <button type="button" class="px-3 py-1 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
            Next
          </button>
        </div>
      </div>
    </div>

    <!-- Add/Edit User Modal -->
    <div 
      v-if="showAddUserModal"
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4"
      @click.self="showAddUserModal = false"
    >
      <div class="bg-white rounded-lg w-full max-w-2xl max-h-[90vh] flex flex-col">
        <!-- Modal Header -->
        <div class="flex items-center justify-between p-6 border-b border-gray-200">
          <h2 class="text-xl font-bold text-gray-900">Add New User</h2>
          <button 
            type="button"
            @click="showAddUserModal = false"
            class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Modal Body - Scrollable -->
        <div class="flex-1 overflow-y-auto p-6">
          <div class="space-y-6">
            <!-- Personal Information Section -->
            <div>
              <h3 class="text-sm font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                Personal Information
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    First Name <span class="text-red-500">*</span>
                  </label>
                  <input 
                    v-model="newUser.firstName"
                    type="text" 
                    placeholder="Enter first name"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Last Name <span class="text-red-500">*</span>
                  </label>
                  <input 
                    v-model="newUser.lastName"
                    type="text" 
                    placeholder="Enter last name"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
              </div>
            </div>

            <!-- Contact Information Section -->
            <div>
              <h3 class="text-sm font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                Contact Information
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Email Address <span class="text-red-500">*</span>
                  </label>
                  <input 
                    v-model="newUser.email"
                    type="email" 
                    placeholder="name@polychemmb.com"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Phone Number <span class="text-red-500">*</span>
                  </label>
                  <input 
                    v-model="newUser.phone"
                    type="tel" 
                    placeholder="+49 123 456 7890"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Mobile Number
                  </label>
                  <input 
                    v-model="newUser.mobile"
                    type="tel" 
                    placeholder="+49 123 456 7890"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Employee ID <span class="text-red-500">*</span>
                  </label>
                  <input 
                    v-model="newUser.employeeId"
                    type="text" 
                    placeholder="EMP-001"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
              </div>
            </div>

            <!-- Work Information Section -->
            <div>
              <h3 class="text-sm font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                Work Information
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Department <span class="text-red-500">*</span>
                  </label>
                  <select 
                    v-model="newUser.department"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  >
                    <option value="">Select Department</option>
                    <option v-for="dept in departments" :key="dept" :value="dept">{{ dept }}</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Role <span class="text-red-500">*</span>
                  </label>
                  <select 
                    v-model="newUser.role"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  >
                    <option value="">Select Role</option>
                    <option value="Admin">Admin</option>
                    <option value="Manager">Manager</option>
                    <option value="Employee">Employee</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Job Title <span class="text-red-500">*</span>
                  </label>
                  <input 
                    v-model="newUser.jobTitle"
                    type="text" 
                    placeholder="e.g. Senior Engineer"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">
                    Join Date <span class="text-red-500">*</span>
                  </label>
                  <input 
                    v-model="newUser.joinDate"
                    type="date" 
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
              </div>
            </div>

            <!-- Address Information Section -->
            <div>
              <h3 class="text-sm font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                Address
              </h3>
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Street Address</label>
                  <input 
                    v-model="newUser.address"
                    type="text" 
                    placeholder="Enter street address"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                  />
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">City</label>
                    <input 
                      v-model="newUser.city"
                      type="text" 
                      placeholder="Frankfurt"
                      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                    />
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">State/Province</label>
                    <input 
                      v-model="newUser.state"
                      type="text" 
                      placeholder="Hesse"
                      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                    />
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Postal Code</label>
                    <input 
                      v-model="newUser.postalCode"
                      type="text" 
                      placeholder="60311"
                      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal Footer -->
        <div class="flex gap-3 p-6 border-t border-gray-200">
          <button 
            type="button"
            @click="showAddUserModal = false"
            class="flex-1 px-4 py-2.5 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors font-medium"
          >
            Cancel
          </button>
          <button 
            type="button"
            @click="addUser"
            class="flex-1 px-4 py-2.5 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors font-medium"
          >
            Add User
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
      searchQuery: '',
      filterDepartment: '',
      filterRole: '',
      showAddUserModal: false,
      newUser: {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        mobile: '',
        employeeId: '',
        department: '',
        role: '',
        jobTitle: '',
        joinDate: '',
        address: '',
        city: '',
        state: '',
        postalCode: ''
      },
      departments: ['Management', 'Sales', 'Marketing', 'HR', 'Finance', 'Operations'],
      users: [
        {
          id: 1,
          name: 'Florence Shaw',
          email: 'florence@untitledui.com',
          department: 'Management',
          role: 'Admin',
          status: 'Active',
          lastActive: 'Mar 4, 2024',
          dateAdded: 'July 4, 2022'
        },
        {
          id: 2,
          name: 'Amelie Laurent',
          email: 'amelie@untitledui.com',
          department: 'Sales',
          role: 'Admin',
          status: 'Active',
          lastActive: 'Mar 4, 2024',
          dateAdded: 'July 4, 2022'
        },
        {
          id: 3,
          name: 'Ammar Foley',
          email: 'ammar@untitledui.com',
          department: 'Marketing',
          role: 'Manager',
          status: 'Active',
          lastActive: 'Mar 2, 2024',
          dateAdded: 'July 4, 2022'
        },
        {
          id: 4,
          name: 'Caitlyn King',
          email: 'caitlyn@untitledui.com',
          department: 'HR',
          role: 'Employee',
          status: 'Active',
          lastActive: 'Mar 8, 2024',
          dateAdded: 'July 4, 2022'
        },
        {
          id: 5,
          name: 'Sienna Hewitt',
          email: 'sienna@untitledui.com',
          department: 'Finance',
          role: 'Manager',
          status: 'Active',
          lastActive: 'Mar 8, 2024',
          dateAdded: 'July 4, 2022'
        },
        {
          id: 6,
          name: 'Olly Shoeder',
          email: 'olly@untitledui.com',
          department: 'Operations',
          role: 'Employee',
          status: 'Inactive',
          lastActive: 'Mar 6, 2024',
          dateAdded: 'July 4, 2022'
        },
        {
          id: 7,
          name: 'Mathilde Lewis',
          email: 'mathilde@untitledui.com',
          department: 'Management',
          role: 'Employee',
          status: 'Active',
          lastActive: 'Mar 4, 2024',
          dateAdded: 'July 4, 2022'
        },
        {
          id: 8,
          name: 'Jaya Willis',
          email: 'jaya@untitledui.com',
          department: 'Sales',
          role: 'Employee',
          status: 'Active',
          lastActive: 'Mar 4, 2024',
          dateAdded: 'July 4, 2022'
        }
      ]
    }
  },
  computed: {
    filteredUsers() {
      return this.users.filter(user => {
        const matchesSearch = user.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                            user.email.toLowerCase().includes(this.searchQuery.toLowerCase())
        const matchesDepartment = !this.filterDepartment || user.department === this.filterDepartment
        const matchesRole = !this.filterRole || user.role === this.filterRole
        return matchesSearch && matchesDepartment && matchesRole
      })
    },
    activeUsers() {
      return this.users.filter(u => u.status === 'Active').length
    },
    adminCount() {
      return this.users.filter(u => u.role === 'Admin').length
    }
  },
  methods: {
    addUser() {
      if (!this.newUser.firstName || !this.newUser.lastName || !this.newUser.email || 
          !this.newUser.phone || !this.newUser.employeeId || !this.newUser.department || 
          !this.newUser.role || !this.newUser.jobTitle || !this.newUser.joinDate) {
        alert('Please fill in all required fields marked with *')
        return
      }

      const user = {
        id: this.users.length + 1,
        name: `${this.newUser.firstName} ${this.newUser.lastName}`,
        email: this.newUser.email,
        phone: this.newUser.phone,
        mobile: this.newUser.mobile,
        employeeId: this.newUser.employeeId,
        department: this.newUser.department,
        role: this.newUser.role,
        jobTitle: this.newUser.jobTitle,
        joinDate: this.newUser.joinDate,
        address: this.newUser.address,
        city: this.newUser.city,
        state: this.newUser.state,
        postalCode: this.newUser.postalCode,
        status: 'Active',
        lastActive: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        dateAdded: new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })
      }
      this.users.unshift(user)
      this.showAddUserModal = false
      this.newUser = {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        mobile: '',
        employeeId: '',
        department: '',
        role: '',
        jobTitle: '',
        joinDate: '',
        address: '',
        city: '',
        state: '',
        postalCode: ''
      }
    },
    editUser(user) {
      console.log('Edit user:', user)
    }
  }
}
</script>

<style scoped>
/* Hover Effects for Cards */
/* Stat Card Hover Effects */
.stat-card {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(180deg, #FFCD05 0%, #FFCD05 100%);
  transform: scaleY(0);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.stat-card:hover::before {
  transform: scaleY(1);
}

/* Table Row Hover */
tbody tr {
  transition: all 0.3s ease;
  position: relative;
}

tbody tr::before {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(180deg, #FFCD05 0%, #FFCD05 100%);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

tbody tr:hover {
  background-color: #f8fafc;
}

tbody tr:hover::before {
  transform: scaleX(1);
}

/* Button Hover Effects */
button {
  transition: all 0.3s ease;
}

button.bg-gray-900:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(31, 41, 55, 0.3);
}

/* Input/Select Focus Effects */
input[type="text"],
select {
  transition: all 0.3s ease;
}

input[type="text"]:hover,
select:hover {
  border-color: #cbd5e1;
}

input[type="text"]:focus,
select:focus {
  outline: none;
  border-color: #1f2937;
  box-shadow: 0 0 0 3px rgba(31, 41, 55, 0.1);
}
</style>