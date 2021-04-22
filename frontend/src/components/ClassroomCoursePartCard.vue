<template>
  <router-link tag="div" class="classroom-course-part-card border rounded shadow-sm" :to="nextLessonLink">
    <span class="caps-header mb-2">Lesson {{i}}</span>
    <h3>{{ part.title }}</h3>
    <p class="flex-grow-1">{{ part.description }}</p>
    <button class="btn btn-outline-secondary d-inline-flex">
      Continue <i class="material-icons ms-2">arrow_forward</i>
    </button>
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
