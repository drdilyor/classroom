<template>
  <div class="container">
    <h1>Courses</h1>
    <div v-if="loading">
      <div class="progress"><div class="indeterminate"></div></div>
      <p>Loading...</p>
    </div>
    <p v-else-if="error">
      <strong>Error</strong>: something went wrong :(
    </p>
    <template v-else>
      <div class="explore-tile"
        v-for="course in courses"
        :key="course.id">
        <div class="explore-tile-image">
          <img :src="course.image_link">
        </div>
        <div class="explore-tile-body">
          <span class="explore-tile-title">{{ course.title }}</span>
          <p class="flex-grow-1">{{ course.description }}</p>
          <div class="explore-tile-action">
            <router-link :to="`/courses/${course.id}`">Details</router-link>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  data() { return {
    courses: [],
    loading: true,
    error: false,
  } },
  created() {
    fetch(this.$backend + '/courses')
    .then(res => res.json())
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
.explore-tile {
  height: 20rem;
  margin-bottom: 1rem;
  border-radius: 4px;
  box-shadow: 0 .25rem .5rem #00000044;

  &-image {
    height: 50%;
    img {
      height: 100%;
      width: 100%;
      object-fit: cover;
      border-top-left-radius: 4px;
      border-top-right-radius: 4px;
    }
  }
  
  &-body {
    display: flex;
    height: 50%;
    flex-direction: column;
    padding: .5rem;
  }
  &-title {
    font-size: 1.6rem;
  }
  &-action {
    padding: .5rem;
    border-top: 1px solid #00000044;
    a {
      text-decoration: none;
      color: var(--bs-blue);
    }
  }
}

@media screen and (min-width: 992px) {
  .explore-tile {
    display: flex;
    flex-direction: row;
    height: 14rem;
    &-image {
      height: 100%;
      width: 20rem
    }
    &-body {
      height: 100%;
      flex-grow: 1;
    }
  }
}

</style>
