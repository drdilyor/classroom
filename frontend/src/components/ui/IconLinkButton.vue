<template>
  <!-- Router Link with an Icon -->
  <router-link :to="to" class="d-inline-flex align-content-between" :class="{btn}">
    <i class="material-icons me-1" v-if="licon">{{licon}}</i>
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
    },
    btn: {type: Boolean, default: true}
  }
}
</script>
