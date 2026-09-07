<template>
  <div class="chat-widget-root" v-if="!isLoading">

    <!-- ═══════════════════════════════════════════════
         CONTACT LAUNCHER PILL
    ═══════════════════════════════════════════════ -->
    <div class="contact-launcher">
      <!-- Collapsed pill button -->
      <transition name="pill-fade">
        <button
          v-if="!launcherPanelOpen"
          class="launcher-pill"
          @click="launcherPanelOpen = true"
          :aria-label="language === 'fa' ? 'تماس و پشتیبانی' : 'Chat or call us'"
        >
          <span class="pill-icon-wrap">
            <svg class="pill-icon" viewBox="0 0 24 24" fill="none">
              <path d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-4l-4 4z"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
          <span class="pill-divider"></span>
          <span class="pill-icon-wrap">
            <svg class="pill-icon" viewBox="0 0 24 24" fill="none">
              <path d="M14.05 6C15.0268 6.19057 15.9244 6.66826 16.6281 7.37194C17.3318 8.07561 17.8095 8.97326 18 9.95M14.05 2C16.0793 2.22544 17.9716 3.13417 19.4163 4.57701C20.8609 6.01984 21.7721 7.91101 22 9.94M18.5 21C9.93959 21 3 14.0604 3 5.5C3 5.11378 3.01413 4.73086 3.04189 4.35173C3.07375 3.91662 3.08968 3.69907 3.2037 3.50103C3.29814 3.33701 3.4655 3.18146 3.63598 3.09925C3.84181 3 4.08188 3 4.56201 3H7.37932C7.78308 3 7.98496 3 8.15802 3.06645C8.31089 3.12515 8.44701 3.22049 8.55442 3.3441C8.67601 3.48403 8.745 3.67376 8.88299 4.05321L10.0491 7.26005C10.2096 7.70153 10.2899 7.92227 10.2763 8.1317C10.2643 8.31637 10.2012 8.49408 10.0942 8.64506C9.97286 8.81628 9.77145 8.93713 9.36863 9.17882L8 10C9.2019 12.6489 11.3501 14.7999 14 16L14.8212 14.6314C15.0629 14.2285 15.1837 14.0271 15.3549 13.9058C15.5059 13.7988 15.6836 13.7357 15.8683 13.7237C16.0777 13.7101 16.2985 13.7904 16.74 13.9509L19.9468 15.117C20.3262 15.255 20.516 15.324 20.6559 15.4456C20.7795 15.553 20.8749 15.6891 20.9335 15.842C21 16.015 21 16.2169 21 16.6207V19.438C21 19.9181 21 20.1582 20.9007 20.364C20.8185 20.5345 20.663 20.7019 20.499 20.7963C20.3009 20.9103 20.0834 20.9262 19.6483 20.9581C19.2691 20.9859 18.8862 21 18.5 21Z"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
        </button>
      </transition>

      <!-- Expanded panel -->
      <transition name="panel-slide">
        <div v-if="launcherPanelOpen" class="launcher-panel" role="dialog">
          <button class="panel-close-btn" @click="launcherPanelOpen = false" :aria-label="language === 'fa' ? 'بستن' : 'Close'">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" width="16" height="16">
              <path d="M18 6L6 18M6 6l12 12" stroke-width="2.5" stroke-linecap="round"/>
            </svg>
          </button>

          <button class="panel-action-row" @click="handleChatNowFromLauncher">
            <span class="panel-action-icon">
              <svg viewBox="0 0 24 24" fill="none" width="20" height="20">
                <path d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-4l-4 4z"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="panel-action-label">{{ language === 'fa' ? 'چت آنلاین' : 'Chat now' }}</span>
          </button>

          <div class="panel-sep"></div>

          <button class="panel-action-row" @click="handleWhatsApp">
            <span class="panel-action-icon whatsapp-icon">
              <svg viewBox="0 0 24 24" width="20" height="20" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2ZM12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.02L7.55 18.85L4.43 19.65L5.25 16.61L5.06 16.29C4.24 14.99 3.8 13.47 3.8 11.91C3.81 7.37 7.5 3.67 12.05 3.67ZM8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7 8.5 7 9.71C7 10.93 7.89 12.1 8 12.27C8.14 12.44 9.76 14.94 12.25 16C12.84 16.27 13.3 16.42 13.66 16.53C14.25 16.72 14.79 16.69 15.22 16.63C15.7 16.56 16.68 16.03 16.89 15.45C17.1 14.87 17.1 14.37 17.04 14.27C16.97 14.17 16.81 14.1 16.56 13.98C16.31 13.86 15.09 13.26 14.87 13.18C14.64 13.1 14.5 13.06 14.31 13.31C14.22 13.43 13.95 13.73 13.72 13.95C13.54 14.12 13.35 14.15 13.1 14.04C12.84 13.92 12.01 13.63 11.03 12.76C10.26 12.08 9.74 11.26 9.58 11.01C9.44 10.76 9.58 10.63 9.7 10.51C9.82 10.39 9.97 10.22 10.1 10.07C10.21 9.93 10.26 9.84 10.35 9.67C10.44 9.5 10.4 9.35 10.34 9.23C10.28 9.11 9.74 7.88 9.5 7.36C9.32 6.95 9.11 6.94 8.95 6.93C8.81 6.93 8.64 6.93 8.53 7.33Z" fill="currentColor"/>
              </svg>
            </span>
            <span class="panel-action-label">{{ language === 'fa' ? 'واتس‌اپ' : 'WhatsApp' }}</span>
          </button>

          <div class="panel-sep"></div>

          <div class="panel-call-group">
            <button class="panel-action-row" @click="handleCallSales">
              <span class="panel-action-icon">
                <svg viewBox="0 0 24 24" fill="none" width="20" height="20">
                  <path d="M14.05 6C15.0268 6.19057 15.9244 6.66826 16.6281 7.37194C17.3318 8.07561 17.8095 8.97326 18 9.95M14.05 2C16.0793 2.22544 17.9716 3.13417 19.4163 4.57701C20.8609 6.01984 21.7721 7.91101 22 9.94M18.5 21C9.93959 21 3 14.0604 3 5.5C3 5.11378 3.01413 4.73086 3.04189 4.35173C3.07375 3.91662 3.08968 3.69907 3.2037 3.50103C3.29814 3.33701 3.4655 3.18146 3.63598 3.09925C3.84181 3 4.08188 3 4.56201 3H7.37932C7.78308 3 7.98496 3 8.15802 3.06645C8.31089 3.12515 8.44701 3.22049 8.55442 3.3441C8.67601 3.48403 8.745 3.67376 8.88299 4.05321L10.0491 7.26005C10.2096 7.70153 10.2899 7.92227 10.2763 8.1317C10.2643 8.31637 10.2012 8.49408 10.0942 8.64506C9.97286 8.81628 9.77145 8.93713 9.36863 9.17882L8 10C9.2019 12.6489 11.3501 14.7999 14 16L14.8212 14.6314C15.0629 14.2285 15.1837 14.0271 15.3549 13.9058C15.5059 13.7988 15.6836 13.7357 15.8683 13.7237C16.0777 13.7101 16.2985 13.7904 16.74 13.9509L19.9468 15.117C20.3262 15.255 20.516 15.324 20.6559 15.4456C20.7795 15.553 20.8749 15.6891 20.9335 15.842C21 16.015 21 16.2169 21 16.6207V19.438C21 19.9181 21 20.1582 20.9007 20.364C20.8185 20.5345 20.663 20.7019 20.499 20.7963C20.3009 20.9103 20.0834 20.9262 19.6483 20.9581C19.2691 20.9859 18.8862 21 18.5 21Z"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
              <span class="panel-action-label">{{ language === 'fa' ? 'تماس با فروش' : 'Call Sales' }}</span>
            </button>
            <div class="panel-phone-num translate-x-4">
              <a :href="`tel:${companyInfo.whatsappPhone.replace(/\s/g,'')}`" class="panel-phone-link">{{ companyInfo.whatsappPhone }}</a>
            </div>
            
          </div>
        </div>
      </transition>
    </div>
    <!-- ═══════════════════ END LAUNCHER ══════════════ -->


    <!-- ═══════════════════════════════════════════════
         CHAT WINDOW
    ═══════════════════════════════════════════════ -->
    <div class="chat-window" :class="{ active: !minimized }" role="dialog" aria-label="POLYCHEM Sales Chat" v-cloak>
      <!-- Header -->
      <div class="chat-header">
        <div class="header-left">
          <div class="header-avatar">
            <img src="/english%20logo%20W1.png" alt="POLYCHEM logo" stroke="currentColor"/>
          </div>
          <div class="header-info">
            <h2>بات پلیکم</h2>
            <div class="header-status"></div>
          </div>
        </div>
        <div class="header-actions">
          <button class="header-btn" @click="clearChat" :title="language === 'fa' ? 'پاک کردن' : 'Clear chat'">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="M3 6h18M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2m3 0v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6h14z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
          <button class="header-btn" @click="closeChat" :title="language === 'fa' ? 'کوچک کردن' : 'Minimize'">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="M19 9l-7 7-7-7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Messages -->
      <div class="chat-messages" ref="chatMessages">
        <div
          v-for="msg in messages"
          :key="msg.id"
          :class="['message', msg.sender === 'user' ? 'user' : 'bot']"
          :dir="msg.lang === 'fa' ? 'rtl' : 'ltr'"
        >
          <div class="message-avatar" aria-hidden="true">
            <img v-if="msg.sender === 'bot'" src="/english%20logo%20W1.png" alt="POLYCHEM logo">
            <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" stroke-width="2"/>
            </svg>
          </div>
          <div class="message-bubble">
            <span v-html="msg.text"></span>
          </div>
        </div>

        <!-- ── QUICK ACTIONS (shown before first user message) ── -->
        <transition name="quick-actions-fade">
          <div v-if="showQuickActions" class="quick-actions-wrapper">
            <p class="quick-actions-label">
              {{ language === 'fa' ? 'چند چیزی که می‌توانم کمک کنم:' : 'A few things I can help you with:' }}
            </p>
            <div class="quick-actions-list">
              <button
                v-for="(action, idx) in currentQuickActions"
                :key="idx"
                class="quick-action-btn"
                @click="sendQuickAction(action.prompt)"
              >
                {{ action.label }}
              </button>
            </div>
          </div>
        </transition>
        <!-- ── END QUICK ACTIONS ── -->

        <!-- Typing Indicator -->
        <div v-if="isTyping" class="message bot">
          <div class="message-avatar" aria-hidden="true">
            <img src="/english%20logo%20W1.png" alt="POLYCHEM logo" stroke="currentColor"/>
          </div>
          <div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
          </div>
        </div>
      </div>

      <!-- Input Area -->
      <div class="chat-input-area">
        <input
          ref="chatInputRef"
          v-model="input"
          type="text"
          class="chat-input"
          :placeholder="language === 'fa' ? 'پیام خود را بنویسید...' : 'Type your message...'"
          @keypress.enter.prevent="sendMessage"
          :dir="language === 'fa' ? 'rtl' : 'ltr'"
        />
        <button class="send-btn" @click="sendMessage" :aria-label="language === 'fa' ? 'ارسال' : 'Send'">
          <svg viewBox="0 0 24 24" fill="none" stroke="#FFFFFF">
            <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </div>
    </div>
    <!-- ═══════════════════ END CHAT WINDOW ═══════════════ -->

  </div>
