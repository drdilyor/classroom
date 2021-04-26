<template>
  <div id="app" class="app-classroom">
    <classroom-sidenav :show="showSidenav" />
    <div class="app-classroom-content">
      <header>
        <navbar-burger :is-open="showSidenav" @click="showSidenav = !showSidenav"/>
        <span style="height: 3.25rem" class="ml-4 is-hidden-touch"></span>
        Home
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
import NavbarBurger from 'buefy/src/components/navbar/NavbarBurger.vue'
import ClassroomCourseCard from '../components/ClassroomCourseCard.vue'
import ClassroomSidenav from '../components/ClassroomSidenav.vue'

export default {
  components: {
    NavbarBurger,
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
      this.courses = await this.$api.get('/enrolled-courses')
      this.loading = false
    },
  },
  created() {
    this.fetchData()
  },
}
</script>

<style lang="scss">

// general
.app-classroom {
  height: 100%;
}
.app-classroom > .sidenav {
  flex-shrink: 0;
}
.app-classroom-content {
  > header {
    display: flex;
    align-items: center;
  }
  .navbar-burger {
    margin-left: 0;
  }
}

// mobile
@media screen and (max-width: 1023.9px) {
  .app-classroom {
    display: flex;
    align-items: stretch;
    height: 100%;

    &-content {
      flex: 1 0;
      min-width: 100%;
      width: 100%;
    }
  }
}

// desktop 
@media screen and (min-width: 1024px) {
  .app-classroom {
    display: flex;
    align-items: stretch;
  }
}

.app-classroom main {
  padding: 0 1em;
}

.caps-header {
  font-size: 1rem;
  color: #778;
  text-transform: uppercase;
}

</style>
