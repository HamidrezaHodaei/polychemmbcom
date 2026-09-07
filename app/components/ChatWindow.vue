<template>
  <div style="display: flex; flex-direction: column; height: 100%;">
    <div style="padding: 20px; border-bottom: 1px solid #e0e0e0; background: white;">
      <div style="display: flex; align-items: center;">
        <div style="width: 40px; height: 40px; border-radius: 50%; background: #0084ff; color: white; display: flex; align-items: center; justify-content: center; margin-left: 10px;">
          {{ activeChat.username[0].toUpperCase() }}
        </div>
        <div>
          <div style="font-weight: 500;">{{ activeChat.full_name || activeChat.username }}</div>
          <div style="font-size: 12px; color: #65676b;">
            {{ isOnline(activeChat.id) ? 'آنلاین' : 'آفلاین' }}
          </div>
        </div>
      </div>
    </div>
    
    <div ref="messagesContainer" style="flex: 1; overflow-y: auto; padding: 20px; background: #f0f2f5;">
      <div v-for="msg in messages" :key="msg.id" style="margin-bottom: 15px;">
        <div :style="{
          display: 'flex',
          justifyContent: msg.sender_id === user.id ? 'flex-end' : 'flex-start'
        }">
          <div :style="{
            maxWidth: '60%',
            padding: '10px 15px',
            borderRadius: '18px',
            background: msg.sender_id === user.id ? '#0084ff' : 'white',
            color: msg.sender_id === user.id ? 'white' : 'black'
          }">
            {{ msg.content }}
          </div>
        </div>
      </div>
    </div>
    
    <MessageInput />
  </div>
</template>

<script setup lang="ts">
const chatStore = useChatStore()
const authStore = useAuthStore()

const activeChat = computed(() => chatStore.activeChat)
const messages = computed(() => chatStore.messages)
const user = computed(() => authStore.user)

const messagesContainer = ref<HTMLElement | null>(null)

watch(messages, () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
})

const isOnline = (userId: number) => {
  return chatStore.onlineUsers.includes(userId)
}
</script>