</template>

<script setup>
import { ref, computed, nextTick, watch, onMounted, onUnmounted } from 'vue'

const isLoading = useLoadingState()

/* Quick Actions Configuration */
const quickActionsConfig = {
  fa: [
    { label: 'مشاهده محصولات و کامپاندها',      prompt: 'محصولات پلیکم چیست؟' },
    { label: 'درخواست استعلام قیمت',            prompt: 'می‌خواهم استعلام قیمت بگیرم' },
    { label: 'درخواست نمونه رایگان',            prompt: 'می‌خواهم نمونه محصول درخواست دهم' }
  ]
}

/* Launcher State */
const launcherPanelOpen = ref(false)

const handleChatNowFromLauncher = () => {
  launcherPanelOpen.value = false
  openChat()
}
const handleCallSales = () => {
  window.location.href = `tel:${companyInfo.whatsappPhone.replace(/\s/g, '')}`
}
const handleWhatsApp = () => {
  const phoneNumber = companyInfo.whatsappPhone.replace(/\s/g, '').replace(/\D/g, '')
  window.open(`https://wa.me/${phoneNumber}`, '_blank')
}

/* Chat State */
const messages = ref([
  {
    id: 1,
    sender: 'bot',
    text: `سلام! به پلیکم خوش آمدید. ما از سال 1394 به صورت تخصصی در زمینه تولید کامپاندها و مستربچ‌های پلیمری فعالیت می‌کنیم. چطور می‌توانم شما را راهنمایی کنم؟`,
    lang: 'fa'
  }
])
const input = ref('')
const isTyping = ref(false)
const language = ref('fa')
const chatMessages = ref(null)
const minimized = ref(true)
const unreadCount = ref(0)
const chatInputRef = ref(null)

