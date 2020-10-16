<template>
  <section id="feed">
    <category>
      <slot />
    </category>
  </section>
</template>

<script>
  export default {
    name: 'CategoryArticles',

    components: {
      Category: () => import('@/components/Category'),
    },
  }
</script>
