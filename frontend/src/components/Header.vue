<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light mb-4">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">&lt;A&gt;Code</router-link>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav me-auto mb-lg-0">
          <li v-for="link in navLinks" :key="link.to" class="nav-item">
            <router-link :to="link.to" class="nav-link" exact-active-class="active">{{ link.name }}</router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link to="/profile" class="nav-link" exact-active-class="active">Profile</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() { return {
    navLinks: [
      {to: '/courses', name: 'Explore'},
      {to: '/classroom', name: 'Classroom'},
    ]
  } }
}
</script>
