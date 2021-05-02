<template>
  <div class="bg-light lesson-sidenav" v-if="course">
    <router-link
      tag="a"
      :to="'/classroom/course/' + part.course_id"
      class="lesson-sidenav-header pointer"
    >
      <b-icon icon="arrow-left" />
      <h2>{{ title }}</h2>
    </router-link>

    <ul v-if="part" class="lesson-list p-2">
      <router-link
        v-for="(lesson, i) in part.lessons" :key="lesson.id"
        tag="li"
        :to="'/classroom/lesson/'+lesson.id"
        class="button is-light is-fullwidth is-justify-content-left pl-0 mb-2"
        exact-active-class="is-primary">
        <i class="mdi lesson-status" :class="lesson.is_viewed ? 'mdi-check done has-text-success' : 'mdi-circle'" />
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
    align-items: center;
    padding-left: .5em;
    border-bottom: 1px solid #888;
    > h2 {
      padding-left: .5em;
    }
  }
}
.lesson-list {
  flex-grow: 1;
  list-style-type: none;
  padding: 0;
  margin-bottom: 0;
  overflow: auto;
  // li {
    // display: flex;
    // align-items: center;
    // height: 3em;
    // border-left: 4px solid transparent;
    // color: rgba(0, 0, 0, .5);
    // cursor: pointer;
    // transition: color .2s;
    // &:hover {
      // color: rgba(0, 0, 0, .7);
    // }
    // &.active {
      // border-left-color: var(--bs-primary);
      // color: black;
    // }
  // }
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
    }
  }
}

</style>
