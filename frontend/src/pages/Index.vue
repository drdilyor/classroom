<template>
  <div id="app" class="app-index">
    <Header></Header>
    <main class="site-main">
      <RouterView></RouterView>
    </main>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'

export default {
  components: {Header, Footer},
  beforeCreate() {
    this.$auth.init()
  }
}
</script>

<style>

.app-index {
  display: flex;
  flex-direction: column;
  justify-content: stretch;
}

html {
  overflow: auto !important;
}

html, body, .app-index {
  /* I'm not sure why but using `%` instead of `vh`
     is showing double scrollbars on desktop */
  height: 100%;
}

.app-index main {
  flex: 1;
}
</style>

<style>
.site-main {
  padding: 0 1em;
}
</style>
