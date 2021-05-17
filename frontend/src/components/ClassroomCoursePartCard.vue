<template>
  <router-link tag="div" class="classroom-course-part-card card" :to="nextLessonLink">
    <span class="heading is-size-6">Part {{i}}</span>
    <h3 class="title pt-2 is-4">{{ part.title }}</h3>
    <p class="is-flex-grow-1">{{ part.description }}</p>
    <b-button class="my-5 is-hidden-mobile" type="is-primary is-light" icon-right="arrow-right">
      Continue
    </b-button>
    <footer>
      <b-progress class="mb-0" :value="progress.percentage" size="is-small" type="is-success" />
      <span class="ml-4 is-flex-grow-1">{{ progress.percentage }}%</span>
      <span>{{ progress.all - progress.viewed }} left</span>
    </footer>
  </router-link>
</template>

<script>
export default {
  props: {
    part: {
      type: Object,
      required: true,
    },
    i: {
      type: Number,
      default: 0,
    }
  },
  computed: {
    nextLesson() {
      const lessons = this.part.lessons
      for (const lesson of lessons) {
        if (!lesson.is_viewed)
          return lesson.id
      }
      if (lessons.length)
        return lessons[0].id
      else
        return null
    },
    nextLessonLink() {
      const next = this.nextLesson
      //console.log({next})
      return next ? '/classroom/lesson/' + next : '#'
    },
    progress() {
      const lessons = this.part.lessons
      const all = lessons.length
      const viewed = lessons.filter(i => i.is_viewed).length
      const percentage = Math.round(all === 0 ? 100 : viewed / all * 100)
      return {all, viewed, percentage}
    },
  }
}
</script>

<style>
.classroom-course-part-card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  min-height: 20rem;
  padding: 2rem;
  margin-bottom: 2rem;
  cursor: pointer;
}
.classroom-course-part-card footer {
  align-self: stretch;
  display: flex;
  align-items: center;
}
</style>
