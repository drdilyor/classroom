<template>
  <div class="container">
    <h1 class="title">Courses</h1>
    <p v-if="error" class="content">
      <strong>Error</strong>: something went wrong :(
    </p>
    <Loading v-else-if="loading" class="content" />
    <template v-else>
      <explore-card v-for="course in courses" :course="course" :key="course.id" class="media"/>
    </template>
  </div>
</template>

<script>
import ExploreCard from '@/components/ExploreCard.vue'
export default {
  components: { ExploreCard },
  data() { return {
    courses: [],
    loading: true,
    error: false,
  } },
  created() {
    this.$api.get('/courses')
    .then(data => {
      this.courses = data
      this.loading = false
    })
    .catch(err => {
      this.error = err
      this.loading = false
    })
  },
}
</script>

<style lang="scss">
// .explore-tile {
//   height: 20rem;
//   margin-bottom: 1rem;
//   border-radius: 4px;
//   box-shadow: 0 .25rem .5rem #00000044;

//   &-image {
//     height: 50%;
//     img {
//       height: 100%;
//       width: 100%;
//       object-fit: cover;
//       border-top-left-radius: 4px;
//       border-top-right-radius: 4px;
//     }
//   }
  
//   &-body {
//     display: flex;
//     height: 50%;
//     flex-direction: column;
//     padding: .5rem;
//   }
//   &-title {
//     font-size: 1.6rem;
//   }
//   &-action {
//     padding: .5rem;
//     border-top: 1px solid #00000044;
//     a {
//       text-decoration: none;
//       color: var(--bs-blue);
//     }
//   }
// }

// @media screen and (min-width: 992px) {
//   .explore-tile {
//     display: flex;
//     flex-direction: row;
//     height: 14rem;
//     &-image {
//       height: 100%;
//       width: 20rem
//     }
//     &-body {
//       height: 100%;
//       flex-grow: 1;
//     }
//   }
// }

</style>
