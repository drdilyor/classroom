<template>
  <div class="container">
    <h1>Welcome to &lt;A&gt;Code</h1>
    <p>An open source E-Learning platform!</p>
    <p>
      <LinkButton to="/courses" class="btn-secondary" ricon="arrow_forward">Explore Courses</LinkButton>
    </p>
  </div>
</template>

<script>
export default {
  components: {
    LinkButton: require('@/components/ui/IconLinkButton.vue').default,
  }
}
</script>
