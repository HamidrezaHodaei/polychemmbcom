<!-- /fa/contact/index.vue -->
<template>
  <div>
    <navbar />
    <div dir="rtl" class="font-[IRANYekan]">
      <div class="min-h-screen bg-[#f1f2f2] py-16 px-4 relative font-[IRANYekan]">

        <!-- بخش آدرس -->
        <div id="address-section" ref="addressSection" class="max-w-7xl mx-auto mb-12 relative z-10">
          <div class="bg-white rounded-lg shadow-lg p-8">
            <div class="flex flex-col lg:flex-row gap-8 items-start">
              <div class="flex-1 space-y-6 text-right">
                <div>
                  <h3 class="text-2xl font-semibold text-[#848484] mb-4">دفتر مرکزی</h3>
                  <p class="text-[#848484] leading-relaxed">
                    تهران - خیابان شریعتی – بالاتر از میرداماد<br />
                    خیابان منظر نژاد – ساختمان یاس<br />
                    پلاک ۴۵
                  </p>
                </div>
                <div>
                  <h3 class="text-2xl font-semibold text-[#848484] mb-4">کارخانه</h3>
                  <p class="text-[#848484] leading-relaxed">
                    منطقه آزاد ارس – جلفا – شهرک صنعتی فاز دو<br />
                    خیابان C یک جنوبی - قطعات ۴۳۷ و ۴۳۸
                  </p>
                </div>
                <div>
                  <h4 class="text-lg font-semibold text-[#848484] mb-2">اطلاعات تماس</h4>
                  <div class="space-y-2">
                    <p class="text-[#848484]">
                      <span class="font-medium">ایمیل:</span>
                      <a href="mailto:info@polychemmb.com" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                        info@polychemmb.com
                      </a>
                    </p>
                    <p class="text-[#848484]">
                      <span class="font-medium">تلفن:</span>
                      <a href="tel:+982122898979" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                        ۸۰-۸۹۷۹ ۲۲۸۹ ۰۲۱
                      </a>
                    </p>
                  </div>
                </div>

                <div>
                  <h4 class="text-lg font-semibold text-[#848484] mb-2">ساعات کاری</h4>
                  <p class="text-[#848484]">
                    <span class="font-medium">شنبه تا چهارشنبه:</span><br />
                    ۰۸:۰۰ – ۱۷:۰۰<br /><br />
                    <span class="font-medium">پنجشنبه و جمعه:</span><br />
                    ۰۸:۰۰ – ۱۶:۰۰
                  </p>
                </div>

                <div>
                  <h4 class="text-lg font-semibold text-[#848484] mb-2">تماس با واحد بازاریابی و فروش</h4>
                  <div class="space-y-2">
                    <p class="text-[#848484]">
                      <span class="font-medium inline-block w-16">ایمیل:</span>
                      <a href="mailto:Sales@polychemmb.com" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                        Sales@polychemmb.com
                      </a>
                    </p>
                    <p class="text-[#848484]">
                      <span class="font-medium inline-block w-16">تلفن:</span>
                      <a href="tel:+989144605066" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                        ۶۶ ۵۰ ۴۶۰ ۰۹۱۴
                      </a>
                    </p>
                    <p class="text-[#848484]">
                      <span class="font-medium inline-block w-16">تلفن:</span>
                      <a href="tel:+989004605066" class="text-[#848484] hover:text-[#FFD700] transition-colors">
                        ۶۶ ۵۰ ۴۶۰ ۰۹۰۰
                      </a>
                    </p>
                  </div>
                </div>
              </div>

              <div class="flex-1 w-full">
                <MapComponent />
              </div>
            </div>
          </div>
        </div>

        <!-- فرم تماس -->
        <div id="form-section" ref="formSection" class="max-w-7xl mx-auto mb-12">
          <FormComponent :countries="allContactCountryNames" />
        </div>

      </div>
    </div>
    <Chatbox />
    <footer2 />
  </div>
</template>

<script setup>
import FormComponent from '~/components/fa/contact/form.vue'
import MapComponent from '~/components/fa/contact/map.vue'
import navbar from '~/components/fa/layout/navbar.vue'
import footer2 from '~/components/fa/layout/footer.vue'
import Chatbox from '~/components/fa/chatbox/chatbox.vue'

// کشورها فقط برای فرم تماس
const allContactCountryNames = [
  'Iraq', 'Iran', 'Kuwait',
  'Armenia', 'Azerbaijan', 'Belarus', 'Kazakhstan',
  'Kyrgyzstan', 'Russia', 'Tajikistan', 'Uzbekistan',
  'Turkey', 'Greece',
  'China', 'India', 'Pakistan'
]
</script>