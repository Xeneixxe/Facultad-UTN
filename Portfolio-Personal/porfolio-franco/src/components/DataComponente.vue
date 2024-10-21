<script lang="js" setup>
import { ref, onMounted } from 'vue'
import { GetLocation } from './IpComponent.vue'

const datalocation = ref([])

onMounted(async () => {
  datalocation.value = await GetLocation.city()
})
</script>

<template>
  <div>
    <p>{{ datalocation }}</p>
  </div>
</template>

<style></style>
