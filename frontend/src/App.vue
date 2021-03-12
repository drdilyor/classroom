<template>
  <div id="app">
    <Header></Header>
    <div class="container">
      <RouterView></RouterView>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import M from 'materialize-css'

export default {
  name: 'App',
  components: {
    Header, Footer
  },
  mounted() {
    M.AutoInit()
  }
}
</script>

<style>
</style>
