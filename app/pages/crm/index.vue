<!--
  داشبورد CRM فروش — نسخه متصل به بک‌اند
  ============================================
  - اتصال کامل به Flask API با احراز هویت JWT
  - ایمپورت اکسل (XLS SpreadsheetML از نرم‌افزار حسابداری)
  - بازه تاریخ دستی در فیلترها
  - ادیت و حذف مستقیم در گزارش فروش
  - فاکتور برگشتی (نوع سند = برگشت از فروش)
-->
<script setup>
import { ref, reactive, computed, onMounted, onUnmounted, nextTick, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useCrmAuth } from '~/composables/useCrmAuth'

// این صفحه فقط برای کاربران لاگین‌شده در دسترس است
definePageMeta({
  middleware: 'crm-auth',
})

const router = useRouter()
const { getCrmToken, getCrmUser, clearCrmToken } = useCrmAuth()
const currentUser = ref(getCrmUser())

/* ==========================================================================
   ۱) تنظیمات بک‌اند
   ========================================================================== */
// آدرس بک‌اند — موقع دیپلوی روی هاست تغییر بده
const API_BASE = import.meta.env.VITE_API_BASE || 'https://crmapi.polychemmb.com'

async function apiFetch(path, options = {}) {
  const token = getCrmToken()
  const res = await fetch(`${API_BASE}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
    ...options,
  })

  // اگر توکن منقضی/نامعتبر بود، خارج کن و به لاگین بفرست
  if (res.status === 401) {
    clearCrmToken()
    router.push('/Crm/login')
    throw new Error('نشست شما منقضی شده است. دوباره وارد شوید.')
  }

  const json = await res.json()
  if (!res.ok) throw new Error(json.message || `خطای سرور ${res.status}`)
  return json
}

function handleLogout() {
  clearCrmToken()
  router.push('/Crm/login')
}

/* ==========================================================================
   ۲) داده‌های پایه (از بک‌اند)
   ========================================================================== */
const provinces = ref([])
const industries = ref([])
const paymentMethods = ref([])
const products = ref([])
const customers = ref([])
const allSales = ref([])

async function loadLookups() {
  const [pr, ind, pm, prod] = await Promise.all([
    apiFetch('/api/provinces'),
    apiFetch('/api/industries'),
    apiFetch('/api/payment-methods'),
    apiFetch('/api/products'),
  ])
  provinces.value = pr.data.map(x => x.name)
  industries.value = ind.data.map(x => x.name)
  paymentMethods.value = pm.data.map(x => x.name)
  products.value = prod.data
}

async function loadCustomers() {
  const res = await apiFetch('/api/customers?perPage=200')
  customers.value = res.data
}

async function loadSales(params = {}) {
  const qs = new URLSearchParams({ perPage: 200, ...params }).toString()
  const res = await apiFetch(`/api/sales?${qs}`)
  allSales.value = res.data
}

/* ==========================================================================
   ۳) وضعیت کلی صفحه
   ========================================================================== */
const isLoading = ref(true)
const isDark = ref(false)
const toast = reactive({ show: false, message: '', type: 'success' })
let toastTimer = null

function showToast(message, type = 'success') {
  toast.message = message; toast.type = type; toast.show = true
  clearTimeout(toastTimer)
  toastTimer = setTimeout(() => { toast.show = false }, 3200)
}
function toggleDark() {
  isDark.value = !isDark.value
  try { localStorage.setItem('sales-dashboard-theme', isDark.value ? 'dark' : 'light') } catch (e) {}
}

/* ==========================================================================
   ۴) ناوبری تب‌ها
   ========================================================================== */
const tabs = [
  { key: 'main', label: 'داشبورد اصلی', icon: 'home' },
  { key: 'report', label: 'گزارش فروش', icon: 'chart' },
  { key: 'manage', label: 'مدیریت فروش', icon: 'list' },
  { key: 'customers', label: 'مشتریان', icon: 'users' },
  { key: 'settings', label: 'تنظیمات کلی', icon: 'gear' },
]
const activeTab = ref('main')
const profileMenuOpen = ref(false)
const sidebarOpenMobile = ref(false)

function setTab(key) {
  activeTab.value = key
  sidebarOpenMobile.value = false
  nextTick(() => {
    if (isLoading.value || !ApexCharts) return
    if (key === 'main') renderMainCharts()
    if (key === 'report') renderReportCharts()
  })
}

/* ==========================================================================
   ۵) ابزارهای کمکی
   ========================================================================== */
function toFaNum(n) { return Number(n).toLocaleString('fa-IR') }

// نمایش تاریخ — چون بک‌اند رشته شمسی می‌فرستد مستقیم نمایش داده می‌شود
function displayDate(d) {
  if (!d) return '—'
  if (typeof d === 'string' && d.includes('/')) return d  // شمسی: 1405/10/05
  if (typeof d === 'string' && d.includes('-') && d.length === 10) {
    // ISO میلادی — فقط string برگردان (نباید بیاد ولی safe باشیم)
    return d
  }
  return String(d)
}

function formatRial(n) { return toFaNum(Math.round(n || 0)) + ' ریال' }

// فشرده برای نمایش در KPI کارت‌ها — بدون "ریال" برای توضیح جداگانه
function formatRialCompact(n) {
  const abs = Math.abs(n || 0)
  const sign = (n || 0) < 0 ? '−' : ''
  if (abs >= 1e12) return sign + toFaNum(Number((abs / 1e12).toFixed(2))) + ' تریلیون ریال'
  if (abs >= 1e9)  return sign + toFaNum(Number((abs / 1e9).toFixed(1)))  + ' میلیارد ریال'
  if (abs >= 1e6)  return sign + toFaNum(Number((abs / 1e6).toFixed(1)))  + ' میلیون ریال'
  if (abs >= 1e3)  return sign + toFaNum(Number((abs / 1e3).toFixed(0)))  + ' هزار ریال'
  return sign + toFaNum(Math.round(abs)) + ' ریال'
}

// فشرده برای axis/tooltip نمودارها — واحد اضافه نمی‌کند (tooltip خودش می‌زند)
function fmtAxisRial(n) {
  const abs = Math.abs(n || 0)
  if (abs >= 1e12) return toFaNum(Number((abs / 1e12).toFixed(1))) + 'T'
  if (abs >= 1e9)  return toFaNum(Number((abs / 1e9).toFixed(1)))  + 'B'
  if (abs >= 1e6)  return toFaNum(Number((abs / 1e6).toFixed(0)))  + 'M'
  if (abs >= 1e3)  return toFaNum(Number((abs / 1e3).toFixed(0)))  + 'K'
  return toFaNum(Math.round(abs))
}

// فرمت کیلوگرم با واحد مناسب
function formatKg(n) {
  const abs = Math.abs(n || 0)
  const sign = (n || 0) < 0 ? '−' : ''
  if (abs >= 1e6) return sign + toFaNum(Number((abs / 1e6).toFixed(2))) + ' هزار تن'
  if (abs >= 1e3) return sign + toFaNum(Number((abs / 1e3).toFixed(1))) + ' تن'
  return sign + toFaNum(Math.round(abs)) + ' کگ'
}

function formatTon(n) { return formatKg(n) }

// تبدیل تاریخ شمسی (YYYY/M/D یا YYYY/MM/DD) به عدد واقعاً قابل مقایسه
// نکته مهم: قبلاً این تابع فقط "/" رو حذف می‌کرد و رشته رو به عدد تبدیل می‌کرد،
// که اگر ماه/روز از بک‌اند بدون صفر ابتدایی می‌اومد (مثلاً 1404/9/5)، ترتیب
// اشتباه از آب درمی‌اومد. اینجا هر بخش جدا پارس و با ارزش مکانی درست جمع می‌شود.
function jalaliToNum(d) {
  if (!d) return 0
  const parts = String(d).split('/')
  if (parts.length < 3) return 0
  const y = parseInt(parts[0], 10) || 0
  const m = parseInt(parts[1], 10) || 0
  const day = parseInt(parts[2], 10) || 0
  return y * 10000 + m * 100 + day
}

/* ==========================================================================
   ۶) محاسبات آماری
   ========================================================================== */
const customerStats = computed(() => {
  const map = {}
  customers.value.forEach(c => { map[c.name] = { amount: 0, tons: 0, count: 0, lastDate: '—' } })
  allSales.value.forEach(s => {
    const m = map[s.customer]
    if (!m) return
    m.amount += s.amount; m.tons += s.tons; m.count += 1
    if (!m.lastDate || m.lastDate === '—' || jalaliToNum(s.dateLabel) > jalaliToNum(m.lastDate)) m.lastDate = s.dateLabel
  })
  return map
})
function statFor(name) { return customerStats.value[name] || { amount: 0, tons: 0, count: 0, lastDate: '—' } }

const monthLabels = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

/* ==========================================================================
   ۷) فیلترهای پیشرفته (با بازه تاریخ دستی)
   ========================================================================== */
function defaultFilterState() {
  return {
    range: 'all',         // all | 1 | 3 | 6 | custom
    dateFrom: '',         // بازه دستی: از تاریخ (شمسی YYYY/MM/DD)
    dateTo: '',           // بازه دستی: تا تاریخ (شمسی YYYY/MM/DD)
    year: 'all',
    month: 'all',
    customer: 'all',
    product: 'all',
    province: 'all',
    industry: 'all',
    saleType: 'all',
    payment: 'all',
    docType: 'all',       // all | فاكتور | برگشتی
  }
}
const draftFilters = reactive(defaultFilterState())
const appliedFilters = reactive(defaultFilterState())
const hasActiveFilters = computed(() => Object.keys(appliedFilters).some(k => appliedFilters[k] !== 'all' && appliedFilters[k] !== ''))

function applyFilters() {
  Object.assign(appliedFilters, draftFilters)
  currentPage.value = 1
  showToast('فیلترها اعمال شد', 'success')
  nextTick(() => { if (!isLoading.value && ApexCharts) renderReportCharts() })
}
function resetFilters() {
  Object.assign(draftFilters, defaultFilterState())
  Object.assign(appliedFilters, defaultFilterState())
  currentPage.value = 1
  showToast('فیلترها پاک شد', 'info')
  nextTick(() => { if (!isLoading.value && ApexCharts) renderReportCharts() })
}

const filteredSales = computed(() => {
  return allSales.value.filter(s => {
    const dateNum = jalaliToNum(s.dateLabel)

    // بازه زمانی آماده
    if (appliedFilters.range === '1') {
      const cutoff = jalaliToNum(getCurrentJalaliMinus(1))
      if (dateNum < cutoff) return false
    }
    if (appliedFilters.range === '3') {
      const cutoff = jalaliToNum(getCurrentJalaliMinus(3))
      if (dateNum < cutoff) return false
    }
    if (appliedFilters.range === '6') {
      const cutoff = jalaliToNum(getCurrentJalaliMinus(6))
      if (dateNum < cutoff) return false
    }
    // بازه دستی
    if (appliedFilters.range === 'custom') {
      if (appliedFilters.dateFrom && dateNum < jalaliToNum(appliedFilters.dateFrom)) return false
      if (appliedFilters.dateTo && dateNum > jalaliToNum(appliedFilters.dateTo)) return false
    }

    if (appliedFilters.year !== 'all' && !s.dateLabel?.startsWith(appliedFilters.year)) return false
    if (appliedFilters.customer !== 'all' && s.customer !== appliedFilters.customer) return false
    if (appliedFilters.product !== 'all' && s.product !== appliedFilters.product) return false
    if (appliedFilters.province !== 'all' && s.province !== appliedFilters.province) return false
    if (appliedFilters.industry !== 'all' && s.industry !== appliedFilters.industry) return false
    if (appliedFilters.saleType !== 'all' && s.saleType !== appliedFilters.saleType) return false
    if (appliedFilters.payment !== 'all' && s.payment !== appliedFilters.payment) return false
    if (appliedFilters.docType !== 'all') {
      if (appliedFilters.docType === 'برگشتی' && !s.isReturn) return false
      if (appliedFilters.docType === 'فاكتور' && s.isReturn) return false
    }
    return true
  })
})

// ==========================================================================
// تبدیل دقیق میلادی → شمسی (الگوریتم استاندارد jalaali)
// ==========================================================================
function gregorianToJalali(gy, gm, gd) {
  const g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
  let gy2 = (gm > 2) ? (gy + 1) : gy
  let days = 355666 + (365 * gy) + Math.floor((gy2 + 3) / 4) - Math.floor((gy2 + 99) / 100) +
    Math.floor((gy2 + 399) / 400) + gd + g_d_m[gm - 1]
  let jy = -1595 + (33 * Math.floor(days / 12053))
  days %= 12053
  jy += 4 * Math.floor(days / 1461)
  days %= 1461
  if (days > 365) {
    jy += Math.floor((days - 1) / 365)
    days = (days - 1) % 365
  }
  let jm, jd
  if (days < 186) {
    jm = 1 + Math.floor(days / 31)
    jd = 1 + (days % 31)
  } else {
    jm = 7 + Math.floor((days - 186) / 30)
    jd = 1 + ((days - 186) % 30)
  }
  return { jy, jm, jd }
}

// تاریخ شمسی امروز به فرمت YYYY/MM/DD
function todayJalaliStr() {
  const now = new Date()
  const { jy, jm, jd } = gregorianToJalali(now.getFullYear(), now.getMonth() + 1, now.getDate())
  return `${jy}/${String(jm).padStart(2, '0')}/${String(jd).padStart(2, '0')}`
}

// N ماه شمسی قبل از امروز — با کم کردن صحیح ماه/سال شمسی (نه میلادی)
function getCurrentJalaliMinus(months) {
  const now = new Date()
  const { jy, jm, jd } = gregorianToJalali(now.getFullYear(), now.getMonth() + 1, now.getDate())
  let totalMonths = (jy * 12 + (jm - 1)) - months
  const newJy = Math.floor(totalMonths / 12)
  const newJm = (totalMonths % 12) + 1
  return `${newJy}/${String(newJm).padStart(2, '0')}/${String(jd).padStart(2, '0')}`
}

const customerOptions = computed(() => customers.value.map(c => c.name))
const productOptions = computed(() => products.value.map(p => p.name))

/* ==========================================================================
   ۸) KPI های داشبورد
   ========================================================================== */
const totalRial = computed(() => filteredSales.value.reduce((a, s) => a + (s.isReturn ? -s.amount : s.amount), 0))
const totalTon = computed(() => filteredSales.value.reduce((a, s) => a + (s.isReturn ? -s.tons : s.tons), 0))
const uniqueCustomerCount = computed(() => new Set(filteredSales.value.map(s => s.customer)).size)
const avgSale = computed(() => filteredSales.value.length ? Math.abs(totalRial.value) / filteredSales.value.length : 0)
const returnCount = computed(() => filteredSales.value.filter(s => s.isReturn).length)

function topEntity(keyFn) {
  const map = {}
  filteredSales.value.forEach(s => {
    const k = keyFn(s)
    if (!map[k]) map[k] = { name: k, amount: 0, tons: 0 }
    map[k].amount += s.isReturn ? -s.amount : s.amount
    map[k].tons += s.isReturn ? -s.tons : s.tons
  })
  return Object.values(map).sort((a, b) => b.amount - a.amount)[0] || null
}
const topCustomerAll = computed(() => topEntity(s => s.customer))
const topProductAll = computed(() => {
  const map = {}
  filteredSales.value.forEach(s => { map[s.product] = (map[s.product] || 0) + (s.isReturn ? -s.tons : s.tons) })
  const arr = Object.entries(map).sort((a, b) => b[1] - a[1])
  return arr.length ? { name: arr[0][0], tons: arr[0][1] } : null
})

// آمار ماهانه از داده‌های واقعی — مرتب بر اساس سال/ماه
const monthlyAgg = computed(() => {
  const map = {}
  filteredSales.value.forEach(s => {
    const parts = (s.dateLabel || '').split('/')
    if (parts.length < 3) return
    const year  = parts[0]
    const mNum  = parseInt(parts[1])
    if (!mNum || mNum < 1 || mNum > 12) return
    // کلید ترکیب سال+ماه برای مرتب‌سازی صحیح چند‌ساله
    const key   = `${year}/${String(mNum).padStart(2,'0')}`
    const label = monthLabels[mNum - 1] || parts[1]
    if (!map[key]) map[key] = { key, label, mNum, year, tons: 0, rial: 0 }
    map[key].tons += s.isReturn ? -s.tons : s.tons
    map[key].rial += s.isReturn ? -s.amount : s.amount
  })
  // مرتب‌سازی زمانی صحیح
  return Object.values(map).sort((a, b) => a.key.localeCompare(b.key))
})

const yearlyAgg = computed(() => {
  const map = {}
  filteredSales.value.forEach(s => {
    const y = (s.dateLabel || '').split('/')[0]
    if (!y) return
    if (!map[y]) map[y] = { label: y, tons: 0, rial: 0 }
    map[y].tons += s.isReturn ? -s.tons : s.tons
    map[y].rial += s.isReturn ? -s.amount : s.amount
  })
  return Object.values(map).sort((a, b) => a.label.localeCompare(b.label))
})

const monthlyKpis = computed(() => [
  { key: 'rial', featured: true, icon: 'coin', label: 'مجموع فروش خالص (ریال)', value: formatRialCompact(totalRial.value), dir: totalRial.value >= 0 ? 'up' : 'down', trend: null },
  { key: 'ton', featured: true, icon: 'box', label: 'مجموع مقدار خالص (کیلوگرم)', value: formatTon(totalTon.value), dir: totalTon.value >= 0 ? 'up' : 'down', trend: null },
  { key: 'customers', icon: 'users', label: 'تعداد مشتریان', value: toFaNum(uniqueCustomerCount.value), dir: null, note: 'مشتری در بازه انتخابی' },
  { key: 'avg', icon: 'chart', label: 'میانگین فروش', value: formatRialCompact(avgSale.value), dir: null, note: 'به‌ازای هر فاکتور' },
  { key: 'returns', icon: 'warning', label: 'فاکتور برگشتی', value: toFaNum(returnCount.value), dir: null, note: 'در بازه انتخابی' },
  { key: 'topCustomer', icon: 'star', label: 'بهترین مشتری', value: topCustomerAll.value?.name || '—', dir: null, note: topCustomerAll.value ? formatRialCompact(topCustomerAll.value.amount) : '' },
  { key: 'topProduct', icon: 'medal', label: 'پرفروش‌ترین محصول', value: topProductAll.value?.name || '—', dir: null, note: topProductAll.value ? formatTon(topProductAll.value.tons) : '' },
  { key: 'total', icon: 'calendar', label: 'تعداد کل فاکتور', value: toFaNum(filteredSales.value.length), dir: null, note: 'فاکتور در بازه انتخابی' },
])

/* ==========================================================================
   ۹) داده‌های نمودار
   ========================================================================== */
function groupTopN(arr, keyFn, valFn, n) {
  const map = {}
  arr.forEach(item => { const k = keyFn(item); map[k] = (map[k] || 0) + valFn(item) })
  const entries = Object.entries(map).sort((a, b) => b[1] - a[1])
  const top = entries.slice(0, n)
  const rest = entries.slice(n).reduce((a, [, v]) => a + v, 0)
  if (rest > 0) top.push(['سایر', rest])
  return top
}
// فروش بر اساس محصول — ریالی
const byProduct = computed(() => groupTopN(filteredSales.value, s => s.product, s => s.isReturn ? -s.amount : s.amount, 8))
// فروش بر اساس محصول — تناژ (کیلوگرم)
const byProductTon = computed(() => groupTopN(filteredSales.value, s => s.product, s => s.isReturn ? -s.tons : s.tons, 8))
const byCustomer = computed(() => groupTopN(filteredSales.value, s => s.customer, s => s.isReturn ? -s.amount : s.amount, 6))
const byType = computed(() => {
  const map = {}
  filteredSales.value.forEach(s => { const k = s.isReturn ? 'برگشتی' : s.saleType; map[k] = (map[k] || 0) + s.amount })
  return Object.entries(map)
})

/* ==========================================================================
   ۱۰) نمودارها (ApexCharts)
   ========================================================================== */
let ApexCharts = null
const charts = {}
const elTonMain = ref(null), elRialMain = ref(null)
const elYearCompare = ref(null), elYearGrowth = ref(null)
const elTon = ref(null), elRial = ref(null)
const elProduct = ref(null), elProductTon = ref(null), elProductRial = ref(null), elCustomer = ref(null)
const elType = ref(null)

function destroyChart(key) { if (charts[key]) { try { charts[key].destroy() } catch (e) {} charts[key] = null } }
function chartForeColor() { return isDark.value ? '#C7C7C9' : '#58585B' }
function chartGrid() { return isDark.value ? '#2E2E30' : '#E6E6E7' }
function tooltipTheme() { return isDark.value ? 'dark' : 'light' }
const baseFont = 'Vazirmatn, sans-serif'

function renderMainCharts() {
  if (!ApexCharts) return
  const months = monthlyAgg.value
  const cats   = months.map(m => m.label)   // نام ماه فارسی

  destroyChart('tonMain')
  if (elTonMain.value && months.length) {
    charts.tonMain = new ApexCharts(elTonMain.value, {
      chart: { type: 'bar', height: 280, toolbar: { show: false }, fontFamily: baseFont, background: 'transparent', foreColor: chartForeColor() },
      series: [{ name: 'مقدار', data: months.map(m => +(m.tons.toFixed(1))) }],
      xaxis: { categories: cats, axisBorder: { show: false }, axisTicks: { show: false }, labels: { rotate: -30 } },
      yaxis: { labels: { formatter: v => formatKg(v) } },
      grid: { borderColor: chartGrid(), strokeDashArray: 4 },
      colors: ['#58585B'], plotOptions: { bar: { borderRadius: 5, columnWidth: '55%' } },
      dataLabels: { enabled: false },
      tooltip: { theme: tooltipTheme(), y: { formatter: v => formatKg(v) } },
    })
    charts.tonMain.render()
  }

  destroyChart('rialMain')
  if (elRialMain.value && months.length) {
    charts.rialMain = new ApexCharts(elRialMain.value, {
      chart: { type: 'area', height: 280, toolbar: { show: false }, fontFamily: baseFont, background: 'transparent', foreColor: chartForeColor() },
      series: [{ name: 'فروش', data: months.map(m => Math.round(m.rial)) }],
      xaxis: { categories: cats, labels: { rotate: -30 } },
      yaxis: { labels: { formatter: v => fmtAxisRial(v) } },
      stroke: { curve: 'smooth', width: 3 },
      fill: { type: 'gradient', gradient: { shadeIntensity: 1, opacityFrom: 0.45, opacityTo: 0.05 } },
      colors: ['#FFCD05'], grid: { borderColor: chartGrid(), strokeDashArray: 4 },
      dataLabels: { enabled: false },
      tooltip: { theme: tooltipTheme(), y: { formatter: v => formatRialCompact(v) } },
    })
    charts.rialMain.render()
  }

  destroyChart('yearCompare')
  if (elYearCompare.value && yearlyAgg.value.length) {
    charts.yearCompare = new ApexCharts(elYearCompare.value, {
      chart: { type: 'bar', height: 280, toolbar: { show: false }, fontFamily: baseFont, background: 'transparent', foreColor: chartForeColor() },
      series: [{ name: 'فروش', data: yearlyAgg.value.map(y => Math.round(y.rial)) }],
      xaxis: { categories: yearlyAgg.value.map(y => y.label) },
      yaxis: { labels: { formatter: v => fmtAxisRial(v) } },
      grid: { borderColor: chartGrid(), strokeDashArray: 4 },
      colors: ['#FFCD05'], plotOptions: { bar: { borderRadius: 8, columnWidth: '48%', distributed: true } },
      legend: { show: false }, dataLabels: { enabled: false },
      tooltip: { theme: tooltipTheme(), y: { formatter: v => formatRialCompact(v) } },
    })
    charts.yearCompare.render()
  }

  destroyChart('yearGrowth')
  if (elYearGrowth.value && yearlyAgg.value.length) {
    charts.yearGrowth = new ApexCharts(elYearGrowth.value, {
      chart: { type: 'line', height: 280, toolbar: { show: false }, fontFamily: baseFont, background: 'transparent', foreColor: chartForeColor() },
      series: [{ name: 'تناژ', data: yearlyAgg.value.map(y => +(y.tons.toFixed(1))) }],
      xaxis: { categories: yearlyAgg.value.map(y => y.label) },
      yaxis: { labels: { formatter: v => formatKg(v) } },
      stroke: { curve: 'smooth', width: 3 }, markers: { size: 5 },
      colors: ['#FFCD05'], grid: { borderColor: chartGrid(), strokeDashArray: 4 },
      dataLabels: { enabled: false },
      tooltip: { theme: tooltipTheme(), y: { formatter: v => formatKg(v) } },
    })
    charts.yearGrowth.render()
  }
}

function renderReportCharts() {
  if (!ApexCharts) return

  const monthly = monthlyAgg.value
  // اگه داده ماهانه خالی بود نمودار نساز
  const hasMonthly = monthly.length > 0

  // ۱) فروش ماهانه — تناژ (کیلوگرم)
  destroyChart('ton')
  if (elTon.value && hasMonthly) {
    charts.ton = new ApexCharts(elTon.value, {
      chart: { type: 'bar', height: 290, toolbar: { show: false }, fontFamily: baseFont, background: 'transparent', foreColor: chartForeColor() },
      series: [{ name: 'کیلوگرم', data: monthly.map(m => Math.round(m.tons)) }],
      xaxis: { categories: monthly.map(m => `${m.label} ${m.year}`), labels: { rotate: -30, style: { fontSize: '11px' } } },
      yaxis: { labels: { formatter: v => formatKg(v) } },
      grid: { borderColor: chartGrid(), strokeDashArray: 4 },
      colors: ['#58585B'], plotOptions: { bar: { borderRadius: 5, columnWidth: '55%' } },
      dataLabels: { enabled: false },
      tooltip: { theme: tooltipTheme(), y: { formatter: v => formatKg(v) } },
    })
    charts.ton.render()
  }

  // ۲) فروش ماهانه — ریالی
  destroyChart('rial')
  if (elRial.value && hasMonthly) {
    charts.rial = new ApexCharts(elRial.value, {
      chart: { type: 'area', height: 290, toolbar: { show: false }, fontFamily: baseFont, background: 'transparent', foreColor: chartForeColor() },
      series: [{ name: 'ریال', data: monthly.map(m => Math.round(m.rial)) }],
      xaxis: { categories: monthly.map(m => `${m.label} ${m.year}`), labels: { rotate: -30, style: { fontSize: '11px' } } },
      yaxis: { labels: { formatter: v => fmtAxisRial(v) } },
      stroke: { curve: 'smooth', width: 3 },
      fill: { type: 'gradient', gradient: { shadeIntensity: 1, opacityFrom: 0.4, opacityTo: 0.05 } },
      colors: ['#FFCD05'],
      grid: { borderColor: chartGrid(), strokeDashArray: 4 }, dataLabels: { enabled: false },
      tooltip: { theme: tooltipTheme(), y: { formatter: v => formatRialCompact(v) } },
    })
    charts.rial.render()
  }

  // ۳) فروش بر اساس محصول — ریالی (افقی)
  destroyChart('product')
  if (elProduct.value) {
    const data = byProduct.value.filter(d => d[1] > 0)
    if (data.length) {
      charts.product = new ApexCharts(elProduct.value, {
        chart: { type: 'bar', height: Math.max(300, data.length * 45 + 60), toolbar: { show: false }, fontFamily: baseFont, background: 'transparent', foreColor: chartForeColor() },
        series: [{ name: 'مبلغ (ریال)', data: data.map(d => Math.round(d[1])) }],
        xaxis: {
          categories: data.map(d => d[0]),
          labels: { formatter: v => fmtAxisRial(Number(v)) },
        },
        plotOptions: { bar: { horizontal: true, borderRadius: 5, barHeight: '60%', distributed: true } },
        colors: ['#FFCD05', '#58585B', '#14B8A6', '#F59E0B', '#FB7185', '#38BDF8', '#A78BFA', '#9CA3AF', '#FCE38A'],
        legend: { show: false }, grid: { borderColor: chartGrid(), strokeDashArray: 4 },
        dataLabels: { enabled: true, formatter: v => fmtAxisRial(v), style: { fontSize: '11px' } },
        tooltip: { theme: tooltipTheme(), y: { formatter: v => formatRialCompact(v) } },
      })
      charts.product.render()
    }
  }

  // ۴) فروش بر اساس محصول — تناژ (افقی)
  destroyChart('productTon')
  if (elProductTon.value) {
    const data = byProductTon.value.filter(d => d[1] > 0)
    if (data.length) {
      charts.productTon = new ApexCharts(elProductTon.value, {
        chart: { type: 'bar', height: Math.max(300, data.length * 45 + 60), toolbar: { show: false }, fontFamily: baseFont, background: 'transparent', foreColor: chartForeColor() },
        series: [{ name: 'مقدار (کگ)', data: data.map(d => Math.round(d[1])) }],
        xaxis: {
          categories: data.map(d => d[0]),
          labels: { formatter: v => formatKg(Number(v)) },
        },
        plotOptions: { bar: { horizontal: true, borderRadius: 5, barHeight: '60%', distributed: true } },
        colors: ['#58585B', '#FFCD05', '#14B8A6', '#F59E0B', '#FB7185', '#38BDF8', '#A78BFA', '#9CA3AF'],
        legend: { show: false }, grid: { borderColor: chartGrid(), strokeDashArray: 4 },
        dataLabels: { enabled: true, formatter: v => formatKg(v), style: { fontSize: '11px' } },
        tooltip: { theme: tooltipTheme(), y: { formatter: v => formatKg(v) } },
      })
      charts.productTon.render()
    }
  }

  // ۵) فروش بر اساس مشتری — دونات
  destroyChart('customer')
  if (elCustomer.value) {
    const data = byCustomer.value.filter(d => d[1] > 0)
    if (data.length) {
      charts.customer = new ApexCharts(elCustomer.value, {
        chart: { type: 'donut', height: 360, fontFamily: baseFont, background: 'transparent' },
        series: data.map(d => Math.round(Math.abs(d[1]))),
        labels: data.map(d => d[0]),
        colors: ['#FFCD05', '#58585B', '#14B8A6', '#F59E0B', '#FB7185', '#38BDF8', '#A78BFA'],
        legend: { show: true, position: 'bottom', fontSize: '11px', labels: { colors: isDark.value ? '#D8D8D9' : '#4B4B4D' } },
        dataLabels: { enabled: true, formatter: v => toFaNum(v.toFixed(0)) + '٪' },
        stroke: { show: true, width: 2, colors: [isDark.value ? '#1E1E20' : '#ffffff'] },
        tooltip: { theme: tooltipTheme(), y: { formatter: v => formatRialCompact(v) } },
      })
      charts.customer.render()
    }
  }

  // ۶) نوع فروش — پای
  destroyChart('type')
  if (elType.value) {
    const data = byType.value.filter(d => d[1] > 0)
    if (data.length) {
      charts.type = new ApexCharts(elType.value, {
        chart: { type: 'pie', height: 320, fontFamily: baseFont, background: 'transparent' },
        series: data.map(d => Math.round(Math.abs(d[1]))),
        labels: data.map(d => d[0]),
        colors: ['#58585B', '#FFCD05', '#FB7185'],
        legend: { position: 'bottom', labels: { colors: isDark.value ? '#D8D8D9' : '#4B4B4D' } },
        dataLabels: { enabled: true, formatter: v => toFaNum(v.toFixed(0)) + '٪' },
        stroke: { width: 2, colors: [isDark.value ? '#1E1E20' : '#ffffff'] },
        tooltip: { theme: tooltipTheme(), y: { formatter: v => formatRialCompact(v) } },
      })
      charts.type.render()
    }
  }
}

watch(isDark, async () => {
  if (isLoading.value) return
  await nextTick()
  if (activeTab.value === 'main') renderMainCharts()
  if (activeTab.value === 'report') renderReportCharts()
})

/* ==========================================================================
   ۱۱) ایمپورت اکسل
   ========================================================================== */
const importState = reactive({ show: false, loading: false, preview: [], errors: [], success: 0 })
const xlsFileInput = ref(null)

function parseSpreadsheetML(xmlText) {
  const parser = new DOMParser()
  const doc = parser.parseFromString(xmlText, 'application/xml')
  const NS = 'urn:schemas-microsoft-com:office:spreadsheet'

  const rows = [...doc.getElementsByTagNameNS(NS, 'Row')]
  if (rows.length < 2) throw new Error('فایل خالی است')

  // استخراج هدر
  const headerCells = [...rows[0].getElementsByTagNameNS(NS, 'Cell')]
  const headers = headerCells.map(c => {
    const d = c.getElementsByTagNameNS(NS, 'Data')[0]
    return d ? (d.textContent || '') : ''
  })

  const col = name => headers.indexOf(name)
  const required = ['نوع سند', 'تاريخ', 'مشتري', 'كالا/خدمت(2)', 'مقدار-اصلي', 'في به ارز پايه', 'خالص به ارز پايه']
  const missing = required.filter(r => col(r) === -1)
  if (missing.length) throw new Error(`ستون‌های مورد نیاز یافت نشد: ${missing.join('، ')}`)

  const records = []
  for (let i = 1; i < rows.length; i++) {
    const cells = [...rows[i].getElementsByTagNameNS(NS, 'Cell')]
    const vals = cells.map(c => {
      const d = c.getElementsByTagNameNS(NS, 'Data')[0]
      return d ? (d.textContent || '').trim() : ''
    })
    const get = name => vals[col(name)] || ''

    const docType = get('نوع سند')
    const isReturn = docType.includes('برگشت')

    const customer = get('مشتري')
    const product = get('كالا/خدمت(2)')  // اسم کوتاه محصول
    const dateLabel = get('تاريخ')
    const kgs = parseFloat(get('مقدار-اصلي')) || 0
    const pricePerKg = parseFloat(get('في به ارز پايه')) || 0
    const netAmount = parseFloat(get('خالص به ارز پايه')) || 0
    // ستون «نوع فروش» در اکسل = نحوه پرداخت (نقدی، چکی، ...)
    // «رسمی/غیررسمی» مربوط به نوع سند فروش است که در اکسل موجود نیست
    const paymentRaw = get('نوع فروش') || get('گروه مشتري') || ''
    // نرمال‌سازی: اگه نقدی، چکی، حواله بانکی یا اعتباری بود نگه دار، وگرنه نقدی
    const knownPayments = ['نقدی', 'نقدي', 'چکی', 'چكي', 'حواله بانکی', 'حواله بانكي', 'اعتباری', 'اعتباري']
    const payment = knownPayments.some(p => paymentRaw.includes(p.slice(0,3)))
      ? (paymentRaw.includes('چک') || paymentRaw.includes('چك') ? 'چکی'
        : paymentRaw.includes('حواله') ? 'حواله بانکی'
        : paymentRaw.includes('اعتبار') ? 'اعتباری'
        : 'نقدی')
      : 'نقدی'

    if (!customer || !dateLabel) continue

    records.push({
      customer,
      product: product || 'نامشخص',
      tons: kgs,
      price: pricePerKg,
      amount: netAmount,
      payment,
      date: dateLabel,
      saleType: 'رسمی',   // همه فاکتورهای ایمپورت = رسمی
      isReturn,
      docType,
    })
  }
  return records
}

function onXlsFileChange(e) {
  const file = e.target.files[0]
  if (!file) return
  importState.preview = []
  importState.errors = []

  const reader = new FileReader()
  reader.onload = ev => {
    try {
      const records = parseSpreadsheetML(ev.target.result)
      importState.preview = records.slice(0, 10)
      importState.show = true
    } catch (err) {
      showToast('خطا در خواندن فایل: ' + err.message, 'error')
    }
  }
  reader.readAsText(file, 'utf-8')
  e.target.value = ''
}

async function confirmImport() {
  importState.loading = true
  importState.errors = []
  let ok = 0

  const allRecords = await new Promise((resolve) => {
    const reader = new FileReader()
    reader.onload = ev => {
      try { resolve(parseSpreadsheetML(ev.target.result)) }
      catch (e) { resolve([]) }
    }
    // چون فایل رو نگه نداشتیم، از preview کار می‌کنیم - در عمل باید فایل رو نگه داری
    resolve(importState.preview)
  })

  for (const rec of importState.preview) {
    try {
      await apiFetch('/api/sales', {
        method: 'POST',
        body: JSON.stringify({
          customer: rec.customer,
          product: rec.product,
          tons: rec.tons,
          price: rec.price || (rec.tons > 0 ? rec.amount / rec.tons : 0),
          saleType: 'رسمی',
          payment: rec.payment,
          date: rec.date,
          status: rec.isReturn ? 'برگشتی' : 'تکمیل شده',
          description: rec.isReturn ? `برگشت از فروش — ${rec.docType}` : '',
        }),
      })
      ok++
    } catch (err) {
      importState.errors.push(`${rec.customer}: ${err.message}`)
    }
  }

  importState.success = ok
  importState.loading = false
  if (ok > 0) {
    showToast(`${toFaNum(ok)} رکورد با موفقیت وارد شد`, 'success')
    await loadSales()
  }
  if (importState.errors.length === 0) importState.show = false
}

// ایمپورت کامل (نه فقط preview)
const pendingImportFile = ref(null)

function onXlsFileChangeFull(e) {
  const file = e.target.files[0]
  if (!file) return
  pendingImportFile.value = file
  importState.preview = []
  importState.errors = []
  importState.success = 0

  const reader = new FileReader()
  reader.onload = ev => {
    try {
      const records = parseSpreadsheetML(ev.target.result)
      importState.preview = records
      importState.show = true
    } catch (err) {
      showToast('خطا در خواندن فایل: ' + err.message, 'error')
    }
  }
  reader.readAsText(file, 'utf-8')
  e.target.value = ''
}

async function confirmImportFull() {
  importState.loading = true
  importState.errors = []
  let ok = 0

  for (const rec of importState.preview) {
    try {
      await apiFetch('/api/sales', {
        method: 'POST',
        body: JSON.stringify({
          customer: rec.customer,
          product: rec.product,
          tons: rec.tons,
          price: rec.price || (rec.tons > 0 ? rec.amount / rec.tons : 0),
          saleType: 'رسمی',
          payment: rec.payment,
          date: rec.date,
          status: rec.isReturn ? 'برگشتی' : 'تکمیل شده',
          description: rec.isReturn ? `برگشت از فروش` : '',
        }),
      })
      ok++
    } catch (err) {
      importState.errors.push(`ردیف ${ok + importState.errors.length + 1} — ${rec.customer}: ${err.message}`)
    }
  }

  importState.loading = false
  importState.success = ok
  if (ok > 0) {
    showToast(`${toFaNum(ok)} رکورد با موفقیت وارد شد`, 'success')
    await loadSales()
  }
  if (importState.errors.length === 0) importState.show = false
}

/* ==========================================================================
   ۱۲) مدیریت فروش — جدول با ادیت/حذف
   ========================================================================== */
const tableSearch = ref('')
const currentPage = ref(1)
const pageSize = 8

const tableRows = computed(() => {
  const q = tableSearch.value.trim()
  const base = [...filteredSales.value].sort((a, b) => jalaliToNum(b.dateLabel) - jalaliToNum(a.dateLabel))
  if (!q) return base
  return base.filter(s => s.customer?.includes(q) || s.product?.includes(q))
})
const totalPages = computed(() => Math.max(1, Math.ceil(tableRows.value.length / pageSize)))
const paginatedRows = computed(() => tableRows.value.slice((currentPage.value - 1) * pageSize, currentPage.value * pageSize))
watch([tableRows, tableSearch], () => { if (currentPage.value > totalPages.value) currentPage.value = 1 })
function goPage(p) { if (p >= 1 && p <= totalPages.value) currentPage.value = p }

function statusClasses(s) {
  if (s === 'تکمیل شده') return 'bg-emerald-50 text-emerald-700 ring-1 ring-emerald-600/20 dark:bg-emerald-500/10 dark:text-emerald-400'
  if (s === 'در حال پردازش') return 'bg-amber-50 text-amber-700 ring-1 ring-amber-600/20 dark:bg-amber-500/10 dark:text-amber-400'
  if (s === 'برگشتی') return 'bg-rose-50 text-rose-700 ring-1 ring-rose-600/20 dark:bg-rose-500/10 dark:text-rose-400'
  return 'bg-slate-100 text-slate-500 dark:bg-white/10 dark:text-slate-400'
}

const confirmState = reactive({ show: false, message: '', onConfirm: null })
function askConfirm(msg, fn) { confirmState.message = msg; confirmState.onConfirm = fn; confirmState.show = true }
function closeConfirm() { confirmState.show = false; confirmState.onConfirm = null }
function runConfirm() { if (confirmState.onConfirm) confirmState.onConfirm(); closeConfirm() }

async function deleteSale(row) {
  askConfirm(`آیا از حذف فروش «${row.customer}» مطمئن هستید؟`, async () => {
    try {
      await apiFetch(`/api/sales/${row.id}`, { method: 'DELETE' })
      allSales.value = allSales.value.filter(s => s.id !== row.id)
      showToast('رکورد با موفقیت حذف شد', 'success')
    } catch (e) { showToast(e.message, 'error') }
  })
}

// مودال فروش
const showModal = ref(false)
const modalMode = ref('create') // create | edit | view
const editingId = ref(null)

function emptyForm() {
  return {
    customer: '', product: products.value[0]?.name || '', tons: null, price: null,
    saleType: 'رسمی', date: '', payment: paymentMethods.value[0] || 'نقدی',
    industry: industries.value[0] || '', province: provinces.value[0] || '',
    status: 'در حال پردازش', description: '',
  }
}
const saleForm = reactive(emptyForm())

function openCreateModal() { Object.assign(saleForm, emptyForm()); modalMode.value = 'create'; editingId.value = null; showModal.value = true }
function openViewModal(row) { fillForm(row); modalMode.value = 'view'; showModal.value = true }
function openEditModal(row) { fillForm(row); modalMode.value = 'edit'; editingId.value = row.id; showModal.value = true }
function fillForm(row) {
  Object.assign(saleForm, {
    customer: row.customer, product: row.product, tons: row.tons,
    price: row.tons ? Math.round(row.amount / row.tons) : 0,
    saleType: row.saleType, date: row.dateLabel, payment: row.payment,
    industry: row.industry || '', province: row.province || '',
    status: row.status, description: row.description || '',
  })
}
function closeModal() { showModal.value = false }

async function submitSale() {
  if (!saleForm.customer || !saleForm.product || !saleForm.tons || !saleForm.price) {
    showToast('لطفاً فیلدهای الزامی را تکمیل کنید', 'error'); return
  }
  try {
    const payload = {
      customer: saleForm.customer, product: saleForm.product,
      tons: Number(saleForm.tons), price: Number(saleForm.price),
      saleType: saleForm.saleType, payment: saleForm.payment,
      province: saleForm.province, industry: saleForm.industry,
      date: saleForm.date, status: saleForm.status, description: saleForm.description,
    }
    if (modalMode.value === 'edit' && editingId.value) {
      await apiFetch(`/api/sales/${editingId.value}`, { method: 'PUT', body: JSON.stringify(payload) })
      showToast('فروش با موفقیت ویرایش شد', 'success')
    } else {
      await apiFetch('/api/sales', { method: 'POST', body: JSON.stringify(payload) })
      showToast('فروش جدید با موفقیت ثبت شد', 'success')
    }
    await loadSales()
    closeModal()
  } catch (e) { showToast(e.message, 'error') }
}

/* ==========================================================================
   ۱۳) تب مشتریان
   ========================================================================== */
const customerSearch = ref('')
const customerPage = ref(1)
const customerPageSize = 8
const filteredCustomers = computed(() => {
  const q = customerSearch.value.trim()
  if (!q) return customers.value
  return customers.value.filter(c => c.name?.includes(q) || c.industry?.includes(q) || c.province?.includes(q))
})
const customerTotalPages = computed(() => Math.max(1, Math.ceil(filteredCustomers.value.length / customerPageSize)))
const paginatedCustomers = computed(() => filteredCustomers.value.slice((customerPage.value - 1) * customerPageSize, customerPage.value * customerPageSize))
watch(customerSearch, () => { customerPage.value = 1 })
function goCustomerPage(p) { if (p >= 1 && p <= customerTotalPages.value) customerPage.value = p }
const topCustomerCards = computed(() => [...customers.value].sort((a, b) => statFor(b.name).amount - statFor(a.name).amount).slice(0, 4))

const showCustomerModal = ref(false)
const customerModalMode = ref('create')
const editingCustomerId = ref(null)
function emptyCustomerForm() { return { name: '', phone: '', email: '', province: provinces.value[0] || '', address: '', industry: industries.value[0] || '', description: '' } }
const customerForm = reactive(emptyCustomerForm())

function openCreateCustomer() { Object.assign(customerForm, emptyCustomerForm()); customerModalMode.value = 'create'; editingCustomerId.value = null; showCustomerModal.value = true }
function openEditCustomer(c) {
  Object.assign(customerForm, { name: c.name, phone: c.phone, email: c.email, province: c.province, address: c.address, industry: c.industry, description: c.description || '' })
  customerModalMode.value = 'edit'; editingCustomerId.value = c.id; showCustomerModal.value = true
}
function closeCustomerModal() { showCustomerModal.value = false }

async function submitCustomer() {
  if (!customerForm.name || !customerForm.phone) { showToast('نام و شماره تماس الزامی است', 'error'); return }
  try {
    if (customerModalMode.value === 'edit' && editingCustomerId.value) {
      await apiFetch(`/api/customers/${editingCustomerId.value}`, { method: 'PUT', body: JSON.stringify(customerForm) })
      showToast('مشتری ویرایش شد', 'success')
    } else {
      await apiFetch('/api/customers', { method: 'POST', body: JSON.stringify(customerForm) })
      showToast('مشتری جدید افزوده شد', 'success')
    }
    await loadCustomers()
    closeCustomerModal()
  } catch (e) { showToast(e.message, 'error') }
}

async function deleteCustomer(c) {
  askConfirm(`آیا از حذف مشتری «${c.name}» مطمئن هستید؟`, async () => {
    try {
      await apiFetch(`/api/customers/${c.id}`, { method: 'DELETE' })
      await loadCustomers()
      showToast('مشتری حذف شد', 'success')
    } catch (e) { showToast(e.message, 'error') }
  })
}

const showHistoryModal = ref(false)
const historyCustomer = ref(null)
const historyRows = computed(() => historyCustomer.value ? allSales.value.filter(s => s.customer === historyCustomer.value.name).sort((a, b) => jalaliToNum(b.dateLabel) - jalaliToNum(a.dateLabel)) : [])
function openHistory(c) { historyCustomer.value = c; showHistoryModal.value = true }
function closeHistory() { showHistoryModal.value = false; historyCustomer.value = null }

/* ==========================================================================
   ۱۴) تنظیمات — مدیریت داده‌های پایه از بک‌اند
   ========================================================================== */
const settingsSection = ref('products')

// محصولات
const showProductModal = ref(false)
const productModalMode = ref('create')
const editingProductId = ref(null)
function emptyProductForm() { return { name: '', code: '', category: '' } }
const productForm = reactive(emptyProductForm())

function openCreateProduct() { Object.assign(productForm, emptyProductForm()); productModalMode.value = 'create'; editingProductId.value = null; showProductModal.value = true }
function openEditProduct(p) { Object.assign(productForm, { name: p.name, code: p.code, category: p.category }); productModalMode.value = 'edit'; editingProductId.value = p.id; showProductModal.value = true }
function closeProductModal() { showProductModal.value = false }

async function submitProduct() {
  if (!productForm.name || !productForm.code) { showToast('نام و کد محصول الزامی است', 'error'); return }
  try {
    if (productModalMode.value === 'edit' && editingProductId.value) {
      await apiFetch(`/api/products/${editingProductId.value}`, { method: 'PUT', body: JSON.stringify(productForm) })
      showToast('محصول ویرایش شد', 'success')
    } else {
      await apiFetch('/api/products', { method: 'POST', body: JSON.stringify(productForm) })
      showToast('محصول افزوده شد', 'success')
    }
    await loadLookups()
    closeProductModal()
  } catch (e) { showToast(e.message, 'error') }
}

async function deleteProduct(p) {
  askConfirm(`آیا از حذف محصول «${p.name}» مطمئن هستید؟`, async () => {
    try {
      await apiFetch(`/api/products/${p.id}`, { method: 'DELETE' })
      await loadLookups()
      showToast('محصول حذف شد', 'success')
    } catch (e) { showToast(e.message, 'error') }
  })
}

// مدیریت لیست‌های ساده (استان / صنعت / پرداخت)
function makeApiListManager(endpoint, reloader) {
  const showEditor = ref(false)
  const mode = ref('create')
  const editingId = ref(null)
  const value = ref('')
  function openCreate() { value.value = ''; mode.value = 'create'; editingId.value = null; showEditor.value = true }
  function openEdit(item) { value.value = item.name; mode.value = 'edit'; editingId.value = item.id; showEditor.value = true }
  function close() { showEditor.value = false }
  async function submit() {
    if (!value.value.trim()) { showToast('نام نمی‌تواند خالی باشد', 'error'); return }
    try {
      if (mode.value === 'edit' && editingId.value) {
        await apiFetch(`/api/${endpoint}/${editingId.value}`, { method: 'PUT', body: JSON.stringify({ name: value.value.trim() }) })
        showToast('ویرایش شد', 'success')
      } else {
        await apiFetch(`/api/${endpoint}`, { method: 'POST', body: JSON.stringify({ name: value.value.trim() }) })
        showToast('افزوده شد', 'success')
      }
      await reloader()
      close()
    } catch (e) { showToast(e.message, 'error') }
  }
  async function remove(item) {
    askConfirm(`آیا از حذف «${item.name}» مطمئن هستید؟`, async () => {
      try {
        await apiFetch(`/api/${endpoint}/${item.id}`, { method: 'DELETE' })
        await reloader()
        showToast('حذف شد', 'success')
      } catch (e) { showToast(e.message, 'error') }
    })
  }
  return { showEditor, mode, value, openCreate, openEdit, close, submit, remove }
}

const provinceManager = makeApiListManager('provinces', loadLookups)
const industryManager = makeApiListManager('industries', loadLookups)
const paymentManager = makeApiListManager('payment-methods', loadLookups)

// داده‌های آماده برای نمایش در تنظیمات
const provincesWithId = computed(() => provinces.value.map((name, i) => ({ id: i + 1, name })))
const industriesWithId = computed(() => industries.value.map((name, i) => ({ id: i + 1, name })))
const paymentsWithId = computed(() => paymentMethods.value.map((name, i) => ({ id: i + 1, name })))

async function reloadLookupsFull() {
  const [pr, ind, pm] = await Promise.all([
    apiFetch('/api/provinces'),
    apiFetch('/api/industries'),
    apiFetch('/api/payment-methods'),
  ])
  provinces.value = pr.data.map(x => x.name)
  industries.value = ind.data.map(x => x.name)
  paymentMethods.value = pm.data.map(x => x.name)
  return { provinces: pr.data, industries: ind.data, payments: pm.data }
}
const lookupData = ref({ provinces: [], industries: [], payments: [] })
async function reloadAndStore() {
  const data = await reloadLookupsFull()
  lookupData.value = data
}

/* ==========================================================================
   ۱۵) خروجی
   ========================================================================== */
/* ==========================================================================
   خروجی Excel (CSV با BOM برای پشتیبانی صحیح از فارسی در اکسل)
   ========================================================================== */
function exportExcel() {
  const rows = filteredSales.value
  if (!rows.length) { showToast('داده‌ای برای خروجی گرفتن وجود ندارد', 'error'); return }

  const headers = ['تاریخ', 'مشتری', 'محصول', 'مقدار (کیلوگرم)', 'مبلغ (ریال)', 'نوع سند', 'نوع فروش', 'نحوه پرداخت', 'وضعیت']
  const csvRows = [headers.join(',')]

  rows.forEach(r => {
    const line = [
      r.dateLabel || '',
      `"${(r.customer || '').replace(/"/g, '""')}"`,
      `"${(r.product || '').replace(/"/g, '""')}"`,
      r.tons ?? 0,
      r.amount ?? 0,
      r.isReturn ? 'برگشتی' : 'فاکتور',
      r.saleType || '',
      r.payment || '',
      r.status || '',
    ]
    csvRows.push(line.join(','))
  })

  const csvContent = csvRows.join('\r\n')
  // BOM برای نمایش درست حروف فارسی وقتی با Excel باز می‌شود
  const blob = new Blob(['\uFEFF' + csvContent], { type: 'text/csv;charset=utf-8;' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = `گزارش-فروش-${todayJalaliStr().replace(/\//g, '-')}.csv`
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
  URL.revokeObjectURL(url)
  showToast(`فایل اکسل با ${toFaNum(rows.length)} رکورد دانلود شد`, 'success')
}

/* ==========================================================================
   خروجی PDF (باز کردن پنجره چاپ با جدول فرمت‌شده — از دیالوگ مرورگر Save as PDF)
   ========================================================================== */
function exportPdf() {
  const rows = filteredSales.value
  if (!rows.length) { showToast('داده‌ای برای خروجی گرفتن وجود ندارد', 'error'); return }

  const win = window.open('', '_blank')
  if (!win) {
    showToast('مرورگر اجازه باز کردن پنجره جدید را نداد — Popup Blocker را غیرفعال کنید', 'error')
    return
  }

  const tableRowsHtml = rows.map(r => `
    <tr>
      <td>${r.dateLabel || ''}</td>
      <td>${r.customer || ''}</td>
      <td>${r.product || ''}</td>
      <td>${toFaNum(r.tons ?? 0)}</td>
      <td>${formatRial(r.amount ?? 0)}</td>
      <td>${r.isReturn ? 'برگشتی' : 'فاکتور'}</td>
      <td>${r.status || ''}</td>
    </tr>
  `).join('')

  const totalAmount = rows.reduce((a, s) => a + (s.isReturn ? -s.amount : s.amount), 0)

  win.document.write(`
    <!DOCTYPE html>
    <html dir="rtl" lang="fa">
    <head>
      <meta charset="utf-8">
      <title>گزارش فروش</title>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;800&display=swap');
        * { box-sizing: border-box; }
        body { font-family: 'Vazirmatn', sans-serif; padding: 24px; color: #2b2b2c; }
        h1 { font-size: 20px; margin-bottom: 4px; }
        p.meta { color: #777; font-size: 12px; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; font-size: 12px; }
        th, td { border: 1px solid #ddd; padding: 8px 10px; text-align: right; }
        th { background: #FFCD05; color: #2b2b2c; font-weight: 800; }
        tr:nth-child(even) { background: #fafafa; }
        .summary { margin-top: 16px; font-weight: 800; font-size: 14px; }
        @media print {
          body { padding: 0; }
          @page { size: A4; margin: 14mm; }
        }
      </style>
    </head>
    <body>
      <h1>گزارش فروش — PolyChem CRM</h1>
      <p class="meta">تاریخ تهیه گزارش: ${todayJalaliStr()} — تعداد رکورد: ${toFaNum(rows.length)}</p>
      <table>
        <thead>
          <tr>
            <th>تاریخ</th><th>مشتری</th><th>محصول</th><th>مقدار (کگ)</th><th>مبلغ</th><th>نوع سند</th><th>وضعیت</th>
          </tr>
        </thead>
        <tbody>${tableRowsHtml}</tbody>
      </table>
      <p class="summary">جمع کل خالص: ${formatRial(totalAmount)}</p>
    </body>
    </html>
  `)
  win.document.close()

  // صبر برای لود کامل فونت/استایل، بعد دیالوگ چاپ (Save as PDF) باز شود
  win.onload = () => {
    win.focus()
    win.print()
  }
  showToast('پنجره چاپ باز شد — از دیالوگ چاپ گزینه Save as PDF را انتخاب کنید', 'info')
}

function printReport() { window.print() }

/* ==========================================================================
   ۱۶) آیکون‌های SVG
   ========================================================================== */
const icons = {
  search: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.2" y2="16.2"/></svg>',
  plus: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>',
  filter: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16M7 12h10M10 19h4"/></svg>',
  close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="6" y1="18" x2="18" y2="6"/></svg>',
  chevron: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>',
  coin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="8"/><path d="M9.5 9.5a2.5 2 0 0 1 5 0c0 1-1 1.5-2.5 2s-2.5 1-2.5 2a2.5 2.5 0 0 0 5 0" stroke-linecap="round"/></svg>',
  box: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M21 8 12 3 3 8l9 5 9-5Z"/><path d="M3 8v8l9 5 9-5V8"/><path d="M12 13v8"/></svg>',
  users: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/><circle cx="17.5" cy="9" r="2.4"/><path d="M21 20c0-2.6-1.7-4.4-3.8-5"/></svg>',
  chart: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M12 20V4M20 20v-7"/></svg>',
  star: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.5l2.9 6 6.6.7-4.9 4.5 1.3 6.5L12 16.9 5.9 20.2l1.3-6.5-4.9-4.5 6.6-.7L12 2.5Z"/></svg>',
  medal: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M7 3h10l-3 8H10L7 3Z"/><circle cx="12" cy="15" r="6"/></svg>',
  calendar: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M8 3v4M16 3v4M3.5 10h17"/></svg>',
  trend: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 16 9.5 9.5 14 14 21 6"/><polyline points="15 6 21 6 21 12"/></svg>',
  trendDown: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 8 9.5 14.5 14 10 21 18"/><polyline points="15 18 21 18 21 12"/></svg>',
  warning: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.5 2 20.5h20L12 3.5Z"/><line x1="12" y1="9.5" x2="12" y2="14"/><circle cx="12" cy="17" r="0.6" fill="currentColor"/></svg>',
  pdf: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h7l5 5v13a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z"/><path d="M14 3v5h5"/></svg>',
  excel: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="4" width="17" height="16" rx="1.5"/><path d="M3.5 9.5h17M3.5 14.5h17M9 4v16M15 4v16"/></svg>',
  print: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 9V4h11v5"/><rect x="4" y="9" width="16" height="8" rx="1.4"/><path d="M6.5 14.5h11V21h-11v-6.5Z"/></svg>',
  upload: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>',
  eye: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.8-7 10-7 10 7 10 7-3.8 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>',
  edit: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20.5 4.7 17 16 5.7a1.8 1.8 0 0 1 2.5 0l1.8 1.8a1.8 1.8 0 0 1 0 2.5L9 21.3 4 20.5Z"/></svg>',
  trash: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M9 7V4.5h6V7M6 7l1 13.5h10L18 7"/></svg>',
  sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.3M12 19.2v2.3M4.3 4.3l1.6 1.6M18.1 18.1l1.6 1.6M2.5 12h2.3M19.2 12h2.3M4.3 19.7l1.6-1.6M18.1 5.9l1.6-1.6"/></svg>',
  moon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 14.3A8.5 8.5 0 1 1 9.7 4a7 7 0 0 0 10.3 10.3Z"/></svg>',
  crown: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M3 18h18M4 18l-1-9 5 3.3L12 6l4 6.3 5-3.3-1 9"/></svg>',
  empty: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="7" width="17" height="13" rx="1.6"/><path d="M3.5 11h17M8 4.5h8"/></svg>',
  home: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11.5 12 4l8 7.5"/><path d="M6 10v9.5a1 1 0 0 0 1 1h4v-6h2v6h4a1 1 0 0 0 1-1V10"/></svg>',
  list: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 6h13M8 12h13M8 18h13"/><circle cx="3.5" cy="6" r="1.1" fill="currentColor" stroke="none"/><circle cx="3.5" cy="12" r="1.1" fill="currentColor" stroke="none"/><circle cx="3.5" cy="18" r="1.1" fill="currentColor" stroke="none"/></svg>',
  gear: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.2"/><path d="M19.4 13.5a7.7 7.7 0 0 0 0-3l1.9-1.5-2-3.4-2.3.7a7.6 7.6 0 0 0-2.6-1.5L14 2h-4l-.4 2.3a7.6 7.6 0 0 0-2.6 1.5l-2.3-.7-2 3.4L4.6 10a7.7 7.7 0 0 0 0 3l-1.9 1.6 2 3.4 2.3-.7c.8.6 1.7 1.2 2.6 1.5L10 22h4l.4-2.3c1-.3 1.8-.9 2.6-1.5l2.3.7 2-3.4-1.9-1.5Z"/></svg>',
  building: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="10" height="18"/><path d="M14 8h6v13h-6M7 7h1M7 11h1M7 15h1"/></svg>',
  history: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/><path d="M12 7.5V12l3 2"/></svg>',
  logout: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 4H6a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h9"/><path d="M10 12h11m0 0-3-3m3 3-3 3"/></svg>',
  chevronDown: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>',
  menu: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
  refresh: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7"/><path d="M21 3v5h-5"/></svg>',
  map: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4 3 6.5v13L9 17m0-13 6 2m-6-2v13m6-11 6-2.5v13L15 17m0-13v13"/></svg>',
}

/* ==========================================================================
   ۱۷) چرخه عمر
   ========================================================================== */
onMounted(async () => {
  try { isDark.value = localStorage.getItem('sales-dashboard-theme') === 'dark' } catch (e) {}
  try {
    await Promise.all([loadLookups(), loadCustomers(), loadSales()])
    await reloadAndStore()
  } catch (e) {
    showToast('خطا در اتصال به سرور: ' + e.message, 'error')
  }
  isLoading.value = false
  await nextTick()
  try {
    const mod = await import('apexcharts')
    ApexCharts = mod.default
    renderMainCharts()
  } catch (e) { /* apexcharts نصب نیست */ }
})
onUnmounted(() => { Object.keys(charts).forEach(k => destroyChart(k)); clearTimeout(toastTimer) })
</script>

<template>
  <div :class="['min-h-screen flex flex-col overflow-x-hidden font-[Vazirmatn] transition-colors duration-300', isDark ? 'dark bg-[#1c1c1e] text-slate-100' : 'bg-[#f1f2f2] text-[#4B4B4D]']" dir="rtl">

    <!-- Toast -->
    <Transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 -translate-y-3" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-to-class="opacity-0 -translate-y-2">
      <div v-if="toast.show" class="fixed top-5 inset-x-0 z-[100] flex justify-center px-4 pointer-events-none">
        <div :class="['pointer-events-auto flex items-center gap-2 rounded-2xl px-4 py-3 shadow-xl ring-1 backdrop-blur text-sm font-medium', toast.type === 'success' ? 'bg-emerald-600/95 text-white ring-emerald-700/30' : toast.type === 'error' ? 'bg-rose-600/95 text-white ring-rose-700/30' : 'bg-[#3a3a3c]/95 text-white ring-black/20']">{{ toast.message }}</div>
      </div>
    </Transition>

    <!-- Confirm Modal -->
    <Transition enter-active-class="transition duration-150 ease-out" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition duration-100 ease-in" leave-to-class="opacity-0">
      <div v-if="confirmState.show" class="fixed inset-0 z-[110] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm" @click.self="closeConfirm">
        <div class="w-full max-w-sm rounded-3xl p-6 shadow-2xl ring-1" :class="isDark ? 'bg-[#2a2a2c] ring-white/10 text-slate-100' : 'bg-white ring-black/5'">
          <div class="w-11 h-11 rounded-xl bg-rose-500/10 text-rose-500 flex items-center justify-center mb-4"><span class="w-5 h-5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.warning"></span></div>
          <p class="font-bold text-sm mb-6 leading-relaxed">{{ confirmState.message }}</p>
          <div class="flex items-center gap-3">
            <button @click="runConfirm" class="flex-1 rounded-full bg-rose-600 text-white py-2.5 text-sm font-bold">تأیید حذف</button>
            <button @click="closeConfirm" class="flex-1 rounded-full py-2.5 text-sm font-bold ring-1" :class="isDark ? 'ring-white/15' : 'ring-black/10'">انصراف</button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Import Preview Modal -->
    <Transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition duration-150 ease-in" leave-to-class="opacity-0">
      <div v-if="importState.show" class="fixed inset-0 z-[90] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm" @click.self="importState.show = false">
        <div class="w-full max-w-4xl max-h-[90vh] overflow-y-auto rounded-3xl p-6 shadow-2xl ring-1" :class="isDark ? 'bg-[#2a2a2c] ring-white/10 text-slate-100' : 'bg-white ring-black/5'">
          <div class="flex items-center justify-between mb-5">
            <div>
              <h3 class="font-extrabold text-lg">پیش‌نمایش ایمپورت اکسل</h3>
              <p class="text-sm text-[#9a9a9c] mt-1">{{ toFaNum(importState.preview.length) }} ردیف یافت شد — همه به‌عنوان فروش رسمی ثبت می‌شوند</p>
            </div>
            <button @click="importState.show = false" class="w-9 h-9 rounded-full flex items-center justify-center hover:bg-black/5"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.close"></span></button>
          </div>

          <!-- خطاهای ایمپورت -->
          <div v-if="importState.errors.length" class="mb-4 rounded-2xl bg-rose-50 dark:bg-rose-500/10 p-4 ring-1 ring-rose-200 dark:ring-rose-500/20">
            <p class="font-bold text-rose-700 dark:text-rose-400 text-sm mb-2">خطاهای ثبت:</p>
            <ul class="space-y-1">
              <li v-for="e in importState.errors" :key="e" class="text-xs text-rose-600 dark:text-rose-300">• {{ e }}</li>
            </ul>
          </div>

          <!-- جدول پیش‌نمایش -->
          <div class="overflow-x-auto rounded-2xl ring-1 mb-5" :class="isDark ? 'ring-white/10' : 'ring-black/5'">
            <table class="w-full text-[12px] whitespace-nowrap">
              <thead><tr :class="isDark ? 'bg-white/[0.04]' : 'bg-slate-50'">
                <th class="th-cell">نوع سند</th>
                <th class="th-cell">تاریخ</th>
                <th class="th-cell">مشتری</th>
                <th class="th-cell">محصول</th>
                <th class="th-cell">مقدار (کگ)</th>
                <th class="th-cell">فی (ریال)</th>
                <th class="th-cell">خالص (ریال)</th>
                <th class="th-cell">پرداخت</th>
              </tr></thead>
              <tbody>
                <tr v-for="(r, i) in importState.preview.slice(0, 15)" :key="i" :class="[r.isReturn ? 'bg-rose-50/60 dark:bg-rose-500/5' : '', i % 2 && !r.isReturn ? (isDark ? 'bg-white/[0.015]' : 'bg-slate-50/60') : '']">
                  <td class="td-cell">
                    <span :class="['px-2 py-0.5 rounded-full text-[11px] font-bold', r.isReturn ? 'bg-rose-100 text-rose-700 dark:bg-rose-500/20 dark:text-rose-400' : 'bg-emerald-50 text-emerald-700 dark:bg-emerald-500/10 dark:text-emerald-400']">{{ r.isReturn ? 'برگشتی' : 'فاکتور' }}</span>
                  </td>
                  <td class="td-cell text-[#9a9a9c]">{{ r.date }}</td>
                  <td class="td-cell font-bold">{{ r.customer }}</td>
                  <td class="td-cell">{{ r.product }}</td>
                  <td class="td-cell">{{ toFaNum(r.tons) }}</td>
                  <td class="td-cell">{{ toFaNum(Math.round(r.price)) }}</td>
                  <td class="td-cell">{{ toFaNum(Math.round(r.amount)) }}</td>
                  <td class="td-cell">{{ r.payment }}</td>
                </tr>
              </tbody>
            </table>
            <p v-if="importState.preview.length > 15" class="p-3 text-[12px] text-[#9a9a9c] text-center">... و {{ toFaNum(importState.preview.length - 15) }} ردیف دیگر</p>
          </div>

          <div class="flex items-center gap-3">
            <button @click="confirmImportFull" :disabled="importState.loading" class="flex-1 rounded-full bg-[#FFCD05] text-[#3a3a3c] py-3 text-sm font-bold shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all disabled:opacity-60">
              {{ importState.loading ? 'در حال ثبت...' : `ثبت ${toFaNum(importState.preview.length)} رکورد` }}
            </button>
            <button @click="importState.show = false" class="flex-1 rounded-full py-3 text-sm font-bold ring-1 transition" :class="isDark ? 'ring-white/15' : 'ring-black/10'">انصراف</button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Header -->
    <header class="sticky top-0 z-30 border-b backdrop-blur-lg" :class="isDark ? 'bg-[#1c1c1e]/85 border-white/10' : 'bg-[#f1f2f2]/85 border-black/5'">
      <div class="max-w-[1500px] mx-auto px-4 sm:px-6 py-3 flex items-center gap-3 flex-wrap lg:flex-nowrap">
        <button @click="sidebarOpenMobile = !sidebarOpenMobile" class="lg:hidden w-10 h-10 rounded-full flex items-center justify-center ring-1 shrink-0" :class="isDark ? 'bg-white/5 ring-white/10' : 'bg-white ring-black/5 shadow-sm'">
          <span class="w-5 h-5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.menu"></span>
        </button>
        <div class="flex items-center shrink-0">
          <img src="/polychem.png" alt="لوگوی شرکت" class="h-12 w-auto max-w-[150px] object-contain" />
        </div>
        <div class="flex-1"></div>
        <div class="flex items-center gap-2 shrink-0">
          <!-- دکمه ایمپورت اکسل -->
          <label class="flex items-center gap-1.5 rounded-full bg-emerald-600 text-white px-4 py-2.5 text-sm font-bold shadow-lg cursor-pointer hover:shadow-xl hover:-translate-y-0.5 transition-all">
            <span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.upload"></span>
            <span class="hidden sm:inline">ایمپورت اکسل</span>
            <input type="file" accept=".xls,.xlsx" class="hidden" @change="onXlsFileChangeFull" />
          </label>
          <button @click="openCreateModal" class="flex items-center gap-1.5 rounded-full bg-[#FFCD05] text-[#3a3a3c] px-4 py-2.5 text-sm font-bold shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all">
            <span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.plus"></span>
            <span class="hidden sm:inline">افزودن فروش</span>
          </button>
          <button @click="toggleDark" class="w-10 h-10 rounded-full flex items-center justify-center ring-1 transition hover:-translate-y-0.5" :class="isDark ? 'bg-white/5 ring-white/10' : 'bg-white ring-black/5 shadow-sm'">
            <span class="w-5 h-5 text-[#FFCD05] [&>svg]:w-full [&>svg]:h-full" v-html="isDark ? icons.moon : icons.sun"></span>
          </button>

          <!-- کاربر لاگین‌شده + خروج -->
          <div class="relative flex items-center gap-2 ps-2 border-s ms-1" :class="isDark ? 'border-white/10' : 'border-black/10'">
            <div class="hidden md:flex flex-col items-end leading-tight">
              <span class="text-xs font-bold">{{ currentUser?.name || 'کاربر' }}</span>
              <span class="text-[10px] text-[#9a9a9c]">مدیر پنل</span>
            </div>
            <div class="w-9 h-9 rounded-full bg-gradient-to-br from-[#FFCD05] to-[#e6b900] flex items-center justify-center text-[#3a3a3c] text-xs font-extrabold shrink-0">
              {{ (currentUser?.name || 'ک').charAt(0) }}
            </div>
            <button @click="handleLogout" class="w-9 h-9 rounded-full flex items-center justify-center transition hover:bg-rose-50 hover:text-rose-500 dark:hover:bg-rose-500/10" :class="isDark ? 'text-slate-400' : 'text-[#9a9a9c]'" title="خروج">
              <span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.logout"></span>
            </button>
          </div>
        </div>
      </div>
      <div class="max-w-[1500px] mx-auto px-4 sm:px-6 pb-3">
        <h1 class="text-[17px] sm:text-[19px] font-extrabold">داشبورد گزارش فروش</h1>
      </div>
    </header>

    <!-- Body -->
    <div class="flex-1 w-full max-w-[1500px] mx-auto px-4 sm:px-6 py-6 flex items-start gap-5">
      <Transition enter-active-class="transition duration-200" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition duration-150" leave-to-class="opacity-0">
        <div v-if="sidebarOpenMobile" class="fixed inset-0 z-40 bg-black/40 lg:hidden" @click="sidebarOpenMobile = false"></div>
      </Transition>

      <!-- Sidebar -->
      <aside :class="['shrink-0 w-64 rounded-3xl ring-1 shadow-sm p-3 lg:sticky lg:top-24 transition-transform duration-300 flex flex-col', isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-white ring-black/5', 'fixed z-50 top-20 bottom-4 right-4 lg:static lg:z-auto', sidebarOpenMobile ? 'translate-x-0' : 'translate-x-[110%] lg:translate-x-0']">
        <nav class="flex flex-col gap-1.5 overflow-y-auto flex-1">
          <button v-for="t in tabs" :key="t.key" @click="setTab(t.key)"
            :class="['group relative flex items-center gap-3 rounded-2xl px-3.5 py-2.5 text-sm font-bold text-right overflow-hidden transition-all duration-300 ease-out',
              activeTab === t.key
                ? 'bg-gradient-to-l from-[#FFF6D6] to-[#FFF9E6] ring-1 ring-[#FFCD05]/50 text-[#8a6d00] shadow-sm dark:from-[#FFCD05]/15 dark:to-[#FFCD05]/5 dark:ring-[#FFCD05]/30 dark:text-[#FFCD05]'
                : (isDark
                    ? 'text-slate-400 hover:text-slate-100 hover:bg-white/[0.06] hover:translate-x-[-2px]'
                    : 'text-[#6b6b6d] hover:text-[#3a3a3c] hover:bg-[#FFF9E0] hover:translate-x-[-2px] hover:shadow-sm')]">
            <!-- نوار کناری فعال/هاور -->
            <span :class="['absolute right-0 top-1/2 -translate-y-1/2 w-[3px] rounded-full transition-all duration-300',
              activeTab === t.key ? 'h-5 bg-[#FFCD05]' : 'h-0 bg-[#FFCD05] group-hover:h-3']"></span>
            <span :class="['w-8 h-8 rounded-xl flex items-center justify-center shrink-0 transition-all duration-300 [&>svg]:w-4.5 [&>svg]:h-4.5',
              activeTab === t.key
                ? 'bg-[#FFCD05] text-[#2b2b2c] shadow-md shadow-[#FFCD05]/30'
                : 'bg-transparent group-hover:bg-[#FFCD05]/15 group-hover:text-[#FFCD05] group-hover:scale-105']"
              v-html="icons[t.icon]"></span>
            <span class="transition-colors duration-300">{{ t.label }}</span>
          </button>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 min-w-0 space-y-6">
        <!-- Loading -->
        <template v-if="isLoading">
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 animate-pulse">
            <div v-for="n in 8" :key="n" class="h-28 rounded-2xl" :class="isDark ? 'bg-white/5' : 'bg-black/5'"></div>
          </div>
        </template>

        <template v-else>
          <Transition mode="out-in" enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-100 ease-in" leave-to-class="opacity-0">

            <!-- TAB 1: داشبورد اصلی -->
            <div v-if="activeTab === 'main'" key="main" class="space-y-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <div v-for="k in monthlyKpis" :key="k.key"
                  :class="['group relative overflow-hidden rounded-2xl p-5 ring-1 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300',
                    k.featured ? 'lg:col-span-2 bg-gradient-to-br from-[#3a3a3c] to-[#58585B] text-white ring-black/10' : (isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-white ring-black/5')]">
                  <div class="flex items-start justify-between">
                    <div>
                      <p :class="['text-[12px] font-medium mb-2', k.featured ? 'text-white/60' : 'text-[#9a9a9c]']">{{ k.label }}</p>
                      <p :class="['font-extrabold', k.featured ? 'text-2xl text-[#FFCD05]' : 'text-lg truncate max-w-[180px]']">{{ k.value }}</p>
                      <div v-if="k.dir" class="mt-2 inline-flex items-center gap-1 text-[11px] font-bold px-2 py-0.5 rounded-full"
                        :class="k.dir === 'up' ? 'bg-emerald-500/15 text-emerald-400' : 'bg-rose-500/15 text-rose-400'">
                        <span class="w-3 h-3 [&>svg]:w-full [&>svg]:h-full" v-html="k.dir === 'up' ? icons.trend : icons.trendDown"></span>
                      </div>
                      <p v-else-if="k.note" :class="['mt-1.5 text-[11px] truncate max-w-[180px]', k.featured ? 'text-white/50' : 'text-[#9a9a9c]']">{{ k.note }}</p>
                    </div>
                    <div :class="['w-11 h-11 rounded-xl flex items-center justify-center shrink-0', k.featured ? 'bg-white/10 text-[#FFCD05]' : 'bg-[#FFF6D6] text-[#8a6d00] dark:bg-[#FFCD05]/10 dark:text-[#FFCD05]']">
                      <span class="w-5 h-5 [&>svg]:w-full [&>svg]:h-full" v-html="icons[k.icon]"></span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="grid grid-cols-1 xl:grid-cols-2 gap-4">
                <div class="chart-card"><h3 class="chart-title">فروش ماهانه ریالی</h3><div ref="elRialMain"></div></div>
                <div class="chart-card"><h3 class="chart-title">فروش ماهانه (کیلوگرم)</h3><div ref="elTonMain"></div></div>
                <div class="chart-card"><h3 class="chart-title">مقایسه فروش سالانه</h3><div ref="elYearCompare"></div></div>
                <div class="chart-card"><h3 class="chart-title">روند تناژ سالانه</h3><div ref="elYearGrowth"></div></div>
              </div>
            </div>

            <!-- TAB 2: گزارش فروش -->
            <div v-else-if="activeTab === 'report'" key="report" class="space-y-6">
              <!-- فیلترهای پیشرفته -->
              <section class="rounded-3xl p-5 sm:p-6 ring-1 shadow-sm" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-white ring-black/5'">
                <div class="flex items-center gap-2 mb-4">
                  <span class="w-5 h-5 text-[#FFCD05] [&>svg]:w-full [&>svg]:h-full" v-html="icons.filter"></span>
                  <h2 class="font-bold text-[15px]">فیلترهای گزارش تحلیلی</h2>
                  <span v-if="hasActiveFilters" class="text-[11px] px-2 py-0.5 rounded-full bg-[#FFCD05]/30 text-[#8a6d00] dark:text-[#FFCD05] font-bold">فعال</span>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3 mb-3">
                  <!-- بازه زمانی -->
                  <div>
                    <label class="form-label">بازه زمانی</label>
                    <select v-model="draftFilters.range" class="select-field">
                      <option value="all">همه بازه‌ها</option>
                      <option value="1">۱ ماه اخیر</option>
                      <option value="3">۳ ماه اخیر</option>
                      <option value="6">۶ ماه اخیر</option>
                      <option value="custom">بازه دستی</option>
                    </select>
                  </div>

                  <!-- از تاریخ / تا تاریخ — فقط وقتی custom انتخاب شده -->
                  <template v-if="draftFilters.range === 'custom'">
                    <div>
                      <label class="form-label">از تاریخ (شمسی)</label>
                      <input v-model="draftFilters.dateFrom" type="text" placeholder="۱۴۰۴/۰۱/۰۱" class="select-field" />
                    </div>
                    <div>
                      <label class="form-label">تا تاریخ (شمسی)</label>
                      <input v-model="draftFilters.dateTo" type="text" placeholder="۱۴۰۴/۱۲/۲۹" class="select-field" />
                    </div>
                  </template>

                  <div>
                    <label class="form-label">سال</label>
                    <select v-model="draftFilters.year" class="select-field">
                      <option value="all">همه سال‌ها</option>
                      <option v-for="y in [...new Set(allSales.map(s => s.dateLabel?.split('/')[0]).filter(Boolean))].sort().reverse()" :key="y" :value="y">{{ y }}</option>
                    </select>
                  </div>
                  <div>
                    <label class="form-label">مشتری</label>
                    <select v-model="draftFilters.customer" class="select-field">
                      <option value="all">همه مشتریان</option>
                      <option v-for="c in customerOptions" :key="c" :value="c">{{ c }}</option>
                    </select>
                  </div>
                  <div>
                    <label class="form-label">محصول</label>
                    <select v-model="draftFilters.product" class="select-field">
                      <option value="all">همه محصولات</option>
                      <option v-for="p in productOptions" :key="p" :value="p">{{ p }}</option>
                    </select>
                  </div>
                  <div>
                    <label class="form-label">نوع فروش</label>
                    <select v-model="draftFilters.saleType" class="select-field">
                      <option value="all">همه</option>
                      <option value="رسمی">رسمی</option>
                      <option value="غیررسمی">غیررسمی</option>
                    </select>
                  </div>
                  <div>
                    <label class="form-label">نحوه پرداخت</label>
                    <select v-model="draftFilters.payment" class="select-field">
                      <option value="all">همه روش‌ها</option>
                      <option v-for="p in paymentMethods" :key="p" :value="p">{{ p }}</option>
                    </select>
                  </div>
                  <div>
                    <label class="form-label">نوع سند</label>
                    <select v-model="draftFilters.docType" class="select-field">
                      <option value="all">همه</option>
                      <option value="فاكتور">فاکتور فروش</option>
                      <option value="برگشتی">برگشت از فروش</option>
                    </select>
                  </div>
                </div>

                <div class="flex items-center gap-3">
                  <button @click="applyFilters" class="rounded-full bg-[#FFCD05] text-[#3a3a3c] px-5 py-2.5 text-sm font-bold shadow-md hover:shadow-lg hover:-translate-y-0.5 transition-all">اعمال فیلتر</button>
                  <button @click="resetFilters" class="rounded-full px-5 py-2.5 text-sm font-bold ring-1 transition hover:-translate-y-0.5" :class="isDark ? 'ring-white/15 hover:bg-white/5' : 'ring-black/10 hover:bg-slate-50'">پاک کردن</button>
                </div>
              </section>

              <!-- نمودارها -->
              <section class="grid grid-cols-1 xl:grid-cols-2 gap-4">
                <div class="chart-card">
                  <h3 class="chart-title">فروش ماهانه (کیلوگرم)</h3>
                  <div v-if="monthlyAgg.length === 0" class="empty-box py-10 text-sm">داده‌ای برای نمایش وجود ندارد</div>
                  <div ref="elTon"></div>
                </div>
                <div class="chart-card">
                  <h3 class="chart-title">فروش ماهانه (ریال)</h3>
                  <div v-if="monthlyAgg.length === 0" class="empty-box py-10 text-sm">داده‌ای برای نمایش وجود ندارد</div>
                  <div ref="elRial"></div>
                </div>
                <div class="chart-card">
                  <h3 class="chart-title">فروش بر اساس محصول — مبلغ (ریال)</h3>
                  <div ref="elProduct"></div>
                </div>
                <div class="chart-card">
                  <h3 class="chart-title">فروش بر اساس محصول — مقدار (کیلوگرم)</h3>
                  <div ref="elProductTon"></div>
                </div>
                <div class="chart-card">
                  <h3 class="chart-title">سهم مشتریان از فروش</h3>
                  <div ref="elCustomer"></div>
                </div>
                <div class="chart-card">
                  <h3 class="chart-title">نوع فروش و برگشتی</h3>
                  <div ref="elType"></div>
                </div>
              </section>

              <!-- جدول گزارش با ادیت/حذف -->
              <section class="rounded-3xl ring-1 shadow-sm overflow-hidden" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-white ring-black/5'">
                <div class="p-5 sm:p-6 flex items-center justify-between flex-wrap gap-3 border-b" :class="isDark ? 'border-white/10' : 'border-black/5'">
                  <h3 class="font-bold text-[15px]">گزارش کامل فروش</h3>
                  <div class="flex items-center gap-2">
                    <button @click="exportPdf" class="icon-btn" title="PDF"><span class="w-4 h-4 text-rose-500 [&>svg]:w-full [&>svg]:h-full" v-html="icons.pdf"></span></button>
                    <button @click="exportExcel" class="icon-btn" title="Excel"><span class="w-4 h-4 text-emerald-500 [&>svg]:w-full [&>svg]:h-full" v-html="icons.excel"></span></button>
                    <button @click="printReport" class="icon-btn" title="چاپ"><span class="w-4 h-4 text-sky-500 [&>svg]:w-full [&>svg]:h-full" v-html="icons.print"></span></button>
                  </div>
                </div>
                <div class="overflow-x-auto">
                  <table class="w-full text-[13px] whitespace-nowrap">
                    <thead>
                      <tr :class="isDark ? 'bg-white/[0.04]' : 'bg-slate-50'">
                        <th class="th-cell">تاریخ</th>
                        <th class="th-cell">مشتری</th>
                        <th class="th-cell">محصول</th>
                        <th class="th-cell">مقدار (کگ)</th>
                        <th class="th-cell">مبلغ خالص</th>
                        <th class="th-cell">نوع</th>
                        <th class="th-cell">وضعیت</th>
                        <th class="th-cell">عملیات</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(row, i) in filteredSales.slice(0, 80)" :key="row.id"
                        :class="['transition-colors', row.isReturn ? 'bg-rose-50/40 dark:bg-rose-500/5' : '', isDark ? 'hover:bg-white/[0.06]' : 'hover:bg-[#FFF9E0]']">
                        <td class="td-cell text-[#9a9a9c]">{{ row.dateLabel }}</td>
                        <td class="td-cell font-bold">{{ row.customer }}</td>
                        <td class="td-cell">{{ row.product }}</td>
                        <td class="td-cell">{{ toFaNum(row.tons) }}</td>
                        <td class="td-cell" :class="row.isReturn ? 'text-rose-600 dark:text-rose-400' : ''">{{ formatRial(row.amount) }}</td>
                        <td class="td-cell">
                          <span :class="['px-2 py-0.5 rounded-full text-[11px] font-bold',
                            row.isReturn
                              ? 'bg-rose-100 text-rose-700 dark:bg-rose-500/20 dark:text-rose-400'
                              : (row.saleType === 'غیررسمی'
                                  ? 'bg-slate-100 text-slate-600 dark:bg-white/10 dark:text-slate-300'
                                  : 'bg-[#58585B] text-white dark:bg-[#FFCD05] dark:text-[#2b2b2c]')]">
                            {{ row.isReturn ? 'برگشتی' : (row.saleType || 'رسمی') }}
                          </span>
                        </td>
                        <td class="td-cell"><span :class="['px-2.5 py-1 rounded-full text-[11px] font-bold', statusClasses(row.status)]">{{ row.status }}</span></td>
                        <td class="td-cell">
                          <div class="flex items-center gap-1">
                            <button @click="openViewModal(row)" class="icon-btn" title="مشاهده"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.eye"></span></button>
                            <button @click="openEditModal(row)" class="icon-btn" title="ویرایش"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.edit"></span></button>
                            <button @click="deleteSale(row)" class="icon-btn hover:!text-rose-500" title="حذف"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.trash"></span></button>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div v-if="!filteredSales.length" class="empty-box m-6">
                    <span class="w-10 h-10 mx-auto mb-3 block text-slate-300 [&>svg]:w-full [&>svg]:h-full" v-html="icons.empty"></span>
                    نتیجه‌ای یافت نشد
                  </div>
                </div>
                <p class="p-4 text-[12px] text-[#9a9a9c] border-t" :class="isDark ? 'border-white/10' : 'border-black/5'">
                  نمایش {{ toFaNum(Math.min(80, filteredSales.length)) }} از {{ toFaNum(filteredSales.length) }} رکورد
                  <span v-if="returnCount > 0" class="mr-3 text-rose-500">• {{ toFaNum(returnCount) }} فاکتور برگشتی</span>
                </p>
              </section>
            </div>

            <!-- TAB 3: مدیریت فروش -->
            <div v-else-if="activeTab === 'manage'" key="manage" class="space-y-6">
              <section class="rounded-3xl ring-1 shadow-sm overflow-hidden" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-white ring-black/5'">
                <div class="p-5 sm:p-6 flex items-center justify-between flex-wrap gap-3 border-b" :class="isDark ? 'border-white/10' : 'border-black/5'">
                  <h3 class="font-bold text-[15px]">فروش‌ها</h3>
                  <div class="flex items-center gap-2">
                    <div class="relative w-full sm:w-64">
                      <span class="absolute inset-y-0 start-3.5 flex items-center pointer-events-none text-[#9a9a9c]"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.search"></span></span>
                      <input v-model="tableSearch" type="text" placeholder="جستجو..." class="w-full ps-10 pe-3 py-2 rounded-full text-[13px] outline-none ring-1 focus:ring-2" :class="isDark ? 'bg-white/5 ring-white/10 focus:ring-[#FFCD05]/50' : 'bg-slate-50 ring-black/5 focus:ring-[#FFCD05]/50'" />
                    </div>
                    <button @click="loadSales" class="icon-btn" title="بارگذاری مجدد"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.refresh"></span></button>
                  </div>
                </div>
                <div class="overflow-x-auto">
                  <table class="w-full text-[13px] whitespace-nowrap">
                    <thead>
                      <tr :class="isDark ? 'bg-white/[0.04]' : 'bg-slate-50'">
                        <th class="th-cell">شماره</th>
                        <th class="th-cell">مشتری</th>
                        <th class="th-cell">محصول</th>
                        <th class="th-cell">مقدار (کگ)</th>
                        <th class="th-cell">مبلغ</th>
                        <th class="th-cell">تاریخ</th>
                        <th class="th-cell">وضعیت</th>
                        <th class="th-cell">عملیات</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(row, i) in paginatedRows" :key="row.id" :class="['transition-colors', row.isReturn ? 'bg-rose-50/40 dark:bg-rose-500/5' : (i % 2 ? (isDark ? 'bg-white/[0.015]' : 'bg-slate-50/60') : ''), isDark ? 'hover:bg-white/[0.06]' : 'hover:bg-[#FFF9E0]']">
                        <td class="td-cell text-[#9a9a9c]">#{{ toFaNum(row.id) }}</td>
                        <td class="td-cell font-bold">{{ row.customer }}</td>
                        <td class="td-cell">{{ row.product }}</td>
                        <td class="td-cell">{{ toFaNum(row.tons) }}</td>
                        <td class="td-cell" :class="row.isReturn ? 'text-rose-500' : ''">{{ formatRial(row.amount) }}</td>
                        <td class="td-cell text-[#9a9a9c]">{{ row.dateLabel }}</td>
                        <td class="td-cell"><span :class="['px-2.5 py-1 rounded-full text-[11px] font-bold', statusClasses(row.status)]">{{ row.status }}</span></td>
                        <td class="td-cell">
                          <div class="flex items-center gap-1">
                            <button @click="openViewModal(row)" class="icon-btn"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.eye"></span></button>
                            <button @click="openEditModal(row)" class="icon-btn"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.edit"></span></button>
                            <button @click="deleteSale(row)" class="icon-btn hover:!text-rose-500"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.trash"></span></button>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div v-if="!paginatedRows.length" class="empty-box m-6"><span class="w-10 h-10 mx-auto mb-3 block text-slate-300 [&>svg]:w-full [&>svg]:h-full" v-html="icons.empty"></span>نتیجه‌ای یافت نشد</div>
                </div>
                <div class="flex items-center justify-between flex-wrap gap-3 p-4 border-t" :class="isDark ? 'border-white/10' : 'border-black/5'">
                  <p class="text-[12px] text-[#9a9a9c]">{{ toFaNum(paginatedRows.length) }} از {{ toFaNum(tableRows.length) }} رکورد</p>
                  <div class="flex items-center gap-1.5">
                    <button @click="goPage(currentPage - 1)" :disabled="currentPage === 1" class="page-btn rotate-180"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.chevron"></span></button>
                    <button v-for="p in Math.min(totalPages, 7)" :key="p" @click="goPage(p)" :class="['page-btn min-w-[2.2rem]', p === currentPage ? 'bg-[#FFCD05] text-[#3a3a3c]' : '']">{{ toFaNum(p) }}</button>
                    <button @click="goPage(currentPage + 1)" :disabled="currentPage === totalPages" class="page-btn"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.chevron"></span></button>
                  </div>
                </div>
              </section>
            </div>

            <!-- TAB 4: مشتریان -->
            <div v-else-if="activeTab === 'customers'" key="customers" class="space-y-6">
              <section>
                <div class="flex items-center justify-between mb-4">
                  <h3 class="section-title !mb-0">مشتریان برتر</h3>
                  <button @click="openCreateCustomer" class="flex items-center gap-1.5 rounded-full bg-[#FFCD05] text-[#3a3a3c] px-4 py-2.5 text-sm font-bold shadow-md hover:shadow-lg hover:-translate-y-0.5 transition-all">
                    <span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.plus"></span>افزودن
                  </button>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                  <div v-for="c in topCustomerCards" :key="c.id" class="rounded-2xl p-5 ring-1 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-white ring-black/5'">
                    <div class="flex items-center gap-3 mb-3">
                      <div class="w-10 h-10 rounded-xl bg-[#FFF6D6] text-[#8a6d00] dark:bg-[#FFCD05]/10 dark:text-[#FFCD05] flex items-center justify-center shrink-0"><span class="w-5 h-5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.building"></span></div>
                      <div class="min-w-0"><p class="font-bold text-sm truncate">{{ c.name }}</p><p class="text-[11px] text-[#9a9a9c] truncate">{{ c.industry }} · {{ c.province }}</p></div>
                    </div>
                    <div class="space-y-1.5 text-[12px] text-[#9a9a9c]">
                      <div class="flex justify-between"><span>مجموع خرید</span><span class="font-bold text-slate-600 dark:text-slate-200">{{ formatRialCompact(statFor(c.name).amount) }}</span></div>
                      <div class="flex justify-between"><span>تعداد فاکتور</span><span class="font-bold text-slate-600 dark:text-slate-200">{{ toFaNum(statFor(c.name).count) }}</span></div>
                    </div>
                  </div>
                </div>
              </section>

              <section class="rounded-3xl ring-1 shadow-sm overflow-hidden" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-white ring-black/5'">
                <div class="p-5 flex items-center justify-between flex-wrap gap-3 border-b" :class="isDark ? 'border-white/10' : 'border-black/5'">
                  <h3 class="font-bold text-[15px]">فهرست مشتریان</h3>
                  <div class="relative w-full sm:w-64">
                    <span class="absolute inset-y-0 start-3.5 flex items-center pointer-events-none text-[#9a9a9c]"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.search"></span></span>
                    <input v-model="customerSearch" type="text" placeholder="جستجو..." class="w-full ps-10 pe-3 py-2 rounded-full text-[13px] outline-none ring-1 focus:ring-2" :class="isDark ? 'bg-white/5 ring-white/10 focus:ring-[#FFCD05]/50' : 'bg-slate-50 ring-black/5 focus:ring-[#FFCD05]/50'" />
                  </div>
                </div>
                <div class="overflow-x-auto">
                  <table class="w-full text-[13px] whitespace-nowrap">
                    <thead><tr :class="isDark ? 'bg-white/[0.04]' : 'bg-slate-50'">
                      <th class="th-cell">نام شرکت</th><th class="th-cell">شماره تماس</th><th class="th-cell">صنعت</th><th class="th-cell">استان</th><th class="th-cell">وضعیت</th><th class="th-cell">عملیات</th>
                    </tr></thead>
                    <tbody>
                      <tr v-for="(c, i) in paginatedCustomers" :key="c.id" :class="['transition-colors', isDark ? 'hover:bg-white/[0.06]' : 'hover:bg-[#FFF9E0]']">
                        <td class="td-cell font-bold">{{ c.name }}</td>
                        <td class="td-cell text-[#9a9a9c]">{{ c.phone }}</td>
                        <td class="td-cell">{{ c.industry }}</td>
                        <td class="td-cell">{{ c.province }}</td>
                        <td class="td-cell"><span :class="['px-2.5 py-1 rounded-full text-[11px] font-bold', c.status === 'فعال' ? 'bg-emerald-50 text-emerald-700 ring-1 ring-emerald-600/20 dark:bg-emerald-500/10 dark:text-emerald-400' : 'bg-slate-100 text-slate-500']">{{ c.status }}</span></td>
                        <td class="td-cell">
                          <div class="flex items-center gap-1">
                            <button @click="openHistory(c)" class="icon-btn"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.history"></span></button>
                            <button @click="openEditCustomer(c)" class="icon-btn"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.edit"></span></button>
                            <button @click="deleteCustomer(c)" class="icon-btn hover:!text-rose-500"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.trash"></span></button>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div v-if="!paginatedCustomers.length" class="empty-box m-6"><span class="w-10 h-10 mx-auto mb-3 block text-slate-300 [&>svg]:w-full [&>svg]:h-full" v-html="icons.empty"></span>مشتری‌ای یافت نشد</div>
                </div>
                <div class="flex items-center justify-between flex-wrap gap-3 p-4 border-t" :class="isDark ? 'border-white/10' : 'border-black/5'">
                  <p class="text-[12px] text-[#9a9a9c]">{{ toFaNum(paginatedCustomers.length) }} از {{ toFaNum(filteredCustomers.length) }} مشتری</p>
                  <div class="flex items-center gap-1.5">
                    <button @click="goCustomerPage(customerPage - 1)" :disabled="customerPage === 1" class="page-btn rotate-180"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.chevron"></span></button>
                    <button v-for="p in customerTotalPages" :key="p" @click="goCustomerPage(p)" :class="['page-btn min-w-[2.2rem]', p === customerPage ? 'bg-[#FFCD05] text-[#3a3a3c]' : '']">{{ toFaNum(p) }}</button>
                    <button @click="goCustomerPage(customerPage + 1)" :disabled="customerPage === customerTotalPages" class="page-btn"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.chevron"></span></button>
                  </div>
                </div>
              </section>
            </div>

            <!-- TAB 5: تنظیمات -->
            <div v-else-if="activeTab === 'settings'" key="settings" class="space-y-6">
              <section class="rounded-3xl ring-1 shadow-sm overflow-hidden" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-white ring-black/5'">
                <div class="flex flex-wrap gap-2 p-4 border-b" :class="isDark ? 'border-white/10' : 'border-black/5'">
                  <button v-for="s in [{k:'products',l:'محصولات'},{k:'provinces',l:'استان‌ها'},{k:'industries',l:'صنایع'},{k:'payments',l:'نحوه پرداخت'}]" :key="s.k" @click="settingsSection = s.k"
                    :class="['rounded-full px-4 py-2 text-[13px] font-bold transition-all', settingsSection === s.k ? 'bg-[#FFCD05] text-[#3a3a3c]' : (isDark ? 'text-slate-300 hover:bg-white/5' : 'text-[#58585B] hover:bg-slate-50')]">{{ s.l }}</button>
                </div>

                <!-- محصولات -->
                <div v-if="settingsSection === 'products'" class="p-5">
                  <div class="flex items-center justify-between mb-4">
                    <h3 class="font-bold text-[15px]">مدیریت محصولات</h3>
                    <button @click="openCreateProduct" class="flex items-center gap-1.5 rounded-full bg-[#FFCD05] text-[#3a3a3c] px-4 py-2 text-[13px] font-bold shadow-md hover:-translate-y-0.5 transition-all"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.plus"></span>افزودن</button>
                  </div>
                  <div class="overflow-x-auto rounded-2xl ring-1" :class="isDark ? 'ring-white/10' : 'ring-black/5'">
                    <table class="w-full text-[13px] whitespace-nowrap">
                      <thead><tr :class="isDark ? 'bg-white/[0.04]' : 'bg-slate-50'"><th class="th-cell">نام</th><th class="th-cell">کد</th><th class="th-cell">دسته</th><th class="th-cell">عملیات</th></tr></thead>
                      <tbody>
                        <tr v-for="p in products" :key="p.id" class="border-t" :class="isDark ? 'border-white/5' : 'border-black/5'">
                          <td class="td-cell font-bold border-t-0">{{ p.name }}</td>
                          <td class="td-cell border-t-0 text-[#9a9a9c]">{{ p.code }}</td>
                          <td class="td-cell border-t-0">{{ p.category }}</td>
                          <td class="td-cell border-t-0">
                            <div class="flex items-center gap-1">
                              <button @click="openEditProduct(p)" class="icon-btn"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.edit"></span></button>
                              <button @click="deleteProduct(p)" class="icon-btn hover:!text-rose-500"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.trash"></span></button>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <!-- لیست‌های ساده -->
                <div v-else class="p-5">
                  <template v-if="settingsSection === 'provinces'">
                    <div class="flex items-center justify-between mb-4">
                      <h3 class="font-bold text-[15px]">مدیریت استان‌ها</h3>
                      <button @click="provinceManager.openCreate" class="flex items-center gap-1.5 rounded-full bg-[#FFCD05] text-[#3a3a3c] px-4 py-2 text-[13px] font-bold shadow-md hover:-translate-y-0.5 transition-all"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.plus"></span>افزودن</button>
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
                      <div v-for="item in lookupData.provinces" :key="item.id" class="flex items-center justify-between gap-2 rounded-xl px-4 py-3 ring-1" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-slate-50 ring-black/5'">
                        <span class="font-bold text-sm truncate">{{ item.name }}</span>
                        <div class="flex items-center gap-0.5 shrink-0">
                          <button @click="provinceManager.openEdit(item)" class="icon-btn !w-7 !h-7"><span class="w-3.5 h-3.5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.edit"></span></button>
                          <button @click="provinceManager.remove(item)" class="icon-btn !w-7 !h-7 hover:!text-rose-500"><span class="w-3.5 h-3.5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.trash"></span></button>
                        </div>
                      </div>
                    </div>
                  </template>
                  <template v-else-if="settingsSection === 'industries'">
                    <div class="flex items-center justify-between mb-4">
                      <h3 class="font-bold text-[15px]">مدیریت دسته صنایع</h3>
                      <button @click="industryManager.openCreate" class="flex items-center gap-1.5 rounded-full bg-[#FFCD05] text-[#3a3a3c] px-4 py-2 text-[13px] font-bold shadow-md hover:-translate-y-0.5 transition-all"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.plus"></span>افزودن</button>
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
                      <div v-for="item in lookupData.industries" :key="item.id" class="flex items-center justify-between gap-2 rounded-xl px-4 py-3 ring-1" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-slate-50 ring-black/5'">
                        <span class="font-bold text-sm truncate">{{ item.name }}</span>
                        <div class="flex items-center gap-0.5 shrink-0">
                          <button @click="industryManager.openEdit(item)" class="icon-btn !w-7 !h-7"><span class="w-3.5 h-3.5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.edit"></span></button>
                          <button @click="industryManager.remove(item)" class="icon-btn !w-7 !h-7 hover:!text-rose-500"><span class="w-3.5 h-3.5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.trash"></span></button>
                        </div>
                      </div>
                    </div>
                  </template>
                  <template v-else-if="settingsSection === 'payments'">
                    <div class="flex items-center justify-between mb-4">
                      <h3 class="font-bold text-[15px]">نحوه پرداخت</h3>
                      <button @click="paymentManager.openCreate" class="flex items-center gap-1.5 rounded-full bg-[#FFCD05] text-[#3a3a3c] px-4 py-2 text-[13px] font-bold shadow-md hover:-translate-y-0.5 transition-all"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.plus"></span>افزودن</button>
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
                      <div v-for="item in lookupData.payments" :key="item.id" class="flex items-center justify-between gap-2 rounded-xl px-4 py-3 ring-1" :class="isDark ? 'bg-white/[0.03] ring-white/10' : 'bg-slate-50 ring-black/5'">
                        <span class="font-bold text-sm truncate">{{ item.name }}</span>
                        <div class="flex items-center gap-0.5 shrink-0">
                          <button @click="paymentManager.openEdit(item)" class="icon-btn !w-7 !h-7"><span class="w-3.5 h-3.5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.edit"></span></button>
                          <button @click="paymentManager.remove(item)" class="icon-btn !w-7 !h-7 hover:!text-rose-500"><span class="w-3.5 h-3.5 [&>svg]:w-full [&>svg]:h-full" v-html="icons.trash"></span></button>
                        </div>
                      </div>
                    </div>
                  </template>
                </div>
              </section>
            </div>
          </Transition>
        </template>
      </main>
    </div>

    <!-- FAB -->
    <button @click="openCreateModal" class="fixed bottom-6 left-6 z-40 w-14 h-14 rounded-full bg-[#FFCD05] text-[#3a3a3c] shadow-2xl flex items-center justify-center hover:scale-110 active:scale-95 transition-transform ring-4 ring-[#FFCD05]/30">
      <span class="w-6 h-6 [&>svg]:w-full [&>svg]:h-full" v-html="icons.plus"></span>
    </button>

    <!-- Sale Modal -->
    <Transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition duration-150 ease-in" leave-to-class="opacity-0">
      <div v-if="showModal" class="fixed inset-0 z-[90] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm" @click.self="closeModal">
        <div class="w-full max-w-2xl max-h-[90vh] overflow-y-auto rounded-3xl p-6 sm:p-7 shadow-2xl ring-1" :class="isDark ? 'bg-[#2a2a2c] ring-white/10 text-slate-100' : 'bg-white ring-black/5'">
          <div class="flex items-center justify-between mb-5">
            <h3 class="font-extrabold text-lg">{{ modalMode === 'create' ? 'افزودن فروش جدید' : modalMode === 'edit' ? 'ویرایش فروش' : 'مشاهده فروش' }}</h3>
            <button @click="closeModal" class="w-9 h-9 rounded-full flex items-center justify-center hover:bg-black/5"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.close"></span></button>
          </div>
          <fieldset :disabled="modalMode === 'view'" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="sm:col-span-2">
              <label class="form-label">نام مشتری *</label>
              <input v-model="saleForm.customer" list="clist" type="text" class="input-field" placeholder="نام شرکت" />
              <datalist id="clist"><option v-for="c in customerOptions" :key="c" :value="c" /></datalist>
            </div>
            <div>
              <label class="form-label">محصول *</label>
              <select v-model="saleForm.product" class="input-field"><option v-for="p in productOptions" :key="p" :value="p">{{ p }}</option></select>
            </div>
            <div>
              <label class="form-label">مقدار (کیلوگرم) *</label>
              <input v-model.number="saleForm.tons" type="number" min="0" class="input-field" />
            </div>
            <div>
              <label class="form-label">قیمت هر کیلو (ریال) *</label>
              <input v-model.number="saleForm.price" type="number" min="0" class="input-field" />
            </div>
            <div>
              <label class="form-label">تاریخ (شمسی)</label>
              <input v-model="saleForm.date" type="text" class="input-field" placeholder="۱۴۰۵/۰۴/۱۰" />
            </div>
            <div>
              <label class="form-label">نوع فروش</label>
              <div class="flex gap-2">
                <button type="button" @click="saleForm.saleType = 'رسمی'" :class="['toggle-chip', saleForm.saleType === 'رسمی' && 'toggle-chip-active']">رسمی</button>
                <button type="button" @click="saleForm.saleType = 'غیررسمی'" :class="['toggle-chip', saleForm.saleType === 'غیررسمی' && 'toggle-chip-active']">غیررسمی</button>
              </div>
            </div>
            <div>
              <label class="form-label">نحوه پرداخت</label>
              <select v-model="saleForm.payment" class="input-field"><option v-for="p in paymentMethods" :key="p" :value="p">{{ p }}</option></select>
            </div>
            <div>
              <label class="form-label">وضعیت</label>
              <select v-model="saleForm.status" class="input-field">
                <option>در حال پردازش</option><option>تکمیل شده</option><option>لغو شده</option><option>برگشتی</option>
              </select>
            </div>
            <div class="sm:col-span-2">
              <label class="form-label">توضیحات</label>
              <textarea v-model="saleForm.description" rows="3" class="input-field resize-none"></textarea>
            </div>
          </fieldset>
          <div class="flex items-center gap-3 mt-6">
            <button v-if="modalMode !== 'view'" @click="submitSale" class="flex-1 rounded-full bg-[#FFCD05] text-[#3a3a3c] py-3 text-sm font-bold shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all">ذخیره</button>
            <button @click="closeModal" class="flex-1 rounded-full py-3 text-sm font-bold ring-1 transition" :class="isDark ? 'ring-white/15' : 'ring-black/10'">{{ modalMode === 'view' ? 'بستن' : 'انصراف' }}</button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Customer Modal -->
    <Transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition duration-150 ease-in" leave-to-class="opacity-0">
      <div v-if="showCustomerModal" class="fixed inset-0 z-[90] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm" @click.self="closeCustomerModal">
        <div class="w-full max-w-xl max-h-[90vh] overflow-y-auto rounded-3xl p-6 sm:p-7 shadow-2xl ring-1" :class="isDark ? 'bg-[#2a2a2c] ring-white/10 text-slate-100' : 'bg-white ring-black/5'">
          <div class="flex items-center justify-between mb-5">
            <h3 class="font-extrabold text-lg">{{ customerModalMode === 'edit' ? 'ویرایش مشتری' : 'افزودن مشتری' }}</h3>
            <button @click="closeCustomerModal" class="w-9 h-9 rounded-full flex items-center justify-center hover:bg-black/5"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.close"></span></button>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="sm:col-span-2"><label class="form-label">نام شرکت *</label><input v-model="customerForm.name" type="text" class="input-field" /></div>
            <div><label class="form-label">شماره تماس *</label><input v-model="customerForm.phone" type="text" class="input-field" /></div>
            <div><label class="form-label">ایمیل</label><input v-model="customerForm.email" type="email" class="input-field" /></div>
            <div><label class="form-label">استان</label><select v-model="customerForm.province" class="input-field"><option v-for="p in provinces" :key="p" :value="p">{{ p }}</option></select></div>
            <div><label class="form-label">صنعت</label><select v-model="customerForm.industry" class="input-field"><option v-for="i in industries" :key="i" :value="i">{{ i }}</option></select></div>
            <div class="sm:col-span-2"><label class="form-label">آدرس</label><input v-model="customerForm.address" type="text" class="input-field" /></div>
          </div>
          <div class="flex items-center gap-3 mt-6">
            <button @click="submitCustomer" class="flex-1 rounded-full bg-[#FFCD05] text-[#3a3a3c] py-3 text-sm font-bold shadow-lg hover:-translate-y-0.5 transition-all">ذخیره</button>
            <button @click="closeCustomerModal" class="flex-1 rounded-full py-3 text-sm font-bold ring-1" :class="isDark ? 'ring-white/15' : 'ring-black/10'">انصراف</button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- History Modal -->
    <Transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition duration-150 ease-in" leave-to-class="opacity-0">
      <div v-if="showHistoryModal" class="fixed inset-0 z-[90] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm" @click.self="closeHistory">
        <div class="w-full max-w-2xl max-h-[85vh] overflow-y-auto rounded-3xl p-6 shadow-2xl ring-1" :class="isDark ? 'bg-[#2a2a2c] ring-white/10 text-slate-100' : 'bg-white ring-black/5'">
          <div class="flex items-center justify-between mb-5">
            <h3 class="font-extrabold text-lg">تاریخچه — {{ historyCustomer?.name }}</h3>
            <button @click="closeHistory" class="w-9 h-9 rounded-full flex items-center justify-center hover:bg-black/5"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.close"></span></button>
          </div>
          <div class="overflow-x-auto rounded-2xl ring-1" :class="isDark ? 'ring-white/10' : 'ring-black/5'">
            <table class="w-full text-[13px] whitespace-nowrap">
              <thead><tr :class="isDark ? 'bg-white/[0.04]' : 'bg-slate-50'"><th class="th-cell">تاریخ</th><th class="th-cell">محصول</th><th class="th-cell">مقدار</th><th class="th-cell">مبلغ</th><th class="th-cell">نوع</th></tr></thead>
              <tbody>
                <tr v-for="row in historyRows" :key="row.id" class="border-t" :class="isDark ? 'border-white/5' : 'border-black/5'">
                  <td class="td-cell border-t-0 text-[#9a9a9c]">{{ row.dateLabel }}</td>
                  <td class="td-cell border-t-0 font-bold">{{ row.product }}</td>
                  <td class="td-cell border-t-0">{{ toFaNum(row.tons) }} کگ</td>
                  <td class="td-cell border-t-0" :class="row.isReturn ? 'text-rose-500' : ''">{{ formatRial(row.amount) }}</td>
                  <td class="td-cell border-t-0">
                    <span :class="['px-2 py-0.5 rounded-full text-[11px] font-bold',
                      row.isReturn
                        ? 'bg-rose-100 text-rose-700 dark:bg-rose-500/20 dark:text-rose-400'
                        : (row.saleType === 'غیررسمی'
                            ? 'bg-slate-100 text-slate-600 dark:bg-white/10 dark:text-slate-300'
                            : 'bg-emerald-50 text-emerald-700 dark:bg-emerald-500/10 dark:text-emerald-400')]">
                      {{ row.isReturn ? 'برگشتی' : (row.saleType || 'رسمی') }}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
            <div v-if="!historyRows.length" class="empty-box m-6">سابقه‌ای ثبت نشده</div>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Product Modal -->
    <Transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition duration-150 ease-in" leave-to-class="opacity-0">
      <div v-if="showProductModal" class="fixed inset-0 z-[90] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm" @click.self="closeProductModal">
        <div class="w-full max-w-md rounded-3xl p-6 sm:p-7 shadow-2xl ring-1" :class="isDark ? 'bg-[#2a2a2c] ring-white/10 text-slate-100' : 'bg-white ring-black/5'">
          <div class="flex items-center justify-between mb-5">
            <h3 class="font-extrabold text-lg">{{ productModalMode === 'edit' ? 'ویرایش محصول' : 'افزودن محصول' }}</h3>
            <button @click="closeProductModal" class="w-9 h-9 rounded-full flex items-center justify-center hover:bg-black/5"><span class="w-4 h-4 [&>svg]:w-full [&>svg]:h-full" v-html="icons.close"></span></button>
          </div>
          <div class="space-y-4">
            <div><label class="form-label">نام محصول *</label><input v-model="productForm.name" type="text" class="input-field" /></div>
            <div><label class="form-label">کد محصول *</label><input v-model="productForm.code" type="text" class="input-field" /></div>
            <div><label class="form-label">دسته‌بندی</label><input v-model="productForm.category" type="text" class="input-field" /></div>
          </div>
          <div class="flex items-center gap-3 mt-6">
            <button @click="submitProduct" class="flex-1 rounded-full bg-[#FFCD05] text-[#3a3a3c] py-3 text-sm font-bold shadow-lg hover:-translate-y-0.5 transition-all">ذخیره</button>
            <button @click="closeProductModal" class="flex-1 rounded-full py-3 text-sm font-bold ring-1" :class="isDark ? 'ring-white/15' : 'ring-black/10'">انصراف</button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Simple List Editors -->
    <template v-for="mgr in [{ m: provinceManager, t: 'استان' }, { m: industryManager, t: 'صنعت' }, { m: paymentManager, t: 'روش پرداخت' }]" :key="mgr.t">
      <Transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition duration-150 ease-in" leave-to-class="opacity-0">
        <div v-if="mgr.m.showEditor.value" class="fixed inset-0 z-[90] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm" @click.self="mgr.m.close">
          <div class="w-full max-w-sm rounded-3xl p-6 shadow-2xl ring-1" :class="isDark ? 'bg-[#2a2a2c] ring-white/10 text-slate-100' : 'bg-white ring-black/5'">
            <h3 class="font-extrabold text-lg mb-4">{{ mgr.m.mode.value === 'edit' ? 'ویرایش' : 'افزودن' }} {{ mgr.t }}</h3>
            <input v-model="mgr.m.value.value" type="text" class="input-field" :placeholder="`نام ${mgr.t}`" />
            <div class="flex items-center gap-3 mt-5">
              <button @click="mgr.m.submit" class="flex-1 rounded-full bg-[#FFCD05] text-[#3a3a3c] py-2.5 text-sm font-bold shadow-md">ذخیره</button>
              <button @click="mgr.m.close" class="flex-1 rounded-full py-2.5 text-sm font-bold ring-1" :class="isDark ? 'ring-white/15' : 'ring-black/10'">انصراف</button>
            </div>
          </div>
        </div>
      </Transition>
    </template>

  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap');

