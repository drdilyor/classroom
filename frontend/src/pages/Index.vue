<template>
  <div id="app" class="app-index">
    <Header :class="isHome ? 'is-primary' : ''"></Header>
    <main :class="{'site-main': !isHome}">
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
  data() { return {
    isHome: false,
  } },
  watch: {
    $route() {
      this.setIsHome()
    },
  },
  methods: {
    setIsHome() {
      let url = this.$router.history.current.path
      console.log({url})
      this.isHome = ['/', ''].includes(url)
    }
  },
  beforeCreate() {
    this.$auth.init()
  },
  created() {
    this.setIsHome()
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
