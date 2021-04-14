<template>
  <div class="
    position-relative
    d-flex
    flex-column
    flex-lg-row
    align-items-start
    align-items-lg-center
    justify-content-lg-between
    shadow-sm p-2 mb-2
    border rounded">
    <div class="course-card-body">
      <h3>{{ course.title }}</h3>
      <p class="grey-text text-darken-2">{{ course.description }}</p>
    </div>
    <icon-link-button
      :to="'/classroom/course/'+course.id"
      class="btn-outline-secondary border-0"
      ricon="arrow_forward">
      Program home</icon-link-button>
  </div>
</template>

<script>
import IconLinkButton from '@/components/ui/IconLinkButton.vue'

export default {
  components: {
    IconLinkButton,
  },
  props: {
    course: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style lang="scss" scoped>
// .course-card {
//   display: flex;
//   flex-direction: column;
//   align-items: flex-start;
//   padding: 1em;
//   min-height: 8rem;
// 
//   &-body {
//     padding-bottom: 1em;
//   }
// }
// 
// .course-card h3 {
//   margin: 0;
//   font-size: 1.618em;
// }
// 
// .course-link {
//   color: var(--bs-secondary);
// }
// 
// @media screen and (max-width: 992px) {
//   .course-card {
//     flex-direction: row;
//     align-items: center;
//     &-body {
//       flex: 5;
//       padding-bottom: 0;
//     }
//   }
// }
</style>
