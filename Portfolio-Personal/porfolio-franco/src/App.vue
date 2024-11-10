<script setup>
import DataComponente from './components/DataComponente.vue'
import NavComponent from './components/NavComponent.vue'
import DatosPersonales from './components/DatosPersonales.vue'
import EducacionComponent from './components/EducacionComponent.vue'
import ProyectosComponente from './components/ProyectosComponente.vue'
import FooterComponente from './components/FooterComponente.vue'
import SectionTitle from './components/SectionTitle.vue'
import HabilidadesComponente from './components/HabilidadesComponente.vue'
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
  <div class="wrap">
    <h1>Bienvenido desde<DataComponente /></h1>
  </div>
  <span id="Education"></span>
  <SectionTitle children="Educación" />
  <EducacionComponent />
  <span id="proyects"></span>
  <SectionTitle children="Proyectos" />

  <ProyectosComponente />

  <span id="hablidades"></span>
  <SectionTitle children="Habilidades" />
  <HabilidadesComponente />
  <section id="intereses"><h2>Intereses</h2></section>
  <FooterComponente />
</template>

<style scoped>
.wrap {
  text-align: center;
}
</style>
