<template>
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
  transition: all .3s;
}
</style>
