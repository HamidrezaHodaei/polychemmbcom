<template>
  <section>
    <!-- Stats Bar -->
    <div class="flex items-center gap-8 mb-8">
      <div class="flex items-center gap-4 flex-1">
        <div class="flex-1 flex items-center bg-gray-900 text-white rounded-full overflow-hidden h-12">
          <div class="px-6 text-sm font-medium">In Progress 35%</div>
        </div>
        <div class="flex-1 flex items-center bg-yellow-300 rounded-full overflow-hidden h-12">
          <div class="px-6 text-sm font-medium">Completed 48%</div>
        </div>
      </div>
      <div class="flex items-center gap-4">
        <div class="px-6 py-3 bg-white/50 rounded-full border border-gray-300">
          <span class="text-sm font-medium">Pending 12%</span>
        </div>
        <div class="px-6 py-3 bg-white/50 rounded-full border border-gray-300">
          <span class="text-sm font-medium">Overdue 5%</span>
        </div>
      </div>
    </div>

    <!-- Filters -->
    <div class="flex items-center justify-between mb-6">
      <div class="flex items-center gap-4">
        <select v-model="filters.priority" class="px-4 py-2 bg-white/70 rounded-lg border border-gray-300">
          <option value="">Priority</option>
          <option value="High">High</option>
          <option value="Medium">Medium</option>
          <option value="Low">Low</option>
        </select>
        <select v-model="filters.status" class="px-4 py-2 bg-white/70 rounded-lg border border-gray-300">
          <option value="">Status</option>
          <option value="To Do">To Do</option>
          <option value="In Progress">In Progress</option>
          <option value="Review">Review</option>
          <option value="Completed">Completed</option>
        </select>
        <select v-model="filters.department" class="px-4 py-2 bg-white/70 rounded-lg border border-gray-300">
          <option value="">Department</option>
          <option value="Product">Product</option>
          <option value="Engineering">Engineering</option>
          <option value="Operations">Operations</option>
          <option value="Marketing">Marketing</option>
        </select>
        <select v-model="filters.assignee" class="px-4 py-2 bg-white/70 rounded-lg border border-gray-300">
          <option value="">Assignee</option>
          <option value="All">All Members</option>
        </select>
        <div class="relative">
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Search tasks..."
            class="pl-10 pr-4 py-2 bg-white/70 rounded-lg border border-gray-300 w-64"
          />
          <svg class="w-5 h-5 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <select class="px-4 py-2 bg-white/70 rounded-lg border border-gray-300">
          <option>Board View</option>
          <option>List View</option>
          <option>Calendar View</option>
        </select>
        <button @click="showAddTaskModal = true" class="px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 flex items-center gap-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          New Task
        </button>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="flex items-center gap-3 mb-6">
      <button class="p-2 bg-white rounded-lg hover:bg-gray-50 border border-gray-300">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
        </svg>
      </button>
      <button class="p-2 bg-white rounded-lg hover:bg-gray-50 border border-gray-300">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>
      <button class="px-4 py-2 bg-white rounded-lg hover:bg-gray-50 border border-gray-300 flex items-center gap-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
        </svg>
        Export Tasks
      </button>
      <button class="px-4 py-2 bg-white rounded-lg hover:bg-gray-50 border border-gray-300 flex items-center gap-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
        Timeline
      </button>
    </div>

    <!-- Table -->
    <div class="bg-white/70 rounded-2xl overflow-hidden border border-gray-200">
      <table class="w-full">
        <thead>
          <tr class="border-b border-gray-200">
            <th class="px-6 py-4 text-left">
              <input type="checkbox" @change="toggleSelectAll" class="rounded" />
            </th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-600">Task Name</th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-600">Assignee</th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-600">Department</th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-600">Priority</th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-600">Status</th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-600">Due Date</th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-600">Progress</th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-600">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="task in filteredTasks" :key="task.id" :class="{'bg-yellow-100': task.highlighted}" class="border-b border-gray-200 hover:bg-gray-50">
            <td class="px-6 py-4">
              <input type="checkbox" v-model="task.checked" class="rounded" />
            </td>
            <td class="px-6 py-4">
              <div class="flex items-center gap-3">
                <div :class="getPriorityIconClass(task.priority)" class="w-2 h-2 rounded-full"></div>
                <div>
                  <div class="font-medium">{{ task.name }}</div>
                  <div class="text-xs text-gray-500">{{ task.description }}</div>
                </div>
              </div>
            </td>
            <td class="px-6 py-4">
              <div class="flex items-center gap-2">
                <img :src="task.assigneeAvatar" :alt="task.assignee" class="w-8 h-8 rounded-full" />
                <span class="text-sm">{{ task.assignee }}</span>
              </div>
            </td>
            <td class="px-6 py-4">
              <span class="text-sm">{{ task.department }}</span>
            </td>
            <td class="px-6 py-4">
              <span :class="getPriorityClass(task.priority)" class="px-3 py-1 rounded-full text-xs font-medium">
                {{ task.priority }}
              </span>
            </td>
            <td class="px-6 py-4">
              <span :class="getStatusClass(task.status)" class="px-3 py-1 rounded-full text-xs font-medium">
                {{ task.status }}
              </span>
            </td>
            <td class="px-6 py-4">
              <span class="text-sm" :class="{'text-red-600 font-medium': isOverdue(task.dueDate)}">
                {{ task.dueDate }}
              </span>
            </td>
            <td class="px-6 py-4">
              <div class="flex items-center gap-2">
                <div class="flex-1 bg-gray-200 rounded-full h-2 max-w-[80px]">
                  <div :style="{width: task.progress + '%'}" class="bg-green-500 h-2 rounded-full"></div>
                </div>
                <span class="text-xs text-gray-600">{{ task.progress }}%</span>
              </div>
            </td>
            <td class="px-6 py-4">
              <div class="flex items-center gap-2">
                <button @click="editTask(task)" class="p-1 hover:bg-gray-200 rounded">
                  <svg class="w-4 h-4 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                </button>
                <button @click="deleteTask(task.id)" class="p-1 hover:bg-gray-200 rounded">
                  <svg class="w-4 h-4 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add Task Modal -->
    <div v-if="showAddTaskModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50" @click.self="showAddTaskModal = false">
      <div class="bg-white rounded-2xl p-8 max-w-2xl w-full mx-4">
        <h2 class="text-2xl font-bold mb-6">Create New Task</h2>
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Task Name</label>
            <input type="text" v-model="newTask.name" class="w-full px-4 py-2 border border-gray-300 rounded-lg" placeholder="Enter task name" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
            <textarea v-model="newTask.description" class="w-full px-4 py-2 border border-gray-300 rounded-lg" rows="3" placeholder="Enter task description"></textarea>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Assignee</label>
              <select v-model="newTask.assignee" class="w-full px-4 py-2 border border-gray-300 rounded-lg">
                <option value="">Select assignee</option>
                <option value="Anatoly Belik">Anatoly Belik</option>
                <option value="Ksenia Bator">Ksenia Bator</option>
                <option value="Bogdan Nikitin">Bogdan Nikitin</option>
                <option value="Arsen Yatsenko">Arsen Yatsenko</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Department</label>
              <select v-model="newTask.department" class="w-full px-4 py-2 border border-gray-300 rounded-lg">
                <option value="">Select department</option>
                <option value="Product">Product</option>
                <option value="Engineering">Engineering</option>
                <option value="Operations">Operations</option>
                <option value="Marketing">Marketing</option>
              </select>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Priority</label>
              <select v-model="newTask.priority" class="w-full px-4 py-2 border border-gray-300 rounded-lg">
                <option value="Low">Low</option>
                <option value="Medium">Medium</option>
                <option value="High">High</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Due Date</label>
              <input type="date" v-model="newTask.dueDate" class="w-full px-4 py-2 border border-gray-300 rounded-lg" />
            </div>
          </div>
        </div>
        <div class="flex items-center justify-end gap-3 mt-6">
          <button @click="showAddTaskModal = false" class="px-6 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">Cancel</button>
          <button @click="addTask" class="px-6 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800">Create Task</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'TaskManager',
  data() {
    return {
      searchQuery: '',
      showAddTaskModal: false,
      filters: {
        priority: '',
        status: '',
        department: '',
        assignee: ''
      },
      newTask: {
        name: '',
        description: '',
        assignee: '',
        department: '',
        priority: 'Medium',
        dueDate: ''
      },
      tasks: [
        {
          id: 1,
          name: 'Update website homepage',
          description: 'Redesign hero section',
          assignee: 'Anatoly Belik',
          assigneeAvatar: 'https://i.pravatar.cc/150?img=12',
          department: 'Product',
          priority: 'High',
          status: 'In Progress',
          dueDate: 'Dec 28, 2024',
          progress: 65,
          checked: false,
          highlighted: false
        },
        {
          id: 2,
          name: 'Fix payment gateway bug',
          description: 'Resolve checkout errors',
          assignee: 'Ksenia Bator',
          assigneeAvatar: 'https://i.pravatar.cc/150?img=5',
          department: 'Engineering',
          priority: 'High',
          status: 'Review',
          dueDate: 'Dec 25, 2024',
          progress: 90,
          checked: true,
          highlighted: true
        },
        {
          id: 3,
          name: 'Create marketing campaign',
          description: 'Q1 2025 strategy',
          assignee: 'Bogdan Nikitin',
          assigneeAvatar: 'https://i.pravatar.cc/150?img=33',
          department: 'Marketing',
          priority: 'Medium',
          status: 'To Do',
          dueDate: 'Jan 15, 2025',
          progress: 20,
          checked: false,
          highlighted: false
        },
        {
          id: 4,
          name: 'Database optimization',
          description: 'Improve query performance',
          assignee: 'Arsen Yatsenko',
          assigneeAvatar: 'https://i.pravatar.cc/150?img=14',
          department: 'Engineering',
          priority: 'Medium',
          status: 'In Progress',
          dueDate: 'Dec 30, 2024',
          progress: 45,
          checked: false,
          highlighted: false
        },
        {
          id: 5,
          name: 'Customer feedback analysis',
          description: 'Review Q4 surveys',
          assignee: 'Daria Yurchenko',
          assigneeAvatar: 'https://i.pravatar.cc/150?img=9',
          department: 'Operations',
          priority: 'Low',
          status: 'Completed',
          dueDate: 'Dec 20, 2024',
          progress: 100,
          checked: false,
          highlighted: false
        },
        {
          id: 6,
          name: 'Mobile app UI update',
          description: 'New design system',
          assignee: 'Yulia Polishchuk',
          assigneeAvatar: 'https://i.pravatar.cc/150?img=20',
          department: 'Product',
          priority: 'High',
          status: 'In Progress',
          dueDate: 'Jan 5, 2025',
          progress: 55,
          checked: false,
          highlighted: false
        }
      ]
    }
  },
  computed: {
    filteredTasks() {
      return this.tasks.filter(task => {
        const matchesSearch = task.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                            task.description.toLowerCase().includes(this.searchQuery.toLowerCase())
        const matchesPriority = !this.filters.priority || task.priority === this.filters.priority
        const matchesStatus = !this.filters.status || task.status === this.filters.status
        const matchesDepartment = !this.filters.department || task.department === this.filters.department
        
        return matchesSearch && matchesPriority && matchesStatus && matchesDepartment
      })
    }
  },
  methods: {
    getPriorityClass(priority) {
      const classes = {
        'High': 'bg-red-100 text-red-700',
        'Medium': 'bg-yellow-100 text-yellow-700',
        'Low': 'bg-green-100 text-green-700'
      }
      return classes[priority] || 'bg-gray-100 text-gray-700'
    },
    getPriorityIconClass(priority) {
      const classes = {
        'High': 'bg-red-500',
        'Medium': 'bg-yellow-500',
        'Low': 'bg-green-500'
      }
      return classes[priority] || 'bg-gray-500'
    },
    getStatusClass(status) {
      const classes = {
        'To Do': 'bg-gray-100 text-gray-700',
        'In Progress': 'bg-blue-100 text-blue-700',
        'Review': 'bg-purple-100 text-purple-700',
        'Completed': 'bg-green-100 text-green-700'
      }
      return classes[status] || 'bg-gray-100 text-gray-700'
    },
    isOverdue(dueDate) {
      const due = new Date(dueDate)
      const today = new Date()
      return due < today
    },
    toggleSelectAll(event) {
      this.tasks.forEach(task => {
        task.checked = event.target.checked
      })
    },
    addTask() {
      if (!this.newTask.name || !this.newTask.assignee) {
        alert('Please fill in required fields')
        return
      }
      
      const task = {
        id: this.tasks.length + 1,
        name: this.newTask.name,
        description: this.newTask.description,
        assignee: this.newTask.assignee,
        assigneeAvatar: 'https://i.pravatar.cc/150?img=' + (Math.floor(Math.random() * 50) + 1),
        department: this.newTask.department,
        priority: this.newTask.priority,
        status: 'To Do',
        dueDate: new Date(this.newTask.dueDate).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        progress: 0,
        checked: false,
        highlighted: false
      }
      
      this.tasks.unshift(task)
      this.showAddTaskModal = false
      this.resetNewTask()
    },
    resetNewTask() {
      this.newTask = {
        name: '',
        description: '',
        assignee: '',
        department: '',
        priority: 'Medium',
        dueDate: ''
      }
    },
    editTask(task) {
      alert('Edit task: ' + task.name)
    },
    deleteTask(id) {
      if (confirm('Are you sure you want to delete this task?')) {
        this.tasks = this.tasks.filter(task => task.id !== id)
      }
    }
  }
}
</script>