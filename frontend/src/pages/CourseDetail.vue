<template>
  <div class="container">
    <!-- Error -->
    <div v-if="error">
      <h1>Server error</h1>
      <p>Something went wrong in our side</p>
    </div>

    <!-- Loading -->
    <div v-else-if="loading">
      <h1>Loading...</h1>
      <div class="progress"><div class="indeterminate"></div></div>
    </div>

    <!-- Content -->
    <div class="row" v-else>
      <div class="col s12 l8">
        <h1>{{ course.title }}</h1>
        <p>{{ course.description }}</p>
      </div>
      <div class="col s12 l4 course-image">
        <p><img class="responsive-img" :src="course.image_link" alt="Course image"></p>
      </div>

      <!-- Enroll button -->
      <div class="col s12">
        <p v-if="$auth.loggedIn()">
          <button
            v-if="!courseEnrolled"
            class="btn waves-effect waves-light"
            @click="enroll">
            Enroll<i class="material-icons right">arrow_forward</i>
          </button>
          <router-link
            v-else
            :to="'/classroom/course/'+courseId"
            class="btn waves-effect waves-light">
            Go to course<i class="material-icons right">arrow_forward</i>
          </router-link>
        </p>

        <p v-else>
          Login to enroll
          <button class="btn waves-effect waves-light" @click="$auth.login">
          Login<i class="material-icons right">arrow_forward</i>
          </button>
        </p>
      </div>

      <!-- Syllabus -->
      <div class="col s12">
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
    error: null,
    course: {},
    courseId: this.$route.params.id,
    courseEnrolled: true,
  } },
  methods: {
    async fetchData() {
      try {
        const res = await fetch(`${this.$backend}/courses/${this.courseId}`)
        const data = await res.json()
        this.course = data
        console.log(data)
        if (res.status != 200)
          this.error = res.status

        if (this.$auth.loggedIn()) {
          console.log('logged in')
          this.courseEnrolled = (await (await
            fetch(`${this.$backend}/courses/${this.courseId}/is-enrolled`, {
              headers: {Authorization: 'Bearer ' + this.$auth.getJwt()}
            })
          ).json()).is_enrolled
          this.loading = false
        }
        else {
          this.loading = false
        }
      }
      catch (err) {
        this.error = err
        this.loading = false
      }
    },
    enroll(e) {
      console.assert(this.$auth.loggedIn())
      e.target.disabled = true
      fetch(`${this.$backend}/courses/${this.courseId}/enroll`, {
        method: 'PUT',
        headers: {Authorization: 'Bearer ' + this.$auth.getJwt()},
      })
      .then(res => res.json())
      .then(data => {
        M.toast({html: 'Enrolled successfull!'})
        this.$router.push('/classroom')
      })
      .catch(err => {
        console.error(err)
        M.toast({html: 'Something went wrong!'})
        e.target.disabled = false
      })
    },
  },
  created() {
    this.fetchData()
  },
}
</script>

<style lang="scss">
.course-part-list {
  margin-top: 2rem;
}
.course-part {
  position: relative;
  padding-left: 2rem;
  padding-bottom: 2rem;
  border-left: 1px solid #aaa;

  &::before {
    $size: 1rem;
    content: "";
    position: absolute;
    width: $size;
    height: $size;
    left: $size / 2 * -1;
    display: block;
    border-radius: 50%;
    background: var(--bs-primary);
  }

  & > * {
    position: relative;
    top: -1rem;
  }

  &-header {
    margin-top: 0;
  }
}

.no-mt {
  margin-top: 0;
}
</style>
