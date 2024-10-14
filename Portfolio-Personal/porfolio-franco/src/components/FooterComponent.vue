<script lang="js" setup>
const redes = [
  { name: 'Instagram', link: 'https://www.instagram.com/franco.morales.12/' },
  { name: 'GitHub', link: 'https://github.com/Xeneixxe' },
  { name: 'Correo', link: 'francomorale36@gmail.com' },
]
</script>

<template>
  <footer v-for="(red, index) in redes" :key="index">
    <div class="contenedor-redes">
      <ul>
        <li>
          <a :href="red.link">{{ red.name }}</a>
        </li>
      </ul>
    </div>
  </footer>
</template>
<style lang="css" scoped>
footer {
  background: linear-gradient(to bottom, #251919a2, #000000);
  display: flex;
  width: 100%;
  height: 35px;
  bottom: 0;
  
}
.contenedor-redes {
  display: flex;
  justify-content: space-between;
  gap: 8px;
}
a {
  color: aqua;
  display: inline-flex;
  text-decoration: none;
}
</style>
