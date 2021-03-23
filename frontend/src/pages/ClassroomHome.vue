<template>
  <div id="app">
    <header>
    </header>
    <main>
      <div class="container">
        <h1>Home</h1>
        <div v-for="c in courses" :key="c.id">
          <h2>{{ c.title }}</h2>
          <p>{{ c.description }}</p>
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
