<template>
  <div class="card z-depth-1">
    <div class="body">
      <h3>{{ course.title }}</h3>
      <p class="grey-text text-darken-2">{{ course.description }}</p>
    </div>
    <icon-link-button
      :to="'/classroom/course/'+course.id"
      class="btn-outline-secondary border-0"
      ricon="arrow_forward">
      Program home</icon-link-button>
  </div>
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
}
</script>

<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 1em;
}

.body {
  padding-bottom: 1em;
}

h3 {
  margin: 0;
  font-size: 1.618em;
}
p {
  margin-top: .5em;
  margin-bottom: 0;
}
.course-link {
  color: var(--bs-secondary);
}

@media screen and (max-width: 992px) {
  .card {
    flex-direction: row;
    align-items: center;
  }
  .body {
    flex: 5;
    padding-bottom: 0;
  }
}
</style>
