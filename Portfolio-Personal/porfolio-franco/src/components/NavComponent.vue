<script lang="js" setup></script>

<template>
  <nav class="navbar">
    <ul>
      <li><a href="#acerca">Acerca de mi</a></li>
      <li><a href="#contacto">Formas de Contacto</a></li>
      <li><a href="#proyecto">Proyectos</a></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 80px;
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
