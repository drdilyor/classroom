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
      <div class="card horizontal"
        v-for="course in courses"
        :key="course.id">
        <div class="card-image">
          <img :src="course.image_link">
        </div>
        <div class="card-stacked">
          <div class="card-content">
            <span class="card-title">{{ course.title }}</span>
            <p>{{ course.description }}</p>
          </div>
          <div class="card-action">
            <a href="#">Details</a>
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

<style scoped>
.card {
  height: 14rem;
}
.card-image,
.card-image img {
  height: 100%;
}
</style>
