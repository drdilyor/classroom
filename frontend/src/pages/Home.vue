<template>
  <div style="margin: -1em -1em 0"> <!-- Remove navbar margin -->
    <section class="hero is-primary is-halfheight">
      <div class="hero-body has-text-centered">
        <div class="container">
          <h1 class="title">Welcome to &lt;A&gt;Code</h1>
          <p class="subtitle">An open source E-Learning platform!</p>
          <p class="buttons is-centered">
            <b-button
              tag="router-link"
              to="/courses"
              type="is-primary"
              size="is-large"
              inverted
              icon-left="view-dashboard">
              Explore courses
            </b-button>
            <b-button
              type="is-primary"
              size="is-large"
              outlined inverted
              @click="$auth.loggedIn()?$router.push('/classroom'):$auth.login()"
              icon-left="account-box">
              {{ $auth.loggedIn() ? 'My classroom' : 'Register for free' }}
            </b-button>
          </p>
        </div>
      </div>
    </section>
    <section class="container section">
      <div class="columns">
        <div class="column">
          <div class="promo">
            <b-icon class="has-text-primary" icon="flash" size="is-large" />
            <h3 class="subtitle is-3">Gain new skills quickly</h3>
            <p class="is-size-5">We did our best to make sure our student will learn content as quickly as possible</p>
          </div>
        </div>
        <div class="column">
          <div class="promo">
            <b-icon class="has-text-primary" icon="arrow-up-bold-circle" size="is-large" />
            <h3 class="subtitle is-3">Learn up-to-date technologies</h3>
            <p class="is-size-5">Unlike some other similar web sites, we offer fresh content only</p>
          </div>
        </div>
        <div class="column">
          <div class="promo">
            <b-icon class="has-text-primary" icon="web" size="is-large" />
            <h3 class="subtitle is-3">For uzbeks, by uzbeks</h3>
            <p class="is-size-5">We are one of the very few learning platforms which have both uzbek content and quality</p>
          </div>
        </div>
      </div>
    </section>
    <section class="section has-background-info has-text-white">
      <div class="container">
        <div class="columns has-text-centered">
          <div class="column">
            <span class="is-size-3">2</span>
            <span class="heading">Courses</span>
          </div>
          <div class="column">
            <span class="is-size-3">10+</span>
            <span class="heading">Registered users</span>
          </div>
          <div class="column">
            <span class="is-size-3">3</span>
            <span class="heading">Completed courses</span>
          </div>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="columns is-align-items-center">
          <div class="column has-text-centered-mobile">
            <h2 class="title is-4">Sign up now</h2>
            <p>Sign up today and build skills for tomorrow</p>
          </div>
          <div class="column">
            <b-button size="is-medium" expanded @click="$auth.login()">Open register page</b-button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>


<script>
export default {
  data() { return {
  } },
}
</script>

<style>
.promo {
  text-align: center;
}
.promo > .icon {
  display: block;
  margin: 0 auto 1rem;
}
</style>
