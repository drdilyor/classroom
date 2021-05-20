<template>
  <div class="page-404">
    <div>
      <h1 class="title is-1">{{$t('pageNotFound')}}</h1>
      <p>{{$t('goToBefore')}} <router-link to="/">{{$t('goToLink')}}</router-link> {{$t('goToAfter')}}</p>
    </div>
  </div>
</template>

<script>
export default {
  strings: {
    en: {
      pageNotFound: 'Page not found!',
      goToBefore: 'Go to',
      goToLink: 'main page',
      goToAfter: '',
    },
  }
}
</script>

<style>
  .page-404 {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>