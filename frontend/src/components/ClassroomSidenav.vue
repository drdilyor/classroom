<template>
  <transition name="slide-left">
    <div class="sidenav" v-show="desktop || show">
      <div class="overlay"/>
      <slot>
        <!-- <classroom-sidenav-default/> -->
        <router-link to="/" class="has-background-light has-text-centered is-size-4 py-3">&lt;A&gt;code</router-link>
        <nav class="sidenav-default-nav p-4">
          <div class="buttons sidenav-default-buttons">
            <b-button tag="router-link" to="/classroom" type="is-primary" size="is-medium" icon-left="home" inverted>{{$t('home')}}</b-button>
            <b-button tag="router-link" to="/courses" type="is-primary" size="is-medium" icon-left="view-dashboard" inverted>{{$t('catalog')}}</b-button>
          </div>
          <span class="flex-1"/>
          <div class="buttons sidenav-default-buttons">
            <b-button tag="router-link" to="/profile" type="is-primary" size="is-medium" icon-left="account" inverted>{{$t('profile')}}</b-button>
          </div>
        </nav>
      </slot>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    show: {
      type: Boolean,
      default: true,
    }
  },
  data() { return {
    desktop: false,
  } },
  strings: {
    en: {
      catalog: 'Catalog',
    },
  },
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

.sidenav-default-nav {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.sidenav-default-buttons {
  display: grid;
  justify-content: stretch;
  > .button {
    justify-content: left;
  }
  > .button:not(:hover) {
    color: #363636;
  }
}
</style>
