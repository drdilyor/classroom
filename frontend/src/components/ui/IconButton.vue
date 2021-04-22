<template>
  <!-- Just a button with an Icon -->
  <button class="btn d-inline-flex justify-content-center align-content-between">
    <i class="material-icons me-1" v-if="licon">{{icon}}</i>
    <span><slot></slot></span>
    <i class="material-icons ms-2" v-if="ricon">{{ricon}}</i>
  </button>
</template>

<script>
export default {
  props: {
    licon: {type: String, required: false},
    ricon: {type: String, required: false},
  }
}
</script>
