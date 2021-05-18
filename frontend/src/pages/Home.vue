<template>
  <div style="margin: -1em -1em 0"> <!-- Remove navbar margin -->
    <section class="hero is-primary is-halfheight">
      <div class="hero-body has-text-centered">
        <div class="container">
          <h1 class="title">{{$t('welcome')}}</h1>
          <p class="subtitle">{{$t('welcomeSubtitle')}}</p>
          <p class="buttons is-centered">
            <b-button
              tag="router-link"
              to="/courses"
              type="is-primary"
              size="is-large"
              inverted
              icon-left="view-dashboard">
              {{$t('btnExplore')}}
            </b-button>
            <b-button
              type="is-primary"
              size="is-large"
              outlined inverted
              @click="$auth.loggedIn()?$router.push('/classroom'):$auth.login()"
              icon-left="account-box">
              {{$t($auth.loggedIn() ? 'btnClassroom' : 'btnRegister')}}
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
            <h3 class="subtitle is-3">{{$t('promoSkills')}}</h3>
            <p class="is-size-5">{{$t('promoSkillsText')}}</p>
          </div>
        </div>
        <div class="column">
          <div class="promo">
            <b-icon class="has-text-primary" icon="arrow-up-bold-circle" size="is-large" />
            <h3 class="subtitle is-3">{{$t('promoUptodate')}}</h3>
            <p class="is-size-5">{{$t('promoUptodateText')}}</p>
          </div>
        </div>
        <div class="column">
          <div class="promo">
            <b-icon class="has-text-primary" icon="web" size="is-large" />
            <h3 class="subtitle is-3">{{$t('promoUzbeks')}}</h3>
            <p class="is-size-5">{{$t('promoUzbeksText')}}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="section has-background-info has-text-white">
      <div class="container">
        <div class="columns has-text-centered">
          <div class="column">
            <span class="is-size-3">2</span>
            <span class="heading">{{$t('dashboardCourses')}}</span>
          </div>
          <div class="column">
            <span class="is-size-3">10+</span>
            <span class="heading">{{$t('dashboardUsers')}}</span>
          </div>
          <div class="column">
            <span class="is-size-3">3</span>
            <span class="heading">{{$t('dashboardCompleted')}}</span>
          </div>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="columns is-align-items-center">
          <div class="column has-text-centered-mobile">
            <h2 class="title is-4">{{$t('regTitle')}}</h2>
            <p>{{$t('regText')}}</p>
          </div>
          <div class="column">
            <b-button size="is-medium" expanded @click="$auth.login()">{{$t('regBtn')}}</b-button>
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
  strings: {
    en: {
      welcome: 'Welcome to <A>Code',
      welcomeSubtitle: 'An open source E-Learning platform!',
      btnExplore: 'Explore courses',
      btnClassroom: 'My classroom',
      btnRegister: 'Register for free',
      promoSkills: 'Gain new skills quickly',
      promoSkillsText: 'We did our best to make sure our student will learn content as quickly as possible',
      promoUptodate: 'Learn up-to-date technologies',
      promoUptodateText: 'Unlike some other similar web sites, we offer fresh content only',
      promoUzbeks: 'For uzbeks, by uzbeks',
      promoUzbeksText: 'We are one of the very few learning platforms which have both uzbek content and quality',
      dashboardCourses: 'Courses',
      dashboardUsers: 'Registered users',
      dashboardCompleted: 'Completed courses',
      regTitle: 'Sign up now',
      regText: 'Sign up today and build skills for tomorrow',
      regBtn: 'Open register page',
    },
  }
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
