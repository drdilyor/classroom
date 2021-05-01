<template>
  <div id="app" class="app-classroom">
    <classroom-sidenav class="has-background-light" :show="showSidenav">
      <lesson-sidenav />
    </classroom-sidenav>
    <div class="flex-grow-1 app-classroom-content p-relative">
      <Loading v-if="!lesson" />
      <template v-else>
        <header class="classroom-lesson-header has-background-light">
          <navbar-burger :is-opened="showSidenav" @click="showSidenav = !showSidenav" />
          <span class="spacer" />
          <h1 class="is-flex-grow-1 subtitle is-4 has-text-centered">{{ lesson.title }}</h1>
        </header>
        <main class="overflow-auto">
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
            <div class="py-4 is-flex is-justify-content-end">
              <b-button
              tag="router-link"
                v-if="nextLesson !== null"
                type="is-primary is-outlined"
                :to="nextLesson"
                icon-right="arrow-right">
                Next
              </b-button>
              <b-button
                v-else
                type="is-success is-outlined"
                :to="'/classroom/course/'+$store.getters.currentCourse.id"
                icon-right="check"
                @click.native="partDone">
                Done
              </b-button>
            </div>
          </div>
        </main>
      </template>
    </div>
  </div>
</template>

<script>
import NavbarBurger from 'buefy/src/components/navbar/NavbarBurger.vue'
import ClassroomSidenav from '@/components/ClassroomSidenav.vue'
import LessonSidenav from '@/components/LessonSidenav.vue'

export default {
  components: {NavbarBurger, ClassroomSidenav, LessonSidenav},
  data() { return {
    showSidenav: false,
    markdownComponentKey: 0,
  } },
  computed: {
    lesson() {
      console.log('lesson!')
      return this.$store.getters.currentLesson
    },
    nextLesson() {
      const part = this.$store.getters.currentPart
      const lesson = this.lesson
      const lessonIndex = part.lessons.findIndex(L => L.id == lesson.id)
      if (lessonIndex === part.lessons.length - 1)
        // last lesson
        return null
      else
        return String(part.lessons[lessonIndex + 1].id)
    },
    nextPart() {
      return "2"
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
    },
    partDone() {
      this.$toasted.show('Congratulations! Keep moving on', {
        icon: {name: 'trending_up'},
        duration: 3000,
          action: {
            text: 'GREAT',
            onClick: (e, toast) => toast.goAway(0),
          },
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
.lesson-content {
  max-width: 640px !important;
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
