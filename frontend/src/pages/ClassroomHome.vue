<template>
  <div id="app" class="app-classroom">
    <classroom-sidenav :show="showSidenav" />
    <div class="app-classroom-content">
      <header>
        <navbar-burger :is-open="showSidenav" @click="showSidenav = !showSidenav"/>
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

// .app-classroom {
  // display: flex;
  // align-items: stretch;
  // height: 100%;
  // &-content {
  //   flex-grow: 1;
  //   overflow: auto;
  //   @media screen and (max-width: 1023.9px) {
  //     flex-shrink: 0; // This breaks the page on mobile
  //     max-width: calc(100% - 2px) !important;
  //   }
  //   > header {
  //     display: flex;
  //     align-items: center;
  //     min-height: 3.25rem;
  //     margin-bottom: 1.5rem;
  //     // (!) .box's shadow
  //     box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.1), 0 0px 0 1px rgba(10, 10, 10, 0.02);
  //     border-radius: 0;

  //     @media screen and (min-width: 1024px) {
  //       padding-left: 1.25rem;
  //     }
  //   }
  //   .navbar-burger {
  //     margin-left: 0;
  //   }
  // }
// }

.app-classroom main {
  padding: 0 1em;
}

.caps-header {
  font-size: 1rem;
  color: var(--bs-secondary);
  text-transform: uppercase;
}

</style>
