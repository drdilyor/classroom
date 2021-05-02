<template>
  <!-- <nav class="navbar navbar-expand-md navbar-light bg-light mb-4">
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
  </nav> -->
  <b-navbar>
    <template #brand>
      <b-navbar-item tag="router-link" to="/" class="navbar-brand ps-2">
        <strong>&lt;A&gt;Code</strong>
      </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item
        v-for="link in navLinks"
        tag="router-link"
        :to="link.to"
        :key="link.to"
        >{{ link.name }}</b-navbar-item>
    </template>
    <template #end>
      <b-navbar-item v-if="!$auth.loggedIn()" class="buttons">
        <button class="button is-primary" @click="$auth.login()">
          <strong>Join</strong>
        </button>
      </b-navbar-item>
      <b-navbar-item v-else tag="router-link" to="/profile">
        Profile
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  data() {
    return {
      navLinks: [
        { to: "/courses", name: "Explore" },
        { to: "/classroom", name: "Classroom" },
      ],
    }
  },
}
</script>

<style>
.navbar {
  margin-bottom: 1em;
}
</style>
