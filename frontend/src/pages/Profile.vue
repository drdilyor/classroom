<template>
  <div class="container content">
    <h1>Profile</h1>
    <div v-if="$auth.loggedIn()">
      <p>You are logged in</p>
      <pre>{{ $auth.getJwt() }}</pre>
      <div class="buttons">
        <b-button type="is-warning" @click="logout">Log out</b-button>
        <b-button type="is-warning is-light" @click="$auth.logoutHard">Log out hard</b-button>
      </div>
    </div>
    <div v-else>
      <p>You aren't logged in currently</p>
      <b-button @click="$auth.login" type="is-primary" outlined>Login</b-button>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    const match = this.$route.hash.match(/^#access_token=(.*?)&/)

    if (match) {
      const token = match[1]
      if (token) {
        const oldJwt = this.$auth.getJwt()
        this.$auth.setJwt(token)
        if (oldJwt !== token)
          this.$router.go() // reload so navbar updates
        // fix me: the above line won't be required inthe future
        // when auth migrates to use vuex
      }
    }
  },
  methods: {
    logout() {
      this.$auth.logout()
      this.$router.push('/')
      this.$router.go()
    }
  }
}
</script>
