// default
import Vue from 'vue'
import Router from 'vue-router'

import { registerRouter } from "./auth";

Vue.use(Router)

// Routes
import Index from './pages/Index.vue'
import Home from './pages/Home.vue'
import CourseExplore from './pages/CourseExplore.vue'
import CourseDetail from './pages/CourseDetail.vue'
import Profile from './pages/Profile.vue'
import ClassroomHome from './pages/ClassroomHome.vue'
import ClassroomCourse from './pages/ClassroomCourse.vue'
import LearnLesson from './pages/LearnLesson'
import NotFound from './pages/404.vue'

export default registerRouter(new Router({
  mode: 'history',
  routes: [
    { path: '/', component: Index,
      children: [
      {
        path: '',
        name: 'home',
        component: Home,
      },
      {
        path: 'courses',
        name: 'courses',
        component: CourseExplore,
      },
      {
        path: 'courses/:id',
        name: 'courseDetail',
        component: CourseDetail,
      },
      {
        path: 'profile',
        name: 'profile',
        component: Profile,
      },
    ]},
    {
      path: '/classroom',
      name: 'classroom',
      component: ClassroomHome,
      meta: {requiresAuth: true}
    },
    {
      path: '/classroom/course/:id',
      name: 'learnCourse',
      component: ClassroomCourse,
      meta: {requiresAuth: true}
    },
    {
      path: '/classroom/lesson/:id',
      name: 'learnLesson',
      component: LearnLesson,
      meta: {requiresAuth: true}
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
