<template>
  <router-link tag="div" class="card p-4 pointer mb-4" :to="'/classroom/course/'+course.id">
    <div class="content columns is-align-items-center">
      <div class="column">
        <h4>{{ course.title }}</h4>
        <p>{{ course.description }}</p>
      </div>
      <div class="column is-narrow">
        <b-button type="is-primary is-light">
          {{$t('programHome')}}
        </b-button>
      </div>
    </div>
  </router-link>
</template>

<script>
import IconLinkButton from '@/components/ui/IconLinkButton.vue'

export default {
  components: {
    IconLinkButton,
  },
  props: {
    course: {
      type: Object,
      required: true,
    },
  },
  strings: {
    en: {
      programHome: 'Program home',
    },
    uz: {
      programHome: 'Dastur bosh sahifasi',
    },
  },
}
</script>

<style lang="scss" scoped>
</style>
