<template>
  <div id="Food">
    <articles>
    </articles>
  </div>
</template>

<script>
  export default {
    name: 'Food',
    components: {
      Articles: () => import('@/components/category/Articles'),
    },
  }
</script>
