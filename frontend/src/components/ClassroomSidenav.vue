<template>
  <transition name="slide-left">
    <div class="sidenav" v-show="desktop || show">
      <div class="overlay"/>
      <slot>
        <classroom-sidenav-default/>
      </slot>
    </div>
  </transition>
</template>

<script>
import IconLink from '@/components/ui/IconLinkButton.vue'
import ClassroomSidenavDefault from './ClassroomSidenavDefault.vue'

export default {
  components: {IconLink, ClassroomSidenavDefault},
  props: {
    show: {
      type: Boolean,
      default: true,
    }
  },
  data() { return {
    desktop: false,
  } },
  methods: {
    logout() {
      this.$auth.logout()
      window.location = '/'
    },
    onResize() {
      this.desktop = window.innerWidth > 1024
    }
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize)
  }
}
</script>

<style lang="scss">

/* (1) Disable visibility *while* transiting */
.sidenav {
  z-index: 1040;
  display: flex;
  flex-direction: column;
  width: 18rem;
  border-right: 1px solid rgba(0, 0, 0, .125);

  overflow: auto;
  background: white;

  visibility: visible;
  transition: margin-left .3s, visibility 0s .3s; /* (1) */
}

.sidenav.slide-left-enter,
.sidenav.slide-left-leave-active {
  margin-left: -18rem;
}
</style>
