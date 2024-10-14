<script setup>
import NavComponent from './components/NavComponent.vue'
import FooterComponent from './components/FooterComponent.vue'
import SectionTitle from './components/SectionTitle.vue'
import AboutComponent from './components/AboutComponent.vue'
</script>

<template>
  <NavComponent />
  <AboutComponent />
  <SectionTitle children="Acerca de mi" />
  <SectionTitle children="Contacto" />
  <SectionTitle children="Redes" />
  <FooterComponent />
</template>

<style scoped></style>
