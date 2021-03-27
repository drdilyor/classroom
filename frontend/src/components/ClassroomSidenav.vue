<template>
  <div class="nav-groups">
    <ul>
      <li>
        <router-link class="brand-logo" to="/" target="_blank">
          <img src="/assets/img/logo.png" alt="&lt;A&gt;Code">
        </router-link>
      </li>
      <li>
        <router-link to="/classroom">
          <i class="material-icons">home</i>
          Home
        </router-link>
      </li>
      <li>
        <router-link to="/courses">
          <i class="material-icons">dashboard</i>
          Catalog
        </router-link>
      </li>
    </ul>
    <ul>
      <li>
        <router-link to="/classroom/settings">
          <i class="material-icons">settings</i>
          Settings
        </router-link>
      </li>
      <li>
        <a href="javascript:void(0)" @click="logout">
          <i class="material-icons">arrow_backward</i>
          Log out
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$auth.logout()
      window.location = '/'
    }
  }
}
</script>

<style scoped>
.nav-groups {
  min-height: 100%;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.nav-groups > ul:first-child {
  flex: 1;
}
.nav-groups > ul {
  margin-top: 0;
  margin-bottom: 0;
}

.brand-logo {
  font-size: 1.6em;
}
a {
  display: flex;
}
a span:last-child {
  flex: 1;
}
</style>
