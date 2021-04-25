<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light mb-4">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand ps-2">&lt;A&gt;Code</router-link>
      <toggler @click="collapse = !collapse" :on="collapse" class="me-2 d-md-none" />
      <transition name="collapse">
        <div class="navbar-collapse" v-show="collapse" @click="navbarClick">
          <ul class="navbar-nav me-auto mb-lg-0">
            <li v-for="link in navLinks" :key="link.to" class="nav-item">
              <router-link
                :to="link.to"
                class="nav-link"
                exact-active-class="active"
                >{{ link.name }}</router-link>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link
                to="/profile"
                class="nav-link"
                exact-active-class="active"
                >Profile</router-link>
            </li>
          </ul>
        </div>
      </transition>
    </div>
  </nav>
</template>

<script>
import Toggler from "@/components/ui/Toggler.vue";

export default {
  components: {
    Toggler,
  },
  data() {
    return {
      navLinks: [
        { to: "/courses", name: "Explore" },
        { to: "/classroom", name: "Classroom" },
      ],
      collapse: true,
    }
  },
  methods: {
    navbarClick(e) {
      if (e.target.tagName == 'A')
        this.collapse = false
    }
  },
  mounted() {
    // Fix: the navbar is not collapsed on refresh
    this.$nextTick(() => this.collapse = false)
  }
}
</script>

<style>
@media screen and (max-width: 767.9px) {
  .navbar > .container-fluid {
    position: relative;
  }
  .navbar-collapse {
    position: absolute;
    left: 0;
    right: 0;
    bottom: calc(40px * -3);
    top: 100%;
    padding-left: 0.5em;
    background: var(--bs-light);
    overflow: hidden;
    transition: bottom 0.5s;
  }
  .collapse-enter,
  .collapse-leave-active {
    bottom: 0;
  }
}
</style>
