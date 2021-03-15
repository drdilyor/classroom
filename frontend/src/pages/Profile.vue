<template>
  <div class="container">
    <h1>Profile</h1>
    <div v-if="$auth.loggedIn()">
      <p>You are logged in</p>
      <pre style="overflow: auto">{{ $auth.getJwt() }}</pre>
      <p><button @click="$auth.logout(), $forceUpdate()" class="btn waves-effect waves-light">Log out</button></p>
    </div>
    <div v-else>
      <p>You aren't logged in currently</p>
      <p><button @click="$auth.login" class="btn waves-effect waves-light">Login</button></p>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    console.log(this.$route.hash);
    const match = this.$route.hash.match(/^#access_token=(.*?)&/)

    if (match) {
      const token = match[1]
      if (token)
        this.$auth.setJwt(token)
    }
    
  }
}
</script>
