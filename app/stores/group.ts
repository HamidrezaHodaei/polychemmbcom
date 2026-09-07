//stores/groupStore.ts

import { defineStore } from 'pinia'

export const useGroupStore = defineStore('group', {
  state: () => ({
    groups: [] as any[],
    activeGroup: null as any,
    messages: [] as any[]
  }),
  
  actions: {
    async loadGroups() {
      const { apiCall } = useApi()
      try {
        const groups = await apiCall('/api/groups')
        this.groups = groups
      } catch (error) {
        console.error('Error loading groups:', error)
      }
    },
    
    async createGroup(groupData: any) {
      const { apiCall } = useApi()
      try {
        const group = await apiCall('/api/groups', {
          method: 'POST',
          body: groupData
        })
        this.groups.push(group)
        return group
      } catch (error) {
        console.error('Error creating group:', error)
        throw error
      }
    },
    
    async loadMessages(groupId: number) {
      const { apiCall } = useApi()
      try {
        const messages = await apiCall(`/api/groups/${groupId}/messages`)
        this.messages = messages
      } catch (error) {
        console.error('Error loading group messages:', error)
      }
    },
    
    async sendMessage(groupId: number, content: string) {
      const { apiCall } = useApi()
      try {
        const message = await apiCall(`/api/groups/${groupId}/messages`, {
          method: 'POST',
          body: {
            content,
            message_type: 'text'
          }
        })
        this.messages.push(message)
        return message
      } catch (error) {
        console.error('Error sending group message:', error)
      }
    },
    
    setActiveGroup(group: any) {
      this.activeGroup = group
    }
  }
})