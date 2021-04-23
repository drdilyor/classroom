<template>
  <div class="bg-light lesson-sidenav" v-if="course">
    <router-link
      tag="a"
      :to="'/classroom/course/' + part.course_id"
      class="border-bottom lesson-sidenav-header"
      style="cursor: pointer"
    >
      <i class="material-icons p-0 text-secondary" style="font-size: 64px">arrow_left</i>
      <div class="d-flex align-items-center flex-grow-1">
        <h2>{{ title }}</h2>
      </div>
    </router-link>
    <ul v-if="part" class="lesson-list">
      <router-link
        v-for="(lesson, i) in part.lessons" :key="lesson.id"
        tag="li"
        :to="'/classroom/lesson/'+lesson.id"
        exact-active-class="active"
      >
        <i class="material-icons lesson-status" :class="{done: lesson.is_viewed}">
          {{ lesson.is_viewed ? 'done' : 'circle' }}
        </i>
        <span class="lesson">
          {{ i+1 }}. {{ lesson.title }}
        </span>
      </router-link>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
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
    title() {
      return this.part.title
    },
    course() {
      return this.$store.getters.currentCourse
    }
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
    margin: 0;
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
  overflow: auto;
  li {
    display: flex;
    align-items: center;
    height: 3em;
    border-left: 4px solid transparent;
    color: rgba(0, 0, 0, .5);
    cursor: pointer;
    transition: color .2s;
    &:hover {
      color: rgba(0, 0, 0, .7);
    }
    &.active {
      border-left-color: var(--bs-primary);
      color: black;
    }
  }
  .lesson {
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }

  .lesson-status {
    flex-shrink: 0;
    width: 48px;
    font-size: 12px;
    text-align: center;
    color: var(--bs-gray);
    &.done {
      font-size: 24px;
      color: var(--bs-success);
    }
  }
}

</style>
