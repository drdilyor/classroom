<template>
  <div id="app" class="app-classroom">
    <header class="classroom-home-header">
      <div class="small-top-nav">
        <!-- Snippet taken from materializecss.com -->
        <div class="container">
          <div class="row">
            <div class="col s12" style="display: flex; align-items: center">
              <a
                href="#"
                data-target="nav-mobile"
                class="sidenav-trigger fix-micon"
              ><i class="material-icons">menu</i></a>
              <h1>Home</h1>
            </div>
          </div>
        </div>
      </div>
      <div id="nav-mobile" class="sidenav sidenav-fixed">
      </div>
    </header>
    <main>
      <div class="container">
        <div class="row">
          <div class="col">
            <div v-for="c in courses" :key="c.id">
              <h2>{{ c.title }}</h2>
              <p>{{ c.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  data() { return {
    loading: true,
    error: null,
    courses: [],
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
@import "../assets/scss/materializevariables";
$color-gray: rgba(0, 0, 0, 0.14);

@media #{$large-and-up} {
  .classroom-home-header,
  .app-classroom main {
    padding-left: 300px;
  }
}

.small-top-nav {
  padding: 20px /* margin-bottom of .row */ 1em 0;
  border-bottom: 1px solid $color-gray;

  & h1 {
    font-size: 1rem;
    margin: 0;
  }
}
</style>
