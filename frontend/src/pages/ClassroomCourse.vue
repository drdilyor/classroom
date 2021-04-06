<template>
  <div id="app" class="app-classroom">
    <header class="classroom-course-header">
      <div class="course-top-nav-wrapper z-depth-1">
        <div class="container course-top-nav">
          <a
            href="javascript:void(0)"
            data-target="nav-mobile-2"
            class="sidenav-trigger fix-micon hide-on-large-only"
          ><i class="material-icons">menu</i></a>
          <h1 style="flex: 1">{{ course.title }}</h1>
          <a class="btn-small waves-effect waves-light" :href="resumeLink">Resume</a>
        </div>
      </div>
      <div id="nav-mobile-2" class="sidenav sidenav-fixed z-depth-0 my-side-nav">
        <ClassroomSidenav :small="true"/>
      </div>
    </header>
    <main class="classroom-course-main">
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
</template>

<script>
import ClassroomCommon from '../components/ClassroomCommon.js'
import ClassroomSidenav from '../components/ClassroomSidenav.vue'
import CoursePartCard from '../components/ClassroomCoursePartCard.vue'

export default {
  components: {ClassroomSidenav, CoursePartCard},
  mixins: [ClassroomCommon],
  data() { return {
    loading: true,
    error: null,
    course: {},
    mSidenav: null, // required for common mixin
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
    collapseTopNav() {
      const el = document.querySelector(
        '.app-classroom .course-top-nav-wrapper'
      )
      if (window.scrollY > 160) el.classList.add('small')
      else el.classList.remove('small')
    }
  },
  created() {
    this.fetchData()
  },
  mounted() {
    window.addEventListener('scroll', this.collapseTopNav, {passive: true})
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.collapseTopNav)
  }
}
</script>

<style lang="scss">
@import "../assets/scss/materializevariables";
#nav-mobile-2 {
  width: auto !important;
}

.course-top-nav-wrapper {
  z-index: 10;
  position: fixed;
  right: 0;
  top: 0;
  left: 0;
  height: calc(.5em * 2 + 1.6em * 1.5);
  padding: .5em;
  background: white;
  transition: height .3s ease;
}
.course-top-nav {
  height: 100%;
  display: flex;
  align-items: center;

  & .sidenav-trigger {
    align-self: flex-start;
  }
  
  & h1 {
    font-size: 1.6em;
    padding: 0;
    margin: 0;
  }
}

.classroom-course-main {
  padding-top: calc(.5em * 2 + 1.6em * 1.5);
}

@media #{$large-and-up} {
  .course-top-nav-wrapper {
    left: 48px;
  }
  .classroom-course-main {
    padding-left: 48px;
  }
}

@media #{$medium-and-up} and (min-height: 640px) {
  .classroom-course-main {
    padding-top: 16em;
  }
  .course-top-nav-wrapper:not(.small) {
    height: 16em;
    box-shadow: 0 0 40px rgba(0, 0, 0, .25);
    
    & h1 {
      font-size: 3.2em;
      font-weight: 200;
    }
  }
}
</style>
