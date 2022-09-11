<template>
  <div id="app">
    <Header />
    <Main />
    <Footer />
  </div>
</template>

<script setup>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import Main from "@/components/Main.vue";
import '@/public/index.css'
</script>
<style scoped>
#app {
  overflow: hidden;
  width: 90rem;
  min-width: 60rem;
  margin: 0 auto;
}
</style>
