// default
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// Routes
import Home from './pages/Home.vue'
import CourseExplore from './pages/CourseExplore.vue'
import CourseDetail from './pages/CourseDetail.vue'
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
      path: '/courses',
      name: 'courses',
      component: CourseExplore,
    },
    {
      path: '/courses/:id',
      name: 'courseDetail',
      component: CourseDetail,
    },
    {
      path: '*',
      name: 'notFound',
      component: NotFound,
    }
  ]
})

