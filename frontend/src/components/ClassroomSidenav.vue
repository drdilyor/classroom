<template>
  <div
    class="sidenav"
    :class="{show}" :style="{visibility: show}">
    <slot>
      <router-link class="sidenav-brand" to="/">&lt;A&gt;code</router-link>
      <ul class="flex-grow-1 mb-0">
        <li><icon-link :btn="false" to="/classroom" licon="home">
          Home</icon-link></li>
        <li><icon-link :btn="false" to="/courses" licon="dashboard">
          Catalog</icon-link></li>
      </ul>
      <ul class="mb-0">
        <li><icon-link :btn="false" to="/profile" licon="person">Profile</icon-link></li>
      </ul>
    </slot>
  </div>
</template>

<script>
export default {
  components: {
    IconLink: require('@/components/ui/IconLinkButton.vue').default,
  },
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
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    padding: 1rem 3rem;
  }
  a {
    width: 100%;
    text-decoration: none;
    color: black;
  }
  .sidenav-brand {
    display: block;
    padding: .5rem 0;
    background: var(--bs-light);
    font-size: 1.6rem;
    text-align: center;
  }
}
</style>
