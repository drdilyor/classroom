<template>
  <div id="app" class="app-classroom">
    <classroom-sidenav class="flex-shrink-0" :show="showSidenav" />
    <div class="flex-grow-1 app-classroom-content">
      <header class="shadow py-2 mb-4 d-flex">
        <i class="material-icons ms-2 d-lg-none d-inline-block" @click="showSidenav = !showSidenav">
          menu
        </i>
        <span class="ps-2">
          Home
        </span>
      </header>
      <main class="overflow-auto container">
        <!-- no .container here and the class is added to main instead
        Because that causes overflow errors
        -->
          <div v-if="loading">
            <div class="progress"><div class="indeterminate"></div></div>
            <p>Loading...</p>
          </div>
          <p v-else-if="error">
            <strong>Error</strong>: something went wrong :(
          </p>
          <div v-else class="row">
            <h2 class="col-12 caps-header">Current enrollments</h2>
            <div class="col-12" :key="c.id" v-for="c in courses">
              <ClassroomCourseCard :course="c"></ClassroomCourseCard>
            </div>
          </div>
      </main>
    </div>
  </div>
</template>

<script>
import ClassroomCourseCard from '../components/ClassroomCourseCard.vue'
import ClassroomSidenav from '../components/ClassroomSidenav.vue'

export default {
  components: {
    ClassroomCourseCard,
    ClassroomSidenav,
  },
  data() { return {
    loading: true,
    error: null,
    courses: [],
    showSidenav: false,
  } },
  methods: {
    async fetchData() {
      try {
        const res = await fetch(`${this.$backend}/enrolled-courses`, {
          headers: {Authorization: 'Bearer '+this.$auth.getJwt()}
        })
        const data = await res.json()
        this.courses = data
        console.log(data)
        if (res.status != 200)
          this.error = res.status
      }
      catch (err) {
        this.error = err
      }
      finally {
        this.loading = false
      }
    },
  },
  created() {
    this.fetchData()
  },
}
</script>

<style lang="scss">

.app-classroom {
  display: flex;
  align-items: stretch;
  height: 100%;
  &-content {
    overflow: auto;
    @media screen and (max-width: 992.9px) {
      // flex-shrink: 0; // This breaks the page on mobile
    }
  }
}

.caps-header {
  font-size: 1rem;
  color: var(--bs-secondary);
  text-transform: uppercase;
}

</style>
