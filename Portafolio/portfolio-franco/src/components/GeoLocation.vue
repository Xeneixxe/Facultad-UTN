<script setup lang="js">
import { onMounted, ref } from 'vue'

const locationData = ref([])

const getData = async () => {
  const response = await fetch('https://geolocation.microlink.io')
  const dataJson = await response.json()
  locationData.value = dataJson
}

onMounted(async () => {
  await getData()
})
</script>

<template>
  <div class="contenedor" v-for="(data, index) in locationData" :key="index">
    <h1>'Su ubicacion es: {{ data.city.name }}'</h1>
  </div>
</template>

<style lang="css" scoped>
h1 {
  color: var(--color-text);
}
</style>
