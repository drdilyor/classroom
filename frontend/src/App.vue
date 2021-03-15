<template>
  <div id="app">
    <Header></Header>
    <main>
      <RouterView></RouterView>
    </main>
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
  created() {
    // created hook is used because mounted is called after children are rendered
    this.$auth.init()
  },
  mounted() {
    M.AutoInit()
  }
}
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  justify-content: stretch;
}

html, body, #app {
  height: 100%;
}

main {
  flex: 1;
}
</style>
