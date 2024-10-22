<script setup>
const title = 'Franco Javier Morales'
const descripcion = 'Estudiante de Programacion'
const residencia = 'San Rafael, Mendoza Argentina'
const presentacion =
  'Bienvenido a mi portfolio personal, en este encontraran mi trabajos realiza en la U.T.N'
const redesSociales = [
  {
    id: 1,
    name: 'Linkedin',
    src: '/src/assets/logotipo-de-linkedin.png',
    url: 'https://www.linkedin.com/in/franco-morales-08495a295/',
  },
  {
    id: 2,
    name: 'GitHub',
    src: '/src/assets/personaje-github.png',
    url: 'https://github.com/Xeneixxe',
  },
  {
    id: 3,
    name: 'Instagram',
    src: '/src/assets/instagram.png',
    url: 'https://www.instagram.com/franco.morales.12/',
  },
  {
    id: 4,
    name: 'Curriculum',
    src: '/src/assets/curriculum.png',
    url: '/assets/FrancoJavierMorales.pdf',
  },
]
const telefono = +542604812458
</script>

<template>
  <section class="datos-personales">
    <div class="card">
      <h1>{{ title }}</h1>
      <h2>{{ descripcion }}</h2>
      <p>{{ presentacion }}</p>
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a href="red.url"
            ><img
              class="icon.redsocial"
              :src="red.src"
              width="35rem"
              :alt="red.name"
          /></a>
        </li>
      </ul>
      <h3>Mi telefono personal: {{ telefono }}</h3>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
  gap: 8px;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
  gap: 8px;
}

.card {
  background-color: rgb(71, 66, 80);
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
  gap: 12px;
}

.icon-redsocial {
  align-items: center;
  background-color: aliceblue;
  border-radius: 50%;
  padding: 5px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}

.icon-redsocial:hover {
  background-color: rgb(28, 41, 52);
  box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}
</style>
