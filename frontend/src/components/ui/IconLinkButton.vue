<template>
  <!-- Router Link with an Icon -->
  <router-link :to="to" class="btn btn-secondary d-inline-flex justify-content-center align-content-between">
    <i class="material-icons me-1" v-if="licon">{{icon}}</i>
    <span><slot></slot></span>
    <i class="material-icons ms-2" v-if="ricon">{{ricon}}</i>
  </router-link>
</template>

<script>
export default {
  props: {
    licon: {type: String, required: false},
    ricon: {type: String, required: false},
    to: {
      type: String,
      required: true,
    }
  }
}
</script>
