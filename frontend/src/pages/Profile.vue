<template>
  <div class="container">
    <h1>Profile</h1>
    <div v-if="$auth.loggedIn()">
      <p>You are logged in</p>
      <pre style="overflow: auto">{{ $auth.getJwt() }}</pre>
      <p><button @click="logout" class="btn btn-secondary">Log out</button></p>
    </div>
    <div v-else>
      <p>You aren't logged in currently</p>
      <p><button @click="$auth.login" class="btn btn-primary">Login</button></p>
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
