<template>
  <div id="app" class="app-classroom">
    <classroom-sidenav class="flex-shrink-0 bg-light" :show="showSidenav">
      <lesson-sidenav/>
    </classroom-sidenav>
    <div class="flex-grow-1 app-classroom-content p-relative">
      <Loading v-if="!lesson"/>
      <template v-else>
        <header class="shadow classroom-lesson-header mb-4">
          <div class="container py-2 d-flex align-items-center">
            <i class="material-icons d-lg-none pe-1" @click="showSidenav = !showSidenav">menu</i>
            <strong>{{ lesson.title }}</strong>
          </div>
        </header>
        <main class="overflow-auto classroom-course-main">
          <div class="container lesson-content">
            <div class="video-wrapper">
              <iframe
                class="video"
                width="640"
                height="360"
                allowfullscreen="1"
                :src="`https://www.youtube.com/embed/${lesson.video}`"/>
            </div>
            <vue-markdown class="content" :key="'md'+markdownComponentKey">
              {{ lesson.content }}
            </vue-markdown>
          </div>
        </main>
      </template>
    </div>
  </div>
</template>

<script>
import ClassroomSidenav from '@/components/ClassroomSidenav.vue'
import LessonSidenav from '@/components/LessonSidenav.vue'
export default {
  components: {ClassroomSidenav, LessonSidenav},
  data() { return {
    showSidenav: false,
    markdownComponentKey: 0,
  } },
  computed: {
    lesson() {
      console.log('lesson!')
      return this.$store.getters.currentLesson
    }
  },
  methods: {
    onCreated() {
      const id = +this.$route.params.id
      this.$store.dispatch('setLesson', id)
      .then(() => {
        this.markdownComponentKey += 1
        if (this.lesson && !this.lesson.is_viewed)
          this.$store.dispatch('lessonViewed', id)
      })
    }
  },
  created() {
    this.onCreated()
  },
  beforeRouteUpdate(to, from, next) {
    next()
    this.onCreated()
  }
}
</script>

<style>
.classroom-lesson-header .container,
.lesson-content {
  max-width: 640px;
}
.lesson-content .video-wrapper {
  position: relative;
  height: 360px;
  max-width: 640px;
  margin: 0 auto; /* is this really needed? */
}
.lesson-content .video {
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>
