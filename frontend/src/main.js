import Vue from 'vue'
import Buefy from 'buefy';
import 'buefy/dist/buefy.css'
import VueMarkdown from 'vue-markdown';
import './assets/styles/styles.scss'

import App from './App.vue'
import router from './routes'
import auth from './auth'
import api from './api'
import store from './store'

import Loading from '@/components/Loading.vue'

Vue.use(Buefy)
Vue.component('vue-markdown', VueMarkdown)

Vue.config.productionTip = false
Vue.prototype.$backend = 'http://localhost:8000'
Vue.prototype.$auth = auth
Vue.prototype.$api = api
Vue.component('Loading', Loading)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
