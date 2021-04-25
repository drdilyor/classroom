<template>
  <div class="container content">
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
    <div class="columns is-vcentered" v-else>
      <div class="column is-5">
        <h1>{{ course.title }}</h1>
        <p>{{ course.description }}</p>
      </div>
      <div class="column is-7">
        <p><img class="img-fluid" :src="course.image_link" alt="Course image"></p>
      </div>

      <!-- Enroll button -->
    </div>
    <div class="columns">
      <div class="column is-half is-offset-one-quarter">
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
    <div class="course-part-list">
      <div class="course-part" v-for="cpart in course.course_parts" :key="cpart.id">
        <h3 class="course-part-header">{{ cpart.title }}</h3>
        <p>{{ cpart.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import IconButton from '../components/ui/IconButton.vue'
import LinkButton from '@/components/ui/IconLinkButton.vue'

export default {
  components: {
    LinkButton,
    IconButton,
  },
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
        this.$toasted.show('Enrolled successfull!', {
          icon: {name: 'done'},
          duration: 3000,
          action: {
            text: 'GREAT',
            onClick: (e, toast) => toast.goAway(0),
          },
        })
        this.$router.push('/classroom')
      })
      .catch(err => {
        this.$toasted.show('Something went wrong!', {icon: {name: 'error'}})
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
