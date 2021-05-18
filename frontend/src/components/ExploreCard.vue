<template>
  <router-link :to="'/courses/'+course.id" class="block is-block">
    <article class="explore-card card">
      <div class="explore-card-left">
        <img class="explore-card-img" :src="course.image_link" :alt="$t('imgAlt')">
      </div>
      <div class="explore-card-content">
        <div class="title is-4 mb-2">
          {{ course.title }}
        </div>
        <p class="is-flex-grow-1">
          {{ course.description }}
        </p>
        <div class="explore-card-buttons">
        <b-button class="mt-2" type="is-primary">{{$t('details')}}</b-button>
        </div>
        <div class="has-text-black mt-2 bar-info">
          <span>{{$t('by', [course.author])}}</span>
          <span>{{$t('time', [course.estimated_time])}}</span>
          <span>{{ course.language }}</span>
        </div>
      </div>
    </article>
  </router-link>
</template>

<script>
export default {
  props: {course: Object},
  strings: {
    en: {
      imgAlt: 'Course image',
      details: 'Course details',
      by: 'By {0}',
      time: 'Estimated time {0} weeks',
    },
  },
}
</script>

<style lang="scss">
.explore-card {
  &-left {
    height: 8rem;
  }
  &-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  &-content {
    padding: 2em;
  }
  &-buttons {
    display: flex;
    > .button {
      flex: 1;
    }
  }
}
@media screen and (min-width: 768px) {
  .explore-card {
    display: flex;
    height: 16rem;
    &-left {
      width: 14rem;
      height: 16rem;
      padding: 2em;
      padding-right: 0;
    }
    &-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: stretch;
      padding: 2em;
    }
    &-img {
      height: 100%;
      width: 100%;
      object-fit: cover;
    }
    &-buttons {
      display: block;
    }
  }
}
</style>
