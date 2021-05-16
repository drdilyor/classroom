<template>
  <div class="container content">
    <!-- Error -->
    <div v-if="error">
      <h1>Server error</h1>
      <p>Something went wrong in our side</p>
    </div>

    <!-- Loading -->
    <Loading v-else-if="loading" />

    <!-- Content -->
    <template v-else>
      <div class="columns is-vcentered">
        <div class="column">
          <h1>{{ course.title }}</h1>
          <p>{{ course.description }}</p>
        </div>
        <div class="column is-narrow">
          <img style="width: 100%" class="img-fluid" :src="course.image_link" alt="Course image">
        </div>
      </div>
      <div class="columns">
        <div class="column is-half is-offset-one-quarter">
          <!-- Enroll button -->
          <p v-if="$auth.loggedIn()">
            <b-button
              v-if="!courseEnrolled"
              type="is-primary is-fullwidth"
              @click="enroll">
              Enroll
            </b-button>
            <b-button
              v-else
              tag="router-link"
              type="is-primary is-light is-fullwidth"
              :to="'/classroom/course/'+courseId">
              Go to course  
            </b-button>
          </p>
          <template v-else>
            <p class="has-text-centered">
              Login to enroll
            </p>
            <b-button type="is-primary is-fullwidth" @click="$auth.login">
              Login
            </b-button>
          </template>
        </div>
      </div>

        <!-- Syllabus -->
      <h2 class="no-mt">Syllabus</h2>
      <p>To optimize your chances of success we have divided the course into following parts</p>
      <div class="course-part-list mb-4">
        <div class="course-part" v-for="cpart in course.course_parts" :key="cpart.id">
          <h3 class="course-part-header">{{ cpart.title }}</h3>
          <p>{{ cpart.description }}</p>
        </div>
      </div>
      <div class="columns has-text-centered">
        <div class="column"><h3>Language:</h3><p>The courses language is {{ course.language }}</p></div>
        <div class="column"><h3>Taught by:</h3><p>The course is taught by {{ course.author }}</p></div>
        <div class="column"><h3>Time:</h3><p>On average, it takes {{ course.estimated_time }} weeks</p></div>
      </div>
    </template>
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
        this.course = await this.$api.get(`/courses/${this.courseId}`)
        if (this.$auth.loggedIn()) {
          this.courseEnrolled = (await this.$api.get(
            `/courses/${this.courseId}/is-enrolled`
          )).is_enrolled
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
      console.log('enroll');
      console.assert(this.$auth.loggedIn())
      e.target.disabled = true
      this.$api.request('PUT', `/courses/${this.courseId}/enroll`)
      .then(data => {
        if (data.created)
        this.$buefy.snackbar.open({
          duration: 3000,
          message: 'Enrolled successfully!',
          position: 'is-top-right',
          actionText: 'GREAT',
          queue: false,
          onAction: function() {
            this.close()
          }
        })
        this.$router.push('/classroom')
      })
      .catch(err => {
        this.$buefy.snackbar.open({
          message: 'Something went wrong!',
          type: 'is-danger',
        })
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
    background: #7957d5;
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
