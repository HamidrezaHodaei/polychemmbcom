<script setup>
const route = useRoute()

onMounted(() => {
  if (!import.meta.client) return

  const slug = route.params.slug
  if (slug) {
    window.location.replace(`/tr/products/${slug}`)
  } else {
    window.location.replace('/tr/products')
  }
})
</script>

<template>
  <div />
</template>