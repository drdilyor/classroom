<template>
  <div id="app" class="app-classroom">
    <header>
      <div class="course-top-nav">
        <a
          href="javascript:void(0)"
          data-target="nav-mobile-2"
          class="sidenav-trigger fix-micon hide-on-large-only"
        ><i class="material-icons">menu</i></a>
      </div>
      <div id="nav-mobile-2" class="sidenav sidenav-fixed z-depth-0 my-side-nav">
        <ClassroomSidenav :small="true"/>
      </div>
    </header>

    <!-- Error -->
    <div v-if="error">
      <h1>Oops...</h1>
      <p>Something went wrong</p>
    </div>

    <!-- Loading -->
    <div v-else-if="loading">
      <h1>Loading...</h1>
      <div class="progress"><div class="indeterminate"></div></div>
    </div>
    <main>
      <p>Lorem ipsum dolor sit amet.</p>
    </main>
  </div>
</template>

<script>
import ClassroomCommon from '../components/ClassroomCommon.js'
import ClassroomSidenav from '../components/ClassroomSidenav.vue'

export default {
  components: {ClassroomSidenav},
  mixins: [ClassroomCommon],
  data() { return {
    loading: true,
    error: null,
    course: {},
    mSidenav: null, // required for common mixin
  } },
  methods: {
    async fetchData() {
      try {
        const res = await fetch(`${this.$backend}/courses/${this.$route.params.id}`)
        const data = await res.json()
        this.course = data
        console.log(data)
        if (res.status != 200)
          this.error = res.status
        else
          this.loading = false
      }
      catch (err) {
        console.log(err)
        this.error = err
        this.loading = false
      }
    }
  },
  created() {
    this.fetchData()
  }
}
</script>

<style>
#nav-mobile-2 {
  width: auto !important;
}
</style>
