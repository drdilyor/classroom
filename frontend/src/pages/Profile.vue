<template>
  <div class="container content">
    <!-- Kinda hidden dev tools -->
    <h1 @click="showJwt = true">Profile</h1>
    
    <div v-if="$auth.loggedIn()">
      <p v-if="error">Something went wrong when fetching your profile: {{ error }}</p>
      
      <!-- Skeleton -->
      <div v-else-if="profile === null" class="box">
        <div class="columns is-vcentered has-text-centered">
          <div class="column is-narrow">
            <b-skeleton circle width="120px" height="120px" />
          </div>
          <div class="column">
            <b-skeleton size="is-large" width="20em" />
            <b-skeleton class="subtitle" width="14em" />
          </div>
        </div>
      </div>
      
      <!-- Profile -->
      <div v-else class="box">
        <div class="columns is-vcentered has-text-centered">
          <div class="column is-narrow">
            <img class=" is-rounded is-block" :src="profile.picture" width="120" height="120">
          </div>
          <div class="column has-text-left-tablet">
            <h2 class="title">{{ profile.name }}</h2>
            <p class="subtitle mb-0">{{ profile.email }}
              <b-icon v-if="profile.email_verified" class="has-text-success" icon="check" title="This email is verified" />
            </p>
            <p v-if="!profile.email_verified" class="has-text-danger">
              Please verify your email
            </p>
          </div>
        </div>
      </div>
      <pre v-if="showJwt">{{ $auth.getJwt() }}</pre>
      <pre v-if="showJwt">{{ $auth.payload }}</pre>
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
  data() { return {
    profile: null,
    error: null,
    showJwt: false,
  } },
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

    this.$auth.getProfile()
    .then(data => setTimeout(() => this.profile = data, 1000) )
    .catch(err => this.error = err)
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
