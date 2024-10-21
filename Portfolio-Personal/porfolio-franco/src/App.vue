<script setup>
import IpComponent from './components/IpComponent.vue'
import NavComponent from './components/NavComponent.vue'
import DatosPersonales from './components/DatosPersonales.vue'
import EducacionComponent from './components/EducacionComponent.vue'
import ProyectosComponente from './components/ProyectosComponente.vue'
</script>

<template>
  <header>
    <!-- Barra de navegacion -->
    <NavComponent />
    <IpComponent />
    <!-- Datos personales -->
    <DatosPersonales />
  </header>
  <main>
    <section id="ip">
      <h2>Bienvenido</h2>
      <IpComponent />
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
  -
</template>

<style scoped></style>
