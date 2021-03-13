<template>
  <div class="container" v-if="loading">
    <h1>Loading...</h1>
    <div class="progress"><div class="indeterminate"></div></div>
  </div>
  <div class="container" v-else>
    <div class="row">
      <div class="col s12 l8">
        <h1>{{ course.title }}</h1>
        <p>{{ course.description }}</p>
      </div>
      <div class="col s12 l4 course-image">
        <p><img class="responsive-img" :src="course.image_link" alt="Course image"></p>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <h2 class="no-mt">Syllabus</h2>
        <p>To optimize your chances of success we have divided the course into following parts</p>
        <div class="course-part-list">
          <div class="course-part" v-for="cpart in course.course_parts" :key="cpart.id">
            <h3 class="course-part-header">{{ cpart.title }}</h3>
            <p>{{ cpart.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() { return {
    loading: true,
    course: {}
  } },
  created() {
    fetch(`${this.$backend}/courses/${this.$route.params.id}`)
    .then(res => res.json())
    .then(data => {
      this.course = data
      console.log(data);
      this.loading = false
    })
    .catch(err => {
      this.error = err
      this.loading = false
    })
  }
}
</script>

<style>
.course-part-list {
  margin-top: 2rem;
}
.course-part {
  position: relative;
  padding-left: 2rem;
  padding-bottom: 2rem;
  border-left: 1px solid #777;
}
.course-part > * {
  position: relative;
  top: -1rem;
}
.course-part-header {
  margin-top: 0;
}
.course-part::before {
  content: "";
  position: absolute;
  width: .5rem;
  height: .5rem;
  left: -.25rem;
  display: block;
  border-radius: 50%;
  background: black;
}
.no-mt {
  margin-top: 0;
}
</style>
