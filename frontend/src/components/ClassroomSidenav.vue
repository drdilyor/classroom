<template>
  <div
    class="sidenav"
    :class="{show}" :style="{visibility: show}">
    <slot>
      
    </slot>
  </div>
</template>

<script>
export default {
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

<style>

/* (1) Disable visibility *while* transiting */
.sidenav {
  z-index: 1040;
  width: 0;
  border-right: 1px solid rgba(0, 0, 0, .125  );
  visibility: hidden;
  background: white;
  transition: width .3s; /* (1) */
}

@media screen and (max-width: 991.9px) {
  /* .sidenav {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 0;
  } */
  .sidenav.show {
    width: 18rem;
    visibility: visible;
    transition: width .3s, visibility 0s .3s; /* (1) */
  }
}

@media screen and (min-width: 992px) {
  .sidenav {
    width: 18rem;
    height: 100%;
    visibility: visible;
    transition: width .3s, visibility 0s .3s; /* (1) */
  }
}
</style>
