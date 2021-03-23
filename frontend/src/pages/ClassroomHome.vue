<template>
  <div id="app" class="app-classroom">
    <header class="classroom-home-header">
      <div class="small-top-nav">
        <!-- Snippet taken from materializecss.com -->
        <div class="container">
          <div class="row">
            <div class="col s12" style="display: flex; align-items: center">
              <a
                href="#"
                data-target="nav-mobile"
<<<<<<< HEAD
                class="sidenav-trigger fix-micon hide-on-large-only"
=======
                class="sidenav-trigger fix-micon"
>>>>>>> 757546cc8b2f8207f8854fe64967851b184144f3
              ><i class="material-icons">menu</i></a>
              <h1>Home</h1>
            </div>
          </div>
        </div>
      </div>
<<<<<<< HEAD
      <div id="nav-mobile" class="sidenav sidenav-fixed z-depth-0 my-side-nav">
=======
      <div id="nav-mobile" class="sidenav sidenav-fixed">
>>>>>>> 757546cc8b2f8207f8854fe64967851b184144f3
      </div>
    </header>
    <main>
      <div class="container">
        <div class="row">
<<<<<<< HEAD
          <div class="col s12">
            <ClassroomCourseCard v-for="c in courses" :course="c" :key="c.id"></ClassroomCourseCard>
=======
          <div class="col">
            <div v-for="c in courses" :key="c.id">
              <h2>{{ c.title }}</h2>
              <p>{{ c.description }}</p>
            </div>
>>>>>>> 757546cc8b2f8207f8854fe64967851b184144f3
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import ClassroomCourseCard from './ClassroomCourseCard.vue'

export default {
  components: {
    ClassroomCourseCard,
  },
  data() { return {
    loading: true,
    error: null,
    courses: [],
  } },
  methods: {
    async fetchData() {
      try {
        const res = await fetch(`${this.$backend}/enrolled-courses`, {
          headers: {Authorization: 'Bearer '+this.$auth.getJwt()}
        })
        const data = await res.json()
        this.courses = data
        console.log(data)
        if (res.status != 200)
          this.error = res.status
      }
      catch (err) {
        this.error = err
      }
      finally {
        this.loading = false
      }
    },
  },
  created() {
    this.fetchData()
  },
}
</script>

<style lang="scss">
@import "../assets/scss/materializevariables";
$color-gray: rgba(0, 0, 0, 0.14);

@media #{$large-and-up} {
  .classroom-home-header,
  .app-classroom main {
<<<<<<< HEAD
    padding-left: 16rem;
=======
    padding-left: 300px;
>>>>>>> 757546cc8b2f8207f8854fe64967851b184144f3
  }
}

.small-top-nav {
  padding: 20px /* margin-bottom of .row */ 1em 0;
  border-bottom: 1px solid $color-gray;

  & h1 {
    font-size: 1rem;
    margin: 0;
  }
}
<<<<<<< HEAD

.my-side-nav {
  width: 16rem;
  box-shadow: none;
  border-right: 1px solid $color-gray;
}
=======
>>>>>>> 757546cc8b2f8207f8854fe64967851b184144f3
</style>
