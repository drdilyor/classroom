<template>
  <div class="bg-light">
    <div class="border-bottom d-flex">
      <i class="material-icons p-0" style="font-size: 64px">arrow_left</i>
      <div class="flex-grow-1" style="line-height: 100%">
        <h2 style="font-size: 1em">{{ course_part_title }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    course_part_title: {
      default: 'Lesson 1'
    },
    lesson: {
      default() { return {
        title: 'blah',
      } }
    }
  }
}
</script>
