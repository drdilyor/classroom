// default
import Vue from 'vue'
import Router from 'vue-router'

import { registerRouter } from "./auth";

Vue.use(Router)

// Routes
import Home from './pages/Home.vue'
import CourseExplore from './pages/CourseExplore.vue'
import CourseDetail from './pages/CourseDetail.vue'
import Profile from './pages/Profile.vue'
import NotFound from './pages/404.vue'

export default registerRouter(new Router({
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
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/login-required',
      name: 'loginrequired',
      component: Home,
      meta: {requiresAuth: true}
    },
    {
      path: '*',
      name: 'notFound',
      component: NotFound,
    }
  ]
}))
