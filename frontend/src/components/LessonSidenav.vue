<template>
  <div class="bg-light lesson-sidenav">
    <router-link
      tag="a"
      :to="'/classroom/course/' + course_id"
      class="border-bottom d-flex"
      style="cursor: pointer"
    >
      <i class="material-icons p-0 text-secondary" style="font-size: 64px">arrow_left</i>
      <div class="d-flex align-items-center flex-grow-1">
        <h2>{{ course_part_title }}</h2>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    course_part_title: {
      default: 'Lesson 1'
    },
    course_id: {
      type: Number,
      default: 1,
    },
    lesson: {
      default() { return {
        title: 'blah',
      } }
    },
  }
}
</script>

<style>
.lesson-sidenav h2 {
  font-size: 1em;
}
</style>
