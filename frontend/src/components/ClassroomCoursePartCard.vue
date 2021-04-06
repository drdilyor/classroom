<template>
  <div class="card z-depth-1">
    <span class="caps-header">Lesson {{i}}</span>
    <h3>{{ part.title }}</h3>
    <p>{{ part.description }}</p>
    <div>
      <a href="javascript:void(0)" class="btn-small waves-effect waves-light">
        Continue<i class="material-icons right">arrow_forward</i>
      </a>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  props: {
    part: {
      type: Object,
      required: true,
    },
    i: {
      type: Number,
      default: 0,
    }
  }
}
</script>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  min-height: 24em;
  padding: 2em;
}
.card p {
  flex: 1;
}

h3 {
  margin: 0;
  font-size: 1.3em;
}
</style>
