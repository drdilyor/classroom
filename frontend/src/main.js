import Vue from 'vue'
import './pluginbuefy'
const VueMarkdown = () => import(/* webpackChunkName: "vue-markdown" */ 'vue-markdown')
import './assets/styles/styles.scss'

import App from './App.vue'
import router from './routes'
import auth from './auth'
import api from './api'
import store from './store'
import Strings from './strings'

import Loading from '@/components/Loading.vue'

Vue.component('vue-markdown', VueMarkdown)

Vue.config.productionTip = false
Vue.prototype.$backend = 'http://localhost:8000'
Vue.prototype.$auth = auth
Vue.prototype.$api = api
Vue.use(Strings)
Vue.component('Loading', Loading)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