::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-thumb { background: rgba(148,163,184,.4); border-radius: 999px; }

.select-field, .input-field {
  width: 100%; border-radius: 0.9rem; padding: 0.6rem 0.9rem;
  font-size: 13px; outline: none; transition: all .2s;
  background-color: rgba(0,0,0,0.02); border: 1px solid rgba(0,0,0,0.06);
}
.dark .select-field, .dark .input-field {
  background-color: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1); color: #E5E9F0;
}
.select-field:focus, .input-field:focus { box-shadow: 0 0 0 3px rgba(255,205,5,0.3); border-color: #FFCD05; }

.form-label { display:block; font-size:11px; font-weight:600; color:#9a9a9c; margin-bottom:0.35rem; }

.toggle-chip { flex:1; padding:0.55rem 0.8rem; border-radius:999px; font-size:13px; font-weight:700; border:1px solid rgba(0,0,0,0.08); background:transparent; transition:all .2s; cursor:pointer; }
.dark .toggle-chip { border-color: rgba(255,255,255,0.12); color:#CBD5E1; }
.toggle-chip-active { background:#FFCD05; color:#3a3a3c; border-color:#FFCD05; }

.chart-card { border-radius:1.5rem; padding:1.25rem 1.1rem 0.5rem; background:white; box-shadow:0 1px 2px rgba(0,0,0,0.04); border:1px solid rgba(0,0,0,0.05); transition:box-shadow .25s, transform .25s; min-width:0; }
.chart-card:hover { box-shadow:0 12px 30px rgba(0,0,0,0.08); transform:translateY(-2px); }
.dark .chart-card { background:rgba(255,255,255,0.03); border-color:rgba(255,255,255,0.1); }
.chart-title { font-size:13.5px; font-weight:800; margin-bottom:0.5rem; }
.section-title { font-size:15px; font-weight:800; margin-bottom:0.85rem; }

.th-cell { padding:0.85rem 1rem; text-align:start; font-size:11.5px; font-weight:700; color:#9a9a9c; }
.td-cell { padding:0.75rem 1rem; border-top:1px solid rgba(0,0,0,0.045); }
.dark .td-cell { border-top-color:rgba(255,255,255,0.06); }

.icon-btn { width:2rem; height:2rem; border-radius:0.65rem; display:flex; align-items:center; justify-content:center; color:#9a9a9c; transition:all .2s; }
.icon-btn:hover { background:rgba(0,0,0,0.05); color:#3a3a3c; }
.dark .icon-btn:hover { background:rgba(255,255,255,0.08); color:#FFCD05; }

.page-btn { min-width:2rem; height:2rem; padding:0 0.5rem; border-radius:0.65rem; font-size:12px; font-weight:700; display:flex; align-items:center; justify-content:center; color:#9a9a9c; transition:all .2s; }
.page-btn:hover:not(:disabled) { background:rgba(0,0,0,0.05); }
.dark .page-btn:hover:not(:disabled) { background:rgba(255,255,255,0.08); }
.page-btn:disabled { opacity:.35; cursor:not-allowed; }

.empty-box { padding:2.5rem 1rem; text-align:center; font-size:13px; color:#9a9a9c; font-weight:600; }

@media print { header, aside, .fixed, .icon-btn { display:none !important; } }
</style>