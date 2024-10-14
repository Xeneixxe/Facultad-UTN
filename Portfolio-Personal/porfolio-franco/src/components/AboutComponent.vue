<script setup>
import { ref } from 'vue'

const isExpanded = ref(false)
const skills = ref([
  'Vue',
  'JavaScript',
  'HTML',
  'CSS',
  'Node.js',
  'Git',
  'Responsive Design',
])

const toggleSkills = () => {
  isExpanded.value = !isExpanded.value
}
</script>

<template>
  <main class="card-container">
    <div class="card">
      <div class="banner">
        <img
          src="https://images.vexels.com/media/users/3/307065/raw/e1b6a51757cb0b0aeb624229089fa685-dise-o-de-patr-n-de-mandala-de-flores-negras-y-grises.jpg"
          alt="Banner"
          class="banner-image"
        />
        <img
          src="https://avatars.githubusercontent.com/u/134340520?s=400&u=bd13048675c957d288f854449f33ed009a39c23f&v=4"
          alt="Foto de perfil"
          class="profile-image"
        />
      </div>

      <div class="content">
        <h2>Franco Morales</h2>
        <p class="title">Desarrollador en proceso de Web Full Stack</p>

        <p class="description">
          Bienvenidos a mi Portafolio. Soy un apasionado desarrollador web
          especializado en crear experiencias digitales innovadoras y
          eficientes. Mi enfoque se centra en Vue.js, JavaScript y diseño
          responsivo.
        </p>

        <div class="social-links">
          <a href="https://github.com/Xeneixxe" aria-label="GitHub">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path
                d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"
              ></path>
            </svg>
          </a>
          <a
            href="https://www.linkedin.com/in/franco-morales-08495a295/"
            aria-label="LinkedIn"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path
                d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"
              ></path>
              <rect x="2" y="9" width="4" height="12"></rect>
              <circle cx="4" cy="4" r="2"></circle>
            </svg>
          </a>
          <a href="mailto:francomoralew36@gmail.com" aria-label="Email">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path
                d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"
              ></path>
              <polyline points="22,6 12,13 2,6"></polyline>
            </svg>
          </a>
        </div>

        <button @click="toggleSkills" class="toggle-button">
          {{ isExpanded ? 'Ver menos' : 'Ver habilidades' }}
          <span class="chevron" :class="{ up: isExpanded }"></span>
        </button>
      </div>

      <div v-if="isExpanded" class="skills">
        <h3>Habilidades</h3>
        <div class="skill-tags">
          <span v-for="skill in skills" :key="skill" class="skill-tag">
            {{ skill }}
          </span>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
.card-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 160px auto;
  background: linear-gradient(to bottom, #0a0a0a1f, #22232500);
  padding: 20px;
}

.card {
  width: 100%;
  max-width: 600px;
  background-image: url('https://images.vexels.com/media/users/3/307065/raw/e1b6a51757cb0b0aeb624229089fa685-dise-o-de-patr-n-de-mandala-de-flores-negras-y-grises.jpg');
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  border: 2px solid #333;
}

.banner {
  position: relative;
  height: 200px;
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-image {
  position: absolute;
  left: 50%;
  bottom: -50px;
  transform: translateX(-50%);
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 4px solid #9b1123;
}

.content {
  padding: 60px 20px 20px;
  text-align: center;
  color: #ffffff;
}

h2 {
  font-size: 2rem;
  margin-bottom: 10px;
}

.title {
  color: #ffffff;
  font-size: 1.2rem;
  margin-bottom: 15px;
}

.description {
  margin-bottom: 20px;
  line-height: 1.6;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 20px;
}

.social-links a {
  color: #ffffff;
  transition: color 0.3s ease;
}

.social-links a:hover {
  color: #9b1123;
}

.toggle-button {
  background-color: #9b1123;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  border-radius: 25px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  transition: background-color 0.3s ease;
}

.toggle-button:hover {
  background-color: #d63d57;
}

.chevron {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-right: 2px solid #ffffff;
  border-bottom: 2px solid #ffffff;
  transform: rotate(45deg);
  margin-left: 10px;
  transition: transform 0.3s ease;
}

.chevron.up {
  transform: rotate(-135deg);
}

.skills {
  padding: 20px;
  background-image: url('https://images.vexels.com/media/users/3/307065/raw/e1b6a51757cb0b0aeb624229089fa685-dise-o-de-patr-n-de-mandala-de-flores-negras-y-grises.jpg');
  transition:
    max-height 0.3s ease,
    opacity 0.3s ease;
}

.skills h3 {
  text-align: center;
  color: #ffffff;
  margin-bottom: 15px;
}

.skill-tags {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}

.skill-tag {
  background-color: #070b13;
  color: #ffffff;
  padding: 5px 10px;
  border-radius: 15px;
  font-size: 0.9rem;
}

@media (max-width: 600px) {
  .card {
    border-radius: 0;
  }

  .content {
    padding: 50px 15px 15px;
  }

  h2 {
    font-size: 1.5rem;
  }

  .title {
    font-size: 1rem;
  }
}
</style>
