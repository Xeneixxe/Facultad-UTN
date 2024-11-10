<script lang="js" setup>
defineProps({
  children: String,
})
</script>
<template>
  <h1>{{ children }}</h1>
</template>

<style lang="css" scoped>
h1 {
  font-size: 2rem;
  text-align: center;
  margin: 80px auto;
}
</style>
