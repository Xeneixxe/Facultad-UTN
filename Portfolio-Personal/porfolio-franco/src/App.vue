<script setup>
import NavComponent from './components/NavComponent.vue'
import DatosPersonales from './components/DatosPersonales.vue'
import EducacionComponent from './components/EducacionComponent.vue'
</script>

<template>
  <header>
    <!-- Barra de navegacion -->
    <NavComponent />
    <!-- Datos personales -->
    <DatosPersonales />
  </header>
  <main>
    <EducacionComponent />
    <section id="educacion">
      <h2>Educacion-Cursos</h2>
      <Educacion />
    </section>
    <section id="experiencia"><h2>Experiencia</h2></section>
    <section id="proyectos"><h2>Proyectos</h2></section>
    <section id="habilidades"><h2>Habilidades</h2></section>
    <section id="intereses"><h2>intereses</h2></section>
  </main>
 
</template>

<style scoped></style>
