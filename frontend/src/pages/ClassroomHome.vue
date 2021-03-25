<template>
  <div id="app" class="app-classroom">
    <header class="classroom-home-header">
      <div class="small-top-nav">
        <!-- Snippet taken from materializecss.com -->
        <div class="container">
          <div class="row">
            <div class="col s12" style="display: flex; align-items: center">
              <a
                href="javascript:void(0)"
                data-target="nav-mobile"
                class="sidenav-trigger fix-micon hide-on-large-only"
              ><i class="material-icons">menu</i></a>
              <h1>Home</h1>
            </div>
          </div>
        </div>
      </div>
      <div id="nav-mobile" class="sidenav sidenav-fixed z-depth-0 my-side-nav">
        <ClassroomSidenav />
      </div>
    </header>
    <main>
      <div class="container">
        <div class="row">
          <h2 class="col s-12 caps-header">Current enrollments</h2>
          <div class="col s12">
            <ClassroomCourseCard v-for="c in courses" :course="c" :key="c.id"></ClassroomCourseCard>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import ClassroomCourseCard from '../components/ClassroomCourseCard.vue'
import ClassroomSidenav from '../components/ClassroomSidenav.vue'

export default {
  components: {
    ClassroomCourseCard,
    ClassroomSidenav,
  },
  data() { return {
    loading: true,
    error: null,
    courses: [],
    mSidenav: null,
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
  mounted() {
    // initialize sidenav
    const elems = document.querySelectorAll('.app-classroom .sidenav')
    this.mSidenav = M.Sidenav.init(elems, {})[0]
    console.log(this.mSidenav)
  },
  beforeDestroy() {
    this.mSidenav.destroy()
  },
}
</script>

<style lang="scss">
@import "../assets/scss/materializevariables";
$color-gray: rgba(0, 0, 0, 0.14);

@media #{$large-and-up} {
  .classroom-home-header,
  .app-classroom main {
    padding-left: 16rem;
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

.my-side-nav {
  width: 16rem;
  box-shadow: none;
  border-right: 1px solid $color-gray;
}

.caps-header {
  font-size: 1rem;
  color: darken($secondary-color, 15%);
  text-transform: uppercase;
}
</style>