const userHasSentMessage = ref(false)
const showQuickActions = computed(() => !userHasSentMessage.value)
const currentQuickActions = computed(() => quickActionsConfig.fa || quickActionsConfig.fa)

/* Company Info */
const companyInfo = {
  name: 'POLYCHEM',
  phone: '+98 21 22898979',
  whatsappPhone: '+98 914 460 5066',
  fax: '+98 21 22898980',
  email: 'sales@polychemmb.com',
  address: 'واحد 15-شماره 45 – بلوار منظرنژاد- خیابان شریعتی- تهران- ایران',
  website: 'polychemmb.com'
}

const productDetails = {
  fa: {
    'rotochem 0955w': { title: 'ROTOCHEM 0955W', short: 'کامپاند پلی‌اتیلن سفید برای قالب‌گیری چرخشی — مقاومت UV و استحکام ضربه‌ای خوب. بسته‌بندی: 20 کیلوگرمی. دیتاشیت موجود است.' },
    'rotochem 0955b': { title: 'ROTOCHEM 0955B', short: 'کامپاند آبی برای قالب‌گیری چرخشی با خواص مکانیکی و پایداری مناسب. بسته‌بندی: 20 کیلوگرمی.' },
    'polyfil f700': { title: 'POLYFIL F700', short: 'کامپاند HDPE جهت فیلم دمشی (10–25 میکرون). مقاومت کششی بالا، ژل کم، مناسب برای مصارف غذایی.' },
    'hdchem 4760': { title: 'HDCHEM 4760', short: 'کامپاند پلی‌اتیلن برای بلومولدینگ با جریان‌پذیری و سختی مناسب. بسته‌بندی: 25 کیلوگرمی.' },
    'slipchem e 178': { title: 'SlIPCHEM E 178', short: 'مستربچ لغزشی با پخش‌پذیری و پایداری حرارتی بالا برای کاهش ضریب اصطکاک بین لایه‌های فیلم.' },
    'rafcolor 1560': { title: 'RAFCOLOR 1560', short: 'مستربچ سفید با محتوای بالای TiO₂ — پوشش‌دهی و پراکندگی خوب برای رَفیا و نوارها.' },
    'calcichem 126 fp': { title: 'CALCICHEM 126 FP', short: 'مستربچ فیلر پایه پلی‌پروپیلن با تقریباً 80% CaCO₃ — بارگذاری بالا و پراکندگی خوب.' },
    'calcichem 110 frf': { title: 'CALCICHEM 110 FRF', short: 'ماده اصلاح‌کننده معدنی با ذرات بسیار ریز CaCO₃ برای فیلم‌ها و رَفیا — افزایش تولید و کاهش هزینه مواد اولیه.' },
    'calcichem 275 pm': { title: 'CALCICHEM 275 PM', short: 'مستربچ معدنی پلی‌پروپیلن (~75%) برای فیلم‌های BOPP/CPP/OPP با پراکندگی و بارگذاری بالا.' },
    'uvchem mb-r18': { title: 'UVChem MB-R18', short: 'مستربچ تثبیت‌کننده UV برای رَفیا — ترکیب HALS و جذب‌کننده UV برای محافظت بلندمدت. دز معمول ~1 wt%.' }
  }
}

