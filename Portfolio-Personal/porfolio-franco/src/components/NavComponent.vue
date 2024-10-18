<script lang="js" setup></script>

<template>
  <nav class="navbar">
    <div class="navbar-menu">
      <ul>
        <a
          v-for="nav in navegacion"
          :key="nav.nombre"
          href="nav.enlace"
          class="nav.item"
          >{{ nav.nombre }}</a
        >
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const navegacion = ref([
  { id: 1, nombre: 'Educacion', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
])
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  background: linear-gradient(to top, #22222275, #050505d2);
  padding: 1rem;
  border-bottom: 1px solid #333;
  z-index: 99;
}
ul {
  display: flex;
  justify-content: space-around;
  list-style-type: none;
}
li {
  color: #ff8500; /* Color naranja estilo Bleach */
}
a {
  color: inherit;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.2rem;
}
</style>
