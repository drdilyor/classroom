// default
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// Routes
import Home from './pages/Home.vue'
import NotFound from './pages/404.vue'

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '*',
      name: 'notFound',
      component: NotFound,
    }
  ]
})

