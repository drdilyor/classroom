<template>
  <div class="container">
    <h1 class="title">{{$t('courses')}}</h1>
    <p v-if="error" class="content">
      <strong>Error</strong>: something went wrong :(
    </p>
    <Loading v-else-if="loading" class="content" />
    <template v-else>
      <div class="block control has-icons-right">
        <input
          v-model="search" type="search"
          class="input" :placeholder="$t('search')">
        <b-icon icon="magnify" class="is-right"/>
      </div>
      <div class="notification is-primary is-light" v-if="search">
        <h3 class="title is-5">{{$t('results')}} ({{courses.length}})</h3>
        <p>{{ search }}<button class="delete ml-2" @click="search = ''" /></p>
      </div>
      <explore-card v-for="course in courses" :course="course" :key="course.id" />
    </template>
  </div>
</template>

<script>
import ExploreCard from '@/components/ExploreCard.vue'
String.prototype.lower = String.prototype.toLowerCase

export default {
  components: { ExploreCard },
  data() { return {
    allCourses: [],
    loading: true,
    error: false,
    search: this.$route.query.search || '',
  } },
  computed: {
    courses() {
      return this.allCourses.filter(c =>
        c.title.toLowerCase().includes(this.search.toLowerCase())
      )
    }
  },
  watch: {
    search() {
      this.$router.push({
        path: this.$route.path,
        query: this.search ? {search: this.search} : {}
      })
    }
  },
  strings: {
    en: {
      courses: 'Courses',
      search: 'Search',
      results: 'Results',

    },
  },
  created() {
    this.$api.get('/courses')
    .then(data => {
      this.allCourses = data
      this.loading = false
    })
    .catch(err => {
      this.error = err
      this.loading = false
    })
  },
}
</script>
