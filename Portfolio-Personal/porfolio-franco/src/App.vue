<script setup>
import DataComponente from './components/DataComponente.vue'
import NavComponent from './components/NavComponent.vue'
import DatosPersonales from './components/DatosPersonales.vue'
import EducacionComponent from './components/EducacionComponent.vue'
import ProyectosComponente from './components/ProyectosComponente.vue'
import FooterComponente from './components/FooterComponente.vue'
</script>

<template>
  <header>
    <!-- Barra de navegacion -->
    <NavComponent />
    <!-- Datos personales -->
    <DatosPersonales />
  </header>
  <main>
    <section id="ip">
      <h2>Bienvenido desde<DataComponente /></h2>
    </section>
    <section id="educacion">
      <h2>Educacion-Cursos</h2>
      <EducacionComponent />
      <Educacion />
    </section>
    <section id="proyectos">
      <h2>Proyectos</h2>
      <ProyectosComponente />
    </section>
    <section id="habilidades"><h2>Habilidades</h2></section>
    <section id="intereses"><h2>intereses</h2></section>
  </main>
  <FooterComponente />
</template>

<style scoped></style>
