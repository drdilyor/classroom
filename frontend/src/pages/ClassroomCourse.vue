<template>
  <div id="app" class="app-classroom">
    <classroom-sidenav class="flex-shrink-0" :show="showSidenav" />
    <div class="flex-grow-1 app-classroom-content p-relative">
      <header class="shadow classroom-course-header mb-4">
        <div class="container py-2 d-flex align-items-center">
          <i class="material-icons d-lg-none pe-1" @click="showSidenav = !showSidenav">menu</i>
          <span class="flex-grow-1 title m-0 ps-1">{{ course.title }}</span>
          <a class="btn btn-sm btn-primary" :href="resumeLink">Resume</a>
        </div>
      </header>
      <main class="overflow-auto classroom-course-main">
        <div class="container">
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
          <div v-else>
            <CoursePartCard
              v-for="(cp, index) in course.course_parts"
              :key="cp.id"
              :part="cp"
              :i="index+1"/>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import ClassroomSidenav from '../components/ClassroomSidenav.vue'
import CoursePartCard from '../components/ClassroomCoursePartCard.vue'

export default {
  components: {ClassroomSidenav, CoursePartCard},
  data() { return {
    loading: true,
    error: null,
    course: {},
    showSidenav: false,
  } },
  computed: {
    resumeLink() {
      return 'javascript:void(0)'
    }
  },
  methods: {
    async fetchData() {
      try {
        const res = await fetch(`${this.$backend}/enrolled-courses/${this.$route.params.id}`)
        const data = await res.json()
        this.course = data
        console.log(data)
        if (res.status != 200)
          this.error = `${res.status}: ${res.statusText}`
        else
          this.loading = false
      }
      catch (err) {
        console.log(err)
        this.error = err
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

$header-height: .5em * 2 + 1em * 1.5;



// #nav-mobile-2 {
//   width: auto !important;
// }
// 
// .course-top-nav-wrapper {
//   z-index: 10;
//   position: sticky;
//   right: 0;
//   top: 0;
//   left: 0;
//   height: calc(.5em * 2 + 1.6em * 1.5);
//   padding: .5em;
//   background: white;
//   transition: height .3s ease;
// }
// .course-top-nav {
//   height: 100%;
//   display: flex;
//   align-items: center;
// 
//   & .sidenav-trigger {
//     align-self: flex-start;
//   }
//   
//   & h1 {
//     font-size: 1.6em;
//     padding: 0;
//     margin: 0;
//   }
// }
// 
// .classroom-course-main {
//   padding-top: calc(.5em * 2 + 1.6em * 1.5);
// }
// 
// @media screen and (max-width: 992px) and (min-height: 640px) {
//   .classroom-course-main {
//     padding-top: 16em;
//   }
//   .course-top-nav-wrapper:not(.small) {
//     height: 16em;
//     box-shadow: 0 0 40px rgba(0, 0, 0, .25);
//     
//     & h1 {
//       font-size: 3.2em;
//       font-weight: 200;
//     }
//   }
// }
</style>