const normalize = (s = '') => {
  return s.toString().toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9\u0600-\u06FF]+/g, ' ').trim().replace(/\s+/g, ' ')
}

const extractDigits = (s = '') => {
  const m = s.match(/\d+/g)
  return m ? m.join(' ') : ''
}

const levenshtein = (a = '', b = '') => {
  const A = a.split(''), B = b.split('')
  const m = A.length, n = B.length
  if (m === 0) return n
  if (n === 0) return m
  const d = Array.from({ length: m + 1 }, (_, i) => Array(n + 1).fill(0))
  for (let i = 0; i <= m; i++) d[i][0] = i
  for (let j = 0; j <= n; j++) d[0][j] = j
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      const cost = A[i - 1] === B[j - 1] ? 0 : 1
      d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)
    }
  }
  return d[m][n]
}

const findProductResponse = (userText, lang) => {
  if (!userText) return null
  const raw = String(userText)
  const lower = normalize(raw)
  const digits = extractDigits(raw)
  const byLang = productDetails[lang] || productDetails.fa
  const candidates = Object.keys(byLang).map((key) => {
    const info = byLang[key]
    const title = info?.title ?? key
    const normKey = normalize(key)
    const normTitle = normalize(title)
    return { key, normKey, normKeyNoSpace: normKey.replace(/\s+/g, ''), title, normTitle, normTitleNoSpace: normTitle.replace(/\s+/g, ''), tokens: Array.from(new Set([...normKey.split(' '), ...normTitle.split(' ')].filter(Boolean))) }
  })
  for (const c of candidates) {
    if (lower.includes(c.normKey) || lower.includes(c.normKeyNoSpace) || lower.includes(c.normTitle) || lower.includes(c.normTitleNoSpace)) return buildProductReply(byLang[c.key], lang)
  }
  if (digits) {
    const dn = digits.replace(/\s+/g, ''), dnz = dn.replace(/^0+/, '')
    for (const c of candidates) {
      if (c.normKey.includes(dn) || c.normTitle.includes(dn) || (dnz && (c.normKey.includes(dnz) || c.normTitle.includes(dnz)))) return buildProductReply(byLang[c.key], lang)
    }
  }
  const userTokens = lower.split(' ').filter(Boolean)
  for (const t of userTokens) {
    if (!t) continue
    for (const c of candidates) {
      if (c.tokens.includes(t)) return buildProductReply(byLang[c.key], lang)
      if (t.length >= 2) {
        for (const tk of c.tokens) {
          if (tk.startsWith(t) || tk.includes(t) || t.startsWith(tk)) return buildProductReply(byLang[c.key], lang)
        }
      }
      if (/\d/.test(t)) {
        const td = t.replace(/\D/g, '')
        if (td && (c.normKey.includes(td) || c.normTitle.includes(td))) return buildProductReply(byLang[c.key], lang)
      }
    }
  }
  for (const c of candidates) {
    const threshold = Math.max(2, Math.floor(Math.min(c.normKey.length, lower.length) * 0.25))
    if (levenshtein(lower, c.normKey) <= threshold || levenshtein(lower, c.normTitle) <= threshold) return buildProductReply(byLang[c.key], lang)
    for (const t of userTokens) {
      for (const tk of c.tokens) {
        if (levenshtein(t, tk) <= 1) return buildProductReply(byLang[c.key], lang)
      }
    }
  }
  return null
}

const buildProductReply = (info, lang) => {
  if (!info) return null
  return `${info.title}\n\n${info.short}\n\nبرای دریافت دیتاشیت تایپ کنید: دیتاشیت ${info.title} یا بپرسید قیمت و مقدار مورد نیاز را.`
}

const patterns = {
  fa: {
    greeting: ['سلام', 'درود', 'صبح بخیر', 'عصر بخیر', 'هی', 'سلام علیکم'],
    products: ['محصول', 'محصولات', 'پلیمر', 'کامپاند', 'مستربچ', 'فیلر', 'رنگ', 'افزودنی', 'سفید', 'بلند', 'کاتالوگ', 'تالک', 'کلسیم کربنات', 'تیتانیوم', 'ضد میکروب', 'شعله گیر'],
    price: ['قیمت', 'هزینه', 'نرخ', 'چند', 'چقدر', 'دلار', 'یورو', 'تومان'],
    order: ['سفارش', 'خرید', 'نیاز', 'می‌خوام', 'تامین', 'حداقل'],
    technical: ['مشخصات', 'فنی', 'دیتاشیت', 'ویژگی', 'خواص', 'دانسیته', 'کیفیت', 'گواهی'],
    delivery: ['ارسال', 'تحویل', 'حمل', 'زمان', 'روز', 'کی', 'چقدر طول'],
    contact: ['تماس', 'شماره', 'آدرس', 'ایمیل', 'موقعیت', 'دفتر'],
    samples: ['نمونه', 'سمپل', 'تست', 'آزمایش'],
    thanks: ['ممنون', 'متشکر', 'مرسی', 'سپاس'],
    about: ['درباره', 'شرکت', 'کی هستید', 'تاریخچه', 'تاسیس', 'تجربه']
  }
}

