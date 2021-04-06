<template>
  <RouterView></RouterView>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Header, Footer
  },
  beforeCreate() {
    // created hook is used because mounted is called after children are rendered
    this.$auth.init()
  },
}
</script>
