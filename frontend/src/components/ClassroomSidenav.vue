<template>
  <div
    class="sidenav"
    :class="{show}" :style="{visibility: show}">
    <slot>
      <classroom-sidenav-default/>
    </slot>
  </div>
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
  methods: {
    logout() {
      this.$auth.logout()
      windOw.location = '/'
    }
  }
}
</script>

<style lang="scss">

/* (1) Disable visibility *while* transiting */
.sidenav {
  z-index: 1040;
  display: flex;
  flex-direction: column;
  width: 0;
  border-right: 1px solid rgba(0, 0, 0, .125);

  visibility: hidden;
  overflow: auto;
  background: white;
  transition: width .3s; /* (1) */

  @media screen and (max-width: 991.9px) {
    &.show {
      width: 18rem;
      visibility: visible;
      transition: width .3s, visibility 0s .3s; /* (1) */
    }
  }
  @media screen and (min-width: 992px) {
    width: 18rem;
    height: 100%;
    visibility: visible;
    transition: width .3s, visibility 0s .3s; /* (1) */
  }
  
}
</style>