const responses = {
  fa: {
    greeting: [`سلام، به پلیکم خوش آمدید. ما از سال 1394 به صورت تخصصی در زمینه تولید کامپاندها و مستربچ‌های پلیمری فعالیت می‌کنیم.\n\nچطور می‌توانم شما را راهنمایی کنم؟ شما می‌توانید در زمینه‌های زیر اطلاعات کسب کنید:\n• محصولات (کامپاند و مستربچ)\n• مشخصات فنی\n• قیمت و نحوه سفارش\n• درخواست نمونه`, `با سلام، من دستیار فروش پلیکم هستم. ما تولیدکننده کامپاندها و مستربچ‌های باکیفیت برای صنایع مختلف هستیم.\n\nدر چه زمینه‌ای نیاز به راهنمایی دارید؟`],
    products: [`پلیکم طیف کاملی از محصولات و راهکارهای پلیمری را ارائه می‌دهد:\n\nمحصولات اصلی:\n• کامپاندهای پلیمری (مانند PP-Talc برای صنایع خودرو و لوازم خانگی)\n• مستربچ فیلر (بر پایه کربنات کلسیم)\n• مستربچ رنگی (در انواع طیف‌های رنگی)\n• مستربچ افزودنی (ضد چسبندگی، تاخیرانداز شعله، ضدمیکروب)\n• مستربچ سفید (بر پایه دی‌اکسید تیتانیوم)\n• آمیزه‌های پلیمری سفارشی\n\nکدام‌یک از محصولات مورد نظر شماست؟`],
    price: [`برای دریافت قیمت دقیق و به‌روز، لطفاً با تیم فروش ما تماس بگیرید:\n\n• تلفن: ${companyInfo.whatsappPhone}\n• ایمیل: ${companyInfo.email}\n\nقیمت‌ها بر اساس نوع محصول، حجم سفارش و شرایط تحویل تعیین می‌شوند.`],
    order: [`با تشکر از حسن انتخاب شما؛ برای پردازش سریع و دقیق سفارش، به اطلاعات زیر نیاز داریم:\n\n• کد یا مشخصات فنی محصول\n• مقدار مورد نیاز\n• آدرس دقیق تحویل\n\nلطفاً با ما در ارتباط باشید:\n• تلفن: ${companyInfo.whatsappPhone}\n• ایمیل: ${companyInfo.email}`],
    technical: [`تمامی محصولات پلیکم همراه با مستندات فنی جامع ارائه می‌شوند:\n\nاسناد قابل دریافت:\n• برگه مشخصات فنی (TDS)\n• برگه اطلاعات ایمنی مواد (MSDS)\n• گواهینامه‌های کیفیت\n\nلطفاً درخواست خود را به ایمیل ${companyInfo.email} ارسال فرمایید.`],
    delivery: [`اطلاعات تحویل:\n\nارسال داخلی (ایران):\n• تهران: 2 الی 3 روز کاری\n• شهرستان‌ها: 5 الی 7 روز کاری\n\nارسال بین‌المللی:\n• زمان تحویل بسته به مقصد متغیر است\n\nجهت استعلام هزینه حمل‌ونقل با شماره ${companyInfo.whatsappPhone} تماس بگیرید.`],
    contact: [`اطلاعات تماس شرکت پلیکم:\n\n• تلفن: ${companyInfo.whatsappPhone}\n• فکس: ${companyInfo.fax}\n• ایمیل: ${companyInfo.email}\n• وب‌سایت: ${companyInfo.website}\n\nآدرس دفتر مرکزی:\n${companyInfo.address}\n\nساعات کاری: شنبه تا پنج‌شنبه، از ساعت 9:00 الی 17:00`],
    samples: [`بله، شرکت پلیکم نمونه‌های آزمایشگاهی را جهت تست و ارزیابی کیفیت در اختیار مشتریان قرار می‌دهد.\n\nجهت ثبت درخواست نمونه:\n• ایمیل: ${companyInfo.email}\n• تلفن: ${companyInfo.whatsappPhone}`],
    thanks: [`خواهش می‌کنم. در صورتی که سوال دیگری دارید، بفرمایید.\n\n• تلفن: ${companyInfo.phone}\n• ایمیل: ${companyInfo.email}`, `خوشحالم که توانستم کمکتان کنم. آیا اطلاعات دیگری نیاز دارید؟`],
    about: [`درباره پلیکم:\n\nشرکت پلیکم در سال 1394 با هدف تولید پلیمرها و کامپاندهای مهندسی پیشرفته تأسیس شد.\n\nحوزه‌های تخصصی ما:\n• تولید کامپاندهای پلیمری پیشرفته\n• تولید مستربچ‌های تخصصی\n• طراحی فرمولاسیون‌های سفارشی\n• ارائه خدمات مشاوره فنی`],
    default: [`با کمال میل آماده راهنمایی شما هستم. ممکن است لطفاً جزئیات بیشتری درباره درخواست خود ارائه دهید؟\n\nمن می‌توانم در زمینه‌های زیر به شما کمک کنم:\n• اطلاعات فنی و معرفی محصولات\n• قیمت و صدور پیش‌فاکتور\n• ثبت سفارش و ارسال نمونه\n• اطلاعات تماس`, `جهت دریافت راهنمایی دقیق، لطفاً با کارشناسان ما تماس بگیرید:\n\n• تلفن: ${companyInfo.whatsappPhone}\n• ایمیل: ${companyInfo.email}`]
  }
}

