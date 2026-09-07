<template>
  <div style="padding: 20px; border-top: 1px solid #e0e0e0; background: white;">
    <form @submit.prevent="sendMessage" style="display: flex; gap: 10px;">
      <input 
        v-model="message"
        type="text"
        placeholder="پیام خود را بنویسید..."
        style="flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 20px;"
        @input="handleTyping"
      />
      <button type="submit" class="btn btn-primary" style="border-radius: 50%; width: 40px; height: 40px;">
        ➤
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
const chatStore = useChatStore()
const { sendTyping } = useWebSocket()

const message = ref('')
let typingTimeout: any = null

const sendMessage = async () => {
  if (!message.value.trim()) return
  
  const activeChat = chatStore.activeChat
  await chatStore.sendMessage(activeChat.id, message.value)
  message.value = ''
  sendTyping(activeChat.id, false)
}

const handleTyping = () => {
  const activeChat = chatStore.activeChat
  sendTyping(activeChat.id, true)
  
  clearTimeout(typingTimeout)
  typingTimeout = setTimeout(() => {
    sendTyping(activeChat.id, false)
  }, 1000)
}
</script>