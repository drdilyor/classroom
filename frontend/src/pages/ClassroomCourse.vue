<template>
  <div id="app" class="app-classroom">
    <classroom-sidenav class="flex-shrink-0" :show="showSidenav" />
    <div class="app-classroom-content">
      <!-- Loading -->
      <div v-if="!course">
        <Loading/>
      </div>
      <template v-else>
        <header>
          <navbar-burger :is-opened="showSidenav" @click="showSidenav = !showSidenav" />
          <span class="spacer" />
          <div class="is-flex-grow-1">
            <h1 class="is-hidden-mobile subtitle is-4">{{ course.title }}</h1>
          </div>
          <b-button
            v-if="resumeLesson !== null"
            tag="router-link"
            type="is-primary"
            :to="'/classroom/lesson/'+resumeLesson.id"
            :title="resumeLesson.title">
            Resume
          </b-button>
        </header>
        <main class="overflow-auto classroom-course-main">
          <div class="container">
            <CoursePartCard
              v-for="(cp, index) in course.course_parts"
              :key="cp.id"
              :part="cp"
              :i="index+1"/>
          </div>
        </main>
      </template>
    </div>
  </div>
</template>

<script>
import NavbarBurger from 'buefy/src/components/navbar/NavbarBurger.vue'
import ClassroomSidenav from '../components/ClassroomSidenav.vue'
import CoursePartCard from '../components/ClassroomCoursePartCard.vue'

export default {
  components: {NavbarBurger, ClassroomSidenav, CoursePartCard},
  data() { return {
    showSidenav: false,
  } },
  computed: {
    resumeLesson() {
      for (const part of this.course.course_parts)
        for (const lesson of part.lessons)
          if (!lesson.is_viewed)
            return lesson
      return null
    },
    course() {
      const res = this.$store.getters.currentCourse 
      //console.log({res})
      return res
    },
  },
  methods: {
    async fetchData() {
      this.$api.get('/enrolled-courses/'+this.$route.params.id)
      .then(course => {
        this.$store.dispatch('setCourse', course)
        this.course = course
        this.loading = false
      })
    },
  },
  created() {
    //this.fetchData()
    this.$store.dispatch('setCourse', this.$route.params.id)
  },
}
</script>
