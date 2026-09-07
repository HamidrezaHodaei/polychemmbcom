import { defineStore } from 'pinia'

export const useWebSocketStore = defineStore('websocket', {
  state: () => ({
    ws: null as WebSocket | null,
    connected: false
  }),
  
  actions: {
    connect(token: string) {
      const config = useRuntimeConfig()
      this.ws = new WebSocket(`${config.public.wsBase}/ws/${token}`)
      
      this.ws.onopen = () => {
        this.connected = true
        console.log('✅ WebSocket connected')
      }
      
      this.ws.onmessage = (event) => {
        const message = JSON.parse(event.data)
        this.handleMessage(message)
      }
      
      this.ws.onclose = () => {
        this.connected = false
        console.log('❌ WebSocket disconnected')
      }
      
      this.ws.onerror = (error) => {
        console.error('WebSocket error:', error)
      }
    },
    
    disconnect() {
      if (this.ws) {
        this.ws.close()
        this.ws = null
        this.connected = false
      }
    },
    
    send(message: any) {
      if (this.ws && this.connected) {
        this.ws.send(JSON.stringify(message))
      }
    },
    
    handleMessage(message: any) {
      const chatStore = useChatStore()
      
      switch (message.event) {
        case 'new_message':
          chatStore.addMessage(message.data)
          break
        case 'user_online':
          if (!chatStore.onlineUsers.includes(message.data.user_id)) {
            chatStore.onlineUsers.push(message.data.user_id)
          }
          break
        case 'user_offline':
          const index = chatStore.onlineUsers.indexOf(message.data.user_id)
          if (index > -1) {
            chatStore.onlineUsers.splice(index, 1)
          }
          break
      }
    }
  }
})