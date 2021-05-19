<template>
  <b-navbar class="navbar">
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
        >{{$t(link.name)}}</b-navbar-item>
    </template>
    <template #end>
      <b-navbar-item v-if="!$auth.loggedIn()" class="buttons">
        <button class="button is-primary" @click="$auth.login()">
          <strong>{{$t('join')}}</strong>
        </button>
      </b-navbar-item>
      <b-navbar-item v-else tag="router-link" to="/profile">
        {{$t('profile')}}
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  data() {
    return {
      navLinks: [
        { to: "/courses", name: "explore" },
        { to: "/classroom", name: "classroom" },
      ],
    }
  },
  strings: {
    en: {
      explore: 'Explore',
      classroom: 'Classroom',
      join: 'Join',
    },
  },
}
</script>

<style>
.navbar {
  margin-bottom: 1em;
  transition: all .2s linear;
}
</style>
