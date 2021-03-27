<template>
  <div class="nav-groups" :class="{small}">
    <ul>
      <li>
        <router-link class="brand-logo" to="/" target="_blank">
          <img v-if="small" src="/assets/img/logo-small.png" alt="&lt;A&gt;">
          <img v-else src="/assets/img/logo.png" alt="&lt;A&gt;Code">
        </router-link>
      </li>
      <li>
        <router-link to="/classroom">
          <i class="material-icons">home</i>
          <span>Home</span>
        </router-link>
      </li>
      <li>
        <router-link to="/courses">
          <i class="material-icons">dashboard</i>
          <span>Catalog</span>
        </router-link>
      </li>
    </ul>
    <ul>
      <li>
        <router-link to="/classroom/settings">
          <i class="material-icons">settings</i>
          <span>Settings</span>
        </router-link>
      </li>
      <li>
        <a href="javascript:void(0)" @click="logout">
          <i class="material-icons">arrow_backward</i>
          <span>Log out</span>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    small: {
      type: Boolean,
      default: false,
    }
  },
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

.small {
  width: 48px;
}

.small .brand-logo {
  font-size: 1.3em;
}

.small li,
.small a {
  width: 48px !important;
  height: 48px !important;
}
.small a {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0;
  padding-top: 8px;
}
.small a > * {
  float: none !important;
}
.small .material-icons {
  height: 24px;
  margin: 0 !important;
  float: none !important;
  line-height: 24px;
}
.small a span {
  height: 16px;
  font-size: 10px;
  line-height: 16px;
  text-transform: uppercase;
}

</style>
