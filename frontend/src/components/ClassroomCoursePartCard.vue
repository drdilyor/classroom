<template>
  <router-link tag="div" class="classroom-course-part-card card" :to="nextLessonLink">
    <span class="subtitle is-5 has-text-grey">Part {{i}}</span>
    <h3 class="title pt-2">{{ part.title }}</h3>
    <p class="is-flex-grow-1">{{ part.description }}</p>
    <b-button class="mt-4" type="is-primary is-light" icon-right="arrow-right">
      Continue
    </b-button>
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
    }
  }
}
</script>

<style>
.classroom-course-part-card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  min-height: 18rem;
  padding: 2rem;
  margin-bottom: 2rem;
  cursor: pointer;
}
</style>
