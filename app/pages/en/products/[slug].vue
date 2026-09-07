<script setup>
const route = useRoute()

onMounted(() => {
  if (!import.meta.client) return

  const slug = route.params.slug
  if (slug) {
    window.location.replace(`/en/products/${slug}`)
  } else {
    window.location.replace('/en/products')
  }
})
</script>

<template>
  <div />
</template>
