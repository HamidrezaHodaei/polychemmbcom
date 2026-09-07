<template>
  <NuxtPage />
  <AppLoading />
</template>

<script setup>
import AppLoading from '~/components/en/loading/AppLoading.vue'

const config = useRuntimeConfig()
const siteUrl = config.public.siteUrl || 'https://polychemmb.com'
const siteLogo = `${siteUrl}/logo.png`

useHead({
  htmlAttrs: { lang: 'en', dir: 'ltr' },

  meta: [
    { name: 'theme-color', content: '#1a202c' },
    { name: 'color-scheme', content: 'light' },
    { name: 'mobile-web-app-capable', content: 'yes' },
    { name: 'apple-mobile-web-app-capable', content: 'yes' },
    { name: 'author', content: 'Polychem Corporation (Polychemmb)' },
    { name: 'audience', content: 'B2B, Industrial, Manufacturing, Distributors' },
    {
      name: 'keywords',
      content: [
        // فارسی
        'پلیکم', 'پلی کم', 'پلی‌کم', 'پلیمرشیمی ارس', 'پلیمر شیمی ارس',
        'مستربچ', 'مستربچ رنگی', 'مستربچ پرکننده', 'مستربچ افزودنی',
        'کامپاند پلیمر', 'کامپاند PP', 'کامپاند پلی پروپیلن',
        'تولیدکننده مستربچ', 'تولیدکننده مستربچ ایران', 'مستربچ ایران',
        'مستربچ ارس', 'منطقه آزاد ارس', 'کربنات کلسیم مستربچ',
        'رنگ‌دهنده پلاستیک', 'افزودنی پلاستیک', 'تولید مستربچ در ایران',
        // English
        'masterbatch', 'color masterbatch', 'filler masterbatch', 'additive masterbatch',
        'polymer compound', 'PP compound', 'masterbatch manufacturer Iran',
        'Polychem', 'Polychemmb', 'Aras Free Zone', 'CaCO3 masterbatch',
        'UV masterbatch', 'flame retardant masterbatch', 'anti-static masterbatch',
        // Arabic
        'ماسترباتش', 'ماسترباتش ملون', 'ماسترباتش الحشو', 'مركبات البوليمر',
        'مصنع ماسترباتش', 'ماسترباتش إيران', 'بولي بروبيلين مركب',
        // Turkish
        'masterbatch', 'renkli masterbatch', 'dolgu masterbatch', 'polimer bileşik',
        'masterbatch üreticisi', 'PP bileşik', 'İran masterbatch',
      ].join(', ')
    },
  ],

  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico?v=6' },
    { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png?v=6' },
    { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png?v=6' },
    { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png?v=6' },
    { rel: 'manifest', href: '/site.webmanifest' },
    { rel: 'dns-prefetch', href: 'https://fonts.googleapis.com' },
    { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
    { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: 'anonymous' },
    // hreflang global
    { rel: 'alternate', hreflang: 'en', href: `${siteUrl}/en` },
    { rel: 'alternate', hreflang: 'fa', href: `${siteUrl}/fa` },
    { rel: 'alternate', hreflang: 'ar', href: `${siteUrl}/ar` },
    { rel: 'alternate', hreflang: 'tr', href: `${siteUrl}/tr` },
    { rel: 'alternate', hreflang: 'x-default', href: `${siteUrl}/en` },
  ],

  script: [
    // ✅ Organization Schema — چندزبانه کامل
    {
      type: 'application/ld+json',
      key: 'organization-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Organization',
        '@id': `${siteUrl}/#organization`,
        name: 'Polychem',
        legalName: 'Polychem Corporation',
        alternateName: [
          // English variants
          'Polychemmb', 'Polychem MB', 'Polychem Iran',
          // فارسی
          'پلی‌کم', 'پلیکم', 'پلی کم', 'پلی کم ایران',
          'پلیمرشیمی ارس', 'پلیمر شیمی ارس',
          'مستربچ ارس', 'کامپاند پلیمر ارس',
          // Arabic
          'بولي كيم', 'بوليكيم', 'منطقة أراس الحرة',
          // Turkish
          'Polychem Aras', 'Polychem İran',
        ],
        url: siteUrl,
        logo: {
          '@type': 'ImageObject',
          '@id': `${siteUrl}/#logo`,
          url: siteLogo,
          contentUrl: siteLogo,
          caption: 'Polychem Polychemmb Logo - Masterbatch & Polymer Compound Manufacturer Iran',
          width: 250,
          height: 250,
          name: 'Polychem Polychemmb Logo',
          description: 'Logo of Polychem (Polychemmb) — پلیکم — تولیدکننده مستربچ و کامپاند پلیمر در ایران',
        },
        description: [
          // English
          "Polychem (Polychemmb) is Iran's leading manufacturer of masterbatch and polymer compounds. products include color masterbatch, filler masterbatch, additive masterbatch, PP compound, and engineering polymer blends. Located in Aras Free Zone, exporting to Middle East, Caucasus, and Central Asia since 2015.",
          // فارسی
          'پلی‌کم (پلیمرشیمی ارس) پیشروترین تولیدکننده مستربچ و کامپاند پلیمر در ایران است. محصولات شامل مستربچ رنگی، مستربچ پرکننده، مستربچ افزودنی، کامپاند PP و آلیاژهای پلیمری مهندسی می‌شود. واقع در منطقه آزاد ارس، از سال ۱۳۹۴ در حال صادرات به خاورمیانه، قفقاز و آسیای مرکزی.',
        ].join(' | '),
        foundingDate: '2015',
        slogan: 'Innovation in Polymers — Masterbatch & Compound Solutions | نوآوری در پلیمر — راهکارهای مستربچ و کامپاند',
        telephone: ['+98-921-22898980', '+98-921-2289898'],
        email: 'info@polychemmb.com',
        address: {
          '@type': 'PostalAddress',
          streetAddress: 'Aras Free Trade-Industrial Zone',
          addressLocality: 'Jolfa',
          addressRegion: 'East Azerbaijan Province',
          postalCode: '5481',
          addressCountry: { '@type': 'Country', name: 'Iran' },
        },
        geo: {
          '@type': 'GeoCoordinates',
          latitude: 38.930278,
          longitude: 45.633889,
        },
        naics: '325211',
        isicV4: '2013',
        areaServed: [
          { '@type': 'Country', name: 'Iran', alternateName: 'IR' },
          { '@type': 'Country', name: 'Turkey', alternateName: 'TR' },
          { '@type': 'Country', name: 'Iraq', alternateName: 'IQ' },
          { '@type': 'Country', name: 'Armenia', alternateName: 'AM' },
          { '@type': 'Country', name: 'Azerbaijan', alternateName: 'AZ' },
          { '@type': 'Place', name: 'Middle East' },
          { '@type': 'Place', name: 'Caucasus Region' },
          { '@type': 'Place', name: 'Central Asia' },
        ],
        hasOfferCatalog: {
          '@type': 'OfferCatalog',
          name: 'Masterbatch & Polymer Compound products | محصولات مستربچ و کامپاند پلیمر',
          itemListElement: [
            {
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Product',
                name: 'Color Masterbatch',
                alternateName: [
                  'Colour Masterbatch', 'Pigment Masterbatch',
                  'مستربچ رنگی', 'مستربچ رنگ',
                  'ماسترباتش ملون', 'ماسترباتش الألوان',
                  'Renkli Masterbatch', 'Renk Masterbatch',
                ],
                description: 'High-quality concentrated color masterbatch | مستربچ رنگی با کیفیت بالا برای PE، PP، PS، ABS توسط پلی‌کم (پلیمرشیمی ارس) در منطقه آزاد ارس ایران.',
                category: 'Masterbatch',
                brand: { '@type': 'Brand', name: 'Polychem', alternateName: ['Polychemmb', 'پلیکم', 'پلی‌کم'] },
                manufacturer: { '@id': `${siteUrl}/#organization` },
              },
            },
            {
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Product',
                name: 'Filler Masterbatch',
                alternateName: [
                  'CaCO3 Masterbatch', 'Calcium Carbonate Masterbatch',
                  'مستربچ پرکننده', 'مستربچ کربنات کلسیم', 'مستربچ CaCO3',
                  'ماسترباتش الحشو', 'ماسترباتش كربونات الكالسيوم',
                  'Dolgu Masterbatch', 'CaCO3 Masterbatch TR',
                ],
                description: 'Premium CaCO3 filler masterbatch | مستربچ پرکننده CaCO3 پریمیوم توسط پلی‌کم برای بهینه‌سازی هزینه و بهبود خواص مکانیکی محصولات پلاستیکی.',
                category: 'Masterbatch',
                brand: { '@type': 'Brand', name: 'Polychem', alternateName: ['Polychemmb', 'پلیکم'] },
                manufacturer: { '@id': `${siteUrl}/#organization` },
              },
            },
            {
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Product',
                name: 'PP Compound',
                alternateName: [
                  'PP-Talc Compound', 'Polypropylene Compound',
                  'کامپاند PP', 'کامپاند پلی‌پروپیلن', 'کامپاند PP-Talc',
                  'مركب البولي بروبيلين', 'بولي بروبيلين مركب',
                  'PP Bileşik', 'Polipropilen Bileşik',
                ],
                description: 'Engineering grade PP compound | کامپاند PP درجه مهندسی و کامپاند PP-Talc توسط پلی‌کم برای کاربردهای خودرویی و صنعتی.',
                category: 'Polymer Compound',
                brand: { '@type': 'Brand', name: 'Polychem', alternateName: ['Polychemmb', 'پلیکم'] },
                manufacturer: { '@id': `${siteUrl}/#organization` },
              },
            },
            {
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Product',
                name: 'Additive Masterbatch',
                alternateName: [
                  'UV Masterbatch', 'Flame Retardant Masterbatch', 'Anti-Static Masterbatch',
                  'مستربچ افزودنی', 'مستربچ UV', 'مستربچ ضد آتش', 'مستربچ آنتی استاتیک',
                  'ماسترباتش الإضافات', 'ماسترباتش مضاد للحرائق', 'ماسترباتش مضاد للكهرباء الساكنة',
                  'Katkı Masterbatch', 'UV Masterbatch TR', 'Alev Geciktirici Masterbatch',
                ],
                description: 'Specialized additive masterbatch | مستربچ افزودنی تخصصی: UV، ضد آتش، آنتی‌استاتیک توسط پلی‌کم (پلیمرشیمی ارس).',
                category: 'Masterbatch',
                brand: { '@type': 'Brand', name: 'Polychem', alternateName: ['Polychemmb', 'پلیکم'] },
                manufacturer: { '@id': `${siteUrl}/#organization` },
              },
            },
          ],
        },
        contactPoint: [
          {
            '@type': 'ContactPoint',
            telephone: '+98-921-22898980',
            contactType: 'sales',
            availableLanguage: ['English', 'Persian', 'Turkish', 'Arabic'],
            areaServed: ['IR', 'TR', 'IQ', 'AM', 'AZ'],
          },
          {
            '@type': 'ContactPoint',
            email: 'info@polychemmb.com',
            contactType: 'customer service',
            availableLanguage: ['English', 'Persian', 'Arabic', 'Turkish'],
          },
        ],
        sameAs: [
          'https://www.linkedin.com/company/polychemmb',
          'https://twitter.com/polychemmb',
          'https://www.instagram.com/polychemmb',
          'https://www.facebook.com/polychemmb',
        ],
        award: ['ISO 9001:2015 Certified', 'Export Quality Standard'],
        knowAbout: [
          // English
          'Masterbatch Manufacturing', 'Polymer Compound Production',
          'Color Masterbatch', 'Filler Masterbatch', 'PP Compound',
          'Engineering Polymers', 'Plastic Additives', 'Polymer Compounding',
          // فارسی
          'مستربچ', 'مستربچ رنگی', 'مستربچ پرکننده', 'مستربچ افزودنی',
          'کامپاند پلیمر', 'کامپاند PP', 'کامپاند پلی پروپیلن',
          'تولید مستربچ در ایران', 'مستربچ ایران', 'پلیمرشیمی ارس',
          'منطقه آزاد ارس', 'تولیدکننده مستربچ', 'تولیدکننده کامپاند',
          'رنگ‌دهنده پلاستیک', 'افزودنی پلاستیک', 'پلیکم', 'پلی‌کم',
          // Arabic
          'ماسترباتش', 'ماسترباتش ملون', 'ماسترباتش الحشو', 'مركبات البوليمر',
          'مصنع ماسترباتش إيران', 'بولي بروبيلين مركب',
          // Turkish
          'masterbatch üretimi', 'polimer bileşik üretimi',
          'renkli masterbatch', 'dolgu masterbatch', 'PP bileşik',
        ],
      }),
    },

    // ✅ WebSite Schema + SiteLinksSearchBox + Sitelinks signals
    {
      type: 'application/ld+json',
      key: 'website-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'WebSite',
        '@id': `${siteUrl}/#website`,
        url: siteUrl,
        name: 'Polychem Polychemmb — Masterbatch & Polymer Compound | پلیکم — مستربچ و کامپاند پلیمر',
        alternateName: [
          'Polychemmb', 'Polychem Iran', 'پلی‌کم', 'پلیکم',
          'پلیمرشیمی ارس', 'Polychem Aras',
        ],
        description: "Official website of Polychem (Polychemmb) | وب‌سایت رسمی پلی‌کم (پلیمرشیمی ارس) — تولیدکننده مستربچ و کامپاند پلیمر در ایران.",
        publisher: { '@id': `${siteUrl}/#organization` },
        inLanguage: ['en', 'fa', 'ar', 'tr'],
        // ✅ SiteLinksSearchBox — باعث میشه گوگل کادر جستجو زیر نتیجه نشون بده
        potentialAction: [
          {
            '@type': 'SearchAction',
            target: {
              '@type': 'EntryPoint',
              urlTemplate: `${siteUrl}/search?q={search_term_string}`,
            },
            'query-input': 'required name=search_term_string',
          },
          // ✅ این بخش Sitelinks رو تقویت می‌کنه — گوگل میفهمه صفحات مهم کدوماست
          {
            '@type': 'ViewAction',
            name: 'products | محصولات',
            target: [
              `${siteUrl}/en/products`,
              `${siteUrl}/fa/products`,
              `${siteUrl}/ar/products`,
              `${siteUrl}/tr/products`,
            ],
          },
          {
            '@type': 'ViewAction',
            name: 'About | درباره ما',
            target: [
              `${siteUrl}/en/about`,
              `${siteUrl}/fa/about`,
              `${siteUrl}/ar/about`,
              `${siteUrl}/tr/about`,
            ],
          },
          {
            '@type': 'ViewAction',
            name: 'Contact | تماس با ما',
            target: [
              `${siteUrl}/en/contact`,
              `${siteUrl}/fa/contact`,
              `${siteUrl}/ar/contact`,
              `${siteUrl}/tr/contact`,
            ],
          },
        ],
      }),
    },

    // ✅ ItemList Schema — معرفی صفحات اصلی به گوگل برای Sitelinks
    {
      type: 'application/ld+json',
      key: 'sitelinks-itemlist-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        name: 'Polychem Main Pages | صفحات اصلی پلیکم',
        description: 'Key sections of Polychem (Polychemmb) website — masterbatch and polymer compound manufacturer',
        url: siteUrl,
        numberOfItems: 4,
        itemListElement: [
          {
            '@type': 'SiteLinksSearchBox',
            target: {
              '@type': 'EntryPoint',
              urlTemplate: `${siteUrl}/search?q={search_term_string}`,
            },
          },
          {
            '@type': 'ListItem',
            position: 1,
            name: 'products | محصولات | المنتجات | Ürünler',
            description: 'Color masterbatch, filler masterbatch, additive masterbatch, PP compound | مستربچ رنگی، پرکننده، افزودنی، کامپاند PP',
            url: `${siteUrl}/en/products`,
            item: {
              '@type': 'WebPage',
              '@id': `${siteUrl}/en/products`,
              name: 'products — Masterbatch & Polymer Compound | محصولات پلیکم',
              url: `${siteUrl}/en/products`,
              inLanguage: ['en', 'fa', 'ar', 'tr'],
              isPartOf: { '@id': `${siteUrl}/#website` },
            },
          },
          {
            '@type': 'ListItem',
            position: 2,
            name: 'About Polychem | درباره پلیکم | عن بولي كيم | Polychem Hakkında',
            description: "Iran's leading masterbatch manufacturer since 2015, Aras Free Zone | تولیدکننده پیشرو مستربچ ایران از ۱۳۹۴، منطقه آزاد ارس",
            url: `${siteUrl}/en/about`,
            item: {
              '@type': 'WebPage',
              '@id': `${siteUrl}/en/about`,
              name: 'About Polychem (Polychemmb) | درباره پلیکم',
              url: `${siteUrl}/en/about`,
              inLanguage: ['en', 'fa', 'ar', 'tr'],
              isPartOf: { '@id': `${siteUrl}/#website` },
            },
          },
          {
            '@type': 'ListItem',
            position: 3,
            name: 'Contact | تماس با ما | اتصل بنا | İletişim',
            description: 'Contact Polychem for masterbatch and polymer compound inquiries | تماس با پلیکم برای استعلام مستربچ و کامپاند',
            url: `${siteUrl}/en/contact`,
            item: {
              '@type': 'WebPage',
              '@id': `${siteUrl}/en/contact`,
              name: 'Contact Polychem | تماس با پلیکم',
              url: `${siteUrl}/en/contact`,
              inLanguage: ['en', 'fa', 'ar', 'tr'],
              isPartOf: { '@id': `${siteUrl}/#website` },
            },
          },
          {
            '@type': 'ListItem',
            position: 4,
            name: 'Color Masterbatch | مستربچ رنگی | ماسترباتش ملون | Renkli Masterbatch',
            description: 'Custom color masterbatch for PE, PP, PS, ABS | مستربچ رنگی سفارشی برای انواع پلاستیک',
            url: `${siteUrl}/en/products/color-masterbatch`,
            item: {
              '@type': 'WebPage',
              '@id': `${siteUrl}/en/products/color-masterbatch`,
              name: 'Color Masterbatch | مستربچ رنگی',
              url: `${siteUrl}/en/products/color-masterbatch`,
              isPartOf: { '@id': `${siteUrl}/#website` },
            },
          },
        ],
      }),
    },

    // ✅ LocalBusiness Schema
    {
      type: 'application/ld+json',
      key: 'local-business-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': ['LocalBusiness', 'Manufacturer'],
        '@id': `${siteUrl}/#localbusiness`,
        name: 'Polychem (Polychemmb) | پلی‌کم (پلیمرشیمی ارس)',
        telephone: '+98-921-22898980',
        email: 'info@polychemmb.com',
        description: 'Masterbatch and polymer compound manufacturer in Aras Free Zone, Iran | تولیدکننده مستربچ و کامپاند پلیمر در منطقه آزاد ارس، ایران.',
        address: {
          '@type': 'PostalAddress',
          streetAddress: 'Aras Free Trade-Industrial Zone',
          addressLocality: 'Jolfa',
          addressRegion: 'East Azerbaijan',
          postalCode: '5481',
          addressCountry: 'IR',
        },
        geo: {
          '@type': 'GeoCoordinates',
          latitude: 38.930278,
          longitude: 45.633889,
        },
        url: siteUrl,
        priceRange: '$$',
        openingHoursSpecification: {
          '@type': 'OpeningHoursSpecification',
          dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Sunday'],
          opens: '08:00',
          closes: '17:00',
        },
      }),
    },

    // ✅ FAQPage Schema — چهار زبانه
    {
      type: 'application/ld+json',
      key: 'faq-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: [
          // === English FAQ ===
          {
            '@type': 'Question',
            name: 'What is masterbatch?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'Masterbatch is a concentrated mixture of pigments or additives encapsulated in a carrier resin, used to color or improve properties of plastic products. Polychem (Polychemmb) manufactures color masterbatch, filler masterbatch, and additive masterbatch in Iran\'s Aras Free Zone.',
            },
          },
          {
            '@type': 'Question',
            name: 'What is a polymer compound?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'A polymer compound is a mixture of base polymer with fillers, reinforcements, or additives to achieve specific properties. Polychem produces PP compound, PP-Talc compound, and custom polymer blends for industrial use.',
            },
          },
          {
            '@type': 'Question',
            name: 'Who is Polychem (Polychemmb)?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'Polychem (Polychemmb) is Iran\'s leading masterbatch and polymer compound manufacturer, founded in 2015 and located in Aras Free Zone, Jolfa. ISO 9001:2015 certified, exporting to Middle East, Caucasus, and Central Asia.',
            },
          },
          {
            '@type': 'Question',
            name: 'Does Polychem export masterbatch?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'Yes, Polychem exports masterbatch and polymer compound to Turkey, Iraq, Armenia, Azerbaijan, and across the Middle East and Caucasus region.',
            },
          },
          // === فارسی FAQ ===
          {
            '@type': 'Question',
            name: 'پلیمرشیمی ارس یا پلی کم چه شرکتی است؟',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'پلی‌کم (Polychemmb) که با نام‌های پلیمرشیمی ارس، پلیکم و پلی کم نیز شناخته می‌شود، یکی از پیشروترین تولیدکنندگان مستربچ و کامپاند پلیمر در ایران است. این شرکت از سال ۱۳۹۴ در منطقه آزاد ارس، جلفا فعالیت می‌کند و دارای گواهینامه ISO 9001:2015 است.',
            },
          },
          {
            '@type': 'Question',
            name: 'مستربچ چیست؟',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'مستربچ یک مخلوط غلیظ از رنگدانه‌ها یا افزودنی‌هایی است که در یک رزین حامل محصور شده‌اند و برای رنگ‌دهی یا بهبود خواص محصولات پلاستیکی استفاده می‌شود. شرکت پلی‌کم (پلیمرشیمی ارس) انواع مستربچ رنگی، مستربچ پرکننده CaCO3 و مستربچ افزودنی را در منطقه آزاد ارس ایران تولید می‌کند.',
            },
          },
          {
            '@type': 'Question',
            name: 'کامپاند پلیمر چیست و پلی کم چه کامپاندهایی تولید می‌کند؟',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'کامپاند پلیمر ترکیبی از پلیمر پایه با پرکننده‌ها، تقویت‌کننده‌ها یا افزودنی‌ها برای دستیابی به خواص خاص است. پلی‌کم (پلیمرشیمی ارس) انواع کامپاند PP، کامپاند PP-Talc و مخلوط‌های پلیمری سفارشی برای استفاده صنعتی و خودرویی تولید می‌کند.',
            },
          },
          {
            '@type': 'Question',
            name: 'آیا پلی کم (پلیمرشیمی ارس) مستربچ صادر می‌کند؟',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'بله، پلی‌کم محصولات مستربچ و کامپاند پلیمری را به ترکیه، عراق، ارمنستان، آذربایجان و سراسر خاورمیانه و منطقه قفقاز صادر می‌کند.',
            },
          },
          {
            '@type': 'Question',
            name: 'مستربچ رنگی پلی کم برای چه پلاستیک‌هایی مناسب است؟',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'مستربچ رنگی تولید شده توسط پلی‌کم (پلیمرشیمی ارس) برای انواع پلاستیک‌ها از جمله PE (پلی‌اتیلن)، PP (پلی‌پروپیلن)، PS (پلی‌استایرن) و ABS مناسب است و در طیف وسیعی از رنگ‌ها و غلظت‌ها تولید می‌شود.',
            },
          },
          // === Arabic FAQ ===
          {
            '@type': 'Question',
            name: 'ما هو الماسترباتش؟',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'الماسترباتش هو خليط مركز من الأصباغ أو المضافات المحاطة براتنج حامل، ويُستخدم لتلوين المنتجات البلاستيكية أو تحسين خصائصها. تقوم شركة بولي كيم (Polychemmb) بتصنيع ماسترباتش الألوان وماسترباتش الحشو وماسترباتش الإضافات في منطقة آراس الحرة بإيران.',
            },
          },
          {
            '@type': 'Question',
            name: 'من هي شركة POLYCHEM؟',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'POLYCHEM (Polychemmb) هي الشركة الرائدة في إيران في تصنيع الماسترباتش ومركبات البوليمر، تأسست عام 2015 وتقع في منطقة آراس الحرة، جلفا. حاصلة على شهادة ISO 9001:2015 وتصدر منتجاتها إلى الشرق الأوسط والقوقاز وآسيا الوسطى.',
            },
          },
          {
            '@type': 'Question',
            name: 'ما هي منتجات POLYCHEM؟',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'تصنع POLYCHEM: ماسترباتش الألوان، ماسترباتش الحشو (CaCO3)، ماسترباتش الإضافات (مقاوم للأشعة فوق البنفسجية، مقاوم للحرائق، مضاد للكهرباء الساكنة)، مركب PP، مركب PP-Talc، ومخاليط البوليمر المخصصة.',
            },
          },
          // === Turkish FAQ ===
          {
            '@type': 'Question',
            name: 'Masterbatch nedir?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: "Masterbatch, plastik ürünleri renklendirmek veya özelliklerini iyileştirmek için kullanılan, bir taşıyıcı reçine içinde kapsüllenmiş pigment veya katkı maddelerinin yoğunlaştırılmış bir karışımıdır. Polychem (Polychemmb), İran'ın Aras Serbest Bölgesi'nde renkli masterbatch, dolgu masterbatch ve katkı masterbatch üretmektedir.",
            },
          },
          {
            '@type': 'Question',
            name: 'Polychem hangi ürünleri üretmektedir?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: "Polychem şu ürünleri üretmektedir: renkli masterbatch, dolgu masterbatch (CaCO3), katkı masterbatch (UV, alev geciktirici, antistatik), PP bileşik, PP-Talc bileşik ve özel polimer karışımları. Tüm ürünler İran Aras Serbest Bölgesi'nde üretilmektedir.",
            },
          },
        ],
      }),
    },
  ],
})
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');

html, body, #__nuxt {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background-color: #f1f2f2;
}

* { font-family: inherit; }

img {
  content-visibility: auto;
}

@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan thin.ttf') format('truetype');
  font-weight: 100;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan light.ttf') format('truetype');
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan medium.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan extrabold.ttf') format('truetype');
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan black.ttf') format('truetype');
  font-weight: 900;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('/Font/Qs_Iranyekan extrablack.ttf') format('truetype');
  font-weight: 950;
  font-style: normal;
  font-display: swap;
}
</style>