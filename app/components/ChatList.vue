<template>
  <div style="padding: 20px;">
    <h3 style="margin-bottom: 20px;">مکالمات</h3>
    <div 
      v-for="user in conversations" 
      :key="user.id"
      @click="selectChat(user)"
      style="padding: 15px; border-bottom: 1px solid #eee; cursor: pointer;"
      :style="{ background: activeChat?.id === user.id ? '#f0f2f5' : 'white' }"
    >
      <div style="display: flex; align-items: center;">
        <div style="width: 40px; height: 40px; border-radius: 50%; background: #0084ff; color: white; display: flex; align-items: center; justify-content: center; margin-left: 10px;">
          {{ user.username[0].toUpperCase() }}
        </div>
        <div style="flex: 1;">
          <div style="font-weight: 500;">{{ user.full_name || user.username }}</div>
          <div style="font-size: 12px; color: #65676b;">{{ user.username }}</div>
        </div>
        <div v-if="isOnline(user.id)" style="width: 10px; height: 10px; border-radius: 50%; background: #42b72a;"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const chatStore = useChatStore()

const conversations = computed(() => chatStore.conversations)
const activeChat = computed(() => chatStore.activeChat)

const selectChat = (user: any) => {
  chatStore.setActiveChat(user)
  chatStore.loadMessages(user.id)
}

const isOnline = (userId: number) => {
  return chatStore.onlineUsers.includes(userId)
}
</script>