<template>
  <div class="card z-depth-1">
    <div class="body">
      <h3>{{ course.title }}</h3>
      <p class="grey-text text-darken-2">{{ course.description }}</p>
    </div>
    <router-link
      :to="'/classroom/course/'+course.id"
      class="btn-flat waves-effect course-link">
      Program home<i class="material-icons right">arrow_forward</i>
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    course: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style lang="scss" scoped>
@import '../assets/scss/materializevariables.scss';
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
  color: darken($secondary-color, 15%);
}

@media #{$large-and-up} {
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
