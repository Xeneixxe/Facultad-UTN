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
  text-align: center;
  font-size: 2rem;
  font-weight: 800;
  margin: 100px auto;
  color: aliceblue;
  text-shadow: 1px 2px 3px #222;
}
</style>
