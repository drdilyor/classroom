<template>
  <div id="app" class="app-classroom">
    <classroom-sidenav class="has-background-light" :show="showSidenav">
      <lesson-sidenav />
    </classroom-sidenav>
    <div class="flex-grow-1 app-classroom-content" ref="content">
      <Loading v-if="!lesson" />
      <template v-else>
        <header class="classroom-lesson-header has-background-light">
          <navbar-burger :is-opened="showSidenav" @click="showSidenav = !showSidenav" />
          <span class="spacer" />
          <h1 class="is-flex-grow-1 subtitle is-4 has-text-centered">{{ lesson.title }}</h1>
        </header>
        <main>
          <div class="container lesson-content">
            <div class="video-wrapper">
              <iframe
                class="video"
                width="640"
                height="360"
                allowfullscreen
                :src="`https://www.youtube.com/embed/${lesson.video}`"/>
            </div>
            <vue-markdown class="content" :key="'md'+markdownComponentKey">
              {{ lesson.content }}
            </vue-markdown>
            <div class="py-4 is-flex-mobile is-flex is-justify-content-end">
              <b-button
              tag="router-link"
                v-if="nextLesson !== null"
                type="is-primary is-light"
                :to="nextLesson"
                icon-right="arrow-right">
                {{$t('btnNext')}}
              </b-button>
              <b-button
                v-else
                type="is-success is-light"
                :to="'/classroom/course/'+$store.getters.currentCourse.id"
                icon-right="check"
                @click.native="partDone">
                {{$t('btnDone')}}
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
      this.$buefy.snackbar.open({
        duration: 3000,
        message: this.$t('doneSnackbar'),
        position: 'is-top-right',
        actionText: this.$t('doneSnackbarAction'),
        queue: false,
        onAction: function() {
          this.close()
        }
      })
      this.$router.push('/classroom/course/'+this.$store.getters.currentCourse.id)
    }
  },
  strings: {
    en: {
      btnNext: 'Next',
      btnDone: 'Done',
      doneSnackbar: 'Congratulations! Keep moving on',
      doneSnackbarAction: 'GREAT',
    },
    uz: {
      btnNext: 'Keyingi',
      btnDone: 'Tamomlash',
      doneSnackbar: "Tabriklaymiz! Oldinga harafatdan to'xtamang",
      doneSnackbarAction: 'AJOYIB',
    },
  },
  created() {
    this.onCreated()
  },
  beforeRouteUpdate(to, from, next) {
    next()
    this.onCreated()
    this.$refs.content.scrollTo(NaN, 0)
  }
}
</script>

<style>
.lesson-content {
  max-width: 640px !important;
}
.lesson-content .video-wrapper {
  position: relative;
  max-width: 640px;
  margin: 0 auto; /* is this really needed? */
  padding-bottom: calc(9 / 16 * 100%);
  margin-bottom: 1em;
}
.lesson-content .video {
  position: absolute;
  left: 0; right: 0;
  width: 100%;
  height: 100%;
}
</style>
