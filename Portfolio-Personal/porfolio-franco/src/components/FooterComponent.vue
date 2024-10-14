<script lang="js" setup>
// import { Github, Mail, Instagram, icons } from 'lucide-vue-next'

const redes = [
  { name: 'Instagram', link: 'https://www.instagram.com/franco.morales.12/' },
  { name: 'GitHub', link: 'https://github.com/Xeneixxe' },
  { name: 'Correo', link: 'francomorale36@gmail.com' },
]
</script>

<template>
  <footer>
    <div class="contenedor-redes">
      <ul>
        <li v-for="(red, index) in redes" :key="index">
          <a :href="red.link">{{ red.name }}</a>
        </li>
      </ul>
    </div>
  </footer>
</template>

<style lang="css" scoped>
footer {
  background: #000000d9;
  display: flex;
  width: 100%;
  height: 35px;
  bottom: 0;
  justify-content: space-between;
  align-items: center;
}

.contenedor-redes {
  display: flex;
  width: 100%;
}

ul {
  margin: 0;
  padding: 0;
  display: flex;
  gap: 8px;
}

li {
  list-style: none;
}

a {
  padding: 8px 16px;
  text-decoration: none;
  color: var(--color-texto-primario);
}
</style>