const detectLanguage = (text) => {
  return /[\u0600-\u06FF]/.test(text) ? 'fa' : 'en'
}

const getResponseFor = (userText, lang) => {
  const productReply = findProductResponse(userText, lang)
  if (productReply) return productReply
  const lower = userText.toLowerCase()
  const currentPatterns = patterns[lang] || patterns.fa
  const currentResponses = responses[lang] || responses.fa
  for (const [category, keywords] of Object.entries(currentPatterns)) {
    if (keywords.some(k => lower.includes(k))) {
      const arr = currentResponses[category] || currentResponses.default
      return arr[Math.floor(Math.random() * arr.length)]
    }
  }
  const arr = currentResponses.default
  return arr[Math.floor(Math.random() * arr.length)]
}

const sendMessage = async () => {
  const text = input.value.trim()
  if (!text) return
  await dispatchMessage(text)
  input.value = ''
}

const sendQuickAction = async (promptText) => {
  await dispatchMessage(promptText)
}

const dispatchMessage = async (text) => {
  const detected = detectLanguage(text)
  language.value = detected

  userHasSentMessage.value = true

  messages.value.push({ id: Date.now(), sender: 'user', text: escapeHtml(text), lang: detected })
  input.value = ''
  isTyping.value = true
  await nextTick()
  if (chatMessages.value) chatMessages.value.scrollTop = chatMessages.value.scrollHeight

  setTimeout(async () => {
    const reply = await Promise.resolve(getResponseFor(text, detected))
    isTyping.value = false
    messages.value.push({ id: Date.now() + 1, sender: 'bot', text: formatResponse(reply), lang: detected })
    await nextTick()
    if (chatMessages.value) chatMessages.value.scrollTop = chatMessages.value.scrollHeight
    if (minimized.value) unreadCount.value += 1
  }, 1000 + Math.random() * 800)
}

const openChat = () => {
  minimized.value = false
  unreadCount.value = 0
  nextTick(() => { if (chatInputRef.value) chatInputRef.value.focus() })
}

const closeChat = () => { minimized.value = true }

const clearChat = () => {
  userHasSentMessage.value = false
  messages.value = [{
    id: Date.now(), sender: 'bot',
    text: language.value === 'fa' ? 'سلام!  من اینجام برای کمک. چطور می‌تونم کمکتون کنم؟' : 'Hello!  I am here to assist. How can I help you?',
    lang: language.value
  }]
}

const escapeHtml = (s) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]))
const formatResponse = (s) => s.replace(/\n/g, '<br/>')

watch([messages, isTyping], async () => {
  await nextTick()
  if (chatMessages.value) chatMessages.value.scrollTop = chatMessages.value.scrollHeight
})

