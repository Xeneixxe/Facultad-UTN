<script setup>
import DataComponente from './components/DataComponente.vue'
import NavComponent from './components/NavComponent.vue'
import DatosPersonales from './components/DatosPersonales.vue'
import EducacionComponent from './components/EducacionComponent.vue'
import ProyectosComponente from './components/ProyectosComponente.vue'
import FooterComponente from './components/FooterComponente.vue'
</script>

<template>
  <div class="bg-effect-0"></div>
  <div class="bg-effect-1"></div>
  <div class="bg-effect-2"></div>
  <NavComponent />
  <span id="about"></span>
  <SectionTitle children="Acerca" />
  <DatosPersonales />
  <span id="ip"></span>
  <SectionTitle children="Welcome" />
  <h1>Bienvenido desde<DataComponente /></h1>
  <span id="Education"></span>
  <SectionTitle children="Educacion" />
  <h2>Educacion-Cursos</h2>
  <EducacionComponent />
  <span id="proyects"></span>
  <SectionTitle children="Proyectos" />
  <h2>Proyectos</h2>
  <ProyectosComponente />
  <section id="habilidades"><h2>Habilidades</h2></section>
  <section id="intereses"><h2>intereses</h2></section>
  <FooterComponente />
</template>

<style scoped></style>
