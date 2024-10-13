<script setup>
import NavComponent from './components/NavComponent.vue'
import FooterComponent from './components/FooterComponent.vue'
</script>

<template>
  <div class="background"></div>
  <NavComponent />
  <FooterComponent />
</template>

<style scoped>
.background {
  width: 100%;
  height: 100dvh;
  background-image: url('./assets/FondoPortfolio.webp');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
}
</style>
