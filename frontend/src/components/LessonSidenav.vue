<template>
  <div class="bg-light lesson-sidenav">
    <router-link
      tag="a"
      :to="'/classroom/course/' + course_id"
      class="border-bottom lesson-sidenav-header"
      style="cursor: pointer"
    >
      <i class="material-icons p-0 text-secondary" style="font-size: 64px">arrow_left</i>
      <div class="d-flex align-items-center flex-grow-1">
        <h2>{{ course_part_title }}</h2>
      </div>
    </router-link>
    <ul v-if="part" class="lesson-list">
      <router-link
        v-for="lesson in part.lessons" :key="lesson.id"
        tag="li"
        :to="'/classroom/lesson/'+lesson.id"
        exact-active-class="active"
      >
        <i class="material-icons lesson-status" :class="{done: lesson.is_viewed}">
          {{ lesson.is_viewed ? 'done' : 'circle' }}
        </i>
        <span class="lesson">{{ lesson.title }}</span>
      </router-link>
    </ul>
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
  },
  computed: {
    part() {
      return this.$store.getters.currentPart
    },
  },
  destroyed() {
    console.error('hello');
  }
}
</script>

<style lang="scss">
.lesson-sidenav {
  display: flex;
  flex-direction: column;
  height: 100%;
  h2 {
    font-size: 1em;
  }
  a {
    text-decoration: none;
    color: inherit;
  }
  &-header {
    display: flex;
  }
}
.lesson-list {
  flex-grow: 1;
  list-style-type: none;
  padding: 0;
  margin-bottom: 0;
  li {
    display: flex;
    align-items: center;
    height: 5em;
    border-left: 4px solid transparent;
    cursor: pointer;
    &.active {
      border-left-color: var(--bs-primary)
    }
  }
  .lesson-status {
    width: 48px;
    font-size: 12px;
    text-align: center;
    color: var(--bs-gray);
    &.done {
      font-size: 24px;
      color: var(--bs-primary);
    }
  }
}

</style>
