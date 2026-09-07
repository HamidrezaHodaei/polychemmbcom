<template>
  <div></div>
</template>

<script setup>
// ✅ SEO انگلیسی کامل
useSeoMeta({
  title: 'POLYCHEM | Masterbatch & Polymer Compound Manufacturer | Aras Free Zone Iran',
  ogTitle: 'POLYCHEM | Masterbatch & Polymer Compound Manufacturer | Aras Free Zone Iran',
  description: 'POLYCHEM (Polychemmb) — Iran\'s leading manufacturer of color masterbatch, filler masterbatch (CaCO3), additive masterbatch, PP compound and engineering polymer blends. Located in Aras Free Zone, exporting to Middle East & Caucasus.',
  ogDescription: 'Leading manufacturer and exporter of masterbatch and polymer compounds in Iran. ISO 9001:2015 certified. Aras Free Zone, Jolfa.',
  ogUrl: 'https://polychemmb.com/en',
  ogType: 'website',
  ogImage: 'https://polychemmb.com/logo.png',
  twitterCard: 'summary_large_image',
  twitterTitle: 'POLYCHEM | Masterbatch & Polymer Compound | Iran',
  twitterDescription: 'Iran\'s leading masterbatch manufacturer — color, filler, additive masterbatch & PP compound. Aras Free Zone.',
})

useHead({
  htmlAttrs: { lang: 'en', dir: 'ltr' },
  link: [
    { rel: 'canonical', href: 'https://polychemmb.com/en' },
    { rel: 'alternate', hreflang: 'en', href: 'https://polychemmb.com/en' },
    { rel: 'alternate', hreflang: 'fa', href: 'https://polychemmb.com/fa' },
    { rel: 'alternate', hreflang: 'ar', href: 'https://polychemmb.com/ar' },
    { rel: 'alternate', hreflang: 'tr', href: 'https://polychemmb.com/tr' },
    { rel: 'alternate', hreflang: 'x-default', href: 'https://polychemmb.com/en' },
  ],
  meta: [
    { name: 'robots', content: 'index, follow' },
    {
      name: 'keywords',
      content: 'masterbatch, color masterbatch, filler masterbatch, additive masterbatch, polymer compound, PP compound, PP-Talc compound, masterbatch manufacturer Iran, Polychem, Polychemmb, Aras Free Zone, CaCO3 masterbatch, UV masterbatch, flame retardant masterbatch, anti-static masterbatch, engineering polymer, plastic additives, masterbatch exporter Iran'
    },
    { name: 'author', content: 'Polychem Corporation (Polychemmb)' },
    { property: 'og:locale', content: 'en_US' },
    { property: 'og:locale:alternate', content: 'fa_IR' },
    { property: 'og:site_name', content: 'Polychem | Polychemmb' },
  ],
  script: [
    {
      type: 'application/ld+json',
      key: 'en-webpage-schema',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'WebPage',
        '@id': 'https://polychemmb.com/en/#webpage',
        url: 'https://polychemmb.com/en',
        name: 'POLYCHEM | Masterbatch & Polymer Compound Manufacturer | Aras Free Zone Iran',
        description: 'POLYCHEM (Polychemmb) is Iran\'s leading manufacturer of masterbatch and polymer compounds located in Aras Free Zone.',
        inLanguage: 'en',
        isPartOf: { '@id': 'https://polychemmb.com/#website' },
        about: { '@id': 'https://polychemmb.com/#organization' },
        breadcrumb: {
          '@type': 'BreadcrumbList',
          itemListElement: [
            {
              '@type': 'ListItem',
              position: 1,
              name: 'Home',
              item: 'https://polychemmb.com/en',
            },
          ],
        },
        keywords: 'masterbatch, color masterbatch, filler masterbatch, polymer compound, PP compound, masterbatch manufacturer Iran, Polychem, Polychemmb',
      }),
    },
  ],
})

// ✅ ریدایرکت به صفحه انگلیسی
onMounted(() => {
  navigateTo('/en')
})
</script>