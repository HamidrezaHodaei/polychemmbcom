import { defineStore } from 'pinia'

export const useChatStore = defineStore('chat', {
  state: () => ({
    conversations: [] as any[],
    activeChat: null as any,
    messages: [] as any[],
    onlineUsers: [] as number[]
  }),
  
  actions: {
    async loadConversations() {
      const { apiCall } = useApi()
      try {
        // بدون پارامتر search، فقط کاربرانی که قبلاً باهاشون چت کردیم
        const users = await apiCall('/api/users')
        this.conversations = users
      } catch (error) {
        console.error('Error loading conversations:', error)
      }
    },
    
    async searchUsers(query: string) {
      const { apiCall } = useApi()
      try {
        if (!query || query.trim().length === 0) {
          // اگر جستجو خالی بود، لیست چت‌ها رو نشون بده
          await this.loadConversations()
          return this.conversations
        }
        
        // جستجو در کاربران
        const users = await apiCall(`/api/users?search=${encodeURIComponent(query)}`)
        return users
      } catch (error) {
        console.error('Error searching users:', error)
        return []
      }
    },
    
    async loadMessages(userId: number) {
      const { apiCall } = useApi()
      try {
        const messages = await apiCall(`/api/chats/private/${userId}`)
        this.messages = messages
      } catch (error) {
        console.error('Error loading messages:', error)
      }
    },
    
    async sendMessage(receiverId: number, content: string) {
      const { apiCall } = useApi()
      try {
        const message = await apiCall('/api/chats/private', {
          method: 'POST',
          body: {
            receiver_id: receiverId,
            content,
            message_type: 'text'
          }
        })
        this.messages.push(message)
        return message
      } catch (error) {
        console.error('Error sending message:', error)
        throw error
      }
    },
    
    addMessage(message: any) {
      this.messages.push(message)
    },
    
    setActiveChat(chat: any) {
      this.activeChat = chat
    },
    
    updateOnlineUsers(users: number[]) {
      this.onlineUsers = users
    }
  }
})