watch(input, () => {
  if (chatInputRef.value) {
    chatInputRef.value.style.fontFamily = /[\u0600-\u06FF]/.test(input.value)
      ? "'IRANYekan', 'Montserrat', sans-serif"
      : "'Montserrat', 'Segoe UI', sans-serif"
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');

@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan.ttf') format('truetype');
  font-weight: 400;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan light.ttf') format('truetype');
  font-weight: 300;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan medium.ttf') format('truetype');
  font-weight: 500;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan bold.ttf') format('truetype');
  font-weight: 700;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

.quick-actions-wrapper {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 4px 0 8px;
  animation: messageIn 0.35s ease;
}

.quick-actions-label {
  font-size: 13px;
  color: #848484;
  font-family: 'IRANYekan', 'Segoe UI', sans-serif;
  font-weight: 500;
  padding: 0 4px;
  line-height: 1.4;
}

.quick-actions-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.quick-action-btn {
  display: block;
  width: 100%;
  padding: 12px 18px;
  background: #ffffff;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 600;
  color: #555555;
  font-family: 'IRANYekan', 'Segoe UI', sans-serif;
  text-align: right;
  cursor: pointer;
  transition: all 0.18s ease;
  line-height: 1.3;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}

.quick-action-btn:hover {
  background: #ffd000;
  border-color: #ffd000;
  color: #ffffff;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(255,208,0,0.35);
}

.quick-action-btn:active {
  transform: translateY(0);
  box-shadow: 0 1px 4px rgba(255,208,0,0.2);
}

.quick-actions-fade-enter-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.quick-actions-fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.quick-actions-fade-enter-from {
  opacity: 0;
  transform: translateY(8px);
}
.quick-actions-fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}

.contact-launcher {
  position: fixed;
  bottom: 90px;
  right: 0;
  z-index: 99997;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  font-family: 'IRANYekan', 'Segoe UI', sans-serif;
}

.launcher-pill {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #848484;
  border: none;
  border-radius: 14px 0 0 14px;
  padding: 10px 12px;
  cursor: pointer;
  box-shadow: 4px 4px 18px rgba(0,0,0,0.15);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  outline: none;
}
.launcher-pill:hover {
  transform: translateX(4px);
  box-shadow: 6px 6px 24px rgba(0,0,0,0.2);
}

.pill-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 9px;
  border-radius: 8px;
  transition: background 0.15s;
  color: #ffd000;
}
.pill-icon-wrap:hover { background: rgba(0,0,0,0.08); }
.pill-icon { width: 28px; height: 28px; display: block; }
.pill-divider { width: 24px; height: 1px; background: rgba(0,0,0,0.15); margin: 3px 0; }

.launcher-panel {
  background: #808285;
  border-radius: 16px 0 0 16px;
  box-shadow: 6px 6px 32px rgba(0,0,0,0.18);
  padding: 16px 16px 18px 24px;
  min-width: 240px;
  width: auto;
  position: absolute;
  bottom: 0;
  right: 0;
  overflow: visible;
}
.launcher-panel::before {
  content: '';
  position: absolute;
  top: 0; right: 0; left: 0;
  height: 3px;
  background: #ffd000;
  border-radius: 16px 0 0 0;
}

.panel-close-btn {
  position: absolute;
  top: 10px; left: 10px;
  width: 28px; height: 28px;
  display: flex; align-items: center; justify-content: center;
  background: rgba(240, 239, 238, 0.15);
  border: none; border-radius: 50%;
  cursor: pointer; color: #ffd000;
  transition: background 0.15s, transform 0.15s;
}
.panel-close-btn:hover { background: rgba(255,255,255,0.4); transform: scale(1.1); }

.panel-action-row {
  display: flex; align-items: center; gap: 10px;
  width: 100%; background: none; border: none;
  cursor: pointer; padding: 8px 4px 8px 6px;
  border-radius: 8px; text-align: right;
  transition: background 0.15s;
  color: #ffd000; margin-top: 2px;
  flex-direction: row-reverse;
}
.panel-action-row:hover { background: rgba(255,208,0,0.1); }

.panel-action-icon.whatsapp-icon { color: #25D366; }

.panel-action-icon {
  display: flex; align-items: center; justify-content: center;
  width: 48px; height: 48px;
  border-radius: 12px; flex-shrink: 0; color: #ffd000;
}
.panel-action-icon svg { width: 32px; height: 32px; }
.panel-action-label {
  font-size: 15px; font-weight: 600; color: #ffffff;
  font-family: 'IRANYekan', 'Segoe UI', sans-serif; white-space: nowrap;
}

.panel-sep { height: 1px; background: rgba(19, 19, 19, 0.3); margin: 6px 0; }

.panel-call-group { padding-top: 2px; }

.panel-phone-link {
  font-size: 18px; font-weight: 500; color: #ffd000;
  text-decoration: none; font-family: 'Montserrat', sans-serif;
  letter-spacing: 0.4px; display: block; line-height: 1.3;
  transition: opacity 0.15s; white-space: nowrap;
}
.panel-phone-link:hover { opacity: 0.8; text-decoration: underline; }
.panel-phone-sub { padding: 4px 0 2px 0; text-align: right; }
.panel-local-link {
  font-size: 11.5px; color: rgba(0,0,0,0.6);
  text-decoration: underline; text-underline-offset: 2px;
  cursor: pointer; font-family: 'IRANYekan', 'Segoe UI', sans-serif;
  transition: color 0.15s; white-space: nowrap; display: block;
}
.panel-local-link:hover { color: #ffd000; }

.pill-fade-enter-active, .pill-fade-leave-active { transition: opacity 0.2s ease, transform 0.2s ease; }
.pill-fade-enter-from, .pill-fade-leave-to { opacity: 0; transform: translateX(-20px); }
.panel-slide-enter-active { transition: opacity 0.25s ease, transform 0.25s cubic-bezier(0.34,1.2,0.64,1); }
.panel-slide-leave-active { transition: opacity 0.18s ease, transform 0.18s ease; }
.panel-slide-enter-from { opacity: 0; transform: translateX(-30px); }
.panel-slide-leave-from { opacity: 1; transform: translateX(0); }
.panel-slide-leave-to { opacity: 0; transform: translateX(-30px) !important; }

.chat-window {
  position: fixed;
  bottom: 30px; right: 30px;
  width: 420px; height: 650px;
  background: white;
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.15);
  display: none; flex-direction: column;
  overflow: hidden;
  z-index: 99999;
  direction: rtl;
}
.chat-window.active { display: flex; animation: slideUp 0.4s cubic-bezier(0.25,0.8,0.25,1); }

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px) scale(0.9); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

.chat-header {
  background: #848484;
  padding: 24px;
  display: flex; align-items: center; justify-content: space-between;
  flex-direction: row-reverse;
}
.header-left { display: flex; align-items: center; gap: 14px; flex-direction: row-reverse; }
.header-avatar {
  width: 50px; height: 50px;
  background: #bdbbbb; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  overflow: hidden;
}
.header-avatar img { width: 100%; height: 100%; object-fit: contain; display: block; }
.header-info h2 { font-size: 19px; font-weight: 700; color: #ffffff; margin-bottom: 4px; font-family: 'IRANYekan', sans-serif; }
.header-status { display: flex; align-items: center; gap: 6px; font-size: 13px; color: #ffffff; }
.header-actions { display: flex; gap: 8px; flex-direction: row-reverse; }
.header-btn {
  width: 38px; height: 38px;
  background: #ffd000; border: none; border-radius: 50%;
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  transition: all 0.2s;
}
.header-btn:hover { background: rgba(0,0,0,0.2); transform: scale(1.1); }
.header-btn svg { width: 22px; height: 22px; color: #757575; }

.chat-messages {
  flex: 1; padding: 24px;
  overflow-y: auto;
  background: #f1f2f2;
  display: flex; flex-direction: column; gap: 16px;
}
.chat-messages::-webkit-scrollbar { width: 8px; }
.chat-messages::-webkit-scrollbar-thumb { background: #d1d1d1; border-radius: 10px; }
.chat-messages::-webkit-scrollbar-thumb:hover { background: #848484; }

.message {
  display: flex; align-items: flex-end; gap: 10px;
  animation: messageIn 0.3s ease;
}
@keyframes messageIn {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
.message.user { flex-direction: row; }
.message-avatar {
  width: 36px; height: 36px;
  background: #bdbbbb; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.message.user .message-avatar { background: #ffd000; }
.message-avatar svg { width: 18px; height: 18px; color: white; }
.message-avatar img { width: 100%; height: 100%; object-fit: contain; border-radius: 50%; }

.message-bubble {
  max-width: 70%; padding: 14px 18px;
  border-radius: 20px; font-size: 15px;
  line-height: 1.5; word-wrap: break-word;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  background: white; color: #848484;
  font-family: 'IRANYekan', 'Segoe UI', sans-serif;
}
.message[dir="rtl"] .message-bubble { font-family: 'IRANYekan', 'Segoe UI', sans-serif; }
.message.bot .message-bubble { border-bottom-left-radius: 6px; }
.message.user .message-bubble {
  background: #ffd000; color: #ffffff;
  border-bottom-right-radius: 6px;
  font-weight: 500;
}
.message.user[dir="rtl"] .message-bubble { font-family: 'IRANYekan', 'Segoe UI', sans-serif; }

.typing-indicator {
  display: flex; gap: 6px;
  padding: 14px 18px;
  background: white; border-radius: 20px;
  border-bottom-left-radius: 6px;
  width: fit-content;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.typing-dot {
  width: 10px; height: 10px;
  background: #848484; border-radius: 50%;
  animation: typingBounce 1.4s ease-in-out infinite;
}
.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes typingBounce {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-12px); }
}

.chat-input-area {
  padding: 20px 24px; background: white;
  border-top: 2px solid #e5e5e5;
  display: flex; gap: 12px; align-items: center;
  flex-direction: row-reverse;
}
.chat-input {
  flex: 1; padding: 14px 18px;
  border: 2px solid #d1d1d1; border-radius: 25px;
  font-size: 15px; outline: none;
  transition: all 0.2s; background: #f9f9f9;
  font-family: 'IRANYekan', 'Segoe UI', sans-serif;
  text-align: right;
}
.chat-input:focus { border-color: #ffd000; background: white; box-shadow: 0 0 0 4px rgba(251,191,36,0.1); }
.chat-input::placeholder { color: #999; }

.send-btn {
  width: 52px; height: 52px;
  background: #ffd000; border: none; border-radius: 50%;
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(251,191,36,0.4);
}
.send-btn:hover { transform: scale(1.1); box-shadow: 0 6px 16px rgba(251,191,36,0.5); }
.send-btn:active { transform: scale(0.95); }
.send-btn svg { width: 28px; height: 28px; }

@media (max-width: 768px) {
  .contact-launcher {
    bottom: calc(env(safe-area-inset-bottom, 0px) + 130px);
    right: 0;
    z-index: 120000 !important;
  }
  .launcher-pill { padding: 8px 10px; border-radius: 12px 0 0 12px; }
  .pill-icon { width: 28px; height: 28px; }
    .launcher-panel { min-width: 205px; padding: 14px 14px 14px 16px; border-radius: 14px 0 0 14px; }
  .panel-action-label { font-size: 14px; }
  .panel-phone-link { font-size: 16px; }

  .chat-window {
    position: fixed; right: 12px; left: auto;
    bottom: calc(env(safe-area-inset-bottom, 0px) + 30px);
    width: calc(100% - 24px); height: calc(70vh);
    max-height: calc(100vh - (env(safe-area-inset-top, 0px) + 140px));
    border-radius: 14px;
  }
  .chat-header { padding: 12px 14px; }
  .header-avatar { width: 42px; height: 42px; }
  .header-info h2 { font-size: 15px; }
  .header-btn { width: 34px; height: 34px; }
  .chat-messages { padding: 14px; gap: 12px; -webkit-overflow-scrolling: touch; }
  .message-bubble { font-size: 14px; padding: 10px 14px; max-width: 78%; }
  .chat-input-area { padding: 10px 12px; gap: 8px; }
  .chat-input { padding: 10px 12px; font-size: 14px; }
  .send-btn { width: 44px; height: 44px; }

  .quick-action-btn { font-size: 13px; padding: 10px 14px; }
  .quick-actions-label { font-size: 12px; }
}
</style>
